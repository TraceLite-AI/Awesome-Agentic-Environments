# Awesome Agentic Environments

A curated collection of papers, benchmarks, and frameworks on agentic environments — how they are built, scaled, and used for LLM agent post-training and evaluation.

**Why this list exists.** Four communities use the word *environment* for four different things. Agent benchmarks pin it as a constant (a Docker image or VM snapshot). RL infrastructure exposes it as a sandbox with knobs (network policy, isolation level, image layers). ML robustness research treats it as a nuisance the answer must *not* depend on. Software engineering has treated it as a Cartesian product of configuration factors for thirty years. None of them answers the question this list is organized around: **which environment factors change the correct solution to a task?**

Every entry below was checked against the original paper or official page. Numbers quoted are from the source. Entries we could not open are not listed.

**Contents**

1. [Agent benchmarks and their execution environments](#1-agent-benchmarks-and-their-execution-environments)
2. [Cross-environment sensitivity studies](#2-cross-environment-sensitivity-studies)
3. [Sandbox and RL training infrastructure](#3-sandbox-and-rl-training-infrastructure)
4. [Environment vendors, hubs and industry reports](#4-environment-vendors-hubs-and-industry-reports)
5. [Environment in classic RL and robotics](#5-environment-in-classic-rl-and-robotics)
6. [Environment in ML robustness and causality](#6-environment-in-ml-robustness-and-causality)
7. [Configuration spaces and combinatorial testing](#7-configuration-spaces-and-combinatorial-testing)
8. [Environment-dependent bugs, flakiness and reproducibility](#8-environment-dependent-bugs-flakiness-and-reproducibility)
9. [Design of experiments and sensitivity analysis](#9-design-of-experiments-and-sensitivity-analysis)
10. [Environment coordinate space (proposal)](#10-environment-coordinate-space-proposal)
11. [Contributing](#contributing)

---

## 1. Agent benchmarks and their execution environments

What each benchmark fixes, what it declares, and whether the environment is ever an independent variable. "—" means the paper does not state it.

| Benchmark | Venue | Isolation / image | OS (version) | Network | Channel | Environment varied? | Same task across OS? |
|---|---|---|---|---|---|---|---|
| [SWE-bench](https://arxiv.org/abs/2310.06770) | ICLR 2024 | per-repo conda, later Docker; no digest | — (README: x86_64 primary, arm64 experimental) | — | terminal | no | no |
| [SWE-bench Verified](https://www.swebench.com/verified.html) | 2024 | Docker | Linux (Epoch's run) | disabled (Epoch's run) | terminal | no | no |
| [SWE-bench Multimodal](https://arxiv.org/abs/2410.03859) | 2024 | Docker + Node.js + Chrome; ~10 h manual env work per repo | — | — | terminal + headless browser | no | no |
| [Terminal-Bench](https://arxiv.org/abs/2601.11868) | 2026 | Docker; pins package versions, apt packages "shall not be pinned" | — | internet allowed | terminal | no (≥5 repeats) | no; limitations admit "hardware differences (e.g., CPU architectures)" |
| [OSWorld](https://arxiv.org/abs/2404.07972) | NeurIPS 2024 D&B | VM snapshot | Ubuntu / Windows / macOS, no versions | — | GUI | no | 43 tasks Ubuntu→Windows: 4.88% vs 2.55%, r = 0.7 |
| [OSWorld-Verified](https://xlang.ai/blog/osworld-verified) | 2025 | AWS image | Ubuntu / Windows | — | GUI | no | no |
| [WebArena](https://arxiv.org/abs/2307.13854) / [VisualWebArena](https://arxiv.org/abs/2401.13649) | 2023 / ACL 2024 | Docker, self-hosted sites, offline Wikipedia | — | offline | browser | no | no |
| [AgentBench](https://arxiv.org/abs/2308.03688) | ICLR 2024 | Ubuntu Docker per task | Ubuntu | — | terminal etc. | no | no |
| [τ-bench](https://arxiv.org/abs/2406.12045) | 2024 | DB + API + simulated user, no OS | none | — | tool calls | no (pass^k repeats) | no |
| [GAIA](https://arxiv.org/abs/2311.12983) | 2023 | live web, admits decay | none | live | — | uncontrolled | no |
| [MLE-bench](https://arxiv.org/abs/2410.07095) | ICLR 2025 | Docker + sysbox, A10 GPU | Ubuntu 20.04 | — | terminal | **yes: CPU-only / standard / extra GPU; 3 seeds** | no |
| [Windows Agent Arena](https://arxiv.org/abs/2409.08264) | 2024 | Windows VM inside Docker (QEMU/KVM) | Windows 11 | — | GUI | no | 2/3 tasks ported from OSWorld, no numeric comparison |
| [AndroidWorld](https://arxiv.org/abs/2405.14573) | 2024 | emulator | Android 13, Pixel 6 | — | GUI | task parameters only | no |
| [AppWorld](https://arxiv.org/abs/2407.18901) | ACL 2024 | simulated apps, time frozen (freezegun) | none | — | code | no | no |
| [TheAgentCompany](https://arxiv.org/abs/2412.14161) | 2024 | Docker, self-hosted GitLab/OwnCloud/Plane/RocketChat | — | self-hosted | terminal + browser | no | no |
| [MacArena](https://arxiv.org/abs/2606.06560) | AIWILD @ ICML 2026 | UTM VM on Apple silicon | macOS | — | GUI | no | **same OSWorld task set Linux→macOS: −3.23 / −9.26 / −9.84 pp for three models** |
| [macOSWorld](https://arxiv.org/abs/2506.04135) | 2025 | VM | macOS | — | GUI | **yes: 5 interface languages (Arabic −28.8% avg)** | no |

Also: [OSWorld 2.0](https://arxiv.org/abs/2606.29537), [MacAgentBench](https://arxiv.org/abs/2606.22557) (macOS-only, 676 tasks), [MMBench-GUI](https://arxiv.org/abs/2507.19478) (one protocol across six platforms).

**Reading the table.** No benchmark states an image digest. None states the user/permission model. Locale or timezone appears only in AppWorld (frozen time) and macOSWorld (interface language). Same-task cross-OS measurement exists only in the GUI world and is small; for coding and terminal agents we found no study that holds the task fixed and varies OS, shell, locale or runtime.

## 2. Cross-environment sensitivity studies

- **OSWorld §5.3** — 43 Ubuntu tasks adapted to Windows; 4.88% vs 2.55%, correlation 0.7. [paper](https://arxiv.org/abs/2404.07972)
- **MacArena** (AIWILD @ ICML 2026) — identical OSWorld task set on macOS; "strong model performance on existing benchmarks can reflect familiarity with task distributions rather than genuine cross-platform GUI competence". [paper](https://arxiv.org/abs/2606.06560)
- **macOSWorld** — OS interface language as an axis; Arabic −28.8% average vs English. [paper](https://arxiv.org/abs/2506.04135)
- **On the Reliability of Computer Use Agents** (2026) — repeated execution on OSWorld with the environment fixed; decomposes execution stochasticity, task ambiguity and agent variability. The noise-floor paper. [paper](https://arxiv.org/abs/2604.17849)
- **An Empirical Analysis of Cross-OS Portability Issues in Python Projects** (MSR 2026) — 2,042 repos; cross-OS test re-execution shows 11.2% of tested projects have OS-dependent failures; files & directories dominate (path separators, file locking, encoding, CRLF). Not an agent study, but the best evidence for which axes matter. [paper](https://arxiv.org/html/2609.25531)
- **Terminal-Bench, limitations** — "variability in machine resources and container runtime enforcement can lead to differences in effective task environments". [paper](https://arxiv.org/abs/2601.11868)

## 3. Sandbox and RL training infrastructure

What knobs each platform exposes. None of them defines which knobs change the correct solution.

| Platform | OS choice | Isolation | Image / layers | Network policy | User / permissions | GPU | Locale |
|---|---|---|---|---|---|---|---|
| [DSec (DeepSeek)](https://arxiv.org/abs/2609.22978) | Linux base images; Android full VM | FnCall / container / Firecracker microVM / full VM | base + workspace + toolkit (overlayfs, EROFS) | per-service allowlist (`{"npm": False, "pypi": True}`) | `init_user` | FnCall GPU | — |
| [Firecracker](https://www.usenix.org/conference/nsdi20/presentation/agache) (NSDI 2020) | Linux guests only | microVM, jailer | — | device rate limits | — | — | — |
| [E2B](https://docs.e2b.dev/) | Linux | Firecracker snapshot resume | template | allow / deny lists | — | — | — |
| [Modal Sandboxes](https://modal.com/docs/guide/sandbox) | Linux | gVisor; VM beta | Image | block / CIDR / domain allowlist | — | yes | — |
| [Daytona](https://www.daytona.io/docs/en/sandboxes/) | Linux / Windows / macOS | container / VM | image must carry tag or digest | allowlist / blockAll / proxy | root | NVIDIA / AMD, up to 8 | — |
| [OpenAI Code Interpreter](https://developers.openai.com/api/docs/guides/tools-code-interpreter) | — | VM | — | — | — | — | — |
| [Prime Intellect verifiers / Harbor](https://github.com/PrimeIntellect-ai/verifiers) | — | docker / prime / VM | per-task image | no-network / allowlist | solver vs verifier isolation | — | — |
| [Gymnasium](https://gymnasium.farama.org/api/env/) | — | — | — | — | — | — | only `reset(seed)` |

**DSec in one paragraph.** One scale unit: ~160 nodes, ~3 M sandboxes/day, >380 K concurrent, >5,000 creations/s. Environments are composed from three independently versioned layers (base image, workspace, toolkit — the DeepSeek Harness ships as a toolkit layer). Agents build environments interactively and checkpoint them (`pack_diff`). Section 6.4 documents agents obtaining answers through unintended channels (reading platform logs, forging RPCs, overwriting `/bin/bash`, port-scanning for mirrors, pulling reference code via Go module proxies) and concludes: *"Final-output checks alone cannot reliably establish whether the agent solved the task as intended."*

## 4. Environment vendors, hubs and industry reports

- **An FAQ on Reinforcement Learning Environments** — Epoch AI, Jan 2026, 18 interviews. Definition: "the set of actions the model can take … and the surrounding context that determines the effect of these actions"; "the boundary between 'environment' and 'task' is somewhat fuzzy". Prices: tasks $200–2,000; UI replicas ~$20 k; high-fidelity replicas ~$300 k; contracts six to seven figures per quarter; exclusive deals 4–5×. [post](https://epoch.ai/gradient-updates/state-of-rl-envs)
- **Silicon Valley bets big on 'environments' to train AI agents** — TechCrunch, Sept 2025. Anthropic reportedly discussed >$1 B/year on RL environments; "RL environments are prone to reward hacking". [article](https://techcrunch.com/2025/09/21/silicon-valley-bets-big-on-environments-to-train-ai-agents/)
- **Mercor to acquire Deeptune** — July 2026. "Every environment has three parts: the software where the work takes place, the tasks …, and the verifiers". [post](https://www.mercor.com/blog/mercor-to-acquire-deeptune/)
- **Scale AI — RL Environments** — "macOS- and Windows-like operating system environments"; OS as replicated content, not a variable. [page](https://scale.com/rlenvironments)
- **Surge AI** — off-the-shelf RL environments; HANDBOOK.md benchmark; EnterpriseBench. [site](https://surgehq.ai/)
- **Prime Intellect Environments Hub** — Aug 2025; "RL environments and agent evals are basically the same thing". [post](https://www.primeintellect.ai/blog/environments)

## 5. Environment in classic RL and robotics

- **Procgen** — 16 procedurally generated environments; variation = level content inside a fixed simulator. [paper](https://arxiv.org/abs/1912.01588)
- **XLand / Open-Ended Learning** — procedurally generated 3D worlds and game rules. [paper](https://arxiv.org/abs/2107.12808)
- **Domain Randomization** (Tobin et al., IROS 2017) — randomizes textures, lighting, camera pose, distractors so that "the real world may appear to the model as just another variation"; per-factor ablation (no distractors: error 1.8 → 7.2 cm). [paper](https://arxiv.org/abs/1703.06907)
- **Dynamics Randomization** (Peng et al., ICRA 2018) — 95 randomized physical parameters, sampled per episode. [paper](https://arxiv.org/abs/1710.06537)

## 6. Environment in ML robustness and causality

The admission rule here runs the *opposite* way: a factor is admitted because the correct answer must **not** depend on it.

- **Invariant Risk Minimization** — environments = "the same pair of random variables measured under different conditions"; an invariant predictor is "simultaneously optimal for all environments". [paper](https://arxiv.org/abs/1907.02893)
- **Causal inference by using invariant prediction** (Peters, Bühlmann, Meinshausen, JRSS-B 2016) — environments as uncontrolled interventions; "interventions on Y are not allowed". [paper](https://arxiv.org/abs/1501.01332)
- **Toward Causal Representation Learning** (Schölkopf et al., Proc. IEEE 2021) — distributions as products of mechanisms; environment shift = sparse mechanism shift. [paper](https://arxiv.org/abs/2102.11107)
- **WILDS** (ICML 2021) — one named shift axis per dataset; reports worst-group, not mean. [paper](https://arxiv.org/abs/2012.07421)
- **DomainBed** (ICLR 2021) — leave-one-domain-out; headline table is accuracy *by domain*. [paper](https://arxiv.org/abs/2007.01434)
- **ImageNet-C** (ICLR 2019) — 15 corruption types × 5 severities = 75 cells; per-corruption CE first, mCE second, Relative CE alongside. [paper](https://arxiv.org/abs/1903.12261)
- **FormatSpread** (ICLR 2024) — meaning-preserving prompt formats as a product of atomic choices; 24% of atomic changes shift accuracy ≥5 points; report min–max spread, not one format. [paper](https://arxiv.org/abs/2310.11324)
- **PromptRobust** — character / word / sentence / semantic perturbation levels; Performance Drop Rate as a dataset × level matrix. [paper](https://arxiv.org/abs/2306.04528)
- **dSprites** — 6 generative factors, "all possible combinations … present exactly once", 737,280 images: a literal full Cartesian product. [dataset](https://github.com/google-deepmind/dsprites-dataset)
- **Challenging Common Assumptions in Disentanglement** (ICML 2019) — factor-grid datasets; variance decomposition over the Cartesian product of objective × regularization. [paper](https://arxiv.org/abs/1811.12359)

## 7. Configuration spaces and combinatorial testing

- **Software Fault Interactions and Implications for Software Testing** (Kuhn, Wallace, Gallo, IEEE TSE 2004) — the NIST interaction rule: 66–97% of failures need ≤2 conditions, none needed more than 6. [paper](https://csrc.nist.gov/pubs/journal/2004/06/software-fault-interactions-and-implications-for-s/final)
- **Practical Combinatorial Testing** (NIST SP 800-142, 2010) — t-way covering arrays are "effectively exhaustive" for interaction faults. [report](https://csrc.nist.gov/pubs/sp/800/142/final)
- **A survey of combinatorial testing** (Nie & Leung, ACM CSUR 2011). [doi](https://doi.org/10.1145/1883612.1883618)
- **The AETG System** (Cohen et al., IEEE TSE 1997) — pairwise generation; test count grows logarithmically in the number of factors. [doi](https://doi.org/10.1109/32.605761)
- **Performance-Influence Models for Highly Configurable Systems** (Siegmund et al., ESEC/FSE 2015) — score = base + per-option terms + sparse interaction terms. [paper](http://www.cs.cmu.edu/~ckaestne/pdf/fse15_influence.pdf)
- **A Comparison of 10 Sampling Algorithms for Configurable Systems** (ICSE 2016). [paper](https://arxiv.org/abs/1602.02052)
- **Test them all, is it worth it?** (JHipster, EMSE 2019) — all 26,000+ configurations built and tested; 35.7% fail; pairwise sampling finds most faults. [paper](https://arxiv.org/abs/1710.07980)
- **Testing Configuration Changes in Context** (Ctest, OSDI 2020). [paper](https://www.usenix.org/conference/osdi20/presentation/sun)
- **GitHub Actions matrix** — "A job will run for each possible combination of the variables"; the industry's de facto Cartesian product, capped at 256 jobs. [docs](https://docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs)

## 8. Environment-dependent bugs, flakiness and reproducibility

- **Cross-OS Portability Issues in Python Projects** (MSR 2026) — see §2. [paper](https://arxiv.org/html/2609.25531)
- **An Empirical Study of Bugs in Test Code** (ICSME 2015) — "61% of environmental false alarms are platform-specific failures, caused by operating system differences". [paper](https://people.ece.ubc.ca/amesbah/resources/papers/icsme15.pdf)
- **It's About Time** (MSR 2025, Distinguished Paper) — 151 date/time bugs; timezone mistakes are the largest root cause. [page](https://2025.msrconf.org/details/msr-2025-technical-papers/35/)
- **Apple File System Guide, FAQ** — HFS+ stores NFD; APFS preserves the name but hashes the normalized form. The mechanism behind macOS filename bugs. [docs](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/APFS_Guide/FAQ/FAQ.html)
- **An Empirical Analysis of Flaky Tests** (FSE 2014) — "almost all flaky tests (96%) are independent of the platform". [paper](https://mir.cs.illinois.edu/lamyaa/publications/fse14.pdf)
- **An Empirical Study of Flaky Tests in Python** (ICST 2021) — 28% "infrastructure" flakiness; ~170 reruns for 95% confidence. [paper](https://arxiv.org/abs/2101.09077)
- **A Survey of Flaky Tests** (ACM TOSEM 2022) — "Platform Dependency" ranges 0–4% to 34% depending on dataset. [paper](https://eprints.whiterose.ac.uk/id/eprint/230095/1/parry2021.pdf)
- **Reproducible Builds** (Lamb & Zacchiroli, IEEE Software 2022) — bit-for-bit reproducibility; sources of non-reproducibility include timestamps, paths, locale, file order. [post](https://chris-lamb.co.uk/posts/reproducible-builds-increasing-the-integrity-of-software-supply-chains)
- **Nix** (LISA 2004) — environments as pure functions of hashed inputs. [paper](https://www.usenix.org/conference/lisa-04/nix-safe-and-policy-free-system-software-deployment)
- **Reproducibility of Build Environments through Space and Time** (ICSE 2024 NIER) — 99.94% of ~14,000 packages rebuild from a six-year-old Nixpkgs revision. [paper](https://arxiv.org/abs/2402.00424)
- **Learning from, Understanding, and Supporting DevOps Artifacts for Docker** (ICSE 2020) — ~178 K Dockerfiles; ordinary repos violate pinning rules 5× more than the expert set. [paper](https://pages.cs.wisc.edu/~jjhenkel/papers/icse20-docker.pdf)

## 9. Design of experiments and sensitivity analysis

- **Fisher, The Design of Experiments** (1935) — factorial designs estimate main effects and interactions together; one-factor-at-a-time cannot see interactions.
- **Box, Hunter & Hunter, Statistics for Experimenters** (2nd ed., 2005) — fractional factorial and screening designs.
- **Morris, Factorial Sampling Plans for Preliminary Computational Experiments** (Technometrics 1991) — elementary effects: per factor, a mean (influence) and a standard deviation (nonlinearity or interaction). The formal name for "directional derivative per axis".
- **Sobol', Global sensitivity indices** (2001) — variance decomposition into first-order and interaction indices.
- **Saltelli & Annoni, How to avoid a perfunctory sensitivity analysis** (2010) — OAT samples lie inside the inscribed hypersphere; volume ratio ~0.52 at k = 3 and vanishing as k grows. [paper](https://www.nusap.net/spe/Saltelli_and_Annoni_2010.pdf)

## 10. Environment coordinate space (proposal)

Our own attempt at the missing definition: an environment is everything outside the policy under test that can change the correct solution. It is projected onto a finite set of axes, each admitted by a four-step test (the correct solution in cell A fails when moved unchanged to cell B, and B's correct solution is *structurally* different, not merely cheaper). The space is a Cartesian product of 22 factors in five groups (hardware, system, runtime stack, policy-visible surface, external world), measured with a star design plus a 2-way covering array, and reported as per-axis directional derivatives with no total score.

- [Environment axes and values (v0.2)](docs/environment-axes.md) — the full factor table with baseline values, admission test, protocol and reporting rules.
- [Survey and proposal (Chinese, v1.1)](docs/survey-environment-coordinate-space-zh-v1.1.md) — how the four communities use "environment", three coverage tables, the proposal, and a mapping onto existing infrastructure.

## Contributing

Add an entry only if you opened the source. Give the venue and year as the source states them, quote numbers rather than paraphrasing them, and say what the work fixes, varies, or defines about the environment. Entries that merely mention "a sandbox" without saying what is in it are out of scope.

## License

Apache 2.0. See [LICENSE](LICENSE).
