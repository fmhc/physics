#!/usr/bin/env python3
"""QUARK-2 (Runde 12): Dirac-Fermionen im Q-Ball-Profil als Beutel.

Profil: f'' + (2/r) f' = (1 - w2 - 2 f^2 + 1.5 f^4) f  (U = S - S^2 + S^3/2), S = f^2.
Fermion: m(r) = M (1 - lam S(r)), lam = 1/S(0) (Masse innen 0, aussen M).
Radial: G' = -(k/r) G + (E + m) F ;  F' = (k/r) F - (E - m) G.
Gebundene positive Niveaus 0 < E < E_max < M ueber Vorzeichenwechsel von G am Aussenrand, dann Bisektion.
Kontrollen: K1 lam = 0 (keine Niveaus), K2 harte Stufe (MIT-Wert 2,043), K3 zwei Toleranzstufen.
CPU, numpy/scipy, keine GPU noetig.
"""
import argparse
import json
import math
import os
import time

import numpy as np
from scipy.integrate import solve_ivp

KAPPAS = [-1, 1, -2, 2, -3]
NAMEN = {-1: "s1/2", 1: "p1/2", -2: "p3/2", 2: "d3/2", -3: "d5/2"}


def profil(w2, r_max=120.0, n_bis=200):
    """Schiessen auf f(0) per Bisektion. Liefert Gitter r, S(r), a = f(0), R_h, Abbruchradius."""
    c0 = 1.0 - w2

    def rhs(r, y):
        f, fp = y
        return [fp, (c0 - 2.0 * f * f + 1.5 * f ** 4) * f - 2.0 * fp / r]

    def schuss(a):
        r0 = 1e-6
        c = (c0 - 2.0 * a * a + 1.5 * a ** 4) * a
        y0 = [a + c * r0 * r0 / 6.0, c * r0 / 3.0]

        def ueber(r, y):
            return y[0]
        ueber.terminal, ueber.direction = True, -1

        def unter(r, y):
            return y[1]
        unter.terminal, unter.direction = True, 1
        sol = solve_ivp(rhs, (r0, r_max), y0, method="DOP853", rtol=1e-12, atol=1e-14,
                        events=(ueber, unter), dense_output=True)
        if sol.t_events[0].size:
            return "ueber", sol
        if sol.t_events[1].size:
            return "unter", sol
        return "unentschieden", sol

    # Klammer aus dem mechanischen Bild V(S) = S [(w2 - 1) + S - S^2/2]: Start zwischen der Nullstelle
    # S_- = 1 - sqrt(2 w2 - 1) (zu wenig Energie, Unterschuss) und dem Maximum S_h = (2 + sqrt(6 w2 - 2))/3
    # (genug Energie, Ueberschuss); vgl. die Schranke S_max < S_h(omega^2) aus Runde 10.
    S_minus = 1.0 - math.sqrt(2.0 * w2 - 1.0)
    S_h = (2.0 + math.sqrt(6.0 * w2 - 2.0)) / 3.0
    lo, hi = math.sqrt(S_minus) * (1.0 + 1e-6), math.sqrt(S_h) - 1e-14
    if schuss(lo)[0] != "unter" or schuss(hi)[0] != "ueber":
        raise RuntimeError(f"Klammer fuer w2 = {w2} nicht gueltig: {schuss(lo)[0]}, {schuss(hi)[0]}")
    best = None
    for _ in range(n_bis):
        mid = 0.5 * (lo + hi)
        if mid in (lo, hi):
            break
        art, sol = schuss(mid)
        if art == "ueber":
            hi = mid
        else:
            lo = mid
            best = sol
    # Profil der letzten Unterschiessung bis zum Minimum von f (danach steigt es wieder an): dort abschneiden.
    sol = best
    r_end = sol.t[-1]
    rr = np.linspace(1e-6, r_end, 200001)
    ff = sol.sol(rr)[0]
    i_min = int(np.argmin(ff))
    r_cut = rr[i_min]
    S = np.where(rr <= r_cut, ff * ff, 0.0)
    S0 = S[0]
    i_h = int(np.argmax(S < 0.5 * S0))
    R_h = float(rr[i_h])
    return {"r": rr, "S": S, "a": 0.5 * (lo + hi), "S0": float(S0), "R_h": R_h, "r_cut": float(r_cut),
            "a_klammer": [lo, hi]}


def dirac_vorzeichen(E_vec, kappa, m_fun, r_end, rtol, atol, r0=1e-5, bruch=None):
    """Integriert fuer alle E gleichzeitig von r0 bis r_end; liefert G(r_end) (Vorzeichen zaehlt)."""
    E = np.asarray(E_vec, dtype=float)
    n = E.size
    k = abs(kappa)
    m0 = m_fun(np.array([r0]))[0]
    if kappa < 0:
        G0 = np.full(n, r0 ** k)
        F0 = -(E - m0) / (2 * k + 1) * r0 ** (k + 1)
    else:
        F0 = np.full(n, r0 ** k)
        G0 = (E + m0) / (2 * k + 1) * r0 ** (k + 1)
    y = np.concatenate([G0, F0])

    def rhs(r, yy):
        G, F = yy[:n], yy[n:]
        m = m_fun(np.array([r]))[0]
        return np.concatenate([-(kappa / r) * G + (E + m) * F, (kappa / r) * F - (E - m) * G])

    punkte = [r0] + ([b for b in (bruch or []) if r0 < b < r_end]) + [r_end]
    for a, b in zip(punkte[:-1], punkte[1:]):
        sol = solve_ivp(rhs, (a, b), y, method="DOP853", rtol=rtol, atol=atol)
        y = sol.y[:, -1]
        # Normieren je E-Spalte, damit nichts ueberlaeuft (Vorzeichen bleibt).
        s = np.maximum(np.abs(y[:n]), np.abs(y[n:]))
        s = np.where(s > 0, s, 1.0)
        y = np.concatenate([y[:n] / s, y[n:] / s])
    return y[:n]


def niveaus(kappa, m_fun, E_lo, E_hi, r_end, rtol, atol, n_scan=300, n_bis=60, bruch=None):
    Es = np.linspace(E_lo, E_hi, n_scan)
    g = dirac_vorzeichen(Es, kappa, m_fun, r_end, rtol, atol, bruch=bruch)
    sg = np.sign(g)
    idx = np.where(sg[:-1] * sg[1:] < 0)[0]
    lo, hi = Es[idx].copy(), Es[idx + 1].copy()
    if lo.size == 0:
        return []
    s_lo = sg[idx].copy()
    for _ in range(n_bis):
        mid = 0.5 * (lo + hi)
        gm = np.sign(dirac_vorzeichen(mid, kappa, m_fun, r_end, rtol, atol, bruch=bruch))
        gleich = gm == s_lo
        lo = np.where(gleich, mid, lo)
        hi = np.where(gleich, hi, mid)
    return [float(x) for x in 0.5 * (lo + hi)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--M", type=float, default=10.0)
    ap.add_argument("--w2", default="0.55,0.60,0.65,0.70,0.80")
    ap.add_argument("--n-scan", dest="n_scan", type=int, default=150)
    ap.add_argument("--n-bis", dest="n_bis", type=int, default=45)
    ap.add_argument("--t2", default="0.55,0.80", help="omega^2-Werte mit zweiter Toleranzstufe (K3)")
    ap.add_argument("--kappas", default="-1,1,-2,2,-3")
    ap.add_argument("--ohne-k", dest="ohne_k", action="store_true", help="K1/K2 hier auslassen")
    ap.add_argument("--rauch", action="store_true", help="nur kleine Formprobe, Zahlen ohne Bedeutung")
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)
    t0 = time.time()
    M = args.M
    stufen = {"T1": (1e-9, 1e-11), "T2": (1e-11, 1e-13)}
    kappas = [int(k) for k in args.kappas.split(",")]
    t2_liste = [float(x) for x in args.t2.split(",")] if args.t2 else []
    erg = {"M": M, "kappas": kappas, "stufen": {k: list(v) for k, v in stufen.items()}, "baelle": [], "kontrollen": {},
           "fassung": "v2: Rechenbereich bis Wandende + 3, Zwischenspeichern, T2 nur fuer --t2"}
    pfad = os.path.join(args.out, "quark2.json")

    def speichern():
        erg["sekunden"] = time.time() - t0
        with open(pfad + ".neu", "w") as fh:
            json.dump(erg, fh, indent=1)
        os.replace(pfad + ".neu", pfad)

    if not args.ohne_k:
        def m_stufe(r):
            return np.where(r < 10.0, 0.0, 200.0)
        k2 = {}
        for name, (rt, at) in stufen.items():
            lv = niveaus(-1, m_stufe, 0.05, 0.6, 10.5, rt, at, n_scan=60, n_bis=args.n_bis, bruch=[10.0])
            k2[name] = {"E_1s": lv[0] if lv else None, "E_1s_mal_R": (lv[0] * 10.0) if lv else None}
        erg["kontrollen"]["K2_harte_stufe"] = k2
        speichern()
        print(f"K2 fertig nach {time.time() - t0:.1f} s: {json.dumps(k2)}", flush=True)

    w2_liste = [float(x) for x in args.w2.split(",")]
    if args.rauch:
        w2_liste = w2_liste[:1]
    for w2 in w2_liste:
        p = profil(w2)
        r, S = p["r"], p["S"]
        lam = 1.0 / p["S0"]
        i_wand = int(np.argmax(S < 1e-9 * p["S0"]))
        r_wand = float(r[i_wand])
        r_end = r_wand + 3.0

        def m_ball(rq, r=r, S=S, lam=lam):
            return M * (1.0 - lam * np.interp(rq, r, S))
        ball = {"w2": w2, "a": p["a"], "S0": p["S0"], "R_h": p["R_h"], "r_cut": p["r_cut"], "r_wand": r_wand,
                "r_end": r_end, "stufen": {}}
        erg["baelle"].append(ball)
        print(f"w2 = {w2}: Profil nach {time.time() - t0:.1f} s, S0 = {p['S0']:.6f}, R_h = {p['R_h']:.4f}, "
              f"r_wand = {r_wand:.3f}", flush=True)
        for name, (rt, at) in stufen.items():
            if name == "T2" and (args.rauch or w2 not in t2_liste):
                continue
            ball["stufen"][name] = {}
            for kappa in kappas:
                lv = niveaus(kappa, m_ball, 0.02, 0.98 * M, r_end, rt, at, n_scan=args.n_scan, n_bis=args.n_bis)
                ball["stufen"][name][NAMEN[kappa]] = lv
                speichern()
                print(f"  {name} {NAMEN[kappa]}: {len(lv)} Niveaus, erstes {lv[0] if lv else None}, "
                      f"nach {time.time() - t0:.1f} s", flush=True)
        if not args.ohne_k and "K1_lam0" not in erg["kontrollen"]:
            def m_konst(rq):
                return np.full_like(rq, M, dtype=float)
            erg["kontrollen"]["K1_lam0"] = {NAMEN[k]: niveaus(k, m_konst, 0.02, 0.98 * M, r_end, 1e-9, 1e-11,
                                                              n_scan=args.n_scan, n_bis=args.n_bis) for k in kappas}
            speichern()
            print(f"K1 fertig nach {time.time() - t0:.1f} s: {json.dumps(erg['kontrollen']['K1_lam0'])}", flush=True)
    erg["rauch"] = args.rauch
    speichern()
    # Kurzbericht
    zeilen = [f"QUARK-2, M = {M}, Dauer {erg['sekunden']:.1f} s" + ("  RAUCHTEST: Zahlen ohne Bedeutung" if args.rauch else "")]
    zeilen.append(f"K2 harte Stufe: {json.dumps(erg['kontrollen'].get('K2_harte_stufe'))}")
    zeilen.append(f"K1 lam = 0: {json.dumps(erg['kontrollen'].get('K1_lam0'))}")
    for b in erg["baelle"]:
        zeilen.append(f"w2 = {b['w2']}: a = {b['a']:.12f}, S0 = {b['S0']:.6f}, R_h = {b['R_h']:.4f}, r_cut = {b['r_cut']:.3f}")
        for name, lv in b["stufen"].items():
            e1 = lv["s1/2"][0] if lv.get("s1/2") else float("nan")
            zeilen.append(f"  {name}: " + "; ".join(f"{k}: " + ", ".join(f"{x:.6f}" for x in v) for k, v in lv.items()))
            if lv.get("s1/2"):
                zeilen.append(f"    E(1s1/2) R_h = {e1 * b['R_h']:.4f}; Verhaeltnisse p3/2 {lv['p3/2'][0] / e1 if lv.get('p3/2') else float('nan'):.4f},"
                              f" p1/2 {lv['p1/2'][0] / e1 if lv.get('p1/2') else float('nan'):.4f}")
    text = "\n".join(zeilen)
    with open(os.path.join(args.out, "quark2_bericht.txt"), "w") as fh:
        fh.write(text + "\n")
    print(text, flush=True)


if __name__ == "__main__":
    main()
