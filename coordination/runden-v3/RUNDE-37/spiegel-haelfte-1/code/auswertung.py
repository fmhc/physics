#!/usr/bin/env python3
# SPIEGEL-HAELFTE-1, Auswertung nach PLAN.md Abschnitt 4 (Urteile nach Plan und nach Kartenwortlaut).
# Aufruf: auswertung.py --teilA haupt_0A.json --laeufe haupt_1.json,haupt_2.json,haupt_3.json --out auswertung.json
import argparse
import json
import math

import numpy as np

BAND = (0.30, 0.36667)            # 1/3 +- 10 %
SH1_TOL = 0.10
NFJ_FENSTER = (0.3, 0.7)
TEIL_A_SCHREIBTISCH = ("haelt in der Sache, mit Berichtigungen: A3 (Betraege legen P_2 nicht fest; welche Haelfte P_a "
                       "und welche P-quer_a traegt, ist Darstellungs- und Konventionsfrage), A7 (H/P/P'-Verdoppler sind "
                       "die vier FCC-Familien, keine FJ-Unterscheidung)")
TEIL_A_SCHREIBTISCH_HAELT = True


def veff(R2_0, R2_T, T):
    d = R2_T - R2_0
    return math.sqrt(d) / T if d > 0 else 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--teilA", required=True)
    ap.add_argument("--laeufe", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    A = json.load(open(args.teilA))
    files = [x for x in args.laeufe.split(",") if x]
    L = [json.load(open(f)) for f in files]
    out = {"dateien": {"teilA": args.teilA, "laeufe": files}, "band_SH2": BAND, "toleranz_SH1": SH1_TOL}

    # ------------------------------------------------ FJ-Referenz (in jedem Lauf gleich?)
    fj0 = L[0]["fj"]
    T = len(fj0["N_FJ"]) - 1
    NFJ = np.array(fj0["N_FJ"])
    fj_abw = max(float(np.abs(np.array(x["fj"]["N_FJ"]) - NFJ).max()) for x in L)
    out["fj"] = {"N_FJ_10_25_50_100": [float(NFJ[t]) for t in (10, 25, 50, 100)],
                 "N_FJ_gleich_in_allen_laeufen_abw": fj_abw,
                 "veff_FJ": veff(fj0["R2_FJ"]["0"], fj0["R2_FJ"][str(T)], T),
                 "fgross_FJ_0_50_100": [fj0["fbig_FJ"][k] for k in ("0", "50", "100")],
                 "rand_FJ": fj0["rand_FJ"], "sigma": L[0]["sigma"], "kc": L[0]["kc"], "N": L[0]["N"],
                 "C2_regel_gegen_kompression_abw": [x["fj"].get("C2_regel_gegen_kompression_abw") for x in L]}

    # ------------------------------------------------ Laeufe nach W sammeln
    byW = {}
    for x in L:
        for r in x["laeufe"]:
            byW.setdefault(round(r["W"], 12), []).append(r)
    Ws = sorted(byW)
    tab = {}
    for W in Ws:
        rs = byW[W]
        w2 = np.array([r["w2"] for r in rs])
        w2m = w2.mean(0)
        drel_t = np.abs(w2m[1:] - NFJ[1:]) / NFJ[1:]
        drel_s = [float((np.abs(w[1:] - NFJ[1:]) / NFJ[1:]).max()) for w in w2]
        keys = sorted(rs[0]["R2_2"], key=int)
        R2m = {k: float(np.mean([r["R2_2"][k] for r in rs])) for k in keys}
        ve = veff(R2m["0"], R2m[str(T)], T)
        ve_s = [veff(r["R2_2"]["0"], r["R2_2"][str(T)], T) for r in rs]
        vst = (math.sqrt(R2m[str(T)]) - math.sqrt(R2m[str(T // 2)])) / (T - T // 2)
        rq = {}
        for t in (10, 25, 50, 100):
            if t <= T:
                rq[str(t)] = float((w2m[t] - NFJ[t]) / (1 - NFJ[t]))
        fg = {k: float(np.mean([r["fbig_2"][k] for r in rs])) for k in ("0", "50", "100") if k in rs[0]["fbig_2"]}
        ov = {}
        for k in rs[0]["ueberlapp_FJ"]:
            c = np.array([r["ueberlapp_FJ"][k][0] for r in rs])
            ci = np.array([r["ueberlapp_FJ"][k][1] for r in rs])
            t = int(k)
            koh = [(r["ueberlapp_FJ"][k][0] ** 2 + r["ueberlapp_FJ"][k][1] ** 2) / NFJ[t] for r in rs]
            ink = [r["w2"][t] - kk for r, kk in zip(rs, koh)]
            ov[k] = {"Re_c_mittel": float(c.mean()), "Re_c_stdfehler": float(c.std(ddof=1) / math.sqrt(len(c)))
                     if len(c) > 1 else None, "Im_c_mittel": float(ci.mean()), "N_FJ": float(NFJ[t]),
                     "kohaerent_2_mittel": float(np.mean(koh)), "inkohaerent_2_mittel": float(np.mean(ink))}
        prof = np.mean([r["radialprofil_2_T"]["gewicht"] for r in rs], 0)
        dr = rs[0]["radialprofil_2_T"]["dr"]
        tab[str(W)] = {
            "W": W, "saaten": [r["saat"] for r in rs], "anzahl": len(rs),
            "w2_mittel_10_25_50_100": [float(w2m[t]) for t in (10, 25, 50, 100)],
            "w2_min_mittel": float(w2m.min()),
            "D_rel_mittel": float(drel_t.max()), "D_rel_argmax_t": int(drel_t.argmax()) + 1,
            "D_rel_je_saat": drel_s,
            "veff": ve, "veff_je_saat": ve_s, "v_steig": vst,
            "R2_mittel_0_50_100": [R2m["0"], R2m[str(T // 2)], R2m[str(T)]],
            "rueckgabequote_r": rq, "fgross_2_mittel": fg, "ueberlapp": ov,
            "norm_abw_max": max(r["norm_abw_max"] for r in rs),
            "rand_2_max": {kk: max(r["rand_2"][kk] for r in rs) for kk in rs[0]["rand_2"]},
            "rand_gesamt_max": {kk: max(r["rand_gesamt"][kk] for r in rs) for kk in rs[0]["rand_gesamt"]},
            "radialprofil_2_T": {"dr": dr, "gipfel_r": float((int(np.argmax(prof)) + 0.5) * dr),
                                 "gewicht": [float(p) for p in prof]},
            "laufzeit_s_je_saat": [r["laufzeit_s"] for r in rs]}
    out["je_W"] = tab

    # ------------------------------------------------ SH0
    a = A["teil_A_2p2s"]
    bk = A["bloch_kegel_sauber"]
    chir = a["haendigkeit_2_relativ_zu_h"]
    andere = "plus_h" if chir == "minus_h" else "minus_h"
    komp_passend = a["kompression_minus_FJ_Pquer_abw"] if chir == "minus_h" else a["kompression_minus_FJ_P_abw"]
    c2 = [v for v in out["fj"]["C2_regel_gegen_kompression_abw"] if v is not None]
    a_zahlen = {
        "sauber_VVdag": a["sauber_VVdag_abw"] <= 1e-12,
        "sauber_P2_projektor": a["sauber_P2_projektor_abw"] <= 1e-12,
        "sauber_kovarianz": max(a["sauber_kov_phasenbetrag_abw"], a["sauber_kov_P2_abw"], a["sauber_kov_S_abw"]) <= 1e-12,
        "C2_regel_gegen_kompression": bool(c2) and max(c2) <= 1e-12,
        "repr_VdagV_gleich_P2": a["VdagV_minus_P2_abw"] <= 1e-6 and a["VVdag_abw"] <= 1e-6,
        "repr_kompression_gleich_FJ": komp_passend <= 1e-6,
        "repr_bargmann_eindeutig": a["fj_vergleich"][chir]["bargmann_abw"] <= 1e-6
        and a["fj_vergleich"][andere]["bargmann_abw"] >= 1e-2,
        "sauber_gegen_repr_eichverwandt": a["sauber_gegen_repr_nach_eichung_abw"] <= 1e-6,
    }
    a_zahlen = {kk: bool(vv) for kk, vv in a_zahlen.items()}
    sh0a = bool(TEIL_A_SCHREIBTISCH_HAELT and all(a_zahlen.values()))
    w0 = tab.get("0.0")
    b = None
    if w0 is not None:
        for x in L:
            for r in x["laeufe"]:
                if r["W"] == 0.0 and "bloch" in r:
                    b = r["bloch"]
    sh0b = bool(b is not None and b["w2_abw_max"] <= 1e-8 and b.get("zustand_T_abw_rel", 1.0) <= 1e-8)
    sl = bk["steigung_auf_2_min_max"] + bk["steigung_auf_2s_min_max"]
    sh0c = bool(bk["eigenphasen_W0_abw"] <= 1e-12 and max(abs(s - 1 / 3) for s in sl) <= 1e-4
            and bk["P2_gewicht_kegel_2_min"] >= 1 - 1e-6 and bk["P2s_gewicht_kegel_2s_min"] >= 1 - 1e-6
            and bk["M_2_det"] * bk["M_2s_det"] < 0)
    w2_0 = None
    for x in L:
        for r in x["laeufe"]:
            if r["W"] == 0.0:
                w2_0 = np.array(r["w2"])
    rueck = None
    if w2_0 is not None:
        rueck = {"w2_min": float(w2_0.min()), "w2_100": float(w2_0[T]),
                 "mittel_51_100_minus_mittel_1_50": float(w2_0[51:].mean() - w2_0[1:51].mean())}
    sh0 = bool(sh0a and sh0b and sh0c)
    out["SH0"] = {"plan": "eingetroffen" if sh0 else "nicht eingetroffen",
                  "kartenwortlaut": "eingetroffen" if sh0 else "nicht eingetroffen",
                  "teil_a_schreibtisch": TEIL_A_SCHREIBTISCH, "a_zahlen": a_zahlen, "a": sh0a, "b": sh0b, "c": sh0c,
                  "bloch": b, "kegel": {"eigenphasen_W0": bk["eigenphasen_W0"], "steigungen": sl,
                                        "P2_gewicht_min": bk["P2_gewicht_kegel_2_min"],
                                        "P2s_gewicht_min": bk["P2s_gewicht_kegel_2s_min"],
                                        "det_M_2": bk["M_2_det"], "det_M_2s": bk["M_2s_det"]},
                  "haendigkeit_2_relativ_zu_h": chir, "kohaerente_rueckkehr_W0": rueck}

    # ------------------------------------------------ SH1
    W2pi = tab.get(str(round(2 * math.pi, 12)))
    vor1 = bool(sh0b and NFJ_FENSTER[0] <= float(NFJ[T]) <= NFJ_FENSTER[1])
    if W2pi is None or not vor1:
        out["SH1"] = {"plan": "nicht auswertbar", "kartenwortlaut": "nicht auswertbar", "vorbedingung": vor1}
    else:
        p = W2pi["D_rel_mittel"] <= SH1_TOL
        k = all(d <= SH1_TOL for d in W2pi["D_rel_je_saat"])
        out["SH1"] = {"plan": "eingetroffen" if p else "nicht eingetroffen",
                      "kartenwortlaut": "eingetroffen" if k else "nicht eingetroffen",
                      "D_rel_mittel": W2pi["D_rel_mittel"], "bei_t": W2pi["D_rel_argmax_t"],
                      "D_rel_je_saat": W2pi["D_rel_je_saat"], "N_FJ_100": float(NFJ[T]),
                      "w2_mittel_100": W2pi["w2_mittel_10_25_50_100"][3], "rueckgabequote_r": W2pi["rueckgabequote_r"],
                      "vorbedingung": vor1}

    # ------------------------------------------------ SH2
    ve0 = w0["veff"] if w0 is not None else None
    vor2 = bool(ve0 is not None and BAND[0] <= ve0 <= BAND[1])
    if W2pi is None or not vor2:
        out["SH2"] = {"plan": "nicht auswertbar", "kartenwortlaut": "nicht auswertbar", "veff_W0": ve0}
    else:
        p = BAND[0] <= W2pi["veff"] <= BAND[1]
        allew = {k: tab[k]["veff"] for k in tab if tab[k]["W"] > 0}
        k = all(BAND[0] <= v <= BAND[1] for v in allew.values())
        je_saat = {kk: [bool(BAND[0] <= v <= BAND[1]) for v in tab[kk]["veff_je_saat"]] for kk in tab if tab[kk]["W"] > 0}
        out["SH2"] = {"plan": "eingetroffen" if p else "nicht eingetroffen",
                      "kartenwortlaut": "eingetroffen" if k else "nicht eingetroffen",
                      "veff_W2pi": W2pi["veff"], "veff_je_saat_W2pi": W2pi["veff_je_saat"], "veff_W0": ve0,
                      "veff_alle_W": allew, "im_band_je_saat": je_saat, "veff_FJ": out["fj"]["veff_FJ"]}

    # ------------------------------------------------ beschreibend: W^2-Skalierung des Zusatzverlusts
    if w2_0 is not None:
        sk = {}
        for W in Ws:
            if W > 0:
                w2m = np.mean([r["w2"] for r in byW[W]], 0)
                sk[str(W)] = {"verlust_100": float(w2_0[T] - w2m[T]),
                              "verlust_mittel_51_100": float((w2_0[51:] - w2m[51:]).mean())}
        out["zusatzverlust_gegen_W0"] = sk
        k8, k4 = str(round(math.pi / 8, 12)), str(round(math.pi / 4, 12))
        if k8 in sk and k4 in sk and sk[k8]["verlust_mittel_51_100"] != 0:
            out["W2_verhaeltnis_pi4_zu_pi8"] = sk[k4]["verlust_mittel_51_100"] / sk[k8]["verlust_mittel_51_100"]
    with open(args.out, "w") as f:
        json.dump(out, f, indent=1)
    print("SH0", out["SH0"]["plan"], "| SH1", out["SH1"]["plan"], "| SH2", out["SH2"]["plan"], flush=True)


if __name__ == "__main__":
    main()
