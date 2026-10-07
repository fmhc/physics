#!/usr/bin/env python3
"""INDUZIERT-DICHTE-4D (Runde 38): Auswertung, Urteile nach PLAN.md Abschnitt 6, Bilder.

Aufruf: python auswertung4d.py <datenordner> <aus.json> [min_saaten=8]  (Abweichung von 8 nur fuer die Codeprobe)
Erwartet im Datenordner: kontrolle-*.json (Teile K1 bis K6) und dichte-N<N>-*.json (Dichte-Variante und festes Netz
auf demselben Grundnetz, beide Laengenregeln). Dateien je N werden zusammengefuehrt; doppelte Saaten sind ein Fehler.
"""
import glob
import json
import math
import os
import sys

import numpy as np
from scipy.special import iv

REGEL_URTEIL = "sp"          # Schwerpunktregel (Berichtigung [K1])
REGEL_KARTE = "geo+"         # Kartenwortlaut: geodaetische Laengen, nicht einbettbare Simplizes ersetzt
S_URTEIL = 0.25
NLISTE = (1, 2)
MIN_SAATEN = 8               # je Dichte, sonst nicht auswertbar
AUSSCHLUSS_MAX = 0.05        # Anteil ausgeschlossener Saaten je Dichte, sonst nicht auswertbar
NSE_VORZEICHEN = 2.0         # IV0, IV1: c -+ 2 SE
IV2_ZIEL, IV2_TOL, IV2_SE_MAX, IV2_NSE = 0.5, 0.2, 0.2, 2.0
IV3_NSE = 3.0
TOR_NEWTON, TOR_Z, TOR_K3, TOR_K4 = 1e-12, 4.0, 1e-3, 1e-9


def gueltig(p):
    return bool(p["verschieden"] and p["alle_knoten"] and p["orient_min"] > 0 and p["koord_vol_rel_abw"] <= 1e-9
                and p["facetten_genau_zwei"] and p["euler"] == 0 and p.get("versatz_ok", False)
                and p["saum_marge_min"] > 0)


def lu_ok(info):
    return bool(info.get("nicht_einbettbar", 1) == 0 and info.get("neg_U", 1) == 0 and info.get("perm_gleich", False)
                and info.get("min_U", -1.0) > 0)


def mittel_se(v):
    v = np.asarray(v, float)
    if v.size < 2:
        return [float(np.mean(v)) if v.size else float("nan"), float("nan"), int(v.size)]
    return [float(np.mean(v)), float(np.std(v, ddof=1) / math.sqrt(v.size)), int(v.size)]


def lade(ordner):
    daten = {}
    for p in sorted(glob.glob(os.path.join(ordner, "dichte-N*.json"))):
        with open(p) as f:
            d = json.load(f)
        if d.get("blind"):
            raise SystemExit(f"blinde Datei im Laufordner: {p}")
        N = int(d["N"])
        e = daten.setdefault(N, {"kopf": {k: d[k] for k in ("N", "Lv", "V", "h0", "rho", "nlist", "S", "regeln",
                                                             "mit_fest")}, "saaten": {}, "dateien": []})
        e["dateien"].append(os.path.basename(p))
        if abs(e["kopf"]["V"] - d["V"]) > 1e-9 or e["kopf"]["nlist"] != d["nlist"] or e["kopf"]["S"] != d["S"]:
            raise SystemExit(f"Kopf passt nicht: {p}")
        for s in d["saaten"]:
            if s["saat"] in e["saaten"]:
                raise SystemExit(f"Saat {s['saat']} bei N = {N} doppelt ({p})")
            e["saaten"][s["saat"]] = s
    return daten


def saat_pruefen(s, regeln, mit_fest):
    """Alle Netz-, LU- und Newton-Pruefungen einer Saat; Rueckgabe (ok, Gruende)."""
    gr = []
    if not gueltig(s["pruefung0"]):
        gr.append("grundnetz")
    if not lu_ok(s["lu0"]):
        gr.append("lu0")
    for p in s["punkte"]:
        for e in p["je_S"]:
            for seite in ("plus", "minus"):
                x = e[seite]
                if not gueltig(x["pruefung"]):
                    gr.append(f"n{p['n']}/S{e['S']}/{seite}/netz")
                if x["psi"]["residuum"] > TOR_NEWTON:
                    gr.append(f"n{p['n']}/S{e['S']}/{seite}/newton")
                for r in regeln:
                    if not lu_ok(x["lu"][r]):
                        gr.append(f"n{p['n']}/S{e['S']}/{seite}/lu/{r}")
            if mit_fest:
                for seite in ("lu_plus", "lu_minus"):
                    for r in regeln:
                        if not lu_ok(e["fest"][seite][r]):
                            gr.append(f"n{p['n']}/S{e['S']}/fest/{seite}/{r}")
    return len(gr) == 0, gr


def tabelle(d, S, regel, variante):
    """Je gueltige Saat y(n) fuer n in NLISTE; dazu |k|."""
    saaten, Y, kb = [], [], None
    for saat in sorted(d["saaten"]):
        s = d["saaten"][saat]
        if not s["_ok"]:
            continue
        row, kk = [], []
        for n in NLISTE:
            p = [p for p in s["punkte"] if p["n"] == n][0]
            e = [e for e in p["je_S"] if abs(e["S"] - S) < 1e-12][0]
            row.append(e["y"][regel] if variante == "dichte" else e["fest"]["y"][regel])
            kk.append(p["betrag"])
        saaten.append(saat)
        Y.append(row)
        kb = np.array(kk)
    return np.array(saaten), np.array(Y, float), kb


def analyse(d, S, regel, variante):
    saaten, Y, kb = tabelle(d, S, regel, variante)
    if len(saaten) < 2:
        return None
    x = kb ** 2
    X = np.stack([np.ones_like(x), x], axis=1)
    koef, *_ = np.linalg.lstsq(X, Y.T, rcond=None)
    a, c = koef[0], koef[1]
    c0 = (Y @ x) / np.sum(x * x)
    V, N = d["kopf"]["V"], d["kopf"]["N"]
    dy_glob = (N - 1) * math.log(iv(0, 4 * S)) / (2 * S * S * V)
    out = {"saaten": int(len(saaten)), "S": S, "regel": regel, "variante": variante, "betrag": kb.tolist(),
           "betrag_mal_h0": (kb * d["kopf"]["h0"]).tolist(), "c": mittel_se(c), "a": mittel_se(a),
           "a_korr": mittel_se(a - (dy_glob if variante == "dichte" else 0.0)),
           "dy_global": dy_glob if variante == "dichte" else 0.0, "c_std_je_saat": float(np.std(c, ddof=1)),
           "c_ohne_achsenabschnitt": mittel_se(c0),
           "y_je_n": [dict(zip(("mittel", "se", "anzahl"), mittel_se(Y[:, j]))) for j in range(len(NLISTE))],
           "y_std_je_n": [float(np.std(Y[:, j], ddof=1)) for j in range(len(NLISTE))],
           "c_je_n_direkt": [dict(zip(("mittel", "se", "anzahl"), mittel_se(Y[:, j] / kb[j] ** 2)))
                             for j in range(len(NLISTE))],
           "c_je_saat": c.tolist(), "a_je_saat": a.tolist(), "saatliste": saaten.tolist()}
    if variante == "dichte":
        out["c_je_n_nach_abzug_global"] = [dict(zip(("mittel", "se", "anzahl"),
                                                    mittel_se((Y[:, j] - dy_glob) / kb[j] ** 2)))
                                           for j in range(len(NLISTE))]
    return out


def urteil_vorzeichen(c, se, positiv_ist_eingetroffen):
    hi, lo = c + NSE_VORZEICHEN * se, c - NSE_VORZEICHEN * se
    if positiv_ist_eingetroffen:
        return "eingetroffen" if lo > 0 else ("nicht eingetroffen" if hi < 0 else "nicht auswertbar")
    return "eingetroffen" if hi < 0 else ("nicht eingetroffen" if lo > 0 else "nicht auswertbar")


def urteil_iv2(ch, seh, ct, set_, rho_h, rho_t):
    lr = math.log(rho_h / rho_t)
    w = {"c_hoch": ch, "se_hoch": seh, "c_tief": ct, "se_tief": set_, "rho_hoch": rho_h, "rho_tief": rho_t}
    sig_h, sig_t = abs(ch) > IV2_NSE * seh, abs(ct) > IV2_NSE * set_
    if not (sig_h and sig_t):
        w["grund"] = "mindestens ein c nicht von 0 getrennt (2 SE)"
        return "nicht auswertbar", w
    if np.sign(ch) != np.sign(ct):
        w["grund"] = "Vorzeichen verschieden"
        return "nicht eingetroffen", w
    p = math.log(ch / ct) / lr
    sep = math.sqrt((seh / ch) ** 2 + (set_ / ct) ** 2) / lr
    w.update({"p": p, "se_p": sep})
    lo, hi = IV2_ZIEL - IV2_TOL, IV2_ZIEL + IV2_TOL
    abst = 0.0 if lo <= p <= hi else min(abs(p - lo), abs(p - hi))
    w["abstand_zum_band"] = abst
    if abst == 0.0 and sep <= IV2_SE_MAX:
        return "eingetroffen", w
    if abst > IV2_NSE * sep:
        return "nicht eingetroffen", w
    return "nicht auswertbar", w


def urteil_iv3(a, se):
    return ("eingetroffen" if abs(a) <= IV3_NSE * se else "nicht eingetroffen"), {"a": a, "se": se,
                                                                                    "abstand_in_se": abs(a) / se}


def tor_kontrolle(ordner):
    k = {}
    for p in sorted(glob.glob(os.path.join(ordner, "kontrolle*.json"))):
        with open(p) as f:
            d = json.load(f)
        for key, v in d.items():
            if key.startswith("K"):
                if key in k and isinstance(k[key], list) and isinstance(v, list):
                    k[key] = k[key] + v          # Teile aus mehreren Kontrolldateien zusammenfuehren
                else:
                    k[key] = v
    t = {"teile": sorted(k)}
    if "K1_psi" in k:
        t["K1_newton_max"] = max(x["newton"]["residuum"] for x in k["K1_psi"])
        t["K1_z_max"] = max(max(abs(x["z_e^-4sigma"]), abs(x["z_cos"])) for x in k["K1_psi"])
    if "K2_saum" in k:
        t["K2_gleich"] = all(x["gleich_w4"] for x in k["K2_saum"])
        t["K2_leere_umkugeln"] = all(x["umkugeln_mit_punkt_innen"] == 0 for x in k["K2_saum"])
        t["K2_gueltig"] = all(gueltig(x["pruefung"]) and gueltig(x["pruefung_w4"]) for x in k["K2_saum"])
    if "K3_geodaete" in k:
        t["K3_geo_max"] = k["K3_geodaete"]["max_abs_rel_geo"]
        t["K3_mitte_max"] = k["K3_geodaete"]["max_abs_rel_mitte"]
    if "K4_logdet" in k:
        t["K4_max_rel"] = max(max(x["abw_slogdet"], x["abw_eigen"]) / abs(x["gamma_lu"]) for x in k["K4_logdet"])
        t["K4_p1_gegen_induziert"] = max(x["p1_gegen_induziert_max_rel"] for x in k["K4_logdet"])
    t["bestanden_urteil"] = bool(t.get("K1_newton_max", 1) <= TOR_NEWTON and t.get("K1_z_max", 99) <= TOR_Z
                                 and t.get("K2_gleich", False) and t.get("K2_leere_umkugeln", False)
                                 and t.get("K2_gueltig", False) and t.get("K4_max_rel", 1) <= TOR_K4
                                 and t.get("K4_p1_gegen_induziert", 1) <= 1e-9)
    t["bestanden_karte"] = bool(t["bestanden_urteil"] and t.get("K3_geo_max", 1) <= TOR_K3)
    return t, k


def main():
    ordner, ziel = sys.argv[1], sys.argv[2]
    min_saaten = int(sys.argv[3].split("=")[1]) if len(sys.argv) > 3 else MIN_SAATEN   # nur fuer die Codeprobe
    na = "nicht auswertbar"
    daten = lade(ordner)
    tk, kontrolle = tor_kontrolle(ordner)
    erg = {"urteile": {}, "tor": {"kontrolle": tk}, "analyse": {}, "regel_urteil": REGEL_URTEIL,
           "regel_karte": REGEL_KARTE, "S": S_URTEIL, "nliste": list(NLISTE)}
    if len(daten) < 1:
        raise SystemExit("keine Daten")
    Ns = sorted(daten)
    N_h, N_t = Ns[-1], Ns[0]
    regeln = ("sp", "geo+")
    lauf_ok = {}
    for N, d in daten.items():
        aus = []
        for saat, s in d["saaten"].items():
            ok, gr = saat_pruefen(s, regeln, d["kopf"]["mit_fest"])
            s["_ok"] = ok
            if not ok:
                aus.append({"saat": saat, "gruende": gr[:10], "anzahl": len(gr)})
        M = len(d["saaten"])
        anteil = len(aus) / M if M else 1.0
        lauf_ok[N] = bool(M - len(aus) >= min_saaten and anteil <= AUSSCHLUSS_MAX)
        # Netzstatistik (beschreibend)
        neu, ers, ers_f, faktor, marge = [], [], [], [], []
        for s in d["saaten"].values():
            marge.append(s["pruefung0"]["saum_marge_min"])
            for p in s["punkte"]:
                for e in p["je_S"]:
                    for seite in ("plus", "minus"):
                        neu.append(e[seite]["neue_simplizes_anteil"])
                        ers.append(e[seite]["ersetzt"]["geo+"] / e[seite]["pruefung"]["S4"])
                        faktor.append(e[seite]["pruefung"]["faktor_qhull"])
                        marge.append(e[seite]["pruefung"]["saum_marge_min"])
                    if d["kopf"]["mit_fest"]:
                        ers_f.append((e["fest"]["ersetzt_plus"]["geo+"] + e["fest"]["ersetzt_minus"]["geo+"])
                                     / (2.0 * s["pruefung0"]["S4"]))
        erg["tor"][f"N{N}"] = {"saaten": M, "ausgeschlossen": aus, "anteil_ausgeschlossen": anteil,
                               "lauf_ok": lauf_ok[N], "neue_simplizes_mittel": float(np.mean(neu)) if neu else None,
                               "ersetzt_anteil_mittel_bild": float(np.mean(ers)) if ers else None,
                               "ersetzt_anteil_max_bild": float(np.max(ers)) if ers else None,
                               "ersetzt_anteil_mittel_fest": float(np.mean(ers_f)) if ers_f else None,
                               "saum_marge_min": float(np.min(marge)) if marge else None,
                               "qhull_faktor_mittel": float(np.mean(faktor)) if faktor else None,
                               "rho": d["kopf"]["rho"], "h0": d["kopf"]["h0"], "V": d["kopf"]["V"]}
        for r in regeln:
            for var in ("dichte", "fest"):
                if var == "fest" and not d["kopf"]["mit_fest"]:
                    continue
                a = analyse(d, S_URTEIL, r, var)
                if a is not None:
                    erg["analyse"][f"N{N}/{var}/{r}"] = a
    ana = erg["analyse"]
    tor_u = tk["bestanden_urteil"]
    tor_k = tk["bestanden_karte"]
    erg["tor"]["bestanden_urteil"] = tor_u
    erg["tor"]["bestanden_karte"] = tor_k

    def hole(N, var, r):
        a = ana.get(f"N{N}/{var}/{r}")
        return a if (a is not None and lauf_ok.get(N, False)) else None

    # IV0: festes Netz positiv (N hoch)
    for nr, var, pos in (("IV0", "fest", True), ("IV1", "dichte", False)):
        w = {}
        u = {}
        for r, tor in ((REGEL_URTEIL, tor_u), (REGEL_KARTE, tor_k)):
            a = hole(N_h, var, r)
            if a is None or not tor:
                u[r] = na
                w[r] = {"tor": tor, "lauf_ok": lauf_ok.get(N_h, False)}
                continue
            c, se, M = a["c"]
            u[r] = urteil_vorzeichen(c, se, pos)
            w[r] = {"c": c, "se": se, "saaten": M, "c_minus_2se": c - 2 * se, "c_plus_2se": c + 2 * se,
                    "saaten_noetig_fuer_2se": int(math.ceil(M * (2 * se / abs(c)) ** 2)) if c != 0 else None}
            at = hole(N_t, var, r)
            if at is not None and N_t != N_h:
                w[r]["tiefe_dichte"] = {"c": at["c"][0], "se": at["c"][1], "saaten": at["c"][2],
                                        "urteil_gleiche_regel": urteil_vorzeichen(at["c"][0], at["c"][1], pos)}
        erg["urteile"][nr] = {"urteil": u[REGEL_URTEIL], "werte": {"regel_urteil": REGEL_URTEIL, **w[REGEL_URTEIL],
                                                                   "kartenwortlaut_geo+": {"urteil": u[REGEL_KARTE],
                                                                                           **w[REGEL_KARTE]}}}
    # Kartenwortlaut IV1 woertlich: eingetroffen genau dann, wenn Steigung + 2 SE < 0
    for r in (REGEL_URTEIL, REGEL_KARTE):
        a = hole(N_h, "dichte", r)
        if a is not None:
            key = "kartenwortlaut_zweiwertig" if r == REGEL_URTEIL else "kartenwortlaut_zweiwertig_geo+"
            erg["urteile"]["IV1"]["werte"][key] = ("eingetroffen" if a["c"][0] + 2 * a["c"][1] < 0
                                                   else "nicht eingetroffen")
    # IV2: Exponent zwischen zwei Dichten
    for r, tor in ((REGEL_URTEIL, tor_u), (REGEL_KARTE, tor_k)):
        ah, at = hole(N_h, "dichte", r), hole(N_t, "dichte", r)
        if ah is None or at is None or N_h == N_t or not tor:
            u2, w2 = na, {"tor": tor}
        else:
            u2, w2 = urteil_iv2(ah["c"][0], ah["c"][1], at["c"][0], at["c"][1], daten[N_h]["kopf"]["rho"],
                                daten[N_t]["kopf"]["rho"])
            ahf, atf = hole(N_h, "fest", r), hole(N_t, "fest", r)
            if ahf is not None and atf is not None:
                w2["festes_netz_beschreibend"] = urteil_iv2(ahf["c"][0], ahf["c"][1], atf["c"][0], atf["c"][1],
                                                            daten[N_h]["kopf"]["rho"], daten[N_t]["kopf"]["rho"])
        if r == REGEL_URTEIL:
            erg["urteile"]["IV2"] = {"urteil": u2, "werte": {"regel_urteil": r, **w2}}
        else:
            erg["urteile"]["IV2"]["werte"]["kartenwortlaut_geo+"] = {"urteil": u2, **w2}
    # IV3: kein Volumenterm (berichtigt: nach Abzug des exakten globalen Glieds; Kartenwortlaut: roh)
    for r, tor in ((REGEL_URTEIL, tor_u), (REGEL_KARTE, tor_k)):
        a = hole(N_h, "dichte", r)
        if a is None or not tor:
            ub, wb, ur, wr = na, {"tor": tor}, na, {}
        else:
            ub, wb = urteil_iv3(a["a_korr"][0], a["a_korr"][1])
            ur, wr = urteil_iv3(a["a"][0], a["a"][1])
            wb["dy_global"] = a["dy_global"]
            at = hole(N_t, "dichte", r)
            if at is not None and N_t != N_h:
                wb["tiefe_dichte"] = dict(zip(("urteil", "werte"), urteil_iv3(at["a_korr"][0], at["a_korr"][1])))
        if r == REGEL_URTEIL:
            erg["urteile"]["IV3"] = {"urteil": ub, "werte": {"regel_urteil": r, "berichtigt": wb,
                                                             "kartenwortlaut_roh": {"urteil": ur, **wr}}}
        else:
            erg["urteile"]["IV3"]["werte"]["kartenwortlaut_geo+"] = {"urteil": ub, "berichtigt": wb,
                                                                     "roh": {"urteil": ur, **wr}}
    with open(ziel, "w") as f:
        json.dump(erg, f, indent=1)
    for k, v in erg["urteile"].items():
        print(k, v["urteil"], flush=True)
    try:
        bilder(erg, daten, kontrolle, os.path.dirname(os.path.abspath(ziel)), N_h, N_t)
    except Exception as ex:  # Bilder sind beschreibend
        print("Bilder fehlgeschlagen:", repr(ex), flush=True)


def bilder(erg, daten, kontrolle, ordner, N_h, N_t):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    ana = erg["analyse"]
    farbe = {N_h: "tab:green", N_t: "tab:orange"}
    # 1: y gegen k^2 je Variante und Dichte
    fig, axs = plt.subplots(1, 2, figsize=(14, 5.5))
    for j, var in enumerate(("dichte", "fest")):
        ax = axs[j]
        for N in sorted({N_h, N_t}):
            for r, mk, ls in (("sp", "o", "-"), ("geo+", "s", "--")):
                a = ana.get(f"N{N}/{var}/{r}")
                if a is None:
                    continue
                kb = np.array(a["betrag"])
                ym = np.array([x["mittel"] for x in a["y_je_n"]])
                ys = np.array([x["se"] for x in a["y_je_n"]])
                if var == "dichte":
                    ym = ym - a["dy_global"]
                ax.errorbar(kb ** 2 * (1.0 if r == "sp" else 1.02), ym, yerr=ys, fmt=mk, color=farbe[N], ms=5,
                            capsize=3, mfc="none" if r == "geo+" else None,
                            label=f"N = {N} (rho = {daten[N]['kopf']['rho']:.2f}), Regel {r}, {a['saaten']} Saaten")
                xx = np.linspace(0, kb.max() ** 2 * 1.05, 50)
                aa = a["a_korr"][0] if var == "dichte" else a["a"][0]
                ax.plot(xx, aa + a["c"][0] * xx, ls, color=farbe[N], lw=0.8)
        ax.axhline(0, color="0.6", lw=0.6)
        ax.set_xlabel("k^2 (Koordinaten)")
        ax.set_ylabel("y = Gamma''(S)/V" + (" minus globales Glied" if var == "dichte" else ""))
        ax.set_title(("Dichte-Variante (Punkte nach Volumen, neu vernetzt)" if var == "dichte"
                      else "Festes Netz (nur Laengen aendern sich)") + f", S = {S_URTEIL}", fontsize=9)
        ax.legend(fontsize=6.5)
    fig.suptitle("INDUZIERT-DICHTE-4D: konforme Steifigkeit, Steigung = c (negativ = Einstein-Vorzeichen)")
    fig.tight_layout()
    fig.savefig(f"{ordner}/bild-konform.png", dpi=110)
    plt.close(fig)
    # 2: Saatstreuung
    fig, axs = plt.subplots(1, 2, figsize=(14, 5))
    for N in sorted({N_h, N_t}):
        for var, ls in (("dichte", "-"), ("fest", ":")):
            a = ana.get(f"N{N}/{var}/sp")
            if a is None:
                continue
            c = np.array(a["c_je_saat"])
            axs[0].hist(c, bins=20, alpha=0.4, color=farbe[N], histtype="stepfilled" if var == "dichte" else "step",
                        label=f"N = {N}, {var}: c je Saat (Std {np.std(c, ddof=1):.3g})")
            axs[0].axvline(np.mean(c), color=farbe[N], lw=1.5, ls=ls)
            axs[1].plot(a["betrag"], a["y_std_je_n"], "o" + ls, color=farbe[N], label=f"N = {N}, {var}: Std y je Saat")
    axs[0].axvline(0, color="k", lw=0.8)
    axs[0].set_xlabel("c (Steigung von y gegen k^2 je Saat), Regel sp")
    axs[0].legend(fontsize=7)
    axs[1].set_xlabel("abs(k)")
    axs[1].set_ylabel("Standardabweichung von y ueber Saaten")
    axs[1].set_yscale("log")
    axs[1].legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(f"{ordner}/bild-streuung.png", dpi=110)
    plt.close(fig)
    # 3: Kippstatistik
    fig, axs = plt.subplots(1, 2, figsize=(14, 5))
    k5 = kontrolle.get("K5_kippen", [])
    for n in sorted({x["n"] for x in k5}):
        z = [x for x in k5 if x["n"] == n]
        s = np.array([x["s"] for x in z])
        axs[0].loglog(s, [x["neue_simplizes"] / x["F"] for x in z], "o-", ms=4, label=f"n = {n}: neue Simplizes/F")
        axs[1].loglog(s, [max(x["nicht_einbettbar_bild"], 0.5) / x["F"] for x in z], "o-", ms=4,
                      label=f"n = {n}: Bildnetz, geodaetische Laengen")
        axs[1].loglog(s, [max(x["nicht_einbettbar_fest"], 0.5) / x["F"] for x in z], "x:", ms=5,
                      label=f"n = {n}: festes Netz, geodaetische Laengen")
    axs[0].set_xlabel("s")
    axs[0].set_ylabel("Anteil neuer 4-Simplizes gegenueber s = 0")
    axs[0].set_title("Kippen gegen s (Koordinaten-Delaunay der Bildpunkte)", fontsize=9)
    axs[0].legend(fontsize=7)
    axs[1].set_xlabel("s")
    axs[1].set_ylabel("Anteil nicht einbettbarer Simplizes (0 als 0,5 gezeichnet)")
    axs[1].set_title("Splitter: geodaetische Laengen nicht einbettbar (Grund fuer Regel sp)", fontsize=9)
    axs[1].legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(f"{ordner}/bild-kippen.png", dpi=110)
    plt.close(fig)


if __name__ == "__main__":
    main()
