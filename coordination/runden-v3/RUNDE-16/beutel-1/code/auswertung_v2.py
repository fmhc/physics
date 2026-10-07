#!/usr/bin/env python3
# BEUTEL-1 Auswertung: Aeste, p(Q), dE/dQ = omega, Duennwand-Grenzwerte, Wertung B1-B7, Gitterkontrollen, Abbildungen.
# Wertungsregeln aus PLAN.md Abschnitt 4 (eingefroren vor dem Lauf).
import os
for _k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_k, "1")
import sys, json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

D = sys.argv[1]  # Ordner mit M1.json, M2.json, M3.json und *-profile.npz
OUT = sys.argv[2]
os.makedirs(OUT, exist_ok=True)
W0 = {"M1": np.sqrt(0.5), "M2": None}
# omega_0^2 fuer M2 aus 4S^3 - 4S^2 - 1 = 0 (Schreibtisch, hier nur zum Vergleich ausgegeben)
S0M2 = [r.real for r in np.roots([4, -4, 0, -1]) if abs(r.imag) < 1e-12 and r.real > 0][0]
W0["M2"] = np.sqrt(1 / (4 * S0M2) + 1 - S0M2 + S0M2**2 / 2)


def load(m):
    with open(os.path.join(D, m + ".json")) as fh:
        return json.load(fh)


def branches(pts):
    """Sortiert nach omega2; dQ/domega aus Nachbarn; teilt in stabil (dQ/dw<0) und instabil."""
    idx = np.argsort([p["omega2"] for p in pts])
    P = [pts[i] for i in idx]
    w = np.array([p["omega"] for p in P]); Q = np.array([p["Q"] for p in P])
    dQ = np.gradient(Q, w)
    for p, d in zip(P, dQ):
        p["dQdw"] = float(d)
    st = [p for p in P if p["dQdw"] < 0]
    un = [p for p in P if p["dQdw"] > 0]
    st.sort(key=lambda p: p["Q"]); un.sort(key=lambda p: p["Q"])
    return P, st, un


def pvals(br):
    Q = np.array([p["Q"] for p in br]); E = np.array([p["E"] for p in br])
    if len(br) < 3:
        return np.full(len(br), np.nan)
    p = np.gradient(np.log(E), np.log(Q))
    return p


def longest_band(br, p, lo=0.70, hi=0.80):
    best = (1.0, None, None)
    i = 0
    n = len(br)
    while i < n:
        if lo <= p[i] <= hi:
            j = i
            while j + 1 < n and lo <= p[j + 1] <= hi:
                j += 1
            ratio = br[j]["Q"] / br[i]["Q"]
            if ratio > best[0] or best[1] is None:
                best = (ratio, br[i]["Q"], br[j]["Q"])
            i = j + 1
        else:
            i += 1
    return dict(ratio=best[0], Qlo=best[1], Qhi=best[2])


def dEdQ_check(P):
    """Trapez-Probe je Intervall entlang omega: Delta E gegen omega_mitte * Delta Q."""
    devs = []
    for a, b in zip(P[:-1], P[1:]):
        dQ = b["Q"] - a["Q"]; dE = b["E"] - a["E"]
        if abs(dQ) / max(a["Q"], b["Q"]) < 1e-2:
            continue
        wm = 0.5 * (a["omega"] + b["omega"])
        devs.append(abs(dE - wm * dQ) / abs(wm * dQ))
    devs = np.array(devs)
    # zentrale Differenz an Punkten (nur Q-Ast-artig, wo Q monoton)
    return dict(n=int(devs.size), max_rel=float(devs.max()) if devs.size else None,
                median_rel=float(np.median(devs)) if devs.size else None)


def thin_fit(st, key, Rmin=50.0):
    sel = [p for p in st if p["Rhalf"] >= Rmin]
    if len(sel) < 4:
        return None
    x = np.array([p["Q"] ** (-1 / 3) for p in sel]); y = np.array([p[key] for p in sel])
    c = np.polyfit(x, y, 2)
    return dict(limit=float(c[-1]), n=len(sel), Qlo=sel[0]["Q"], Qhi=sel[-1]["Q"],
                raw_at_Qmax=float(y[-1]), Qmax=sel[-1]["Q"])


def control_cmp(res, key):
    pts = res["points"]; ctl = res[key]
    out = dict(mu=[], Q=[])
    fails = 0
    for p, c in zip(pts, ctl):
        if not c.get("ok", False):
            fails += 1; continue
        if p["sweep"] == "mu":
            out["mu"].append((abs(c["Q"] / p["Q"] - 1), abs(c["E"] / p["E"] - 1)))
        else:
            out["Q"].append((abs(c["E"] / p["E"] - 1), abs(c["omega"] / p["omega"] - 1)))
    r = dict(fails=fails)
    if out["mu"]:
        a = np.array(out["mu"]); r["mu_maxrel_Q"] = float(a[:, 0].max()); r["mu_maxrel_E"] = float(a[:, 1].max())
    if out["Q"]:
        a = np.array(out["Q"]); r["Q_maxrel_E"] = float(a[:, 0].max()); r["Q_maxrel_omega"] = float(a[:, 1].max())
    r["vir_max"] = float(max(c["vir"] for c in ctl if c.get("ok")))
    return r


summary = {}
data = {}
for m in ("M1", "M2", "M3"):
    res = load(m)
    P, st, un = branches(res["points"])
    pst, pun = pvals(st), pvals(un)
    for p, v in zip(st, pst):
        p["p"] = float(v)
    for p, v in zip(un, pun):
        p["p"] = float(v)
    for p in P:
        p["p_wQE"] = p["omega"] * p["Q"] / p["E"]
    qmin = min(P, key=lambda p: p["Q"])
    s = dict(n_points=len(P), n_stable=len(st), n_unstable=len(un),
             Qmin=qmin["Q"], omega2_at_Qmin=qmin["omega2"], EQ_at_Qmin=qmin["EQ"],
             largest_Q_stable=st[-1]["Q"] if st else None,
             largest_omega2=max(p["omega2"] for p in P),
             vir_max=max(p["vir"] for p in P), err_max=max(p["err"] for p in P),
             nodes_total=sum(p["nodes"] for p in P), chi_monoton_all=all(p["chimono"] for p in P),
             ftail_max=max(p["ftail"] for p in P), gtail_max=max(p["gtail"] for p in P),
             band_stable=longest_band(st, pst), band_unstable=longest_band(un, pun),
             p_range_stable=[float(np.nanmin(pst)), float(np.nanmax(pst))],
             p_range_unstable=[float(np.nanmin(pun)), float(np.nanmax(pun))] if len(un) >= 3 else None,
             dEdQ=dEdQ_check(P),
             p_neighbor_vs_wQE_maxdiff_stable=float(np.nanmax(np.abs(pst - np.array([p["p_wQE"] for p in st])))),
             p_neighbor_vs_wQE_maxdiff_unstable=float(np.nanmax(np.abs(pun - np.array([p["p_wQE"] for p in un])))) if len(un) >= 3 else None,
             control_fine=control_cmp(res, "control_fine"), control_bigR=control_cmp(res, "control_bigR"),
             laufzeit_s=res["laufzeit_s"])
    top = max(P, key=lambda p: p["omega2"])
    s["thick_end"] = dict(omega2=top["omega2"], Q=top["Q"], EQ=top["EQ"], S0=top["S0"], chi0=top["chi0"], h=top["h"])
    big = st[-1]
    s["at_largest_Q_stable"] = dict(Q=big["Q"], omega=big["omega"], omega2=big["omega2"], EQ=big["EQ"], S0=big["S0"],
                                   chi0=big["chi0"], h=big["h"], Rhalf=big["Rhalf"], p_wQE=big["p_wQE"],
                                   E_over_Q34=big["E"] / big["Q"] ** 0.75)
    if m in ("M1", "M2"):
        s["thin_fit"] = {k: thin_fit(st, k) for k in ("EQ", "S0", "chi0", "h", "omega")}
        # dieselbe Extrapolation auf dem feinen Gitter (Q-Punkte bei gleichem Q)
        fine = [dict(c, Rhalf=c["Rhalf"]) for p, c in zip(res["points"], res["control_fine"])
                if c.get("ok") and p["sweep"] in ("Q", "seed")]
        fine.sort(key=lambda p: p["Q"])
        s["thin_fit_fine"] = {k: thin_fit(fine, k) for k in ("EQ", "S0", "h")}
        s["desk"] = dict(omega0=float(W0[m]), S0=1.0 if m == "M1" else float(S0M2),
                         h_inner=None if m == "M1" else float(0.25 / (2 * W0[m] ** 2 * S0M2)))
    if m == "M3":
        a, b = st[-2], st[-1]
        s["B7"] = dict(Q=b["Q"], p_backward=float(np.log(b["E"] / a["E"]) / np.log(b["Q"] / a["Q"])),
                       p_wQE=b["p_wQE"], h=b["h"], E_over_Q34=b["E"] / b["Q"] ** 0.75, Rhalf=b["Rhalf"])
        near = min(st, key=lambda p: abs(np.log(p["Q"] / 1e4)))
        s["M3_near_1e4"] = dict(Q=near["Q"], p=near["p"], p_wQE=near["p_wQE"], h=near["h"],
                                E_over_Q34=near["E"] / near["Q"] ** 0.75)
        near = min(st, key=lambda p: abs(np.log(p["Q"] / 1e3)))
        s["M3_near_1e3"] = dict(Q=near["Q"], p=near["p"], p_wQE=near["p_wQE"], h=near["h"],
                                E_over_Q34=near["E"] / near["Q"] ** 0.75)
    summary[m] = s
    data[m] = dict(P=P, st=st, un=un)

# ---------- Wertung ----------
V = {}
f1 = summary["M1"]["thin_fit"]
V["B1"] = dict(EQ_limit=f1["EQ"]["limit"], S0_limit=f1["S0"]["limit"],
               EQ_raw=f1["EQ"]["raw_at_Qmax"], S0_raw=f1["S0"]["raw_at_Qmax"], Qmax=f1["EQ"]["Qmax"],
               ok=bool(abs(f1["EQ"]["limit"] - 0.70711) <= 0.0071 and abs(f1["S0"]["limit"] - 1) <= 0.01))
b2 = [summary["M1"]["band_stable"], summary["M1"]["band_unstable"]]
V["B2"] = dict(stable=b2[0], unstable=b2[1], ok=bool(all(b["ratio"] < 3 for b in b2)))
s2 = summary["M2"]
V["B3"] = dict(chi0_largestQ=s2["at_largest_Q_stable"]["chi0"], Q=s2["at_largest_Q_stable"]["Q"],
               chi0_thick=s2["thick_end"]["chi0"], omega2_thick=s2["thick_end"]["omega2"],
               ok=bool(s2["at_largest_Q_stable"]["chi0"] < 0.1 and s2["thick_end"]["chi0"] > 0.8
                       and s2["thick_end"]["omega2"] >= 1.95))
f2 = s2["thin_fit"]
V["B4"] = dict(EQ_limit=f2["EQ"]["limit"], S0_limit=f2["S0"]["limit"], EQ_raw=f2["EQ"]["raw_at_Qmax"],
               S0_raw=f2["S0"]["raw_at_Qmax"],
               ok=bool(abs(f2["EQ"]["limit"] - 0.853) <= 0.01 and abs(f2["S0"]["limit"] - 1.18) <= 0.02))
V["B5"] = dict(h_limit=f2["h"]["limit"], h_raw=f2["h"]["raw_at_Qmax"],
               ok=bool(0.13 <= f2["h"]["limit"] <= 0.17))
b6 = [s2["band_stable"], s2["band_unstable"]]
V["B6"] = dict(stable=b6[0], unstable=b6[1], ok=bool(all(b["ratio"] < 3 for b in b6)))
b7 = summary["M3"]["B7"]
V["B7"] = dict(b7, ok=bool(0.72 <= b7["p_backward"] <= 0.78 and 0.22 <= b7["h"] <= 0.28
                           and 3.56 <= b7["E_over_Q34"] <= 4.82 and b7["Q"] >= 1000))
summary["Wertung"] = V
with open(os.path.join(OUT, "auswertung.json"), "w") as fh:
    json.dump(summary, fh, indent=1)

# Punkttabellen (CSV) je Modell
for m in ("M1", "M2", "M3"):
    with open(os.path.join(OUT, f"punkte-{m}.csv"), "w") as fh:
        keys = ["sweep", "omega2", "omega", "Q", "E", "EQ", "S0", "chi0", "h", "vir", "Rhalf", "dQdw", "p", "p_wQE"]
        fh.write(",".join(keys + ["ast"]) + "\n")
        for p in data[m]["P"]:
            ast = "stabil" if p["dQdw"] < 0 else "instabil"
            fh.write(",".join(str(p.get(k, "")) for k in keys) + f",{ast}\n")

# ---------- Abbildungen ----------
C = {"st": "#1f5fa8", "un": "#c8553d", "ref": "#555555"}


def ax_branches(ax, m, key, logy=False, label=None):
    st, un = data[m]["st"], data[m]["un"]
    ax.plot([p["Q"] for p in st], [p[key] for p in st], "-", color=C["st"], lw=1.6, label="stabil (dQ/dw<0)")
    ax.plot([p["Q"] for p in un], [p[key] for p in un], "--", color=C["un"], lw=1.4, label="instabil (dQ/dw>0)")
    ax.set_xscale("log")
    if logy:
        ax.set_yscale("log")


fig, axs = plt.subplots(1, 3, figsize=(15, 4.4))
for ax, m in zip(axs, ("M1", "M2", "M3")):
    ax_branches(ax, m, "EQ")
    if m in ("M1", "M2"):
        ax.axhline(W0[m], color=C["ref"], lw=0.9, ls=":", label=f"omega_0 = {W0[m]:.4f}")
    else:
        q = np.logspace(np.log10(30), 5, 100)
        ax.plot(q, 4 * np.pi / 3 * q ** -0.25, ":", color=C["ref"], lw=1.0, label="Beutel 4,19 Q^(-1/4)")
    ax.set_title(f"{m}: E/Q gegen Q"); ax.set_xlabel("Q"); ax.set_ylabel("E/Q"); ax.legend(fontsize=8)
fig.tight_layout(); fig.savefig(os.path.join(OUT, "abb1-EQ.png"), dpi=130); plt.close(fig)

fig, axs = plt.subplots(1, 3, figsize=(15, 4.4))
for ax, m in zip(axs, ("M1", "M2", "M3")):
    ax_branches(ax, m, "p")
    st = data[m]["st"]
    ax.plot([p["Q"] for p in st], [p["p_wQE"] for p in st], ".", color=C["st"], ms=3, label="omega Q/E (Probe)")
    ax.axhline(0.75, color=C["ref"], lw=0.9, ls=":"); ax.axhline(1.0, color=C["ref"], lw=0.9, ls="-.")
    ax.axhspan(0.70, 0.80, color="#dddddd", alpha=0.5, lw=0)
    ax.set_ylim(0.5, 1.05)
    ax.set_title(f"{m}: p = d ln E / d ln Q"); ax.set_xlabel("Q"); ax.set_ylabel("p"); ax.legend(fontsize=8)
fig.tight_layout(); fig.savefig(os.path.join(OUT, "abb2-p.png"), dpi=130); plt.close(fig)

fig, axs = plt.subplots(1, 3, figsize=(15, 4.4))
for ax, m in zip(axs, ("M1", "M2", "M3")):
    st, un = data[m]["st"], data[m]["un"]
    ax.plot([p["Q"] for p in st], [p["S0"] for p in st], "-", color=C["st"], lw=1.6, label="S(0) stabil")
    ax.plot([p["Q"] for p in un], [p["S0"] for p in un], "--", color=C["st"], lw=1.2, label="S(0) instabil")
    if m != "M1":
        ax.plot([p["Q"] for p in st], [p["chi0"] for p in st], "-", color=C["un"], lw=1.6, label="chi(0) stabil")
        ax.plot([p["Q"] for p in un], [p["chi0"] for p in un], "--", color=C["un"], lw=1.2, label="chi(0) instabil")
    ax.set_xscale("log")
    if m == "M3":
        ax.set_yscale("log")
    ax.set_title(f"{m}: S(0) und chi(0)"); ax.set_xlabel("Q"); ax.legend(fontsize=8)
fig.tight_layout(); fig.savefig(os.path.join(OUT, "abb3-S0-chi0.png"), dpi=130); plt.close(fig)

fig, axs = plt.subplots(3, 3, figsize=(14, 10))
targets = {"M1": [3e2, 1e5, 1e7], "M2": [3e2, 1e5, 1e7], "M3": [1e3, 1e4, 1e5]}
for row, m in enumerate(("M1", "M2", "M3")):
    z = np.load(os.path.join(D, m + "-profile.npz"))
    Qs = z["Q"]; sw = z["sweep"]; om2 = z["omega2"]
    stQ = {p["Q"] for p in data[m]["st"]}
    for col, qt in enumerate(targets[m]):
        cand = [k for k in range(len(Qs)) if Qs[k] in stQ]
        k = min(cand, key=lambda k: abs(np.log(Qs[k] / qt)))
        ax = axs[row, col]
        r = z["r"]; f = z["f"][k]; g = z["g"][k]
        Rh = [p["Rhalf"] for p in data[m]["P"] if p["Q"] == Qs[k]][0]
        rmax = min(r[-1], 1.6 * Rh + 15) if m != "M3" else min(r[-1], 3.0 * Rh + 8)
        sel = r <= rmax
        ax.plot(r[sel], f[sel], "-", color=C["st"], lw=1.6, label="f")
        if m != "M1":
            ax.plot(r[sel], g[sel], "-", color=C["un"], lw=1.4, label="g = chi")
        ax.set_title(f"{m}: Q = {Qs[k]:.3g}, omega^2 = {om2[k]:.4f}")
        ax.set_xlabel("r"); ax.legend(fontsize=8)
fig.tight_layout(); fig.savefig(os.path.join(OUT, "abb4-profile.png"), dpi=120); plt.close(fig)
print(json.dumps(summary["Wertung"], indent=1))

# ---------- Nachtrag 1 (PLAN-NACHTRAG-1.md): N1 drittes Gitter, N2 Spline-Probe, N3 Konkurrenz, N4 Wiederholung ----------
from scipy.interpolate import CubicSpline

D1 = sys.argv[3] if len(sys.argv) > 3 else None  # Ordner von Lauf 1 (Reproduktion)
NT = {}
for m in ("M1", "M2", "M3"):
    res = load(m)
    pts, c2, c3 = res["points"], res["control_fine"], res.get("control_fine2", [])
    n1 = dict(mu_ratioQ=[], mu_ratioE=[], Q_ratioE=[], mu_rel_02_01_Q=[], mu_rel_02_01_E=[], Q_rel_02_01_E=[],
              Q_rel_02_01_omega=[], vir_max_01=None)
    for p, a, b in zip(pts, c2, c3):
        if not (a.get("ok") and b.get("ok")):
            continue
        if p["sweep"] == "mu":
            for key, lst, rel in (("Q", n1["mu_ratioQ"], n1["mu_rel_02_01_Q"]), ("E", n1["mu_ratioE"], n1["mu_rel_02_01_E"])):
                d1, d2 = p[key] - a[key], a[key] - b[key]
                if abs(d2) > 0:
                    lst.append(d1 / d2)
                rel.append(abs(a[key] / b[key] - 1))
        else:
            d1, d2 = p["E"] - a["E"], a["E"] - b["E"]
            if abs(d2) > 0:
                n1["Q_ratioE"].append(d1 / d2)
            n1["Q_rel_02_01_E"].append(abs(a["E"] / b["E"] - 1))
            n1["Q_rel_02_01_omega"].append(abs(a["omega"] / b["omega"] - 1))
    out = {}
    for k, v in n1.items():
        if isinstance(v, list) and v:
            arr = np.array(v)
            if "ratio" in k:
                out[k] = dict(median=float(np.median(arr)), p10=float(np.percentile(arr, 10)), p90=float(np.percentile(arr, 90)))
            else:
                out[k] = float(arr.max())
    out["vir_max_dr001"] = float(max(c["vir"] for c in c3 if c.get("ok"))) if c3 else None
    out["fails_dr001"] = int(sum(not c.get("ok", False) for c in c3))
    # N2: Spline-Probe je Ast
    n2 = {}
    for name, br in (("stabil", data[m]["st"]), ("instabil", data[m]["un"])):
        if len(br) < 4:
            continue
        x = np.log([p["Q"] for p in br]); y = np.array([p["omega"] * p["Q"] for p in br])
        E = np.array([p["E"] for p in br])
        cs = CubicSpline(x, y)
        dev = np.array([abs((E[k + 1] - E[k]) - cs.integrate(x[k], x[k + 1])) / abs(E[k + 1] - E[k])
                        for k in range(len(br) - 1)])
        n2[name] = dict(n=int(dev.size), max_rel=float(dev.max()), max_rel_ohne_2_an_Faltung=float(dev[2:].max()),
                        median_rel=float(np.median(dev)))
    out["N2_spline_dEdQ"] = n2
    out["N3_konkurrenz"] = res.get("konkurrenz")
    if D1:
        with open(os.path.join(D1, m + ".json")) as fh:
            r1 = json.load(fh)
        mx = 0.0
        for a, b in zip(r1["points"], pts):
            for key in ("Q", "E", "omega"):
                mx = max(mx, abs(a[key] / b[key] - 1))
        out["N4_reproduktion_maxrel"] = mx
        out["N4_punkte_lauf1_lauf2"] = [len(r1["points"]), len(pts)]
    NT[m] = out
k3 = os.path.join(D, "M3-konkurrenz-dt001.json")
if os.path.exists(k3):
    with open(k3) as fh:
        NT["M3"]["N3_konkurrenz_dt001"] = json.load(fh)
summary["Nachtrag1"] = NT
with open(os.path.join(OUT, "auswertung.json"), "w") as fh:
    json.dump(summary, fh, indent=1)
print(json.dumps(NT, indent=1, default=str)[:6000])
