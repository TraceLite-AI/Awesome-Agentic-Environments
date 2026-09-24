from bs4 import BeautifulSoup
from pathlib import Path
import re,json,collections
root=Path('/Users/conglin/Downloads/环境综述/文献库500')
soup=BeautifulSoup((root/'source_environment_survey.html').read_text(),'html.parser')
source='https://arxiv.org/html/2606.12191v1'
selected=set(range(27,199))-{29,41,49,50,51,64,67,72,74,76,77,92,101,104,113,129,131,132,133,140,143,150,169,173,183,184,188,189,195,196}
selected |= {3,9,11,15,16}
selected |= set(range(296,321))-{296,298,299,305,313}
selected |= {337,338,341,343,344,346,347,350,351,352,353,354,355,359,361,362,363,364,366,368,369,370,371,372,373,374,375,376,378,379,382,383,384,386,387,388,391,392,394,395,396,398,399,402,403,407,408,409,411,412,413,414,415,416,417,419,422,423,424,426,427,428,429,430,431,432,434,435,437,439,443}
rows=[];seen=set();missing=[]
def norm(u):
 m=re.search(r'(?:arxiv[^0-9]*|abs/|pdf/|html/)(\d{4}\.\d{4,5})(?:v\d+)?',u,re.I)
 if m:return 'https://arxiv.org/abs/'+m.group(1)
 return u.replace('http://','https://').strip().rstrip('.,')
def add(u,src,topic,title):
 u=norm(u)
 if u in seen:return
 if not re.match(r'https?://',u):return
 seen.add(u);rows.append(dict(url=u,discovery_url=src,topic=topic,title_hint=title.strip().rstrip(',')))
def topic(n):
 if n in {27,28,52,53,54,55,56,57,58,59,60,61,341,347,350,351,352,353,354,355}:return 'GUI/web/mobile/OS interactive environments'
 if n in {3,9,15,16,42,43,44,45,46,47,48,118,119,120,121,122,123,124,125,126,127,128,134,135,136,137,138,139,141,142,144,145,146,147,148,149,151,359,373,374,375,376,378,379,382,383,386,387,388,391,392,394,395,396,398,399,402,403}:return 'Interactive agent benchmarks/tool/code/enterprise environments'
 if 79<=n<=117 or n in {361,362,363,364,366,368,371,372,384}:return 'Embodied/game/simulation environments'
 if 296<=n<=320:return 'Environment evolution/curriculum/unsupervised environment design'
 if n in {337,338,346,369,370,408,430,431,432,434,435,437,439,443} or 178<=n<=198:return 'Interactive world models/neural simulators'
 if 152<=n<=177 or n in {11,343,344,407,409,411,412,413,414,415,416,417,419,422,423,424,426,427,428,429}:return 'Environment synthesis/generation/executable task construction'
 return 'Research/search interactive environments'
for b in soup.select('.ltx_bibitem'):
 n=int(re.search(r'bib(\d+)$',b.get('id')).group(1))
 if n not in selected:continue
 txt=b.get_text(' ',strip=True)
 m=re.search('“(.+?)”',txt);title=m.group(1) if m else txt
 links=[a.get('href') for a in b.select('a[href]')]
 arxiv=re.search(r'(?:arxiv[:\s]*|abs/)(\d{4}\.\d{4,5})',txt,re.I)
 if arxiv:u='https://arxiv.org/abs/'+arxiv.group(1)
 else:
  links=[u for u in links if re.search(r'arxiv|doi.org|openreview|proceedings\.mlr|aclanthology|neurips|papers\.nips|openaccess.thecvf',u,re.I)]
  if not links:missing.append([n,title]);continue
  u=links[0]
 add(u,source,topic(n),title)
add('https://arxiv.org/abs/2606.12191',source,'Environment survey','Agentic Environment Engineering for Large Language Models: A Survey of Environment Modeling, Synthesis, Evaluation, and Application')
for filename,src,topicname in [('source_world_models.html','https://github.com/journee-live/awesome-world-models','Interactive world models/neural simulators'),('source_coevolution.html','https://github.com/zongqing0068/awesome-co-evolution','Open-ended learning/procedural environment evolution')]:
 s=BeautifulSoup((root/filename).read_text(),'html.parser'); article=s.select_one('article')
 for li in article.select('li') if article else []:
  txt=li.get_text(' ',strip=True)
  if filename=='source_world_models.html' and any(t in txt for t in ['ART•V','Counter-Strike','GameFactory-Dataset']):continue
  if filename=='source_coevolution.html' and not any(t in txt for t in ['Emergent Tool Use','Emergent Complexity','APT-Gen','Asymmetric Self-Play','OMNI-EPIC','XLand','ADR','POET','EnvACE','EvolvingWorld','EvolvingAgent']):continue
  links=[a.get('href') for a in li.select('a[href]') if re.search(r'arxiv.org|openreview.net',a.get('href',''))]
  if links:add(links[0],src,topicname,txt.split('[ Paper')[0])
out=root/'candidates_environment.jsonl'
out.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))
(root/'environment_discovery_notes.json').write_text(json.dumps({'sources_opened':[source,'https://github.com/clvrai/awesome-rl-envs','https://github.com/journee-live/awesome-world-models','https://github.com/zongqing0068/awesome-co-evolution'],'count':len(rows),'topic_counts':dict(collections.Counter(x['topic'] for x in rows)),'source_reference_numbers_without_paper_url':missing,'status':'Discovery candidates only; individual paper metadata verification delegated to parent.'},ensure_ascii=False,indent=2))
print('COUNT',len(rows),'MISSING',len(missing));print(json.dumps(collections.Counter(x['topic'] for x in rows),ensure_ascii=False,indent=2));print('MISSING',missing)
