# MAXWELL-HOLDOUT-1 — frozen before execution

2026-10-08. Test the two fixed weight vectors from the Maxwell reproduction
without optimization or adjustment after looking at results. This is a new
finite momentum sample on the same V × Euclidean-time cell, not a continuum
limit or an independent geometry construction.

Inputs: sibling `maxwell-v/reproduce.py` (SHA-256
`a05feb97c8f1c8d0b35924fbe92c51f2bbe60130abea2282ec36d10c2ab2f283`),
`maxwell-v/result.json` (`153a695ff94816ce1597cf83b45bb4fef668a0133d3851434c8db3ef5b166222`),
and `maxwell-v/archive/gwp.json` (`a91fdfd0c86026d0f211dd8f1bb6812db966007f87bbd84d66cc67da16f6fa35`).
The readable result contains all fixed face weights in the sorted face order.

Sample: 256 NumPy default_rng(20261008) momenta uniform in [-pi,pi]^4,
then positive and negative rays along the four coordinate axes, (1,1,1,1),
and (1,1,1,0), each normalized to Euclidean coordinate norm 1, .1, .01,
.001. Total 304 points, including 48 deterministic ray points. Coordinates
are reciprocal primitive-cell Bloch phases, not orthonormal physical momentum.
No q=0 point is used because its gauge rank changes.

For each point, construct d0 and d1 from immutable geometry; remove the range
of d0 by full SVD with rank threshold 1e-10 times largest singular value.
Diagonalize Hermitian Q†d1†Wd1Q in CUDA complex128 for each arm.
Export the five lowest eigenvalues, largest absolute eigenvalue, gauge rank,
and lowest-mode normalized residual and Rayleigh discrepancy.

Numerical gates: counts (10,146,484,232), rank 10 everywhere,
max(abs(d1*d0)) < 1e-10; lowest-mode normalized eigen residual < 1e-10,
Rayleigh discrepancy < 1e-10. Normalize residuals and classifications by
max(abs(eigenvalues)). A point is negative below -1e-10, positive above
+1e-10, otherwise unresolved at this tolerance. Do not count numerical
zero as a negative or a positive result. Gates test numerical quality;
finding a negative power-dual direction is a scientific finding, not a reason
to rerun or alter weights. Repeated momenta against the old 96-point sample
are checked and forbidden.

Resource bounds: one CUDA run on .69 under the shared GPU lock and lease,
CPUQuota 100%, MemoryMax 3G, RuntimeMaxSec 900. CPU integer geometry, input
PRNG, IO and plotting; all spectral work CUDA. No CPU fallback.

Interpretation: new points strengthen or refute only finite-sample evidence.
No Brillouin-zone proof, reflection-positivity verdict, continuum/infinite-volume
limit, Lorentz-invariance result, physical photon dispersion or new prediction.
Small-q rays are a diagnostic of eigenvalue softening in the edge-coordinate
quadratic form; without a physical kinetic normalization they are not energies.
