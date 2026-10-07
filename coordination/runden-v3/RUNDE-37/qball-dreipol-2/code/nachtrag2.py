#!/usr/bin/env python3
# QBALL-DREIPOL-2, Nachtrag N2 nach Sicht der Hauptwerte (ohne Urteil): Das 2D-Dreieck (g4 = -0,1, Q1 = 60) mit
# Zufallsstoerungen in allen Richtungen statt sechs gewaehlten. Nutzt den eingefrorenen Code dreipol2.py unveraendert
# (Import); neu ist nur dieser Ablauf. Aufruf: nachtrag2.py <out.json>
import sys, os, json, math, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import torch
import dreipol2 as d

t0 = time.time()
d.GERAET = d.geraet()
out_pfad = sys.argv[1]
G = d.Gitter(256, 64.0, 2)
rad = d.Radial(2)
g4, Q1 = -0.1, 60.0
psi1, ball = d.ein_pol_ball(G, rad, g4, Q1)
R = ball["R_halb"]
F1 = G.fft(psi1)
pos, rho = d.dreieck_pos(G, 2.0 * R)
P = torch.stack([G.shiftF(F1, p) for p in pos])
Q = [Q1, Q1, Q1]
Pf, i1 = d.fluss(G, P, Q, g4, nmax=12000, tol=1e-7, wand=170.0)
Pref, i2 = d.fluss(G, Pf, Q, g4, nmax=8000, tol=1e-9, wand=120.0)
ref = dict(Q=Q, status=i2["status"], **d.zustand_info(G, Pref, Q, g4, R))
out = {"modus": "nachtrag2", "geraet": d.GERAET, "start_utc": d.jetzt(), "R": R, "referenz": ref, "laeufe": []}
print("referenz", ref["E"], ref["res"], ref["paarabstand_R"], f"t={time.time() - t0:.0f}s", flush=True)
env = torch.sqrt(d.n2von(Pref).sum(0))
for saat in (11, 12, 13):
    rng = np.random.default_rng(saat)
    for art, eps, verschieb in (("rauschen5", 0.05, 0.0), ("rauschen20", 0.20, 0.0), ("verschieb15+rauschen5", 0.05, 0.15)):
        eta = d.rauschfeld(G, saat * 10 + int(100 * eps))
        P0 = Pref + eps * eta * env[None]
        if verschieb > 0:
            F0 = G.fft(P0)
            for a in range(3):
                w = rng.uniform(0.0, 2.0 * math.pi)
                P0[a] = G.shiftF(F0[a], [verschieb * R * math.cos(w), verschieb * R * math.sin(w)])
        start = d.zustand_info(G, P0, Q, g4, R, ref=ref)
        bo = d.beobachter(G, ref["schwerpunkte"], R)
        Pe, info = d.fluss(G, P0, Q, g4, nmax=30000, tol=1e-8, wand=45.0, beob=bo)
        ende = d.zustand_info(G, Pe, Q, g4, R, ref=ref)
        z = dict(saat=saat, art=art, eps=eps, verschieb_R=verschieb, status=info["status"], it=info["it"],
                 sek=info["sek"], start={k: start[k] for k in ("E", "dE", "d_rms_R", "d_form_R", "reinheit", "res")},
                 ende={k: ende[k] for k in ("E", "dE", "d_rms_R", "d_form_R", "reinheit", "res", "paarabstand_R")})
        out["laeufe"].append(z)
        print(f"{saat} {art}: {info['status']} it={info['it']} d_rms {start['d_rms_R']:.4f} -> {ende['d_rms_R']:.2e} "
              f"d_form {start['d_form_R']:.4f} -> {ende['d_form_R']:.2e} dE {start['dE']:.3e} -> {ende['dE']:.2e} "
              f"t={time.time() - t0:.0f}s", flush=True)
        d.schreibe(out_pfad, out)
out["sek"] = time.time() - t0
out["ende_utc"] = d.jetzt()
d.schreibe(out_pfad, out)
