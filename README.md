# Awesome Agentic Environments [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<p align="left">
  <img src="https://img.shields.io/badge/survey-coming_soon-lightgrey" alt="Survey: coming soon">
  <a href="https://github.com/TraceLite-AI/Awesome-Agentic-Environments/stargazers"><img src="https://img.shields.io/github/stars/TraceLite-AI/Awesome-Agentic-Environments?style=social" alt="GitHub stars"></a>
  <a href="https://github.com/TraceLite-AI/Awesome-Agentic-Environments/commits/main"><img src="https://img.shields.io/github/last-commit/TraceLite-AI/Awesome-Agentic-Environments" alt="Last commit"></a>
  <a href="https://github.com/TraceLite-AI/Awesome-Agentic-Environments/pulls"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen" alt="PRs welcome"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache--2.0-blue" alt="License: Apache-2.0"></a>
</p>

A curated list of work on the **environments** that LLM agents are trained and evaluated in — organized by what an environment is made of, what changes when an environment changes, and how to report it.

This repository accompanies the survey ***Environments for LLM Agents: A Survey of Design, Effects, and Evidence*** (in preparation).

## 🔥 News

- **[2026-10]** Repository restructured around the six-component framework (Runtime → Interface → State → Dynamics → Task → Verification). Entries are being migrated into the new tables.

## Overview

**What we mean by an environment.** Relative to the agent under study, an environment is the external interactive system that hosts a task, together with its task and evaluation conventions. It fixes what goal and external state the agent faces, what it can observe and do, how the world changes in response to actions and events, how the interaction is executed, and how the result is judged.

**Admission test.** A component belongs to the environment if changing it changes what the agent can observe, what actions are available, or how the agent is scored. Anything that can be swapped without rebuilding the environment — prompts, tool selection, context management, orchestration, step or token budgets — belongs to the **harness**. The trainer, which only consumes trajectories and evaluation signals, is outside the environment as well. The environment decides which channels are *offered*; the harness decides which channel is *used*.

<p align="center">
  <img src="assets/figures/framework.svg" width="90%" alt="Six components of an environment for LLM agents">
</p>

| # | Component | Question it answers | Example sub-dimensions |
|---|---|---|---|
| 1 | [Runtime](#1-runtime) | Where does the interaction execute? | isolation backend, lifecycle (reset / snapshot / fork), OS and software stack, network and permissions, concurrency |
| 2 | [Interface](#2-interface) | What can the agent observe and do? | observation channels, action space and granularity, return formats and error semantics, protocols |
| 3 | [State](#3-state) | What does the world hold? | initial state and its distribution, residue and contamination, external data snapshots, persistence scope |
| 4 | [Dynamics](#4-dynamics) | How does the world change, and who else acts? | transition rules, stochasticity, time and async events, external service behavior; users, partners, opponents |
| 5 | [Task](#5-task) | What is the agent asked to achieve? | goal and constraints, structure and horizon, task source (real / programmatic / model-generated), difficulty |
| 6 | [Verification](#6-verification) | What counts as success? | judged object (output / final state / trajectory), verifier form, signal type, reliability checks, exploit resistance |

**How to read this list.**

- *Looking for designs and implementations?* Start from [Part I](#-part-i--papers-by-component), organized by component, and the [benchmark tables](#-benchmarks-and-trainable-environments) organized by domain.
- *Want to know which environment differences actually change results?* Go to [Part II](#-part-ii--what-environment-differences-change).
- *Building or reporting an environment?* Use the declaration template and comparison protocol in [Part III](#-part-iii--environment-declaration-and-comparison-protocol).

## Contents

- [Part I · Papers by Component](#-part-i--papers-by-component)
  - [1 Runtime](#1-runtime) · [2 Interface](#2-interface) · [3 State](#3-state) · [4 Dynamics](#4-dynamics) · [5 Task](#5-task) · [6 Verification](#6-verification) · [7 Lifecycle](#7-lifecycle-synthesis-evolution-and-delivery)
- [Environment Recipes in Foundation-Model Reports](#-environment-recipes-in-foundation-model-reports)
- [Benchmarks and Trainable Environments](#-benchmarks-and-trainable-environments)
- [Part II · What Environment Differences Change](#-part-ii--what-environment-differences-change)
- [Part III · Environment Declaration and Comparison Protocol](#-part-iii--environment-declaration-and-comparison-protocol)
- [Infrastructure and Tools](#-infrastructure-and-tools)
- [Related Surveys and Resources](#-related-surveys-and-resources)
- [Contributing](#-contributing) · [Citation](#-citation)

---

## 📜 Part I · Papers by Component

Each row states what the work contributes **to that component**. The same work can appear under several components with different contributions. Domain tags: `code` `web` `gui` `tool` `game` `science` `embodied` `multi-agent`.

### 1 Runtime

The execution infrastructure that hosts the environment: isolation, resources, and lifecycle management.
*Sub-dimensions:* execution backend and isolation · lifecycle (create / reset / snapshot / restore / fork) · platform and software configuration · execution boundary (network, identity, permissions) · concurrency and service quality · image building and maintenance.

| Paper | Date | Venue | Contribution in this component | Domain | Links |
|---|---|---|---|---|---|
| [DeepSeek Elastic Compute (DSec): A Sandbox Infrastructure for Effective Agentic Training at Scale](https://arxiv.org/abs/2609.22978) | 2026.09 | arXiv | One SDK over four execution backends (FnCall, container, Firecracker microVM, full VM); environments composed from independently versioned base-image, workspace and toolkit layers; one ~160-node production unit serves ~3M sandboxes/day, >380K concurrent, >5,000 creations/s | `code` `gui` | [paper](https://arxiv.org/abs/2609.22978) |

### 2 Interface

The observation and action contract the environment offers, and the protocols that expose it.
*Sub-dimensions:* observation space and visibility · action space and granularity · interaction contract (arguments, return formats, error semantics, sync / async) · display and input configuration · protocols and adapters.

| Paper | Date | Venue | Contribution in this component | Domain | Links |
|---|---|---|---|---|---|
| [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://arxiv.org/abs/2404.07972) | 2024.04 | NeurIPS 2024 D&B | Same tasks offered through four observation settings — screenshot, accessibility tree, screenshot + accessibility tree, Set-of-Mark — with mouse/keyboard actions on a real desktop | `gui` | [paper](https://arxiv.org/abs/2404.07972) · [project](https://os-world.github.io) |

### 3 State

The external state the agent acts on: entities, attributes and their current values.
*Sub-dimensions:* state objects and representation · true state vs. observable projection · initial state and its distribution · residue and contamination · external data and snapshots · persistence scope (across calls, episodes, sessions).

| Paper | Date | Venue | Contribution in this component | Domain | Links |
|---|---|---|---|---|---|
| [OSWorld](https://arxiv.org/abs/2404.07972) | 2024.04 | NeurIPS 2024 D&B | Each task carries an initial-state setup configuration that simulates work in progress (files, open applications) on top of a VM snapshot | `gui` | [paper](https://arxiv.org/abs/2404.07972) · [project](https://os-world.github.io) |

### 4 Dynamics

How the environment's state changes in response to actions, time, external events, and other actors.
*Sub-dimensions:* transition rules and side effects · determinism and stochasticity · time and concurrency · external service behavior · **actors**: users, partners, opponents, humans in the loop · implementation (real system, programmatic simulation, learned world model, hybrid).

#### Passive dynamics

_Entries being migrated._

#### Actors

| Paper | Date | Venue | Contribution in this component | Domain | Links |
|---|---|---|---|---|---|
| [τ²-Bench: Evaluating Conversational Agents in a Dual-Control Environment](https://arxiv.org/abs/2506.07982) | 2025.06 | arXiv | Dual-control telecom domain modeled as a Dec-POMDP: both agent and simulated user act on a shared world through tools; the user simulator's behavior is constrained by tools and observable state | `tool` | [paper](https://arxiv.org/abs/2506.07982) · [code](https://github.com/sierra-research/tau2-bench) |

### 5 Task

What the agent is asked to achieve, and where tasks come from.
*Sub-dimensions:* goal, inputs and constraints · structure, dependencies and horizon · task distribution and difficulty · task source (real / programmatic / model-generated) · quality control (solvability, contamination, coverage).

| Paper | Date | Venue | Contribution in this component | Domain | Links |
|---|---|---|---|---|---|
| [GLM-5: from Vibe Coding to Agentic Engineering](https://arxiv.org/abs/2602.15763) | 2026.02 | arXiv | Terminal tasks synthesized from seed tasks and from code-relevant web pages; a construction agent instantiates drafts in Harbor format and a refine agent iterates against rubrics (§4.2.2) | `code` | [paper](https://arxiv.org/abs/2602.15763) · [code](https://github.com/zai-org/GLM-5) |

### 6 Verification

How outcomes are judged and turned into evaluation signals.
*Sub-dimensions:* judged object and timing · verifier form (tests, rules, rubrics, state checks, model judges, humans) · signal form and use · reliability checks (reference solution, no-op, hidden tests, false positives / negatives) · exploit resistance and audit.

| Paper | Date | Venue | Contribution in this component | Domain | Links |
|---|---|---|---|---|---|
| [GLM-5](https://arxiv.org/abs/2602.15763) | 2026.02 | arXiv | Fail-to-pass and pass-to-pass tests extracted from real issue–PR pairs via LLM-generated, language-aware log parsers; terminal tasks refined so tests stay consistent with specifications and robust to shortcuts (§4.2.1–4.2.2) | `code` | [paper](https://arxiv.org/abs/2602.15763) · [code](https://github.com/zai-org/GLM-5) |

### 7 Lifecycle: synthesis, evolution, and delivery

Cross-component work on building, checking, evolving and shipping environments: joint synthesis of tasks, states and verifiers; difficulty- or weakness-driven evolution; packaging, versioning and hubs.

_Entries being migrated._

---

## 🏭 Environment Recipes in Foundation-Model Reports

What technical reports disclose about their training environments. Scale is quoted as reported, **with its unit** — environments, tasks, images, concurrent sandboxes and cumulative sandboxes are not comparable to one another.

| Model / Report | Org | Date | Disclosed scale (unit) | Environment types and key practices | Source |
|---|---|---|---|---|---|
| [GLM-5](https://arxiv.org/abs/2602.15763) | Zhipu AI | 2026.02 | >10K verifiable SWE environments (thousands of repos, 9 languages) · thousands of terminal environments (Docker build accuracy >90%) · >2M web pages (search corpus) | SWE environments built from real issue–PR pairs with a RepoLaunch-based setup pipeline; terminal tasks synthesized in Harbor format; multi-hop search QA from a web knowledge graph; slide-generation environment with rendering-based verification | §4.2 |

---

## 📊 Benchmarks and Trainable Environments

Grouped by domain. *Trainable* means the work exposes an interface for interactive learning (e.g. reset / step), not only offline scoring.

### Code and software engineering
_Entries being migrated._

### Web and search
_Entries being migrated._

### GUI and computer use

| Benchmark | Date | Venue | Runtime | Interface | Verification | Trainable | Links |
|---|---|---|---|---|---|---|---|
| [OSWorld](https://arxiv.org/abs/2404.07972) | 2024.04 | NeurIPS 2024 D&B | Real VMs (Ubuntu, Windows, macOS) with snapshot reset; 369 tasks + 43 Windows tasks for analysis | screenshot / accessibility tree / Set-of-Mark; mouse and keyboard | execution-based scripts per task (134 evaluation functions) | yes | [paper](https://arxiv.org/abs/2404.07972) · [project](https://os-world.github.io) |

### Tools, APIs and simulated users

| Benchmark | Date | Venue | Runtime | Interface | Verification | Trainable | Links |
|---|---|---|---|---|---|---|---|
| [τ²-Bench](https://arxiv.org/abs/2506.07982) | 2025.06 | arXiv | simulated domains with databases and tools (airline, retail, telecom) | tool calls for both agent and user; conversation | programmatically generated verifiable tasks; pass^k | — | [paper](https://arxiv.org/abs/2506.07982) · [code](https://github.com/sierra-research/tau2-bench) |

### Games and puzzles
_Entries being migrated._

### Science and ML research
_Entries being migrated._

### Embodied and world models
_Entries being migrated._

### Multi-agent and social
_Entries being migrated._

---

## 🧪 Part II · What Environment Differences Change

Findings where an environment condition was changed and an outcome was measured. Each row records **which component changed**, **which outcome it affected**, and the **finding as reported**. Outcomes: feasible strategies · difficulty and cost · verification result · capability attribution · learning and transfer.

Evidence types: **controlled** (same tasks, one condition varied) · **observational** (conditions differ but were not manipulated) · **adjacent-field** (non-agent evidence, e.g. software engineering) · **claim-only** (stated without a measured comparison). A design that merely *supports* a condition is not listed here.

| Changed condition | Component | Outcome | Finding (as reported) | Evidence | Source |
|---|---|---|---|---|---|
| Ubuntu → Windows, 43 adapted tasks, GPT-4V screenshot-only | Runtime · OS | difficulty | Success rate 4.88% → 2.55%; per-task correlation 0.7, which the authors read as good transfer across OSes | controlled (adapted tasks, one model) | [OSWorld](https://arxiv.org/abs/2404.07972) §5.3 |
| No-user → dual-control (telecom domain) | Dynamics · actors | difficulty | pass^1 drops by 18% (gpt-4.1) and 25% (o4-mini) when the agent must guide a user instead of acting alone | controlled ablation | [τ²-Bench](https://arxiv.org/abs/2506.07982) |

Sub-dimensions with no controlled evidence found so far will be listed explicitly rather than omitted.

---

## 📐 Part III · Environment Declaration and Comparison Protocol

Coverage and disclosure findings from the survey's coding study will be added here when the analysis is complete. Until then, this section provides the two artifacts readers can already use.

<details>
<summary><b>Environment declaration template</b> (six components)</summary>

Fill one declaration per environment version and configuration. Every value needs a source (paper section, or code path and commit). Use `unspecified` when the material does not say, and `n/a` only when the field has no meaning for the object; absence in code is `unspecified`, not `none`. Record the model, harness and budget separately — they are not part of the environment.

```yaml
object:            # environment family / version / configuration
sources:           # papers, code (commit), docs consulted
filled_by:         # authors or third party

runtime:
  backend:         # function call / process / container / microVM / full VM / emulator
  lifecycle:       # reset, snapshot, restore, fork; stateless / ephemeral / persistent
  platform:        # arch, OS and version, file-system semantics
  software:        # language runtimes, dependencies, shell, image digest or tag
  context:         # encoding, locale, time zone, clock, run-as identity
  boundary:        # network policy, permissions, mounts, devices, resource quotas
interface:
  observations:    # channels offered (terminal, screenshot, a11y tree, DOM, API returns)
  actions:         # action space and granularity
  contract:        # return formats, error semantics, sync / async
  display_input:   # resolution, scaling, UI language, input method
state:
  initial:         # initial state and how it is sampled
  residue:         # leftover files, processes, caches across tasks
  external_data:   # data versions and snapshots
  persistence:     # across calls / episodes / sessions
dynamics:
  transitions:     # rules, side effects, reversibility
  randomness:      # controlled seeds vs uncontrolled sources
  time_events:     # time advance, async events
  services:        # external services: frozen / live / simulated
  actors:          # users and other agents: none / simulated (persona) / human
task:
  goal:            # goal, constraints, termination
  source:          # real / programmatic / model-generated
  distribution:    # domains, difficulty, horizon
verification:
  form:            # tests / rules / rubric / state check / model judge / human
  signal:          # binary / scalar / multi-dimensional; visibility to the agent
  checks:          # reference solution, no-op, hidden tests, audit

agent_side:        # recorded separately: model, harness, budget
repeat_policy:     # number of runs per configuration
```

</details>

<details>
<summary><b>Comparison protocol</b> (default procedure and when to deviate)</summary>

1. **Pin everything else.** Hold all other components at a declared configuration (image digest, data snapshot, verifier version).
2. **Measure the noise floor.** Repeat runs within one configuration before attributing any difference to an environment change.
3. **Screen main effects.** Change one condition at a time from the base configuration (star / Morris-style screening).
4. **Explore combinations.** Use a constrained 2-way covering array over feasible configurations to surface pairwise failures; covering arrays find combinations but do not by themselves estimate interaction effects.
5. **Report per condition.** Success rate, effect size, outcome flips, time and cost, failure signatures and uncertainty — per condition, not as a single aggregate score.

Deviate when conditions are numeric (use sensitivity analysis), when interactions must be estimated (use a factorial design with stated identifiability assumptions), or when the budget allows only a tiered subset.

</details>

### Case studies
_To be added: cross-platform attribution, verifier audits, and run-to-run variation._

---

## 💻 Infrastructure and Tools

| Name | Org | Type | What it provides | Links |
|---|---|---|---|---|
| DSec | DeepSeek | sandbox platform | Unified SDK over FnCall / container / microVM / full-VM backends with layered, independently versioned environment images | [paper](https://arxiv.org/abs/2609.22978) |

Types: interface standard · environment hub · sandbox platform · training framework.

---

## 📚 Related Surveys and Resources

- **Agentic Environment Engineering for Large Language Models: A Survey of Environment Modeling, Synthesis, Evaluation, and Application** (CASIA, 2026.06) — organizes environments by an engineering lifecycle (design → creation → evaluation → application), with symbolic vs. neural synthesis and three environment-evolution paradigms. [paper](https://arxiv.org/abs/2606.12191)

---

## 🤝 Contributing

Contributions are welcome via issues or pull requests. Please check the original source before submitting; numbers should be quoted from the paper with a section, table or figure reference.

- **Add a paper** — title with link, date (YYYY.MM), venue, the component(s) it contributes to, one sentence per component, domain tags, code link.
- **Add an effect** — the changed condition, the component, the outcome, the finding with its original numbers, the evidence type, and where it appears in the source.
- **Correct an entry** — the row, the proposed change, and the source supporting it.

Entries that could not be checked against the original source are marked ⚠ until verified.

## 📖 Citation

The survey is in preparation. A BibTeX entry will be added here when it is released.

## License

Apache-2.0. See [LICENSE](LICENSE).
