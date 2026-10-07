#!/usr/bin/env python3
"""INDUZIERT-1, Nachtrag (beschreibend, nicht eingefroren, nicht geurteilt): c0s gegen c2 je Richtung bei abs(k) = 0,05,
mit Einsteins Gerade c0s = -2 c2. Liest nur lauf/auswertung.json.

Aufruf: python nachtrag_bild.py <auswertung.json> <bild.png>
"""
import json
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

with open(sys.argv[1]) as f:
    erg = json.load(f)
fig, axs = plt.subplots(1, 2, figsize=(15, 6))
marker = {"P": "o", "R2_fusspunkt": "x", "R1_mitte": "+", "G_ganz": "^", "L_laengen": "s"}
for ax, m2 in zip(axs, (0.01, 0.04)):
    kk = erg["ketten"][f"n4-m{m2}-L64"]
    for var, mk in marker.items():
        pk = [e for e in kk["punkte"] if e["betrag"] == 0.05]
        x = [e[var]["schur"]["c2"] for e in pk]
        y = [e[var]["schur"]["c0s"] for e in pk]
        ax.plot(x, y, mk, ms=7 if var == "P" else 6, label=f"Variante {var}")
        if var == "P":
            for e, xi, yi in zip(pk, x, y):
                ax.annotate(e["richtung"], (xi, yi), fontsize=7, xytext=(4, 3), textcoords="offset points")
    t = np.linspace(-0.03, 0.03, 10)
    ax.plot(t, -2 * t, "k-", lw=1, label="Einstein: c0s = -2 c2")
    ax.axhline(0, color="0.6", lw=0.6)
    ax.axvline(0, color="0.6", lw=0.6)
    ax.set_xlim(-0.012, 0.03)
    ax.set_ylim(-0.06, 0.14)
    ax.set_xlabel("c2 (Spin 2, Schur-Form)")
    ax.set_ylabel("c0s (konformer Modus)")
    ax.set_title(f"INDUZIERT-1, n = 4, m^2 = {m2}, L_q = 64, abs(k) = 0,05: 8 Richtungen")
    ax.legend(fontsize=7)
fig.tight_layout()
fig.savefig(sys.argv[2], dpi=110)
print("geschrieben", sys.argv[2])
