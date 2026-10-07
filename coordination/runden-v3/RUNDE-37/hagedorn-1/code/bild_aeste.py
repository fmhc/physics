#!/usr/bin/env python3
"""HAGEDORN-1, nach dem Einfrieren (rein beschreibend): Bild aller ringlokalisierten reellen Moden (beide Vorzeichen)
der stabilen Profile aus lauf/nach/aeste_*.json. Ausgabe bild_aeste.png.
Aufruf: bild_aeste.py --nach lauf/nach --out lauf/auswertung"""
import argparse
import glob
import json
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nach", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    dateien = sorted(glob.glob(os.path.join(args.nach, "aeste_m*_w*.json")))
    fig, axs = plt.subplots(1, len(dateien), figsize=(4.2 * len(dateien), 4.2), sharey=True)
    if len(dateien) == 1:
        axs = [axs]
    for ax, p in zip(axs, dateien):
        with open(p) as fh:
            d = json.load(fh)
        for e in d["aeste"]:
            for mo in e["moden"]:
                ax.plot(e["l"], mo["re"], "o", ms=3 + 3 * mo["ringanteil"], color="C0" if mo["re"] > 0 else "C3",
                        alpha=0.4 + 0.6 * mo["ringanteil"])
        ax.axhline(0.0, color="k", lw=0.6)
        ax.axhspan(-(1 - d["omega"] if "omega" in d else 0.258), 0, alpha=0)
        ax.set_title(f"m = {d['m']}, omega^2 = {d['w2']} (R = {d['R_max']:.2f})", fontsize=9)
        ax.set_xlabel("l")
        ax.grid(alpha=0.3)
    axs[0].set_ylabel("Re Omega der Ringmoden (|Re| <= 0,6; Punktgroesse ~ Ringanteil)")
    fig.suptitle("Stabile Profile: alle ringlokalisierten reellen Moden (Nachauswertung, beschreibend)", fontsize=10)
    fig.tight_layout()
    fig.savefig(os.path.join(args.out, "bild_aeste.png"), dpi=130)


if __name__ == "__main__":
    main()
