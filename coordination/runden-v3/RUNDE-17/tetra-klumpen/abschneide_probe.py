#!/usr/bin/env python3
"""TETRA-KLUMPEN, nachtraegliche Empfindlichkeitsprobe (post hoc, Leitung 02.10.2026): Kontakt-Abschneideradius.
Liest die gespeicherten LJ-Koordinaten (klumpen-a.json, klumpen-b.json) und rechnet Kontakte, Tetraeder und
Frustrationsenergie fuer mehrere Abschneidefaktoren neu, dazu die Kopplung Delta = E_f(19) - 2 E_f(13) + E_f(7).
Aufruf: python abschneide_probe.py <aus.json>
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import json
import sys

import numpy as np

import tetraklumpen as tk


def main(pfad):
    daten = {}
    for f in ("klumpen-a.json", "klumpen-b.json"):
        daten.update(json.load(open(f))["N"])
    aus = {}
    for faktor in (1.10, 1.15, 1.20, 1.25):
        rc = faktor * 2 ** (1 / 6)
        z = {}
        for N in (7, 13, 19, 23):
            X = np.array(daten[str(N)]["X"])
            D = np.linalg.norm(X[:, None] - X[None], axis=2)
            k = [(i, j) for i in range(N) for j in range(i + 1, N) if D[i, j] < rc]
            ef, L = tk.frustration(X, k)
            z[str(N)] = {"kanten": len(k), "tetraeder": len(tk.tetraeder(N, k)), "E_frust": ef,
                         "dehnung_max": float(np.max(np.abs(L - 1)))}
        z["Delta_19"] = z["19"]["E_frust"] - 2 * z["13"]["E_frust"] + z["7"]["E_frust"]
        aus["%.2f" % faktor] = z
    json.dump(aus, open(pfad, "w"), indent=1)
    print("probe fertig")


if __name__ == "__main__":
    main(sys.argv[1])
