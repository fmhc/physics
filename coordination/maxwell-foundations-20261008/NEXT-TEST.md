# Next mathematical gate after the finite Maxwell scan

This is a proposal, not an executed calculation or a frozen numerical run plan.
The present follow-ups test fixed weights on new momenta and one explicitly defined reflection. Neither certifies
whole-zone positivity or a unitary continuum theory.

## Positivity certificate rather than another arbitrary sample

The Euclidean operator is K(q) = d1(q)^* W d1(q) on edge cochains, with four dimensionless primitive-cell Bloch
phases, each defined modulo 2 pi. Its kernel includes gauge directions im d0(q). At the origin on this Bloch torus,
the gauge rank and harmonic content change. Other possible physical zero modes must be investigated rather than
excluded by assumption.
A uniform positive gap on all physical modes is therefore not the appropriate target for a massless theory.

A rigorous next approach would separate a neighborhood of q = 0 from the remaining compact zone:

1. Away from zero, derive certified bounds for the operator variation and physical-subspace handling, then cover
   cells with intervals small enough that a positive lower eigenvalue bound survives. A dense grid without an
   inter-point bound does not suffice. Projection derivatives and changes in basis cannot be ignored.
   One alternative avoids a moving projection: with fixed alpha > 0, study the full edge-space matrix
   H(q) = K(q) + alpha d0(q) d0(q)^*. Where d0 has full column rank, the exact chain identity makes gauge and
   orthogonal physical blocks decouple. The gauge block is positive, so H is positive exactly when K is positive
   on the physical complement. This is an algebraic route to a bound, not an already computed certificate.
2. Near zero, identify the harmonic/acoustic and gapped sectors, eliminate the gapped sector with a controlled
   Schur complement, and bound the higher-order remainder of the small-q expansion in every direction.
   Constant-field normalization alone is not this bound.
3. A negative Rayleigh quotient of a verified physical vector at even one q is a counterexample to positivity.
   Preserve that vector, q, residuals and weights. A new weight search would define a new test, not repair the
   original result retroactively.

The matrix geometry, all four phases, coordinate conventions, tolerances and any candidate certificate must be
reviewed before allocating a large scan. No such certificate is claimed here.
Archived weights are floating approximations. A proof must specify whether their decimal values define the model
or whether it certifies exact geometric weights enclosed in intervals; coefficient rounding and geometry errors
must be included in the latter case.

## Time reconstruction

Failure of pure (x,t) -> (x,2t0-t) symmetry of a staggered embedding does not by itself exclude a combined spatial
and temporal symmetry, a different admissible time slicing, a block transfer construction, or a suitable continuum
limit. Each alternative changes the question and needs its own explicit action, field map and proof obligations.
The sign of three local weights cannot settle these alternatives.

## Physics, after consistency

A spacing study must distinguish a regulator from an assumed physical lattice. At fixed physical box size and
matched parameters, varying a checks discretization dependence. At fixed a, varying the box checks finite-volume
sensitivity. Dimensionless small-q softening of a Euclidean quadratic form is neither this two-parameter limit nor
a real-time photon-dispersion measurement. A physical prediction also needs a specified physical scale and an
observable that can be compared with data.
