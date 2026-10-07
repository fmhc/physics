#!/usr/bin/env python3
# PAAR-REGGE-1: Bild, NACH dem Einfrieren geschrieben (2026-10-04 ab 18:37:35 CEST, date). Nur Darstellung, keine
# Auswertung. Grund: Der Bildmodus des eingefrorenen paar_regge.py zeichnet Kurven ueber ein festes eta-Fenster; bei
# m ~ 1e-8 (beste Fits fuer A) liegt die ganze Kurve am Ursprung und ist unsichtbar. Hier werden die Kurven ueber
# J_cl aufgebaut (loese aus dem eingefrorenen Modul). Gezeichnet werden nur Zahlen aus fits.json.
# Aufruf: bild2.py <fits.json> <aus.png>
import json
import math
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, "/home/fmh/fmhc-physics-remote/paar-regge-1/code")
from paar_regge import (A_4D, DATEN_A, J_PUNKTE, KAPPA, LINIE_B, EJ, linien_punkte, loese)  # noqa: E402

d = json.load(open(sys.argv[1]))
k = KAPPA["9/4"]
farbe = {"0": "#2a78d6", "1/12": "#eb6834"}
ink, ink2, grau = "#0b0b0b", "#52514e", "#9a9893"
x_max, y_max = 90.0, 6.5


def kurve(m, a):
    Jc = np.linspace(0.02, y_max - a, 300)
    E = np.array([loese(m, k, float(j))["E"] for j in Jc])
    return E ** 2, Jc + a


def s_konst_v(v):
    E1, J1, _, _ = EJ(1.0, k, math.atanh(v), "P")
    return 2.0 * math.pi * J1 / (E1 * E1)


fig, axs = plt.subplots(1, 2, figsize=(12.5, 5.8), sharey=True)
fig.patch.set_facecolor("#fcfcfb")
xs = np.linspace(0.0, x_max, 200)
s34 = s_konst_v(0.75)
for ax, ds, titel in ((axs[0], "A", "(A) Athenodorou/Teper 2020: 2++ 4,894(22), 4++ 7,60(12)"),
                      (axs[1], "B", "(B) Meyer/Teper-Gerade 2004: 0,281(22), 0,93(24)")):
    ax.set_facecolor("#fcfcfb")
    ax.plot(xs, xs / (2.0 * math.pi * k), color=grau, lw=1.4, ls=":", label="masselos, a = 0 (Steigung 4/9)")
    ax.plot(xs, s34 * xs / (2.0 * math.pi), color=grau, lw=1.2, ls="--",
            label=f"Enden fest bei v = 3/4 (Steigung {s34:.3f})")
    if ds == "A":
        M = np.array(DATEN_A["M"]); dM = np.array(DATEN_A["dM"])
        ax.errorbar(M ** 2, J_PUNKTE, xerr=2 * M * dM, fmt="o", ms=8, color=ink, capsize=4,
                    label="Gitter 2++, 4++ (A)", zorder=5)
        les = "diag"
    else:
        L = LINIE_B
        ax.plot(xs, L["a0"] + L["s"] * xs / (2 * math.pi), color=ink2, lw=1.4, label="MT-Gerade (B)")
        Mp, C = linien_punkte(L)
        Mp = np.array(Mp)
        ax.errorbar(Mp ** 2, J_PUNKTE, xerr=2 * Mp * np.sqrt(np.diag(C)), fmt="s", ms=8, color=ink, capsize=4,
                    label="Punkte (B), Bandbreite je Punkt (R1)", zorder=5)
        les = "R3"
    for r in d["fits"]:
        if r["datensatz"] != ds or r["kappa"] != "9/4" or r["variante"] != "P":
            continue
        if r["lesart"] == les:
            xx, yy = kurve(r["m"], A_4D[r["a"]])
            ax.plot(xx, yy, color=farbe[r["a"]], lw=2.0,
                    label=f"Fit{' R3' if ds == 'B' else ''}, a = {r['a']}: m = {r['m']:.2f}, "
                          f"v(2) = {r['v_end2']:.2f}, p = {r['p']:.1e}")
        elif ds == "B" and r["lesart"] == "R1":
            xx, yy = kurve(r["m"], A_4D[r["a"]])
            ax.plot(xx, yy, color=farbe[r["a"]], lw=1.2, ls="-.",
                    label=f"Lesart R1, a = {r['a']}: m = {r['m']:.2f}, v(2) = {r['v_end2']:.2f}, p = {r['p']:.2f}")
    ax.set_xlim(0, x_max)
    ax.set_ylim(0, y_max)
    ax.set_xlabel("M² / σ", color=ink)
    ax.set_title(titel, color=ink, fontsize=10.5)
    ax.grid(True, color="#e4e3df", lw=0.6)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    ax.legend(loc="upper left", fontsize=8, frameon=False)
axs[0].set_ylabel("J", color=ink)
fig.suptitle("PAAR-REGGE-1: rotierender String mit zwei gleichen Endmassen, σ_A = 9/4 σ, Intercept a fest (3+1D)",
             color=ink, fontsize=12)
fig.tight_layout()
fig.savefig(sys.argv[2], dpi=130, facecolor=fig.get_facecolor())
print("fertig")
