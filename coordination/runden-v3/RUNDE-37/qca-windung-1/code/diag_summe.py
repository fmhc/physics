#!/usr/bin/env python3
# QCA-WINDUNG-1, Diagnose NACH dem Einfrieren (aendert kein Urteil): Kreuzen sich bei K4_direkte_Summe_0 die Baender der
# zwei entkoppelten Bloecke auf Flaechen (Kodimension 1) statt in Punkten? Mass: Anteil der Gitterpunkte, an denen eine
# Eigenphase von Block 1 einer von Block 2 naeher als eps kommt. Flaechen: Anteil ~ eps; Punkte: Anteil ~ eps^3.
# Start nur auf der .69 ueber kleintest.sh: diag_summe.py --ein ref_rueck/haupt_0.json --out DATEI.json
import argparse
import json

import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("--ein", required=True)
ap.add_argument("--out", required=True)
args = ap.parse_args()
J = json.load(open(args.ein))
r = J["teil0"]["konstruktionen"]["K4_direkte_Summe_0"]["repr"]
A = np.array(r["A"]["re"]) + 1j * np.array(r["A"]["im"])
F = np.array(r["freqs"], float)
off = float(max(np.abs(A[:, :4, 4:]).max(), np.abs(A[:, 4:, :4]).max()))
B = np.pi * np.array([[1, 1, 0], [1, 0, 1], [0, 1, 1]], float).T
N = 48
t1 = (np.arange(N) + 0.37) / N
T = np.stack(np.meshgrid(t1, t1, t1, indexing="ij"), -1).reshape(-1, 3)
u = T @ B.T
U = (np.exp(1j * (u @ F.T)) @ A.reshape(len(F), 64)).reshape(-1, 8, 8)
p1 = np.angle(np.linalg.eigvals(U[:, :4, :4]))
p2 = np.angle(np.linalg.eigvals(U[:, 4:, 4:]))
d = np.abs(np.angle(np.exp(1j * (p1[:, :, None] - p2[:, None, :])))).min(axis=(1, 2))
d1 = np.sort(np.abs(np.angle(np.exp(1j * (p1[:, :, None] - p1[:, None, :])))) + 10 * np.eye(4), axis=2)[:, :, 0].min(axis=1)
out = {"block_ausserdiag_max": off, "gitter": N, "min_abstand_zwischen_bloecken": float(d.min()),
       "anteil": {str(e): float((d < e).mean()) for e in (0.2, 0.1, 0.05, 0.02, 0.01)},
       "anteil_innerhalb_block1": {str(e): float((d1 < e).mean()) for e in (0.2, 0.1, 0.05, 0.02, 0.01)}}
json.dump(out, open(args.out, "w"), indent=1)
print(json.dumps(out))
