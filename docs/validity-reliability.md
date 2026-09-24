# Reliability: two independent fillers, six Environment Cards (2026-09-24)

Filler A filled the six cards on 2026-09-23 from papers and official code. Filler B refilled them on 2026-09-24 under the instruction not to open A's cards, from the same kinds of material. 132 cells (22 factors × 6 objects).

| reading | agreement | Cohen's κ |
|---|---|---|
| value level (same status and same meaning; "unstated" and "n/a" merged as "no value") | 115/132 = 0.87 | |
| stated vs no value (2 classes) | 0.89 | 0.77 |
| stated / unstated / n/a (3 classes) | 0.71 | 0.54 |

The 3-class κ is low almost entirely because the fillers used "n/a" differently (B used it for τ-bench and for GPU factors on GPU-less objects; A wrote "unstated"). Per object: WebArena 21/22, DSec 21/22, SWE-bench 19/22, Terminal-Bench 19/22, τ-bench 19/22, OSWorld 16/22.

17 substantive disagreements: 5 where one filler found evidence the other missed (OSWorld's Ubuntu 22.04 in appendix B.2; SWE-bench's django `LANG=en_US.UTF-8` export in `constants/python.py`; OSWorld's `python` entry in `controllers/python.py`; τ-bench's fictional time in `wiki.md`); 6 inference-vs-strict (A inferred GNU coreutils from an ubuntu base and "no mount" from the absence of mount config; B wrote unstated); 2 same-code-different-coding (OSWorld shell: "sh via subprocess" vs "bash", since `run_bash` prepends `#!/bin/bash`); 4 host-vs-guest (DSec's host CPU model; interpreter that runs the harness rather than the agent).

Rules added to the card (rules 5–8 in `environment-card.md`): "n/a" only when the factor is meaningless for the object; absence in code is "unstated", not "none"; the card describes the environment the agent acts in, host facts go elsewhere; evidence at file or function level. The merged cards are in `environment-cards-2026-09.md`.
