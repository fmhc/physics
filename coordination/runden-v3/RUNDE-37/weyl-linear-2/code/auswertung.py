#!/usr/bin/env python3
"""WEYL-LINEAR-1: Auswertung (PLAN.md Abschnitt 5; vor jeder Sicht auf lambda1-Werte eingefroren).

Teile:
  A  Altdaten STRICH-NETZ-1 (weyl-1-0/x/d, N = 50 000, Saat 1, nur Ast E > 0): Fit v - 1 = l1 k + l2 k^2
     (Achsenabschnitt 1, Kartenansatz) in den Fenstern W0 (k <= 0,25, Hauptfenster), Wk (k <= 0,15) und Wg (k <= 0,37)
     mit Fenstergewicht >= 0,5; Bootstrap ueber Richtungs-Cluster (13 Richtungen, Vorzeichen egal), B = 2000.
     Beschreibend: freier Achsenabschnitt, M/2-Zentren.
  S  Altdaten SPIN-ZUFALLSNETZ-1 (beide Helizitaeten, schalengemittelte KPM-Dichten auf dem Raster -1,5..1,5):
     Zentrum je Ast im Raster (Maximum in [0,3 k; 1,7 k], Fenster +-4 sigma_E), Ast E < 0 gespiegelt;
     lambda_A = (E_plus - |E_minus|)/(2 k^2) je Schale mit k <= 0,30.
  N  Neue Laeufe (lauf/zweig-*.json): je Saat und Ast Fit v - 1 = l1 k + l2 k^2 an alle k und Richtungen;
     lambda_A = (l1+ - l1-)/2, lambda_S = (l1+ + l1-)/2; je N Mittel, Streuung, zweistufiger Bootstrap
     (Saaten, darin Richtungen; B = 4000); N-Exponent der Streuung; WL1 bei der groessten N.
  K  Kontrollen (Gitter, Reproduktion der Altdaten) und Netzweiten-Umrechnung.
Aufruf (nur ueber kleintest.sh):  python auswertung.py <lauf-ordner> <alt-ordner> <aus.json> [bild.png] [teile=ASNK]
"""
import glob
import json
import math
import os
import sys

import numpy as np

HBARC_GEV_M = 1.97327e-16      # hbar c in GeV m
L_P = 1.616255e-35             # Planck-Laenge in m
M_PL = 1.22e19                 # Planck-Energie in GeV (JLM-Massstab, Dossier)
E_QG1 = 1.0e20                 # LHAASO linear, subluminal, 95 %
E_QG1_SUPER = 1.1e20           # LHAASO linear, superluminal
E_QG2 = 6.9e11                 # LHAASO quadratisch
E_QG2_MART = 2.4e14            # Martynenko u. a. 2025 (nur Photonen)

_r = np.array([(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1), (1, -1, 0), (1, 0, -1), (0, 1, -1),
               (1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1)], dtype=float)
RICHT13 = _r / np.linalg.norm(_r, axis=1)[:, None]
FENSTER_ALT = {"W0": 0.25, "Wk": 0.15, "Wg": 0.37}
GEWICHT_MIN = 0.5
B_ALT = 2000
B_NEU = 4000
K_MAX_SPIN = 0.30


def js(x):
    if isinstance(x, dict):
        return {str(k): js(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [js(v) for v in x]
    if isinstance(x, np.ndarray):
        return js(x.tolist())
    if isinstance(x, (np.integer,)):
        return int(x)
    if isinstance(x, (np.floating,)):
        return float(x)
    if isinstance(x, (np.bool_,)):
        return bool(x)
    if isinstance(x, float) and not math.isfinite(x):
        return None
    return x


def fit_fix(k, v):
    """v - 1 = l1 k + l2 k^2 (kleinste Quadrate, ungewichtet). Rueckgabe l1, l2, se_l1 (aus Residuen), rms."""
    k = np.asarray(k, float)
    y = np.asarray(v, float) - 1.0
    X = np.stack([k, k * k], 1)
    c, *_ = np.linalg.lstsq(X, y, rcond=None)
    r = y - X @ c
    n = len(k)
    se = float("nan")
    if n > 2:
        s2 = float(r @ r) / (n - 2)
        cov = s2 * np.linalg.inv(X.T @ X)
        se = float(math.sqrt(cov[0, 0]))
    return float(c[0]), float(c[1]), se, float(math.sqrt(np.mean(r * r)))


def fit_frei(k, v):
    k = np.asarray(k, float)
    X = np.stack([np.ones_like(k), k, k * k], 1)
    c, *_ = np.linalg.lstsq(X, np.asarray(v, float), rcond=None)
    return float(c[0]), float(c[1]), float(c[2])


def quantile(x):
    x = np.asarray(x, float)
    x = x[np.isfinite(x)]
    if x.size == 0:
        return None
    return {"mittel": float(x.mean()), "se": float(x.std(ddof=1)) if x.size > 1 else None,
            "q": {p: float(np.percentile(x, p)) for p in (2.5, 16, 50, 84, 97.5)}, "anzahl": int(x.size)}


# ---------------------------------------------------------------------------------------------------- Teil A
def teil_A(alt):
    pts = []
    for name in ("weyl-1-0.json", "weyl-1-x.json", "weyl-1-d.json"):
        d = json.load(open(os.path.join(alt, name)))
        for lauf in d["laeufe"]:
            for w in lauf["wellen"]:
                kv = np.asarray(w["k_vec"], float)
                kh = kv / np.linalg.norm(kv)
                cl = int(np.argmax(np.abs(RICHT13 @ kh)))
                pts.append({"datei": name, "k": float(w["k"]), "v": float(w["v"]), "v_halbM": float(w["v_halbM"]),
                            "gewicht": float(w["gewicht_fenster"]), "cluster": cl, "m": w["m"], "theta": w["theta"]})
    out = {"punkte_gesamt": len(pts), "fenster": {}}
    rng = np.random.default_rng([42, 1])
    for fn, kmax in FENSTER_ALT.items():
        sel = [p for p in pts if p["k"] <= kmax and p["gewicht"] >= GEWICHT_MIN]
        k = np.array([p["k"] for p in sel])
        v = np.array([p["v"] for p in sel])
        cl = np.array([p["cluster"] for p in sel])
        l1, l2, se, rms = fit_fix(k, v)
        v0f, l1f, l2f = fit_frei(k, v)
        l1h, l2h, seh, _ = fit_fix(k, np.array([p["v_halbM"] for p in sel]))
        cls = np.unique(cl)
        boot, skip = [], 0
        for _ in range(B_ALT):
            draw = rng.choice(cls, size=cls.size, replace=True)
            idx = np.concatenate([np.nonzero(cl == c)[0] for c in draw])
            if idx.size < 3 or np.unique(np.round(k[idx], 6)).size < 2:
                skip += 1
                continue
            boot.append(fit_fix(k[idx], v[idx])[0])
        out["fenster"][fn] = {"k_max": kmax, "punkte": int(len(sel)), "cluster": cls.tolist(), "n_cluster": int(cls.size),
                              "l1": l1, "l2": l2, "se_l1_residuen": se, "rms": rms,
                              "bootstrap_l1": quantile(boot), "bootstrap_ausgelassen": skip,
                              "bootstrap_gueltig": bool(cls.size >= 3),
                              "frei_v0": v0f, "frei_l1": l1f, "frei_l2": l2f, "halbM_l1": l1h, "halbM_l2": l2h,
                              "halbM_se_l1": seh}
    return out


# ---------------------------------------------------------------------------------------------------- Teil S
E_RASTER = np.round(np.arange(-1.5, 1.50001, 0.005), 4)


def zentrum_raster(A, E, k, sE):
    msk = (E >= 0.3 * k) & (E <= 1.7 * k)
    i = int(np.argmax(np.where(msk, A, -np.inf)))
    Em = float(E[i])
    w = (E >= Em - 4 * sE) & (E <= Em + 4 * sE) & (E > 0)
    W = float(np.trapezoid(A[w], E[w]))
    return float(np.trapezoid(A[w] * E[w], E[w]) / W), Em, W


def teil_S(alt_spin):
    out = {"raster_symmetrie": float(np.max(np.abs(E_RASTER[::-1] + E_RASTER))), "dateien": {}}
    for name in ("netz1e4-a.json", "netz1e5-1.json"):
        d = json.load(open(os.path.join(alt_spin, name)))
        res = []
        for s in d["saaten"]:
            sp = s.get("spektral")
            if not sp:
                continue
            a, M = float(sp["a"]), int(sp["M"])
            sE = math.pi * a / M
            for key in sorted(sp["schalen"]):
                sch, h = key.split("_")
                if h != "-1" or f"{sch}_1" not in sp["schalen"]:
                    continue
                pl, mi = sp["schalen"][key], sp["schalen"][f"{sch}_1"]
                k = float(pl["k_mittel"])
                Ap = np.asarray(pl["A"], float)
                Am = np.asarray(mi["A"], float)[::-1]
                Ep, _, Wp = zentrum_raster(Ap, E_RASTER, k, sE)
                Em, _, Wm = zentrum_raster(Am, E_RASTER, k, sE)
                res.append({"saat": s["saat"], "schale": int(sch), "k": k, "k_minus": float(mi["k_mittel"]),
                            "anzahl": pl["anzahl"], "E_plus": Ep, "E_minus_betrag": Em, "v_plus": Ep / k,
                            "v_minus": Em / k, "W_plus": Wp, "W_minus": Wm, "lambda_A": (Ep - Em) / (2 * k * k),
                            "haupt": bool(k <= K_MAX_SPIN), "sigma_E": sE, "M": M})
        haupt = [r for r in res if r["haupt"]]
        lam = np.array([r["lambda_A"] for r in haupt])
        out["dateien"][name] = {"N": d["N"], "schalen": res,
                                "haupt_lambda_A_mittel": float(lam.mean()) if lam.size else None,
                                "haupt_lambda_A_sd": float(lam.std(ddof=1)) if lam.size > 1 else None,
                                "haupt_anzahl": int(lam.size)}
    return out


# ---------------------------------------------------------------------------------------------------- Teil N
def zeilen_neu(lauf):
    rows = []
    for f in sorted(glob.glob(os.path.join(lauf, "zweig-*.json"))):
        d = json.load(open(f))
        for s in d["saaten"]:
            for w in s["wellen"]:
                p, m = w["aeste"]["plus"], w["aeste"]["minus"]
                rows.append({"datei": os.path.basename(f), "N": int(d["N"]), "saat": int(s["saat"]),
                             "richtung": w["richtung"], "k": float(w["k"]), "v_plus": p["v"], "v_minus": m["v"],
                             "v_plus_halbM": p["v_halbM"], "v_minus_halbM": m["v_halbM"],
                             "g_plus": p["gewicht_fenster"], "g_minus": m["gewicht_fenster"], "a": w["a"],
                             "a_fest_ok": w.get("a_fest_ok"), "mu_max": w["mu_max"]})
    return rows


def saat_fit(rows, kmax=None, feld=("v_plus", "v_minus")):
    sel = [r for r in rows if kmax is None or r["k"] <= kmax + 1e-12]
    k = np.array([r["k"] for r in sel])
    l1p = fit_fix(k, [r[feld[0]] for r in sel])
    l1m = fit_fix(k, [r[feld[1]] for r in sel])
    return l1p[0], l1m[0], l1p[1], l1m[1]


def teil_N(lauf):
    rows = zeilen_neu(lauf)
    out = {"zeilen": len(rows), "je_N": {}, "a_fest_alle_ok": bool(all(r["a_fest_ok"] for r in rows)) if rows else None,
           "mu_max": float(max(r["mu_max"] for r in rows)) if rows else None}
    if not rows:
        return out
    Ns = sorted({r["N"] for r in rows})
    alle_p, alle_m = [], []
    for N in Ns:
        rN = [r for r in rows if r["N"] == N]
        saaten = sorted({r["saat"] for r in rN})
        je = []
        for s in saaten:
            rs = [r for r in rN if r["saat"] == s]
            l1p, l1m, l2p, l2m = saat_fit(rs)
            k_l1p, k_l1m, _, _ = saat_fit(rs, kmax=0.18)
            h_l1p, h_l1m, _, _ = saat_fit(rs, feld=("v_plus_halbM", "v_minus_halbM"))
            k = np.array([r["k"] for r in rs])
            fp = fit_frei(k, [r["v_plus"] for r in rs])
            fm = fit_frei(k, [r["v_minus"] for r in rs])
            direkt = float(np.mean([(r["v_plus"] - r["v_minus"]) / (2 * r["k"]) for r in rs]))
            je.append({"saat": s, "l1_plus": l1p, "l1_minus": l1m, "l2_plus": l2p, "l2_minus": l2m,
                       "lambda_A": 0.5 * (l1p - l1m), "lambda_S": 0.5 * (l1p + l1m), "lambda_A_direkt": direkt,
                       "probe_k018_l1_plus": k_l1p, "probe_k018_l1_minus": k_l1m,
                       "probe_halbM_l1_plus": h_l1p, "probe_halbM_l1_minus": h_l1m,
                       "probe_frei_v0_plus": fp[0], "probe_frei_l1_plus": fp[1], "probe_frei_v0_minus": fm[0],
                       "probe_frei_l1_minus": fm[1], "punkte": len(rs),
                       "g_min": float(min(min(r["g_plus"], r["g_minus"]) for r in rs))})
            alle_p.append(l1p)
            alle_m.append(l1m)
        st = {}
        for q in ("l1_plus", "l1_minus", "lambda_A", "lambda_S", "lambda_A_direkt", "probe_k018_l1_plus",
                  "probe_k018_l1_minus", "probe_halbM_l1_plus", "probe_halbM_l1_minus"):
            x = np.array([e[q] for e in je])
            st[q] = {"mittel": float(x.mean()), "sd": float(x.std(ddof=1)) if x.size > 1 else None,
                     "se": float(x.std(ddof=1) / math.sqrt(x.size)) if x.size > 1 else None,
                     "rms": float(math.sqrt(np.mean(x * x)))}
        # zweistufiger Bootstrap: Saaten mit Zuruecklegen, darin Richtungen mit Zuruecklegen
        rng = np.random.default_rng([42, 2, N])
        bp, bm = [], []
        nach_saat = {s: {d: [r for r in rN if r["saat"] == s and r["richtung"] == d]
                         for d in sorted({r["richtung"] for r in rN if r["saat"] == s})} for s in saaten}
        for _ in range(B_NEU):
            ps, ms = [], []
            for s in rng.choice(saaten, size=len(saaten), replace=True):
                dirs = list(nach_saat[s].keys())
                rs = []
                for dd in rng.choice(dirs, size=len(dirs), replace=True):
                    rs += nach_saat[s][dd]
                l1p, l1m, _, _ = saat_fit(rs)
                ps.append(l1p)
                ms.append(l1m)
            bp.append(np.mean(ps))
            bm.append(np.mean(ms))
        bp, bm = np.array(bp), np.array(bm)
        boot = {"l1_plus": quantile(bp), "l1_minus": quantile(bm), "lambda_A": quantile(0.5 * (bp - bm)),
                "lambda_S": quantile(0.5 * (bp + bm))}
        xp = np.array([e["l1_plus"] for e in je])
        xm = np.array([e["l1_minus"] for e in je])
        korr = float(np.corrcoef(xp, xm)[0, 1]) if len(je) > 2 else None
        out["je_N"][str(N)] = {"N": N, "saaten": saaten, "je_saat": je, "statistik": st, "bootstrap": boot,
                               "korrelation_plus_minus": korr}
    # N-Exponent der Streuung (nur N mit >= 3 Saaten)
    expo = {}
    gN = [N for N in Ns if len(out["je_N"][str(N)]["saaten"]) >= 3]
    for q in ("l1_plus", "l1_minus", "lambda_A", "lambda_S"):
        if len(gN) >= 2:
            x = np.log(np.array(gN, float))
            y = np.log(np.array([out["je_N"][str(N)]["statistik"][q]["sd"] for N in gN]))
            sl, ic = np.polyfit(x, y, 1)
            expo[q] = {"N": gN, "exponent": float(sl), "C": float(math.exp(ic))}
    out["exponent_streuung"] = expo
    out["korrelation_plus_minus_alle"] = float(np.corrcoef(alle_p, alle_m)[0, 1]) if len(alle_p) > 2 else None
    # WL1 bei der groessten N
    Nmax = Ns[-1]
    e = out["je_N"][str(Nmax)]
    if len(e["saaten"]) < 3:
        wl1 = {"urteil": "nicht auswertbar", "grund": "weniger als 3 Saaten", "N": Nmax}
    else:
        teil = {}
        for b in ("l1_plus", "l1_minus"):
            m, se = e["statistik"][b]["mittel"], e["bootstrap"][b]["se"]
            teil[b] = {"mittel": m, "se_boot": se, "verhaeltnis": abs(m) / se if se else None,
                       "unter_3_sigma": bool(se and abs(m) < 3 * se)}
        ok = all(t["unter_3_sigma"] for t in teil.values())
        wl1 = {"urteil": "eingetroffen" if ok else "nicht eingetroffen", "N": Nmax, "aeste": teil}
    out["WL1"] = wl1
    return out


# ---------------------------------------------------------------------------------------------------- Teil K
def l_linear(lam, E):
    return HBARC_GEV_M / (2.0 * abs(lam) * E)


def l_quadrat(kappa, E):
    return HBARC_GEV_M / (E * math.sqrt(2.0 * kappa))


def teil_K(lauf, alt, neu):
    out = {}
    f = os.path.join(lauf, "kontrolle.json")
    if os.path.exists(f):
        d = json.load(open(f))
        out["gitter"] = {"max_abw": d["max_abw"], "max_plus_minus": d["max_plus_minus"], "L": d["gitter_L"], "M": d["M"]}
    f = os.path.join(lauf, "repro-50000-1.json")
    if os.path.exists(f):
        d = json.load(open(f))
        w = d["saaten"][0]["wellen"][0]
        a = json.load(open(os.path.join(alt, "weyl-1-x.json")))
        wa = a["laeufe"][0]["wellen"][0]
        out["reproduktion"] = {"v_plus_neu": w["aeste"]["plus"]["v"], "v_alt": wa["v"],
                               "abw": abs(w["aeste"]["plus"]["v"] - wa["v"]), "k_neu": w["k"], "k_alt": wa["k"],
                               "v_minus_neu": w["aeste"]["minus"]["v"],
                               "lambda_A_direkt": (w["aeste"]["plus"]["v"] - w["aeste"]["minus"]["v"]) / (2 * w["k"])}
    # Netzweite (Formeln des Dossiers, Einheiten: hbar c in GeV m, E in GeV -> m)
    nw = {"formel_linear": "l = hbar c / (2 |lambda1| E_QG,1)", "formel_quadratisch": "l = hbar c / (E_QG,2 sqrt(2 kappa))",
          "dossier_pruefung": {
              "lin_0.0011_LHAASO_m": l_linear(0.0011, E_QG1), "lin_0.0011_LHAASO_lP": l_linear(0.0011, E_QG1) / L_P,
              "lin_0.0011_MPl_m": l_linear(0.0011, M_PL), "lin_0.0011_MPl_lP": l_linear(0.0011, M_PL) / L_P,
              "quad_0.117_LHAASO_m": l_quadrat(0.117, E_QG2), "quad_0.0218_LHAASO_m": l_quadrat(0.0218, E_QG2),
              "quad_0.117_Mart_m": l_quadrat(0.117, E_QG2_MART), "quad_0.0218_Mart_m": l_quadrat(0.0218, E_QG2_MART)},
          "lambda_krit_bei_lP_LHAASO": HBARC_GEV_M / (2 * L_P * E_QG1),
          "lambda_krit_bei_quadratschranke": HBARC_GEV_M / (2 * l_quadrat(0.117, E_QG2) * E_QG1)}
    if neu and neu.get("je_N"):
        jN = {}
        for N, e in neu["je_N"].items():
            r = e["statistik"]["l1_plus"]["rms"]
            jN[N] = {"rms_l1_plus": r, "l_LHAASO_m": l_linear(r, E_QG1), "l_LHAASO_lP": l_linear(r, E_QG1) / L_P,
                     "l_JLM_lP": l_linear(r, M_PL) / L_P}
        nw["je_N_rms"] = jN
        ex = neu.get("exponent_streuung", {}).get("l1_plus")
        if ex:
            lam_q = nw["lambda_krit_bei_quadratschranke"]
            nw["N_eff_fuer_quadratschranke"] = (lam_q / ex["C"]) ** (1.0 / ex["exponent"]) if ex["exponent"] < 0 else None
    out["netzweite"] = nw
    return out


# ---------------------------------------------------------------------------------------------------- Bild
def bild(pfad, alt, A, neu):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(2, 2, figsize=(12, 9))
    # (a) Altdaten
    a = ax[0, 0]
    pts = []
    for name in ("weyl-1-0.json", "weyl-1-x.json", "weyl-1-d.json"):
        d = json.load(open(os.path.join(alt, name)))
        for lauf in d["laeufe"]:
            for w in lauf["wellen"]:
                pts.append((w["k"], w["v"], w["gewicht_fenster"]))
    pts = np.array(pts)
    a.plot(pts[:, 0], pts[:, 1] - 1, "o", ms=4, color="tab:blue", label="STRICH-NETZ-1, E > 0 (N = 50 000, Saat 1)")
    if A:
        f = A["fenster"]["W0"]
        kk = np.linspace(0, 0.37, 200)
        a.plot(kk, f["l1"] * kk + f["l2"] * kk ** 2, "-", color="tab:red",
               label=f"Fit W0 (k <= 0,25): l1 = {f['l1']:.4f}")
    a.axvline(0.25, color="0.6", ls=":")
    a.axhline(0, color="0.3", lw=0.6)
    a.set_xlabel("k (1/l, l = n^(-1/3))")
    a.set_ylabel("v - 1 = E/(c k) - 1")
    a.set_title("(a) Altdaten: ein Ast, ein Netz")
    a.legend(fontsize=8)
    if neu and neu.get("je_N"):
        Ns = sorted(int(N) for N in neu["je_N"])
        # (b) lambda1 je Saat und Ast gegen N
        b = ax[0, 1]
        for N in Ns:
            e = neu["je_N"][str(N)]["je_saat"]
            xp = [s["l1_plus"] for s in e]
            xm = [s["l1_minus"] for s in e]
            b.plot([N * 0.93] * len(xp), xp, "o", color="tab:red", ms=4, alpha=0.8)
            b.plot([N * 1.07] * len(xm), xm, "s", color="tab:blue", ms=4, alpha=0.8)
        b.plot([], [], "o", color="tab:red", label="Ast E > 0 (je Saat)")
        b.plot([], [], "s", color="tab:blue", label="Ast E < 0 (je Saat)")
        b.axhline(0, color="0.3", lw=0.6)
        b.set_xscale("log")
        b.set_xlabel("N (Punkte im Netz)")
        b.set_ylabel("lambda1 (Fit k = 0,06 bis 0,24)")
        b.set_title("(b) lambda1 je Netz und Ast")
        b.legend(fontsize=8)
        # (c) Streuung gegen N
        c = ax[1, 0]
        for q, col, lab in (("lambda_A", "tab:purple", "Streuung lambda_A (Gegenteil)"),
                            ("lambda_S", "tab:green", "Streuung lambda_S (Gleichteil)")):
            ys = [neu["je_N"][str(N)]["statistik"][q]["sd"] for N in Ns]
            c.plot(Ns, ys, "o-", color=col, label=lab)
        ms = [abs(neu["je_N"][str(N)]["statistik"]["lambda_S"]["mittel"]) for N in Ns]
        c.plot(Ns, ms, "x--", color="tab:green", label="|Mittel lambda_S|")
        y0 = neu["je_N"][str(Ns[0])]["statistik"]["lambda_A"]["sd"]
        if y0:
            NN = np.array([Ns[0], Ns[-1]], float)
            c.plot(NN, y0 * (NN / Ns[0]) ** -0.5, ":", color="0.4", label="Steigung N^(-1/2)")
        c.set_xscale("log")
        c.set_yscale("log")
        c.set_xlabel("N")
        c.set_ylabel("Streuung ueber Saaten")
        c.set_title("(c) Faellt die Streuung mit der Netzgroesse?")
        c.legend(fontsize=8)
        # (d) plus gegen minus
        d_ = ax[1, 1]
        for N, mk in zip(Ns, ("o", "s", "^", "D")):
            e = neu["je_N"][str(N)]["je_saat"]
            d_.plot([s["l1_plus"] for s in e], [s["l1_minus"] for s in e], mk, ms=5, label=f"N = {N}")
        lim = max(1e-6, max(abs(s[q]) for N in Ns for s in neu["je_N"][str(N)]["je_saat"] for q in ("l1_plus", "l1_minus")))
        d_.plot([-lim, lim], [lim, -lim], ":", color="0.4", label="l1(E<0) = -l1(E>0)")
        d_.plot([-lim, lim], [-lim, lim], "--", color="0.75", label="l1(E<0) = l1(E>0)")
        d_.axhline(0, color="0.3", lw=0.5)
        d_.axvline(0, color="0.3", lw=0.5)
        d_.set_xlabel("lambda1, Ast E > 0")
        d_.set_ylabel("lambda1, Ast E < 0")
        d_.set_title("(d) Beide Aeste desselben Netzes")
        d_.legend(fontsize=8)
    fig.suptitle("WEYL-LINEAR-1: lineares Glied der Weyl-Dispersion im Zufallsnetz (synthetische Rechnung)")
    fig.tight_layout()
    fig.savefig(pfad, dpi=110)


def main():
    lauf, alt, ziel = sys.argv[1], sys.argv[2], sys.argv[3]
    pos = [a for a in sys.argv[4:] if "=" not in a]
    opts = {a.split("=")[0]: a.split("=")[1] for a in sys.argv[4:] if "=" in a}
    teile = opts.get("teile", "ASNK")
    out = {"teile": teile}
    A = teil_A(alt) if "A" in teile else None
    out["A_altdaten_strichnetz"] = A
    out["S_altdaten_spinnetz"] = teil_S(alt) if "S" in teile else None
    neu = teil_N(lauf) if "N" in teile else None
    out["N_neue_laeufe"] = neu
    out["K_kontrollen_netzweite"] = teil_K(lauf, alt, neu) if "K" in teile else None
    tmp = ziel + ".tmp"
    with open(tmp, "w") as f:
        json.dump(js(out), f, indent=1)
    os.replace(tmp, ziel)
    if pos:
        bild(pos[0], alt, A, neu)
    print("geschrieben", ziel, flush=True)


if __name__ == "__main__":
    main()
