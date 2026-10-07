#!/usr/bin/env python3
# Fassung 2 (nach dem Hauptlauf, nur Darstellung: Zeile 3 als Punkte statt Linien). KAC-DIAMANT-WICK-1: Baender ueber |k| fuer [100], [110], [111], beide Regeln, Wick-rotiert und reell (Re, Im).
# Aufruf (nur auf der .69 ueber kleintest.sh): python bild.py <ziel.png> [punkte]
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kac_wick as kw  # noqa: E402

ziel = sys.argv[1]
npkt = int(sys.argv[2]) if len(sys.argv) > 2 else 301
ks = np.linspace(0.0, 3.0, npkt)
RICHT = [("[100]", np.array([1.0, 0, 0]), "#2a78d6", "-"),
         ("[110]", np.array([1.0, 1, 0]) / np.sqrt(2), "#eb6834", "--"),
         ("[111]", np.array([1.0, 1, 1]) / np.sqrt(3), "#1baf7a", ":")]
TXT, TXT2, FLAECHE = "#0b0b0b", "#52514e", "#fcfcfb"
plt.rcParams.update({"font.size": 9, "axes.edgecolor": TXT2, "axes.labelcolor": TXT, "xtick.color": TXT2,
                     "ytick.color": TXT2, "axes.facecolor": FLAECHE, "figure.facecolor": FLAECHE})
fig, ax = plt.subplots(3, 2, figsize=(11, 11), sharex=True)
for c, (name, (P, p)) in enumerate(kw.REGELN.items()):
    M = kw.mischmatrix(P)
    for lab, n, farbe, stil in RICHT:
        kv = ks[:, None] * n[None, :]
        E = np.linalg.eigvalsh(kw.batch(kv, M, "wick"))
        w = np.linalg.eigvals(kw.batch(kv, M, "reell"))
        w = np.take_along_axis(w, np.argsort(-w.real, axis=1, kind="stable"), axis=1)
        for b in range(8):
            ax[0, c].plot(ks, E[:, b], color=farbe, ls=stil, lw=1.4, label=lab if b == 0 else None)
            ax[1, c].plot(ks, w[:, b].real, color=farbe, ls=stil, lw=1.4, label=lab if b == 0 else None)
            ax[2, c].plot(ks, np.abs(w[:, b].imag), color=farbe, ls="none", marker="o", ms=1.6, label=lab if b == 0 else None)
    ce = kw.CEFF_SCHREIB[name]
    dirac = np.sqrt(1 + ce ** 2 * ks ** 2)
    ax[0, c].plot(ks, 1 - dirac, color=TXT2, lw=0.8, ls=(0, (1, 2)), label="1 +- Wurzel(1 + c_eff^2 k^2), Schreibtisch")
    ax[0, c].plot(ks, 1 + dirac, color=TXT2, lw=0.8, ls=(0, (1, 2)))
    titel = {"gleich": "gleichverteilt P = J/4", "ohne_rueck": "ohne Ruecksprung P = (J - I)/3"}[name]
    ax[0, c].set_title(f"Wick (Ghose): H = T(k) + lambda(I - M)\n{titel}", color=TXT, fontsize=10)
    ax[1, c].set_title(f"reell (Kac): Re g, G = -i T(k) + lambda(M - I)\n{titel}", color=TXT, fontsize=10)
    ax[2, c].set_title(f"reell (Kac): |Im g| (konjugierte Paare deckungsgleich)\n{titel}", color=TXT, fontsize=10)
    for r in range(3):
        a = ax[r, c]
        a.axvspan(0, 0.1, color="#cde2fb", alpha=0.5, lw=0)
        a.grid(True, color="#e4e3df", lw=0.6)
        a.set_axisbelow(True)
        if c == 0:
            a.set_ylabel(["E / hbar lambda", "Re g / lambda", "|Im g| / lambda"][r])
    ax[2, c].set_xlabel("|k| l   (l = c/lambda = Bindungslaenge; hellblau: Kartenbereich bis 0,1)")
ax[0, 0].legend(loc="upper left", fontsize=8, frameon=False)
ax[1, 0].legend(loc="lower left", fontsize=8, frameon=False)
fig.suptitle("KAC-DIAMANT-WICK-1: 8x8-Kantenwahl auf dem Diamantnetz, Baender laengs [100], [110], [111]  (c = lambda = hbar = 1)",
             color=TXT, fontsize=11)
fig.tight_layout(rect=(0, 0, 1, 0.97))
fig.savefig(ziel, dpi=130)
print("bild", ziel, npkt)
