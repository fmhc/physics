#!/usr/bin/env python3
"""Hilfsauswertung nach den Laeufen (beschreibend, aendert keine Regel): lokale Dichtemaxima in den gespeicherten
|psi|^2-Bildern (alle 100 Zeiteinheiten, Abstand 0,5). Aufruf: python bilder.py <roh.npz> [schwelle]"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_v] = "1"
import sys  # noqa: E402

import numpy as np  # noqa: E402

z = np.load(sys.argv[1], allow_pickle=False)
schwelle = float(sys.argv[2]) if len(sys.argv) > 2 else 0.01
B, bt, bx = z["bilder"], z["bild_t"], z["bild_x"]
dx = float(bx[1] - bx[0])
for k in range(B.shape[0]):
    S = B[k].astype(np.float64)
    i = np.nonzero((S[1:-1] > S[:-2]) & (S[1:-1] >= S[2:]) & (S[1:-1] > schwelle))[0] + 1
    teile = []
    for j in i:
        lo = j
        while lo > 0 and S[lo - 1] < S[lo] and S[lo - 1] > 0.02 * S[j]:
            lo -= 1
        hi = j
        while hi < S.size - 1 and S[hi + 1] < S[hi] and S[hi + 1] > 0.02 * S[j]:
            hi += 1
        teile.append(f"x={bx[j]:8.1f} S={S[j]:.3f} int|psi|^2={dx * S[lo:hi + 1].sum():.3f}")
    print(f"t={bt[k]:6.0f}: " + (" | ".join(teile) if teile else "-"))
