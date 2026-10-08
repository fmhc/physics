# Frozen bounded reproduction plan — 2026-10-08

Question: does the signed circumcentric diagonal Maxwell Hodge star on V × time
have negative physical quadratic modes, and does the archived power-dual choice
remove them at the *same previously tested* 96 momenta?

No parameter search, continuum extrapolation, new prediction, or Monte Carlo.
Spatial dimension 3, Euclidean time dimension 1; 10 vertex sublattices. Primitive
fcc conventional cubic edge is 1. Fix tau and both omega choices to archive/gwp.json.
Fix NumPy default_rng(99), uniform [-pi,pi]^4, 96 momenta, matching the archive.
This is a reproduction sample, not an independent holdout.

Translate the source geometry construction using exact integer coordinates.
Compute signed dual areas, constant-field normalization, d1*d0, gauge-complement
projection and Hermitian eigenvalues in float64/complex128 on CUDA .69. CPU only
handles exact integer combinatorics, deterministic random input generation and IO.

Predeclared checks: V counts (10 vertices,146 edges,484 faces,232 4-simplices);
normalization and d1*d0 <1e-10; relative minimum eigenvalue agrees with archived
value to absolute 1e-8; negative face and negative momentum counts match archive;
96 projected modes computed per arm. Also expose negative-face counts at 1e-12
relative threshold to distinguish numerical zeros. Save all weights, momenta and
per-momentum eigenvalue extrema. Failure exits nonzero, with output preserved.

Budget: one P5000, <3 GiB process RAM, one CPU thread, 900 s; shared GPU lock and
lease. No CPU fallback. No changes to historical records. Independent software
rewrite from common geometry/source is not an independent scientific validation.
