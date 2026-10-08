# Independent code and methods review

Date: 2026-10-08. Files read: PLAN.md, run.py, models.py, AMENDMENT.md and analyse.py in this directory. This is source inspection, not execution, numerical reproduction or inspection of finished numerical outputs. The already frozen REVIEW.md was not changed during this review.

## Verdict

No blocking algebraic or implementation error was found in the inspected construction of the seven linear spectral models. Numerical acceptance still depends on completion of the run and final analysis. In particular, the interpretation of the excluded l = 1 mode is conditional until the cross-grid checks in analyse.py pass.

## Mass whitening and physical reconstruction

The Cholesky implementation is correct. With Mq = L Lᵀ, the two triangular solves form L⁻¹ Kq L⁻ᵀ, the coupling blocks become L⁻¹ times their original values, and physical q is reconstructed by L⁻ᵀ. Thus the ordinary eigenvector orthogonality check in whitened coordinates is the required generalized mass orthogonality check.

The real and imaginary matter blocks use fixed-frequency curvature. The fixed-charge rank term is removed once in models.py for l = 0 and is reintroduced through the conserved-momentum construction, avoiding double counting.

The stabilized physical reconstruction correctly accounts for the fact that run.py's R already contains sqrt(dvals): `nu * R @ (w / dvals)` is the range contribution. The l = 0 kernel contribution uses the actually removed eigenvector. Original matter/Higgs equations, reconstructed momentum and linearized charge are subsequently checked. The signs are consistent with p = i t and exp(−iνt).

The exact frequency-dependent Higgs Schur check uses C − ν²I, as required. It is tested on the full reference eigenmodes, rather than being mislabeled as an additional approximation.

## Seven model definitions

The full, Schur-static and Schur-inertia models share the full equilibrium. `sol = C⁻¹ Bᵀ`, so the expressions A − B sol and I + solᵀ sol are the correct static curvature and induced inertia.

E3 and Ecomp use their respective saved equilibria and consistently derived fixed-frequency curvature and phase blocks. Their Jacobians have the appropriate Higgs canonical normalization 1/sqrt(2). E3 retains J1ᵀJ1 and the two cross terms through portal order three; Ecomp also includes J2ᵀJ2. Positive definiteness is checked before whitening.

The response depends on invariant matter densities. Therefore at the real background its quadratic kinetic pullback modifies real-amplitude inertia only; keeping the canonical matter gyroscopic and imaginary kinetic terms is consistent.

The radial energy-HVP comparison is a useful independent representation check. The tangent JVP compares the assembled Jacobian with an analytic tangent implemented through matrix-vector operations. It does not independently rederive the response approximation, and it tests J1 + J2 rather than the two pieces separately. This is a limitation of the QA description, not a discovered equation error. The angular response derivation relies on the previously archived angular study, as declared in PLAN.md.

## Spectral selection and stability scope

The code computes the complete finite-matrix eigenvalue spectrum, records its minimum and counts eigenvalues below −1e−6. Detailed physical eigenvector residual checks are performed only for the retained low positive modes, not every high-frequency eigenvector. These scopes should be stated separately.

The eight-frequency comparison excludes the first l = 1 eigenvalue provisionally. analyse.py then requires the specified overlap, small squared frequency and fine-grid reduction ratio for every model. This is consistent with the preregistered conditional exclusion. The exclusion is justified only after those checks pass.

Frequency comparisons concern ordered spectra in each fixed angular sector. Matter overlaps are recorded, but no positive overlap gate is imposed. Therefore low overlap at an accidental crossing would prevent a claim of one-to-one eigenvector identity, although the ordered-spectrum comparison remains defined.

Negative counts are counts per radial angular-sector matrix. They do not include the spherical multiplicity 2l + 1. Summing these counts across three discretizations is a bookkeeping total, not the number of distinct physical unstable modes. A zero total is unambiguous evidence of no resolved negative eigenvalues in the inspected sectors and discretizations, subject to the −1e−6 threshold.

The Ritz-order check is correctly restricted to the three models with the same full background. The positive-system premise must remain part of the reported mathematical statement; arbitrary negative eigenvalues would not satisfy the second ordering in the same way. The separate full negative count should be inspected before reporting overall linear stability.

No direct time integration is performed. The result is a linear spectral dynamics calculation, not nonlinear evolution, long-time stability, quantum stability or a particle-mass calculation.

## Resumption and provenance

The resumed calculation preserves the failed attempt and retains the 28 completed spectra instead of repeating them. Its provenance records hashes of the original results, QA, comparisons and provenance. The amended reconstruction changes numerical conditioning without relaxing thresholds or changing the operator being diagonalized.

The first 28 QA entries retain their original reconstruction and do not contain the newly added momentum-reconstruction residual field. Do not claim that this new diagnostic was rerun on all 63 spectra. The original equation residuals remain available for those entries.

The loader checks seven entries per completed stage/angular-sector group and six comparisons, but does not itself assert unique model names or compare the old and new input/model/plan hashes for semantic compatibility. For final archive validation, check that the expected 63 `(stage, ell, method)` keys and corresponding QA keys occur exactly once, that there are 54 expected comparison keys, and that archived input, models.py and PLAN.md hashes agree across attempts. The changed run.py hash and added amendment are expected. This validation is an integrity check, not another physics calculation.

STATUS.json `complete = true` means the numerical loops completed. The separate analysis must pass translation validation and expose the frequency, drift and negativity decision results before the experiment is described as accepted. The final elapsed_seconds refers to the resumed process; it is not total wall time including the initial attempt.

## Required final reporting distinctions

- State which decision gates passed and which failed; numerical completion alone is insufficient.
- Identify the 28 retained and 35 amended-reconstruction spectra and preserve the initial QA failure.
- Separate complete-spectrum negative-eigenvalue screening from low-mode residual validation.
- Describe the calculation as fixed-charge linear spectral dynamics in l = 0, 1, 2 at one parameter point and three discretizations.
- Do not infer success for other parameters, nonlinear evolution, quantum corrections or the V lattice.
