#!/usr/bin/env python3
# QCA-TETRA-1, Runde 37: Bild zu Teil C aus mehreren C-Laeufen.
# Aufruf (nur ueber kleintest.sh auf der .69): bild_c.py OUT.png C_a.json [C_b.json ...]
import json
import sys

import numpy as np

import qca_tetra as q


def main():
    out = sys.argv[1]
    statsC = {"C1": {}, "C2": {}}
    best = {"C1": (np.inf, None), "C2": (np.inf, None)}
    for p in sys.argv[2:]:
        d = json.load(open(p))
        for f in ("C1", "C2"):
            statsC[f].update(d["teil_C"][f])
            b = d["teil_C_bester"][f]
            if b is not None and b["D"] < best[f][0]:
                best[f] = (b["D"], np.array(b["A_re"]) + 1j * np.array(b["A_im"]))
    names = [n for n in statsC["C1"] if n in statsC["C2"]]
    statsC = {f: {n: statsC[f][n] for n in names} for f in ("C1", "C2")}
    q.bild_C(statsC, best["C1"][1], best["C2"][1], q.Composite(), out)
    print("bild", out, {f: best[f][0] for f in best}, flush=True)


if __name__ == "__main__":
    main()
