#!/usr/bin/env python3
# QBALL-DREIPOL-3, Nachtrag N1 nach Sicht der Hauptwerte (beschreibend, ohne Urteil, nicht eingefroren).
# Anlass: Beide Bisektionen brachen am ersten entmischten Zustand mit kleinstem Paarabstand < R ab (Ausgang "offen",
# Gestalt Zwischenform). Hier: Feinabtastung zwischen den Klammerenden mit einer Entmischungsregel statt der
# Dreiecksregel. Nutzt dreipol3.schritt und dreipol2 unveraendert (Import); neu ist nur dieser Ablauf.
# Aufruf: nachtrag3.py <out.json> <dim> <Q1,Q1,...> <wand_fluss> <zeitgrenze>
import sys, os, json, math, time, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import torch
import dreipol2 as d
import dreipol3 as d3

out_pfad, dim = sys.argv[1], int(sys.argv[2])
Qs = [float(q) for q in sys.argv[3].split(",")]
wand, zeitgrenze = float(sys.argv[4]), float(sys.argv[5])
d.GERAET = d.geraet()
if dim == 3:   # wie Hauptlauf bisekt3 (PLAN 3), nur laengere Wandzeit je Fluss
    a = argparse.Namespace(g4=-0.1, N=80, L=48.0, dr=0.01, rmax=60.0, tol_ball=1e-6, nmax_ball=20000,
                           wand_ball=90.0, wand_rad=60.0, tol=1e-6, nfluss=400000, alle=50, wand_fluss=wand, beta=1.5)
else:          # wie Hauptlauf bisekt2
    a = argparse.Namespace(g4=-0.1, N=256, L=64.0, dr=0.01, rmax=60.0, tol_ball=1e-8, nmax_ball=6000,
                           wand_ball=120.0, wand_rad=60.0, tol=1e-7, nfluss=400000, alle=50, wand_fluss=wand, beta=1.5)
t0 = time.time()
G = d.Gitter(a.N, a.L, dim)
rad = d.Radial(dim, dr=a.dr, rmax=a.rmax)
out = dict(modus="nachtrag3", geraet=d.GERAET, dim=dim, N=a.N, L=a.L, h=G.h, g4=a.g4, Q_liste=Qs, wand_fluss=wand,
           regel="entmischt: konvergiert, groesster Paarabstand >= 0,01 R und E_Ende < E_Misch; verschmolzen: "
                 "konvergiert und groesster Paarabstand < 0,01 R; sonst offen (beschreibend)",
           start_utc=d.jetzt(), schritte=[])
snaps = {}
for i, q in enumerate(Qs):
    if time.time() - t0 > zeitgrenze:
        out["schritte"].append(dict(Q1=q, status="nicht gerechnet (zeitgrenze)"))
        continue
    s = d3.schritt(G, rad, a, q, t0, snaps, "n%d" % i)
    s["rolle"] = "nachtrag"
    for teil in ("beruehrend", "sektor"):
        x = s[teil]
        pa = x["ende"]["paarabstand"]
        konv = x["status"] == "konvergiert"
        if konv and max(pa) < 0.01 * s["R_halb"]:
            k = "verschmolzen"
        elif konv and x["ende"]["E"] < s["vorab"]["E_Misch"]:
            k = "entmischt"
        else:
            k = "offen"
        x["entmischung"] = k
    print("nachtrag Q1=%g: beruehrend %s, sektor %s" % (q, s["beruehrend"]["entmischung"],
                                                         s["sektor"]["entmischung"]), flush=True)
    out["schritte"].append(s)
    d.schreibe(out_pfad, out)
np.savez_compressed(out_pfad.replace(".json", "_bilder.npz"), x=(G.x if dim == 3 else G.x[::2]), **snaps)
out["sek"] = time.time() - t0
out["ende_utc"] = d.jetzt()
d.schreibe(out_pfad, out)
