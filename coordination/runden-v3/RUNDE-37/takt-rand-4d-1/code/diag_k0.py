#!/usr/bin/env python3
# DIAGNOSE nach dem Einfrieren (aendert kein Urteil): Warum findet die Suche bei P4a keine Randknoten?
# Nutzt nur eingefrorene Funktionen aus takt4d.py. Aufruf ueber kleintest.sh: diag_k0.py --modell P4a --out DATEI.json
import argparse
import json
import sys

import numpy as np

import takt4d as T


def zustaende(model, k, wmax=0.6):
    U = model.U(np.asarray(k, float)[None, :])[0]
    ph, Z, wt = T.eigen_rand(U, model.ptop)
    o = np.argsort(np.abs(ph))
    out = []
    for i in o:
        if abs(ph[i]) < wmax:
            prof = np.sum(np.abs(Z[:, i].reshape(model.L, 4)) ** 2, axis=1)
            out.append({"phase": float(ph[i]), "wt_oben": float(wt[i]), "lage_max": int(np.argmax(prof)),
                        "profil": np.round(prof, 4).tolist()})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--modell", default="P4a")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    tau, M, ordnung, L = T.MODELLE[a.modell]
    model = T.Plan4D(tau, M, ordnung, L)
    vol = T.volumen_4d(model, N=20)
    fns = T.fenster_fns(vol)
    res = {"volumen": vol, "fenster": {g: (0.97 * vol["halb_0"] if g == "0" else 0.97 * vol["halb_pi"]) for g in fns}}
    # Volumenphasen an k = 0 (4D, k4 = 0 und pi) und die Lage der Luecke um 0 (beide Kanten)
    g = -np.pi + 2 * np.pi * np.arange(20) / 20
    K = np.stack(np.meshgrid(g, g, g, g, indexing="ij"), -1).reshape(-1, 4)
    ph = np.angle(np.linalg.eigvals(model.U4(K))).ravel()
    res["volumen_kante_unten"] = float(ph[ph < 0].max()) if np.any(ph < 0) else None
    res["volumen_kante_oben"] = float(ph[ph > 0].min()) if np.any(ph > 0) else None
    res["k0"] = zustaende(model, [0.0, 0.0, 0.0])
    res["k01"] = zustaende(model, [0.1, 0.0, 0.0])
    res["kpi"] = zustaende(model, [np.pi, np.pi, np.pi])
    # Paar und Newton an k = 1e-9 fuer beide Raender
    for r in ("oben", "unten"):
        for gname, (fn, c) in fns.items():
            p = T.paar(model, np.array([1e-9, 1e-9, 1e-9]), r, fn, c)
            res[f"paar_{r}_{gname}"] = None if p is None else {"phc": p["phc"], "spalt": p["spalt"], "wt": p["wt"],
                                                                "b": p["b"].tolist(), "M": p["M"].tolist()}
            n = T.newton(model, np.array([0.05, -0.03, 0.02]), r, fn, c)
            res[f"newton_{r}_{gname}"] = n
    with open(a.out, "w") as fh:
        json.dump(res, fh, indent=1, default=lambda o: o.tolist() if hasattr(o, "tolist") else str(o))
    print("fertig", flush=True)


if __name__ == "__main__":
    sys.exit(main())
