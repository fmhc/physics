# Reproduce the Maxwell positivity problem on V

This small package reconstructs V × Euclidean time and tests two **fixed**
diagonal Hodge stars: the original circumcentric star and the archived searched
power-dual weights. It reproduces a mathematical consistency problem, not a
measurement, a continuum limit, or a new law of nature.

## Run

Python 3.12, NVIDIA GPU with a driver supporting CUDA 12.1, and approximately
1 GiB free device memory are sufficient for this bounded calculation. No private
data, special hostnames, geometry libraries, or historical `.npz` files are needed.

```sh
python3.12 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python reproduce.py --output result.json
```

The final command exits nonzero on any declared mismatch. CUDA is required; there
is no CPU fallback. Pinning covers direct numerical dependencies; the result
records the actual Python, Torch, NumPy, CUDA runtime, GPU and input hashes.
Driver/OS differences can change last digits, so numerical comparisons use the
predeclared tolerances in [PLAN.md](PLAN.md), not byte-identical JSON.

Read [SOURCES.md](SOURCES.md) for derivation provenance and the original script
hash discrepancy. The geometry uses integer coordinates and periodic incidence
on the CPU; Hodge weights, projections and eigensystems run in CUDA float64 and
complex128. The random generator creates the same 96 input momenta as the old
run (seed 99); these are **not unseen validation points**.

## Meaning of the checks

- `d1*d0 = 0` tests the discrete gauge identity. Changing diagonal weights does
  not change this identity.
- `sum_f w_f S_f S_f^T = (tau/4) I` tests constant-field normalization. Passing
  this check does not guarantee a positive quadratic form.
- Negative eigenvalues of `Q† d1† W d1 Q` indicate actual negative quadratic
  directions after removing the gauge subspace, not merely negative entries in W.
- Positivity at 96 momenta is a finite sample, not a proof over the Brillouin zone,
  reflection positivity, uniqueness of the selected weights, a continuum limit,
  or Lorentz invariance.

All weights, momenta and spectral extrema are exported as readable JSON.
The rewrite follows the same source geometry and mathematical construction;
agreement therefore is a software reproduction, **not independent physical
validation**. It does not reproduce the U(1) Monte Carlo, phase transition,
photon dispersion, confinement or SU(2) claims in RESULTS.md.

## Recorded result (2026-10-08)

| Fixed arm | Negative face weights | Negative physical spectra / 96 | Minimum lambda / max(abs(lambda)) |
|---|---:|---:|---:|
| Circumcentric | 99 | 96 | -0.026323642740016386 |
| Archived power dual | 3 | 0 | +0.0022592913672106183 |

The archive reproduction passed all predeclared checks. Constant-field
normalization residuals were at most 1.60e-15 and `max(abs(d1*d0))` was
9.94e-16. The bounded run took 7.46 s on a Quadro P5000; peak allocated CUDA
memory was 123,675,136 bytes. See [result.json](result.json) for all data and
[SOURCES.md](SOURCES.md) for the shared-source limitations.

[Face classification](face-classification.json) shows that the three remaining
negative power-dual triangles all span different integer time layers and different
actual embedding times. Actual time is `tau*(b/10+n_t)`: equal integer layer alone
does not imply a constant-time face. Their temporal support is a warning worth
analyzing, **not by itself a proof that reflection positivity fails**.
The circumcentric case has 12 negative triangles within one integer layer,
but none has all three vertices at the same actual embedding time.

Optional postprocessing and archival integrity checks (no new spectrum calculation):

```sh
python classify_faces.py --input result.json --output face-classification.json
python verify_archive.py
```

The integrity checker uses Python's standard library only. It checks stored
inputs, sample size and declared results, and does not replace rerunning the
CUDA calculation. No continuous integration run or external scientific review
has been performed for this package.
