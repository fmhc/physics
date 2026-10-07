#!/usr/bin/env python3
"""INDUZIERT-DICHTE-2D (Runde 38): Auswertung, Urteile nach PLAN.md Abschnitt 6, Bilder.

Aufruf: python dichte_auswertung.py <datenordner> <aus.json>
Erwartet im Datenordner: kontrolle.json, fest-N64000-*.json (ID0), dichte-N64000-*.json (Urteil),
optional dichte-N16000-*.json und intr-N16000-*.json (beschreibend). Alle Dateien je Art und N werden
zusammengefuehrt; doppelte Saaten sind ein Fehler.
"""
import glob
import json
import math
import os
import sys

import numpy as np

POLYAKOV = -1.0 / (24.0 * math.pi)
C_FEST_KARTE = 0.159                        # Karte: INDUZIERT-ZUFALL-2D, festes Netz
C_FEST_IZ2D = 0.15909                       # INDUZIERT-ZUFALL-2D ERGEBNIS 3.1 (N = 64 000, Achsen, n = 2)
ID0_N, ID0_n, ID0_TOL = 64000, 2, 0.02
HAUPT_N, HAUPT_S = 64000, 0.5
HAUPT_NLISTE = (2, 4, 8, 12)
NEBEN_N, NEBEN_NLISTE = 16000, (1, 2, 4, 6)
ACHSEN = ("r000", "r090")
ID1_TOL = 0.30
GATE_SE = (C_FEST_KARTE - POLYAKOV) / 3.0   # Unterscheidbarkeit +0,159 gegen -1/(24 pi) mit 3 Standardfehlern
ID2_NSE = 3.0
ID3_NSE = 2.0
ID1_NSE = 2.0
TOR_K3 = 1e-3
TOR_K4 = 1e-9
TOR_NEWTON = 1e-12
TOR_Z = 4.0
MIN_SAATEN = 16                             # PLAN Abschnitt 6: unter 16 Saaten bei N = 64 000 nicht auswertbar


def lade_art(ordner, muster):
    daten = {}
    for p in sorted(glob.glob(os.path.join(ordner, muster))):
        with open(p) as f:
            d = json.load(f)
        N = int(d["N"])
        daten.setdefault(N, {"saaten": {}, "dateien": [], "kopf": d})
        daten[N]["dateien"].append(os.path.basename(p))
        for s in d["saaten"]:
            if s["saat"] in daten[N]["saaten"]:
                raise SystemExit(f"Saat {s['saat']} bei N = {N} doppelt ({p})")
            daten[N]["saaten"][s["saat"]] = s
    return daten


def gueltig(p):
    return (p["euler"] == 0 and p["kanten_genau_zwei"] and p["orient_min"] > 0 and p["koord_flaeche_rel_abw"] <= 1e-9
            and p["E"] == 3 * p["V"] and p["F"] == 2 * p["V"] and p["phys_flaeche_min"] > 0
            and p["l_max_durch_L"] < 0.25)


def lu_ok(info):
    return info["neg_U"] == 0 and info["perm_ungleich"] == 0 and info["min_U"] > 0


def tor_dichte(dichte):
    """Netz-, LU- und Newton-Pruefungen fuer alle Auswertungen eines Datensatzes."""
    fehler, anzahl, neg, negsum, neu = [], 0, [], [], []
    for N, d in dichte.items():
        for saat, s in d["saaten"].items():
            ok = gueltig(s["pruefung0"]) and s["pruefung0_z2"]["delaunay_verletzt_1e-9"] == 0 and lu_ok(s["lu0"])
            if not ok:
                fehler.append(f"N{N}/s{saat}/basis")
            for p in s["punkte"]:
                for e in p["je_S"]:
                    for seite in ("plus", "minus"):
                        x = e[seite]
                        anzahl += 1
                        ok = (gueltig(x["koord_pruefung"]) and lu_ok(x["lu"]["koord"])
                              and x["psi"]["residuum"] <= TOR_NEWTON)
                        if "intr_pruefung" in x:
                            ok = ok and gueltig(x["intr_pruefung"]) and lu_ok(x["lu"]["intr"])
                        if not ok:
                            fehler.append(f"N{N}/s{saat}/{p['richtung']}/n{p['n']}/S{e['S']}/{seite}")
                        neg.append(x["koord_pruefung"]["w_negativ"] / x["koord_pruefung"]["E"])
                        negsum.append(x["koord_pruefung"].get("w_neg_summe", 0.0))
                        neu.append(x["koord_neue_kanten"] / x["koord_pruefung"]["E"])
    return {"auswertungen": anzahl, "fehler": fehler[:50], "fehler_anzahl": len(fehler),
            "anteil_negativ_max": float(max(neg)) if neg else None,
            "anteil_negativ_mittel": float(np.mean(neg)) if neg else None,
            "w_neg_summe_min": float(min(negsum)) if negsum else None,
            "anteil_neue_kanten_mittel": float(np.mean(neu)) if neu else None}


def tor_kontrolle(k):
    t = {}
    k1 = k["K1_psi"]
    t["K1_newton_max"] = max(x["newton"]["residuum"] for x in k1)
    t["K1_z_max"] = max(max(abs(x["z_e^-2sigma"]), abs(x["z_cos"])) for x in k1)
    t["K2_gleich"] = all(x["gleich_grund"] and x["gleich_bild_s0.5"] for x in k["K2_streifen"])
    t["K3_geo_max"] = k["K3_geodaete"]["max_abs_rel_geo"]
    t["K3_mitte_max"] = k["K3_geodaete"]["max_abs_rel_mitte"]
    t["K4_max_rel"] = max(max(x["abw_slogdet"], x["abw_eigen"]) / abs(x["gamma_lu"]) for x in k["K4_logdet"])
    t["bestanden"] = bool(t["K1_newton_max"] <= TOR_NEWTON and t["K1_z_max"] <= TOR_Z and t["K2_gleich"]
                          and t["K3_geo_max"] <= TOR_K3 and t["K4_max_rel"] <= TOR_K4)
    return t


def seed_tabelle(d, nliste, S, variante="koord", richtungen=ACHSEN):
    """Je Saat: y(n) gemittelt ueber die Richtungen; dazu k(n)."""
    saaten = sorted(d["saaten"])
    Y = np.full((len(saaten), len(nliste)), np.nan)
    Yr = {r: np.full((len(saaten), len(nliste)), np.nan) for r in richtungen}
    kb = np.full(len(nliste), np.nan)
    for i, saat in enumerate(saaten):
        s = d["saaten"][saat]
        for j, n in enumerate(nliste):
            werte = []
            for p in s["punkte"]:
                if p["n"] != n or p["richtung"] not in richtungen:
                    continue
                for e in p["je_S"]:
                    if abs(e["S"] - S) < 1e-12 and f"y_{variante}" in e:
                        werte.append(e[f"y_{variante}"])
                        Yr[p["richtung"]][i, j] = e[f"y_{variante}"]
                        kb[j] = p["betrag"]
            if len(werte) == len(richtungen):
                Y[i, j] = float(np.mean(werte))
    ok = ~np.any(np.isnan(Y), axis=1)
    return np.array(saaten)[ok], Y[ok], kb, {r: v[ok] for r, v in Yr.items()}


def fit_je_saat(Y, kb, mit_k4=False):
    x = kb ** 2
    X = np.stack([np.ones_like(x), x] + ([x ** 2] if mit_k4 else []), axis=1)
    koef, *_ = np.linalg.lstsq(X, Y.T, rcond=None)
    return koef.T                      # je Saat (a, c[, d])


def mittel_se(v):
    v = np.asarray(v, float)
    return float(np.mean(v)), float(np.std(v, ddof=1) / math.sqrt(v.size)), int(v.size)


def analyse(d, nliste, S, variante="koord", richtungen=ACHSEN):
    saaten, Y, kb, Yr = seed_tabelle(d, nliste, S, variante, richtungen)
    if len(saaten) < 2:
        return None
    ac = fit_je_saat(Y, kb)
    a, c = ac[:, 0], ac[:, 1]
    acd = fit_je_saat(Y, kb, True)
    c0 = (Y @ kb ** 2) / np.sum(kb ** 4)
    ckmin = (Y[:, 0] - a) / kb[0] ** 2
    out = {"saaten": int(len(saaten)), "S": S, "variante": variante, "n": list(nliste), "betrag": kb.tolist(),
           "c": mittel_se(c), "a": mittel_se(a), "c_std_je_saat": float(np.std(c, ddof=1)),
           "c_kmin_kartenwortlaut": mittel_se(ckmin), "c_ohne_achsenabschnitt": mittel_se(c0),
           "fit_k4": {"a": mittel_se(acd[:, 0]), "c": mittel_se(acd[:, 1]), "d": mittel_se(acd[:, 2])},
           "y_je_n": [dict(zip(("mittel", "se", "anzahl"), mittel_se(Y[:, j]))) for j in range(len(nliste))],
           "y_std_je_n": [float(np.std(Y[:, j], ddof=1)) for j in range(len(nliste))],
           "c_je_n_nach_abzug": [dict(zip(("mittel", "se", "anzahl"), mittel_se((Y[:, j] - a) / kb[j] ** 2)))
                                 for j in range(len(nliste))],
           "c_je_n_direkt": [dict(zip(("mittel", "se", "anzahl"), mittel_se(Y[:, j] / kb[j] ** 2)))
                             for j in range(len(nliste))],
           "c_je_saat": c.tolist(), "a_je_saat": a.tolist()}
    je_r = {}
    for r in richtungen:
        acr = fit_je_saat(Yr[r], kb)
        je_r[r] = {"c": mittel_se(acr[:, 1]), "a": mittel_se(acr[:, 0])}
    out["je_richtung"] = je_r
    return out


def urteil_id1(c, se):
    lo, hi = (1 + ID1_TOL) * POLYAKOV, (1 - ID1_TOL) * POLYAKOV       # P < 0: lo < hi
    drin = lo <= c <= hi
    abstand = 0.0 if drin else min(abs(c - lo), abs(c - hi))
    if drin and se <= ID1_TOL * abs(POLYAKOV):
        u = "eingetroffen"
    elif (not drin) and abstand > ID1_NSE * se:
        u = "nicht eingetroffen"
    else:
        u = "nicht auswertbar"
    return u, {"band": [lo, hi], "im_band": drin, "abstand_zum_band": abstand, "rel_abw": abs(c / POLYAKOV - 1)}


def main():
    ordner, ziel = sys.argv[1], sys.argv[2]
    with open(os.path.join(ordner, "kontrolle.json")) as f:
        kontrolle = json.load(f)
    fest = lade_art(ordner, "fest-N*.json")
    dichte = lade_art(ordner, "dichte-N*.json")
    intr = lade_art(ordner, "intr-N*.json")
    na = "nicht auswertbar"
    erg = {"urteile": {}, "polyakov": POLYAKOV, "gate_se": GATE_SE}
    tk = tor_kontrolle(kontrolle)
    td = tor_dichte(dichte)
    ti = tor_dichte(intr) if intr else None
    erg["tor"] = {"kontrolle": tk, "dichte": td, "intr": ti,
                  "bestanden": bool(tk["bestanden"] and td["fehler_anzahl"] == 0)}

    # ---------------- ID0: feste Punkte, nur Kantenlaengen (geo, Richardson), N = 64 000, n = 2, Achsen
    if ID0_N in fest:
        werte = {"geo": [], "ecken": [], "mitte": [], "geo_S": []}
        netze_ok = True
        for saat, s in sorted(fest[ID0_N]["saaten"].items()):
            p0 = s["pruefung0"]
            netze_ok = netze_ok and p0["euler"] == 0 and p0["delaunay_verletzt_1e-9"] == 0 and lu_ok(s["lu"])
            for name in werte:
                v = [p[name]["c"] for p in s["punkte"] if p["n"] == ID0_n and p["richtung"] in ACHSEN]
                if len(v) == 2:
                    werte[name].append(float(np.mean(v)))
        m, se, k = mittel_se(werte["geo"])
        rel = abs(m / C_FEST_KARTE - 1)
        u = ("eingetroffen" if rel <= ID0_TOL else "nicht eingetroffen") if (netze_ok and tk["K4_max_rel"] <= TOR_K4) \
            else na
        erg["urteile"]["ID0"] = {"urteil": u, "werte": {
            "c_fest_geo": m, "se": se, "saaten": k, "rel_abw_zu_0_159": rel,
            "rel_abw_zu_0_15909": abs(m / C_FEST_IZ2D - 1), "c_fest_ecken": mittel_se(werte["ecken"]),
            "c_fest_mitte": mittel_se(werte["mitte"]), "c_fest_geo_S0.5": mittel_se(werte["geo_S"]),
            "je_saat_geo": werte["geo"], "je_saat_ecken": werte["ecken"], "netze_ok": netze_ok}}
        # beschreibend: festes Netz ueber alle k
        tab = []
        for n in sorted({p["n"] for s in fest[ID0_N]["saaten"].values() for p in s["punkte"]}):
            row = {"n": n}
            for name in ("geo", "ecken", "mitte", "geo_S"):
                v = [float(np.mean([p[name]["c"] for p in s["punkte"] if p["n"] == n and p["richtung"] in ACHSEN]))
                     for s in fest[ID0_N]["saaten"].values()]
                row[name] = mittel_se(v)
            row["betrag"] = [p["betrag"] for p in next(iter(fest[ID0_N]["saaten"].values()))["punkte"]
                             if p["n"] == n][0]
            tab.append(row)
        erg["fest_tabelle"] = tab
    else:
        erg["urteile"]["ID0"] = {"urteil": na, "werte": {}}

    # ---------------- Hauptgroesse: N = 64 000, S = 0,5, koord (Kartenwortlaut des Netzes), Achsen
    ana = {}
    for N, nl in ((HAUPT_N, HAUPT_NLISTE), (NEBEN_N, NEBEN_NLISTE)):
        if N in dichte:
            for S in sorted({e["S"] for s in dichte[N]["saaten"].values() for p in s["punkte"] for e in p["je_S"]}):
                r = analyse(dichte[N], nl, S)
                if r is not None:
                    ana[f"N{N}/S{S}/koord"] = r
    for N, d in intr.items():
        nl = HAUPT_NLISTE if N == HAUPT_N else NEBEN_NLISTE
        for S in sorted({e["S"] for s in d["saaten"].values() for p in s["punkte"] for e in p["je_S"]}):
            for var in ("koord", "intr"):
                r = analyse(d, nl, S, var, tuple(sorted({p["richtung"] for s in d["saaten"].values()
                                                         for p in s["punkte"]})))
                if r is not None:
                    ana[f"intr-lauf/N{N}/S{S}/{var}"] = r
    erg["analyse"] = ana
    haupt = ana.get(f"N{HAUPT_N}/S{HAUPT_S}/koord")
    if haupt is None or not erg["tor"]["bestanden"] or haupt["saaten"] < MIN_SAATEN:
        for nr in ("ID1", "ID2", "ID3"):
            erg["urteile"][nr] = {"urteil": na, "werte": {"tor": erg["tor"]["bestanden"]}}
    else:
        c, se, M = haupt["c"]
        gate = se <= GATE_SE
        # ID1
        u1, w1 = urteil_id1(c, se)
        ck, sek, _ = haupt["c_kmin_kartenwortlaut"]
        u1k, w1k = urteil_id1(ck, sek)
        se_ziel = ID1_TOL * abs(POLYAKOV) / 2
        erg["urteile"]["ID1"] = {"urteil": u1 if gate else na, "werte": {
            "c": c, "se": se, "saaten": M, "polyakov": POLYAKOV, "verhaeltnis": c / POLYAKOV, **w1,
            "gate_unterscheidbar": gate, "saaten_noetig_fuer_se_halbe_toleranz": int(math.ceil(M * (se / se_ziel) ** 2)),
            "kartenwortlaut_kleinstes_k": {"urteil": u1k if gate else na, "c_kmin": ck, "se": sek,
                                           "betrag_kmin": haupt["betrag"][0], **w1k,
                                           "saaten_noetig_fuer_se_halbe_toleranz":
                                               int(math.ceil(M * (sek / se_ziel) ** 2))}}}
        # ID2
        z2 = abs(c - C_FEST_KARTE) / se
        erg["urteile"]["ID2"] = {"urteil": ("eingetroffen" if z2 > ID2_NSE else "nicht eingetroffen") if gate else na,
                                 "werte": {"c": c, "se": se, "abstand_in_se": z2, "referenz": C_FEST_KARTE,
                                           "gate_unterscheidbar": gate}}
        # ID3
        if c + ID3_NSE * se < 0:
            u3 = "eingetroffen"
        elif c - ID3_NSE * se > 0:
            u3 = "nicht eingetroffen"
        else:
            u3 = na
        erg["urteile"]["ID3"] = {"urteil": u3 if gate else na, "werte": {
            "c": c, "se": se, "c_plus_2se": c + 2 * se, "c_minus_2se": c - 2 * se,
            "kartenwortlaut_vorzeichen_negativ": bool(c < 0), "gate_unterscheidbar": gate}}
        erg["flaechenglied_a"] = {"a": haupt["a"], "vorhersage_a_gleich_0_in_se": abs(haupt["a"][0]) / haupt["a"][1]}
    with open(ziel, "w") as f:
        json.dump(erg, f, indent=1)
    for k, v in erg["urteile"].items():
        print(k, v["urteil"], flush=True)
    try:
        bilder(erg, dichte, kontrolle, os.path.dirname(os.path.abspath(ziel)))
    except Exception as ex:  # Bilder sind beschreibend
        print("Bilder fehlgeschlagen:", repr(ex), flush=True)


def bilder(erg, dichte, kontrolle, ordner):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    ana = erg["analyse"]
    farbe = {64000: "tab:green", 16000: "tab:orange"}
    # 1: konforme Steifigkeit/k^2 gegen k
    fig, axs = plt.subplots(1, 2, figsize=(14, 5.5))
    for N in (16000, 64000):
        for S, mk in ((0.5, "o"), (0.25, "^")):
            r = ana.get(f"N{N}/S{S}/koord")
            if r is None:
                continue
            kb = np.array(r["betrag"])
            ym = np.array([x["mittel"] for x in r["y_je_n"]])
            ys = np.array([x["se"] for x in r["y_je_n"]])
            axs[0].errorbar(kb ** 2, ym, yerr=ys, fmt=mk, color=farbe[N], ms=5, capsize=3,
                            label=f"Dichte-Streuung N = {N}, S = {S} ({r['saaten']} Saaten)")
            xx = np.linspace(0, kb.max() ** 2 * 1.05, 50)
            axs[0].plot(xx, r["a"][0] + r["c"][0] * xx, "-", color=farbe[N], lw=0.8, alpha=0.8 if S == 0.5 else 0.4)
            cm = np.array([x["mittel"] for x in r["c_je_n_nach_abzug"]])
            cs = np.array([x["se"] for x in r["c_je_n_nach_abzug"]])
            axs[1].errorbar(kb * (1.0 if S == 0.5 else 1.03), cm, yerr=cs, fmt=mk, color=farbe[N], ms=5, capsize=3,
                            label=f"Dichte-Streuung N = {N}, S = {S}: (y - a)/k^2")
            if S == 0.5:
                axs[1].axhspan(r["c"][0] - r["c"][1], r["c"][0] + r["c"][1], color=farbe[N], alpha=0.15,
                               label=f"Fit-Steigung N = {N}: {r['c'][0]:+.4f} +- {r['c'][1]:.4f}")
    ft = erg.get("fest_tabelle")
    if ft:
        kb = np.array([x["betrag"] for x in ft])
        cg = np.array([x["geo"][0] for x in ft])
        axs[1].plot(kb, cg, "s", mfc="none", color="k", ms=7, label="festes Netz (feste Punkte), N = 64 000")
        axs[0].plot(kb ** 2, cg * kb ** 2, "s", mfc="none", color="k", ms=7, label="festes Netz: c k^2")
    xx = np.linspace(0, 0.095, 50)
    axs[0].plot(xx, C_FEST_KARTE * xx, ":", color="k", lw=1, label="+0,159 k^2 (festes Netz)")
    axs[0].plot(xx, POLYAKOV * xx, "-", color="r", lw=1.5, label="Polyakov -k^2/(24 pi)")
    axs[0].axhline(0, color="0.6", lw=0.6)
    axs[0].set_xlabel("k^2")
    axs[0].set_ylabel("y = Gamma''/A (Saatmittel +- SE)")
    axs[0].set_title("Gamma''/Flaeche gegen k^2: Achsenabschnitt = Flaechenglied, Steigung = Steifigkeit", fontsize=9)
    axs[0].legend(fontsize=6.5)
    axs[1].axhline(POLYAKOV, color="r", lw=1.5, label="Polyakov -1/(24 pi)")
    axs[1].axhline(C_FEST_KARTE, color="k", lw=0.8, ls=":", label="+0,159 (INDUZIERT-ZUFALL-2D)")
    axs[1].axhline(0, color="0.6", lw=0.6)
    axs[1].set_xscale("log")
    axs[1].set_xlabel("abs(k) (mittlerer Abstand 1)")
    axs[1].set_ylabel("konforme Steifigkeit / (Flaeche k^2)")
    axs[1].set_title("Steifigkeit/k^2 gegen k nach Abzug des Flaechenglieds (a je Saat)", fontsize=9)
    axs[1].legend(fontsize=6.5)
    fig.suptitle("INDUZIERT-DICHTE-2D: Punkte nach physikalischer Flaeche gestreut, neu vernetzt (Koordinaten-Delaunay)")
    fig.tight_layout()
    fig.savefig(f"{ordner}/bild-konform.png", dpi=110)
    plt.close(fig)
    # 2: Saatstreuung
    fig, axs = plt.subplots(1, 2, figsize=(14, 5))
    for i, N in enumerate((64000, 16000)):
        r = ana.get(f"N{N}/S0.5/koord")
        if r is None:
            continue
        c = np.array(r["c_je_saat"])
        axs[0].hist(c, bins=25, alpha=0.5, color=farbe[N], label=f"N = {N}: c je Saat (Std {np.std(c, ddof=1):.3f})")
        axs[0].axvline(np.mean(c), color=farbe[N], lw=1.5)
        ys = np.array(r["y_std_je_n"])
        axs[1].plot(r["betrag"], ys, "o-", color=farbe[N], label=f"N = {N}: Std von y je Saat (S = 0,5)")
        r2 = ana.get(f"N{N}/S0.25/koord")
        if r2 is not None:
            axs[1].plot(r2["betrag"], r2["y_std_je_n"], "^--", color=farbe[N], label=f"N = {N}: S = 0,25")
    axs[0].axvline(POLYAKOV, color="r", lw=1.5, label="Polyakov")
    axs[0].axvline(C_FEST_KARTE, color="k", ls=":", label="+0,159")
    axs[0].set_xlabel("c (Steigung von y gegen k^2, je Saat)")
    axs[0].legend(fontsize=7)
    axs[1].set_xlabel("abs(k)")
    axs[1].set_ylabel("Standardabweichung von y ueber Saaten")
    axs[1].set_xscale("log")
    axs[1].legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(f"{ordner}/bild-streuung.png", dpi=110)
    plt.close(fig)
    # 3: Kantenkippen gegen s
    fig, axs = plt.subplots(1, 2, figsize=(14, 5))
    k5 = kontrolle.get("K5_kippen", [])
    for N in sorted({x["N"] for x in k5}):
        for n in sorted({x["n"] for x in k5 if x["N"] == N}):
            z = [x for x in k5 if x["N"] == N and x["n"] == n]
            s = np.array([x["s"] for x in z])
            axs[0].loglog(s, [x["koord_neu"] / x["E"] for x in z], "o-", ms=4,
                          label=f"N = {N}, abs(k) = {z[0]['betrag']:.3f}: neue Kanten/E")
            axs[1].loglog(s, [max(x["koord_negativ"], 0.5) / x["E"] for x in z], "o-", ms=4,
                          label=f"N = {N}, abs(k) = {z[0]['betrag']:.3f}: Koordinaten-Netz")
            axs[1].loglog(s, [max(x["intr"]["rest_negativ"], 0.5) / x["E"] for x in z], "x:", ms=5,
                          label=f"N = {N}, abs(k) = {z[0]['betrag']:.3f}: nach Kippen")
    axs[0].set_xlabel("s")
    axs[0].set_ylabel("Anteil der Kanten, die gegenueber s = 0 neu sind")
    axs[0].set_title("Kantenkippen gegen s (Koordinaten-Delaunay der Bildpunkte)", fontsize=9)
    axs[0].legend(fontsize=6)
    axs[1].set_xlabel("s")
    axs[1].set_ylabel("Anteil negativer Kotangens-Gewichte (physikalische Laengen); 0 als 0,5 gezeichnet")
    axs[1].set_title("Abweichung vom Delaunay in der physikalischen Metrik", fontsize=9)
    axs[1].legend(fontsize=6)
    fig.tight_layout()
    fig.savefig(f"{ordner}/bild-kippen.png", dpi=110)
    plt.close(fig)


if __name__ == "__main__":
    main()
