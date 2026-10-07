#!/usr/bin/env python3
"""INDUZIERT-DICHTE-2D-GROB (Runde 38, Code-Agent): Auswertung nach PLAN.md (Urteile IG0 bis IG3), Tabellen, Bilder.

Einheiten: Netzabstand eps = sqrt(A/N) (A = Torusflaeche bei s = 0). Je Datensatz y_eps = Gamma''/N = y_koord A/N und
x = (k eps)^2. Modell (Karte): y_eps = a + c x + d x^2 gemeinsam ueber beide Dichten; c ist der Grenzwert k -> 0.

Aufruf (nur ueber kleintest.sh):
  python grob_auswertung.py auswerten <haupt_lauf_ordner> <grob_lauf_ordner> <aus.json>
      haupt_lauf_ordner: INDUZIERT-DICHTE-2D (dichte-N64000-*.json, dichte-N16000-*.json), nur gelesen
      grob_lauf_ordner:  a-*.json (Lauf a: N = 16 000, A = 64 000), b-*.json (Kontrolle b: N = 16 000, A = N)
  python grob_auswertung.py vergleich <haupt_lauf_ordner> <datei.json> <aus.json>
      Saat fuer Saat gegen den Hauptlauf N = 16 000 (gleiche Saat, gleiches n): Gamma bitgleich?
  python grob_auswertung.py selbsttest <aus.json>
      synthetische Daten mit bekanntem a, c, d (keine Messdaten)
"""
import glob
import json
import math
import os
import sys

import numpy as np
from scipy import stats

POLYAKOV = -1.0 / (24.0 * math.pi)
S_U = 0.5
ACHSEN = ("r000", "r090")
NL_64, NL_16, NL_G = (2, 4, 8, 12), (1, 2, 4, 6), (2, 4, 8, 12)
IG0_NSE = 2.0                  # Karte: innerhalb 2 SE des Hauptlaufs
IG1_SE_MAX = 0.01              # Karte: d auf <= +-0,01 (1 SE)
IG2_BAND = (1.2, 0.7)          # Karte: zwischen 0,7 P und 1,2 P
IG3_BAND = (1.15, 0.85)        # Karte: innerhalb 15 % von P
NSE_NEIN = 2.0                 # nicht eingetroffen: Abstand zum Band > 2 SE
P_LOF = 0.01                   # Modellprobe: p(chi^2) < 0,01 -> IG1 bis IG3 nicht auswertbar
MIN_SAATEN_G = 32
TOR_NEWTON = 1e-12
FENSTER_KLEIN = 0.40           # beschreibend: Fenster k eps <= 0,40


# ---------------------------------------------------------------------- Einlesen und Tor (wie eingefroren)
def lade(ordner, muster):
    saaten, kopf, dateien = {}, None, []
    for p in sorted(glob.glob(os.path.join(ordner, muster))):
        with open(p) as f:
            d = json.load(f)
        if kopf is None:
            kopf = {"N": int(d["N"]), "A": float(d.get("A", float(d["N"]))), "S": d["S"], "nlist": d["nlist"]}
        elif int(d["N"]) != kopf["N"] or float(d.get("A", float(d["N"]))) != kopf["A"]:
            raise SystemExit(f"{p}: N oder A passt nicht")
        dateien.append(os.path.basename(p))
        for s in d["saaten"]:
            if s["saat"] in saaten:
                raise SystemExit(f"Saat {s['saat']} doppelt ({p})")
            saaten[s["saat"]] = s
    return {"saaten": saaten, "kopf": kopf, "dateien": dateien}


def gueltig(p):
    return (p["euler"] == 0 and p["kanten_genau_zwei"] and p["orient_min"] > 0 and p["koord_flaeche_rel_abw"] <= 1e-9
            and p["E"] == 3 * p["V"] and p["F"] == 2 * p["V"] and p["phys_flaeche_min"] > 0
            and p["l_max_durch_L"] < 0.25)


def lu_ok(info):
    return info["neg_U"] == 0 and info["perm_ungleich"] == 0 and info["min_U"] > 0


def tor(d):
    fehler, anzahl, neg, neu = [], 0, [], []
    for saat, s in d["saaten"].items():
        if not (gueltig(s["pruefung0"]) and s["pruefung0_z2"]["delaunay_verletzt_1e-9"] == 0 and lu_ok(s["lu0"])):
            fehler.append(f"s{saat}/basis")
        for p in s["punkte"]:
            for e in p["je_S"]:
                for seite in ("plus", "minus"):
                    x = e[seite]
                    anzahl += 1
                    if not (gueltig(x["koord_pruefung"]) and lu_ok(x["lu"]["koord"])
                            and x["psi"]["residuum"] <= TOR_NEWTON):
                        fehler.append(f"s{saat}/{p['richtung']}/n{p['n']}/S{e['S']}/{seite}")
                    neg.append(x["koord_pruefung"]["w_negativ"] / x["koord_pruefung"]["E"])
                    neu.append(x["koord_neue_kanten"] / x["koord_pruefung"]["E"])
    return {"netze": anzahl, "fehler_anzahl": len(fehler), "fehler": fehler[:30], "bestanden": len(fehler) == 0,
            "anteil_negativ_mittel": float(np.mean(neg)) if neg else None,
            "anteil_negativ_max": float(np.max(neg)) if neg else None,
            "anteil_neue_kanten_mittel": float(np.mean(neu)) if neu else None}


def tabelle(d, nliste, S=S_U):
    """Je Saat: y_koord(n) gemittelt ueber 0 und 90 Grad; dazu |k| in Koordinaten."""
    saaten = sorted(d["saaten"])
    Y = np.full((len(saaten), len(nliste)), np.nan)
    kb = np.full(len(nliste), np.nan)
    for i, saat in enumerate(saaten):
        for j, n in enumerate(nliste):
            w = []
            for p in d["saaten"][saat]["punkte"]:
                if p["n"] != n or p["richtung"] not in ACHSEN:
                    continue
                for e in p["je_S"]:
                    if abs(e["S"] - S) < 1e-12:
                        w.append(e["y_koord"])
                        kb[j] = p["betrag"]
            if len(w) == len(ACHSEN):
                Y[i, j] = float(np.mean(w))
    ok = ~np.any(np.isnan(Y), axis=1)
    return np.array(saaten)[ok], Y[ok], kb


def mittel_se(v):
    v = np.asarray(v, float)
    return float(np.mean(v)), float(np.std(v, ddof=1) / math.sqrt(v.size)), int(v.size)


def fit_je_saat(Y, x, grad=1):
    X = np.stack([x ** p for p in range(grad + 1)], axis=1)
    koef, *_ = np.linalg.lstsq(X, Y.T, rcond=None)
    return koef.T


# ---------------------------------------------------------------------- gemeinsamer Ausgleich (GLS auf Zellmitteln)
def zellen(saetze, fenster=None, cov_art="frei"):
    """saetze: Liste (name, Y_eps (M x n), x (n)). Zellmittel und blockdiagonale Kovarianz der Mittel."""
    ys, xs, ns, bl = [], [], [], []
    for name, Y, x in saetze:
        keep = np.ones(x.size, bool) if fenster is None else (np.sqrt(x) <= fenster + 1e-12)
        Yk = Y[:, keep]
        M, n = Yk.shape
        if cov_art == "frei":
            Sig = np.atleast_2d(np.cov(Yk, rowvar=False, ddof=1))
        else:                                   # Versatz-Modell: sigma^2 I + tau^2 J (Varianzanalyse)
            sig2, tau2 = varianzanteile(Yk)
            Sig = sig2 * np.eye(n) + tau2 * np.ones((n, n))
        ys.append(Yk.mean(axis=0))
        xs.append(x[keep])
        ns += [name] * n
        bl.append(Sig / M)
    C = np.zeros((len(ns), len(ns)))
    i = 0
    for b in bl:
        C[i:i + b.shape[0], i:i + b.shape[0]] = b
        i += b.shape[0]
    return np.concatenate(ys), np.concatenate(xs), np.array(ns), C


def varianzanteile(Y):
    M, n = Y.shape
    r = Y - Y.mean(axis=0)
    rb = r.mean(axis=1)
    sig2 = float(np.sum((r - rb[:, None]) ** 2) / ((M - 1) * (n - 1)))
    tau2 = max(0.0, float((n * np.sum(rb ** 2) / (M - 1) - sig2) / n))
    return sig2, tau2


def design(x, ns, modell):
    if modell == "quad":
        return np.stack([np.ones_like(x), x, x ** 2], axis=1), ["a", "c", "d"]
    if modell == "kub":
        return np.stack([np.ones_like(x), x, x ** 2, x ** 3], axis=1), ["a", "c", "d", "f"]
    if modell == "a_je_satz":
        namen = sorted(set(ns.tolist()))
        cols = [(ns == nm).astype(float) for nm in namen]
        return np.stack(cols + [x, x ** 2], axis=1), [f"a_{nm}" for nm in namen] + ["c", "d"]
    if modell == "lin":
        return np.stack([np.ones_like(x), x], axis=1), ["a", "c"]
    raise ValueError(modell)


def gls(y, X, C):
    Lc = np.linalg.cholesky(C)
    Xw = np.linalg.solve(Lc, X)
    yw = np.linalg.solve(Lc, y)
    th, *_ = np.linalg.lstsq(Xw, yw, rcond=None)
    F = Xw.T @ Xw
    cov = np.linalg.inv(F)
    r = yw - Xw @ th
    chi2 = float(r @ r)
    dof = y.size - X.shape[1]
    p = float(stats.chi2.sf(chi2, dof)) if dof > 0 else float("nan")
    birge = max(1.0, math.sqrt(chi2 / dof)) if dof > 0 else 1.0
    return th, cov, chi2, dof, p, birge


def ausgleich(saetze, modell="quad", fenster=None, cov_art="frei"):
    y, x, ns, C = zellen(saetze, fenster, cov_art)
    X, namen = design(x, ns, modell)
    th, cov, chi2, dof, p, birge = gls(y, X, C)
    se = np.sqrt(np.diag(cov))
    out = {"modell": modell, "fenster_k_eps_max": fenster, "kovarianz": cov_art, "zellen": int(y.size),
           "chi2": chi2, "dof": dof, "p": p, "birge": birge}
    for i, nm in enumerate(namen):
        out[nm] = {"wert": float(th[i]), "se_gls": float(se[i]), "se_u": float(se[i] * birge)}
    if "c" in namen and "d" in namen:
        ic, idd = namen.index("c"), namen.index("d")
        out["korr_c_d"] = float(cov[ic, idd] / (se[ic] * se[idd]))
    out["_th"], out["_cov"], out["_y"], out["_x"], out["_ns"], out["_C"] = th, cov, y, x, ns, C
    return out


def oeffentlich(r):
    return {k: v for k, v in r.items() if not k.startswith("_")}


def jackknife(saetze, modell="quad"):
    """Geschichtetes Delete-one-Jackknife ueber Saaten (Kovarianz je Durchgang neu geschaetzt)."""
    var = None
    for k, (name, Y, x) in enumerate(saetze):
        M = Y.shape[0]
        th = []
        for i in range(M):
            s2 = list(saetze)
            s2[k] = (name, np.delete(Y, i, axis=0), x)
            th.append(ausgleich(s2, modell)["_th"])
        th = np.array(th)
        v = (M - 1) / M * np.sum((th - th.mean(axis=0)) ** 2, axis=0)
        var = v if var is None else var + v
    return np.sqrt(var)


def feste_versaetze(saetze):
    """Je Saat eigener Achsenabschnitt, gemeinsame c und d; Gewicht 1/sigma_D^2 (Varianzanalyse je Datensatz)."""
    F = np.zeros((2, 2))
    b = np.zeros(2)
    for name, Y, x in saetze:
        sig2, _ = varianzanteile(Y)
        Z = np.stack([x - x.mean(), x ** 2 - (x ** 2).mean()], axis=1)
        Yc = Y - Y.mean(axis=1, keepdims=True)
        F += Y.shape[0] * Z.T @ Z / sig2
        b += Z.T @ Yc.sum(axis=0) / sig2
    cov = np.linalg.inv(F)
    th = cov @ b
    return {"c": float(th[0]), "d": float(th[1]), "se_c": float(math.sqrt(cov[0, 0])),
            "se_d": float(math.sqrt(cov[1, 1]))}


# ---------------------------------------------------------------------- Urteilsregeln
def band_urteil(c, se, faktoren, tol_se):
    lo, hi = faktoren[0] * POLYAKOV, faktoren[1] * POLYAKOV          # P < 0: lo < hi
    drin = lo <= c <= hi
    abstand = 0.0 if drin else min(abs(c - lo), abs(c - hi))
    if drin and se <= tol_se:
        u = "eingetroffen"
    elif (not drin) and abstand > NSE_NEIN * se:
        u = "nicht eingetroffen"
    else:
        u = "nicht auswertbar"
    return u, {"band": [lo, hi], "im_band": bool(drin), "abstand_zum_band": abstand,
               "abstand_in_se": abstand / se if se > 0 else None, "se_schwelle": tol_se,
               "kartenwortlaut": "eingetroffen" if drin else "nicht eingetroffen"}


# ---------------------------------------------------------------------- Vergleich mit dem Hauptlauf (bitgleich?)
def vergleich_saaten(d, ref, S=S_U):
    """Gleiche Saat, Richtung, n und S: Gamma(0), Gamma(+-S), D und y in Netzabstands-Einheiten."""
    fa = d["kopf"]["A"] / d["kopf"]["N"]
    fr = ref["kopf"]["A"] / ref["kopf"]["N"]
    zeilen, gleich, max_abs = 0, 0, {"gamma0": 0.0, "gamma_pm": 0.0, "D": 0.0, "y_eps": 0.0}
    for saat, s in d["saaten"].items():
        if saat not in ref["saaten"]:
            continue
        r = ref["saaten"][saat]
        max_abs["gamma0"] = max(max_abs["gamma0"], abs(s["gamma0"] - r["gamma0"]))
        for p in s["punkte"]:
            q = [u for u in r["punkte"] if u["n"] == p["n"] and u["richtung"] == p["richtung"]]
            if not q:
                continue
            for e in p["je_S"]:
                f = [u for u in q[0]["je_S"] if abs(u["S"] - e["S"]) < 1e-12]
                if abs(e["S"] - S) > 1e-12 or not f:
                    continue
                f = f[0]
                zeilen += 1
                dg = max(abs(e["plus"]["gamma_koord"] - f["plus"]["gamma_koord"]),
                         abs(e["minus"]["gamma_koord"] - f["minus"]["gamma_koord"]))
                dD = abs(e["D_koord"] - f["D_koord"])
                dy = abs(e["y_koord"] * fa - f["y_koord"] * fr)
                max_abs["gamma_pm"] = max(max_abs["gamma_pm"], dg)
                max_abs["D"] = max(max_abs["D"], dD)
                max_abs["y_eps"] = max(max_abs["y_eps"], dy)
                gleich += int(dg == 0 and dD == 0 and dy == 0 and s["gamma0"] == r["gamma0"])
    return {"zeilen": zeilen, "bitgleich": gleich, "max_abs_abw": max_abs,
            "alle_bitgleich": bool(zeilen > 0 and gleich == zeilen)}


# ---------------------------------------------------------------------- Hauptauswertung
def auswerten(haupt, grob, ziel):
    na = "nicht auswertbar"
    m64 = lade(haupt, "dichte-N64000-*.json")
    m16 = lade(haupt, "dichte-N16000-*.json")
    ga = lade(grob, "a-*.json")
    gb = lade(grob, "b-*.json")
    erg = {"polyakov": POLYAKOV, "urteile": {}, "dateien": {"M64": m64["dateien"], "M16": m16["dateien"],
                                                            "G": ga["dateien"], "B": gb["dateien"]}}
    erg["tor"] = {"G": tor(ga) if ga["saaten"] else None, "B": tor(gb) if gb["saaten"] else None}

    # ---- Datensaetze in Netzabstands-Einheiten
    saetze, info = [], {}
    for name, d, nl in (("M64", m64, NL_64), ("M16", m16, NL_16), ("G", ga, NL_G)):
        if not d["saaten"]:
            continue
        sa, Y, kb = tabelle(d, nl)
        eps = math.sqrt(d["kopf"]["A"] / d["kopf"]["N"])
        Ye = Y * (d["kopf"]["A"] / d["kopf"]["N"])
        x = (kb * eps) ** 2
        saetze.append((name, Ye, x))
        sig2, tau2 = varianzanteile(Ye)
        Sig = np.atleast_2d(np.cov(Ye, rowvar=False, ddof=1))
        info[name] = {"N": d["kopf"]["N"], "A": d["kopf"]["A"], "eps": eps, "saaten": int(len(sa)),
                      "saat_min": int(sa.min()), "saat_max": int(sa.max()), "n": list(nl),
                      "k_koord": kb.tolist(), "k_eps": (kb * eps).tolist(), "x": x.tolist(),
                      "y_eps_mittel": Ye.mean(axis=0).tolist(),
                      "y_eps_se": (Ye.std(axis=0, ddof=1) / math.sqrt(Ye.shape[0])).tolist(),
                      "y_eps_std_je_k": Ye.std(axis=0, ddof=1).tolist(),
                      "sigma_rest": math.sqrt(sig2), "tau_versatz": math.sqrt(tau2),
                      "versatz_anteil": tau2 / (tau2 + sig2) if tau2 + sig2 > 0 else None,
                      "kovarianz": Sig.tolist(),
                      "korrelation": (Sig / np.sqrt(np.outer(np.diag(Sig), np.diag(Sig)))).tolist()}
        # eingefrorene Fit-Regel je Saat (a + c k^2 ueber die vier k, Koordinaten) und quadratisch je Saat
        ac = fit_je_saat(Ye, x, 1)
        acd = fit_je_saat(Ye, x, 2)
        info[name]["fenster_steigung_c"] = mittel_se(ac[:, 1])
        info[name]["fenster_a_eps"] = mittel_se(ac[:, 0])
        info[name]["quad_je_saat"] = {"a": mittel_se(acd[:, 0]), "c": mittel_se(acd[:, 1]), "d": mittel_se(acd[:, 2])}
    erg["datensaetze"] = info

    # ---- IG0: Kontrolle (b) gegen den Hauptlauf N = 16 000 (eingefrorene Fit-Regel, S = 0,5)
    c16 = info.get("M16", {}).get("fenster_steigung_c")
    if gb["saaten"] and c16:
        sa_b, Yb, kbb = tabelle(gb, NL_16)
        cb = mittel_se(fit_je_saat(Yb, kbb ** 2, 1)[:, 1])
        diff = abs(cb[0] - c16[0])
        tor_b = erg["tor"]["B"]["bestanden"]
        u0 = ("eingetroffen" if diff <= IG0_NSE * c16[1] else "nicht eingetroffen") if tor_b else na
        erg["urteile"]["IG0"] = {"urteil": u0, "werte": {
            "c_b": cb[0], "se_b": cb[1], "saaten_b": cb[2], "c_hauptlauf": c16[0], "se_hauptlauf": c16[1],
            "saaten_hauptlauf": c16[2], "abstand": diff, "abstand_in_se_hauptlauf": diff / c16[1],
            "tor_b": tor_b, "bitvergleich": vergleich_saaten(gb, m16), "karte": {"c": -0.0131, "se": 0.0022}}}
    else:
        erg["urteile"]["IG0"] = {"urteil": na, "werte": {"grund": "Kontrolle (b) fehlt"}}

    # ---- gemeinsamer Ausgleich (Urteil): a + c x + d x^2, freie Kovarianz je Datensatz, alle k
    namen = [s[0] for s in saetze]
    if not all(nm in namen for nm in ("M64", "M16", "G")):
        for nr in ("IG1", "IG2", "IG3"):
            erg["urteile"][nr] = {"urteil": na, "werte": {"grund": "Datensatz fehlt", "da": namen}}
    else:
        h = ausgleich(saetze, "quad")
        erg["ausgleich"] = oeffentlich(h)
        c, d = h["c"]["wert"], h["d"]["wert"]
        se_c, se_d = h["c"]["se_u"], h["d"]["se_u"]
        tor_ok = bool(erg["tor"]["G"]["bestanden"] and erg["urteile"]["IG0"]["urteil"] == "eingetroffen"
                      and info["G"]["saaten"] >= MIN_SAATEN_G)
        modell_ok = h["p"] >= P_LOF
        erg["vorbedingungen"] = {"tor_G": erg["tor"]["G"]["bestanden"], "IG0": erg["urteile"]["IG0"]["urteil"],
                                 "saaten_G": info["G"]["saaten"], "modellprobe_p": h["p"], "modell_ok": modell_ok}
        if not tor_ok or not modell_ok:
            grund = "Tor" if not tor_ok else f"Modellprobe p = {h['p']:.4f} < {P_LOF}"
            for nr in ("IG1", "IG2", "IG3"):
                erg["urteile"][nr] = {"urteil": na, "vermerk": grund, "werte": {"c": c, "se_c": se_c, "d": d,
                                                                                 "se_d": se_d}}
        else:
            erg["urteile"]["IG1"] = {"urteil": "eingetroffen" if se_d <= IG1_SE_MAX else "nicht eingetroffen",
                                     "werte": {"d": d, "se_d_u": se_d, "se_d_gls": h["d"]["se_gls"],
                                               "schwelle": IG1_SE_MAX, "birge": h["birge"],
                                               "kartenwortlaut_ohne_birge": "eingetroffen" if h["d"]["se_gls"]
                                               <= IG1_SE_MAX else "nicht eingetroffen"}}
            u2, w2 = band_urteil(c, se_c, IG2_BAND, 0.25 * abs(POLYAKOV))
            erg["urteile"]["IG2"] = {"urteil": u2, "werte": {"c": c, "se_c_u": se_c, "c_durch_P": c / POLYAKOV,
                                                             **w2}}
            u3, w3 = band_urteil(c, se_c, IG3_BAND, 0.15 * abs(POLYAKOV))
            erg["urteile"]["IG3"] = {"urteil": u3, "werte": {"c": c, "se_c_u": se_c, "c_durch_P": c / POLYAKOV,
                                                             "rel_abw": abs(c / POLYAKOV - 1), **w3}}

        # ---- beschreibend
        b = {}
        b["ohne_M64"] = oeffentlich(ausgleich([s for s in saetze if s[0] != "M64"], "quad"))
        b["fenster_k_eps_0.40"] = oeffentlich(ausgleich(saetze, "quad", FENSTER_KLEIN))
        b["mit_k6"] = oeffentlich(ausgleich(saetze, "kub"))
        b["a_je_datensatz"] = oeffentlich(ausgleich(saetze, "a_je_satz"))
        b["versatzmodell_kovarianz"] = oeffentlich(ausgleich(saetze, "quad", cov_art="versatz"))
        b["nur_k2_alle_k"] = oeffentlich(ausgleich(saetze, "lin"))
        b["nur_k2_fenster_0.40"] = oeffentlich(ausgleich(saetze, "lin", FENSTER_KLEIN))
        b["feste_saatversaetze"] = feste_versaetze(saetze)
        jk = jackknife(saetze, "quad")
        b["jackknife_se"] = {"a": float(jk[0]), "c": float(jk[1]), "d": float(jk[2]),
                             "verhaeltnis_zu_gls_c": float(jk[1] / h["c"]["se_gls"]),
                             "verhaeltnis_zu_gls_d": float(jk[2] / h["d"]["se_gls"])}
        # Fenster-Steigungen: gleiche k in Torus-Einheiten, Netzabstand 1 (M64) gegen 2 (G)
        xg = np.array(info["G"]["x"])
        w = (xg - xg.mean()) / np.sum((xg - xg.mean()) ** 2)
        x64 = np.array(info["M64"]["x"])
        w64 = (x64 - x64.mean()) / np.sum((x64 - x64.mean()) ** 2)
        hebel_g, hebel_64 = float(np.sum(w * xg ** 2)), float(np.sum(w64 * x64 ** 2))
        dc = info["G"]["fenster_steigung_c"][0] - info["M64"]["fenster_steigung_c"][0]
        dse = math.hypot(info["G"]["fenster_steigung_c"][1], info["M64"]["fenster_steigung_c"][1])
        dh = hebel_g - hebel_64
        b["fenster_steigungen"] = {"G": info["G"]["fenster_steigung_c"], "M64": info["M64"]["fenster_steigung_c"],
                                   "M16": info["M16"]["fenster_steigung_c"], "hebel_d_G": hebel_g,
                                   "hebel_d_M64": hebel_64, "differenz_G_minus_M64": dc, "se_differenz": dse,
                                   "d_aus_differenz": dc / dh if abs(dh) > 1e-12 else None,
                                   "se_d_aus_differenz": dse / dh if abs(dh) > 1e-12 else None}
        # gleiche k eps, gleiches N: G (n = 2, 4) gegen M16 (n = 2, 4) (Skalengleichheit, unabhaengige Saaten)
        z = []
        for jg, jm in (((0, 1), (1, 2)) if info["G"]["eps"] == 2.0 else ()):
            mg, sg = info["G"]["y_eps_mittel"][jg], info["G"]["y_eps_se"][jg]
            mm, sm = info["M16"]["y_eps_mittel"][jm], info["M16"]["y_eps_se"][jm]
            z.append({"k_eps": info["G"]["k_eps"][jg], "y_G": mg, "y_M16": mm, "z": (mg - mm) / math.hypot(sg, sm)})
        b["G_gegen_M16_gleiches_k_eps"] = z
        # c(k) je Zelle nach Abzug von a (gemeinsamer Ausgleich)
        a = h["a"]["wert"]
        ck = []
        for nm, Y, x in saetze:
            for j in range(x.size):
                m, s, _ = mittel_se(Y[:, j])
                ck.append({"satz": nm, "k_eps": float(math.sqrt(x[j])), "x": float(x[j]), "c_k": (m - a) / x[j],
                           "se": s / x[j], "modell_c_plus_d_x": c + d * x[j]})
        b["c_je_k"] = ck
        # noetige Saaten in G fuer SE(d) = 0,005 bzw. 0,01 (gemeinsamer Ausgleich, Kovarianz skaliert)
        noetig = {}
        for ziel_se in (0.005, 0.01):
            gefunden = None
            for Mg in list(range(4, 64, 2)) + list(range(64, 5000, 16)):
                s2 = []
                for nm, Y, x in saetze:
                    s2.append((nm, Y, x))
                yy, xx, ns, C = zellen(s2)
                mask = ns == "G"
                C2 = C.copy()
                C2[np.ix_(mask, mask)] *= info["G"]["saaten"] / Mg
                X, _ = design(xx, ns, "quad")
                _, cov, _, _, _, _ = gls(yy, X, C2)
                if math.sqrt(cov[2, 2]) <= ziel_se:
                    gefunden = Mg
                    break
            noetig[f"se_d_{ziel_se}"] = gefunden
        qg = info["G"]["quad_je_saat"]["d"]
        noetig["G_allein_se_d_0.005"] = int(math.ceil(qg[2] * (qg[1] / 0.005) ** 2))
        b["saaten_noetig_G"] = noetig
        erg["beschreibend"] = b
        erg["_bild"] = {"saetze": [(nm, Y.mean(axis=0).tolist(), (Y.std(axis=0, ddof=1) / math.sqrt(Y.shape[0])).tolist(),
                                    x.tolist()) for nm, Y, x in saetze], "a": a, "c": c, "d": d}

    bild = erg.pop("_bild", None)
    with open(ziel, "w") as f:
        json.dump(erg, f, indent=1)
    for k, v in erg["urteile"].items():
        print(k, v["urteil"], v.get("vermerk", ""), flush=True)
    if bild:
        try:
            bilder(bild, erg, os.path.dirname(os.path.abspath(ziel)))
        except Exception as ex:   # Bilder sind beschreibend
            print("Bilder fehlgeschlagen:", repr(ex), flush=True)


def bilder(bild, erg, ordner):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    farbe = {"M64": "tab:green", "M16": "tab:orange", "G": "tab:blue"}
    text = {"M64": "Netzabstand 1, N = 64 000 (Hauptlauf)", "M16": "Netzabstand 1, N = 16 000 (Hauptlauf)",
            "G": "Netzabstand 2, N = 16 000 auf L = sqrt(64 000) (Lauf a)"}
    a, c, d = bild["a"], bild["c"], bild["d"]
    h = erg["ausgleich"]
    fig, axs = plt.subplots(1, 2, figsize=(15, 6))
    xx = np.linspace(0, 0.37, 200)
    for nm, ym, ys, x in bild["saetze"]:
        x, ym, ys = np.array(x), np.array(ym), np.array(ys)
        axs[0].errorbar(x, ym, yerr=ys, fmt="o", color=farbe[nm], capsize=3, ms=5, label=text[nm])
        axs[1].errorbar(x * (1.0 if nm != "M16" else 1.04), (ym - a) / x, yerr=ys / x, fmt="o", color=farbe[nm],
                        capsize=3, ms=5, label=text[nm])
    axs[0].plot(xx, a + c * xx + d * xx ** 2, "-", color="k", lw=1.2,
                label=f"Ausgleich a + c x + d x^2: c = {c:+.5f}, d = {d:+.4f}")
    axs[0].plot(xx, a + POLYAKOV * xx, "-", color="r", lw=1.2, label="a + P x (Polyakov, P = -1/(24 pi))")
    axs[0].axhline(0, color="0.6", lw=0.6)
    axs[0].set_xlabel("x = (k eps)^2   (eps = mittlerer Netzabstand)")
    axs[0].set_ylabel("y = Gamma''/N (Saatmittel +- SE)")
    axs[0].set_title("Gamma'' je Punkt gegen (k eps)^2, beide Dichten", fontsize=10)
    axs[0].legend(fontsize=7)
    axs[1].plot(xx, c + d * xx, "-", color="k", lw=1.2, label="Ausgleich: c(k) = c + d (k eps)^2")
    se_c = h["c"]["se_u"]
    axs[1].fill_between([0, 0.37], c - se_c, c + se_c, color="0.5", alpha=0.2, label=f"c(0) = {c:+.5f} +- {se_c:.5f}")
    axs[1].axhline(POLYAKOV, color="r", lw=1.5, label="Polyakov P = -1/(24 pi)")
    axs[1].axhspan(1.2 * POLYAKOV, 0.7 * POLYAKOV, color="r", alpha=0.08, label="IG2-Band 0,7 P bis 1,2 P")
    axs[1].axhline(0, color="0.6", lw=0.6)
    axs[1].set_ylim(-0.045, 0.02)
    axs[1].set_xlim(0, 0.37)
    axs[1].set_xlabel("x = (k eps)^2")
    axs[1].set_ylabel("c(k) = (y - a)/x   (a aus dem gemeinsamen Ausgleich)")
    axs[1].set_title("konforme Steifigkeit c(k) gegen k^2: Achsenabschnitt = Grenzwert k -> 0, Steigung = d",
                     fontsize=10)
    axs[1].legend(fontsize=7, loc="lower left")
    fig.suptitle("INDUZIERT-DICHTE-2D-GROB: gemeinsamer Ausgleich ueber Netzabstand 1 und 2 "
                 f"(chi^2 = {h['chi2']:.1f} bei {h['dof']} FG, p = {h['p']:.3f})", fontsize=11)
    fig.tight_layout()
    fig.savefig(os.path.join(ordner, "bild-ck-gegen-k2.png"), dpi=110)
    plt.close(fig)
    fig, ax = plt.subplots(figsize=(7.5, 5))
    for nm, Y in ((k, v) for k, v in erg["datensaetze"].items()):
        ax.plot(Y["k_eps"], Y["y_eps_std_je_k"], "o-", color=farbe[nm], label=f"{text[nm]}: Std je Saat")
    ax.set_xlabel("k eps")
    ax.set_ylabel("Standardabweichung von y = Gamma''/N ueber Saaten")
    ax.set_title("Saatstreuung je k (Netzabstands-Einheiten)", fontsize=10)
    ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(os.path.join(ordner, "bild-streuung-grob.png"), dpi=110)
    plt.close(fig)


# ---------------------------------------------------------------------- synthetischer Selbsttest
def selbsttest(ziel, wdh=300):
    rng = np.random.default_rng(20261004)
    x1 = (2 * np.pi * np.array([2, 4, 8, 12]) / math.sqrt(64000)) ** 2
    x16 = (2 * np.pi * np.array([1, 2, 4, 6]) / math.sqrt(16000)) ** 2
    xg = 4 * x1
    wahr = {"a": 3e-4, "c": POLYAKOV, "d": -0.035}
    plan = (("M64", 66, x1, 0.00064, 0.0013), ("M16", 64, x16, 0.0012, 0.0026), ("G", 240, xg, 0.0012, 0.0026))
    th, se, chi2, p = [], [], [], []
    for _ in range(wdh):
        saetze = []
        for nm, M, x, sig, tau in plan:
            Y = (wahr["a"] + wahr["c"] * x + wahr["d"] * x ** 2)[None, :] + tau * rng.standard_normal((M, 1)) \
                + sig * rng.standard_normal((M, x.size))
            saetze.append((nm, Y, x))
        h = ausgleich(saetze, "quad")
        th.append(h["_th"])
        se.append([h["a"]["se_gls"], h["c"]["se_gls"], h["d"]["se_gls"]])
        chi2.append(h["chi2"])
        p.append(h["p"])
    th, se = np.array(th), np.array(se)
    w = np.array([wahr["a"], wahr["c"], wahr["d"]])
    zug = (th - w) / se
    out = {"wiederholungen": wdh, "wahr": wahr, "mittel": th.mean(axis=0).tolist(),
           "bias_in_se_des_mittels": ((th.mean(axis=0) - w) / (th.std(axis=0, ddof=1) / math.sqrt(wdh))).tolist(),
           "std_schaetzer": th.std(axis=0, ddof=1).tolist(), "se_gls_mittel": se.mean(axis=0).tolist(),
           "zug_std": zug.std(axis=0, ddof=1).tolist(), "chi2_mittel": float(np.mean(chi2)),
           "dof": 9, "anteil_p_unter_0.01": float(np.mean(np.array(p) < 0.01))}
    # Probe: ein k^6-Glied muss die Modellprobe ausloesen
    saetze = []
    for nm, M, x, sig, tau in plan:
        Y = (wahr["a"] + wahr["c"] * x + wahr["d"] * x ** 2 + 0.5 * x ** 3)[None, :] \
            + tau * rng.standard_normal((M, 1)) + sig * rng.standard_normal((M, x.size))
        saetze.append((nm, Y, x))
    h = ausgleich(saetze, "quad")
    out["probe_k6_f0.5"] = {"p": h["p"], "c": h["c"]["wert"], "d": h["d"]["wert"]}
    with open(ziel, "w") as f:
        json.dump(out, f, indent=1)
    print(json.dumps(out, indent=1), flush=True)


def main():
    modus = sys.argv[1]
    if modus == "auswerten":
        auswerten(sys.argv[2], sys.argv[3], sys.argv[4])
    elif modus == "vergleich":
        ref = lade(sys.argv[2], "dichte-N16000-*.json")
        d = lade(os.path.dirname(os.path.abspath(sys.argv[3])), os.path.basename(sys.argv[3]))
        out = vergleich_saaten(d, ref)
        out["datei"] = sys.argv[3]
        out["kopf"] = d["kopf"]
        out["tor"] = tor(d)
        with open(sys.argv[4], "w") as f:
            json.dump(out, f, indent=1)
        print(json.dumps({k: v for k, v in out.items() if k != "tor"}, indent=1), "tor", out["tor"]["bestanden"],
              flush=True)
    elif modus == "selbsttest":
        selbsttest(sys.argv[2])
    else:
        raise SystemExit("unbekannter Modus")


if __name__ == "__main__":
    main()
