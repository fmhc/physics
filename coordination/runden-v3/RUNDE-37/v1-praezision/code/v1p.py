#!/usr/bin/env python3
"""V-1-PRAEZISION (Runde 37), Code-Agent fuer die Leitung claude-primary, 04.10.2026.
Karte: RUNDE-37/v1-praezision/KARTE.md, Plan: RUNDE-37/v1-praezision/PLAN.md.
Vorlaeufer: RUNDE-36/v1-weiter/code/v1w.py (float64). Dasselbe Modell und dieselben Groessen, hier mit erweiterter
Genauigkeit:

  Feld:          phi_tt - phi_xx + eps phi_xxxx + U'(|phi|^2) phi = 0, U = S - S^2 + beta S^3, beta = 1
  Hintergrund:   eps f'''' - f'' + (U'(f^2) - om^2) f = 0, om = om_min = sqrt(3/4)
  Schwankungen:  eps Z'''' - Z'' + V(x) Z = 0, V = [[W - (rho-om)^2, C], [C, W - (rho+om)^2]],
                 W = 1 - 4S + 9 beta S^2, C = -2S + 6 beta S^2, S = f^2

Verfahren (Plan Abschnitt 3):
  - Taylor-Reihen-Integrator der Ordnung N mit fester Schrittweite h (Kh = kh fuer den schnellsten Kanal), Koeffizienten
    als Festkomma-Ganzzahlen mit 2^-P (P = bits + 20). Normierte Koeffizienten z_j = Z_j h^j.
  - Hintergrund "karte": eps-Hintergrund, Start auf der instabilen Mannigfaltigkeit von f_c bei x = -L (kein Schwanz
    innen), Taylor-Integration ueber das ganze Gebiet; die Koeffizienten von S und S^2 werden je Gitterpunkt gespeichert.
    Hintergrund "f0": S = S_c/(1 + e^x) (eps nur in den Schwankungen, Diagnose D aus V-1-WEITER).
  - Stille-Funktion E(rho) = det[Q_aus | Q_innen] (reelle Basen, QR mit positiver Diagonale), Nullstelle rho_z
    (Illinois-Verfahren).
  - Streuung bei rho_z: Einfall im alten Innenkanal e1, Amplituden aus dem Endblock der akkumulierten Dreiecksmatrix
    (wie v1w.py), Fluss k + 2 eps k^3 je laufender Mode.

Aufruf: python v1p.py <eps> <bits> <N> <kh> <L> <modell karte|f0> <rho_start> <aus.json> [halbbreite] [rho_tol] [offset]
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import json  # noqa: E402
import math  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402
from operator import mul  # noqa: E402

import mpmath  # noqa: E402
from mpmath import mp, mpf, mpc  # noqa: E402

T0 = time.time()


def log(msg):
    print(f"[{time.time() - T0:7.1f} s] {msg}", flush=True)


# ------------------------------------------------------------------------------------------------------------------
# Argumente und Konstanten
# ------------------------------------------------------------------------------------------------------------------
EPS_S, BITS, NORD, KH, LGEB, MODELL, RHO_S, PFAD = sys.argv[1:9]
HB = mpf(sys.argv[9]) if len(sys.argv) > 9 else None
RHO_TOL_S = sys.argv[10] if len(sys.argv) > 10 else None
OFFSET_S = sys.argv[11] if len(sys.argv) > 11 else "0"
BITS, NORD = int(BITS), int(NORD)
P = BITS + 20
mp.prec = P
EPS = mpf(EPS_S)
KH = mpf(KH)
LGEB = mpf(LGEB)
BETA = mpf(1)
OM = mpmath.sqrt(1 - 1 / (4 * BETA))
SC = 1 / (2 * BETA)
FC = mpmath.sqrt(SC)
ONE = 1 << P
assert MODELL in ("karte", "f0")
HB = HB if HB is not None else mpf("5e-8")
RHO_TOL = mpf(RHO_TOL_S) if RHO_TOL_S else (mpf("1e-22") if EPS < 0 else mpf(2) ** (-(BITS - 10)))
OUT = {"version": 1, "eps": EPS_S, "bits": BITS, "P": P, "N": NORD, "kh": float(KH), "L": float(LGEB),
       "modell": MODELL, "rho_start": RHO_S, "halbbreite": float(HB), "rho_tol": mpmath.nstr(RHO_TOL, 5)}


def schreibe():
    OUT["sek"] = time.time() - T0
    with open(PFAD + ".tmp", "w") as fh:
        json.dump(OUT, fh, indent=1)
    os.replace(PFAD + ".tmp", PFAD)


def fx(x):
    """mpf -> Festkomma-Ganzzahl (Skala 2^P)."""
    return int(mpmath.nint(mpmath.ldexp(x, P)))


def fl(n):
    return mpmath.ldexp(mpf(n), -P)


def s(x, d=25):
    """Zahl als Zeichenkette (fuer JSON, volle Stellen bis d)."""
    return mpmath.nstr(x, d)


# ------------------------------------------------------------------------------------------------------------------
# Kanaele (asymptotische Moden), wie v1w.py
# ------------------------------------------------------------------------------------------------------------------
def wurzeln(mu):
    """(typ, wert, zweig): eps lam^4 - lam^2 + mu = 0; typ 'r' (lam = +-wert) oder 'i' (lam = +-i wert)."""
    D = 1 - 4 * EPS * mu
    if D <= 0:
        raise ValueError(f"komplexe Wurzeln: mu={mu}")
    sD = mpmath.sqrt(D)
    s_klein = 2 * mu / (1 + sD)
    s_gross = (1 + sD) / (2 * EPS)
    out = []
    for sq, zw in ((s_klein, "alt"), (s_gross, "neu")):
        out.append(("r", mpmath.sqrt(sq), zw) if sq > 0 else ("i", mpmath.sqrt(-sq), zw))
    return out


def eigen(ende, rho):
    am, ap = (rho - OM) ** 2, (rho + OM) ** 2
    if ende == "aus":
        mus = [(1 - am, [mpf(1), mpf(0)], "A"), (1 - ap, [mpf(0), mpf(1)], "B")]
    else:
        Win, Cin = 1 - 4 * SC + 9 * BETA * SC ** 2, -2 * SC + 6 * BETA * SC ** 2
        a, b, c = Win - am, Cin, Win - ap
        m_, d_ = (a + c) / 2, mpmath.sqrt(((a - c) / 2) ** 2 + b ** 2)
        lam1, lam2 = m_ - d_, m_ + d_
        vecs = []
        for lam in (lam1, lam2):
            # (a - lam) x + b y = 0 -> (b, lam - a) bzw. (lam - c, b)
            v = [b, lam - a] if abs(b) > abs(lam - c) * mpf("1e-30") else [lam - c, b]
            nv = mpmath.sqrt(v[0] ** 2 + v[1] ** 2)
            v = [v[0] / nv, v[1] / nv]
            if v[0] < 0:
                v = [-v[0], -v[1]]
            vecs.append(v)
        if not (lam1 < 0 < lam2):
            raise ValueError("Innenmatrix nicht ein laufend / ein abklingend")
        mus = [(lam1, vecs[0], "e1"), (lam2, vecs[1], "e2")]
    moden = []
    for mu, u, kanal in mus:
        for typ, w, zweig in wurzeln(mu):
            moden.append({"kanal": kanal, "zweig": zweig, "typ": typ, "wert": w, "u": u, "mu": mu})
    return moden


def fluss_mode(wert, vorz):
    """Fluss der Mode u e^{lam x}, lam = vorz * i * wert, |u| = 1: vorz (k + 2 eps k^3)."""
    return vorz * (wert + 2 * EPS * wert ** 3)


# ------------------------------------------------------------------------------------------------------------------
# Gitter und Festkomma-Konstanten
# ------------------------------------------------------------------------------------------------------------------
def kmax(rho):
    return max(m["wert"] for e in ("aus", "innen") for m in eigen(e, rho) if m["zweig"] == "neu")


RHO0 = mpf(RHO_S)
KMAX = kmax(RHO0)
NH = int(mpmath.ceil(LGEB * KMAX / KH))          # Schritte je Seite
H = LGEB / NH
XS = [-LGEB + n * H for n in range(2 * NH + 1)]   # XS[NH] = 0
OUT.update({"h": float(H), "n_halb": NH, "K_max": float(KMAX), "Kh": float(KMAX * H)})
log(f"eps {EPS_S} bits {BITS} N {NORD} kh {KH} L {LGEB} modell {MODELL}: h = {float(H):.6f}, n_halb = {NH}, "
    f"Kmax = {float(KMAX):.4f}")

AJ = [fx(H ** 2 / (EPS * (j + 4) * (j + 3))) for j in range(NORD - 3)]
BJ = [fx(H ** 4 / (EPS * (j + 4) * (j + 3) * (j + 2) * (j + 1))) for j in range(NORD - 3)]
COF_V = [[math.comb(j, k) for j in range(k, NORD + 1)] for k in range(4)]
COF_R = [[math.comb(j, k) * (-1) ** (j - k) for j in range(k, NORD + 1)] for k in range(4)]


# ------------------------------------------------------------------------------------------------------------------
# Hintergrund: normierte Taylor-Koeffizienten von S und S^2 an jedem Gitterpunkt
# ------------------------------------------------------------------------------------------------------------------
def koeff_aus_S(sv, ssv):
    W = [-4 * a + 9 * b for a, b in zip(sv, ssv)]     # beta = 1
    W[0] += ONE
    C = [-2 * a + 6 * b for a, b in zip(sv, ssv)]
    return W, C


def hintergrund_karte():
    g1 = fx(1 - OM ** 2)
    lam1 = mpmath.sqrt((1 - mpmath.sqrt(1 - 4 * EPS)) / (2 * EPS))   # instabile Richtung bei f_c (lam^2 ~ 1)
    a0 = FC / 2 * mpmath.exp(lam1 * XS[0])
    b = [fx(FC - a0)] + [fx(-a0 * (H * lam1) ** k / mpmath.factorial(k)) for k in (1, 2, 3)]
    koeffs = []
    for n in range(2 * NH + 1):
        F = list(b)
        F2, F4 = [], []
        for j in range(NORD + 1):
            Fj = F[: j + 1]
            F2.append(sum(map(mul, Fj, F[j::-1])) >> P)
            F4.append(sum(map(mul, F2, F2[::-1])) >> P)
            if j <= NORD - 4:
                F3j = sum(map(mul, Fj, F2[::-1])) >> P
                F5j = sum(map(mul, Fj, F4[::-1])) >> P
                gj = ((g1 * F[j]) >> P) - 2 * F3j + 3 * F5j
                F.append((AJ[j] * F[j + 2] - BJ[j] * gj) >> P)
        koeffs.append(koeff_aus_S(F2, F4))
        if n < 2 * NH:
            b = [sum(map(mul, COF_V[k], F[k:])) for k in range(4)]
    # Schwanzdiagnose am rechten Ende: Zerlegung von (f, f', f'', f''') in die vier Moden bei f = 0
    fb = [fl(b[k]) * mpmath.factorial(k) / H ** k for k in range(4)]
    mu0 = 1 - OM ** 2
    lam = []
    for typ, w, zw in wurzeln(mu0):
        lam += [w, -w] if typ == "r" else [mpc(0, w), mpc(0, -w)]
    M = mpmath.matrix([[lam[i] ** k for i in range(4)] for k in range(4)])
    c = mpmath.lu_solve(M, mpmath.matrix(fb))
    diag = {"x_rechts": float(XS[-1]), "f_rechts": s(fb[0], 8), "lam_moden": [s(v, 8) for v in lam],
            "koeff_moden": [s(abs(c[i]), 6) for i in range(4)], "lam1_innen": s(lam1, 12), "a0": s(a0, 8)}
    return koeffs, diag


def hintergrund_f0():
    hf = fx(H)
    koeffs = []
    for n in range(2 * NH + 1):
        sv = [fx(SC / (1 + mpmath.exp(XS[n])))]
        ss = []
        for j in range(NORD + 1):
            ss.append(sum(map(mul, sv, sv[::-1])) >> P)
            if j < NORD:
                sv.append(((hf * (2 * ss[j] - sv[j])) >> P) // (j + 1))
        koeffs.append(koeff_aus_S(sv, ss))
    return koeffs, {"art": "f0 analytisch"}


# ------------------------------------------------------------------------------------------------------------------
# Taylor-Schritt fuer Schwankungsspalten (Festkomma)
# ------------------------------------------------------------------------------------------------------------------
def schritt(vecs, W, C, amf, apf, cof):
    P2 = 2 * P
    zs = [(list(v[0:4]), list(v[4:8])) for v in vecs]
    for j in range(NORD - 3):
        Ws, Cs = W[: j + 1], C[: j + 1]
        aj, bj = AJ[j], BJ[j]
        for zA, zB in zs:
            rA, rB = zA[j::-1], zB[j::-1]
            accA = sum(map(mul, Ws, rA)) + sum(map(mul, Cs, rB)) - amf * zA[j]
            accB = sum(map(mul, Cs, rA)) + sum(map(mul, Ws, rB)) - apf * zB[j]
            zA.append((((aj * zA[j + 2]) << P) - bj * accA) >> P2)
            zB.append((((aj * zB[j + 2]) << P) - bj * accB) >> P2)
    out = []
    tailmax = 0
    for zA, zB in zs:
        out.append([sum(map(mul, cof[k], zA[k:])) for k in range(4)] + [sum(map(mul, cof[k], zB[k:])) for k in range(4)])
        tailmax = max(tailmax, abs(zA[-1]), abs(zB[-1]), abs(zA[-2]), abs(zB[-2]))
    return out, tailmax


# ------------------------------------------------------------------------------------------------------------------
# QR (modifiziertes Gram-Schmidt, positive Diagonale) in mpmath
# ------------------------------------------------------------------------------------------------------------------
def mgs(cols):
    m = len(cols)
    Q, R = [], [[mpf(0)] * m for _ in range(m)]
    for k in range(m):
        v = list(cols[k])
        for _ in range(2):                     # zweimal orthogonalisieren
            for i in range(k):
                qi = Q[i]
                r = mpmath.fsum([mpmath.conj(qi[t]) * v[t] for t in range(8)])
                R[i][k] += r
                v = [v[t] - r * qi[t] for t in range(8)]
        nv = mpmath.sqrt(mpmath.fsum([abs(v[t]) ** 2 for t in range(8)]))
        R[k][k] = nv
        Q.append([v[t] / nv for t in range(8)])
    return Q, R


def zu_ints(Q, kompl):
    vecs = []
    for q, kp in zip(Q, kompl):
        vecs.append([fx(mpmath.re(q[t])) for t in range(8)])
        if kp:
            vecs.append([fx(mpmath.im(q[t])) for t in range(8)])
    return vecs


def von_ints(vecs, kompl):
    Q, i = [], 0
    for kp in kompl:
        if kp:
            Q.append([mpc(fl(vecs[i][t]), fl(vecs[i + 1][t])) for t in range(8)])
            i += 2
        else:
            Q.append([fl(vecs[i][t]) for t in range(8)])
            i += 1
    return Q


def matmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    return [[mpmath.fsum([A[i][t] * B[t][j] for t in range(k)]) for j in range(m)] for i in range(n)]


def integriere(cols, kompl, ende, rho, n_trail, qr_alle):
    """cols: Startspalten (normierte Zustaende) am Rand; ende 'innen' (vorwaerts von x = -L bis 0) oder 'aus'
    (rueckwaerts von x = +L bis 0). Gibt Q (mpmath-Spalten) und den akkumulierten Endblock der Dreiecksmatrix."""
    am, ap = (rho - OM) ** 2, (rho + OM) ** 2
    # normierte Koeffizienten: (v z)_j = sum_i V_i h^i z_{j-i}; die Konstanten am, ap gehoeren zu V_0 (ohne h-Faktor)
    amf, apf = fx(am), fx(ap)
    Q, R = mgs(cols)
    m = len(cols)
    trail = [row[m - n_trail:] for row in R[m - n_trail:]] if n_trail else None
    vecs = zu_ints(Q, kompl)
    if ende == "innen":
        punkte, cof = list(range(0, NH)), COF_V
    else:
        punkte, cof = list(range(2 * NH, NH, -1)), COF_R
    tmax = 0
    for i, n in enumerate(punkte):
        W, C = KOEFFS[n]
        vecs, tm = schritt(vecs, W, C, amf, apf, cof)
        tmax = max(tmax, tm)
        if (i + 1) % qr_alle == 0 or i == len(punkte) - 1:
            Q, R = mgs(von_ints(vecs, kompl))
            if n_trail:
                Rt = [row[m - n_trail:] for row in R[m - n_trail:]]
                trail = matmul(Rt, trail)
            vecs = zu_ints(Q, kompl)
    return Q, trail, tmax


def modenvektor(u, lam):
    """normierter Zustand (z_0..z_3 fuer A, dann B) der Mode u e^{lam (x - x_rand)}."""
    out = []
    for comp in (0, 1):
        out += [u[comp] * (H * lam) ** k / mpmath.factorial(k) for k in range(4)]
    return out


def startspalten(ende, rho, zweck):
    moden = eigen(ende, rho)
    sgn = -1 if ende == "aus" else 1
    abkl = sorted([mo for mo in moden if mo["typ"] == "r"], key=lambda mo: -mo["wert"])
    cols, kompl, etik, fl_ = [], [], [], []
    for mo in abkl:
        cols.append(modenvektor(mo["u"], sgn * mo["wert"]))
        kompl.append(False)
        etik.append(f"{mo['kanal']}-{mo['zweig']}-abkl")
    lauf = [mo for mo in moden if mo["typ"] == "i"]
    if zweck == "E":
        if ende == "innen":
            for mo in lauf:
                v = modenvektor(mo["u"], mpc(0, mo["wert"]))
                cols += [[mpmath.re(t) for t in v], [mpmath.im(t) for t in v]]
                kompl += [False, False]
                etik += [f"{mo['kanal']}-{mo['zweig']}-re", f"{mo['kanal']}-{mo['zweig']}-im"]
        return cols, kompl, etik, 0, []
    einfall = None
    for mo in lauf:
        fp, fm = fluss_mode(mo["wert"], 1), fluss_mode(mo["wert"], -1)
        vp, vm = modenvektor(mo["u"], mpc(0, mo["wert"])), modenvektor(mo["u"], mpc(0, -mo["wert"]))
        if ende == "aus":
            v, f_ = (vp, fp) if fp > 0 else (vm, fm)
            etik.append(f"{mo['kanal']}-{mo['zweig']}-aus")
        else:
            v, f_ = (vm, fm) if fm < 0 else (vp, fp)
            etik.append(f"{mo['kanal']}-{mo['zweig']}-refl")
            if mo["kanal"] == "e1" and mo["zweig"] == "alt":
                einfall = (vp, fp) if fp > 0 else (vm, fm)
        cols.append(v)
        kompl.append(True)
        fl_.append(f_)
    n_lauf = len(lauf)
    if ende == "innen":
        cols.append(einfall[0])
        kompl.append(True)
        fl_.append(einfall[1])
        etik.append("e1-alt-einfall")
        n_lauf += 1
    return cols, kompl, etik, n_lauf, fl_


def E_von(rho):
    t = time.time()
    co, ko, _, _, _ = startspalten("aus", rho, "E")
    ci, ki, _, _, _ = startspalten("innen", rho, "E")
    qa = 1 if EPS > 0 else 10
    Qo, _, t1 = integriere(co, ko, "aus", rho, 0, qa)
    Qi, _, t2 = integriere(ci, ki, "innen", rho, 0, qa)
    M = mpmath.matrix([[q[t_] for q in Qo + Qi] for t_ in range(8)])
    E = mpmath.det(M)
    log(f"E({s(rho, 22)}) = {s(E, 8)} ({time.time() - t:.1f} s)")
    return E, max(t1, t2)


def streuung(rho):
    t = time.time()
    co, ko, eo, ro, flo = startspalten("aus", rho, "S")
    ci, ki, ei, ri, fli = startspalten("innen", rho, "S")
    qa = 1 if EPS > 0 else 10
    Qo, To, t1 = integriere(co, ko, "aus", rho, ro, qa)
    Qi, Ti, t2 = integriere(ci, ki, "innen", rho, ri, qa)
    po, pi_ = len(co), len(ci)
    M = mpmath.matrix(8, po + pi_ - 1)
    rhs = mpmath.matrix(8, 1)
    for t_ in range(8):
        for j in range(po):
            M[t_, j] = Qo[j][t_]
        for j in range(pi_ - 1):
            M[t_, po + j] = -Qi[j][t_]
        rhs[t_] = Qi[pi_ - 1][t_]
    c = mpmath.lu_solve(M, rhs)
    c_o = [c[j] for j in range(po)]
    c_i = [c[po + j] for j in range(pi_ - 1)] + [mpf(1)]
    a_o = mpmath.lu_solve(mpmath.matrix(To), mpmath.matrix(c_o[po - ro:]))
    a_i = mpmath.lu_solve(mpmath.matrix(Ti), mpmath.matrix(c_i[pi_ - ri:]))
    a_inc, f_inc = a_i[ri - 1], fli[-1]
    erg = {"rho": s(rho, 30), "kanaele_aus": {}, "kanaele_innen": {}}
    T_aus, R_in, P_aus, P_in, T_alt = mpf(0), mpf(0), mpf(0), mpf(0), mpf(0)
    for k in range(ro):
        amp = a_o[k] / a_inc
        Tk = abs(amp) ** 2 * abs(flo[k]) / abs(f_inc)
        erg["kanaele_aus"][eo[po - ro + k]] = {"amp_abs": s(abs(amp), 15), "T": s(Tk, 15), "fluss": s(flo[k], 12)}
        T_aus += Tk
        if "-neu-" in eo[po - ro + k]:
            P_aus += Tk
        else:
            T_alt += Tk
    for k in range(ri - 1):
        amp = a_i[k] / a_inc
        Rk = abs(amp) ** 2 * abs(fli[k]) / abs(f_inc)
        erg["kanaele_innen"][ei[pi_ - ri + k]] = {"amp_abs": s(abs(amp), 15), "R": s(Rk, 15), "fluss": s(fli[k], 12)}
        R_in += Rk
        if "-neu-" in ei[pi_ - ri + k]:
            P_in += Rk
    erg.update({"T_aus": s(T_aus, 20), "R_innen": s(R_in, 20), "P_neu_aus": s(P_aus, 20), "P_neu_innen": s(P_in, 20),
                "T_alt_aus": s(T_alt, 20), "flussbilanz": s(T_aus + R_in - 1, 6),
                "ln_P_neu_aus": s(mpmath.log(P_aus), 20) if P_aus > 0 else None,
                "ln_T_aus": s(mpmath.log(T_aus), 20) if T_aus > 0 else None,
                "taylor_rest_max": s(fl(max(t1, t2)), 4), "sek": time.time() - t})
    log(f"Streuung rho = {s(rho, 20)}: P_neu_aus = {s(P_aus, 12)}, P_neu_innen = {s(P_in, 12)}, T_alt = {s(T_alt, 6)}, "
        f"T_aus = {s(T_aus, 6)}, Bilanz = {s(T_aus + R_in - 1, 4)} ({time.time() - t:.1f} s)")
    return erg


# ------------------------------------------------------------------------------------------------------------------
# Ablauf
# ------------------------------------------------------------------------------------------------------------------
t = time.time()
KOEFFS, HDIAG = hintergrund_karte() if MODELL == "karte" else hintergrund_f0()
OUT["hintergrund"] = HDIAG
OUT["hintergrund_sek"] = time.time() - t
log(f"Hintergrund {MODELL} fertig ({time.time() - t:.1f} s): {json.dumps(HDIAG)[:300]}")
schreibe()

# Kanalbild und Wellenzahlen bei rho_start
OUT["kanaele_start"] = {e: [{"kanal": m_["kanal"], "zweig": m_["zweig"], "typ": m_["typ"], "wert": s(m_["wert"], 20),
                             "mu": s(m_["mu"], 20)} for m_ in eigen(e, RHO0)] for e in ("aus", "innen")}

# Nullstelle von E: Klammer um rho_start, dann Illinois
verlauf = []
a, b = RHO0 - HB, RHO0 + HB
Ea, _ = E_von(a)
Eb, _ = E_von(b)
verlauf += [[s(a, 30), s(Ea, 10)], [s(b, 30), s(Eb, 10)]]
k = 0
while Ea * Eb > 0 and k < 3:
    HB *= 8
    a, b = RHO0 - HB, RHO0 + HB
    Ea, _ = E_von(a)
    Eb, _ = E_von(b)
    verlauf += [[s(a, 30), s(Ea, 10)], [s(b, 30), s(Eb, 10)]]
    k += 1
OUT["E_verlauf"] = verlauf
schreibe()
if Ea * Eb > 0:
    OUT["fehler"] = "kein Vorzeichenwechsel von E"
    schreibe()
    sys.exit(2)
seite = 0
for it in range(40):
    c = (a * Eb - b * Ea) / (Eb - Ea)
    Ec, _ = E_von(c)
    verlauf.append([s(c, 30), s(Ec, 10)])
    OUT["E_verlauf"] = verlauf
    schreibe()
    if Ec == 0:
        a = b = c
        break
    if Ec * Eb < 0:
        a, Ea = b, Eb
        b, Eb = c, Ec
        seite = 0
    else:
        b, Eb = c, Ec
        Ea = Ea / 2 if seite == 1 else Ea
        seite = 1
    if abs(b - a) < RHO_TOL:
        break
RHO_Z = b if abs(Eb) <= abs(Ea) else a
OUT["rho_z"] = s(RHO_Z, 40)
OUT["E_bei_rho_z"] = s(min(abs(Ea), abs(Eb)), 8)
OUT["klammer"] = s(abs(b - a), 6)
log(f"rho_z = {s(RHO_Z, 30)}, Klammer {s(abs(b - a), 4)}")
schreibe()

# Wellenzahlen der neuen Kanaele bei rho_z
OUT["K_rho_z"] = {f"{m_['kanal']}-{m_['zweig']}": s(m_["wert"], 25) for e in ("aus", "innen") for m_ in eigen(e, RHO_Z)}
OUT["streuung"] = {"0": streuung(RHO_Z)}
schreibe()
for off in OFFSET_S.split(","):
    if off and mpf(off) != 0:
        OUT["streuung"][off] = streuung(RHO_Z + mpf(off))
        schreibe()
log("fertig")
schreibe()
