Q-BALL QUANTIZATION — ENGLISH WORKING DRAFT v0.1

This folder contains a NEW English paper on canonical quantization of the
sextic scalar Q-ball sector. It is not a translation or replacement of the
coordinator's full particle-model manuscript or the existing BIC ladder paper.
Human authorship remains undecided.

main.tex: manuscript source.
paper.pdf: final compiled five-page manuscript for this v0.1 handover.
paper.html: standalone HTML with MathML, derived from the same source.
build-remote.sh: reproducible build using the previously installed remote tools.
qa/: final LaTeX log, PDF metadata/text and rendered pages, source/output hashes.

What has been done:
- Explicit finite-lattice quantum Hamiltonian and exact integer U(1) sectors.
- Collective-phase quantization and q=zeta n matching to classical profiles.
- Canonical rotating-frame fluctuation Hamiltonian and zero-mode constraints.
- Correlator/Wick controls and distinction between branch and ground-sector energy.
- Spatial dimension and EFT/renormalization boundaries.

What has NOT been computed:
Quantum masses, n=2/3 binding, the one-loop correction, real-time quantum
lifetimes, quantization of evolving Regge geometry or Standard Model identities.
Claude's concurrent QUANT-1 HMC task owns the new numerical spectrum effort.
No duplicate HMC or physics run has been started by this author.

Independent limited paper-algebra review:
coordination/resonance-20260930/ag-phy-lat-quantisierung-20261005/REVIEW.txt
One substantive scope issue (stationary branch energy versus lowest sector
energy) was corrected and specifically reread. Literature was not independently
reviewed again. Later changes only replace TeX roman-font syntax for MathML
compatibility and move a long inline formula into display; no algebra change.

Build location: ubuntu-auto / 192.168.178.69, CPU11 nice19, existing shared
lock-klein-cpu11.lock with wait45s; each build timeout60s. No GPU, physics,
local interpreter/compiler/tests, persistent service or dependency installation.
Remote folder /home/fmh/fmhc-physics-remote/qball-quantization-20261005-en-codex/.
A first build exposed one overfull paragraph and legacy TeX syntax unsupported
by Pandoc MathML; both were corrected before final delivery.

Inputs/coordination:
coordination/resonance-20260930/ag-phy-lat-quantisierung-20261005/.
Primary literature links and exact reading depth are in the manuscript.
