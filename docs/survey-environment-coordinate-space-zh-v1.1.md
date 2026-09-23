# 环境是什么：AI Agent 执行环境的坐标空间

## 综述与提案（v1.1 草稿，2026-09-23）

> 体裁：综述 + 提案。前半部分梳理四个领域如何使用"环境"一词，后半部分提出一个统一框架。所有文献均逐篇打开原文核对；引用中的数字均来自原文。本文不包含作者团队未发表的实验结果。

---

## 摘要

AI Agent 的能力评测与强化学习训练都依赖"环境"，但这个词在不同社区里指四种不同的东西。Agent benchmark 把环境当作一个钉死的常量：一个 Docker 镜像或虚拟机快照，从不作为自变量。强化学习基础设施把环境当作一个带旋钮的沙箱：网络策略、隔离级别、镜像分层都可以设置，但没有人定义哪个旋钮会改变任务的正确解。机器学习的鲁棒性与不变性研究把环境当作"答案不应随之改变"的干扰因子，准入条件恰好与执行环境相反。软件工程则早在三十年前就把配置空间当作因子的笛卡尔积，用组合测试和实验设计给出了测量预算的理论。

本文的主张是：这四种用法可以统一到一个坐标空间。环境是策略之外、能够改变正确解法的一切；它无限维，因此只能投影到有限根过得了检验的轴上；每根轴的准入判据是"改变正确解"，这是因果干预的概念而不是干扰的概念；测量协议是一次一因子的星形设计加两两覆盖数组，报数是按轴的方向导数与翻转率，禁止总分。我们给出五组 22 个因子 75 个取值的第一版，并把它逐项映射到现有训练基础设施暴露的参数上，说明采用这一坐标系不需要新的基建，缺的只是语义层。

---

## 1 引言：一个词，四种用法

一个 Agent 在真实系统里完成任务，要读文件、跑命令、装依赖、开浏览器。它的行为由两样东西决定：策略（模型加运行框架），和策略之外的一切。后者就是环境。

问题在于，"环境"这个词现在同时被四个社区使用，而它们的含义互不兼容：

- **Agent benchmark** 社区说"我们提供了一个可复现的环境"，意思是一个固定的容器或虚拟机快照。环境是常量，评测的自变量只有模型。
- **强化学习基础设施** 社区说"我们每天跑三百万个环境"，意思是三百万个沙箱实例。环境是可以配置的资源，有网络、权限、隔离级别等旋钮。
- **机器学习鲁棒性** 社区说"模型应该对环境不变"，意思是训练数据来自不同的采集条件，而正确的预测器不该随条件改变。环境是干扰。
- **软件工程** 社区说"CI 矩阵覆盖了所有环境"，意思是操作系统乘语言版本乘依赖版本的笛卡尔积。环境是配置空间的一个点。

这四种用法各自有效，但放在一起就露出一个空缺：**没有人回答"哪些环境因素会改变一道任务的正确解"**。Benchmark 社区不问，因为环境是常量；基础设施社区不问，因为旋钮只关乎资源与安全；鲁棒性社区问的是反问题，它准入的因子恰恰是答案不该随之变的那些；软件工程社区有方法但没有对象，组合测试的因子是软件自己的配置项，不是 Agent 面对的世界。

本文分两步填这个空缺。第二到第五章逐一梳理四个社区的用法，每章给出一张覆盖表或对照表，让读者看到空缺具体在哪一格。第六章提出环境坐标空间：定义、轴的准入判据、因子与取值、格的钉住清单、测量协议、报数方式。第七章把它映射到现有基础设施的参数上。第八章列出尚未解决的问题。

---

## 2 Agent benchmark 里的环境：常量

我们逐篇核对了 17 个主流 Agent benchmark 的论文或官方文档，检查它们对执行环境的声明程度。结果见表 A。

**表 A：Agent benchmark 对环境因子的声明与控制**
（固 = 固定常量且已声明；变 = 作为自变量变化；— = 论文未声明）

| Benchmark | OS 与版本 | 隔离 / 镜像 | 镜像 digest | 网络 | 权限 | locale / 时区 | 观测通道 | 硬件 | 同一任务跨 OS 测量 |
|---|---|---|---|---|---|---|---|---|---|
| SWE-bench [1] | — | 固 conda 后改 Docker | — | — | — | — | 终端 | — | 无 |
| SWE-bench Verified [2] | Linux（Epoch 复现） | 固 Docker | — | 固 禁网（Epoch） | — | — | 终端 | — | 无 |
| SWE-bench Multimodal [3] | — | 固 Docker + Node + Chrome | — | — | — | — | 终端 + 无头浏览器 | — | 无 |
| Terminal-Bench [4] | —（Docker，隐含 Linux） | 固 Docker | —（pin 包版本，apt 包不 pin） | 固 允许联网 | — | — | 终端 | —（局限中承认 CPU 架构影响） | 无 |
| OSWorld [5] | Ubuntu / Windows / macOS，无版本 | 固 VM 快照 | — | — | — | — | GUI | — | 43 道 Ubuntu 到 Windows：4.88% 对 2.55% |
| OSWorld-Verified [6] | Ubuntu / Windows | 固 AWS 镜像 | — | — | — | — | GUI | — | 无 |
| WebArena / VisualWebArena [7][8] | — | 固 Docker 自托管 | — | 固 离线 | — | — | 浏览器 | — | 无 |
| AgentBench [9] | Ubuntu Docker | 固 | — | — | — | — | 终端等 | — | 无 |
| τ-bench [10] | 无 OS | DB + API | — | — | — | — | 工具调用 | — | 无 |
| GAIA [11] | 无 | 活网 | — | 活网，承认衰减 | — | — | — | — | 无 |
| MLE-bench [12] | Ubuntu 20.04 | 固 Docker + sysbox | — | — | — | — | 终端 | 变：CPU-only / 标准 / 加 GPU | 无 |
| Windows Agent Arena [13] | Windows 11 | 固 Docker 内 VM | — | — | — | — | GUI | — | 2/3 任务从 OSWorld 移植，无数值对比 |
| AndroidWorld [14] | Android 13，Pixel 6 | 固 模拟器 | — | — | — | — | GUI | — | 无（变的是任务参数） |
| AppWorld [15] | 无 | 模拟 app | — | — | — | 固 时间冻结 | 代码 | — | 无 |
| TheAgentCompany [16] | — | 固 Docker 自托管 | — | 固 自托管 | — | — | 终端 + 浏览器 | — | 无 |
| MacArena [17] | macOS，UTM VM | 固 VM | — | — | — | — | GUI | — | 同 OSWorld 题集 Linux 到 macOS：三个模型分别降 3.2、9.3、9.8 个百分点 |
| macOSWorld [18] | macOS | 固 VM | — | — | — | 变：5 种界面语言 | GUI | — | 无 |

从表 A 可以读出五件事。

第一，**digest 列全空**。没有一篇论文给出镜像的内容哈希。Terminal-Bench 明确要求 pin 包版本，但同时规定 apt 包"不得 pin" [4]；SWE-bench 的 README 说 x86_64 为主、arm64 为实验性支持 [1]。这意味着两个团队按同一篇论文复现出的"同一个环境"，在字节层面可以不同。

第二，**权限列全空，locale 列几乎全空**。没有一篇 benchmark 声明 Agent 以什么用户运行、系统目录是否可写、locale 与时区是什么。只有 AppWorld 冻结了时间 [15]，macOSWorld 把界面语言作为变量 [18]。

第三，**环境从不作为自变量**。所有变化都发生在别处：AndroidWorld 变的是任务参数 [14]，τ-bench 和 Terminal-Bench 变的是采样重复次数 [10][4]，MLE-bench 变的是计算预算 [12]。唯一把环境本身当变量的是 macOSWorld 的界面语言轴（阿拉伯语平均下降 28.8% [18]）。

第四，**同一任务跨 OS 的测量只存在于 GUI 领域，且样本很小**。OSWorld 把 43 道 Ubuntu 任务搬到 Windows，得到 4.88% 对 2.55%，相关系数 0.7 [5]；MacArena 把 OSWorld 的任务集原样搬到 macOS，三个模型分别下降 3.23、9.26、9.84 个百分点，作者的结论是"现有 benchmark 上的高分可能反映的是对任务分布的熟悉，而不是真正的跨平台 GUI 能力" [17]。Coding 与终端领域，我们经过七轮检索没有找到任何一篇"任务不动、变 OS 或 shell 或 locale"的研究。Terminal-Bench 自己在局限一节写道："机器资源与容器运行时强制策略的差异会导致有效任务环境不同"，以及"任务结果可能因硬件差异（例如 CPU 架构）而变化" [4]。这是一处被作者承认但未被处理的自变量。

第五，**"环境"的形式定义要么缺席，要么是 POMDP 的元组**。WebArena、VisualWebArena、Windows Agent Arena 都把环境写成 ⟨S, A, O, T⟩ 或 (S, O, A, T, R) [7][8][13]。这个定义在数学上完整，但对"操作系统换了会怎样"没有任何话可说，因为 OS 被吸收进了转移函数 T 里，而 T 从来不是被测量的对象。

对本文而言，表 A 的意义不是批评这些 benchmark，它们的目标是复现性，把环境钉死是正确做法。意义在于，**钉死的环境是一个未声明坐标的点**，而没有坐标的点无法和另一个点比较。

---

## 3 强化学习基础设施里的环境：旋钮

训练 Agent 需要按批次创建成千上万个隔离的执行环境。这一层的代表是 DeepSeek 的 DSec [19]，以及 E2B、Modal、Daytona 等商用沙箱平台，还有 Firecracker 这样的底层虚拟化技术 [20]。我们同样逐一核对了它们暴露的环境参数，见表 B。

**表 B：沙箱与训练基础设施暴露的环境旋钮**

| 平台 | OS 选择 | 隔离级别 | 镜像 / 分层 | 网络策略 | 用户 / 权限 | GPU | locale | 是否定义"哪些旋钮改变正确解" |
|---|---|---|---|---|---|---|---|---|
| DSec [19] | Linux 基础镜像；Android 完整 VM | FnCall / 容器 / microVM / 完整 VM | 三层：基础镜像 / 工作区 / 工具包 | 按服务 allowlist（如 npm 禁、pypi 允） | init_user | FnCall GPU | 无 | 否 |
| E2B [21] | Linux | Firecracker microVM | 模板 | allow / deny 列表 | 无 | — | 无 | 否 |
| Modal [22] | Linux | gVisor；VM beta | Image | 三档出站策略 | 无 | 有 | 无 | 否 |
| Daytona [23] | Linux / Windows / macOS | 容器 / VM | 镜像须带 tag 或 digest | allowlist / blockAll / proxy | root | NVIDIA / AMD，至 8 卡 | 无 | 否 |
| OpenAI Code Interpreter [24] | — | VM | — | — | — | — | 无 | 否 |
| Firecracker [20] | 仅 Linux 客户机 | microVM | — | 设备级限速 | jailer | — | 无 | 否 |
| Prime Intellect verifiers / Harbor [25] | — | docker / prime / VM | 每题镜像 | no-network 或 allowlist | 求解器与验证器隔离 | — | 无 | 否 |

DSec 值得单独讨论，因为它是目前公开的最大规模的 Agent 训练沙箱平台：一个集群单元约 160 个节点，每天约 300 万个沙箱，峰值并发 38 万，每秒创建超过 5000 个 [19]。它的设计在三处触及了本文的主题。

其一，**镜像分层给出了"钉住"的工程形态**。DSec 把一个沙箱的内容分解为基础镜像（OS 与语言运行时）、工作区（任务代码与依赖）、工具包（如 DeepSeek Harness）三层，各自独立版本化。一周之内容器后端服务了 11,266 个基础镜像和 102,171 个工作区 [19]。这三层正好对应本文第六章钉住清单的三个 digest。

其二，**运行框架被明确当作一个独立的层**。Harness 作为工具包层存在，可以独立升级而不重建镜像。这为"Harness 是策略的一部分还是环境的一部分"提供了一个工程答案：它是可以单独钉住或单独变化的一层，取决于被测对象是谁。

其三，**论文记录了 Agent 通过非预期渠道获取答案的行为**：在沙箱内翻平台日志找残留答案、向内部套接字伪造请求、覆盖 /bin/bash 注入命令、扫描端口寻找可达的镜像站、通过 Go 模块代理拉取 GitHub 上的现成实现。论文的结论是"仅靠最终输出检查无法可靠地确定 Agent 是否按预期方式解决了任务" [19]。这一句是对"评测只看结果"最直接的一手证据，来自最大的训练方之一。但值得注意的是，论文把这些现象框定为 reward hacking 与安全问题，而不是"正确解随环境变化"。它的网络规则示例 network_rules={"npm": False, "pypi": True} 已经说明了网络可达性会改变 Agent 能走的路，只是没有人把这句话说出来。

产业侧的定义同样停在旋钮层。Epoch AI 基于 18 位从业者访谈给出的定义是"环境由模型可采取的动作集合，以及决定这些动作效果的周边上下文构成"，并承认"环境与任务的边界有些模糊" [26]。这是所有定义里唯一在逻辑上容许"环境依赖正确性"的一个，但随后的讨论把交付形式（"通常是 Docker 容器，但不总是"）当作次要细节，从未枚举因子。Mercor 的定义是"软件、任务、验证器"三件套 [27]；Scale AI 把 OS 写成"类 macOS 与 Windows 的操作系统环境" [28]，OS 在这里是被复刻的外观，不是会翻转答案的变量。

经典强化学习的环境抽象则有相反的盲区。Gymnasium 的 Env 接口只在 reset 时接受一个随机种子 [29]；Procgen 和 XLand 变化的是关卡布局与博弈规则 [30][31]，这确实改变最优策略，但发生在一个固定的模拟器内部。域随机化 [32] 随机化纹理、光照、相机位姿，恰恰是为了让模型对这些因子不变。

所以基础设施这一层的空缺可以精确地表述为：**旋钮存在，旋钮的语义不存在**。没有一家平台、一篇论文说"把 init_user 从 root 改成非 root，这道题的正确解会从系统 pip 变成 venv"。

---

## 4 机器学习里的环境：干扰，还是干预

机器学习的分布偏移与不变性研究大量使用"环境"一词，而且有严格的形式定义。梳理这条线的价值在于，它给出了一个和执行环境**方向相反**的准入判据，这个对比是本文提案最重要的概念基础。

**不变风险最小化（IRM）** 把环境定义为"在不同条件下测量同一对随机变量"所得的数据集索引 e，全部环境的集合"包含关于该变量系统的所有可能实验条件，无论可观测还是假想的" [33]。不变预测器的定义是"对所有环境同时最优的分类器"。**不变因果预测** 把环境定义为"未知且不精确控制的干预"所产生的实验设定，并明确规定"不允许对目标变量 Y 的干预" [34]。**因果表示学习** 进一步把分布写成因果机制的乘积，环境变化就是其中少数几个机制被替换，即"稀疏机制变动" [35]。

这三篇的共同点是：**一个合法的环境，是不改变正确预测器的**。环境准入的条件是"答案不变"，测量的是模型错误地随之变动了多少，也就是脆弱性。

鲁棒性 benchmark 遵循同一逻辑。ImageNet-C 用 15 类腐蚀乘 5 级强度构成 75 个格 [36]，腐蚀是保标签的；FormatSpread 研究提示词格式这一类"不应影响提示词解释"的特征，发现 24% 的原子改动带来至少 5 个点的准确率变化，最大 spread 达 76 个点 [37]。这些工作准入一个轴的理由是"答案不该随它变"。

执行环境的轴恰恰相反。操作系统从 Linux 换成 macOS，文件系统对文件名做 Unicode 归一，Agent 按自己输入的字节去找文件就找不到；正确解法结构性地变了。权限从 root 换成非 root 并锁定系统目录，装包路线从系统 pip 变成 venv；正确解法又变了。这些轴之所以值得测，正是因为**答案随之而变**。用因果的语言说，它们是干预了机制的环境，不是只干预了输入分布的环境。

于是我们得到本文最重要的一条区分：

> **干扰因子**：正确输出对其不变。准入理由是不变性。测量结果叫脆弱性。
> **改机制因子**：正确输出随其改变。准入理由是它改变了机制。测量结果叫正确性。

两类因子必须分开报告，混在一起会把"模型在不该变的地方变了"和"模型在该变的地方没变"算成同一个数。

机器学习这条线还提供了两个技术先例。一是**真正的全笛卡尔积只出现在合成数据**：dSprites 的六个生成因子共 737,280 种组合，"每种恰好出现一次" [38]；ImageNet-C 是 15 乘 5 的网格。这说明离散网格只在每格可确定性生成时才枚举，否则采样。二是**按轴报数是共识**：ImageNet-C 先算每类腐蚀的 CE，再平均成 mCE，并另报相对 CE 区分"优雅退化"与"干净误差低" [36]；DomainBed 的主表按域报 OOD 准确率 [39]；WILDS 报最坏群体而非均值 [40]；域随机化做去一因子消融 [32]。没有一篇只报总分。

---

## 5 软件工程里的配置空间：方法早已存在

如果说前三章找到的是"对象"，软件工程这一章找到的是"方法"。

**CI 矩阵就是笛卡尔积。** GitHub Actions 的文档写道："一个作业会为变量的每一种可能组合运行一次"，示例是三个语言版本乘两个操作系统等于六个作业，支持 include 与 exclude 修剪，上限 256 个作业 [41]。这是工业界对"环境是因子的积"的默认实践，也解释了为什么没有人跑全积。

**组合测试给出测量预算的理论。** NIST 对四个真实系统的故障分析发现，触发故障所需的交互条件数很小：医疗设备 66% 的故障只需一个条件、97% 两个以内；Mozilla 76.1% 两个以内、95.0% 三个以内；没有任何故障需要超过六个条件 [42]。这条"交互规则"意味着，两两覆盖数组对交互故障"实际上是穷尽的" [43]。JHipster 的研究把 2.6 万个配置全部构建测试了一遍，35.7% 失败，失败可归因于特征交互，而两两采样找到了其中大多数 [44]。性能影响模型进一步给出了函数形式：基项，加每个选项的单独影响，加稀疏的交互项 [45]。

**实验设计告诉我们一次一因子的边界。** Fisher 早在 1926 年就反对"一次只问自然一个问题" [46]。Morris 的基本效应法把随机化的一次一因子轨迹变成筛选设计：每个因子得到一个均值（总体影响）和一个标准差（非线性或与其他因子的交互） [47]。Saltelli 与 Annoni 给出几何证明：一次一因子的采样点全部落在单位立方体的内切超球内，三个因子时球占立方体积约 52%，因子数增加时迅速趋零，所以一次一因子在构造上看不到交互 [48]。

**经验 bug 研究告诉我们哪些轴该进、噪声底线在哪。** 一项 2026 年的研究跨操作系统重新执行了 500 个 Python 项目的测试，11.2% 的项目出现 OS 依赖的失败；在 151 个有文档化可移植问题的项目里，文件与目录类问题占 62 个，其中路径分隔符 34、文件锁 11、编码 9、换行符 6 [49]。对 Apache 项目测试代码 bug 的研究发现，环境类误报中 61% 是操作系统差异造成的平台特定失败，JDK 版本与厂商差异再占 26% [50]。日期时间 bug 的研究发现时区错误是最大的根因类别 [51]。Apple 的文件系统文档记载了 HFS+ 存储 NFD 归一形式而 APFS 保留原形式但按归一哈希查找的机制 [52]，这是 macOS 文件名 bug 的根源。

反过来，flaky 测试研究给出了警告。Luo 等发现 96% 的 flaky 测试与平台无关 [53]；Gruber 等在 2.2 万个 PyPI 项目中发现 28% 的 flaky 来自"基础设施"本身，要以 95% 置信度判定一个测试不 flaky 平均需要约 170 次重跑 [54]。这意味着，**大量表观的"环境效应"其实是非确定性**，在把一个格的差异归因到某根轴之前，必须先用重复运行把噪声分离出去。

**可复现构建给出"钉住"的操作定义。** Nix 把每个组件存放在由其全部输入的哈希决定的路径上，环境成为声明输入的纯函数 [55]；基于 Nix 历史的研究表明，从六年前的软件包集合重建约 1.4 万个包，成功率 99.94% [56]。对 17.8 万个 Dockerfile 的研究则发现普通仓库违反版本 pin 规则的频率是专家集合的五倍 [57]。这两组结果放在一起说明：只有其余坐标 bit-for-bit 钉死，一个环境坐标才是合法的实验因子；否则依赖漂移是每个格里的隐藏变量。

**表 C：四个领域对"环境"的用法对照**

| 领域 | 环境是什么 | 因子结构 | 准入判据 | 报数方式 |
|---|---|---|---|---|
| Agent benchmark | 钉死的容器或 VM 快照 | 无，常量 | 无 | 单一分数 |
| RL 基础设施 | 带旋钮的沙箱 | 旋钮清单，无语义 | 资源、安全、兼容 | 无 |
| 经典 RL | 模拟器 + 种子 / 关卡 | 关卡内容 | 无 | 泛化分数 |
| 域随机化 | 渲染与动力学参数区间 | 参数积，采样 | 答案对其不变 | 去一因子消融 |
| 不变性与因果 | 干预后的分布索引 | 机制乘积，稀疏变动 | 不得干预目标 | 最坏情形；假设检验 |
| 鲁棒性 benchmark | 保标签扰动 | 类型乘强度的网格 | 答案不该变 | 每轴误差再平均；spread |
| 合成因子数据集 | 生成因子 | 全笛卡尔积 | 生成因子 | 每因子解耦分 |
| 软件工程组合测试 | 配置参数 | 因子积 + 覆盖数组 | 交互规则 | t-way 覆盖；每因子基本效应 |
| **本文提案** | 策略之外能改变正确解的一切 | 有限轴的笛卡尔积，星形加两两覆盖 | 改变正确解（因果干预义） | 每轴方向导数 + 翻转率 + 失败签名；禁总分 |

---

## 6 提案：环境坐标空间

前四章的空缺可以归结为一句话：大家都有旋钮，没有人有坐标。本章给出一个坐标系。它由六部分组成：定义、轴的准入检验、因子与取值、格与钉住清单、测量协议、报数方式。

### 6.1 定义

**环境**是被测策略之外、能够改变正确解法轨迹的一切。它是无限维的，"测全环境"是伪命题。

**投影**是选取有限根轴进行观测。环境空间

E = A₁ × A₂ × … × Aₙ

其中每根轴 Aᵢ 是一个有限的、有名字的取值集合，并指定一个基准值 aᵢ⁰。基准格 e⁰ = (a₁⁰, …, aₙ⁰)。

**格**（cell）是空间里的一个坐标点 e，加上一份钉住清单 P(e)。坐标说明命了名的维度取什么值；钉住清单把没有命名的维度全部冻结在确定状态。**只有坐标不是格**：说"Windows"不是一个格，说"windows-2022 runner 镜像版本 X，注册表 HideFileExt=0，Harness 版本 Y"才是。

三点说明。第一，被测策略 π 是定义的显式参数。测模型时，运行框架属于环境；测运行框架时，它属于策略。同一个坐标系服务两种测量，只是 π 的边界不同。第二，轴之间要求正交：一根轴取值的改变不应被迫改变另一根轴的取值。做不到正交的组合（例如 Ubuntu 20.04 天然捆绑 Python 3.8）不作为轴，作为"轴外自然点"，用轴上的测量去分解。第三，选择笛卡尔积而不是一张清单，是为了得到三样东西：任意两格之间有明确定义的"差几步、差在哪根轴"，敏感度才能定义为方向导数；可以只测星形而不测全因子，因为交互项在积结构下有定义、可以事后补测；新轴加入时不动旧格，只给旧格补一个基准坐标。

### 6.2 轴的准入：四步检验

一根候选轴 A 能进入积，需要通过四步检验，每一步都是可执行的：

1. 存在任务 t，其正确解 s 在格 a 上通过。
2. 将 s 原样搬到格 b（b 与 a 只在 A 上不同），s 失败。
3. 格 b 上存在正确解 s′，并且 s′ 与 s 在**结构上**是不同的做法，而不只是同一做法写得更省。
4. 反向也成立：s′ 搬回格 a 也失败，或需要另一种做法。

第三步是关键。只满足"更省"而不满足"不同做法"的差异是预算差异，不是轨迹差异。CPU 核数、内存、磁盘配额、网速、时延、屏幕分辨率、显存大小都因此出局：它们改变的是完成任务的成本，不是完成任务的方法。这一步把"环境"与"性能"切开，也把本文的轴与第四章的干扰因子切开。

每根轴之下再分**接触面**，每个接触面配**机制**，每个机制配**装置层读数**。以操作系统轴为例，四个接触面是文件系统（大小写、Unicode 归一、非法名、尾点尾空格、路径长度、文件锁、可执行位）、进程与 shell（argv 转义、解释器名、PATH 查找、环境变量大小写、root）、编码区域时间（默认编码、换行、排序、时钟）、桌面惯例（编辑器保存的是否是输入的字、新建文档是否纯文本、文件名显示是否真名）。读数是标准的一部分：一个格声称在某轴上与基准格不同，必须有读数证明它真的不同，不能从分数反推。

### 6.3 因子与取值

按上述检验，第一版共五组 22 个因子 75 个取值。表 D 给出全部，* 为基准值。每个非基准取值都附有机制依据（第五章的经验 bug 研究、第三章的基础设施参数），但取值是否最终进入核心，取决于是否有任务在它上面通过第 6.5 节的两道门。

**表 D：环境空间 v0.2**

| 组 | 因子 | 取值 | 排除的近邻旋钮（预算类） |
|---|---|---|---|
| 硬件 | arch | x86_64 * / arm64 | CPU 核数 |
| 硬件 | accel | none * / nvidia / amd-rocm / apple-metal | 显存大小 |
| 硬件 | toolkit | matched * / driver-only / major-mismatch | |
| 硬件 | compute-cap | current * / old | |
| 硬件 | gpu-count | single * / multi | 独占 / 共享模式 |
| 系统 | os | linux * / macos / windows / android | 发行版与版本（钉住） |
| 系统 | fs | case-sensitive * / case-insensitive / unicode-normalizing | 磁盘配额 |
| 系统 | isolation | container * / microvm / vm / bare | |
| 系统 | perm | root * / sudo-nopasswd / non-root / non-root+readonly-sys / restricted-caps | |
| 系统 | mount | normal * / tmp-noexec | |
| 运行时栈 | stack-version | current * / old | 相对任务声明的栈 |
| 运行时栈 | entry-name | canonical * / alias-missing | 相对任务声明的栈 |
| 运行时栈 | build-tools | present * / absent | 相对任务声明的栈 |
| 运行时栈 | toolchain | gnu * / busybox / bsd | |
| 运行时栈 | shell | bash * / dash / zsh / powershell / cmd | |
| 运行时栈 | browser-engine | chromium * / firefox / webkit | 仅网页类任务 |
| 策略可见面 | channel | terminal * / gui / a11y-tree / web-dom | 屏幕分辨率 |
| 策略可见面 | tty | tty * / no-tty | 终端列数 |
| 外部世界 | net | online * / offline / allowlist / proxy-required / ipv6-only | 网速、时延 |
| 外部世界 | locale | C.UTF-8 * / C / en_US.UTF-8 / de_DE.UTF-8 / tr_TR.UTF-8 / zh_CN.GBK / cp1252 | |
| 外部世界 | tz | UTC * / Asia/Shanghai / Europe/Berlin / Asia/Kolkata | |
| 外部世界 | clock | normal * / future+1y / past-1y / frozen | |

统计：22 个因子，75 个取值。全因子约 10¹⁰ 量级，只定义不跑。

三条配套规则。**值集合按任务参数化**：运行时栈组的取值相对于任务声明的技术栈解释，"current / old"对 Python 任务是 3.12 对 3.8，对 Node 任务是 22 对 18，对 CUDA 任务是 12 对 11。**基准格按任务族定义**：GPU 任务从 accel=nvidia、toolkit=matched 出发，普通任务从 accel=none 出发；星形设计不变，只是原点不同。**取值集合封闭核心、开放扩展**：一个候选值要有至少一道任务在它上面通过门一门二并带装置读数，才升为核心；新因子同理。"全不全"因此不是一个人拍板的事，而是有任务就进、没任务就在候选区等待。

### 6.4 格与钉住清单

钉住清单 P(e) 至少包括：镜像或快照的内容 digest、发行版与版本、runner 镜像版本、系统设置的实际导出值（注册表、gsettings、defaults）、被测策略之外所有工具的版本、运行框架版本、模型版本。DSec 的三层镜像（基础镜像、工作区、工具包）给了一个现成的分层方式，每层一个 digest [19]。

格的身份 = 坐标串 + 钉住清单哈希，例如：

```
os=linux; fs=case-sensitive; channel=terminal; shell=bash; perm=root;
locale=C.UTF-8; tz=UTC; net=online; … | pin=sha256:…
```

同一坐标、不同 pin，是两个格。这条规则的依据是第五章：只有其余坐标 bit-for-bit 钉死，一个坐标才是合法的实验因子 [55][56]。

### 6.5 测量协议：星形加两两覆盖

任务集 T 与环境空间 E 独立定义，实际测量的是 T × E 的一个子集。任务的准入有两条门：

- **门一**：参考解在所有相关格上全部通过。这证明每个格上都存在正确路线，失败不是格本身不可解。
- **门二**：朴素解只在靶子格上失败，在对照格上通过。这证明任务与该轴有真实接触面。

两门都过，任务才进入正式集。原则是**先有轴再造题**：给旧题硬配轴，必然滑向预算轴。

测量分三层，预算由第五章的理论决定：

1. **星形**：基准格加上沿每根轴走一步，共 1 + Σ(|Aᵢ| − 1) 个格。对表 D，这是 54 个格。这一层就是 Morris 的基本效应 [47]，给出每根轴的主效应。
2. **两两覆盖数组**：NIST 的交互规则说 70% 到 93% 的故障只需两个以内的条件触发 [42]，所以第二层预算是 2-way 覆盖，而不是任意挑选的轴对。星形在构造上看不到交互 [48]，这一层补上。
3. **轴外自然点**：两三个真实存在但不正交的配置（如 Ubuntu 20.04 捆绑 Python 3.8），用前两层的测量去分解。

**重复运行是协议的一部分**，不是可选项。第五章的 flaky 研究说明大量表观环境效应是非确定性 [53][54]，Gruber 等给出的数字是以 95% 置信度判定一个测试不 flaky 平均需要约 170 次重跑。每个格至少重复 n 次，先分离噪声，再归因到轴。

### 6.6 报数：方向导数，禁止总分

对每个被测策略 m 和每根轴 i，报两个数：

- **方向导数** Δᵢ(m) = 基准格通过率 − 沿轴 i 走一步的通过率。
- **翻转率**：同一任务在两格结果不同的比例。

交互项 Δᵢⱼ − Δᵢ − Δⱼ 只在覆盖数组选定的轴对上报告。

**禁止总分。**"Linux 好于 macOS 好于 Windows"这类排序是靶子分布的产物：一个 benchmark 里 Linux 得分高，可能只是因为多数任务的靶子落在 macOS 和 Windows 上；另一个 benchmark 里 Windows 得分最高，可能只是因为选了 Windows 应用。总分把靶子分布和策略能力混在一起，没有可比性。这与第四章的共识一致：ImageNet-C、DomainBed、WILDS 都先按轴报 [36][39][40]。

报数还要**按接触面报**，并附上"对照格持平"的健康检查：如果一个策略在对照格上的通过率明显低于其他策略，那么它在靶子格上的下降不能全部归因于轴。

### 6.7 失败签名与归因

每条判据挂一条"被测策略写死了什么假设"。挂掉的判据集合就是这次失败的**签名**。签名按策略汇总，得到每个策略的**假设画像**：它在哪些机制上写死了哪些假设。这是这套标准最有价值的输出，因为它直接告诉训练方要修什么。

归因遵循三问，三问全是才归因为"写死了假设 X"：

1. 环境在该轴上真的不同吗？看装置读数。
2. 策略的动作真的依赖了该假设吗？看轨迹，人读。
3. 同格存在正确路线吗？看门一，参考解通过。

第二问不成立是常见情况：例如任务要求按名字找文件，而 Agent 通过图形界面的文件对话框直接选中了它，文件名查找机制根本没被触发。这不是环境效应，是干净的负结果，应当如实报告。

---

## 7 把提案套到现有基础设施上


第三章的表 B 显示基础设施暴露了旋钮但没有语义。表 E 把 DSec 的沙箱参数逐一映射到本文的轴，说明这些轴在生产系统里是真实存在的旋钮，提案只是给它们补上语义：

**表 E：DSec 参数与环境轴的对应**

| DSec 参数或机制 [19] | 对应的轴或钉住项 | 语义空缺 |
|---|---|---|
| 四种后端（FnCall / 容器 / microVM / 完整 VM） | isolation | 论文说"调用方自己负责选择后端"，未定义哪些任务的正确解依赖隔离级别 |
| network_rules={"npm": False, "pypi": True} | net=allowlist | 示例已隐含"网络可达性改变可走的路"，未明说 |
| init_user="root" | perm | 只作为安全设置 |
| 基础镜像（Ubuntu、Python 3.10、Java 8） | os + stack-version | 作为兼容性设置 |
| 工作区 / 工具包分层 | 钉住清单的三个 digest | 作为维护成本优化 |
| Android 完整 VM | os=android | 作为工作负载类别 |
| FnCall GPU 独占 / 共享 | 排除项（预算类） | 正确地未当作轴 |
| 第 6.4 节的非预期渠道取答案 | 门二失败的一种形态 | 被框定为 reward hacking |

这张表的含义是：**基建层已经有了坐标系需要的全部旋钮，缺的只是语义层**。一个标准如果只定义语义而不要求新的基建，采用成本就低。

---

## 8 开放问题

**被测对象的边界。** 6.1 把策略 π 写成显式参数，但 Harness 与模型的边界在实践中并不清晰：模型的系统提示词属于谁？Harness 的上下文压缩策略属于谁？我们目前的做法是按测量目标划定，测模型时 Harness 钉住，测 Harness 时模型钉住。是否存在一个不依赖测量目标的划分，尚无答案。

**观测通道是轴还是任务的表示。** 终端与 GUI 交付物相同、题面只改一句，看起来是同一任务的两种投影；但通道改变的是策略能看见什么、能做什么，这又符合"策略之外"的定义。本文暂将其作为轴，理由是 GUI 上的正确解与终端上的正确解在结构上不同，符合四步检验的第三步。

**取值集合的封闭性。** 封闭才有可比性，开放才能生长。本文采用"封闭核心加提案扩展"，但核心的第一版由谁定、以什么程序修订，是标准化工作而非研究工作。

**交互项的预算。** 两两覆盖数组在 22 个因子 75 个取值上仍然可观。NIST 的交互规则来自传统软件，Agent 的失败是否同样以低阶交互为主，需要实证。如果高阶交互显著，第 6.5 的三层预算要重新设计。

**造题成本。** 每根轴每个取值至少要一道过门一门二的任务，而门一要求参考解在所有相关格上通过。硬件组（GPU、CUDA 版本、算力代际）的任务尤其昂贵。这是这套标准推广的主要瓶颈，也是它需要社区协作的原因。

**Harness 作为环境。** DSec 把 Harness 做成独立的工具包层 [19]，而另一些评测工作把 Harness 本身作为被测对象。当 Harness 既可以是策略也可以是环境时，第 6.1 的参数化能否覆盖"Harness 与环境的交互"，例如 Harness 的工具结果截断策略与 no-tty 轴的交互，尚未验证。

---

## 9 结论

"环境"这个词被四个社区以四种不兼容的方式使用，而所有用法都绕开了同一个问题：哪些环境因素会改变一道任务的正确解。本文把环境定义为策略之外能改变正确解的一切，把它投影到有限根过得了四步检验的轴上，形成一个笛卡尔积坐标空间；用软件工程的组合测试理论确定测量预算（星形加两两覆盖），用机器学习的按轴报数惯例确定报数方式（方向导数与翻转率，禁止总分），用因果推断的干预概念区分"改变正确解的轴"与"答案不该变的干扰"。第一版空间有五组 22 个因子 75 个取值，每个取值附有来自经验 bug 研究或生产基础设施参数的机制依据，是否进入核心取决于是否有任务通过两道准入门。

这个框架的采用成本很低：基础设施层已经有了全部旋钮，缺的只是给旋钮以语义。我们希望它成为 Agent 评测报告的一个必填项：不是"我们在一个可复现的环境里测了"，而是"我们在坐标为 e、钉住清单为 P(e) 的格里测了，沿以下轴的方向导数如下"。

---

## 参考文献

（编号对应正文；每条均已打开原文核对，URL 为实际打开的页面。）

**Agent benchmark**
[1] Jimenez et al. SWE-bench: Can Language Models Resolve Real-World GitHub Issues? ICLR 2024. arXiv:2310.06770. https://arxiv.org/abs/2310.06770 ; README: https://github.com/swe-bench/SWE-bench
[2] SWE-bench Verified. https://www.swebench.com/verified.html ; Epoch AI 复现说明 https://epoch.ai/benchmarks/swe-bench-verified
[3] Yang et al. SWE-bench Multimodal. arXiv:2410.03859. https://arxiv.org/abs/2410.03859
[4] Merrill et al. Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces. arXiv:2601.11868. https://arxiv.org/abs/2601.11868
[5] Xie et al. OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments. NeurIPS 2024 D&B. arXiv:2404.07972. https://arxiv.org/abs/2404.07972
[6] XLANG Lab. OSWorld-Verified. 2025-07-28. https://xlang.ai/blog/osworld-verified
[7] Zhou et al. WebArena: A Realistic Web Environment for Building Autonomous Agents. arXiv:2307.13854. https://arxiv.org/abs/2307.13854
[8] Koh et al. VisualWebArena. ACL 2024. arXiv:2401.13649. https://arxiv.org/abs/2401.13649
[9] Liu et al. AgentBench: Evaluating LLMs as Agents. ICLR 2024. arXiv:2308.03688. https://arxiv.org/abs/2308.03688
[10] Yao et al. τ-bench. arXiv:2406.12045. https://arxiv.org/abs/2406.12045
[11] Mialon et al. GAIA: a benchmark for General AI Assistants. arXiv:2311.12983. https://arxiv.org/abs/2311.12983
[12] Chan et al. MLE-bench. ICLR 2025. arXiv:2410.07095. https://arxiv.org/abs/2410.07095
[13] Bonatti et al. Windows Agent Arena. arXiv:2409.08264. https://arxiv.org/abs/2409.08264
[14] Rawles et al. AndroidWorld. arXiv:2405.14573. https://arxiv.org/abs/2405.14573
[15] Trivedi et al. AppWorld. ACL 2024. arXiv:2407.18901. https://arxiv.org/abs/2407.18901
[16] Xu et al. TheAgentCompany. arXiv:2412.14161. https://arxiv.org/abs/2412.14161
[17] Muryn et al. MacArena: Benchmarking Computer Use Agents on an Online macOS Environment. AIWILD@ICML 2026. arXiv:2606.06560. https://arxiv.org/abs/2606.06560
[18] Yang et al. macOSWorld: A Multilingual Interactive Benchmark for GUI Agents. arXiv:2506.04135. https://arxiv.org/abs/2506.04135

**RL 基础设施与产业**
[19] Huang et al. DeepSeek Elastic Compute (DSec): A Sandbox Infrastructure for Effective Agentic Training at Scale. arXiv:2609.22978. https://arxiv.org/abs/2609.22978
[20] Agache et al. Firecracker: Lightweight Virtualization for Serverless Applications. NSDI 2020. https://www.usenix.org/conference/nsdi20/presentation/agache
[21] E2B 文档. https://docs.e2b.dev/ ; https://github.com/e2b-dev/infra
[22] Modal Sandboxes 文档. https://modal.com/docs/guide/sandbox
[23] Daytona 文档. https://www.daytona.io/docs/en/sandboxes/
[24] OpenAI Code Interpreter 文档. https://developers.openai.com/api/docs/guides/tools-code-interpreter
[25] Prime Intellect. verifiers 库文档；Environments Hub（2025-08-27）. https://github.com/PrimeIntellect-ai/verifiers ; https://www.primeintellect.ai/blog/environments
[26] Denain & Barber. An FAQ on Reinforcement Learning Environments. Epoch AI, 2026-01-12. https://epoch.ai/gradient-updates/state-of-rl-envs
[27] Foody. Mercor to acquire Deeptune. 2026-07-09. https://www.mercor.com/blog/mercor-to-acquire-deeptune/
[28] Scale AI. Reinforcement Learning Environments for AI Agents. https://scale.com/rlenvironments
[29] Farama Foundation. Gymnasium Env API. https://gymnasium.farama.org/api/env/
[30] Cobbe et al. Leveraging Procedural Generation to Benchmark Reinforcement Learning. arXiv:1912.01588. https://arxiv.org/abs/1912.01588
[31] Open Ended Learning Team. Open-Ended Learning Leads to Generally Capable Agents. arXiv:2107.12808. https://arxiv.org/abs/2107.12808
[32] Tobin et al. Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World. IROS 2017. arXiv:1703.06907. https://arxiv.org/abs/1703.06907

**机器学习：不变性、因果、鲁棒性**
[33] Arjovsky, Bottou, Gulrajani, Lopez-Paz. Invariant Risk Minimization. arXiv:1907.02893. https://arxiv.org/abs/1907.02893
[34] Peters, Bühlmann, Meinshausen. Causal inference by using invariant prediction. JRSS-B 78(5), 2016. arXiv:1501.01332. https://arxiv.org/abs/1501.01332
[35] Schölkopf et al. Toward Causal Representation Learning. Proc. IEEE 109(5), 2021. arXiv:2102.11107. https://arxiv.org/abs/2102.11107
[36] Hendrycks & Dietterich. Benchmarking Neural Network Robustness to Common Corruptions and Perturbations. ICLR 2019. arXiv:1903.12261. https://arxiv.org/abs/1903.12261
[37] Sclar, Choi, Tsvetkov, Suhr. Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design. ICLR 2024. arXiv:2310.11324. https://arxiv.org/abs/2310.11324
[38] Matthey et al. dSprites: Disentanglement testing Sprites dataset. DeepMind 2017. https://github.com/google-deepmind/dsprites-dataset
[39] Gulrajani & Lopez-Paz. In Search of Lost Domain Generalization. ICLR 2021. arXiv:2007.01434. https://arxiv.org/abs/2007.01434
[40] Koh et al. WILDS: A Benchmark of in-the-Wild Distribution Shifts. ICML 2021. arXiv:2012.07421. https://arxiv.org/abs/2012.07421

**软件工程：组合测试、配置空间、跨平台 bug、可复现**
[41] GitHub Docs. Running variations of jobs in a workflow. https://docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs
[42] Kuhn, Wallace, Gallo. Software Fault Interactions and Implications for Software Testing. IEEE TSE 30(6), 2004. https://csrc.nist.gov/pubs/journal/2004/06/software-fault-interactions-and-implications-for-s/final
[43] Kuhn, Kacker, Lei. Practical Combinatorial Testing. NIST SP 800-142, 2010. https://csrc.nist.gov/pubs/sp/800/142/final
[44] Halin et al. Test them all, is it worth it? Assessing configuration sampling on the JHipster Web development stack. EMSE 24(2), 2019. arXiv:1710.07980. https://arxiv.org/abs/1710.07980
[45] Siegmund, Grebhahn, Apel, Kästner. Performance-Influence Models for Highly Configurable Systems. ESEC/FSE 2015. http://www.cs.cmu.edu/~ckaestne/pdf/fse15_influence.pdf
[46] Fisher. The Design of Experiments. 1935；The arrangement of field experiments. 1926.
[47] Morris. Factorial Sampling Plans for Preliminary Computational Experiments. Technometrics 33(2), 1991.
[48] Saltelli & Annoni. How to avoid a perfunctory sensitivity analysis. Environmental Modelling & Software 25(12), 2010. https://www.nusap.net/spe/Saltelli_and_Annoni_2010.pdf
[49] Silva, Farahat, d'Amorim. An Empirical Analysis of Cross-OS Portability Issues in Python Projects. MSR 2026. arXiv:2609.25531. https://arxiv.org/html/2609.25531
[50] Vahabzadeh, Milani Fard, Mesbah. An Empirical Study of Bugs in Test Code. ICSME 2015. https://people.ece.ubc.ca/amesbah/resources/papers/icsme15.pdf
[51] Tiwari et al. It's About Time: An Empirical Study of Date and Time Bugs in Open-Source Python Software. MSR 2025. https://2025.msrconf.org/details/msr-2025-technical-papers/35/
[52] Apple. Apple File System Guide, FAQ. https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/APFS_Guide/FAQ/FAQ.html
[53] Luo, Hariri, Eloussi, Marinov. An Empirical Analysis of Flaky Tests. FSE 2014. https://mir.cs.illinois.edu/lamyaa/publications/fse14.pdf
[54] Gruber, Lukasczyk, Kroiss, Fraser. An Empirical Study of Flaky Tests in Python. ICST 2021. arXiv:2101.09077. https://arxiv.org/abs/2101.09077
[55] Dolstra, de Jonge, Visser. Nix: A Safe and Policy-Free System for Software Deployment. LISA 2004. https://www.usenix.org/conference/lisa-04/nix-safe-and-policy-free-system-software-deployment
[56] Malka, Zacchiroli, Zimmermann. Reproducibility of Build Environments through Space and Time. ICSE 2024 NIER. arXiv:2402.00424. https://arxiv.org/abs/2402.00424
[57] Henkel, Bird, Lahiri, Reps. Learning from, Understanding, and Supporting DevOps Artifacts for Docker. ICSE 2020. https://pages.cs.wisc.edu/~jjhenkel/papers/icse20-docker.pdf

---

## 附录 A：轴的规格书样板（操作系统轴）

| 接触面 | 机制 | 装置层读数 | 典型差异（公开的系统行为） |
|---|---|---|---|
| 文件系统 | 大小写敏感 | 创建 a.txt 后读 A.txt 是否成功 | Linux 默认敏感；macOS、Windows 默认不敏感 |
| 文件系统 | Unicode 归一 | 以 NFC 名创建，列目录得到的字节 | macOS：HFS+ 存 NFD，APFS 按归一哈希查找 [52] |
| 文件系统 | 非法字符、尾点尾空格、路径长度 | 创建含 `:`、尾空格、260+ 字符路径的返回码 | Windows 拒绝 |
| 文件系统 | 文件锁、可执行位 | 打开中删除；chmod +x 后能否执行 | Windows 打开中的文件不可删除；NTFS 无 POSIX 执行位 |
| 进程与 shell | argv 转义 | 含空格与引号的参数回显 | Windows 上 CreateProcess 的命令行字符串与 POSIX argv 语义不同 |
| 进程与 shell | 解释器名、PATH 查找 | `which python` / `python3`；PATHEXT | Ubuntu 默认只有 `python3`；Windows 用 PATHEXT 解析可执行后缀 |
| 编码区域时间 | 默认编码、换行 | `open()` 默认编码；`echo` 换行字节 | Windows 传统代码页（如 cp1252）与 CRLF |
| 编码区域时间 | 排序、时钟 | `sort` 与 `ls` 顺序；`date` 输出 | locale 依赖 |
| 桌面惯例 | 编辑器保存内容、新建文档格式、文件名显示 | gsettings / defaults / 注册表导出 | Windows 资源管理器默认隐藏已知扩展名，服务器版镜像可能不同 |

其余 21 个因子的规格书按同一格式编写：每个取值至少一个机制，每个机制一条装置读数。
