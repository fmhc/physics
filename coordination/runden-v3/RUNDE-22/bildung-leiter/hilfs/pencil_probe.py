#!/usr/bin/env python3
"""BILDUNG-LEITER, Methodenprobe vor dem Einfrieren (Code-Agent, 02.10.2026). Synthetisch, keine Laufdaten.

Misst Zeitbedarf und Treffsicherheit von matrix_pencil (Runde-12-Modul) und der Bandwahl aus zeit2d_v2 fuer die
Fenster der Karte. Testsignal wie eine erwartete Projektion: Driftanteil (a + b t), zwei gebundene Paare, das Paar der
stillen Mode (+-1,556) mit bekannter Rate gamma, eine breite Bandkomponente (1,50), ein hohes Paar (2,5), Rauschen.
Abtastung 0,2 wie im Lauf. Aufruf: python pencil_probe.py <aus.json>
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import json
import sys
import time

import torch

torch.set_num_threads(1)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "code"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bic2_2d_praez_v2 as m  # noqa: E402
import zeit2d_v2 as z  # noqa: E402

MESS = 0.2


def signal(t0, t1, gamma, gen):
    t = torch.arange(int(round(t0 / MESS)), int(round(t1 / MESS)) + 1, dtype=m.F64) * MESS
    komps = [(0.10, -1e-6, 0.30), (-0.10, -1e-6, 0.25), (0.22, -1e-5, 0.10), (-0.22, -1e-5, 0.08),
             (1.556, -gamma, 0.010), (-1.556, -gamma, 0.008), (1.50, -5e-3, 0.005), (-1.50, -5e-3, 0.004),
             (2.5, -1e-4, 0.010), (-2.5, -1e-4, 0.008)]
    y = (0.5 + 1e-3j * t).to(m.C128)
    for (re, im, amp) in komps:
        y = y + amp * torch.exp(-1j * complex(re, im) * t.to(m.C128))
    y = y + 1e-7 * (torch.randn(t.numel(), generator=gen, dtype=m.F64)
                    + 1j * torch.randn(t.numel(), generator=gen, dtype=m.F64))
    return y


def main():
    gen = torch.Generator().manual_seed(20261002)
    faelle = [("Sprosse", 200.0, 2000.0, 1e-6), ("daneben", 200.0, 2000.0, 1.5e-4), ("dazwischen", 50.0, 400.0, 1e-2),
              ("dazwischen_schwach", 50.0, 400.0, 3e-3)]
    aus = []
    for (name, t0, t1, gamma) in faelle:
        y = signal(t0, t1, gamma, gen)
        for K in (12, 24):
            tz = time.time()
            pen = m.matrix_pencil(y, MESS, K=K)[:K]
            sek = time.time() - tz
            b = z.bandwahl(pen)
            aus.append({"fall": name, "t0": t0, "t1": t1, "gamma_wahr": gamma, "K": K, "n_punkte": y.numel(),
                        "sek": sek, "band": b, "gamma_gemessen": (-b["im"] if b else None),
                        "rel_fehler": (abs(-b["im"] - gamma) / gamma if b else None), "pencil": pen})
            print(f"{name:20s} K={K:2d} n={y.numel():5d} {sek:6.2f} s  gamma wahr {gamma:.2e}  gemessen "
                  f"{(-b['im'] if b else float('nan')):.3e}  re {(b['re'] if b else float('nan')):+.5f}", flush=True)
    with open(sys.argv[1] + ".tmp", "w") as fh:
        json.dump(m.jsonfest(aus), fh, indent=1)
    os.replace(sys.argv[1] + ".tmp", sys.argv[1])


if __name__ == "__main__":
    main()
