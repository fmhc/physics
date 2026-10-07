#!/usr/bin/env python3
"""TETRA-KLUMPEN (Runde 17), Leitung claude-primary, 02.10.2026. Karte: RUNDE-17.md, Abschnitt TETRA-KLUMPEN.

Lennard-Jones-Grundzustaende (Basin-Hopping, mit Koordinaten), Kontaktgraph, Tetraeder (4er-Cliquen),
Frustrationsenergie der Kontakte als Federn mit Ruhelaenge 1. Kernfunktionen aus stabil.py (STABIL-6-8-12).
Aufruf (kleintest.sh, .69): python tetraklumpen.py <seed> <Nmin> <Nmax> <schritte> <aus.json>
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import itertools
import json
import sys
import time

import numpy as np
from scipy.optimize import minimize

from stabil import lj_binden, lj_eg, lj_lokal

RC = 1.2 * 2 ** (1 / 6)


def lj_bh_x(N, rng, schritte, T=0.8, schritt=0.36):
    R0 = 0.6 * N ** (1 / 3) + 0.4
    x, e = lj_lokal(rng.uniform(-R0, R0, size=3 * N))
    x = lj_binden(x, rng)
    e = lj_eg(x)[0]
    xb, eb = x.copy(), e
    for _ in range(schritte):
        y, _ = lj_lokal(x + rng.uniform(-schritt, schritt, size=x.shape))
        y = lj_binden(y, rng)
        ey = lj_eg(y)[0]
        if ey < e or rng.random() < np.exp(-(ey - e) / T):
            x, e = y, ey
        if ey < eb - 1e-9:
            xb, eb = y.copy(), ey
    return eb, xb.reshape(N, 3)


def kontakte(X):
    D = np.linalg.norm(X[:, None] - X[None], axis=2)
    n = len(X)
    return [(i, j) for i in range(n) for j in range(i + 1, n) if D[i, j] < RC]


def tetraeder(n, kanten):
    adj = [set() for _ in range(n)]
    for i, j in kanten:
        adj[i].add(j)
        adj[j].add(i)
    out = []
    for a, b, c, d in itertools.combinations(range(n), 4):
        if b in adj[a] and c in adj[a] and d in adj[a] and c in adj[b] and d in adj[b] and d in adj[c]:
            out.append((a, b, c, d))
    return out


def frustration(X, kanten):
    E = np.array(kanten)
    L0 = np.mean([np.linalg.norm(X[i] - X[j]) for i, j in kanten])
    y0 = (X / L0).ravel()

    def eg(y):
        Y = y.reshape(-1, 3)
        d = Y[E[:, 0]] - Y[E[:, 1]]
        L = np.linalg.norm(d, axis=1)
        g = ((L - 1) / L)[:, None] * d
        G = np.zeros_like(Y)
        np.add.at(G, E[:, 0], g)
        np.add.at(G, E[:, 1], -g)
        return 0.5 * float(np.sum((L - 1) ** 2)), G.ravel()

    res = minimize(eg, y0, jac=True, method="L-BFGS-B", options=dict(maxiter=50000, gtol=1e-13, ftol=1e-18))
    Y = res.x.reshape(-1, 3)
    L = np.linalg.norm(Y[E[:, 0]] - Y[E[:, 1]], axis=1)
    return float(res.fun), L


def main(seed, nmin, nmax, schritte, pfad):
    rng = np.random.default_rng(seed)
    aus = {"seed": seed, "schritte": schritte, "rc": RC, "N": {}}
    for N in range(nmin, nmax + 1):
        t0 = time.time()
        e, X = lj_bh_x(N, rng, schritte)
        k = kontakte(X)
        tet = tetraeder(N, k)
        grad = np.zeros(N, int)
        for i, j in k:
            grad[i] += 1
            grad[j] += 1
        abgedeckt = sorted(set(v for t in tet for v in t))
        ef, L = frustration(X, k)
        eintrag = {"E_LJ": e, "kanten": len(k), "tetraeder": len(tet), "alle_in_tetraedern": len(abgedeckt) == N,
                   "grad": grad.tolist(), "E_frust": ef, "E_frust_je_tetraeder": ef / max(len(tet), 1),
                   "dehnung_max": float(np.max(np.abs(L - 1))), "dehnung_min": float(np.min(L - 1)),
                   "dehnung_maxpos": float(np.max(L - 1)), "X": X.tolist(), "sek": time.time() - t0}
        zentren = [i for i in range(N) if grad[i] == 12]
        if zentren:
            radial = [L[m] - 1 for m, (i, j) in enumerate(k) if i in zentren or j in zentren]
            sonst = [L[m] - 1 for m, (i, j) in enumerate(k) if not (i in zentren or j in zentren)]
            eintrag.update(zentren=zentren, dehnung_radial_mittel=float(np.mean(radial)),
                           dehnung_oberflaeche_mittel=float(np.mean(sonst)) if sonst else None)
        aus["N"][str(N)] = eintrag
        with open(pfad + ".tmp", "w") as f:
            json.dump(aus, f, indent=1)
        os.replace(pfad + ".tmp", pfad)
    print("tetraklumpen fertig")


if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5])
