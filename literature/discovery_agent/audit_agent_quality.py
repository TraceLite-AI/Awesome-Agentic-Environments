from pathlib import Path
import json,re,collections,datetime,hashlib
root=Path('/Users/conglin/Downloads/环境综述/文献库500')
a=[json.loads(x) for x in (root/'candidates_agent.jsonl').read_text().splitlines()]
es={}
for p in (root/'evidence').glob('*.json'):
 try:e=json.loads(p.read_text())
 except (ValueError,OSError):continue
 e['_path']=str(p);es[e['url']]=e
byid={x['url'].rsplit('/',1)[-1]:x for x in a}
def entry(aid,**kw):
 c=byid[aid];e=es[c['url']]
 return dict(url=c['url'],verified_title=e['title'],discovery_title_hint=c['title_hint'],evidence_file=e['_path'],**kw)
corrections=[
entry('2307.06135',issue='confirmed_discovery_label_link_swap',action='retain_with_verified_title',reason='发现目录hint为RoCo；原始arXiv标题及摘要均为SayPlan，摘要明确提出3D scene graph-based robotics planning。与2307.04738的hint构成互换。'),
entry('2307.04738',issue='confirmed_discovery_label_link_swap',action='retain_with_verified_title',reason='发现目录hint为Sayplan；原始arXiv标题及摘要均为RoCo，摘要明确提出LLM multi-robot collaboration，并引入RoCoBench。与2307.06135的hint构成互换。'),
]
aliasids=['2402.16906','2402.16823','2310.02170','2402.02172','2403.16218','2402.05102','2404.10887','2409.17140','2510.02250','2505.16938','2502.18864','2404.18021','2402.12993','2506.07551','2505.04997','2412.06412','2310.06500','2310.01444','2306.03604','2306.07929']
aliases=[entry(x,action='use_verified_title_count_arxiv_id_once',reason='发现目录标题/缩写与当前原始页标题不同，但摘要仍与agent/harness主题相关；此处不把书目差异当作已核实的历史改题。') for x in aliasids]
priority=[
entry('2303.17651',action='background_or_lower_priority_for_500_cap',reason='Self-Refine摘要讲单个LLM自行生成、反馈、迭代精炼，未声称外部执行环境、工具调用或环境因素干预。可作为harness/refinement背景，不列作环境因素直接证据。'),
entry('2403.02419',action='background_or_lower_priority_for_500_cap',reason='摘要研究Vote/Filter-Vote的多次LM调用与响应聚合，不是交互agent实验。广义compound-system/harness背景相关，但不宜标为多代理环境研究。'),
entry('2309.02726',action='background_or_lower_priority_for_500_cap',reason='摘要是从原始web语料进行科学假说生成及多模块反馈系统，未给出外部工具/执行环境交互。保留为scientific workflow背景合理，若按500篇限定核心agent/environment可优先让位。'),
]
relabelling=[
entry('2410.07706',suggested_topic='agent_training_and_trajectories',reason='AgentBank摘要覆盖16任务和五种agent技能，并非仅coding。'),
entry('2410.05434',suggested_topic='agent_training_with_feedback',reason='LEAP摘要覆盖ALFWorld、WebShop、Intercode Bash，并非仅coding。'),
entry('2306.07929',suggested_topic='agent_memory_and_rl',reason='原始摘要的方法名为REMEMBERER；是长期经验记忆与RLEM agent framework，不宜仅归具身。'),
entry('2307.15833',suggested_topic='text_game_agents',reason='摘要明确为text-based game中NPC对话与RL训练，不是物理或3D具身操作。'),
entry('2411.07228',suggested_topic='scientific_agent_tool_evaluation',reason='ChemToolAgent摘要重点是检验化学工具对多种任务的收益，属于agent工具评估，仍相关。'),
entry('2510.19898',suggested_topic='agent_training_data_synthesis',reason='BugPilot摘要主要是由SWE agents生成复杂bug和训练数据；相关但不是新的通用solver agent。'),
entry('2308.04748',suggested_topic='llm_execution_feedback_and_testing',reason='Fuzz4All主要为迭代LLM驱动的fuzzing loop；可按execution harness / testing背景纳入，不宜直接称自主agent。'),
entry('2401.00563',suggested_topic='llm_execution_feedback_and_testing',reason='KernelGPT主要为syscall规格生成及基于validation feedback的调试修复；可按execution harness / testing纳入。'),
]
nonmerge=[
{'urls':['https://arxiv.org/abs/2401.07339','https://arxiv.org/abs/2402.02172'],'reason':'均叫CodeAgent但原始标题、任务和摘要不同：前者repo-level code generation，后者code review。不要按方法短名合并。'},
{'urls':['https://arxiv.org/abs/2506.07551','https://arxiv.org/abs/2501.06590','https://arxiv.org/abs/2411.07228'],'reason':'目录存在ChemAgent近名；原始页分别为CheMatAgent、ChemAgent、ChemToolAgent，摘要分别是工具学习、动态记忆、工具评估。不是改题重复。'},
{'urls':['https://arxiv.org/abs/2501.06327','https://arxiv.org/abs/2504.19338'],'reason':'OpenFOAMGPT与2.0拥有不同arXiv ID；摘要分别为RAG simulator agent与多代理端到端workflow，不能仅因同系列合并。'},
{'urls':['https://arxiv.org/abs/2506.21805','https://arxiv.org/abs/2608.16897'],'reason':'CitySim与CityReal为同系列，后者摘要新增textual adapters及与人群统计对齐；仅凭相似摘要不能认定重复。当前各算独立候选，全文阶段再判工作继承。'},
]
backgroundids={x['url'] for x in priority};correctionids={x['url'] for x in corrections};relabids={x['url'] for x in relabelling}
checks=[]
for c in a:
 e=es[c['url']]
 checks.append({'url':c['url'],'title':e.get('title'),'verification_status':e.get('verification_status'),'has_abstract':bool(e.get('abstract')),'evidence_file':e['_path'],'recommendation':'background_lower_priority' if c['url'] in backgroundids else 'retain_correct_discovery_label' if c['url'] in correctionids else 'retain_relabel_topic' if c['url'] in relabids else 'retain','scope_basis':'title and abstract describe an agent method/application, interaction, tool or execution-feedback pipeline, or agent-system scaffolding; no full-text causal-factor claim is inferred'})
report={
'audit_date_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
'audit_scope':'240 candidates from candidates_agent.jsonl, using root-fetched original source landing-page titles and abstracts. Bibliographic/abstract-level relevance audit only; not full-text verification, not evidence that any paper controls environment factors.',
'method':'All 240 title/abstract availability and title hints screened; agent-role and framework sentences inspected across the library; full abstracts inspected for changed labels, short aliases, and scope-boundary papers. Cross-source normalized-title matching and fuzzy-title duplicate screen found no pair at >=0.85 similarity among current evidence involving these candidates.',
'counts':{'candidates':len(a),'verified_metadata':sum(es[c['url']].get('verification_status')=='verified_metadata' for c in a),'with_abstract':sum(bool(es[c['url']].get('abstract')) for c in a),'hard_exclude':0,'confirmed_discovery_label_link_swaps':2,'lower_priority_background':3,'title_or_alias_normalizations':len(aliases)},
'exclude_urls':[],
'hard_exclusions':[],
'confirmed_discovery_errors':corrections,
'use_verified_title_instead_of_discovery_hint':aliases,
'lower_priority_background':priority,
'reclassification_suggestions':relabelling,
'do_not_merge_by_short_method_name_or_family':nonmerge,
'general_recommendation':'在environment / harness / agent的宽口径书目库内，未发现必须剔除的明显离题或指向无关论文的URL。若只能选500篇，3篇纯/主要背景候选可优先让位。所有条目都不能仅因被收录就宣称研究了哪些环境因素改变正确解。',
'per_candidate_checks':checks}
(root/'quality_agent.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps(report['counts'],ensure_ascii=False))
print('Wrote',root/'quality_agent.json')
