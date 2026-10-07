#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GUERTEL-FELD-STAB-2: mechanische Auswertung (PLAN.md, Abschnitt 5) und Bilder (PNG).

Liest die Laufdateien aus --lauf und die GFS-1-Kopien aus --gfs1; schreibt auswertung.json, energie-verlauf.png und
sprunggrenze.png nach --aus. Fehlt eine Datei, lautet das betroffene Urteil "nicht auswertbar".
Aufruf nur ueber kleintest.sh auf der .69.
"""
import argparse
import hashlib
import json
import math
import os
import time

GITTER = [("g8", 8, 16), ("g12", 12, 24), ("g16", 16, 32)]
SEGMENTE = {"g8": ["prot-g8.json"], "g12": ["prot-g12.json"], "g16": ["prot-g16a.json", "prot-g16b.json"]}
EPS = [0.01, 0.1, 0.3]
THETA_A = 450          # Teil A (GT1, GT0)
THETA_REF = 270        # E(720 - 450)
THETA_Z = 420          # Zusatz (16, 32), beschreibend
THETA_ZREF = 300
TOL_E = 1.0e-6         # GT0, GT1: Energie auf 1e-6 relativ (Karte)
RHO_AST = 0.90         # Plan-Klasse "ast" (wie GFS-1)
SO2_BAND_PLAN = 1.0e-3  # SO(2) "ast" nach Plan
SO2_BAND_WORT = 0.10    # SO(2) "ast" nach Wortlaut ("E bleibt auf dem Ast")
FTOL = 1.0e-5          # Referenz konvergiert
TMAX_B = 720.0         # Teil B: Protokoll bis 720 Grad
RASTER = 30.0          # Teil B: theta_max in Schritten von 30 Grad
INF = float("inf")


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


def rel(a, b):
    return abs(a - b) / abs(b)


# ----------------------------------------------------------------------------- Teil B

def protokoll_gitter(lauf, tag):
    """Fuegt die Protokoll-Abschnitte eines Gitters zusammen; None, wenn der erste fehlt."""
    pr = None
    for name in SEGMENTE[tag]:
        d = lade(os.path.join(lauf, name))
        if d is None:
            break
        p = d["protokoll"]
        if pr is None:
            pr = {k: list(v) for k, v in p.items() if isinstance(v, list)}
            continue
        if abs(p["theta_schritt"][0] - (pr["theta_schritt"][-1] + 10.0)) > 1e-9:
            raise SystemExit("Abschnitte passen nicht: %s" % name)
        for k, v in p.items():
            if isinstance(v, list):
                pr[k].extend(v)
    return pr


def winkelreihe(pr):
    """Je Protokollwinkel: Sonde der Zustaende (Schritt und Gitter), Sonde im Lauf, q_z aussen, E am Ende."""
    out = []
    for i, th in enumerate(pr["theta_schritt"]):
        s_z = pr["sonde_schritt"][i]
        s_l = pr["sonde_lauf_schritt"][i]
        E = pr["E_schritt"][i]
        k = idx(pr["gitter"], th)
        if k is not None:
            s_z = min(s_z, pr["sonde_gitter"][k])
            s_l = min(s_l, pr["sonde_lauf_gitter"][k])
            E = pr["E_gitter"][k]
        out.append({"theta": th, "sonde_zust": s_z, "sonde_lauf": s_l, "qz": pr["qz_aussen"][i], "E": E,
                    "P": pr["kipp"][i]})
    return out


def theta_max(reihe, schluessel):
    thJ = next((w["theta"] for w in reihe if w[schluessel] <= 0.0), None)
    vor = [w for w in reihe if thJ is None or w["theta"] < thJ]
    thU = next((w["theta"] for w in vor if w["qz"] is not None and w["qz"] < 0.0), None)
    t_end = reihe[-1]["theta"] if reihe else None
    if thU is not None:
        return {"theta_J": thJ, "theta_U": thU, "art": "glatt umgelegt vor einem Sprung", "theta_max": None,
                "lo": INF, "hi": INF}
    if thJ is not None:
        tm = math.ceil(thJ / RASTER - 1e-9) * RASTER
        return {"theta_J": thJ, "theta_U": None, "art": "sprung", "theta_max": tm, "lo": tm, "hi": tm}
    if t_end is None or t_end < TMAX_B - 1e-9:
        return None
    return {"theta_J": None, "theta_U": None, "art": "kein Sprung bis %g" % TMAX_B, "theta_max": None,
            "lo": TMAX_B + RASTER, "hi": INF}


def kleiner(a, b):
    if a is None or b is None:
        return "fehlt"
    if a["hi"] == INF and b["hi"] == INF:
        return None
    if a["hi"] < b["lo"]:
        return True
    if a["lo"] >= b["hi"]:
        return False
    return None


def gt2(tm):
    c = [kleiner(tm["g8"], tm["g12"]), kleiner(tm["g12"], tm["g16"])]
    if any(x is False for x in c):
        u = "nicht eingetroffen"
    elif any(x == "fehlt" for x in c):
        u = "nicht auswertbar"
    elif all(x is True for x in c):
        u = "eingetroffen"
    else:
        u = "nicht entschieden"
    return u, c


# ----------------------------------------------------------------------------- Teil A (SO(3))

def ref_wert(lauf, tag, th_ref):
    r = lade(os.path.join(lauf, "stoss-%s-T%d-e0.json" % (tag, th_ref)))
    if r is None:
        return None, None, {"theta": th_ref, "fehlt": True}
    qz = r["struktur_end"]["qz_mittel_aussen"]
    info = {"theta": th_ref, "E_vor": r["E_vor"], "E_end": r["E_end"], "sonde_lauf_mit_start": r["sonde_lauf_mit_start"],
            "fmax_end": r["fmax_end"], "schritte": r["schritte"], "qz_mittel_aussen_end": qz}
    wort = r["E_end"] if (r["sonde_lauf_mit_start"] > 0.0 and r["E_end"] > 0.0) else None
    plan = wort if (wort is not None and qz > 0.0 and r["fmax_end"] <= FTOL) else None
    info["gueltig_plan"] = plan is not None
    info["gueltig_wort"] = wort is not None
    return plan, wort, info


def klasse3(run, E_ref_plan, E_ref_wort):
    E_end, E_ast = run["E_end"], run["E_vor"]
    sprung = not (run["sonde_lauf_mit_start"] > 0.0)
    P = run["verlauf"]["kipp"]
    P0, Pend = P[0], P[-1]
    qv = run["struktur_vor"]["qz_mittel_aussen"]
    qe = run["struktur_end"]["qz_mittel_aussen"]
    rho = None
    if sprung:
        kp = "sprung"
    elif E_ref_plan is None:
        kp = None
    else:
        rho = (E_end - E_ref_plan) / (E_ast - E_ref_plan)
        if rel(E_end, E_ref_plan) <= TOL_E and qv > 0.0 and qe < 0.0:
            kp = "umgekehrt"
        elif rho >= RHO_AST and Pend <= P0:
            kp = "ast"
        else:
            kp = "dazwischen"
    if sprung:
        kw = "sprung"
    elif E_ref_wort is None:
        kw = None
    elif rel(E_end, E_ref_wort) <= TOL_E:
        kw = "umgekehrt"
    else:
        kw = "nicht umgekehrt"
    S = run["verlauf"]["sonde"]
    E = run["verlauf"]["E"]
    Eref = E_ref_plan if E_ref_plan is not None else E_ref_wort
    halb = None
    if Eref is not None:
        halb = next((k for k, e in enumerate(E) if e < 0.5 * (E_ast + Eref)), None)
    return {"theta": run["theta"], "eps": run["eps"], "klasse_plan": kp, "klasse_wort": kw, "rho": rho,
            "E_vor": E_ast, "E_nach_stoss": run["E_nach_stoss"], "E_end": E_end, "E_ref": Eref,
            "E_end_rel_zu_E_ref": None if Eref is None else (E_end - Eref) / Eref,
            "sonde_vor": run["sonde_vor"], "sonde_nach_stoss": run["sonde_nach_stoss"],
            "sonde_lauf_mit_start": run["sonde_lauf_mit_start"], "sonde_end": run["sonde_end"],
            "erster_sprung_schritt": next((k for k, s in enumerate(S) if not (s > 0.0)), None),
            "fmax_end": run["fmax_end"], "schritte": run["schritte"], "halb": halb,
            "kipp_P0": P0, "kipp_Pend": Pend, "kipp_Pmax": max(P), "kipp_Pmax_schritt": int(P.index(max(P))),
            "qz_mittel_aussen_vor": qv, "qz_mittel_aussen_end": qe,
            "q0_min_frei_end": run["struktur_end"]["q0_min_frei"], "kipp_delta_max": run["kipp_delta_max"],
            "kipp_plaetze": run["kipp_plaetze"], "laufzeit_s": run["laufzeit_s"]}


def laeufe3(lauf, tag, th, th_ref):
    E_p, E_w, info = ref_wert(lauf, tag, th_ref)
    out, kp, kw = [], [], []
    for eps in EPS:
        r = lade(os.path.join(lauf, "stoss-%s-T%d-e%g.json" % (tag, th, eps)))
        if r is None:
            out.append({"theta": th, "eps": eps, "fehlt": True})
            kp.append(None)
            kw.append(None)
            continue
        c = klasse3(r, E_p, E_w)
        out.append(c)
        kp.append(c["klasse_plan"])
        kw.append(c["klasse_wort"])
    return out, kp, kw, info


def urteil_alle_um(kl):
    if any(k is not None and k != "umgekehrt" for k in kl):
        return "nicht eingetroffen"
    if any(k is None for k in kl):
        return "nicht auswertbar"
    return "eingetroffen"


# ----------------------------------------------------------------------------- Teil C (SO(2)) und GT0

def klasse2(run, E_ast, band):
    """SO(2)-Klasse. Plan: E_ast = Endwert des SO(2)-Referenzlaufs eps = 0 (auskonvergierter Ast); Wortlaut: E_ast =
    Protokollzustand vor dem Stoss (Rauchlauf: der Protokollzustand ist nicht auskonvergiert)."""
    if not (run["sonde_lauf_mit_start"] < math.pi):
        return "sprung"
    if E_ast is None:
        return None
    E_end = run["E_end"]
    if abs(E_end - E_ast) <= band * E_ast:
        return "ast"
    if E_end < E_ast - band * E_ast:
        return "entdrillt"
    return "dazwischen"


def gt0(lauf, gfs1, prot12, l12, ref12):
    # (a) SO(2)
    so2, kp, kw = [], [], []
    r0s = lade(os.path.join(lauf, "stoss-s2-T%d-e0.json" % THETA_A))
    E_ast_ref = None
    ref_s2 = {"fehlt": True}
    if r0s is not None:
        ref_s2 = {"E_vor": r0s["E_vor"], "E_end": r0s["E_end"], "sonde_lauf_mit_start": r0s["sonde_lauf_mit_start"],
                  "fmax_end": r0s["fmax_end"], "schritte": r0s["schritte"]}
        if r0s["sonde_lauf_mit_start"] < math.pi and r0s["fmax_end"] <= FTOL:
            E_ast_ref = r0s["E_end"]
        ref_s2["gueltig_plan"] = E_ast_ref is not None
    for eps in EPS:
        r = lade(os.path.join(lauf, "stoss-s2-T%d-e%g.json" % (THETA_A, eps)))
        if r is None:
            so2.append({"eps": eps, "fehlt": True})
            kp.append(None)
            kw.append(None)
            continue
        a, b = klasse2(r, E_ast_ref, SO2_BAND_PLAN), klasse2(r, r["E_vor"], SO2_BAND_WORT)
        so2.append({"eps": eps, "klasse_plan": a, "klasse_wort": b, "E_ast_ref": E_ast_ref,
                    "E_end_rel_zu_E_ast_ref": None if E_ast_ref is None else (r["E_end"] - E_ast_ref) / E_ast_ref,
                    "E_vor": r["E_vor"], "E_nach_stoss": r["E_nach_stoss"],
                    "E_end": r["E_end"], "E_end_rel_zu_E_vor": (r["E_end"] - r["E_vor"]) / r["E_vor"],
                    "sonde_vor": r["sonde_vor"], "sonde_lauf_mit_start": r["sonde_lauf_mit_start"],
                    "sonde_end": r["sonde_end"], "schritte": r["schritte"], "fmax_end": r["fmax_end"],
                    "kipp_delta_max": r["kipp_delta_max"], "kipp_plaetze": r["kipp_plaetze"]})
        kp.append(a)
        kw.append(b)

    def ua(kl):
        if any(k is None for k in kl):
            return "nicht auswertbar"
        return "eingetroffen" if all(k in ("ast", "sprung") for k in kl) else "nicht eingetroffen"
    a_plan, a_wort = ua(kp), ua(kw)
    # (b) (12, 24) gegen GFS-1
    g_prot = lade(os.path.join(gfs1, "prot.json"))
    werte = {}
    ok_plan, ok_wort, fehlt = True, True, False
    if prot12 is None or g_prot is None:
        fehlt = True
    else:
        for art, tk, ek, sk in (("schritt", "theta_schritt", "E_schritt", "sonde_schritt"),
                                ("gitter", "gitter", "E_gitter", "sonde_gitter")):
            i1 = idx(g_prot["protokoll"][tk], THETA_A)
            i2 = idx(prot12[tk], THETA_A)
            if i1 is None or i2 is None:
                fehlt = True
                continue
            E1, E2 = g_prot["protokoll"][ek][i1], prot12[ek][i2]
            werte[art] = {"E_GFS1": E1, "E_neu": E2, "rel": rel(E2, E1), "sonde_neu": prot12[sk][i2]}
            ok_plan &= werte[art]["rel"] <= TOL_E and prot12[sk][i2] > 0.0
            if art == "gitter":
                ok_wort &= werte[art]["rel"] <= TOL_E
    stoss = []
    for c in l12:
        g = lade(os.path.join(gfs1, "stoss-T%d-e%g.json" % (THETA_A, c["eps"])))
        if g is None or c.get("fehlt"):
            fehlt = True
            stoss.append({"eps": c["eps"], "fehlt": True})
            continue
        rr = rel(c["E_end"], g["E_end"])
        stoss.append({"eps": c["eps"], "E_end_GFS1": g["E_end"], "E_end_neu": c["E_end"], "rel": rr,
                      "klasse_plan": c["klasse_plan"]})
        ok_wort &= rr <= TOL_E
        ok_plan &= rr <= TOL_E and c["klasse_plan"] == "umgekehrt"
    g_ref = lade(os.path.join(gfs1, "stoss-T%d-e0.json" % THETA_REF))
    ref = None
    if g_ref is None or ref12.get("fehlt"):
        fehlt = True
    else:
        ref = {"E_ref_GFS1": g_ref["E_end"], "E_ref_neu": ref12["E_end"], "rel": rel(ref12["E_end"], g_ref["E_end"]),
               "gueltig_plan": ref12["gueltig_plan"]}
        ok_plan &= ref["rel"] <= TOL_E and ref12["gueltig_plan"]

    def ub(ok):
        if not ok:
            return "nicht eingetroffen"
        return "nicht auswertbar" if fehlt else "eingetroffen"
    b_plan, b_wort = ub(ok_plan), ub(ok_wort)

    def zus(a, b):
        if "nicht eingetroffen" in (a, b):
            return "nicht eingetroffen"
        if "nicht auswertbar" in (a, b):
            return "nicht auswertbar"
        return "eingetroffen"
    return {"plan": zus(a_plan, b_plan), "wort": zus(a_wort, b_wort),
            "teil_a_so2": {"plan": a_plan, "wort": a_wort, "referenz_eps0": ref_s2, "laeufe": so2},
            "teil_b_g12": {"plan": b_plan, "wort": b_wort, "protokoll": werte, "stoesse": stoss, "referenz": ref}}


# ----------------------------------------------------------------------------- Bilder

def bilder(lauf, aus, ref_E, reihen, tms):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    surface, ink, ink2, gridc, grau = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df", "#8a8984"
    farben = {0.01: "#2a78d6", 0.1: "#eb6834", 0.3: "#1baf7a"}
    gfarben = {"g8": "#2a78d6", "g12": "#eb6834", "g16": "#1baf7a"}
    plt.rcParams.update({"font.size": 10, "axes.edgecolor": ink2, "axes.labelcolor": ink, "xtick.color": ink2,
                         "ytick.color": ink2, "text.color": ink})

    def stil(a):
        a.set_facecolor(surface)
        a.grid(True, color=gridc, lw=0.8)
        for sp in ("top", "right"):
            a.spines[sp].set_visible(False)

    # Bild 1: Energieverlauf je Stoss
    spalten = [(t, "SO(3), Z^3-Kugel (r0, R) = (%d, %d)" % (r0, R)) for t, r0, R in GITTER] + \
              [("s2", "Kontrolle SO(2), Z^2-Scheibe (12, 24)")]
    fig, ax = plt.subplots(3, 4, figsize=(19, 10.5), sharex="col", facecolor=surface)
    for j, (tag, titel) in enumerate(spalten):
        Ea = None
        for eps in EPS:
            r = lade(os.path.join(lauf, "stoss-%s-T%d-e%g.json" % (tag, THETA_A, eps)))
            if r is None:
                continue
            v = r["verlauf"]
            n = list(range(len(v["E"])))
            ax[0, j].plot(n, v["E"], color=farben[eps], lw=2, label="eps = %g" % eps)
            ax[1, j].plot(n, v["sonde"], color=farben[eps], lw=2, label="eps = %g" % eps)
            if tag != "s2":
                ax[2, j].plot(n, [max(p, 1e-12) for p in v["kipp"]], color=farben[eps], lw=2, label="eps = %g" % eps)
                k = next((i for i, s in enumerate(v["sonde"]) if not (s > 0.0)), None)
            else:
                k = next((i for i, s in enumerate(v["sonde"]) if not (s < math.pi)), None)
            if k is not None:
                for row, yy in ((0, v["E"][k]), (1, v["sonde"][k])):
                    ax[row, j].plot([k], [yy], marker="X", ms=10, color=farben[eps], mec=surface, mew=1.5)
            Ea = r["E_vor"]
        if tag != "s2" and ref_E.get(tag) is not None:
            ax[0, j].axhline(ref_E[tag], color=ink2, ls="--", lw=1)
            ax[0, j].annotate("E(%d) = %.1f" % (THETA_REF, ref_E[tag]), (0.99, ref_E[tag]),
                              xycoords=("axes fraction", "data"), ha="right", va="bottom", color=ink2, fontsize=9)
        if Ea is not None:
            ax[0, j].axhline(Ea, color=grau, ls=":", lw=1)
            ax[0, j].annotate("Ast bei %d Grad = %.1f" % (THETA_A, Ea), (0.99, Ea), xycoords=("axes fraction", "data"),
                              ha="right", va="top", color=ink2, fontsize=9)
        if tag != "s2":
            ax[1, j].axhline(0.0, color=ink2, ls="--", lw=1)
            ax[1, j].set_ylabel("Sonde min q_a . q_b (<= 0: Sprung)")
            ax[2, j].set_yscale("log")
            ax[2, j].set_ylabel("Kipp-Amplitude P (log)")
        else:
            ax[1, j].axhline(math.pi, color=ink2, ls="--", lw=1)
            ax[1, j].set_ylabel("Sonde max |phi_a - phi_b| (>= pi: Sprung)")
            ax[2, j].text(0.5, 0.5, "SO(2): keine Kipprichtung,\nkeine Kipp-Amplitude", ha="center", va="center",
                          transform=ax[2, j].transAxes, color=ink2)
        ax[0, j].set_title(titel + ", theta = %d Grad" % THETA_A, color=ink, fontsize=10)
        ax[0, j].set_ylabel("Energie E")
        ax[2, j].set_xlabel("FIRE-Schritt nach dem Stoss")
        for row in range(3):
            stil(ax[row, j])
        ax[0, j].legend(loc="center right", frameon=False, fontsize=9)
    fig.suptitle("GUERTEL-FELD-STAB-2: Energie, Sonde und Kipp-Amplitude ueber die Relaxation je Stoss "
                 "(X = erster Schritt mit Gittersprung; gestrichelt E(270) = E(720 - 450), gepunktet der Ast)", color=ink)
    fig.tight_layout()
    p1 = os.path.join(aus, "energie-verlauf.png")
    fig.savefig(p1, dpi=100, facecolor=surface)
    plt.close(fig)
    # Bild 2: Protokoll und Sprunggrenze
    fig, ax = plt.subplots(2, 1, figsize=(12, 9), sharex=True, facecolor=surface)
    for tag, r0, R in GITTER:
        rw = reihen.get(tag)
        if not rw:
            continue
        th = [w["theta"] for w in rw]
        lab = "(r0, R) = (%d, %d)" % (r0, R)
        ax[0].plot(th, [w["E"] for w in rw], color=gfarben[tag], lw=2, label=lab)
        ax[1].plot(th, [w["sonde_zust"] for w in rw], color=gfarben[tag], lw=2, label=lab)
        t = tms.get(tag)
        if t is not None and t["theta_max"] is not None:
            for a in ax:
                a.axvline(t["theta_max"], color=gfarben[tag], ls="--", lw=1)
            ax[1].annotate("theta_max = %d" % t["theta_max"], (t["theta_max"], 0.9), color=ink2, fontsize=9,
                           rotation=90, ha="right", va="top")
    ax[1].axhline(0.0, color=ink2, ls="--", lw=1)
    ax[0].set_ylabel("Energie E des Protokollzustands")
    ax[1].set_ylabel("Sonde min q_a . q_b (<= 0: Sprung)")
    ax[1].set_xlabel("Verdrillung theta (Grad), ungestossenes 10-Grad-Protokoll")
    for a in ax:
        stil(a)
        a.legend(loc="upper left", frameon=False, fontsize=9)
    fig.suptitle("GUERTEL-FELD-STAB-2, Teil B: Vorwaertsast und Sprunggrenze je Gitter (SO(3), Z^3)", color=ink)
    fig.tight_layout()
    p2 = os.path.join(aus, "sprunggrenze.png")
    fig.savefig(p2, dpi=100, facecolor=surface)
    plt.close(fig)
    return [p1, p2]


# ----------------------------------------------------------------------------- Hauptteil

def main():
    pa = argparse.ArgumentParser()
    pa.add_argument("--lauf", required=True)
    pa.add_argument("--gfs1", required=True)
    pa.add_argument("--aus", required=True)
    pa.add_argument("--theta_a", type=int, default=0)     # nur Rauchlauf
    pa.add_argument("--theta_ref", type=int, default=0)   # nur Rauchlauf
    pa.add_argument("--tmax_b", type=float, default=0.0)  # nur Rauchlauf
    a = pa.parse_args()
    global THETA_A, THETA_REF, TMAX_B
    if a.theta_a:
        THETA_A = a.theta_a
    if a.theta_ref:
        THETA_REF = a.theta_ref
    if a.tmax_b:
        TMAX_B = a.tmax_b
    out = {"kopf": {"code_sha256": sha_datei(os.path.abspath(__file__)), "lauf": a.lauf, "gfs1": a.gfs1,
                    "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())},
           "regeln": {"TOL_E": TOL_E, "RHO_AST": RHO_AST, "SO2_BAND_PLAN": SO2_BAND_PLAN,
                      "SO2_BAND_WORT": SO2_BAND_WORT, "FTOL": FTOL, "TMAX_B": TMAX_B, "RASTER": RASTER,
                      "THETA_A": THETA_A, "THETA_REF": THETA_REF}}
    # Teil B
    reihen, tm_p, tm_w, tb = {}, {}, {}, {}
    prot = {}
    for tag, r0, R in GITTER:
        pr = protokoll_gitter(a.lauf, tag)
        prot[tag] = pr
        if pr is None:
            tm_p[tag] = tm_w[tag] = None
            tb[tag] = {"fehlt": True}
            continue
        rw = winkelreihe(pr)
        reihen[tag] = rw
        tm_p[tag] = theta_max(rw, "sonde_lauf")
        tm_w[tag] = theta_max(rw, "sonde_zust")
        tb[tag] = {"r0": r0, "R": R, "plan": tm_p[tag], "wort": tm_w[tag], "theta_ende": rw[-1]["theta"],
                   "je_30_grad": [w for w in rw if abs(w["theta"] / RASTER - round(w["theta"] / RASTER)) < 1e-9]}
    u_p, c_p = gt2(tm_p)
    u_w, c_w = gt2(tm_w)
    out["teil_b"] = tb
    out["GT2"] = {"plan": u_p, "wort": u_w, "vergleiche_plan": c_p, "vergleiche_wort": c_w}
    # Teil A
    ref_E, ta, kp_all, kw_all = {}, {}, [], []
    l12, ref12 = [], {"fehlt": True}
    for tag, r0, R in GITTER:
        l, kp, kw, info = laeufe3(a.lauf, tag, THETA_A, THETA_REF)
        ref_E[tag] = info.get("E_end") if not info.get("fehlt") else None
        ta[tag] = {"referenz": info, "stoesse": l}
        if tag in ("g8", "g16"):
            kp_all += kp
            kw_all += kw
        if tag == "g12":
            l12, ref12 = l, info
    out["teil_a"] = ta
    out["GT1"] = {"plan": urteil_alle_um(kp_all), "wort": urteil_alle_um(kw_all), "klassen_plan": kp_all,
                  "klassen_wort": kw_all}
    lz, _, _, infoz = laeufe3(a.lauf, "g16", THETA_Z, THETA_ZREF)
    out["zusatz_g16_420_beschreibend"] = {"referenz": infoz, "stoesse": lz}
    # GT0
    out["GT0"] = gt0(a.lauf, a.gfs1, prot.get("g12"), l12, ref12)
    try:
        out["bilder"] = bilder(a.lauf, a.aus, ref_E, reihen, tm_p)
    except Exception as e:  # Bilder sind beschreibend; Urteile bleiben
        out["bild_fehler"] = repr(e)

    def sauber(o):
        if isinstance(o, float) and (math.isinf(o) or math.isnan(o)):
            return str(o)
        if isinstance(o, dict):
            return {k: sauber(v) for k, v in o.items()}
        if isinstance(o, list):
            return [sauber(v) for v in o]
        return o
    with open(os.path.join(a.aus, "auswertung.json.neu"), "w") as f:
        json.dump(sauber(out), f, indent=1)
    os.replace(os.path.join(a.aus, "auswertung.json.neu"), os.path.join(a.aus, "auswertung.json"))
    print("auswertung fertig: GT0 plan=%s wort=%s; GT1 plan=%s wort=%s; GT2 plan=%s wort=%s" % (
        out["GT0"]["plan"], out["GT0"]["wort"], out["GT1"]["plan"], out["GT1"]["wort"], out["GT2"]["plan"],
        out["GT2"]["wort"]))


if __name__ == "__main__":
    main()
