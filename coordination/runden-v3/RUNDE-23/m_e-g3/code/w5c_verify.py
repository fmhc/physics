# W5c-Nachpruefung mit feiner Quadratur: Positivitaet eines B2/B3-Funktionals (psi2, psi3 aus einer LP-Ausgabe)
# auf schweren Zustaenden bei grossem J. Gauss-Legendre exakt bis Polynomgrad 2*NP-1; der Integrand hat Grad ~2J+deg(psi).
# Aufruf: w5c_verify.py <lp-ausgabe.out> <jmax> [NP]
import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
import sys
import json
import time
import numpy as np
from numpy.polynomial import polynomial as npp
from scipy.special import roots_legendre

T0 = time.time()
txt = open(sys.argv[1]).read()
js = json.loads(txt[txt.index("{"): txt.rindex("}") + 1])
psi2 = np.array(js["psi2"])
psi3 = np.array(js["psi3"])
q = float(js.get("q", 1.0))
jmax = int(sys.argv[2])
NP = int(sys.argv[3]) if len(sys.argv) > 3 else 2 * jmax + 200
x0, w0 = roots_legendre(NP)
p = 0.5 * q * (x0 + 1.0)
w = 0.5 * q * w0
v2 = npp.polyval(p, psi2)
v3 = npp.polyval(p, psi3)


def legendre_rows(x, jmax):
    a = np.ones_like(x)
    b = x.copy()
    yield 0, a
    yield 1, b
    for n in range(1, jmax):
        a, b = b, ((2 * n + 1) * x * b - n * a) / (n + 1)
        yield n + 1, b


def jacobi08_rows(x, jmax, al=0.0, be=8.0):
    nmax = jmax - 4
    a = np.ones_like(x)
    b = (al + 1.0) + (al + be + 2.0) * (x - 1.0) / 2.0
    yield 4, a
    if nmax >= 1:
        yield 5, b
    for n in range(2, nmax + 1):
        s = 2 * n + al + be
        a1 = 2 * n * (n + al + be) * (s - 2)
        a2 = (s - 1) * (al * al - be * be)
        a3 = (s - 2) * (s - 1) * s
        a4 = 2 * (n + al - 1) * (n + be - 1) * s
        a, b = b, ((a2 + a3 * x) * b - a4 * a) / a1
        yield n + 4, b


out = {"datei": sys.argv[1], "q": q, "jmax": jmax, "NP": NP, "m": {}}
worst = (np.inf, None)
MLIST = (1.0, 1.0 + 1e-6, 1.0 + 1e-4, 1.001, 1.01, 1.05, 1.1, 1.2, 1.3, 1.5, 2.0, 3.0, 5.0)
if len(sys.argv) > 4 and sys.argv[4] == "grossm":
    MLIST = (5.0, 7.0, 10.0, 15.0, 20.0, 30.0, 40.0, 60.0)
for m in MLIST:
    x = 1.0 - 2.0 * p * p / (m * m)
    bpp = w * (v2 * (2 * m * m - p * p) + v3)
    bpm = w * (v2 * (2 * m * m - p * p) - v3)
    res = {}
    for kind, gen, base in (("pp", legendre_rows(x, jmax), bpp), ("pm", jacobi08_rows(x, jmax), bpm)):
        mn = (np.inf, None, None)
        for J, d in gen:
            if kind == "pp" and J % 2 == 1:
                continue
            f = float(d @ base)
            sc = float(np.abs(d) @ np.abs(base)) + 1e-300
            r = f / sc
            if r < mn[0]:
                mn = (r, J, f)
        res[kind] = mn
        if mn[0] < worst[0]:
            worst = (mn[0], (m, kind, mn[1], mn[2]))
    out["m"]["%.6f" % m] = res
out["schlimmster_fall"] = worst
out["sekunden"] = time.time() - T0
print(json.dumps(out, indent=1, default=float))
