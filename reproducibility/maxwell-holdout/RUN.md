# Execution record

- One run, 2026-10-08 18:34:37–18:34:50 UTC, host ubuntu-auto (.69).
  Host timezone verified as Etc/UTC; this is 20:34:37–20:34:50 CEST.
- Unit codex-maxwell-holdout-20261008; invocation
  5911676566ce4cf59e2023876d774293.
- CPUQuota 100%, MemoryMax 3G, RuntimeMaxSec 900; shared exclusive
  gauntlet-gpu.lock and lease codex-maxwell-holdout f2277267, released normally.
- Quadro P5000, Torch 2.5.1+cu121, CUDA 12.1, Python 3.12.3, NumPy 2.4.4.
- CUDA spectral computation 10.2296 s, peak Torch allocated memory 15,357,952
  bytes. This memory excludes driver/context and other services.
- Unit CPU time 13.038 s includes imports, integer geometry, PRNG, IO and
  orchestration. No CPU eigensystem fallback. Existing services left running.
- Final frozen plan SHA-256:
  5d69344d85ed1db03c3d869969e34de463eefd745a7771e77c85c565e914d9a3.
- Executed source SHA-256:
  3f0a87e20a570b7eacffc748174dcd43d8957127f347f02afb774ec5b7c9ef6e.
- Before launch, the default sibling directory name was corrected from
  maxwell to maxwell-v in source and plan. No numerical method, gate or sample
  changed; the final hashes were announced on the coordination bus before run.
- Host launch passed `--base ../maxwell-repro-20261008`; the published default
  is the corresponding sibling maxwell-v. Exact input hashes were verified.
- Source plan reviewed before execution by a separate Codex agent. This is
  software/method checking, not independent human scientific validation.
- Postprocessing on .69 under the small-CPU lock, CPUQuota 100%, MemoryMax
  1G, RuntimeMaxSec 60; unit codex-maxwell-holdout-plot-20261008, successful.
  Plot CPU rendering and scalar JSON summaries are descriptive only. SVG
  trailing whitespace was trimmed for repository hygiene.
- No optimization, retry or additional spectrum run was performed.
