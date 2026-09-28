# 环境维度轴（定稿草案 v1，2026-09-28）

> 本文替换上一版因子表（v0.2，5 组 22 因子）与中文综述 v3.0。旧版在仓库的 git 历史里。

本文件回答一件事：**AI agent 的执行环境由哪些维度构成，每根维度取哪些值。**
它对应 harness 综述里"harness 由哪些维度构成"的那张表。harness 综述定义了 (agent, harness, environment) 三元组的第二项，这里定义第三项。

## 结构一览

四级：**层 → 维度 → 子维度 → 取值**，每个非基准取值要配一条装置读数。

| 级 | 数量 | 定死的程度 |
|---|---|---|
| 层 | 7 | 定死。按三道判定题划分，第 1 节 |
| 维度 | 26 | 定死。每个维度是一个"接触面" |
| 子维度 | 53（核心 43，候选 10） | 核心定死；候选按证据升降 |
| 取值 | 每个子维度 2–7 个 | 开放。新取值走准入检验 |

**核心**＝至少一条一手记录同时满足"基准做法在该取值下失败"和"该取值下正确做法结构上不同"；**候选**＝只有失败记录，或失败多是 harness 自身的问题。

---

## 0 依据

五路调研，每一条都打开原文核对过：

| 证据 | 规模 | 用来做什么 |
|---|---|---|
| harness 综述四篇：Li（ETCLOVG）、Meng（ETCSLV）、Guo（六组件）、Zhang（ETCSOVG） | 全文 | 对齐体例 |
| 其他领域的环境分层模型：Apptainer、12-factor、OCI runtime spec、POSIX 第 7–8 章、Nix/Guix、ReproZip、CodeMeta、RO-Crate、ISO/IEC/IEEE 29119、feature model、binding-time 文献、POMDP、Sutton & Barto | 20 个来源 | 定分层原则 |
| 16 个沙箱与执行平台的配置参数：E2B、Modal、Daytona、Runloop、Morph、Fly、Codex、Claude Code、devcontainer、OCI image、Kubernetes、Firecracker、gVisor、GitHub Actions、Harbor、OpenEnv；外加 DSec | 约 300 个参数名 | 自下而上收集候选、检验完备性 |
| 16 个 benchmark 与训练环境声明的环境属性：SWE-bench、SWE-Gym、R2E-Gym、SWE-bench-Live、Terminal-Bench 2/Harbor、OSWorld、Windows Agent Arena、macOSWorld、AndroidWorld/AndroidEnv、WebArena/BrowserGym、AppWorld、τ/τ²-bench、GEM、MLE-bench、OpenApps、Gaia2/ARE | 代码与配置原文 | 找出"有人当自变量变过"的属性 |
| agent 因环境失败的一手记录：Claude Code、Codex、Gemini CLI、OpenHands、SWE-agent、Cline、browser-use、cua 等的 issue；AI 编码工具 bug 研究（3,864 条）；GUI 扰动研究 | 约 50 条 issue + 4 篇论文 | 每个子维度的准入证据 |

**从 harness 综述学到的三条体例。**
1. 分层按工程面或运行职责，承认层之间有依赖。Li 等明说七层"应读成依赖结构，而不是清单"。本文的 7 层也是栈，下层约束上层。
2. 要有一张"每个维度填具体值"的卡片。四篇里只有 Zhang 的 Harness Card 做到了；本文第 6 节的环境卡片沿用这种形式。
3. 四篇都没有按维度区分"改变结果"和"只影响成本"。本文每个子维度先过准入检验，只影响成本的进第 5 节排除清单。

---

## 1 分层原则：三道判定题

| 判定题 | 回答 | 来源 |
|---|---|---|
| **谁能改它** | 基础设施方 / 镜像构建者 / 启动者 / 沙箱方 / 出题方 / 其他行动者 / agent 自己的动作 | Sutton & Barto："anything that cannot be changed arbitrarily by the agent is … part of its environment"；protection ring |
| **改它要重建什么** | 换机器 / 重建镜像 / 重建容器 / 只重启进程 / 只 reset | Apptainer build 与 runtime；12-factor build / release / run；binding-time 的 compile / load / run |
| **它在 agent 第一个动作之前定死，还是之后会变** | 配置类（动作前定死）/ 状态类（动作或时间会改变它） | POMDP 的 T₀ 与 T；ReproZip 的读与写；29119 把环境状态列为前置条件 |

"是什么东西"不是分层依据。同样是"文件"：系统库在软件栈层，挂载可见性在边界层，工作区残留在状态层。同样是"时间"：时区在执行上下文层（改变解读），时钟偏移在边界层（改变证书是否有效），时间推进方式在状态层（改变世界是否在 agent 思考时变化）。按施加时点和改动者分，每个取值落在唯一一层。

---

## 2 七层

| 层 | 名称 | 谁能改 | 改它要重建什么 | 生效时点 | 这一层变了，改变的是什么 |
|---|---|---|---|---|---|
| **E1** | 平台层 | 基础设施方 | 换机器或虚拟硬件 | provision | 哪些二进制能运行、有没有加速器 |
| **E2** | 系统层 | 基础设施方 / 沙箱方 | 换 OS 镜像或隔离后端 | 创建沙箱 | 系统调用、路径与文件名的语义、系统能力 |
| **E3** | 软件栈层 | 镜像构建者 | 重建镜像 | build | 有哪些程序、什么版本、从哪里装 |
| **E4** | 执行上下文层 | 启动者（harness / 运维） | 只重启进程 | 进程启动 | **同一个动作被怎么解读** |
| **E5** | 边界层 | 沙箱方 | 重建容器，不必重建镜像；可按阶段改 | 创建容器 | **哪些动作可行、哪些资源可达** |
| **E6** | 状态层 | 出题方设初值；**agent 的动作、时间和其他行动者会改变它** | 只需 reset | 动作前定初值，之后演化 | 起点在哪、世界处于哪个时点、谁还在里面行动 |
| **E7** | 界面层 | 操作系统与应用 | 换显示或输入配置 | 每一步都经过它 | agent 看到什么、怎么输入（仅 GUI 与浏览器任务） |

**不属于环境的两样东西。**
- **harness**：工具定义、上下文管理、重试、截断、步数上限。由 harness 卡片声明。测模型时要钉住，但它不是环境的一层：harness 是环境与策略之间可移动的那条线，测模型时它属于钉住项，测 harness 时它属于策略。
- **评判与预算**：grader、奖励、终止条件、超时。属于任务或评测协议。

---

## 3 维度表

每行一个子维度。"平台参数"说明它在真实平台上可施加；"有人当自变量变过"标 ★。

### E1 平台层

| 维度 | 子维度 | 取值（* 基准） | 准入 | 平台参数 / 被当自变量 | 一手证据 |
|---|---|---|---|---|---|
| **E1.1 CPU 架构** | arch | x86_64 * / arm64 / riscv64 / 跨架构模拟 | 核心 | Runloop `architecture`；SWE-bench `ImageSpec.arch`（amd64 / arm64） | claude-code#84749：Apple Silicon 上跑 amd64 容器，Rosetta 丢掉 argv[0]，靠 argv[0] 分派的做法不成立；OpenHands#17470：aarch64 下 SIGILL，须设 `OPENSSL_armcap=0`；Build-bench 268 个跨架构构建失败 |
| **E1.2 加速器** | accel 类型 | none * / nvidia / amd-rocm / apple-metal / virtual-gpu | 核心 | Modal `gpu`；Harbor `gpus`、`gpu_types`；DSec virtio-gpu；★ MLE-bench 只用 CPU / 1 GPU / 2 GPU | [准入案例表](validity-admission-cases.md) 硬件组；codex#19676 |
| | 驱动与 CUDA | matched * / driver-only / major-mismatch | 核心 | — | DL 依赖栈研究：版本不兼容 70.0% |
| | 算力代际 | current * / old | 核心 | — | [准入案例表](validity-admission-cases.md) |
| | 数量 | single * / multi | 核心 | Modal `"H100:8"` | [准入案例表](validity-admission-cases.md)；MLE-bench：agent 从未尝试用第二块 GPU |

### E2 系统层

| 维度 | 子维度 | 取值 | 准入 | 平台参数 / 被当自变量 | 一手证据 |
|---|---|---|---|---|---|
| **E2.1 OS 家族** | os | linux * / macos / windows / android | 核心 | Daytona `sandbox_class`；Harbor `environment.os`；SWE-bench-Live `--platform`；★ AndroidWorld 两个设备与系统版本 | codex#413：模型以为在 WSL，在 PowerShell 里跑 Linux 命令；claude-code#4928：Windows 上写出真文件 `nul` |
| **E2.2 隔离方式** | isolation | container * / microvm / vm / gvisor / os-sandbox / wsl / bare | 核心 | Modal `vm_runtime`；Harbor 30 种后端；OSWorld 12 种 provider | Modal 文档：loop mount 与 dockerd 只在 VM 下可用；OpenHands#8590；SWE-bench-Live："docker does not guarantee full isolation" |
| **E2.3 文件系统语义** | 大小写 | sensitive * / insensitive | 核心 | ext4 casefold、APFS 大小写可选 | claude-code#90524：APFS 上只改大小写的重命名要分两步；FAST'23 大小写冲突研究 |
| | Unicode 归一 | none * / nfd-normalizing | 核心 | — | claude-code#87822：NFC 与 NFD 路径不一致导致会话丢失 |
| | 长度上限 | long * / win-max-path-260 / name-255-bytes | 核心 | Windows `LongPathsEnabled` | codex#36768：MAX_PATH 须 `\\?\` 前缀；Linux ext4 文件名上限 255 字节（多字节字符约 85 个） |
| | 保留名与尾部字符 | posix * / win-reserved | 核心 | — | claude-code#4928：Windows 上写出真文件 `nul`，只能用 `\\?\` 前缀删除；Win32 路径规范化会去掉尾点与尾空格 |
| | 符号链接 | resolved * / symlink-to-other-fs | 核心 | — | codex#43838：经软链 apply_patch 失败，须先解析真实路径 |
| **E2.4 系统约定** | 换行 | lf * / crlf | 核心 | — | claude-code#56946、#89307、#88114：CRLF 文件上编辑出错，须检测并保留换行 |
| | 路径分隔符 | slash * / backslash | 核心 | — | 清单与配置里写死的反斜杠路径在 Linux 与 macOS 上被当成文件名的一部分；OSWorld 与 Windows Agent Arena 分别维护两套路径 |
| **E2.5 内核与设备能力** | kernel-caps | full * / no-nested-virt / no-fuse / no-loop-mount | 候选 | Daytona `kvm`；Morph FUSE；GitHub Actions `ubuntu-slim` | 平台文档；agent 层记录未找到 |

### E3 软件栈层

| 维度 | 子维度 | 取值 | 准入 | 平台参数 / 被当自变量 | 一手证据 |
|---|---|---|---|---|---|
| **E3.1 语言运行时** | 版本 | current * / old / future（相对任务声明的栈） | 核心 | Modal `python_version`；SWE-bench 按实例 specs | SWE-agent#1179；RustEvo²：训练截止后的 API 32.5% vs 之前 56.1% |
| | 入口名 | canonical * / alias-missing | 核心 | — | [准入案例表](validity-admission-cases.md) |
| **E3.2 依赖与包** | 预装情况 | present * / absent / partial | 核心 | E2B `apt_install`；Codex setup script；DSec 工作区层 | OpenHands#12765：没有 JDK，agent 反复 `pip3 install openjdk` 卡死；Jupyter 研究只有 24.11% 能跑完 |
| | 包来源 | public-registry * / internal-mirror / unreachable | 核心 | DSec 按镜像服务放行 | hermes-agent#123132：lockfile 写死公网 registry，只能访问内部镜像时须改写 lockfile；DSec §6.4 agent 扫端口找镜像 |
| | 编译工具 | present * / absent | 核心 | — | [准入案例表](validity-admission-cases.md)；Jupyter 研究 8.73% |
| **E3.3 系统工具** | 工具实现 | gnu * / bsd / busybox | 核心 | — | claude-code#95705：BSD 上 `sed -i` 静默成功却多出备份文件；claude-code#79862：BusyBox 没有 printenv |
| | shell | bash * / sh-dash / zsh / fish / powershell-5 / powershell-7 / cmd | 核心 | GitHub Actions `defaults.run.shell`；SWE-bench-Live Windows 用 PowerShell | cline#346、gemini-cli#20773、kilocode#700：PowerShell 5.1 不认 `&&` |
| **E3.4 浏览器引擎** | browser-engine | chromium * / firefox / webkit | 核心（webkit 候选） | WebArena `playwright==1.32.1`；BrowserGym `playwright==1.44` | [准入案例表](validity-admission-cases.md) |

### E4 执行上下文层

这一层改变的是**同一个动作被怎么解读**：命令能执行，但输入输出的含义变了。

| 维度 | 子维度 | 取值 | 准入 | 平台参数 / 被当自变量 | 一手证据 |
|---|---|---|---|---|---|
| **E4.1 区域** | 默认编码 | utf-8 * / cp1252 / gbk / cp950 | 核心 | SWE-bench-Live Windows 建议 `PYTHONUTF8=1` | claude-code#56946：Edit 把 GBK 文件转成 UTF-8，须检测并保留；codex#32958：`read_text()` 在 cp936 下报 UnicodeDecodeError；PEP 597 |
| | 区域约定 | C.UTF-8 * / en_US / de_DE / tr_TR / zh_CN | 核心 | BrowserGym `locale`；SWE-bench django 实例写死 `LANG` | [准入案例表](validity-admission-cases.md)；codex#21957 |
| | 时区 | UTC * / 夏令时时区 / 半小时偏移时区 | 核心 | BrowserGym `timezone_id`；SWE-bench `TZ=Etc/UTC`，R2E-Gym 却是 `America/Los_Angeles` | codex#48436：agent 按系统时区买票造成实际损失，须从用户所在地推时区 |
| **E4.2 进程上下文** | 运行身份 | root * / 普通用户 | 核心 | E2B 默认非 root；Harbor `agent.user`；SWE-bench `execute_test_as_nonroot` | [准入案例表](validity-admission-cases.md)：非 root 下系统 pip 不可用，改用 venv |
| | tty | pty * / no-tty | 核心 | E2B `pty.create`；Fly `init.tty` | claude-code#237：无 tty 时交互菜单无限挂起，须改非交互参数 |
| | 环境变量继承 | inherited * / minimal / pure | 候选 | Codex `shell_environment_policy`；Guix `--pure` | codex#37662；AI 编码工具 bug 研究 127 条（多为 harness 层） |

### E5 边界层

这一层改变的是**哪些动作可行、哪些资源可达**，可以按阶段取不同值（第 4 节）。

| 维度 | 子维度 | 取值 | 准入 | 平台参数 / 被当自变量 | 一手证据 |
|---|---|---|---|---|---|
| **E5.1 权限** | 权限与能力 | full * / sudo-nopasswd / no-sudo / readonly-sys / restricted-caps | 核心 | Kubernetes `readOnlyRootFilesystem`、`capabilities`、`seccompProfile`；DSec AppArmor；Windows 只读属性 | [准入案例表](validity-admission-cases.md)；Windows 上带只读属性的文件 `os.remove` 与 `rmtree` 报 PermissionError，须先改属性 |
| | 挂载 | normal * / tmp-noexec / readonly-workspace | 核心 | Firecracker `is_read_only`；OCI `readonlyPaths` | claude-code#26741：/tmp noexec 时 Search 静默返回 0 结果 |
| **E5.2 网络** | 出网 | online * / offline / allowlist / mirror-only / proxy-required / ipv6-only | 核心 | E2B `allow_out`；Modal `outbound_domain_allowlist`；Harbor `network_mode`；Codex agent 阶段默认关网 | codex#376：出网被挡，须预置依赖或离线安装 |
| | DNS | normal * / servfail / sandbox-resolver | 候选 | Fly `dns` | claude-code#72706、codex#16312（多为 harness 层） |
| | HTTP 方法 | all * / read-only | 候选 | Codex Allowed HTTP methods | 平台文档 |
| **E5.3 时钟** | 时钟偏移 | synced * / future+1y / past-1y / frozen | 核心 | Firecracker `clock_realtime`；OCI `timeOffsets`；AndroidWorld、AppWorld 冻结时间 | [准入案例表](validity-admission-cases.md)：时钟拨快后 apt 与 TLS 证书过期；libfaketime：冻结时钟使等待型程序挂起 |
| **E5.4 凭据** | 可见性 | visible * / setup-only / placeholder | 候选 | Codex secret 只在 setup 阶段可见；Daytona 占位符 | 平台文档 |
| **E5.5 限额执行** | 执行语义 | guaranteed * / overcommit / hard-kill | 候选 | DSec 超分；cgroup | Anthropic 基础设施噪声实验；claude-code#85639 |

### E6 状态层

这一层唯一的特点：**agent 的动作、时间流逝、其他行动者都会改变它**。

| 维度 | 子维度 | 取值 | 准入 | 平台参数 / 被当自变量 | 一手证据 |
|---|---|---|---|---|---|
| **E6.1 平台残留** | residual | clean * / stale-files / stale-processes / leaked-logs | 核心 | DSec 清理答案残留；Codex 容器缓存 | claude-code#90524、#42269：残留目录与僵尸进程使后续命令失败；DSec §6.4 agent 从日志翻残留答案 |
| **E6.2 应用初始状态** | 设置与进度 | default * / non-default-settings / partially-done | 核心 | OSWorld `snapshot`、`config[]`；AndroidEnv `setup_steps` | WorldGUI |
| | 窗口与干扰 | clean * / window-moved / minimized / irrelevant-apps-open / popup | 核心 | ★ OSWorld 窗口扰动（下降 60%–80%）；★ macOSWorld 欺骗弹窗 | D-GARA：注入弹窗后 AgentCPM-GUI 59.87%→26.97%；browser-use#2276 |
| **E6.3 外部世界** | 外部服务时点 | frozen-snapshot * / live / drifted | 核心 | WebArena 自托管站点；Harbor `mcp_servers` | WebCanvas 一年后 12% 任务过期；Online-Mind2Web 47% 任务无效或过时；claude-code#86440 |
| | 接口版本 | pinned * / evolved | 核心 | — | MCPEvol-Bench 下降 13.7%–14.4%；Deprecated API Usage |
| | 服务可靠性 | reliable * / flaky-tools / rate-limited | 候选 | ★ Gaia2 Noise `tool_failure_probability=0.1`；ReliabilityBench | ReliabilityBench：限流伤害最大；多数只需重试，结构未必不同 |
| **E6.4 其他行动者** | 用户 | none * / cooperative-sim / hard-persona / human | 核心 | ★ τ² No-User / Default / Oracle，Easy 与 Hard 画像；τ `--user-strategy` | τ²：从无用户换到默认用户，gpt-4.1 下降 18%、o4-mini 下降 25%；须主动问询、协调，路径不同 |
| | 其他 agent | none * / peer-agent | 核心 | ★ Gaia2 Agent2Agent | Gaia2 A2A 子集 |
| | 异步事件 | none * / poisson-events | 候选 | ★ Gaia2 `EnvEventsConfig` | Gaia2 Noise 子集（与工具故障混测） |
| **E6.5 时间推进** | 思考是否计时 | paused-while-thinking * / real-time | 核心 | ★ Gaia2 `simulated_generation_time_mode` | Gaia2：Claude 4.0 Sonnet 计生成时间 8.2%，instant 模式 26.7% |

**边界说明。** 任务声明的初始状态（工作区放了哪些文件、数据库有哪些记录）属于任务。只有"同一个任务声明下，平台、时间或其他行动者带来的差异"才算 E6。这是 DSec 快照提出的问题；判定是：出题方写进任务的归任务，平台或时间带来的归环境。

### E7 界面层

只对 GUI 与浏览器任务有意义；终端任务里整层标"不适用"。

| 维度 | 子维度 | 取值 | 准入 | 平台参数 / 被当自变量 | 一手证据 |
|---|---|---|---|---|---|
| **E7.1 通道** | 观测与动作模态 | terminal * / gui-screenshot / a11y-tree / web-dom / api | 核心 | OSWorld `require_a11y_tree`；★ Windows Agent Arena `a11y-backend`（uia / win32）与 `som-origin` 组合对比；★ OpenApps axtree / screenshot | OSWorld 与 Windows Agent Arena 在同一任务上比较了不同观测组合；同一交付物经终端与经 GUI 完成，正确操作序列结构不同 |
| **E7.2 显示** | 缩放与 DPI | 100% * / 125–200% / 分数缩放 / 页面缩放 70% | 核心 | — | browser-use#4571：200% 下点击偏移 2 倍；trycua/cua#3061；GUI-Perturbed |
| | 分辨率与视口 | 1920×1080 * / 小屏 / 平板横屏 | 候选 | ★ OSWorld 截图降采样 0.2–0.8；★ OpenApps 三种分辨率；WebArena 1280×720 | VenusBench-Mobile 平板模式降幅最大（与其他因素混测） |
| | 主题与字体 | light * / dark / 高对比 / 难读字体 | 候选 | ★ OpenApps `dark_theme`、`challenging_font` | OpenApps：Kimi-VL 跨外观与内容变体 63%→4%（多因素） |
| **E7.3 语言与输入** | 界面语言 | en * / 其他语言 / 从右到左 | 核心 | ★ macOSWorld 五种界面语言；★ OpenApps 德语、中文 | trycua/cua#3137、#3139：按英文文字找按钮，本地化后找不到；macOSWorld 阿拉伯语下降 28.8% |
| | 输入通道 | direct * / ime / remote-desktop | 核心 | — | trycua/cua#2083：RDP 里 Unicode 输入静默丢字，须改用扫描码 |

---

## 4 横切属性：每个子维度都要标

| 属性 | 取值 | 为什么要标 |
|---|---|---|
| **阶段** | setup / agent / verifier | 同一任务里 E5 的取值可以随阶段变：Harbor 让 agent 与 verifier 分设网络、用户、超时；Codex setup 阶段有网、agent 阶段断网；DSec 网络规则按阶段动态改。卡片上写成"setup=online, agent=allowlist" |
| **谁决定** | 基础设施 / 镜像 / 启动者 / 沙箱 / 出题方 / 任务声明 | 判断一个差异该归环境还是归任务；复现时找谁要这个值 |
| **读数** | 一条可执行的观测 | 例如 `touch a && ls A` 判大小写，`locale charmap` 判编码。不能从分数反推子维度被触发 |

---

## 5 排除清单

完备性检验：16 个平台约 300 个参数、16 个 benchmark 声明的属性、DSec 全部参数，每一个要么落进第 3 节某个子维度，要么落进下面某一类。

| 类别 | 例子 | 为什么不是维度 | 什么时候例外 |
|---|---|---|---|
| **预算类** | CPU 核数、内存、磁盘大小、`timeout`、`ttl`、步数上限、`provisioning_tier`、`spot`、限速 | 只改变代价，同一做法等久一点仍能完成 | **阈值效应**：低到装不下依赖、编译被 OOM 杀、超时短于任务实际需要时，阈值点作为取值走准入（例：mem-below-input） |
| **钉住项** | 内核版本、镜像 digest、发行版小版本、OS 小版本、harness 版本、模型版本、推理服务的 batch 与数值精度、随机种子 | 影响复现，必须写进钉住清单；或属于三元组另两项 | 被证明改变正确解时升级为子维度。OS 版本目前只有 AndroidWorld 的总分差，留在钉住项 |
| **运维类** | 快照、暂停与恢复、`wake_on_http`、就绪探针、日志与观测出口 | 平台自己的生命周期管理 | 快照恢复改变时钟时归 E5.3 |
| **地理与入站** | `region`、公网入站端口、`custom_domain` | 一般不改变 agent 可走的路 | 任务依赖地理可达性或入站访问时归 E5.2、E6.3 |
| **harness 项** | 工具列表、MCP 服务器定义、上下文策略、截断、观测加工（截图压缩、a11y 树裁剪） | 三元组第二项，由 harness 卡片声明 | 与 E4.2 tty、E2.3 文件系统、E5.2 网络共用接触面的，交互项单独报 |
| **任务项** | 任务声明的初始数据、政策文档（τ 的 wiki、policy.md）、grader | 属于任务 | — |

---

## 6 环境卡片

仿 Zhang 的 Harness Card：7 层 26 个维度，每个子维度填"取值 + 阶段 + 谁决定 + 出处"，填不出的写"未声明"，对该对象无意义的写"不适用"。模板、JSON schema 与填写规则见 [environment-card.md](environment-card.md)，编号换成本文的子维度编号。

---

## 7 两个检验

### 7.1 用这套维度描述 DSec

53 个子维度逐一可填（依据 DSec 论文 arXiv:2609.22978 正文）：

- **在变的**：E2.2 隔离、E2.1 os（linux 与 android）、E3.1 运行时版本、E3.2 预装依赖与包来源、E5.2 出网、E1.2 加速器、E7.1 通道、E4.2 运行身份。
- **钉死的**：E1.1 arch（x86_64）、E2.3 文件系统语义（Linux 默认）、E3.3 shell（bash）、E2.4 换行（lf）。
- **没声明的**：E4.1 编码、区域约定、时区；E5.3 时钟；E3.3 工具实现；E4.2 tty；E6.4、E6.5 全部。

### 7.2 "OS"是一组子维度的捆绑点

公开记录里的 OS 类失败，几乎都能落到更细的子维度上：

| 公开记录 | 实际咬中的子维度 |
|---|---|
| claude-code#90524：APFS 上只改大小写的重命名 | E2.3 大小写 |
| claude-code#87822：NFC 与 NFD 路径不一致 | E2.3 Unicode 归一 |
| codex#36768：Windows MAX_PATH | E2.3 长度上限 |
| claude-code#4928：Windows 上写出真文件 `nul` | E2.3 保留名与尾部字符 |
| claude-code#56946、#89307：CRLF 文件编辑出错 | E2.4 换行 |
| claude-code#56946、codex#32958：GBK 与 cp936 编码 | E4.1 默认编码 |
| cline#346、gemini-cli#20773：PowerShell 不认 `&&` | E3.3 shell |
| claude-code#95705：BSD 上 `sed -i`、`date -d` 行为不同 | E3.3 工具实现 |

而且这些子维度可以脱离 OS 独立变化：Linux 可以给目录开 casefold（大小写不敏感），APFS 可以格式化成大小写敏感，Windows 可以打开长路径，同一个 Linux 镜像可以设不同的编码与区域。所以本版保留 E2.1 os 作为一个维度，同时把它常捆绑的差异拆成独立子维度：说"Windows"不够，要说它在 E2.3、E2.4、E3.3、E4.1 上各取什么值。

## 8 与上一版因子表（v0.2）的对应

| v0.2（5 组 22 因子） | 本版（7 层 26 维 53 子维度） |
|---|---|
| 硬件组 5 个因子 | E1：两个维度，加速器下 4 个子维度；accel 加 virtual-gpu |
| 系统组 os、fs、isolation | E2：fs 拆成 5 个子维度；新增系统约定（换行、分隔符）；perm、mount 移到 E5 |
| 运行时栈 6 个因子 | E3：新增预装情况（候选升核心）、包来源 |
| 策略可见面 channel、tty | channel 进 E7；tty 进 E4 |
| 外部世界 net、locale、tz、clock | locale 拆成编码与区域约定、tz 进 E4；net 拆出 DNS、HTTP 方法进 E5；clock 进 E5 |
| v0.2 的三个候选 installed-packages、limit-enforcement、external-state | 分别为 E3.2 核心、E5.5 候选、E6.3 核心 |
| — | 新增 E6 状态层（残留、应用初始状态、外部世界、其他行动者、时间推进）与 E7 显示、语言与输入 |

---

## 9 还没定的

1. **E7 界面层与 harness 的边界。** 显示缩放、界面语言由操作系统与应用提供，归环境；截图怎么压缩、a11y 树怎么裁剪归 harness。需要和 Harness Card 对一次边。
2. **E2.1 os 要不要保留。** 它的效应大多能拆到 E2.3、E2.4、E3.3、E4.1。保留的理由：还有拆不完的差异（系统 API、进程模型），而且 OS 是实验里的自然捆绑点。
3. **E6.4 其他行动者算环境还是算任务。** Sutton 的定义算环境；τ² 把用户画像写进任务。本版的切法：有没有用户、用户是什么类型归环境；用户具体要什么归任务。
4. **10 个候选子维度**（E2.5 内核能力、E4.2 环境变量继承、E5.2 DNS 与 HTTP 方法、E5.4 凭据、E5.5 限额执行、E6.3 服务可靠性、E6.4 异步事件、E7.2 分辨率与主题；另有 webkit、virtual-gpu 等个别候选取值）需要一轮受控实验或更多一手记录才能升降。
5. **虚拟化、文件系统语义、权限、网络从未被当作自变量。** 在调研的 16 个 agent benchmark 里，这四项都只是复刻原环境。运行时只在库版本这一层被变过（GitChameleon、VersiCode、LibEvolutionEval），依赖是否预装只在 Dockerless 里被变过。这几个子维度目前的核心地位主要靠公开 issue 撑着，最需要受控测量。

---

## 10 调研中的三个观察

1. **编码、区域约定、时区、时钟在 16 个沙箱平台里都不是一等参数。** 它们只能靠环境变量或镜像间接设置；只有 Firecracker 有一个 `clock_realtime`。DSec 也没有声明这几项。而编码与时区是经验研究里反复出现的失败来源：日期时间 bug 的首要根因是时区，AI 编码工具的环境类 bug 里有专门的换行与编码类。
2. **"会影响结果但作者建议别改"。** BrowserGym 的 viewport、locale、timezone 注释写着 "might change its behaviour and difficulty. Should only be set for debugging/testing"；AppWorld 的 `allow_datetime_change` 注释写着不应为真实模型改成非默认值。作者承认这些属性影响结果，但没有去测。
3. **同一子维度在不同 benchmark 里取值不一致。** 时区：SWE-bench 是 `Etc/UTC`，R2E-Gym 是 `America/Los_Angeles`，AndroidWorld 冻结在 2023-10-15 UTC。这些差异没有写进任何论文，是环境卡片要解决的问题。
