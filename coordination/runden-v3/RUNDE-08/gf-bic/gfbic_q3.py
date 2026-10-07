#!/usr/bin/env python3
"""Runde 8, Karte GF-BIC, Nachtrag B (PLAN.md): Breite einer psi_2-Resonanz entlang g bei festem omega^2
(Fortsetzung per Newton, lineare Extrapolation). Code begonnen 2026-09-30 06:32:12 CEST (date). Explorativ.
Importiert gfbic.py (unveraendert) und resonanz3d.py.
Kommando: gscan --w2 W --keim RE,IM --gliste g1,g2,...  (Keim gilt fuer das erste g)
"""
import argparse
import json
import math
import os
import sys
import traceback

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import torch  # noqa: E402

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import gfbic as G  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("kommando", choices=["gscan"])
    ap.add_argument("--w2", type=float, required=True)
    ap.add_argument("--keim", required=True)
    ap.add_argument("--gliste", required=True)
    ap.add_argument("--h", default="0.02,0.01", help="Stufen (Schiess-Schritt); zweite Stufe nur zum Nachpolieren")
    ap.add_argument("--frand", default="1e-6,1e-8")
    ap.add_argument("--iter", type=int, default=25)
    ap.add_argument("--out", default=None)
    ap.add_argument("--budget", type=float, default=540.0)
    a = ap.parse_args()
    torch.set_num_threads(1)
    dev = torch.device("cpu")
    budget = G.Budget(a.budget)
    out = a.out or os.path.join(HIER, "ausgabe-gscan")
    os.makedirs(out, exist_ok=True)
    kopf = (f"Runde 8 GF-BIC gscan Start {G.jetzt()}; gfbic_q3.py sha256 {G.sha256(os.path.abspath(__file__))[:16]}, "
            f"gfbic.py {G.sha256(G.__file__)[:16]}, resonanz3d.py {G.sha256(G.R3_PFAD)[:16]}; omega^2 = {a.w2}")
    zeilen = [kopf]
    print(kopf, flush=True)
    erg = {"argumente": vars(a), "start": G.jetzt(), "stufen": {}}
    rc = 0
    try:
        re_, im_ = [float(x) for x in a.keim.split(",")]
        gl = [float(x) for x in a.gliste.split(",")]
        hs = [float(x) for x in a.h.split(",")]
        fr = [float(x) for x in a.frand.split(",")]
        for h, frand in zip(hs, fr):
            if not budget.ok(f"Stufe h = {h}", 40.0):
                continue
            prof, mom = G.profil_momente(a.w2, 0.5 * h, dev)
            B = G.basis(prof, h, frand, dev)
            spur = []
            vor = [complex(re_, im_)]
            if h != hs[0] and hs[0] in [float(k) for k in erg["stufen"]]:
                # zweite Stufe: alle Punkte der ersten als Keime, in einem Stapel
                erste = erg["stufen"][str(hs[0])]
                keime = [complex(p["nu"][0], p["nu"][1]) for p in erste]
                gg = [p["g"] for p in erste]
                nw = G.newton_g(B, "psi2", keime, gg, iters=a.iter)
                for g, w_ in zip(gg, nw):
                    spur.append({"g": g, "nu": [w_["nu"].real, w_["nu"].imag], "absD": w_["absD"],
                                 "konv": w_["konvergiert"]})
                    zeilen.append(f"  h {h}: g = {g:.4f}: nu = {G.fz(w_['nu'], 10)}, |D| {w_['absD']:.1e}, "
                                  f"konv {w_['konvergiert']}")
            else:
                for i, g in enumerate(gl):
                    if not budget.ok(f"g = {g}", 15.0):
                        break
                    if len(vor) >= 2 and i >= 2:
                        k = vor[-1] + (vor[-1] - vor[-2]) * (g - gl[i - 1]) / (gl[i - 1] - gl[i - 2])
                    else:
                        k = vor[-1]
                    w_ = G.newton_g(B, "psi2", [k], [g], iters=a.iter)[0]
                    spur.append({"g": g, "nu": [w_["nu"].real, w_["nu"].imag], "absD": w_["absD"],
                                 "konv": w_["konvergiert"]})
                    zeilen.append(f"  h {h}: g = {g:.4f}: nu = {G.fz(w_['nu'], 10)}, |D| {w_['absD']:.1e}, "
                                  f"konv {w_['konvergiert']} ({G.uhr():.0f} s)")
                    if w_["konvergiert"] and w_["absD"] < 1e-8:
                        vor.append(w_["nu"])
            erg["stufen"][str(h)] = spur
            with open(os.path.join(out, "gscan.json"), "w") as fh:
                json.dump(G.jsonfest(erg), fh, indent=1)
    except Exception:                                     # noqa: BLE001
        tb = traceback.format_exc()
        zeilen.append("FEHLER:\n" + tb)
        erg["fehler"] = tb
        rc = 1
    zeilen.append(f"Ende {G.jetzt()}, {G.uhr():.1f} s; entfallen: {budget.abgebrochen or 'nichts'}")
    with open(os.path.join(out, "gscan.json"), "w") as fh:
        json.dump(G.jsonfest(erg), fh, indent=1)
    with open(os.path.join(out, "gscan_bericht.txt"), "w") as fh:
        fh.write("\n".join(zeilen) + "\n")
    print("\n".join(zeilen[1:]), flush=True)
    sys.exit(rc)


if __name__ == "__main__":
    main()
