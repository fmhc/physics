#!/usr/bin/env python3
# DIM-BEUTEL Auswertung nach PLAN.md.eingefroren-20261002-095901 Abschnitt 4, PLAN-NACHTRAG-1 (N1-N3)
# und PLAN-NACHTRAG-2 (Einhuellende, zweitrangig).
import os
for _k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_k] = "1"
import sys, json, glob, math
import numpy as np

R_Q = (3.0 * np.sqrt(5.0)) ** (1.0 / 12.0)
LNP = 12.0 * np.log(R_Q)  # ln(3 sqrt 5)
GTOL = 1e-7
KS = 40
BASE = sys.argv[1] if len(sys.argv) > 1 else "aus"
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(BASE, "auswertung")
os.makedirs(OUT, exist_ok=True)

GRAPHS = {
    "G1": dict(name="Kette 4096", auf="haupt/punkte-ket4096m20-auf.jsonl", ab="haupt/punkte-ket4096-ab.jsonl",
               kontrolle="kontrolle/punkte-ket8192m20-auf.jsonl", frisch="frisch/frisch-ket4096.jsonl",
               oben=None, d=1, soll_p=0.5, soll_h=0.5, tol_p=0.02, tol_h=0.03),
    "G2": dict(name="Quadratgitter 256^2", auf="haupt/punkte-qu256-auf.jsonl", ab="haupt/punkte-qu256-ab.jsonl",
               kontrolle="kontrolle/punkte-qu192-auf.jsonl", frisch="frisch/frisch-qu256.jsonl",
               oben="haupt/punkte-qu256-oben.jsonl", d=2, soll_p=0.667, soll_h=0.333, tol_p=0.02, tol_h=0.03),
    "G3": dict(name="kubisch 64^3", auf="haupt/punkte-kub64-auf.jsonl", ab="haupt/punkte-kub64-ab.jsonl",
               kontrolle="kontrolle/punkte-kub48-auf.jsonl", frisch="frisch/frisch-kub64.jsonl",
               oben=None, d=3, soll_p=0.75, soll_h=0.25, tol_p=0.02, tol_h=0.03),
    "G4": dict(name="Sierpinski g=10, s1", auf="haupt/punkte-sie10s1-auf.jsonl", ab="haupt/punkte-sie10s1-ab.jsonl",
               kontrolle="kontrolle/punkte-sie9s1-auf.jsonl", frisch="frisch/frisch-sie10s1.jsonl",
               oben="haupt/punkte-sie10s1-oben.jsonl", s2="kontrolle/punkte-sie10s2-auf.jsonl",
               frisch_extra="frisch/frisch-sie10s1-z3.jsonl", z4_g9="frisch/frisch-sie9s1-z4.jsonl",
               z4_s2="frisch/frisch-sie10s2-z4.jsonl",
               d=None, soll_p=None, soll_h=None),
}
P_DS = 2 * math.log(3) / (2 * math.log(3) + math.log(5))
P_DH = (math.log(3) / math.log(2)) / ((math.log(3) / math.log(2)) + 1.0)  # Karte: p = d_H/(d_H + 1) = 0,6131


def load(rel):
    if rel is None:
        return []
    p = os.path.join(BASE, rel)
    if not os.path.exists(p):
        return []
    out = []
    with open(p) as fh:
        for line in fh:
            line = line.strip()
            if line:
                try:
                    out.append(json.loads(line))
                except Exception:
                    pass
    return out


def by_k(recs):
    # letzter Eintrag je k gewinnt (Fortsetzungsaufrufe rechnen ZEITGRENZE-Punkte neu)
    d = {}
    for r in recs:
        d[int(r["k"])] = r
    return d


def converged(r):
    return (r.get("msg") != "ZEITGRENZE") and (r.get("gskal", 1.0) <= 100 * GTOL) and (r["ident"] <= 1e-6)


def valid(r):
    return converged(r) and r["chi_min"] < 0.1 and r["rand_phi"] <= 1e-6 and r["rand_chi"] <= 1e-6


def branch(cfg):
    auf = by_k(load(cfg["auf"]))
    ab = by_k(load(cfg["ab"]))
    ast = {}
    for k, r in ab.items():
        if k < KS:
            ast[k] = r
    for k, r in auf.items():
        if k >= KS:
            ast[k] = r
    return ast


def kv_of(ast):
    if KS not in ast or not valid(ast[KS]):
        return None
    k = KS
    while (k + 1) in ast and valid(ast[k + 1]):
        k += 1
    return k


def secant(ast, k1, k0):
    if k1 in ast and k0 in ast:
        return math.log(ast[k1]["E"] / ast[k0]["E"]) / (math.log(ast[k1]["Q"] / ast[k0]["Q"]))
    return None


def analyse(ast, kv, soll=None):
    res = dict(K_v=kv)
    if kv is None:
        return res
    res["Q_Kv"] = ast[kv]["Q"]
    ps = secant(ast, kv, kv - 12)
    pv = secant(ast, kv - 12, kv - 24)
    hs = [ast[j]["h"] for j in range(kv - 12, kv + 1) if j in ast]
    res["p_star"] = ps
    res["p_star_vor"] = pv
    res["h_star"] = float(np.mean(hs)) if hs else None
    res["p_loc_Kv"] = ast[kv]["p_loc"]
    if ps is not None:
        res["d_p"] = ps / (1 - ps)
    if res["h_star"]:
        res["d_h"] = 1 / res["h_star"] - 1
    # alle vollen Perioden (Sekanten) im gueltigen Bereich, rueckwaerts von K_v
    per = []
    j = kv
    while (j - 12) in ast and j - 12 >= min(ast):
        s = secant(ast, j, j - 12)
        per.append(dict(k0=j - 12, k1=j, Q0=ast[j - 12]["Q"], Q1=ast[j]["Q"], p=s,
                        gueltig=all(valid(ast[i]) for i in range(j - 12, j + 1) if i in ast)))
        j -= 12
    res["perioden"] = per
    # dE/dQ = omega: p_fd gegen Mittel p_loc
    dev = []
    for k in sorted(ast):
        if k + 1 in ast and KS <= k and k + 1 <= kv:
            pfd = math.log(ast[k + 1]["E"] / ast[k]["E"]) / math.log(ast[k + 1]["Q"] / ast[k]["Q"])
            dev.append(abs(pfd - 0.5 * (ast[k]["p_loc"] + ast[k + 1]["p_loc"])))
    if dev:
        res["dEdQ_median"] = float(np.median(dev))
        res["dEdQ_max"] = float(np.max(dev))
    # Spline-Integral von omega Q ueber ln Q
    try:
        from scipy.interpolate import CubicSpline
        ks = [k for k in sorted(ast) if KS <= k <= kv]
        x = np.array([math.log(ast[k]["Q"]) for k in ks])
        y = np.array([ast[k]["omega"] * ast[k]["Q"] for k in ks])
        cs = CubicSpline(x, y)
        integ = float(cs.integrate(x[0], x[-1]))
        dE = ast[ks[-1]]["E"] - ast[ks[0]]["E"]
        res["spline_rel"] = abs(integ - dE) / dE
        seg = []
        for i in range(len(ks) - 1):
            seg.append(abs(float(cs.integrate(x[i], x[i + 1])) - (ast[ks[i + 1]]["E"] - ast[ks[i]]["E"]))
                       / (ast[ks[i + 1]]["E"] - ast[ks[i]]["E"]))
        res["spline_seg_median"] = float(np.median(seg))
        res["spline_seg_max"] = float(np.max(seg))
    except Exception as e:
        res["spline_fehler"] = str(e)
    # Konvergenz und Identitaet
    ks_all = sorted(ast)
    res["n_punkte"] = len(ks_all)
    res["n_konvergiert"] = sum(1 for k in ks_all if converged(ast[k]))
    res["ident_max_gueltig"] = max(ast[k]["ident"] for k in range(KS, kv + 1))
    res["gskal_max_gueltig"] = max(ast[k].get("gskal", 0) for k in range(KS, kv + 1))
    res["gmax_unskal_max_gueltig"] = max(ast[k]["gmax"] for k in range(KS, kv + 1))
    return res


def plateau(ast, kv, pstar, use_win=False, tol=0.02):
    if kv is None or pstar is None:
        return None
    ks = [k for k in sorted(ast) if k <= kv and converged(ast[k])]

    def pv(k):
        if use_win:
            return secant(ast, k, k - 12) if (k - 12) in ast else None
        return ast[k]["p_loc"]

    kpl = None
    for k in reversed(ks):
        v = pv(k)
        if v is None or abs(v - pstar) > tol:
            break
        kpl = k
    if kpl is None:
        return dict(k_pl=None)
    below = [k for k in ks if k < kpl and pv(k) is not None]
    devs = [abs(pv(k) - pstar) for k in below]
    q_pl = ast[kpl]["Q"] if not use_win else ast[kpl - 12]["Q"]
    return dict(k_pl=kpl, Q_pl=q_pl, L_pl=math.log10(ast[kv]["Q"] / q_pl),
                max_abw_unterhalb=max(devs) if devs else None, a_erfuellt=(max(devs) >= 0.05) if devs else None,
                Q_min_gerechnet=ast[ks[0]]["Q"], p_loc_Qmin=pv(ks[0]) if pv(ks[0]) is not None else None,
                R_pl=ast[kpl].get("Rvol"), R_Kv=ast[kv].get("Rvol"), Rg_pl=ast[kpl].get("Rgraph"),
                Rg_Kv=ast[kv].get("Rgraph"))


def fit_inf(ast, kpl, kv, d):
    if kpl is None or kv is None:
        return None
    ks = [k for k in range(kpl, kv + 1) if k in ast]
    if len(ks) < 4:
        return None
    x = np.array([ast[k]["Q"] ** (-1.0 / (d + 1)) for k in ks])
    y = np.array([ast[k]["p_loc"] for k in ks])
    A = np.stack([np.ones_like(x), x], 1)
    c, *_ = np.linalg.lstsq(A, y, rcond=None)
    return dict(p_inf=float(c[0]), a=float(c[1]), d_inf=float(c[0] / (1 - c[0])), n=len(ks))


def envelope(cfg, ast):
    env = {}
    src = {}
    lists = [("ast", list(ast.values())), ("oben", load(cfg.get("oben"))), ("frisch", load(cfg.get("frisch"))),
             ("z3", load(cfg.get("frisch_extra")))]
    for name, recs in lists:
        for r in recs:
            k = int(r["k"])
            if not converged(r):
                continue
            if k not in env or r["E"] < env[k]["E"]:
                env[k] = r
                src[k] = name + (("-" + r["form"]) if "form" in r else "")
    return env, src


summary = {"meta": dict(r=R_Q, ln_periode=LNP, p_ds=P_DS, p_dH=P_DH, gtol=GTOL, k_s=KS)}
asts = {}
for G, cfg in GRAPHS.items():
    ast = branch(cfg)
    asts[G] = ast
    kv = kv_of(ast)
    res = analyse(ast, kv)
    res["name"] = cfg["name"]
    # Groessenkontrolle
    kon = by_k(load(cfg["kontrolle"]))
    kvk = kv_of(kon) if kon else None
    res["kontrolle_K_v"] = kvk
    if kon and kv is not None:
        common = [k for k in range(KS, min(kv, kvk if kvk is not None else KS - 1) + 1) if k in kon]
        if common:
            dE = [abs(kon[k]["E"] - ast[k]["E"]) / ast[k]["E"] for k in common]
            dp = [abs(kon[k]["p_loc"] - ast[k]["p_loc"]) for k in common]
            res["groesse_max_dE"] = max(dE)
            res["groesse_max_dp"] = max(dp)
            res["groesse_k_gemeinsam"] = [common[0], common[-1]]
            res["groesse_dp_letzt"] = dp[-1]
            res["groesse_bestanden"] = (max(dE) <= 1e-6 and max(dp) <= 1e-4)
        ak = analyse(kon, kvk) if kvk is not None else {}
        res["kontrolle_p_star"] = ak.get("p_star")
    # Fehlerband
    if res.get("p_star") is not None:
        dp_g = res.get("groesse_dp_letzt", 0.0) or 0.0
        dpv = abs(res["p_star"] - res["p_star_vor"]) if res.get("p_star_vor") is not None else float("nan")
        res["delta_p"] = dpv + dp_g
        res["delta_d"] = res["delta_p"] / (1 - res["p_star"]) ** 2
    # Startformen
    fr = load(cfg["frisch"])
    fl = []
    for r in fr:
        k = int(r["k"])
        if k in ast:
            fl.append(dict(k=k, form=r["form"], Q=r["Q"], E=r["E"], E_ast=ast[k]["E"],
                           rel=(r["E"] - ast[k]["E"]) / ast[k]["E"], konv=converged(r), Vbag=r["Vbag"],
                           Vbag_ast=ast[k]["Vbag"], chi_min=r["chi_min"]))
    res["startformen"] = fl
    if fl:
        res["startform_bestanden"] = all(abs(f["rel"]) <= 1e-6 for f in fl)
        res["startform_tiefer"] = [f for f in fl if f["rel"] < -1e-6]
    # Plateau
    if G in ("G1", "G2", "G3"):
        res["plateau"] = plateau(ast, kv, res.get("p_star"))
        pl = res["plateau"]
        if pl and pl.get("k_pl") is not None:
            res["fit_inf"] = fit_inf(ast, pl["k_pl"], kv, cfg["d"])
        ok_p = res.get("p_star") is not None and abs(res["p_star"] - cfg["soll_p"]) <= cfg["tol_p"]
        ok_h = res.get("h_star") is not None and abs(res["h_star"] - cfg["soll_h"]) <= cfg["tol_h"]
        dek = math.log10(ast[kv]["Q"] / pl["Q_pl"]) if (kv is not None and pl and pl.get("Q_pl")) else 0
        res["D"] = dict(p_ok=ok_p, h_ok=ok_h, eingetroffen=ok_p and ok_h, dekaden_plateau=dek,
                        offen=(kv is None or dek < 1.0))
    else:
        res["plateau_win"] = plateau(ast, kv, res.get("p_star"), use_win=True)
        if res.get("p_star") is not None:
            res["D4"] = dict(p_star=res["p_star"], naeher_ds=res["p_star"] < 0.5 * (P_DS + P_DH),
                             abstand_ds=abs(res["p_star"] - P_DS), abstand_dH=abs(res["p_star"] - P_DH))
        s2 = by_k(load(cfg["s2"]))
        kv2 = kv_of(s2) if s2 else None
        res["s2"] = analyse(s2, kv2) if kv2 is not None else dict(K_v=None)
        z3 = {int(r["k"]): r for r in load(cfg.get("frisch_extra"))}
        zl = []
        for k0 in sorted(z3):
            if k0 + 12 in z3:
                rr = z3[k0 + 12]["E"] / z3[k0]["E"]
                zl.append(dict(k0=k0, k1=k0 + 12, E0=z3[k0]["E"], E1=z3[k0 + 12]["E"], ratio=rr,
                               p=math.log(rr) / math.log(z3[k0 + 12]["Q"] / z3[k0]["Q"]),
                               V0=z3[k0]["Vbag"], V1=z3[k0 + 12]["Vbag"], konv=converged(z3[k0]) and converged(z3[k0 + 12])))
        res["z3_perioden"] = zl
        for zk in ("z4_g9", "z4_s2"):
            zz = {int(r["k"]): r for r in load(cfg.get(zk))}
            res[zk] = [dict(k0=k0, k1=k0 + 12, E0=zz[k0]["E"], E1=zz[k0 + 12]["E"],
                            ratio=zz[k0 + 12]["E"] / zz[k0]["E"],
                            p=math.log(zz[k0 + 12]["E"] / zz[k0]["E"]) / math.log(zz[k0 + 12]["Q"] / zz[k0]["Q"]),
                            V0=zz[k0]["Vbag"], V1=zz[k0 + 12]["Vbag"],
                            konv=converged(zz[k0]) and converged(zz[k0 + 12]),
                            E0_z3=(z3[k0]["E"] if k0 in z3 else None))
                       for k0 in sorted(zz) if k0 + 12 in zz]
        res["z3_punkte"] = [dict(k=k, Q=z3[k]["Q"], E=z3[k]["E"], p_loc=z3[k]["p_loc"], Vbag=z3[k]["Vbag"],
                                 Rgraph=z3[k]["Rgraph"], konv=converged(z3[k])) for k in sorted(z3)]
    # Einhuellende (Nachtrag 2)
    env, src = envelope(cfg, ast)
    kve = kv_of(env)
    ae = analyse(env, kve)
    diffs = []
    for k in sorted(env):
        if k in ast and src[k] != "ast":
            rel = (env[k]["E"] - ast[k]["E"]) / ast[k]["E"]
            if rel < -1e-6:
                diffs.append(dict(k=k, Q=env[k]["Q"], quelle=src[k], rel=rel, Vbag_env=env[k]["Vbag"],
                                  Vbag_ast=ast[k]["Vbag"]))
    res["einhuellende"] = dict(K_v=kve, p_star=ae.get("p_star"), p_star_vor=ae.get("p_star_vor"),
                               h_star=ae.get("h_star"), perioden=ae.get("perioden"),
                               d_p=ae.get("d_p"), tiefer_als_ast=diffs, quellen={str(k): src[k] for k in sorted(src)})
    summary[G] = res
    print(G, cfg["name"], "K_v", kv, "p*", res.get("p_star"), "h*", res.get("h_star"), "d_p", res.get("d_p"),
          "env p*", ae.get("p_star"), flush=True)

# D5
try:
    L = {G: summary[G]["plateau"]["L_pl"] for G in ("G1", "G2", "G3")}
    a_ok = all(summary[G]["plateau"]["a_erfuellt"] for G in ("G1", "G2", "G3"))
    b_ok = L["G3"] < L["G2"] and L["G3"] < L["G1"]
    summary["D5"] = dict(L_pl=L, a=a_ok, b=b_ok, eingetroffen=a_ok and b_ok)
except Exception as e:
    summary["D5"] = dict(fehler=str(e))

# d_s direkt
dsp = os.path.join(BASE, "ds", "ds.json")
if os.path.exists(dsp):
    summary["ds"] = json.load(open(dsp))

with open(os.path.join(OUT, "auswertung.json"), "w") as fh:
    json.dump(summary, fh, indent=1, default=float)

# CSV je Graph
for G, ast in asts.items():
    with open(os.path.join(OUT, f"punkte-{G}.csv"), "w") as fh:
        keys = ["k", "Q", "E", "omega", "p_loc", "h", "Echi", "ident", "gskal", "gmax", "chi_min", "chi_s",
                "phi_max", "Vbag", "Rgraph", "Rvol", "d_phimax", "rand_phi", "rand_chi", "nit", "sek", "msg"]
        fh.write(",".join(keys) + ",gueltig\n")
        for k in sorted(ast):
            r = ast[k]
            fh.write(",".join(str(r.get(c, "")) for c in keys) + f",{valid(r)}\n")

# Abbildungen
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 2, figsize=(13, 9))
for ax, G in zip(axs.ravel(), ["G1", "G2", "G3", "G4"]):
    cfg = GRAPHS[G]
    ast = asts[G]
    ks = sorted(ast)
    if not ks:
        continue
    Q = np.array([ast[k]["Q"] for k in ks])
    p = np.array([ast[k]["p_loc"] for k in ks])
    v = np.array([valid(ast[k]) for k in ks])
    ax.semilogx(Q, p, "-", color="C0", lw=1, label="p_loc = omega Q/E (Ast)")
    ax.semilogx(Q[v], p[v], "o", ms=3, color="C0")
    ax.semilogx(Q[~v], p[~v], "x", ms=4, color="C3", label="nicht gueltig")
    win = [(ast[k]["Q"], secant(ast, k, k - 12)) for k in ks if (k - 12) in ast]
    if win:
        ax.semilogx([w[0] for w in win], [w[1] for w in win], "-", color="C1", lw=2,
                    label="Sekante ueber eine Periode (bis Q)")
    kon = by_k(load(cfg["kontrolle"]))
    if kon:
        kk = sorted(kon)
        ax.semilogx([kon[k]["Q"] for k in kk], [kon[k]["p_loc"] for k in kk], ".", ms=2, color="C2",
                    label="Groessenkontrolle")
    if G == "G4":
        ax.axhline(P_DS, color="k", ls="--", lw=1, label=f"d_s: {P_DS:.4f}")
        ax.axhline(P_DH, color="0.5", ls=":", lw=1.5, label=f"d_H: {P_DH:.4f}")
        ob = by_k(load(cfg.get("oben")))
        if ob:
            kk = sorted(ob)
            ax.semilogx([ob[k]["Q"] for k in kk], [ob[k]["p_loc"] for k in kk], "-", color="C4", lw=0.8,
                        label="Abwaertsast von oben (Nachtrag)")
        s2 = by_k(load(cfg["s2"]))
        if s2:
            kk = sorted(s2)
            ax.semilogx([s2[k]["Q"] for k in kk], [s2[k]["p_loc"] for k in kk], "-", color="C5", lw=0.8,
                        label="Startknoten s2")
        env, src = envelope(cfg, ast)
        ke = sorted(env)
        winE = [(env[k]["Q"], secant(env, k, k - 12)) for k in ke if (k - 12) in env]
        if winE:
            ax.semilogx([w[0] for w in winE], [w[1] for w in winE], "--", color="C6", lw=2,
                        label="Sekante Einhuellende (Nachtrag)")
    else:
        ax.axhline(cfg["soll_p"], color="k", ls="--", lw=1, label=f"Soll d/(d+1) = {cfg['soll_p']}")
        ax.axhspan(cfg["soll_p"] - 0.02, cfg["soll_p"] + 0.02, color="0.9")
        ob = by_k(load(cfg.get("oben")))
        if ob:
            kk = sorted(ob)
            ax.semilogx([ob[k]["Q"] for k in kk], [ob[k]["p_loc"] for k in kk], "-", color="C4", lw=0.8,
                        label="Abwaertsast von oben (Nachtrag)")
    kv = summary[G].get("K_v")
    if kv is not None:
        ax.axvline(ast[kv]["Q"], color="C3", lw=0.8, ls=":")
    ax.set_ylim(0.3, 1.05)
    ax.set_xlabel("Q")
    ax.set_ylabel("p")
    ax.set_title(f"{G}: {cfg['name']}")
    ax.legend(fontsize=7, loc="lower left")
    ax.grid(alpha=0.3)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "abb1-p.png"), dpi=120)
plt.close(fig)

# Profile
fig, axs = plt.subplots(2, 2, figsize=(13, 9))
pre = {"G1": "ket4096m20", "G2": "qu256", "G3": "kub64", "G4": "sie10s1"}
for ax, G in zip(axs.ravel(), ["G1", "G2", "G3", "G4"]):
    for i, k in enumerate((40, 52, 64, 76, 86)):
        fn = os.path.join(BASE, "haupt", f"profil-{pre[G]}-auf-k{k:03d}.npz")
        if not os.path.exists(fn):
            continue
        z = np.load(fn)
        if G != "G4":
            pos = z["pos"]
            ph = z["phi"]
            sc = ph.max() if ph.max() > 0 else 1
            ax.plot(pos, ph / sc, "-", color=f"C{i}", lw=1, label=f"phi/max, k={k}, Q={R_Q ** k:.3g}")
            ax.plot(pos, z["chi"], "--", color=f"C{i}", lw=1)
        else:
            dist = z["dist"]
            ph = z["phi"].astype(float)
            ch = z["chi"].astype(float)
            m = dist <= 300
            ax.plot(dist[m], ph[m] / ph.max(), ".", ms=1, color=f"C{i}", label=f"phi/max, k={k}, Q={R_Q ** k:.3g}")
            ax.plot(dist[m] + 0.3, ch[m], "x", ms=1.5, color=f"C{i}")
    ax.set_title(f"{G} Profile: phi/max (Linie bzw. Punkte), chi (gestrichelt bzw. x)")
    ax.set_xlabel("Abstand vom Startknoten (Gitter: Schnitt Achse 0; Sierpinski: Graphabstand)")
    ax.legend(fontsize=7)
    ax.grid(alpha=0.3)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "abb2-profile.png"), dpi=120)
plt.close(fig)

# Energie relativ zur Einhuellenden (Hysterese) und Beutelvolumen
fig, axs = plt.subplots(1, 2, figsize=(13, 4.8))
for G, c in zip(["G1", "G2", "G3", "G4"], ["C0", "C1", "C2", "C3"]):
    ast = asts[G]
    ks = sorted(ast)
    if not ks:
        continue
    axs[1].loglog([ast[k]["Q"] for k in ks], [max(ast[k]["Vbag"], 0.5) for k in ks], "-", color=c, label=G)
    env, src = envelope(GRAPHS[G], ast)
    kk = [k for k in ks if k in env]
    axs[0].semilogx([ast[k]["Q"] for k in kk], [(ast[k]["E"] - env[k]["E"]) / env[k]["E"] for k in kk], "-",
                    color=c, label=G + " Ast")
    ob = by_k(load(GRAPHS[G].get("oben")))
    if ob:
        kk2 = [k for k in sorted(ob) if k in env]
        axs[0].semilogx([ob[k]["Q"] for k in kk2], [(ob[k]["E"] - env[k]["E"]) / env[k]["E"] for k in kk2], ":",
                        color=c, label=G + " von oben")
axs[0].set_ylabel("(E - E_env)/E_env")
axs[0].set_xlabel("Q")
axs[0].set_title("Abstand zur Einhuellenden (Nachtrag 2)")
axs[0].legend(fontsize=7)
axs[0].grid(alpha=0.3)
axs[1].set_xlabel("Q")
axs[1].set_ylabel("V_bag = #(chi < 1/2)")
axs[1].set_title("Beutelvolumen auf dem Ast")
axs[1].legend(fontsize=7)
axs[1].grid(alpha=0.3)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "abb3-hysterese-volumen.png"), dpi=120)
plt.close(fig)

# d_s direkt
if "ds" in summary:
    fig, axs = plt.subplots(1, 2, figsize=(13, 4.8))
    for st, c in (("s1", "C0"), ("s2", "C1")):
        fn = os.path.join(BASE, "ds", f"rueckkehr-g10-{st}.npy")
        if os.path.exists(fn):
            ret = np.load(fn)
            t = np.arange(1, ret.size)
            axs[0].loglog(t, ret[1:], "-", color=c, label=f"P(t), Start {st}")
    t = np.array([10, 15625])
    axs[0].loglog(t, 0.5 * (t / 10.0) ** (-math.log(3) / math.log(5)), "k--", label="Steigung -ln3/ln5 (d_s/2)")
    axs[0].set_xlabel("t")
    axs[0].set_ylabel("Rueckkehrwahrscheinlichkeit")
    axs[0].legend(fontsize=7)
    axs[0].grid(alpha=0.3)
    for g, c in ((7, "C2"), (8, "C3")):
        fn = os.path.join(BASE, "ds", f"eigen-g{g}.npy")
        if os.path.exists(fn):
            ev = np.load(fn)
            evp = ev[ev > 1e-10]
            axs[1].loglog(evp, np.arange(1, evp.size + 1), "-", color=c, label=f"N(lambda), g={g}")
    lam = np.array([1e-4, 1.0])
    axs[1].loglog(lam, 3000 * lam ** (math.log(3) / math.log(5)), "k--", label="Steigung ln3/ln5")
    axs[1].set_xlabel("lambda")
    axs[1].set_ylabel("Anzahl Eigenwerte <= lambda (ohne Nullmode)")
    axs[1].legend(fontsize=7)
    axs[1].grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "abb4-ds.png"), dpi=120)
    plt.close(fig)
print("fertig", flush=True)
