# Harness 候选发现与选材说明

日期：2026-09-24。此文件记录候选发现过程；题名、作者、年份与论文链接是否匹配，以根代理逐篇打开原始论文页的核验为准。候选目录的说明和引用数字未作为论文结论使用。

## 选材范围与优先级

关注 LLM 之外组织行动的运行层：工具接口、执行循环、规划与恢复、记忆与上下文、多个代理的协作、训练与实际运行的衔接、权限与验证。

1. 直接把 harness/scaffold/runtime/agent-computer interface 当研究对象的论文优先，包括控制条件下比较 harness、自动优化 harness、工作流与调度研究。
2. 组件研究须解释可识别的运行机制：工具选择/调用格式、计划生成/执行反馈/修复、状态记忆/检索/压缩、多代理通信/工作流。保留 ReAct、Reflexion、CodeAct、MemGPT 等相应路线的早期工作，再补近期直接关联该运行机制的研究。
3. 训练研究侧重运行与学习的接口、轨迹与奖励采集、异步执行或部署 harness 进入训练过程。Agent Lightning、AgentRL、HybridFlow、AReaL 等用于该接口脉络；Web/GUI/coding RL 论文作为具体执行闭环实例。
4. 安全研究侧重代理实际读入或执行外部内容后的风险、工具/权限边界、运行时约束、记忆污染及动作验证。纯聊天模型对齐或与 LLM 无关的传统 MARL 不作为此组核心。
5. 多代理论文须有通信、编排、协作或失败诊断的机制；宽泛社会模拟与领域应用只有直接关系清楚时才保留。
6. 综述用于连接文献脉络，数量保持较少；普通 LLM 总综述、纯产品文档/博客/README 和只有代码仓库而没有论文的项目没有计入本候选表。

采用按组件分组的有限初选，避免论文量大的记忆或工具目录占满列表；随后人工替换泛化过宽的条目，增加直接比较 harness、权限与执行机制的近期论文。组内顺序不代表质量排名；未以引用量、作者名气或检索排序推断结论可信度。主题可能交叉，当前每篇只给一个主标签，根代理可重标。

## 已通过 WebSearch 发现并用 Web Open 打开的目录

- https://github.com/NeuraLiying/Awesome-Agent-Harnesses
- https://github.com/Gloriaameng/Awesome-Agent-Harness
- https://github.com/js-lee-AI/awesome-llm-agent-papers
- https://github.com/ggjy/Awesome-Agent-Engineering
- https://github.com/areal-project/AReaL

前四个 README 已保存快照；`candidate_pool.jsonl` 是从相关章节抽出的广池，未整体纳入主候选。它包含待重新审查范围的条目，不能直接当最终书目。

## 额外原页已打开的种子

- https://arxiv.org/abs/2605.27922 — Harness-Bench: Measuring Harness Effects across Models in Realistic Agent Workflows
- https://arxiv.org/abs/2605.29682 — Scaling Laws for Agent Harnesses via Effective Feedback Compute
- https://arxiv.org/abs/2508.03680 — Agent Lightning: Train ANY AI Agents with Reinforcement Learning
- https://arxiv.org/abs/2608.17528 — Agent Lightning v1.0: Towards Harnessed Agentic RL
- https://arxiv.org/abs/2510.04206 — AgentRL: Scaling Agentic Reinforcement Learning with a Multi-Turn, Multi-Task Framework
- https://arxiv.org/abs/2409.19256 — HybridFlow: A Flexible and Efficient RLHF Framework
- https://arxiv.org/abs/2505.24298 — AReaL: A Large-Scale Asynchronous Reinforcement Learning System for Language Reasoning
- https://arxiv.org/abs/2607.01120 — Next-Generation Agentic Reinforcement Learning Systems Enable Self-Evolving Agents

其中 2605.29682 曾被口头指认为综述，原页显示是 scaling laws 论文；主候选已采用原页题名。其他候选的 title_hint 保留发现源写法，不能视为已核验题名。

## 当前候选数

共 225 个去重 arXiv URL。

- harness_runtime_and_orchestration: 33
- agent_training_and_rl: 18
- harness_foundations_and_surveys: 10
- planning_search_and_reflection: 29
- tool_use_and_interfaces: 30
- memory_and_context: 35
- multi_agent_coordination: 31
- security_permissions_and_verification: 39
