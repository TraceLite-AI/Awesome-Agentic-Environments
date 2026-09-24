# Coverage validity: do documented environment-dependent failures land in the 22 factors? (2026-09-24)

Test set: 134 leaf categories from nine independently published catalogs — cross-OS portability issues in Python (Silva et al., MSR 2026: 7 categories / 24 sub-categories), bugs in test code (Vahabzadeh et al., ICSME 2015), date/time bugs (Tiwari et al., MSR 2025), flaky tests in Python (Gruber et al., ICST 2021), the flaky-test survey (Parry et al., TOSEM 2022), DSec §6.4 misbehavior instances, Terminal-Bench limitations, OSWorld-Verified fixed-issue types, Anthropic's infrastructure-noise experiment, and sources of randomness in agentic evals (Bjarnason et al.). Every source was opened; category names are verbatim.

Each leaf gets exactly one label: a factor; EXCLUDED-budget; NOT-ENVIRONMENT (model/harness/task/grader cause); or UNMAPPED (environment cause with no factor).

| label | leaves |
|---|---|
| mapped to a factor | 59 |
| EXCLUDED-budget | 17 |
| NOT-ENVIRONMENT | 46 |
| UNMAPPED | 12 |

Hit rate = mapped / (mapped + UNMAPPED) = 59/71 = 0.83 (0.88 after removing three non-settable noise items). Factor hits: os 19, net 10, perm 5, tz 5, clock 5, fs 4, arch 2, isolation 2, stack-version 2, shell 2, channel 1, tty 1, locale 1. Zero hits for the hardware group, mount, entry-name, build-tools, toolchain, browser-engine — the catalogs contain no GPU or toolchain studies (a test-set limitation; the admission table shows these values have strong engineering-doc cases).

UNMAPPED residue collapses into candidate factors for v0.3: **installed-packages** (system libraries / fonts present), **limit-enforcement** (guaranteed allocation vs lenient over-allocation at the same nominal quota — Anthropic's data moves scores at constant budget, so it is not the budget knob), **external-state** (time-varying state of third-party services the task depends on), and **infra-reliability** (transient cluster faults; a noise term, not settable). Seven labels are judgement calls (file locking → os, binary-wheel mismatch → arch, two I/O rows, XFS ioctl and /proc crash → isolation, time limits and concurrency → budget); relabelling moves the hit rate within 0.80–0.85.
