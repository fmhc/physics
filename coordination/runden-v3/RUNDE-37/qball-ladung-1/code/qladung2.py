"""QBALL-LADUNG-1, Fassung 2 (Runde 37, Leitung claude-primary): geeichte M1-Q-Baelle, kugelsymmetrisch, statisch.

Gleichungen mit g(r) = Omega(r) = omega - e A_0(r):
    f'' + (2/r) f' + g^2 f - U'(f^2) f = 0
    g'' + (2/r) g' = 2 e^2 f^2 g
U(S) = S - S^2 + beta S^3, beta = 1/2.
Ladung Q = int 2 g f^2 d^3x, Energie E = int [g^2 f^2 + f'^2 + U + g'^2/(2 e^2)] d^3x (+ Feld aussen).
Familienparameter Omega_0 = g(0); f(0) per Bisektion (Ueberschiessen: f < 0; Unterschiessen: f' > 0 bei f > 0 oder f > 5).

Neu gegenueber Fassung 1 (nach den ersten Familienlaeufen, offengelegt):
  - robuste Klammer: Gitterabtastung in S0 = f(0)^2, wenn die schnelle Klammer (S_minus bis knapp unter der Spitze) versagt;
  - Gueltigkeit: Schnittamplitude f(r_c)/f(0) < 1e-3, sonst "ungueltig";
  - Modus zielQ: Omega_0 per Bisektion so, dass Q einen Zielwert trifft (fuer QL1 statt Interpolation).

Aufruf (nur ueber kleintest.sh auf der .69):
  qladung2.py <e1,e2,...> familie2 <ausgabe.json>
  qladung2.py <e1,e2,...> zielQ:300,1000 <ausgabe.json>
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


def ev_gross(r, y, e2):
    return y[0] - 5.0
ev_gross.terminal = True
ev_gross.direction = 1


def schiessen(f0, g0, e2, dichte=False):
    sol = solve_ivp(rhs, (R0, RMAX), start(f0, g0, e2), args=(e2,), method="DOP853", rtol=RTOL, atol=ATOL,
                    events=(ev_ueber, ev_unter, ev_gross), dense_output=dichte)
    if sol.t_events[0].size:
        return +1, sol
    if sol.t_events[1].size or sol.t_events[2].size:
        return -1, sol
    return (+1 if sol.y[0, -1] < 0 else -1), sol


def bisektion(lo, hi, g0, e2, iter_max=80):
    for _ in range(iter_max):
        mid = 0.5 * (lo + hi)
        if mid == lo or mid == hi:
            break
        k, _ = schiessen(np.sqrt(mid), g0, e2)
        if k == +1:
            hi = mid
        else:
            lo = mid
    return lo, hi


def auswerten(lo, hi, g0, e2):
    k1, s1 = schiessen(np.sqrt(lo), g0, e2, dichte=True)
    k2, s2 = schiessen(np.sqrt(hi), g0, e2, dichte=True)
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
    knotenfrei = bool(np.all(y1[0, :i_min + 1] > 0))
    omega = g_c + rc * gp_c
    e_aussen = 2.0 * np.pi * rc ** 3 * gp_c ** 2 / e2 if e2 > 0 else 0.0
    E = e_c + e_aussen
    Q = q_c
    i_half = int(np.argmin(np.abs(y1[0, :i_min + 1] ** 2 - 0.5 * f0 ** 2)))
    f_rel = float(abs(f_c) / f0)
    return {"status": "ok" if (f_rel < 1e-3 and knotenfrei) else "ungueltig", "Omega0_2": g0 * g0, "f0_2": lo,
            "Klammerbreite": hi - lo, "r_schnitt": float(rc), "f_schnitt_rel": f_rel, "knotenfrei": knotenfrei,
            "omega": float(omega), "omega2": float(omega * omega), "Q": float(Q), "E": float(E),
            "E_durch_Q": float(E / Q), "E_feld_aussen": float(e_aussen), "g_rand": float(g_c),
            "R_halb": float(rr[i_half])}


def loesung(g0, e2, robust=True):
    w2 = g0 * g0
    disk = 2.0 * w2 - 1.0
    if disk <= 0:
        return {"status": "kein Bereich", "Omega0_2": w2}
    s_minus = 1.0 - np.sqrt(disk)
    s_spitze = (2.0 + np.sqrt(max(6.0 * w2 - 2.0, 0.0))) / 3.0
    lo = s_minus * (1 + 1e-9)
    k_lo, _ = schiessen(np.sqrt(lo), g0, e2)
    k_hi, hi = -1, s_spitze
    if k_lo == -1:
        for delta in (1e-10, 1e-8, 1e-6, 1e-4, 1e-3, 1e-2, 3e-2):
            hi = s_spitze * (1.0 - delta)
            k_hi, _ = schiessen(np.sqrt(hi), g0, e2)
            if k_hi == +1:
                break
    if k_lo == -1 and k_hi == +1:
        lo, hi = bisektion(lo, hi, g0, e2)
        res = auswerten(lo, hi, g0, e2)
        res["klammer"] = "schnell"
        if res["status"] == "ok" or not robust:
            return res
    if not robust:
        return {"status": "keine Klammer", "Omega0_2": w2}
    # Gitterabtastung in S0
    gitter = np.concatenate([np.geomspace(1e-3, 0.3, 12), np.linspace(0.32, 3.0, 50)])
    ks = [schiessen(np.sqrt(s), g0, e2)[0] for s in gitter]
    muster = "".join("+" if k == 1 else "-" for k in ks)
    kandidaten = []
    for i in range(len(gitter) - 1):
        if ks[i] == -1 and ks[i + 1] == +1:
            a, b = bisektion(gitter[i], gitter[i + 1], g0, e2)
            r = auswerten(a, b, g0, e2)
            r["klammer"] = "gitter"
            kandidaten.append(r)
    gueltig = [r for r in kandidaten if r["status"] == "ok"]
    if gueltig:
        best = gueltig[0]
        best["muster"] = muster
        best["kandidaten"] = len(kandidaten)
        return best
    return {"status": "keine Loesung", "Omega0_2": w2, "muster": muster, "kandidaten": len(kandidaten),
            "kandidaten_f_rel": [r["f_schnitt_rel"] for r in kandidaten]}


def ziel_q(e, qziel, w2_start=0.80, w2_ende=0.56, schritt=0.02):
    e2 = e * e
    vorher = None
    w2 = w2_start
    while w2 >= w2_ende - 1e-12:
        r = loesung(np.sqrt(w2), e2)
        if r.get("status") == "ok":
            if vorher is not None and (vorher["Q"] - qziel) * (r["Q"] - qziel) <= 0:
                a, b = vorher["Omega0_2"], r["Omega0_2"]
                qa, qb = vorher["Q"], r["Q"]
                for _ in range(60):
                    m = 0.5 * (a + b)
                    rm = loesung(np.sqrt(m), e2)
                    if rm.get("status") != "ok":
                        return {"status": "Abbruch in Bisektion", "e": e, "Q_ziel": qziel}
                    if (qa - qziel) * (rm["Q"] - qziel) <= 0:
                        b, qb, r_b = m, rm["Q"], rm
                    else:
                        a, qa = m, rm["Q"]
                    if abs(rm["Q"] / qziel - 1.0) < 1e-8 or abs(b - a) < 1e-14:
                        rm["Q_ziel"] = qziel
                        rm["e"] = e
                        return rm
                rm["Q_ziel"] = qziel
                rm["e"] = e
                rm["status"] = "ok (Iterationsgrenze)"
                return rm
            vorher = r
        w2 = round(w2 - schritt, 6)
    return {"status": "Ziel nicht geklammert", "e": e, "Q_ziel": qziel}


def main():
    elist = [float(x) for x in sys.argv[1].split(",")]
    modus = sys.argv[2]
    ausgabe = sys.argv[3]
    t0 = time.time()
    erg = {"e": elist, "modus": modus, "beta": BETA, "rmax": RMAX, "rtol": RTOL, "skript_sha256": SKRIPT_SHA,
           "numpy": np.__version__, "scipy": scipy.__version__}

    def sichern():
        erg["zeit_s"] = round(time.time() - t0, 1)
        with open(ausgabe, "w") as fh:
            json.dump(erg, fh, indent=1)

    if modus == "familie2":
        w2liste = list(np.round(np.concatenate([np.arange(0.98, 0.60, -0.02), np.arange(0.60, 0.5049, -0.005),
                                                [0.503, 0.502, 0.501]]), 4))
        erg["Omega0_2_liste"] = w2liste
        erg["familien"] = {}
        for e in elist:
            fam = []
            for w2 in w2liste:
                t1 = time.time()
                res = loesung(np.sqrt(w2), e * e)
                res["sek"] = round(time.time() - t1, 2)
                fam.append(res)
                erg["familien"][str(e)] = fam
                sichern()
    elif modus.startswith("zielQ:"):
        ziele = [float(x) for x in modus.split(":")[1].split(",")]
        erg["ziele"] = []
        for e in elist:
            for qz in ziele:
                t1 = time.time()
                res = ziel_q(e, qz)
                res["sek"] = round(time.time() - t1, 2)
                erg["ziele"].append(res)
                sichern()
    erg["zeit_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    sichern()
    print(json.dumps({"e": elist, "modus": modus, "zeit_s": erg["zeit_s"]}))


if __name__ == "__main__":
    main()
