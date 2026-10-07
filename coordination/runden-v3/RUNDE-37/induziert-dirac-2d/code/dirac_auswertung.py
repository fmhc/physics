#!/usr/bin/env python3
"""INDUZIERT-DIRAC-2D (Runde 39, Code-Agent): Auswertung nach PLAN.md (Urteile ID-F0 bis ID-F3), Tabellen, Bilder.

Einheiten wie -GROB: eps = sqrt(A/N); je Datensatz y_eps = y A/N, x = (k eps)^2; Modell y_eps = a + c x + d x^2
gemeinsam ueber beide Netzabstaende (GLS auf Zellmitteln, freie Kovarianz je Datensatz, grob_auswertung.py
unveraendert). c_eff = c/P mit P = -1/(24 pi) (Fermion-Konvention: Gamma_F = -log|det' D_F|).

Aufruf (nur ueber kleintest.sh):
  python dirac_auswertung.py auswerten <lauf_ordner> <aus.json> [<M16-Ordner> <G-Ordner>]
      lauf_ordner: e1-*.json (N = 16 000, A = N), e2-*.json (N = 16 000, A = 64 000), regulaer-L*.json
      M16-/G-Ordner (nur gelesen): Skalar aus INDUZIERT-DICHTE-2D bzw. -GROB fuer den Bitvergleich
  python dirac_auswertung.py vergleich <datei.json> <ref.json> <aus.json>
  python dirac_auswertung.py selbsttest <aus.json>
"""
import glob
import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import grob_auswertung as ga  # noqa: E402  (unveraendert, eingefroren 20261004-091915)

POLYAKOV = -1.0 / (24.0 * math.pi)
ACHSEN = ("r000", "r090")
S_U = 0.5
NL_E1, NL_E2 = (1, 2, 4, 6), (2, 4, 8, 12)
OPS = ("B", "A", "KD", "KD0", "KD2", "lokal_m", "lokal_A")
P_LOF = 0.01                    # Modellprobe wie -GROB
MIN_SAATEN = 16                 # je Datensatz
NSE_NEIN = 2.0
RES_MAX = 1e-8                  # Tor (A): Nullvektor-Residuum (relativ)
GRAM_REL_MAX = 1e-6             # Tor (A): Gram der Nullvektoren komplex-strukturiert (g11 = g22, g12 = 0)
TOR_NEWTON = 1e-12
# Baender in c_eff-Einheiten (Karte), Rauschschwelle = halbe Bandbreite
BAND_F0_REG = (3.0, 5.0)        # regelmaessig (A): 4 +- 1 (deterministisch)
BAND_F0_B = (0.8, 1.2)          # Skalar: 1 +- 0,2
BAND_F1 = (0.6, 1.4)            # (A) Zufallsnetz: 1 +- 0,4
BAND_F2 = (1.5, 2.5)            # (B) Kaehler-Dirac: 2 +- 0,5 (Kartenwortlaut)
BAND_F2K = (-5.0, -3.0)         # [K] berichtigte Erwartung -4 +- 1 (beschreibend, keine Kartenvorhersage)


# ---------------------------------------------------------------------- Einlesen und Tor
def lade(ordner, muster):
    saaten, kopf, dateien = {}, None, []
    for p in sorted(glob.glob(os.path.join(ordner, muster))):
        with open(p) as f:
            d = json.load(f)
        k = {"N": int(d["N"]), "A": float(d.get("A", float(d["N"]))), "nlist": d["nlist"]}
        if kopf is None:
            kopf = k
        elif k["N"] != kopf["N"] or k["A"] != kopf["A"]:
            raise SystemExit(f"{p}: N oder A passt nicht")
        dateien.append(os.path.basename(p))
        for s in d["saaten"]:
            if s["saat"] in saaten:
                raise SystemExit(f"Saat {s['saat']} doppelt ({p})")
            saaten[s["saat"]] = s
    return {"saaten": saaten, "kopf": kopf, "dateien": dateien}


def tor_netz(x):
    return bool(ga.gueltig(x["pruefung"]) and ga.lu_ok(x["lu_B"]) and x["psi"]["residuum"] <= TOR_NEWTON)


def tor_A(ia):
    g = ia["gram"]
    return bool(ia["endlich"] and ia["nullvektor_residuum"] <= RES_MAX
                and ia["gram_komplex_abw"] <= GRAM_REL_MAX * abs(g[0][0]))


def tor_KD(ik):
    return bool(ik["ok_eingang"] and ik["endlich"])


def tor(d):
    f = {"netz": [], "A": [], "KD": []}
    n_netze, res, gab, wneg, neu = 0, [], [], [], []
    for saat, s in d["saaten"].items():
        g0 = s["gamma0"]
        if not (ga.gueltig(s["pruefung0"]) and s["pruefung0_z2"]["delaunay_verletzt_1e-9"] == 0
                and ga.lu_ok(s["lu0_B"])):
            f["netz"].append(f"s{saat}/basis")
        if not tor_A(g0["info_A"]):
            f["A"].append(f"s{saat}/basis")
        if not tor_KD(g0["info_KD"]):
            f["KD"].append(f"s{saat}/basis")
        for p in s["punkte"]:
            for e in p["je_S"]:
                for seite in ("plus", "minus"):
                    x = e[seite]
                    n_netze += 1
                    tag = f"s{saat}/{p['richtung']}/n{p['n']}/{seite}"
                    if not tor_netz(x):
                        f["netz"].append(tag)
                    if not tor_A(x["info_A"]):
                        f["A"].append(tag)
                    if not tor_KD(x["info_KD"]):
                        f["KD"].append(tag)
                    res.append(x["info_A"]["nullvektor_residuum"])
                    gab.append(x["info_A"]["gram_komplex_abw"] / abs(x["info_A"]["gram"][0][0]))
                    wneg.append(x["info_KD"]["w_negativ"] / x["pruefung"]["E"])
                    neu.append(x["neue_kanten"] / x["pruefung"]["E"])
    out = {"netze": n_netze}
    for k, v in f.items():
        out[k] = {"fehler_anzahl": len(v), "fehler": v[:20], "bestanden": len(v) == 0}
    out["nullvektor_residuum_max"] = float(np.max(res)) if res else None
    out["gram_rel_abw_max"] = float(np.max(gab)) if gab else None
    out["anteil_w_negativ_mittel"] = float(np.mean(wneg)) if wneg else None
    out["anteil_w_negativ_max"] = float(np.max(wneg)) if wneg else None
    out["anteil_neue_kanten_mittel"] = float(np.mean(neu)) if neu else None
    return out


def tabelle(d, nliste, op, S=S_U):
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
                        w.append(e["y_" + op])
                        kb[j] = p["betrag"]
            if len(w) == len(ACHSEN):
                Y[i, j] = float(np.mean(w))
    ok = ~np.any(np.isnan(Y), axis=1)
    return np.array(saaten)[ok], Y[ok], kb


# ---------------------------------------------------------------------- Urteilsregeln
def band(ce, se, lo, hi):
    drin = lo <= ce <= hi
    abstand = 0.0 if drin else min(abs(ce - lo), abs(ce - hi))
    tol = 0.5 * (hi - lo)
    if drin and se <= tol:
        u = "eingetroffen"
    elif (not drin) and abstand > NSE_NEIN * se:
        u = "nicht eingetroffen"
    else:
        u = "nicht auswertbar"
    return u, {"band_c_eff": [lo, hi], "im_band": bool(drin), "abstand": abstand,
               "abstand_in_se": abstand / se if se > 0 else None, "se_schwelle": tol,
               "kartenwortlaut": "eingetroffen" if drin else "nicht eingetroffen"}


def fit_op(saetze, modell="quad", fenster=None):
    h = ga.ausgleich(saetze, modell, fenster)
    o = ga.oeffentlich(h)
    o["c_eff"] = h["c"]["wert"] / POLYAKOV
    o["se_c_eff"] = h["c"]["se_u"] / abs(POLYAKOV)
    o["se_c_eff_gls"] = h["c"]["se_gls"] / abs(POLYAKOV)
    if "d" in h:
        o["d_eff"] = h["d"]["wert"] / POLYAKOV
        o["se_d_eff"] = h["d"]["se_u"] / abs(POLYAKOV)
    return h, o


# ---------------------------------------------------------------------- Bitvergleich Skalar gegen -GROB/-DICHTE
def vergleich_skalar(d, ref, S=S_U):
    zeilen, gleich, mx = 0, 0, 0.0
    for saat, s in d["saaten"].items():
        if saat not in ref["saaten"]:
            continue
        r = ref["saaten"][saat]
        g0 = s["gamma0"]["B"] == r["gamma0"]
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
                dg = max(abs(e["plus"]["B"] - f["plus"]["gamma_koord"]), abs(e["minus"]["B"] - f["minus"]["gamma_koord"]))
                mx = max(mx, dg, abs(s["gamma0"]["B"] - r["gamma0"]))
                gleich += int(dg == 0 and g0 and e["D_B"] == f["D_koord"])
    return {"zeilen": zeilen, "bitgleich": gleich, "max_abs_abw_gamma": mx,
            "alle_bitgleich": bool(zeilen > 0 and gleich == zeilen)}


# ---------------------------------------------------------------------- regelmaessiges Netz
def regulaer_auswerten(pfad):
    with open(pfad) as f:
        d = json.load(f)
    erg = {"L": d["L"], "N": d["N"], "datei": os.path.basename(pfad)}
    for op in ("A", "B"):
        ns = sorted(set(p["n"] for p in d["punkte"]))
        kk, cc, cs = [], [], []
        je = []
        for n in ns:
            pp = [p for p in d["punkte"] if p["n"] == n and p["richtung"] in ACHSEN]
            c = float(np.mean([p[op]["c"] for p in pp]))
            c_s = float(np.mean([p[op]["c_S"] for p in pp]))
            kk.append(pp[0]["betrag"])
            cc.append(c)
            cs.append(c_s)
            je.append({"n": n, "k": pp[0]["betrag"], "c_eff_richardson": c / POLYAKOV, "c_eff_S": c_s / POLYAKOV,
                       "richtungen_abw": float(np.ptp([p[op]["c"] for p in pp]) / POLYAKOV),
                       "richardson_abw_rel_max": float(max(p[op]["richardson_abw_rel"] for p in pp))})
        k2 = np.array(kk) ** 2
        X = np.stack([np.ones_like(k2), k2], axis=1)
        th, *_ = np.linalg.lstsq(X, np.array(cc), rcond=None)
        ths, *_ = np.linalg.lstsq(X, np.array(cs), rcond=None)
        erg[op] = {"je_k": je, "c0_eff": float(th[0] / POLYAKOV), "b": float(th[1]),
                   "c0_eff_S_schema": float(ths[0] / POLYAKOV)}
    # Nullmoden-Trennung und Doppler-Stufe (betragskleinste Eigenwerte bei s = h)
    p0 = d["punkte"][0]
    erg["nullvektor_residuum_max"] = max(q["info_A"][sv]["nullvektor_residuum"] for q in d["punkte"] for sv in q["info_A"])
    return erg


# ---------------------------------------------------------------------- Hauptauswertung
def auswerten(lauf, ziel, m16=None, gord=None):
    na = "nicht auswertbar"
    e1 = lade(lauf, "e1-*.json")
    e2 = lade(lauf, "e2-*.json")
    erg = {"polyakov": POLYAKOV, "urteile": {}, "dateien": {"E1": e1["dateien"], "E2": e2["dateien"]}}
    erg["tor"] = {"E1": tor(e1) if e1["saaten"] else None, "E2": tor(e2) if e2["saaten"] else None}
    regs = sorted(glob.glob(os.path.join(lauf, "regulaer-L*.json")))
    erg["regulaer"] = [regulaer_auswerten(p) for p in regs]

    # ---- Datensaetze je Operator in Netzabstands-Einheiten
    tab, info = {}, {}
    for name, d, nl in (("E1", e1, NL_E1), ("E2", e2, NL_E2)):
        if not d["saaten"]:
            continue
        eps = math.sqrt(d["kopf"]["A"] / d["kopf"]["N"])
        info[name] = {"N": d["kopf"]["N"], "A": d["kopf"]["A"], "eps": eps}
        for op in OPS:
            sa, Y, kb = tabelle(d, nl, op)
            Ye = Y * (d["kopf"]["A"] / d["kopf"]["N"])
            x = (kb * eps) ** 2
            tab[(name, op)] = (sa, Ye, x)
        # abgeleitete Groessen je Saat: A mit Massenmatrix, Differenzen
        sa, YA, x = tab[(name, "A")]
        _, YB, _ = tab[(name, "B")]
        _, Ym, _ = tab[(name, "lokal_m")]
        _, YK, _ = tab[(name, "KD")]
        tab[(name, "A_m")] = (sa, YA + 2.0 * Ym, x)
        tab[(name, "A_minus_B")] = (sa, YA - YB, x)
        tab[(name, "KD_plus_4B")] = (sa, YK + 4.0 * YB, x)
        info[name].update({"saaten": int(len(sa)), "saat_min": int(sa.min()) if len(sa) else None,
                           "saat_max": int(sa.max()) if len(sa) else None, "x": x.tolist(),
                           "k_eps": np.sqrt(x).tolist()})
    erg["datensaetze"] = info
    alle_ops = OPS + ("A_m", "A_minus_B", "KD_plus_4B")
    fits, roh = {}, {}
    zwei = all(nm in info for nm in ("E1", "E2"))
    for op in alle_ops:
        if not zwei:
            break
        saetze = [(nm, tab[(nm, op)][1], tab[(nm, op)][2]) for nm in ("E1", "E2")]
        h, o = fit_op(saetze)
        roh[op] = h
        o["je_datensatz"] = {}
        for nm, Y, x in saetze:
            sig2, tau2 = ga.varianzanteile(Y)
            o["je_datensatz"][nm] = {"y_mittel": Y.mean(axis=0).tolist(),
                                     "y_se": (Y.std(axis=0, ddof=1) / math.sqrt(Y.shape[0])).tolist(),
                                     "y_std": Y.std(axis=0, ddof=1).tolist(), "sigma_rest": math.sqrt(sig2),
                                     "tau_versatz": math.sqrt(tau2),
                                     "c_eff_je_k": ((Y.mean(axis=0) - h["a"]["wert"]) / x / POLYAKOV).tolist(),
                                     "se_c_eff_je_k": (Y.std(axis=0, ddof=1) / math.sqrt(Y.shape[0]) / x
                                                       / abs(POLYAKOV)).tolist()}
        # beschreibend
        b = {}
        b["nur_E1"] = fit_op([saetze[0]])[1] if saetze[0][1].shape[0] > 4 else None
        b["nur_E2"] = fit_op([saetze[1]])[1] if saetze[1][1].shape[0] > 4 else None
        b["mit_k6"] = fit_op(saetze, "kub")[1]
        b["a_je_datensatz"] = fit_op(saetze, "a_je_satz")[1]
        b["fenster_k_eps_0.40"] = fit_op(saetze, "quad", 0.40)[1]
        b["nur_k2_fenster_0.40"] = fit_op(saetze, "lin", 0.40)[1]
        try:
            jk = ga.jackknife(saetze, "quad")
            b["jackknife_se_c_eff"] = float(jk[1] / abs(POLYAKOV))
        except Exception as ex:   # beschreibend
            b["jackknife_se_c_eff"] = repr(ex)
        o["beschreibend"] = b
        fits[op] = o
    erg["fits"] = fits

    # ---- Urteile
    def vorbed(op):
        if not zwei:
            return False, "Datensatz fehlt"
        if min(info["E1"]["saaten"], info["E2"]["saaten"]) < MIN_SAATEN:
            return False, "weniger als 16 Saaten je Datensatz"
        if fits[op]["p"] < P_LOF:
            return False, f"Modellprobe p = {fits[op]['p']:.4f} < 0,01"
        return True, ""

    tor_netz_ok = bool(erg["tor"]["E1"] and erg["tor"]["E2"] and erg["tor"]["E1"]["netz"]["bestanden"]
                       and erg["tor"]["E2"]["netz"]["bestanden"])
    tor_A_ok = bool(tor_netz_ok and erg["tor"]["E1"]["A"]["bestanden"] and erg["tor"]["E2"]["A"]["bestanden"])
    tor_KD_ok = bool(tor_netz_ok and erg["tor"]["E1"]["KD"]["bestanden"] and erg["tor"]["E2"]["KD"]["bestanden"])
    erg["vorbedingungen"] = {"tor_netz": tor_netz_ok, "tor_A": tor_A_ok, "tor_KD": tor_KD_ok}

    def urteil_band(op, lo, hi, tor_ok):
        ok, grund = vorbed(op)
        if not tor_ok:
            ok, grund = False, "Tor"
        if not ok:
            w = {"c_eff": fits[op]["c_eff"], "se": fits[op]["se_c_eff"]} if op in fits else {}
            return na, grund, w
        u, w = band(fits[op]["c_eff"], fits[op]["se_c_eff"], lo, hi)
        w.update({"c_eff": fits[op]["c_eff"], "se": fits[op]["se_c_eff"], "p_modell": fits[op]["p"],
                  "birge": fits[op]["birge"], "d_eff": fits[op].get("d_eff"), "se_d_eff": fits[op].get("se_d_eff")})
        return u, "", w

    # ID-F0
    reg = [r for r in erg["regulaer"] if r["L"] == 127]
    if reg:
        c0 = reg[0]["A"]["c0_eff"]
        u_reg = "eingetroffen" if BAND_F0_REG[0] <= c0 <= BAND_F0_REG[1] else "nicht eingetroffen"
        w_reg = {"c0_eff_A_regulaer": c0, "band": list(BAND_F0_REG), "L": 127,
                 "c0_eff_B_regulaer": reg[0]["B"]["c0_eff"]}
    else:
        u_reg, w_reg = na, {"grund": "regulaer-L127 fehlt"}
    u_b, g_b, w_b = urteil_band("B", *BAND_F0_B, tor_netz_ok)
    if u_reg == "eingetroffen" and u_b == "eingetroffen":
        u0 = "eingetroffen"
    elif "nicht eingetroffen" in (u_reg, u_b):
        u0 = "nicht eingetroffen"
    else:
        u0 = na
    kw0 = ("eingetroffen" if (u_reg == "eingetroffen" and w_b.get("kartenwortlaut") == "eingetroffen")
           else "nicht eingetroffen")
    erg["urteile"]["ID-F0"] = {"urteil": u0, "vermerk": g_b or None,
                               "werte": {"teil_regulaer": {"urteil": u_reg, **w_reg},
                                         "teil_skalar": {"urteil": u_b, **w_b}, "kartenwortlaut": kw0}}
    # ID-F1
    u1, g1, w1 = urteil_band("A", *BAND_F1, tor_A_ok)
    erg["urteile"]["ID-F1"] = {"urteil": u1, "vermerk": g1 or None, "werte": w1}
    # ID-F2 (Kartenwortlaut) und [K] berichtigte Erwartung (beschreibend)
    u2, g2, w2 = urteil_band("KD", *BAND_F2, tor_KD_ok)
    u2k, g2k, w2k = urteil_band("KD", *BAND_F2K, tor_KD_ok)
    w2["berichtigt_K_minus4"] = {"urteil": u2k, "vermerk": g2k or None, **w2k}
    erg["urteile"]["ID-F2"] = {"urteil": u2, "vermerk": g2 or None, "werte": w2}
    # ID-F3: Vorzeichen wie Skalar (c_eff > 0) fuer beide Bauweisen
    teil = {}
    for op, tor_ok in (("A", tor_A_ok), ("KD", tor_KD_ok)):
        ok, grund = vorbed(op)
        ok = ok and tor_ok
        ce, se = fits[op]["c_eff"], fits[op]["se_c_eff"]
        if not ok:
            teil[op] = {"urteil": na, "grund": grund or "Tor", "c_eff": ce, "se": se}
        elif ce - NSE_NEIN * se > 0:
            teil[op] = {"urteil": "eingetroffen", "c_eff": ce, "se": se}
        elif ce + NSE_NEIN * se < 0:
            teil[op] = {"urteil": "nicht eingetroffen", "c_eff": ce, "se": se}
        else:
            teil[op] = {"urteil": na, "grund": "Vorzeichen innerhalb 2 SE offen", "c_eff": ce, "se": se}
    if all(t["urteil"] == "eingetroffen" for t in teil.values()):
        u3 = "eingetroffen"
    elif any(t["urteil"] == "nicht eingetroffen" for t in teil.values()):
        u3 = "nicht eingetroffen"
    else:
        u3 = na
    kw3 = "eingetroffen" if all(fits[op]["c_eff"] > 0 for op in ("A", "KD")) else "nicht eingetroffen"
    erg["urteile"]["ID-F3"] = {"urteil": u3, "werte": {"teile": teil, "kartenwortlaut": kw3}}

    # ---- Bitvergleich Skalar
    if m16 and gord:
        erg["bitvergleich_skalar"] = {
            "E1_gegen_DICHTE_N16000": vergleich_skalar(e1, lade_ref(m16, "dichte-N16000-*.json")),
            "E2_gegen_GROB_a": vergleich_skalar(e2, lade_ref(gord, "a-*.json"))}
    with open(ziel, "w") as f:
        json.dump(erg, f, indent=1)
    for k, v in erg["urteile"].items():
        print(k, v["urteil"], v.get("vermerk") or "", flush=True)
    try:
        bilder(erg, tab, fits, os.path.dirname(os.path.abspath(ziel)))
    except Exception as ex:   # Bilder sind beschreibend
        print("Bilder fehlgeschlagen:", repr(ex), flush=True)


def lade_ref(ordner, muster):
    saaten = {}
    for p in sorted(glob.glob(os.path.join(ordner, muster))):
        with open(p) as f:
            d = json.load(f)
        for s in d["saaten"]:
            saaten[s["saat"]] = s
    return {"saaten": saaten}


def bilder(erg, tab, fits, ordner):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    farbe = {"E1": "tab:orange", "E2": "tab:blue"}
    text = {"E1": "Netzabstand 1 (N = 16 000, L = sqrt N)", "E2": "Netzabstand 2 (N = 16 000, L = sqrt 64 000)"}
    titel = {"B": "Skalar (Kotangens-Laplace), Zufallsnetz", "A": "(A) naiver Dirac-Operator, Zufallsnetz",
             "KD": "(B) Kaehler-Dirac, Zufallsnetz"}
    fig, axs = plt.subplots(2, 2, figsize=(15, 11))
    xx = np.linspace(0, 0.37, 200)
    for ax, op in zip(axs.ravel()[:3], ("B", "A", "KD")):
        if op not in fits:
            continue
        o = fits[op]
        a, c, d = o["a"]["wert"], o["c"]["wert"], o["d"]["wert"]
        for nm in ("E1", "E2"):
            sa, Y, x = tab[(nm, op)]
            m = Y.mean(axis=0)
            se = Y.std(axis=0, ddof=1) / math.sqrt(Y.shape[0])
            ax.errorbar(x, (m - a) / x / POLYAKOV, yerr=se / x / abs(POLYAKOV), fmt="o", color=farbe[nm], capsize=3,
                        ms=5, label=f"{text[nm]} ({Y.shape[0]} Saaten)")
        ax.plot(xx, (c + d * xx) / POLYAKOV, "-", color="k", lw=1.2,
                label=f"Ausgleich: c_eff(0) = {o['c_eff']:+.2f} +- {o['se_c_eff']:.2f} (p = {o['p']:.2f})")
        for lv, st in ((1, ":"), (2, "--"), (4, "-.")):
            ax.axhline(lv, color="tab:red", lw=1.0, ls=st, label=f"c = {lv}")
        if op == "KD":
            ax.axhline(-4, color="tab:purple", lw=1.0, ls="-.", label="c = -4 (Kontinuum Kaehler-Dirac, [M])")
            ax.axhline(-2, color="tab:purple", lw=0.8, ls=":", label="c = -2")
        ax.axhline(0, color="0.6", lw=0.6)
        ax.set_xlim(0, 0.37)
        ax.set_xlabel("x = (k eps)^2")
        ax.set_ylabel("c_eff(k) = (y - a)/(x P)")
        ax.set_title(titel[op], fontsize=10)
        ax.legend(fontsize=7)
    ax = axs[1, 1]
    for r in erg["regulaer"]:
        for op, col in (("A", "tab:green"), ("B", "tab:gray")):
            k2 = [q["k"] ** 2 for q in r[op]["je_k"]]
            ce = [q["c_eff_richardson"] for q in r[op]["je_k"]]
            ax.plot(k2, ce, "o-" if r["L"] == 127 else "s--", color=col,
                    label=f"{'(A) naiv' if op == 'A' else 'Skalar'}, L = {r['L']} (fest): c0_eff = {r[op]['c0_eff']:+.2f}")
    for lv, st in ((1, ":"), (2, "--"), (4, "-.")):
        ax.axhline(lv, color="tab:red", lw=1.0, ls=st, label=f"c = {lv}")
    ax.axhline(0, color="0.6", lw=0.6)
    ax.set_xlabel("k^2 (Netzabstand 1)")
    ax.set_ylabel("c_eff(k) = Gamma''/(k^2 A P)  (Richardson)")
    ax.set_title("Regelmaessiges Quadratnetz, festes Netz (Kartenkontrolle ID-F0)", fontsize=10)
    ax.legend(fontsize=7)
    fig.suptitle("INDUZIERT-DIRAC-2D: c_eff(k) gegen k^2 je Bauweise und Netz (Fermion-Konvention, Dirac = +1)",
                 fontsize=11)
    fig.tight_layout()
    fig.savefig(os.path.join(ordner, "bild-ck-gegen-k2.png"), dpi=105)
    plt.close(fig)


# ---------------------------------------------------------------------- synthetischer Selbsttest
def selbsttest(ziel, wdh=400):
    rng = np.random.default_rng(20261004)
    x1 = (2 * np.pi * np.array([1, 2, 4, 6]) / math.sqrt(16000)) ** 2
    x2 = 4 * x1
    wahr = {"a": 3e-4, "c": POLYAKOV, "d": 0.02}
    plan = (("E1", 64, x1, 0.0012, 0.0026), ("E2", 64, x2, 0.0012, 0.0026))
    th, se, p = [], [], []
    for _ in range(wdh):
        saetze = []
        for nm, M, x, sig, tau in plan:
            Y = (wahr["a"] + wahr["c"] * x + wahr["d"] * x ** 2)[None, :] + tau * rng.standard_normal((M, 1)) \
                + sig * rng.standard_normal((M, x.size))
            saetze.append((nm, Y, x))
        h = ga.ausgleich(saetze, "quad")
        th.append(h["_th"])
        se.append([h["a"]["se_gls"], h["c"]["se_gls"], h["d"]["se_gls"]])
        p.append(h["p"])
    th, se = np.array(th), np.array(se)
    w = np.array([wahr["a"], wahr["c"], wahr["d"]])
    out = {"wiederholungen": wdh, "wahr": wahr, "mittel": th.mean(axis=0).tolist(),
           "zug_std": ((th - w) / se).std(axis=0, ddof=1).tolist(), "se_gls_mittel": se.mean(axis=0).tolist(),
           "se_c_eff_mittel": float(se[:, 1].mean() / abs(POLYAKOV)),
           "anteil_p_unter_0.01": float(np.mean(np.array(p) < 0.01)), "dof": 5}
    with open(ziel, "w") as f:
        json.dump(out, f, indent=1)
    print(json.dumps(out, indent=1), flush=True)


def main():
    modus = sys.argv[1]
    if modus == "auswerten":
        auswerten(sys.argv[2], sys.argv[3], *(sys.argv[4:6] if len(sys.argv) > 5 else (None, None)))
    elif modus == "vergleich":
        d = lade(os.path.dirname(os.path.abspath(sys.argv[2])), os.path.basename(sys.argv[2]))
        ref = lade_ref(os.path.dirname(os.path.abspath(sys.argv[3])), os.path.basename(sys.argv[3]))
        out = vergleich_skalar(d, ref)
        out["tor"] = tor(d)
        with open(sys.argv[4], "w") as f:
            json.dump(out, f, indent=1)
        print(json.dumps(out, indent=1), flush=True)
    elif modus == "selbsttest":
        selbsttest(sys.argv[2])
    else:
        raise SystemExit("unbekannter Modus")


if __name__ == "__main__":
    main()
