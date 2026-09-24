#!/usr/bin/env python3
"""Build a separate bibliography from individually opened source pages."""
import collections
import csv
import datetime
import hashlib
import json
import re
from pathlib import Path

from verify_sources import ROOT, canonical, title_key, load_candidates

CUTOFF = '2026-09-24'
TARGET = 500


def classify(r):
    title = r['title'].lower()
    ds = r['discoveries']
    topics = ' | '.join(d.get('topic', '') for d in ds).lower()
    files = ' '.join(d.get('candidate_file', '') for d in ds)
    # This is a provisional bibliographic organization, not a full-text coding of environment factors.
    if 'harness' in title:
        return 'Harness', '框架与运行编排'
    if 'environment_variation' in files:
        return 'Environment', '环境变化与鲁棒性'
    if re.search(r'environment (synthesis|generation|design|engineering|evolution)|environments? for.*training|world models?|neural simulators?', title):
        return 'Environment', '世界模型与模拟器' if re.search(r'world model|neural simulator', title) else '环境生成与演化'
    if re.search(r'benchmark|\bbench\b|bench:|arena:|\bgym\b|environments? hub', title) and not re.search(r'memory|tool use|tool-use|function call|harness|prompt injection|security', title):
        return 'Environment', '交互环境与评测基准'
    if 'foundations' in files or ('existing' in files and re.search('软件工程|机器学习|泛化|非平稳', topics)):
        return 'Environment', '理论基础、配置与可复现性'
    if 'candidates_harness' in files:
        for needle, label in [('security_permissions','安全、权限与执行验证'), ('memory_and_context','记忆与上下文'),
                              ('tool_use_and_interfaces','工具调用与接口'), ('planning_search','规划、搜索与反思'),
                              ('agent_training','训练与反馈基础设施'), ('multi_agent_coordination','多代理协作编排'),
                              ('harness_foundations','框架与综述'), ('harness_runtime','框架与运行编排')]:
            if needle in topics:
                return 'Harness', label
    if 'candidates_agent' in files:
        if re.search(r'software|coding|code agent|swe-|developer|programming|软件|代码', title + ' ' + topics):
            return 'Agent', '软件工程与代码智能体'
        if re.search(r'gui|web|computer|mobile|desktop|browser|android|网页|桌面|移动', title + ' ' + topics):
            return 'Agent', '网页、桌面与移动智能体'
        if re.search(r'scien|research|discover|lab|科学|研究', title + ' ' + topics):
            return 'Agent', '科学与研究智能体'
        if re.search(r'embodi|robot|具身', title + ' ' + topics):
            return 'Agent', '具身智能体'
        return 'Agent', '通用与多代理方法'
    if re.search(r'world model|neural simulator', topics):
        return 'Environment', '世界模型与模拟器'
    if re.search(r'synthesis|generation|curriculum|evolution|open-ended', topics):
        return 'Environment', '环境生成与演化'
    if re.search(r'embodied|game|simulation|机器人', topics):
        return 'Environment', '具身、游戏与模拟环境'
    if re.search(r'contextual|variation', topics):
        return 'Environment', '环境变化与鲁棒性'
    return 'Environment', '交互环境与评测基准'


def score(r):
    t = r['title'].lower()
    ds = r['discoveries']
    s = 0
    core_patterns = [r'^react:', r'^toolformer:', r'^memgpt:', r'^do as i can', r'^sayplan:', r'^roco:',
                     r'^firecracker:', r'^openai gym$', r'^alfworld:', r'^alfred:', r'^habitat:',
                     r'^babyai:', r'^textworld:', r'^scienceworld:', r'^webshop:', r'^minedojo:',
                     r'^voyager:', r'^autogen:', r'^metagpt:', r'^camel:', r'^reflexion:',
                     r'^generative agents:', r'^swe-agent:', r'^openhands:', r'^webvoyager:',
                     r'^webgpt:', r'^mind2web:', r'^contextualize me', r'^contextual markov',
                     r'^agentic environment engineering', r'^harness-bench:', r'^openapps:',
                     r'^b-moca:', r'^worldgui:', r'^cli-gym:', r'^endless terminals:']
    if any(re.search(pattern, t) for pattern in core_patterns):
        s += 500
    if any(d.get('existing_reference_number') for d in ds):
        s += 90
    if 'harness' in t:
        s += 75
    if re.search(r'environment.*(?:variation|design|synthesis|generation|engineering)|contextual|cross.environment|cross.platform|reproducib', t):
        s += 55
    if re.search(r'survey|review|benchmark|agent|tool|memory|planning|reflection', t):
        s += 20
    s += min(len(ds), 4) * 7
    s += min(max(r.get('year', 2020) - 2020, 0), 6)
    return s


def dump_csv(path, records, fields):
    with path.open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        w.writeheader()
        for r in records:
            row = {k: r.get(k, '') for k in fields}
            for k,v in row.items():
                if isinstance(v, list):
                    row[k] = ' | '.join(str(x) for x in v)
            w.writerow(row)


def tex(s):
    parts = str(s).split('$')
    for i in range(0,len(parts),2):
        parts[i] = parts[i].replace('\\', '\\textbackslash{}').replace('{', '\\{').replace('}', '\\}').replace('&','\\&').replace('%','\\%').replace('#','\\#').replace('_','\\_')
    return '$'.join(parts)


def main():
    candidates = load_candidates()
    review_notes = {}
    harness_review = ROOT / 'quality_harness.json'
    if harness_review.exists():
        for row in json.loads(harness_review.read_text()).get('records', []):
            review_notes[canonical(row['url'])] = {'review_decision':row['decision'], 'review_note':row['reason'], 'review_level':'AI-assisted title and abstract review; not full text'}
    agent_review = ROOT / 'quality_agent.json'
    if agent_review.exists():
        audit = json.loads(agent_review.read_text())
        for row in audit.get('per_candidate_checks', []):
            review_notes.setdefault(canonical(row['url']), {'review_decision':row.get('recommendation','retain'), 'review_note':'代理方法、应用或执行框架相关；仅作题名与摘要级初筛。', 'review_level':'AI-assisted title and abstract review; not full text'})
        for row in audit.get('lower_priority_background', []):
            review_notes[canonical(row['url'])] = {'review_decision':'keep_background_only', 'review_note':row['reason'], 'review_level':'AI-assisted title and abstract review; not full text'}
    exclusions = {}
    ex_path = ROOT / 'manual_exclusions.json'
    if ex_path.exists():
        exclusions = json.loads(ex_path.read_text())
    records, pending = [], []
    for url, candidate in candidates.items():
        key = hashlib.sha256(url.encode()).hexdigest()[:20]
        path = ROOT / 'evidence' / (key + '.json')
        if not path.exists():
            pending.append({'url': url, 'status': 'unverified', 'reason': '尚未抓取原始页面'})
            continue
        r = json.loads(path.read_text())
        r['discoveries'] = candidate['discoveries']
        if r.get('verification_status') != 'verified_metadata':
            pending.append({'url':url, 'status':'unverified', 'reason':r.get('error', '未核验'), 'title_hint':candidate['discoveries'][0].get('title_hint','')})
            continue
        if url in exclusions:
            pending.append({'url':url,'status':'excluded_after_review','title_hint':r['title'],'reason':exclusions[url]})
            continue
        date = r.get('source_date','').replace('/','-')[:10]
        if re.match(r'\d{4}-\d{2}-\d{2}$', date) and date > CUTOFF:
            pending.append({'url':url,'status':'excluded_after_cutoff','title_hint':r['title'],'reason':'原页首发日期晚于检索截止日：'+date})
            continue
        r['evidence_json'] = str(path.relative_to(ROOT))
        r.update(review_notes.get(url, {'review_decision':'bibliographic_screening', 'review_note':'按发现源主题与题名归类；具体环境因素及结论待全文编码。', 'review_level':'Source metadata verification and topic screening'}))
        records.append(r)
    dedup, duplicate_log = {}, []
    for r in sorted(records, key=lambda x:(0 if x.get('arxiv_id') else 1,x['url'])):
        key = title_key(r['title'])
        if key in dedup:
            kept = dedup[key]
            kept.setdefault('alternate_verified_urls',[]).append(r['opened_url'])
            kept['discoveries'].extend(d for d in r['discoveries'] if d not in kept['discoveries'])
            duplicate_log.append({'kept_url':kept['url'],'duplicate_url':r['url'],'title':r['title'],'reason':'规范化标题相同；同一作品不重复计数'})
        else:
            dedup[key] = r
    records = list(dedup.values())
    for r in records:
        r['primary_area'],r['subcategory'] = classify(r)
        r['selection_score'] = score(r)
        if r.get('review_decision') == 'keep_background_only':
            r['selection_score'] -= 12
        r['discovery_topics'] = sorted(set(d.get('topic','') for d in r['discoveries']))
    grouped = collections.defaultdict(list)
    for r in records:
        grouped[r['primary_area']].append(r)
    # Balanced starting allocations; any unused slots transfer to other relevant eligible papers.
    budgets = {'Environment':200, 'Harness':170, 'Agent':130}
    selected = []
    for group in budgets:
        items = sorted(grouped[group], key=lambda r:(-r['selection_score'], -r['year'], r['title']))
        subgroups = collections.defaultdict(list)
        for item in items:
            subgroups[item['subcategory']].append(item)
        # Preserve breadth inside each major direction, then fill with the most directly relevant works.
        base = [r for sub in subgroups.values() for r in sub[:min(8,len(sub))]]
        base_urls = {r['url'] for r in base}
        rest = [r for r in items if r['url'] not in base_urls]
        selected.extend((base + rest)[:budgets[group]])
    chosen = {r['url'] for r in selected}
    reserve = sorted((r for r in records if r['url'] not in chosen), key=lambda r:(-r['selection_score'], -r['year'], r['title']))
    need = TARGET-len(selected)
    if need > 0:
        selected.extend(reserve[:need])
        reserve=reserve[need:]
    selected.sort(key=lambda r:({'Environment':0,'Harness':1,'Agent':2}[r['primary_area']],r['subcategory'],-r['year'],r['title']))
    public = []
    bib = []
    md = ['# Environment / Harness / Agent 分类文献库', '',
          '检索截止：'+CUTOFF+'。下列条目已逐篇打开原始来源页面，核对题名、作者与年份；属于书目及摘要级初筛，尚不代表全文证据已逐篇审查。',
          '论文与预印本计入主库；官方产品文档、博客、代码仓库和未打开来源不计入。分类为综述组织用途，允许跨主题标签。', '']
    current = None
    for i,r in enumerate(selected,1):
        identifier='P%04d'%i
        r['id']=identifier
        group=(r['primary_area'],r['subcategory'])
        if group!=current:
            md.extend(['## '+group[0]+' · '+group[1],''])
            current=group
        author=r['first_author']+(' et al.' if len(r['authors'])>1 else '')
        venue=r['venue_from_source'] or '原始页面未声明会场'
        display_venue='arXiv 预印本' if venue.startswith('arXiv (') else venue
        md.extend([identifier+'. **'+r['title'].replace('\n',' ')+'**',
                   '   '+author+'；'+str(r['year'])+'；'+display_venue+'。',
                   '   已打开原页：'+r['opened_url'],
                   '   核验记录：['+identifier+' evidence]('+r['evidence_json']+')；全文环境因素编码：待完成。',''])
        item={k:r.get(k,'') for k in ['id','title','authors','first_author','year','source_date','primary_area','subcategory','discovery_topics','arxiv_id','doi','venue_from_source','journal_reference_from_source','opened_url','opened_at_utc','http_status','verification_status','evidence_scope','fetch_method','evidence_json','evidence_html','html_sha256','review_decision','review_note','review_level','metadata_correction_note']}
        item['full_text_review']='未完成全文逐篇核验；不据书目初筛推断环境因素或实验结论'
        item['discovery_urls']=sorted(set(d.get('discovery_url','') for d in r['discoveries']))
        public.append(item)
        key='agentenv_'+(r.get('arxiv_id','').replace('.','') or hashlib.sha256(r['url'].encode()).hexdigest()[:12])
        lines=['@misc{'+key+',','  title = {{'+tex(r['title'])+'}},','  author = {'+' and '.join(tex(a) for a in r['authors'])+'},','  year = {'+str(r['year'])+'},','  url = {'+r['opened_url']+'},','  urldate = {'+CUTOFF+'},']
        if r.get('arxiv_id'):
            lines.extend(['  eprint = {'+r['arxiv_id']+'},','  archivePrefix = {arXiv},'])
        if r.get('doi'):
            lines.append('  doi = {'+r['doi']+'},')
        lines.append('  note = {Original source page metadata verified; '+tex(r['primary_area']+' / '+r['subcategory'])+'}\n}')
        bib.append('\n'.join(lines))
    (ROOT/'500篇分类文献.md').write_text('\n'.join(md))
    (ROOT/'论文库.jsonl').write_text('\n'.join(json.dumps(r,ensure_ascii=False) for r in public)+'\n')
    fields=['id','title','first_author','authors','year','primary_area','subcategory','discovery_topics','venue_from_source','journal_reference_from_source','arxiv_id','doi','opened_url','verification_status','review_decision','review_note','review_level','full_text_review','opened_at_utc','evidence_json','discovery_urls','metadata_correction_note']
    dump_csv(ROOT/'论文库.csv',public,fields)
    (ROOT/'论文库.bib').write_text('\n\n'.join(bib)+'\n')
    dump_csv(ROOT/'已核验备用文献.csv',reserve,['title','first_author','year','primary_area','subcategory','opened_url','evidence_json'])
    dump_csv(ROOT/'待核验与排除.csv',pending,['url','status','title_hint','reason'])
    dump_csv(ROOT/'重复文献合并记录.csv',duplicate_log,['kept_url','duplicate_url','title','reason'])
    counts=collections.Counter(r['primary_area'] for r in selected)
    subcounts=collections.Counter((r['primary_area'],r['subcategory']) for r in selected)
    stats={'target':TARGET,'selected_verified_papers':len(selected),'unique_candidate_urls':len(candidates),
           'eligible_verified_unique_works':len(records),'verified_reserve':len(reserve),'pending_or_excluded':len(pending),
           'duplicate_records_merged':len(duplicate_log),'primary_areas':dict(counts),
           'subcategories':{' / '.join(k):v for k,v in subcounts.items()},
           'year_counts':dict(sorted(collections.Counter(r['year'] for r in selected).items())),
           'cutoff':CUTOFF,'verification_level':'Bibliographic metadata and abstract landing page only; full-text extraction not completed.'}
    (ROOT/'统计.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2))
    summary=['# 独立文献库：Environment / Harness / Agent','',
             '截至 '+CUTOFF+'，主库收录 **'+str(len(selected))+' 篇**去重论文/预印本。已逐篇打开原始论文页面，提取题名、作者和年份，并保存网址、时间及页面证据。','',
             '- [分类文献清单](500篇分类文献.md)', '- [CSV：筛选、排序与导入表格](论文库.csv)',
             '- [BibTeX：论文写作引用](论文库.bib)', '- [JSONL：完整结构化条目](论文库.jsonl)',
             '- [已核验备用文献](已核验备用文献.csv)', '- [待核验与排除记录](待核验与排除.csv)',
             '- [重复文献合并记录](重复文献合并记录.csv)', '- [机器可读统计](统计.json)','',
             '| 主方向 | 主库篇数 |','|---|---:|']
    summary += ['| '+k+' | '+str(v)+' |' for k,v in counts.items()]
    summary += ['', '候选原始网址 '+str(len(candidates))+' 个；可纳入的已核验去重作品 '+str(len(records))+' 篇；主库外已核验备用 '+str(len(reserve))+' 篇；待核验或排除 '+str(len(pending))+' 条。','',
                '核验范围：已打开论文原始落地页并核对书目元数据；主题来自发现源分区及题名/摘要初筛。没有把打开摘要页写成阅读全文，也没有声称完成500篇的环境因素编码。具体 OS、隔离、网络、权限、镜像、GPU、locale 和解法变化结论仍需后续全文提取。','',
                'arXiv条目按来源首发年份和预印本形式记录；不从第三方目录推断录用会场。原页给出的 journal reference 另存 CSV。正式发表版与预印本原则上只计一次；本轮按 arXiv ID、原页 URL 和规范化题名去重，改题发表版仍可能需要人工合并。','',
                '本库独立维护，没有向综述正文插入引用或修改正文内容。工程文档与产业材料不计入论文目标。','',
                '发现流程：WebSearch检索和WebFetch打开综述/作者目录；从已打开的发现源提取论文链接；逐篇HTTP GET原始页面并保存HTML证据；抽取来源元数据、处理失败、去重和分区选取。各条记录真实 fetch_method，未声称所有页面均由同一种浏览工具打开。','',
                '数量选择：约500篇是文献库规模目标，不是系统综述的穷尽性声明。主库以环境、harness、agent三条线平衡组织，优先现有核心文献、直接环境变化/执行机制研究及多源共同收录工作。检索受公开可访问性、英文文献及arXiv覆盖影响。','']
    (ROOT/'README.md').write_text('\n'.join(summary))
    print(json.dumps(stats,ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
