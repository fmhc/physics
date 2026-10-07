#!/usr/bin/env python3
"""KUGELSCHALE-1 (Runde 23), Leitung claude-primary, 02.10.2026. Karte: RUNDE-23/kugelschale-1/KARTE.md.

Geodaetische Kugel (Ikosaeder, Frequenz n), Federn k = 1 mit Ruhelaenge 1 (Positionen auf mittlere Kantenlaenge 1
skaliert), Biegeenergie kappa Sum (1 - n1.n2) ueber Nachbardreiecke. Relaxation mit L-BFGS (Gradient per torch-Autograd).
gamma = Y R^2 / kappa_c mit Y = 2/sqrt3, kappa_c = (sqrt3/2) kappa, also gamma = (4/3) R^2 / kappa.
Aufruf: python kugelschale.py <n> <gammas, Komma> <aus.json>
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import json
import math
import sys
import time

import numpy as np
import torch
from scipy.optimize import minimize

torch.set_num_threads(1)
PHI = (1.0 + math.sqrt(5.0)) / 2.0
IKO_V = [(-1, PHI, 0), (1, PHI, 0), (-1, -PHI, 0), (1, -PHI, 0), (0, -1, PHI), (0, 1, PHI), (0, -1, -PHI), (0, 1, -PHI),
         (PHI, 0, -1), (PHI, 0, 1), (-PHI, 0, -1), (-PHI, 0, 1)]
IKO_F = [(0, 11, 5), (0, 5, 1), (0, 1, 7), (0, 7, 10), (0, 10, 11), (1, 5, 9), (5, 11, 4), (11, 10, 2), (10, 7, 6),
         (7, 1, 8), (3, 9, 4), (3, 4, 2), (3, 2, 6), (3, 6, 8), (3, 8, 9), (4, 9, 5), (2, 4, 11), (6, 2, 10), (8, 6, 7),
         (9, 8, 1)]


def geodaetisch(n):
    V = [np.array(v, dtype=np.float64) / np.linalg.norm(v) for v in IKO_V]
    index, pos, tris = {}, [], []

    def vid(p):
        q = p / np.linalg.norm(p)
        key = tuple(np.round(q, 9))
        if key not in index:
            index[key] = len(pos)
            pos.append(q)
        return index[key]

    for a, b, c in IKO_F:
        A, B, C = V[a], V[b], V[c]
        g = {}
        for i in range(n + 1):
            for j in range(n + 1 - i):
                g[(i, j)] = vid(A + (B - A) * i / n + (C - A) * j / n)
        for i in range(n):
            for j in range(n - i):
                tris.append((g[(i, j)], g[(i + 1, j)], g[(i, j + 1)]))
                if i + j <= n - 2:
                    tris.append((g[(i + 1, j)], g[(i + 1, j + 1)], g[(i, j + 1)]))
    pos = np.array(pos)
    # Orientierung nach aussen
    out = []
    for t in tris:
        a, b, c = pos[list(t)]
        if np.dot(np.cross(b - a, c - a), a + b + c) < 0:
            t = (t[0], t[2], t[1])
        out.append(t)
    kanten = sorted({(min(x, y), max(x, y)) for t in out for x, y in ((t[0], t[1]), (t[1], t[2]), (t[2], t[0]))})
    fuenf = [index[tuple(np.round(v, 9))] for v in V]
    return pos, kanten, out, fuenf


def nachbarpaare(dreiecke):
    kz = {}
    for t, (a, b, c) in enumerate(dreiecke):
        for x, y in ((a, b), (b, c), (c, a)):
            kz.setdefault((min(x, y), max(x, y)), []).append(t)
    return [tuple(v) for v in kz.values() if len(v) == 2]


def relax(pos0, kanten, dreiecke, kappa, saat=1, maxiter=60000):
    N = len(pos0)
    E = torch.tensor(kanten, dtype=torch.long)
    T = torch.tensor(dreiecke, dtype=torch.long)
    P = torch.tensor(nachbarpaare(dreiecke), dtype=torch.long)
    rng = np.random.default_rng(saat)
    x0 = pos0 + 1e-3 * rng.standard_normal(pos0.shape)

    def teile(X):
        d = X[E[:, 1]] - X[E[:, 0]]
        es = 0.5 * ((torch.sqrt((d * d).sum(1)) - 1.0) ** 2).sum()
        a, b, c = X[T[:, 0]], X[T[:, 1]], X[T[:, 2]]
        nn = torch.linalg.cross(b - a, c - a)
        nn = nn / torch.sqrt((nn * nn).sum(1, keepdim=True))
        eb = kappa * (1.0 - (nn[P[:, 0]] * nn[P[:, 1]]).sum(1)).sum()
        return es, eb

    def eg(xf):
        X = torch.tensor(xf.reshape(N, 3), dtype=torch.float64, requires_grad=True)
        es, eb = teile(X)
        en = es + eb
        en.backward()
        return float(en.detach()), X.grad.detach().numpy().ravel().copy()

    res = minimize(eg, x0.ravel(), jac=True, method="L-BFGS-B",
                   options=dict(maxiter=maxiter, maxfun=2 * maxiter, gtol=1e-10, ftol=1e-16, maxcor=30))
    X = res.x.reshape(N, 3)
    es, eb = teile(torch.tensor(X, dtype=torch.float64))
    return X, float(es), float(eb), res


def main():
    n = int(sys.argv[1])
    gammas = [float(g) for g in sys.argv[2].split(",")]
    pfad = sys.argv[3]
    t0 = time.time()
    pos, kanten, dreiecke, fuenf = geodaetisch(n)
    L = np.mean([np.linalg.norm(pos[a] - pos[b]) for a, b in kanten])
    pos = pos / L
    R0 = float(np.mean(np.linalg.norm(pos, axis=1)))
    grade = np.zeros(len(pos), int)
    for a, b in kanten:
        grade[a] += 1
        grade[b] += 1
    out = {"n": n, "N": len(pos), "kanten": len(kanten), "dreiecke": len(dreiecke), "R0": R0,
           "grade_hist": {str(k): int((grade == k).sum()) for k in sorted(set(grade.tolist()))},
           "euler_V_minus_E_plus_F": len(pos) - len(kanten) + len(dreiecke), "werte": []}
    for g in gammas:
        kappa = (4.0 / 3.0) * R0 * R0 / g
        X, es, eb, res = relax(pos, kanten, dreiecke, kappa)
        c = X.mean(0)
        r = np.linalg.norm(X - c, axis=1)
        A = float(np.var(r) / np.mean(r) ** 2)
        R = float(np.mean(r))
        g_eff = (4.0 / 3.0) * R * R / kappa
        spitzen = float(np.mean(r[fuenf]) / R)
        out["werte"].append({"gamma_soll": g, "kappa": kappa, "R": R, "gamma_eff": g_eff, "A": A,
                             "spitzen_rel": spitzen, "E_dehn": es, "E_bieg": eb,
                             "anteil_dehn": es / (es + eb) if es + eb > 0 else None,
                             "nit": int(res.nit), "meldung": str(res.message)})
        print(f"  gamma {g:8.1f}: A = {A:.3e}, Spitzen {spitzen:.4f}, Dehnanteil {es / (es + eb):.3f}, nit {res.nit}",
              flush=True)
    out["sek"] = time.time() - t0
    with open(pfad + ".tmp", "w") as fh:
        json.dump(out, fh, indent=1)
    os.replace(pfad + ".tmp", pfad)
    print(f"kugelschale fertig: n = {n}, {out['sek']:.1f} s", flush=True)


if __name__ == "__main__":
    main()
