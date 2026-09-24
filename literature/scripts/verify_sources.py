#!/usr/bin/env python3
"""Fetch individual original paper pages; preserve evidence and extract only source metadata."""
import argparse
import concurrent.futures
import datetime
import gzip
import hashlib
import json
import re
import threading
import time
import unicodedata
from pathlib import Path
from urllib.parse import urlparse, parse_qs

import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
LOCK = threading.Lock()
NEXT_REQUEST = 0.0


def canonical(url):
    url = str(url).strip().rstrip('.,;')
    m = re.search(r'(?:arxiv\.org/(?:abs|pdf|html)/|arxiv:|arXiv:)(\d{4}\.\d{4,5})(?:v\d+)?', url)
    if m:
        return 'https://arxiv.org/abs/' + m.group(1)
    if 'aclanthology.org/' in url:
        return url.replace('http://', 'https://').removesuffix('.pdf').rstrip('/') + '/' if hasattr(str, 'removesuffix') else re.sub(r'\.pdf$', '', url.replace('http://', 'https://')).rstrip('/') + '/'
    if 'openreview.net/pdf?' in url:
        return url.replace('/pdf?', '/forum?')
    return url.replace('http://arxiv.org/', 'https://arxiv.org/').split('#')[0]


def title_key(title):
    t = unicodedata.normalize('NFKD', title).casefold()
    return ''.join(c for c in t if c.isalnum())


def load_candidates():
    records = {}
    for path in sorted(ROOT.glob('candidates_*.jsonl')):
        for line in path.read_text().splitlines():
            if not line.strip():
                continue
            r = json.loads(line)
            url = canonical(r['url'])
            item = records.setdefault(url, {'url': url, 'discoveries': []})
            entry = dict(r)
            entry['candidate_file'] = path.name
            if entry not in item['discoveries']:
                item['discoveries'].append(entry)
    return records


def extract(html, url):
    soup = BeautifulSoup(html, 'html.parser')
    meta = {}
    for m in soup.select('meta'):
        name = m.get('name', m.get('property', '')).lower()
        if name and m.get('content'):
            meta.setdefault(name, []).append(m['content'].strip())
    def first(*names):
        for name in names:
            if meta.get(name):
                return meta[name][0]
        return ''
    title = first('citation_title', 'dc.title', 'dcterms.title')
    authors = meta.get('citation_author', meta.get('dc.creator', []))
    date = first('citation_date', 'citation_publication_date', 'dc.date', 'dc.date.issued', 'dcterms.issued')
    venue = first('citation_journal_title', 'citation_conference_title')
    abstract = first('citation_abstract', 'dc.description')
    # Prefer the visible abstract: some source pages incorrectly put revision comments in citation_abstract.
    el = soup.select_one('blockquote.abstract, .acl-abstract, .paper-abstract, #abstract, .abstract, .note-content-value[data-field="abstract"]')
    if el:
        abstract = re.sub(r'^Abstract\s*:?\s*', '', el.get_text(' ', strip=True))
    # arXiv canonical page explicitly identifies a preprint; do not infer a conference from a README.
    arxiv_id = first('citation_arxiv_id')
    if not arxiv_id:
        m = re.search(r'arxiv\.org/abs/(\d{4}\.\d{4,5})', url)
        if m:
            arxiv_id = m.group(1)
    if arxiv_id and not venue:
        venue = 'arXiv (preprint repository; acceptance not inferred)'
    year_match = re.search(r'\b(?:19|20)\d{2}\b', date)
    year = int(year_match.group(0)) if year_match else None
    if not year and arxiv_id:
        year = 2000 + int(arxiv_id[:2])
    doi = first('citation_doi', 'dc.identifier.doi')
    journal_ref = soup.select_one('.jref')
    journal_ref = journal_ref.get_text(' ', strip=True) if journal_ref else ''
    return {'title': title, 'authors': authors, 'first_author': authors[0] if authors else '',
            'year': year, 'source_date': date, 'venue_from_source': venue,
            'journal_reference_from_source': journal_ref, 'doi': doi, 'arxiv_id': arxiv_id,
            'abstract': abstract, 'source_metadata': meta}


def fetch(record, interval):
    global NEXT_REQUEST
    url = record['url']
    key = hashlib.sha256(url.encode()).hexdigest()[:20]
    output = ROOT / 'evidence' / (key + '.json')
    if output.exists():
        old = json.loads(output.read_text())
        if old.get('verification_status') == 'verified_metadata':
            old['discoveries'] = record['discoveries']
            output.write_text(json.dumps(old, ensure_ascii=False, indent=2))
            return old
    result = dict(record)
    result.update({'verification_status': 'unverified', 'requested_url': url,
                   'fetch_method': 'individual HTTP GET of original source page via requests; HTML metadata extracted',
                   'opened_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat()})
    for attempt in range(2):
        try:
            with LOCK:
                wait = max(0, NEXT_REQUEST - time.monotonic())
                NEXT_REQUEST = max(NEXT_REQUEST, time.monotonic()) + interval
            if wait:
                time.sleep(wait)
            r = requests.get(url, timeout=(12, 35), headers={'User-Agent': 'Mozilla/5.0 (academic bibliography source verification)'})
            result.update({'http_status': r.status_code, 'opened_url': r.url,
                           'content_type': r.headers.get('Content-Type', ''), 'response_bytes': len(r.content)})
            if r.status_code in (429, 503):
                time.sleep(4 + attempt * 4)
                continue
            r.raise_for_status()
            if 'pdf' in r.headers.get('Content-Type', '').lower() or r.content.startswith(b'%PDF'):
                result['error'] = 'PDF source opened; metadata requires manual extraction; not automatically counted.'
                break
            metadata = extract(r.text, r.url)
            result.update(metadata)
            result['html_sha256'] = hashlib.sha256(r.content).hexdigest()
            html_path = ROOT / 'evidence' / (key + '.html.gz')
            with gzip.open(str(html_path), 'wb') as f:
                f.write(r.content)
            result['evidence_html'] = str(html_path.relative_to(ROOT))
            if metadata['title'] and metadata['authors'] and metadata['year']:
                result['verification_status'] = 'verified_metadata'
                result['evidence_scope'] = 'Original landing page bibliographic metadata and abstract; not full-text verification of scientific claims.'
            else:
                result['error'] = 'Opened page lacks complete machine-readable title/authors/year; manual review required.'
            break
        except Exception as e:
            result['error'] = type(e).__name__ + ': ' + str(e)[:350]
            if attempt == 0:
                time.sleep(1)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2))
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--workers', type=int, default=4)
    parser.add_argument('--interval', type=float, default=0.65)
    parser.add_argument('--limit', type=int, default=0)
    args = parser.parse_args()
    (ROOT / 'evidence').mkdir(exist_ok=True)
    records = list(load_candidates().values())
    if args.limit:
        records = records[:args.limit]
    print('CANDIDATES', len(records), flush=True)
    done = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(fetch, r, args.interval) for r in records]
        for f in concurrent.futures.as_completed(futures):
            r = f.result()
            done.append(r)
            if len(done) % 25 == 0 or len(done) == len(records):
                count = sum(x['verification_status'] == 'verified_metadata' for x in done)
                print('PROGRESS', len(done), '/', len(records), 'VERIFIED', count, flush=True)
    path = ROOT / 'verified_all.jsonl'
    path.write_text('\n'.join(json.dumps(r, ensure_ascii=False) for r in sorted(done, key=lambda r:r['url'])) + '\n')
    print('SAVED', str(path), flush=True)


if __name__ == '__main__':
    main()
