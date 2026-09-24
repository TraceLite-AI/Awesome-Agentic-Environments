from pathlib import Path
import re,json,collections,html
BASE=Path('/Users/conglin/Downloads/环境综述/文献库500')
S=BASE/'discovery_harness'
repos=['NeuraLiying/Awesome-Agent-Harnesses','Gloriaameng/Awesome-Agent-Harness','js-lee-AI/awesome-llm-agent-papers','ggjy/Awesome-Agent-Engineering']
pool=[]

def title_of(line):
    if line.startswith('|'): return line.split('|')[1].strip()
    m=re.search(r'\*\*\[([^\]]+)\]\(https?://(?:www\.)?arxiv',line)
    if m:return m.group(1)
    m=re.search(r'\*\*"(.+?)"\*\*',line)
    if m:return m.group(1)
    m=re.search(r'\*\*_(.+?)_\*\*',line)
    if m:return m.group(1)
    return None

def topic_of(repo,heading):
    h=heading.lower()
    if 'surveys' in h or 'meta-analyses' in h:return 'harness_foundations_and_surveys'
    if any(s in h for s in ['security','safety','protocol standard']):return 'security_permissions_and_verification'
    if any(s in h for s in ['memory','context']):return 'memory_and_context'
    if any(s in h for s in ['agent-native training']):return 'agent_training_and_rl'
    if any(s in h for s in ['multi-agent','multi agent']):return 'multi_agent_coordination'
    if any(s in h for s in ['planning','reasoning','foundations of the agent loop','early llm']):return 'planning_search_and_reflection'
    if any(s in h for s in ['tool use','function calling']):return 'tool_use_and_interfaces'
    if any(s in h for s in ['harness & scaffold','full-stack','frameworks & modules','agent architectures','harness, runtime','coding & software engineering','code & swe agents']):return 'harness_runtime_and_orchestration'
    return None

for repo in repos:
    heading=''
    for lineno,line in enumerate((S/(repo.replace('/','__')+'.md')).read_text().splitlines(),1):
        if line.startswith('#'):heading=line.lstrip('# ').strip()
        if not line.startswith(('|','- ','* ')):continue
        title=title_of(line)
        if not title:continue
        ids=re.findall(r'https?://(?:www\.)?arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})',line)
        if not ids:continue
        topic=topic_of(repo,heading)
        if not topic:continue
        if topic=='agent_training_and_rl':
            if not re.search(r'(agent|tool|web|computer|swe|gui|reason)',title,re.I):continue
            if re.search(r'(vehicular|traffic signal|SDN-IoT|mobile systems|incentive aware|adaptive robust estimator|MARL-GPT)',title,re.I):continue
        for aid in dict.fromkeys(ids):
            pool.append({'url':'https://arxiv.org/abs/'+aid,'discovery_url':'https://github.com/'+repo,'topic':topic,'title_hint':html.unescape(re.sub(r'<[^>]+>','',title)),'_line':lineno,'_heading':heading})

seeds=[
('2605.27922','Harness-Bench: Measuring Harness Effects across Models in Realistic Agent Workflows','harness_runtime_and_orchestration'),
('2605.29682','Scaling Laws for Agent Harnesses via Effective Feedback Compute','harness_runtime_and_orchestration'),
('2508.03680','Agent Lightning: Train ANY AI Agents with Reinforcement Learning','agent_training_and_rl'),
('2608.17528','Agent Lightning v1.0: Towards Harnessed Agentic RL','agent_training_and_rl'),
('2510.04206','AgentRL: Scaling Agentic Reinforcement Learning with a Multi-Turn, Multi-Task Framework','agent_training_and_rl'),
('2409.19256','HybridFlow: A Flexible and Efficient RLHF Framework','agent_training_and_rl'),
]
seedrows=[dict(url='https://arxiv.org/abs/'+a,discovery_url='https://arxiv.org/abs/'+a,topic=t,title_hint=title) for a,title,t in seeds]
unique={}
for r in seedrows+pool:
    unique.setdefault(r['url'],r)
quotas={'harness_foundations_and_surveys':10,'harness_runtime_and_orchestration':30,'tool_use_and_interfaces':30,'planning_search_and_reflection':30,'memory_and_context':35,'multi_agent_coordination':30,'agent_training_and_rl':20,'security_permissions_and_verification':35}
selected=[];counts=collections.Counter()
for r in unique.values():
    if counts[r['topic']]>=quotas[r['topic']]:continue
    selected.append(r);counts[r['topic']]+=1
for f,rows in [('candidates_harness.jsonl',selected),('discovery_harness/candidate_pool.jsonl',list(unique.values()))]:
    with (BASE/f).open('w') as out:
        for r in rows:
            out.write(json.dumps({k:v for k,v in r.items() if not k.startswith('_')},ensure_ascii=False)+'\n')
print('POOL',len(unique),'SELECTED',len(selected),dict(counts))
for topic in quotas:
    print('\nTOPIC',topic)
    for r in selected:
        if r['topic']==topic:print(r['url'].split('/')[-1],r['title_hint'])
