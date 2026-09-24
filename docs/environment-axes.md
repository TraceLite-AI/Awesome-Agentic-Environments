# Environment axes and values (v0.2, 2026-09-23)

**Definition.** The environment is everything outside the policy under test that can change the trajectory of the correct solution. It is infinite-dimensional; "testing the whole environment" is not a meaningful goal. We *project* it onto a finite set of named axes. The environment space is the Cartesian product

    E = A_1 × A_2 × … × A_n

where each axis A_i is a finite, named value set with a designated baseline value. A **cell** is a coordinate in E **plus a pin list**: image digests, distribution version, runner image version, exported system settings, harness version, model version. A coordinate without a pin list is not a cell; the same coordinate with a different pin list is a different cell.

## Axis admission: the four-step test

A candidate axis A enters the product only if all four steps hold for some task t:

1. A correct solution s passes in cell a.
2. Moved unchanged to cell b (differing from a only on A), s fails.
3. Cell b has a correct solution s′ that is **structurally** a different approach, not the same approach written more cheaply.
4. The reverse also holds.

Step 3 excludes budget knobs: CPU count, memory, VRAM, disk quota, bandwidth, latency, screen resolution, exclusive vs shared GPU. They change the cost of a solution, not its shape.

Under each axis: **contact surfaces** → **mechanisms** → **device-level readings**. A cell that claims to differ from baseline on an axis must show a reading; differences are never inferred from scores.

## The factor table

Legend: `*` baseline. `(candidate)` marks values demoted after the admission check in `validity-admission-cases.md` (no documented case in which the correct approach is structurally different). Every other non-baseline value has at least one documented case.

| Group | Factor | Values | Excluded neighbours (budget) |
|---|---|---|---|
| Hardware | arch | x86_64 * / arm64 | CPU count |
| Hardware | accel | none * / nvidia (candidate) / amd-rocm / apple-metal | VRAM |
| Hardware | toolkit | matched * / driver-only / major-mismatch | |
| Hardware | compute-cap | current * / old | |
| Hardware | gpu-count | single * / multi | exclusive / shared mode |
| System | os | linux * / macos / windows / android | distribution and version (pinned) |
| System | fs | case-sensitive * / case-insensitive / unicode-normalizing | disk quota |
| System | isolation | container * / microvm (candidate) / vm (candidate) / bare (candidate) | |
| System | perm | root * / sudo-nopasswd / non-root / non-root+readonly-sys / restricted-caps | |
| System | mount | normal * / tmp-noexec | |
| Runtime stack | stack-version | current * / old | relative to the task's declared stack |
| Runtime stack | entry-name | canonical * / alias-missing | relative to the task's declared stack |
| Runtime stack | build-tools | present * / absent | relative to the task's declared stack |
| Runtime stack | toolchain | gnu * / busybox / bsd | |
| Runtime stack | shell | bash * / dash / zsh / powershell / cmd | |
| Runtime stack | browser-engine | chromium * / firefox / webkit (candidate) | web tasks only |
| Policy-visible surface | channel | terminal * / gui (candidate) / a11y-tree / web-dom | screen resolution |
| Policy-visible surface | tty | tty * / no-tty | terminal width |
| External world | net | online * / offline / allowlist / proxy-required / ipv6-only | bandwidth, latency |
| External world | locale | C.UTF-8 * / C / en_US.UTF-8 / de_DE.UTF-8 / tr_TR.UTF-8 / zh_CN.GBK / cp1252 | |
| External world | tz | UTC * / Asia/Shanghai (candidate) / Europe/Berlin / Asia/Kolkata | |
| External world | clock | normal * / future+1y / past-1y / frozen | |

22 factors, 74 values. Star design: 1 + Σ(|A_i| − 1) = 53 cells (formal count, before removing infeasible combinations such as busybox on macOS). Full factorial ≈ 10¹⁰: defined, never run.

## Candidate factors for v0.3 (from the coverage check)

- **installed-packages** — presence of system libraries and fonts (13 projects in the cross-OS study fail on missing libraries; OSWorld-Verified fixed font installation).
- **limit-enforcement** — guaranteed allocation with hard kill vs lenient over-allocation at the same nominal quota; moves scores at constant budget, so it is not the budget knob.
- **external-state** — the time-varying state of third-party services a task depends on.

## Rules

1. **Values are parameterized by the task's stack.** Runtime-stack values are interpreted relative to the stack a task declares: `current / old` is py3.12 / py3.8 for a Python task, node22 / node18 for a Node task, CUDA 12 / 11 for a CUDA task.
2. **The baseline cell is defined per task family.** GPU tasks start from `accel=nvidia, toolkit=matched`; ordinary tasks from `accel=none`. The star design is unchanged; only the origin moves.
3. **Closed core, open extension.** A candidate value becomes core only when at least one task passes both admission gates on it with a device reading. New factors follow the same route.
4. **Pinning is bit-for-bit.** A coordinate is a valid experimental factor only if every other coordinate is pinned (digest-addressed images, exported settings), otherwise dependency drift is a hidden factor in every cell.

## Measurement protocol

- **Task gates.** Gate 1: the reference solution passes in every relevant cell. Gate 2: the naive solution fails only in target cells. Axes first, tasks second; never retrofit axes onto existing tasks.
- **Three tiers of budget.** (1) Star: baseline plus one step along each axis (Morris elementary effects → main effect per axis). (2) 2-way covering array: the NIST interaction rule says 70–93% of failures need ≤2 conditions, and one-at-a-time designs cannot see interactions at all. (3) A few off-axis natural points (e.g. Ubuntu 20.04 bundling Python 3.8), decomposed with tiers 1–2.
- **Pairwise is a budget, not a guarantee.** NIST's own guide notes pairwise testing can miss 10–40% of faults; it is the cheap second tier, not a sufficiency claim.
- **Repeated runs are part of the protocol.** Flakiness studies (Gruber et al.: ~170 reruns for 95% confidence that a test is not flaky) mean noise must be separated before any cell difference is attributed to an axis.

## Reporting

Per policy m and axis i: **discrete difference** Δ_i(m) = pass rate at baseline − pass rate one step along i (for categorical axes this is a difference at a given baseline, not a derivative), and **flip rate** = fraction of tasks whose outcome differs between the two cells. Interaction terms Δ_ij − Δ_i − Δ_j only for pairs in the covering array. **Aggregate scores only with conditions stated**: an OS ranking is an artifact of where the targets happen to be; an aggregate is comparable only when the task distribution, weights and comparison set are declared. Report by contact surface, with a "controls hold" health check.

Each criterion carries the assumption the policy is suspected of hard-coding; the set of failed criteria is the failure **signature**, aggregated per policy into an **assumption profile**. Attribution requires three yes answers: the environment really differs on that axis (reading); the policy's action really depended on that assumption (trajectory, read by a human); a correct route exists in the same cell (gate 1).
