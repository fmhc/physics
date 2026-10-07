#!/usr/bin/env python3
"""NACHRECHNUNG-ROUTH (Runde 17), Leitung claude-primary, 02.10.2026.
Lineare Stabilitaet von L4 im elliptischen eingeschraenkten Dreikoerperproblem (pulsierende Koordinaten, wahre Anomalie f):
  x'' - 2 y' = (Uxx x + Uxy y) / (1 + e cos f),  y'' + 2 x' = (Uxy x + Uyy y) / (1 + e cos f)
  Uxx = 3/4, Uyy = 9/4, Uxy = (3 sqrt(3)/4)(1 - 2 mu).
Monodromie ueber f in [0, 2 pi] (RK4, vektorisiert ueber das Gitter); stabil, wenn max |Multiplikator| <= 1 + 1e-6.
Aufruf: python floquet.py <aus.json>
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import json
import sys
import time

import numpy as np


def monodromie(mu, e, schritte):
    """mu, e: Arrays gleicher Laenge P. Rueckgabe: Monodromiematrizen (P, 4, 4)."""
    P = mu.size
    uxx, uyy = 0.75, 2.25
    uxy = (3 * np.sqrt(3) / 4) * (1 - 2 * mu)

    def A(f):
        d = 1 + e * np.cos(f)
        M = np.zeros((P, 4, 4))
        M[:, 0, 2] = 1
        M[:, 1, 3] = 1
        M[:, 2, 0] = uxx / d
        M[:, 2, 1] = uxy / d
        M[:, 3, 0] = uxy / d
        M[:, 3, 1] = uyy / d
        M[:, 2, 3] = 2
        M[:, 3, 2] = -2
        return M

    Z = np.broadcast_to(np.eye(4), (P, 4, 4)).copy()
    h = 2 * np.pi / schritte
    f = 0.0
    for _ in range(schritte):
        k1 = A(f) @ Z
        k2 = A(f + h / 2) @ (Z + h / 2 * k1)
        k3 = A(f + h / 2) @ (Z + h / 2 * k2)
        k4 = A(f + h) @ (Z + h * k3)
        Z = Z + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        f += h
    return Z


def main(pfad):
    t0 = time.time()
    mus = np.round(np.arange(0.030, 0.0500001, 0.0005), 6)
    es = np.round(np.arange(0.0, 0.5000001, 0.01), 6)
    MU, E = np.meshgrid(mus, es, indexing="ij")
    aus = {"mu": mus.tolist(), "e": es.tolist(), "stabil": {}, "maxbetrag": {}, "det_abw": {}}
    for schritte in (2000, 4000):
        Mo = monodromie(MU.ravel(), E.ravel(), schritte)
        ev = np.linalg.eigvals(Mo)
        mb = np.max(np.abs(ev), axis=1).reshape(MU.shape)
        aus["maxbetrag"][str(schritte)] = mb.tolist()
        aus["stabil"][str(schritte)] = (mb <= 1 + 1e-6).tolist()
        aus["det_abw"][str(schritte)] = float(np.max(np.abs(np.linalg.det(Mo) - 1)))
    s = np.array(aus["stabil"]["4000"])
    jenseits = [(float(mus[i]), float(es[j])) for i in range(len(mus)) for j in range(len(es))
                if s[i, j] and mus[i] > 0.0390 and es[j] > 0]
    aus["jenseits_routh_stabil"] = jenseits
    aus["max_mu_stabil_jenseits"] = max((m for m, _ in jenseits), default=None)
    aus["e_bei_max_mu"] = [e for m, e in jenseits if m == aus["max_mu_stabil_jenseits"]]
    aus["e0_grenze"] = {"stabil_bis": float(max(mus[i] for i in range(len(mus)) if s[i, 0])),
                        "instabil_ab": float(min(mus[i] for i in range(len(mus)) if not s[i, 0]))}
    j01 = int(np.argmin(np.abs(es - 0.1)))
    aus["e01_instabile_mu"] = [float(mus[i]) for i in range(len(mus)) if not s[i, j01]]
    aus["stufen_gleich"] = bool(np.array_equal(np.array(aus["stabil"]["2000"]), s))
    aus["sek"] = time.time() - t0
    with open(pfad, "w") as fh:
        json.dump(aus, fh, indent=1)
    print("floquet fertig", round(aus["sek"], 1), "s")


if __name__ == "__main__":
    main(sys.argv[1])
