#!/usr/bin/env python3
"""INDUZIERT-KUGEL-2 (Runde 40, Code-Agent): mechanische Auswertung nach PLAN.md (Abschnitte 5 und 6).

Kugelseite aus den eigenen Laufdateien (Regeln C, S, Q, G, Gs), Torusseite aus den Laufdateien von INDUZIERT-KUGEL-1
(gleiche Saat und gleiches N). Fit und Statistik unveraendert aus auswertung_kugel.py (INDUZIERT-KUGEL-1):
  y_j(N) = (G_Kugel(N) - G_Torus(N))/sqrt(N);  je Saat y_j(N) = beta_j + delta_j/sqrt(N);  beta = Mittel, SE = Std/sqrt(M).
Aufruf (nur ueber kleintest.sh): python auswertung_kugel2.py <lauf-ordner> <kugel1-lauf-ordner> <aus.json>
"""
import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import auswertung_kugel as k1a  # noqa: E402  (unveraendert aus INDUZIERT-KUGEL-1)

REGELN = ("C", "S", "Q", "Gs")
GROESSEN = ("gamma", "gamma_M")
FASSUNGEN = ("korr", "roh")
VERGLEICH = ("gamma", "gamma_M", "sum_log_m", "V", "korr", "korr_M", "lam_min")
MIN_SAATEN = 8
MAX_AUSFALL = 0.10
SCHWELLE_K22 = 0.3
SCHWELLE_K23 = 0.4
GAMMA_KONT = -29.0 / 360.0
PAARE_DIFF = (("Q", "S"), ("Gs", "S"), ("Q", "C"), ("Gs", "C"), ("S", "C"), ("Gs", "Q"))
PAARE_DIFF_G = (("G", "S"), ("G", "C"), ("G", "Q"), ("G", "Gs"))


def mstd(vals):
    a = np.asarray([v for v in vals if v is not None], dtype=float)
    if a.size == 0:
        return None
    return {"mittel": float(a.mean()), "std": float(a.std(ddof=1)) if a.size > 1 else None, "min": float(a.min()),
            "max": float(a.max())}


def fits_fuer(recs, Ns, saaten, r):
    erg = {}
    for q in GROESSEN:
        for v in FASSUNGEN:
            Y = np.array([[k1a.y_wert(recs[(4, N, s)], r, q, v) for N in Ns] for s in saaten])
            fo, bj = k1a.fits(Ns, Y)
            fo["beta_mit_gamma_kont"] = fo["beta"]["mittel"] - GAMMA_KONT * fo["gamma_empfindlichkeit_b0"]
            fo["saaten"] = list(saaten)
            erg[f"{r}/{q}/{v}"] = (fo, bj)
    return erg


def main():
    ordner, ordner1, ziel = sys.argv[1], sys.argv[2], sys.argv[3]
    mein, dateien, doppelt = k1a.laden(ordner)
    alt, dateien1, doppelt1 = k1a.laden(ordner1)
    mein = {k: v for k, v in mein.items() if k[0] == 4}
    alt = {k: v for k, v in alt.items() if k[0] == 4}
    out = {"dateien": dateien, "doppelt_ignoriert": doppelt, "dateien_kugel1": dateien1,
           "konstanten": {"MIN_SAATEN": MIN_SAATEN, "MAX_AUSFALL": MAX_AUSFALL, "SCHWELLE_K22": SCHWELLE_K22,
                          "SCHWELLE_K23": SCHWELLE_K23, "GAMMA_KONT": GAMMA_KONT}}

    # ------------------------------------------------------------------ K2-0: Reproduktion gegen INDUZIERT-KUGEL-1
    vergleich, fehlt = [], []
    for key in sorted(mein):
        m, a_ = mein[key], alt.get(key)
        if a_ is None:
            fehlt.append(list(key))
            continue
        e = {"N": key[1], "saat": key[2]}
        for r in ("C", "S"):
            for fld in VERGLEICH:
                x, y = m["kugel"]["regeln"][r].get(fld), a_["kugel"]["regeln"][r].get(fld)
                e[f"{r}/{fld}/gleich"] = bool(x is not None and y is not None and x == y)
                e[f"{r}/{fld}/abw"] = abs(x - y) if (x is not None and y is not None) else None
        for fld in ("a", "V_K", "V_C_kreuz", "V_S_mittelpunkt", "V_Q_quadratur"):
            e[f"geo/{fld}/gleich"] = bool(m["kugel"]["geo"][fld] == a_["kugel"]["geo"][fld])
        e["F_gleich"] = bool(m["kugel"]["pruefung"]["F"] == a_["kugel"]["pruefung"]["F"])
        vergleich.append(e)
    k20 = {"anzahl_netze": len(vergleich), "fehlt_in_kugel1": fehlt}
    for r in ("C", "S"):
        for fld in VERGLEICH:
            k20[f"{r}/{fld}/alle_gleich"] = bool(vergleich) and all(e[f"{r}/{fld}/gleich"] for e in vergleich)
            ab = [e[f"{r}/{fld}/abw"] for e in vergleich if e[f"{r}/{fld}/abw"] is not None]
            k20[f"{r}/{fld}/max_abw"] = max(ab) if ab else None
    for fld in ("a", "V_K", "V_C_kreuz", "V_S_mittelpunkt", "V_Q_quadratur"):
        k20[f"geo/{fld}/alle_gleich"] = bool(vergleich) and all(e[f"geo/{fld}/gleich"] for e in vergleich)
    k20["F/alle_gleich"] = bool(vergleich) and all(e["F_gleich"] for e in vergleich)
    k20_ok = bool(vergleich and not fehlt and k20["C/gamma/alle_gleich"] and k20["S/gamma/alle_gleich"])
    out["K2_0_vergleich"] = k20
    out["K2_0_je_netz"] = vergleich

    # ------------------------------------------------------------------ Zusammenfuehren, Tor
    recs = {}
    for key, m in mein.items():
        a_ = alt.get(key)
        if a_ is None:
            continue
        t_ok = bool(a_["torus"]["gueltig"] and a_["lu_ok"][2])
        recs[key] = {"n": 4, "N": key[1], "saat": key[2], "kugel": m["kugel"], "torus": a_["torus"],
                     "gueltig": bool(m["gueltig"] and t_ok), "gueltig_G": bool(m["gueltig_G"] and t_ok),
                     "lu_ok": m["lu_ok"], "torus_ok": t_ok, "sekunden": m["sekunden"], "sek_neu": m["sek_neu"],
                     "rss_mb": m["rss_mb"]}
    Ns = sorted({k[1] for k in recs})
    saaten = sorted({k[2] for k in mein})
    gut, aus, unvollst, gruende = [], [], [], {}
    for s in saaten:
        vorhanden = [(4, N, s) in recs for N in Ns]
        gueltig = [recs[(4, N, s)]["gueltig"] for N in Ns if (4, N, s) in recs]
        if not all(gueltig):
            aus.append(s)
            gruende[str(s)] = [{"N": N, "kugel": recs[(4, N, s)]["kugel"]["gueltig"], "torus": recs[(4, N, s)]["torus_ok"],
                                "lu_ok": recs[(4, N, s)]["lu_ok"]} for N in Ns
                               if (4, N, s) in recs and not recs[(4, N, s)]["gueltig"]]
        elif not all(vorhanden):
            unvollst.append(s)
        else:
            gut.append(s)
    M = len(gut)
    ausfall = len(aus) / max(1, len(aus) + M)
    tor = bool(M >= MIN_SAATEN and ausfall <= MAX_AUSFALL)
    gutG = [s for s in gut if all(recs[(4, N, s)]["gueltig_G"] for N in Ns)]
    ausfall_G = (M - len(gutG)) / max(1, M)
    tor_G = bool(tor and len(gutG) >= MIN_SAATEN and ausfall_G <= MAX_AUSFALL)
    dout = {"Nlist": Ns, "saaten_gut": gut, "saaten_ausgeschlossen": aus, "gruende": gruende,
            "saaten_unvollstaendig": unvollst, "M": M, "ausfall_anteil": ausfall, "tor_bestanden": tor,
            "saaten_G_einbettbar": gutG, "M_G": len(gutG), "ausfall_G_anteil": ausfall_G, "tor_G_bestanden": tor_G,
            "fits": {}}

    # ------------------------------------------------------------------ Fits und gepaarte Differenzen
    erg = {}
    if M >= 2:
        for r in REGELN:
            erg.update(fits_fuer(recs, Ns, gut, r))
        for k, (fo, bj) in erg.items():
            dout["fits"][k] = fo
        dout["differenzen"] = {}
        for r1, r2 in PAARE_DIFF:
            for q in GROESSEN:
                for v in FASSUNGEN:
                    dout["differenzen"][f"{r1}-{r2}/{q}/{v}"] = k1a.stat(erg[f"{r1}/{q}/{v}"][1] - erg[f"{r2}/{q}/{v}"][1])
        dout["differenz_K22_Q_roh_minus_S_korr"] = k1a.stat(erg["Q/gamma/roh"][1] - erg["S/gamma/korr"][1])
        dout["massdifferenz"] = {f"{r}/{v}": k1a.stat(erg[f"{r}/gamma/{v}"][1] - erg[f"{r}/gamma_M/{v}"][1])
                                 for r in REGELN for v in FASSUNGEN}
    ergG = {}
    if len(gutG) >= 2:
        for r in REGELN + ("G",):
            ergG.update(fits_fuer(recs, Ns, gutG, r))
        dout["fits_G_teilmenge"] = {k: fo for k, (fo, bj) in ergG.items()}
        dout["differenzen_G"] = {}
        for r1, r2 in PAARE_DIFF_G:
            for q in GROESSEN:
                for v in FASSUNGEN:
                    dout["differenzen_G"][f"{r1}-{r2}/{q}/{v}"] = k1a.stat(ergG[f"{r1}/{q}/{v}"][1]
                                                                           - ergG[f"{r2}/{q}/{v}"][1])

    # ------------------------------------------------------------------ beschreibend je N
    besch = []
    for N in Ns:
        rs = [recs[(4, N, s)] for s in saaten if (4, N, s) in recs]
        if not rs:
            continue
        sN = math.sqrt(N)

        def gk(x, *pfad):
            for p in pfad:
                x = x.get(p) if isinstance(x, dict) else None
            return x
        e = {"N": N, "anzahl": len(rs), "a": rs[0]["kugel"]["geo"]["a"]}
        for r in ("C", "S", "Q", "G", "Gs"):
            e[f"V_{r}/V_K"] = mstd([gk(x["kugel"], "regeln", r, "V") / x["kugel"]["geo"]["V_K"]
                                    if gk(x["kugel"], "regeln", r, "V") is not None else None for x in rs])
            e[f"korr_{r}_je_wurzelN"] = mstd([gk(x["kugel"], "regeln", r, "korr") / sN
                                              if gk(x["kugel"], "regeln", r, "korr") is not None else None for x in rs])
            e[f"lu_min_U_{r}"] = mstd([gk(x["kugel"], "regeln", r, "lu", "min_U") for x in rs])
            e[f"lam_min_{r}"] = mstd([gk(x["kugel"], "regeln", r, "lam_min") for x in rs])
        e["V_G_einbettbar/V_K"] = mstd([x["kugel"]["G_einbettung"]["V_einbettbar"] / x["kugel"]["geo"]["V_K"] for x in rs])
        for fld in ("gram_nicht_einbettbar", "cm_irgendeine_seite", "cm2_simplizes_verletzt", "cm3_simplizes_verletzt",
                    "cm4_simplizes_verletzt", "gram_cm_uneinig", "anteil_nicht_einbettbar", "Gs_ersetzt",
                    "lam_unter_0.01", "lam_unter_0.001", "lam_unter_0.0001", "lam_unter_1e-06",
                    "arcsin_gegen_arccos_max_rel", "G_durch_C_laenge_max", "F"):
            e[f"G/{fld}"] = mstd([x["kugel"]["G_einbettung"].get(fld) for x in rs])
        e["G/netze_mit_verletzung"] = int(sum(x["kugel"]["G_einbettung"]["gram_nicht_einbettbar"] > 0
                                              or x["kugel"]["G_einbettung"]["cm_irgendeine_seite"] > 0 for x in rs))
        for fld in ("gram_nicht_einbettbar", "cm_irgendeine_seite", "gram_cm_uneinig", "lam_unter_0.01",
                    "lam_unter_0.001", "lam_unter_0.0001", "lam_unter_1e-06"):
            e[f"C/{fld}"] = mstd([x["kugel"]["G_einbettung"]["C_kontrolle"].get(fld) for x in rs])
        for fld in ("J_neu_gegen_kugelnetz_max_rel", "max_rel_Jq5_gegen_Jq3", "max_rel_Jq5_gegen_Jq2",
                    "V_Q2_neu_gegen_KUGEL1_rel", "Jq5_min", "Jq5_max", "faktor_Q_durch_S_min", "faktor_Q_durch_S_max"):
            e[f"Q/{fld}"] = mstd([x["kugel"]["Q_quadratur"].get(fld) for x in rs])
        e["Q/V_Q5/V_K-1"] = mstd([x["kugel"]["Q_quadratur"]["V_Q5"] / x["kugel"]["geo"]["V_K"] - 1.0 for x in rs])
        e["Q/V_Q3/V_K-1"] = mstd([x["kugel"]["Q_quadratur"]["V_Q3"] / x["kugel"]["geo"]["V_K"] - 1.0 for x in rs])
        e["Q/V_Q2/V_K-1"] = mstd([x["kugel"]["Q_quadratur"]["V_Q2_neu"] / x["kugel"]["geo"]["V_K"] - 1.0 for x in rs])
        e["sekunden"] = mstd([x["sekunden"] for x in rs])
        e["sek_neu"] = mstd([x["sek_neu"] for x in rs])
        e["rss_mb_max"] = max(x["rss_mb"] for x in rs)
        e["kugel_gueltig"] = int(sum(x["kugel"]["gueltig"] for x in rs))
        e["lu_ok_je_regel"] = {r: int(sum(bool(x["lu_ok"].get(r)) for x in rs)) for r in ("C", "S", "Q", "G", "Gs")}
        besch.append(e)
    dout["beschreibend_je_N"] = besch
    out["dim4"] = dout

    # ------------------------------------------------------------------ Urteile
    U = {}
    vorbehalt = []
    if not tor:
        vorbehalt.append("Tor nicht bestanden: Urteile K2-1 bis K2-3 nicht auswertbar")
    if not k20_ok:
        ab = [k20.get("C/gamma/max_abw"), k20.get("S/gamma/max_abw")]
        vorbehalt.append(f"K2-0 nicht eingetroffen (max. Abweichung Gamma C/S {ab}): Netze bzw. Werte nicht bitgleich")
    U["K2-0"] = {"plan": "eingetroffen" if k20_ok else "nicht eingetroffen",
                 "karte": "eingetroffen" if k20_ok else "nicht eingetroffen",
                 "netze": len(vergleich), "C_gamma_alle_gleich": k20.get("C/gamma/alle_gleich"),
                 "S_gamma_alle_gleich": k20.get("S/gamma/alle_gleich"),
                 "max_abw_C_gamma": k20.get("C/gamma/max_abw"), "max_abw_S_gamma": k20.get("S/gamma/max_abw"),
                 "fehlt_in_kugel1": fehlt}
    if M >= 2:
        f = {k: fo["beta"] for k, (fo, bj) in erg.items()}
        # K2-1: Regel G, Gamma, korr; Tor G
        if tor_G:
            bG = ergG["G/gamma/korr"][0]["beta"]
            k21 = "eingetroffen" if bG["mittel"] <= -3 * bG["se"] else "nicht eingetroffen"
            U["K2-1"] = {"plan": k21, "karte": k21, "beta_G": bG, "vorzeichen_gekippt_2SE": bool(bG["mittel"] >= 2 * bG["se"]),
                         "roh": ergG["G/gamma/roh"][0]["beta"], "M_G": len(gutG)}
        else:
            U["K2-1"] = {"plan": "nicht auswertbar (Regel G nicht einbettbar)",
                         "karte": "nicht auswertbar (Regel G nicht einbettbar)", "M_G": len(gutG),
                         "ausfall_G_anteil": ausfall_G}
            if len(gutG) >= 2:
                U["K2-1"]["beschreibend_G_auf_einbettbaren_saaten"] = ergG["G/gamma/korr"][0]["beta"]
        bGs = f["Gs/gamma/korr"]
        U["K2-1"]["nebenlesart_Gs"] = {
            "urteil_nach_K2-1-Regel": "eingetroffen" if bGs["mittel"] <= -3 * bGs["se"] else "nicht eingetroffen",
            "beta_Gs_korr": bGs, "beta_Gs_roh": f["Gs/gamma/roh"],
            "vorzeichen_gekippt_2SE": bool(bGs["mittel"] >= 2 * bGs["se"])}
        # K2-2: Regel Q roh gegen S korr
        bQr, bSk = f["Q/gamma/roh"], f["S/gamma/korr"]
        c1 = bool(bQr["mittel"] <= -3 * bQr["se"])
        dpkt = bQr["mittel"] - bSk["mittel"]
        c2 = bool(abs(dpkt) <= SCHWELLE_K22)
        k22 = "eingetroffen" if (c1 and c2) else "nicht eingetroffen"
        U["K2-2"] = {"plan": k22, "karte": k22, "beta_Q_roh": bQr, "beta_S_korr": bSk, "teil1_Q_roh_le_minus_3SE": c1,
                     "differenz_punkt": dpkt, "teil2_abs_diff_le_0.3": c2,
                     "differenz_gepaart": dout["differenz_K22_Q_roh_minus_S_korr"], "beta_Q_korr": f["Q/gamma/korr"]}
        # K2-3: Spanne C, S, G, Q (Gamma, korr)
        b3 = {r: f[f"{r}/gamma/korr"]["mittel"] for r in ("C", "S", "Q")}
        span3 = max(b3.values()) - min(b3.values())
        if tor_G:
            b4 = dict(b3)
            b4["G"] = ergG["G/gamma/korr"][0]["beta"]["mittel"]
            span4 = max(b4.values()) - min(b4.values())
            k23 = "eingetroffen" if span4 <= SCHWELLE_K23 else "nicht eingetroffen"
            U["K2-3"] = {"plan": k23, "karte": k23, "betas": b4, "spanne": span4,
                         "hinweis": "G auf der Teilmenge der einbettbaren Saaten, C/S/Q auf allen guten Saaten"}
        else:
            k23 = "nicht eingetroffen" if span3 > SCHWELLE_K23 else "nicht auswertbar (Regel G fehlt)"
            U["K2-3"] = {"plan": k23, "karte": k23, "betas": b3, "spanne_C_S_Q": span3}
        b5 = dict(b3)
        b5["Gs"] = bGs["mittel"]
        span_gs = max(b5.values()) - min(b5.values())
        U["K2-3"]["nebenlesart_Gs"] = {"betas": b5, "spanne": span_gs,
                                       "urteil_nach_K2-3-Regel": "eingetroffen" if span_gs <= SCHWELLE_K23
                                       else "nicht eingetroffen"}
        if vorbehalt:
            for k in ("K2-1", "K2-2", "K2-3"):
                U[k]["vorbehalt"] = vorbehalt
                if not tor:
                    U[k]["plan"] = "nicht auswertbar (Tor)"
    out["urteile"] = U
    with open(ziel + ".tmp", "w") as fh:
        json.dump(out, fh, indent=1)
    os.replace(ziel + ".tmp", ziel)
    print("geschrieben", ziel, flush=True)


if __name__ == "__main__":
    main()
