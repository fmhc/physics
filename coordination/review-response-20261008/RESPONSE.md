# Response to two user-supplied reviews, 8 October 2026

Both reviews correctly identify the central gap: agreement with an intended continuum theory on a few small meshes
is an implementation consistency check, not a derivation of that theory or a new experimentally tested law.
We accept the priority of reproducibility, Maxwell consistency and separate spacing/volume studies. Additional
precision in the radial Higgs model cannot close the missing V-network, chiral-fermion or SU(3) mechanisms.

The supplied reviews are preserved as [review 1](USER-REVIEW.txt) and [review 2](USER-REVIEW-2.txt).
Their authorship and independent execution have not been established. File and commit counts describe the reviewers'
snapshots, not permanent repository properties. An opinion about the probability of eventual Standard Model recovery
is not a measured probability. Claude received both texts and wrote [a response](CLAUDE-REVIEW.md); this is another
AI review, not external human validation.

## Changes made in response

- A [claims register](../../CLAIMS.md) connects all eight reported findings to implementation/derivation sources,
  the type of error, available convergence evidence and explicit prospective failure tests.
- A [reproduction entry point](../../REPRODUCIBILITY.md) starts with the problematic Maxwell weights on V.
  It does not imply that the entire historical archive has a reproducible environment.
- The README retains the requested percentages but explicitly states that they have no objective denominator or
  calibrated weighting. Documentation changes do not raise these estimates. Replacing 65 with another arbitrary
  number would not solve this methodological criticism.
- RESULTS no longer presents generic Regge convergence as a theorem covering these meshes. Its Q-ball claim is
  limited to unresolved binding in the tested cases. Its dimension-calibration claim distinguishes low
  quadrangulation estimates from the high CDT Hausdorff estimate.
- The current work plan puts Maxwell consistency, reproducibility and convergence before further Higgs precision
  or new speculative particle mechanisms. Completed angular and linear dynamic Higgs checks are distinguished
  from still-open nonlinear evolution.

## Assessment of Claude's response

We retain Claude's response as delivered rather than silently revising another review. Several statements require
qualification before becoming project claims:

1. For fixed, gauge-independent weights, the Abelian identity d1 d0 = 0 protects gauge invariance of the plaquette
   action. This does not establish positivity of d1* W d1 on physical modes, and neither statement establishes
   reflection positivity of the interacting Euclidean measure.
2. Three negative triangle weights by themselves do not prove or disprove reflection positivity. One must specify
   a reflection of the actual staggered tent geometry and analyze the measure or transfer construction. Classifying
   triangles by integer slab labels alone is insufficient: sublattice vertices have different physical times.
   Claude's categorical statement about negative crossing terms is not accepted as a proof for this geometry.
3. The Euclidean Bloch problem has four momentum components. A spatial 24^3 scan alone is not a certificate over
   the full four-dimensional zone. Close to zero momentum, physical massless modes also approach zero; a positive
   uniform gap cannot simply be assumed. A finite scan remains a diagnostic unless supplied with valid bounds
   between sample points and treatment of symmetry modes.
4. The photon data are compatible with masslessness and approximate isotropy at the tested scales, not a proof of
   exact masslessness or isotropy. Likewise, interpreting the SU(2) discrepancy at the second flow reference as a
   lattice artifact is a hypothesis to test by refinement, not a reason to discard that discrepancy.
5. Existing partial environment and provenance records do exist in newer Higgs packets. The reproducibility
   criticism concerns completeness and portability of the reported findings, not the literal absence of every
   environment record or data file.

## Gates for the next research decisions

| Priority | Question | Required evidence before strengthening the claim | Failure consequence |
|---|---|---|---|
| P0 | Can an outsider rerun one finding? | Self-contained inputs, pinned environment, exact command, machine-readable tolerances, recorded run and failure output | Repair packaging or mark result not reproduced; do not change expected values merely to pass |
| P0 | Is the fixed Maxwell prescription consistent? | Gauge identity, independent assembly, fixed-weight holdout modes; ultimately full-zone bounds and a specified reflection analysis | Negative physical mode rejects that prescription's weak-field stability; reweighting creates a new model and test |
| P0 | Does an observable converge? | Independently varied spacing at fixed physical volume and volume at fixed spacing, matched scales, frozen fit windows and controls | Report sensitivity; do not call two nearby numbers a continuum result |
| P1 | Is there a distinctive prediction? | Matched V/control geometries; quantify dispersion/anisotropy versus spacing, identify which physical lattice scale is an assumption, propagate its uncertainty | A disappearing cutoff artifact is a numerical property, not a new measured effect |
| P1 | Is a narrow paper ready? | Portable result plus independent human reproduction; SU(2) scale-choice and finite-volume sensitivity included | Keep the manuscript exploratory; no claim of peer review |

No finite Maxwell rerun resolves the continuum limit, derives the optimized weights from a principle, establishes
SU(3), or produces an experimental prediction. Those remain open. An external reviewer has not been contacted.
