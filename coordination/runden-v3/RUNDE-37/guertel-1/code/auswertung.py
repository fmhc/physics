#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GUERTEL-1 (Runde 41): mechanische Auswertung nach PLAN.md Abschnitt 5 (Urteilsregeln).

Liest die Laufdateien (protokoll-*, abkuehlen-*, sperre-*, gegenprobe-*) aus --lauf und schreibt
auswertung.json. Synthetische Modellrechnung, keine Messdaten.
"""
import argparse
import hashlib
import json
import math
import os
import time

import numpy as np

LFAKS = (1.3, 1.8)
HAUPT_L = 1.8
SYSNAMEN = ["zweizaehlig", "allgemein", "ebene"]
BAND = 0.10          # "innerhalb 10 %" relativ zu E_min(0)
NSE = 3.0            # ">= 3 SE ueber Saaten"
ANTEIL_GUELTIG = 0.8  # Winkel ausgewertet, wenn >= 80 % der Saaten die Sonde bestehen
ENTWIRRT = 0.5       # mittleres |W_i| < 0.5 bei 720 Grad
GITTER_HALB = list(range(30, 331, 30))
GITTER_VOLL = list(range(30, 691, 30))


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def sauber(o):
    if isinstance(o, float) and (math.isnan(o) or math.isinf(o)):
        return None
    if isinstance(o, dict):
        return {k: sauber(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [sauber(v) for v in o]
    if isinstance(o, (np.floating,)):
        return sauber(float(o))
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.bool_,)):
        return bool(o)
    return o


def lade(p):
    with open(p) as f:
        return json.load(f)


def tabelle(ab):
    """Je Winkel: gueltige Saaten, E_min, Mittel, SE, bester Zustand (Moment, Windung)."""
    winkel = ab["winkel"]
    ok = ab["sonde"]["ok"]
    E = ab["E_end"]
    M = ab["M_end"]
    W = ab["W_end"]
    fm = ab["fmax_end"]
    tab = {}
    for w in sorted(set(winkel)):
        idx = [b for b in range(len(winkel)) if winkel[b] == w]
        gi = [b for b in idx if ok[b]]
        e = np.array([E[b] for b in gi])
        z = {"winkel": w, "n_saaten": len(idx), "n_gueltig": len(gi),
             "ausgewertet": len(gi) >= ANTEIL_GUELTIG * len(idx) and len(gi) >= 2,
             "fmax_end_max": float(max(fm[b] for b in idx)),
             "W_mittel_je_saat": [float(np.mean(W[b])) for b in idx],
             "E_je_saat": [float(E[b]) for b in idx], "sonde_ok_je_saat": [bool(ok[b]) for b in idx]}
        if len(gi):
            bb = gi[int(np.argmin(e))]
            z.update({"E_min": float(e.min()), "E_mittel": float(e.mean()),
                      "E_sd": float(e.std(ddof=1)) if len(e) > 1 else float("nan"),
                      "E_se": float(e.std(ddof=1) / math.sqrt(len(e))) if len(e) > 1 else float("nan"),
                      "M_best": float(M[bb]), "W_best": [float(x) for x in W[bb]],
                      "W_best_mittel": float(np.mean(W[bb])),
                      "W_best_mittel_abs": float(np.mean(np.abs(W[bb]))), "saat_best": ab["saat"][bb]})
        tab[str(float(w))] = z
    return tab


def zeile(tab, w):
    return tab.get(str(float(w)))


def se_komb(a, b):
    return math.sqrt(a["E_se"] ** 2 + b["E_se"] ** 2)


def urteil_gt0(tab):
    """Plan: k = 1, 2 (360, 720; PLAN.md 7.3). Wortlaut: alle Vielfachen bis 1440."""
    A = [0, 360, 720, 1080, 1440]
    z = [zeile(tab, a) for a in A]
    da = [x is not None and x["ausgewertet"] for x in z]
    stufen = []
    for k in range(1, 5):
        if da[k] and da[k - 1]:
            d = z[k]["E_mittel"] - z[k - 1]["E_mittel"]
            s = se_komb(z[k], z[k - 1])
            stufen.append({"von": A[k - 1], "bis": A[k], "dE_mittel": d, "SE_komb": s,
                           "dE_min": z[k]["E_min"] - z[k - 1]["E_min"], "groesser_3SE": d > NSE * s})
        else:
            stufen.append({"von": A[k - 1], "bis": A[k], "nicht_auswertbar": True})
    windung = []
    for k in range(5):
        if z[k] is None:
            windung.append(None)
            continue
        wm = z[k]["W_mittel_je_saat"]
        windung.append(all(abs(x - k) < 0.25 for x, o in zip(wm, z[k]["sonde_ok_je_saat"]) if o))
    aus = {"stufen": stufen, "ausgewertet_je_vielfaches": da, "windungen_erhalten_je_vielfaches": windung}
    if all(da[:3]):
        plan_ok = all(stufen[k]["groesser_3SE"] for k in range(2))
        band_plan = z[2]["E_min"] > (1.0 + BAND) * z[0]["E_min"]
        aus["plan"] = "eingetroffen" if (plan_ok and band_plan) else "nicht eingetroffen"
        aus["E_min_720_durch_E_min_0"] = z[2]["E_min"] / z[0]["E_min"]
    else:
        aus["plan"] = "nicht auswertbar"
    if all(da):
        wort_ok = all(z[k]["E_min"] > z[k - 1]["E_min"] for k in range(1, 5))
        band_wort = all(z[k]["E_min"] > (1.0 + BAND) * z[0]["E_min"] for k in range(1, 5))
        aus["wortlaut"] = "eingetroffen" if (wort_ok and band_wort) else "nicht eingetroffen"
    else:
        aus["wortlaut"] = "nicht auswertbar"
    return aus


def urteil_gt1(tab):
    z0, z3, z7 = zeile(tab, 0), zeile(tab, 360), zeile(tab, 720)
    if any(x is None or not x["ausgewertet"] for x in (z0, z3, z7)):
        return {"plan": "nicht auswertbar", "wortlaut": "nicht auswertbar", "grund": "Winkel fehlt oder < 80 % gueltig"}
    s = se_komb(z3, z0)
    a = z7["E_min"] <= (1.0 + BAND) * z0["E_min"]
    b = (z3["E_mittel"] - z0["E_mittel"]) >= NSE * s
    c = z7["W_best_mittel_abs"] < ENTWIRRT
    aw = abs(z7["E_min"] - z0["E_min"]) <= BAND * z0["E_min"]
    bw = (z3["E_min"] - z0["E_min"]) >= NSE * s
    n_entw = sum(1 for x, o in zip(z7["W_mittel_je_saat"], z7["sonde_ok_je_saat"]) if o and abs(x) < ENTWIRRT)
    return {"plan": "eingetroffen" if (a and b and c) else "nicht eingetroffen",
            "wortlaut": "eingetroffen" if (aw and bw) else "nicht eingetroffen",
            "teil_a_band": a, "teil_b_360_ueber_0": b, "teil_c_entwirrt": c,
            "E_min_0": z0["E_min"], "E_min_360": z3["E_min"], "E_min_720": z7["E_min"],
            "E_mittel_0": z0["E_mittel"], "E_mittel_360": z3["E_mittel"], "E_mittel_720": z7["E_mittel"],
            "SE_komb_360_0": s, "verhaeltnis_720_0": z7["E_min"] / z0["E_min"],
            "abstand_360_in_SE": (z3["E_mittel"] - z0["E_mittel"]) / s if s > 0 else float("inf"),
            "saaten_entwirrt_720": n_entw, "saaten_gueltig_720": z7["n_gueltig"]}


def weg(tab, gitter):
    return [zeile(tab, w) for w in gitter]


def urteil_gt2a(tab):
    zz = weg(tab, [0] + GITTER_HALB + [360])
    if any(x is None or not x["ausgewertet"] for x in zz):
        return {"plan": "nicht auswertbar", "wortlaut": "nicht auswertbar"}
    M = [x["M_best"] for x in zz[1:-1]]
    E = [x["E_min"] for x in zz]
    hub = abs(E[-1] - E[0])
    a = all(m > 0 for m in M)
    a_plan = all(E[k + 1] >= E[k] - 0.02 * hub for k in range(len(E) - 1))
    a_wort = all(E[k + 1] > E[k] for k in range(len(E) - 1))
    kp = GITTER_HALB[int(np.argmax(M))]
    b = 135 <= kp <= 225
    return {"plan": "eingetroffen" if (a and a_plan and b) else "nicht eingetroffen",
            "wortlaut": "eingetroffen" if (a and a_wort and b) else "nicht eingetroffen",
            "teil_moment_positiv": a, "teil_monoton_toleranz": a_plan, "teil_monoton_streng": a_wort,
            "kraftspitze_grad": kp, "teil_spitze_180_pm_45": b,
            "M_best": dict(zip([str(g) for g in GITTER_HALB], M)), "E_min": dict(zip([str(g) for g in [0] + GITTER_HALB + [360]], E))}


def urteil_gt2b(tab):
    zz = weg(tab, GITTER_VOLL)
    if any(x is None or not x["ausgewertet"] for x in zz):
        return {"plan": "nicht auswertbar", "wortlaut": "nicht auswertbar"}
    M = np.array([x["M_best"] for x in zz])
    sg = np.sign(M)
    wechsel = [k for k in range(len(M) - 1) if sg[k] != sg[k + 1]]
    a = (len(wechsel) == 1 and sg[0] > 0 and sg[-1] < 0)
    th0 = None
    if wechsel:
        k = wechsel[0]
        g1, g2 = GITTER_VOLL[k], GITTER_VOLL[k + 1]
        th0 = g1 + (g2 - g1) * M[k] / (M[k] - M[k + 1])
    b = th0 is not None and 330 <= th0 <= 390
    c = False
    kp = None
    if th0 is not None:
        vor = [(GITTER_VOLL[k], M[k]) for k in range(len(M)) if GITTER_VOLL[k] < th0]
        if vor:
            kp = max(vor, key=lambda x: x[1])[0]
            c = 135 <= kp <= 225
    return {"plan": "eingetroffen" if (a and b and c) else "nicht eingetroffen",
            "wortlaut": "eingetroffen" if (a and b and c) else "nicht eingetroffen",
            "nur_nullstelle": "eingetroffen" if (a and b) else "nicht eingetroffen",
            "vorzeichenwechsel_nach_gitterpunkt": [GITTER_VOLL[k] for k in wechsel], "nullstelle_grad": th0,
            "teil_ein_wechsel": a, "teil_nullstelle_360_pm_30": b, "kraftspitze_grad": kp, "teil_spitze_180_pm_45": c,
            "M_best": dict(zip([str(g) for g in GITTER_VOLL], M.tolist()))}


def formmass(tab):
    zz = weg(tab, GITTER_VOLL)
    if any(x is None for x in zz):
        return None
    M = np.array([x["M_best"] for x in zz])
    th = np.array(GITTER_VOLL, float)
    mmax = float(np.max(np.abs(M)))
    i330 = GITTER_VOLL.index(330)
    i390 = GITTER_VOLL.index(390)
    J = min(abs(M[i330]), abs(M[i390])) / mmax if mmax > 0 else float("nan")
    if J >= 0.5 and M[i330] > 0 and M[i390] < 0:
        art = "Sprung"
    elif J <= 0.25:
        art = "glatt"
    else:
        art = "unklar"
    sinus = np.sin(np.deg2rad(th) / 2.0)
    saege = np.where(th < 360, th, np.where(th > 360, th - 720.0, 0.0))
    r_sin = float(np.corrcoef(M, sinus)[0, 1])
    r_saege = float(np.corrcoef(M, saege)[0, 1])
    return {"J": float(J), "art": art, "r_sinus": r_sin, "r_saege": r_saege,
            "M_330": float(M[i330]), "M_390": float(M[i390]), "M_max_abs": mmax}


def protokoll_info(pr, s):
    th = np.array(pr["fein_theta"])
    M = np.array([m[s] for m in pr["fein_M"]])
    E = np.array([e[s] for e in pr["fein_E"]])
    pos = th > 0
    erste_neg = None
    for t, m in zip(th[pos], M[pos]):
        if m < 0:
            erste_neg = float(t)
            break
    g = pr["gitter"]
    W = {str(g[k]): pr["W"][k][s] for k in range(len(g))}
    i720 = g.index(720.0) if 720.0 in g else None
    w720 = pr["W"][i720][s] if i720 is not None else None
    ok = all(iv["ok"][s] for iv in pr["sonde_intervall"])
    erste_fehl = None
    for k, iv in enumerate(pr["sonde_intervall"]):
        if not iv["ok"][s]:
            erste_fehl = g[k]
            break
    bis720 = th <= 720
    kmax = int(np.argmax(np.where(bis720 & (th <= 360), M, -np.inf)))
    return {"erste_negative_momentstelle_grad": erste_neg, "W_gitter": W,
            "W_720": w720, "entwirrt_beim_drehen_720": (w720 is not None and float(np.mean(np.abs(w720))) < ENTWIRRT),
            "sonde_ok_ganz": ok, "erste_sondenverletzung_bis_gitter": erste_fehl,
            "M_max_0_360": float(M[kmax]), "theta_M_max_0_360": float(th[kmax]),
            "E_gitter": {str(g[k]): pr["E"][k][s] for k in range(len(g))},
            "M_gitter": {str(g[k]): pr["M"][k][s] for k in range(len(g))},
            "fmax_gitter_max": float(max(f[s] for f in pr["fmax"]))}


def urteil_gt3(tab, pinfo, sp):
    z0, z3 = zeile(tab, 0), zeile(tab, 360)
    if z0 is None or z3 is None or not z0["ausgewertet"] or not z3["ausgewertet"]:
        return {"plan": "nicht auswertbar", "wortlaut": "nicht auswertbar", "grund": "0 oder 360 nicht ausgewertet"}
    dE = z3["E_mittel"] - z0["E_mittel"]
    S = None
    H = None
    quelle = None
    if pinfo["entwirrt_beim_drehen_720"]:
        S = 0.0
        quelle = "Protokoll schon bei 720 entwirrt (Sperre 0 auf dem Drehweg)"
    elif sp is not None and sp.get("ergebnis") == "string":
        if sp["pruefung"]["ok"]:
            S = sp["S"]
            H = sp["E_anfang"] + sp["S"] - z0["E_min"]
            quelle = "Stringmethode (Pfadpruefung bestanden)"
        else:
            quelle = "Stringmethode, Pfadpruefung nicht bestanden"
    elif sp is not None:
        quelle = "keine entwirrte Saat bei 720"
    else:
        quelle = "keine Sperrdatei"
    if S is None:
        u = "nicht auswertbar"
    else:
        u = "eingetroffen" if S < dE else "nicht eingetroffen"
    return {"plan": u, "wortlaut": u, "S": S, "H": H, "dE_360": dE, "quelle": quelle,
            "H_kleiner_dE360": (H < dE) if H is not None else None}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--lauf", default=".")
    p.add_argument("--aus", default="auswertung.json")
    a = p.parse_args()
    out = {"karte": "GUERTEL-1 (Runde 41)", "code_sha256": sha(os.path.abspath(__file__)),
           "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "regeln": "PLAN.md Abschnitt 5",
           "eingaben": {}, "tabellen": {}, "protokoll": {}, "urteile": {}, "formmass": {}, "sperre": {}}
    for f in sorted(os.listdir(a.lauf)):
        if f.endswith(".json") and f != os.path.basename(a.aus):
            out["eingaben"][f] = sha(os.path.join(a.lauf, f))
    tabs = {}
    pinfos = {}
    for L in LFAKS:
        pp = os.path.join(a.lauf, "protokoll-L%.1f.json" % L)
        pr = lade(pp) if os.path.exists(pp) else None
        for s in range(3):
            key = "L%.1f-%s" % (L, SYSNAMEN[s])
            ap = os.path.join(a.lauf, "abkuehlen-L%.1f-s%d.json" % (L, s))
            if os.path.exists(ap):
                tabs[key] = tabelle(lade(ap))
                out["tabellen"][key] = tabs[key]
            if pr is not None:
                pinfos[key] = protokoll_info(pr, s)
                out["protokoll"][key] = pinfos[key]
    for L in LFAKS:
        u = {}
        k2 = "L%.1f-zweizaehlig" % L
        kg = "L%.1f-allgemein" % L
        ke = "L%.1f-ebene" % L
        if ke in tabs:
            u["GT0"] = urteil_gt0(tabs[ke])
        if k2 in tabs:
            u["GT1"] = urteil_gt1(tabs[k2])
            u["GT2a"] = urteil_gt2a(tabs[k2])
            out["formmass"][k2] = formmass(tabs[k2])
        if kg in tabs:
            u["GT1_allgemeine_achse"] = urteil_gt1(tabs[kg])
            u["GT2b"] = urteil_gt2b(tabs[kg])
            u["GT2a_muster_allgemeine_achse"] = urteil_gt2a(tabs[kg])
            out["formmass"][kg] = formmass(tabs[kg])
        for s, kk in ((0, k2), (1, kg)):
            if kk in tabs and kk in pinfos:
                spp = os.path.join(a.lauf, "sperre-L%.1f-s%d.json" % (L, s))
                sp = lade(spp) if os.path.exists(spp) else None
                if sp is not None:
                    out["sperre"][kk] = {x: sp[x] for x in sp if x in ("ergebnis", "S", "E_anfang", "E_ende", "imax", "pruefung", "saat", "kandidaten")}
                name = "GT3" if s == 0 else "GT3_allgemeine_achse"
                u[name] = urteil_gt3(tabs[kk], pinfos[kk], sp)
        out["urteile"]["L%.1f" % L] = u
    hp = "L%.1f" % HAUPT_L
    out["haupturteile_nach_plan"] = {g: out["urteile"].get(hp, {}).get(g, {}).get("plan") for g in ("GT0", "GT1", "GT2a", "GT2b", "GT3")}
    out["haupturteile_nach_wortlaut"] = {g: out["urteile"].get(hp, {}).get(g, {}).get("wortlaut") for g in ("GT0", "GT1", "GT2a", "GT2b", "GT3")}
    gp = os.path.join(a.lauf, "gegenprobe-L1.8.json")
    if os.path.exists(gp):
        g = lade(gp)
        out["gegenprobe"] = {"sonde_drehen_ok": g["sonde_drehen"]["ok"], "sonde_abkuehlen_ok": g["sonde_abkuehlen"]["ok"],
                             "W_vor": g["W_vor_abkuehlen"], "W_nach": g["W_nach_abkuehlen"],
                             "min_rho_drehen": g["sonde_drehen"]["min_rho"], "min_rand_ff_drehen": g["sonde_drehen"]["min_rand_ff"],
                             "min_rho_abkuehlen": g["sonde_abkuehlen"]["min_rho"], "min_rand_ff_abkuehlen": g["sonde_abkuehlen"]["min_rand_ff"],
                             "schlaegt_an": (not all(g["sonde_drehen"]["ok"])) or (not all(g["sonde_abkuehlen"]["ok"]))}
    tmp = a.aus + ".neu"
    with open(tmp, "w") as f:
        json.dump(sauber(out), f, indent=1)
    os.replace(tmp, a.aus)
    print("auswertung geschrieben:", a.aus)


if __name__ == "__main__":
    main()
