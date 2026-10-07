#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GUERTEL-FINN-NETZ-1: mechanische Auswertung (PLAN.md Abschnitt 7) und Bilder (PNG).

Liest lauf/prot-*.json, lauf/wahl.json, lauf/stoss-*.json und eingaben-gfs1/prot.json (GFS1, K0-Bezug); schreibt
auswertung.json, energie-verlauf.png und vorwaertsast.png. Fehlt eine Datei, lautet das betroffene Urteil
"nicht auswertbar". Regeln fuer theta_max und Gueltigkeit kommen aus finn.py (eine Quelle).
Aufruf nur ueber kleintest.sh auf der .69.
"""
import argparse
import hashlib
import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import finn  # noqa: E402

EPS = [0.01, 0.1, 0.3]          # Vorgabe; per --eps aenderbar (nur Rauchlauf)
SO2_THETAS = [420.0, 450.0]     # Teil C (fest); per --so2_thetas aenderbar (nur Rauchlauf)
GRENZE = 450.0                  # GF1: theta_max > 450; per --grenze aenderbar (nur Rauchlauf)
TOL_K0 = 1.0e-6                 # K0: Energie auf 1e-6 relativ
RHO_UM = 0.10                   # Plan: umgekehrt, wenn rho <= 0,10 und Drehsinn aussen < 0
RHO_AST = 0.90                  # Plan: Ast, wenn rho >= 0,90 und P_end <= P_0
TOL_WORT_GF2 = 1.0e-6           # Wortlaut GF2: E auf E(720 - theta) auf 1e-6 relativ
SO2_BAND = 0.10                 # Teil C: entdrillt, wenn E_end < 0,90 E_vor
MIN_UM = 2                      # GF2: mindestens 2 von 3 Stoessen je Winkel
K0_PLAN = [("schritt", 420.0), ("schritt", 450.0), ("gitter", 450.0)]
K0_WORT = [("schritt", 450.0), ("gitter", 450.0)]


def sha_datei(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def idx(liste, wert):
    for i, v in enumerate(liste):
        if v is not None and abs(v - wert) < 1e-9:
            return i
    return None


def k0(pz, gfs):
    na = {"plan": "nicht auswertbar", "wort": "nicht auswertbar"}
    if pz is None or gfs is None:
        return dict(na, grund="Datei fehlt", werte=[])
    werte = []
    for art, th in K0_PLAN:
        tk, ek, sk = (("theta_schritt", "E_schritt", "sonde_schritt") if art == "schritt"
                      else ("gitter", "E_gitter", "sonde_gitter"))
        i1 = idx(gfs["protokoll"][tk], th)
        i2 = idx(pz["protokoll"][tk], th)
        if i1 is None or i2 is None:
            return dict(na, grund="Winkel fehlt", werte=werte)
        E1 = gfs["protokoll"][ek][i1]
        E2 = pz["protokoll"][ek][i2]
        werte.append({"art": art, "theta": th, "E_gfs1": E1, "E_neu": E2, "rel": abs(E2 - E1) / abs(E1),
                      "sonde_gfs1": gfs["protokoll"][sk][i1], "sonde_neu": pz["protokoll"][sk][i2]})
    plan = all(w["rel"] <= TOL_K0 for w in werte) and all(w["sonde_neu"] > 0.0 for w in werte)
    wort = all(w["rel"] <= TOL_K0 for w in werte if (w["art"], w["theta"]) in K0_WORT)
    return {"plan": "eingetroffen" if plan else "nicht eingetroffen",
            "wort": "eingetroffen" if wort else "nicht eingetroffen", "werte": werte,
            "z3_gleich_g2": pz["netz_info"].get("z3_gleich_g2")}


def teil_a(prj):
    if prj is None:
        return None
    feld = prj["kopf"]["args"]["feld"]
    ras = prj["protokoll"]["raster"]
    zeilen = []
    for t, E, s, sl, st in zip(ras["theta"], ras["E"], ras["sonde"], ras["sonde_lauf"], ras["struktur"]):
        zeilen.append({"theta": t, "E": E, "sonde": s, "sonde_lauf": sl, "sinn_aussen": finn.sinn_aussen(feld, st),
                       "P": st["kipp_amplitude"]})
    return {"feld": feld, "dtheta": prj["kopf"]["args"]["fdtheta"], "theta_max": finn.theta_max(prj),
            "theta_sprung_fein": finn.theta_sprung_fein(prj),
            "gueltig_plan_grenze": finn.gueltig_plan(prj, GRENZE), "gueltig_wort_grenze": finn.gueltig_wort(prj, GRENZE),
            "netz_info": prj["netz_info"], "laufzeit_s": prj["laufzeit_s"], "raster": zeilen}


def gt(tm, grenze):
    return tm is None or tm > grenze


def lade_lauf(lauf, netz, feld, th, eps):
    return finn.lade_json(os.path.join(lauf, "stoss-%s-%s-T%d-e%g.json" % (netz, feld, int(round(th)), eps)))


def ref_wert(lauf, th_ref):
    r = lade_lauf(lauf, "diamant", "so3", th_ref, 0.0)
    if r is None:
        return None, {"theta": th_ref, "fehlt": True}
    info = {"theta": th_ref, "E_vor": r["E_vor"], "E_end": r["E_end"], "sonde_lauf": r["sonde_lauf"],
            "fmax_end": r["fmax_end"], "schritte": r["schritte"],
            "qz_mittel_aussen_end": r["struktur_end"]["qz_mittel_aussen"]}
    if not (r["sonde_lauf"] > 0.0 and r["E_end"] > 0.0):
        info["ungueltig"] = True
        return None, info
    return r["E_end"], info


def klasse_so3(run, E_ref, pd10):
    th = run["theta"]
    E_end, E_ast = run["E_end"], run["E_vor"]
    rho = (E_end - E_ref) / (E_ast - E_ref)
    P = run["verlauf"]["kipp"]
    P0, Pend = P[0], P[-1]
    qz = run["struktur_end"]["qz_mittel_aussen"]
    sprung_lauf = not (run["sonde_lauf"] > 0.0)
    sprung_plan = sprung_lauf or not finn.gueltig_plan(pd10, th)
    sprung_wort = sprung_lauf or not finn.gueltig_wort(pd10, th)
    if sprung_plan:
        kp = "sprung"
    elif rho <= RHO_UM and qz < 0.0:
        kp = "umgekehrt"
    elif rho >= RHO_AST and Pend <= P0:
        kp = "ast"
    else:
        kp = "dazwischen"
    if sprung_wort:
        kw = "sprung"
    elif abs(E_end - E_ref) <= TOL_WORT_GF2 * E_ref:
        kw = "umgekehrt"
    else:
        kw = "nicht umgekehrt"
    S = run["verlauf"]["sonde"]
    E = run["verlauf"]["E"]
    return {"theta": th, "eps": run["eps"], "klasse_plan": kp, "klasse_wort": kw, "rho": rho,
            "E_vor": E_ast, "E_nach_stoss": run["E_nach_stoss"], "E_end": E_end, "E_ref": E_ref,
            "E_end_durch_E_ref_minus_1": E_end / E_ref - 1.0, "E_min_lauf": min(E), "E_max_lauf": max(E),
            "sonde_nach_stoss": run["sonde_nach_stoss"], "sonde_end": run["sonde_end"],
            "sonde_lauf": run["sonde_lauf"], "erster_sprung_schritt": next((k for k, s in enumerate(S)
                                                                            if not (s > 0.0)), None),
            "halb_schritt": next((k for k, e in enumerate(E) if e < 0.5 * (E_ast + E_ref)), None),
            "fmax_end": run["fmax_end"], "schritte": run["schritte"], "kipp_delta_max": run["kipp_delta_max"],
            "kipp_plaetze": run["kipp_plaetze"], "kipp_P0": P0, "kipp_Pend": Pend, "kipp_Pmax": max(P),
            "kipp_Pmax_schritt": int(P.index(max(P))),
            "qz_mittel_aussen_vor": run["struktur_vor"]["qz_mittel_aussen"], "qz_mittel_aussen_end": qz,
            "q0_min_frei_end": run["struktur_end"]["q0_min_frei"], "laufzeit_s": run["laufzeit_s"],
            "E_bei": {str(k): E[k] for k in (0, 250, 500, 1000, 1500, 2000, 2500, 3000) if k < len(E)}}


def klasse_so2(run, sd10):
    th = run["theta"]
    sprung = (not (run["sonde_lauf"] < np.pi)) or (sd10 is None) or (not finn.gueltig_wort(sd10, th))
    band = run["E_end"] >= (1.0 - SO2_BAND) * run["E_vor"]
    kp = "sprung" if sprung else ("bleibt" if band else "entdrillt")
    kw = "bleibt" if band else "entdrillt"
    E = run["verlauf"]["E"]
    return {"theta": th, "eps": run["eps"], "klasse_plan": kp, "klasse_wort": kw, "E_vor": run["E_vor"],
            "E_nach_stoss": run["E_nach_stoss"], "E_end": run["E_end"], "E_end_durch_E_vor": run["E_end"] / run["E_vor"],
            "E_max_lauf": max(E), "sonde_lauf_max_dphi": run["sonde_lauf"], "sonde_end": run["sonde_end"],
            "schritte": run["schritte"], "fmax_end": run["fmax_end"], "kipp_delta_max": run["kipp_delta_max"],
            "phi_mittel_aussen_vor": run["struktur_vor"]["phi_mittel_aussen"],
            "phi_mittel_aussen_end": run["struktur_end"]["phi_mittel_aussen"], "laufzeit_s": run["laufzeit_s"]}


def gf2(winkel, klassen):
    if not winkel:
        return "nicht eingetroffen", "kein gueltiger Rasterwinkel ueber 360"
    for th in winkel:
        if any(k is None for k in klassen.get(th, [None])):
            return "nicht auswertbar", "Lauf oder Referenz fehlt bei %g" % th
    ok = all(sum(k == "umgekehrt" for k in klassen[th]) >= MIN_UM for th in winkel)
    return ("eingetroffen" if ok else "nicht eingetroffen"), ""


FARBE = {"diamant": "#2a78d6", "z3": "#eb6834"}
EPS_FARBE = {0.0: "#8a8984", 0.01: "#2a78d6", 0.1: "#eb6834", 0.3: "#1baf7a"}
SURFACE, INK, INK2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df"


def stil(ax):
    ax.set_facecolor(SURFACE)
    ax.grid(True, color=GRID, lw=0.8)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)


def bild_stoss(lauf, aus, winkel, refs):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"font.size": 10, "axes.edgecolor": INK2, "axes.labelcolor": INK, "xtick.color": INK2,
                         "ytick.color": INK2, "text.color": INK})
    sp = max(1, len(winkel))
    fig, ax = plt.subplots(3, sp, figsize=(6 * sp, 10.5), sharex=True, facecolor=SURFACE, squeeze=False)
    for j, th in enumerate(winkel):
        for eps in [0.0] + EPS:
            r = lade_lauf(lauf, "diamant", "so3", th, eps)
            if r is None:
                continue
            v = r["verlauf"]
            n = list(range(len(v["E"])))
            lab = "ohne Stoss (eps = 0)" if eps == 0.0 else "eps = %g" % eps
            ax[0, j].plot(n, v["E"], color=EPS_FARBE[eps], lw=2, label=lab)
            ax[1, j].plot(n, v["sonde"], color=EPS_FARBE[eps], lw=2, label=lab)
            ax[2, j].plot(n, [max(p, 1e-12) for p in v["kipp"]], color=EPS_FARBE[eps], lw=2, label=lab)
            k = next((i for i, s in enumerate(v["sonde"]) if not (s > 0.0)), None)
            if k is not None:
                for row, yy in ((0, v["E"][k]), (1, v["sonde"][k])):
                    ax[row, j].plot([k], [yy], marker="X", ms=10, color=EPS_FARBE[eps], mec=SURFACE, mew=1.5)
        tr = refs.get("%d" % int(round(th)))
        Eref = tr[1] if tr else None
        if Eref is not None:
            ax[0, j].axhline(Eref, color=INK2, ls="--", lw=1)
            ax[0, j].annotate("E(720 - theta) = E(%d) = %.0f" % (tr[0], Eref), (0.99, Eref),
                              xycoords=("axes fraction", "data"), ha="right", va="bottom", color=INK2, fontsize=9)
        r0 = lade_lauf(lauf, "diamant", "so3", th, 0.0)
        if r0 is not None:
            ax[0, j].axhline(r0["E_vor"], color=INK2, ls=":", lw=1)
            ax[0, j].annotate("Ast bei %d Grad (Start) = %.0f" % (th, r0["E_vor"]), (0.99, r0["E_vor"]),
                              xycoords=("axes fraction", "data"), ha="right", va="top", color=INK2, fontsize=9)
        ax[1, j].axhline(0.0, color=INK2, ls="--", lw=1)
        ax[0, j].set_title("Diamant-Netz, Vorwaertsast theta = %d Grad" % th, color=INK)
        ax[0, j].set_ylabel("Energie E")
        ax[1, j].set_ylabel("Sonde: min q_a . q_b\n(<= 0: Gittersprung)")
        ax[2, j].set_ylabel("Kipp-Amplitude P (log)")
        ax[2, j].set_yscale("log")
        ax[2, j].set_xlabel("FIRE-Schritt nach dem Stoss")
        for row in range(3):
            stil(ax[row, j])
        ax[0, j].legend(loc="center right", frameon=False, fontsize=9)
    if not winkel:
        ax[0, 0].text(0.5, 0.5, "kein Stosswinkel (kein gueltiger Ast ueber 360 Grad)", ha="center",
                      transform=ax[0, 0].transAxes)
    fig.suptitle("GUERTEL-FINN-NETZ-1: SO(3)-Feld auf dem Diamant-Netz (r0, R) = (12, 24), Energie ueber die "
                 "Relaxation je Stoss (X = erster Gittersprung)", color=INK)
    fig.tight_layout()
    p = os.path.join(aus, "energie-verlauf.png")
    fig.savefig(p, dpi=110, facecolor=SURFACE)
    plt.close(fig)
    return p


def bild_ast(aus, prots):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(1, 2, figsize=(14, 5.6), facecolor=SURFACE)
    stile = {("so3", 10): ("-", "SO(3), 10-Grad-Schritte (Plan)"), ("so3", 30): ("--", "SO(3), 30-Grad-Schritte (Wortlaut)"),
             ("so2", 10): (":", "SO(2), 10-Grad-Schritte")}
    for (netz, feld, d), prj in prots.items():
        if prj is None:
            continue
        pr = prj["protokoll"]
        ls, lab = stile[(feld, d)]
        lab = ("Diamant" if netz == "diamant" else "Z^3") + ", " + lab
        th = pr["theta_schritt"]
        sl = pr["sonde_lauf_schritt"]
        if feld == "so2":
            sl = [np.cos(min(s, np.pi) / 2.0) if s is not None else np.nan for s in sl]
        ax[0].plot(th, pr["E_schritt"], color=FARBE[netz], ls=ls, lw=2, label=lab)
        ax[1].plot(th, sl, color=FARBE[netz], ls=ls, lw=2, label=lab)
        tm = finn.theta_max(prj)
        if tm is not None:
            ax[1].plot([tm], [0.0], marker="X", ms=10, color=FARBE[netz], mec=SURFACE, mew=1.5)
    ax[1].axhline(0.0, color=INK2, ls="--", lw=1)
    ax[1].axvline(GRENZE, color=INK2, ls=":", lw=1)
    ax[0].set_xlabel("Kernwinkel theta (Grad)")
    ax[1].set_xlabel("Kernwinkel theta (Grad)")
    ax[0].set_ylabel("Energie E am Schrittende")
    ax[1].set_ylabel("laufende Sonde min q_a . q_b\n(SO(2): cos(max|dphi|/2); <= 0: Sprung)")
    ax[0].set_title("Vorwaertsast: Energie", color=INK)
    ax[1].set_title("Vorwaertsast: Sprung-Sonde (X = theta_max im 30-Grad-Raster)", color=INK)
    for a in ax:
        stil(a)
    ax[0].legend(loc="upper left", frameon=False, fontsize=8)
    fig.suptitle("GUERTEL-FINN-NETZ-1: Diamant-Netz gegen Z^3 bei gleicher Knotenzahl, (r0, R) = (12, 24)", color=INK)
    fig.tight_layout()
    p = os.path.join(aus, "vorwaertsast.png")
    fig.savefig(p, dpi=110, facecolor=SURFACE)
    plt.close(fig)
    return p


def main():
    pa = argparse.ArgumentParser()
    pa.add_argument("--lauf", required=True)
    pa.add_argument("--gfs1", required=True)
    pa.add_argument("--aus", required=True)
    pa.add_argument("--eps", default="")
    pa.add_argument("--so2_thetas", default="")
    pa.add_argument("--grenze", type=float, default=None)
    a = pa.parse_args()
    global EPS, SO2_THETAS, GRENZE
    if a.eps:
        EPS = [float(e) for e in a.eps.split(",")]
    if a.so2_thetas:
        SO2_THETAS = [float(t) for t in a.so2_thetas.split(",")]
    if a.grenze is not None:
        GRENZE = a.grenze
    L = lambda n: finn.lade_json(os.path.join(a.lauf, n))  # noqa: E731
    prots = {("diamant", "so3", 10): L("prot-diamant-so3-d10.json"), ("z3", "so3", 10): L("prot-z3-so3-d10.json"),
             ("diamant", "so3", 30): L("prot-diamant-so3-d30.json"), ("z3", "so3", 30): L("prot-z3-so3-d30.json"),
             ("diamant", "so2", 10): L("prot-diamant-so2-d10.json"), ("z3", "so2", 10): L("prot-z3-so2-d10.json")}
    pd10, pz10 = prots[("diamant", "so3", 10)], prots[("z3", "so3", 10)]
    pd30, sd10 = prots[("diamant", "so3", 30)], prots[("diamant", "so2", 10)]
    gfs = finn.lade_json(a.gfs1)
    wahl = L("wahl.json")
    out = {"kopf": {"code_sha256": sha_datei(os.path.abspath(__file__)),
                    "finn_code_sha256": sha_datei(os.path.abspath(finn.__file__)), "lauf": a.lauf, "gfs1": a.gfs1,
                    "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())},
           "regeln": {"EPS": EPS, "SO2_THETAS": SO2_THETAS, "GRENZE": GRENZE, "TOL_K0": TOL_K0, "RHO_UM": RHO_UM,
                      "RHO_AST": RHO_AST, "TOL_WORT_GF2": TOL_WORT_GF2, "SO2_BAND": SO2_BAND, "MIN_UM": MIN_UM}}
    # --- K0 ---
    out["K0"] = k0(pz10, gfs)
    # --- Teil A ---
    out["teil_A"] = {"%s-%s-d%d" % k: teil_a(v) for k, v in prots.items()}
    if pd10 is None or pd30 is None:
        out["GF1"] = {"plan": "nicht auswertbar", "wort": "nicht auswertbar"}
    else:
        tm10, tm30 = finn.theta_max(pd10), finn.theta_max(pd30)
        gp = gt(tm10, GRENZE) and finn.gueltig_plan(pd10, GRENZE)
        out["GF1"] = {"plan": "eingetroffen" if gp else "nicht eingetroffen",
                      "wort": "eingetroffen" if gt(tm30, GRENZE) else "nicht eingetroffen",
                      "theta_max_p10_diamant": tm10, "theta_max_p30_diamant": tm30,
                      "theta_max_p10_z3": finn.theta_max(pz10) if pz10 else "fehlt",
                      "theta_max_p30_z3": finn.theta_max(prots[("z3", "so3", 30)]) if prots[("z3", "so3", 30)] else "fehlt",
                      "gueltig_plan_bei_grenze": finn.gueltig_plan(pd10, GRENZE)}
    # Kontinuumsvergleich bei 90 Grad (beschreibend)
    if pd10 is not None and pz10 is not None:
        i_d = idx(pd10["protokoll"]["raster"]["theta"], 90.0)
        i_z = idx(pz10["protokoll"]["raster"]["theta"], 90.0)
        if i_d is not None and i_z is not None:
            out["E_diamant_durch_E_z3_bei_90"] = (pd10["protokoll"]["raster"]["E"][i_d]
                                                  / pz10["protokoll"]["raster"]["E"][i_z])
    # --- Teil B ---
    refs, refinfo, refs_bild = {}, {}, {}
    winkel = wahl["alle"] if wahl else []
    for th in winkel:
        tr = wahl["refs"]["%d" % int(round(th))]
        E_ref, info = ref_wert(a.lauf, tr)
        refs[th] = E_ref
        refinfo["%d" % int(round(tr))] = info
        refs_bild["%d" % int(round(th))] = (tr, E_ref)
    out["wahl"] = wahl
    out["referenz"] = refinfo
    laeufe, kp, kw = [], {}, {}
    for th in winkel:
        kp[th], kw[th] = [], []
        for eps in EPS:
            r = lade_lauf(a.lauf, "diamant", "so3", th, eps)
            if r is None or refs[th] is None or pd10 is None:
                laeufe.append({"theta": th, "eps": eps, "fehlt_oder_ohne_referenz": True})
                kp[th].append(None)
                kw[th].append(None)
                continue
            c = klasse_so3(r, refs[th], pd10)
            laeufe.append(c)
            kp[th].append(c["klasse_plan"])
            kw[th].append(c["klasse_wort"])
    out["stoesse"] = laeufe
    if wahl is None:
        out["GF2"] = {"plan": "nicht auswertbar", "wort": "nicht auswertbar", "grund": "wahl.json fehlt"}
    else:
        up, gp_ = gf2(wahl["plan"], kp) if wahl["p10_da"] else ("nicht auswertbar", "P10 fehlt")
        uw, gw_ = gf2(wahl["wort"], kw) if wahl["p30_da"] else ("nicht auswertbar", "P30 fehlt")
        out["GF2"] = {"plan": up, "wort": uw, "grund_plan": gp_, "grund_wort": gw_, "winkel_plan": wahl["plan"],
                      "winkel_wort": wahl["wort"], "klassen_plan": {str(k): v for k, v in kp.items()},
                      "klassen_wort": {str(k): v for k, v in kw.items()}}
    kontr = []
    for th in winkel:
        r = lade_lauf(a.lauf, "diamant", "so3", th, 0.0)
        if r is not None and refs.get(th) is not None and pd10 is not None:
            kontr.append(klasse_so3(r, refs[th], pd10))
    out["kontrolle_ohne_stoss_beschreibend"] = kontr
    # --- Teil C ---
    so2, so2_k = [], []
    for th in SO2_THETAS:
        for eps in EPS:
            r = lade_lauf(a.lauf, "diamant", "so2", th, eps)
            if r is None:
                so2.append({"theta": th, "eps": eps, "fehlt": True})
                so2_k.append(None)
                continue
            c = klasse_so2(r, sd10)
            so2.append(c)
            so2_k.append(c)
    out["so2_stoesse"] = so2
    out["so2_kontrolle_eps0_beschreibend"] = [klasse_so2(r, sd10) for r in
                                              (lade_lauf(a.lauf, "diamant", "so2", th, 0.0) for th in SO2_THETAS)
                                              if r is not None]
    if out["K0"]["plan"] == "nicht auswertbar" or any(c is None for c in so2_k):
        out["GF0"] = {"plan": "nicht auswertbar", "wort": "nicht auswertbar"}
    else:
        p_ok = out["K0"]["plan"] == "eingetroffen" and all(c["klasse_plan"] == "bleibt" for c in so2_k)
        w_ok = out["K0"]["wort"] == "eingetroffen" and not any(c["klasse_wort"] == "entdrillt" for c in so2_k)
        out["GF0"] = {"plan": "eingetroffen" if p_ok else "nicht eingetroffen",
                      "wort": "eingetroffen" if w_ok else "nicht eingetroffen"}
    # --- Bilder (beschreibend; Urteile bleiben bei Fehlern) ---
    try:
        out["bild_stoss"] = bild_stoss(a.lauf, a.aus, winkel, refs_bild)
    except Exception as e:
        out["bild_stoss_fehler"] = repr(e)
    try:
        out["bild_ast"] = bild_ast(a.aus, {(k[0], k[1], k[2]): v for k, v in prots.items()})
    except Exception as e:
        out["bild_ast_fehler"] = repr(e)
    tmp = os.path.join(a.aus, "auswertung.json.neu")
    with open(tmp, "w") as f:
        json.dump(finn.g2.sauber(out), f, indent=1)
    os.replace(tmp, os.path.join(a.aus, "auswertung.json"))
    print("auswertung fertig: GF0 %s/%s; GF1 %s/%s; GF2 %s/%s" % (
        out["GF0"]["plan"], out["GF0"]["wort"], out["GF1"]["plan"], out["GF1"]["wort"], out["GF2"]["plan"],
        out["GF2"]["wort"]))


if __name__ == "__main__":
    main()
