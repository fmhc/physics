#!/usr/bin/env python3
# RUECKFLUSS-INFO-1, Auswertung nach PLAN.md Abschnitt 5 (Urteile nach Plan und nach Kartenwortlaut).
# Aufruf: rueckfluss_auswertung.py --fest a.json,b.json --neu c.json,d.json --leiter4 e.json --leiter8 f.json
#         [--leiter12 g.json] --out auswertung.json
import argparse
import json
import math

import numpy as np

SCHWELLE = 1e-3          # RI1/RI2: Anstieg um mehr als 1e-3
RI0_SOLL, RI0_TOL = 0.440, 0.01
RI3_SOLL, RI3_TOL = 0.44, 0.03
T = 100


def anstiege(D, T=T):
    # PLAN 2.6: Summe der Anstiege; Wiederanstieg A_max = max_t [D(t) - min_{s<=t} D(s)] (bindend fuer "um mehr als 1e-3");
    # beschreibend: groesste Episode positiver Zuwaechse, groesster Einzelschritt, Anzahl positiver Schritte
    x = np.asarray(D[:T + 1], dtype=float)
    d = np.diff(x)
    best = cur = 0.0
    for z in d:
        cur = cur + z if z > 0 else 0.0
        best = max(best, cur)
    wa = x - np.minimum.accumulate(x)
    return {"summe": float(d[d > 0].sum()), "A_max": float(wa.max()), "A_max_bei_t": int(wa.argmax()),
            "max_episode": float(best), "max_schritt": float(max(d.max(), 0.0)), "n_pos": int((d > 0).sum())}


def rq(w2, nfj, t):
    return float((w2[t] - nfj[t]) / (1 - nfj[t]))


def lade(liste):
    return [json.load(open(f)) for f in liste.split(",") if f]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fest", required=True)
    ap.add_argument("--neu", required=True)
    ap.add_argument("--leiter4", default="")
    ap.add_argument("--leiter8", default="")
    ap.add_argument("--leiter12", default="")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    F, NEU = lade(args.fest), lade(args.neu)
    out = {"dateien": vars(args), "schwelle": SCHWELLE}

    # ------------------------------------------------ Kontrollen
    fj = F[0]["fj"]
    fj_abw = max(float(np.max(np.abs(np.array(x["fj"]["Dg"]) - np.array(fj["Dg"])))) for x in F)
    kontr = {"fj_Dg_anstiege": anstiege(fj["Dg"]), "fj_gleich_in_allen_festlaeufen_abw": fj_abw,
             "start_ueberlapp_max": max(x["start_ueberlapp_AB"] for x in F + NEU),
             "norm_abw_max": max(r["norm_abw_max"] for x in F + NEU for r in x["laeufe"]),
             "rand_0.9Rin_max_D": max(r["rand_gesamt_0.75_0.9"][1] for x in F + NEU for r in x["laeufe"]),
             "rand_0.75Rin_max_D": max(r["rand_gesamt_0.75_0.9"][0] for x in F + NEU for r in x["laeufe"]),
             "kraum_W0_Dg_abw": [r["kraum_W0_Dg_abw"] for x in F for r in x["laeufe"] if "kraum_W0_Dg_abw" in r],
             "gram_diag_gegen_w2_abw": max(r["gram_diag_gegen_w2_abw"] for x in NEU for r in x["laeufe"])}
    vorb = bool(kontr["fj_Dg_anstiege"]["summe"] <= 1e-12 and kontr["norm_abw_max"] <= 1e-10
                and kontr["start_ueberlapp_max"] <= 1e-12 and kontr["kraum_W0_Dg_abw"]
                and max(kontr["kraum_W0_Dg_abw"]) <= 1e-8)
    kontr["vorbedingung_RI1_RI2"] = vorb
    out["kontrollen"] = kontr
    NFJ = 0.5 * (np.array(fj["n"][0]) + np.array(fj["n"][1]))
    out["fj"] = {"Dg_10_25_50_100": [fj["Dg"][t] for t in (10, 25, 50, 100)],
                 "N_FJ_A_B_100": [fj["n"][0][T], fj["n"][1][T]],
                 "spinz_halbdiff_10_25_50_100": [0.5 * (fj["spin"][0][t][2] - fj["spin"][1][t][2]) for t in (10, 25, 50, 100)]}

    # ------------------------------------------------ feste Takte
    byW = {}
    for x in F:
        for r in x["laeufe"]:
            byW.setdefault(round(r["W"], 12), []).append(r)
    fest = {}
    for W in sorted(byW):
        rs = byW[W]
        Dg = np.array([r["Dg"] for r in rs])
        Dm = Dg.mean(0)
        wbar = np.mean([0.5 * (np.array(r["nA"]) + np.array(r["nB"])) for r in rs], 0)
        Du = np.mean([r["Du"] for r in rs], 0)
        Dn = np.mean([r["Dn"] for r in rs], 0)
        sz = np.mean([[0.5 * (a[2] - b[2]) for a, b in zip(r["spinA"], r["spinB"])] for r in rs], 0)
        q = {}
        for t in (10, 25, 50, 100):
            den = wbar[t] - NFJ[t]
            q[str(t)] = float((Dm[t] - fj["Dg"][t]) / den) if abs(den) > 1e-12 else None
        fest[str(W)] = {"W": W, "saaten": [r["saat"] for r in rs],
                        "Dg_mittel_0_10_25_50_100": [float(Dm[t]) for t in (0, 10, 25, 50, 100)],
                        "Dg_min_mittel": float(Dm[:T + 1].min()), "Dg_argmin_t": int(Dm[:T + 1].argmin()),
                        "anstiege_mittel": anstiege(Dm), "anstiege_je_saat": [anstiege(d) for d in Dg],
                        "Du_mittel_100": float(Du[T]), "Dn_mittel_10_25_50_100": [float(Dn[t]) for t in (10, 25, 50, 100)],
                        "anstiege_Du_mittel": anstiege(Du), "anstiege_Dn_mittel": anstiege(Dn),
                        "wbar_10_25_50_100": [float(wbar[t]) for t in (10, 25, 50, 100)],
                        "anstiege_wbar": anstiege(wbar),
                        "infoanteil_q": q, "spinz_halbdiff_10_25_50_100": [float(sz[t]) for t in (10, 25, 50, 100)],
                        "Dg_mittel_reihe": [float(x) for x in Dm[:T + 1]],
                        "laufzeit_s_je_saat": [r["laufzeit_s"] for r in rs]}
    out["fest"] = fest

    # ------------------------------------------------ neu gezogene Takte
    neu = {}
    for x in NEU:
        for r in x["laeufe"]:
            D = r["D"]
            M = r["M"]
            wA = np.mean(r["w2"][:M], 0)
            wB = np.mean(r["w2"][M:], 0)
            nullmax = max(max(D["null_A"]["Dg"][:T + 1]), max(D["null_B"]["Dg"][:T + 1]))
            sz = [0.5 * (a[2] - b[2]) for a, b in zip(r["spin_mittel"]["A"], r["spin_mittel"]["B"])]
            neu[str(round(r["W"], 12))] = {
                "W": r["W"], "M": M, "saatbasis": r["saatbasis"],
                "Dg_M_0_10_25_50_100": [D["M"]["Dg"][t] for t in (0, 10, 25, 50, 100)],
                "anstiege_Dg_M": anstiege(D["M"]["Dg"]),
                "anstiege_Dg_haelfte1": anstiege(D["haelfte1"]["Dg"]), "anstiege_Dg_haelfte2": anstiege(D["haelfte2"]["Dg"]),
                "Dg_haelfte1_2_100": [D["haelfte1"]["Dg"][T], D["haelfte2"]["Dg"][T]],
                "null_A_B_Dg_10_25_50_100": [[D["null_A"]["Dg"][t], D["null_B"]["Dg"][t]] for t in (10, 25, 50, 100)],
                "null_max": nullmax, "anstiege_null_A": anstiege(D["null_A"]["Dg"]),
                "getrennt_Dg_10_25_50_100": [D["getrennt"]["Dg"][t] for t in (10, 25, 50, 100)],
                "je_ziehung_Dg_mittel_10_25_50_100": [r["je_ziehung"]["Dg_mittel"][t] for t in (10, 25, 50, 100)],
                "anstiege_je_ziehung_mittel": anstiege(r["je_ziehung"]["Dg_mittel"]),
                "w2_A_B_10_25_50_100": [[float(wA[t]), float(wB[t])] for t in (10, 25, 50, 100)],
                "anstiege_w2A": anstiege(wA),
                "spinz_halbdiff_10_25_50_100": [sz[t] for t in (10, 25, 50, 100)],
                "Dg_M_reihe": D["M"]["Dg"][:T + 1], "laufzeit_s": r["laufzeit_s"]}
    out["neu"] = neu

    # ------------------------------------------------ RI1
    k2 = str(round(2 * math.pi, 12))
    f2 = fest.get(k2)
    if f2 is None or not vorb:
        out["RI1"] = {"plan": "nicht auswertbar", "kartenwortlaut": "nicht auswertbar", "vorbedingung": vorb}
    else:
        p = f2["anstiege_mittel"]["A_max"] > SCHWELLE
        ks = [a["A_max"] > SCHWELLE for a in f2["anstiege_je_saat"]]
        out["RI1"] = {"plan": "eingetroffen" if p else "nicht eingetroffen",
                      "kartenwortlaut": "eingetroffen" if all(ks) else ("nicht eingetroffen" if not any(ks) else
                                                                         "gemischt (%d von %d Saaten)" % (sum(ks), len(ks))),
                      "A_max_mittel": f2["anstiege_mittel"]["A_max"],
                      "max_episode_mittel": f2["anstiege_mittel"]["max_episode"],
                      "summe_mittel": f2["anstiege_mittel"]["summe"],
                      "A_max_je_saat": [a["A_max"] for a in f2["anstiege_je_saat"]],
                      "vorbedingung": vorb}

    # ------------------------------------------------ RI2
    n2 = neu.get(k2)
    if f2 is None or n2 is None or not vorb:
        out["RI2"] = {"plan": "nicht auswertbar", "kartenwortlaut": "nicht auswertbar", "vorbedingung": vorb}
    else:
        a = n2["anstiege_Dg_M"]["A_max"] <= SCHWELLE
        b = f2["anstiege_mittel"]["summe"] > n2["anstiege_Dg_M"]["summe"]
        kw = "eingetroffen" if (a and b) else "nicht eingetroffen"
        bias_ok = n2["null_max"] <= SCHWELLE
        out["RI2"] = {"plan": kw if bias_ok else "nicht auswertbar (Schaetzer-Bias)", "kartenwortlaut": kw,
                      "teil_a_kein_anstieg": a, "teil_b_summe_fest_groesser": b,
                      "A_max_neu": n2["anstiege_Dg_M"]["A_max"], "summe_neu": n2["anstiege_Dg_M"]["summe"],
                      "summe_fest": f2["anstiege_mittel"]["summe"], "null_max": n2["null_max"],
                      "biasvorbedingung": bias_ok, "vorbedingung": vorb}

    # ------------------------------------------------ RI0 (sigma = 4, N = 96, Festlauf, Zustaende A)
    if f2 is not None:
        rs = byW[round(2 * math.pi, 12)]
        nfjA = np.array(fj["n"][0])
        wA = np.array([r["nA"] for r in rs])
        rA = [(w[T] - nfjA[T]) / (1 - nfjA[T]) for w in wA]
        rm = float(np.mean(rA))
        se = float(np.std(rA, ddof=1) / math.sqrt(len(rA))) if len(rA) > 1 else None
        nfjB = np.array(fj["n"][1])
        rB = [(np.array(r["nB"])[T] - nfjB[T]) / (1 - nfjB[T]) for r in rs]
        rand_ok = max(r["rand_gesamt_0.75_0.9"][1] for r in rs) <= 1e-5
        ok = abs(rm - RI0_SOLL) <= RI0_TOL
        out["RI0"] = {"plan": ("eingetroffen" if ok else "nicht eingetroffen") if rand_ok else "nicht auswertbar",
                      "kartenwortlaut": "eingetroffen" if ok else "nicht eingetroffen",
                      "r100_mittel_A": rm, "stdfehler": se, "r100_je_saat_A": [float(x) for x in rA],
                      "r100_mittel_B": float(np.mean(rB)), "r_A_10_25_50_100": [
                          float((wA.mean(0)[t] - nfjA[t]) / (1 - nfjA[t])) for t in (10, 25, 50, 100)],
                      "N_FJ_A_100": float(nfjA[T]), "rand_ok": rand_ok}

    # ------------------------------------------------ sigma-Leiter
    leiter = {}
    for nm, f in (("4", args.leiter4), ("8", args.leiter8), ("12", args.leiter12)):
        if not f:
            continue
        L = lade(f)
        nfj = np.array(L[0]["N_FJ"])
        fjgleich = max(float(np.max(np.abs(np.array(x["N_FJ"]) - nfj))) for x in L)
        rs = [r for x in L for r in x["laeufe"]]
        TT = len(nfj) - 1
        w2 = np.array([r["w2"] for r in rs])
        wm = w2.mean(0)
        ts = [t for t in (10, 25, 50, 100, 150, 200) if t <= TT]
        r100 = [rq(w, nfj, T) for w in w2]
        leiter[nm] = {"sigma": L[0]["sigma"], "N": L[0]["N"], "R_in": L[0]["R_in_hop"], "schritte": TT,
                      "saaten": [r["saat"] for r in rs], "N_FJ": {str(t): float(nfj[t]) for t in ts},
                      "w2_mittel": {str(t): float(wm[t]) for t in ts},
                      "r_mittel": {str(t): rq(wm, nfj, t) for t in ts},
                      "r100_je_saat": r100,
                      "r100_stdfehler": float(np.std(r100, ddof=1) / math.sqrt(len(r100))) if len(r100) > 1 else None,
                      "rand_0.75_0.9_max": [max(r["rand_gesamt_0.75_0.9"][0] for r in rs),
                                            max(r["rand_gesamt_0.75_0.9"][1] for r in rs)],
                      "norm_abw_max": max(r["norm_abw_max"] for r in rs), "fj_gleich_abw": fjgleich,
                      "laufzeit_s_je_saat": [r["laufzeit_s"] for r in rs]}
    out["leiter"] = leiter

    # ------------------------------------------------ RI3
    if "8" not in leiter:
        out["RI3"] = {"plan": "nicht auswertbar", "kartenwortlaut": "nicht auswertbar"}
    else:
        werte = {k: leiter[k]["r_mittel"][str(T)] for k in ("8", "12") if k in leiter}
        rand_ok = all(leiter[k]["rand_0.75_0.9_max"][1] <= 1e-5 for k in werte)
        ok = all(abs(v - RI3_SOLL) <= RI3_TOL for v in werte.values())
        se = {k: leiter[k]["r100_stdfehler"] for k in werte}
        knapp = any(se[k] is not None and abs(abs(werte[k] - RI3_SOLL) - RI3_TOL) <= 2 * se[k] for k in werte)
        urteil = ("eingetroffen" if ok else "nicht eingetroffen") + (" (knapp)" if knapp else "")
        out["RI3"] = {"plan": urteil if rand_ok else "nicht auswertbar",
                      "kartenwortlaut": urteil, "r100": werte, "stdfehler": se, "knapp": knapp, "rand_ok": rand_ok}
    with open(args.out, "w") as f:
        json.dump(out, f, indent=1)
    print("RI0", out.get("RI0", {}).get("plan"), "| RI1", out["RI1"]["plan"], "| RI2", out["RI2"]["plan"],
          "| RI3", out["RI3"]["plan"], flush=True)


if __name__ == "__main__":
    main()
