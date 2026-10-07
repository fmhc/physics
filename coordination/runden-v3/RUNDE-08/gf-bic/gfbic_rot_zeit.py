#!/usr/bin/env python3
"""Runde 9, ROT-2: Zeitverlauf aus einer npz-Datei von gfbic_rot.py ausgeben (langsame Phase, z, Q_1, Q_2 an 25
Zeitpunkten; Laufstrecken der Phase je Zeitfenster). Nur Auswertung, keine Physik-Rechnung. 2026-09-30 08:10 CEST."""
import math
import sys

import numpy as np

for pfad in sys.argv[1:]:
    d = np.load(pfad)
    t, dth, q1, q2 = d["t"], d["dth_g"], d["q1"], d["q2"]
    dtm = t[1] - t[0]
    om = 0.869332
    nw = max(1, int(round((math.pi / om) / dtm)))
    slow = np.convolve(dth, np.ones(nw) / nw, mode="same")
    Q = q1 + q2
    z = (q1 - q2) / Q
    print(f"=== {pfad}: {len(t)} Punkte, T = {t[-1]:.1f}")
    idx = np.linspace(nw, len(t) - nw - 1, 25).astype(int)
    for i in idx:
        print(f"  t {t[i]:8.1f}: phi_langsam {slow[i]:+9.4f}, z {z[i]:+.4f}, Q1 {q1[i]:9.3f}, Q2 {q2[i]:9.3f}, Q {Q[i]:9.3f}")
    fen = np.array_split(np.arange(nw, len(t) - nw), 12)
    zeile = []
    for f in fen:
        zeile.append(f"[{t[f[0]]:.0f}-{t[f[-1]]:.0f}]: Spanne {np.max(slow[f]) - np.min(slow[f]):.2f}, "
                     f"Netto {slow[f[-1]] - slow[f[0]]:+.2f}")
    print("  Fenster: " + "; ".join(zeile))
