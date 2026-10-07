"""QBALL-LADUNG-1 (Runde 37, Leitung claude-primary): geeichte M1-Q-Baelle, kugelsymmetrisch, statisch.

Gleichungen mit g(r) = Omega(r) = omega - e A_0(r):
    f'' + (2/r) f' + g^2 f - U'(f^2) f = 0
    g'' + (2/r) g' = 2 e^2 f^2 g
U(S) = S - S^2 + beta S^3, beta = 1/2.
Ladung Q = int 2 g f^2 d^3x, Energie E = int [g^2 f^2 + f'^2 + U + g'^2/(2 e^2)] d^3x (+ Feld aussen).
Familienparameter Omega_0 = g(0); f(0) per Bisektion (Ueberschiessen: f < 0; Unterschiessen: f' > 0 bei f > 0).

Aufruf (nur ueber kleintest.sh auf der .69): qladung.py <e1,e2,...> <omega0^2-Liste oder "familie"> <ausgabe.json>
"""
import hashlib
import json
import os
import sys
import time

import numpy as np
import scipy
from scipy.integrate import solve_ivp

BETA = 0.5
R0 = 1e-6
RMAX = 600.0
RTOL = 1e-12
ATOL = 1e-14
SKRIPT_SHA = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()


def Up(S):
    return 1.0 - 2.0 * S + 3.0 * BETA * S * S


def U(S):
    return S - S * S + BETA * S ** 3


def rhs(r, y, e2):
    f, fp, g, gp, q, en = y
    S = f * f
    fpp = -(2.0 / r) * fp - (g * g - Up(S)) * f
    gpp = -(2.0 / r) * gp + 2.0 * e2 * S * g
    dq = 8.0 * np.pi * g * S * r * r
    feld = gp * gp / (2.0 * e2) if e2 > 0 else 0.0
    den = 4.0 * np.pi * r * r * (g * g * S + fp * fp + U(S) + feld)
    return [fp, fpp, gp, gpp, dq, den]


def start(f0, g0, e2):
    fpp0 = -(g0 * g0 - Up(f0 * f0)) * f0 / 3.0
    gpp0 = 2.0 * e2 * f0 * f0 * g0 / 3.0
    return [f0 + 0.5 * fpp0 * R0 ** 2, fpp0 * R0, g0 + 0.5 * gpp0 * R0 ** 2, gpp0 * R0, 0.0, 0.0]


def ev_ueber(r, y, e2):
    return y[0]
ev_ueber.terminal = True
ev_ueber.direction = -1


def ev_unter(r, y, e2):
    return y[1]
ev_unter.terminal = True
ev_unter.direction = 1


def schiessen(f0, g0, e2, dichte=False):
    sol = solve_ivp(rhs, (R0, RMAX), start(f0, g0, e2), args=(e2,), method="DOP853", rtol=RTOL, atol=ATOL,
                    events=(ev_ueber, ev_unter), dense_output=dichte)
    if sol.t_events[0].size:
        return +1, sol      # ueberschiesst: f0 zu gross
    if sol.t_events[1].size:
        return -1, sol      # unterschiesst: f0 zu klein
    return (+1 if sol.y[0, -1] < 0 else -1), sol


def loesung(g0, e2, iter_max=70):
    """Bisektion ueber S0 = f0^2 im Bereich (S_minus, S_spitze) zu g0; Klammer bei Bedarf erweitern."""
    w2 = g0 * g0
    disk = 2.0 * w2 - 1.0
    if disk <= 0:
        return None
    s_minus = 1.0 - np.sqrt(disk)
    s_spitze = (2.0 + np.sqrt(max(6.0 * w2 - 2.0, 0.0))) / 3.0
    lo = s_minus * (1 + 1e-9)
    k_lo, _ = schiessen(np.sqrt(lo), g0, e2)
    # Obere Klammer: knapp unter der Spitze von W (innerer Hang); auf der Spitze selbst rollt das Teilchen beliebig ab.
    k_hi, hi = -1, s_spitze
    for delta in (1e-10, 1e-8, 1e-6, 1e-4, 1e-3, 1e-2, 3e-2):
        hi = s_spitze * (1.0 - delta)
        k_hi, _ = schiessen(np.sqrt(hi), g0, e2)
        if k_hi == +1:
            break
    if k_lo != -1 or k_hi != +1:
        return {"status": "keine Klammer", "k_lo": k_lo, "k_hi": k_hi, "S_lo": lo, "S_hi": hi}
    for _ in range(iter_max):
        mid = 0.5 * (lo + hi)
        if mid == lo or mid == hi:
            break
        k, _ = schiessen(np.sqrt(mid), g0, e2)
        if k == +1:
            hi = mid
        else:
            lo = mid
    k1, s1 = schiessen(np.sqrt(lo), g0, e2, dichte=True)
    k2, s2 = schiessen(np.sqrt(hi), g0, e2, dichte=True)
    # Schnittradius: bis dahin stimmen beide Laeufe auf 1e-7 relativ zu f0 ueberein, und f ist klein
    rr = np.linspace(R0, min(s1.t[-1], s2.t[-1]), 20001)
    y1, y2 = s1.sol(rr), s2.sol(rr)
    f0 = np.sqrt(lo)
    abw = np.abs(y1[0] - y2[0]) / f0
    gut = np.nonzero(abw > 1e-7)[0]
    i_ab = gut[0] if gut.size else len(rr) - 1
    i_min = int(np.argmin(np.abs(y1[0, :i_ab + 1])))
    rc = rr[i_min]
    yc = y1[:, i_min]
    f_c, g_c, gp_c, q_c, e_c = yc[0], yc[2], yc[3], yc[4], yc[5]
    omega = g_c + rc * gp_c
    e_aussen = 2.0 * np.pi * rc ** 3 * gp_c ** 2 / e2 if e2 > 0 else 0.0
    E = e_c + e_aussen
    Q = q_c
    # Halbwertsradius von f^2
    i_half = int(np.argmin(np.abs(y1[0, :i_min + 1] ** 2 - 0.5 * f0 ** 2)))
    return {"status": "ok", "Omega0_2": g0 * g0, "f0_2": lo, "Klammerbreite": hi - lo, "r_schnitt": float(rc),
            "f_schnitt_rel": float(abs(f_c) / f0), "omega": float(omega), "omega2": float(omega * omega),
            "Q": float(Q), "E": float(E), "E_durch_Q": float(E / Q), "E_feld_aussen": float(e_aussen),
            "g_rand": float(g_c), "R_halb": float(rr[i_half])}


def main():
    elist = [float(x) for x in sys.argv[1].split(",")]
    modus = sys.argv[2]
    ausgabe = sys.argv[3]
    t0 = time.time()
    if modus == "familie":
        w2liste = list(np.round(np.concatenate([np.arange(0.98, 0.60, -0.02), np.arange(0.60, 0.5049, -0.005)]), 4))
    else:
        w2liste = [float(x) for x in modus.split(",")]
    erg = {"e": elist, "Omega0_2_liste": w2liste, "familien": {}, "beta": BETA, "rmax": RMAX, "rtol": RTOL,
           "skript_sha256": SKRIPT_SHA, "numpy": np.__version__, "scipy": scipy.__version__}
    for e in elist:
        fam = []
        for w2 in w2liste:
            t1 = time.time()
            res = loesung(np.sqrt(w2), e * e)
            if res is None:
                res = {"status": "kein Bereich", "Omega0_2": w2}
            res["sek"] = round(time.time() - t1, 2)
            fam.append(res)
            with open(ausgabe, "w") as fh:
                erg["familien"][str(e)] = fam
                erg["zeit_s"] = round(time.time() - t0, 1)
                json.dump(erg, fh, indent=1)
        erg["familien"][str(e)] = fam
    erg["zeit_s"] = round(time.time() - t0, 1)
    erg["zeit_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    with open(ausgabe, "w") as fh:
        json.dump(erg, fh, indent=1)
    print(json.dumps({"e": elist, "n": len(w2liste), "zeit_s": erg["zeit_s"]}))


if __name__ == "__main__":
    main()
