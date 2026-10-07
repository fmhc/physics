"""PONZANO-1 (Runde 37, Code-Agent): exakte 6j-Symbole, Ponzano-Regge, Biedenharn-Elliott, 2-3-Zug.

Nur auf der .69 ueber kleintest.sh (Spur cpu):
  python ponzano.py <teil> <ausgabe.json> [argumente]
  teile: geometrie | zeit | konvention | po0 | po1 | po2 | po3 <K1|K2> <lambda>
Konventionen (PLAN.md, Abschnitt 2):
  {j1 j2 j3; j4 j5 j6}: j1 = BC, j2 = AC, j3 = AB, j4 = AD, j5 = BD, j6 = CD.
  Triaden (Flaechen): (j1 j2 j3) = ABC, (j1 j5 j6) = BCD, (j4 j2 j6) = ACD, (j4 j5 j3) = ABD.
  Spins intern verdoppelt (J = 2j, ganze Zahlen).
  Racah-Formel ohne Zusatzphase; exakt mit ganzen Zahlen, Wurzeln erst am Ende (mpmath, DPS Stellen).
  Ponzano-Regge: {6j} ~ cos(sum_e l_e theta_e + pi/4)/sqrt(12 pi V), l_e = j_e + 1/2, theta_e = pi - Innenwinkel.
"""
import functools
import itertools
import json
import math
import random
import sys
import time
from fractions import Fraction

import mpmath as mp

DPS = 50
mp.mp.dps = DPS
PI = mp.pi
HALB = mp.mpf(1) / 2

# ------------------------------------------------------------------ exakte 6j-Symbole
TRIADEN = ((0, 1, 2), (0, 4, 5), (3, 1, 5), (3, 4, 2))


@functools.lru_cache(maxsize=None)
def fak(n):
    return math.factorial(n)


def triade_ok(a, b, c):
    """Doppelte Spins: nicht negativ, ganzzahlige Summe, Dreiecksungleichung."""
    if a < 0 or b < 0 or c < 0 or (a + b + c) % 2:
        return False
    return a <= b + c and b <= a + c and c <= a + b


def zulaessig(J):
    return all(triade_ok(J[i], J[k], J[m]) for i, k, m in TRIADEN)


def delta2_zn(a, b, c):
    """Delta(abc)^2 als (Zaehler, Nenner), doppelte Spins."""
    return (fak((a + b - c) // 2) * fak((a - b + c) // 2) * fak((-a + b + c) // 2), fak((a + b + c) // 2 + 1))


def racah_ganz(J):
    """Racah-Summe S = I/M mit ganzen I, M (M = prod (zmax-a_i)! prod (b_j-zmin)!, jeder Summand mal M ganz)."""
    j1, j2, j3, j4, j5, j6 = J
    a = ((j1 + j2 + j3) // 2, (j1 + j5 + j6) // 2, (j4 + j2 + j6) // 2, (j4 + j5 + j3) // 2)
    b = ((j1 + j2 + j4 + j5) // 2, (j2 + j3 + j5 + j6) // 2, (j3 + j1 + j6 + j4) // 2)
    zmin, zmax = max(a), min(b)
    if zmin > zmax:
        return 0, 1
    n = zmax - zmin
    M = 1
    for ai in a:
        M *= fak(zmax - ai)
    for bj in b:
        M *= fak(bj - zmin)
    U = fak(zmin + 1)
    for ai in a:
        U *= math.perm(zmax - ai, n)  # (zmax-a_i)!/(zmin-a_i)!
    vz = -1 if zmin % 2 else 1
    I = vz * U
    for z in range(zmin, zmax):
        # U(z+1) = U(z) (z+2) prod_j (b_j - z) / prod_i (z+1-a_i), exakt teilbar
        U = U * ((z + 2) * (b[0] - z) * (b[1] - z) * (b[2] - z)) // (
            (z + 1 - a[0]) * (z + 1 - a[1]) * (z + 1 - a[2]) * (z + 1 - a[3]))
        vz = -vz
        I += vz * U
    return I, M


def sechsj_exakt(J):
    """(Vorzeichen, Quadrat als Fraction); (0, 0) wenn unzulaessig oder null."""
    if not zulaessig(J):
        return 0, Fraction(0)
    I, M = racah_ganz(J)
    if I == 0:
        return 0, Fraction(0)
    zn, nn = I * I, M * M
    for i, k, m in TRIADEN:
        z, n = delta2_zn(J[i], J[k], J[m])
        zn *= z
        nn *= n
    return (1 if I > 0 else -1), Fraction(zn, nn)


def sechsj_wert(J):
    """mpmath-Wert aus der exakten ganzzahligen Racah-Summe (keine Ausloeschung)."""
    if not zulaessig(J):
        return mp.mpf(0)
    I, M = racah_ganz(J)
    if I == 0:
        return mp.mpf(0)
    zn, nn = 1, 1
    for i, k, m in TRIADEN:
        z, n = delta2_zn(J[i], J[k], J[m])
        zn *= z
        nn *= n
    return mp.mpf(I) / mp.mpf(M) * mp.sqrt(mp.mpf(zn) / mp.mpf(nn))


def teile(J):
    """6j = r * prod_t sqrt(Delta^2(t)), r rational; t sortierte Triaden."""
    I, M = racah_ganz(J)
    return Fraction(I, M), [tuple(sorted((J[i], J[k], J[m]))) for i, k, m in TRIADEN]


def produkt_exakt(koeff, faktoren):
    """koeff * prod 6j = c * sqrt(prod_{t in schluessel} Delta^2(t)), c rational."""
    c = Fraction(koeff)
    zaehl = {}
    for J in faktoren:
        if not zulaessig(J):
            return (), Fraction(0)
        r, tri = teile(J)
        c *= r
        for t in tri:
            zaehl[t] = zaehl.get(t, 0) + 1
    rest = []
    for t, n in zaehl.items():
        z, nn = delta2_zn(*t)
        c *= Fraction(z, nn) ** (n // 2)
        if n % 2:
            rest.append(t)
    return tuple(sorted(rest)), c


def summe_exakt(terme):
    erg = {}
    for koeff, faktoren in terme:
        k, c = produkt_exakt(koeff, faktoren)
        if c != 0:
            erg[k] = erg.get(k, Fraction(0)) + c
    return {k: v for k, v in erg.items() if v != 0}


def symmetrien():
    """Die 24 Tetraedersymmetrien als Indexabbildungen (Spaltenpermutation, oben/unten in zwei Spalten)."""
    out = []
    for perm in itertools.permutations(range(3)):
        for flip in ((0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1)):
            idx = [0] * 6
            for neu, alt in enumerate(perm):
                o, u = alt, alt + 3
                if flip[neu]:
                    o, u = u, o
                idx[neu], idx[neu + 3] = o, u
            out.append(tuple(idx))
    return out


# ------------------------------------------------------------------ Geometrie (mpmath)
def v_sub(p, q):
    return tuple(x - y for x, y in zip(p, q))


def v_dot(p, q):
    return sum(x * y for x, y in zip(p, q))


def v_norm(p):
    return mp.sqrt(v_dot(p, p))


def v_mul(p, s):
    return tuple(x * s for x in p)


def dieder(P, Q, R, S):
    """Innerer Diederwinkel an der Kante PQ zwischen den Flaechen PQR und PQS."""
    e = v_sub(Q, P)
    e = v_mul(e, 1 / v_norm(e))
    u = v_sub(R, P)
    u = v_sub(u, v_mul(e, v_dot(u, e)))
    w = v_sub(S, P)
    w = v_sub(w, v_mul(e, v_dot(w, e)))
    c = v_dot(u, w) / (v_norm(u) * v_norm(w))
    return mp.acos(max(mp.mpf(-1), min(mp.mpf(1), c)))


def laengen(J):
    return [mp.mpf(x) / 2 + HALB for x in J]


def cm_v2(l):
    """V^2 aus der Cayley-Menger-Determinante; l = (BC, AC, AB, AD, BD, CD)."""
    BC, AC, AB, AD, BD, CD = [x ** 2 for x in l]
    M = mp.matrix([[0, 1, 1, 1, 1], [1, 0, AB, AC, AD], [1, AB, 0, BC, BD], [1, AC, BC, 0, CD],
                   [1, AD, BD, CD, 0]])
    return mp.det(M) / 288


def ecken(l):
    """Einbettung A, B, C (z = 0), D (z >= 0); zd2 < 0 heisst nicht geometrisch."""
    BC, AC, AB, AD, BD, CD = l
    xc = (AB ** 2 + AC ** 2 - BC ** 2) / (2 * AB)
    yc = mp.sqrt(AC ** 2 - xc ** 2)
    xd = (AB ** 2 + AD ** 2 - BD ** 2) / (2 * AB)
    yd = (AC ** 2 + AD ** 2 - CD ** 2 - 2 * xc * xd) / (2 * yc)
    zd2 = AD ** 2 - xd ** 2 - yd ** 2
    null = mp.mpf(0)
    return (null, null, null), (AB, null, null), (xc, yc, null), (xd, yd, zd2)


KANTEN = (("B", "C", "A", "D"), ("A", "C", "B", "D"), ("A", "B", "C", "D"), ("A", "D", "B", "C"),
          ("B", "D", "A", "C"), ("C", "D", "A", "B"))


def tetraeder(l):
    """(V, Innenwinkel phi_e in der Reihenfolge von l); nur fuer geometrische l."""
    A, B, C, (xd, yd, zd2) = ecken(l)
    if zd2 <= 0:
        return None
    D = (xd, yd, mp.sqrt(zd2))
    V = B[0] * C[1] * D[2] / 6
    P = {"A": A, "B": B, "C": C, "D": D}
    phi = [dieder(P[p], P[q], P[r], P[s]) for p, q, r, s in KANTEN]
    return V, phi


def regge_phase(l):
    """(sum_e l_e theta_e mit theta = pi - phi, V, theta-Liste)."""
    t = tetraeder(l)
    if t is None:
        return None
    V, phi = t
    th = [PI - p for p in phi]
    return sum(le * x for le, x in zip(l, th)), V, th


def ponzano_regge(J, winkel="aussen", viertel=1):
    """PR-Wert, Amplitude 1/sqrt(12 pi V), Phase; None wenn nicht geometrisch."""
    l = laengen(J)
    t = tetraeder(l)
    if t is None:
        return None
    V, phi = t
    th = [PI - p for p in phi] if winkel == "aussen" else phi
    phase = sum(le * x for le, x in zip(l, th)) + viertel * PI / 4
    amp = 1 / mp.sqrt(12 * PI * V)
    return amp * mp.cos(phase), amp, phase, V


def flaechen_rand(l):
    """Kleinster relativer Abstand von der Dreiecksgleichheit ueber die vier Flaechen."""
    BC, AC, AB, AD, BD, CD = l
    werte = []
    for x, y, z in ((BC, AC, AB), (BC, BD, CD), (AD, AC, CD), (AD, BD, AB)):
        s = x + y + z
        werte.append(min(x + y - z, x - y + z, -x + y + z) / s)
    return min(werte)


# ------------------------------------------------------------------ Formen (PLAN.md, Abschnitt 3)
# Reihenfolge b = (BC, AC, AB, AD, BD, CD) = (j1, ..., j6)
FORMEN = {
    "A": (6, 7, 8, 7, 9, 5),
    "B": (4, 9, 7, 10, 8, 6),
    "N": (10, 6, 7, 9, 6, 5),
    "N_rand": (6, 7, 8, 7, 9, 13),
}
# 2-3-Zug: (p, q, r, e, a, d, f, b, c) = (BC, AC, AB, AD, BD, CD, AE, BE, CE)
KONFIG = {
    "K1": (5, 5, 6, 4, 4, 4, 5, 4, 4),
    "K2": (5, 6, 7, 5, 4, 4, 4, 6, 5),
}
LAMBDA_PO1 = (5, 10, 20, 50, 100, 200)


def J_form(b, lam):
    return tuple(2 * lam * x for x in b)


# ------------------------------------------------------------------ 2-3-Zug
def be_tripel(K, X):
    """Die drei 6j des 2-3-Zugs fuer doppelte Spins K = (p..c) und doppeltes X."""
    p, q, r, e, a, d, f, b, c = K
    return (a, b, X, c, d, p), (c, d, X, e, f, q), (e, f, X, b, a, r)


def be_rechts(K):
    p, q, r, e, a, d, f, b, c = K
    return (p, q, r, e, a, d), (p, q, r, f, b, c)


def be_x_bereich(K):
    p, q, r, e, a, d, f, b, c = K
    lo = max(abs(a - b), abs(c - d), abs(e - f))
    hi = min(a + b, c + d, e + f)
    return [X for X in range(lo, hi + 1) if all(triade_ok(*t) for t in ((a, b, X), (c, d, X), (e, f, X)))]


def be_phase(K, X):
    s2 = sum(K) + X
    assert s2 % 2 == 0
    return -1 if (s2 // 2) % 2 else 1


def bipyramide(Kb, lam):
    """Flache Einbettung: Basis ABC, D oben, E unten. Laengen l = lam b + 1/2."""
    p, q, r, e, a, d, f, b, c = [lam * mp.mpf(x) + HALB for x in Kb]
    AB, AC, BC = r, q, p
    xc = (AB ** 2 + AC ** 2 - BC ** 2) / (2 * AB)
    yc = mp.sqrt(AC ** 2 - xc ** 2)

    def spitze(l_a, l_b, l_c, oben):
        x = (AB ** 2 + l_a ** 2 - l_b ** 2) / (2 * AB)
        y = (AC ** 2 + l_a ** 2 - l_c ** 2 - 2 * xc * x) / (2 * yc)
        z2 = l_a ** 2 - x ** 2 - y ** 2
        z = mp.sqrt(z2) if z2 > 0 else mp.mpf("nan")
        return (x, y, z if oben else -z), z2

    D, zd2 = spitze(e, a, d, True)
    E, ze2 = spitze(f, b, c, False)
    Ef = (E[0], E[1], -E[2])
    DE = v_norm(v_sub(D, E))
    DEf = v_norm(v_sub(D, Ef))
    # Durchstosspunkt von DE durch z = 0, baryzentrisch in ABC
    t = D[2] / (D[2] - E[2])
    P = tuple(D[i] + t * (E[i] - D[i]) for i in range(3))
    Bp = (AB, 0)
    Cp = (xc, yc)
    det = Bp[0] * Cp[1] - Bp[1] * Cp[0]
    u = (P[0] * Cp[1] - P[1] * Cp[0]) / det
    w = (Bp[0] * P[1] - Bp[1] * P[0]) / det
    bary = (1 - u - w, u, w)
    return {"x_stern": DE - HALB, "x_fold": DEf - HALB, "zd2": zd2, "ze2": ze2, "bary": bary, "DE": DE}


def defizit(Kb, lam, lx):
    """2 pi - Summe der drei Innenwinkel an der inneren Kante (Laenge lx), Laengen l = lam b + 1/2."""
    p, q, r, e, a, d, f, b, c = [lam * mp.mpf(x) + HALB for x in Kb]
    summe = 0
    for (j1, j2, _, j4, j5, j6) in ((a, b, None, c, d, p), (c, d, None, e, f, q), (e, f, None, b, a, r)):
        t = tetraeder((j1, j2, lx, j4, j5, j6))
        if t is None:
            return None
        summe += t[1][2]  # Innenwinkel an Position j3 = innere Kante
    return 2 * PI - summe


# ------------------------------------------------------------------ Teile
def f(x):
    return float(x)


def teil_geometrie():
    out = {"formen": {}, "konfig": {}}
    for name, b in FORMEN.items():
        lb = [mp.mpf(x) for x in b]
        mitte = sum(lb) / 6
        vreg2 = (mitte ** 3 / (6 * mp.sqrt(2))) ** 2
        row = {"b": b, "V2_b": f(cm_v2(lb)), "V2_b_rel_regulaer": f(cm_v2(lb) / vreg2),
               "flaechen_rand_b": f(flaechen_rand(lb))}
        for lam in (1, 5, 20, 200):
            l = laengen(J_form(b, lam))
            v2 = cm_v2(l)
            A, B, C, (xd, yd, zd2) = ecken(l)
            v2e = (B[0] * C[1]) ** 2 * zd2 / 36
            row["V2_lam%d" % lam] = f(v2)
            row["V2_einbettung_rel_abw_lam%d" % lam] = f(abs(v2e - v2) / abs(v2))
        # Vorzeichen von V^2 fuer alle lambda 1..200
        row["V2_vorzeichen_konstant_1_200"] = len({mp.sign(cm_v2(laengen(J_form(b, lam)))) for lam in range(1, 201)}) == 1
        out["formen"][name] = row
    for name, Kb in KONFIG.items():
        row = {"b": Kb}
        for lam in (1, 50, 100, 200):
            g = bipyramide(Kb, lam)
            dz = defizit(Kb, lam, g["DE"])
            row["lam%d" % lam] = {"x_stern": f(g["x_stern"]), "x_fold": f(g["x_fold"]), "zd2": f(g["zd2"]),
                                  "ze2": f(g["ze2"]), "bary": [f(x) for x in g["bary"]],
                                  "defizit_bei_x_stern": f(dz) if dz is not None else None}
        # Huellkurven-Vorhersage (PR-Amplituden, ohne 6j): Schwerpunkt von (2x+1)/sqrt(V1 V2 V3)
        for lam in (50, 100, 200):
            K = tuple(2 * lam * x for x in Kb)
            xs, ws = [], []
            for X in be_x_bereich(K):
                vs = [cm_v2(laengen(J)) for J in be_tripel(K, X)]
                if all(v > 0 for v in vs):
                    xs.append(mp.mpf(X) / 2)
                    # Amplitude je 6j ~ 1/sqrt(V_i) = (V_i^2)^(-1/4)
                    ws.append((X + 1) / (vs[0] * vs[1] * vs[2]) ** (mp.mpf(1) / 4))
            sw = sum(ws)
            row["huelle_lam%d" % lam] = {
                "x_min_geometrisch": f(xs[0]), "x_max_geometrisch": f(xs[-1]),
                "x_schwerpunkt_huelle": f(sum(x * w for x, w in zip(xs, ws)) / sw),
                "x_bereich_dreiecke": [be_x_bereich(K)[0] / 2, be_x_bereich(K)[-1] / 2]}
        out["konfig"][name] = row
    return out


def teil_zeit():
    out = {}
    for name in ("A", "B", "N"):
        J = J_form(FORMEN[name], 200)
        t0 = time.time()
        sechsj_wert(J)
        out["6j_lam200_%s_s" % name] = time.time() - t0
    K = tuple(400 * x for x in KONFIG["K1"])
    xs = be_x_bereich(K)
    X = xs[len(xs) // 2]
    t0 = time.time()
    for J in be_tripel(K, X):
        sechsj_wert(J)
    out["po3_K1_lam200_eine_zeile_s"] = time.time() - t0
    out["po3_K1_lam200_zeilen"] = len(xs)
    return out


def teil_konvention():
    """Konventionsprobe am gleichseitigen Tetraeder (nicht Teil von PO1)."""
    out = {}
    for j in (10, 20, 40, 80):
        J = (2 * j,) * 6
        w = sechsj_wert(J)
        row = {"6j": f(w)}
        for winkel in ("aussen", "innen"):
            for viertel in (1, -1):
                pr, amp, _, _ = ponzano_regge(J, winkel, viertel)
                row["e_%s_%+d" % (winkel, viertel)] = f(abs(w - pr) / amp)
        out["j%d" % j] = row
    return out


def zufall_J(rng, jmax2, n):
    out = []
    while len(out) < n:
        J = tuple(rng.randint(0, jmax2) for _ in range(6))
        if zulaessig(J):
            out.append(J)
    return out


def teil_po0():
    from sympy import Rational, sign
    from sympy.physics.wigner import wigner_6j

    rng = random.Random(37001)
    out = {}
    # (a) Orthogonalitaet, exakt
    ortho = {"saetze": 0, "paare": 0, "fehler": 0, "beispiele": []}
    while ortho["saetze"] < 10:
        a, b, c, d = (rng.randint(0, 16) for _ in range(4))
        fs = [F for F in range(0, 40) if triade_ok(a, d, F) and triade_ok(c, b, F)]
        xs = [X for X in range(0, 40) if triade_ok(a, b, X) and triade_ok(c, d, X)]
        if len(fs) < 2 or not xs:
            continue
        ortho["saetze"] += 1
        for F, F2 in itertools.combinations_with_replacement(fs, 2):
            terme = [((X + 1) * (F + 1), [(a, b, X, c, d, F), (a, b, X, c, d, F2)]) for X in xs]
            erg = summe_exakt(terme)
            soll = {(): Fraction(1)} if F == F2 else {}
            ortho["paare"] += 1
            if erg != soll:
                ortho["fehler"] += 1
        ortho["beispiele"].append([a, b, c, d])
    out["orthogonalitaet"] = ortho
    # (a2) Orthogonalitaet bei groesseren j mit mpmath (Form A, lambda = 10: a, b, c, d aus der Form)
    bA = J_form(FORMEN["A"], 10)
    a, b, c, d = bA[3], bA[4], bA[0], bA[1]  # beliebige zulaessige Vierer aus der Form
    fs = [F for F in range(0, 400, 2) if triade_ok(a, d, F) and triade_ok(c, b, F)]
    xs = [X for X in range(0, 400, 2) if triade_ok(a, b, X) and triade_ok(c, d, X)]
    groesst = mp.mpf(0)
    for F, F2 in ((fs[0], fs[0]), (fs[len(fs) // 2], fs[len(fs) // 2]), (fs[0], fs[1]), (fs[1], fs[-1])):
        s = sum((X + 1) * (F + 1) * sechsj_wert((a, b, X, c, d, F)) * sechsj_wert((a, b, X, c, d, F2)) for X in xs)
        groesst = max(groesst, abs(s - (1 if F == F2 else 0)))
    out["orthogonalitaet_mp_formA_lam10"] = {"spins_doppelt": [a, b, c, d], "max_abw": f(groesst),
                                             "x_anzahl": len(xs)}
    # (b) Biedenharn-Elliott an 20 Zufallssaetzen, exakt und mpmath
    be = {"saetze": [], "fehler_exakt": 0, "max_rel_abw_mp": 0.0}
    while len(be["saetze"]) < 20:
        K = tuple(rng.randint(0, 16) for _ in range(9))
        p, q, r, e, a, d, f_, b, c = K
        rechts_tri = ((p, q, r), (p, a, d), (e, q, d), (e, a, r), (p, b, c), (f_, q, c), (f_, b, r))
        if not all(triade_ok(*t) for t in rechts_tri):
            continue
        xs = be_x_bereich(K)
        if len(xs) < 2:
            continue
        links = summe_exakt([(be_phase(K, X) * (X + 1), list(be_tripel(K, X))) for X in xs])
        rechts = summe_exakt([(1, list(be_rechts(K)))])
        ok = links == rechts
        terme = [be_phase(K, X) * (X + 1) * sechsj_wert(J1) * sechsj_wert(J2) * sechsj_wert(J3)
                 for X in xs for (J1, J2, J3) in [be_tripel(K, X)]]
        lm = sum(terme)
        R1, R2 = be_rechts(K)
        rm = sechsj_wert(R1) * sechsj_wert(R2)
        # relativ zur Skala der Summanden (rechte Seite kann zufaellig null sein)
        rel = abs(lm - rm) / max(sum(abs(t) for t in terme), abs(rm))
        be["saetze"].append({"K_doppelt": K, "x_anzahl": len(xs), "exakt_gleich": ok, "rechts_null": not rechts,
                             "rel_abw_mp": f(rel)})
        be["fehler_exakt"] += 0 if ok else 1
        be["max_rel_abw_mp"] = max(be["max_rel_abw_mp"], f(rel))
    out["biedenharn_elliott"] = be
    # (c) 24 Symmetrien an 50 Zufalls-6j
    syms = symmetrien()
    assert len(set(syms)) == 24
    fehler = 0
    for J in zufall_J(rng, 16, 50):
        w = sechsj_exakt(J)
        for s in syms:
            if sechsj_exakt(tuple(J[i] for i in s)) != w:
                fehler += 1
    out["symmetrien"] = {"symbole": 50, "abbildungen": 24, "fehler": fehler}
    # (d) sympy: alle J mit 2j <= 4, 200 Zufall bis j = 12, Formen bei lambda = 5 und 10
    def vergleich(J):
        mein = sechsj_exakt(J)
        try:
            v = wigner_6j(*[Rational(x, 2) for x in J])
        except ValueError:
            return mein == (0, Fraction(0)), "sympy_unzulaessig"
        v2 = (v * v).expand()
        if not v2.is_Rational:
            return False, "kein_rational"
        fremd = (int(sign(v)), Fraction(int(v2.p), int(v2.q)))
        return mein == fremd, "ok"

    sy = {"alle_2j_bis_4": 0, "zufall_bis_j12": 0, "formen": 0, "fehler": 0, "sympy_unzulaessig": 0,
          "nicht_null_verglichen": 0}
    for J in itertools.product(range(5), repeat=6):
        ok, art = vergleich(J)
        sy["alle_2j_bis_4"] += 1
        sy["fehler"] += 0 if ok else 1
        sy["sympy_unzulaessig"] += art == "sympy_unzulaessig"
        sy["nicht_null_verglichen"] += zulaessig(J) and art == "ok"
    for J in zufall_J(rng, 24, 200):
        ok, _ = vergleich(J)
        sy["zufall_bis_j12"] += 1
        sy["fehler"] += 0 if ok else 1
    for name in ("A", "B", "N"):
        for lam in (5, 10):
            ok, _ = vergleich(J_form(FORMEN[name], lam))
            sy["formen"] += 1
            sy["fehler"] += 0 if ok else 1
    out["sympy"] = sy
    # (e) Sonderwert {a b c; 0 c b} = (-1)^(a+b+c)/sqrt((2b+1)(2c+1))
    sw_fehler = 0
    for (a, b, c) in [(A2, B2, C2) for A2 in range(0, 13) for B2 in range(0, 13) for C2 in range(0, 13)
                      if triade_ok(A2, B2, C2)]:
        vz, q = sechsj_exakt((a, b, c, 0, c, b))
        s = (a + b + c) // 2
        soll = ((-1) ** s, Fraction(1, (b + 1) * (c + 1)))
        sw_fehler += (vz, q) != soll
    out["sonderwert"] = {"fehler": sw_fehler}
    # (f) mpmath-Pfad gegen exakten Pfad
    abw = mp.mpf(0)
    for J in zufall_J(rng, 24, 100):
        vz, q = sechsj_exakt(J)
        w = sechsj_wert(J)
        if vz:
            abw = max(abw, abs(w - vz * mp.sqrt(mp.mpf(q.numerator) / q.denominator)) / abs(w))
    out["mp_gegen_exakt_max_rel"] = f(abw)
    return out


def teil_po1():
    out = {"formen": {}}
    for name in ("A", "B"):
        b = FORMEN[name]
        row = {"b": b, "lam": {}, "dicht": []}
        for lam in range(1, 201):
            J = J_form(b, lam)
            w = sechsj_wert(J)
            pr, amp, phase, V = ponzano_regge(J)
            e = abs(w - pr) / amp
            rec = {"lam": lam, "sechsj": f(w), "pr": f(pr), "amp": f(amp), "e": f(e), "V": f(V)}
            row["dicht"].append(rec)
            if lam in LAMBDA_PO1:
                row["lam"][str(lam)] = rec
        out["formen"][name] = row
    # Schlaefli-Kontrolle: d(sum l theta)/dl_k = theta_k (Form A, lambda = 50)
    l = laengen(J_form(FORMEN["A"], 50))
    S0, _, th = regge_phase(l)
    h = mp.mpf(10) ** -12
    abw = mp.mpf(0)
    for k in range(6):
        lp = list(l)
        lm = list(l)
        lp[k] += h
        lm[k] -= h
        d = (regge_phase(lp)[0] - regge_phase(lm)[0]) / (2 * h)
        abw = max(abw, abs(d - th[k]))
    out["schlaefli_max_abw"] = f(abw)
    # CM gegen Einbettung fuer V
    abwv = mp.mpf(0)
    for name in ("A", "B"):
        for lam in LAMBDA_PO1:
            l = laengen(J_form(FORMEN[name], lam))
            V = tetraeder(l)[0]
            abwv = max(abwv, abs(V ** 2 - cm_v2(l)) / V ** 2)
    out["volumen_cm_gegen_einbettung_max_rel"] = f(abwv)
    # Spinfolge: Form A, lambda = 50, j6 = CD laeuft ueber den ganzen Dreiecksbereich
    b = FORMEN["A"]
    J0 = list(J_form(b, 50))
    folge = []
    for X in range(0, 2 * 50 * 30 + 1, 2):
        J = tuple(J0[:5] + [X])
        if not zulaessig(J):
            continue
        w = sechsj_wert(J)
        v2 = cm_v2(laengen(J))
        rec = {"j6": X // 2, "sechsj": f(w), "V2": f(v2)}
        if v2 > 0:
            pr, amp, phase, V = ponzano_regge(J)
            rec.update({"pr": f(pr), "amp": f(amp)})
        else:
            rec["ln_abs"] = f(mp.log(abs(w))) if w != 0 else None
        folge.append(rec)
    out["spinfolge_A_lam50_j6"] = folge
    return out


def teil_po2():
    out = {}
    for name in ("N", "N_rand"):
        b = FORMEN[name]
        rows = []
        for lam in range(1, 201):
            J = J_form(b, lam)
            w = sechsj_wert(J)
            rows.append({"lam": lam, "ln_abs": f(mp.log(abs(w))) if w != 0 else None,
                         "vorzeichen": int(mp.sign(w)), "V2": f(cm_v2(laengen(J)))})
        out[name] = {"b": b, "werte": rows}
    return out


def teil_po3(name, lam):
    Kb = KONFIG[name]
    K = tuple(2 * lam * x for x in Kb)
    xs = be_x_bereich(K)
    rows = []
    s_mp = []
    summe = mp.mpf(0)
    t0 = time.time()
    for X in xs:
        tri = be_tripel(K, X)
        w = [sechsj_wert(J) for J in tri]
        s = be_phase(K, X) * (X + 1) * w[0] * w[1] * w[2]
        summe += s
        s_mp.append(s)
        rec = {"x": X // 2, "s": f(s)}
        prs = [ponzano_regge(J) for J in tri]
        if all(p is not None for p in prs):
            rec["s_pr"] = f(be_phase(K, X) * (X + 1) * prs[0][0] * prs[1][0] * prs[2][0])
            rec["huelle"] = f((X + 1) * prs[0][1] * prs[1][1] * prs[2][1])
        rows.append(rec)
    R1, R2 = be_rechts(K)
    rechts = sechsj_wert(R1) * sechsj_wert(R2)
    g = bipyramide(Kb, lam)
    x_s, x_f = g["x_stern"], g["x_fold"]
    # Schwerpunkt nach Betrag (PO3)
    gew = [abs(s) for s in s_mp]
    xc = sum(mp.mpf(r["x"]) * w for r, w in zip(rows, gew)) / sum(gew)
    # PR-Aufteilung der rechten Seite
    S1, V1, _ = regge_phase(laengen(R1))
    S2, V2, _ = regge_phase(laengen(R2))
    a = 1 / (24 * PI * mp.sqrt(V1 * V2))
    t_conv = a * mp.cos(S1 + S2 + PI / 2)
    t_fold = a * mp.cos(S1 - S2)
    r_pr = 2 * a * mp.cos(S1 + PI / 4) * mp.cos(S2 + PI / 4)
    # Fensterfummen mit Plateau +-w und cos^2-Uebergang bis +-2w, w = 3 sqrt(lambda)
    wbr = 3 * mp.sqrt(lam)

    def fenster(c):
        tot = mp.mpf(0)
        for r, s in zip(rows, s_mp):
            u = abs(r["x"] - c) / wbr
            if u <= 1:
                tau = 1
            elif u < 2:
                tau = mp.cos(PI * (u - 1) / 2) ** 2
            else:
                continue
            tot += tau * s
        return tot

    w_stern = fenster(x_s)
    w_fold = fenster(x_f)
    # geglaettetes Profil |sum s(x) exp(-(x-c)^2/(2 lambda))|
    profil = []
    for r0 in rows:
        c = r0["x"]
        tot = 0.0
        for r in rows:
            d = r["x"] - c
            if abs(d) <= 8 * math.sqrt(lam):
                tot += r["s"] * math.exp(-d * d / (2.0 * lam))
        profil.append(abs(tot))
    imax = max(range(len(profil)), key=lambda i: profil[i])
    return {
        "K": name, "lam": lam, "b": Kb, "zeilen": len(rows), "rechenzeit_s": time.time() - t0,
        "summe": f(summe), "rechts": f(rechts), "be_rel_abw": f(abs(summe - rechts) / abs(rechts)),
        "be_abw_rel_zu_betragssumme": f(abs(summe - rechts) / sum(gew)),
        "betragssumme_durch_rechts": f(sum(gew) / abs(rechts)),
        "x_stern": f(x_s), "x_fold": f(x_f), "x_schwerpunkt": f(xc),
        "rel_abstand_schwerpunkt": f(abs(xc - x_s) / x_s),
        "bary": [f(x) for x in g["bary"]],
        "pr_rechts": f(r_pr), "pr_konvex": f(t_conv), "pr_gefaltet": f(t_fold),
        "fenster_halbbreite": f(wbr), "fenster_x_stern": f(w_stern), "fenster_x_fold": f(w_fold),
        "profil_max_x": rows[imax]["x"], "profil": profil, "zeilen_daten": rows,
    }


def main():
    teil = sys.argv[1]
    ziel = sys.argv[2]
    t0 = time.time()
    if teil == "geometrie":
        out = teil_geometrie()
    elif teil == "zeit":
        out = teil_zeit()
    elif teil == "konvention":
        out = teil_konvention()
    elif teil == "po0":
        out = teil_po0()
    elif teil == "po1":
        out = teil_po1()
    elif teil == "po2":
        out = teil_po2()
    elif teil == "po3":
        out = teil_po3(sys.argv[3], int(sys.argv[4]))
    else:
        raise SystemExit("unbekannter Teil " + teil)
    out["_teil"] = teil
    out["_dps"] = DPS
    out["_laufzeit_s"] = time.time() - t0
    with open(ziel + ".neu", "w") as fh:
        json.dump(out, fh, indent=1)
    import os
    os.replace(ziel + ".neu", ziel)
    print("geschrieben", ziel, "laufzeit_s", round(out["_laufzeit_s"], 2))


if __name__ == "__main__":
    main()
