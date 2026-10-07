#!/usr/bin/env python3
"""BAD-TAKT, Nachtrag nach den Laeufen (nicht im eingefrorenen PLAN.md, keine Urteilsgrundlage).
Code-Agent, 02.10.2026. Prueft die Hypothese [H], dass die langsamen Aenderungen der Fenstermittel ein
langsamer Dreiball-Takt sind: Kombinationsphase c = ph_1 - 2 ph_2 + ph_3 (Frequenz omega_1 - 2 omega_2 + omega_3,
nahezu resonant, weil die omega fast gleichabstaendig sind). Glaettet Q_i mit gleitendem Mittel der Breite 600
(> 2 Paarschwebungen) und passt Q_glatt = a + b cos(c) + d sin(c) an.
Aufruf: python nachtrag_dreier.py lauf/B1.npz lauf/B1f.npz lauf/B2.npz lauf/K1.npz
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import math  # noqa: E402
import sys  # noqa: E402

import numpy as np  # noqa: E402

BREITE = 600.0
for pfad in sys.argv[1:]:
    z = np.load(pfad, allow_pickle=False)
    t = z["r_t"]
    dts = float(t[1] - t[0])
    ph = [np.unwrap(z[f"r_ph{i}"]) for i in range(3)]
    c = ph[0] - 2.0 * ph[1] + ph[2]
    m = (t >= 100.0)
    f_c = -float(np.polyfit(t[m], c[m], 1)[0])
    n = int(round(BREITE / dts))
    ker = np.ones(n) / n
    lo, hi = n // 2, len(t) - n // 2
    sel = slice(lo, hi)
    tt = t[sel]
    mm = (tt >= 400.0) & (tt <= t[-1] - 300.0)
    print(f"{os.path.basename(pfad)}: Frequenz der Kombinationsphase omega_1 - 2 omega_2 + omega_3 = {f_c:.6f}, "
          f"Periode {2 * math.pi / abs(f_c):.0f}")
    for i in range(3):
        qg = np.convolve(z[f"r_Q{i}"], ker, mode="same")[sel][mm]
        cc = c[sel][mm]
        A = np.stack([np.ones_like(cc), np.cos(cc), np.sin(cc)], axis=1)
        koef, *_ = np.linalg.lstsq(A, qg, rcond=None)
        rest = qg - A @ koef
        r2 = 1.0 - float(rest.var() / qg.var()) if qg.var() > 0 else float("nan")
        amp = math.hypot(koef[1], koef[2])
        # Vergleich: lineare Drift
        kl = np.polyfit(tt[mm], qg, 1)
        r2l = 1.0 - float((qg - np.polyval(kl, tt[mm])).var() / qg.var())
        print(f"   Ball {i + 1}: Q_glatt Spanne {qg.max() - qg.min():.2e}, Fit a + b cos c + d sin c: Amplitude "
              f"{amp:.2e}, Phase {math.degrees(math.atan2(koef[2], koef[1])):.0f} Grad, R^2 {r2:.3f}; "
              f"lineare Drift {kl[0] * 1e3:+.2e} je 1000, R^2 {r2l:.3f}")
