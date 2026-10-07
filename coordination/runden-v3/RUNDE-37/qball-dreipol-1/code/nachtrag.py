#!/usr/bin/env python3
# QBALL-DREIPOL-1, NACHTRAG (nach Sicht der Hauptwerte geschrieben, ohne Urteil; aendert keine Regel und keinen
# eingefrorenen Code). Frage: Verlagert die Stiftrelaxation in Modus b Ladung von einem Ball in den anderen?
# Die Stifte halten nur den Schwerpunkt jeder Komponente fest. Gemessen wird je Endzustand der Anteil von
# |psi_1|^2 auf der Seite des anderen Balls (x < 0; Ball 1 sitzt bei +d/2) und umgekehrt, eingespannt gegen
# relaxiert. Rechenweg identisch zu dreipol.modus_b (gleiche Funktionen und Parameter).
import sys, json, time, math
import numpy as np
sys.path.insert(0, "/home/fmh/fmhc-physics-remote/runde42-qball-dreipol/code")
import dreipol as dp

out = {"zweck": "Nachtrag ohne Urteil: Ladungsverlagerung in der Stiftrelaxation", "start_utc": dp.jetzt(),
       "faelle": []}
G = dp.Gitter(256, 64.0)
rad = dp.Radial()
faelle = [(-0.1, 2.0), (0.0, 2.0), (0.1, 2.0), (0.1, 4.0)]
for g4, x in faelle:
    t0 = time.time()
    psi1, ball = dp.ein_pol_ball(G, rad, g4, 60.0)
    F1 = G.fft(psi1)
    R = ball["R_halb"]
    d = x * R
    A = G.shiftF(F1, 0.5 * d, 0.0)
    B = G.shiftF(F1, -0.5 * d, 0.0)
    z3 = np.zeros_like(A)
    P = np.stack([A, B, z3])
    Qv = np.array([60.0, 60.0, 0.0])
    E_ein = dp.energie_Q(G, P, Qv, g4)[0] - 2.0 * ball["E"]
    Pr, info = dp.fluss(G, P, Qv, g4, nmax=4000, tolE=1e-11, pins=[(0.5 * d, 0.0), (-0.5 * d, 0.0), None],
                        wand=60.0)
    E_rel = dp.energie_Q(G, Pr, Qv, g4)[0] - 2.0 * ball["E"]

    def anteile(Z):
        n2 = Z.real ** 2 + Z.imag ** 2
        links = G.X < 0.0
        f12 = float(n2[0][links].sum() / n2[0].sum())
        f21 = float(n2[1][~links].sum() / n2[1].sum())
        # Hoechstwert jeder Komponente am eigenen und am fremden Platz (Kreis vom Radius R um den Platz)
        def maxkreis(k, xc):
            m = ((G.X - xc) ** 2 + G.Y ** 2) < R * R
            return float(n2[k][m].max())
        return dict(fremdanteil_1=f12, fremdanteil_2=f21, max1_eigen=maxkreis(0, 0.5 * d),
                    max1_fremd=maxkreis(0, -0.5 * d), max2_eigen=maxkreis(1, -0.5 * d),
                    max2_fremd=maxkreis(1, 0.5 * d), S_max=float(n2.sum(0).max()))
    f = dict(g4=g4, d_R=x, d=d, R_halb=R, E_int_eingespannt=E_ein, E_int_relaxiert=E_rel, status=info["status"],
             it=info["it"], sek=time.time() - t0, eingespannt=anteile(P), relaxiert=anteile(Pr),
             schwerpunkte_relaxiert=dp.schwerpunkte(G, Pr.real ** 2 + Pr.imag ** 2))
    out["faelle"].append(f)
    print(json.dumps(f), flush=True)
out["ende_utc"] = dp.jetzt()
with open(sys.argv[1] + ".tmp", "w") as fh:
    json.dump(out, fh, indent=1)
import os
os.replace(sys.argv[1] + ".tmp", sys.argv[1])
