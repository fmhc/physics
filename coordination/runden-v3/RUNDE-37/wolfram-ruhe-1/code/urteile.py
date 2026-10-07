"""WOLFRAM-RUHE-1 (Runde 42): Urteilsregeln nach PLAN.md Abschn. 4 und 6, je Plan und Kartenwortlaut.
Nur ueber kleintest.sh auf der .69 benutzt."""
import math

import numpy as np

N_BINS = [(50, 100), (100, 200), (200, 500), (500, 1000), (1000, 2001)]
ETA_BINS = [0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 2.0]


def steigung(x, r):
    """Kleinste Quadrate r = a + b x fuer 1 <= x <= 4; (b, Standardfehler, n)."""
    x = np.asarray(x, float)
    r = np.asarray(r, float)
    m = (x >= 1.0) & (x <= 4.0)
    x = x[m]
    r = r[m]
    n = len(x)
    if n < 10 or np.ptp(x) <= 0:
        return None, None, int(n)
    xm = x.mean()
    sxx = float(((x - xm) ** 2).sum())
    b = float(((x - xm) * (r - r.mean())).sum() / sxx)
    a = float(r.mean() - b * xm)
    res = r - (a + b * x)
    se = math.sqrt(float(res @ res) / (n - 2) / sxx)
    return b, se, int(n)


def median_boot(w, saat, B=200):
    w = np.asarray(w, float)
    if len(w) == 0:
        return [None, None, None]
    rng = np.random.default_rng(saat)
    meds = [float(np.median(rng.choice(w, len(w)))) for _ in range(B)]
    return [float(np.median(w)), float(np.percentile(meds, 16)), float(np.percentile(meds, 84))]


def bin_tabelle(daten, saat=1):
    """Je N-Bin: Anzahl, Steigung r gegen x, Mediane (mit 16-/84-%-Bootstrap), eta-Bins. Dazu max abs(r - x)."""
    N = np.asarray(daten["N"], float)
    L = np.asarray(daten["L"], float)
    x = np.asarray(daten["x"], float)
    r = L / (2.0 * np.sqrt(N))
    eta = np.arccosh(np.maximum(x, 1.0))
    tab = []
    for k, (lo, hi) in enumerate(N_BINS):
        m = (N >= lo) & (N < hi)
        zeile = {"bin": [lo, hi - 1 if hi == 2001 else hi], "anzahl": int(m.sum())}
        b, se, n = steigung(x[m], r[m])
        zeile["steigung"] = b
        zeile["steigung_se"] = se
        zeile["steigung_n"] = n
        zeile["median_r"] = median_boot(r[m], saat + k)
        zeile["median_r_durch_x"] = median_boot((r / x)[m], saat + 10 + k)
        if "cosh_wahr" in daten:
            cw = np.asarray(daten["cosh_wahr"], float)
            zeile["median_r_durch_cosh_wahr"] = median_boot((r / cw)[m], saat + 20 + k)
        eb = []
        for j in range(len(ETA_BINS) - 1):
            mm = m & (eta >= ETA_BINS[j]) & (eta < ETA_BINS[j + 1])
            eb.append({"eta": [ETA_BINS[j], ETA_BINS[j + 1]], "anzahl": int(mm.sum()),
                       "median_r": float(np.median(r[mm])) if mm.any() else None,
                       "q16_r": float(np.percentile(r[mm], 16)) if mm.any() else None,
                       "q84_r": float(np.percentile(r[mm], 84)) if mm.any() else None,
                       "median_x": float(np.median(x[mm])) if mm.any() else None})
        zeile["eta_bins"] = eb
        zeile["anzahl_x_le_1_2"] = int((m & (x <= 1.2)).sum())
        zeile["anzahl_x_ge_1_8"] = int((m & (x >= 1.8)).sum())
        tab.append(zeile)
    maxabw = float(np.max(np.abs(r - x))) if len(r) else None
    return tab, maxabw


def urteil_wr0(tabP, tabG, maxabw_G):
    P_i = all(z["steigung"] is not None and abs(z["steigung"]) <= 0.05 for z in tabP if z["anzahl"] >= 200)
    mP = tabP[-1]["median_r"][0]
    P_ii = mP is not None and 0.92 <= mP <= 1.05
    G_i = maxabw_G is not None and maxabw_G <= 1e-9
    mG = tabG[-1]["median_r_durch_cosh_wahr"][0]
    G_ii = mG is not None and abs(mG - 1.0) <= 0.02
    G_iii = all(z["steigung"] is not None and 0.9 <= z["steigung"] <= 1.1 for z in tabG if z["anzahl"] >= 200)
    plan = P_i and P_ii and G_i and G_ii and G_iii
    kP_niveau = all(z["median_r"][0] is not None and 0.95 <= z["median_r"][0] <= 1.05 for z in tabP if z["anzahl"] > 0)
    kP_trend = P_i
    kG = all(abs(z["median_r_durch_x"][0] - 1.0) <= 0.02 for z in tabG if z["anzahl"] > 0)
    kG_wahr = all(abs(z["median_r_durch_cosh_wahr"][0] - 1.0) <= 0.02 for z in tabG if z["anzahl"] > 0)
    karte = kP_niveau and kP_trend and kG
    return {"plan": {"P_i": P_i, "P_ii": P_ii, "G_i": G_i, "G_ii": G_ii, "G_iii": G_iii,
                     "urteil": "eingetroffen" if plan else "verfehlt"},
            "kartenwortlaut": {"poisson_niveau_jeder_bin": kP_niveau, "poisson_ohne_trend": kP_trend,
                               "gitter_programm_eta": kG, "gitter_eta_wahr_zusatz": kG_wahr,
                               "urteil": "eingetroffen" if karte else "verfehlt"}}


def urteil_wr1(e):
    a_bestimmbar = e.get("D_geo") is not None
    a = a_bestimmbar and 1.8 <= e["D_geo"] <= 2.2
    b = e.get("s_b") is not None and e["s_b"] >= 0.25 and e["ereignisse_je_gen_letztes_zehntel"] >= 10
    c = 1.8 <= e["D_gen"] <= 2.2
    plan = a and b and c
    if not a_bestimmbar:
        karte = "nicht bestimmbar"
    else:
        karte = "eingetroffen" if a else "verfehlt"
    return {"a_geodaetisch": a, "a_bestimmbar": a_bestimmbar, "b_front_Z_K1": b, "c_generationskegel_Z_A": c,
            "plan": "eingetroffen" if plan else "verfehlt", "kartenwortlaut": karte}


def urteil_wr2(tabR, tabG, c_R2, bedingung):
    if not bedingung:
        return {"urteil": "nicht geprueft (WR1 nicht erfuellt)"}
    if c_R2 is None or not (c_R2 == c_R2) or tabR is None:
        return {"urteil": "nicht entscheidbar (c^2 <= 0, eta nicht definiert)"}
    s = []
    for k in (-2, -1):
        zR = tabR[k]
        zG = tabG[k]
        if zR["anzahl_x_le_1_2"] < 30 or zR["anzahl_x_ge_1_8"] < 30 or zR["steigung"] is None or not zG["steigung"]:
            return {"urteil": "nicht entscheidbar (eta-Spannweite fehlt)", "bin": zR["bin"]}
        s.append(zR["steigung"] / zG["steigung"])
    if s[0] >= 0.5 and s[1] >= 0.5:
        u = "eingetroffen"
    elif s[1] < 0.5:
        u = "verfehlt"
    else:
        u = "unentschieden"
    return {"urteil": u, "s_zweitgroesster_bin": s[0], "s_groesster_bin": s[1]}
