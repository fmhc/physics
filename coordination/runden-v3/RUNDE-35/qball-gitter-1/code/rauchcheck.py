# QBALL-GITTER-1: Rauch-Kurzauswertung (nur Rauch): G0-Groessen und Vorzeichen/Formel gamma M v = Q E t.
import sys, json
import numpy as np
import auswertung as aw

ordner = sys.argv[1]
out = {}
for name in sys.argv[2:]:
    d = aw.lade(ordner, name)
    if d is None:
        out[name] = "fehlt"; continue
    k = d["kopf"]; t = d["t"]
    r = dict(status=k["status"], wand_s=round(k["wandzeit_s"], 2), N=k["N"], dt=k["dt"], M0=k["M0"], Q0=k["Q0"], E=k["E"])
    r["drift_max"] = float(np.max(np.abs(d["X"] - d["X"][0])))
    r["dQ_rel"] = float(np.max(np.abs(d["Qdom"] - d["Qdom"][0])) / d["Qdom"][0])
    r["dH_rel"] = float(np.max(np.abs(d["H"] - d["H"][0])) / d["H"][0])
    bil = d["H"] + d["Eabs"] + d["Edrop"] - d["H"][0] - d["W"]
    r["bilanz_E_rel"] = float(np.max(np.abs(bil)) / k["M0"])
    r["bilanz_Q_rel"] = float(np.max(np.abs(d["Qdom"] + d["Qabs"] + d["Qdrop"] - d["Qdom"][0])) / k["Q0"])
    r["n0_ende"] = float(d["n0"][-1]); r["X_ende"] = float(d["X"][-1]); r["XE_ende"] = float(d["XE"][-1])
    if k["E"] > 0:
        v = aw.schnelle(t, d["X"], aw.TAU); g = aw.gamma_aus_v(v)
        tab = {}
        for tz in (20, 30, 50, 70, 90):
            if tz <= t[-1] - aw.TAU:
                i = int(round(tz / 0.5))
                tab[str(tz)] = dict(v=float(v[i]), gamma=float(g[i]),
                                    abw=float(g[i] * k["M0"] * v[i] / (k["Q0"] * k["E"] * t[i]) - 1),
                                    abwP=float(d["P"][i] / (k["Q0"] * k["E"] * t[i]) - 1))
        r["formel"] = tab
    out[name] = r
print(json.dumps(out, indent=1))
