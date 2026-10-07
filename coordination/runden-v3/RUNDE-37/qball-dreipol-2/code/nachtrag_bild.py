#!/usr/bin/env python3
# QBALL-DREIPOL-2, Bild zum Nachtrag N1 (ohne Urteil): Endzustaende des 3D-Dreiecksflusses bei g4 = -0,1 fuer
# Q1 = 200, 400, 800 (Nachtrag) und 2500 (Hauptlauf), Ebene z = 0. Aufruf: nachtrag_bild.py <laufordner>
import sys, os, json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

D = sys.argv[1]
reihen = [("nachtrag/B_m01_Q200", 200), ("nachtrag/B_m01_Q400", 400), ("nachtrag/B_m01_Q800", 800), ("B_m01", 2500)]
fig, axs = plt.subplots(2, 4, figsize=(15, 7.6))
for j, (stamm, Q) in enumerate(reihen):
    b = json.load(open(os.path.join(D, stamm + ".json")))
    z = np.load(os.path.join(D, stamm + "_bilder.npz"))
    x = z["x"]
    m = np.abs(x) <= 0.45 * b["L"]
    norm = float(z["start"].max())
    for i, k in enumerate(("start", "ende")):
        arr = z[k]
        rgb = np.clip(np.stack([arr[0], arr[1], arr[2]], -1) / norm, 0, 1)[np.ix_(m, m)]
        axs[i, j].imshow(np.transpose(rgb, (1, 0, 2)), origin="lower", extent=[x[m][0], x[m][-1]] * 2)
        e = b["fluss"]["ende"]
        if k == "start":
            axs[i, j].set_title("Q1 = %d, om = %.3f, Start (2R)" % (Q, b["ball"]["om"]), fontsize=9)
        else:
            axs[i, j].set_title("Ende: E - E_Misch = %+.2f, Paar %.2f R" % (e["E"] - b["mischball"]["E"],
                                                                       e["paarabstand_R"][0]), fontsize=9)
fig.suptitle("3D, g4 = -0,1, Ebene z = 0: Fluss bei festen Ladungen vom beruehrenden Dreieck "
             "(|phi_1|^2 rot, |phi_2|^2 gruen, |phi_3|^2 blau)", fontsize=10)
fig.tight_layout()
fig.savefig(os.path.join(D, "nachtrag", "teilB_ladungsreihe.png"), dpi=100)
print("geschrieben")
