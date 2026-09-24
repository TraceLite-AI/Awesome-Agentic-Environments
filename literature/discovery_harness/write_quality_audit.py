import json,collections,datetime,hashlib
from pathlib import Path
root=Path('/Users/conglin/Downloads/环境综述/文献库500')
ours={r['url']:r for r in map(json.loads,(root/'candidates_harness.jsonl').read_text().splitlines())}
read=[]
for name in ['audit_snapshot.json','audit_snapshot_new.json','audit_snapshot_final.json']:
 read+=json.loads((root/'discovery_harness'/name).read_text())
read={r['url']:r for r in read}
background={
'2201.11903':'讨论思维链示例如何改善数学、常识和符号推理；可作推理控制的历史背景，但摘要没有外部环境或执行闭环。',
'2203.11171':'研究多条推理路径采样与答案聚合；属于推理控制/集成的基础方法，不是执行环境或运行基础设施研究。',
'2205.11916':'研究零样本提示触发推理；可留作 prompting 方法背景，不能作为环境因素影响的证据。',
'2305.04091':'Plan-and-Solve 研究提示式问题分解与解答；为规划组件背景，不是有状态外部执行环境研究。',
'2211.09527':'研究 GPT-3 提示中的目标劫持与提示泄漏；是早期提示注入背景，摘要并未研究带工具的运行闭环。',
'2401.05566':'研究带后门模型在安全训练后的行为持续性；是威胁模型背景，不能等同于运行时权限/沙箱机制论文。',
'2306.07174':'LongMem 使用冻结编码器及可训练残差侧网络读取长记忆；核心是模型架构与长上下文建模，不是纯外置 agent harness。',
'2307.03172':'研究长上下文信息位置对问答/键值检索的影响；是上下文设计的基础证据，未直接评估 agent 行动闭环。',
'2403.11901':'Larimar 研究带分布式情节记忆的模型架构、事实编辑与遗忘；与外置 agent 工作记忆相关但机制层次不同。',
'2405.14831':'HippoRAG 研究知识图谱与 PageRank 检索并评估多跳问答；可作记忆检索机制背景，不应当作执行环境研究。',
'2407.16833':'研究静态 RAG 与长上下文及其路由折中；与上下文供给有关，但对 agent 运行层的关联间接，篇数受限时可移到扩展库。',
'2409.12917':'研究以多轮强化学习学习自我纠错，在数学/代码任务上评估；可作为反思训练背景，非环境运行系统研究。',
'2409.19256':'HybridFlow 研究 RLHF 的混合数据流、分布式执行与资源利用；可作训练系统背景，摘要没有直接证明 agent 环境因素效应。',
'2504.15585':'覆盖 LLM 数据、预训练、后训练、部署和商业化全周期安全；含 agent 但范围远宽于 harness，宜作广义安全背景。',
'2505.24298':'AReaL 早期论文主要研究数学/代码推理的异步生成与训练、陈旧样本和 GPU 利用；与 agentic RL 系统相关但不是完整代理部署闭环。'
}
notes={
'2309.15817':'ToolEmu 的 sandbox 是语言模型模拟工具执行；不能据此推断其提供 OS 级隔离或容器安全边界。',
'2408.04682':'ToolSandbox 是状态化工具执行与会话评测环境；题名中的 Sandbox 不等于微虚机/容器隔离平台。',
'2506.06326':'MemoryOS 的 OS 指记忆存储、更新与检索管理的类比；不得标注为操作系统版本/内核变化证据。',
'2507.03724':'MemOS 统一明文、激活与参数级记忆；OS 是记忆资源管理抽象，不能当宿主操作系统因素研究。',
'2309.17234':'原页是多方交互谈判测试床，覆盖合作、竞争、恶意参与者和动态多轮协作；相关但应标多代理交互/评测，而非一般推理辩论框架。',
'2310.02170':'候选 title_hint 已说明 v2 改题；当前原页是 DyLAN 动态选队与通信结构论文。采用原页题名，不判为错链。',
'2507.13334':'目录题名是描述性改写，原页正式题名为 A Survey of Context Engineering for Large Language Models；内容涵盖上下文、记忆、工具与多代理，非错论文。',
'2510.21236':'目录使用简写 Securing AI Agent Execution；原页 AgentBound 讨论代理执行边界，内容相关。采用原页完整题名。',
'2605.29682':'原页是 Scaling Laws for Agent Harnesses via Effective Feedback Compute；不是 Harness survey。早期口头分类已更正，按 scaling/feedback-compute 方法论文保留。',
'2508.07935':'SHIELDA 摘要核心是异常分类、运行时处理与恢复，应补标签 runtime_error_recovery，不宜只归为权限/安全。',
'2604.11378':'摘要明确称 position paper and design proposal；作为架构提案保留，不能在综述中描述成已完成部署验证的系统。',
'2603.11853':'OpenClaw PRISM 摘要报告 preliminary curated benchmarks/microbenchmarks；保留为运行架构研究，效果外推需受这些评估边界约束。',
'2603.13404':'Schema First Tool APIs 的摘要明确是单模型小规模 pilot，终任务成功率在全部条件为零；证据支持接口误用下降，不支持任务成功率提高。',
'2607.01120':'摘要以三支柱的系统论证/架构建议为主，并实例化 AReaL2.0 的一条分支；不要把全部愿景都写成已经实现。',
'2606.25447':'直接把 harness 设计设为可控变量，并区分任务/工具环境迁移与后训练，属于高相关核心文献。',
'2609.04518':'直接区分多 harness 暴露与跨 harness 优势分组，并在未见 harness 上评估迁移；属于高相关核心文献。摘要结论有明确限定，不能只摘选效应最大的数字。',
'2607.10569':'直接交叉比较任务类型、agent 设计和执行工具表面；其结果区分成本与通过率，不能概括为限制工具普遍提高正确率。',
'2602.10453':'摘要特别讨论任务的正确行动依赖运行时环境观察；与 survey 的环境条件依赖问题直接相关。',
'2605.03378':'ARGUS/AgentLure 明确研究 context-dependent 任务和环境证据对具体行动的因果支持；与权限边界及正确行动条件直接相关。',
'2607.25656':'OrchBench 用确定性模拟器评估编排计划，不实际调用 worker；可作编排评价证据，不能当成所有结果均来自真实执行。',
'2608.17528':'Agent Lightning v1.0 是 2508.03680 的后续系统工作，题名和摘要所述训练/harness 机制有新增内容；不按版本名直接视为重复。',
'2606.21856':'Harness-MU 研究多用户治理及执行 hooks，直接相关；摘要的绝对安全措辞属于作者主张，书目核验不等于验证其普适保证。',
'2605.02801':'该文区分开放学术方法与工业公开部署信息，属于编排轨迹/RL综述；不可把公开工业报告写成已独立核验的训练轨迹。'
}
topic_reason={
'harness_runtime_and_orchestration':'摘要讨论代理运行结构、工作流、执行接口或编排机制，与 harness 主范围直接相关。',
'agent_training_and_rl':'摘要讨论代理动作/轨迹学习、训练执行接口或交互式强化学习，与运行层—学习层接口相关。',
'harness_foundations_and_surveys':'摘要提供 agent/harness 架构、组成或评测的组织框架，可用于综述脉络。',
'planning_search_and_reflection':'摘要讨论计划、搜索、反馈纠错、验证或执行控制，可用于 harness 控制机制的分类。',
'memory_and_context':'摘要讨论状态/经验的保存、检索、压缩、更新或上下文管理，可用于代理记忆与上下文组件分类。',
'multi_agent_coordination':'摘要讨论代理间角色、通信、协作、编排或故障，可用于多代理控制层分类。',
'security_permissions_and_verification':'摘要讨论代理工具、外部信息、记忆或执行中的攻击、防御、权限与验证，与运行边界相关。',
 'tool_use_and_interfaces':'摘要讨论外部工具的表示、选择、调用、执行反馈或评测，与工具接口层直接相关。'
}
records=[]
for url,e in sorted(read.items()):
 ident=url.rsplit('/',1)[-1];c=ours[url]
 decision='keep_relevant';reason=topic_reason[c['topic']]
 if ident in background:decision='keep_background_only';reason=background[ident]
 if ident=='2603.00195':
  decision='exclude_from_main_pending_content_review'
  reason='原页 Abstract 栏本身为 v2 修订/勘误说明，不能据此正常完成方法内容的摘要级分类。暂移出主库而保留证据；这不是错链、虚构论文或抓取字段错误。'
 r={'url':url,'title':e['title'],'topic_at_discovery':c['topic'],'decision':decision,'reason':reason,'title_and_abstract_read':True,'full_text_reviewed':False,'abstract_sha256_at_review':hashlib.sha256(e.get('abstract','').encode()).hexdigest()}
 if ident in notes:r['specific_note']=notes[ident]
 if c['title_hint']!=e['title']:r['title_hint_differs_from_source']=True
 records.append(r)
duplicate_groups=[
 {'preferred_record':'https://arxiv.org/abs/2304.08244','alternate_urls':['https://doi.org/10.18653/v1/2023.emnlp-main.187'],'title':'API-Bank: A Comprehensive Benchmark for Tool-Augmented LLMs','basis':'人工比对两页已抓取的完整标题、作者序列与摘要一致。'},
 {'preferred_record':'https://arxiv.org/abs/2403.07714','alternate_urls':['https://doi.org/10.18653/v1/2024.findings-acl.664'],'title':'StableToolBench: Towards Stable Large-Scale Benchmarking on Tool Learning of Large Language Models','basis':'人工比对两页已抓取的完整标题、作者序列与摘要一致。'},
 {'preferred_record':'https://arxiv.org/abs/2412.21139','alternate_urls':['https://proceedings.mlr.press/v267/pan25g.html'],'title':'Training Software Engineering Agents and Verifiers with SWE-Gym','basis':'人工比对两页已抓取的完整标题、作者序列与摘要一致。'}
]
out={
 'audit_date':'2026-09-24','reviewer':'harness candidate subagent / independent metadata-and-abstract relevance audit',
 'scope':'225 条 candidates_harness.jsonl 候选；逐条人工阅读原始来源页已核验的标题与完整摘要，审查相关性、目录错链及书目重复。',
 'not_performed':['未把 225 篇当作全文精读','未独立复现实验或核验摘要中的效果数字','未验证作者关于首创、SOTA、绝对安全或可扩展性的断言'],
 'method':'根代理逐篇请求原始论文页并保存 evidence；本审计读取这些原页标题/摘要记录。人工阅读全文段后判定相关性。字符串相似度仅用于发现待核对的异名/重复候选，未作为最终排除依据。2603.00195 额外用 Web Open 重新打开原页并确认异常摘要确属原站内容。',
 'candidate_count':len(ours),'title_abstract_reviewed_count':len(records),
 'decision_counts':dict(collections.Counter(r['decision'] for r in records)),
 'confirmed_wrong_paper_links':[],
 'confirmed_completely_unrelated_papers':[],
 'main_findings':[
   '未发现已核验候选指向明显无关论文的目录错链；若目录题名与原页不同，以原页题名为准。',
   '15 篇是提示、模型记忆、静态检索、安全训练或通用 RL 系统背景，不应全部算作直接 harness/执行环境证据；约 500 篇的主库如需优先直接相关论文，可把这组移到扩展库。',
   '2603.00195 原页摘要为勘误说明，建议暂移出主库；不是 metadata 提取错误，也不能据此认定论文虚构。',
   '发现 3 组 arXiv 与正式出版页的同篇别名，应各计 1 篇；未发现本 harness 候选中不同 arXiv ID 的明确同篇重复。',
   'MemoryOS/MemOS 的 OS、ToolEmu/ToolSandbox 的 sandbox 等术语应按实际机制分类，避免误标为宿主 OS/隔离技术。',
   '保留研究设计与证据类型：position/proposal、pilot、确定性模拟和实际执行不可混写；元数据核验不背书论文的经验结果。'
 ],
 'duplicate_groups':duplicate_groups,
 'pending_candidates':[u for u in ours if u not in read],
 'source_snapshots':['discovery_harness/audit_snapshot.json','discovery_harness/audit_snapshot_new.json','discovery_harness/audit_snapshot_final.json'],
 'special_source_opened':{'url':'https://arxiv.org/abs/2603.00195','method':'Web Open','finding':'页面 Abstract 字段本身包含修订说明；Comments 为另一个字段。'},
 'records':records
}
(root/'quality_harness.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['candidate_count','title_abstract_reviewed_count','decision_counts','pending_candidates']},ensure_ascii=False,indent=2))
print('wrote',root/'quality_harness.json')
