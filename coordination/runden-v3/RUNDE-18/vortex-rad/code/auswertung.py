#!/usr/bin/env python3
"""Auswertung VORTEX-RAD: W1 bis W5 nach PLAN.md Abschnitt 5, Stabilitaetskarten, Kontrollen, Abbildungen.
Aufruf: python auswertung.py <ordner mit scan_J*.json, lokal.json, kontrolle.json, nmax.json, zeit.json>
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import json
import sys
from collections import defaultdict

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vortex_rad as vr  # noqa: E402

AUS = sys.argv[1]
PRIM = {5, 7, 11, 13, 17, 19, 23}
JS = (0.02, 0.05, 0.1)
ASTE = ("klein", "gross")
NS = list(range(4, 25))
TXT = []


def p(*a):
    s = " ".join(str(x) for x in a)
    print(s, flush=True)
    TXT.append(s)


def lade(name):
    with open(os.path.join(AUS, name)) as fh:
        return json.load(fh)


def jkey(J):
    return "%g" % J


import glob  # noqa: E402

U = []
for J in JS:
    for fn in sorted(glob.glob(os.path.join(AUS, "scan_J%s.json" % jkey(J))) +
                     glob.glob(os.path.join(AUS, "scan_J%s_teil*.json" % jkey(J)))):
        U += lade(os.path.basename(fn))["punkte"]
conv = [q for q in U if q["konvergiert"]]
erg = {}

# ------------------------------------------------------------------ W1
nb = [q for q in conv if "neustart_ok" in q]
w1 = {"punkte": len(U), "konvergiert": len(conv),
      "nicht_konvergiert": [(q["N"], q["m"], q["J"], q["ast"], round(q["c"], 4), q["grund"]) for q in U
                            if not q["konvergiert"]][:20],
      "pfad_A": sum(q["pfad"] == "A" for q in conv), "pfad_B": sum(q["pfad"] == "B" for q in conv),
      "max_formel_abw": max(q["formel_abw"] for q in conv),
      "max_formel_abw_pfadA": max([q["formel_abw"] for q in conv if q["pfad"] == "A"], default=None),
      "max_nabe": max(q["nabe"] for q in conv), "max_phasen_abw": max(q["phasen_abw"] for q in conv),
      "max_residuum": max(q["residuum"] for q in conv),
      "neustart_ok": sum(q["neustart_ok"] for q in nb), "neustart_gesamt": len(nb),
      "neustart_max_abw": max([q["neustart_abw"] for q in nb if q["neustart_ok"]], default=None),
      "neustart_max_nabe": max([q["neustart_nabe"] for q in nb if q["neustart_ok"]], default=None),
      "neustart_abw_gt_1e-8": sum(1 for q in nb if q["neustart_ok"] and q["neustart_abw"] > 1e-8)}
w1["eingetroffen"] = bool(len(conv) == len(U) and w1["max_formel_abw"] <= 1e-10 and w1["max_nabe"] <= 1e-10)
erg["W1"] = w1
p("W1", json.dumps(w1))

# ------------------------------------------------------------------ f(N, m)
grp = defaultdict(list)
for q in conv:
    grp[(q["J"], q["ast"], q["N"], q["m"])].append(q)
for k in grp:
    grp[k].sort(key=lambda q: q["c"])
f = {k: float(np.mean([q["maxRe"] <= vr.TOL for q in v])) for k, v in grp.items()}


def domtyp(k):
    v = [q["dom"] for q in grp[k] if q["maxRe"] > vr.TOL]
    if not v:
        return ""
    nr, no = v.count("reell"), v.count("oszillatorisch")
    return "r" if nr > no else ("o" if no > nr else "g")


# ------------------------------------------------------------------ W2
w2tab = {jkey(J): {N: f.get((J, "gross", N, 1)) for N in NS} for J in JS}
anz = {jkey(J): sum(1 for N in NS if (f.get((J, "gross", N, 1)) or 0) >= 0.5) for J in JS}
erg["W2"] = {"f_gross_m1": w2tab, "anzahl_N_stabil": anz, "eingetroffen": bool(anz["0.02"] >= 14)}
p("W2", json.dumps(erg["W2"]))


# ------------------------------------------------------------------ W3
def schwelle(xs, ys):
    xs = np.array(xs, float)
    ys = np.array(ys, bool)
    ux = np.unique(xs)
    kand = [ux[0] - 1] + list((ux[:-1] + ux[1:]) / 2) + [ux[-1] + 1]
    best = None
    for t in kand:
        for richtung in ("stabil_unter", "stabil_ueber"):
            pred = xs < t if richtung == "stabil_unter" else xs > t
            err = int(np.sum(pred != ys))
            if best is None or err < best[0]:
                best = (err, float(t), richtung, pred)
    return best


w3 = {"kombis": {}}
fehl_prim = fehl_zus = n_prim = n_zus = 0
beide = 0
a_ok = True
for J in JS:
    for ast in ASTE:
        paare = [(N, m) for N in NS for m in range(1, N // 2 + 1) if (J, ast, N, m) in f]
        xs = [m / N for N, m in paare]
        ys = [f[(J, ast, N, m)] >= 0.5 for N, m in paare]
        kombi = {"paare": len(paare), "stabil": int(sum(ys))}
        hoch = [f[(J, ast, N, m)] for N, m in paare if m / N >= 0.45]
        kombi["f_mittel_mN_ab_0.45"] = float(np.mean(hoch)) if hoch else None
        kombi["f_mittel_alle"] = float(np.mean([f[(J, ast, N, m)] for N, m in paare])) if paare else None
        if 0 < sum(ys) < len(ys):
            beide += 1
            err, t, richtung, pred = schwelle(xs, ys)
            acc = 1 - err / len(ys)
            kombi.update(schwelle=t, richtung=richtung, fehler=err, trefferquote=acc)
            falsch = [paare[i] for i in range(len(ys)) if pred[i] != ys[i]]
            kombi["falsch"] = falsch
            if acc < 0.9:
                a_ok = False
            for i, (N, m) in enumerate(paare):
                if N in PRIM:
                    n_prim += 1
                    fehl_prim += int(pred[i] != ys[i])
                else:
                    n_zus += 1
                    fehl_zus += int(pred[i] != ys[i])
        else:
            kombi["einheitlich"] = True
        w3["kombis"]["%s_%s" % (jkey(J), ast)] = kombi
w3["kombis_mit_beiden"] = beide
w3["a"] = bool(a_ok and beide >= 3)
w3["fehlerquote_prim"] = fehl_prim / n_prim if n_prim else None
w3["fehlerquote_zusammengesetzt"] = fehl_zus / n_zus if n_zus else None
w3["b"] = bool(n_prim == 0 or (fehl_prim / n_prim) <= (fehl_zus / max(n_zus, 1)) + 0.10)
w3["eingetroffen"] = bool(w3["a"] and w3["b"])
erg["W3"] = w3
p("W3", json.dumps(w3))


# ------------------------------------------------------------------ W4
def f_interp(J, ast, N, x):
    ms = [m for m in range(1, N // 2 + 1) if (J, ast, N, m) in f]
    if not ms:
        return np.nan
    return float(np.interp(x, [m / N for m in ms], [f[(J, ast, N, m)] for m in ms]))


w4 = {}
alle_ok = True
for Ns in (11, 19):
    for J in JS:
        for ast in ASTE:
            d = []
            for m in range(1, Ns // 2 + 1):
                if (J, ast, Ns, m) not in f:
                    continue
                x = m / Ns
                nbw = np.nanmean([f_interp(J, ast, Ns - 1, x), f_interp(J, ast, Ns + 1, x)])
                d.append(f[(J, ast, Ns, m)] - nbw)
            D = float(np.mean(d)) if d else None
            w4["N%d_%s_%s" % (Ns, jkey(J), ast)] = {"Delta": D, "je_m": [round(x, 3) for x in d]}
            if D is None or D > 0.10:
                alle_ok = False
w4["eingetroffen"] = bool(alle_ok)
erg["W4"] = w4
p("W4", json.dumps(w4))

# ------------------------------------------------------------------ W5
inst = [q for q in conv if q["maxRe"] > vr.TOL]
osz = [q for q in inst if q["dom"] == "oszillatorisch"]
w5 = {"instabil": len(inst), "oszillatorisch_dominant": len(osz),
      "anteil": len(osz) / len(inst) if inst else None,
      "mit_reellem_paar": sum(1 for q in inst if q["N_r"] > 0),
      "art_zaehlung": {a: sum(1 for q in inst if q["art"] == a) for a in ("reell", "oszillatorisch", "gemischt")}}
for ast in ASTE:
    for J in JS:
        ii = [q for q in inst if q["ast"] == ast and q["J"] == J]
        oo = [q for q in ii if q["dom"] == "oszillatorisch"]
        w5["%s_%s" % (ast, jkey(J))] = {"instabil": len(ii), "oszillatorisch": len(oo)}
belegt = 0
for q in osz:
    v = grp[(q["J"], q["ast"], q["N"], q["m"])]
    i = next(k for k, x in enumerate(v) if x["c"] == q["c"])
    nbs = [v[k] for k in (i - 1, i + 1) if 0 <= k < len(v)]
    if any(x["maxRe"] <= vr.TOL and x["n_minus"] >= 1 for x in nbs):
        belegt += 1
w5["osz_mit_stabilem_nachbarn_nKminus"] = belegt
w5["osz_im_max"] = max([q["dom_im"] for q in osz], default=None)
w5["eingetroffen"] = bool(inst and len(osz) / len(inst) > 0.5)
erg["W5"] = w5
p("W5", json.dumps(w5))

# ------------------------------------------------------------------ Technische Kontrollen U
tk = {"kks_abweichung": sum(1 for q in conv if q["kks_l"] != q["kks_r"]),
      "kks_abweichung_ohne_unklar": sum(1 for q in conv if q["kks_l"] != q["kks_r"] and q["krein_unklar"] == 0),
      "krein_unklar_punkte": sum(1 for q in conv if q["krein_unklar"] > 0),
      "max_null_betrag": max(q["null_betrag"] for q in conv),
      "weitere_null_punkte": sum(1 for q in conv if q["weitere_null"] > 0),
      "art_aendert_sich_1e-6": sum(1 for q in conv if q["art"] != q["art_1e-6"]),
      "art_aendert_sich_1e-10": sum(1 for q in conv if q["art"] != q["art_1e-10"]),
      "stabil_mit_nKminus": sum(1 for q in conv if q["maxRe"] <= vr.TOL and q["n_minus"] > 0)}
kks_bsp = [(q["N"], q["m"], q["J"], q["ast"], round(q["c"], 4), q["kks_l"], q["kks_r"], q["krein_unklar"])
           for q in conv if q["kks_l"] != q["kks_r"]][:15]
tk["kks_beispiele"] = kks_bsp
erg["technik_U"] = tk
p("TECHNIK_U", json.dumps(tk))

# ------------------------------------------------------------------ Stabilitaetskarten (Text)
karten = {}
for J in JS:
    for ast in ASTE:
        zeilen = ["m\\N " + "".join("%4d" % N for N in NS)]
        for m in range(1, 13):
            z = "%3d " % m
            for N in NS:
                k = (J, ast, N, m)
                if m > N // 2:
                    z += "    "
                elif k not in f:
                    z += "   x"
                else:
                    fv = f[k]
                    a = "S" if fv == 1 else ("T" if fv > 0 else "-")
                    z += "%4s" % (a + (domtyp(k) if fv < 1 else ""))
            zeilen.append(z)
        karten["%s_%s" % (jkey(J), ast)] = zeilen
        p("KARTE J=%s Ast=%s (S alle stabil, T teils, - keiner; r/o/g dominante Instabilitaet)" % (jkey(J), ast))
        for z in zeilen:
            p(z)
erg["karten"] = karten

# Krein-Uebersicht stabiler Punkte je Ast und m/N-Seite
kr = {}
for ast in ASTE:
    for seite, sel in (("mN_unter_0.25", lambda q: q["m"] / q["N"] < 0.25), ("mN_0.25", lambda q: q["m"] * 4 == q["N"]),
                       ("mN_ueber_0.25", lambda q: q["m"] / q["N"] > 0.25)):
        st = [q for q in conv if q["ast"] == ast and sel(q) and q["maxRe"] <= vr.TOL]
        alle = [q for q in conv if q["ast"] == ast and sel(q)]
        kr["%s_%s" % (ast, seite)] = {"punkte": len(alle), "stabil": len(st),
                                      "stabil_mit_nKminus": sum(1 for q in st if q["n_minus"] > 0),
                                      "instabil_reell_dom": sum(1 for q in alle if q["dom"] == "reell"),
                                      "instabil_osz_dom": sum(1 for q in alle if q["dom"] == "oszillatorisch")}
erg["krein_uebersicht"] = kr
p("KREIN", json.dumps(kr))

# ------------------------------------------------------------------ Lokal
LO = {"L-a": [], "L-b": [], "L-c": []}
for fn in sorted(glob.glob(os.path.join(AUS, "lokal*.json"))):
    teil = lade(os.path.basename(fn))
    for fam in LO:
        LO[fam] += teil[fam]
lok = {}
for fam in ("L-a", "L-b"):
    g2 = defaultdict(list)
    for r in LO[fam]:
        key = (r["N"], r.get("K", 3), r.get("m", 1), r["J"], r["ast"])
        g2[key].append(r)
    zus = []
    for key, v in sorted(g2.items()):
        ex = [r for r in v if r["existiert"]]
        st = [r for r in ex if r["maxRe"] <= vr.TOL]
        doms = [r["dom"] for r in ex if r["maxRe"] > vr.TOL]
        zus.append({"N": key[0], "K": key[1], "m": key[2], "J": key[3], "ast": key[4], "existiert": len(ex),
                    "raster": len(v), "w2_min": min([r["w2"] for r in ex], default=None),
                    "w2_max": max([r["w2"] for r in ex], default=None), "stabil": len(st),
                    "reell": doms.count("reell"), "osz": doms.count("oszillatorisch"),
                    "kks_abw": sum(1 for r in ex if r["kks_l"] != r["kks_r"]),
                    "max_res": max([r["residuum"] for r in ex], default=None),
                    "gruende": sorted(set(r["grund"] for r in v if not r["existiert"]))})
    lok[fam] = zus
    for z in zus:
        p(fam, json.dumps(z))
lc = LO["L-c"]
lok["L-c"] = {"versuche": len(lc), "existiert": sum(r["existiert"] for r in lc),
              "gruende": {g: sum(1 for r in lc if r.get("grund") == g) for g in ("ok", "newton", "sprung", "null")},
              "konvergiert_aber_kein_wirbel": sum(1 for r in lc if r.get("grund") == "ok" and not r["existiert"])}
p("L-c", json.dumps(lok["L-c"]))
erg["lokal"] = lok

# ------------------------------------------------------------------ Kontrolle V5
KT = lade("kontrolle.json")["punkte"]
kv = {}
for J in (0.05, 0.1):
    for mode in ("ring", "zentrum"):
        for ast in ASTE:
            gg = defaultdict(list)
            for r in KT:
                if r["J"] == J and r["mode"] == mode and r["ast"] == ast:
                    gg[r["N"]].append(r)
            if not gg:
                kv["%s_%s_%s" % (jkey(J), mode, ast)] = {"existiert_fuer_N": []}
                continue
            mins = [min(r["w2"] for r in v) for v in gg.values()]
            maxs = [max(r["w2"] for r in v) for v in gg.values()]
            stmax = [max([r["w2"] for r in v if r["maxRe"] <= vr.TOL], default=np.nan) for v in gg.values()]
            kv["%s_%s_%s" % (jkey(J), mode, ast)] = {
                "existiert_fuer_N": sorted(gg.keys()), "w2_min": [min(mins), max(mins)], "w2_max": [min(maxs), max(maxs)],
                "stabil_bis": [float(np.nanmin(stmax)), float(np.nanmax(stmax))],
                "je_N": {N: [min(r["w2"] for r in v), max(r["w2"] for r in v)] for N, v in sorted(gg.items())}
                if mode == "zentrum" else None}
regel = sum(1 for r in KT if r["v5_regel_stabil"] == (r["maxRe"] <= vr.TOL))
kv["v5_regel_trifft"] = [regel, len(KT)]
kv["kks_abweichung"] = sum(1 for r in KT if r["kks_l"] != r["kks_r"])
kv["imag_max"] = max(r["imag_max"] for r in KT)
kv["arten"] = {a: sum(1 for r in KT if r["art"] == a) for a in ("stabil", "reell", "oszillatorisch", "gemischt")}
NM = lade("nmax.json")["existenz"]
nm = {}
for J in (0.03, 0.04, 0.05, 0.06, 0.08):
    for ast in ASTE + ("beide",):
        Ns = [r["N"] for r in NM if r["J"] == J and r["anzahl"] > 0 and (ast == "beide" or r["ast"] == ast)]
        nm["%s_%s" % (jkey(J), ast)] = max(Ns) if Ns else None
kv["N_max"] = nm
erg["kontrolle_v5"] = kv
p("KONTROLLE", json.dumps(kv))

# ------------------------------------------------------------------ Zeit
ZT = lade("zeit.json")
erg["zeit"] = [{k: r.get(k) for k in ("N", "m", "J", "ast", "c", "w2", "maxRe", "art", "dom", "dom_im", "rate_fit",
                                      "dev_start", "dev_max", "dev_ende", "rel_dE", "rel_dQ", "sekunden", "status")}
               for r in ZT["laeufe"]]
erg["zeit_osz_kandidaten"] = ZT.get("oszillatorisch_kandidaten")
for r in erg["zeit"]:
    p("ZEIT", json.dumps(r))

with open(os.path.join(AUS, "auswertung.json"), "w") as fh:
    json.dump(erg, fh, indent=1)

# ------------------------------------------------------------------ Abbildungen
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

fig, axs = plt.subplots(2, 3, figsize=(16, 8.5), constrained_layout=True)
for i, ast in enumerate(ASTE):
    for jx, J in enumerate(JS):
        ax = axs[i, jx]
        M = np.full((12, len(NS)), np.nan)
        for a, N in enumerate(NS):
            for m in range(1, N // 2 + 1):
                if (J, ast, N, m) in f:
                    M[m - 1, a] = f[(J, ast, N, m)]
        im = ax.imshow(M, origin="lower", aspect="auto", cmap="cividis", vmin=0, vmax=1,
                       extent=(NS[0] - 0.5, NS[-1] + 0.5, 0.5, 12.5))
        for a, N in enumerate(NS):
            for m in range(1, N // 2 + 1):
                k = (J, ast, N, m)
                if k in f and f[k] < 1:
                    t = domtyp(k)
                    ax.text(N, m, t, ha="center", va="center", fontsize=8,
                            color="white" if f[k] < 0.5 else "black")
        xx = np.linspace(4, 24, 50)
        ax.plot(xx, xx / 4, "--", color="tab:red", lw=1.2, label="m = N/4")
        ax.plot(xx, xx / 2, ":", color="gray", lw=1)
        ax.set_xticks(NS)
        ax.set_xticklabels([("%d*" % N) if N in PRIM else str(N) for N in NS], fontsize=7)
        ax.set_yticks(range(1, 13))
        ax.set_xlim(3.5, 24.5)
        ax.set_ylim(0.5, 12.5)
        ax.set_title("Ast %s, J = %s" % (ast, jkey(J).replace(".", ",")))
        ax.set_xlabel("N (* = prim)")
        ax.set_ylabel("Ladung m")
        if i == 0 and jx == 0:
            ax.legend(loc="upper left", fontsize=8)
fig.colorbar(im, ax=axs, shrink=0.8, label="Anteil spektral stabiler Rasterpunkte f")
fig.suptitle("Stabilitaetskarte gleichfoermiger Wirbel auf dem Rad (r = reell, o = oszillatorisch, g = gemischt dominant)")
fig.savefig(os.path.join(AUS, "stabilitaetskarte.png"), dpi=110)
plt.close(fig)

fig, axs = plt.subplots(2, 3, figsize=(15, 7.5), constrained_layout=True, sharex=True, sharey=True)
for i, ast in enumerate(ASTE):
    for jx, J in enumerate(JS):
        ax = axs[i, jx]
        for N in NS:
            ms = [m for m in range(1, N // 2 + 1) if (J, ast, N, m) in f]
            xs = [m / N for m in ms]
            ys = [f[(J, ast, N, m)] for m in ms]
            if N == 11 or N == 19:
                ax.plot(xs, ys, "o-", ms=6, lw=1.2, color="tab:red" if N == 11 else "tab:blue", label="N = %d" % N,
                        zorder=3)
            elif N in PRIM:
                ax.plot(xs, ys, "s", ms=4, color="tab:orange", alpha=0.8, zorder=2,
                        label="andere Primzahl" if N == 5 else None)
            else:
                ax.plot(xs, ys, ".", ms=5, color="0.5", zorder=1, label="zusammengesetzt" if N == 4 else None)
        ax.axvline(0.25, color="tab:red", ls="--", lw=1)
        ax.set_title("Ast %s, J = %s" % (ast, jkey(J).replace(".", ",")))
        ax.set_xlabel("m/N")
        ax.set_ylabel("f")
        if i == 0 and jx == 0:
            ax.legend(fontsize=8)
fig.suptitle("Stabiler Anteil f gegen m/N")
fig.savefig(os.path.join(AUS, "stabil_mN.png"), dpi=110)
plt.close(fig)

# Wirbelprofile
cbsp = vr.c_raster()[12]
beisp = []
r, phi = vr.wirbel(12, 1, 0.1, True, cbsp)
beisp.append(("U: N = 12, m = 1, J = 0,1, gross, omega^2 = %.3f" % r["w2"], phi, r))
r, phi = vr.teilring(12, 4, 1, 0.1, False, cbsp)
beisp.append(("L-a: N = 12, K = 4, m' = 1, J = 0,1, klein, omega^2 = %.3f" % cbsp, phi, r))
r, phi = vr.dreier(11, 0.1, False, cbsp)
beisp.append(("L-b: N = 11, Orte %s, J = 0,1, klein, omega^2 = %.3f" % (vr.drei_orte(11), cbsp), phi, r))
fig, axs = plt.subplots(2, 3, figsize=(15, 9), constrained_layout=True)
for a, (titel, phi, r) in enumerate(beisp):
    ax = axs[0, a]
    ax.set_aspect("equal")
    ax.axis("off")
    if phi is None:
        ax.set_title(titel + "\n(existiert nicht)", fontsize=9)
        axs[1, a].axis("off")
        continue
    N = phi.size - 1
    ang = 2 * np.pi * np.arange(N) / N
    pos = np.stack([np.cos(ang), np.sin(ang)], 1)
    pos = np.vstack([pos, [0, 0]])
    for j in range(N):
        ax.plot([pos[j, 0], pos[(j + 1) % N, 0]], [pos[j, 1], pos[(j + 1) % N, 1]], color="0.75", lw=1)
        ax.plot([pos[j, 0], 0], [pos[j, 1], 0], color="0.88", lw=0.8)
    amax = np.max(np.abs(phi))
    sc = ax.scatter(pos[:, 0], pos[:, 1], c=np.abs(phi), cmap="viridis", vmin=0, vmax=amax, s=90, zorder=3)
    for j in range(N + 1):
        lj = 0.32 * abs(phi[j]) / amax
        if lj > 1e-3:
            ax.arrow(pos[j, 0], pos[j, 1], lj * np.cos(np.angle(phi[j])), lj * np.sin(np.angle(phi[j])),
                     head_width=0.04, color="tab:red", zorder=4, length_includes_head=True)
    st = "stabil" if r.get("maxRe", 1) <= vr.TOL else "instabil (%s, max Re %.2g)" % (r.get("dom"), r.get("maxRe"))
    ax.set_title(titel + "\n" + st, fontsize=9)
    fig.colorbar(sc, ax=ax, shrink=0.7, label="|phi_j|")
    ax2 = axs[1, a]
    jj = np.arange(N + 1)
    ax2.bar(jj, np.abs(phi), color="tab:green", alpha=0.6, label="|phi_j|")
    ax2.set_xlabel("Knoten j (N = Nabe)")
    ax2.set_ylabel("|phi_j|")
    ax3 = ax2.twinx()
    msk = np.abs(phi) > 1e-6 * amax
    ax3.plot(jj[msk], np.angle(phi[msk]) / np.pi, "o", color="tab:red", label="arg phi_j / pi")
    ax3.set_ylim(-1.1, 1.1)
    ax3.set_ylabel("arg(phi_j) / pi")
    ax2.set_title("Betrag (Balken) und Phase (Punkte)", fontsize=9)
fig.suptitle("Wirbelprofile (Pfeile: phi_j als Zeiger, Richtung = Phase, Laenge = Betrag)")
fig.savefig(os.path.join(AUS, "wirbelprofil.png"), dpi=110)
plt.close(fig)

fig, ax = plt.subplots(figsize=(8, 5), constrained_layout=True)
for r in ZT["laeufe"]:
    if "t" not in r:
        continue
    t = np.array(r["t"])
    d = np.array(r["dev"])
    lab = "N=%d m=%d %s c=%.3f J=%s" % (r["N"], r["m"], r["ast"], r["c"], jkey(r["J"]))
    line, = ax.semilogy(t, d, label=lab)
    if r["maxRe"] > vr.TOL:
        ax.semilogy(t, r["dev_start"] * np.exp(r["maxRe"] * t), "--", color=line.get_color(), lw=0.8)
ax.set_ylim(1e-8, 10)
ax.set_xlabel("t")
ax.set_ylabel("Abstand zur mitrotierenden Loesung")
ax.set_title("Zeitentwicklung; gestrichelt: exp(max Re t) aus der Linearisierung")
ax.legend(fontsize=7)
fig.savefig(os.path.join(AUS, "zeit.png"), dpi=110)
plt.close(fig)

with open(os.path.join(AUS, "auswertung.txt"), "w") as fh:
    fh.write("\n".join(TXT) + "\n")
p("auswertung fertig")
