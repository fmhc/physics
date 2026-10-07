#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GUERTEL-2 (Runde 42): mechanische Auswertung nach PLAN.md (Urteilsregeln GZ0 bis GZ6).

Liest die Laufdateien aus --lauf und schreibt auswertung.json. Synthetische Modellrechnung, keine Messdaten.
"""
import argparse
import hashlib
import json
import math
import os
import time

import numpy as np

G1 = {"1.8": {"E_min_0": 8.409001624606447, "dE_360": 41.2424821730006},
      "1.3": {"E_min_0": 5.109646378082074, "dE_360": 249.9658883534072}}
ANTEIL = 0.8
WINKEL5 = ["0", "360", "720", "1080", "1440"]


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def lade(lauf, name):
    p = os.path.join(lauf, name)
    if not os.path.exists(p):
        return None
    with open(p) as f:
        return json.load(f)


def sauber(o):
    if isinstance(o, float) and (math.isnan(o) or math.isinf(o)):
        return None
    if isinstance(o, dict):
        return {str(k): sauber(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [sauber(v) for v in o]
    if isinstance(o, (np.floating,)):
        return sauber(float(o))
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.bool_,)):
        return bool(o)
    return o


def string_info(s, L):
    if s is None:
        return None
    v = s["verlauf"]
    S_end = v[-1]["S"]
    it75 = int(round(0.75 * s["kopf"]["args"]["niter"]))
    S_vor = [x["S"] for x in v if x["it"] == it75]
    konv = (abs(S_end - S_vor[0]) <= 0.02 * G1[L]["dE_360"]) if S_vor else None
    return {"gueltig": s["gueltig"], "S_plan": s["S_plan"], "S_wort": s["S_wort"], "H": s["H"],
            "E_anfang": s["E_anfang"], "E_ende": s["E_ende"], "E_max": s["E_max"], "imax": s["imax"],
            "anfang_entwirrt": s["anfang_entwirrt"], "ende_entwirrt": s["ende_entwirrt"],
            "W_anfang": s["W_anfang"], "W_ende": s["W_ende"], "konvergiert": konv,
            "S_bei_75proz": S_vor[0] if S_vor else None, "it_75proz": it75, "pruefung_end": s["pruefung_end"],
            "pruefung_lauf": s["pruefung_lauf"], "lokale_minima": s["lokale_minima"]}


def feld_tabelle(js):
    """Je Winkel: Protokollzustand + Saaten; E_min, Mittel, SE ueber gueltige; ausgewertet bei >= 80 %."""
    if js is None or "saaten" not in js:
        return None
    tab = {}
    for w, sa in js["saaten"].items():
        pz = js["saaten_protokollzustand"][w]
        E = [pz["E"]] + list(sa["E"])
        ok = [pz["gueltig"]] + list(sa["gueltig"])
        eg = np.array([e for e, o in zip(E, ok) if o])
        z = {"E_alle": E, "gueltig": ok, "n": len(E), "n_gueltig": int(sum(ok)),
             "ausgewertet": sum(ok) >= ANTEIL * len(E) and sum(ok) >= 2,
             "E_min_ohne_sonde": float(min(E))}
        if len(eg):
            z.update({"E_min": float(eg.min()), "E_mittel": float(eg.mean()),
                      "E_se": float(eg.std(ddof=1) / math.sqrt(len(eg))) if len(eg) > 1 else float("nan")})
        tab[w] = z
    return tab


def ok5(tab):
    return tab is not None and all(w in tab and tab[w]["ausgewertet"] for w in WINKEL5)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--lauf", default=".")
    p.add_argument("--aus", default="auswertung.json")
    a = p.parse_args()
    out = {"karte": "GUERTEL-2 (Runde 42)", "code_sha256": sha(os.path.abspath(__file__)),
           "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "regeln": "PLAN.md, Urteilsregeln",
           "eingaben": {}, "teil_a": {}, "teil_b": {}, "urteile": {}}
    for f in sorted(os.listdir(a.lauf)):
        if f.endswith(".json") and f != os.path.basename(a.aus):
            out["eingaben"][f] = sha(os.path.join(a.lauf, f))
    U = out["urteile"]
    # ---------------- Teil A ----------------
    pf = {L: lade(a.lauf, "pfad-L%s.json" % L) for L in ("1.8", "1.3")}
    st = {}
    for w in ("S1", "S0", "S2"):
        for L in ("1.8", "1.3"):
            st[(w, L)] = string_info(lade(a.lauf, "string-%s-L%s.json" % (w, L)), L)
    lei = {L: lade(a.lauf, "leiter-L%s.json" % L) for L in ("1.8", "1.3")}
    A = out["teil_a"]
    A["pfad"] = {L: ({k: pf[L][k] for k in pf[L] if k.startswith(("gz0a_staley", "start_", "reproduktion",
                                                                   "s1_", "s2_", "s0_", "E_B0"))
                      and k != "gz0a_staley_je_bild"} if pf[L] else None) for L in pf}
    A["strings"] = {"%s-L%s" % k: v for k, v in st.items() if v is not None}
    # GZ0
    g0a = all(pf[L] is not None and pf[L]["gz0a_staley"]["alle_bilder_ok"] for L in ("1.8", "1.3"))
    g0a_da = all(pf[L] is not None for L in ("1.8", "1.3"))
    g0b_plan, g0b_wort, g0b_da = True, True, True
    for L in ("1.8", "1.3"):
        s0 = st[("S0", L)]
        if s0 is None:
            g0b_da = False
            continue
        g0b_plan &= bool(s0["gueltig"] and abs(s0["S_plan"]) <= 0.01 * G1[L]["dE_360"])
        g0b_wort &= bool(s0["gueltig"] and abs(s0["S_plan"]) <= 0.01 * s0["E_anfang"])
    if g0a_da and g0b_da:
        U["GZ0"] = {"plan": "eingetroffen" if (g0a and g0b_plan) else "nicht eingetroffen",
                    "wortlaut": "eingetroffen" if (g0a and g0b_wort) else "nicht eingetroffen",
                    "teil_a_staley_durchdringungsfrei": g0a, "teil_b_S0_plan": g0b_plan, "teil_b_S0_wort": g0b_wort,
                    "S0": {L: (st[("S0", L)]["S_plan"] if st[("S0", L)] else None) for L in ("1.8", "1.3")}}
    else:
        U["GZ0"] = {"plan": "nicht auswertbar", "wortlaut": "nicht auswertbar"}
    # GZ1
    s1 = st[("S1", "1.8")]
    if s1 is None:
        U["GZ1"] = {"plan": "nicht auswertbar", "wortlaut": "nicht auswertbar"}
    else:
        dE = G1["1.8"]["dE_360"]
        Sp = 0.0 if s1["anfang_entwirrt"] else s1["S_plan"]
        Sw = s1["S_wort"]
        basis = s1["gueltig"] and s1["ende_entwirrt"]
        U["GZ1"] = {"plan": "eingetroffen" if (basis and Sp < dE) else "nicht eingetroffen",
                    "wortlaut": "eingetroffen" if (basis and Sw < dE) else "nicht eingetroffen",
                    "S_plan": Sp, "S_wort": Sw, "dE_360": dE, "S_plan_durch_dE": Sp / dE, "S_wort_durch_dE": Sw / dE,
                    "gueltig": s1["gueltig"], "ende_entwirrt": s1["ende_entwirrt"],
                    "anfang_entwirrt": s1["anfang_entwirrt"], "konvergiert": s1["konvergiert"]}
    # GZ2
    a18, a13 = st[("S1", "1.8")], st[("S1", "1.3")]
    if a18 and a13 and a18["gueltig"] and a13["gueltig"] and a18["ende_entwirrt"] and a13["ende_entwirrt"]:
        sp18 = 0.0 if a18["anfang_entwirrt"] else a18["S_plan"]
        sp13 = 0.0 if a13["anfang_entwirrt"] else a13["S_plan"]
        U["GZ2"] = {"plan": "eingetroffen" if sp18 < sp13 else "nicht eingetroffen",
                    "wortlaut": "eingetroffen" if a18["S_wort"] < a13["S_wort"] else "nicht eingetroffen",
                    "S_plan_18": sp18, "S_plan_13": sp13, "S_wort_18": a18["S_wort"], "S_wort_13": a13["S_wort"],
                    "S_plan_durch_dE_18": sp18 / G1["1.8"]["dE_360"], "S_plan_durch_dE_13": sp13 / G1["1.3"]["dE_360"]}
    else:
        U["GZ2"] = {"plan": "nicht auswertbar", "wortlaut": "nicht auswertbar",
                    "grund": "ein S1-String fehlt, ist ungueltig oder endet nicht entwirrt"}
    # GZ3
    A["leiter"] = {}
    for L in ("1.8", "1.3"):
        lj = lei[L]
        if lj is None:
            continue
        w = np.array(lj["winkel"])
        E = np.array(lj["E_end"])
        ok = np.array(lj["sonde_ok"])
        T0 = np.array(lj["T0"])
        m0 = w == 0.0
        info = {"E_B0": lj["E_B0"], "anteil_gueltig_0": float(ok[m0].mean()),
                "E_min_0_neu": float(E[m0 & ok].min()) if (m0 & ok).any() else None, "je_stufe_0": {}}
        for T in sorted(set(T0[m0].tolist())):
            mm = m0 & (T0 == T)
            info["je_stufe_0"][str(T)] = {"E": E[mm].tolist(), "ok": ok[mm].tolist(),
                                          "E_min": float(E[mm & ok].min()) if (mm & ok).any() else None}
        m7 = w == 720.0
        if m7.any():
            ent = np.array(lj["entwirrt"])
            info["je_stufe_720"] = {}
            for T in sorted(set(T0[m7].tolist())):
                mm = m7 & (T0 == T)
                info["je_stufe_720"][str(T)] = {"E": E[mm].tolist(), "ok": ok[mm].tolist(),
                                                "entwirrt": ent[mm].tolist(),
                                                "Wx": np.array(lj["Wx"])[mm].tolist()}
        info["verhaeltnis_zu_g1"] = (info["E_min_0_neu"] / G1[L]["E_min_0"]) if info["E_min_0_neu"] else None
        A["leiter"][L] = info
    l18 = A["leiter"].get("1.8")
    if l18 and l18["E_min_0_neu"] is not None and l18["anteil_gueltig_0"] >= ANTEIL:
        u = "eingetroffen" if l18["E_min_0_neu"] <= 0.90 * G1["1.8"]["E_min_0"] else "nicht eingetroffen"
        U["GZ3"] = {"plan": u, "wortlaut": u, "E_min_0_neu": l18["E_min_0_neu"], "E_min_0_g1": G1["1.8"]["E_min_0"],
                    "grenze": 0.90 * G1["1.8"]["E_min_0"], "verhaeltnis": l18["verhaeltnis_zu_g1"]}
    else:
        U["GZ3"] = {"plan": "nicht auswertbar", "wortlaut": "nicht auswertbar"}
    # ---------------- Teil B ----------------
    B = out["teil_b"]
    namen = {"3d-grob": ["feld-3d-r3-R12-prot-saat-string.json"],
             "3d-fein": ["feld-3d-r6-R24-prot.json", "feld-3d-r6-R24-saat.json", "feld-3d-r6-R24-string.json"],
             "2d-r3": ["feld-2d-r3-R12-prot-saat.json"], "2d-r6": ["feld-2d-r6-R24-prot-saat.json"],
             "2d-r16": ["feld-2d-r16-R64-prot-saat.json"]}
    fj = {}
    for k, fs in namen.items():
        z = {}
        for f in fs:
            j = lade(a.lauf, f)
            if j is not None:
                z.update({kk: v for kk, v in j.items() if kk in ("protokoll", "saaten", "saaten_protokollzustand",
                                                                  "string", "gitter_info")})
        fj[k] = z if z else None
    tabs = {k: feld_tabelle(v) for k, v in fj.items()}
    for k in fj:
        if fj[k] is None:
            continue
        b = {"tabelle": tabs[k], "gitter_info": fj[k].get("gitter_info")}
        pr = fj[k].get("protokoll")
        if pr:
            b["protokoll_gitter"] = {"theta": pr["gitter"], "E": pr["E_gitter"], "sonde": pr["sonde_gitter"],
                                     "gueltig": pr["gueltig_gitter"]}
            Es = np.array(pr["E_schritt"])
            th = np.array(pr["theta_schritt"])
            spr = [{"von": float(th[i - 1]), "bis": float(th[i]), "E_vor": float(Es[i - 1]), "E_nach": float(Es[i])}
                   for i in range(1, len(Es)) if Es[i - 1] > 1.0 and Es[i] < 0.7 * Es[i - 1]]
            b["spruenge_30proz"] = spr
            b["E_max_protokoll"] = float(Es.max())
            b["theta_E_max"] = float(th[int(np.argmax(Es))])
        if fj[k].get("string"):
            s = fj[k]["string"]
            b["string"] = {x: s[x] for x in ("gueltig", "S_plan", "S_wort", "E_anfang", "E_ende", "imax", "start",
                                             "verlauf")}
            b["string"]["staley_anfang_alle_gueltig"] = s["staley_anfang"]["alle_gueltig"]
        B[k] = b
    # GZ4
    t2 = tabs.get("2d-r16")
    if ok5(t2):
        Em = [t2[w]["E_min"] for w in WINKEL5]
        dEk = [Em[k] - Em[k - 1] for k in range(1, 5)]
        plan = dEk[0] > 0 and all(dEk[k] > 0.5 * dEk[0] for k in range(1, 4))
        wort = all(Em[k] > Em[k - 1] for k in range(1, 5))
        U["GZ4"] = {"plan": "eingetroffen" if plan else "nicht eingetroffen",
                    "wortlaut": "eingetroffen" if wort else "nicht eingetroffen", "E_min": Em, "stufen": dEk,
                    "E1440_durch_E360": Em[4] / Em[1] if Em[1] > 0 else None}
    else:
        U["GZ4"] = {"plan": "nicht auswertbar", "wortlaut": "nicht auswertbar",
                    "grund": "Winkel fehlt oder < 80 % gueltig (Gittersprung)"}
    # GZ5
    t3 = tabs.get("3d-fein")
    if ok5(t3):
        e = {w: t3[w]["E_min"] for w in WINKEL5}
        d360 = e["360"] - e["0"]
        sek = math.sqrt(t3["360"]["E_se"] ** 2 + t3["0"]["E_se"] ** 2)
        a_ = (e["720"] - e["0"]) <= 0.10 * d360
        b_ = d360 > 0 and d360 >= 3.0 * sek
        c_ = (e["1440"] - e["0"]) <= 0.10 * d360 and e["1080"] <= 1.10 * e["360"]
        eps = 1.0e-6 * d360
        aw = abs(e["720"] - e["0"]) <= 0.10 * e["0"] + eps
        U["GZ5"] = {"plan": "eingetroffen" if (a_ and b_ and c_) else "nicht eingetroffen",
                    "wortlaut": "eingetroffen" if (aw and b_ and c_) else "nicht eingetroffen",
                    "E_min": e, "teil_a": a_, "teil_a_wort": aw, "teil_b": b_, "teil_c": c_, "SE_komb_360_0": sek,
                    "E720_durch_dE360": (e["720"] - e["0"]) / d360 if d360 > 0 else None, "eps": eps}
    else:
        U["GZ5"] = {"plan": "nicht auswertbar", "wortlaut": "nicht auswertbar",
                    "grund": "Winkel fehlt oder < 80 % gueltig (Gittersprung)"}
    # GZ6
    sf = B.get("3d-fein", {}).get("string") if B.get("3d-fein") else None
    if sf and sf["gueltig"] and t3 and "360" in t3 and "0" in t3 and t3["360"].get("E_mittel") is not None \
            and s1 is not None and s1["gueltig"]:
        dEf = t3["360"]["E_mittel"] - t3["0"]["E_mittel"]
        ent_f = sf["E_anfang"] <= 0.10 * dEf
        Sfp = 0.0 if ent_f else sf["S_plan"]
        Sfw = sf["S_wort"]
        Sp = 0.0 if s1["anfang_entwirrt"] else s1["S_plan"]
        Sw = s1["S_wort"]
        dE = G1["1.8"]["dE_360"]
        U["GZ6"] = {"plan": "eingetroffen" if (Sfp / dEf < Sp / dE) else "nicht eingetroffen",
                    "wortlaut": "eingetroffen" if (Sfw / dEf < Sw / dE) else "nicht eingetroffen",
                    "feld": {"S_plan": Sfp, "S_wort": Sfw, "dE_360": dEf, "start_entdrillt": ent_f,
                             "S_plan_durch_dE": Sfp / dEf, "S_wort_durch_dE": Sfw / dEf},
                    "faden": {"S_plan": Sp, "S_wort": Sw, "dE_360": dE, "S_plan_durch_dE": Sp / dE,
                              "S_wort_durch_dE": Sw / dE}}
    else:
        U["GZ6"] = {"plan": "nicht auswertbar", "wortlaut": "nicht auswertbar",
                    "grund": "Feld- oder Faden-String fehlt oder ungueltig"}
    out["kurz"] = {g: {"plan": U[g]["plan"], "wortlaut": U[g]["wortlaut"]} for g in sorted(U)}
    tmp = a.aus + ".neu"
    with open(tmp, "w") as f:
        json.dump(sauber(out), f, indent=1)
    os.replace(tmp, a.aus)
    print("auswertung geschrieben:", a.aus)


if __name__ == "__main__":
    main()
