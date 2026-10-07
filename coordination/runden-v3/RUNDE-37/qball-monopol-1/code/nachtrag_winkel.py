"""QBALL-MONOPOL-1, Nachtrag nach dem Hauptlauf (beschreibend, nicht geurteilt; nicht im eingefrorenen Plan):
punktweises Verhaeltnis f^2(r, theta -> 0)/f^2(r, pi/2) in den innersten r-Zellen der haftenden Zustaende (V0 = 2).
Erwartung [M]: -> 2 fuer r -> 0, weil die j = 1/2-Mode (r^0,366) vor j = 3/2 (r^1,45) dominiert.

Aufruf (nur ueber kleintest.sh): nachtrag_winkel.py lauf/haupt.npz lauf/haupt.json <ausgabe.json>
"""
import hashlib
import json
import os
import sys

import numpy as np

SKRIPT_SHA = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()


def main():
    npz = np.load(sys.argv[1])
    H = json.load(open(sys.argv[2]))
    r = npz["gitter_r"]
    t = npz["gitter_t"]
    nr, nt = len(r), len(t)
    j = nt // 2
    erg = {"skript_sha256": SKRIPT_SHA, "r": [float(x) for x in r[:12]], "faelle": []}
    for c in H["faelle"]:
        if c["V0"] != 2.0 or c["start"] != "A":
            continue
        F2 = (npz["f_V%s_Q%s_%s" % (c["V0"], int(c["Q"]), c["start"])] ** 2).reshape(nr, nt)
        f0 = (9 * F2[:, 0] - F2[:, 1]) / 8.0
        f90 = 0.5 * (F2[:, j - 1] + F2[:, j])
        erg["faelle"].append({"V0": c["V0"], "Q": c["Q"], "ratio_r": [float(x) for x in (f0 / f90)[:12]],
                              "ratio_r_1": float(np.interp(1.0, r, f0 / f90)),
                              "ratio_r_2": float(np.interp(2.0, r, f0 / f90))})
    with open(sys.argv[3], "w") as fh:
        json.dump(erg, fh, indent=1)
    print(json.dumps([[x["Q"], round(x["ratio_r"][0], 4), round(x["ratio_r_1"], 3)] for x in erg["faelle"]]))


if __name__ == "__main__":
    main()
