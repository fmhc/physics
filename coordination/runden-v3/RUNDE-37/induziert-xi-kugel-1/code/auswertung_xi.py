#!/usr/bin/env python3
"""INDUZIERT-XI-KUGEL-1 (Runde 40/41, Code-Agent): mechanische Auswertung nach PLAN.md (Abschnitte 3, 5 und 6).

Kugelseite (Regel Q, A(xi) = K + xi R M) aus den eigenen Laufdateien, Torusseite aus den Laufdateien von
INDUZIERT-KUGEL-1 (gleiche Saat, gleiches N), Vergleich XI0 gegen die Laufdateien von INDUZIERT-KUGEL-2 (Regel Q, Gamma).
Fit und Statistik unveraendert aus auswertung_kugel.py (INDUZIERT-KUGEL-1):
  je Saat y_j(N) = beta_j + delta_j/sqrt(N) (OLS ueber die N), beta = Mittel der beta_j, SE = Std(ddof 1)/sqrt(M).
Fassungen von y(N, xi) = (G_Kugel(xi) - Gamma_Torus)/sqrt(N):
  haupt     G = Gamma~(xi) = Gamma(xi) - 1/2 ln(xi R V_R/N) fuer xi > 0 (fruehere Nullmode exakt abgezogen; Plan),
            G = Gamma(0) fuer xi = 0 (bitgleich KUGEL-2, Regel Q, Gamma, roh).
  null_drin G = Gamma(xi) ohne Abzug (beschreibend: Groesse des Nullmoden-Glieds).
  log_voll  G = Gamma~(xi) - (xi - 3 xi^2) ln N (zusaetzlich das universelle ln-N-Glied der Masse; beschreibend).
Aufruf (nur ueber kleintest.sh):
  python auswertung_xi.py <lauf-ordner> <kugel1-lauf-ordner> <kugel2-lauf-ordner> <aus.json> [kugel2-auswertung.json]
"""
import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import auswertung_kugel as k1a  # noqa: E402  (unveraendert aus INDUZIERT-KUGEL-1)

XI = (0.0, 1.0 / 12.0, 1.0 / 6.0, 0.25)
XI_NAME = ("0", "1/12", "1/6", "1/4")
XI_KONS = 1.0 / 6.0
MIN_SAATEN = 18
MAX_AUSFALL = 0.10
FENSTER_XI2 = (0.10, 0.25)
FENSTER_XI3_PLAN = (2.0 / 15.0, 0.2)
FENSTER_XI3_KARTE = (0.133, 0.200)
GAMMA_KONT0 = -29.0 / 360.0
VERGLEICH_XI0 = ("gamma", "gamma_M", "sum_log_m", "V", "korr", "korr_M", "lam_min")
FASSUNGEN = ("haupt", "null_drin", "log_voll")


def g_log_m(xi):
    """Universeller ln-N-Koeffizient der Nicht-Null-Moden relativ zu xi = 0 [M, PLAN S5]: xi - 3 xi^2."""
    return xi - 3.0 * xi * xi


def pseudo(q0, torus, N):
    return {"kugel": {"regeln": {"Q": q0}}, "torus": torus, "N": N}


def y_xi(rec, torus, N, ix, fassung):
    """y(N, xi_ix) einer Messung in einer Fassung (ix = 0..3); ix = 'kons' fuer die konsistente Masse bei xi = 1/6."""
    k = rec["kugel"]
    if ix == 0:
        return k1a.y_wert(pseudo(k["Q0"], torus, N), "Q", "gamma", "roh")
    r = k["xi_kons"] if ix == "kons" else k["xi"][ix - 1]
    g = r["gamma"] if fassung == "null_drin" else r["gamma_tilde"]
    if fassung == "log_voll":
        g = g - g_log_m(r["xi"]) * math.log(N)
    return (g - torus["gamma"]) / math.sqrt(N)


def steigung(B):
    """B: (M, 4) beta_j(xi). Je Saat OLS-Gerade ueber xi: Achsenabschnitt b_j, Steigung g_j, Reste r_j(xi)."""
    x = np.asarray(XI)
    xc = x - x.mean()
    sxx = float(np.sum(xc ** 2))
    g = (B - B.mean(axis=1, keepdims=True)) @ xc / sxx
    b = B.mean(axis=1) - g * x.mean()
    r = B - (b[:, None] + g[:, None] * x[None, :])
    return b, g, r


def xi_stern(B0, G):
    """xi* = -mean(B0)/mean(G); SE per Delta-Methode mit gepaarter Kovarianz und per Jackknife ueber die Saaten."""
    B0, G = np.asarray(B0, float), np.asarray(G, float)
    M = B0.size
    mb, mg = float(B0.mean()), float(G.mean())
    xs = -mb / mg
    out = {"xi_stern": xs, "beta0": mb, "gamma": mg, "M": int(M), "se_delta": None, "se_jackknife": None}
    if M >= 2:
        C = np.cov(np.vstack([B0, G]), ddof=1)
        var = (C[0, 0] + xs ** 2 * C[1, 1] + 2.0 * xs * C[0, 1]) / (M * mg ** 2)
        jk = np.array([-(B0.sum() - B0[i]) / (G.sum() - G[i]) for i in range(M)])
        out["se_delta"] = math.sqrt(max(float(var), 0.0))
        out["se_jackknife"] = math.sqrt((M - 1) / M * float(np.sum((jk - jk.mean()) ** 2)))
        out["korrelation_beta0_gamma"] = float(C[0, 1] / math.sqrt(C[0, 0] * C[1, 1])) if C[0, 0] * C[1, 1] > 0 else None
    return out


def linearitaet(B):
    b, g, r = steigung(B)
    M = B.shape[0]
    se_p = B.std(axis=0, ddof=1) / math.sqrt(M)
    se_r = r.std(axis=0, ddof=1) / math.sqrt(M)
    rm = r.mean(axis=0)
    d2 = np.stack([B[:, 2] - 2 * B[:, 1] + B[:, 0], B[:, 3] - 2 * B[:, 2] + B[:, 1]], axis=1)
    return {"gamma": k1a.stat(g), "achsenabschnitt": k1a.stat(b), "beta_je_xi": [k1a.stat(B[:, i]) for i in range(4)],
            "rest": rm.tolist(), "se_punkt": se_p.tolist(), "se_rest_gepaart": se_r.tolist(),
            "rest_durch_se_punkt": (rm / se_p).tolist(),
            "rest_durch_se_gepaart": [float(x / y) if y > 0 else None for x, y in zip(rm, se_r)],
            "linear_punkt_2SE": bool(np.all(np.abs(rm) <= 2.0 * se_p)),
            "linear_gepaart_2SE": bool(np.all(np.abs(rm) <= 2.0 * se_r)),
            "zweite_differenzen": [k1a.stat(d2[:, 0]), k1a.stat(d2[:, 1])],
            "xi_stern": xi_stern(B[:, 0], g), "xi_stern_linie": -float(b.mean()) / float(g.mean()),
            "gamma_je_saat": g.tolist()}, g


def main():
    ordner, ordner1, ordner2, ziel = sys.argv[1:5]
    pfad_aw2 = sys.argv[5] if len(sys.argv) > 5 else None
    mein, dateien, doppelt = k1a.laden(ordner)
    alt1, dateien1, _ = k1a.laden(ordner1)
    alt2, dateien2, _ = k1a.laden(ordner2)
    mein = {k: v for k, v in mein.items() if k[0] == 4}
    alt1 = {k: v for k, v in alt1.items() if k[0] == 4}
    alt2 = {k: v for k, v in alt2.items() if k[0] == 4}
    out = {"dateien": dateien, "doppelt_ignoriert": doppelt, "dateien_kugel1": dateien1, "dateien_kugel2": dateien2,
           "konstanten": {"XI": list(XI), "XI_KONS": XI_KONS, "MIN_SAATEN": MIN_SAATEN, "MAX_AUSFALL": MAX_AUSFALL,
                          "FENSTER_XI2": list(FENSTER_XI2), "FENSTER_XI3_PLAN": list(FENSTER_XI3_PLAN),
                          "FENSTER_XI3_KARTE": list(FENSTER_XI3_KARTE), "GAMMA_KONT0": GAMMA_KONT0}}

    # ------------------------------------------------------------------ XI0 je Netz: Gamma_Q(0) gegen INDUZIERT-KUGEL-2
    vergleich, fehlt2 = [], []
    for key in sorted(mein):
        a2 = alt2.get(key)
        if a2 is None:
            fehlt2.append(list(key))
            continue
        q0, q2 = mein[key]["kugel"]["Q0"], a2["kugel"]["regeln"]["Q"]
        e = {"N": key[1], "saat": key[2]}
        for f in VERGLEICH_XI0:
            x, y = q0.get(f), q2.get(f)
            e[f + "/gleich"] = bool(x is not None and y is not None and x == y)
            e[f + "/abw"] = abs(x - y) if (x is not None and y is not None) else None
        for f in ("a", "V_K"):
            e["geo/" + f + "/gleich"] = bool(mein[key]["kugel"]["geo"][f] == a2["kugel"]["geo"][f])
        e["F/gleich"] = bool(mein[key]["kugel"]["pruefung"]["F"] == a2["kugel"]["pruefung"]["F"])
        vergleich.append(e)
    x0 = {"anzahl_netze": len(vergleich), "fehlt_in_kugel2": fehlt2}
    for f in [g + "/" for g in VERGLEICH_XI0] + ["geo/a/", "geo/V_K/", "F/"]:
        x0[f + "alle_gleich"] = bool(vergleich) and all(e[f + "gleich"] for e in vergleich)
        ab = [e.get(f + "abw") for e in vergleich if e.get(f + "abw") is not None]
        if ab:
            x0[f + "max_abw"] = max(ab)
    x0_netz = bool(vergleich and not fehlt2 and x0["gamma/alle_gleich"])
    out["XI0_vergleich"] = x0
    out["XI0_je_netz"] = vergleich

    # ------------------------------------------------------------------ Zusammenfuehren, Tor
    recs = {}
    for key, m in mein.items():
        a1 = alt1.get(key)
        if a1 is None:
            continue
        t_ok = bool(a1["torus"]["gueltig"] and a1["lu_ok"][2])
        recs[key] = {"m": m, "torus": a1["torus"], "torus_ok": t_ok, "gueltig": bool(m["gueltig"] and t_ok)}
    Ns = sorted({k[1] for k in recs})
    saaten = sorted({k[2] for k in mein})
    gut, aus, unvollst, gruende = [], [], [], {}
    for s in saaten:
        vorhanden = [(4, N, s) in recs for N in Ns]
        gueltig = [recs[(4, N, s)]["gueltig"] for N in Ns if (4, N, s) in recs]
        if not all(gueltig):
            aus.append(s)
            gruende[str(s)] = [{"N": N, "kugel": recs[(4, N, s)]["m"]["kugel"]["gueltig"],
                                "torus": recs[(4, N, s)]["torus_ok"], "lu_ok": recs[(4, N, s)]["m"]["lu_ok"]}
                               for N in Ns if (4, N, s) in recs and not recs[(4, N, s)]["gueltig"]]
        elif not all(vorhanden):
            unvollst.append(s)
        else:
            gut.append(s)
    M = len(gut)
    ausfall = len(aus) / max(1, len(aus) + M)
    tor = bool(M >= MIN_SAATEN and ausfall <= MAX_AUSFALL)
    dout = {"Nlist": Ns, "saaten_gut": gut, "saaten_ausgeschlossen": aus, "gruende": gruende,
            "saaten_unvollstaendig": unvollst, "M": M, "ausfall_anteil": ausfall, "tor_bestanden": tor}

    # ------------------------------------------------------------------ Kontrollen in jedem Netz
    alle = list(recs.values())
    kon = {"netze": len(alle),
           "form_monoton": int(sum(bool(r["m"]["form"].get("monoton")) for r in alle)),
           "form_konkav": int(sum(bool(r["m"]["form"].get("konkav")) for r in alle)),
           "form_kons_monoton": int(sum(bool(r["m"]["form"].get("kons_monoton")) for r in alle)),
           "R_mal_a2_max_abw": max((abs(r["m"]["kugel"]["masse"]["R_mal_a2"] - 12.0) for r in alle), default=None),
           "summe_m_rel_max": max((r["m"]["kugel"]["masse"].get("summe_m_rel", 1.0) for r in alle), default=None),
           "Mk_zeilensumme_rel_max": max((r["m"]["kugel"]["masse"].get("Mk_zeilensumme_rel", 1.0) for r in alle),
                                         default=None),
           "Mk_summe_rel_max": max((r["m"]["kugel"]["masse"].get("Mk_summe_rel", 1.0) for r in alle), default=None)}
    kon["form_alle"] = bool(alle and kon["form_monoton"] == len(alle) and kon["form_konkav"] == len(alle)
                            and kon["form_kons_monoton"] == len(alle))
    dout["kontrollen_je_netz"] = kon

    U = {}
    if M >= 2:
        # -------------------------------------------------------------- Fits je Fassung und xi
        fits, Bm = {}, {}
        for f in FASSUNGEN:
            cols = []
            for ix, xn in enumerate(XI_NAME):
                Y = np.array([[y_xi(recs[(4, N, s)]["m"], recs[(4, N, s)]["torus"], N, ix, f) for N in Ns]
                              for s in gut])
                fo, bj = k1a.fits(Ns, Y)
                fits[f"{f}/{xn}"] = fo
                cols.append(bj)
            Bm[f] = np.stack(cols, axis=1)
            Yk = np.array([[y_xi(recs[(4, N, s)]["m"], recs[(4, N, s)]["torus"], N, "kons", f) for N in Ns]
                           for s in gut])
            fo, bk = k1a.fits(Ns, Yk)
            fits[f"{f}/kons_1/6"] = fo
            Bm[f + "/kons"] = bk
        YM = np.array([[k1a.y_wert(pseudo(recs[(4, N, s)]["m"]["kugel"]["Q0"], recs[(4, N, s)]["torus"], N), "Q",
                                   "gamma_M", "roh") for N in Ns] for s in gut])
        foM, bM = k1a.fits(Ns, YM)
        fits["gamma_M/0"] = foM
        dout["fits"] = fits
        b0_empf = fits["haupt/0"]["gamma_empfindlichkeit_b0"]

        # -------------------------------------------------------------- Steigung, Linearitaet, xi*
        lin, gj = {}, {}
        for f in FASSUNGEN:
            lin[f], gj[f] = linearitaet(Bm[f])
        dout["linearitaet"] = lin
        B0 = Bm["haupt"][:, 0]
        gk = (Bm["haupt/kons"] - B0) / XI_KONS
        neben = {"Mk_konsistente_masse": {"gamma_k": k1a.stat(gk), "xi_stern": xi_stern(B0, gk),
                                          "beta_kons_1/6": k1a.stat(Bm["haupt/kons"]),
                                          "beta_kons_minus_beta_1/6": k1a.stat(Bm["haupt/kons"] - Bm["haupt"][:, 2]),
                                          "verhaeltnis_gamma_k_durch_gamma": float(gk.mean() / gj["haupt"].mean())},
                 "gamma_M": {"beta_M0": k1a.stat(bM), "xi_stern": xi_stern(bM, gj["haupt"]),
                             "hinweis": "Steigung exakt gleich der von Gamma (PLAN S2)"},
                 "beta0_mit_gamma_kont": {"beta0": float(B0.mean() - GAMMA_KONT0 * b0_empf),
                                          "xi_stern_log_voll": -float(B0.mean() - GAMMA_KONT0 * b0_empf)
                                          / float(gj["log_voll"].mean())}}
        # Nullmoden-Glied: Verschiebung null_drin - haupt gegen -b0/4
        neben["nullmode_verschiebung"] = {XI_NAME[i]: k1a.stat(Bm["null_drin"][:, i] - Bm["haupt"][:, i])
                                          for i in range(1, 4)}
        neben["nullmode_verschiebung"]["erwartet_minus_b0_viertel"] = -0.25 * b0_empf
        # F3: freier Dreiparameterfit (beta, gamma_ln, delta) auf die gepaarten Differenzen y(xi) - y(0), Fassung null_drin
        if len(Ns) >= 3:
            X3 = k1a.design(Ns, "3p")
            cols, gln = [np.zeros(M)], {}
            for ix in range(1, 4):
                D = np.array([[y_xi(recs[(4, N, s)]["m"], recs[(4, N, s)]["torus"], N, ix, "null_drin")
                               - y_xi(recs[(4, N, s)]["m"], recs[(4, N, s)]["torus"], N, 0, "haupt") for N in Ns]
                              for s in gut])
                B3 = np.linalg.lstsq(X3, D.T, rcond=None)[0]
                cols.append(B3[0])
                gln[XI_NAME[ix]] = {"gamma_ln": k1a.stat(B3[1]), "erwartet": -0.25 + g_log_m(XI[ix]),
                                    "beta_D": k1a.stat(B3[0])}
            BF = np.stack(cols, axis=1) + B0[:, None]
            linF, gF = linearitaet(BF)
            neben["F3_frei"] = {"ln_koeffizienten": gln, "gamma": linF["gamma"], "xi_stern": linF["xi_stern"],
                                "linear_punkt_2SE": linF["linear_punkt_2SE"], "rest": linF["rest"],
                                "se_punkt": linF["se_punkt"]}
        dout["nebenlesarten"] = neben

        # -------------------------------------------------------------- XI0 auf Fit-Ebene
        x0_fit = {"vergleich_moeglich": False}
        try:
            Y2 = np.array([[k1a.y_wert(pseudo(alt2[(4, N, s)]["kugel"]["regeln"]["Q"], alt1[(4, N, s)]["torus"], N),
                                       "Q", "gamma", "roh") for N in Ns] for s in gut])
            fo2, b2 = k1a.fits(Ns, Y2)
            x0_fit = {"vergleich_moeglich": True, "beta0_hier": fits["haupt/0"]["beta"]["mittel"],
                      "beta0_kugel2_gleiche_saaten": fo2["beta"]["mittel"],
                      "beta0_gleich": bool(fits["haupt/0"]["beta"]["mittel"] == fo2["beta"]["mittel"]),
                      "se_gleich": bool(fits["haupt/0"]["beta"]["se"] == fo2["beta"]["se"]),
                      "beta_je_saat_gleich": bool(np.array_equal(Bm["haupt"][:, 0], b2)),
                      "max_abw_beta_je_saat": float(np.max(np.abs(Bm["haupt"][:, 0] - b2)))}
        except KeyError as exc:
            x0_fit["fehler"] = f"fehlender Schluessel {exc}"
        if pfad_aw2:
            try:
                with open(pfad_aw2) as fh:
                    aw2 = json.load(fh)
                d2 = aw2["dim4"]
                x0_fit["kugel2_auswertung"] = {"saaten_gleich": bool(d2["saaten_gut"] == gut),
                                               "beta_Q_roh": d2["fits"]["Q/gamma/roh"]["beta"]["mittel"]}
                if d2["saaten_gut"] == gut:
                    x0_fit["kugel2_auswertung"]["gleich"] = bool(
                        d2["fits"]["Q/gamma/roh"]["beta"]["mittel"] == fits["haupt/0"]["beta"]["mittel"])
            except (OSError, KeyError, ValueError) as exc:
                x0_fit["kugel2_auswertung"] = {"fehler": str(exc)}
        out["XI0_fit"] = x0_fit

        # -------------------------------------------------------------- Urteile
        x0_ok = bool(x0_netz and x0_fit.get("beta0_gleich") and x0_fit.get("beta_je_saat_gleich"))
        U["XI0"] = {"plan": "eingetroffen" if x0_ok else "nicht eingetroffen",
                    "karte": "eingetroffen" if bool(x0_fit.get("beta0_gleich")) else "nicht eingetroffen",
                    "netze_gleich": x0_netz, "netze": len(vergleich), "max_abw_gamma": x0.get("gamma/max_abw"),
                    "fit": x0_fit}
        L = lin["haupt"]
        gs = L["gamma"]
        teil1 = bool(gs["mittel"] >= 3.0 * gs["se"])
        teil2 = L["linear_punkt_2SE"]
        k1u = "eingetroffen" if (teil1 and teil2) else "nicht eingetroffen"
        U["XI1"] = {"plan": k1u, "karte": k1u, "gamma": gs, "teil1_gamma_ge_3SE": teil1, "teil2_linear_2SE_punkt": teil2,
                    "rest": L["rest"], "se_punkt": L["se_punkt"], "rest_durch_se_punkt": L["rest_durch_se_punkt"],
                    "streng_gepaart": {"linear": L["linear_gepaart_2SE"], "se_rest": L["se_rest_gepaart"],
                                       "rest_durch_se": L["rest_durch_se_gepaart"]}}
        xs = L["xi_stern"]
        se = xs["se_delta"] or 0.0

        def im(f):
            return bool(f[0] <= xs["xi_stern"] <= f[1])

        def grenz(f):
            lo, hi = xs["xi_stern"] - 2 * se, xs["xi_stern"] + 2 * se
            return bool(lo < f[0] < hi or lo < f[1] < hi)
        U["XI2"] = {"plan": "eingetroffen" if im(FENSTER_XI2) else "nicht eingetroffen",
                    "karte": "eingetroffen" if im(FENSTER_XI2) else "nicht eingetroffen", "xi_stern": xs,
                    "fenster": list(FENSTER_XI2), "grenzfall_2SE": grenz(FENSTER_XI2)}
        U["XI3"] = {"plan": "eingetroffen" if im(FENSTER_XI3_PLAN) else "nicht eingetroffen",
                    "karte": "eingetroffen" if im(FENSTER_XI3_KARTE) else "nicht eingetroffen", "xi_stern": xs,
                    "fenster_plan": list(FENSTER_XI3_PLAN), "fenster_karte": list(FENSTER_XI3_KARTE),
                    "grenzfall_2SE": grenz(FENSTER_XI3_PLAN), "abstand_zu_1/6_in_SE": (xs["xi_stern"] - 1.0 / 6.0) / se
                    if se > 0 else None}
        vorbehalt = []
        if not tor:
            vorbehalt.append("Tor nicht bestanden: XI1 bis XI3 (Plan) nicht auswertbar")
        if U["XI0"]["plan"] != "eingetroffen":
            vorbehalt.append(f"XI0 nicht eingetroffen (max. Abweichung Gamma {x0.get('gamma/max_abw')})")
        if not kon["form_alle"]:
            vorbehalt.append("Formkontrolle (monoton, konkav) nicht in allen Netzen erfuellt")
        for k in ("XI1", "XI2", "XI3"):
            if vorbehalt:
                U[k]["vorbehalt"] = vorbehalt
            if not tor:
                U[k]["plan"] = "nicht auswertbar (Tor)"

    # ------------------------------------------------------------------ beschreibend je N
    besch = []
    for N in Ns:
        rs = [recs[(4, N, s)] for s in gut if (4, N, s) in recs]
        if not rs:
            continue
        e = {"N": N, "anzahl": len(rs), "a": rs[0]["m"]["kugel"]["geo"]["a"],
             "F": k1a.stat([r["m"]["kugel"]["pruefung"]["F"] for r in rs]),
             "V_Q5/V_K-1": k1a.stat([r["m"]["kugel"]["Q_quadratur"]["V_Q5"] / r["m"]["kugel"]["geo"]["V_K"] - 1.0
                                     for r in rs]),
             "sekunden": k1a.stat([r["m"]["sekunden"] for r in rs]),
             "rss_mb_max": max(r["m"]["rss_mb"] for r in rs),
             "nullmode": {XI_NAME[i]: k1a.stat([r["m"]["kugel"]["xi"][i - 1]["nullmode"] for r in rs]) for i in (1, 2, 3)},
             "sek_lu": {XI_NAME[i]: k1a.stat([r["m"]["kugel"]["xi"][i - 1]["lu"]["sek_lu"] for r in rs]) for i in (1, 2, 3)},
             "min_U": min(min(x["lu"]["min_U"] for x in r["m"]["kugel"]["xi"]) for r in rs),
             "y_haupt": {XI_NAME[i]: k1a.stat([y_xi(r["m"], r["torus"], N, i, "haupt") for r in rs]) for i in range(4)},
             "zuwachs_haupt": {XI_NAME[i]: k1a.stat([y_xi(r["m"], r["torus"], N, i, "haupt")
                                                     - y_xi(r["m"], r["torus"], N, 0, "haupt") for r in rs])
                               for i in (1, 2, 3)},
             "zuwachs_kons_1/6": k1a.stat([y_xi(r["m"], r["torus"], N, "kons", "haupt")
                                           - y_xi(r["m"], r["torus"], N, 0, "haupt") for r in rs])}
        besch.append(e)
    dout["beschreibend_je_N"] = besch
    out["dim4"] = dout
    out["urteile"] = U
    with open(ziel + ".tmp", "w") as fh:
        json.dump(out, fh, indent=1)
    os.replace(ziel + ".tmp", ziel)
    print("geschrieben", ziel, flush=True)


if __name__ == "__main__":
    main()
