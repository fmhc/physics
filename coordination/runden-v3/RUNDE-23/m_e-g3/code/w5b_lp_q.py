# W5 (Plan M_E-G3): Funktionale fuer die Vier-Graviton-MHV-Regeln B2^(1), B3^(1) (CHLPSD 2201.06602).
# Modi:
#   check        W5a (3.3a)->(3.4a) mit/ohne g5, W5b (3.7)->1598, W5c Positivitaet von (3.7) und F_g3 auf schweren Zustaenden
#   lp N b0      W5d lineares Programm: reine B2/B3-Funktionale, Polynomgrad N, b0=0/1 (psi3(0) frei oder null)
# Einheiten M = 1, G = 1 auf der IR-Seite. Glaettung der UV-Seite ab p = 0 (BBIRRS 2512.13780, Gl. (5.9), (5.13)).
# Schwere Dichten nach CHLPSD (2.33), (2.35a), Anh. A: d00 = P_J(x), d44 = P^(0,8)_{J-4}(x), x = 1 - 2 p^2/m^2.
import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
import sys
import time
import json
import numpy as np
from numpy.polynomial import polynomial as npp
from scipy.special import eval_jacobi, j0, roots_legendre
from scipy.optimize import linprog

T0 = time.time()
PI = np.pi


def gl01(n):
    x, w = roots_legendre(n)
    return 0.5 * (x + 1.0), 0.5 * w


PN, PW = gl01(700)


def pev(c, p):
    """Polynom mit aufsteigenden Koeffizienten c an Stellen p."""
    return npp.polyval(p, c)


def legendre_all(x, jmax):
    out = np.empty((jmax + 1, x.size))
    out[0] = 1.0
    if jmax >= 1:
        out[1] = x
    for n in range(1, jmax):
        out[n + 1] = ((2 * n + 1) * x * out[n] - n * out[n - 1]) / (n + 1)
    return out


def jac08_all(x, jmax, al=0.0, be=8.0):
    """d44~^J(x) = P^(0,8)_{J-4}(x) fuer J = 4..jmax; Zeile J-4. Drei-Term-Rekursion (Abramowitz-Stegun 22.7.1)."""
    nmax = jmax - 4
    out = np.empty((nmax + 1, x.size))
    out[0] = 1.0
    if nmax >= 1:
        out[1] = (al + 1.0) + (al + be + 2.0) * (x - 1.0) / 2.0
    for n in range(2, nmax + 1):
        s = 2 * n + al + be
        a1 = 2 * n * (n + al + be) * (s - 2)
        a2 = (s - 1) * (al * al - be * be)
        a3 = (s - 2) * (s - 1) * s
        a4 = 2 * (n + al - 1) * (n + be - 1) * s
        out[n] = ((a2 + a3 * x) * out[n - 1] - a4 * out[n - 2]) / a1
    return out


def jac08_selftest():
    x = np.linspace(-1, 1, 7)
    d = jac08_all(x, 60)
    ref = eval_jacobi(np.arange(0, 57)[:, None], 0.0, 8.0, x[None, :])
    return float(np.max(np.abs(d - ref) / (1 + np.abs(ref))))


def ir_side(psi2, psi3, c4=0.0):
    """IR-Seite -F|low = 16 pi (a1 L + c0) + xcoef * x + c4 * g5 (G = M = 1), CHLPSD (2.31a,b), (2.32a)."""
    psi2 = np.asarray(psi2, float)
    psi3 = np.asarray(psi3, float)
    assert abs(psi2[0]) < 1e-12
    a1 = psi2[1]
    c0 = sum(psi2[k] / (k - 1) for k in range(2, psi2.size))
    i2p6 = sum(psi2[k] / (k + 7) for k in range(psi2.size))
    i3p4 = sum(psi3[k] / (k + 5) for k in range(psi3.size))
    xcoef = 2 * PI * (i2p6 - i3p4) + 4 * PI * c4  # Koeffizient von x auf der IR-Seite
    slope = 16 * PI * a1 / (-xcoef)
    const = 16 * PI * c0 / (-xcoef)
    g5c = c4 / (-xcoef)
    return dict(a1=a1, c0=c0, I2p6=i2p6, I3p4=i3p4, xcoef_over_pi=xcoef / PI,
                slope=slope, const=const, g5_coeff=g5c)


def heavy_min(psi2, psi3, c4, mgrid, jmax, bgrid):
    """Minimum der (positiv reskalierten) Wirkung auf schweren Zustaenden, getrennt ++ und +-,
    und im Grenzfall m -> unendlich bei festem b (B2-dominiert, CHLPSD (3.5))."""
    p = PN
    w = PW
    v2 = pev(psi2, p)
    v3 = pev(psi3, p)
    res = {"pp": (np.inf, None), "pm": (np.inf, None)}
    for m in mgrid:
        x = 1.0 - 2.0 * p * p / (m * m)
        base_pp = w * (v2 * (2 * m * m - p * p) + v3)
        base_pm = w * (v2 * (2 * m * m - p * p) - v3)
        L = legendre_all(x, jmax)
        Jv = np.arange(jmax + 1)
        calJ = Jv * (Jv + 1.0)
        fpp = L @ base_pp + c4 * (1 - 2 * calJ) / m**4
        # Normierung fuer Vergleichbarkeit: m^6 F / (2 m^2 * max(1, b^-...)) -> hier relative Skala per |Integrand|
        scale_pp = np.abs(L) @ np.abs(base_pp) + abs(c4) * np.abs(1 - 2 * calJ) / m**4 + 1e-300
        rpp = fpp / scale_pp
        for J in range(0, jmax + 1, 2):
            if rpp[J] < res["pp"][0]:
                res["pp"] = (float(rpp[J]), (float(m), J, float(fpp[J])))
        D = jac08_all(x, jmax)
        Jm = np.arange(4, jmax + 1)
        calJm = Jm * (Jm + 1.0)
        fpm = D @ base_pm + c4 * (41 - 2 * calJm) / m**4
        scale_pm = np.abs(D) @ np.abs(base_pm) + abs(c4) * np.abs(41 - 2 * calJm) / m**4 + 1e-300
        rpm = fpm / scale_pm
        k = int(np.argmin(rpm))
        if rpm[k] < res["pm"][0]:
            res["pm"] = (float(rpm[k]), (float(m), int(Jm[k]), float(fpm[k])))
    # Grenzfall m -> unendlich, b fest: Int psi2(p) J0(b p) dp
    lim = []
    for b in bgrid:
        lim.append(float(np.sum(w * v2 * j0(b * p))))
    lim = np.array(lim)
    k = int(np.argmin(lim))
    res["scaling"] = (float(lim[k]), float(bgrid[k]))
    return res


def mgrid_std(mmax=40.0):
    return np.unique(np.concatenate([[1.0], 1.0 + np.geomspace(1e-5, 0.2, 40),
                                     np.linspace(1.2, 3.0, 46), np.geomspace(3.0, mmax, 50)]))


def run_check():
    out = {}
    out["jacobi_rekursion_vs_scipy_maxrelfehler"] = jac08_selftest()
    # (3.3a) F_g3 = int (1-p)^3 ( p(65+155p+47p^2) B2 + 2(81-1927p+4601p^2) B3 ) - 5 d/dp^2 B4|_{p=0}
    om3 = npp.polypow([1.0, -1.0], 3)
    psi2_g3 = npp.polymul(om3, [0.0, 65.0, 155.0, 47.0])
    psi3_g3 = npp.polymul(om3, [162.0, -3854.0, 9202.0])
    out["W5a_Fg3_ir"] = ir_side(psi2_g3, psi3_g3, c4=-5.0)
    # (3.3b) F_g4 nur IR-Seite zum Vergleich mit (3.4b): -(7 + d/dp^2) B4 -> g4-Term -14 g4, x-Term -4 pi x, g5-Term -g5
    psi2_g4 = npp.polymul(om3, [0.0, 99.0, 282.0, 49.0])
    psi3_g4 = npp.polymul(om3, [21.0, -474.0, 1216.0])
    r = ir_side(psi2_g4, psi3_g4, c4=-1.0)
    # g4 <= [16 pi (a1 L + c0) + xcoef x - g5] / 14 ; in Einheiten 8 pi G: /(8 pi)
    r["g4_slope_over_8piG"] = 16 * PI * r["a1"] / 14 / (8 * PI)
    r["g4_const_over_8piG"] = 16 * PI * r["c0"] / 14 / (8 * PI)
    r["g4_x_over_8piG"] = r["xcoef_over_pi"] * PI / 14 / (8 * PI)
    out["W5a_Fg4_ir"] = r
    # (3.7) reines B2/B3-Funktional
    psi2_37 = npp.polymul(npp.polypow([1.0, -1.0], 2),
                          [0.0, 798.968, -2194.19, 5294.87, -2322.66, -3443.55, 2006.03, -154.020])
    psi3_37 = np.array([0.00171, -157.911, 7603.72, -25581.3, 32684.9, -18251.2, 3701.82])
    out["W5b_37_ir"] = ir_side(psi2_37, psi3_37, c4=0.0)
    out["W5b_37_psi3_at_1"] = float(pev(psi3_37, 1.0))
    # Positivitaet (Gitter): m in [1, 40], J <= 200; Grenzfall b in (0, 400]
    bgrid = np.concatenate([np.linspace(0.0, 40.0, 801), np.linspace(40.0, 400.0, 1801)])
    mg = mgrid_std()
    out["W5c_37_heavy"] = heavy_min(psi2_37, psi3_37, 0.0, mg, 200, bgrid)
    out["W5c_Fg3_heavy"] = heavy_min(psi2_g3, psi3_g3, -5.0, mg, 200, bgrid)
    out["sekunden"] = time.time() - T0
    print(json.dumps(out, indent=1, default=float))


def basis_rows(N, b0free, mgrid, jmax, bgrid):
    """Zeilen der Positivitaetsbedingungen fuer v = (a_1..a_N, b_0..b_N), psi2 = (1-p)^2 sum a_n p^n,
    psi3 = (1-p)^2 sum b_n p^n."""
    p = PN
    w = PW
    om2 = (1 - p) ** 2
    phi = np.array([om2 * p**n for n in range(1, N + 1)])          # psi2-Basis
    chi = np.array([om2 * p**n for n in range(0, N + 1)])          # psi3-Basis
    if not b0free:
        chi = chi[1:]
    rows = []
    tags = []
    for m in mgrid:
        x = 1.0 - 2.0 * p * p / (m * m)
        A = phi * (w * (2 * m * m - p * p))[None, :]
        B = chi * w[None, :]
        jm = jmax if m > 1.5 else max(jmax, 320)   # an der Schwelle groessere Spins
        L = legendre_all(x, jm)
        Lpp = L[0::2]
        rpp = np.hstack([Lpp @ A.T, Lpp @ B.T])
        D = jac08_all(x, jm)
        rpm = np.hstack([D @ A.T, -(D @ B.T)])
        for blk, kind in ((rpp, "pp"), (rpm, "pm")):
            nrm = np.max(np.abs(blk), axis=1, keepdims=True) + 1e-300
            rows.append(blk / nrm)
            tags.append((kind, m, blk.shape[0]))
    # Grenzfall m -> unendlich: Int psi2 J0(b p) >= 0
    Jb = np.array([[np.sum(w * f * j0(b * p)) for f in phi] for b in bgrid])
    Jb = np.hstack([Jb, np.zeros((Jb.shape[0], chi.shape[0]))])
    nrm = np.max(np.abs(Jb), axis=1, keepdims=True) + 1e-300
    rows.append(Jb / nrm)
    return np.vstack(rows), phi.shape[0], chi.shape[0]


def thr_check(psi2, psi3, jmax=600):
    """+- an der Schwelle m = M (und knapp darueber) bis J = jmax: dort waechst d44~ = P^(0,8)_{J-4} bei x -> -1
    wie J^8 (Rueckwaertsrichtung); relative Minima."""
    p = PN
    w = PW
    v2 = pev(psi2, p)
    v3 = pev(psi3, p)
    out = {}
    for m in (1.0, 1.0 + 1e-6, 1.0 + 1e-4, 1.0 + 1e-3, 1.0 + 1e-2, 1.05, 1.1, 1.2, 1.3, 1.5, 2.0, 3.0):
        x = 1.0 - 2.0 * p * p / (m * m)
        base = w * (v2 * (2 * m * m - p * p) - v3)
        D = jac08_all(x, jmax)
        f = D @ base
        sc = np.abs(D) @ np.abs(base) + 1e-300
        r = f / sc
        k = int(np.argmin(r))
        out["m=%.6f" % m] = (float(r[k]), int(k + 4))
    return out


def run_lp(N, b0free, kthr):
    mg = np.unique(np.concatenate([[1.0], 1.0 + np.geomspace(1e-6, 0.5, 90), np.linspace(1.5, 4.0, 76),
                                   np.geomspace(4.0, 40.0, 40)]))
    jmax = 200
    bgrid = np.concatenate([np.linspace(0.0, 60.0, 1201), np.linspace(60.0, 400.0, 681)[1:]])
    R, na, nb = basis_rows(N, b0free, mg, jmax, bgrid)
    nv = na + nb
    # Zielfunktion: maximiere K = Int psi3 p^4 - Int psi2 p^6  (Int_0^1 (1-p)^2 p^k = 2/((k+1)(k+2)(k+3)))
    def I(k):
        return 2.0 / ((k + 1) * (k + 2) * (k + 3))
    ka = np.array([-I(n + 6) for n in range(1, N + 1)])
    kb = np.array([I(n + 4) for n in range(0 if b0free else 1, N + 1)])
    cobj = -np.concatenate([ka, kb])
    # a_1 = 1
    Aeq = [np.zeros(nv)]; Aeq[0][0] = 1.0
    beq = [1.0]
    # Schwellenbedingungen bei m = M, p -> 1: B(p) = psi2^(p)(2 - p^2) - psi3^(p) verschwindet bis Ordnung kthr-1
    nA = np.arange(1, N + 1, dtype=float)
    nB = np.arange(0 if b0free else 1, N + 1, dtype=float)
    conds = [(np.ones_like(nA), -np.ones_like(nB)),
             (nA - 2.0, -nB),
             (nA * nA - 5.0 * nA - 2.0, -nB * (nB - 1.0))]
    for k in range(kthr):
        ca, cb = conds[k]
        Aeq.append(np.concatenate([ca, cb])); beq.append(0.0)
    Aeq = np.vstack(Aeq); beq = np.array(beq)
    # Grossb-Bedingungen: nicht-oszillierender Schwanz ~ -g2/b^3 mit g2 = 2 m^2 psi2_2 +- psi3_2 (psi3(0) = 0 noetig),
    # schlimmster Fall m = M: 2 psi2_2 + psi3_2 <= -d und 2 psi2_2 - psi3_2 <= -d;
    # psi2_2 = a_2 - 2 a_1, psi3_2 = b_2 - 2 b_1 + b_0.
    Aub = [-R]
    bub = [np.zeros(R.shape[0])]
    if N >= 2:
        ia1, ia2 = 0, 1
        ib = {n: na + (n if b0free else n - 1) for n in range(0 if b0free else 1, N + 1)}
        for sgn in (+1.0, -1.0):
            row = np.zeros((1, nv))
            row[0, ia1] += -4.0; row[0, ia2] += 2.0
            row[0, ib[2]] += sgn * 1.0; row[0, ib[1]] += sgn * (-2.0)
            if b0free:
                row[0, ib[0]] += sgn * 1.0
            Aub.append(row); bub.append(np.array([-0.05]))
    Aub = np.vstack(Aub); bub = np.concatenate(bub)
    bounds = [(-5e4, 5e4)] * nv
    sol = linprog(cobj, A_ub=Aub, b_ub=bub, A_eq=Aeq, b_eq=beq, bounds=bounds, method="highs")
    out = {"N": N, "b0free": b0free, "kthr": kthr, "status": sol.status, "msg": sol.message,
           "rows": int(R.shape[0])}
    if sol.status == 0:
        v = sol.x
        a = v[:na]
        b = v[na:]
        K = -sol.fun
        psi2 = npp.polymul([1.0, -2.0, 1.0], np.concatenate([[0.0], a]))
        bfull = b if b0free else np.concatenate([[0.0], b])
        psi3 = npp.polymul([1.0, -2.0, 1.0], bfull)
        ir = ir_side(psi2, psi3, 0.0)
        out.update(K=K, c0_slope=8.0 / K, ir=ir, a=a.tolist(), b=b.tolist(),
                   max_abs_coef=float(np.max(np.abs(v))))
        # Nachpruefung auf feinerem und groesserem Gitter
        bfine = np.concatenate([np.linspace(0.0, 40.0, 2001), np.linspace(40.0, 600.0, 2801)])
        mfine = np.unique(np.concatenate([mgrid_std(60.0), np.linspace(1.0, 2.0, 101)]))
        out["nachpruefung"] = heavy_min(psi2, psi3, 0.0, mfine, 260, bfine)
        out["schwelle"] = thr_check(psi2, psi3, 600)
        out["psi2"] = psi2.tolist()
        out["psi3"] = psi3.tolist()
    out["sekunden"] = time.time() - T0
    print(json.dumps(out, indent=1, default=float))




# ---------------------------------------------------------------------------------------------------------------
# Variante mit Glaettung nur bis p = q < M (wie FRS (4.27): psi ~ (1 - p/q)^2 am Rand). Dann erreicht keine schwere
# Welle die Rueckwaertsrichtung x = -1, wo d44~ wie J^8 waechst (Schwellenecke m = M, J gross).

def ir_side_q(psi2, psi3, q):
    """IR-Seite fuer Glaettung p in [E, q]: -F|low = 16 pi (a1 log(1/E) + c0q) + xcoef x  (M = G = 1)."""
    psi2 = np.asarray(psi2, float)
    psi3 = np.asarray(psi3, float)
    a1 = psi2[1]
    c0q = sum(psi2[k] * q ** (k - 1) / (k - 1) for k in range(2, psi2.size)) + a1 * np.log(q)
    i2p6 = sum(psi2[k] * q ** (k + 7) / (k + 7) for k in range(psi2.size))
    i3p4 = sum(psi3[k] * q ** (k + 5) / (k + 5) for k in range(psi3.size))
    xcoef = 2 * PI * (i2p6 - i3p4)
    return dict(a1=a1, c0q=c0q, I2p6=i2p6, I3p4=i3p4, xcoef_over_pi=xcoef / PI,
                slope=16 * PI * a1 / (-xcoef), const=16 * PI * c0q / (-xcoef))


def run_lpq(N, q, jmax_lp, kend=2, delta=0.05):
    global PN, PW
    PN0, PW0 = gl01(700)
    PN, PW = q * PN0, q * PW0
    p, w = PN, PW
    u = p / q
    om2 = (1 - u) ** kend
    phi = np.array([om2 * u**n for n in range(1, N + 1)])
    chi = np.array([om2 * u**n for n in range(1, N + 1)])       # psi3(0) = 0
    na, nb = phi.shape[0], chi.shape[0]
    nv = na + nb
    mg = np.unique(np.concatenate([[1.0], 1.0 + np.geomspace(1e-6, 0.5, 90), np.linspace(1.0, 2.0, 201), np.linspace(1.5, 4.0, 101),
                                   np.geomspace(4.0, 40.0, 50)]))
    bgrid = np.concatenate([np.linspace(0.0, 60.0, 1201), np.linspace(60.0, 400.0, 681)[1:]])
    rows = []
    for m in mg:
        x = 1.0 - 2.0 * p * p / (m * m)
        A = phi * (w * (2 * m * m - p * p))[None, :]
        B = chi * w[None, :]
        L = legendre_all(x, jmax_lp)
        Lpp = L[0::2]
        D = jac08_all(x, jmax_lp)
        for blk in (np.hstack([Lpp @ A.T, Lpp @ B.T]), np.hstack([D @ A.T, -(D @ B.T)])):
            rows.append(blk / (np.max(np.abs(blk), axis=1, keepdims=True) + 1e-300))
    Jb = np.array([[np.sum(w * f * j0(b * p)) for f in phi] for b in bgrid])
    Jb = np.hstack([Jb, np.zeros((Jb.shape[0], nb))])
    rows.append(Jb / (np.max(np.abs(Jb), axis=1, keepdims=True) + 1e-300))
    R = np.vstack(rows)
    # Ziel: maximiere K = Int_0^q (psi3 p^4 - psi2 p^6) dp, Normierung a_1 = 1 (psi2 ~ p/q bei p -> 0)
    ka = np.array([-np.sum(w * f * p**6) for f in phi])
    kb = np.array([np.sum(w * f * p**4) for f in chi])
    cobj = -np.concatenate([ka, kb])
    Aeq = np.zeros((1, nv)); Aeq[0, 0] = 1.0
    beq = np.array([1.0])
    # Grossb: 2 psi2_2 +- psi3_2 <= -d (p^2-Koeffizienten in u: a_2 - 2 a_1 bzw. b_2 - 2 b_1)
    Aub = [-R]; bub = [np.zeros(R.shape[0])]
    for sgn in (+1.0, -1.0):
        row = np.zeros((1, nv))
        row[0, 0] += -2.0 * kend; row[0, 1] += 2.0
        row[0, na + 1] += sgn * 1.0; row[0, na + 0] += sgn * (-1.0 * kend)
        Aub.append(row); bub.append(np.array([-delta]))
    Aub = np.vstack(Aub); bub = np.concatenate(bub)
    sol = linprog(cobj, A_ub=Aub, b_ub=bub, A_eq=Aeq, b_eq=beq, bounds=[(-1e5, 1e5)] * nv, method="highs")
    out = {"N": N, "q": q, "kend": kend, "delta": delta, "jmax_lp": jmax_lp, "status": sol.status, "msg": sol.message, "rows": int(R.shape[0])}
    if sol.status == 0:
        v = sol.x
        a, b = v[:na], v[na:]
        # Polynome in p: psi = (1 - p/q)^2 sum c_n (p/q)^n
        ca = np.concatenate([[0.0], a / q ** np.arange(1, N + 1)])
        cb = np.concatenate([[0.0], b / q ** np.arange(1, N + 1)])
        omk = npp.polypow([1.0, -1.0 / q], kend)
        psi2 = npp.polymul(omk, ca)
        psi3 = npp.polymul(omk, cb)
        ir = ir_side_q(psi2, psi3, q)
        out.update(K=-sol.fun, ir=ir, a=a.tolist(), b=b.tolist(), max_abs_coef=float(np.max(np.abs(v))))
        bfine = np.concatenate([np.linspace(0.0, 40.0, 2001), np.linspace(40.0, 600.0, 2801)])
        mfine = np.unique(np.concatenate([mgrid_std(60.0), np.linspace(1.0, 2.0, 201), 1.0 + np.geomspace(1e-7, 1e-2, 30)]))
        out["nachpruefung"] = heavy_min(psi2, psi3, 0.0, mfine, 400, bfine)
        out["schwelle_bis_J3000"] = thr_check(psi2, psi3, 3000)
        out["psi2"] = psi2.tolist()
        out["psi3"] = psi3.tolist()
    out["sekunden"] = time.time() - T0
    print(json.dumps(out, indent=1, default=float))


if __name__ == "__main__":
    run_lpq(int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5]))
