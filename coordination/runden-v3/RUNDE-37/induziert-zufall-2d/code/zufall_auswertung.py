#!/usr/bin/env python3
"""INDUZIERT-ZUFALL-2D (Runde 38): Auswertung, Urteile nach PLAN.md Abschnitt 6, Bilder.

Aufruf: python zufall_auswertung.py <datenordner> <aus.json>
Erwartet im Datenordner: kontrolle.json, regulaer-L256.json (IZ0, Tor), optional regulaer-L64.json und
regulaer-L128.json, zufall-N<N>-*.json (Saatbloecke; alle Dateien je N werden zusammengefuehrt).
"""
import glob
import json
import math
import os
import sys

import numpy as np

POLYAKOV = -1.0 / (24.0 * math.pi)
# IZ0: Referenz aus INDUZIERT-1 lauf-69/teilA.json, L = 256, achse_10, n = 2 (abs(k) = 0,0491), c_P_eckenskalierung
IZ0_REF = 0.12492171825863749
IZ0_KARTE = 0.1249
IZ0_TOL_REL = 1e-3
IZ1_N, IZ1_n, IZ1_RICHT, IZ1_TOL = 64000, 2, ("r000", "r090"), 0.20
IZ2_N, IZ2_n, IZ2_TOL = 64000, 2, 0.05
IZ3_N, IZ3_n, IZ3_TOL = 64000, 2, 0.10
IZ4_n = {4000: 1, 16000: 2, 64000: 4}            # gleiches abs(k) = 2 pi/sqrt(4000) = 0,0993 auf den Achsen
IZ4_RICHT, IZ4_ZIEL, IZ4_TOL = ("r000", "r090"), -0.5, 0.15
TOR_FD_REL = 1e-4
TOR_LOGDET_REL = 1e-9
RICHT = ("r000", "r045", "r090", "r135")
WINKEL = {"r000": 0, "r045": 45, "r090": 90, "r135": 135}


def lade(ordner):
    def j(name):
        p = os.path.join(ordner, name)
        if not os.path.exists(p):
            return None
        with open(p) as f:
            return json.load(f)

    kontrolle = j("kontrolle.json")
    regulaer = {}
    for L in (64, 128, 256):
        r = j(f"regulaer-L{L}.json")
        if r is not None:
            regulaer[L] = r
    zufall = {}
    for p in sorted(glob.glob(os.path.join(ordner, "zufall-N*.json"))):
        with open(p) as f:
            d = json.load(f)
        N = int(d["N"])
        zufall.setdefault(N, {"saaten": {}, "dateien": []})
        zufall[N]["dateien"].append(os.path.basename(p))
        for s in d["saaten"]:
            if s["saat"] in zufall[N]["saaten"]:
                raise SystemExit(f"Saat {s['saat']} bei N = {N} doppelt")
            zufall[N]["saaten"][s["saat"]] = s
    return kontrolle, regulaer, zufall


def wert(s, richtung, n, feld):
    for p in s["punkte"]:
        if p["richtung"] == richtung and p["n"] == n:
            teile = feld.split(".")
            x = p
            for t in teile:
                if t not in x:
                    return None
                x = x[t]
            return x
    return None


def mittel_sem(x):
    x = np.asarray([v for v in x if v is not None], dtype=float)
    if x.size == 0:
        return None, None, 0
    if x.size == 1:
        return float(x[0]), None, 1
    return float(np.mean(x)), float(np.std(x, ddof=1) / math.sqrt(x.size)), int(x.size)


def tor_pruefen(kontrolle, regulaer, zufall):
    t = {"netze": {}, "lu": {}, "logdet": {}, "fd": {}}
    ok = True
    for N, z in zufall.items():
        schlecht = []
        for saat, s in z["saaten"].items():
            p = s["pruefung"]
            gut = (p["euler"] == 0 and p["kanten_genau_zwei"] and p["ecken_verschieden"] and p["orient_min"] > 0
                   and p["flaeche_summe_rel_abw"] <= 1e-9 and p["delaunay_verletzt_1e-9"] == 0
                   and p["l_max_durch_L"] < 0.25 and p["E"] == 3 * p["V"] and p["F"] == 2 * p["V"])
            lu = s["lu"]
            gut_lu = lu["neg_U"] == 0 and lu["perm_ungleich"] == 0 and lu["min_U"] > 0
            if not (gut and gut_lu):
                schlecht.append(saat)
        t["netze"][str(N)] = {"saaten": len(z["saaten"]), "mit_fehler": schlecht}
        ok = ok and not schlecht
    k2 = kontrolle["K2_regulaer_L16"]
    rel = [k2["gamma_abw"] / abs(k2["gamma_lu"])]
    for x in kontrolle["K3_logdet"]:
        rel += [x["abw_slogdet"] / abs(x["gamma_lu"]), x["abw_eigen"] / abs(x["gamma_lu"])]
    t["logdet"] = {"max_rel": float(max(rel)), "schwelle": TOR_LOGDET_REL,
                   "matrix_regulaer_max_abs": k2["matrix_max_abs"]}
    ok = ok and max(rel) <= TOR_LOGDET_REL
    fd = [max(x["rel_konform"], x["rel_laengs"], x["rel_quer"]) for x in kontrolle["K4_fd_gegen_blase"]]
    fd_l = {}
    for L, r in regulaer.items():
        m = 0.0
        for p in r["punkte"]:
            ex = p["exakt"]
            m = max(m, abs(p["konform"]["gamma2"] / ex["gamma2_konform"] - 1),
                    abs(p["versch_laengs"]["gamma2"] / ex["gamma2_versch_laengs"] - 1),
                    abs(p["versch_quer"]["gamma2"] / ex["gamma2_versch_quer"] - 1))
        fd_l[str(L)] = m
    t["fd"] = {"K4_max_rel": float(max(fd)), "regulaer_max_rel": fd_l, "schwelle": TOR_FD_REL}
    ok = ok and max(fd) <= TOR_FD_REL and all(v <= TOR_FD_REL for v in fd_l.values()) and 256 in regulaer
    t["bestanden"] = bool(ok)
    return t


def steigung(Ns, sig):
    x = np.log(np.asarray(Ns, dtype=float))
    y = np.log(np.asarray(sig, dtype=float))
    return float(np.polyfit(x, y, 1)[0])


def main():
    ordner, ziel = sys.argv[1], sys.argv[2]
    kontrolle, regulaer, zufall = lade(ordner)
    erg = {"urteile": {}, "polyakov": POLYAKOV}
    tor = tor_pruefen(kontrolle, regulaer, zufall)
    erg["tor"] = tor
    na = "nicht auswertbar"

    # ---------------- IZ0
    r256 = regulaer.get(256)
    p0 = None
    if r256 is not None:
        p0 = [p for p in r256["punkte"] if p["richtung"] == "r000" and p["n"] == 2]
    if not p0:
        erg["urteile"]["IZ0"] = {"urteil": na, "werte": {}}
    else:
        c = p0[0]["konform"]["c_P"]
        rel = abs(c / IZ0_REF - 1)
        erg["urteile"]["IZ0"] = {
            "urteil": "eingetroffen" if rel <= IZ0_TOL_REL else "nicht eingetroffen",
            "werte": {"c_P_regulaer_L256_r000_n2": c, "referenz_INDUZIERT1": IZ0_REF, "rel_abw": rel,
                      "c_P_exakt_blase": p0[0]["exakt"]["c_P"],
                      "kartenwortlaut_abs_abw_zu_0_1249": abs(c - IZ0_KARTE),
                      "kartenwortlaut_eingetroffen": abs(c - IZ0_KARTE) <= 1e-3}}

    # ---------------- Tabellen je N
    tab = {}
    for N, z in sorted(zufall.items()):
        saaten = list(z["saaten"].values())
        ns = sorted({p["n"] for s in saaten for p in s["punkte"]})
        tN = {"saaten": len(saaten), "dateien": z["dateien"], "punkte": []}
        for r in RICHT:
            for n in ns:
                zeile = {"richtung": r, "n": n}
                bet = [wert(s, r, n, "betrag") for s in saaten]
                zeile["betrag"] = bet[0]
                for feld, name in (("konform.c_P", "c_P"), ("konform.c_D", "c_D"), ("konform.kappa", "kappa_konf"),
                                   ("versch_laengs.c", "c_laengs"), ("versch_quer.c", "c_quer"),
                                   ("versch_laengs.kappa", "kappa_laengs"), ("versch_quer.kappa", "kappa_quer"),
                                   ("versch_laengs.verhaeltnis_zu_konform", "verh_laengs"),
                                   ("versch_quer.verhaeltnis_zu_konform", "verh_quer"),
                                   ("konform.gamma1", "gamma1_konf"),
                                   ("konform.richardson_abw_rel", "richardson_konf")):
                    vals = [wert(s, r, n, feld) for s in saaten]
                    m, e, k = mittel_sem(vals)
                    zeile[name] = {"mittel": m, "sem": e, "anzahl": k}
                    if name in ("c_P", "c_D") and k > 1:
                        v = np.array([x for x in vals if x is not None], float)
                        zeile[name]["std"] = float(np.std(v, ddof=1))
                tN["punkte"].append(zeile)
        tab[str(N)] = tN
    erg["tabellen"] = tab

    def saatwerte(N, richt, n, feld="konform.c_P"):
        out = []
        for s in zufall[N]["saaten"].values():
            v = [wert(s, r, n, feld) for r in richt]
            if all(x is not None for x in v):
                out.append(float(np.mean(v)))
        return np.array(out)

    # PLAN Abschnitt 6: mindestens 8 Saaten bei N = 64 000, sonst IZ1 bis IZ4 nicht auswertbar
    erg["saaten_64000"] = len(zufall[64000]["saaten"]) if 64000 in zufall else 0
    auswertbar = tor["bestanden"] and erg["saaten_64000"] >= 8
    # ---------------- IZ1
    if not auswertbar or IZ1_N not in zufall:
        erg["urteile"]["IZ1"] = {"urteil": na, "werte": {"tor": tor["bestanden"]}}
    else:
        v = saatwerte(IZ1_N, IZ1_RICHT, IZ1_n)
        c = float(np.mean(v))
        v4 = saatwerte(IZ1_N, RICHT, IZ1_n)
        rel = abs(c / POLYAKOV - 1)
        L = math.sqrt(IZ1_N)
        erg["urteile"]["IZ1"] = {
            "urteil": "eingetroffen" if rel <= IZ1_TOL else "nicht eingetroffen",
            "werte": {"c_P_saatmittel": c, "sem": float(np.std(v, ddof=1) / math.sqrt(v.size)),
                      "saaten": int(v.size), "betrag_k": 2 * math.pi * IZ1_n / L, "polyakov": POLYAKOV,
                      "verhaeltnis_zu_polyakov": c / POLYAKOV, "rel_abw": rel,
                      "vier_richtungen_mittel": float(np.mean(v4)),
                      "vier_richtungen_rel_abw": abs(float(np.mean(v4)) / POLYAKOV - 1)}}
    # ---------------- IZ2
    if not auswertbar or IZ2_N not in zufall:
        erg["urteile"]["IZ2"] = {"urteil": na, "werte": {}}
    else:
        mitt, sems = [], []
        for r in RICHT:
            v = saatwerte(IZ2_N, (r,), IZ2_n)
            mitt.append(float(np.mean(v)))
            sems.append(float(np.std(v, ddof=1) / math.sqrt(v.size)))
        mitt, sems = np.array(mitt), np.array(sems)
        mm = float(np.mean(mitt))
        streu = float(np.std(mitt, ddof=1) / abs(mm))
        rausch = float(math.sqrt(np.mean(sems ** 2)) / abs(mm))
        chi2 = float(np.sum(((mitt - np.average(mitt, weights=1 / sems ** 2)) / sems) ** 2))
        if rausch > IZ2_TOL:
            u = na
        else:
            u = "eingetroffen" if streu <= IZ2_TOL else "nicht eingetroffen"
        erg["urteile"]["IZ2"] = {"urteil": u, "werte": {
            "richtungsmittel": dict(zip(RICHT, mitt.tolist())), "sem": dict(zip(RICHT, sems.tolist())),
            "mittel": mm, "streuung_std_ddof1_rel": streu, "spanne_rel": float((mitt.max() - mitt.min()) / abs(mm)),
            "rauschen_rel": rausch, "chi2_3fg": chi2}}
    # ---------------- IZ3
    if not auswertbar or IZ3_N not in zufall:
        erg["urteile"]["IZ3"] = {"urteil": na, "werte": {}}
    else:
        verh, verh_sig = {}, {}
        for r in RICHT:
            kc = float(np.mean(saatwerte(IZ3_N, (r,), IZ3_n, "konform.kappa")))
            for m in ("versch_laengs", "versch_quer"):
                km = float(np.mean(saatwerte(IZ3_N, (r,), IZ3_n, m + ".kappa")))
                verh[f"{r}/{m}"] = abs(km) / abs(kc)
                verh_sig[f"{r}/{m}"] = km / abs(kc)
        R = max(verh.values())
        erg["urteile"]["IZ3"] = {"urteil": "eingetroffen" if R <= IZ3_TOL else "nicht eingetroffen",
                                 "werte": {"max_verhaeltnis": R, "verhaeltnisse": verh,
                                           "min_verhaeltnis": min(verh.values()),
                                           "kartenwortlaut_vorzeichen_max": max(verh_sig.values()),
                                           "kartenwortlaut_eingetroffen": max(verh_sig.values()) <= IZ3_TOL}}
    # ---------------- IZ4
    if not auswertbar or not all(N in zufall for N in IZ4_n):
        erg["urteile"]["IZ4"] = {"urteil": na, "werte": {}}
    else:
        Ns, sig, mitt, anz, werte_n = [], [], [], [], {}
        for N, n in sorted(IZ4_n.items()):
            v = saatwerte(N, IZ4_RICHT, n)
            Ns.append(N)
            sig.append(float(np.std(v, ddof=1)))
            mitt.append(float(np.mean(v)))
            anz.append(int(v.size))
            werte_n[N] = v
        b = steigung(Ns, sig)
        rng = np.random.default_rng(4)
        boot = []
        for _ in range(4000):
            sb = [float(np.std(rng.choice(werte_n[N], size=werte_n[N].size, replace=True), ddof=1)) for N in Ns]
            if min(sb) > 0:
                boot.append(steigung(Ns, sb))
        boot = np.array(boot)
        erg["urteile"]["IZ4"] = {"urteil": "eingetroffen" if abs(b - IZ4_ZIEL) <= IZ4_TOL else "nicht eingetroffen",
                                 "werte": {"N": Ns, "std": sig, "mittel": mitt, "saaten": anz, "steigung": b,
                                           "betrag_k": 2 * math.pi / math.sqrt(4000),
                                           "bootstrap_68": [float(np.percentile(boot, 16)),
                                                            float(np.percentile(boot, 84))],
                                           "bootstrap_95": [float(np.percentile(boot, 2.5)),
                                                            float(np.percentile(boot, 97.5))],
                                           "std_rel": [s / abs(m) for s, m in zip(sig, mitt)]}}
    # ---------------- beschreibend: Streuung bei kleinstem n je N (alle vier Richtungen)
    besch = {}
    for N in sorted(zufall):
        ns = sorted({p["n"] for s in zufall[N]["saaten"].values() for p in s["punkte"]})
        for n in ns:
            v = saatwerte(N, RICHT, n)
            if v.size > 1:
                besch[f"N{N}/n{n}"] = {"mittel_4richt": float(np.mean(v)), "std": float(np.std(v, ddof=1)),
                                       "saaten": int(v.size), "betrag_achse": 2 * math.pi * n / math.sqrt(N)}
    erg["beschreibend_streuung_4richtungen"] = besch
    # ---------------- regelmaessiges Netz
    erg["regulaer"] = {}
    for L, r in sorted(regulaer.items()):
        erg["regulaer"][str(L)] = [{"richtung": p["richtung"], "n": p["n"], "betrag": p["betrag"],
                                    "c_P": p["konform"]["c_P"], "c_P_exakt": p["exakt"]["c_P"],
                                    "c_D": p["konform"]["c_D"], "c_laengs": p["versch_laengs"]["c"],
                                    "c_quer": p["versch_quer"]["c"],
                                    "verh_laengs": p["versch_laengs"]["verhaeltnis_zu_konform"],
                                    "verh_quer": p["versch_quer"]["verhaeltnis_zu_konform"]}
                                   for p in r["punkte"]]
    with open(ziel, "w") as f:
        json.dump(erg, f, indent=1)
    for k, v in erg["urteile"].items():
        print(k, v["urteil"], flush=True)
    try:
        bilder(erg, zufall, regulaer, os.path.dirname(os.path.abspath(ziel)))
    except Exception as ex:  # Bilder sind beschreibend; Urteile stehen schon in der Datei
        print("Bilder fehlgeschlagen:", repr(ex), flush=True)


def bilder(erg, zufall, regulaer, ordner):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    tab = erg["tabellen"]
    farbe = {4000: "tab:blue", 16000: "tab:orange", 64000: "tab:green"}
    reg = regulaer.get(256)
    # 1: konforme Steifigkeit gegen abs(k)
    fig, axs = plt.subplots(1, 2, figsize=(14, 5.5))
    for ax, feld, titel in ((axs[0], "c_P", "c_P: 1/2 log det' K, Ecken-Skalierung (gewertet)"),
                            (axs[1], "c_D", "c_D: det'(M^-1 K) ohne Flaechenglied (beschreibend)")):
        for N in sorted(zufall):
            pk = tab[str(N)]["punkte"]
            for r in RICHT:
                z = [p for p in pk if p["richtung"] == r]
                ax.errorbar([p["betrag"] for p in z], [p[feld]["mittel"] for p in z],
                            yerr=[p[feld]["sem"] or 0 for p in z], fmt="o-" if r == "r000" else ".",
                            color=farbe.get(N, "k"), alpha=1.0 if r == "r000" else 0.5, ms=4, lw=1,
                            label=f"Zufall N = {N} ({len(zufall[N]['saaten'])} Saaten)" if r == "r000" else None)
        if reg is not None:
            for r, mk in zip(RICHT, ("s", "^", "s", "v")):
                z = [p for p in reg["punkte"] if p["richtung"] == r]
                ax.plot([p["betrag"] for p in z], [p["konform"][feld] for p in z], mk, mfc="none", color="k",
                        ms=6, label=f"regelmaessig L = 256, {WINKEL[r]} Grad")
        ax.axhline(POLYAKOV, color="r", lw=1.5, label="Polyakov -1/(24 pi)")
        ax.axhline(0, color="0.6", lw=0.6)
        ax.set_xscale("log")
        ax.set_xlabel("abs(k) (mittlerer Abstand 1)")
        ax.set_ylabel("Steifigkeit / (Flaeche k^2)")
        ax.set_title(titel, fontsize=9)
        ax.legend(fontsize=6.5)
    fig.suptitle("INDUZIERT-ZUFALL-2D: konforme Mode, Saatmittel +- Standardfehler (Punkte: 45/90/135 Grad)")
    fig.tight_layout()
    fig.savefig(f"{ordner}/bild-konform.png", dpi=110)
    plt.close(fig)
    # 2: Richtungsabhaengigkeit
    fig, axs = plt.subplots(1, 2, figsize=(14, 5))
    for ax, N, n in ((axs[0], 64000, 2), (axs[1], 16000, 1)):
        if N not in zufall:
            continue
        for i, r in enumerate(RICHT):
            v = [wert(s, r, n, "konform.c_P") for s in zufall[N]["saaten"].values()]
            ax.plot(np.full(len(v), i) + np.linspace(-0.15, 0.15, len(v)), v, ".", color=farbe[N], alpha=0.6)
            m, e, _ = mittel_sem(v)
            ax.errorbar([i + 0.25], [m], yerr=[e], fmt="o", color="k", capsize=4)
        if reg is not None:
            for i, r in enumerate(RICHT):
                z = [p for p in reg["punkte"] if p["richtung"] == r and p["n"] == min(2, n * 2)]
                if z:
                    ax.plot([i - 0.3], [z[0]["konform"]["c_P"]], "s", mfc="none", color="r", ms=8)
        ax.set_xticks(range(4))
        ax.set_xticklabels([f"{WINKEL[r]} Grad" for r in RICHT])
        ax.set_ylabel("c_P")
        ax.set_title(f"N = {N}, n = {n}: Saaten (Punkte), Mittel +- SEM (schwarz), regelmaessig (rote Quadrate)",
                     fontsize=9)
    fig.tight_layout()
    fig.savefig(f"{ordner}/bild-richtung.png", dpi=110)
    plt.close(fig)
    # 3: Streuung gegen N
    iz4 = erg["urteile"].get("IZ4", {}).get("werte", {})
    if iz4.get("N"):
        fig, ax = plt.subplots(figsize=(7, 5))
        Ns, sig = np.array(iz4["N"], float), np.array(iz4["std"], float)
        ax.loglog(Ns, sig, "o", color="k", label="Std. ueber Saaten, abs(k) = 0,0993, Achsenmittel")
        b = iz4["steigung"]
        xx = np.geomspace(Ns.min() * 0.8, Ns.max() * 1.25, 20)
        c0 = np.exp(np.mean(np.log(sig) - b * np.log(Ns)))
        ax.loglog(xx, c0 * xx ** b, "-", color="k", lw=1, label=f"Fit: Steigung {b:.3f}")
        c1 = np.exp(np.mean(np.log(sig) + 0.5 * np.log(Ns)))
        ax.loglog(xx, c1 * xx ** -0.5, "--", color="r", lw=1, label="N^(-1/2)")
        for key, v in erg.get("beschreibend_streuung_4richtungen", {}).items():
            N = int(key.split("/")[0][1:])
            n = int(key.split("/")[1][1:])
            if n == 1:
                ax.loglog([N], [v["std"]], "x", color=farbe.get(N, "0.5"),
                          label=f"n = 1, Mittel ueber 4 Richtungen (N = {N})")
        ax.set_xlabel("N")
        ax.set_ylabel("Streuung von c_P ueber Saaten")
        ax.legend(fontsize=7)
        fig.tight_layout()
        fig.savefig(f"{ordner}/bild-streuung.png", dpi=110)
        plt.close(fig)
    # 4: Knotenverschiebungen
    fig, axs = plt.subplots(1, 2, figsize=(14, 5.5))
    for N in sorted(zufall):
        pk = tab[str(N)]["punkte"]
        for m, mk in (("laengs", "o"), ("quer", "^")):
            z = [p for p in pk if p[f"c_{m}"]["mittel"] is not None]
            axs[0].errorbar([p["betrag"] for p in z], [p[f"c_{m}"]["mittel"] for p in z],
                            yerr=[p[f"c_{m}"]["sem"] or 0 for p in z], fmt=mk, color=farbe.get(N, "k"), ms=4,
                            alpha=0.7, label=f"N = {N}, {m}")
            axs[1].loglog([p["betrag"] for p in z], [abs(p[f"verh_{m}"]["mittel"]) for p in z], mk,
                          color=farbe.get(N, "k"), ms=4, alpha=0.7, label=f"N = {N}, {m}")
        z = [p for p in pk if p["c_P"]["mittel"] is not None]
        axs[0].plot([p["betrag"] for p in z], [p["c_P"]["mittel"] for p in z], "x", color=farbe.get(N, "k"), ms=5,
                    label=f"N = {N}, konform c_P")
    if reg is not None:
        for m, mk in (("laengs", "s"), ("quer", "D")):
            axs[0].plot([p["betrag"] for p in reg["punkte"]], [p[f"versch_{m}"]["c"] for p in reg["punkte"]], mk,
                        mfc="none", color="k", ms=6, label=f"regelmaessig L = 256, {m}")
            axs[1].loglog([p["betrag"] for p in reg["punkte"]],
                          [abs(p[f"versch_{m}"]["verhaeltnis_zu_konform"]) for p in reg["punkte"]], mk, mfc="none",
                          color="k", ms=6, label=f"regelmaessig L = 256, {m}")
    axs[1].axhline(IZ3_TOL, color="r", lw=1.2, label="Schwelle IZ3 (0,1)")
    axs[0].set_xscale("log")
    axs[0].set_xlabel("abs(k)")
    axs[0].set_ylabel("Gamma''/(k^2 A) je Amplitude^2")
    axs[0].set_title("Knotenverschiebung xi = s e cos(k.x): Steifigkeit je Amplitude", fontsize=9)
    axs[1].set_xlabel("abs(k)")
    axs[1].set_ylabel("abs(kappa_versch)/abs(kappa_konform), je Kantenlaengen-Norm")
    axs[1].set_title("gleiche Kantenlaengen-Norm: Verschiebung gegen konforme Mode", fontsize=9)
    axs[0].legend(fontsize=6.5)
    axs[1].legend(fontsize=6.5)
    fig.tight_layout()
    fig.savefig(f"{ordner}/bild-verschiebung.png", dpi=110)
    plt.close(fig)


if __name__ == "__main__":
    main()
