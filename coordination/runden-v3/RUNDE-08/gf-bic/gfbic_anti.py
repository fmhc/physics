#!/usr/bin/env python3
"""Runde 9, Karte ROT-2 Teil (c) (PLAN.md Nachtrag F, VF7): Gegentakt (antisymmetrischer Sektor) des gemischten Balls,
Gegenlaeufer-Pol nu ~ 2 omega: Breite entlang omega^2 und Umlauftest an einem Minimum. Code begonnen 2026-09-30 07:56 CEST.
Koeffizienten (R8 Nachtrag A): dp = U'(S) + g J S, sp = -g J S/2, dp' = U''(S) + g J, sp' = -g J/2 (S = 2 h^2, nativ).
Importiert gfbic_umlauf (unveraendert, Fassung 2) und ueber ihn bic2.py.
Kommandos: scan --g G --xs a,b,c | umlauf --g G --x0 X --nu0 N
"""
import argparse
import json
import math
import os
import sys
import traceback

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import numpy as np  # noqa: E402
import torch  # noqa: E402

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import gfbic_umlauf as GU  # noqa: E402
import gfbic as G  # noqa: E402

JK = 1.0


def k_anti(S, g):
    return GU.U1(S) + g * JK * S, -0.5 * g * JK * S, GU.U2(S) + g * JK, -0.5 * g * JK + 0.0 * S


GU.KOEFF["anti"] = k_anti


def scan(a, dev, budget, zeilen):
    xs = [float(v) for v in a.xs.split(",")]
    out = []
    for x in xs:
        if not budget.ok(f"scan {x}", 20.0):
            break
        prof = GU.prof_nativ(x, a.g, 0.5 * a.h)
        L = GU.lin_multi_k([prof], a.h, a.frand, dev, k_anti, a.g)
        om = math.sqrt(x)
        n = int(GU.B2.radius_wo(prof, 1e-12 * prof["f0"]) / prof["h"]) + 2
        f, _ = GU.B2.f_werte(prof, n)
        f = np.array(f)
        rr = prof["h"] * np.arange(n)
        h2 = 0.5 * f ** 2
        alpha = 2 * a.g * JK * np.sum(h2 ** 2 * rr ** 2) / np.sum(h2 * rr ** 2)
        nu_s = math.sqrt(4 * x + 3 * alpha)
        grid = [nu_s - 0.08 + 0.16 * i / 159 for i in range(160)]
        Dw = GU.B2.det_liste_m(L, [complex(v, 0.0) for v in grid], [0] * len(grid), [1.0] * len(grid))
        i0 = int(np.argmin([abs(z) for z in Dw]))
        keim = complex(grid[i0], -1e-6)
        pol = GU.B2.newton_m(L, [keim], [0], [1.0], iters=a.iter_newton)[0]
        e = {"x": x, "nu": pol["rho"], "Gamma": -pol["rho"].imag, "absD": pol["absD"], "konv": pol["konvergiert"],
             "nu_zwei_moden": nu_s, "alpha": float(alpha), "nu_keim": grid[i0]}
        out.append(e)
        zeilen.append(f"  omega^2 = {x:.5f}: nu = {G.fz(pol['rho'], 9)}, |D| {pol['absD']:.1e}, konv {pol['konvergiert']} "
                      f"(Keim {grid[i0]:.5f}, Zwei-Moden {nu_s:.5f})")
    # lokale Minima der Breite
    gam = [e["Gamma"] for e in out]
    mins = [out[i]["x"] for i in range(1, len(out) - 1) if gam[i] < gam[i - 1] and gam[i] <= gam[i + 1]]
    zeilen.append(f"  lokale Minima der Breite bei omega^2 = {mins}")
    return {"punkte": out, "minima": mins}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("kommando", choices=["scan", "umlauf"])
    ap.add_argument("--g", type=float, default=0.05)
    ap.add_argument("--xs", default="0.70,0.705,0.71,0.715,0.72")
    ap.add_argument("--x0", type=float, default=0.711)
    ap.add_argument("--nu0", type=float, default=1.70)
    ap.add_argument("--cgam", type=float, default=0.001)
    ap.add_argument("--h", type=float, default=0.02)
    ap.add_argument("--frand", type=float, default=1e-6)
    ap.add_argument("--offs", default="0,-5e-4,5e-4,-2e-3,2e-3")
    ap.add_argument("--dxs", default="5e-4,1e-4")
    ap.add_argument("--iter-newton", dest="iter_newton", type=int, default=25)
    ap.add_argument("--u-n", dest="u_n", type=int, default=60)
    ap.add_argument("--u-drho", dest="u_drho", type=float, default=2e-5)
    ap.add_argument("--u-drho-ohne-fit", dest="u_drho_ohne_fit", type=float, default=5e-4)
    ap.add_argument("--out", default=None)
    ap.add_argument("--budget", type=float, default=540.0)
    a = ap.parse_args()
    torch.set_num_threads(1)
    dev = torch.device("cpu")
    budget = G.Budget(a.budget)
    out = a.out or os.path.join(HIER, "ausgabe-anti")
    os.makedirs(out, exist_ok=True)
    kopf = (f"Runde 9 ROT-2 (c) Gegentakt {a.kommando} Start {G.jetzt()}; gfbic_anti.py sha256 "
            f"{G.sha256(os.path.abspath(__file__))[:16]}, gfbic_umlauf.py {G.sha256(GU.__file__)[:16]}; g = {a.g}, h = {a.h}")
    zeilen = [kopf]
    print(kopf, flush=True)
    erg = {"argumente": vars(a)}
    rc = 0
    try:
        if a.kommando == "scan":
            erg["scan"] = scan(a, dev, budget, zeilen)
        else:
            GU.PUNKTE["AG"] = ("anti", a.g, a.x0, a.nu0, 1.2, a.cgam, "nativ")
            a.x0_ = None
            erg["AG"] = GU.stelle("AG", a, dev, budget, zeilen)
    except Exception:                                   # noqa: BLE001
        tb = traceback.format_exc()
        zeilen.append("FEHLER:\n" + tb)
        erg["fehler"] = tb
        rc = 1
    zeilen.append(f"Ende {G.jetzt()}, {G.uhr():.1f} s; entfallen: {budget.abgebrochen or 'nichts'}")
    with open(os.path.join(out, f"anti_{a.kommando}.json"), "w") as fh:
        json.dump(G.jsonfest(erg), fh, indent=1)
    with open(os.path.join(out, f"anti_{a.kommando}_bericht.txt"), "w") as fh:
        fh.write("\n".join(zeilen) + "\n")
    print("\n".join(zeilen[1:]), flush=True)
    sys.exit(rc)


if __name__ == "__main__":
    main()
