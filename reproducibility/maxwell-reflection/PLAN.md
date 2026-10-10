# Frozen plan: pure Euclidean time reflection of the V tent embedding

Date: 2026-10-08. Frozen before execution of `check_reflection.py`.

Question: Does any map `(x,t) -> (x,2*t0-t)` preserve the vertex set of
the actual 3-spatial-plus-1-Euclidean-time V tent embedding? Spatial positions
are fixed, with equality allowed modulo FCC period translations. This is
not a test of arbitrary combined spatial and temporal transformations.

Input: the ten spatial representatives `pos8` and temporal offsets `b/10`
in `../maxwell/reproduce.py`, function `geometry()` and function `pos()`.
Spatial coordinates are in units of 1/8 of the conventional cell edge.
FCC translations are `(4*(ny+nz),4*(nx+nz),4*(nx+ny))` in these units.

1. Independently reconstruct the ten integer spatial representatives from
   their displayed formulas and verify that all ten are distinct modulo FCC
   translations using an exact divisibility criterion.
2. Write `c=2*t0/tau`. A site of sublattice b has temporal coordinates
   `n+b/10`. Its reflected image lies on the same site iff
   `c-b/5` is an integer. Enumerate the five possible c classes modulo one
   supplied by these ten offsets and find their intersection.
3. Produce the exact b=0 versus b=1 contradiction as a small certificate.
   An empty intersection rules out a simplicial automorphism before any
   simplex matching is necessary. Report the simplex test as not reached,
   never as an executed simplex search.
4. Control: synchronous offsets must admit c=0 at the vertex level. A
   single chosen b must admit its expected reflection planes. These controls
   make no assertion about the simplex connectivity of modified embeddings.

Expected finding from the algebra: no pure time-reflection plane, all five
candidate classes preserve only two of ten spatial sublattices. No floating
point tolerances, random seeds, physics simulation, or fitted parameters.
Acceptance: counts and exact checks above pass. Failed checks invalidate
the implementation certificate and must be reported without changing this plan.

Execution: Python standard library, one CPU core on `.69`, serialized by
`/home/fmh/fmhc-physics-remote/lock-klein-cpu2.lock`. Parent coordinator manages
the concurrent GPU task. Record host, Python version and input hashes.
Do not infer violation of Osterwalder–Schrader positivity, nonunitarity,
failure of all generalized reflections, or failure of a continuum limit.
