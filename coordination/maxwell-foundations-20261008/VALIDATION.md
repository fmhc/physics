# Validation and provenance corrections

The holdout run passed its frozen gauge-rank, incidence, eigenvector and Rayleigh-quotient checks on CUDA .69.
The reflection checker passed eight exact integer/rational checks on .69. A separate AI agent reviewed both
implementations and outputs; see REVIEW.md. This is not independent human validation.

Timestamp correction to the previous package: reproducibility/maxwell-v/RUN.md labels the lease interval
18:25:01–18:25:12 as CEST. The host is configured in Etc/UTC, and `journalctl --utc` for unit
codex-maxwell-repro-20261008 confirms that interval is UTC (20:25:01–20:25:12 CEST).
The old record is retained; this note corrects its timezone label. No numerical result, input or duration changes.
The new holdout record uses 18:34:37–18:34:50 UTC (20:34 CEST).

Documentation QA on .69 passed: 14 Markdown files, 218 local targets, zero missing;
systemd invocation 56922a6221e4448e9829afa0a3b09b61, 53 ms. Git whitespace checks passed.
No repository-wide CI or full-zone positivity certificate is claimed.
