#!/usr/bin/env python3
"""REGGE-ZEIT-1, Rauchlauf 0 (nur Struktur, vor dem Einfrieren): Wirkt die Hyperdiagonale auf die Fehlwinkel?
Und: Gelenktypen, Laufzeit von Weg T. Keine Quelle, keine Loesung, keine Urteilsgroesse.
Aufruf: python rauch0_struktur.py <ausgabe.json>
"""
import json
import sys
import time

import numpy as np

sys.path.insert(0, __file__.rsplit("/", 1)[0])
import regge4d as R4  # noqa: E402


def main():
    t0 = time.time()
    git = R4.Gitter(4, 4)
    eT, fehler, betroffen = git.ableitung_T()
    t1 = time.time()
    out = {"laufzeit_T_s": t1 - t0, "fehler_T": fehler, "betroffen_je_kantentyp": betroffen,
           "kanten": [list(map(int, d)) for d in git.dirs], "top": int(git.top),
           "gelenktypen": [[list(map(int, s)) for s in t] for t in git.gtypen]}
    # Spalte top von E(k): bei k = 0 und einigen statischen k
    ks = np.array([[0, 0, 0, 0], [0, 0.2, 0, 0], [0, 0.2, 0.2, 0], [0, 0.5, 0.3, 0.1], [0.3, 0.1, 0.2, 0.4]], float)
    Am, Em, M = git.matrizen(ks, eT)
    out["E_top_norm"] = [float(np.linalg.norm(Em[i][:, git.top])) for i in range(len(ks))]
    out["E_norm"] = [float(np.linalg.norm(Em[i])) for i in range(len(ks))]
    out["A_top_norm"] = [float(np.linalg.norm(Am[i][:, git.top])) for i in range(len(ks))]
    out["M_top_norm"] = [float(np.linalg.norm(M[i][:, git.top])) for i in range(len(ks))]
    # Eichmoden: E g = 0?
    res = []
    for i, k in enumerate(ks):
        G = git.eich_basis(k)
        res.append(float(np.linalg.norm(Em[i] @ G) / (np.linalg.norm(Em[i]) * max(np.linalg.norm(G), 1e-300))))
    out["E_eich_rel"] = res
    # Welche Gelenktypen sieht top bei k = 0 (Betrag)?
    out["E0_top_je_gelenktyp"] = [float(x) for x in np.abs(Em[0][:, git.top])]
    print(json.dumps({k: out[k] for k in ("laufzeit_T_s", "E_top_norm", "E_norm", "A_top_norm", "M_top_norm",
                                          "E_eich_rel")}))
    with open(sys.argv[1], "w") as f:
        json.dump(out, f, indent=1)


if __name__ == "__main__":
    main()
