#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GUERTEL-FELD-STAB-1: mechanische Auswertung (PLAN.md, Abschnitt Urteilsregeln) und Bild (PNG).

Liest lauf/prot.json, lauf/stoss-T*-e*.json und die N1-Datei aus GUERTEL-2; schreibt auswertung.json und
energie-verlauf.png. Fehlt eine Datei, lautet das betroffene Urteil "nicht auswertbar".
Aufruf nur ueber kleintest.sh auf der .69.
"""
import argparse
import hashlib
import json
import os
import time

THETAS = [420, 450]          # Vorgabe; per --thetas aenderbar (nur Rauchlauf)
EPS = [0.01, 0.1, 0.3]       # Vorgabe; per --eps aenderbar (nur Rauchlauf)
REFS = {420: 300, 450: 270}   # theta -> 720 - theta; per --refs aenderbar (nur Rauchlauf)
TOL_GS0 = 1.0e-6          # GS0: Energie auf 1e-6 relativ
RHO_UM = 0.10             # Plan: umgekehrt, wenn rho <= 0,10 (und Drehsinn aussen umgekehrt)
RHO_AST = 0.90            # Plan: Ast, wenn rho >= 0,90 und Kipp-Amplitude am Ende <= nach dem Stoss
WORT_BAND = 0.10          # Wortlaut: "etwa" = innerhalb 10 % von E(720 - theta) bzw. von E_Ast


def sha_datei(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def lade(p):
    if not os.path.exists(p):
        return None
    with open(p) as f:
        return json.load(f)


def idx(liste, wert):
    for i, v in enumerate(liste):
        if v is not None and abs(v - wert) < 1e-9:
            return i
    return None


def gs0(prot, n1):
    if prot is None or n1 is None:
        return {"plan": "nicht auswertbar", "wort": "nicht auswertbar", "grund": "Datei fehlt", "werte": []}
    werte = []
    for art, th in (("schritt", 420.0), ("schritt", 450.0), ("gitter", 450.0)):
        tk, ek, sk = (("theta_schritt", "E_schritt", "sonde_schritt") if art == "schritt"
                      else ("gitter", "E_gitter", "sonde_gitter"))
        i1 = idx(n1["protokoll"][tk], th)
        i2 = idx(prot["protokoll"][tk], th)
        if i1 is None or i2 is None:
            return {"plan": "nicht auswertbar", "wort": "nicht auswertbar", "grund": "Winkel fehlt", "werte": werte}
        E1 = n1["protokoll"][ek][i1]
        E2 = prot["protokoll"][ek][i2]
        werte.append({"art": art, "theta": th, "E_N1": E1, "E_neu": E2, "rel": abs(E2 - E1) / abs(E1),
                      "sonde_N1": n1["protokoll"][sk][i1], "sonde_neu": prot["protokoll"][sk][i2]})
    wort = all(w["rel"] <= TOL_GS0 for w in werte)
    plan = wort and all(w["sonde_neu"] > 0.0 for w in werte)
    return {"plan": "eingetroffen" if plan else "nicht eingetroffen",
            "wort": "eingetroffen" if wort else "nicht eingetroffen", "werte": werte}


def ref_wert(lauf, theta_ref):
    r = lade(os.path.join(lauf, "stoss-T%d-e0.json" % theta_ref))
    if r is None:
        return None, {"theta": theta_ref, "fehlt": True}
    info = {"theta": theta_ref, "E_vor": r["E_vor"], "E_end": r["E_end"], "sonde_lauf": r["sonde_lauf"],
            "fmax_end": r["fmax_end"], "schritte": r["schritte"],
            "qz_mittel_aussen_end": r["struktur_end"]["qz_mittel_aussen"]}
    if not (r["sonde_lauf"] > 0.0 and r["E_end"] > 0.0):
        info["ungueltig"] = True
        return None, info
    return r["E_end"], info


def klasse(run, E_ref):
    """Je Lauf: Klasse nach Plan und nach Wortlaut (PLAN.md)."""
    E_end = run["E_end"]
    E_ast = run["E_vor"]
    rho = (E_end - E_ref) / (E_ast - E_ref)
    P = run["verlauf"]["kipp"]
    P0, Pend = P[0], P[-1]
    qz = run["struktur_end"]["qz_mittel_aussen"]
    sprung = not (run["sonde_lauf"] > 0.0)
    if sprung:
        kp = "sprung"
    elif rho <= RHO_UM and qz < 0.0:
        kp = "umgekehrt"
    elif rho >= RHO_AST and Pend <= P0:
        kp = "ast"
    else:
        kp = "dazwischen"
    if sprung:
        kw = "sprung"
    elif abs(E_end - E_ref) <= WORT_BAND * E_ref:
        kw = "umgekehrt"
    elif abs(E_end - E_ast) <= WORT_BAND * E_ast:
        kw = "ast"
    else:
        kw = "dazwischen"
    S = run["verlauf"]["sonde"]
    erster_sprung = next((k for k, s in enumerate(S) if not (s > 0.0)), None)
    E = run["verlauf"]["E"]
    return {"theta": run["theta"], "eps": run["eps"], "klasse_plan": kp, "klasse_wort": kw, "rho": rho,
            "E_vor": E_ast, "E_nach_stoss": run["E_nach_stoss"], "E_end": E_end, "E_ref": E_ref,
            "E_end_durch_E_ref": E_end / E_ref, "E_min_lauf": min(E),
            "sonde_nach_stoss": run["sonde_nach_stoss"], "sonde_end": run["sonde_end"],
            "sonde_lauf": run["sonde_lauf"], "erster_sprung_schritt": erster_sprung,
            "fmax_end": run["fmax_end"], "schritte": run["schritte"],
            "kipp_P0": P0, "kipp_Pend": Pend, "kipp_Pmax": max(P), "kipp_Pmax_schritt": int(P.index(max(P))),
            "qz_mittel_aussen_vor": run["struktur_vor"]["qz_mittel_aussen"],
            "qz_mittel_aussen_end": qz, "q0_min_frei_end": run["struktur_end"]["q0_min_frei"],
            "E_bei": {str(k): E[k] for k in (0, 250, 500, 1000, 1500, 2000, 2500, 3000) if k < len(E)}}


def urteil(klassen):
    if any(k is None for k in klassen):
        return "nicht auswertbar"
    if all(k == "umgekehrt" for k in klassen):
        return "eingetroffen"
    if any(k in ("sprung", "ast") for k in klassen):
        return "nicht eingetroffen"
    return "nicht entschieden"


def bild(lauf, aus, refs):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    surface, ink, ink2, grid = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df"
    farben = {0.0: "#8a8984", 0.01: "#2a78d6", 0.1: "#eb6834", 0.3: "#1baf7a"}
    plt.rcParams.update({"font.size": 10, "axes.edgecolor": ink2, "axes.labelcolor": ink, "xtick.color": ink2,
                         "ytick.color": ink2, "text.color": ink})
    fig, ax = plt.subplots(3, 2, figsize=(12, 10.5), sharex=True, facecolor=surface)
    for j, th in enumerate(THETAS):
        for eps in [0.0] + EPS:
            r = lade(os.path.join(lauf, "stoss-T%d-e%g.json" % (th, eps)))
            if r is None:
                continue
            v = r["verlauf"]
            n = list(range(len(v["E"])))
            lab = "ohne Stoss (eps = 0)" if eps == 0.0 else "eps = %g" % eps
            ax[0, j].plot(n, v["E"], color=farben[eps], lw=2, label=lab)
            ax[1, j].plot(n, v["sonde"], color=farben[eps], lw=2, label=lab)
            ax[2, j].plot(n, [max(p, 1e-12) for p in v["kipp"]], color=farben[eps], lw=2, label=lab)
            k = next((i for i, s in enumerate(v["sonde"]) if not (s > 0.0)), None)
            if k is not None:
                for row, yy in ((0, v["E"][k]), (1, v["sonde"][k])):
                    ax[row, j].plot([k], [yy], marker="X", ms=10, color=farben[eps], mec=surface, mew=1.5)
        Eref = refs.get(REFS[th])
        if Eref is not None:
            ax[0, j].axhline(Eref, color=ink2, ls="--", lw=1)
            ax[0, j].annotate("E(720 - theta) = E(%d) = %.0f" % (REFS[th], Eref), (0.99, Eref),
                              xycoords=("axes fraction", "data"), ha="right", va="bottom", color=ink2, fontsize=9)
        r0 = lade(os.path.join(lauf, "stoss-T%d-e0.json" % th))
        if r0 is not None:
            ax[0, j].axhline(r0["E_vor"], color=ink2, ls=":", lw=1)
            ax[0, j].annotate("Ast bei %d Grad (Start) = %.0f" % (th, r0["E_vor"]), (0.99, r0["E_vor"]),
                              xycoords=("axes fraction", "data"), ha="right", va="top", color=ink2, fontsize=9)
        ax[1, j].axhline(0.0, color=ink2, ls="--", lw=1)
        ax[0, j].set_title("Vorwaertsast theta = %d Grad, Gitter (r0, R) = (12, 24)" % th, color=ink)
        ax[0, j].set_ylabel("Energie E")
        ax[1, j].set_ylabel("Sonde: min q_a . q_b\n(<= 0: Gittersprung)")
        ax[2, j].set_ylabel("Kipp-Amplitude P (log)")
        ax[2, j].set_yscale("log")
        ax[2, j].set_xlabel("FIRE-Schritt nach dem Stoss")
        for row in range(3):
            ax[row, j].set_facecolor(surface)
            ax[row, j].grid(True, color=grid, lw=0.8)
            for sp in ("top", "right"):
                ax[row, j].spines[sp].set_visible(False)
        ax[0, j].legend(loc="center right", frameon=False, fontsize=9)
    fig.suptitle("GUERTEL-FELD-STAB-1: SO(3)-Feld auf Z^3, Energie ueber die Relaxation je Stoss "
                 "(X = erster Schritt mit Gittersprung)", color=ink)
    fig.tight_layout()
    p = os.path.join(aus, "energie-verlauf.png")
    fig.savefig(p, dpi=110, facecolor=surface)
    return p


def main():
    pa = argparse.ArgumentParser()
    pa.add_argument("--lauf", required=True)
    pa.add_argument("--n1", required=True)
    pa.add_argument("--aus", required=True)
    pa.add_argument("--thetas", default="")
    pa.add_argument("--eps", default="")
    pa.add_argument("--refs", default="")
    a = pa.parse_args()
    global THETAS, EPS, REFS
    if a.thetas:
        THETAS = [int(t) for t in a.thetas.split(",")]
    if a.eps:
        EPS = [float(e) for e in a.eps.split(",")]
    if a.refs:
        REFS = {int(k): int(v) for k, v in (p.split(":") for p in a.refs.split(","))}
    prot = lade(os.path.join(a.lauf, "prot.json"))
    n1 = lade(a.n1)
    out = {"kopf": {"code_sha256": sha_datei(os.path.abspath(__file__)), "lauf": a.lauf, "n1": a.n1,
                    "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())},
           "regeln": {"TOL_GS0": TOL_GS0, "RHO_UM": RHO_UM, "RHO_AST": RHO_AST, "WORT_BAND": WORT_BAND}}
    out["GS0"] = gs0(prot, n1)
    refs, refinfo = {}, {}
    for th in THETAS:
        E_ref, info = ref_wert(a.lauf, REFS[th])
        refs[REFS[th]] = E_ref
        refinfo[str(REFS[th])] = info
    out["referenz"] = refinfo
    laeufe, kp, kw = [], [], []
    for th in THETAS:
        for eps in EPS:
            r = lade(os.path.join(a.lauf, "stoss-T%d-e%g.json" % (th, eps)))
            if r is None or refs[REFS[th]] is None:
                laeufe.append({"theta": th, "eps": eps, "fehlt_oder_ohne_referenz": True})
                kp.append(None)
                kw.append(None)
                continue
            c = klasse(r, refs[REFS[th]])
            laeufe.append(c)
            kp.append(c["klasse_plan"])
            kw.append(c["klasse_wort"])
    out["stoesse"] = laeufe
    out["GS1"] = {"plan": urteil(kp), "wort": urteil(kw), "klassen_plan": kp, "klassen_wort": kw}
    kontr = []
    for th in THETAS:
        r = lade(os.path.join(a.lauf, "stoss-T%d-e0.json" % th))
        if r is not None and refs[REFS[th]] is not None:
            kontr.append(klasse(r, refs[REFS[th]]))
    out["kontrolle_ohne_stoss_beschreibend"] = kontr
    try:
        out["bild"] = bild(a.lauf, a.aus, refs)
    except Exception as e:  # Bild ist beschreibend; Urteile bleiben
        out["bild_fehler"] = repr(e)
    with open(os.path.join(a.aus, "auswertung.json.neu"), "w") as f:
        json.dump(out, f, indent=1)
    os.replace(os.path.join(a.aus, "auswertung.json.neu"), os.path.join(a.aus, "auswertung.json"))
    print("auswertung fertig: GS0 plan=%s wort=%s; GS1 plan=%s wort=%s" % (
        out["GS0"]["plan"], out["GS0"]["wort"], out["GS1"]["plan"], out["GS1"]["wort"]))


if __name__ == "__main__":
    main()
