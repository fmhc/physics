# Independent analytic review: linear Higgs dynamics

Date: 2026-10-08. Analytic review only; no numerical calculation or independent reproduction is claimed.

## Assumptions and exact transformation

All matrices must be expressed in a common orthonormal discretized inner product. Radial integration weights must therefore already be absorbed into the fields. Assume real symmetric A, D and C, with D positive semidefinite and C positive definite. A is the fixed-frequency rotating-frame curvature, **not** the fixed-charge Hessian.

Start from

    q̈ − 2ω ṗ + A q + B h = 0,
    p̈ + 2ω q̇ + D p = 0,
    ḧ + C h + Bᵀ q = 0.

Define P = ṗ + 2ωq. Then Ṗ = −Dp and

    q̈ + (A + 4ω²I)q − 2ωP + Bh = 0,
    P̈ + DP − 2ωDq = 0.

The projection of P onto ker(D) is constant. For oscillatory modes it is zero. If ker(D) is precisely the common phase profile f, fixing this projection is equivalent to fixing the linearized Noether charge: δQ is proportional to ⟨f,P⟩. Any additional exact kernel requires separate interpretation; it must not automatically be called the common phase.

Let R contain orthonormal eigenvectors spanning range(D), with D R = R Λ and Λ > 0. Set T = R sqrt(Λ) and P = T w. The exact symmetric eigenproblem for s = ν² is

    H = [[A + 4ω²I, −2ωT, B],
         [−2ωTᵀ,       Λ, 0],
         [Bᵀ,          0, C]],
    H (q,w,h)ᵀ = s (q,w,h)ᵀ.

Using a full square root of D is equivalent only if its null-space w coordinates are removed; otherwise artificial zero eigenvalues are added. Do not silently clip materially negative eigenvalues of D. This construction requires checking its positivity first.

For ν ≠ 0 and the convention exp(−iνt), reconstruct

    p = (T w − 2ωq)/(−iν).

This reconstructs the original gyroscopic equations and fixes δQ = 0. The pure global phase zero mode q = h = 0, p ∝ f is intentionally absent; it cannot be reconstructed by division by ν at zero frequency. Translational zero modes and possible critical amplitude zero modes require their own interpretation. A nonzero constant kernel component of P describes a charge-changing perturbation, outside this fixed-charge comparison.

At s = 0, eliminating w gives the q-block A + 4ω²Πker(D), rather than A + 4ω²I. This provides a direct consistency check against the previously used fixed-charge Hessian; for a one-dimensional kernel Πker(D) = ffᵀ/⟨f,f⟩.

## Static and leading dynamical Higgs reductions

Exact frequency-dependent Higgs elimination is

    h = −(C − sI)⁻¹ Bᵀq.

The two-block exact Schur pencil is

    [[A + 4ω²I − B(C − sI)⁻¹Bᵀ − sI, −2ωT],
     [−2ωTᵀ,                                  Λ − sI]].

The static approximation uses C⁻¹. Define

    Hred = [[A + 4ω²I − BC⁻¹Bᵀ, −2ωT],
            [−2ωTᵀ,                    Λ]].

The leading dynamical approximation uses

    (C − sI)⁻¹ = C⁻¹ + s C⁻² + O(s²),
    Mred = diag(I + BC⁻²Bᵀ, I),
    Hred z = s Mred z.

Thus the extra inertia has a **positive** sign. The gyroscopic coupling, the definition of P, and the w block do not change at this order. Solve the generalized problem through a symmetric positive-definite mass transformation; do not feed the generally nonsymmetric product Mred⁻¹Hred into a Hermitian eigensolver.

This approximation is only controlled below the Higgs spectral gap. If cmin = λmin(C) and 0 ≤ s < cmin, the omitted q-block has norm at most

    s² ||B||² / [cmin² (cmin − s)].

This is an operator remainder bound, not by itself a bound on individual frequency errors near degeneracies.

## Strong validation identities

The dynamical reduction is exactly Rayleigh–Ritz of H in the subspace h = −C⁻¹Bᵀq. The restricted potential is Hred and the induced mass is Mred. Consequently, if Hred is positive semidefinite and all models use the same symmetry treatment, their ordered low eigenvalues obey

    s_full,k ≤ s_dynamic,k ≤ s_static,k.

This statement compares ordered eigenvalues, not arbitrary modes paired only by their ordinal position across unrelated symmetry sectors. Near degeneracies, compare invariant subspaces or use overlaps.

Because C is positive definite, the Schur complement inertia identity also implies that H and Hred have the same number of negative eigenvalues. A positive mass transformation leaves that number unchanged. Thus full, static and leading-dynamical systems agree on linear instability count under these assumptions. Frequencies and mode shapes can still differ substantially. If a numerical computation violates these statements beyond solver/discretization tolerances, investigate matrices, projections and units before interpreting it physically.

For each computed mode, report residuals and reconstruct h with the exact frequency-dependent inverse. For a reduced mode, the exact residual is

    rq = [A + 4ω²I − sI − B(C − sI)⁻¹Bᵀ]q − 2ωT w,
    rw = (Λ − sI)w − 2ωTᵀq.

The full eigenvector residual and the residual in the original q,p,h equations provide independent algebraic QA. The charge projection must be checked numerically as well.

## Scope of any result

Use the same converged background for the principal full/static/dynamic comparison; otherwise background error is mixed with the reduction error. Report ν as well as ν², remove known symmetry modes by predeclared criteria, and check grid refinement. A frequency-dependent Schur reconstruction is an exact diagnostic, not an independent approximation.

Normal modes test infinitesimal time evolution. Reconstructing a sinusoid from the same eigenvectors is not an independent direct-integration test. A claimed time-domain validation should integrate the coupled linear equations independently or explicitly be described as spectral linear validation.

No result here establishes nonlinear stability, quantum stability, a complete Standard Model Higgs sector, a hadron interpretation, or transfer to a different lattice. A perturbative Higgs effective action must not be used near or above a Higgs resonance merely because its static energy approximation worked well.

## Extension to E3 and Ecomp on their own equilibria

For canonical coordinates (u, z/√2), set J1 = (∂z1/∂u)/√2 and J2 = (∂z2/∂u)/√2. If z1 = O(b) and z2 = O(b²), the consistent kinetic truncation through portal order three is

    M3 = I + J1ᵀJ1 + J1ᵀJ2 + J2ᵀJ1.

For the composite response, its exact induced mass is

    Mcomp = I + (J1 + J2)ᵀ(J1 + J2).

Mcomp is automatically positive definite. M3 is a truncation and must be checked for positive definiteness; loss of positivity means the approximation is unusable in this form, not a newly discovered physical ghost.

At a real rotating-frame background, a Higgs response depending on U(1)-invariant densities has zero first derivative with respect to the imaginary perturbation. Its background time derivative is zero. Therefore its quadratic pullback adds a real-amplitude kinetic term only: there is no added imaginary-field mass or gyroscopic term at this order. The canonical matter rotational coupling remains unchanged. This reasoning presumes the response functional itself is U(1)-invariant.

The same symmetric/generalized construction consequently applies to E3-static, E3-inertia, Ecomp-static and Ecomp-inertia, provided their A and D are derived consistently from each model's own equilibrium and action. Remove the fixed-charge rank correction from any previously stored l = 0 fixed-charge Hessian before using it as A. The transformed dynamics reintroduces charge conservation explicitly.

Comparing these models on their own equilibria is a valid end-to-end test, but combines equilibrium displacement and action truncation error. Do not apply the exact full/static/tangent Ritz ordering to E3 or Ecomp, or to models evaluated on different equilibria.
