# Execution record

- Date: 2026-10-08; host: ubuntu-auto (.69).
- Frozen PLAN SHA-256: d228db507ed9a6472c2e90e05400dabdd06d4e994de214997d17bd4af136ed33.
- Kernel source SHA-256: a05feb97c8f1c8d0b35924fbe92c51f2bbe60130abea2282ec36d10c2ab2f283.
- Systemd unit: codex-maxwell-repro-20261008; invocation 67ccab0e94a44f35a5c064f18e90823a.
- Limits: CPUQuota=100%, MemoryMax=3G, RuntimeMaxSec=900.
- Exclusive shared GPU lock: gauntlet-gpu.lock; lease codex-maxwell-repro,
  identifier cbfed06f, acquired 18:25:01 CEST and released 18:25:12 CEST.
- CUDA device: Quadro P5000. Existing services were not stopped or unloaded.
- One run, no optimization, no retries, all checks passed. Kernel wall time
  7.4635796546936035 seconds; unit CPU time 10.062 seconds (includes Torch import,
  integer geometry and orchestration, not CPU numerical spectrum evaluation).
- The optional face classification was added after the frozen reproduction run
  at the coordinator's request. It is descriptive postprocessing of the same
  fixed negative faces, not an added acceptance gate or new statistical sample.
- Reference public main at task start: d4490d8137b3efc56e116262b8e0bde6565e417d.
  Actual source and input were read from the Precision working tree; file hashes
  are authoritative and are in SOURCES.md and result.json.

The host-specific launch/lease files are intentionally not required by the
portable package. The one-command calculation in README performs the same
numerical work on a suitable CUDA system. The memory number in result.json is
Torch allocated memory, not total NVIDIA context/driver memory or process RAM.

Terminology correction to the frozen plan: “96 projected modes per arm” means
96 momentum-dependent spectral problems per arm. Each gauge-projected matrix
has 136 eigenvalues (146 edges minus gauge rank 10); the code diagonalizes the
full matrix and exports its minimum and largest absolute eigenvalue. It does
not export each individual eigenvalue. The original plan remains unchanged.
