#!/usr/bin/env python3
"""V-1-PRAEZISION (Runde 37): mechanische Auswertung nach PLAN.md Abschnitte 4 bis 6.
Liest lauf/<M>_<C>_<eps>.json (M = K Kartenmodell, D f0-Hintergrund; C = H, G, S, R), schreibt lauf/auswertung.json
und lauf/bild_lnP.svg.
Aufruf: python auswertung.py <lauf-ordner>
"""
import glob
import json
import math
import os
import sys

import numpy as np

ORD = sys.argv[1] if len(sys.argv) > 1 else "lauf"
EPS_LISTE = ["m1e-2", "m7e-3", "m5e-3", "m4e-3", "m3e-3", "m2e-3"]
PFLICHT = ["m1e-2", "m7e-3", "m5e-3", "m4e-3", "m3e-3"]
P_REF = 9.378187026973642e-17          # V-1-WEITER A_m1e-2x (gewertet), PLAN Abschnitt 6
P_REF_B = 8.811714585493334e-17        # V-1-WEITER B_m1e-2x
P_REF_D = 4.7479746866749636e-17       # V-1-WEITER D_m1e-2f0 (Diagnose, f0-Hintergrund)
OM = math.sqrt(0.75)


def lade(name):
    p = os.path.join(ORD, name + ".json")
    if not os.path.exists(p):
        return None
    with open(p) as fh:
        d = json.load(fh)
    return d if "streuung" in d and "0" in d["streuung"] else None


def epsw(e):
    return (-1.0 if e[0] == "m" else 1.0) * float(e[1:])


def lnP(d):
    s = d["streuung"]["0"].get("ln_P_neu_aus")
    return float(s) if s is not None else None


def info(d):
    s0 = d["streuung"]["0"]
    r = {"rho_z": d["rho_z"], "P_neu_aus": s0["P_neu_aus"], "ln_P": s0.get("ln_P_neu_aus"),
         "P_neu_innen": s0["P_neu_innen"], "T_alt_aus": s0["T_alt_aus"], "T_aus": s0["T_aus"],
         "flussbilanz": s0["flussbilanz"], "kanaele_aus": s0["kanaele_aus"], "taylor_rest_max": s0["taylor_rest_max"],
         "h": d["h"], "n_halb": d["n_halb"], "Kh": d["Kh"], "sek": d.get("sek"), "E_bei_rho_z": d.get("E_bei_rho_z"),
         "klammer": d.get("klammer"), "K_rho_z": d.get("K_rho_z"), "hintergrund": d.get("hintergrund")}
    for off, s in d["streuung"].items():
        if off != "0":
            r[f"P_neu_aus_bei_{off}"] = s["P_neu_aus"]
    return r


def ausgleich(X, y):
    X, y = np.asarray(X, float), np.asarray(y, float)
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    res = y - X @ beta
    return beta, res


out = {"urteile": {}, "tabelle": {}, "ausgleich": {}, "kontrollen": {}}

# ---------------- Tabelle und Aufloesung ----------------
punkte = []
for e in EPS_LISTE:
    H, G, S = lade(f"K_H_{e}"), lade(f"K_G_{e}"), lade(f"K_S_{e}")
    z = {"eps": epsw(e), "gerechnet": H is not None}
    if H is None:
        out["tabelle"][e] = z
        continue
    z["H"] = info(H)
    lh = lnP(H)
    z["ln_P_H"] = lh
    for nm, D in (("G", G), ("S", S)):
        if D is not None:
            z[nm] = {"ln_P": D["streuung"]["0"].get("ln_P_neu_aus"), "rho_z": D["rho_z"],
                     "flussbilanz": D["streuung"]["0"]["flussbilanz"]}
            l2 = lnP(D)
            z[f"rel_lnP_H_{nm}"] = abs(lh - l2) / abs(lh) if (lh is not None and l2 is not None) else None
            z[f"rho_z_H_minus_{nm}"] = float(H["rho_z"]) - float(D["rho_z"])
        else:
            z[f"rel_lnP_H_{nm}"] = None
    fb = abs(float(H["streuung"]["0"]["flussbilanz"]))
    z["aufgeloest"] = bool(lh is not None and z.get("rel_lnP_H_G") is not None and z["rel_lnP_H_G"] <= 1e-6
                           and z.get("rel_lnP_H_S") is not None and z["rel_lnP_H_S"] <= 1e-6 and fb < 1e-40)
    out["tabelle"][e] = z
    if z["aufgeloest"]:
        K = H["K_rho_z"]
        punkte.append({"e": e, "eps": epsw(e), "lnP": lh, "rho_z": float(H["rho_z"]),
                       "K_B": float(K["B-neu"]), "K_A": float(K["A-neu"])})

# Reihe D (beschreibend)
reiheD = {}
for e in EPS_LISTE:
    D = lade(f"D_H_{e}")
    if D is not None:
        reiheD[e] = info(D)
out["reihe_D"] = reiheD

# ---------------- Ausgleich ----------------
aufl = [p["e"] for p in punkte]
n = len(punkte)
out["ausgleich"]["punkte"] = aufl
pflicht_ok = all(e in aufl for e in PFLICHT)
if n >= 5:
    ae = np.array([abs(p["eps"]) for p in punkte])
    y = np.array([p["lnP"] for p in punkte])
    u = 1 / np.sqrt(ae)
    one = np.ones(n)
    # F1, F0
    b1, r1 = ausgleich(np.c_[one, np.log(ae), -u], y)
    b0, r0 = ausgleich(np.c_[one, -u], y)
    out["ausgleich"]["F1"] = {"a": b1[0], "q": b1[1], "c": b1[2], "reste": r1.tolist(), "max_rest": float(np.max(np.abs(r1)))}
    out["ausgleich"]["F0"] = {"a": b0[0], "c": b0[1], "reste": r0.tolist(), "max_rest": float(np.max(np.abs(r0)))}
    # Kanal-k-Varianten
    rz = np.array([p["rho_z"] for p in punkte])
    varianten = {
        "K_B": np.array([p["K_B"] for p in punkte]),
        "K_A": np.array([p["K_A"] for p in punkte]),
        "Karte_woertlich": np.sqrt((1 + np.sqrt(1 + 4 * ae * (rz ** 2 - 1))) / (2 * ae)),
        "Karte_vorzeichen_berichtigt": np.sqrt((1 + np.sqrt(1 - 4 * ae * (rz ** 2 - 1))) / (2 * ae)),
        "eins_durch_wurzel": u,
    }
    for nm, Kv in varianten.items():
        bk, rk = ausgleich(np.c_[one, np.log(ae), -2 * Kv], y)
        bk0, rk0 = ausgleich(np.c_[one, -2 * Kv], y)
        out["ausgleich"][f"FK_{nm}"] = {"a": bk[0], "q": bk[1], "d": bk[2], "d_durch_pi_minus_1": bk[2] / math.pi - 1,
                                        "reste": rk.tolist(), "max_rest": float(np.max(np.abs(rk))),
                                        "K": Kv.tolist(),
                                        "q0": {"a": bk0[0], "d": bk0[1], "d_durch_pi_minus_1": bk0[1] / math.pi - 1,
                                               "max_rest": float(np.max(np.abs(rk0)))}}
    # oertliche Werte (beschreibend): c zwischen Nachbarn
    lok = []
    for i in range(n - 1):
        lok.append({"zwischen": [punkte[i]["e"], punkte[i + 1]["e"]],
                    "c_lokal": float((y[i] - y[i + 1]) / (u[i + 1] - u[i]))})
    out["ausgleich"]["c_lokal_q0"] = lok

# ---------------- Urteile ----------------
# PR0
t = out["tabelle"]
teil_a = None
werte_a = {}
gerechnete = [e for e in EPS_LISTE if t[e].get("gerechnet")]
if gerechnete and all(t[e].get("rel_lnP_H_G") is not None for e in gerechnete):
    teil_a = all(t[e]["rel_lnP_H_G"] <= 1e-6 for e in gerechnete)
    werte_a = {e: t[e]["rel_lnP_H_G"] for e in gerechnete}
teil_b, werte_b = None, {}
if t["m1e-2"].get("gerechnet"):
    PH = float(t["m1e-2"]["H"]["P_neu_aus"])
    werte_b = {"P_H": PH, "P_ref": P_REF, "rel": PH / P_REF - 1, "rel_zu_B": PH / P_REF_B - 1}
    teil_b = abs(PH / P_REF - 1) <= 0.05
Hp, Gp = lade("D_H_p3e-3"), lade("D_G_p3e-3")
teil_c, werte_c = None, {}
if Hp is not None:
    TH = float(Hp["streuung"]["0"]["T_aus"])
    werte_c = {"T_aus_H": Hp["streuung"]["0"]["T_aus"], "rho_z_H": Hp["rho_z"], "E_bei_rho_z": Hp["E_bei_rho_z"],
               "klammer": Hp["klammer"], "flussbilanz": Hp["streuung"]["0"]["flussbilanz"]}
    if Gp is not None:
        werte_c.update({"T_aus_G": Gp["streuung"]["0"]["T_aus"], "rho_z_G": Gp["rho_z"]})
    teil_c = TH < 1e-60
if None in (teil_a, teil_b, teil_c):
    u0 = "nicht auswertbar"
else:
    u0 = "eingetroffen" if (teil_a and teil_b and teil_c) else "nicht eingetroffen"
out["urteile"]["PR0"] = {"urteil": u0, "werte": {"a_genauigkeiten_rel_lnP": werte_a, "b_m1e-2": werte_b,
                                                  "c_p3e-3_f0": werte_c, "teile": [teil_a, teil_b, teil_c]}}
if n >= 5:
    c = out["ausgleich"]["F1"]["c"]
    out["urteile"]["PR1"] = {"urteil": "eingetroffen" if 6.22 <= c <= 6.35 else "nicht eingetroffen",
                             "werte": {"c": c, "q": out["ausgleich"]["F1"]["q"], "punkte": aufl}}
    fk = out["ausgleich"]["FK_K_B"]
    out["urteile"]["PR2"] = {"urteil": "eingetroffen" if abs(fk["d_durch_pi_minus_1"]) <= 0.003 else "nicht eingetroffen",
                             "werte": {"d": fk["d"], "d_durch_pi_minus_1": fk["d_durch_pi_minus_1"], "q": fk["q"],
                                       "K": "K_B (PLAN Abschnitt 5)"}}
    mr = out["ausgleich"]["F1"]["max_rest"]
    out["urteile"]["PR3"] = {"urteil": "eingetroffen" if mr < 0.05 else "nicht eingetroffen",
                             "werte": {"max_rest_F1": mr, "reste_F1": out["ausgleich"]["F1"]["reste"]}}
else:
    for k in ("PR1", "PR2", "PR3"):
        out["urteile"][k] = {"urteil": "nicht auswertbar", "vermerk": f"nur {n} aufgeloeste Punkte: {aufl}"}

# Kontrollen
R = lade("K_R_m2e-3")
if R is not None and t["m2e-3"].get("gerechnet"):
    out["kontrollen"]["gebiet_L85_m2e-3"] = {"ln_P_R": R["streuung"]["0"]["ln_P_neu_aus"],
                                             "rel_lnP_H_R": abs(t["m2e-3"]["ln_P_H"] - lnP(R)) / abs(t["m2e-3"]["ln_P_H"])}
Dm = lade("D_H_m1e-2")
if Dm is not None:
    PD = float(Dm["streuung"]["0"]["P_neu_aus"])
    out["kontrollen"]["gleichwert_D_m1e-2"] = {"P_D_H": PD, "P_V1W_D": P_REF_D, "rel": PD / P_REF_D - 1,
                                               "rho_z": Dm["rho_z"]}

with open(os.path.join(ORD, "auswertung.json"), "w") as fh:
    json.dump(out, fh, indent=1, default=float)

# ---------------- Bild ----------------
if n >= 5:
    W_, H_ = 760, 620
    x0, x1 = 9.0, 23.5
    ys = [p["lnP"] for p in punkte] + [float(v["ln_P"]) for v in reiheD.values() if v.get("ln_P")]
    y0, y1 = min(ys) - 5, max(ys) + 5
    def X(v):
        return 70 + (v - x0) / (x1 - x0) * (W_ - 100)
    def Y(v):
        return 30 + (y1 - v) / (y1 - y0) * 330
    rmax = max(0.06, max(abs(r) for r in out["ausgleich"]["F1"]["reste"] + out["ausgleich"]["FK_K_B"]["reste"]) * 1.2)
    def YR(v):
        return 420 + (rmax - v) / (2 * rmax) * 160
    sv = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W_}" height="{H_}" font-family="sans-serif" font-size="12">',
          '<rect width="100%" height="100%" fill="white"/>',
          f'<text x="70" y="18">V-1-PRAEZISION: ln P gegen 1/sqrt(abs(eps)); Kartenmodell H (gefuellt), Reihe D f0 (offen)</text>',
          f'<rect x="70" y="30" width="{W_ - 100}" height="330" fill="none" stroke="black"/>',
          f'<rect x="70" y="420" width="{W_ - 100}" height="160" fill="none" stroke="black"/>']
    for tx in range(10, 24, 2):
        sv.append(f'<line x1="{X(tx):.1f}" y1="360" x2="{X(tx):.1f}" y2="366" stroke="black"/>'
                  f'<text x="{X(tx) - 6:.1f}" y="378">{tx}</text>')
        sv.append(f'<line x1="{X(tx):.1f}" y1="580" x2="{X(tx):.1f}" y2="586" stroke="black"/>'
                  f'<text x="{X(tx) - 6:.1f}" y="598">{tx}</text>')
    for ty in range(int(math.ceil(y0 / 10) * 10), int(y1) + 1, 10):
        sv.append(f'<line x1="64" y1="{Y(ty):.1f}" x2="70" y2="{Y(ty):.1f}" stroke="black"/>'
                  f'<text x="28" y="{Y(ty) + 4:.1f}">{ty}</text>')
    for tr in (-rmax, -rmax / 2, 0, rmax / 2, rmax):
        sv.append(f'<line x1="64" y1="{YR(tr):.1f}" x2="70" y2="{YR(tr):.1f}" stroke="black"/>'
                  f'<text x="14" y="{YR(tr) + 4:.1f}">{tr:+.3f}</text>')
    sv.append(f'<line x1="70" y1="{YR(0):.1f}" x2="{W_ - 30}" y2="{YR(0):.1f}" stroke="#999" stroke-dasharray="4,3"/>')
    sv.append(f'<text x="{W_ / 2 - 60:.0f}" y="612">1/sqrt(abs(eps))</text>')
    sv.append('<text x="74" y="414">Reste in ln P: F1 (Kreuz), FK mit K_B (Kreis)</text>')
    b1 = out["ausgleich"]["F1"]
    fk = out["ausgleich"]["FK_K_B"]
    pts = []
    for i in range(201):
        uu = 9.5 + i * (23.0 - 9.5) / 200
        ee = 1 / uu ** 2
        pts.append(f"{X(uu):.1f},{Y(b1['a'] + b1['q'] * math.log(ee) - b1['c'] * uu):.1f}")
    sv.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="#1f77b4" stroke-width="1.5"/>')
    for i, p in enumerate(punkte):
        uu = 1 / math.sqrt(abs(p["eps"]))
        yy = b1["a"] + b1["q"] * math.log(abs(p["eps"])) - 2 * fk["d"] * 0  # nur Platzhalter
        sv.append(f'<circle cx="{X(uu):.1f}" cy="{Y(p["lnP"]):.1f}" r="4" fill="#d62728"/>')
        r1v, rkv = b1["reste"][i], fk["reste"][i]
        sv.append(f'<path d="M{X(uu) - 4:.1f},{YR(r1v) - 4:.1f} l8,8 m0,-8 l-8,8" stroke="#1f77b4" stroke-width="1.5"/>')
        sv.append(f'<circle cx="{X(uu):.1f}" cy="{YR(rkv):.1f}" r="4" fill="none" stroke="#ff7f0e" stroke-width="1.5"/>')
    for e, v in reiheD.items():
        if v.get("ln_P"):
            uu = 1 / math.sqrt(abs(epsw(e)))
            sv.append(f'<circle cx="{X(uu):.1f}" cy="{Y(float(v["ln_P"])):.1f}" r="4" fill="none" stroke="#2ca02c" stroke-width="1.5"/>')
    sv.append(f'<text x="{W_ - 330}" y="50">F1: c = {b1["c"]:.4f}, q = {b1["q"]:.3f} (2 pi = 6.2832)</text>')
    sv.append(f'<text x="{W_ - 330}" y="66">FK (K_B): d/pi - 1 = {fk["d_durch_pi_minus_1"]:+.5f}</text>')
    sv.append('</svg>')
    with open(os.path.join(ORD, "bild_lnP.svg"), "w") as fh:
        fh.write("\n".join(sv))
print(json.dumps(out["urteile"], indent=1, default=float))
