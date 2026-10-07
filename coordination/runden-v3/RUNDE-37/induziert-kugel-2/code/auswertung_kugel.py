#!/usr/bin/env python3
"""INDUZIERT-KUGEL-1 (Runde 39, Code-Agent): mechanische Auswertung nach PLAN.md (Abschnitte 6 und 7).

Messgroesse je Saat j, Dimension n, Regel r (C, S), Groesse q (Gamma, Gamma_M) und Fassung v (korr, roh):
  y_j(N) = (G_Kugel(N) - G_Torus(N))/sqrt(N);  Fit je Saat y_j(N) = beta_j + delta_j/sqrt(N) (gamma = 0, OLS ueber N).
  beta = Mittel der beta_j, SE = Std(beta_j, ddof 1)/sqrt(M).
Aufruf (nur ueber kleintest.sh): python auswertung_kugel.py <lauf-ordner> <aus.json>
"""
import glob
import json
import math
import os
import sys

import numpy as np
from scipy.special import iv
from scipy.stats import chi2

C_T, SE_C_T = 0.111, 0.045                          # INDUZIERT-DICHTE-4D, rho = 1, Regel sp
INT_R = 16.0 * math.pi * math.sqrt(1.5)             # Int sqrt(g) R auf S^4 durch sqrt(N), Dichte 1 (61,562)
ZIEL_KARTE = (1.14, 0.46)                           # Karte KU2: 10,26 c_Torus
S_FAKTOR = float((iv(1, 0.5) / 0.25) * iv(0, 1.0) ** -0.5)   # 0,9168 (S-Schema und Dichte bei fester Punktzahl)
FAKTOR_PLAN = INT_R / (6.0 * S_FAKTOR)              # 11,19
ZIEL_PLAN = (FAKTOR_PLAN * C_T, FAKTOR_PLAN * SE_C_T)
H_KONT = -0.58
GAMMA_KONT = {4: -29.0 / 360.0, 2: -1.0 / 6.0}
MIN_SAATEN = 8
MAX_AUSFALL = 0.10
REGELN = ("C", "S")
GROESSEN = ("gamma", "gamma_M")
FASSUNGEN = ("korr", "roh")


def f(x):
    return None if x is None else float(x)


def laden(ordner):
    recs, dateien, doppelt = {}, [], []
    for d in sorted(glob.glob(os.path.join(ordner, "messung-*.json"))):
        with open(d) as fh:
            inhalt = json.load(fh)
        dateien.append(os.path.basename(d))
        if inhalt.get("blind"):
            continue
        for r in inhalt["messungen"]:
            key = (int(r["n"]), int(r["N"]), int(r["saat"]))
            if key in recs:
                doppelt.append(list(key))
                continue
            r["_datei"] = os.path.basename(d)
            recs[key] = r
    return recs, dateien, doppelt


def y_wert(rec, r, q, v):
    k = rec["kugel"]["regeln"][r]
    t = rec["torus"]
    kq = "korr" if q == "gamma" else "korr_M"
    gs = k[q] + (k[kq] if v == "korr" else 0.0)
    gt = t[q] + (t[kq] if v == "korr" else 0.0)
    return (gs - gt) / math.sqrt(rec["N"])


def design(Ns, basis):
    Ns = np.asarray(Ns, dtype=float)
    u = 1.0 / np.sqrt(Ns)
    if basis == "2p":
        return np.stack([np.ones_like(u), u], axis=1)
    return np.stack([np.ones_like(u), np.log(Ns) * u, u], axis=1)


def stat(werte):
    w = np.asarray(werte, dtype=float)
    M = w.size
    if M < 2:
        return {"mittel": f(w.mean()) if M else None, "std": None, "se": None, "M": int(M), "t": None}
    sd = float(np.std(w, ddof=1))
    se = sd / math.sqrt(M)
    return {"mittel": float(w.mean()), "std": sd, "se": se, "M": int(M), "t": float(w.mean() / se) if se > 0 else None}


def fits(Ns, Y):
    """Y: (M, len(Ns)) je Saat. Rueckgabe: Hauptfit (2p je Saat), 3p je Saat, WLS auf Mittelwerte, Teilbereiche."""
    Ns = list(Ns)
    X2 = design(Ns, "2p")
    B2 = np.linalg.lstsq(X2, Y.T, rcond=None)[0]          # (2, M)
    out = {"beta": stat(B2[0]), "delta": stat(B2[1]), "beta_je_saat": [float(x) for x in B2[0]]}
    if len(Ns) >= 3:
        X3 = design(Ns, "3p")
        B3 = np.linalg.lstsq(X3, Y.T, rcond=None)[0]
        out["drei_parameter"] = {"beta": stat(B3[0]), "gamma": stat(B3[1]), "delta": stat(B3[2])}
    # gamma-Empfindlichkeit: Achsenabschnitt b0 des OLS-Fits von ln N/sqrt N auf [1, 1/sqrt N]
    ell = np.log(np.asarray(Ns, float)) / np.sqrt(np.asarray(Ns, float))
    b0 = float(np.linalg.lstsq(X2, ell, rcond=None)[0][0])
    out["gamma_empfindlichkeit_b0"] = b0
    # WLS auf die Mittelwerte je N (Gewichte 1/SE^2 aus der Saatstreuung) und Modellprobe
    m = Y.mean(axis=0)
    se = Y.std(axis=0, ddof=1) / math.sqrt(Y.shape[0])
    W = 1.0 / se ** 2
    A = X2.T @ (W[:, None] * X2)
    cov = np.linalg.inv(A)
    b = cov @ (X2.T @ (W * m))
    res = m - X2 @ b
    chi = float(np.sum(W * res ** 2))
    dof = len(Ns) - 2
    out["wls_mittelwerte"] = {"beta": float(b[0]), "se_beta": float(math.sqrt(cov[0, 0])), "delta": float(b[1]),
                              "se_delta": float(math.sqrt(cov[1, 1])), "chi2": chi, "fg": dof,
                              "p": float(chi2.sf(chi, dof)) if dof > 0 else None}
    out["je_N"] = [{"N": int(N), "y_mittel": float(m[i]), "y_se": float(se[i]), "y_std": float(Y[:, i].std(ddof=1))}
                   for i, N in enumerate(Ns)]
    # Teilbereiche (beschreibend): ohne kleinstes N, ohne groesstes N
    teil = {}
    if len(Ns) >= 3:
        for name, sel in (("ohne_kleinstes_N", slice(1, None)), ("ohne_groesstes_N", slice(0, -1))):
            Xs = design(Ns[sel], "2p")
            Bs = np.linalg.lstsq(Xs, Y[:, sel].T, rcond=None)[0]
            teil[name] = {"Nlist": [int(x) for x in Ns[sel]], "beta": stat(Bs[0])}
    out["teilbereiche"] = teil
    return out, B2[0]


def urteil_ku0(b):
    m, se = b["mittel"], b["se"]
    karte = "eingetroffen" if (abs(m) <= 2 * se and abs(m) <= 0.05) else "nicht eingetroffen"
    if abs(m) <= 2 * se and abs(m) <= 0.05:
        plan = "eingetroffen"
    elif abs(m) > 2 * se:
        plan = "nicht eingetroffen"
    else:
        plan = "nicht auswertbar"
    return plan, karte


def urteil_ku1(b):
    m, se = b["mittel"], b["se"]
    karte = "eingetroffen" if m >= 3 * se else "nicht eingetroffen"
    if m - 3 * se >= 0:
        plan = "eingetroffen"
    elif m + 2 * se < 0:
        plan = "nicht eingetroffen"
    else:
        plan = "nicht auswertbar"
    return plan, karte, bool(m <= -3 * se)


def urteil_ku2(b, ziel):
    m, se = b["mittel"], b["se"]
    sek = math.sqrt(se ** 2 + ziel[1] ** 2)
    abst = abs(m - ziel[0])
    return ("eingetroffen" if abst <= 2 * sek else "nicht eingetroffen"), {
        "ziel": ziel[0], "se_ziel": ziel[1], "se_kombiniert": sek, "abstand": abst, "abstand_in_se_komb": abst / sek,
        "eng_nur_se_beta": "eingetroffen" if abst <= 2 * se else "nicht eingetroffen"}


def urteil_ku3(bC, bS):
    karte = "eingetroffen" if np.sign(bC["mittel"]) != np.sign(bS["mittel"]) else "nicht eingetroffen"
    getrennt = abs(bC["mittel"]) > 2 * bC["se"] and abs(bS["mittel"]) > 2 * bS["se"]
    if getrennt and np.sign(bC["mittel"]) != np.sign(bS["mittel"]):
        plan = "eingetroffen"
    elif getrennt:
        plan = "nicht eingetroffen"
    else:
        plan = "nicht auswertbar"
    return plan, karte


def urteil_ku4(d):
    return "eingetroffen" if abs(d["mittel"]) > 2 * d["se"] else "nicht eingetroffen"


def main():
    ordner, ziel = sys.argv[1], sys.argv[2]
    recs, dateien, doppelt = laden(ordner)
    out = {"dateien": dateien, "doppelt_ignoriert": doppelt, "konstanten": {
        "C_T": C_T, "SE_C_T": SE_C_T, "INT_R": INT_R, "S_FAKTOR": S_FAKTOR, "FAKTOR_PLAN": FAKTOR_PLAN,
        "ZIEL_PLAN": list(ZIEL_PLAN), "ZIEL_KARTE": list(ZIEL_KARTE), "H_KONT": H_KONT,
        "GAMMA_KONT": {str(k): v for k, v in GAMMA_KONT.items()}, "MIN_SAATEN": MIN_SAATEN,
        "MAX_AUSFALL": MAX_AUSFALL}, "dim": {}}
    ergebnisse = {}
    for n in sorted({k[0] for k in recs}):
        Ns = sorted({k[1] for k in recs if k[0] == n})
        saaten = sorted({k[2] for k in recs if k[0] == n})
        gut, aus, unvollst = [], [], []
        gruende = {}
        for s in saaten:
            vorhanden = [(n, N, s) in recs for N in Ns]
            gueltig = [recs[(n, N, s)]["gueltig"] for N in Ns if (n, N, s) in recs]
            if not all(gueltig):
                aus.append(s)
                gruende[str(s)] = [{"N": N, "kugel": recs[(n, N, s)]["kugel"]["gueltig"],
                                    "torus": recs[(n, N, s)]["torus"]["gueltig"], "lu_ok": recs[(n, N, s)]["lu_ok"]}
                                   for N in Ns if (n, N, s) in recs and not recs[(n, N, s)]["gueltig"]]
            elif not all(vorhanden):
                unvollst.append(s)
            else:
                gut.append(s)
        M = len(gut)
        ausfall = len(aus) / max(1, len(aus) + M)
        tor = bool(M >= MIN_SAATEN and ausfall <= MAX_AUSFALL)
        dout = {"Nlist": Ns, "saaten_gut": gut, "saaten_ausgeschlossen": aus, "gruende": gruende,
                "saaten_unvollstaendig": unvollst, "M": M, "ausfall_anteil": ausfall, "tor_bestanden": tor,
                "fits": {}}
        if M >= 2:
            for r in REGELN:
                for q in GROESSEN:
                    for v in FASSUNGEN:
                        Y = np.array([[y_wert(recs[(n, N, s)], r, q, v) for N in Ns] for s in gut])
                        fo, bj = fits(Ns, Y)
                        g = GAMMA_KONT[n]
                        fo["beta_mit_gamma_kont"] = fo["beta"]["mittel"] - g * fo["gamma_empfindlichkeit_b0"]
                        fo["beta_bias_je_gamma_1"] = fo["gamma_empfindlichkeit_b0"]
                        dout["fits"][f"{r}/{q}/{v}"] = fo
                        ergebnisse[(n, r, q, v)] = (fo, bj)
            # KU4-Differenzen je Saat (gepaart, gleiche Netze)
            dout["massdifferenz"] = {}
            for r in REGELN:
                for v in FASSUNGEN:
                    d = ergebnisse[(n, r, "gamma", v)][1] - ergebnisse[(n, r, "gamma_M", v)][1]
                    dout["massdifferenz"][f"{r}/{v}"] = stat(d)
            dout["regeldifferenz_S_minus_C"] = {
                f"{q}/{v}": stat(ergebnisse[(n, "S", q, v)][1] - ergebnisse[(n, "C", q, v)][1])
                for q in GROESSEN for v in FASSUNGEN}
        # beschreibend je N: Geometrie, Volumen, Regge, Laufzeit, Netzgroessen
        besch = []
        for N in Ns:
            rs = [recs[(n, N, s)] for s in gut if (n, N, s) in recs]
            if not rs:
                continue

            def mstd(vals):
                a = np.asarray(vals, dtype=float)
                return {"mittel": float(a.mean()), "std": float(a.std(ddof=1)) if a.size > 1 else None,
                        "min": float(a.min()), "max": float(a.max())}
            e = {"N": N, "anzahl": len(rs), "a": rs[0]["kugel"]["geo"]["a"],
                 "V_C/V_K": mstd([x["kugel"]["regeln"]["C"]["V"] / x["kugel"]["geo"]["V_K"] for x in rs]),
                 "V_S/V_K": mstd([x["kugel"]["regeln"]["S"]["V"] / x["kugel"]["geo"]["V_K"] for x in rs]),
                 "V_Q/V_K": mstd([x["kugel"]["geo"]["V_Q_quadratur"] / x["kugel"]["geo"]["V_K"] for x in rs]),
                 "korr_C_je_wurzelN": mstd([x["kugel"]["regeln"]["C"]["korr"] / math.sqrt(N) for x in rs]),
                 "korr_S_je_wurzelN": mstd([x["kugel"]["regeln"]["S"]["korr"] / math.sqrt(N) for x in rs]),
                 "korrM_C_je_wurzelN": mstd([x["kugel"]["regeln"]["C"]["korr_M"] / math.sqrt(N) for x in rs]),
                 "korrM_S_je_wurzelN": mstd([x["kugel"]["regeln"]["S"]["korr_M"] / math.sqrt(N) for x in rs]),
                 "torus_log_V_VR": mstd([x["torus"]["log_VK_VR"] for x in rs]),
                 "regge_rel": mstd([x["kugel"]["pruefung"]["regge_rel"] for x in rs]),
                 "F_je_N_kugel": mstd([x["kugel"]["pruefung"]["F_je_N"] for x in rs]),
                 "euler": sorted({x["kugel"]["pruefung"]["euler"] for x in rs}),
                 "kappen_mit_punkt_innen_max": max(x["kugel"]["pruefung"]["kappen_mit_punkt_innen"] for x in rs),
                 "normale_min_cos": min(x["kugel"]["pruefung"]["normale_gegen_qhull_min_cos"] for x in rs),
                 "vol_min": min(x["kugel"]["pruefung"]["vol_min"] for x in rs),
                 "sigma_mittel": mstd([x["kugel"]["pruefung"]["sigma_mittel"] for x in rs]),
                 "gamma_kugel_C_je_N": mstd([x["kugel"]["regeln"]["C"]["gamma"] / N for x in rs]),
                 "gamma_torus_je_N": mstd([x["torus"]["gamma"] / N for x in rs]),
                 "std_gamma_kugel_C_je_wurzelN": float(np.std([x["kugel"]["regeln"]["C"]["gamma"] for x in rs],
                                                              ddof=1) / math.sqrt(N)) if len(rs) > 1 else None,
                 "std_gamma_torus_je_wurzelN": float(np.std([x["torus"]["gamma"] for x in rs], ddof=1)
                                                     / math.sqrt(N)) if len(rs) > 1 else None,
                 "sekunden": mstd([x["sekunden"] for x in rs]), "rss_mb_max": max(x["rss_mb"] for x in rs),
                 "lu_min_U": min(min(x["kugel"]["regeln"][r]["lu"]["min_U"] for r in REGELN)
                                 for x in rs),
                 "zeilensumme_rel_max": max(max(x["kugel"]["regeln"][r]["zeilensumme_rel"] for r in REGELN)
                                            for x in rs)}
            if n == 2:
                e["gauss_bonnet_abw_max"] = max(abs(x["kugel"]["pruefung"]["gauss_bonnet_abw"]) for x in rs)
            besch.append(e)
        dout["beschreibend_je_N"] = besch
        out["dim"][str(n)] = dout

    # ------------------------------------------------------------------ Urteile
    U = {}
    d2 = out["dim"].get("2")
    d4_ = out["dim"].get("4")
    ku0_plan = None
    if d2 and d2["M"] >= 2:
        b = d2["fits"]["C/gamma/korr"]["beta"]
        plan, karte = urteil_ku0(b)
        if not d2["tor_bestanden"]:
            plan = "nicht auswertbar (Tor)"
        ku0_plan = plan
        U["KU0"] = {"plan": plan, "karte": karte, "beta_2D": b["mittel"], "se": b["se"], "M": b["M"],
                    "abs_beta_durch_se": abs(b["mittel"]) / b["se"],
                    "mitberichtet": {k: d2["fits"][k]["beta"] for k in ("C/gamma/roh", "C/gamma_M/korr",
                                                                         "S/gamma_M/korr", "C/gamma_M/roh")}}
    if d4_ and d4_["M"] >= 2:
        fz = d4_["fits"]
        vorbehalt = []
        if not d4_["tor_bestanden"]:
            vorbehalt.append("Tor 4D nicht bestanden: Urteile nicht auswertbar")
        if ku0_plan != "eingetroffen":
            vorbehalt.append(f"KU0 (Plan) = {ku0_plan}: keine 4D-Lesart (Kartenregel)")
        bS = fz["S/gamma/korr"]["beta"]
        bC = fz["C/gamma/korr"]["beta"]
        plan1, karte1, zweig = urteil_ku1(bS)
        U["KU1"] = {"plan": plan1, "karte": karte1, "beta_S": bS["mittel"], "se": bS["se"], "t": bS["t"], "M": bS["M"],
                    "zweig_verfehlt_durch_beta_negativ_3SE": zweig,
                    "roh": dict(zip(("plan", "karte", "zweig"), urteil_ku1(fz["S/gamma/roh"]["beta"]))) | {
                        "beta": fz["S/gamma/roh"]["beta"]["mittel"], "se": fz["S/gamma/roh"]["beta"]["se"]},
                    "regel_C": dict(zip(("plan", "karte", "zweig"), urteil_ku1(bC))),
                    "abstand_H_kont_in_se": (bS["mittel"] - H_KONT) / bS["se"]}
        k2p, k2pd = urteil_ku2(bS, ZIEL_PLAN)
        k2k, k2kd = urteil_ku2(bS, ZIEL_KARTE)
        U["KU2"] = {"plan": k2p, "karte": k2k, "plan_details": k2pd, "karte_details": k2kd,
                    "roh_plan": urteil_ku2(fz["S/gamma/roh"]["beta"], ZIEL_PLAN)[0]}
        p3, k3 = urteil_ku3(bC, bS)
        U["KU3"] = {"plan": p3, "karte": k3, "beta_C": bC["mittel"], "se_C": bC["se"], "beta_S": bS["mittel"],
                    "se_S": bS["se"], "roh": dict(zip(("plan", "karte"), urteil_ku3(fz["C/gamma/roh"]["beta"],
                                                                                     fz["S/gamma/roh"]["beta"]))),
                    "differenz_S_minus_C": d4_["regeldifferenz_S_minus_C"]["gamma/korr"]}
        dS = d4_["massdifferenz"]["S/korr"]
        dC = d4_["massdifferenz"]["C/korr"]
        bMS = fz["S/gamma_M/korr"]["beta"]
        U["KU4"] = {"plan": urteil_ku4(dS), "karte": urteil_ku4(dS), "differenz_beta_Gamma_minus_Gamma_M_S": dS,
                    "beta_M_S": bMS, "vorzeichen_gleich_S": bool(np.sign(bMS["mittel"]) == np.sign(bS["mittel"])),
                    "regel_C": {"urteil": urteil_ku4(dC), "differenz": dC, "beta_M_C": fz["C/gamma_M/korr"]["beta"]},
                    "roh_S": urteil_ku4(d4_["massdifferenz"]["S/roh"])}
        if vorbehalt:
            for k in ("KU1", "KU2", "KU3", "KU4"):
                U[k]["vorbehalt"] = vorbehalt
                if not d4_["tor_bestanden"]:
                    U[k]["plan"] = "nicht auswertbar (Tor)"
    out["urteile"] = U
    with open(ziel + ".tmp", "w") as fh:
        json.dump(out, fh, indent=1)
    os.replace(ziel + ".tmp", ziel)
    print("geschrieben", ziel, flush=True)


if __name__ == "__main__":
    main()
