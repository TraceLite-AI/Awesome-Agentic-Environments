# Environment Card (v0.1)

A one-page declaration of the execution environment behind a benchmark, a platform, or a single experiment. Modeled on Model Cards and Datasheets for Datasets: cheap to fill, cheap to check, no theory required to use it.

**Rules**

1. Every value must have a source: `(paper §X)` or `(code: path/to/file)`. Do not fill inferred values.
2. `unstated` means the material does not say. It is information, not blame. A card full of `unstated` is still useful: it says the results have no coordinates.
3. `n/a` means the factor has no meaning for this object (e.g. `browser-engine` for a terminal-only task set).
4. The card describes the object as it **is**, not as it should be. Recommendations do not go on the card.
5. Third parties may fill a card and must say so. A card confirmed or corrected by the original authors is the highest grade.
6. `n/a` only when the factor is meaningless for the object (τ-bench has no execution environment, so `os` is n/a; a terminal-only task set has no `browser-engine`; no GPU means `toolkit` is n/a).
7. Absence in code is `unstated`, not `none`. No mount configuration means `unstated`, unless an explicit empty configuration exists.
8. The card describes the environment the agent acts in. The host machine's CPU model or the interpreter that runs the harness are not coordinates; record them separately.
9. Evidence at file or function level. "The README says" is not enough; give the path or the section number.

**Template**

```
Environment Card v0.1
Object:                 Version:            Date:            Filled by:
Sources consulted:

COORDINATES  (value | source | evidence)
Hardware        arch | accel | toolkit | compute-cap | gpu-count
System          os | fs | isolation | perm | mount
Runtime stack   stack-version | entry-name | build-tools | toolchain | shell | browser-engine
Visible surface channel | tty
External world  net | locale | tz | clock

PIN LIST
Image digest or tag:                 Pin policy (digest / tag / none):
Package version pin policy:
Harness / scaffold version:          Model version policy:
Snapshot IDs:                        Exported system settings:

Factors the authors vary:
Author-acknowledged environment sensitivity (verbatim):
Repeat-run policy:
```

Allowed values per factor are listed in [environment-axes.md](environment-axes.md). A machine-readable schema is in [environment-card.schema.json](environment-card.schema.json).

**How it relates to existing definitions.** WebArena's ⟨S, A, O, T⟩ is the abstract form of the COORDINATES block: everything absorbed into the transition function T is unpacked into 22 factors. Epoch AI's "the set of actions … and the surrounding context that determines the effect of these actions" — the context is coordinates plus pin list. Mercor's "software, tasks, verifiers" — the software is the System and Runtime-stack groups. The card is the common refinement of all three; it does not replace any of them.
