#!/usr/bin/env python3
"""FADEN-DIM-2 (Runde 43, Fast Lane): Zusatzmodul zu faden.py.

faden.py ist eine unveraenderte Kopie aus FADEN-DIM-1 (gleiche sha256). Startlage, Dynamik (G, RP), Treffpruefung,
T = 4 L^2 und die Zeitgrenze von 560 s kommen unveraendert von dort. Neu hier:
  - konstante Rauheit: Nennwert p_nom je (D, L), so dass die mittlere Knickdichte der geschlossenen Faeden
    (Gleichgewicht der geschlossenen RSOS-Kette mit Gewicht exp(-J K), exakt abgezaehlt) RHO_ZIEL = 0,6 ist.
    J = ln(2 (D-1) (1 - p_nom) / p_nom) wie in faden.run_R; kappa = J / 2.
  - eigene Saat mit Blockindex (eine Zelle darf auf mehrere Laeufe verteilt werden),
  - Auswertung FD0 bis FD2 der Karte (Plan- und Kartenwortlaut-Lesart).

Modi (nur ueber kleintest.sh auf der .69):
  kalib                             Kalibrierung; gibt NUR p_nom, J, kappa und Knickdichten aus (keine Treffzahlen)
  rauch                             Laufzeiten (faden.zeitprobe), keine Treffzahlen
  lauf --zellen Z1,Z2 --out F       Zelle DYN:D:L:P:N:B; P = "kal" (kalibriert) oder Zahl; B = Block (Saat)
  auswertung --ein F1,F2 --out-json A --out-txt B
  bild --ein A --out PNG
"""
import json
import math
import time
import argparse
from fractions import Fraction
import numpy as np
import faden as F

SEED2 = [20261004, 2]
RHO_ZIEL = 0.6
RHO_TOL = 0.01
KALIB_DL = [(4, 16), (4, 24), (4, 32), (4, 48), (4, 64), (5, 8), (5, 12), (5, 16), (5, 24)]
GEGENPROBE_DIM1 = [(4, 8), (4, 12), (4, 16), (4, 24), (4, 32), (5, 4), (5, 6), (5, 8), (5, 12), (5, 16)]
NBOOT = 2000
FD1_BAND = (-0.75, -0.35)
FD2_SCHWELLE = -0.25
L4 = [16, 24, 32, 48, 64]
L4G = [32, 48, 64]
L5 = [8, 12, 16, 24]


# ---------------------------------------------------------------- Kalibrierung (exakt)
def gewichte(L, dp):
    """w[K] = C(L, K) * N_dp(K); N_dp(K) = Zahl der geschlossenen Wege aus K Einheitsschritten auf Z^dp (exakt)."""
    mmax = L // 2
    a = [Fraction(1, math.factorial(k) ** 2) for k in range(mmax + 1)]
    s = [Fraction(0)] * (mmax + 1)
    s[0] = Fraction(1)
    for _ in range(dp):
        t = [Fraction(0)] * (mmax + 1)
        for i in range(mmax + 1):
            if s[i] == 0:
                continue
            for k in range(mmax + 1 - i):
                t[i + k] += s[i] * a[k]
        s = t
    w = [0] * (L + 1)
    for m in range(mmax + 1):
        N = s[m] * math.factorial(2 * m)
        if N.denominator != 1:
            raise RuntimeError("N_dp nicht ganzzahlig")
        w[2 * m] = math.comb(L, 2 * m) * N.numerator
    return w


def dichte_exakt(w, L, lx):
    """<K>/L der geschlossenen Kette bei Knickgewicht x = exp(lx) je Richtung (freie Kette: p = 2dp x/(1 + 2dp x))."""
    terms = [(K, math.log(wk) + K * lx) for K, wk in enumerate(w) if wk > 0]
    mx = max(t for _, t in terms)
    Z = sum(math.exp(t - mx) for _, t in terms)
    KZ = sum(K * math.exp(t - mx) for K, t in terms)
    return KZ / Z / L


def p_aus_lx(lx, dp):
    Mx = 2 * dp * math.exp(lx)
    return Mx / (1.0 + Mx)


def lx_aus_p(p, dp):
    return -math.log(2 * dp * (1 - p) / p)


def kalib(D, L):
    """p_nom (auf 6 Stellen), J, kappa und exakte Dichte bei diesem gerundeten p_nom."""
    dp = D - 1
    w = gewichte(L, dp)
    lo, hi = -30.0, 30.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if dichte_exakt(w, L, mid) < RHO_ZIEL:
            lo = mid
        else:
            hi = mid
    p = round(p_aus_lx(0.5 * (lo + hi), dp), 6)
    lx = lx_aus_p(p, dp)
    return {"D": D, "L": L, "p_nom": p, "J": -lx, "kappa": -lx / 2, "rho_exakt": dichte_exakt(w, L, lx)}


def modus_kalib():
    t0 = time.time()
    print("FADEN-DIM-2 Kalibrierung: nur p_nom, J, kappa und Knickdichten (keine Treffzahlen)", flush=True)
    print("Gegenprobe der exakten Formel an FADEN-DIM-1 (p_nom = 0,6, dortiges p_start):", flush=True)
    for D, L in GEGENPROBE_DIM1:
        w = gewichte(L, D - 1)
        print(f"  D={D} L={L:>3} p_nom=0.6 rho_exakt={dichte_exakt(w, L, lx_aus_p(0.6, D - 1)):.4f}", flush=True)
    out = []
    for D, L in KALIB_DL:
        k = kalib(D, L)
        dp = D - 1
        rng = np.random.default_rng(SEED2 + [77, D, L])
        nb = 4096
        cod = F.sample_bridges(rng, nb, L, dp, k["p_nom"])
        rho_mc = float((cod != 0).mean())
        # Dynamikprobe: 512 Bruecken, 200 Sweeps lokaler Metropolis-Zuege (ohne Verschiebung, ohne zweiten Faden)
        nd = 512
        NB = F.nb_table(dp, L)
        ADD, SUB = F.code_tables(dp)
        M = 2 * dp
        ACC = np.array([min(1.0, math.exp(-k["J"] * d)) for d in range(-2, 3)])
        c = cod[:nd].copy()
        y = F.build_y(c, rng.integers(0, L ** dp, nd), NB)
        for _ in range(200):
            for q in (0, 1):
                F.halbsweep(rng, y, c, q, L, M, NB, ADD, SUB, ACC)
        rho_dyn = float((c != 0).mean())
        k.update({"rho_mc": rho_mc, "n_mc": nb, "rho_dyn_200": rho_dyn, "n_dyn": nd,
                  "ok_mc": bool(abs(rho_mc - RHO_ZIEL) <= RHO_TOL),
                  "ok_dyn": bool(abs(rho_dyn - RHO_ZIEL) <= RHO_TOL)})
        out.append(k)
        print(f"  D={D} L={L:>3} p_nom={k['p_nom']:.6f} J={k['J']:.4f} kappa={k['kappa']:.4f} "
              f"rho_exakt={k['rho_exakt']:.5f} rho_mc={rho_mc:.4f} rho_dyn200={rho_dyn:.4f} "
              f"ok_mc={k['ok_mc']} ok_dyn={k['ok_dyn']}", flush=True)
    print("KALIB_JSON " + json.dumps(out), flush=True)
    print(f"kalib gesamt {time.time() - t0:.1f} s", flush=True)


def modus_rauch():
    proben = [("RP", 4, 64, 1024, 20), ("RP", 4, 48, 1024, 30), ("RP", 5, 24, 4096, 30), ("G", 4, 64, 8192, 200)]
    t_start = time.time()
    for dyn, D, L, n, ns in proben:
        p = 0.0 if dyn == "G" else kalib(D, L)["p_nom"]
        z = f"{dyn}:{D}:{L}:{p}:{n}"
        ti, ns_el = F.zeitprobe(z, ns)
        print(f"rauch {z}: start {ti:.2f} s, {ns_el:.1f} ns je (Paar*Schritt*Spalte) "
              f"[G: je Paar*Schritt*Querrichtung]", flush=True)
    print(f"rauch gesamt {time.time() - t_start:.1f} s", flush=True)


# ---------------------------------------------------------------- Laeufe
def parse_zelle2(z):
    dyn, D, L, p, n, b = z.split(":")
    D, L, n, b = int(D), int(L), int(n), int(b)
    kal = None
    if dyn == "G":
        p = 0.0
    elif p == "kal":
        kal = kalib(D, L)
        p = kal["p_nom"]
    else:
        p = float(p)
    return dyn, D, L, p, n, b, kal


def rechne_zelle2(z, t_start):
    dyn, D, L, p, n, b, kal = parse_zelle2(z)
    rng = np.random.default_rng(SEED2 + [F.DYN_CODE[dyn], D, L, n, b])
    t0 = time.time()
    if dyn == "G":
        tmeet, T, ab, extra = F.run_G(D, L, n, rng, t_start)
    else:
        tmeet, T, ab, extra = F.run_R(dyn, D, L, p, n, rng, t_start)
    dt = time.time() - t0
    met = ~np.isnan(tmeet)
    rec = {"zelle": z, "dyn": dyn, "D": D, "L": L, "p_nom": p, "n": n, "block": b, "T": T, "c": F.C_T,
           "rho_exakt": (kal["rho_exakt"] if kal else None),
           "treffer": int(met.sum()), "abgebrochen": bool(ab), "laufzeit_s": round(dt, 3)}
    rec.update(extra)
    rec["t_treffen"] = [round(float(v), 3) for v in np.sort(tmeet[met])]
    return rec


def modus_lauf(zellen, out):
    t_start = time.time()
    for z in zellen:
        rec = rechne_zelle2(z, t_start)
        with open(out, "a") as f:
            f.write(json.dumps(rec) + "\n")
        print(f"{z} fertig, {rec['laufzeit_s']:.1f} s, abgebrochen={rec['abgebrochen']}", flush=True)
        if rec["abgebrochen"]:
            print("Zeitgrenze erreicht, Rest nicht gerechnet", flush=True)
            break
    print(f"lauf gesamt {time.time() - t_start:.1f} s", flush=True)


# ---------------------------------------------------------------- Auswertung
def lade(ein):
    recs = []
    for f in ein:
        with open(f) as fh:
            for line in fh:
                line = line.strip()
                if line:
                    recs.append(json.loads(line))
    Z = {}
    for r in recs:
        key = (r["dyn"], r["D"], r["L"])
        z = Z.get(key)
        if z is None:
            z = {"dyn": r["dyn"], "D": r["D"], "L": r["L"], "p_nom": r["p_nom"], "kappa": r["kappa"],
                 "rho_exakt": r.get("rho_exakt"), "n": 0, "treffer": 0, "bloecke": [], "abgebrochen": False,
                 "t": [], "ps_sum": 0.0, "pe_sum": 0.0, "pe_n": 0, "acc_sum": 0.0, "laufzeit_s": 0.0}
            Z[key] = z
        if r["p_nom"] != z["p_nom"]:
            raise RuntimeError(f"p_nom verschieden in {key}")
        if r["block"] in [bb[0] for bb in z["bloecke"]]:
            raise RuntimeError(f"Block doppelt in {key}")
        z["bloecke"].append([r["block"], r["treffer"], r["n"], r["abgebrochen"]])
        z["abgebrochen"] = z["abgebrochen"] or r["abgebrochen"]
        z["n"] += r["n"]
        z["treffer"] += r["treffer"]
        z["t"] += r["t_treffen"]
        z["ps_sum"] += r["p_start"] * r["n"]
        rest = r["n"] - r["treffer"]
        if r["p_end_rest"] is not None and rest > 0:
            z["pe_sum"] += r["p_end_rest"] * rest
            z["pe_n"] += rest
        if r["akzeptanz_lokal"] is not None:
            z["acc_sum"] += r["akzeptanz_lokal"] * r["n"]
        z["laufzeit_s"] += r["laufzeit_s"]
    for z in Z.values():
        z["p_start"] = z["ps_sum"] / z["n"]
        z["p_end_rest"] = (z["pe_sum"] / z["pe_n"]) if z["pe_n"] else None
        z["akzeptanz_lokal"] = (z["acc_sum"] / z["n"]) if z["dyn"] != "G" else None
    return Z


def rho_ok(z):
    return z["dyn"] == "G" or abs(z["p_start"] - RHO_ZIEL) <= RHO_TOL


def zell_info(z):
    h, n, L = z["treffer"], z["n"], z["L"]
    P = h / n
    lo, hi = F.wilson(h, n)
    Pt = (h + 0.5) / (n + 1.0)
    tt = z["t"]
    return {"dyn": z["dyn"], "D": z["D"], "L": L, "n": n, "treffer": h, "bloecke": z["bloecke"],
            "P": P, "P_lo": lo, "P_hi": hi, "PL": P * L, "PL_lo": lo * L, "PL_hi": hi * L,
            "rate": -math.log1p(-Pt), "p_nom": z["p_nom"], "kappa": z["kappa"], "rho_exakt": z["rho_exakt"],
            "p_start": z["p_start"], "p_end_rest": z["p_end_rest"], "rho_ok": bool(rho_ok(z)),
            "akzeptanz_lokal": z["akzeptanz_lokal"], "abgebrochen": z["abgebrochen"],
            "t_median_durch_L2": (float(np.median(tt)) / L ** 2) if tt else None,
            "laufzeit_s": z["laufzeit_s"]}


def wfit(X, Y, w):
    W = w / w.sum()
    xm = (W * X).sum()
    ym = (W * Y).sum()
    return float((W * (X - xm) * (Y - ym)).sum() / (W * (X - xm) ** 2).sum())


def fit_rate(Ls, hits, ns):
    """Exponent von -ln(1 - P) gegen L: gewichtete Gerade in ln/ln, Gewicht = 1/Varianz (Deltamethode)."""
    X = np.log(np.asarray(Ls, float))
    n = np.asarray(ns, float)
    P = (np.asarray(hits, float) + 0.5) / (n + 1.0)
    lq = np.log1p(-P)
    Y = np.log(-lq)
    w = n * (1.0 - P) * lq ** 2 / P
    return wfit(X, Y, w)


def zwei_punkt(Ls, hits, ns):
    """Steigung von ln P zwischen erstem und letztem L (Kartenwortlaut FD2)."""
    n = np.asarray(ns, float)
    P = (np.asarray(hits, float) + 0.5) / (n + 1.0)
    return float(math.log(P[-1] / P[0]) / math.log(Ls[-1] / Ls[0]))


def boot(fun, Ls, hits, ns, rng):
    s0 = fun(Ls, hits, ns)
    n = np.asarray(ns)
    ph = np.asarray(hits, float) / n
    bs = np.array([fun(Ls, rng.binomial(n, ph), ns) for _ in range(NBOOT)])
    lo, hi = np.percentile(bs, [2.5, 97.5])
    return s0, float(lo), float(hi)


def serie(Z, dyn, D, Ls, nur_ok):
    out_L, out_h, out_n = [], [], []
    for L in Ls:
        k = (dyn, D, L)
        if k not in Z or Z[k]["abgebrochen"]:
            continue
        if nur_ok and not rho_ok(Z[k]):
            continue
        out_L.append(L)
        out_h.append(Z[k]["treffer"])
        out_n.append(Z[k]["n"])
    return out_L, out_h, out_n


def modus_auswertung(ein, out_json, out_txt):
    Z = lade(ein)
    rng = np.random.default_rng(SEED2 + [99])
    erg = {"zellen": [zell_info(Z[k]) for k in sorted(Z)], "fits": {}, "urteile": {}}
    fits = erg["fits"]

    def fitrec(name, fun, Ls, h, n):
        if len(Ls) < 2:
            fits[name] = {"L": Ls, "fehlt": True}
            return None
        s, lo, hi = boot(fun, Ls, h, n, rng)
        fits[name] = {"L": Ls, "treffer": h, "n": n, "s": s, "lo": lo, "hi": hi}
        return fits[name]

    f1p = fitrec("FD1_rate_RP4_16_64_plan", fit_rate, *serie(Z, "RP", 4, L4, True))
    f1k = fitrec("FD1_rate_RP4_16_64_karte", fit_rate, *serie(Z, "RP", 4, L4, False))
    f2p = fitrec("FD2_lnP_RP4_32_48_64_plan", F.fit_steigung, *serie(Z, "RP", 4, [32, 48, 64], True))
    f2k = fitrec("FD2_zweipunkt_RP4_32_64_karte", zwei_punkt, *serie(Z, "RP", 4, [32, 64], False))
    fitrec("G4_lnP_32_64", F.fit_steigung, *serie(Z, "G", 4, L4G, False))
    fitrec("G4_rate_32_64", fit_rate, *serie(Z, "G", 4, L4G, False))
    fitrec("RP4_lnP_16_64", F.fit_steigung, *serie(Z, "RP", 4, L4, True))
    fitrec("RP5_lnP_8_24", F.fit_steigung, *serie(Z, "RP", 5, L5, True))
    fitrec("RP5_rate_8_24", fit_rate, *serie(Z, "RP", 5, L5, True))
    for (dyn, D, Ls) in [("RP", 4, L4), ("G", 4, L4G), ("RP", 5, L5)]:
        for a, b in zip(Ls[:-1], Ls[1:]):
            fitrec(f"lokal_lnP_{dyn}{D}_{a}_{b}", F.fit_steigung, *serie(Z, dyn, D, [a, b], True))
            fitrec(f"lokal_rate_{dyn}{D}_{a}_{b}", fit_rate, *serie(Z, dyn, D, [a, b], True))

    U = {}
    # FD0: G bei D = 4, P L zwischen L = 32 und 64 konstant bis Faktor 1,5
    try:
        gz = []
        for L in L4G:
            if Z[("G", 4, L)]["abgebrochen"]:
                raise KeyError(f"G:4:{L} abgebrochen")
            gz.append(zell_info(Z[("G", 4, L)]))
        PL = [x["PL"] for x in gz]
        fk = max(PL) / min(PL) if min(PL) > 0 else float("inf")
        lo_min = min(x["PL_lo"] for x in gz)
        fp = max(x["PL_hi"] for x in gz) / lo_min if lo_min > 0 else float("inf")
        U["FD0_karte"] = {"PL": PL, "faktor": fk, "urteil": "eingetroffen" if fk <= 1.5 else "nicht eingetroffen"}
        U["FD0_plan"] = {"faktor_wilson_aussen": fp, "faktor_punkt": fk,
                         "urteil": ("eingetroffen" if fp <= 1.5 else
                                    ("nicht eingetroffen" if fk > 1.5 else "uneindeutig"))}
    except KeyError as e:
        U["FD0_karte"] = {"urteil": f"nicht auswertbar ({e})"}
        U["FD0_plan"] = {"urteil": f"nicht auswertbar ({e})"}
    # FD1: Exponent der Rate -ln(1 - P), RP D = 4, L = 16 bis 64, Band [-0,75; -0,35]
    a1, b1 = FD1_BAND
    if f1k is None:
        U["FD1_karte"] = {"urteil": "nicht auswertbar"}
    else:
        U["FD1_karte"] = {"exponent": f1k["s"], "ci95": [f1k["lo"], f1k["hi"]], "L": f1k["L"],
                          "urteil": "eingetroffen" if a1 <= f1k["s"] <= b1 else "nicht eingetroffen"}
    if f1p is None or f1p["L"] != L4:
        U["FD1_plan"] = {"urteil": "nicht auswertbar (nicht alle fuenf L mit Knickdichte im Band)",
                         "L": (f1p or {}).get("L")}
    else:
        lo, hi = f1p["lo"], f1p["hi"]
        if a1 <= lo and hi <= b1:
            u = "eingetroffen"
        elif hi < a1 or lo > b1:
            u = "nicht eingetroffen"
        else:
            u = "uneindeutig"
        U["FD1_plan"] = {"exponent": f1p["s"], "ci95": [lo, hi], "L": f1p["L"], "urteil": u}
    # FD2: lokale Steigung von ln P zwischen L = 32 und 64, RP D = 4, Schwelle -0,25
    if f2p is None or f2p["L"] != [32, 48, 64]:
        U["FD2_plan"] = {"urteil": "nicht auswertbar", "L": (f2p or {}).get("L")}
    else:
        faellt = bool(f2p["s"] < F.S_PLAN and f2p["hi"] < 0)
        U["FD2_plan"] = {"steigung": f2p["s"], "ci95": [f2p["lo"], f2p["hi"]], "faellt_schwellregel": faellt,
                         "ci_ganz_unter_schwelle": bool(f2p["hi"] < FD2_SCHWELLE),
                         "urteil": "eingetroffen (Grenze 3)" if faellt else "nicht eingetroffen"}
    if f2k is None or f2k["L"] != [32, 64]:
        U["FD2_karte"] = {"urteil": "nicht auswertbar"}
    else:
        U["FD2_karte"] = {"steigung_zweipunkt": f2k["s"], "ci95": [f2k["lo"], f2k["hi"]],
                          "urteil": "eingetroffen" if f2k["s"] < FD2_SCHWELLE else "nicht eingetroffen"}
    erg["urteile"] = U
    with open(out_json, "w") as f:
        json.dump(erg, f, indent=1)
    lines = ["FADEN-DIM-2 Auswertung (eingefrorener Code)", "",
             "Zellen: P (Wilson-95-%), P*L, Rate -ln(1-P), Knickdichte Start/Ende, kappa, Bloecke (Block, Treffer, n, ab)"]
    for z in erg["zellen"]:
        tm = z["t_median_durch_L2"]
        pe = z["p_end_rest"]
        lines.append(f"{z['dyn']:>2} D={z['D']} L={z['L']:>3} n={z['n']:>6} treffer={z['treffer']:>6} "
                     f"P={z['P']:.4f} [{z['P_lo']:.4f},{z['P_hi']:.4f}] PL={z['PL']:.3f} rate={z['rate']:.4f} "
                     f"tmed/L2={'-' if tm is None else f'{tm:.3f}'} p_nom={z['p_nom']} kappa={z['kappa']} "
                     f"rho0={z['p_start']:.4f} rhoE={'-' if pe is None else f'{pe:.4f}'} rho_ok={z['rho_ok']} "
                     f"acc={z['akzeptanz_lokal']} ab={z['abgebrochen']} bloecke={z['bloecke']}")
    lines.append("")
    lines.append("Fits (Steigung bzw. Exponent, Bootstrap-95-%)")
    for name, v in fits.items():
        if v.get("fehlt"):
            lines.append(f"{name}: fehlt (L = {v['L']})")
        else:
            lines.append(f"{name}: s={v['s']:+.4f} [{v['lo']:+.4f},{v['hi']:+.4f}] L={v['L']}")
    lines.append("")
    lines.append("Urteile")
    for k, v in U.items():
        lines.append(f"{k}: {json.dumps(v)}")
    with open(out_txt, "w") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(lines[-7:]), flush=True)


def modus_bild(ein, out):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    with open(ein) as f:
        erg = json.load(f)
    zs = erg["zellen"]
    fits = erg["fits"]
    fig, axs = plt.subplots(1, 3, figsize=(17, 5.4))
    stil = [("RP", 4, "#08519c", "s", "RP rau (Knickdichte 0,6), D = 4"), ("G", 4, "#222222", "o", "G glatt, D = 4"),
            ("RP", 5, "#d94801", "^", "RP rau (Knickdichte 0,6), D = 5")]
    for i, (dyn, D, col, mk, lab) in enumerate(stil):
        ax = axs[0] if D == 4 else axs[2]
        s = sorted([z for z in zs if z["dyn"] == dyn and z["D"] == D], key=lambda z: z["L"])
        if not s:
            continue
        L = np.array([z["L"] for z in s], float)
        P = np.array([z["P"] for z in s])
        lo = np.array([z["P_lo"] for z in s])
        hi = np.array([z["P_hi"] for z in s])
        ax.errorbar(L, P, yerr=[np.maximum(P - lo, 0), np.maximum(hi - P, 0)], color=col, marker=mk,
                    label=lab + ": P", capsize=2, lw=1.2, ms=5)
        R = np.array([z["rate"] for z in s])
        ax.plot(L, R, color=col, marker=mk, mfc="none", ls=":", lw=1, ms=7, label=lab + ": -ln(1-P)")
    for ax, t in [(axs[0], "D = 4: Treffanteil P und Rate -ln(1-P) bis T = 4 L^2"),
                  (axs[2], "D = 5 (beschreibend): P und Rate")]:
        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set_xlabel("Kantenlaenge L")
        ax.set_title(t, fontsize=10)
        ax.grid(True, which="both", alpha=0.3)
        ax.legend(fontsize=7, loc="lower left")
    f1 = fits.get("FD1_rate_RP4_16_64_plan", {})
    if "s" in f1:
        axs[0].text(0.98, 0.98, f"Rate RP D=4, L=16..64: Exponent {f1['s']:+.3f} [{f1['lo']:+.3f}; {f1['hi']:+.3f}]",
                    transform=axs[0].transAxes, ha="right", va="top", fontsize=8)
    ax = axs[1]
    for dyn, D, col, mk, Ls in [("RP", 4, "#08519c", "s", L4), ("G", 4, "#222222", "o", L4G), ("RP", 5, "#d94801", "^", L5)]:
        xs, ys, ylo, yhi = [], [], [], []
        for a, b in zip(Ls[:-1], Ls[1:]):
            v = fits.get(f"lokal_lnP_{dyn}{D}_{a}_{b}", {})
            if "s" not in v:
                continue
            xs.append(math.sqrt(a * b))
            ys.append(v["s"])
            ylo.append(v["s"] - v["lo"])
            yhi.append(v["hi"] - v["s"])
        if xs:
            ax.errorbar(xs, ys, yerr=[ylo, yhi], color=col, marker=mk, capsize=2, lw=1.2, ms=5,
                        label=f"{dyn} D = {D}: d ln P / d ln L (Nachbar-L)")
    f2 = fits.get("FD2_lnP_RP4_32_48_64_plan", {})
    if "s" in f2:
        ax.plot([32, 64], [f2["s"], f2["s"]], color="#08519c", lw=3, alpha=0.5,
                label=f"RP D = 4, L = 32..64 (Plan FD2): {f2['s']:+.3f}")
    ax.axhline(FD2_SCHWELLE, color="#999999", lw=0.9, ls="--", label="Schwelle -0,25")
    ax.axhline(0, color="#bbbbbb", lw=0.8)
    ax.set_xscale("log")
    ax.set_xlabel("L (geometrisches Mittel des Paares)")
    ax.set_ylabel("lokale Steigung")
    ax.set_title("Lokale Steigungen von ln P", fontsize=10)
    ax.grid(True, which="both", alpha=0.3)
    ax.legend(fontsize=7, loc="lower left")
    fig.suptitle("FADEN-DIM-2: geschlossene Faeden (+1/-1) auf Z_L^D, Rauheit ueber L konstant (synthetisch)")
    fig.tight_layout()
    fig.savefig(out, dpi=110)
    print("bild geschrieben", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("modus", choices=["kalib", "rauch", "lauf", "auswertung", "bild"])
    ap.add_argument("--zellen", default="")
    ap.add_argument("--out", default="")
    ap.add_argument("--ein", default="")
    ap.add_argument("--out-json", default="")
    ap.add_argument("--out-txt", default="")
    a = ap.parse_args()
    if a.modus == "kalib":
        modus_kalib()
    elif a.modus == "rauch":
        modus_rauch()
    elif a.modus == "lauf":
        modus_lauf([z for z in a.zellen.split(",") if z], a.out)
    elif a.modus == "auswertung":
        modus_auswertung([f for f in a.ein.split(",") if f], a.out_json, a.out_txt)
    else:
        modus_bild(a.ein, a.out)


if __name__ == "__main__":
    main()
