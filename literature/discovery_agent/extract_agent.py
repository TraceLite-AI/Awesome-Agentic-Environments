from pathlib import Path
import re,json,html,collections
ROOT=Path('/Users/conglin/Downloads/环境综述/文献库500')
D=ROOT/'discovery_agent'
repos={'se':'FudanSELab/Agent4SE-Paper-List','general':'Paitesanshi/LLM-Agent-Survey','multi':'taichengguo/LLM_MultiAgents_Survey_Papers','all':'luo-junyu/Awesome-Agent-Papers','os':'OS-Agent-Survey/OS-Agent-Survey','science':'AgenticScience/Awesome-Agent-Scientists','code':'EuniAI/awesome-code-agents'}
rows=[]
def add(key,text,title,topic):
 urls=re.findall(r'https?://(?:www\.)?arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})(?:v\d+)?',text)
 if not urls:return
 title=html.unescape(re.sub(r'<[^>]+>',' ',title)); title=re.sub(r'\s+',' ',title).strip(' *.-\\')
 for aid in urls[:1]:
  if aid[:4]>'2609':continue
  rows.append(dict(url='https://arxiv.org/abs/'+aid,discovery_url='https://github.com/'+repos[key],topic=topic,title_hint=title,source_key=key))
# Software-engineering survey: first task-perspective list only to avoid repetitions.
s=(D/'se.md').read_text().split('## 🖥️ SE Perspectives',1)[-1].split('## 🤖 Agent Perspectives',1)[0]
section=''
for line in s.splitlines():
 if line.startswith('#'):section=line.strip('# ')
 if 'arxiv.org' in line and line.lstrip().startswith(('-', '*')):
  mt=re.search(r'\*\*(.+?)\*\*',line)
  title=mt.group(1) if mt else line.split('[[paper]')[0]
  if re.search(r'bench|dataset|survey|empirical|evaluating|evaluation|measuring|study of|analysis of',title,re.I):continue
  add('se',line,title,'coding_agents')
# Most recent code agents, multi-line markdown blocks, exclude evaluation-only material.
s=(D/'code.md').read_text().split('## 🧱 Code as Artifact',1)[-1].split('## 🗺️ Research Landscape',1)[0]
for m in re.finditer(r'^- \*\*(.+?)\*\*(.*?)(?=^- \*\*|^#{1,4} |\Z)',s,re.M|re.S):
 title=m.group(1).strip();block=m.group(0)
 if re.search(r'bench|dataset|survey|empirical|evaluating|evaluation|measuring|study of|analysis of',title,re.I):continue
 add('code',block,title,'coding_agents')
# OS methods and foundation agents; dataset/benchmark entries excluded.
s=(D/'os.md').read_text().split('## Full List',1)[-1].split('### Evaluation & Benchmark',1)[0]
for line in s.splitlines():
 if not re.match(r'\d+\.',line):continue
  # Standard list record with title before [[paper]].
 title=re.sub(r'^\d+\.\s*\[\d{4}/\d{2}/\d{2}\]\s*','',line).split('[[paper]')[0]
 if re.search(r'bench|dataset|MM1.5|survey|safety|attack',title,re.I):continue
 add('os',line,title,'web_computer_mobile_agents')
# Scientific agents, title and URL extracted from the same HTML list item.
s=(D/'science.md').read_text()
for block in re.findall(r'<li>(.*?)</li>',s,re.S):
 mt=re.search(r'<b>(.*?)</b>',block,re.S)
 if not mt:continue
 title=mt.group(1)
 if re.search(r'bench|survey|dataset|bibliometric|review of',title,re.I):continue
 if not re.search(r'agent|autonom|scientist|tool|closed.loop|workflow|automated|automation',title,re.I):continue
 add('science',block,title,'scientific_research_agents')
# Embodied agents from applications table of the autonomous-agent survey.
s=(D/'general.md').read_text().split('## 📍 Applications',1)[-1].split('## 📊 Evaluation',1)[0]
for block in re.findall(r'<tr>(.*?)</tr>',s,re.S):
 cells=re.findall(r'<td[^>]*>(.*?)</td>',block,re.S)
 if not cells:continue
 if 'Robotics' in block or 'Embodied' in block:add('general',block,cells[0],'embodied_llm_agents')
# Multi-agent interaction/coordination, avoiding datasets and domain branches outside scope.
s=(D/'multi.md').read_text().split('# Multi-Agents Framework',1)[-1].split('# Multi-Agents Datasets and Benchmarks',1)[0]
section='Multi-Agents Framework'
for line in s.splitlines():
 if line.startswith('#'):section=line.strip('# ')
 if 'arxiv.org' not in line:continue
 if section in ['Psychology','Economy','Recommender System','Policy Making','Disease propagation Simulation']:continue
 title=re.sub(r'^\\?\[\d{4}/\d{2}\\?\]\s*','',line).split('[\\[paper')[0]
 if 'Embodied' in section:topic='embodied_llm_agents'
 elif 'Science Team' in section:topic='scientific_research_agents'
 else:topic='multi_agent_interaction'
 add('multi',line,title,topic)
# General updated repository: selectively add scientific/embodied/collaborative works.
s=(D/'all.md').read_text()
section=''
for line in s.splitlines():
 if line.startswith('### '):section=line[4:]
 m=re.match(r'- \*\*\[(.+?)\]\((https?://arxiv\.org/[^)]+)\)',line)
 if not m:continue
 title,url=m.groups()
 if re.search(r'bench|survey|dataset|evaluation|evaluating|ethical|attack',title,re.I):continue
 if section=='Agent Collaboration':topic='multi_agent_interaction'
 elif section=='Applications' and re.search(r'agent|autonom|scientist|workflow',title,re.I):
  if re.search(r'scien|research|chem|bio|drug|protein|experiment|CFD',title,re.I):topic='scientific_research_agents'
  elif re.search(r'robot|embodied|mine|physical|game',title,re.I):topic='embodied_llm_agents'
  else:continue
 else:continue
 add('all',url,title,topic)
# Record all extracted eligible candidates for transparent later sampling.
seen=set();allrows=[]
for r in rows:
 if r['url'] in seen:continue
 seen.add(r['url']);allrows.append(r)
(D/'eligible_all.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in allrows))
print('Eligible',len(allrows));print(collections.Counter(r['topic'] for r in allrows));print(collections.Counter(r['source_key'] for r in allrows))
for topic in dict.fromkeys(r['topic'] for r in allrows):
 print('\n',topic)
 for i,r in enumerate([r for r in allrows if r['topic']==topic]):print(i,r['url'].rsplit('/',1)[-1],r['source_key'],r['title_hint'][:130])
