#!/usr/bin/env python3
"""STRING-1 (Runde 35), NACHTRAEGLICH und nur beschreibend (nicht eingefroren, aendert kein Urteil):
1. Fensterabhaengigkeit der Ausgleiche (r_min, r_max) fuer alle vier Wurm-Faelle auf beiden L.
2. Fehlerpruefung: Jackknife mit 50 Bloecken gegen 25 zusammengelegte Bloecke (Autokorrelation).
3. Lokaler Exponent a(r) aus drei benachbarten Punkten (String-Form exakt durch r-1, r, r+1).
Aufruf: empfindlichkeit.py <laufordner> <ausgabe.json>
"""
import sys, os, json
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from auswertung import wurm_daten, ausgleich, jkf  # eingefrorene Routinen wiederverwenden


def daten_zusammengelegt(npz, faktor):
    axz = npz["axz"]
    B = axz.shape[0] // faktor * faktor
    neu = axz[:B].reshape(B // faktor, faktor, -1).sum(axis=1)
    return {"axz": neu, "nvec": npz["nvec"], "w_ax": npz["w_ax"]}


def main():
    lauf, aus = sys.argv[1], sys.argv[2]
    erg = {"hinweis": "nachtraeglich, nur beschreibend"}
    for d, K, Ls in [(2, 2.5, (64, 128)), (2, 0.5, (64, 128)), (3, 4.5, (24, 32)), (3, 1.5, (24, 32))]:
        for L in Ls:
            p = os.path.join(lauf, "w_d%d_L%d_K%s.npz" % (d, L, K))
            if not os.path.exists(p):
                continue
            npz = np.load(p)
            w = wurm_daten(npz)
            e = {"fenster": [], "fehler_50_gegen_25": None, "a_lokal": []}
            rmaxs = sorted(set([L // 8, L // 4, 3 * L // 8]))
            for rmin in (1, 2, 3, 4):
                for rmax in rmaxs:
                    r = np.arange(rmin, rmax + 1)
                    if len(r) < 4:
                        continue
                    if not (np.all(np.isfinite(w["y"][r])) and np.all(w["Sjk_min"][r] > 0)):
                        continue
                    z = {"rmin": int(rmin), "rmax": int(rmax)}
                    for form in ("string", "log", "coulomb", "linear"):
                        f = ausgleich(form, r, w["y"][r], w["sy"][r], w["yjk"][:, r])
                        z[form] = {"param": f["param"], "fehler": f["fehler"], "aic": f["aic"], "chi2": f["chi2"]}
                    e["fenster"].append(z)
            w25 = wurm_daten(daten_zusammengelegt(npz, 2))
            rr = np.arange(1, L // 4 + 1)
            e["fehler_50_gegen_25"] = {"r": rr.tolist(), "sy50": w["sy"][rr].tolist(), "sy25": w25["sy"][rr].tolist(),
                                       "verhaeltnis_mittel": float(np.mean(w25["sy"][rr] / w["sy"][rr]))}
            for r0 in range(2, L // 2 - 1):
                r = np.array([r0 - 1, r0, r0 + 1])
                if r0 - 1 < 1 or not np.all(np.isfinite(w["y"][r])):
                    continue
                X = np.stack([r, np.log(r), np.ones(3)], 1).astype(float)
                b = np.linalg.solve(X, w["y"][r])
                bj = np.array([np.linalg.solve(X, yy[r]) for yy in w["yjk"]])
                e["a_lokal"].append({"r": int(r0), "a": float(b[1]), "fehler": float(jkf(bj)[1]), "inv_xi": float(b[0])})
            erg["d%d_K%s_L%d" % (d, K, L)] = e
    with open(aus, "w") as f:
        json.dump(erg, f, indent=1)
    print("fertig")


if __name__ == "__main__":
    main()
