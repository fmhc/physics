# Separate code and mathematical review

2026-10-08. Reviewed by a separate Codex agent, not an external human reviewer.
Scope: the frozen Maxwell holdout plan/code/result and descriptive summary,
the exact time-reflection plan/code/result, and the proposed next mathematical
gate. No numerical tests
were executed by this reviewer. This review does not independently reconstruct
the entire V geometry or prove continuum physics.

## Gauge projection and small momenta

The holdout code constructs the incidence matrices in the established sorted
face order and reads the two immutable weight vectors from the reproduced
archive. Its full SVD of d0 removes its column space; the resulting quadratic
matrix is Hermitianized before diagonalization. The gauge identity d1*d0=0,
rank, eigenvector residual and Rayleigh quotient are explicitly checked.

The main hazard at small momentum is the change in gauge rank at the origin.
The plan excludes zero, stops at coordinate norm 0.001, requires rank ten at
every point, and exports the smallest/largest singular-value ratio. This
addresses accidental retention of a nearly gauge direction, subject to the
recorded ratios being comfortably above the 1e-10 rank threshold. At exactly
zero, constant scalar gauge transformations disappear from the image of d0
and harmonic one-form modes require a different analysis. The present code
does not claim to perform that analysis.

The 1e-10 classification band correctly treats numerically tiny eigenvalues
as unresolved rather than assigning a sign. A positive finite sample cannot
certify the intervening momenta. The 48 deterministic ray evaluations include
opposite-sign pairs and must not be described as independent random samples.
The coordinate eigenvalues use the unweighted edge-coordinate metric; they
are not physical photon energies or a measured dispersion relation.

The recorded run passed its five numerical gates. Its smallest d0 singular
ratio is 0.0001144596892699107, comfortably above the rank threshold. The
power-dual arm has 304 positive classifications, with minimum relative
eigenvalue 1.177005914520586e-9, above the declared 1e-10 sign threshold.
The circumcentric arm has 304 negative classifications. The largest stored
lowest-mode eigen residual is 1.4824006096563115e-15. The separately reported
post hoc sign-pair diagnostic agrees for all q/-q minima; it was correctly
kept separate from the frozen acceptance criteria.

The ray summaries support the narrowly worded observations: the circumcentric
minimum stays near -0.595 as q decreases, whereas the power-dual minimum
softens approximately as q squared along the sampled rays. No limit or
physical dispersion is thereby demonstrated. No numerical rerun was needed
for this review.

## Pure time reflection

The exact argument is valid for the specified embedding
`t/tau = m + b/10`. The spatial representatives occupy distinct FCC cosets,
so a map fixing space cannot change b. Writing `c=2*t0/tau`, vertex invariance
requires `c-b/5` to be an integer for every b. The b=0 and b=1 requirements
already contradict each other. Enumeration of five candidate classes is
exhaustive because each individual sublattice restricts c modulo one to its
own class.

The stored result passes the eight declared exact checks. Failure at the
vertex level suffices; the report correctly says simplex matching was not
performed. This is a restriction on the chosen staggered time embedding, not
a general obstruction of the spatial network V. It is not an evaluation of
Osterwalder–Schrader inequalities or a proof of nonunitarity. Combined spatial
and temporal maps, other time slicings and continuum restoration remain open.

The checker transcribes the source formulas rather than importing and checking
them at runtime. Its README explicitly discloses that the source hash was
recorded after execution. Inspection of the displayed representatives agrees
with the source formulas; this is a limited software/algebra review.

## Next mathematical gate

Separating a neighborhood of the Bloch-torus origin from its complement is
appropriate for a massless problem. A finite grid is insufficient without
bounds between sample points, and the absence of additional zero modes must
be established rather than assumed. The origin means q=0 modulo 2*pi.

One useful simplification away from the origin is to bound the full matrix

`H(q) = d1(q)* W d1(q) + alpha d0(q) d0(q)*`, with fixed `alpha > 0`.

When d0 has full column rank and d1*d0=0, the gauge and orthogonal physical
subspaces are invariant. The added term is positive definite on the gauge
subspace and zero on its orthogonal complement. Thus H is positive definite
exactly when the physical block is positive definite. This offers a fixed
matrix of trigonometric polynomials for interval bounds and avoids derivatives
of a numerically selected SVD basis. It does not remove the need for a separate
small-q treatment or establish a physical gauge-fixing prescription.

A rigorous future certificate must also identify its coefficient target:
the recorded decimal weights as exact model inputs, or intervals enclosing
the geometric Hodge weights before floating-point rounding. Ordinary float64
eigenvalues alone are not a rigorous lower bound.

No blocker was found in the reviewed mathematical argument or implementation
plan. This statement is limited to their explicitly declared scope; it is not
a positivity certificate or physical validation.
