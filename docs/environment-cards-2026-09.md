# Environment Cards: six agent benchmarks and platforms (filled 2026-09-23, third-party)

Filled by opening the paper (PDF/HTML) and the official repository (Dockerfiles, configs, harness source) for each object. Every value carries its source: `(paper §X)` or `(code: path)`. `unstated` = not found in anything opened. Filled by TraceLite AI as a third party; not yet confirmed by the original authors.

Caveats: SWE-bench values come from harness tag v4.1.0 (last version with `swebench/harness/dockerfiles/*.py`); the 2023 paper describes conda environments, the Docker harness arrived in 2024. Terminal-Bench values cover TB-2.0 tasks (`harbor-framework/terminal-bench`) run by Harbor 0.23.0, with TB-1.x (`laude-institute/terminal-bench` 0.2.18) noted where different. DSec is paper-only.

## Summary: factor × object

| factor | SWE-bench | Terminal-Bench | OSWorld | WebArena | τ-bench | DSec |
|---|---|---|---|---|---|---|
| arch | x86_64 forced (code) | host Docker arch, no pin (code) | host-dependent x86_64/arm64 VM (code) | unstated (t3a.xlarge recommended) | unstated | AMD EPYC 9655 hosts (paper §8.1) |
| accel | none (code) | per-task `gpus`, 0 in sampled tasks (code) | none; KVM optional (code) | unstated | unstated | GPU containers / virtio-gpu (paper) |
| toolkit | unstated | unstated | unstated | unstated | unstated | unstated |
| compute-cap | unstated | unstated | unstated | unstated | unstated | unstated |
| gpu-count | 0 (code) | 0, max 1 (code) | unstated | unstated | unstated | unstated |
| os | ubuntu:22.04 (code) | per task: ubuntu:24.04 / python:3.x-slim (Debian) / others (code) | Ubuntu guest, release unstated; Windows 10 x64 (code/paper) | unstated | unstated | Linux 7.0 hosts, 6.1 guests; Ubuntu bases; Android VMs (paper) |
| fs | unstated | unstated | unstated | unstated | unstated | overlayfs + EROFS + ext4 (paper §5.2) |
| isolation | Docker container (code) | Docker compose; Daytona (paper) / Modal (README) | VM: VMware / VirtualBox / Docker-QEMU-KVM / cloud (code/paper) | Docker per site; host Playwright browser (paper/code) | none, bare Python | FnCall / containers-in-QEMU / Firecracker / QEMU VMs (paper) |
| perm | root (code) | root (code) | `user` with sudo (README) | unstated | unstated | root + AppArmor (paper) |
| mount | none (code) | log volumes only (code) | qcow2 read-only on host (code) | none (paper A.2) | unstated | read-only EROFS + writable overlay (paper) |
| stack-version | conda per repo×version, pinned (code) | per-task image tags (code/paper) | host Python ≥3.10; guest unstated | Python 3.10; partial pins (code) | unpinned, `>=` only (code) | per-layer versioned, unpinned (paper) |
| entry-name | python (code) | varies; python3 in traces | unstated | python (code) | python (code) | unstated |
| build-tools | build-essential etc. (code) | per task (code) | unstated | unstated | unstated | unstated |
| toolchain | GNU (ubuntu base) | GNU (ubuntu/debian bases) | unstated | unstated | unstated | unstated |
| shell | bash (code) | bash in tmux (code/paper) | sh via subprocess; `bash -lc` setup (code) | none | none | bash via chronus (paper) |
| browser-engine | none | none | Chrome in guest, version unstated (code) | Chromium via Playwright 1.32.1 (code) | none | unstated |
| channel | none: patch in, tests out | terminal, tmux pane (code/paper) | screenshot 1920×1080 + a11y/SoM (code/paper) | a11y tree / HTML / screenshot, 1280×720 (code) | JSON tool calls + user text | shell / tool calls; GUI via VM (paper) |
| tty | no pty (code) | pty via tmux (code) | no pty, HTTP + PIPE (code) | none, headless browser | none | unstated |
| net | online, default bridge (code) | public internet (paper/code); allowlist / none optional | online; proxy recommended (README) | online; self-hosted sites + offline Wikipedia (paper/code) | online for LLM APIs only | eBPF per-task allowlist (paper) |
| locale | unstated | unstated | unstated | unstated | unstated | unstated |
| tz | Etc/UTC (code) | unstated | unstated | unstated | fictional 2024-05-15 15:00 EST (code/paper) | unstated |
| clock | unstated | unstated | unstated | unstated | frozen / fictional (code) | unstated |

**Pin lists.** SWE-bench: `FROM ubuntu:22.04` (mutable tag), prebuilt images pulled at tag `latest`, no digest anywhere; pip packages mostly `==`-pinned, some unpinned; apt unpinned. Terminal-Bench: tags only, none of 12 sampled Dockerfiles uses `@sha256:`; TB-1 base images date-tagged but themselves `FROM ubuntu:24.04`. OSWorld: VM images by fixed HF URL without hash check; AWS AMIs pinned by ID per region × resolution; VM snapshot `init_state` reverted before every task. WebArena: date-suffixed image names (`shopping_final_0712`), no digests; AMI `ami-08a862bf98e3bd7aa`; 4 pinned Python packages, rest floating. τ-bench: no container; deps lower-bounded only; DB state = JSON in repo, reward = SHA-256 of final DB state. DSec: example `registry.../sphinx-9658:official` (tag); layers immutable in EROFS; harness is an "independently versioned" toolkit, scheme unstated.

**Factors the authors vary.** Only OSWorld varies card factors (resolution downsampling, observation type, OS on 43 tasks). MLE-bench (not carded here) varies compute. The others vary agents, models, prompts, or repeat counts only.

**Author-acknowledged environment sensitivity.** Terminal-Bench §5: "variability in machine resources and container runtime enforcement can lead to differences in effective task environments." OSWorld §6: "Efforts can be made to ensure our environment's seamless deployment across various hardware and software settings." DSec §2.3: backends "have different startup costs, isolation boundaries, filesystem semantics, and operating-system capabilities." SWE-bench, WebArena, τ-bench: none on hardware/OS.

**Blank at a glance.** `toolkit`, `compute-cap`, `locale`: unstated for all six. `fs`: unstated for all but DSec. `clock`: unstated for all but τ-bench. `tz`: stated only by SWE-bench (in code) and τ-bench (fictional). Many values exist only in code, never in the paper: SWE-bench's OS, user and timezone; WebArena's viewport and browser engine; Terminal-Bench's shell and pty.

---

## Card 1 — SWE-bench (harness swe-bench/SWE-bench v4.1.0; paper arXiv 2310.06770, ICLR 2024)

| factor | value | source | evidence |
|---|---|---|---|
| arch | x86_64 forced | code: `swebench/harness/test_spec/test_spec.py`, README | `make_test_spec(..., arch="x86_64")` → `platform="linux/x86_64"`; `FROM --platform={platform} ubuntu:{ubuntu_version}`; README: "Support for arm64 machines is experimental" |
| accel | none | code: `docker_build.py` | `containers.create(...)` passes no device/GPU flags |
| toolkit | unstated | — | paper mentions A100s only for SWE-Llama training |
| compute-cap | unstated | — | — |
| gpu-count | 0 | code | see accel |
| os | ubuntu:22.04 (default) | code: `constants/__init__.py`, `dockerfiles/python.py` | `DEFAULT_DOCKER_SPECS = {"conda_version": "py311_23.11.0-2", "node_version": "21.6.2", "pnpm_version": "9.5.0", "python_version": "3.9", "ubuntu_version": "22.04"}`. Paper: unstated |
| fs | unstated | — | — |
| isolation | Docker container (Modal optional) | code: `docker_build.py`; paper A.3 | paper (2023): "Create executable contexts as conda envs." |
| perm | root | code: `constants/__init__.py` | `DOCKER_USER = "root"`; a `nonroot` user exists in the image but eval runs as root |
| mount | none | code: `docker_build.py` | no volumes; patch copied to `/tmp/patch.diff`; workdir `/testbed` |
| stack-version | Python pinned per repo×version via conda | code: `constants/python.py`; paper A.3 | e.g. `SPECS_FLASK["2.0"] = {"python": "3.9", "pip_packages": [...]}` |
| entry-name | `python` | code: `dockerfiles/python.py` | installs `python-is-python3`; `.bashrc` activates `testbed` |
| build-tools | build-essential, libffi-dev, libtiff-dev, git, wget, curl, jq | code: `dockerfiles/python.py` | apt install line |
| toolchain | GNU (ubuntu base) | code | — |
| shell | bash | code: `test_spec/test_spec.py`, `run_evaluation.py` | `#!/bin/bash`, `set -uxo pipefail`; `exec_run_with_timeout(container, "/bin/bash /eval.sh")` |
| browser-engine | n/a | — | — |
| channel | none (patch in, tests out) | code: `run_evaluation.py`; paper §2 | `git apply` of `model_patch` |
| tty | no pty | code: `docker_utils.py` | `exec_create` / `exec_start(stream=True)` without `tty=` |
| net | online (Docker default bridge) | code: `docker_build.py`, `test_spec/utils.py` | `git clone` at build; `git remote remove origin  # so the agent won't see newer commits` |
| locale | unstated | code: `dockerfiles/python.py` | installs `locales locales-all`, sets no `LANG` |
| tz | Etc/UTC | code: `dockerfiles/python.py` | `ENV TZ=Etc/UTC` |
| clock | unstated | — | — |

Pin list: tag not digest (`ubuntu:22.04`; DockerHub `swebench/*:latest` by default; v5 image name from dataset row). Harness `swebench` v4.1.0 examined, main = v5.0.1. Snapshot = per-instance `base_commit` SHA + repo mirrors. Varied in paper: none of the 22 factors. Acknowledged sensitivity: none in paper; repo docs claim containerization "eliminates environment discrepancies".

## Card 2 — Terminal-Bench (TB-2.0 + Harbor 0.23.0; TB-1.x noted; paper arXiv 2601.11868)

| factor | value | source | evidence |
|---|---|---|---|
| arch | host Docker arch, no pin | code: `harbor/src/harbor/environments/docker/utils.py` | `default_docker_platform()` reads `docker version --format {{.Server.Os}}/{{.Server.Arch}}` |
| accel | per-task `gpus`, 0 sampled | code: `task.toml`, `docs/task-template.toml` | `gpus = 0 # max 1, expect H100` |
| toolkit / compute-cap | unstated | — | — |
| gpu-count | 0, max 1 | code | — |
| os | heterogeneous per task | code: `tasks/*/environment/Dockerfile` | 12 sampled FROM lines: `python:3.11-slim` ×3, `ubuntu:24.04` ×3, `oven/bun:1.2.15-debian`, `python:3.12-slim`, `python:3.13-slim-bookworm`, `coqorg/coq:8.18`, `node:22-bookworm`, `eclipse-temurin:17-jdk-jammy`. Paper §2.1: "a Docker image" per task, no OS named |
| fs | unstated | — | — |
| isolation | Docker compose; Daytona in paper; Modal in CI | code: `docker-compose-build.yaml`; paper §3.4 | "we use Daytona and run between 32 and 100 containers in parallel" |
| perm | root (image default) | code: compose templates; TB-1 `terminal.py` | no `user:` set |
| mount | log volumes only | code: TB-1 `docker-compose.yaml` | — |
| stack-version | per-task image tags | code; paper §5 | "pinning package versions, providing pre-built Docker images" |
| entry-name | varies; `python3` in traces | code; paper appendix | `"keystrokes": "python3 /app/eval.py\n"` |
| build-tools | per task | code | e.g. `build-essential cmake clang ... ninja-build` |
| toolchain | GNU (ubuntu/debian bases) | code | — |
| shell | bash inside tmux | code: `terminus_2/tmux_session.py`; paper §3.3 | `tmux new-session ... 'bash --login'`; "completes tasks using only Bash commands" |
| browser-engine | n/a | — | — |
| channel | terminal (tmux pane capture; TB-1 160×40) | code; paper §3.3 | `tmux capture-pane -p` |
| tty | pty via tmux | code | `tmux send-keys` |
| net | public internet by default; `allowlist` / `none` available | paper §5; code: `models/task/config.py` | `network_mode = "public" # Terminal-Bench is open internet` |
| locale / tz / clock | unstated | — | — |

Pin list: tags only, no `@sha256:` in 12 sampled Dockerfiles; TB-1 base images date-tagged but `FROM ubuntu:24.04`. Package pinning stated as policy, enforced by contributor checklist. Per-task resources `cpus = 2, memory_mb = 4096, storage_mb = 10240`. Varied in paper: agents and models only. Acknowledged: §5 limitation on internet access and "variability in machine resources and container runtime enforcement"; checklist "Some non-determinism remains."

## Card 3 — OSWorld (xlang-ai/OSWorld main; paper arXiv 2404.07972, NeurIPS 2024)

| factor | value | source | evidence |
|---|---|---|---|
| arch | host-dependent x86_64 / arm64 VM (VMware); Docker/AWS x86 | code: `providers/vmware/manager.py`, `providers/aws/manager.py`; paper A.1 | `platform.machine()` selects `Ubuntu-x86.zip` vs `Ubuntu-arm.zip`; AWS `t3.xlarge` |
| accel | none; KVM optional | code: `providers/docker/provider.py` | `/dev/kvm` if present, else "running without hardware acceleration" |
| toolkit / compute-cap / gpu-count | unstated | — | — |
| os | Ubuntu guest, release unstated; Windows 10 x64 for 43 tasks | code: `desktop_env.py` `os_type="Ubuntu"`, `Windows-10-x64.qcow2.zip`; paper §2.4, §3 | Ubuntu release number appears nowhere |
| fs | unstated | — | — |
| isolation | VM: VMware (default, `vmrun`), VirtualBox, Docker-wrapped QEMU/KVM, or cloud (AWS, GCP, Azure, Aliyun, Volcengine, Modal, Daytona) | code: `providers/*`; paper §2.2 | `containers.run("happysixd/osworld-docker", environment={"DISK_SIZE":"32G","RAM_SIZE":"4G","CPU_CORES":"4"}, ...)` |
| perm | guest `user` / `password` with sudo | README | "the agent needs the password to obtain sudo privileges" |
| mount | qcow2 read-only host-side | code | `"bind": "/System.qcow2", "mode": "ro"` |
| stack-version | host Python ≥3.10; guest unstated | README | — |
| entry-name | unstated (pyautogui strings run by in-VM Flask server) | code: `server/main.py` | `subprocess.run(..., shell=True)` |
| build-tools / toolchain | unstated | — | — |
| shell | sh via subprocess; `bash -lc` for setup | code | — |
| browser-engine | Chrome/Chromium in guest, remote-debugging 9222, version unstated | code; paper appendix | — |
| channel | screenshot 1920×1080 default, a11y tree (AT-SPI / PyWinAuto), SoM | code: `desktop_env.py`, `run.py`; paper §2.3, A.2.1 | "The raw resolution of the screen is set to 1920 × 1080" |
| tty | no pty; HTTP + PIPE | code: `server/main.py` | — |
| net | online; proxy recommended for some tasks | README, `SETUP_GUIDELINE.md` | residential proxy config `settings/proxy/dataimpulse.json` |
| locale / tz / clock | unstated | — | — |

Pin list: VM images by fixed HF URL, no hash check; `happysixd/osworld-docker` untagged; AWS AMIs by ID per region × resolution (e.g. `(1920,1080): "ami-0d23263edb96951d8"`); Daytona snapshot `osworld-ubuntu-v1`; VM snapshot `init_state` reverted before every task. Varied in paper: resolution downsampling (0.2–0.8), observation type, history length, OS (43 tasks), UI noise. Acknowledged: §6 "seamless deployment across various hardware and software settings"; §5 "not robust to UI layout and noise".

## Card 4 — WebArena (web-arena-x/webarena v0.2.0; paper arXiv 2307.13854)

| factor | value | source | evidence |
|---|---|---|---|
| arch | unstated (EC2 `t3a.xlarge` recommended) | code: `environment_docker/README.md` | — |
| accel / toolkit / compute-cap / gpu-count | unstated | — | — |
| os | unstated (site images opaque tars; AMI OS unnamed; CI `ubuntu-latest`) | code | images `shopping_final_0712`, `gitlab-populated-final-port8023`, `kiwix33`, ... |
| fs | unstated | — | — |
| isolation | Docker per site; agent browser un-sandboxed on host via Playwright | paper A.2; code: `browser_env/envs.py` | "one per website ... fully self-contained" |
| perm | unstated | — | — |
| mount | none | paper A.2 | "do not rely on external volume mounts" |
| stack-version | Python 3.10 (CI 3.10.9); `playwright==1.32.1`, `openai==0.27.0`, `transformers==4.33.2`, `beartype==0.12.0` pinned; rest floating | code: `requirements.txt`, `tests.yml` | — |
| entry-name | `python` | code: README | — |
| build-tools / toolchain | unstated | — | — |
| shell | n/a (Playwright actions) | code | — |
| browser-engine | Chromium via Playwright 1.32.1 (bundled version unstated) | code: `envs.py` | `self.playwright.chromium.launch(headless=self.headless, ...)`. Paper does not name Playwright |
| channel | a11y tree default; raw HTML; screenshot; viewport 1280×720, `device_scale_factor=1`; obs ≤1920 tokens | code: `envs.py`, `run.py`; paper §2.3 | viewport size is not in the paper |
| tty | n/a; headless | code | `headless: bool = True` |
| net | online, unrestricted from browser; sites self-hosted; Wikipedia offline (Kiwix, May 2023) | code: `env_config.py`; paper A.1 | AMI opens ports 80/3000/7770/7780/8023/8888/9999 to 0.0.0.0/0 |
| locale | unstated (no `locale` / `timezone_id` in Playwright context; per-task `geolocation` only) | code: `envs.py` | — |
| tz / clock | unstated | — | — |

Pin list: date-suffixed image names, no digests; AMI `ami-08a862bf98e3bd7aa`; reset = restart containers from original images. Varied in paper: no environment factor (prompting and models). Acknowledged: none on hardware/OS.

## Card 5 — τ-bench (sierra-research/tau-bench main; paper arXiv 2406.12045)

| factor | value | source | evidence |
|---|---|---|---|
| arch / accel / toolkit / compute-cap / gpu-count / os / fs | unstated | — | pure-Python, API-only |
| isolation | none (bare Python process) | code: README, `setup.py`; paper §4 | `pip install -e .` |
| perm / mount | unstated | — | — |
| stack-version | Python unpinned; deps `>=` only | code: `setup.py` | `openai>=1.13.3, litellm>=1.41.0, ...` |
| entry-name | `python` | code: README | — |
| build-tools / toolchain | unstated | — | — |
| shell | n/a (in-process Python tools) | code: `envs/base.py` | `self.tools_map[action.name].invoke(...)` |
| browser-engine | n/a | — | — |
| channel | JSON tool calls (function calling / ReAct) + simulated-user text | code; paper §3 | — |
| tty | n/a | — | — |
| net | online for LLM APIs only; environment data local JSON | code: `envs/user.py` | — |
| locale | unstated | — | — |
| tz | fictional "2024-05-15 15:00:00 EST" declared in policy | code: `envs/airline/wiki.md`; paper Fig. 1 | — |
| clock | frozen / fictional | code | sampled tool uses only dates from data |

Pin list: no container; deps lower-bounded; DB state = JSON reloaded on every `reset()`; reward = SHA-256 of final DB state vs ground truth. User simulator `gpt-4-0613`, agent temperature 0.0, user 1.0, ≥3 trials. README: tasks outdated, use tau2/τ³-bench. Varied in paper: agent method, models, k. Acknowledged: stochasticity from LM sampling; user instruction typos/ambiguity.

## Card 6 — DeepSeek DSec (paper arXiv 2609.22978; no code)

| factor | value | source | evidence |
|---|---|---|---|
| arch | AMD EPYC 9655 hosts; label unstated | paper §8.1 | — |
| accel | GPU containers for FnCall (shared / exclusive); virtio-gpu for full VMs; model unnamed | paper §2.2, §3.3 | — |
| toolkit / compute-cap | unstated | — | — |
| gpu-count | unstated (per-request placement) | paper §3.2 | — |
| os | Linux 7.0 hosts, Linux 6.1 microVM guests; Ubuntu base images (release unstated); Android VMs via QEMU | paper §8.1, §4.2, §2.2 | — |
| fs | overlayfs: read-only EROFS lower + writable upper (ext4 in microVMs) | paper §5.2 | — |
| isolation | FnCall / containers (inside QEMU/libvirt VMs) / Firecracker microVMs / QEMU full VMs | paper §2.2, §3.3 | "FnCall and containers run inside QEMU/libvirt VMs rather than directly on the host." |
| perm | root (example); AppArmor applies even to root | paper §2.1, §6.5 | `init_user = "root"` |
| mount | read-only EROFS base/toolkit layers + writable overlay; AppArmor file controls | paper §5.2, §6.5 | — |
| stack-version | per layer, independently versioned; no pins stated | paper §4.2 | 11,266 base images, 102,171 workspaces, 103 toolkits in one week |
| entry-name / build-tools / toolchain | unstated | — | — |
| shell | bash (chronus shell sessions) | paper §3.3, §6.4 | "agents also tried overwriting /bin/bash" |
| browser-engine | unstated (browsers in full-VM backend) | paper §3.3 | — |
| channel | shell / tool calls via libdsec + chronus; GUI via full VM, resolution unstated | paper §2.1, §3.3 | — |
| tty | unstated (stdout captured asynchronously) | paper §6.4 | — |
| net | per-task allowlist enforced by eBPF (IP / port / protocol) | paper §2.1, §6.5 | `network_rules = {"npm": False, "pypi": True}` |
| locale / tz / clock | unstated | — | — |

Pin list: example image by tag (`sphinx-9658:official`); layers immutable in EROFS; DeepSeek Harness is an independently versioned toolkit, scheme unstated; `pack_diff` incremental snapshots, IDs unstated. Varied in paper: backend, image-loading strategy, memory settings; not OS/locale/tz/arch. Acknowledged: §2.3 backends differ in "filesystem semantics, and operating-system capabilities"; §6.5 controls "address only part of the problem".
