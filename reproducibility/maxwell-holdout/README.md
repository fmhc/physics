# New-momentum test of the fixed Maxwell weights

The archived power-dual weights have no negative projected quadratic direction
at these **304 new momentum evaluations**. The circumcentric weights have a
negative direction at all 304. This strengthens a finite-sample observation;
it does not resolve positivity throughout the Brillouin zone.

| Fixed weights | New random points | Ray evaluations | Negative / positive / unresolved |
|---|---:|---:|---:|
| Circumcentric | 256 | 48 | 304 / 0 / 0 |
| Archived power dual | 256 | 48 | 0 / 304 / 0 |

The 48 ray evaluations include q and -q pairs; they are not 48 statistically
independent tests. No weight was refitted. New random seed: 20261008. The
[plan](PLAN.md) and source were frozen before execution. Input SHA-256 hashes
are checked before importing the sibling geometry or reading its weights.

![Small-q diagnostic](small-q.svg)

The circumcentric minimum remains approximately -0.5950 near q=0. The
power-dual minimum softens approximately quadratically on these rays and stays
resolved positive: the smallest relative eigenvalue is 1.1770e-9, above the
predeclared 1e-10 threshold. This is an eigenvalue of the edge-coordinate
Euclidean quadratic form. Bloch phases use reciprocal primitive coordinates;
their norm is not calibrated physical momentum. The plot is **not photon
dispersion**, evidence for Lorentz invariance or a continuum-limit study.

All numerical gates passed. Lowest-mode normalized eigen residuals were below
1.49e-15. The smallest singular-value ratio of d0 was 1.1446e-4, far above
the 1e-10 rank threshold; rank was 10 throughout. Post hoc q/-q comparison
found identical stored minimum eigenvalues for all sign pairs. That comparison
was a diagnostic, not an additional acceptance gate.

## Reproduce

From this directory in the public checkout, using Python 3.12 and a suitable
CUDA GPU:

```sh
python3.12 -m venv .venv
. .venv/bin/activate
pip install -r ../maxwell-v/requirements.txt
python run.py --output result.json
```

The sibling [maxwell-v package](../maxwell-v/README.md) contains the immutable
inputs. `--base /path/to/maxwell-v` overrides their location. The numerical
calculation has no plotting dependency. Optional `plot.py` uses Matplotlib
to regenerate the figure and descriptive [postprocess.json](postprocess.json),
without recomputing any spectrum.

Raw results and complete metadata: [result.json](result.json).
Execution details: [RUN.md](RUN.md). This extends the previous software
reproduction using its geometry and weights. It is not independent physical
validation or an external human review. General positivity, reflection
positivity, uniqueness of the selected Hodge star, controlled refinement and
a network-specific prediction remain open.
