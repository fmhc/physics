#!/usr/bin/env python3
"""V-1-PRAEZISION (Runde 37): Zusatzauswertung, beschreibend, kein Urteil (nach dem Einfrieren geschrieben).
- Hintergrund-Schwanz T(eps) des Kartenmodells gegen exp(-pi k0)
- Kanalweise Ausgleiche (A neu, B neu) mit eigenem K
- Reihe D (f0-Hintergrund): F1 und FK
Aufruf: python zusatz.py <lauf-ordner>
"""
import json
import math
import os
import sys

import numpy as np

ORD = sys.argv[1] if len(sys.argv) > 1 else "lauf"
EPS_LISTE = ["m1e-2", "m7e-3", "m5e-3", "m4e-3", "m3e-3", "m2e-3"]


def lade(name):
    p = os.path.join(ORD, name + ".json")
    if not os.path.exists(p):
        return None
    with open(p) as fh:
        d = json.load(fh)
    return d if "streuung" in d and "0" in d["streuung"] else None


def epsw(e):
    return (-1.0 if e[0] == "m" else 1.0) * float(e[1:])


def fit(X, y):
    X, y = np.asarray(X, float), np.asarray(y, float)
    b, *_ = np.linalg.lstsq(X, y, rcond=None)
    r = y - X @ b
    return b.tolist(), r.tolist(), float(np.max(np.abs(r)))


out = {}
for modell in ("K", "D"):
    rows = []
    for e in EPS_LISTE:
        d = lade(f"{modell}_H_{e}")
        if d is None:
            continue
        s0 = d["streuung"]["0"]
        ka = s0["kanaele_aus"]
        row = {"e": e, "ae": abs(epsw(e)), "lnP": float(s0["ln_P_neu_aus"]),
               "lnPA": math.log(float(ka["A-neu-aus"]["T"])), "lnPB": math.log(float(ka["B-neu-aus"]["T"])),
               "K_A": float(d["K_rho_z"]["A-neu"]), "K_B": float(d["K_rho_z"]["B-neu"]),
               "K_e1": float(d["K_rho_z"]["e1-neu"]), "K_e2": float(d["K_rho_z"]["e2-neu"]),
               "anteil_B": float(ka["B-neu-aus"]["T"]) / float(s0["P_neu_aus"]),
               "P_innen_durch_aus": float(s0["P_neu_innen"]) / float(s0["P_neu_aus"])}
        if modell == "K":
            hd = d["hintergrund"]
            k0 = float(complex(hd["lam_moden"][2].replace(" ", "")).imag)
            row.update({"k0": k0, "T_schwanz": float(hd["koeff_moden"][2]),
                        "wachsend_bei_L": float(hd["koeff_moden"][0])})
            row["T_mal_exp_pi_k0"] = row["T_schwanz"] * math.exp(math.pi * k0)
        rows.append(row)
    if len(rows) < 3:
        continue
    ae = np.array([r["ae"] for r in rows])
    one = np.ones(len(rows))
    u = 1 / np.sqrt(ae)
    res = {"punkte": [r["e"] for r in rows], "zeilen": rows}
    y = np.array([r["lnP"] for r in rows])
    res["F1"] = fit(np.c_[one, np.log(ae), -u], y)
    res["F0"] = fit(np.c_[one, -u], y)
    for nm in ("A", "B"):
        yk = np.array([r[f"lnP{nm}"] for r in rows])
        Kk = np.array([r[f"K_{nm}"] for r in rows])
        res[f"kanal_{nm}_FK"] = fit(np.c_[one, np.log(ae), -2 * Kk], yk)
        res[f"kanal_{nm}_F1"] = fit(np.c_[one, np.log(ae), -u], yk)
    if modell == "K":
        yT = np.array([math.log(r["T_schwanz"]) for r in rows])
        k0 = np.array([r["k0"] for r in rows])
        res["schwanz_q_frei"] = fit(np.c_[one, np.log(ae), -k0], yT)
        res["schwanz_q0"] = fit(np.c_[one, -k0], yT)
    out[modell] = res

with open(os.path.join(ORD, "zusatz.json"), "w") as fh:
    json.dump(out, fh, indent=1)
for m, r in out.items():
    print(m, "F1 [a, q, c] =", r["F1"][0], "max Rest", r["F1"][2])
    print(m, "F0 [a, c] =", r["F0"][0], "max Rest", r["F0"][2])
    for nm in ("A", "B"):
        print(m, f"Kanal {nm} FK [a, q, d] =", r[f"kanal_{nm}_FK"][0], "max Rest", r[f"kanal_{nm}_FK"][2])
    if "schwanz_q_frei" in r:
        print(m, "Schwanz [a, q, d] =", r["schwanz_q_frei"][0], "max Rest", r["schwanz_q_frei"][2])
        print(m, "Schwanz q0 [a, d] =", r["schwanz_q0"][0], "max Rest", r["schwanz_q0"][2])
