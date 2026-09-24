from pathlib import Path
import re,json,collections
root=Path('/Users/conglin/Downloads/环境综述/文献库500');d=root/'discovery_agent'
a=[json.loads(l) for l in (d/'eligible_all.jsonl').read_text().splitlines()]
out=[]
def source(key,inds):
 rs=[x for x in a if x['source_key']==key]
 for i in inds:out.append(rs[i])
def topic(t,inds):
 rs=[x for x in a if x['topic']==t]
 for i in inds:out.append(rs[i])
source('se',[0,1,9,11,12,13,15,16,19,20,22,25,26,29,32,33,34,36,37,40,41,44,46,48,49,50,55,56,57,58,70,72,75,77,82,83,85,89,90,95,96,99,111,120,121,122,123,130,131,132,134,135,138,139,140])
source('code',[1,2,4,6,16,17,18,19,20,21,22,23,24,25,26,29,30,31,32,36,37,38,41,59,64])
topic('web_computer_mobile_agents',[3,4,7,8,13,18,22,23,24,28,30,34,37,43,52,55,57,58,59,63,65,69,75,76,77,78,79,80,83,87,88,91,92,93,94,95,97,98,106,107])
# Modern GUI methods; title/URL are extracted from the opened discovery README.
s=(d/'gui_new.md').read_text()
ids=['2501.12326','2509.02544','2508.09123','2602.09082','2602.16855','2601.15876','2503.21620','2503.15937','2504.14239','2412.17589','2501.04575','2508.15144','2505.22648']
for aid in ids:
 matches=re.findall(r'\[([^\]\n]+)\]\((https?://arxiv.org/(?:abs|pdf)/'+re.escape(aid)+r'[^)]*)\)',s)
 assert matches,aid
 title,_=max(matches,key=lambda t:len(t[0]))
 out.append(dict(url='https://arxiv.org/abs/'+aid,discovery_url='https://github.com/DeLunnLi/Awesome-Multimodal-GUI-Agents',topic='web_computer_mobile_agents',title_hint=title.strip('* '),source_key='gui_new'))
s=(d/'agent_s.md').read_text()
for aid in ['2504.00906','2510.02250']:
 assert 'https://arxiv.org/abs/'+aid in s
 for block in s.split('@'):
  if aid in block and 'title=' in block:
   title=re.search(r'title=\{([^}]+)',block).group(1);break
 out.append(dict(url='https://arxiv.org/abs/'+aid,discovery_url='https://github.com/simular-ai/Agent-S',topic='web_computer_mobile_agents',title_hint=title,source_key='agent_s'))
topic('scientific_research_agents',[1,2,4,5,6,7,8,9,10,11,14,16,17,18,19,20,21,22,24,27,28,29,30,36,37,39,40,43,46,48,49,50,52,54,57,64,66,68,71,73,74,76,80,81,82])
topic('embodied_llm_agents',range(26))
topic('multi_agent_interaction',[0,1,2,3,4,5,6,7,8,9,11,12,13,14,15,18,20,21,23,25,27,30,32,34,36,39,40,41,43,45,48,49,53,55])
# The source metadata are discovery hints only. The parent will verify each paper.
assert len(out)==len(set(x['url'] for x in out)), 'duplicate'
for x in out:
 aid=x['url'].rsplit('/',1)[-1]
 assert aid in (d/(x['source_key']+'.md')).read_text(),x
 assert x['title_hint'].strip(),x
reclassified=collections.Counter()
for x in out:
 if x['url'].rsplit('/',1)[-1] in ['2402.16823','2310.02170','2308.08155','2308.04030','2308.01285','2303.17760','2309.17288','2308.10848','2308.00352','2307.07924']:
  x['topic']='multi_agent_interaction'
# Keep required portable schema, with snapshots and this script as provenance.
(root/'candidates_agent.jsonl').write_text(''.join(json.dumps({k:x[k] for k in ['url','discovery_url','topic','title_hint']},ensure_ascii=False)+'\n' for x in out))
(d/'selected_agent_with_sources.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in out))
print('Selected',len(out));print(collections.Counter(x['topic'] for x in out));print(collections.Counter(x['source_key'] for x in out))
