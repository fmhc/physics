# Source provenance

The fixed historical input is `archive/gwp.json`, copied verbatim from
`coordination/runden-v3/RUNDE-37/quant-2/lauf-69/gwp.json`. Historical run:
2026-10-05T16:37:32Z, Python 3.12.3, NumPy 2.4.4. It is a comparison target,
not independently verified evidence.

The compact implementation translates these source algorithms at their observed
SHA-256 (paths relative to `coordination/runden-v3/RUNDE-37/quant-2/code/`):

| File | SHA-256 | Use |
|---|---|---|
| ew.py | fa7b6417d39177102f0b19c5474453cd16a7595e23bc25ca548e081c4060b142 | V integer geometry, hexagon cycles |
| tp.py | 419d7da6caa211c721eb6a8c87403977415cf3050f03365377f51cb77b374dfd | primitive lattice and vertex coordinates |
| rk.py | afd778897795839f84695db580e401507b5d9ba00266913bd23b8ad6fecac17f | periodic equivalence, edge orientation, tent lifting |
| rk2.py | eb361e43564a2aa76a3109f88df44485cacd068cc293c891d1c3d1a2059cff81 | sublattice lift order |
| gw.py | b818a7406c1eb85bbff52e115f56a96c358f174cf352d5f13d2610753c00b46e | signed orthogonal dual, Bloch gauge complement |
| gwp.py | a999596f73e8ef998ef7f900f4af49392e69cf3c198b1b3afba00f0376d4d9b5 | archived fixed input evaluation |

The current gwp.py hash differs from the script hash recorded in the old result;
this package preserves that distinction and does not rewrite its provenance.
No unpublished npz/npy inputs or host-specific geometry imports are required.
