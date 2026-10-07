#!/usr/bin/env python3
"""BILDUNG-LEITER, NACHTRAEGLICH (Code-Agent, 02.10.2026; nach Kenntnis der gewerteten Ergebnisse, NICHT gewertet).

Frage: Wie fein misst der Stillanteil von Arm G? Mit K = 12 liegt die Nachweisgrenze beim Anteil der schwaechsten
erfassten Komponente (0,3 bis 0,8 %). Gegenprobe auf den gespeicherten Rohsignalen (aus/nl-*.json.roh.pt), Reihe
"gauss", Fenster [100, 600], Mittelwert abgezogen:
  (1) Pencil mit K = 12, 24, 40 und anteile() aus zeit2d_v2 (gleiche Definition wie gewertet);
  (2) Periodogramm mit Hann-Fenster: Leistungsanteil im Band 1,45 <= |f| <= 1,65 und unter der Schwelle
      0,01 < |f| < 1 - omega, jeweils gegen alle |f| > 0,01 (f = Kreisfrequenz).
Aufruf: python still_nachtrag.py <aus.json> <roh.pt> [<roh.pt> ...]
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import json
import math
import sys

import torch

torch.set_num_threads(1)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bic2_2d_praez_v2 as m  # noqa: E402
import zeit2d_v2 as z  # noqa: E402


def main():
    aus = []
    for pfad in sys.argv[2:]:
        roh = torch.load(pfad, weights_only=False)
        mess, om = roh["mess"], roh["omega"]
        sz = roh["szen"][:, 0]
        i0, i1 = int(round(100.0 / mess)), min(sz.numel(), int(round(600.0 / mess)) + 1)
        y = sz[i0:i1] - sz[i0:i1].mean()
        e = {"datei": os.path.basename(pfad), "w2": roh["meta"]["w2"], "dr": roh["meta"]["dr"], "n": y.numel()}
        for K in (12, 24, 40):
            pen = m.matrix_pencil(y.to(m.C128), mess, K=K)[:K]
            e[f"anteile_K{K}"] = z.anteile(pen, 1.0 - om)
            e[f"band_K{K}"] = [p for p in pen if z.BIC_BAND[0] <= abs(p["re"]) <= z.BIC_BAND[1]]
        n = y.numel()
        w = torch.hann_window(n, periodic=False, dtype=m.F64)
        F = torch.fft.fft((y * w).to(m.C128))
        f = torch.fft.fftfreq(n, d=mess).to(m.F64) * 2.0 * math.pi
        P = F.abs() ** 2
        alle = float(P[f.abs() > 0.01].sum())
        band = float(P[(f.abs() >= z.BIC_BAND[0]) & (f.abs() <= z.BIC_BAND[1])].sum())
        geb = float(P[(f.abs() > 0.01) & (f.abs() < 1.0 - om)].sum())
        e["periodogramm"] = {"band_anteil": band / alle, "gebunden_anteil": geb / alle}
        aus.append(e)
        print(f"{e['datei']}: K12 {e['anteile_K12']}, K24 {e['anteile_K24']}, K40 {e['anteile_K40']}, "
              f"Periodogramm band {band / alle:.2e} gebunden {geb / alle:.3f}", flush=True)
    with open(sys.argv[1] + ".tmp", "w") as fh:
        json.dump(m.jsonfest(aus), fh, indent=1)
    os.replace(sys.argv[1] + ".tmp", sys.argv[1])


if __name__ == "__main__":
    main()
