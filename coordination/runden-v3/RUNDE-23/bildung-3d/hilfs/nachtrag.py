#!/usr/bin/env python3
"""BILDUNG-3D (Runde 23), NACHTRAG nach Kenntnis der gewerteten Ergebnisse, NICHT gewertet.
Liest die Rohdateien der Zeitlaeufe (zeit3d.py lauf) und die Familiendateien; rechnet nichts neu.
  (a) omega aus einem langen Phasenfit ueber [500; 1000] und Q_F dazu (Lesart: Fensterlaenge 50 gegen Atmung).
  (b) Ladung und Energie in r < 10 / 20 / 30 / 40 / r_sd im Fenster [950; 1000] (Mittel).
  (c) Zentralfeld psi(0, t) in [500; 1000]: Leistungsanteil positiver und negativer Frequenzen (Konvention
      psi ~ exp(-i w t): w > 0 heisst Ladung +), dazu die drei staerksten Linien.
  (d) Schnappschuss T = 1000: S(r) an einigen Radien, r_halb der Dichte.
Aufruf: python nachtrag.py <aus.json> <familie,familie,...> <roh.pt> [<roh.pt> ...]"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import json  # noqa: E402
import math  # noqa: E402
import sys  # noqa: E402

import numpy as np  # noqa: E402
import torch  # noqa: E402

torch.set_num_threads(1)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zeit3d as z  # noqa: E402

aus = {"hinweis": "Nachtrag nach Kenntnis der gewerteten Ergebnisse, nicht gewertet", "laeufe": []}
for p in sys.argv[3:]:
    roh = torch.load(p, weights_only=False)
    meta = roh["meta"]
    fam = z.familie_laden(sys.argv[2].split(","), meta["dr"], meta["r_max"])
    ts = np.array(roh["ts"])
    dt = meta["dt"]
    zen = roh["zentrum"].numpy()
    lad = roh["ladung"].numpy()
    ene = roh["energie"].numpy()
    sn = roh["schnapp"].numpy()
    st = np.array(roh["schnapp_t"])
    r_s = np.arange(sn.shape[2]) * meta["k_schnapp"] * meta["dr"]
    lauf = {"quelle": p, "dr": meta["dr"], "reihen": []}
    for b, nm in enumerate(meta["namen"]):
        p0 = zen[:, b]
        dphi = np.angle(p0[1:] / p0[:-1])
        ph = np.concatenate([[np.angle(p0[0])], np.angle(p0[0]) + np.cumsum(dphi)])
        e = {"reihe": nm}
        m = (ts >= 500.0 - 1e-9) & (ts <= 1000.0 + 1e-9)
        b1, b0 = np.polyfit(ts[m], ph[m], 1)
        om = 2.0 / dt * math.sin(0.5 * (-b1) * dt)
        w2 = om * om
        qb = float(lad[(ts >= 950.0 - 1e-9) & (ts <= 1000.0 + 1e-9), b, meta["k_sd"]].mean())
        e["lang_500_1000"] = {"omega": om, "w2": w2, "phase_rest_max": float(np.abs(ph[m] - (b0 + b1 * ts[m])).max())}
        if fam["x"][0] <= w2 <= fam["x"][-1]:
            qf = float(math.exp(fam["q"](w2)))
            e["lang_500_1000"].update({"Q_F": qf, "Q_Ball_950_1000": qb, "abw": (qb - qf) / qf,
                                        "E_durch_Q_F": float(fam["eq"](w2))})
        # Fenster-Omegas ueber [500; 1000] in 50er-Schritten (Streuung durch Atmung)
        oms = []
        for t1 in np.arange(550.0, 1000.0 + 1e-9, 50.0):
            mm = (ts >= t1 - 50.0 - 1e-9) & (ts <= t1 + 1e-9)
            c1, _ = np.polyfit(ts[mm], ph[mm], 1)
            oms.append(2.0 / dt * math.sin(0.5 * (-c1) * dt))
        e["omega_50er_500_1000"] = {"min": min(oms), "max": max(oms), "mittel": float(np.mean(oms)),
                                    "streuung": float(np.std(oms))}
        mf = (ts >= 950.0 - 1e-9) & (ts <= 1000.0 + 1e-9)
        e["schalen_950_1000"] = [{"r": meta["radien"][k], "Q": float(lad[mf, b, k].mean()),
                                  "E": float(ene[mf, b, k].mean())} for k in range(len(meta["radien"]))]
        y = p0[m]
        y = y * np.hanning(len(y))
        n = 8 * len(y)
        F = np.fft.fft(y, n)
        fr = 2.0 * math.pi * np.fft.fftfreq(n, ts[1] - ts[0])      # psi ~ exp(-i w t) -> Gipfel bei fr = -w
        P = np.abs(F) ** 2
        pos = float(P[fr < 0].sum())                                 # w > 0 (Ladung +)
        neg = float(P[fr > 0].sum())
        e["zentrum_spektrum_500_1000"] = {"anteil_w_positiv": pos / (pos + neg), "anteil_w_negativ": neg / (pos + neg)}
        idx = np.argsort(P)[::-1]
        linien = []
        for k in idx:
            w = float(-fr[k])
            if all(abs(w - l["w"]) > 0.02 for l in linien):
                linien.append({"w": w, "P_rel": float(P[k] / P.max())})
            if len(linien) == 3:
                break
        e["zentrum_spektrum_500_1000"]["linien"] = linien
        js = np.where(np.abs(st - 1000.0) < 1e-6)[0]
        if js.size:
            S = sn[js[0], b]
            e["schnapp_1000"] = {"S_bei_r": {str(rr): float(S[int(round(rr / (r_s[1] - r_s[0])))]) for rr in
                                             (0.0, 1.0, 2.0, 3.0, 4.0, 6.0, 8.0, 10.0, 15.0, 20.0, 30.0, 40.0)},
                                 "r_halb": z.r_halb_np(S, r_s[1] - r_s[0])}
        lauf["reihen"].append(e)
    aus["laeufe"].append(lauf)
z.schreiben(aus, sys.argv[1])
print("nachtrag fertig", flush=True)
