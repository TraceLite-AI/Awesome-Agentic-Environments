# Awesome Multimodal GUI Agents [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

<p align="center">
  <img src="assets/awesome-multimodal-gui-agents.svg" alt="Awesome Multimodal GUI Agents" width="100%">
</p>

A curated list of **papers, datasets, benchmarks, models, tools, and open-source projects** for **Multimodal GUI Agents**.

This repository focuses on vision-language-based agents that can perceive visual interfaces, understand user instructions, reason over GUI states, and execute actions across **web, mobile, desktop, and general computer-use environments**.

We will keep tracking recent advances in multimodal GUI agents and updating relevant information.

**Keywords:** GUI Agent, Multimodal Agent, Computer Use, Vision-Language Model, VLM, Web Agent, Mobile Agent, Desktop Agent, GUI Grounding, Screen Understanding, Action Prediction, Long-Horizon Automation

🔥🔥🔥 Contributions to our repository are welcome. Feel free to categorize the papers and [pull requests](https://github.com/DeLunnLi/Awesome-Multimodal-GUI-Agents/pulls).

---

## Scope and Inclusion Criteria

This list uses a broad but explicit **GUI-agent / computer-use agent** scope.

- **Core GUI-agent papers:** methods that perceive GUIs, ground UI elements, predict actions, plan over screen states, or execute tasks in web, mobile, desktop, or cross-platform computer-use environments.
- **Benchmarks and datasets:** evaluation environments, UI datasets, interaction traces, screen understanding data, and trajectory data that directly support GUI-agent research.
- **Related foundations:** earlier web/mobile control environments, UI understanding datasets, and browser/mobile/desktop automation resources that are useful background but are not counted as core GUI-agent method papers.
- **Tools and projects:** automation frameworks, open-source systems, model repositories, and engineering resources. These are implementation resources, not paper-only entries.

Generic LLM-agent work is included only when it has a clear path to GUI perception, browser/mobile/desktop operation, computer-use evaluation, or GUI-agent safety.

Venue labels are kept conservative: prefer official paper pages, repositories, or proceedings pages; use arXiv metadata only when it is specific and not contradicted by official sources. Otherwise use `arXiv` or `Tech Report`.

---

## Table of Contents


- [Scope and Inclusion Criteria](#scope-and-inclusion-criteria)
- [Latest Updates](#latest-updates)
- [SOTA / Representative Methods with Code](#sota--representative-methods-with-code)
- [Recommended Datasets / Benchmarks](#recommended-datasets--benchmarks)
- [Model / Data Collections](#model--data-collections)
- [Recent Research](#recent-research)
  - [ICML 2026](#icml-2026)
  - [AAAI 2026](#aaai-2026)
  - [arXiv 2026](#arxiv-2026)
  - [CVPR 2025](#cvpr-2025)
  - [ICLR 2025](#iclr-2025)
  - [ACL 2024](#acl-2024)
  - [CVPR 2024](#cvpr-2024)
  - [NeurIPS / Datasets & Benchmarks](#neurips)
  - [ICML 2024](#icml-2024)
  - [arXiv 2025](#arxiv-2025)
  - [arXiv 2024](#arxiv-2024)
  - [2023 and Before](#2023-and-before)
- [Paper Tree](#paper-tree)
- [Timeline](#timeline)
- [Paper List](#paper-list)
  - [Surveys](#surveys)
  - [GUI Grounding and Screen Understanding](#gui-grounding-and-screen-understanding)
  - [General GUI Agents](#general-gui-agents)
  - [Web Agents](#web-agents)
  - [Mobile Agents](#mobile-agents)
  - [Desktop and Computer-Use Agents](#desktop-and-computer-use-agents)
  - [Evaluation and Benchmarks](#evaluation-and-benchmarks)
  - [Training, Data Synthesis, and Reinforcement Learning](#training-data-synthesis-and-reinforcement-learning)
  - [Safety, Robustness, and Security](#safety-robustness-and-security)
- [Open-Source Projects / Tools](#open-source-projects--tools)
- [Related Repositories](#related-repositories)
- [Contributing](#contributing)
- [Citation](#citation)

---

## Latest Updates

> Recent high-signal additions. The full categorized list is below.

+ **2026.05** - [Recovering Policy-Induced Errors / RoTS](https://arxiv.org/abs/2605.29447) introduces GUI-RobustEval and robustness-driven trajectory synthesis for error recovery. [[code]](https://github.com/AlibabaResearch/RoTS)
+ **2026.05** - [MobileGym](https://arxiv.org/abs/2605.26114) provides a verifiable, highly parallel simulation platform for mobile GUI-agent research. [[website]](https://mobilegym.github.io)
+ **2026.05** - [OpenComputer](https://arxiv.org/abs/2605.19769) proposes verifier-grounded software worlds for computer-use agents across desktop applications.
+ **2026.05** - [Video2GUI / WildGUI](https://arxiv.org/abs/2605.14747) extracts large-scale GUI trajectories from unlabeled videos for generalized GUI-agent pretraining.
+ **2026.05** - [PhoneWorld](https://arxiv.org/abs/2605.29486) scales phone-use agent environments for mobile-agent research.
+ **2026.04** - [OpenMobile](https://arxiv.org/abs/2604.15093) builds open mobile agents with task and trajectory synthesis. [[project]](https://njucckevin.github.io/openmobile/)
+ **2026.02** - [UI-Venus-1.5](https://arxiv.org/abs/2602.09082) releases a technical report, codebase, and model/data collection for GUI agents. [[code]](https://github.com/inclusionAI/UI-Venus) [[model]](https://huggingface.co/collections/inclusionAI/ui-venus)
+ **2026.01** - [EvoCUA](https://arxiv.org/abs/2601.15876) studies scalable synthetic experience for evolving computer-use agents. [[model]](https://huggingface.co/collections/harbingeva/evocua-687c664a9bb7b48f2272ff8a)
+ **2025.09** - [UI-TARS-2](https://arxiv.org/abs/2509.02544) advances GUI agents with multi-turn reinforcement learning. [[code]](https://github.com/bytedance/UI-TARS)
+ **2025.08** - [OpenCUA](https://arxiv.org/abs/2508.09123) provides open foundations for computer-use agents and the AgentNet ecosystem. [[code]](https://github.com/xlang-ai/OpenCUA)
+ **2025.03** - [UI-R1](https://arxiv.org/abs/2503.21620), [ScreenLLM](https://arxiv.org/abs/2503.20978), and [V-Droid](https://arxiv.org/abs/2503.15937) fill early-2025 gaps in GUI action prediction and practical mobile deployment.
+ **2024.12** - [BrowserGym](https://arxiv.org/abs/2412.05467), [AutoDroid-V2](https://arxiv.org/abs/2412.18116), [Ponder & Press](https://arxiv.org/abs/2412.01268), and [AgentTrek](https://arxiv.org/abs/2412.09605) enrich web, mobile, and general computer-control research.
+ **2024.10** - [OpenWebVoyager](https://arxiv.org/abs/2410.19609), [Web Agents with World Models](https://arxiv.org/abs/2410.13232), [OSCAR](https://arxiv.org/abs/2410.18963), [EDGE](https://arxiv.org/abs/2410.19461), and [ClickAgent](https://arxiv.org/abs/2410.11872) expand 2024 GUI/web-agent coverage.
+ **2023.04** - [DroidBot-GPT](https://arxiv.org/abs/2304.07061) and [Mobile-Env](https://arxiv.org/abs/2305.08144) are added as early LLM-GUI / Android automation foundations.

---

## SOTA / Representative Methods with Code

> This table lists representative GUI-agent models and systems. It is not intended to be a definitive leaderboard.

|  Title  |   Venue  |   Date   |   Code   |   Topic   |
|:--------|:--------:|:--------:|:--------:|:--------:|
| ![Star](https://img.shields.io/github/stars/THUDM/CogAgent.svg?style=social&label=Star) <br> [**CogAgent: A Visual Language Model for GUI Agents**](https://arxiv.org/abs/2312.08914) <br> | CVPR | 2024 | [Github](https://github.com/THUDM/CogAgent) | GUI understanding, navigation |
| ![Star](https://img.shields.io/github/stars/njucckevin/SeeClick.svg?style=social&label=Star) <br> [**SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents**](https://arxiv.org/abs/2401.10935) <br> | ACL | 2024 | [Github](https://github.com/njucckevin/SeeClick) | GUI grounding, click prediction |
| ![Star](https://img.shields.io/github/stars/OS-Copilot/OS-Atlas.svg?style=social&label=Star) <br> [**OS-ATLAS: A Foundation Action Model for Generalist GUI Agents**](https://arxiv.org/abs/2410.23218) <br> | ICLR | 2025 | [Github](https://github.com/OS-Copilot/OS-Atlas) | Cross-platform GUI grounding |
| ![Star](https://img.shields.io/github/stars/showlab/ShowUI.svg?style=social&label=Star) <br> [**ShowUI: One Vision-Language-Action Model for GUI Visual Agent**](https://arxiv.org/abs/2411.17465) <br> | CVPR | 2025 | [Github](https://github.com/showlab/ShowUI) | Lightweight GUI action model |
| ![Star](https://img.shields.io/github/stars/bytedance/UI-TARS.svg?style=social&label=Star) <br> [**UI-TARS: Pioneering Automated GUI Interaction with Native Agents**](https://arxiv.org/abs/2501.12326) <br> | arXiv | 2025 | [Github](https://github.com/bytedance/UI-TARS) | End-to-end GUI interaction |
| ![Star](https://img.shields.io/github/stars/bytedance/UI-TARS.svg?style=social&label=Star) <br> [**UI-TARS-2: Advancing GUI Agent with Multi-Turn Reinforcement Learning**](https://arxiv.org/abs/2509.02544) <br> | arXiv | 2025 | [Github](https://github.com/bytedance/UI-TARS) | Multi-turn RL GUI agent |
| ![Star](https://img.shields.io/github/stars/xlang-ai/OpenCUA.svg?style=social&label=Star) <br> [**OpenCUA: Open Foundations for Computer-Use Agents**](https://arxiv.org/abs/2508.09123) <br> | arXiv | 2025 | [Github](https://github.com/xlang-ai/OpenCUA) | Open computer-use foundation |
| ![Star](https://img.shields.io/github/stars/inclusionAI/UI-Venus.svg?style=social&label=Star) <br> [**UI-Venus-1.5 Technical Report**](https://arxiv.org/abs/2602.09082) <br> | arXiv | 2026 | [Github](https://github.com/inclusionAI/UI-Venus) | Foundation GUI agent |
| ![Star](https://img.shields.io/github/stars/X-PLUG/MobileAgent.svg?style=social&label=Star) <br> [**Mobile-Agent-v3.5: Multi-platform Fundamental GUI Agents**](https://arxiv.org/abs/2602.16855) <br> | arXiv | 2026 | [Github](https://github.com/X-PLUG/MobileAgent) | Multi-platform mobile / GUI agent |
| [**EvoCUA: Evolving Computer Use Agents via Learning from Scalable Synthetic Experience**](https://arxiv.org/abs/2601.15876) <br> | arXiv | 2026 | [Model](https://huggingface.co/collections/harbingeva/evocua-687c664a9bb7b48f2272ff8a) | Synthetic-experience CUA training |
| ![Star](https://img.shields.io/github/stars/OSU-NLP-Group/UGround.svg?style=social&label=Star) <br> [**UGround: Universal GUI Visual Grounding for GUI Agents**](https://arxiv.org/abs/2410.05243) <br> | ICLR | 2025 | [Github](https://github.com/OSU-NLP-Group/UGround) | Universal visual grounding |
| ![Star](https://img.shields.io/github/stars/lll6gg/UI-R1.svg?style=social&label=Star) <br> [**UI-R1: Enhancing Efficient Action Prediction of GUI Agents by Reinforcement Learning**](https://arxiv.org/abs/2503.21620) <br> | arXiv | 2025 | [Github](https://github.com/lll6gg/UI-R1) | RL action prediction |
| ![Star](https://img.shields.io/github/stars/V-Droid-Agent/V-Droid.svg?style=social&label=Star) <br> [**V-Droid: Advancing Mobile GUI Agents with a Verifier-Driven Approach**](https://arxiv.org/abs/2503.15937) <br> | arXiv | 2025 | [Github](https://github.com/V-Droid-Agent/V-Droid) | Verifier-driven mobile deployment |
| ![Star](https://img.shields.io/github/stars/microsoft/Phi-Ground.svg?style=social&label=Star) <br> [**Phi-Ground: Advancing Perception in GUI Grounding**](https://arxiv.org/abs/2507.23779) <br> | arXiv | 2025 | [Github](https://github.com/microsoft/Phi-Ground) | GUI grounding model |
| ![Star](https://img.shields.io/github/stars/Reallm-Labs/InfiGUI-R1.svg?style=social&label=Star) <br> [**InfiGUI-R1: From Reactive Actors to Deliberative Reasoners**](https://arxiv.org/abs/2504.14239) <br> | arXiv | 2025 | [Github](https://github.com/Reallm-Labs/InfiGUI-R1) | Reasoning GUI agent |
| ![Star](https://img.shields.io/github/stars/X-PLUG/MobileAgent.svg?style=social&label=Star) <br> [**Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent**](https://arxiv.org/abs/2401.16158) <br> | arXiv | 2024 | [Github](https://github.com/X-PLUG/MobileAgent) | Smartphone operation |
| ![Star](https://img.shields.io/github/stars/MinorJerry/WebVoyager.svg?style=social&label=Star) <br> [**WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models**](https://arxiv.org/abs/2401.13919) <br> | arXiv | 2024 | [Github](https://github.com/MinorJerry/WebVoyager) | Web navigation |
| ![Star](https://img.shields.io/github/stars/mnotgod96/AppAgent.svg?style=social&label=Star) <br> [**AppAgent: Multimodal Agents as Smartphone Users**](https://arxiv.org/abs/2312.13771) <br> | arXiv | 2023 | [Github](https://github.com/mnotgod96/AppAgent) | App control |
| ![Star](https://img.shields.io/github/stars/showlab/assistgui.svg?style=social&label=Star) <br> [**AssistGUI: Task-Oriented Desktop Graphical User Interface Automation**](https://arxiv.org/abs/2312.13108) <br> | CVPR | 2024 | [Github](https://github.com/showlab/assistgui) | Desktop automation |
| ![Star](https://img.shields.io/github/stars/microsoft/UFO.svg?style=social&label=Star) <br> [**UFO: A UI-Focused Agent for Windows OS Interaction**](https://arxiv.org/abs/2402.07939) <br> | arXiv | 2024 | [Github](https://github.com/microsoft/UFO) | Windows desktop agent |
| ![Star](https://img.shields.io/github/stars/xlang-ai/Aguvis.svg?style=social&label=Star) <br> [**Aguvis: Unified Pure Vision Agents for Autonomous GUI Interaction**](https://arxiv.org/abs/2412.04454) <br> | arXiv | 2024 | [Github](https://github.com/xlang-ai/aguvis) | Pure vision GUI agent |
| ![Star](https://img.shields.io/github/stars/THUDM/AutoGLM.svg?style=social&label=Star) <br> [**AutoGLM: Autonomous Foundation Agents for GUIs**](https://arxiv.org/abs/2411.00820) <br> | arXiv | 2024 | [Github](https://github.com/THUDM/AutoGLM) | Foundation GUI agent |
| ![Star](https://img.shields.io/github/stars/simular-ai/Agent-S.svg?style=social&label=Star) <br> [**Agent S: An Open Agentic Framework that Uses Computers Like a Human**](https://arxiv.org/abs/2410.08164) <br> | arXiv | 2024 | [Github](https://github.com/simular-ai/Agent-S) | Open agentic framework |
| ![Star](https://img.shields.io/github/stars/GAIR-NLP/PC-Agent.svg?style=social&label=Star) <br> [**PC Agent: While You Sleep, AI Works**](https://arxiv.org/abs/2412.17589) <br> | arXiv | 2024 | [Github](https://github.com/GAIR-NLP/PC-Agent) | Desktop cognitive agent |

---

## Recommended Datasets / Benchmarks

> This section is not paper-only. It includes core GUI-agent benchmarks plus related UI, web, mobile, and computer-use datasets that support training or evaluation.

|  Title  | Platform | Task Type |   Venue   |   Date   |   Code   |
|:--------|:--------:|:---------:|:---------:|:--------:|:--------:|
| ![Star](https://img.shields.io/github/stars/OSU-NLP-Group/Mind2Web.svg?style=social&label=Star) <br> [**Mind2Web**](https://arxiv.org/abs/2306.06070) | Web | Web task automation | arXiv | 2023 | [Github](https://github.com/OSU-NLP-Group/Mind2Web) |
| ![Star](https://img.shields.io/github/stars/web-arena-x/webarena.svg?style=social&label=Star) <br> [**WebArena**](https://arxiv.org/abs/2307.13854) | Web | Realistic web environment | arXiv | 2023 | [Github](https://github.com/web-arena-x/webarena) |
| ![Star](https://img.shields.io/github/stars/web-arena-x/visualwebarena.svg?style=social&label=Star) <br> [**VisualWebArena**](https://arxiv.org/abs/2401.13649) | Web | Visual web tasks | ACL | 2024 | [Github](https://github.com/web-arena-x/visualwebarena) |
| ![Star](https://img.shields.io/github/stars/princeton-nlp/WebShop.svg?style=social&label=Star) <br> [**WebShop**](https://arxiv.org/abs/2207.01206) | Web | Related web-interaction foundation | NeurIPS | 2022 | [Github](https://github.com/princeton-nlp/WebShop) |
| ![Star](https://img.shields.io/github/stars/McGill-NLP/weblinx.svg?style=social&label=Star) <br> [**WebLINX**](https://arxiv.org/abs/2402.05930) | Web | Multi-turn web navigation | arXiv | 2024 | [Github](https://github.com/McGill-NLP/weblinx) |
| ![Star](https://img.shields.io/github/stars/google-research/google-research.svg?style=social&label=Star) <br> [**Android in the Wild**](https://arxiv.org/abs/2307.10088) | Mobile | Android control | arXiv | 2023 | [Github](https://github.com/google-research/google-research/tree/master/android_in_the_wild) |
| [**Rico**](https://dl.acm.org/doi/10.1145/3126594.3126651) | Mobile | Related UI dataset | UIST | 2017 | [Dataset](https://www.interactionmining.org/archive/rico) |
| ![Star](https://img.shields.io/github/stars/njucckevin/SeeClick.svg?style=social&label=Star) <br> [**ScreenSpot**](https://arxiv.org/abs/2401.10935) | Web / Mobile / Desktop | GUI grounding | ACL | 2024 | [Github](https://github.com/njucckevin/SeeClick) |
| ![Star](https://img.shields.io/github/stars/xlang-ai/OSWorld.svg?style=social&label=Star) <br> [**OSWorld**](https://arxiv.org/abs/2404.07972) | Desktop | Open-ended computer tasks | arXiv | 2024 | [Github](https://github.com/xlang-ai/OSWorld) |
| [**OmniACT**](https://arxiv.org/abs/2402.17553) | Web / Desktop | Generalist autonomous agents | arXiv | 2024 | [Data](https://huggingface.co/datasets/Writer/omniact) |
| ![Star](https://img.shields.io/github/stars/OpenGVLab/GUI-Odyssey.svg?style=social&label=Star) <br> [**GUI Odyssey**](https://arxiv.org/abs/2406.08451) | Mobile | Cross-app navigation | arXiv | 2024 | [Github](https://github.com/OpenGVLab/GUI-Odyssey) |
| [**VisualWebBench**](https://arxiv.org/abs/2404.05955) | Web | Web understanding / grounding | arXiv | 2024 | [Github](https://github.com/VisualWebBench/VisualWebBench) |
| ![Star](https://img.shields.io/github/stars/deepmind/android_env.svg?style=social&label=Star) <br> [**AndroidEnv**](https://arxiv.org/abs/2105.13231) | Mobile | Related Android-control platform | arXiv | 2021 | [Github](https://github.com/deepmind/android_env) |
| ![Star](https://img.shields.io/github/stars/skyworkai/agent-studio.svg?style=social&label=Star) <br> [**AgentStudio**](https://arxiv.org/abs/2403.17918) | Cross-platform | General virtual agents | arXiv | 2024 | [Github](https://github.com/skyworkai/agent-studio) |
| ![Star](https://img.shields.io/github/stars/LlamaTouch/LlamaTouch.svg?style=social&label=Star) <br> [**LlamaTouch**](https://arxiv.org/abs/2404.16054) | Mobile | Mobile UI automation evaluation | arXiv | 2024 | [Github](https://github.com/LlamaTouch/LlamaTouch) |
| ![Star](https://img.shields.io/github/stars/MobileAgentBench/mobile-agent-bench.svg?style=social&label=Star) <br> [**MobileAgentBench**](https://arxiv.org/abs/2406.08184) | Mobile | Mobile LLM agent benchmark | arXiv | 2024 | [Github](https://github.com/MobileAgentBench/mobile-agent-bench) |
| ![Star](https://img.shields.io/github/stars/google-research/android_world.svg?style=social&label=Star) <br> [**AndroidWorld**](https://arxiv.org/abs/2405.14573) | Mobile | Dynamic benchmarking environment | arXiv | 2024 | [Github](https://github.com/google-research/android_world) |
| ![Star](https://img.shields.io/github/stars/camel-ai/crab.svg?style=social&label=Star) <br> [**CRAB**](https://arxiv.org/abs/2407.01511) | Cross-environment | Multimodal agent benchmark | arXiv | 2024 | [Github](https://github.com/camel-ai/crab) |
| ![Star](https://img.shields.io/github/stars/xlang-ai/Spider2-V.svg?style=social&label=Star) <br> [**Spider2-V**](https://arxiv.org/abs/2407.10956) | Desktop | Data science workflows | arXiv | 2024 | [Github](https://github.com/xlang-ai/Spider2-V) |
| ![Star](https://img.shields.io/github/stars/YuxiangChai/AMEX-codebase.svg?style=social&label=Star) <br> [**AMEX**](https://arxiv.org/abs/2407.17490) | Mobile | Android multi-annotation dataset | arXiv | 2024 | [Github](https://github.com/YuxiangChai/AMEX-codebase) |
| ![Star](https://img.shields.io/github/stars/microsoft/WindowsAgentArena.svg?style=social&label=Star) <br> [**Windows Agent Arena**](https://arxiv.org/abs/2409.08264) | Desktop | Windows OS agent benchmark | arXiv | 2024 | [Github](https://github.com/microsoft/WindowsAgentArena) |
| [**SPA-Bench**](https://arxiv.org/abs/2410.15164) | Mobile | Smartphone agent evaluation | ICLR | 2025 | [Website](https://ai-agents-2030.github.io/SPA-Bench/) |
| ![Star](https://img.shields.io/github/stars/likaixin2000/ScreenSpot-Pro-GUI-Grounding.svg?style=social&label=Star) <br> [**ScreenSpot-Pro**](https://arxiv.org/abs/2504.07981) | Desktop | Professional GUI grounding | arXiv | 2025 | [Github](https://github.com/likaixin2000/ScreenSpot-Pro-GUI-Grounding) |
| ![Star](https://img.shields.io/github/stars/showlab/WorldGUI.svg?style=social&label=Star) <br> [**WorldGUI**](https://arxiv.org/abs/2502.08047) | Desktop | Dynamic desktop GUI testing | arXiv | 2025 | [Github](https://github.com/showlab/WorldGUI) |
| ![Star](https://img.shields.io/github/stars/OS-Copilot/ScienceBoard.svg?style=social&label=Star) <br> [**ScienceBoard**](https://arxiv.org/abs/2505.19897) | Desktop | Scientific workflow evaluation | arXiv | 2025 | [Github](https://github.com/OS-Copilot/ScienceBoard) |
| ![Star](https://img.shields.io/github/stars/lgy0404/LearnAct.svg?style=social&label=Star) <br> [**LearnAct**](https://arxiv.org/abs/2504.13805) | Mobile | Few-shot mobile GUI agent data | arXiv | 2025 | [Github](https://github.com/lgy0404/LearnAct) |
| ![Star](https://img.shields.io/github/stars/Alibaba-nlp/WebWalker.svg?style=social&label=Star) <br> [**WebWalker**](https://github.com/Alibaba-nlp/WebWalker) | Web | Web traversal benchmark | arXiv | 2025 | [Github](https://github.com/Alibaba-nlp/WebWalker) |
| [**A3: Android Agent Arena**](https://arxiv.org/abs/2501.01149) | Mobile | Mobile GUI agent evaluation | arXiv | 2025 | [Website](https://yuxiangchai.github.io/Android-Agent-Arena/) |
| ![Star](https://img.shields.io/github/stars/runamu/monday.svg?style=social&label=Star) <br> [**MONDAY**](https://arxiv.org/abs/2505.12632) | Mobile | Video-to-dataset generation | CVPR | 2025 | [Github](https://github.com/runamu/monday) |
| ![Star](https://img.shields.io/github/stars/ServiceNow/BrowserGym.svg?style=social&label=Star) <br> [**BrowserGym**](https://arxiv.org/abs/2412.05467) | Web | Web-agent research ecosystem | arXiv | 2024 | [Github](https://github.com/ServiceNow/BrowserGym) |
| ![Star](https://img.shields.io/github/stars/ServiceNow/WorkArena.svg?style=social&label=Star) <br> [**WorkArena**](https://arxiv.org/abs/2403.07718) | Web / Enterprise | Knowledge-work tasks | arXiv | 2024 | [Github](https://github.com/ServiceNow/WorkArena) |
| ![Star](https://img.shields.io/github/stars/ServiceNow/WorkArena.svg?style=social&label=Star) <br> [**WorkArena++**](https://arxiv.org/abs/2407.05291) | Web / Enterprise | Compositional planning tasks | arXiv | 2024 | [Github](https://github.com/ServiceNow/WorkArena) |
| [**WebCanvas**](https://arxiv.org/abs/2406.12373) | Web | Online web-agent benchmark | arXiv | 2024 | [Paper](https://arxiv.org/abs/2406.12373) |
| [**WebQuest**](https://arxiv.org/abs/2409.13711) | Web | Multimodal QA on web page sequences | arXiv | 2024 | [Paper](https://arxiv.org/abs/2409.13711) |
| [**Mobile-Env**](https://arxiv.org/abs/2305.08144) | Mobile | LLM-GUI interaction benchmark | arXiv | 2023 | [Paper](https://arxiv.org/abs/2305.08144) |
| [**Mobile-Bench**](https://arxiv.org/abs/2407.00993) | Mobile | LLM-based mobile-agent benchmark | arXiv | 2024 | [Paper](https://arxiv.org/abs/2407.00993) |
| ![Star](https://img.shields.io/github/stars/open-compass/MMBench-GUI.svg?style=social&label=Star) <br> [**MMBench-GUI**](https://arxiv.org/abs/2507.19478) | Cross-platform | Hierarchical multi-platform evaluation | arXiv | 2025 | [Github](https://github.com/open-compass/MMBench-GUI) |
| [**macOSWorld**](https://arxiv.org/abs/2506.04135) | Desktop | Multilingual macOS interactive benchmark | arXiv | 2025 | [Website](https://macos-world.github.io) |
| ![Star](https://img.shields.io/github/stars/SAAgent/MCPWorld.svg?style=social&label=Star) <br> [**MCPWorld**](https://arxiv.org/abs/2506.07672) | API / GUI / Hybrid | Unified computer-use benchmark | arXiv | 2025 | [Github](https://github.com/SAAgent/MCPWorld) |
| ![Star](https://img.shields.io/github/stars/KeLes-Coding/NatureGAIA.svg?style=social&label=Star) <br> [**NaturalGAIA**](https://arxiv.org/abs/2508.01330) | Desktop / Web | Verifiable long-horizon GUI tasks | arXiv | 2025 | [Github](https://github.com/KeLes-Coding/NatureGAIA) |
| ![Star](https://img.shields.io/github/stars/OpenGVLab/ScaleCUA.svg?style=social&label=Star) <br> [**ScaleCUA**](https://arxiv.org/abs/2509.15221) | Cross-platform | Cross-platform computer-use data | arXiv | 2025 | [Github](https://github.com/OpenGVLab/ScaleCUA) |
| ![Star](https://img.shields.io/github/stars/OS-Copilot/OS-Map.svg?style=social&label=Star) <br> [**OS-MAP**](https://arxiv.org/abs/2507.19132) | Desktop | Breadth-depth computer-use evaluation | arXiv | 2025 | [Github](https://github.com/OS-Copilot/OS-Map) |
| [**OSWorld-MCP**](https://arxiv.org/abs/2510.24563) | Desktop / Tool | MCP tool invocation benchmark | arXiv | 2025 | [Website](https://osworld-mcp.github.io) |
| [**GUI-360**](https://arxiv.org/abs/2511.04307) | Cross-platform | Computer-using agent dataset / benchmark | arXiv | 2025 | [Data](https://huggingface.co/datasets/vyokky/GUI-360) |
| [**VenusBench-Mobile**](https://arxiv.org/abs/2604.06182) | Mobile | User-centric mobile GUI benchmark | arXiv | 2026 | [Github](https://github.com/inclusionAI/UI-Venus/tree/VenusBench-Mobile) |
| [**VenusBench-GD**](https://arxiv.org/abs/2512.16501) | Cross-platform | Diverse GUI grounding tasks | arXiv | 2025 | [Paper](https://arxiv.org/abs/2512.16501) |
| ![Star](https://img.shields.io/github/stars/wwh0411/FedGUI.svg?style=social&label=Star) <br> [**FedGUI**](https://arxiv.org/abs/2604.14956) | Cross-platform | Federated GUI-agent benchmark | arXiv | 2026 | [Github](https://github.com/wwh0411/FedGUI) |
| [**OpenComputer**](https://arxiv.org/abs/2605.19769) | Desktop | Verifiable software worlds | arXiv | 2026 | [Paper](https://arxiv.org/abs/2605.19769) |
| [**CUA-Gym**](https://arxiv.org/abs/2605.25624) | Web / Desktop | Verifiable RLVR training environments | arXiv | 2026 | [Paper](https://arxiv.org/abs/2605.25624) |
| [**MobileGym**](https://arxiv.org/abs/2605.26114) | Mobile | Parallel simulation platform | arXiv | 2026 | [Website](https://mobilegym.github.io) |
| [**AndroidDaily**](https://arxiv.org/abs/2605.27761) | Mobile | Verifiable closed-source app tasks | arXiv | 2026 | [Paper](https://arxiv.org/abs/2605.27761) |
| ![Star](https://img.shields.io/github/stars/UniPat-AI/SaaS-Bench.svg?style=social&label=Star) <br> [**SaaS-Bench**](https://arxiv.org/abs/2605.15777) | Web / SaaS | Professional workflow benchmark | arXiv | 2026 | [Github](https://github.com/UniPat-AI/SaaS-Bench) |
| ![Star](https://img.shields.io/github/stars/ZZZhr-1/WinDeskGround.svg?style=social&label=Star) <br> [**WinDeskGround**](https://arxiv.org/abs/2605.16402) | Desktop | Multi-window GUI grounding | arXiv | 2026 | [Github](https://github.com/ZZZhr-1/WinDeskGround) |
| [**AgentHijack**](https://arxiv.org/abs/2605.25707) | Desktop | Robustness under environment corruptions | ICML | 2026 | [Website](https://AgentHijack.github.io) |
| ![Star](https://img.shields.io/github/stars/AlibabaResearch/RoTS.svg?style=social&label=Star) <br> [**GUI-RobustEval / RoTS**](https://arxiv.org/abs/2605.29447) | Cross-platform | Error recovery benchmark and synthesis | ICML | 2026 | [Github](https://github.com/AlibabaResearch/RoTS) |
| [**WindowsWorld**](https://arxiv.org/abs/2604.27776) | Desktop | Process-centric professional workflows | arXiv | 2026 | [Paper](https://arxiv.org/abs/2604.27776) |
| [**CUA-Suite**](https://arxiv.org/abs/2603.24440) | Cross-platform | Human-annotated video demonstrations | arXiv | 2026 | [Paper](https://arxiv.org/abs/2603.24440) |
| [**A11y-CUA Dataset**](https://arxiv.org/abs/2602.09310) | Cross-platform | Accessibility-gap evaluation | arXiv | 2026 | [Paper](https://arxiv.org/abs/2602.09310) |
| [**OS-Marathon**](https://arxiv.org/abs/2601.20650) | Desktop | Long-horizon repetitive tasks | arXiv | 2026 | [Website](https://os-marathon.github.io/) |
| [**ProSoftArena**](https://arxiv.org/abs/2601.02399) | Desktop | Professional software environments | arXiv | 2025 | [Website](https://prosoftarena.github.io) |
| ![Star](https://img.shields.io/github/stars/friedrichor/WebTestBench.svg?style=social&label=Star) <br> [**WebTestBench**](https://arxiv.org/abs/2603.25226) | Web | End-to-end automated web testing | arXiv | 2026 | [Github](https://github.com/friedrichor/WebTestBench) |
| [**Odysseys**](https://arxiv.org/abs/2604.24964) | Web | Realistic long-horizon web tasks | arXiv | 2026 | [Website](https://odysseys-website.pages.dev) |
| [**SecureWebArena**](https://arxiv.org/abs/2510.10073) | Web | Security evaluation for LVLM web agents | arXiv | 2025 | [Paper](https://arxiv.org/abs/2510.10073) |
| [**GUIDE-Bench**](https://arxiv.org/abs/2603.25864) | GUI | Open-ended user assistance tasks | arXiv | 2026 | [Website](https://guide-bench.github.io) |
| [**OmniGUI**](https://arxiv.org/abs/2605.18758) | Mobile | Omni-modal smartphone environments | arXiv | 2026 | [Website](https://omni-gui.github.io) |
| [**UI-Vision**](https://arxiv.org/abs/2503.15661) | Desktop | Visual perception and interaction | arXiv | 2025 | [Paper](https://arxiv.org/abs/2503.15661) |
| [**Mobile-Bench-v2**](https://arxiv.org/abs/2505.11891) | Mobile | Realistic mobile-agent benchmark | arXiv | 2025 | [Data](https://huggingface.co/datasets/xwk123/MobileBench-v2) |
| [**MVISU-Bench**](https://arxiv.org/abs/2508.09057) | Mobile | Multi-app / vague / interactive tasks | ACM MM | 2025 | [Paper](https://arxiv.org/abs/2508.09057) |
| [**MAS-Bench**](https://arxiv.org/abs/2509.06477) | Mobile | Shortcut-augmented hybrid agents | arXiv | 2025 | [Website](https://pengxiang-zhao.github.io/MAS-Bench) |
| ![Star](https://img.shields.io/github/stars/MadeAgents/ColorBench.svg?style=social&label=Star) <br> [**ColorBench**](https://arxiv.org/abs/2510.14621) | Mobile | Long-horizon graph-structured tasks | arXiv | 2025 | [Github](https://github.com/MadeAgents/ColorBench) |
| [**MobiBench**](https://arxiv.org/abs/2512.12634) | Mobile | Multi-branch modular benchmark | arXiv | 2025 | [Paper](https://arxiv.org/abs/2512.12634) |
| ![Star](https://img.shields.io/github/stars/jacklishufan/MobileWorld.svg?style=social&label=Star) <br> [**MobileWorldBench**](https://arxiv.org/abs/2512.14014) | Mobile | Semantic world modeling | arXiv | 2025 | [Github](https://github.com/jacklishufan/MobileWorld) |
| [**MobileWorld**](https://arxiv.org/abs/2512.19432) | Mobile | Agent-user interactive and MCP-augmented environments | arXiv | 2025 | [Paper](https://arxiv.org/abs/2512.19432) |
| [**OpenApps**](https://arxiv.org/abs/2511.20766) | Mobile / UI | Environment-variation reliability | arXiv | 2025 | [Website](https://facebookresearch.github.io/OpenApps/) |
| [**DiffSpot**](https://arxiv.org/abs/2605.29615) | Web | Fine-grained visual difference spotting | arXiv | 2026 | [Paper](https://arxiv.org/abs/2605.29615) |
| [**WebChain**](https://arxiv.org/abs/2603.05295) | Web | Human-annotated web interaction traces | arXiv | 2026 | [Paper](https://arxiv.org/abs/2603.05295) |
| [**WebSP-Eval**](https://arxiv.org/abs/2604.06367) | Web | Website security and privacy tasks | arXiv | 2026 | [Paper](https://arxiv.org/abs/2604.06367) |
| [**GameWorld**](https://arxiv.org/abs/2604.07429) | Game / GUI | Verifiable multimodal game-agent evaluation | arXiv | 2026 | [Website](https://gameworld-bench.github.io) |
| [**HealthAdminBench**](https://arxiv.org/abs/2604.09937) | Desktop / Web | Healthcare administration workflows | arXiv | 2026 | [Paper](https://arxiv.org/abs/2604.09937) |
| [**EntWorld**](https://arxiv.org/abs/2601.17722) | Enterprise GUI | Verifiable enterprise GUI tasks | arXiv | 2026 | [Paper](https://arxiv.org/abs/2601.17722) |
| [**GUI-CEval**](https://arxiv.org/abs/2603.15039) | Mobile | Chinese mobile GUI benchmark | arXiv | 2026 | [Paper](https://arxiv.org/abs/2603.15039) |
| [**MemGUI-Bench**](https://arxiv.org/abs/2602.06075) | Mobile | Dynamic memory benchmark | arXiv | 2026 | [Website](https://lgy0404.github.io/MemGUI-Bench/) |
| [**GUIGuard-Bench**](https://arxiv.org/abs/2601.18842) | GUI | Privacy-preserving GUI-agent evaluation | arXiv | 2026 | [Website](https://futuresis.github.io/GUIGuard-page/) |
| [**KnowU-Bench**](https://arxiv.org/abs/2604.08455) | Mobile | Interactive proactive personalized evaluation | arXiv | 2026 | [Paper](https://arxiv.org/abs/2604.08455) |
| [**PhoneWorld**](https://arxiv.org/abs/2605.29486) | Mobile | Scalable phone-use environments | arXiv | 2026 | [Paper](https://arxiv.org/abs/2605.29486) |
| [**ProactiveMobile**](https://arxiv.org/abs/2602.21858) | Mobile | Proactive mobile intelligence benchmark | arXiv | 2026 | [Paper](https://arxiv.org/abs/2602.21858) |
| [**AmbiBench**](https://arxiv.org/abs/2602.11750) | Mobile | Beyond one-shot instructions | arXiv | 2026 | [Paper](https://arxiv.org/abs/2602.11750) |
| [**WebTestPilot**](https://arxiv.org/abs/2602.11724) | Web | Agentic end-to-end web testing | arXiv | 2026 | [Paper](https://arxiv.org/abs/2602.11724) |

---

## Model / Data Collections

> Model checkpoints, data collections, and code-linked resources are grouped here when the released artifact is as important as the paper.

|  Name  | Type | Platform | Link |
|:-------|:----:|:--------:|:-----|
| [**OpenCUA / AgentNet**](https://arxiv.org/abs/2508.09123) | Model / data / benchmark | Computer use | [Github](https://github.com/xlang-ai/OpenCUA) |
| [**UI-Venus Collection**](https://arxiv.org/abs/2602.09082) | Model / data collection | Cross-platform GUI | [Hugging Face](https://huggingface.co/collections/inclusionAI/ui-venus) |
| [**EvoCUA Collection**](https://arxiv.org/abs/2601.15876) | Model checkpoints | Computer use | [Hugging Face](https://huggingface.co/collections/harbingeva/evocua-687c664a9bb7b48f2272ff8a) |
| ![Star](https://img.shields.io/github/stars/microsoft/Phi-Ground.svg?style=social&label=Star) [**Phi-Ground**](https://arxiv.org/abs/2507.23779) | Model / benchmark | GUI grounding | [Github](https://github.com/microsoft/Phi-Ground) |
| ![Star](https://img.shields.io/github/stars/OpenGVLab/ScaleCUA.svg?style=social&label=Star) [**ScaleCUA**](https://arxiv.org/abs/2509.15221) | Cross-platform data | Computer use | [Github](https://github.com/OpenGVLab/ScaleCUA) |
| [**GUI-360**](https://arxiv.org/abs/2511.04307) | Dataset / benchmark | Computer use | [Hugging Face](https://huggingface.co/datasets/vyokky/GUI-360) |
| [**CMGUI**](https://arxiv.org/abs/2603.08533) | Dataset | Mobile GUI | [Hugging Face](https://huggingface.co/datasets/alibabagroup/CMGUI) |
| [**WildGUI**](https://arxiv.org/abs/2605.14747) | Video-derived trajectory data | Cross-platform GUI | [Paper](https://arxiv.org/abs/2605.14747) |
| [**CUA-Suite**](https://arxiv.org/abs/2603.24440) | Human-annotated video demonstrations | Computer use | [Paper](https://arxiv.org/abs/2603.24440) |
| ![Star](https://img.shields.io/github/stars/AlibabaResearch/RoTS.svg?style=social&label=Star) [**RoTS Data**](https://arxiv.org/abs/2605.29447) | Error-recovery trajectories | GUI agents | [Github](https://github.com/AlibabaResearch/RoTS) |
| [**A11y-CUA Dataset**](https://arxiv.org/abs/2602.09310) | Accessibility-oriented data | Computer use | [Paper](https://arxiv.org/abs/2602.09310) |
| ![Star](https://img.shields.io/github/stars/tsinghua-fib-lab/FingerTip-20K.svg?style=social&label=Star) [**FingerTip 20K**](https://arxiv.org/abs/2507.21071) | Proactive / personalized mobile data | Mobile | [Github](https://github.com/tsinghua-fib-lab/FingerTip-20K) |
| ![Star](https://img.shields.io/github/stars/V-Droid-Agent/V-Droid.svg?style=social&label=Star) [**V-Droid**](https://arxiv.org/abs/2503.15937) | Verifier-driven deployment framework | Mobile GUI | [Github](https://github.com/V-Droid-Agent/V-Droid) |
| ![Star](https://img.shields.io/github/stars/lll6gg/UI-R1.svg?style=social&label=Star) [**UI-R1**](https://arxiv.org/abs/2503.21620) | RL action-prediction model | GUI agents | [Github](https://github.com/lll6gg/UI-R1) |
| [**DeskVision**](https://arxiv.org/abs/2503.11170) | Desktop region captions | Desktop GUI | [Paper](https://arxiv.org/abs/2503.11170) |
| [**ScreenParse**](https://arxiv.org/abs/2602.14276) | Complete screen parsing supervision | Computer use | [Project](https://saidgurbuz.github.io/screenparse/) |
| [**WebChain**](https://arxiv.org/abs/2603.05295) | Human-annotated web traces | Web | [Paper](https://arxiv.org/abs/2603.05295) |
| [**MolmoWeb**](https://arxiv.org/abs/2604.08516) | Open visual web-agent data | Web | [Paper](https://arxiv.org/abs/2604.08516) |
| [**OpenMobile**](https://arxiv.org/abs/2604.15093) | Task / trajectory synthesis | Mobile | [Project](https://njucckevin.github.io/openmobile/) |
| [**OpenApps**](https://arxiv.org/abs/2511.20766) | UI environment variations | Mobile / UI | [Website](https://facebookresearch.github.io/OpenApps/) |
| ![Star](https://img.shields.io/github/stars/jacklishufan/MobileWorld.svg?style=social&label=Star) [**MobileWorldBench**](https://arxiv.org/abs/2512.14014) | Semantic world-modeling data | Mobile | [Github](https://github.com/jacklishufan/MobileWorld) |
| [**PhoneWorld**](https://arxiv.org/abs/2605.29486) | Phone-use environments | Mobile | [Paper](https://arxiv.org/abs/2605.29486) |
| [**MobileViews**](https://arxiv.org/abs/2409.14337) | Million-scale mobile GUI data | Mobile | [Hugging Face](https://huggingface.co/datasets/mllmTeam/MobileViews) |
| ![Star](https://img.shields.io/github/stars/UbiquitousLearning/DroidCall.svg?style=social&label=Star) [**DroidCall**](https://arxiv.org/abs/2412.00402) | Android intent invocation dataset | Mobile | [Github](https://github.com/UbiquitousLearning/DroidCall) |
| ![Star](https://img.shields.io/github/stars/MobileLLM/AutoDroid-V2.svg?style=social&label=Star) [**AutoDroid-V2**](https://arxiv.org/abs/2412.18116) | Code-generation GUI-agent framework | Mobile | [Github](https://github.com/MobileLLM/AutoDroid-V2) |
| ![Star](https://img.shields.io/github/stars/caap-agent/caap-agent.svg?style=social&label=Star) [**CAAP**](https://arxiv.org/abs/2406.06947) | Front-end-UI-only computer-task agent | Web / GUI | [Github](https://github.com/caap-agent/caap-agent) |
| [**DroidBot-GPT**](https://arxiv.org/abs/2304.07061) | GPT-powered Android UI automation | Mobile | [Paper](https://arxiv.org/abs/2304.07061) |

---

## Recent Research

### ICML 2026
+ ![Star](https://img.shields.io/github/stars/AlibabaResearch/RoTS.svg?style=social&label=Star) [Recovering Policy-Induced Errors: Benchmarking and Trajectory Synthesis for Robust GUI Agents](https://arxiv.org/abs/2605.29447) [[code]](https://github.com/AlibabaResearch/RoTS)
+ [AgentHijack: Benchmarking Computer Use Agent Robustness to Common Environment Corruptions](https://arxiv.org/abs/2605.25707) [[website]](https://AgentHijack.github.io)
+ [Agent JIT Compilation for Latency-Optimizing Web Agent Planning and Scheduling](https://arxiv.org/abs/2605.21470)
+ [Video2GUI: Synthesizing Large-Scale Interaction Trajectories for Generalized GUI Agent Pretraining](https://arxiv.org/abs/2605.14747)

### AAAI 2026
+ ![Star](https://img.shields.io/github/stars/TongUI-agent/TongUI-agent.svg?style=social&label=Star) [TongUI: Internet-Scale Trajectories from Multimodal Web Tutorials for Generalized GUI Agents](https://arxiv.org/abs/2504.12679) [[code]](https://github.com/TongUI-agent/TongUI-agent)

### arXiv 2026
+ ![Star](https://img.shields.io/github/stars/inclusionAI/UI-Venus.svg?style=social&label=Star) [UI-Venus-1.5 Technical Report](https://arxiv.org/abs/2602.09082) [[code]](https://github.com/inclusionAI/UI-Venus) [[model]](https://huggingface.co/collections/inclusionAI/ui-venus)
+ ![Star](https://img.shields.io/github/stars/Neur-IO/BAMI.svg?style=social&label=Star) [BAMI: Training-Free Bias Mitigation in GUI Grounding](https://arxiv.org/abs/2605.06664) (Tech Report 2026) [[project]](https://github.com/Neur-IO/BAMI)
+ [EvoCUA: Evolving Computer Use Agents via Learning from Scalable Synthetic Experience](https://arxiv.org/abs/2601.15876) [[model]](https://huggingface.co/collections/harbingeva/evocua-687c664a9bb7b48f2272ff8a)
+ ![Star](https://img.shields.io/github/stars/X-PLUG/MobileAgent.svg?style=social&label=Star) [Mobile-Agent-v3.5: Multi-platform Fundamental GUI Agents](https://arxiv.org/abs/2602.16855) [[code]](https://github.com/X-PLUG/MobileAgent)
+ ![Star](https://img.shields.io/github/stars/UITron-hub/TreeCUA.svg?style=social&label=Star) [TreeCUA: Efficiently Scaling GUI Automation with Tree-Structured Verifiable Evolution](https://arxiv.org/abs/2602.09662) [[code]](https://github.com/UITron-hub/TreeCUA)
+ [OpenComputer: Verifiable Software Worlds for Computer-Use Agents](https://arxiv.org/abs/2605.19769)
+ [CUA-Gym: Scaling Verifiable Training Environments and Tasks for Computer-Use Agents](https://arxiv.org/abs/2605.25624)
+ [MobileGym: A Verifiable and Highly Parallel Simulation Platform for Mobile GUI Agent Research](https://arxiv.org/abs/2605.26114) [[website]](https://mobilegym.github.io)
+ [AndroidDaily: A Verifiable Benchmark for Mobile GUI Agents on Real-World Closed-Source Applications](https://arxiv.org/abs/2605.27761)
+ ![Star](https://img.shields.io/github/stars/Wuzheng02/GUI-CIDER.svg?style=social&label=Star) [GUI-CIDER: Mid-training GUI Agents via Causal Internalization and Density-aware Exemplar Reselection](https://arxiv.org/abs/2605.28534) [[code]](https://github.com/Wuzheng02/GUI-CIDER)
+ ![Star](https://img.shields.io/github/stars/ZZZhr-1/WinDeskGround.svg?style=social&label=Star) [WinDeskGround: A Benchmark for Robust GUI Grounding in Complex Multi-Window Desktop Environments](https://arxiv.org/abs/2605.16402) [[code]](https://github.com/ZZZhr-1/WinDeskGround)
+ ![Star](https://img.shields.io/github/stars/linjiaping1/Re-Prefill.svg?style=social&label=Star) [What Happens Before Decoding? Prefill Determines GUI Grounding in VLMs](https://arxiv.org/abs/2605.12549) [[code]](https://github.com/linjiaping1/Re-Prefill)
+ [Learn where to Click from Yourself: On-Policy Self-Distillation for GUI Grounding](https://arxiv.org/abs/2605.00642) [[project]](https://zhangyan-ucas.github.io/GUI-SD/)
+ [PRO-CUA: Process-Reward Optimization for Computer Use Agents](https://arxiv.org/abs/2605.29119)
+ [Learn from Weaknesses: Automated Domain Specialization for Small Computer-Use Agents](https://arxiv.org/abs/2605.28775)
+ [DiffSpot: Can VLMs Spot Fine-Grained Visual Differences in Web Interfaces?](https://arxiv.org/abs/2605.29615)
+ [PhoneWorld: Scaling Phone-Use Agent Environments](https://arxiv.org/abs/2605.29486)
+ [MementoGUI: Learning Agentic Multimodal Memory Control for Long-Horizon GUI Agents](https://arxiv.org/abs/2605.18652)
+ [ReVision: Scaling Computer-Use Agents via Temporal Visual Redundancy Reduction](https://arxiv.org/abs/2605.11212)
+ [Covering Human Action Space for Computer Use: Data Synthesis and Benchmark](https://arxiv.org/abs/2605.12501) [[code]](https://github.com/microsoft/Phi-Ground)
+ ![Star](https://img.shields.io/github/stars/UniPat-AI/SaaS-Bench.svg?style=social&label=Star) [SaaS-Bench: Can Computer-Use Agents Leverage Real-World SaaS to Solve Professional Workflows?](https://arxiv.org/abs/2605.15777) [[code]](https://github.com/UniPat-AI/SaaS-Bench)
+ [DocOS: Towards Proactive Document-Guided Actions in GUI Agents](https://arxiv.org/abs/2605.18048)
+ [ScreenSearch: Uncertainty-Aware OS Exploration](https://arxiv.org/abs/2605.16024)
+ [HealthAdminBench: Evaluating Computer-Use Agents on Healthcare Administration Tasks](https://arxiv.org/abs/2604.09937)
+ [MolmoWeb: Open Visual Web Agent and Open Data for the Open Web](https://arxiv.org/abs/2604.08516)
+ [OpenMobile: Building Open Mobile Agents with Task and Trajectory Synthesis](https://arxiv.org/abs/2604.15093) [[project]](https://njucckevin.github.io/openmobile/)
+ [GameWorld: Towards Standardized and Verifiable Evaluation of Multimodal Game Agents](https://arxiv.org/abs/2604.07429) [[website]](https://gameworld-bench.github.io)
+ [Gym-Anything: Turn any Software into an Agent Environment](https://arxiv.org/abs/2604.06126)
+ [GUIDE: Interpretable GUI Agent Evaluation via Hierarchical Diagnosis](https://arxiv.org/abs/2604.04399)
+ [Don't Act Blindly: Robust GUI Automation via Action-Effect Verification and Self-Correction](https://arxiv.org/abs/2604.05477)
+ [OS-Themis: A Scalable Critic Framework for Generalist GUI Rewards](https://arxiv.org/abs/2603.19191)
+ [AndroTMem: From Interaction Trajectories to Anchored Memory in Long-Horizon GUI Agents](https://arxiv.org/abs/2603.18429) [[code]](https://github.com/CVC2233/AndroTMem)
+ [ScreenParse: Moving Beyond Sparse Grounding with Complete Screen Parsing Supervision](https://arxiv.org/abs/2602.14276) [[project]](https://saidgurbuz.github.io/screenparse/)
+ [ActionEngine: From Reactive to Programmatic GUI Agents via State Machine Memory](https://arxiv.org/abs/2602.20502)
+ [UI-Mem: Self-Evolving Experience Memory for Online Reinforcement Learning in Mobile GUI Agents](https://arxiv.org/abs/2602.05832) [[project]](https://ui-mem.github.io)
+ [ToolTok: Tool Tokenization for Efficient and Generalizable GUI Agents](https://arxiv.org/abs/2602.02548) [[code]](https://github.com/ZephinueCode/ToolTok)
+ [Agent Alpha: Tree Search Unifying Generation, Exploration and Evaluation for Computer-Use Agents](https://arxiv.org/abs/2602.02995)
+ [MemGUI-Bench: Benchmarking Memory of Mobile GUI Agents in Dynamic Environments](https://arxiv.org/abs/2602.06075) [[website]](https://lgy0404.github.io/MemGUI-Bench/)
+ [GUIGuard-Bench: Toward a General Evaluation for Privacy-Preserving GUI Agents](https://arxiv.org/abs/2601.18842) [[website]](https://futuresis.github.io/GUIGuard-page/)
+ [EntWorld: A Holistic Environment and Benchmark for Verifiable Enterprise GUI Agents](https://arxiv.org/abs/2601.17722)
+ [GUI-GENESIS: Automated Synthesis of Efficient Environments with Verifiable Rewards for GUI Agent Post-Training](https://arxiv.org/abs/2602.14093)
+ [AutoWebWorld: Synthesizing Infinite Verifiable Web Environments via Finite State Machines](https://arxiv.org/abs/2602.14296)
+ [OS-Marathon: Benchmarking Computer-Use Agents on Long-Horizon Repetitive Tasks](https://arxiv.org/abs/2601.20650) [[website]](https://os-marathon.github.io/)
+ [CaMeLs Can Use Computers Too: System-level Security for Computer Use Agents](https://arxiv.org/abs/2601.09923)

### CVPR 2025
+ ![Star](https://img.shields.io/github/stars/showlab/ShowUI.svg?style=social&label=Star) [ShowUI: One Vision-Language-Action Model for GUI Visual Agent](https://arxiv.org/abs/2411.17465) [[code]](https://github.com/showlab/ShowUI)

### ICLR 2025
+ ![Star](https://img.shields.io/github/stars/OS-Copilot/OS-Atlas.svg?style=social&label=Star) [OS-ATLAS: A Foundation Action Model for Generalist GUI Agents](https://arxiv.org/abs/2410.23218) [[code]](https://github.com/OS-Copilot/OS-Atlas)
+ ![Star](https://img.shields.io/github/stars/OSU-NLP-Group/UGround.svg?style=social&label=Star) [UGround: Navigating the Digital World as Humans Do: Universal Visual Grounding for GUI Agents](https://arxiv.org/abs/2410.05243) [[code]](https://github.com/OSU-NLP-Group/UGround)

### ACL 2024
+ ![Star](https://img.shields.io/github/stars/njucckevin/SeeClick.svg?style=social&label=Star) [SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents](https://arxiv.org/abs/2401.10935) [[code]](https://github.com/njucckevin/SeeClick)
+ ![Star](https://img.shields.io/github/stars/web-arena-x/visualwebarena.svg?style=social&label=Star) [VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks](https://arxiv.org/abs/2401.13649) [[code]](https://github.com/web-arena-x/visualwebarena)

### CVPR 2024
+ ![Star](https://img.shields.io/github/stars/THUDM/CogAgent.svg?style=social&label=Star) [CogAgent: A Visual Language Model for GUI Agents](https://arxiv.org/abs/2312.08914) [[code]](https://github.com/THUDM/CogAgent)
+ ![Star](https://img.shields.io/github/stars/showlab/assistgui.svg?style=social&label=Star) [AssistGUI: Task-Oriented Desktop Graphical User Interface Automation](https://arxiv.org/abs/2312.13108) [[code]](https://github.com/showlab/assistgui)
+ [Dual-View Visual Contextualization for Web Navigation](https://arxiv.org/abs/2402.04476)

### ICML 2024
+ ![Star](https://img.shields.io/github/stars/OSU-NLP-Group/SeeAct.svg?style=social&label=Star) [GPT-4V(ision) is a Generalist Web Agent, if Grounded](https://arxiv.org/abs/2401.01614) [[code]](https://github.com/OSU-NLP-Group/SeeAct)

### NeurIPS
+ ![Star](https://img.shields.io/github/stars/showlab/videogui.svg?style=social&label=Star) [VideoGUI: A Benchmark for GUI Automation from Instructional Videos](https://arxiv.org/abs/2406.10227) [[code]](https://github.com/showlab/videogui) (NeurIPS 2024 D&B)
+ ![Star](https://img.shields.io/github/stars/princeton-nlp/WebShop.svg?style=social&label=Star) [WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents](https://arxiv.org/abs/2207.01206) [[code]](https://github.com/princeton-nlp/WebShop) (2022; related web-agent foundation)

### ICLR 2024
+ ![Star](https://img.shields.io/github/stars/ltzheng/synapse.svg?style=social&label=Star) [Synapse: Trajectory-as-Exemplar Prompting with Memory for Computer Control](https://arxiv.org/abs/2306.07863) [[code]](https://github.com/ltzheng/synapse)

### arXiv 2025
+ ![Star](https://img.shields.io/github/stars/bytedance/UI-TARS.svg?style=social&label=Star) [UI-TARS: Pioneering Automated GUI Interaction with Native Agents](https://arxiv.org/abs/2501.12326) [[code]](https://github.com/bytedance/UI-TARS)
+ ![Star](https://img.shields.io/github/stars/xlang-ai/OpenCUA.svg?style=social&label=Star) [OpenCUA: Open Foundations for Computer-Use Agents](https://arxiv.org/abs/2508.09123) [[code]](https://github.com/xlang-ai/OpenCUA)
+ ![Star](https://img.shields.io/github/stars/showlab/WorldGUI.svg?style=social&label=Star) [WorldGUI: An Interactive Benchmark for Desktop GUI Automation from Any Starting Point](https://arxiv.org/abs/2502.08047) (Tech Report) [[code]](https://github.com/showlab/WorldGUI)
+ ![Star](https://img.shields.io/github/stars/Reallm-Labs/InfiGUIAgent.svg?style=social&label=Star) [InfiGUIAgent: A Multimodal Generalist GUI Agent with Native Reasoning and Reflection](https://arxiv.org/abs/2501.04575) [[code]](https://github.com/Reallm-Labs/InfiGUIAgent)
+ [GUI-Bee: Align GUI Action Grounding to Novel Environments via Autonomous Exploration](https://arxiv.org/abs/2501.13896)
+ ![Star](https://img.shields.io/github/stars/OpenBMB/AgentCPM-GUI.svg?style=social&label=Star) [AgentCPM-GUI: Building Mobile-Use Agents with Reinforcement Fine-Tuning](https://arxiv.org/abs/2506.01391) [[code]](https://github.com/OpenBMB/AgentCPM-GUI)
+ ![Star](https://img.shields.io/github/stars/zju-real/gui-rcpo.svg?style=social&label=Star) [Test-Time Reinforcement Learning for GUI Grounding via Region Consistency](https://arxiv.org/abs/2508.05615) [[code]](https://github.com/zju-real/gui-rcpo)
+ [EVA: Red-Teaming GUI Agents via Evolving Indirect Prompt Injection](https://arxiv.org/abs/2505.14289)
+ ![Star](https://img.shields.io/github/stars/bytedance/UI-TARS.svg?style=social&label=Star) [UI-TARS-2 Technical Report: Advancing GUI Agent with Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2509.02544) [[code]](https://github.com/bytedance/UI-TARS)
+ ![Star](https://img.shields.io/github/stars/microsoft/Phi-Ground.svg?style=social&label=Star) [Phi-Ground Tech Report: Advancing Perception in GUI Grounding](https://arxiv.org/abs/2507.23779) [[code]](https://github.com/microsoft/Phi-Ground)
+ ![Star](https://img.shields.io/github/stars/Reallm-Labs/InfiGUI-R1.svg?style=social&label=Star) [InfiGUI-R1: Advancing Multimodal GUI Agents from Reactive Actors to Deliberative Reasoners](https://arxiv.org/abs/2504.14239) [[code]](https://github.com/Reallm-Labs/InfiGUI-R1)
+ [GUI-R1: A Generalist R1-Style Vision-Language Action Model For GUI Agents](https://arxiv.org/abs/2504.10458)
+ ![Star](https://img.shields.io/github/stars/OpenGVLab/ZeroGUI.svg?style=social&label=Star) [ZeroGUI: Automating Online GUI Learning at Zero Human Cost](https://arxiv.org/abs/2505.23762) [[code]](https://github.com/OpenGVLab/ZeroGUI)
+ ![Star](https://img.shields.io/github/stars/dvlab-research/ARPO.svg?style=social&label=Star) [ARPO: End-to-End Policy Optimization for GUI Agents with Experience Replay](https://arxiv.org/abs/2505.16282) [[code]](https://github.com/dvlab-research/ARPO)
+ ![Star](https://img.shields.io/github/stars/KDEGroup/UI-AGILE.svg?style=social&label=Star) [UI-AGILE: Advancing GUI Agents with Effective Reinforcement Learning and Precise Inference-Time Grounding](https://arxiv.org/abs/2507.22025) [[code]](https://github.com/KDEGroup/UI-AGILE)
+ ![Star](https://img.shields.io/github/stars/X-PLUG/MobileAgent.svg?style=social&label=Star) [Mobile-Agent-v3: Fundamental Agents for GUI Automation](https://arxiv.org/abs/2508.15144) [[code]](https://github.com/X-PLUG/MobileAgent)
+ ![Star](https://img.shields.io/github/stars/X-PLUG/MobileAgent.svg?style=social&label=Star) [UI-S1: Advancing GUI Automation via Semi-online Reinforcement Learning](https://arxiv.org/abs/2509.11543) [[code]](https://github.com/X-PLUG/MobileAgent/tree/main/UI-S1)
+ ![Star](https://img.shields.io/github/stars/THUDM/MobileRL.svg?style=social&label=Star) [MobileRL: Online Agentic Reinforcement Learning for Mobile GUI Agents](https://arxiv.org/abs/2509.18119) [[code]](https://github.com/THUDM/MobileRL)
+ ![Star](https://img.shields.io/github/stars/THUDM/ComputerRL.svg?style=social&label=Star) [ComputerRL: Scaling End-to-End Online Reinforcement Learning for Computer Use Agents](https://arxiv.org/abs/2508.14040) [[code]](https://github.com/thudm/ComputerRL)
+ ![Star](https://img.shields.io/github/stars/OpenGVLab/ScaleCUA.svg?style=social&label=Star) [ScaleCUA: Scaling Open-Source Computer Use Agents with Cross-Platform Data](https://arxiv.org/abs/2509.15221) [[code]](https://github.com/OpenGVLab/ScaleCUA)
+ [UltraCUA: A Foundation Model for Computer Use Agents with Hybrid Action](https://arxiv.org/abs/2510.17790)
+ [Surfer 2: The Next Generation of Cross-Platform Computer Use Agents](https://arxiv.org/abs/2510.19949)
+ ![Star](https://img.shields.io/github/stars/showlab/showui-pi.svg?style=social&label=Star) [ShowUI-pi: Flow-based Generative Models as GUI Dexterous Hands](https://arxiv.org/abs/2512.24965) [[code]](https://github.com/showlab/showui-pi)
+ ![Star](https://img.shields.io/github/stars/numbmelon/OS-Oracle.svg?style=social&label=Star) [OS-Oracle: A Comprehensive Framework for Cross-Platform GUI Critic Models](https://arxiv.org/abs/2512.16295) [[code]](https://github.com/numbmelon/OS-Oracle)
+ ![Star](https://img.shields.io/github/stars/MobileLLM/AgentProg.svg?style=social&label=Star) [AgentProg: Empowering Long-Horizon GUI Agents with Program-Guided Context Management](https://arxiv.org/abs/2512.10371) [[code]](https://github.com/MobileLLM/AgentProg)
+ [Fara-7B: An Efficient Agentic Model for Computer Use](https://arxiv.org/abs/2511.19663)
+ [UI-R1: Enhancing Efficient Action Prediction of GUI Agents by Reinforcement Learning](https://arxiv.org/abs/2503.21620) [[code]](https://github.com/lll6gg/UI-R1)
+ [ScreenLLM: Stateful Screen Schema for Efficient Action Understanding and Prediction](https://arxiv.org/abs/2503.20978)
+ [VeriSafe Agent: Safeguarding Mobile GUI Agent via Logic-based Action Verification](https://arxiv.org/abs/2503.18492)
+ [GUI-Xplore: Empowering Generalizable GUI Agents with One Exploration](https://arxiv.org/abs/2503.17709)
+ [Does Chain-of-Thought Reasoning Help Mobile GUI Agent? An Empirical Study](https://arxiv.org/abs/2503.16788) [[code]](https://github.com/LlamaTouch/VLM-Reasoning-Traces)
+ [Advancing Mobile GUI Agents: A Verifier-Driven Approach to Practical Deployment](https://arxiv.org/abs/2503.15937) [[code]](https://github.com/V-Droid-Agent/V-Droid)
+ [DeskVision: Large Scale Desktop Region Captioning for Advanced GUI Agents](https://arxiv.org/abs/2503.11170)
+ [API Agents vs. GUI Agents: Divergence and Convergence](https://arxiv.org/abs/2503.11069)
+ [SpiritSight Agent: Advanced GUI Agent with One Look](https://arxiv.org/abs/2503.03196) [[project]](https://hzhiyuan.github.io/SpiritSight-Agent)
+ [AppAgentX: Evolving GUI Agents as Proficient Smartphone Users](https://arxiv.org/abs/2503.02268)
+ [Smoothing Grounding and Reasoning for MLLM-Powered GUI Agents with Query-Oriented Pivot Tasks](https://arxiv.org/abs/2503.00401) [[code]](https://github.com/ZrW00/GUIPivot)
+ [OS-Kairos: Adaptive Interaction for MLLM-Powered GUI Agents](https://arxiv.org/abs/2503.16465) [[code]](https://github.com/Wuzheng02/OS-Kairos)
+ [VEM: Environment-Free Exploration for Training GUI Agent with Value Environment Model](https://arxiv.org/abs/2502.18906)
+ [PC-Agent: A Hierarchical Multi-Agent Collaboration Framework for Complex Task Automation on PC](https://arxiv.org/abs/2502.14282) [[code]](https://github.com/X-PLUG/MobileAgent/tree/main/PC-Agent)
+ [TRISHUL: Towards Region Identification and Screen Hierarchy Understanding for Large VLM based GUI Agents](https://arxiv.org/abs/2502.08226)
+ [MobileA3gent: Training Mobile GUI Agents Using Decentralized Self-Sourced Data from Diverse Users](https://arxiv.org/abs/2502.02982)
+ [Mobile-Agent-E: Self-Evolving Mobile Assistant for Complex Tasks](https://arxiv.org/abs/2501.11733) [[project]](https://x-plug.github.io/MobileAgent)
+ [Mobile-Bench-v2: A More Realistic and Comprehensive Benchmark for VLM-based Mobile Agents](https://arxiv.org/abs/2505.11891) [[data]](https://huggingface.co/datasets/xwk123/MobileBench-v2)
+ [Mobile-R1: Towards Interactive Capability for VLM-Based Mobile Agent via Systematic Training](https://arxiv.org/abs/2506.20332) [[project]](https://mobile-r1.github.io/Mobile-R1/)
+ [MobileGUI-RL: Advancing Mobile GUI Agent through Reinforcement Learning in Online Environment](https://arxiv.org/abs/2507.05720)
+ [MVISU-Bench: Benchmarking Mobile Agents for Real-World Tasks by Multi-App, Vague, Interactive, Single-App and Unethical Instructions](https://arxiv.org/abs/2508.09057) (ACM MM 2025)
+ [InquireMobile: Teaching VLM-based Mobile Agent to Request Human Assistance via Reinforcement Fine-Tuning](https://arxiv.org/abs/2508.19679)
+ [MobileRAG: Enhancing Mobile Agent with Retrieval-Augmented Generation](https://arxiv.org/abs/2509.03891) [[code]](https://github.com/liuxiaojieOutOfWorld/MobileRAG_arxiv)
+ [MAS-Bench: A Unified Benchmark for Shortcut-Augmented Hybrid Mobile GUI Agents](https://arxiv.org/abs/2509.06477) [[website]](https://pengxiang-zhao.github.io/MAS-Bench)
+ [ColorBench: Benchmarking Mobile Agents with Graph-Structured Framework for Complex Long-Horizon Tasks](https://arxiv.org/abs/2510.14621) [[code]](https://github.com/MadeAgents/ColorBench)
+ [MobileWorldBench: Towards Semantic World Modeling For Mobile Agents](https://arxiv.org/abs/2512.14014) [[code]](https://github.com/jacklishufan/MobileWorld)
+ [MobiBench: Multi-Branch, Modular Benchmark for Mobile GUI Agents](https://arxiv.org/abs/2512.12634)
+ [OpenApps: Simulating Environment Variations to Measure UI-Agent Reliability](https://arxiv.org/abs/2511.20766) [[website]](https://facebookresearch.github.io/OpenApps/)
+ [WASP: Benchmarking Web Agent Security Against Prompt Injection Attacks](https://arxiv.org/abs/2504.18575)

### arXiv 2024
+ ![Star](https://img.shields.io/github/stars/MinorJerry/WebVoyager.svg?style=social&label=Star) [WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models](https://arxiv.org/abs/2401.13919) [[code]](https://github.com/MinorJerry/WebVoyager)
+ ![Star](https://img.shields.io/github/stars/xlang-ai/OSWorld.svg?style=social&label=Star) [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://arxiv.org/abs/2404.07972) [[code]](https://github.com/xlang-ai/OSWorld)
+ ![Star](https://img.shields.io/github/stars/X-PLUG/MobileAgent.svg?style=social&label=Star) [Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent](https://arxiv.org/abs/2401.16158) [[code]](https://github.com/X-PLUG/MobileAgent)
+ ![Star](https://img.shields.io/github/stars/X-PLUG/MobileAgent.svg?style=social&label=Star) [Mobile-Agent-v2: Mobile Device Operation Assistant with Effective Navigation via Multi-Agent Collaboration](https://arxiv.org/abs/2406.01014) [[code]](https://github.com/X-PLUG/MobileAgent)
+ ![Star](https://img.shields.io/github/stars/microsoft/UFO.svg?style=social&label=Star) [UFO: A UI-Focused Agent for Windows OS Interaction](https://arxiv.org/abs/2402.07939) [[code]](https://github.com/microsoft/UFO)
+ ![Star](https://img.shields.io/github/stars/OS-Copilot/OS-Copilot.svg?style=social&label=Star) [OS-Copilot: Towards Generalist Computer Agents with Self-Improvement](https://arxiv.org/abs/2402.07456) [[code]](https://github.com/OS-Copilot/OS-Copilot)
+ ![Star](https://img.shields.io/github/stars/niuzaisheng/ScreenAgent.svg?style=social&label=Star) [ScreenAgent: A Computer Control Agent Driven by Visual Language Large Model](https://arxiv.org/abs/2402.07945) [[code]](https://github.com/niuzaisheng/ScreenAgent)
+ ![Star](https://img.shields.io/github/stars/BAAI-Agents/Cradle.svg?style=social&label=Star) [Towards General Computer Control: A Multimodal Agent for Red Dead Redemption II](https://arxiv.org/abs/2403.03186) [[code]](https://github.com/BAAI-Agents/Cradle)
+ ![Star](https://img.shields.io/github/stars/THUDM/AutoWebGLM.svg?style=social&label=Star) [AutoWebGLM: Bootstrap and Reinforce a Large Language Model-based Web Navigating Agent](https://arxiv.org/abs/2404.03648) [[code]](https://github.com/THUDM/AutoWebGLM)
+ ![Star](https://img.shields.io/github/stars/apple/ml-ferret.svg?style=social&label=Star) [Ferret-UI: Grounded Mobile UI Understanding with Multimodal LLMs](https://arxiv.org/abs/2404.05719) [[code]](https://github.com/apple/ml-ferret)
+ ![Star](https://img.shields.io/github/stars/DigiRL-agent/digirl.svg?style=social&label=Star) [DigiRL: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning](https://arxiv.org/abs/2406.11896) [[code]](https://github.com/DigiRL-agent/digirl)
+ [VisualWebBench: How Far Have Multimodal LLMs Evolved in Web Page Understanding and Grounding?](https://arxiv.org/abs/2404.05955)
+ [GUI Odyssey: A Comprehensive Dataset for Cross-App GUI Navigation on Mobile Devices](https://arxiv.org/abs/2406.08451)
+ ![Star](https://img.shields.io/github/stars/showlab/GUI-Action-Narrator.svg?style=social&label=Star) [GUI Action Narrator: Where and When Did That Action Take Place?](https://arxiv.org/abs/2406.13719) [[code]](https://github.com/showlab/GUI-Action-Narrator)
+ ![Star](https://img.shields.io/github/stars/simular-ai/Agent-S.svg?style=social&label=Star) [Agent S: An Open Agentic Framework that Uses Computers Like a Human](https://arxiv.org/abs/2410.08164) [[code]](https://github.com/simular-ai/Agent-S)
+ ![Star](https://img.shields.io/github/stars/THUDM/AutoGLM.svg?style=social&label=Star) [AutoGLM: Autonomous Foundation Agents for GUIs](https://arxiv.org/abs/2411.00820) [[code]](https://github.com/THUDM/AutoGLM)
+ ![Star](https://img.shields.io/github/stars/xlang-ai/aguvis.svg?style=social&label=Star) [Aguvis: Unified Pure Vision Agents for Autonomous GUI Interaction](https://arxiv.org/abs/2412.04454) [[code]](https://github.com/xlang-ai/aguvis)
+ ![Star](https://img.shields.io/github/stars/chengyou-jia/AgentStore.svg?style=social&label=Star) [AgentStore: Scalable Integration of Heterogeneous Agents As Specialized Generalist Computer Assistant](https://arxiv.org/abs/2410.18603) [[code]](https://github.com/chengyou-jia/AgentStore)
+ ![Star](https://img.shields.io/github/stars/GAIR-NLP/PC-Agent.svg?style=social&label=Star) [PC Agent: While You Sleep, AI Works](https://arxiv.org/abs/2412.17589) [[code]](https://github.com/GAIR-NLP/PC-Agent)
+ ![Star](https://img.shields.io/github/stars/OpenDFM/MobA.svg?style=social&label=Star) [MobA: Multifaceted Memory-Enhanced Adaptive Planning for Efficient Mobile Task Automation](https://arxiv.org/abs/2410.13757) (NAACL 2025 Demo) [[code]](https://github.com/OpenDFM/MobA)
+ ![Star](https://img.shields.io/github/stars/jylee425/b-moca.svg?style=social&label=Star) [Benchmarking Mobile Device Control Agents across Diverse Configurations](https://arxiv.org/abs/2404.16660) (CoLLAs 2025; ICLR 2024 workshop) [[code]](https://github.com/jylee425/b-moca)
+ [MobileVLM: A Vision-Language Model for Better Intra- and Inter-UI Understanding](https://arxiv.org/abs/2409.14818)
+ ![Star](https://img.shields.io/github/stars/zorazrw/agent-workflow-memory.svg?style=social&label=Star) [Agent Workflow Memory](https://arxiv.org/abs/2409.07429) [[code]](https://github.com/zorazrw/agent-workflow-memory)
+ ![Star](https://img.shields.io/github/stars/THUDM/CogAgent.svg?style=social&label=Star) [CogAgent v2](https://github.com/THUDM/CogAgent) [[code]](https://github.com/THUDM/CogAgent)
+ ![Star](https://img.shields.io/github/stars/AriaUI/Aria-UI.svg?style=social&label=Star) [Aria-UI: Visual Grounding for GUI Instructions](https://arxiv.org/abs/2412.16256) [[code]](https://github.com/AriaUI/Aria-UI)
+ ![Star](https://img.shields.io/github/stars/OS-Copilot/OS-Genesis.svg?style=social&label=Star) [OS-Genesis: Automating GUI Agent Trajectory Construction via Reverse Task Synthesis](https://arxiv.org/abs/2412.19723) [[code]](https://github.com/OS-Copilot/OS-Genesis)
+ [Falcon-UI: Understanding GUI Before Following User Instructions](https://arxiv.org/abs/2412.09362)
+ [Iris: Breaking GUI Complexity with Adaptive Focus and Self-Refining](https://arxiv.org/abs/2412.10342)
+ [Attacking Vision-Language Computer Agents via Pop-ups](https://arxiv.org/abs/2411.02391)
+ [OmniParser for Pure Vision Based GUI Agent](https://arxiv.org/abs/2408.00203)
+ ![Star](https://img.shields.io/github/stars/THUDM/VisualAgentBench.svg?style=social&label=Star) [VisualAgentBench: Towards Large Multimodal Models as Visual Foundation Agents](https://arxiv.org/abs/2408.06327) [[code]](https://github.com/THUDM/VisualAgentBench)
+ [MobileFlow: A Multimodal LLM For Mobile GUI Agent](https://arxiv.org/abs/2407.04346)
+ ![Star](https://img.shields.io/github/stars/EmergenceAI/Agent-E.svg?style=social&label=Star) [Agent-E: From Autonomous Web Navigation to Foundational Design Principles in Agentic Systems](https://arxiv.org/abs/2407.13032) [[code]](https://github.com/EmergenceAI/Agent-E)
+ [AppAgent v2: Advanced Agent for Flexible Mobile Interactions](https://arxiv.org/abs/2408.11824)
+ [AdaptAgent: Adapting Multimodal Web Agents with Few-Shot Learning from Human Demonstrations](https://arxiv.org/abs/2411.13451)
+ [Lightweight Neural App Control](https://arxiv.org/abs/2410.17883)
+ [DistRL: An Asynchronous Distributed Reinforcement Learning Framework for On-Device Control Agents](https://arxiv.org/abs/2410.14803)
+ [Ponder & Press: Advancing Visual GUI Agent towards General Computer Control](https://arxiv.org/abs/2412.01268) [[project]](https://invinciblewyq.github.io/ponder-press-page/)
+ ![Star](https://img.shields.io/github/stars/MobileLLM/AutoDroid-V2.svg?style=social&label=Star) [AutoDroid-V2: Boosting SLM-based GUI Agents via Code Generation](https://arxiv.org/abs/2412.18116) [[code]](https://github.com/MobileLLM/AutoDroid-V2)
+ ![Star](https://img.shields.io/github/stars/ServiceNow/BrowserGym.svg?style=social&label=Star) [The BrowserGym Ecosystem for Web Agent Research](https://arxiv.org/abs/2412.05467) [[code]](https://github.com/ServiceNow/BrowserGym)
+ [AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials](https://arxiv.org/abs/2412.09605)
+ ![Star](https://img.shields.io/github/stars/UbiquitousLearning/DroidCall.svg?style=social&label=Star) [DroidCall: A Dataset for LLM-powered Android Intent Invocation](https://arxiv.org/abs/2412.00402) [[code]](https://github.com/UbiquitousLearning/DroidCall)
+ [Attention-driven GUI Grounding: Leveraging Pretrained Multimodal Large Language Models without Fine-Tuning](https://arxiv.org/abs/2412.10840)
+ [Improved GUI Grounding via Iterative Narrowing](https://arxiv.org/abs/2411.13591)
+ [OpenWebVoyager: Building Multimodal Web Agents via Iterative Real-World Exploration, Feedback and Optimization](https://arxiv.org/abs/2410.19609)
+ [Web Agents with World Models: Learning and Leveraging Environment Dynamics in Web Navigation](https://arxiv.org/abs/2410.13232)
+ [Auto-Intent: Automated Intent Discovery and Self-Exploration for Large Language Model Web Agents](https://arxiv.org/abs/2410.22552)
+ [AgentOccam: A Simple Yet Strong Baseline for LLM-Based Web Agents](https://arxiv.org/abs/2410.13825)
+ [WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning](https://arxiv.org/abs/2411.02337)
+ [OSCAR: Operating System Control via State-Aware Reasoning and Re-Planning](https://arxiv.org/abs/2410.18963)
+ [EDGE: Enhanced Grounded GUI Understanding with Enriched Multi-Granularity Synthetic Data](https://arxiv.org/abs/2410.19461)
+ [ClickAgent: Enhancing UI Location Capabilities of Autonomous Agents](https://arxiv.org/abs/2410.11872)
+ ![Star](https://img.shields.io/github/stars/sqzhang-lazy/D-PoT.svg?style=social&label=Star) [Dynamic Planning for LLM-based Graphical User Interface Automation](https://arxiv.org/abs/2410.00467) [[code]](https://github.com/sqzhang-lazy/D-PoT)
+ [From Interaction to Impact: Towards Safer AI Agents Through Understanding and Evaluating Mobile UI Operation Impacts](https://arxiv.org/abs/2410.09006)
+ [MobileViews: A Million-scale and Diverse Mobile GUI Dataset](https://arxiv.org/abs/2409.14337) [[data]](https://huggingface.co/datasets/mllmTeam/MobileViews)
+ [Mobile-Bench: An Evaluation Benchmark for LLM-based Mobile Agents](https://arxiv.org/abs/2407.00993)
+ ![Star](https://img.shields.io/github/stars/ServiceNow/WorkArena.svg?style=social&label=Star) [WorkArena++: Towards Compositional Planning and Reasoning-based Common Knowledge Work Tasks](https://arxiv.org/abs/2407.05291) [[code]](https://github.com/ServiceNow/WorkArena)
+ [WebCanvas: Benchmarking Web Agents in Online Environments](https://arxiv.org/abs/2406.12373)
+ ![Star](https://img.shields.io/github/stars/caap-agent/caap-agent.svg?style=social&label=Star) [CAAP: Context-Aware Action Planning Prompting to Solve Computer Tasks with Front-End UI Only](https://arxiv.org/abs/2406.06947) [[code]](https://github.com/caap-agent/caap-agent)
+ [On the Effects of Data Scale on UI Control Agents](https://arxiv.org/abs/2406.03679)
+ [Training a Vision Language Model as Smartphone Assistant](https://arxiv.org/abs/2404.08755)
+ ![Star](https://img.shields.io/github/stars/ServiceNow/WorkArena.svg?style=social&label=Star) [WorkArena: How Capable Are Web Agents at Solving Common Knowledge Work Tasks?](https://arxiv.org/abs/2403.07718) [[code]](https://github.com/ServiceNow/WorkArena)
+ [On the Multi-turn Instruction Following for Conversational Web Agents](https://arxiv.org/abs/2402.15057)

### 2023 and Before
+ [World of Bits: An Open-Domain Platform for Web-Based Agents](https://proceedings.mlr.press/v70/shi17a.html) (2017; related web-agent foundation)
+ ![Star](https://img.shields.io/github/stars/princeton-nlp/WebShop.svg?style=social&label=Star) [WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents](https://arxiv.org/abs/2207.01206) [[code]](https://github.com/princeton-nlp/WebShop) (2022; related web-agent foundation)
+ ![Star](https://img.shields.io/github/stars/OSU-NLP-Group/Mind2Web.svg?style=social&label=Star) [Mind2Web: Towards a Generalist Agent for the Web](https://arxiv.org/abs/2306.06070) [[code]](https://github.com/OSU-NLP-Group/Mind2Web) (2023)
+ [Android in the Wild: A Large-Scale Dataset for Android Device Control](https://arxiv.org/abs/2307.10088) (2023)
+ ![Star](https://img.shields.io/github/stars/web-arena-x/webarena.svg?style=social&label=Star) [WebArena: A Realistic Web Environment for Building Autonomous Agents](https://arxiv.org/abs/2307.13854) [[code]](https://github.com/web-arena-x/webarena) (2023)
+ ![Star](https://img.shields.io/github/stars/mnotgod96/AppAgent.svg?style=social&label=Star) [AppAgent: Multimodal Agents as Smartphone Users](https://arxiv.org/abs/2312.13771) [[code]](https://github.com/mnotgod96/AppAgent) (2023)
+ ![Star](https://img.shields.io/github/stars/zzxslp/MM-Navigator.svg?style=social&label=Star) [GPT-4V in Wonderland: Large Multimodal Models for Zero-Shot Smartphone GUI Navigation](https://arxiv.org/abs/2311.07562) [[code]](https://github.com/zzxslp/MM-Navigator) (2023)
+ [A Data-Driven Approach for Learning to Control Computers](https://arxiv.org/abs/2202.08137) (2022)
+ [Reinforcement Learning on Web Interfaces using Workflow-Guided Exploration](https://arxiv.org/abs/1802.08802) (2018)
+ [Mapping Natural Language Instructions to Mobile UI Action Sequences](https://arxiv.org/abs/2005.03776) (2020)
+ [DroidBot-GPT: GPT-powered UI Automation for Android](https://arxiv.org/abs/2304.07061) (2023)
+ [Mobile-Env: Building Qualified Evaluation Benchmarks for LLM-GUI Interaction](https://arxiv.org/abs/2305.08144) (2023)
+ [Multimodal Web Navigation with Instruction-Finetuned Foundation Models](https://arxiv.org/abs/2305.11854) (2023)
+ [A Zero-Shot Language Agent for Computer Control with Structured Reflection](https://arxiv.org/abs/2310.08740) (2023)
+ [AllTogether: Investigating the Efficacy of Spliced Prompt for Web Navigation using Large Language Models](https://arxiv.org/abs/2310.18331) (2023)

---

## Paper Tree

```text
Multimodal GUI Agents
├── 1. GUI Perception and Grounding
│   ├── Screen understanding
│   ├── UI element detection
│   ├── OCR / text-rich screen reasoning
│   ├── Coordinate / bounding-box grounding
│   └── GUI grounding pre-training
│
├── 2. Action Modeling
│   ├── Click prediction
│   ├── Typing / text input
│   ├── Keyboard and mouse control
│   ├── Action sequence generation
│   └── Vision-language-action modeling
│
├── 3. Agent Planning and Reasoning
│   ├── Task decomposition
│   ├── Multi-step planning
│   ├── Memory and reflection
│   ├── Error recovery
│   └── Long-horizon execution
│
├── 4. Platform-Specific Agents
│   ├── Web agents
│   ├── Mobile agents
│   ├── Desktop agents
│   └── Cross-platform computer-use agents
│
├── 5. Training and Data
│   ├── GUI grounding data synthesis
│   ├── Demonstration collection
│   ├── Imitation learning
│   ├── Reinforcement learning
│   ├── RLVR / verifiable reward design
│   ├── Video-to-trajectory mining
│   └── Self-improvement / environment feedback
│
├── 6. Evaluation
│   ├── GUI grounding benchmarks
│   ├── Web navigation benchmarks
│   ├── Mobile control benchmarks
│   ├── Desktop / OS benchmarks
│   ├── Verifier-grounded software worlds
│   └── Safety and robustness evaluation
│
└── 7. Deployment and Tooling
    ├── Browser automation
    ├── Desktop automation
    ├── Mobile automation
    ├── RPA integration
    ├── Human-in-the-loop control
    └── Privacy / policy guardrails
```

---

## Timeline

```text
2017  World of Bits, Rico
2018  RL on Web Interfaces (WGE)
2020  Mapping NL Instructions to Mobile UI
2021  AndroidEnv, Screen2Words, WebSRC
2022  WebShop, Data-Driven Computer Control
2023  Mind2Web, WebArena, AITW, CogAgent, AppAgent, AssistGUI, Synapse, MM-Navigator
2024  SeeClick, VisualWebArena, WebVoyager, OSWorld, GUI Odyssey, UFO, OS-Copilot, ScreenAgent,
      Ferret-UI, AutoWebGLM, DigiRL, Aguvis, AutoGLM, Agent-S, PC Agent, OmniParser, AgentStudio
2025  OS-Atlas, ShowUI, UI-TARS, UI-TARS-2, UGround, InfiGUIAgent, AgentCPM-GUI, TongUI,
      WorldGUI, OpenCUA, Phi-Ground, InfiGUI-R1, Mobile-Agent-v3, ScreenSpot-Pro,
      MMBench-GUI, macOSWorld, NaturalGAIA, ComputerRL, MobileRL, ScaleCUA, UI-R1,
      ScreenLLM, V-Droid, Mobile-Bench-v2, Mobile-R1, MobileWorldBench
2026  UI-Venus-1.5, EvoCUA, Mobile-Agent-v3.5, TreeCUA, OpenComputer, CUA-Gym, MobileGym,
      Video2GUI / WildGUI, RoTS, GUI-CIDER, AgentHijack, WinDeskGround, CUA-Suite,
      OpenMobile, PhoneWorld, DiffSpot, ScreenParse, EntWorld, MemGUI-Bench, GUIGuard-Bench
```

---

## Paper List

> The sections below focus on papers and paper-backed resources. Foundational or broader-agent entries are retained only when they help contextualize GUI-agent research.

## Surveys

> This section keeps GUI-agent, OS-agent, mobile-agent, and computer-use focused surveys.

+ ![Star](https://img.shields.io/github/stars/OS-Agent-Survey/OS-Agent-Survey.svg?style=social&label=Star) [OS Agents: A Survey on MLLM-based Agents for General Computing Devices Use](https://github.com/OS-Agent-Survey/OS-Agent-Survey) (Dec. 2024) [[Website]](https://os-agent-survey.github.io/)
+ [GUI Agents with Foundation Models: A Comprehensive Survey](https://arxiv.org/abs/2411.04890) (Nov. 2024)
+ [Large Language Model-Brained GUI Agents: A Survey](https://arxiv.org/abs/2411.18279) (Nov. 2024) [[Website]](https://vyokky.github.io/LLM-Brained-GUI-Agents-Survey/)
+ [GUI Agents: A Survey](https://arxiv.org/abs/2412.13501) (Dec. 2024)
+ ![Star](https://img.shields.io/github/stars/PhoneLLM/Awesome-LLM-Powered-Phone-GUI-Agents.svg?style=social&label=Star) [LLM-Powered GUI Agents in Phone Automation: Surveying Progress and Prospects](https://arxiv.org/abs/2504.19838) (Apr. 2025)
+ [A Survey on (M)LLM-Based GUI Agents](https://arxiv.org/abs/2504.13865) (Apr. 2025)
+ [Towards Trustworthy GUI Agents: A Survey](https://arxiv.org/abs/2503.23434) (Mar. 2025)
+ [A Survey on GUI Agents with Foundation Models Enhanced by Reinforcement Learning](https://arxiv.org/abs/2504.20464) (Apr. 2025)

## GUI Grounding and Screen Understanding

+ ![Star](https://img.shields.io/github/stars/njucckevin/SeeClick.svg?style=social&label=Star) [SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents](https://arxiv.org/abs/2401.10935) (ACL 2024) [[code]](https://github.com/njucckevin/SeeClick)
+ ![Star](https://img.shields.io/github/stars/OS-Copilot/OS-Atlas.svg?style=social&label=Star) [OS-ATLAS: A Foundation Action Model for Generalist GUI Agents](https://arxiv.org/abs/2410.23218) (ICLR 2025) [[code]](https://github.com/OS-Copilot/OS-Atlas)
+ ![Star](https://img.shields.io/github/stars/OSU-NLP-Group/UGround.svg?style=social&label=Star) [UGround: Navigating the Digital World as Humans Do: Universal Visual Grounding for GUI Agents](https://arxiv.org/abs/2410.05243) (ICLR 2025) [[code]](https://github.com/OSU-NLP-Group/UGround)
+ [VisualWebBench: How Far Have Multimodal LLMs Evolved in Web Page Understanding and Grounding?](https://arxiv.org/abs/2404.05955) (2024)
+ [ScreenSpot: GUI grounding benchmark introduced by SeeClick](https://arxiv.org/abs/2401.10935) (ACL 2024)
+ ![Star](https://img.shields.io/github/stars/likaixin2000/ScreenSpot-Pro-GUI-Grounding.svg?style=social&label=Star) [ScreenSpot-Pro: GUI Grounding for Professional High-Resolution Computer Use](https://arxiv.org/abs/2504.07981) (2025) [[code]](https://github.com/likaixin2000/ScreenSpot-Pro-GUI-Grounding) [[leaderboard]](https://gui-agent.github.io/grounding-leaderboard)
+ ![Star](https://img.shields.io/github/stars/apple/ml-ferret.svg?style=social&label=Star) [Ferret-UI: Grounded Mobile UI Understanding with Multimodal LLMs](https://arxiv.org/abs/2404.05719) (2024) [[code]](https://github.com/apple/ml-ferret)
+ [ScreenAI: A Vision-Language Model for UI and Infographics Understanding](https://arxiv.org/abs/2402.04615) (2024)
+ ![Star](https://img.shields.io/github/stars/AriaUI/Aria-UI.svg?style=social&label=Star) [Aria-UI: Visual Grounding for GUI Instructions](https://arxiv.org/abs/2412.16256) (2024) [[code]](https://github.com/AriaUI/Aria-UI)
+ [Visual Grounding for User Interfaces](https://aclanthology.org/2024.naacl-industry.9.pdf) (NAACL 2024)
+ ![Star](https://img.shields.io/github/stars/eric-ai-lab/Screen-Point-and-Read.svg?style=social&label=Star) [Read Anywhere Pointed: Layout-aware GUI Screen Reading with Tree-of-Lens Grounding](https://arxiv.org/abs/2406.19263) (2024) [[code]](https://github.com/eric-ai-lab/Screen-Point-and-Read)
+ [Visual Grounding Methods for Efficient Interaction with Desktop Graphical User Interfaces](https://arxiv.org/abs/2407.01558) (2024)
+ [MobileViews: A Million-scale and Diverse Mobile GUI Dataset](https://arxiv.org/abs/2409.14337) (2024) [[data]](https://huggingface.co/datasets/mllmTeam/MobileViews)
+ [ClickAgent: Enhancing UI Location Capabilities of Autonomous Agents](https://arxiv.org/abs/2410.11872) (2024)
+ [EDGE: Enhanced Grounded GUI Understanding with Enriched Multi-Granularity Synthetic Data](https://arxiv.org/abs/2410.19461) (2024)
+ [Improved GUI Grounding via Iterative Narrowing](https://arxiv.org/abs/2411.13591) (2024)
+ [Attention-driven GUI Grounding: Leveraging Pretrained Multimodal Large Language Models without Fine-Tuning](https://arxiv.org/abs/2412.10840) (2024)
+ [AutoGUI: Scaling GUI Grounding with Automatic Functionality Annotations from LLMs](https://arxiv.org/abs/2502.01977) (2025) [[project]](https://autogui-project.github.io/)
+ ![Star](https://img.shields.io/github/stars/microsoft/Phi-Ground.svg?style=social&label=Star) [Phi-Ground Tech Report: Advancing Perception in GUI Grounding](https://arxiv.org/abs/2507.23779) (2025) [[code]](https://github.com/microsoft/Phi-Ground)
+ ![Star](https://img.shields.io/github/stars/Yuqi-Zhou/GUI-G1.svg?style=social&label=Star) [GUI-G1: Understanding R1-Zero-Like Training for Visual Grounding in GUI Agents](https://arxiv.org/abs/2505.15810) (2025) [[code]](https://github.com/Yuqi-Zhou/GUI-G1)
+ [R-VLM: Region-Aware Vision Language Model for Precise GUI Grounding](https://arxiv.org/abs/2507.05673) (2025)
+ [GTA1: GUI Test-time Scaling Agent](https://arxiv.org/abs/2507.05791) (2025)
+ ![Star](https://img.shields.io/github/stars/InfiXAI/InfiGUI-G1.svg?style=social&label=Star) [InfiGUI-G1: Advancing GUI Grounding with Adaptive Exploration Policy Optimization](https://arxiv.org/abs/2508.05731) (2025) [[code]](https://github.com/InfiXAI/InfiGUI-G1)
+ ![Star](https://img.shields.io/github/stars/ZJUSCL/MVP.svg?style=social&label=Star) [MVP: Multiple View Prediction Improves GUI Grounding](https://arxiv.org/abs/2512.08529) (2025) [[code]](https://github.com/ZJUSCL/MVP)
+ ![Star](https://img.shields.io/github/stars/samsungsds-research-papers/mega-gui.svg?style=social&label=Star) [MEGA-GUI: Multi-stage Enhanced Grounding Agents for GUI Elements](https://arxiv.org/abs/2511.13087) (2025) [[code]](https://github.com/samsungsds-research-papers/mega-gui)
+ ![Star](https://img.shields.io/github/stars/alibaba/UI-Ins.svg?style=social&label=Star) [UI-Ins: Enhancing GUI Grounding with Multi-Perspective Instruction-as-Reasoning](https://arxiv.org/abs/2510.20286) (2025) [[code]](https://github.com/alibaba/UI-Ins)
+ ![Star](https://img.shields.io/github/stars/sjz5202/GUI-AIMA.svg?style=social&label=Star) [GUI-AIMA: Aligning Intrinsic Multimodal Attention with a Context Anchor for GUI Grounding](https://arxiv.org/abs/2511.00810) (2025) [[code]](https://github.com/sjz5202/GUI-AIMA)
+ [SafeGround: Know When to Trust GUI Grounding Models via Uncertainty Calibration](https://arxiv.org/abs/2602.02419) (2026)
+ ![Star](https://img.shields.io/github/stars/Neur-IO/BAMI.svg?style=social&label=Star) [BAMI: Training-Free Bias Mitigation in GUI Grounding](https://arxiv.org/abs/2605.06664) (Tech Report 2026) [[project]](https://github.com/Neur-IO/BAMI)
+ [DRS-GUI: Dynamic Region Search for Training-Free GUI Grounding](https://arxiv.org/abs/2605.15542) (2026)
+ ![Star](https://img.shields.io/github/stars/ZZZhr-1/WinDeskGround.svg?style=social&label=Star) [WinDeskGround: A Benchmark for Robust GUI Grounding in Complex Multi-Window Desktop Environments](https://arxiv.org/abs/2605.16402) (2026) [[code]](https://github.com/ZZZhr-1/WinDeskGround)
+ ![Star](https://img.shields.io/github/stars/linjiaping1/Re-Prefill.svg?style=social&label=Star) [What Happens Before Decoding? Prefill Determines GUI Grounding in VLMs](https://arxiv.org/abs/2605.12549) (2026) [[code]](https://github.com/linjiaping1/Re-Prefill)
+ [GUI-SD: Learn where to Click from Yourself](https://arxiv.org/abs/2605.00642) (2026) [[project]](https://zhangyan-ucas.github.io/GUI-SD/)
+ ![Star](https://img.shields.io/github/stars/zackhuiiiii/WinSpot.svg?style=social&label=Star) [WinClick: GUI Grounding with Multimodal Large Language Models](https://arxiv.org/abs/2503.04730) (2025) [[code]](https://github.com/zackhuiiiii/WinSpot)
+ [TRISHUL: Towards Region Identification and Screen Hierarchy Understanding for Large VLM based GUI Agents](https://arxiv.org/abs/2502.08226) (2025)
+ ![Star](https://img.shields.io/github/stars/ZrW00/GUIPivot.svg?style=social&label=Star) [Smoothing Grounding and Reasoning for MLLM-Powered GUI Agents with Query-Oriented Pivot Tasks](https://arxiv.org/abs/2503.00401) (2025) [[code]](https://github.com/ZrW00/GUIPivot)
+ [UI-Vision: A Desktop-centric GUI Benchmark for Visual Perception and Interaction](https://arxiv.org/abs/2503.15661) (2025)
+ [ScreenLLM: Stateful Screen Schema for Efficient Action Understanding and Prediction](https://arxiv.org/abs/2503.20978) (2025)
+ [DeskVision: Large Scale Desktop Region Captioning for Advanced GUI Agents](https://arxiv.org/abs/2503.11170) (2025)
+ [ScreenParse: Moving Beyond Sparse Grounding with Complete Screen Parsing Supervision](https://arxiv.org/abs/2602.14276) (2026) [[project]](https://saidgurbuz.github.io/screenparse/)
+ [PrecisionCUA: Iterative Visual Refinement for Pixel-Precise Cursor Grounding in Code Editors](https://arxiv.org/abs/2604.13019) (2026) [[code]](https://github.com/microsoft/precision-cua-bench/tree/main)
+ [DiffSpot: Can VLMs Spot Fine-Grained Visual Differences in Web Interfaces?](https://arxiv.org/abs/2605.29615) (2026)
+ [Covering Human Action Space for Computer Use: Data Synthesis and Benchmark](https://arxiv.org/abs/2605.12501) (2026) [[code]](https://github.com/microsoft/Phi-Ground)

## General GUI Agents

+ ![Star](https://img.shields.io/github/stars/THUDM/CogAgent.svg?style=social&label=Star) [CogAgent: A Visual Language Model for GUI Agents](https://arxiv.org/abs/2312.08914) (CVPR 2024) [[code]](https://github.com/THUDM/CogAgent)
+ ![Star](https://img.shields.io/github/stars/THUDM/CogAgent.svg?style=social&label=Star) [CogAgent v2](https://github.com/THUDM/CogAgent) (2024) [[code]](https://github.com/THUDM/CogAgent)
+ ![Star](https://img.shields.io/github/stars/showlab/ShowUI.svg?style=social&label=Star) [ShowUI: One Vision-Language-Action Model for GUI Visual Agent](https://arxiv.org/abs/2411.17465) (CVPR 2025) [[code]](https://github.com/showlab/ShowUI)
+ ![Star](https://img.shields.io/github/stars/bytedance/UI-TARS.svg?style=social&label=Star) [UI-TARS: Pioneering Automated GUI Interaction with Native Agents](https://arxiv.org/abs/2501.12326) (2025) [[code]](https://github.com/bytedance/UI-TARS)
+ ![Star](https://img.shields.io/github/stars/OS-Copilot/OS-Atlas.svg?style=social&label=Star) [OS-ATLAS: A Foundation Action Model for Generalist GUI Agents](https://arxiv.org/abs/2410.23218) (ICLR 2025) [[code]](https://github.com/OS-Copilot/OS-Atlas)
+ ![Star](https://img.shields.io/github/stars/THUDM/AutoGLM.svg?style=social&label=Star) [AutoGLM: Autonomous Foundation Agents for GUIs](https://arxiv.org/abs/2411.00820) (2024) [[code]](https://github.com/THUDM/AutoGLM)
+ ![Star](https://img.shields.io/github/stars/xlang-ai/aguvis.svg?style=social&label=Star) [Aguvis: Unified Pure Vision Agents for Autonomous GUI Interaction](https://arxiv.org/abs/2412.04454) (2024) [[code]](https://github.com/xlang-ai/aguvis)
+ ![Star](https://img.shields.io/github/stars/simular-ai/Agent-S.svg?style=social&label=Star) [Agent S: An Open Agentic Framework that Uses Computers Like a Human](https://arxiv.org/abs/2410.08164) (2024) [[code]](https://github.com/simular-ai/Agent-S)
+ ![Star](https://img.shields.io/github/stars/GAIR-NLP/PC-Agent.svg?style=social&label=Star) [PC Agent: While You Sleep, AI Works](https://arxiv.org/abs/2412.17589) (2024) [[code]](https://github.com/GAIR-NLP/PC-Agent)
+ ![Star](https://img.shields.io/github/stars/Reallm-Labs/InfiGUIAgent.svg?style=social&label=Star) [InfiGUIAgent: A Multimodal Generalist GUI Agent with Native Reasoning and Reflection](https://arxiv.org/abs/2501.04575) (2025) [[code]](https://github.com/Reallm-Labs/InfiGUIAgent)
+ ![Star](https://img.shields.io/github/stars/chengyou-jia/AgentStore.svg?style=social&label=Star) [AgentStore: Scalable Integration of Heterogeneous Agents As Specialized Generalist Computer Assistant](https://arxiv.org/abs/2410.18603) (2024) [[code]](https://github.com/chengyou-jia/AgentStore)
+ ![Star](https://img.shields.io/github/stars/THUDM/AutoWebGLM.svg?style=social&label=Star) [AutoWebGLM: Bootstrap and Reinforce a Large Language Model-based Web Navigating Agent](https://arxiv.org/abs/2404.03648) (KDD 2024) [[code]](https://github.com/THUDM/AutoWebGLM)
+ ![Star](https://img.shields.io/github/stars/cooelf/Auto-UI.svg?style=social&label=Star) [You Only Look at Screens: Multimodal Chain-of-Action Agents](https://arxiv.org/abs/2309.11436) (2023) [[code]](https://github.com/cooelf/Auto-UI)
+ [Reinforced UI Instruction Grounding: Towards a Generic UI Task Automation API](https://arxiv.org/abs/2310.04716) (2023)
+ ![Star](https://img.shields.io/github/stars/OpenBMB/AgentCPM-GUI.svg?style=social&label=Star) [AgentCPM-GUI: Building Mobile-Use Agents with Reinforcement Fine-Tuning](https://arxiv.org/abs/2506.01391) (2025) [[code]](https://github.com/OpenBMB/AgentCPM-GUI)
+ ![Star](https://img.shields.io/github/stars/TongUI-agent/TongUI-agent.svg?style=social&label=Star) [TongUI: Internet-Scale Trajectories from Multimodal Web Tutorials for Generalized GUI Agents](https://arxiv.org/abs/2504.12679) (AAAI 2026) [[code]](https://github.com/TongUI-agent/TongUI-agent)
+ ![Star](https://img.shields.io/github/stars/showlab/WorldGUI.svg?style=social&label=Star) [WorldGUI: An Interactive Benchmark for Desktop GUI Automation from Any Starting Point](https://arxiv.org/abs/2502.08047) (Tech Report 2025) [[code]](https://github.com/showlab/WorldGUI)
+ ![Star](https://img.shields.io/github/stars/bytedance/UI-TARS.svg?style=social&label=Star) [UI-TARS-2: Advancing GUI Agent with Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2509.02544) (2025) [[code]](https://github.com/bytedance/UI-TARS)
+ ![Star](https://img.shields.io/github/stars/xlang-ai/OpenCUA.svg?style=social&label=Star) [OpenCUA: Open Foundations for Computer-Use Agents](https://arxiv.org/abs/2508.09123) (2025) [[code]](https://github.com/xlang-ai/OpenCUA)
+ [UltraCUA: A Foundation Model for Computer Use Agents with Hybrid Action](https://arxiv.org/abs/2510.17790) (2025)
+ [Surfer 2: The Next Generation of Cross-Platform Computer Use Agents](https://arxiv.org/abs/2510.19949) (2025)
+ [Fara-7B: An Efficient Agentic Model for Computer Use](https://arxiv.org/abs/2511.19663) (2025)
+ ![Star](https://img.shields.io/github/stars/inclusionAI/UI-Venus.svg?style=social&label=Star) [UI-Venus-1.5 Technical Report](https://arxiv.org/abs/2602.09082) (2026) [[code]](https://github.com/inclusionAI/UI-Venus) [[model]](https://huggingface.co/collections/inclusionAI/ui-venus)
+ [EvoCUA: Evolving Computer Use Agents via Learning from Scalable Synthetic Experience](https://arxiv.org/abs/2601.15876) (2026) [[model]](https://huggingface.co/collections/harbingeva/evocua-687c664a9bb7b48f2272ff8a)
+ ![Star](https://img.shields.io/github/stars/UITron-hub/TreeCUA.svg?style=social&label=Star) [TreeCUA: Efficiently Scaling GUI Automation with Tree-Structured Verifiable Evolution](https://arxiv.org/abs/2602.09662) (2026) [[code]](https://github.com/UITron-hub/TreeCUA)
+ [GUI-Libra: Training Native GUI Agents to Reason and Act with Action-aware Supervision and Partially Verifiable RL](https://arxiv.org/abs/2602.22190) (2026)
+ [OS-Symphony: A Holistic Framework for Robust and Generalist Computer-Using Agent](https://arxiv.org/abs/2601.07779) (2026)
+ [OmegaUse: Building a General-Purpose GUI Agent for Autonomous Task Execution](https://arxiv.org/abs/2601.20380) (2026)
+ ![Star](https://img.shields.io/github/stars/showlab/showui-pi.svg?style=social&label=Star) [ShowUI-pi: Flow-based Generative Models as GUI Dexterous Hands](https://arxiv.org/abs/2512.24965) (2025) [[code]](https://github.com/showlab/showui-pi)
+ ![Star](https://img.shields.io/github/stars/lll6gg/UI-R1.svg?style=social&label=Star) [UI-R1: Enhancing Efficient Action Prediction of GUI Agents by Reinforcement Learning](https://arxiv.org/abs/2503.21620) (2025) [[code]](https://github.com/lll6gg/UI-R1)
+ [ScreenLLM: Stateful Screen Schema for Efficient Action Understanding and Prediction](https://arxiv.org/abs/2503.20978) (2025)
+ [GUI-Xplore: Empowering Generalizable GUI Agents with One Exploration](https://arxiv.org/abs/2503.17709) (2025)
+ ![Star](https://img.shields.io/github/stars/Wuzheng02/OS-Kairos.svg?style=social&label=Star) [OS-Kairos: Adaptive Interaction for MLLM-Powered GUI Agents](https://arxiv.org/abs/2503.16465) (2025) [[code]](https://github.com/Wuzheng02/OS-Kairos)
+ [SpiritSight Agent: Advanced GUI Agent with One Look](https://arxiv.org/abs/2503.03196) (2025) [[project]](https://hzhiyuan.github.io/SpiritSight-Agent)
+ ![Star](https://img.shields.io/github/stars/ZephinueCode/ToolTok.svg?style=social&label=Star) [ToolTok: Tool Tokenization for Efficient and Generalizable GUI Agents](https://arxiv.org/abs/2602.02548) (2026) [[code]](https://github.com/ZephinueCode/ToolTok)
+ [ActionEngine: From Reactive to Programmatic GUI Agents via State Machine Memory](https://arxiv.org/abs/2602.20502) (2026)
+ [MementoGUI: Learning Agentic Multimodal Memory Control for Long-Horizon GUI Agents](https://arxiv.org/abs/2605.18652) (2026)
+ [ReVision: Scaling Computer-Use Agents via Temporal Visual Redundancy Reduction](https://arxiv.org/abs/2605.11212) (2026)
+ [Learn from Weaknesses: Automated Domain Specialization for Small Computer-Use Agents](https://arxiv.org/abs/2605.28775) (2026)
+ [UI-KOBE: Knowledge-Oriented Behavior Exploration for Lightweight Graph-Guided GUI Agents](https://arxiv.org/abs/2605.29534) (2026)
+ [AQuaUI: Visual Token Reduction for GUI Agents with Adaptive Quadtrees](https://arxiv.org/abs/2605.19260) (2026)

## Web Agents

+ ![Star](https://img.shields.io/github/stars/OSU-NLP-Group/Mind2Web.svg?style=social&label=Star) [Mind2Web: Towards a Generalist Agent for the Web](https://arxiv.org/abs/2306.06070) (2023) [[code]](https://github.com/OSU-NLP-Group/Mind2Web)
+ ![Star](https://img.shields.io/github/stars/web-arena-x/webarena.svg?style=social&label=Star) [WebArena: A Realistic Web Environment for Building Autonomous Agents](https://arxiv.org/abs/2307.13854) (2023) [[code]](https://github.com/web-arena-x/webarena)
+ ![Star](https://img.shields.io/github/stars/web-arena-x/visualwebarena.svg?style=social&label=Star) [VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks](https://arxiv.org/abs/2401.13649) (ACL 2024) [[code]](https://github.com/web-arena-x/visualwebarena)
+ ![Star](https://img.shields.io/github/stars/MinorJerry/WebVoyager.svg?style=social&label=Star) [WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models](https://arxiv.org/abs/2401.13919) (2024) [[code]](https://github.com/MinorJerry/WebVoyager)
+ ![Star](https://img.shields.io/github/stars/McGill-NLP/weblinx.svg?style=social&label=Star) [WebLINX: Real-World Website Navigation with Multi-Turn Dialogue](https://arxiv.org/abs/2402.05930) (2024) [[code]](https://github.com/McGill-NLP/weblinx)
+ ![Star](https://img.shields.io/github/stars/princeton-nlp/WebShop.svg?style=social&label=Star) [WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents](https://arxiv.org/abs/2207.01206) (NeurIPS 2022; related web-agent foundation) [[code]](https://github.com/princeton-nlp/WebShop)
+ [World of Bits: An Open-Domain Platform for Web-Based Agents](https://proceedings.mlr.press/v70/shi17a.html) (ICML 2017; related web-agent foundation)
+ ![Star](https://img.shields.io/github/stars/OSU-NLP-Group/SeeAct.svg?style=social&label=Star) [GPT-4V(ision) is a Generalist Web Agent, if Grounded](https://arxiv.org/abs/2401.01614) (ICML 2024) [[code]](https://github.com/OSU-NLP-Group/SeeAct)
+ ![Star](https://img.shields.io/github/stars/THUDM/AutoWebGLM.svg?style=social&label=Star) [AutoWebGLM: Bootstrap and Reinforce a Large Language Model-based Web Navigating Agent](https://arxiv.org/abs/2404.03648) (KDD 2024) [[code]](https://github.com/THUDM/AutoWebGLM)
+ ![Star](https://img.shields.io/github/stars/EmergenceAI/Agent-E.svg?style=social&label=Star) [Agent-E: From Autonomous Web Navigation to Foundational Design Principles in Agentic Systems](https://arxiv.org/abs/2407.13032) (2024) [[code]](https://github.com/EmergenceAI/Agent-E)
+ [AdaptAgent: Adapting Multimodal Web Agents with Few-Shot Learning from Human Demonstrations](https://arxiv.org/abs/2411.13451) (2024)
+ ![Star](https://img.shields.io/github/stars/Alibaba-nlp/WebWalker.svg?style=social&label=Star) [WebWalker: Benchmarking LLMs in Web Traversal](https://github.com/Alibaba-nlp/WebWalker) (2025) [[code]](https://github.com/Alibaba-nlp/WebWalker)
+ [A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis](https://arxiv.org/abs/2307.12856) (ICLR 2024)
+ [LASER: LLM Agent with State-Space Exploration for Web Navigation](https://arxiv.org/abs/2309.08172) (2023)
+ ![Star](https://img.shields.io/github/stars/WebVLN/WebVLN.svg?style=social&label=Star) [WebVLN: Vision-and-Language Navigation on Websites](https://ojs.aaai.org/index.php/AAAI/article/view/27878) (AAAI 2024) [[code]](https://github.com/WebVLN/WebVLN)
+ [Multimodal Web Navigation with Instruction-Finetuned Foundation Models](https://arxiv.org/abs/2305.11854) (2023)
+ [AllTogether: Investigating the Efficacy of Spliced Prompt for Web Navigation using Large Language Models](https://arxiv.org/abs/2310.18331) (2023)
+ [On the Multi-turn Instruction Following for Conversational Web Agents](https://arxiv.org/abs/2402.15057) (2024)
+ ![Star](https://img.shields.io/github/stars/ServiceNow/WorkArena.svg?style=social&label=Star) [WorkArena: How Capable Are Web Agents at Solving Common Knowledge Work Tasks?](https://arxiv.org/abs/2403.07718) (2024) [[code]](https://github.com/ServiceNow/WorkArena)
+ [WebCanvas: Benchmarking Web Agents in Online Environments](https://arxiv.org/abs/2406.12373) (2024)
+ ![Star](https://img.shields.io/github/stars/ServiceNow/WorkArena.svg?style=social&label=Star) [WorkArena++: Towards Compositional Planning and Reasoning-based Common Knowledge Work Tasks](https://arxiv.org/abs/2407.05291) (2024) [[code]](https://github.com/ServiceNow/WorkArena)
+ [Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents](https://arxiv.org/abs/2408.07199) (2024)
+ [WebQuest: A Benchmark for Multimodal QA on Web Page Sequences](https://arxiv.org/abs/2409.13711) (2024)
+ ![Star](https://img.shields.io/github/stars/ai-nikolai/stateact.svg?style=social&label=Star) [StateAct: Enhancing LLM Base Agents via Self-prompting and State-tracking](https://arxiv.org/abs/2410.02810) (2024) [[code]](https://github.com/ai-nikolai/stateact)
+ [OpenWebVoyager: Building Multimodal Web Agents via Iterative Real-World Exploration, Feedback and Optimization](https://arxiv.org/abs/2410.19609) (2024)
+ [Web Agents with World Models: Learning and Leveraging Environment Dynamics in Web Navigation](https://arxiv.org/abs/2410.13232) (2024)
+ [Auto-Intent: Automated Intent Discovery and Self-Exploration for Large Language Model Web Agents](https://arxiv.org/abs/2410.22552) (2024)
+ [API-Based Web Agents](https://arxiv.org/abs/2410.16464) (2024)
+ [AgentOccam: A Simple Yet Strong Baseline for LLM-Based Web Agents](https://arxiv.org/abs/2410.13825) (2024)
+ [WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning](https://arxiv.org/abs/2411.02337) (2024)
+ ![Star](https://img.shields.io/github/stars/ServiceNow/BrowserGym.svg?style=social&label=Star) [The BrowserGym Ecosystem for Web Agent Research](https://arxiv.org/abs/2412.05467) (2024) [[code]](https://github.com/ServiceNow/BrowserGym)
+ [WEPO: Web Element Preference Optimization for LLM-based Web Navigation](https://arxiv.org/abs/2412.10742) (2024)
+ [Proposer-Agent-Evaluator: Autonomous Skill Discovery For Foundation Model Internet Agents](https://arxiv.org/abs/2412.13194) (2024) [[project]](https://yanqval.github.io/PAE/)
+ [AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials](https://arxiv.org/abs/2412.09605) (2024)
+ [WebDancer: Towards Autonomous Information Seeking Agency](https://arxiv.org/abs/2505.22648) (2025)
+ [WebSailor: Navigating Super-human Reasoning for Web Agent](https://arxiv.org/abs/2507.02592) (2025)
+ [RealWebAssist: A Benchmark for Long-Horizon Web Assistance with Real-World Users](https://arxiv.org/abs/2504.10445) (2025)
+ [WebSTAR: Scalable Data Synthesis for Computer Use Agents with Step-Level Filtering](https://arxiv.org/abs/2512.10962) (2025)
+ [AutoWebWorld: Synthesizing Infinite Verifiable Web Environments via Finite State Machines](https://arxiv.org/abs/2602.14296) (2026)
+ [WebFactory: Automated Compression of Foundational Language Intelligence into Grounded Web Agents](https://arxiv.org/abs/2603.05044) (2026)
+ [AutoSurfer: Teaching Web Agents through Comprehensive Surfing, Learning, and Modeling](https://arxiv.org/abs/2604.27253) (2026)
+ [Region4Web: Rethinking Observation Space Granularity for Web Agents](https://arxiv.org/abs/2605.07134) (2026)
+ [Weblica: Scalable and Reproducible Training Environments for Visual Web Agents](https://arxiv.org/abs/2605.06761) (2026)
+ [ShopGym: An Integrated Framework for Realistic Simulation and Scalable Benchmarking of E-Commerce Web Agents](https://arxiv.org/abs/2605.16116) (2026)
+ [Odysseys: Benchmarking Web Agents on Realistic Long Horizon Tasks](https://arxiv.org/abs/2604.24964) (2026) [[website]](https://odysseys-website.pages.dev)
+ ![Star](https://img.shields.io/github/stars/UniPat-AI/SaaS-Bench.svg?style=social&label=Star) [SaaS-Bench: Can Computer-Use Agents Leverage Real-World SaaS to Solve Professional Workflows?](https://arxiv.org/abs/2605.15777) (2026) [[code]](https://github.com/UniPat-AI/SaaS-Bench)
+ [Agent JIT Compilation for Latency-Optimizing Web Agent Planning and Scheduling](https://arxiv.org/abs/2605.21470) (ICML 2026)
+ [MolmoWeb: Open Visual Web Agent and Open Data for the Open Web](https://arxiv.org/abs/2604.08516) (2026)
+ [WebChain: A Large-Scale Human-Annotated Dataset of Real-World Web Interaction Traces](https://arxiv.org/abs/2603.05295) (2026)
+ [Vision2Web: A Hierarchical Benchmark for Visual Website Development with Agent Verification](https://arxiv.org/abs/2603.26648) (2026)
+ [WebTestPilot: Agentic End-to-End Web Testing against Natural Language Specification by Inferring Oracles with Symbolized GUI Elements](https://arxiv.org/abs/2602.11724) (2026)
+ [Web Agents Should Adopt the Plan-Then-Execute Paradigm](https://arxiv.org/abs/2605.14290) (2026)
+ [WebUncertainty: Dual-Level Uncertainty Driven Planning and Reasoning For Autonomous Web Agent](https://arxiv.org/abs/2604.17821) (2026)
+ [MM-WebAgent: A Hierarchical Multimodal Web Agent for Webpage Generation](https://arxiv.org/abs/2604.15309) (2026) [[project]](https://aka.ms/mm-webagent)

## Mobile Agents

+ [Android in the Wild: A Large-Scale Dataset for Android Device Control](https://arxiv.org/abs/2307.10088) (2023)
+ ![Star](https://img.shields.io/github/stars/mnotgod96/AppAgent.svg?style=social&label=Star) [AppAgent: Multimodal Agents as Smartphone Users](https://arxiv.org/abs/2312.13771) (2023) [[code]](https://github.com/mnotgod96/AppAgent)
+ ![Star](https://img.shields.io/github/stars/X-PLUG/MobileAgent.svg?style=social&label=Star) [Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent](https://arxiv.org/abs/2401.16158) (2024) [[code]](https://github.com/X-PLUG/MobileAgent)
+ ![Star](https://img.shields.io/github/stars/X-PLUG/MobileAgent.svg?style=social&label=Star) [Mobile-Agent-v2: Mobile Device Operation Assistant with Effective Navigation via Multi-Agent Collaboration](https://arxiv.org/abs/2406.01014) (2024) [[code]](https://github.com/X-PLUG/MobileAgent)
+ [GUI Odyssey: A Comprehensive Dataset for Cross-App GUI Navigation on Mobile Devices](https://arxiv.org/abs/2406.08451) (2024)
+ [Rico: A Mobile App Dataset for Building Data-Driven Design Applications](https://dl.acm.org/doi/10.1145/3126594.3126651) (UIST 2017; related UI dataset)
+ ![Star](https://img.shields.io/github/stars/zzxslp/MM-Navigator.svg?style=social&label=Star) [GPT-4V in Wonderland: Large Multimodal Models for Zero-Shot Smartphone GUI Navigation](https://arxiv.org/abs/2311.07562) (2023) [[code]](https://github.com/zzxslp/MM-Navigator)
+ [Comprehensive Cognitive LLM Agent for Smartphone GUI Automation](https://arxiv.org/abs/2402.11941) (2024)
+ [Explore, Select, Derive, and Recall: Augmenting LLM with Human-like Memory for Mobile Task Automation](https://arxiv.org/abs/2312.03003) (MobiCom 2024)
+ ![Star](https://img.shields.io/github/stars/IMNearth/CoAT.svg?style=social&label=Star) [Android in the Zoo: Chain-of-Action-Thought for GUI Agents](https://arxiv.org/abs/2403.02713) (2024) [[code]](https://github.com/IMNearth/CoAT)
+ [MobileFlow: A Multimodal LLM For Mobile GUI Agent](https://arxiv.org/abs/2407.04346) (2024)
+ ![Star](https://img.shields.io/github/stars/OpenDFM/MobA.svg?style=social&label=Star) [MobA: Multifaceted Memory-Enhanced Adaptive Planning for Efficient Mobile Task Automation](https://arxiv.org/abs/2410.13757) (NAACL 2025 Demo) [[code]](https://github.com/OpenDFM/MobA)
+ [AppAgent v2: Advanced Agent for Flexible Mobile Interactions](https://arxiv.org/abs/2408.11824) (2024)
+ [MobileVLM: A Vision-Language Model for Better Intra- and Inter-UI Understanding](https://arxiv.org/abs/2409.14818) (2024)
+ [Octopus: On-device language model for function calling of software APIs](https://arxiv.org/abs/2404.01549) (2024)
+ [Octopus v2: On-device language model for super agent](https://arxiv.org/abs/2404.01744) (2024)
+ [Mobile-Env: Building Qualified Evaluation Benchmarks for LLM-GUI Interaction](https://arxiv.org/abs/2305.08144) (2023)
+ [DroidBot-GPT: GPT-powered UI Automation for Android](https://arxiv.org/abs/2304.07061) (2023)
+ [Training a Vision Language Model as Smartphone Assistant](https://arxiv.org/abs/2404.08755) (2024)
+ [Large Language Models for Mobile GUI Text Input Generation: An Empirical Study](https://arxiv.org/abs/2404.08948) (2024)
+ [Mobile-Bench: An Evaluation Benchmark for LLM-based Mobile Agents](https://arxiv.org/abs/2407.00993) (2024)
+ [MobileViews: A Million-scale and Diverse Mobile GUI Dataset](https://arxiv.org/abs/2409.14337) (2024) [[data]](https://huggingface.co/datasets/mllmTeam/MobileViews)
+ ![Star](https://img.shields.io/github/stars/UbiquitousLearning/DroidCall.svg?style=social&label=Star) [DroidCall: A Dataset for LLM-powered Android Intent Invocation](https://arxiv.org/abs/2412.00402) (2024) [[code]](https://github.com/UbiquitousLearning/DroidCall)
+ ![Star](https://img.shields.io/github/stars/MobileLLM/AutoDroid-V2.svg?style=social&label=Star) [AutoDroid-V2: Boosting SLM-based GUI Agents via Code Generation](https://arxiv.org/abs/2412.18116) (2024) [[code]](https://github.com/MobileLLM/AutoDroid-V2)
+ [From Interaction to Impact: Towards Safer AI Agents Through Understanding and Evaluating Mobile UI Operation Impacts](https://arxiv.org/abs/2410.09006) (2024)
+ ![Star](https://img.shields.io/github/stars/lgy0404/LearnAct.svg?style=social&label=Star) [LearnAct: Few-Shot Mobile GUI Agent with a Unified Demonstration Benchmark](https://arxiv.org/abs/2504.13805) (2025) [[code]](https://github.com/lgy0404/LearnAct)
+ ![Star](https://img.shields.io/github/stars/wwh0411/FedMABench.svg?style=social&label=Star) [FedMABench: Benchmarking Mobile Agents on Decentralized Heterogeneous User Data](https://arxiv.org/abs/2503.05143) (2025) [[code]](https://github.com/wwh0411/FedMABench)
+ ![Star](https://img.shields.io/github/stars/OpenBMB/AgentCPM-GUI.svg?style=social&label=Star) [AgentCPM-GUI: Building Mobile-Use Agents with Reinforcement Fine-Tuning](https://arxiv.org/abs/2506.01391) (2025) [[code]](https://github.com/OpenBMB/AgentCPM-GUI)
+ ![Star](https://img.shields.io/github/stars/X-PLUG/MobileAgent.svg?style=social&label=Star) [Mobile-Agent-v3: Fundamental Agents for GUI Automation](https://arxiv.org/abs/2508.15144) (2025) [[code]](https://github.com/X-PLUG/MobileAgent)
+ ![Star](https://img.shields.io/github/stars/X-PLUG/MobileAgent.svg?style=social&label=Star) [Mobile-Agent-v3.5: Multi-platform Fundamental GUI Agents](https://arxiv.org/abs/2602.16855) (2026) [[code]](https://github.com/X-PLUG/MobileAgent)
+ [MagicGUI: A Foundational Mobile GUI Agent with Scalable Data Pipeline and Reinforcement Fine-tuning](https://arxiv.org/abs/2508.03700) (2025)
+ [OpenPhone: Mobile Agentic Foundation Models](https://arxiv.org/abs/2510.22009) (2025)
+ ![Star](https://img.shields.io/github/stars/MadeAgents/mobile-use.svg?style=social&label=Star) [MobileUse: A GUI Agent with Hierarchical Reflection for Autonomous Mobile Operation](https://arxiv.org/abs/2507.16853) (2025) [[code]](https://github.com/MadeAgents/mobile-use)
+ ![Star](https://img.shields.io/github/stars/LaoKuiZe/AppAgent-Pro.svg?style=social&label=Star) [AppAgent-Pro: A Proactive GUI Agent System for Multidomain Information Integration and User Assistance](https://arxiv.org/abs/2508.18689) (2025) [[code]](https://github.com/LaoKuiZe/AppAgent-Pro)
+ ![Star](https://img.shields.io/github/stars/THUDM/MobileRL.svg?style=social&label=Star) [MobileRL: Online Agentic Reinforcement Learning for Mobile GUI Agents](https://arxiv.org/abs/2509.18119) (2025) [[code]](https://github.com/THUDM/MobileRL)
+ ![Star](https://img.shields.io/github/stars/X-PLUG/MobileAgent.svg?style=social&label=Star) [UI-S1: Advancing GUI Automation via Semi-online Reinforcement Learning](https://arxiv.org/abs/2509.11543) (2025) [[code]](https://github.com/X-PLUG/MobileAgent/tree/main/UI-S1)
+ [AndroidDaily: A Verifiable Benchmark for Mobile GUI Agents on Real-World Closed-Source Applications](https://arxiv.org/abs/2605.27761) (2026)
+ [MobileGym: A Verifiable and Highly Parallel Simulation Platform for Mobile GUI Agent Research](https://arxiv.org/abs/2605.26114) (2026) [[website]](https://mobilegym.github.io)
+ [STAMP: Training Explicit Memory for Mobile GUI Agents in Controllable and Scalable Virtual Environments](https://arxiv.org/abs/2605.29324) (2026)
+ [UI-KOBE: Knowledge-Oriented Behavior Exploration for Lightweight Graph-Guided GUI Agents](https://arxiv.org/abs/2605.29534) (2026)
+ ![Star](https://img.shields.io/github/stars/Zhixin-L/TIPO.svg?style=social&label=Star) [Mobile GUI Agent Privacy Personalization with Trajectory Induced Preference Optimization](https://arxiv.org/abs/2604.11259) (2026) [[code]](https://github.com/Zhixin-L/TIPO)
+ [CORA: Conformal Risk-Controlled Agents for Safeguarded Mobile GUI Automation](https://arxiv.org/abs/2604.09155) (2026)
+ [OmniGUI: Benchmarking GUI Agents in Omni-Modal Smartphone Environments](https://arxiv.org/abs/2605.18758) (2026) [[website]](https://omni-gui.github.io)
+ ![Star](https://img.shields.io/github/stars/V-Droid-Agent/V-Droid.svg?style=social&label=Star) [Advancing Mobile GUI Agents: A Verifier-Driven Approach to Practical Deployment](https://arxiv.org/abs/2503.15937) (2025) [[code]](https://github.com/V-Droid-Agent/V-Droid)
+ [Mobile-Agent-E: Self-Evolving Mobile Assistant for Complex Tasks](https://arxiv.org/abs/2501.11733) (2025) [[project]](https://x-plug.github.io/MobileAgent)
+ [AppAgentX: Evolving GUI Agents as Proficient Smartphone Users](https://arxiv.org/abs/2503.02268) (2025)
+ [Does Chain-of-Thought Reasoning Help Mobile GUI Agent? An Empirical Study](https://arxiv.org/abs/2503.16788) (2025) [[code]](https://github.com/LlamaTouch/VLM-Reasoning-Traces)
+ [Mobile-Bench-v2: A More Realistic and Comprehensive Benchmark for VLM-based Mobile Agents](https://arxiv.org/abs/2505.11891) (2025) [[data]](https://huggingface.co/datasets/xwk123/MobileBench-v2)
+ [Mobile-Agent-V: A Video-Guided Approach for Effortless and Efficient Operational Knowledge Injection in Mobile Automation](https://arxiv.org/abs/2505.13887) (2025)
+ [MobileIPL: Enhancing Mobile Agents Thinking Process via Iterative Preference Learning](https://arxiv.org/abs/2505.12299) (2025)
+ [Mobile-R1: Towards Interactive Capability for VLM-Based Mobile Agent via Systematic Training](https://arxiv.org/abs/2506.20332) (2025) [[project]](https://mobile-r1.github.io/Mobile-R1/)
+ [Atomic-to-Compositional Generalization for Mobile Agents with A New Benchmark and Scheduling System](https://arxiv.org/abs/2506.08972) (2025) [[project]](https://ui-nexus.github.io)
+ [MobileGUI-RL: Advancing Mobile GUI Agent through Reinforcement Learning in Online Environment](https://arxiv.org/abs/2507.05720) (2025)
+ [MVISU-Bench: Benchmarking Mobile Agents for Real-World Tasks by Multi-App, Vague, Interactive, Single-App and Unethical Instructions](https://arxiv.org/abs/2508.09057) (ACM MM 2025)
+ [InquireMobile: Teaching VLM-based Mobile Agent to Request Human Assistance via Reinforcement Fine-Tuning](https://arxiv.org/abs/2508.19679) (2025)
+ ![Star](https://img.shields.io/github/stars/liuxiaojieOutOfWorld/MobileRAG_arxiv.svg?style=social&label=Star) [MobileRAG: Enhancing Mobile Agent with Retrieval-Augmented Generation](https://arxiv.org/abs/2509.03891) (2025) [[code]](https://github.com/liuxiaojieOutOfWorld/MobileRAG_arxiv)
+ [MAS-Bench: A Unified Benchmark for Shortcut-Augmented Hybrid Mobile GUI Agents](https://arxiv.org/abs/2509.06477) (2025) [[website]](https://pengxiang-zhao.github.io/MAS-Bench)
+ ![Star](https://img.shields.io/github/stars/MadeAgents/ColorBench.svg?style=social&label=Star) [ColorBench: Benchmarking Mobile Agents with Graph-Structured Framework for Complex Long-Horizon Tasks](https://arxiv.org/abs/2510.14621) (2025) [[code]](https://github.com/MadeAgents/ColorBench)
+ [Mobile-Agent-RAG: Driving Smart Multi-Agent Coordination with Contextual Knowledge Empowerment for Long-Horizon Mobile Automation](https://arxiv.org/abs/2511.12254) (2025)
+ [MobiBench: Multi-Branch, Modular Benchmark for Mobile GUI Agents](https://arxiv.org/abs/2512.12634) (2025)
+ ![Star](https://img.shields.io/github/stars/jacklishufan/MobileWorld.svg?style=social&label=Star) [MobileWorldBench: Towards Semantic World Modeling For Mobile Agents](https://arxiv.org/abs/2512.14014) (2025) [[code]](https://github.com/jacklishufan/MobileWorld)
+ [MobileWorld: Benchmarking Autonomous Mobile Agents in Agent-User Interactive and MCP-Augmented Environments](https://arxiv.org/abs/2512.19432) (2025)
+ [PhoneWorld: Scaling Phone-Use Agent Environments](https://arxiv.org/abs/2605.29486) (2026)
+ [OpenMobile: Building Open Mobile Agents with Task and Trajectory Synthesis](https://arxiv.org/abs/2604.15093) (2026) [[project]](https://njucckevin.github.io/openmobile/)
+ [KnowU-Bench: Towards Interactive, Proactive, and Personalized Mobile Agent Evaluation](https://arxiv.org/abs/2604.08455) (2026)
+ [Do LLMs Need to See Everything? A Benchmark and Study of Failures in LLM-driven Smartphone Automation using Screentext vs. Screenshots](https://arxiv.org/abs/2604.17817) (2026)
+ [MobiFlow: Real-World Mobile Agent Benchmarking through Trajectory Fusion](https://arxiv.org/abs/2604.09587) (2026)
+ [ProactiveMobile: A Comprehensive Benchmark for Boosting Proactive Intelligence on Mobile Devices](https://arxiv.org/abs/2602.21858) (2026)
+ [AmbiBench: Benchmarking Mobile GUI Agents Beyond One-Shot Instructions in the Wild](https://arxiv.org/abs/2602.11750) (2026)
+ [Me-Agent: A Personalized Mobile Agent with Two-Level User Habit Learning for Enhanced Interaction](https://arxiv.org/abs/2601.20162) (2026)
+ [MobileBench-OL: A Comprehensive Chinese Benchmark for Evaluating Mobile GUI Agents in Real-World Environment](https://arxiv.org/abs/2601.20335) (2026)
+ [Generative Visual Code Mobile World Models](https://arxiv.org/abs/2602.01576) (2026)

## Desktop and Computer-Use Agents

+ ![Star](https://img.shields.io/github/stars/showlab/assistgui.svg?style=social&label=Star) [AssistGUI: Task-Oriented Desktop Graphical User Interface Automation](https://arxiv.org/abs/2312.13108) (CVPR 2024) [[code]](https://github.com/showlab/assistgui)
+ ![Star](https://img.shields.io/github/stars/xlang-ai/OSWorld.svg?style=social&label=Star) [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://arxiv.org/abs/2404.07972) (2024) [[code]](https://github.com/xlang-ai/OSWorld)
+ [OmniACT: A Dataset and Benchmark for Enabling Multimodal Generalist Autonomous Agents for Desktop and Web](https://arxiv.org/abs/2402.17553) (2024)
+ ![Star](https://img.shields.io/github/stars/showlab/computer_use_ootb.svg?style=social&label=Star) [Computer Use Out-of-the-box](https://github.com/showlab/computer_use_ootb)
+ ![Star](https://img.shields.io/github/stars/OpenInterpreter/open-interpreter.svg?style=social&label=Star) [Open Interpreter](https://github.com/OpenInterpreter/open-interpreter)
+ [A Zero-Shot Language Agent for Computer Control with Structured Reflection](https://arxiv.org/abs/2310.08740) (2023)
+ ![Star](https://img.shields.io/github/stars/microsoft/UFO.svg?style=social&label=Star) [UFO: A UI-Focused Agent for Windows OS Interaction](https://arxiv.org/abs/2402.07939) (2024) [[code]](https://github.com/microsoft/UFO)
+ ![Star](https://img.shields.io/github/stars/OS-Copilot/OS-Copilot.svg?style=social&label=Star) [OS-Copilot: Towards Generalist Computer Agents with Self-Improvement](https://arxiv.org/abs/2402.07456) (2024) [[code]](https://github.com/OS-Copilot/OS-Copilot)
+ ![Star](https://img.shields.io/github/stars/niuzaisheng/ScreenAgent.svg?style=social&label=Star) [ScreenAgent: A Computer Control Agent Driven by Visual Language Large Model](https://arxiv.org/abs/2402.07945) (2024) [[code]](https://github.com/niuzaisheng/ScreenAgent)
+ ![Star](https://img.shields.io/github/stars/BAAI-Agents/Cradle.svg?style=social&label=Star) [Towards General Computer Control: A Multimodal Agent for Red Dead Redemption II](https://arxiv.org/abs/2403.03186) (2024) [[code]](https://github.com/BAAI-Agents/Cradle)
+ ![Star](https://img.shields.io/github/stars/GAIR-NLP/PC-Agent.svg?style=social&label=Star) [PC Agent: While You Sleep, AI Works](https://arxiv.org/abs/2412.17589) (2024) [[code]](https://github.com/GAIR-NLP/PC-Agent)
+ ![Star](https://img.shields.io/github/stars/OS-Copilot/ScienceBoard.svg?style=social&label=Star) [ScienceBoard: Evaluating Multimodal Autonomous Agents in Realistic Scientific Workflows](https://arxiv.org/abs/2505.19897) (2025) [[code]](https://github.com/OS-Copilot/ScienceBoard)
+ ![Star](https://img.shields.io/github/stars/xlang-ai/Spider2-V.svg?style=social&label=Star) [Spider2-V: How Far Are Multimodal Agents From Automating Data Science and Engineering Workflows?](https://arxiv.org/abs/2407.10956) (2024) [[code]](https://github.com/xlang-ai/Spider2-V)
+ ![Star](https://img.shields.io/github/stars/microsoft/WindowsAgentArena.svg?style=social&label=Star) [Windows Agent Arena](https://arxiv.org/abs/2409.08264) (2024) [[code]](https://github.com/microsoft/WindowsAgentArena) [[website]](https://microsoft.github.io/WindowsAgentArena)
+ ![Star](https://img.shields.io/github/stars/BraveGroup/SheetCopilot.svg?style=social&label=Star) [SheetCopilot: Bringing Software Productivity to the Next Level through Large Language Models](https://arxiv.org/abs/2305.19308) (NeurIPS 2023) [[code]](https://github.com/BraveGroup/SheetCopilot)
+ ![Star](https://img.shields.io/github/stars/showlab/GUI-Action-Narrator.svg?style=social&label=Star) [GUI Action Narrator: Where and When Did That Action Take Place?](https://arxiv.org/abs/2406.13719) (2024) [[code]](https://github.com/showlab/GUI-Action-Narrator)
+ [Ponder & Press: Advancing Visual GUI Agent towards General Computer Control](https://arxiv.org/abs/2412.01268) (2024) [[project]](https://invinciblewyq.github.io/ponder-press-page/)
+ [OSCAR: Operating System Control via State-Aware Reasoning and Re-Planning](https://arxiv.org/abs/2410.18963) (2024)
+ ![Star](https://img.shields.io/github/stars/caap-agent/caap-agent.svg?style=social&label=Star) [CAAP: Context-Aware Action Planning Prompting to Solve Computer Tasks with Front-End UI Only](https://arxiv.org/abs/2406.06947) (2024) [[code]](https://github.com/caap-agent/caap-agent)
+ [SmartFlow: Robotic Process Automation using LLMs](https://arxiv.org/abs/2405.12842) (2024) [[project]](https://smartflow-4c5a0a.webflow.io/)
+ ![Star](https://img.shields.io/github/stars/sqzhang-lazy/D-PoT.svg?style=social&label=Star) [Dynamic Planning for LLM-based Graphical User Interface Automation](https://arxiv.org/abs/2410.00467) (2024) [[code]](https://github.com/sqzhang-lazy/D-PoT)
+ [IDA: Breaking Barriers in No-code UI Automation Through Large Language Models and Human-Centric Design](https://arxiv.org/abs/2407.15673) (2024)
+ [Identifying User Goals from UI Trajectories](https://arxiv.org/abs/2406.14314) (2024)
+ ![Star](https://img.shields.io/github/stars/showlab/WorldGUI.svg?style=social&label=Star) [WorldGUI: An Interactive Benchmark for Desktop GUI Automation from Any Starting Point](https://arxiv.org/abs/2502.08047) (Tech Report 2025) [[code]](https://github.com/showlab/WorldGUI)
+ ![Star](https://img.shields.io/github/stars/xlang-ai/OpenCUA.svg?style=social&label=Star) [OpenCUA: Open Foundations for Computer-Use Agents](https://arxiv.org/abs/2508.09123) (2025) [[code]](https://github.com/xlang-ai/OpenCUA)
+ ![Star](https://img.shields.io/github/stars/THUDM/ComputerRL.svg?style=social&label=Star) [ComputerRL: Scaling End-to-End Online Reinforcement Learning for Computer Use Agents](https://arxiv.org/abs/2508.14040) (2025) [[code]](https://github.com/thudm/ComputerRL)
+ ![Star](https://img.shields.io/github/stars/OpenGVLab/ScaleCUA.svg?style=social&label=Star) [ScaleCUA: Scaling Open-Source Computer Use Agents with Cross-Platform Data](https://arxiv.org/abs/2509.15221) (2025) [[code]](https://github.com/OpenGVLab/ScaleCUA)
+ [CoAct-1: Computer-using Multi-Agent System with Coding Actions](https://arxiv.org/abs/2508.03923) (2025)
+ [CODA: Coordinating the Cerebrum and Cerebellum for a Dual-Brain Computer Use Agent with Decoupled Reinforcement Learning](https://arxiv.org/abs/2508.20096) (2025)
+ [Magentic-UI: Towards Human-in-the-loop Agentic Systems](https://arxiv.org/abs/2507.22358) (2025) [[code]](https://github.com/microsoft/magentic-ui)
+ [OSWorld-MCP: Benchmarking MCP Tool Invocation In Computer-Use Agents](https://arxiv.org/abs/2510.24563) (2025) [[website]](https://osworld-mcp.github.io)
+ [CUARewardBench: A Benchmark for Evaluating Reward Models on Computer-using Agent](https://arxiv.org/abs/2510.18596) (2025)
+ [OpenComputer: Verifiable Software Worlds for Computer-Use Agents](https://arxiv.org/abs/2605.19769) (2026)
+ [CUA-Gym: Scaling Verifiable Training Environments and Tasks for Computer-Use Agents](https://arxiv.org/abs/2605.25624) (2026)
+ [WindowsWorld: A Process-Centric Benchmark of Autonomous GUI Agents in Professional Cross-Application Environments](https://arxiv.org/abs/2604.27776) (2026)
+ [CUA-Suite: Massive Human-annotated Video Demonstrations for Computer-Use Agents](https://arxiv.org/abs/2603.24440) (2026)
+ [OS-Marathon: Benchmarking Computer-Use Agents on Long-Horizon Repetitive Tasks](https://arxiv.org/abs/2601.20650) (2026) [[website]](https://os-marathon.github.io/)
+ [ProSoftArena: Benchmarking Hierarchical Capabilities of Multimodal Agents in Professional Software Environments](https://arxiv.org/abs/2601.02399) (2025) [[website]](https://prosoftarena.github.io)
+ ![Star](https://img.shields.io/github/stars/friedrichor/WebTestBench.svg?style=social&label=Star) [WebTestBench: Evaluating Computer-Use Agents towards End-to-End Automated Web Testing](https://arxiv.org/abs/2603.25226) (2026) [[code]](https://github.com/friedrichor/WebTestBench)
+ [ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents](https://arxiv.org/abs/2605.12481) (2026) [[project]](https://x-plug.github.io/ToolCUA/)
+ ![Star](https://img.shields.io/github/stars/X-PLUG/MobileAgent.svg?style=social&label=Star) [PC-Agent: A Hierarchical Multi-Agent Collaboration Framework for Complex Task Automation on PC](https://arxiv.org/abs/2502.14282) (2025) [[code]](https://github.com/X-PLUG/MobileAgent/tree/main/PC-Agent)
+ [DeskVision: Large Scale Desktop Region Captioning for Advanced GUI Agents](https://arxiv.org/abs/2503.11170) (2025)
+ ![Star](https://img.shields.io/github/stars/Alokia/COLA-demo.svg?style=social&label=Star) [COLA: A Scalable Multi-Agent Framework For Windows UI Task Automation](https://arxiv.org/abs/2503.09263) (2025) [[code]](https://github.com/Alokia/COLA-demo)
+ [GUIrilla: A Scalable Framework for Automated Desktop UI Exploration](https://arxiv.org/abs/2510.16051) (2025)
+ [ScreenSearch: Uncertainty-Aware OS Exploration](https://arxiv.org/abs/2605.16024) (2026)
+ [HealthAdminBench: Evaluating Computer-Use Agents on Healthcare Administration Tasks](https://arxiv.org/abs/2604.09937) (2026)
+ [EntWorld: A Holistic Environment and Benchmark for Verifiable Enterprise GUI Agents](https://arxiv.org/abs/2601.17722) (2026)
+ [OSExpert: Computer-Use Agents Learning Professional Skills via Exploration](https://arxiv.org/abs/2603.07978) (2026)
+ [Computer-Using World Model](https://arxiv.org/abs/2602.17365) (2026)
+ [IntentCUA: Learning Intent-level Representations for Skill Abstraction and Multi-Agent Planning in Computer-Use Agents](https://arxiv.org/abs/2602.17049) (2026)
+ [TClone: Low-Latency Forking of Live GUI Environments for Computer-Use Agents](https://arxiv.org/abs/2605.17320) (2026)

## Evaluation and Benchmarks

+ ![Star](https://img.shields.io/github/stars/OSU-NLP-Group/Mind2Web.svg?style=social&label=Star) [Mind2Web](https://arxiv.org/abs/2306.06070) (2023) [[code]](https://github.com/OSU-NLP-Group/Mind2Web)
+ ![Star](https://img.shields.io/github/stars/web-arena-x/webarena.svg?style=social&label=Star) [WebArena](https://arxiv.org/abs/2307.13854) (2023) [[code]](https://github.com/web-arena-x/webarena)
+ ![Star](https://img.shields.io/github/stars/web-arena-x/visualwebarena.svg?style=social&label=Star) [VisualWebArena](https://arxiv.org/abs/2401.13649) (ACL 2024) [[code]](https://github.com/web-arena-x/visualwebarena)
+ ![Star](https://img.shields.io/github/stars/xlang-ai/OSWorld.svg?style=social&label=Star) [OSWorld](https://arxiv.org/abs/2404.07972) (2024) [[code]](https://github.com/xlang-ai/OSWorld)
+ [ScreenSpot](https://arxiv.org/abs/2401.10935) (ACL 2024)
+ [VisualWebBench](https://arxiv.org/abs/2404.05955) (2024)
+ [Android in the Wild](https://arxiv.org/abs/2307.10088) (2023)
+ [GUI Odyssey](https://arxiv.org/abs/2406.08451) (2024)
+ ![Star](https://img.shields.io/github/stars/skyworkai/agent-studio.svg?style=social&label=Star) [AgentStudio](https://arxiv.org/abs/2403.17918) (2024) [[code]](https://github.com/skyworkai/agent-studio)
+ ![Star](https://img.shields.io/github/stars/LlamaTouch/LlamaTouch.svg?style=social&label=Star) [LlamaTouch](https://arxiv.org/abs/2404.16054) (2024) [[code]](https://github.com/LlamaTouch/LlamaTouch)
+ ![Star](https://img.shields.io/github/stars/MobileAgentBench/mobile-agent-bench.svg?style=social&label=Star) [MobileAgentBench](https://arxiv.org/abs/2406.08184) (2024) [[code]](https://github.com/MobileAgentBench/mobile-agent-bench)
+ ![Star](https://img.shields.io/github/stars/google-research/android_world.svg?style=social&label=Star) [AndroidWorld](https://arxiv.org/abs/2405.14573) (2024) [[code]](https://github.com/google-research/android_world)
+ ![Star](https://img.shields.io/github/stars/camel-ai/crab.svg?style=social&label=Star) [CRAB](https://arxiv.org/abs/2407.01511) (2024) [[code]](https://github.com/camel-ai/crab)
+ ![Star](https://img.shields.io/github/stars/xlang-ai/Spider2-V.svg?style=social&label=Star) [Spider2-V](https://arxiv.org/abs/2407.10956) (2024) [[code]](https://github.com/xlang-ai/Spider2-V)
+ ![Star](https://img.shields.io/github/stars/YuxiangChai/AMEX-codebase.svg?style=social&label=Star) [AMEX](https://arxiv.org/abs/2407.17490) (2024) [[code]](https://github.com/YuxiangChai/AMEX-codebase)
+ ![Star](https://img.shields.io/github/stars/microsoft/WindowsAgentArena.svg?style=social&label=Star) [Windows Agent Arena](https://arxiv.org/abs/2409.08264) (2024) [[code]](https://github.com/microsoft/WindowsAgentArena) [[website]](https://microsoft.github.io/WindowsAgentArena)
+ [SPA-Bench](https://arxiv.org/abs/2410.15164) (ICLR 2025)
+ ![Star](https://img.shields.io/github/stars/likaixin2000/ScreenSpot-Pro-GUI-Grounding.svg?style=social&label=Star) [ScreenSpot-Pro](https://arxiv.org/abs/2504.07981) (2025) [[code]](https://github.com/likaixin2000/ScreenSpot-Pro-GUI-Grounding) [[leaderboard]](https://gui-agent.github.io/grounding-leaderboard)
+ ![Star](https://img.shields.io/github/stars/showlab/WorldGUI.svg?style=social&label=Star) [WorldGUI](https://arxiv.org/abs/2502.08047) (Tech Report 2025) [[code]](https://github.com/showlab/WorldGUI)
+ ![Star](https://img.shields.io/github/stars/OS-Copilot/ScienceBoard.svg?style=social&label=Star) [ScienceBoard](https://arxiv.org/abs/2505.19897) (2025) [[code]](https://github.com/OS-Copilot/ScienceBoard)
+ ![Star](https://img.shields.io/github/stars/lgy0404/LearnAct.svg?style=social&label=Star) [LearnAct](https://arxiv.org/abs/2504.13805) (2025) [[code]](https://github.com/lgy0404/LearnAct)
+ ![Star](https://img.shields.io/github/stars/THUDM/VisualAgentBench.svg?style=social&label=Star) [VisualAgentBench](https://arxiv.org/abs/2408.06327) (2024) [[code]](https://github.com/THUDM/VisualAgentBench)
+ [A3: Android Agent Arena](https://arxiv.org/abs/2501.01149) (2025)
+ ![Star](https://img.shields.io/github/stars/Alibaba-nlp/WebWalker.svg?style=social&label=Star) [WebWalker](https://github.com/Alibaba-nlp/WebWalker) (2025) [[code]](https://github.com/Alibaba-nlp/WebWalker)
+ ![Star](https://img.shields.io/github/stars/runamu/monday.svg?style=social&label=Star) [MONDAY](https://arxiv.org/abs/2505.12632) (CVPR 2025) [[code]](https://github.com/runamu/monday)
+ ![Star](https://img.shields.io/github/stars/open-compass/MMBench-GUI.svg?style=social&label=Star) [MMBench-GUI](https://arxiv.org/abs/2507.19478) (2025) [[code]](https://github.com/open-compass/MMBench-GUI)
+ [macOSWorld](https://arxiv.org/abs/2506.04135) (2025) [[website]](https://macos-world.github.io)
+ ![Star](https://img.shields.io/github/stars/SAAgent/MCPWorld.svg?style=social&label=Star) [MCPWorld](https://arxiv.org/abs/2506.07672) (2025) [[code]](https://github.com/SAAgent/MCPWorld)
+ ![Star](https://img.shields.io/github/stars/KeLes-Coding/NatureGAIA.svg?style=social&label=Star) [NaturalGAIA](https://arxiv.org/abs/2508.01330) (2025) [[code]](https://github.com/KeLes-Coding/NatureGAIA)
+ [OSWorld-MCP](https://arxiv.org/abs/2510.24563) (2025) [[website]](https://osworld-mcp.github.io)
+ [GUI-360](https://arxiv.org/abs/2511.04307) (2025) [[data]](https://huggingface.co/datasets/vyokky/GUI-360)
+ [OpenComputer](https://arxiv.org/abs/2605.19769) (2026)
+ [CUA-Gym](https://arxiv.org/abs/2605.25624) (2026)
+ [MobileGym](https://arxiv.org/abs/2605.26114) (2026) [[website]](https://mobilegym.github.io)
+ [AndroidDaily](https://arxiv.org/abs/2605.27761) (2026)
+ ![Star](https://img.shields.io/github/stars/UniPat-AI/SaaS-Bench.svg?style=social&label=Star) [SaaS-Bench](https://arxiv.org/abs/2605.15777) (2026) [[code]](https://github.com/UniPat-AI/SaaS-Bench)
+ ![Star](https://img.shields.io/github/stars/ZZZhr-1/WinDeskGround.svg?style=social&label=Star) [WinDeskGround](https://arxiv.org/abs/2605.16402) (2026) [[code]](https://github.com/ZZZhr-1/WinDeskGround)
+ [AgentHijack](https://arxiv.org/abs/2605.25707) (ICML 2026) [[website]](https://AgentHijack.github.io)
+ ![Star](https://img.shields.io/github/stars/AlibabaResearch/RoTS.svg?style=social&label=Star) [GUI-RobustEval / RoTS](https://arxiv.org/abs/2605.29447) (ICML 2026) [[code]](https://github.com/AlibabaResearch/RoTS)
+ [WindowsWorld](https://arxiv.org/abs/2604.27776) (2026)
+ [CUA-Suite](https://arxiv.org/abs/2603.24440) (2026)
+ [A11y-CUA Dataset](https://arxiv.org/abs/2602.09310) (2026)
+ [OS-Marathon](https://arxiv.org/abs/2601.20650) (2026) [[website]](https://os-marathon.github.io/)
+ [WebTestBench](https://arxiv.org/abs/2603.25226) (2026) [[code]](https://github.com/friedrichor/WebTestBench)
+ [Odysseys](https://arxiv.org/abs/2604.24964) (2026) [[website]](https://odysseys-website.pages.dev)
+ [SecureWebArena](https://arxiv.org/abs/2510.10073) (2025)
+ [GUIDE-Bench](https://arxiv.org/abs/2603.25864) (2026) [[website]](https://guide-bench.github.io)
+ [OmniGUI](https://arxiv.org/abs/2605.18758) (2026) [[website]](https://omni-gui.github.io)
+ [Mobile-Env](https://arxiv.org/abs/2305.08144) (2023)
+ [WorkArena](https://arxiv.org/abs/2403.07718) (2024) [[code]](https://github.com/ServiceNow/WorkArena)
+ [WebCanvas](https://arxiv.org/abs/2406.12373) (2024)
+ [WorkArena++](https://arxiv.org/abs/2407.05291) (2024) [[code]](https://github.com/ServiceNow/WorkArena)
+ [Mobile-Bench](https://arxiv.org/abs/2407.00993) (2024)
+ [WebQuest](https://arxiv.org/abs/2409.13711) (2024)
+ [BrowserGym](https://arxiv.org/abs/2412.05467) (2024) [[code]](https://github.com/ServiceNow/BrowserGym)
+ [DroidCall](https://arxiv.org/abs/2412.00402) (2024) [[code]](https://github.com/UbiquitousLearning/DroidCall)
+ [MobileViews](https://arxiv.org/abs/2409.14337) (2024) [[data]](https://huggingface.co/datasets/mllmTeam/MobileViews)
+ [UI-Vision](https://arxiv.org/abs/2503.15661) (2025)
+ [Mobile-Bench-v2](https://arxiv.org/abs/2505.11891) (2025) [[data]](https://huggingface.co/datasets/xwk123/MobileBench-v2)
+ [MVISU-Bench](https://arxiv.org/abs/2508.09057) (ACM MM 2025)
+ [MAS-Bench](https://arxiv.org/abs/2509.06477) (2025) [[website]](https://pengxiang-zhao.github.io/MAS-Bench)
+ [ColorBench](https://arxiv.org/abs/2510.14621) (2025) [[code]](https://github.com/MadeAgents/ColorBench)
+ [MobiBench](https://arxiv.org/abs/2512.12634) (2025)
+ [MobileWorldBench](https://arxiv.org/abs/2512.14014) (2025) [[code]](https://github.com/jacklishufan/MobileWorld)
+ [MobileWorld](https://arxiv.org/abs/2512.19432) (2025)
+ [OpenApps](https://arxiv.org/abs/2511.20766) (2025) [[website]](https://facebookresearch.github.io/OpenApps/)
+ [DiffSpot](https://arxiv.org/abs/2605.29615) (2026)
+ [WebChain](https://arxiv.org/abs/2603.05295) (2026)
+ [WebSP-Eval](https://arxiv.org/abs/2604.06367) (2026)
+ [GameWorld](https://arxiv.org/abs/2604.07429) (2026) [[website]](https://gameworld-bench.github.io)
+ [HealthAdminBench](https://arxiv.org/abs/2604.09937) (2026)
+ [EntWorld](https://arxiv.org/abs/2601.17722) (2026)
+ [GUI-CEval](https://arxiv.org/abs/2603.15039) (2026)
+ [MemGUI-Bench](https://arxiv.org/abs/2602.06075) (2026) [[website]](https://lgy0404.github.io/MemGUI-Bench/)
+ [GUIGuard-Bench](https://arxiv.org/abs/2601.18842) (2026) [[website]](https://futuresis.github.io/GUIGuard-page/)
+ [KnowU-Bench](https://arxiv.org/abs/2604.08455) (2026)
+ [PhoneWorld](https://arxiv.org/abs/2605.29486) (2026)
+ [ProactiveMobile](https://arxiv.org/abs/2602.21858) (2026)
+ [AmbiBench](https://arxiv.org/abs/2602.11750) (2026)
+ [WebTestPilot](https://arxiv.org/abs/2602.11724) (2026)

## Training, Data Synthesis, and Reinforcement Learning

+ ![Star](https://img.shields.io/github/stars/OS-Copilot/OS-Genesis.svg?style=social&label=Star) [OS-Genesis: Automating GUI Agent Trajectory Construction via Reverse Task Synthesis](https://arxiv.org/abs/2412.19723) (2024) [[code]](https://github.com/OS-Copilot/OS-Genesis)
+ [AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials](https://arxiv.org/abs/2412.09605) (2024)
+ [AutoManual: Constructing Instruction Manuals by LLM Agents via Interactive Environmental Learning](https://arxiv.org/abs/2405.16247) (2024) [[code]](https://github.com/minghchen/automanual)
+ [On the Effects of Data Scale on UI Control Agents](https://arxiv.org/abs/2406.03679) (2024)
+ [Navigating WebAI: Training Agents to Complete Web Tasks with Large Language Models and Reinforcement Learning](https://arxiv.org/abs/2405.00516) (2024)
+ [WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning](https://arxiv.org/abs/2411.02337) (2024)
+ ![Star](https://img.shields.io/github/stars/TongUI-agent/TongUI-agent.svg?style=social&label=Star) [TongUI: Internet-Scale Trajectories from Multimodal Web Tutorials for Generalized GUI Agents](https://arxiv.org/abs/2504.12679) (AAAI 2026) [[code]](https://github.com/TongUI-agent/TongUI-agent)
+ [UI-E2I-Synth: Advancing GUI Grounding with Large-Scale Instruction Synthesis](https://arxiv.org/abs/2504.11257) (2025) [[project]](https://microsoft.github.io/FIVE-UI-Evol/)
+ ![Star](https://img.shields.io/github/stars/OpenGVLab/ZeroGUI.svg?style=social&label=Star) [ZeroGUI: Automating Online GUI Learning at Zero Human Cost](https://arxiv.org/abs/2505.23762) (2025) [[code]](https://github.com/OpenGVLab/ZeroGUI)
+ ![Star](https://img.shields.io/github/stars/dvlab-research/ARPO.svg?style=social&label=Star) [ARPO: End-to-End Policy Optimization for GUI Agents with Experience Replay](https://arxiv.org/abs/2505.16282) (2025) [[code]](https://github.com/dvlab-research/ARPO)
+ ![Star](https://img.shields.io/github/stars/KDEGroup/UI-AGILE.svg?style=social&label=Star) [UI-AGILE: Advancing GUI Agents with Effective Reinforcement Learning and Precise Inference-Time Grounding](https://arxiv.org/abs/2507.22025) (2025) [[code]](https://github.com/KDEGroup/UI-AGILE)
+ ![Star](https://img.shields.io/github/stars/X-PLUG/MobileAgent.svg?style=social&label=Star) [UI-S1: Advancing GUI Automation via Semi-online Reinforcement Learning](https://arxiv.org/abs/2509.11543) (2025) [[code]](https://github.com/X-PLUG/MobileAgent/tree/main/UI-S1)
+ ![Star](https://img.shields.io/github/stars/THUDM/MobileRL.svg?style=social&label=Star) [MobileRL: Online Agentic Reinforcement Learning for Mobile GUI Agents](https://arxiv.org/abs/2509.18119) (2025) [[code]](https://github.com/THUDM/MobileRL)
+ ![Star](https://img.shields.io/github/stars/THUDM/ComputerRL.svg?style=social&label=Star) [ComputerRL: Scaling End-to-End Online Reinforcement Learning for Computer Use Agents](https://arxiv.org/abs/2508.14040) (2025) [[code]](https://github.com/thudm/ComputerRL)
+ ![Star](https://img.shields.io/github/stars/OpenGVLab/ScaleCUA.svg?style=social&label=Star) [ScaleCUA: Scaling Open-Source Computer Use Agents with Cross-Platform Data](https://arxiv.org/abs/2509.15221) (2025) [[code]](https://github.com/OpenGVLab/ScaleCUA)
+ [Watch and Learn: Learning to Use Computers from Online Videos](https://arxiv.org/abs/2510.04673) (2025)
+ [VideoAgentTrek: Computer Use Pretraining from Unlabeled Videos](https://arxiv.org/abs/2510.19488) (2025)
+ [WebSTAR: Scalable Data Synthesis for Computer Use Agents with Step-Level Filtering](https://arxiv.org/abs/2512.10962) (2025)
+ ![Star](https://img.shields.io/github/stars/AlibabaResearch/RoTS.svg?style=social&label=Star) [Recovering Policy-Induced Errors: Benchmarking and Trajectory Synthesis for Robust GUI Agents](https://arxiv.org/abs/2605.29447) (ICML 2026) [[code]](https://github.com/AlibabaResearch/RoTS)
+ ![Star](https://img.shields.io/github/stars/Wuzheng02/GUI-CIDER.svg?style=social&label=Star) [GUI-CIDER: Mid-training GUI Agents via Causal Internalization and Density-aware Exemplar Reselection](https://arxiv.org/abs/2605.28534) (2026) [[code]](https://github.com/Wuzheng02/GUI-CIDER)
+ [Video2GUI: Synthesizing Large-Scale Interaction Trajectories for Generalized GUI Agent Pretraining](https://arxiv.org/abs/2605.14747) (ICML 2026)
+ [CUA-Gym: Scaling Verifiable Training Environments and Tasks for Computer-Use Agents](https://arxiv.org/abs/2605.25624) (2026)
+ [GUI-GENESIS: Automated Synthesis of Efficient Environments with Verifiable Rewards for GUI Agent Post-Training](https://arxiv.org/abs/2602.14093) (2026)
+ [AutoWebWorld: Synthesizing Infinite Verifiable Web Environments via Finite State Machines](https://arxiv.org/abs/2602.14296) (2026)
+ [PRO-CUA: Process-Reward Optimization for Computer Use Agents](https://arxiv.org/abs/2605.29119) (2026)
+ ![Star](https://img.shields.io/github/stars/UITron-hub/TreeCUA.svg?style=social&label=Star) [TreeCUA: Efficiently Scaling GUI Automation with Tree-Structured Verifiable Evolution](https://arxiv.org/abs/2602.09662) (2026) [[code]](https://github.com/UITron-hub/TreeCUA)
+ [CUA-Suite: Massive Human-annotated Video Demonstrations for Computer-Use Agents](https://arxiv.org/abs/2603.24440) (2026)
+ [VEM: Environment-Free Exploration for Training GUI Agent with Value Environment Model](https://arxiv.org/abs/2502.18906) (2025)
+ [MobileA3gent: Training Mobile GUI Agents Using Decentralized Self-Sourced Data from Diverse Users](https://arxiv.org/abs/2502.02982) (2025)
+ [Mobile-R1: Towards Interactive Capability for VLM-Based Mobile Agent via Systematic Training](https://arxiv.org/abs/2506.20332) (2025) [[project]](https://mobile-r1.github.io/Mobile-R1/)
+ [MobileGUI-RL: Advancing Mobile GUI Agent through Reinforcement Learning in Online Environment](https://arxiv.org/abs/2507.05720) (2025)
+ [InquireMobile: Teaching VLM-based Mobile Agent to Request Human Assistance via Reinforcement Fine-Tuning](https://arxiv.org/abs/2508.19679) (2025)
+ [OpenMobile: Building Open Mobile Agents with Task and Trajectory Synthesis](https://arxiv.org/abs/2604.15093) (2026) [[project]](https://njucckevin.github.io/openmobile/)
+ [ANCHOR: Branch-Point Data Generation for GUI Agents](https://arxiv.org/abs/2602.07153) (2026)
+ [HATS: Hardness-Aware Trajectory Synthesis for GUI Agents](https://arxiv.org/abs/2603.12138) (2026)
+ [M2-Miner: Multi-Agent Enhanced MCTS for Mobile GUI Agent Data Mining](https://arxiv.org/abs/2602.05429) (2026)
+ [UI-Mem: Self-Evolving Experience Memory for Online Reinforcement Learning in Mobile GUI Agents](https://arxiv.org/abs/2602.05832) (2026) [[project]](https://ui-mem.github.io)
+ [Learning with Challenges: Adaptive Difficulty-Aware Data Generation for Mobile GUI Agent Training](https://arxiv.org/abs/2601.22781) (2026)
+ [Agentic Reward Modeling: Verifying GUI Agent via Online Proactive Interaction](https://arxiv.org/abs/2602.00575) (2026)
+ [Video-Based Reward Modeling for Computer-Use Agents](https://arxiv.org/abs/2603.10178) (2026)
+ [OS-Themis: A Scalable Critic Framework for Generalist GUI Rewards](https://arxiv.org/abs/2603.19191) (2026)
+ [Step-level Optimization for Efficient Computer-use Agents](https://arxiv.org/abs/2604.27151) (2026)
+ [EE-MCP: Self-Evolving MCP-GUI Agents via Automated Environment Generation and Experience Learning](https://arxiv.org/abs/2604.09815) (2026)
+ [Covering Human Action Space for Computer Use: Data Synthesis and Benchmark](https://arxiv.org/abs/2605.12501) (2026) [[code]](https://github.com/microsoft/Phi-Ground)

## Safety, Robustness, and Security

+ [MobileSafetyBench: Evaluating Safety of Autonomous Agents in Mobile Device Control](https://arxiv.org/abs/2410.17520) (2024) [[code]](https://github.com/jylee425/mobilesafetybench)
+ [From Interaction to Impact: Towards Safer AI Agents Through Understanding and Evaluating Mobile UI Operation Impacts](https://arxiv.org/abs/2410.09006) (2024)
+ [AdvAgent: Controllable Blackbox Red-teaming on Web Agents](https://arxiv.org/abs/2410.17401) (ICML 2025)
+ [EIA: Environmental Injection Attack on Generalist Web Agents for Privacy Leakage](https://arxiv.org/abs/2409.11295) (ICLR 2025)
+ [Attacking Vision-Language Computer Agents via Pop-ups](https://arxiv.org/abs/2411.02391) (2024)
+ [EVA: Red-Teaming GUI Agents via Evolving Indirect Prompt Injection](https://arxiv.org/abs/2505.14289) (2025)
+ [Caution for the Environment: Multimodal Agents are Susceptible to Environmental Distractions](https://arxiv.org/abs/2408.02544) (2024)
+ [DistRL: An Asynchronous Distributed Reinforcement Learning Framework for On-Device Control Agents](https://arxiv.org/abs/2410.14803) (2024)
+ [The Obvious Invisible Threat: LLM-Powered GUI Agents' Vulnerability to Fine-Print Injections](https://arxiv.org/abs/2504.11281) (2025)
+ [Mobile GUI Agents under Real-world Threats: Are We There Yet?](https://arxiv.org/abs/2507.04227) (2025) [[website]](https://agenthazard.github.io)
+ [Dark Patterns Meet GUI Agents: LLM Agent Susceptibility to Manipulative Interfaces and the Role of Human Oversight](https://arxiv.org/abs/2509.10723) (2025)
+ [Environmental Injection Attacks against GUI Agents in Realistic Dynamic Environments](https://arxiv.org/abs/2509.11250) (2025)
+ [SecureWebArena: A Holistic Security Evaluation Benchmark for LVLM-based Web Agents](https://arxiv.org/abs/2510.10073) (2025)
+ ![Star](https://img.shields.io/github/stars/OS-Copilot/OS-Sentinel.svg?style=social&label=Star) [OS-Sentinel: Towards Safety-Enhanced Mobile GUI Agents via Hybrid Validation in Realistic Workflows](https://arxiv.org/abs/2510.24411) (2025) [[code]](https://github.com/OS-Copilot/OS-Sentinel)
+ [Just Do It!? Computer-Use Agents Exhibit Blind Goal-Directedness](https://arxiv.org/abs/2510.01670) (2025)
+ [Measuring Harmfulness of Computer-Using Agents](https://arxiv.org/abs/2508.00935) (2025)
+ [A Systematization of Security Vulnerabilities in Computer Use Agents](https://arxiv.org/abs/2507.05445) (2025)
+ [AgentHijack: Benchmarking Computer Use Agent Robustness to Common Environment Corruptions](https://arxiv.org/abs/2605.25707) (ICML 2026) [[website]](https://AgentHijack.github.io)
+ ![Star](https://img.shields.io/github/stars/Theodora-Y/MaskClaw.svg?style=social&label=Star) [MaskClaw: Edge-Side Personalized Privacy Arbitration for GUI Agents with Behavior-Driven Skill Evolution](https://arxiv.org/abs/2605.28646) (2026) [[code]](https://github.com/Theodora-Y/MaskClaw)
+ [MIRAGE: Context-Aware Prompt Injection against Mobile GUI Agents via User-Generated Content](https://arxiv.org/abs/2605.28116) (2026)
+ [WARD: Adversarially Robust Defense of Web Agents Against Prompt Injections](https://arxiv.org/abs/2605.15030) (2026)
+ [SafeGround: Know When to Trust GUI Grounding Models via Uncertainty Calibration](https://arxiv.org/abs/2602.02419) (2026)
+ [LPS-Bench: Benchmarking Safety Awareness of Computer-Use Agents in Long-Horizon Planning under Benign and Adversarial Scenarios](https://arxiv.org/abs/2602.03255) (2026) [[code]](https://github.com/tychenn/LPS-Bench)
+ [Temporal UI State Inconsistency in Desktop GUI Agents: Formalizing and Defending Against TOCTOU Attacks on Computer-Use Agents](https://arxiv.org/abs/2604.18860) (2026)
+ [CaMeLs Can Use Computers Too: System-level Security for Computer Use Agents](https://arxiv.org/abs/2601.09923) (2026)
+ [AgentHazard: A Benchmark for Evaluating Harmful Behavior in Computer-Use Agents](https://arxiv.org/abs/2604.02947) (2026)
+ [VeriSafe Agent: Safeguarding Mobile GUI Agent via Logic-based Action Verification](https://arxiv.org/abs/2503.18492) (2025)
+ [WASP: Benchmarking Web Agent Security Against Prompt Injection Attacks](https://arxiv.org/abs/2504.18575) (2025)
+ [AdInject: Real-World Black-Box Attacks on Web Agents via Advertising Delivery](https://arxiv.org/abs/2505.21499) (2025) [[code]](https://github.com/NicerWang/AdInject)
+ [Manipulating LLM Web Agents with Indirect Prompt Injection Attack via HTML Accessibility Tree](https://arxiv.org/abs/2507.14799) (2025) [[code]](https://github.com/sej2020/manipulating-web-agents)
+ [HarmonyGuard: Toward Safety and Utility in Web Agents via Adaptive Policy Enhancement and Dual-Objective Optimization](https://arxiv.org/abs/2508.04010) (2025) [[code]](https://github.com/YurunChen/HarmonyGuard)
+ [WAInjectBench: Benchmarking Prompt Injection Detections for Web Agents](https://arxiv.org/abs/2510.01354) (2025) [[code]](https://github.com/Norrrrrrr-lyn/WAInjectBench)
+ [BrowseSafe: Understanding and Preventing Prompt Injection Within AI Browser Agents](https://arxiv.org/abs/2511.20597) (2025)
+ [DECEPTICON: How Dark Patterns Manipulate Web Agents](https://arxiv.org/abs/2512.22894) (2025)
+ [MirrorGuard: Toward Secure Computer-Use Agents via Simulation-to-Real Reasoning Correction](https://arxiv.org/abs/2601.12822) (2026) [[website]](https://bmz-q-q.github.io/MirrorGuard/)
+ [SafePred: A Predictive Guardrail for Computer-Using Agents via World Models](https://arxiv.org/abs/2602.01725) (2026)
+ [When Actions Go Off-Task: Detecting and Correcting Misaligned Actions in Computer-Use Agents](https://arxiv.org/abs/2602.08995) (2026)
+ [When Benign Inputs Lead to Severe Harms: Eliciting Unsafe Unintended Behaviors of Computer-Use Agents](https://arxiv.org/abs/2602.08235) (2026)
+ [WebSentinel: Detecting and Localizing Prompt Injection Attacks for Web Agents](https://arxiv.org/abs/2602.03792) (2026) [[code]](https://github.com/wxl-lxw/WebSentinel)
+ [WebTrap Park: An Automated Platform for Systematic Security Evaluation of Web Agents](https://arxiv.org/abs/2601.08406) (2026) [[project]](https://security.fudan.edu.cn/webagent)
+ [MalURLBench: A Benchmark Evaluating Agents' Vulnerabilities When Processing Web URLs](https://arxiv.org/abs/2601.18113) (2026) [[code]](https://github.com/JiangYingEr/MalURLBench)
+ [MUZZLE: Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection Attacks](https://arxiv.org/abs/2602.09222) (2026)
+ [Visual Confused Deputy: Exploiting and Defending Perception Failures in Computer-Using Agents](https://arxiv.org/abs/2603.14707) (2026)
+ [WebPII: Benchmarking Visual PII Detection for Computer-Use Agents](https://arxiv.org/abs/2603.17357) (2026)
+ [SnapGuard: Lightweight Prompt Injection Detection for Screenshot-Based Web Agents](https://arxiv.org/abs/2604.25562) (2026)
+ [WebAgentGuard: A Reasoning-Driven Guard Model for Detecting Prompt Injection Attacks in Web Agents](https://arxiv.org/abs/2604.12284) (2026)
+ [Don't Click That: Teaching Web Agents to Resist Deceptive Interfaces](https://arxiv.org/abs/2605.09497) (2026)
+ [ProjGuard: Safety Monitoring for Computer-Use Agents via Low-Dimensional Projections](https://arxiv.org/abs/2605.13631) (2026)
+ [Constraining Host-Level Abuse in Self-Hosted Computer-Use Agents via TEE-Backed Isolation](https://arxiv.org/abs/2605.06393) (2026)
+ [Securing Computer-Use Agents: A Unified Architecture-Lifecycle Framework for Deployment-Grounded Reliability](https://arxiv.org/abs/2605.07110) (2026)

---

## Open-Source Projects / Tools

> Non-paper resources for building, evaluating, or deploying GUI agents. General automation tools are included only when they are commonly used in GUI-agent pipelines.

|  Project  | Platform |   Type   |   Link   |
|:----------|:--------:|:--------:|:--------:|
| ![Star](https://img.shields.io/github/stars/microsoft/playwright.svg?style=social&label=Star) [**Playwright**](https://github.com/microsoft/playwright) | Web | Browser automation | [Github](https://github.com/microsoft/playwright) |
| ![Star](https://img.shields.io/github/stars/appium/appium.svg?style=social&label=Star) [**Appium**](https://github.com/appium/appium) | Mobile | Mobile automation | [Github](https://github.com/appium/appium) |
| ![Star](https://img.shields.io/github/stars/OpenInterpreter/open-interpreter.svg?style=social&label=Star) [**Open Interpreter**](https://github.com/OpenInterpreter/open-interpreter) | Desktop / OS | Computer-use agent | [Github](https://github.com/OpenInterpreter/open-interpreter) |
| ![Star](https://img.shields.io/github/stars/showlab/computer_use_ootb.svg?style=social&label=Star) [**Computer Use OOTB**](https://github.com/showlab/computer_use_ootb) | Desktop | GUI-agent framework | [Github](https://github.com/showlab/computer_use_ootb) |
| ![Star](https://img.shields.io/github/stars/lavague-ai/LaVague.svg?style=social&label=Star) [**LaVague**](https://github.com/lavague-ai/LaVague) | Web | Web-agent framework | [Github](https://github.com/lavague-ai/LaVague) |
| ![Star](https://img.shields.io/github/stars/OpenAdaptAI/OpenAdapt.svg?style=social&label=Star) [**OpenAdapt**](https://github.com/OpenAdaptAI/OpenAdapt) | Desktop | Process automation | [Github](https://github.com/OpenAdaptAI/OpenAdapt) |
| ![Star](https://img.shields.io/github/stars/ddupont808/WebMarker.svg?style=social&label=Star) [**WebMarker**](https://github.com/ddupont808/WebMarker) | Web | Web annotation | [Github](https://github.com/ddupont808/WebMarker) |
| ![Star](https://img.shields.io/github/stars/browser-use/browser-use.svg?style=social&label=Star) [**browser-use**](https://github.com/browser-use/browser-use) | Web | Browser-use agent framework | [Github](https://github.com/browser-use/browser-use) |
| ![Star](https://img.shields.io/github/stars/browserbase/stagehand.svg?style=social&label=Star) [**Stagehand**](https://github.com/browserbase/stagehand) | Web | AI browser automation SDK | [Github](https://github.com/browserbase/stagehand) |
| ![Star](https://img.shields.io/github/stars/Skyvern-AI/skyvern.svg?style=social&label=Star) [**Skyvern**](https://github.com/Skyvern-AI/skyvern) | Web | Browser workflow automation | [Github](https://github.com/Skyvern-AI/skyvern) |
| ![Star](https://img.shields.io/github/stars/ServiceNow/BrowserGym.svg?style=social&label=Star) [**BrowserGym**](https://github.com/ServiceNow/BrowserGym) | Web | Web-agent environments | [Github](https://github.com/ServiceNow/BrowserGym) |
| ![Star](https://img.shields.io/github/stars/ServiceNow/AgentLab.svg?style=social&label=Star) [**AgentLab**](https://github.com/ServiceNow/AgentLab) | Web | Web-agent experimentation framework | [Github](https://github.com/ServiceNow/AgentLab) |
| ![Star](https://img.shields.io/github/stars/microsoft/magentic-ui.svg?style=social&label=Star) [**Magentic-UI**](https://github.com/microsoft/magentic-ui) | Cross-platform | Human-in-the-loop agentic UI | [Github](https://github.com/microsoft/magentic-ui) |
| ![Star](https://img.shields.io/github/stars/microsoft/OmniParser.svg?style=social&label=Star) [**OmniParser**](https://github.com/microsoft/OmniParser) | Cross-platform | Screen parsing for GUI agents | [Github](https://github.com/microsoft/OmniParser) |
| ![Star](https://img.shields.io/github/stars/xlang-ai/OpenCUA.svg?style=social&label=Star) [**OpenCUA**](https://github.com/xlang-ai/OpenCUA) | Desktop / Web | Open computer-use agent foundation | [Github](https://github.com/xlang-ai/OpenCUA) |
| ![Star](https://img.shields.io/github/stars/inclusionAI/UI-Venus.svg?style=social&label=Star) [**UI-Venus**](https://github.com/inclusionAI/UI-Venus) | Cross-platform | GUI-agent model suite | [Github](https://github.com/inclusionAI/UI-Venus) |
| ![Star](https://img.shields.io/github/stars/bytedance/UI-TARS.svg?style=social&label=Star) [**UI-TARS Desktop**](https://github.com/bytedance/UI-TARS) | Desktop / OS | GUI-agent model and desktop demos | [Github](https://github.com/bytedance/UI-TARS) |
| ![Star](https://img.shields.io/github/stars/microsoft/Phi-Ground.svg?style=social&label=Star) [**Phi-Ground**](https://github.com/microsoft/Phi-Ground) | Cross-platform | GUI grounding toolkit | [Github](https://github.com/microsoft/Phi-Ground) |
| ![Star](https://img.shields.io/github/stars/AlibabaResearch/RoTS.svg?style=social&label=Star) [**RoTS**](https://github.com/AlibabaResearch/RoTS) | Cross-platform | Robust GUI-agent training / evaluation | [Github](https://github.com/AlibabaResearch/RoTS) |
| [**PyAutoGUI**](https://pyautogui.readthedocs.io/) | Desktop | Automation library | [Website](https://pyautogui.readthedocs.io/) |
| [**Selenium**](https://www.selenium.dev/) | Web | Browser automation | [Website](https://www.selenium.dev/) |
| [**nut.js**](https://nutjs.dev/) | Desktop | Desktop automation | [Website](https://nutjs.dev/) |

---

## Related Repositories

+ ![Star](https://img.shields.io/github/stars/showlab/Awesome-GUI-Agent.svg?style=social&label=Star) [showlab/Awesome-GUI-Agent](https://github.com/showlab/Awesome-GUI-Agent)
+ ![Star](https://img.shields.io/github/stars/e2b-dev/awesome-ai-agents.svg?style=social&label=Star) [e2b-dev/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents)
+ ![Star](https://img.shields.io/github/stars/kaushikb11/awesome-llm-agents.svg?style=social&label=Star) [kaushikb11/awesome-llm-agents](https://github.com/kaushikb11/awesome-llm-agents)
+ ![Star](https://img.shields.io/github/stars/ysymyth/awesome-language-agents.svg?style=social&label=Star) [ysymyth/awesome-language-agents](https://github.com/ysymyth/awesome-language-agents)
+ ![Star](https://img.shields.io/github/stars/PhoneLLM/Awesome-LLM-Powered-Phone-GUI-Agents.svg?style=social&label=Star) [PhoneLLM/Awesome-LLM-Powered-Phone-GUI-Agents](https://github.com/PhoneLLM/Awesome-LLM-Powered-Phone-GUI-Agents)
+ ![Star](https://img.shields.io/github/stars/OS-Agent-Survey/OS-Agent-Survey.svg?style=social&label=Star) [OS-Agent-Survey/OS-Agent-Survey](https://github.com/OS-Agent-Survey/OS-Agent-Survey)

---

## Contributing

Contributions are welcome!

Please use the following format when adding a paper or resource:

```markdown
- [Paper Title](paper_link) (Venue / Year) [[code](code_link)]
  - **Scope:** `Core Paper` / `Related Background` / `Dataset` / `Benchmark` / `Tool`
  - **Tags:** `GUI Grounding` `Web Agent` `Mobile Agent`
  - **Why awesome:** One-sentence summary of the key contribution.
```

Recommended tags:

```text
Core Paper · Related Background · GUI Grounding · Screen Understanding · Web Agent · Mobile Agent · Desktop Agent · Computer Use · Vision-Language-Action · Benchmark · Dataset · Safety · Tool
```

Before submitting a pull request, please check:

- The paper / project is related to multimodal GUI agents.
- The scope label is clear: core paper, related background, dataset, benchmark, or tool.
- Venue labels are conservative; use `arXiv` or `Tech Report` unless the conference acceptance is explicitly confirmed.
- The link is valid.
- Duplicate entries are avoided.
- A short description or tag is provided.

---

## Citation

If you find this repository useful, please consider starring this repository and citing the related papers listed above.

```bibtex
@misc{awesome_multimodal_gui_agents,
  title        = {Awesome Multimodal GUI Agents},
  author       = {DeLunnLi},
  year         = {2026},
  howpublished = {\url{https://github.com/DeLunnLi/Awesome-Multimodal-GUI-Agents}}
}
```
