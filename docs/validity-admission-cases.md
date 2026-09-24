# V2 准入效度：52 个非基准取值的外部案例（子代理报告，2026-09-24；所有 URL 已打开）
强 = 有失败记录 + 有结构不同的正确做法记录；弱 = 只有失败/限制记录；无 = 两轮检索无案例。

| factor | value | what breaks | structurally different correct approach | source | strength |
|---|---|---|---|---|---|
| arch | arm64 | `docker pull` on Apple Silicon: "no matching manifest for linux/arm64/v8" (amd64-only image) | `--platform linux/amd64` emulation (slower, may fail) or build/publish native arm64 image | github.com/foundry-rs/foundry/issues/7680 ; docs.docker.com/build/building/multi-platform/ | strong |
| accel | nvidia | CPU wheel silently never uses GPU; no crash in baseline→nvidia direction | install from CUDA wheel index (different artifact) | pytorch.org/get-started/previous-versions/ | weak |
| accel | amd-rocm | CUDA source/wheels do not build/run on AMD | hipify-clang/hipify-perl (manual porting remains) + ROCm wheel index | rocm.docs.amd.com/projects/HIPIFY ; pytorch previous-versions | strong |
| accel | apple-metal | no CUDA wheels on macOS; MPS raises NotImplementedError for unsupported ops | `torch.device("mps")` + `PYTORCH_ENABLE_MPS_FALLBACK=1` | docs.pytorch.org/docs/2.14/notes/mps.html ; pytorch/pytorch#77764 | strong |
| toolkit | driver-only | `pip install flash-attn` source build: "nvcc was not found" | prebuilt wheel or `-devel` CUDA image; don't compile extensions on driver-only host | Dao-AILab/flash-attention#447 | strong |
| toolkit | major-mismatch | `cudaErrorCallRequiresNewerDriver` (min driver per CUDA major: 13.x≥580, 12.x≥525, 11.x≥450) | upgrade driver, `cuda-compat` package, or build against older toolkit / PTX JIT | docs.nvidia.com/deploy/cuda-compatibility/ | strong |
| compute-cap | old | GTX 780 (CC 3.0): "no kernel image is available for execution on the device" | build from source with `TORCH_CUDA_ARCH_LIST` or older wheel | pytorch/pytorch#31285 | strong |
| gpu-count | multi | NCCL all_reduce freezes with >1 RTX 4090; P2P corruption on GeForce | `NCCL_P2P_DISABLE=1` or driver ≥525.105.17 | NVIDIA/nccl-tests#117 ; pugetsystems.com RTX4090 multi-GPU | strong |
| os | macos | Python ≥3.8 defaults multiprocessing to spawn; fork-inherited-state code fails in child | `if __name__ == '__main__'` guard, importable targets, pass state explicitly | cpython Doc/library/multiprocessing.rst | strong |
| os | windows | MAX_PATH 260: cloning long-named repos fails | `\\?\` extended paths or LongPathsEnabled + longPathAware manifest | MicrosoftDocs win32 maximum-file-path-limitation | strong |
| os | android | Termux has no /bin/sh; hardcoded shebangs fail | `termux-fix-shebang` → `$PREFIX/bin/...` | termux/termux-fix-shebang README | strong |
| fs | case-insensitive | git repo with `AFile.txt` and `afile.txt`: one is "always modified" | `git rm --cached` collision, lowercase convention, `core.ignoreCase` | git-scm.com/docs/gitfaq ; core.adoc | strong |
| fs | unicode-normalizing | NFD-tracked filename: permanently untracked duplicate on macOS | re-track in NFC; `core.precomposeUnicode=true` | ManasDasri/NNDL#14 ; git core.adoc | strong |
| isolation | microvm | Firecracker: 6 emulated devices only, no GPU passthrough, no nested virt | move GPU/KVM step outside microVM (implied) | firecracker FAQ.md ; #668 | weak |
| isolation | vm | nested virtualization must be enabled at L1 creation; only KVM supported in L1 | enable nested virt or non-KVM driver | cloud.google.com nested-virtualization overview | weak |
| isolation | bare | no case found | — | — | none |
| perm | sudo-nopasswd | `env_reset`/`secure_path` strip HTTP_PROXY, PYTHONPATH, venv PATH | `sudo -E`, `sudo env VAR=…`, `env_keep`, explicit interpreter path | sudo.ws sudoers man | strong |
| perm | non-root | ports <1024 need CAP_NET_BIND_SERVICE; system site-packages not writable | high port / setcap / reverse proxy; `pip install --user` or venv | man7 capabilities(7) ; pip user guide | strong |
| perm | non-root+readonly-sys | NGINX with readOnlyRootFilesystem cannot write /tmp, /var/log | emptyDir mounts at each writable path + repoint config | docs.nginx.com kubernetes-read-only ; k8s security-context | strong |
| perm | restricted-caps | strace/gdb: "PTRACE_TRACEME: Operation not permitted" even with SYS_PTRACE (seccomp) | `--security-opt seccomp=unconfined` + cap-add, or debug from host | moby/moby#21051 ; docs.docker.com run | strong |
| mount | tmp-noexec | pip stages wheels in /tmp, `access(X_OK)` EACCES → scripts installed 644; pnpm installer "Permission denied" | point TMPDIR at exec-capable fs | pypa/pip#6364 ; pnpm/pnpm#9776 | strong |
| stack-version | old (py3.8 vs 3.12) | `list[int]` at runtime TypeError on 3.8 (PEP 585); reverse: distutils removed in 3.12 (PEP 632) | `from __future__ import annotations` / typing.List; setuptools/sysconfig | peps 585, 632 | strong |
| stack-version | old (Node 16 / JDK 17) | Node 18 made fetch global, ReferenceError on 16; JDK 17 JEP 403 InaccessibleObjectException | node-fetch/undici; `--add-opens` or migrate APIs | nodejs v18 announce ; openjdk JEP 403 | strong |
| entry-name | alias-missing (python) | `python` may be absent or python2 | use `python3` explicitly | PEP 394 | strong |
| entry-name | alias-missing (pwsh) | Windows ships powershell 5.1 only; `??`, `?.` parse errors; `curl` alias | write 5.1 subset or require pwsh; `curl.exe` | PowerShell-Docs differences-from-windows-powershell ; haxx.se curl alias | strong |
| build-tools | absent | `pip install psycopg2` sdist: "Python.h: No such file"/"libpq-fe.h" | `psycopg2-binary` / manylinux wheels / `--only-binary` | psycopg.org/docs/install.html | strong |
| toolchain | busybox | Nextcloud fpm-alpine: "find: unrecognized: -empty" | `apk add findutils` or POSIX-only rewrite | nextcloud/docker#282 | strong |
| toolchain | bsd | BSD `sed -i` requires extension arg; GNU form consumes script as extension | `sed -i '' -e …`, `perl -pi`, or gsed | Xcode sed(1) ; FreeBSD sed(1) | strong |
| shell | dash | bashisms under `#!/bin/sh` fail (Debian Policy 10.4) | `#!/bin/bash` explicitly or POSIX-ify + checkbashisms | debian.org policy ch-files | strong |
| shell | zsh | `pip install napari[all]` → "zsh: no matches found" | quote: `'napari[all]'` | napari/napari#2081 | strong |
| shell | powershell | `curl -H … -d …` invokes Invoke-WebRequest alias | `curl.exe` or remove alias | haxx.se 2016 curl alias | strong |
| shell | cmd | harness prepended `export CI=true …`; cmd.exe: "'export' is not recognized" — every command failed | platform-detect `set`/`$env:`, or spawn real bash | anomalyco/opencode#11927 | strong |
| browser-engine | firefox | Crawlee blockRequests (CDP) under Firefox: "CDP session is only available in Chromium" | engine-neutral `page.route()` | apify/crawlee#1621 ; playwright browsercontext | strong |
| browser-engine | webkit | Chromium-only surfaces absent (CDP, service workers, coverage) | engine-neutral APIs | playwright docs | weak |
| channel | gui | OSWorld 2.0: stale click as pop-up moves; DOM/API bypass fails on artifact-level checks | continuous observation / verify-before-submit stated as open gap | arxiv 2606.29537 | weak |
| channel | a11y-tree | canvas apps (Sheets, Figma, Canva) expose nothing to a11y APIs | hybrid: a11y snapshot + selective vision + coordinate actions | arxiv 2511.19477 | strong |
| channel | web-dom | XPath doesn't pierce shadow roots; iframes unreachable; canvas exposes nothing | frameLocator; CSS/text locators; vision fallback | playwright other-locators, frames ; arxiv 2511.19477 | strong |
| tty | no-tty | sudo: "no tty present and no askpass program" | `sudo -S` / `-A` / NOPASSWD; `ssh -t` | sudo.ws sudo man | strong |
| net | offline | any `pip install` against PyPI fails | `pip download` online then `--no-index --find-links` | pip user guide | strong |
| net | allowlist | self-hosted runners need github.com, api.github.com, *.actions.githubusercontent.com, codeload…; CNAME recursion | allow documented host set via REST meta endpoint | docs.github.com self-hosted runners communicating | strong |
| net | proxy-required | shell HTTP_PROXY does not affect docker daemon | daemon.json proxies / systemd drop-in; pip `--proxy` | docs.docker.com daemon/proxy | strong |
| net | ipv6-only | github.com has no AAAA record; cannot clone | DNS64/NAT64 or reverse proxy/mirror | github community discussion 10539 | strong |
| locale | C | ASCII default; UnicodeEncodeError on non-ASCII (pre-3.7 / non-Python tools) | `LC_CTYPE=C.UTF-8` / PYTHONIOENCODING; PEP 538 coercion | PEP 538 | strong |
| locale | en_US.UTF-8 | coreutils FAQ: locale collation breaks sort/join/comm pipelines | `LC_ALL=C` for pipeline | gnu.org coreutils FAQ | strong |
| locale | de_DE.UTF-8 | awk honours LC_NUMERIC → "24,0"; jq fails | `LC_NUMERIC=C` | Osmantic/ODS#5648 | strong |
| locale | tr_TR.UTF-8 | Java toUpperCase default locale: i→İ | `Locale.ROOT` | Oracle Java 8 String docs | strong |
| locale | zh_CN.GBK | open() uses locale encoding; 82/4000 top packages fail to install on non-UTF-8 locales (PEP 597) | `encoding="utf-8"`; PYTHONUTF8=1 | PEP 597 | strong |
| locale | cp1252 | same mechanism on Windows code pages (PEP 686) | PYTHONUTF8=1 / explicit encoding | PEP 686, 597 | strong (dup of GBK) |
| tz | Asia/Shanghai | naive datetime assumed local; epoch shifted +8h | aware datetimes, UTC internally | cpython datetime.rst | weak |
| tz | Europe/Berlin | DST: tz_localize raises on nonexistent/ambiguous 02:30 | UTC internally; `nonexistent='shift_forward'`, `ambiguous='infer'` | pandas tz_localize docs | strong |
| tz | Asia/Kolkata | `Math.round(delta/60)` shows 6h for 5.5h | preserve fractional hours / minutes; `±HH:MM` | johnyuencm/Hourbridge#1 | strong |
| clock | future+1y | apt Release "expired"; TLS notAfter fails | NTP; `Acquire::Check-Valid-Until=false`; openssl `-attime` | proxmox forum ; apt.conf(5) ; openssl verification options | strong |
| clock | past-1y | apt "not valid yet"; TLS notBefore fails | sync clock; `Acquire::Check-Date=false` | microsoft/WSL#4114 ; apt.conf(5) | strong (dup sign) |
| clock | frozen | libfaketime: programs waiting for a time never reached hang; `java -version` hangs | `FAKETIME_DONT_FAKE_MONOTONIC=1`; monotonic clocks, event-driven waits | libfaketime README | strong |

合计 52：强 45、弱 6、无 1。建议降为候选：isolation=bare、accel=nvidia、isolation=microvm/vm（合并）、browser-engine=webkit、channel=gui、tz=Asia/Shanghai。重复机制：cp1252≈zh_CN.GBK；past-1y≈future+1y。
