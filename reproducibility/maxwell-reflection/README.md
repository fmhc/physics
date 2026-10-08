# Exact obstruction to pure time reflection in the current V embedding

**Result:** The chosen staggered tent embedding `t=tau*(m+b/10)` has no reflection plane for
`(x,t) -> (x,2*t0-t)` with spatial positions fixed. This is a statement about
the embedded vertex set in **three spatial dimensions plus Euclidean time**,
not a proof of nonunitarity or a general failure of reflection positivity.

The [frozen plan](PLAN.md), [standard-library checker](check_reflection.py),
and [exact result](result.json) form a small reproducible certificate.

## Proof and numerical independence

Write the vertices as

\[
x=s_b+A n,\qquad t/\tau=m+b/10,
\quad b=0,\ldots,9,\quad n\in\mathbb Z^3,\quad m\in\mathbb Z.
\]

Here `8*s_b` are the ten integer representatives in the result file and
`8*A*n=(4*(n_y+n_z),4*(n_x+n_z),4*(n_x+n_y))`.
For a difference `(d_x,d_y,d_z)` in these integer coordinates, two
representatives occupy the same FCC spatial coset exactly when all three
integers `-d_x+d_y+d_z`, `d_x-d_y+d_z`, `d_x+d_y-d_z` are divisible by eight.
The ten cosets are distinct. Therefore a reflection that fixes space cannot
change b, even when spatial equality is taken modulo FCC period translations.

Let `c=2*t0/tau`. The reflected temporal coordinate can belong to the same
spatial sublattice only if

\[
c-m-b/10=m'+b/10,
\qquad\text{equivalently}\qquad c-b/5\in\mathbb Z.
\]

Sublattice `b=0` requires `c=0 mod 1`; sublattice `b=1` requires
`c=1/5 mod 1`. These conditions cannot hold simultaneously. Thus no such
reflection preserves the vertex set, and consequently none is an
automorphism of its simplicial complex. **No simplex enumeration was needed
or performed.** This argument holds for every positive tau and is independent
of Maxwell weights, coupling constants, and floating point tolerances.

The five candidate plane classes, modulo `tau/2`, are:

| t0/tau | Sublattices preserved |
| --- | --- |
| 0 | 0, 5 |
| 1/10 | 1, 6 |
| 1/5 | 2, 7 |
| 3/10 | 3, 8 |
| 2/5 | 4, 9 |

Each preserves only two of ten spatial sublattices. Synchronous offsets and
individual sublattices pass the control checks at the vertex level; this
does not certify the simplex connectivity of a modified synchronous model.

## Reproduce

No dependencies beyond Python's standard library. Validated with Python 3.12.3:

```sh
python3 check_reflection.py --output result-local.json
```

Expected: `passed: true`, eight true checks, and `valid_c_classes: []`.
The archived execution ran on `ubuntu-auto` (`.69`) at
`2026-10-08T18:33:45Z`, using one CPU process and exact integer/rational
arithmetic, under the shared small-CPU lock with a 30-second limit. No CUDA,
simulation, random sampling, optimization, or external data were needed.
Output records the hashes of the executed script and pre-existing plan.

Geometry formulas were independently transcribed from
[`../maxwell-v/reproduce.py`](../maxwell-v/reproduce.py), functions `geometry()`
and `pos()`, with source SHA-256
`a05feb97c8f1c8d0b35924fbe92c51f2bbe60130abea2282ec36d10c2ab2f283`.
The frozen plan and script comment used `../maxwell/` as a provisional package
name; the published sibling is `../maxwell-v/`. No runtime dependency on that
path exists. The source hash was recorded after execution; the executed
checker does not load or automatically compare the source implementation.
Its ten representatives were reviewed against the source formulas.
This is an independently written algebraic check of the specified embedding;
it is not an independent human validation of the original geometry.

## What follows, and what does not

A conventional pure-time reflection argument cannot simply assume that this
particular embedded triangulation is invariant. That missing hypothesis must
be addressed explicitly before using such an argument for the Maxwell model.
Searching for positive Bloch eigenvalues does not supply that geometric
hypothesis.

This check does **not** test Osterwalder–Schrader inequalities, a transfer
matrix, combined spatial/time transformations, a changed foliation, a
different triangulation, or continuum restoration of a symmetry. It does
not exclude those routes. Integer FCC translations cannot repair this
particular obstruction because they retain b; transformations that permute
spatial sublattices pose a different question. There is no claim here about
one- or two-dimensional models, Lorentzian time, physical time-reversal
symmetry, or experimental predictions.

The next specific mathematical task is to define a candidate reflection or
transfer construction for the actual action and test its assumptions. This
vertex certificate narrows that task; it does not solve it.
