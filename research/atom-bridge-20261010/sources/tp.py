#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TENSOR-EIS-PYRO-1, Runde 40 (ag-physics), Code-Agent fuer die Leitung claude-primary.

Schritt 1 (Modus 'zaehlung'): Rang der Eichoperatoren auf dem Pyrochlor-Netz (Finns Tetraeder) im k-Raum.
  A  : xi an den Ecken, Kantenwert = Kantendehnung (Vertraeglichkeitsmatrix des Stabnetzes, 12 x 12)
  B1 : xi an den Tetraedermitten, Ecke = Mittel der zwei angrenzenden Mitten, Kantenwert = Kantendehnung (12 x 6)
  B2 : xi an den Tetraedermitten, Kantenwert = Winkelgroesse delta(rho_a . rho_b) an der Mitte (Keating, 12 x 6)
Gitter: kubische Kante a = 1, fcc-Primitivvektoren a1 = (0,1,1)/2, a2 = (1,0,1)/2, a3 = (1,1,0)/2.
Auf-Tetraeder Mitte R, Ecken R + r_a; Ab-Tetraeder Mitte R + 2 r_0, Ecken R + 2 r_0 - r_b.
Bloch-Konvention: Feld am Ort x hat die Phase e^{i k.x} (wirkliche Orte).
"""
import argparse, json, sys, time, platform, os, resource, hashlib, itertools
from fractions import Fraction
import numpy as np

AV = np.array([[0., .5, .5], [.5, 0., .5], [.5, .5, 0.]])          # Zeilen a1, a2, a3
BV = 2 * np.pi * np.linalg.inv(AV).T                                  # Zeilen b1, b2, b3 (a_i . b_j = 2 pi delta)
R8 = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]])    # 8 r_a (ganzzahlig)
PAARE = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
D8 = np.array([2, 2, 2])                                              # 8 * (2 r_0): Ab-Mitte
# sechs Kettenrichtungen (fcc-Nachbarvektoren) und ihre Koeffizienten in a1..a3 (fuer die ganzzahlige Ebenenprobe)
KETTEN_KOEFF = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, -1, 0), (0, 1, -1), (-1, 0, 1)]
KETTEN = np.array([np.array(c) @ AV for c in KETTEN_KOEFF])


def kanten():
    """12 Kanten: (Ort p * 8, Ort q * 8, Untergitter p, Untergitter q); erst 6 Auf-, dann 6 Ab-Kanten."""
    out = []
    for a, b in PAARE:
        out.append((R8[a], R8[b], a, b))
    for a, b in PAARE:
        out.append((D8 - R8[a], D8 - R8[b], a, b))
    return out


KANTEN = kanten()


# ------------------------------------------------------------------------------------------------ Gleitkomma
def phase(k, x8):
    """e^{i k . x} fuer x = x8/8; k (...,3), x8 (3,)."""
    return np.exp(1j * (k @ (np.asarray(x8, float) / 8.0)))


def C_A(k):
    """Vertraeglichkeitsmatrix (...,12,12): Kantendehnung aus Eckverschiebungen (unnormierte Kantenvektoren/2)."""
    sh = k.shape[:-1]
    C = np.zeros(sh + (12, 12), complex)
    for e, (p8, q8, a, b) in enumerate(KANTEN):
        d = (q8 - p8) / 2.0
        C[..., e, 3 * a:3 * a + 3] -= d * phase(k, p8)[..., None]
        C[..., e, 3 * b:3 * b + 3] += d * phase(k, q8)[..., None]
    return C


def P_B1(k):
    """(...,12,6): u_a = (xi_U e^{-i k.r_a} + xi_D e^{i k.r_a})/2."""
    sh = k.shape[:-1]
    P = np.zeros(sh + (12, 6), complex)
    for a in range(4):
        for j in range(3):
            P[..., 3 * a + j, j] = 0.5 * phase(k, -R8[a])
            P[..., 3 * a + j, 3 + j] = 0.5 * phase(k, R8[a])
    return P


def G_B1(k):
    return C_A(k) @ P_B1(k)


def G_B2(k):
    """(...,12,6): Kante (a,b) des Tetraeders: delta(rho_a . rho_b), rho = Mitte -> Nachbarmitte (Skalierung 1/2 von 8 rho)."""
    sh = k.shape[:-1]
    G = np.zeros(sh + (12, 6), complex)
    for e, (a, b) in enumerate(PAARE):
        ra, rb = R8[a].astype(float), R8[b].astype(float)
        # Auf-Tetraeder: rho_a = 2 r_a, Nachbar (Ab-Mitte) bei R + 2 r_a; Phase der Mitte R ausgeklammert
        G[..., e, 3:6] += rb * phase(k, 2 * R8[a])[..., None] + ra * phase(k, 2 * R8[b])[..., None]
        G[..., e, 0:3] -= rb + ra
        # Ab-Tetraeder: rho_b = -2 r_b, Nachbar (Auf-Mitte) bei x_D - 2 r_b; Phase der Mitte x_D ausgeklammert
        G[..., 6 + e, 0:3] += -rb * phase(k, -2 * R8[a])[..., None] - ra * phase(k, -2 * R8[b])[..., None]
        G[..., 6 + e, 3:6] += rb + ra
    return G


def glatt_basen(art):
    """Orthonormalbasen (12x6) des glatten und des versetzten Sektors bei k -> 0 (Einbettung einer glatten Verzerrung H)."""
    Hb = []
    for i, j in [(0, 0), (1, 1), (2, 2), (0, 1), (1, 2), (2, 0)]:
        H = np.zeros((3, 3))
        H[i, j] = H[j, i] = 1.0
        Hb.append(H)
    Eg = np.zeros((12, 6))
    Ev = np.zeros((12, 6))
    for s, H in enumerate(Hb):
        for e, (p8, q8, a, b) in enumerate(KANTEN):
            if art == 'B2':
                w = R8[a] @ H @ R8[b]          # Winkelgroesse: rho_a^T H rho_b (Auf und Ab gleich, rho -> -rho)
            else:
                d = (q8 - p8).astype(float)
                w = d @ H @ d / (d @ d)        # Kantendehnung
            Eg[e, s] = w
            Ev[e, s] = w if e < 6 else -w
    Qg, _ = np.linalg.qr(Eg)
    Qv, _ = np.linalg.qr(Ev)
    return Qg, Qv


def rang_svd(M, tol=1e-9):
    s = np.linalg.svd(M, compute_uv=False)
    smax = s.max(-1, keepdims=True)
    smax = np.where(smax > 0, smax, 1.0)
    return (s > tol * smax).sum(-1), s


def n_fam_gitter(m, L):
    """Zahl der Ebenenscharen k . a_m = 0 mod 2 pi durch den Gitterpunkt k = sum m_i b_i / L (ganzzahlig)."""
    n = np.zeros(m.shape[:-1], int)
    for c in KETTEN_KOEFF:
        n += ((m @ np.array(c)) % L == 0)
    return n


def gitter_k(L):
    m = np.stack(np.meshgrid(np.arange(L), np.arange(L), np.arange(L), indexing='ij'), -1).reshape(-1, 3)
    return m, (m / L) @ BV


def zaehlung_gleitkomma(L=24, nzuf=20000, nebene=2000, seed=5):
    rng = np.random.default_rng(seed)
    out = {'L': L}
    m, k = gitter_k(L)
    nf = n_fam_gitter(m, L)
    out['gitter'] = {}
    for name, f, ncol in (('A', C_A, 12), ('B1', G_B1, 6), ('B2', G_B2, 6)):
        r, s = rang_svd(f(k))
        ns = 12 - r
        n0 = ncol - r
        z = {'rang_verteilung': {str(int(x)): int((r == x).sum()) for x in np.unique(r)},
             'n_s_verteilung': {str(int(x)): int((ns == x).sum()) for x in np.unique(ns)},
             'n_0_verteilung': {str(int(x)): int((n0 == x).sum()) for x in np.unique(n0)},
             'calladine_n0_minus_ns': sorted(set(int(x) for x in (n0 - ns))),
             'anteil_rangarm': float((r < min(12, ncol)).mean())}
        if name == 'A':
            z['n_s_gleich_n_fam_alle'] = bool((ns == nf).all())
            z['abweichungen_n_s_n_fam'] = int((ns != nf).sum())
            z['rangarm_ohne_ebene'] = int(((r < 12) & (nf == 0)).sum())
            z['tabelle_n_fam_n_s'] = {str(int(f_)): sorted(set(int(x) for x in ns[nf == f_])) for f_ in np.unique(nf)}
            z['punkte_je_n_fam'] = {str(int(f_)): int((nf == f_).sum()) for f_ in np.unique(nf)}
        else:
            nz = np.any(m != 0, axis=1)
            z['rang_k_ungleich_0'] = sorted(set(int(x) for x in r[nz]))
            z['rang_k_0'] = int(r[~nz][0])
            z['kleinster_sv_rel_k_ungleich_0'] = float((s[nz].min(-1) / s[nz].max(-1)).min())
        out['gitter'][name] = z
    # Zufalls-k in der Zelle der b_i
    kz = rng.uniform(0, 1, (nzuf, 3)) @ BV
    out['zufall'] = {}
    for name, f, ncol in (('A', C_A, 12), ('B1', G_B1, 6), ('B2', G_B2, 6)):
        r, s = rang_svd(f(kz))
        out['zufall'][name] = {'n': nzuf, 'rang_verteilung': {str(int(x)): int((r == x).sum()) for x in np.unique(r)},
                               'kleinster_sv_rel': float((s.min(-1) / s.max(-1)).min())}
    # Zufalls-k auf jeder Ebenenschar: k = u + 2 pi n_m ... ; Ebene k . a_m = 0: k = Projektion zufaelliger Vektoren
    out['ebenen'] = {}
    for c, am in zip(KETTEN_KOEFF, KETTEN):
        v = rng.uniform(-2 * np.pi, 2 * np.pi, (nebene, 3)) * 2
        v = v - np.outer(v @ am, am) / (am @ am)
        assert np.abs(v @ am).max() < 1e-9
        r, s = rang_svd(C_A(v))
        rb1, _ = rang_svd(G_B1(v))
        rb2, _ = rang_svd(G_B2(v))
        out['ebenen'][str(c)] = {'A_rang_verteilung': {str(int(x)): int((r == x).sum()) for x in np.unique(r)},
                                 'A_zweitkleinster_sv_rel_min': float((np.sort(s, -1)[:, 1] / s.max(-1)).min()),
                                 'B1_rang': sorted(set(int(x) for x in rb1)), 'B2_rang': sorted(set(int(x) for x in rb2))}
    # det C_A gegen Produkt |sin(k . a_m / 2)|
    kd = rng.uniform(0, 1, (2000, 3)) @ BV
    ld = np.log(np.abs(np.linalg.det(C_A(kd))))
    ls = np.log(np.abs(np.sin(0.5 * (kd @ KETTEN.T)))).sum(-1)
    q = ld - ls
    out['det_quotient'] = {'log_mittel': float(q.mean()), 'log_spanne': float(q.max() - q.min()),
                           'quotient': float(np.exp(q.mean()))}
    # B1-Entkopplung
    G = G_B1(kz[:2000])
    out['B1_bloecke'] = {'auf_kanten_xiU_max': float(np.abs(G[:, :6, 0:3]).max()),
                         'ab_kanten_xiD_max': float(np.abs(G[:, 6:, 3:6]).max()),
                         'auf_kanten_xiD_min_norm': float(np.linalg.norm(G[:, :6, 3:6], axis=(-2, -1)).min()),
                         'ab_kanten_xiU_min_norm': float(np.linalg.norm(G[:, 6:, 0:3], axis=(-2, -1)).min())}
    # glatt / versetzt bei kleinem k
    out['klein_k'] = {}
    richt = [np.array([1., 0, 0]), np.array([1., 1, 0]) / np.sqrt(2), np.array([1., 1, 1]) / np.sqrt(3)]
    richt += [x / np.linalg.norm(x) for x in rng.normal(size=(20, 3))]
    for name, f, art in (('A', C_A, 'A'), ('B1', G_B1, 'B1'), ('B2', G_B2, 'B2')):
        Qg, Qv = glatt_basen(art)
        z = {}
        for eps in (1e-4, 1e-9):
            ng, nv, cosg, cosv = [], [], [], []
            for d in richt:
                M = f((eps * d)[None, :])[0]
                U, s, _ = np.linalg.svd(M)
                rr = 12 if name == 'A' else 6
                UG = U[:, :rr]
                cg = np.linalg.svd(Qg.T @ UG, compute_uv=False)
                cv = np.linalg.svd(Qv.T @ UG, compute_uv=False)
                ng.append(6 - int((cg > 1 - 1e-6).sum()))
                nv.append(6 - int((cv > 1 - 1e-6).sum()))
                cosg.append(sorted(float(x) for x in cg))
                cosv.append(sorted(float(x) for x in cv))
            z['eps_%g' % eps] = {'n_glatt': ng, 'n_versetzt': nv, 'cos_glatt_100_110_111': cosg[:3],
                                 'cos_versetzt_100_110_111': cosv[:3],
                                 'n_glatt_menge': sorted(set(ng)), 'n_versetzt_menge': sorted(set(nv))}
        out['klein_k'][name] = z
    return out


# ------------------------------------------------------------------------------------------------ exakt ueber Q(i)
def F(x, y=1):
    return Fraction(x, y)


def cm(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def csub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def cconj(a):
    return (a[0], -a[1])


def cdiv(a, b):
    n = b[0] * b[0] + b[1] * b[1]
    c = cm(a, cconj(b))
    return (c[0] / n, c[1] / n)


def cskal(s, a):
    return (s * a[0], s * a[1])


NULL = (F(0), F(0))
EINS = (F(1), F(0))


def p_aus_t(t):
    """rationaler Punkt auf dem Einheitskreis: ((1 - t^2) + 2 i t)/(1 + t^2)."""
    t = F(t)
    n = 1 + t * t
    return ((1 - t * t) / n, 2 * t / n)


def cpow(p, n):
    r = EINS
    b = p if n >= 0 else cconj(p)
    for _ in range(abs(n)):
        r = cm(r, b)
    return r


def ephase(p, x8):
    """e^{i k . x} mit p_j = e^{i k_j/8}, x8 = 8 x ganzzahlig."""
    r = EINS
    for j in range(3):
        r = cm(r, cpow(p[j], int(x8[j])))
    return r


def C_A_ex(p):
    C = [[NULL] * 12 for _ in range(12)]
    for e, (p8, q8, a, b) in enumerate(KANTEN):
        d = [int(x) for x in (q8 - p8)]
        ep, eq = ephase(p, p8), ephase(p, q8)
        for j in range(3):
            C[e][3 * a + j] = csub(C[e][3 * a + j], cskal(F(d[j]), ep))
            C[e][3 * b + j] = cadd(C[e][3 * b + j], cskal(F(d[j]), eq))
    return C


def P_B1_ex(p):
    P = [[NULL] * 6 for _ in range(12)]
    for a in range(4):
        em, ep_ = ephase(p, -R8[a]), ephase(p, R8[a])
        for j in range(3):
            P[3 * a + j][j] = cskal(F(1, 2), em)
            P[3 * a + j][3 + j] = cskal(F(1, 2), ep_)
    return P


def cmatmul(X, Y):
    n, m, q = len(X), len(Y), len(Y[0])
    Z = [[NULL] * q for _ in range(n)]
    for i in range(n):
        for kk in range(m):
            if X[i][kk] == NULL:
                continue
            for j in range(q):
                if Y[kk][j] != NULL:
                    Z[i][j] = cadd(Z[i][j], cm(X[i][kk], Y[kk][j]))
    return Z


def G_B2_ex(p):
    G = [[NULL] * 6 for _ in range(12)]
    for e, (a, b) in enumerate(PAARE):
        ra, rb = [int(x) for x in R8[a]], [int(x) for x in R8[b]]
        pa, pb = ephase(p, 2 * R8[a]), ephase(p, 2 * R8[b])
        qa, qb = ephase(p, -2 * R8[a]), ephase(p, -2 * R8[b])
        for j in range(3):
            G[e][3 + j] = cadd(cskal(F(rb[j]), pa), cskal(F(ra[j]), pb))
            G[e][j] = (F(-(rb[j] + ra[j])), F(0))
            G[6 + e][j] = csub(cskal(F(-rb[j]), qa), cskal(F(ra[j]), qb))
            G[6 + e][3 + j] = (F(rb[j] + ra[j]), F(0))
    return G


def rang_ex(M):
    M = [row[:] for row in M]
    r = 0
    rows, cols = len(M), len(M[0])
    for col in range(cols):
        piv = next((i for i in range(r, rows) if M[i][col] != NULL), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        for i in range(rows):
            if i != r and M[i][col] != NULL:
                f = cdiv(M[i][col], M[r][col])
                M[i] = [csub(M[i][j], cm(f, M[r][j])) for j in range(cols)]
        r += 1
    return r


def zaehlung_exakt(seed=13):
    import random
    rnd = random.Random(seed)
    werte = [F(pp, qq) for qq in (2, 3, 5, 7, 11) for pp in range(-3 * qq, 3 * qq + 1) if pp != 0]

    def t():
        return rnd.choice(werte)
    punkte = {}
    punkte['allgemein'] = [(t(), t(), t()) for _ in range(6)]
    eb = []
    for _ in range(3):
        x, z = t(), t()
        eb.append((x, -x, z))        # k_y = -k_x: Ebene a3
    for _ in range(3):
        x, z = t(), t()
        eb.append((x, x, z))         # k_y = k_x: Ebene a1 - a2
    punkte['ebene'] = eb
    punkte['linie_zwei_scharen_001'] = [(F(0), F(0), t()) for _ in range(3)]
    li3 = []
    for _ in range(3):
        x = t()
        li3.append((x, -x, -x))      # k || (1,-1,-1): Scharen a2, a3, a2 - a3
    punkte['linie_drei_scharen_1m1m1'] = li3
    punkte['k_null'] = [(F(0), F(0), F(0))]
    out = {}
    for name, pts in punkte.items():
        zeilen = []
        for tt in pts:
            p = [p_aus_t(x) for x in tt]
            CA = C_A_ex(p)
            GB1 = cmatmul(CA, P_B1_ex(p))
            GB2 = G_B2_ex(p)
            blk = all(GB1[e][j] == NULL for e in range(6) for j in range(3)) and \
                all(GB1[e][3 + j] == NULL for e in range(6, 12) for j in range(3))
            zeilen.append({'t': [str(x) for x in tt], 'rang_A': rang_ex(CA), 'rang_B1': rang_ex(GB1),
                           'rang_B2': rang_ex(GB2), 'B1_bloecke_exakt_null': blk})
        out[name] = zeilen
    return out


# =============================================================================================== Schritt 2
# B1 zerfaellt in zwei Kopien. Kopie 1: Regge-Ecken = Ab-Mitten (fcc), Staebe = Auf-Kanten in doppelter Laenge.
# Jede Kopie ist das fcc-Stabnetz mit naechsten Nachbarn; seine Zellen (Tetraeder-Oktaeder-Wabe) sind starr, also
# sind Fehlwinkel an den Staeben Funktionen der Stablaengen allein (linearisierter Regge-Kalkuel).
A1V, A2V, A3V = AV
BM = np.array([A1V, A2V, A3V, A1V - A2V, A2V - A3V, A3V - A1V])      # 6 Stabtypen m
LBAR = float(np.linalg.norm(A1V))                                       # Stablaenge = 2 l_P
NM = BM / LBAR


def _typ(d):
    for m in range(6):
        if np.allclose(d, BM[m]):
            return m, 1
        if np.allclose(d, -BM[m]):
            return m, -1
    raise ValueError(d)


def dieder(X, i, j, k, l):
    """Innerer Diederwinkel an der Kante (i,j) zwischen den Flaechen (i,j,k) und (i,j,l); komplexer Schritt erlaubt."""
    e = X[j] - X[i]
    ee = e / np.sqrt(e @ e)
    u = X[k] - X[i]
    u = u - (u @ ee) * ee
    w = X[l] - X[i]
    w = w - (w @ ee) * ee
    return np.arccos((u @ w) / np.sqrt((u @ u) * (w @ w)))


def baue_zelle(name, ecken, paare, dritte):
    """Zellmatrix D = d(Diederwinkel)/d(Kantenlaenge) (Kanten x Kanten), exakt ueber komplexen Schritt und C^+."""
    X = np.array(ecken, float)
    nV, nE = len(X), len(paare)
    info = []
    for (i, j) in paare:
        m, s = _typ(X[j] - X[i])
        info.append((m, X[i] if s > 0 else X[j]))
    C = np.zeros((nE, 3 * nV))
    for e, (i, j) in enumerate(paare):
        n = (X[j] - X[i]) / np.linalg.norm(X[j] - X[i])
        C[e, 3 * j:3 * j + 3] += n
        C[e, 3 * i:3 * i + 3] -= n
    h = 1e-20
    J = np.zeros((nE, 3 * nV))
    th0 = np.zeros(nE)
    for e, (i, j) in enumerate(paare):
        k_, l_ = dritte[e]
        th0[e] = float(np.real(dieder(X.astype(complex), i, j, k_, l_)))
        for v in range(nV):
            for c in range(3):
                Xc = X.astype(complex)
                Xc[v, c] += 1j * h
                J[e, 3 * v + c] = np.imag(dieder(Xc, i, j, k_, l_)) / h
    Cp = C.T @ np.linalg.inv(C @ C.T)
    D = J @ Cp
    return {'name': name, 'X': X, 'paare': paare, 'info': info, 'D': D, 'theta0': th0, 'C': C, 'J': J}


def zellen():
    z = []
    for name, ecken in (('tet1', [0 * A1V, A1V, A2V, A3V]), ('tet2', [0 * A1V, -A1V, -A2V, -A3V])):
        paare = PAARE
        dritte = [tuple(x for x in range(4) if x not in (i, j)) for (i, j) in paare]
        z.append(baue_zelle(name, ecken, paare, dritte))
    ecken = [A1V, A2V, A3V, A1V + A2V, A2V + A3V, A3V + A1V]
    gegen = [(0, 4), (1, 5), (2, 3)]
    paare = [(i, j) for i in range(6) for j in range(i + 1, 6) if (i, j) not in gegen]
    dritte = []
    for (i, j) in paare:
        p = [g for g in gegen if i not in g and j not in g]
        assert len(p) == 1
        dritte.append(p[0])
    z.append(baue_zelle('okt', ecken, paare, dritte))
    return z


ZELLEN = zellen()
ZELLE = {z['name']: z for z in ZELLEN}


def pmat(z, k):
    """(...,nE,6): Kantenamplituden der Zelle aus den 6 Bloch-Amplituden (Phase des Kantenanfangs)."""
    sh = k.shape[:-1]
    P = np.zeros(sh + (len(z['info']), 6), complex)
    for j, (m, S) in enumerate(z['info']):
        P[..., j, m] = np.exp(1j * (k @ S))
    return P


def A0_tet(z):
    n = np.array([NM[m] for (m, S) in z['info']])
    return (n @ n.T) ** 2 - 0.5


def ops_pyro(k, kopie=1, lam=0.5):
    """Kopie 1 (Finns Auf-Tetraeder = tet2) bzw. 2 (Ab-Tetraeder = tet1). Verzerrungsvariablen a = delta l / l."""
    Bm = 0.0
    for z in ZELLEN:
        P = pmat(z, k)
        Bm = Bm + np.einsum('...ja,jl,...lb->...ab', np.conj(P), z['D'], P)
    B = LBAR ** 2 * Bm                                                   # B = -LBAR^2 d eps/d l (Potential = -Regge)
    ph = np.exp(1j * (k @ BM.T))                                         # (...,6)
    M = NM * ((ph - 1.0) / LBAR)[..., :, None]                         # Eichung: delta l/l = n.(xi(Ende)-xi(Anfang))/l
    w = 1.0 + np.conj(ph)
    crow = -np.einsum('...m,...mb->...b', w, B)                          # Skalarkruemmung an der Ecke 0 (Vorfaktor egal)
    c = np.conj(crow)
    zt = ZELLE['tet2' if kopie == 1 else 'tet1']
    Pt = pmat(zt, k)
    A0 = (lambda n: (n @ n.T) ** 2 - lam)(np.array([NM[m] for (m, S) in zt['info']]))
    A = np.einsum('...ja,jl,...lb->...ab', np.conj(Pt), A0, Pt)
    return {'B': B, 'c': c, 'M': M, 'A': A}


# ---- kubischer Gu/Wen-Nachbau (Operatoren wie RUNDE-36/tensor-eis-n/code/tn.py)
S2 = 1.0 / np.sqrt(2.0)
IJ = [(0, 0), (1, 1), (2, 2), (0, 1), (1, 2), (2, 0)]


def _eps3():
    e = np.zeros((3, 3, 3))
    for (i, j, kk), s in {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1, (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}.items():
        e[i, j, kk] = s
    return e


EPS = _eps3()


def _basis6():
    Bb = np.zeros((6, 3, 3))
    for a, (i, j) in enumerate(IJ):
        if i == j:
            Bb[a, i, i] = 1.0
        else:
            Bb[a, i, j] = Bb[a, j, i] = S2
    return Bb


B6 = _basis6()
TR = np.einsum('aii->a', B6)
W_INC = -np.einsum('imk,jln,ank->aijml', EPS, EPS, B6)
W_INCB = np.einsum('bij,aijml->baml', B6, W_INC)
W_C = np.einsum('aiiml->aml', W_INC)


def ops_kubisch(k, lam=0.5):
    K = 2.0 * np.sin(0.5 * k)
    KK = K[..., :, None] * K[..., None, :]
    Inc = np.einsum('baml,...ml->...ba', W_INCB, KK)
    c = np.einsum('aml,...ml->...a', W_C, KK)
    G15 = np.einsum('aij,...i->...aj', B6, K) + np.einsum('ajk,...k->...aj', B6, K)
    A = np.broadcast_to(np.eye(6) - lam * np.outer(TR, TR), Inc.shape)
    return {'B': Inc.astype(complex), 'c': c.astype(complex), 'M': G15.astype(complex), 'A': A.astype(complex), 'K2': (K * K).sum(-1)}


def bravais(name):
    if name == 'kubisch':
        return np.eye(3), 2 * np.pi * np.eye(3), 1.0
    return AV, BV, LBAR


def ops(name, k):
    if name == 'kubisch':
        return ops_kubisch(k)
    return ops_pyro(k, kopie=2 if name == 'pyro2' else 1)


# ---- Statik (gemeinsames Werkzeug fuer beide Modelle)
def kern_statik_gen(B, c, rcond=1e-10, mit_min=False):
    n = B.shape[-1]
    sh = B.shape[:-2]
    Mx = np.zeros(sh + (n + 1, n + 1), complex)
    Mx[..., :n, :n] = B
    Mx[..., :n, n] = c
    Mx[..., n, :n] = np.conj(c)
    P = np.linalg.pinv(Mx, rcond=rcond, hermitian=True)
    x = P[..., :n, n]
    kap = np.einsum('...a,...ab,...b->...', np.conj(x), B, x)
    res = np.einsum('...a,...a->...', np.conj(c), x) - 1.0
    out = {'kap': kap.real, 'kap_im': np.abs(kap.imag), 'res': np.abs(res)}
    if mit_min:
        cn2 = (np.abs(c) ** 2).sum(-1)
        ok = cn2 > 1e-24
        cn = np.where(ok[..., None], c / np.sqrt(np.where(ok, cn2, 1.0))[..., None], 0.0)
        Pc = np.eye(n) - cn[..., :, None] * np.conj(cn)[..., None, :]
        ev = np.linalg.eigvalsh(Pc @ B @ Pc)
        skal = np.abs(np.linalg.eigvalsh(B)).max(-1)
        skal = np.where(skal > 0, skal, 1.0)
        out['tan_min_rel'] = np.where(ok, ev.min(-1) / skal, 0.0)
        out['tan_neg'] = np.where(ok, (ev < -1e-9 * skal[..., None]).sum(-1), 0)
        Bp = np.linalg.pinv(B, rcond=rcond, hermitian=True)
        d = np.einsum('...a,...ab,...b->...', np.conj(c), Bp, c).real
        out['kap_alt'] = np.where(ok, 1.0 / np.where(np.abs(d) > 0, d, 1.0), 0.0)
        out['ok'] = ok
    return out


def gittervektoren(name, rmax=17.0, nmax=24):
    AVm, _, einheit = bravais(name)
    g = np.arange(-nmax, nmax + 1)
    n = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1).reshape(-1, 3)
    R = n @ AVm
    r = np.linalg.norm(R, axis=1) / einheit
    sel = r <= rmax
    return n[sel], R[sel], r[sel]


def lauf_statik_gen(name, L, chunk=4, mit_min=False):
    t0 = time.time()
    AVm, BVm, einheit = bravais(name)
    m1 = np.arange(L)
    m3 = np.arange(L // 2 + 1)
    kap = np.empty((L, L, L // 2 + 1))
    st = {'res_max': 0.0, 'res_gross_anzahl': 0, 'kap_im_max': 0.0}
    if mit_min:
        st.update({'tan_min_rel': np.inf, 'tan_neg_anzahl': 0, 'kap_alt_maxabw': 0.0})
    for i0 in range(0, L, chunk):
        mm = np.stack(np.meshgrid(m1[i0:i0 + chunk], m1, m3, indexing='ij'), -1)
        k = (mm / L) @ BVm
        null = np.all(mm == 0, axis=-1)
        o = ops(name, k)
        r = kern_statik_gen(o['B'], o['c'], mit_min=mit_min)
        kap[i0:i0 + chunk] = np.where(null, 0.0, r['kap'])
        rr = np.where(null, 0.0, r['res'])
        st['res_max'] = max(st['res_max'], float(rr.max()))
        st['res_gross_anzahl'] += int((rr > 1e-8).sum())
        st['kap_im_max'] = max(st['kap_im_max'], float(r['kap_im'].max()))
        if mit_min:
            st['tan_min_rel'] = min(st['tan_min_rel'], float(np.where(r['ok'] & ~null, r['tan_min_rel'], np.inf).min()))
            st['tan_neg_anzahl'] += int(np.where(null, 0, r['tan_neg']).sum())
            sk = np.abs(r['kap']).max()
            st['kap_alt_maxabw'] = max(st['kap_alt_maxabw'], float(np.abs(np.where(r['ok'] & ~null, r['kap'] - r['kap_alt'], 0.0)).max() / max(sk, 1e-300)))
    t_kern = time.time() - t0
    G = np.fft.irfftn(kap, s=(L, L, L), axes=(0, 1, 2))
    n, R, r = gittervektoren(name)
    U = G[n[:, 0] % L, n[:, 1] % L, n[:, 2] % L]
    res = {'modell': name, 'L': L, 't_kern_s': t_kern, 'stat': st, 'G0': float(G[0, 0, 0]), 'mittel': float(G.mean()),
           'n_vektoren': int(len(n))}
    # Symmetrieprobe: U(R) gegen U(-R)
    idx = {tuple(x): i for i, x in enumerate(n)}
    res['spiegel_max'] = float(max(abs(U[i] - U[idx[tuple(-x)]]) for i, x in enumerate(n)))
    res['t_gesamt_s'] = time.time() - t0
    res['maxrss_MB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    return res, n, U


# ---- Spektrum auf der Zwangsflaeche
def phys_basis(M, c):
    X = np.concatenate([M, c[..., None]], -1)
    U, s, _ = np.linalg.svd(X)
    nfrei = M.shape[-2] - X.shape[-1]
    return U[..., :, X.shape[-1]:], s


def tensor_aus(name, a, k):
    """Glatter Tensor H (3x3) aus Kantenamplituden bei kleinem k (Phasen der Kantenmitte herausgenommen)."""
    if name == 'kubisch':
        return np.einsum('a,aij->ij', a, B6)
    Es = np.array([[NM[m] @ B6[s] @ NM[m] for s in range(6)] for m in range(6)])
    ph = np.exp(-0.5j * (BM @ k))
    x = np.linalg.solve(Es, a * ph)
    return np.einsum('a,aij->ij', x, B6)


def tt_anteil(H, k):
    kh = k / np.linalg.norm(k)
    P = np.eye(3) - np.outer(kh, kh)
    tPH = np.trace(P @ H)
    Htt = P @ H @ P - 0.5 * P * tPH
    ntt = float(np.sum(np.abs(Htt) ** 2))
    nt = float(abs(tPH) ** 2 / 2.0)
    return ntt / max(ntt + nt, 1e-300), ntt, nt


def spektrum_modell(name, L=16, seed=3):
    t0 = time.time()
    AVm, BVm, einheit = bravais(name)
    g = np.arange(L)
    mm = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1).reshape(-1, 3)
    mm = mm[np.any(mm != 0, axis=1)]
    k = (mm / L) @ BVm
    o = ops(name, k)
    A, B, M, c = o['A'], o['B'], o['M'], o['c']
    out = {'modell': name, 'L': L, 'nk': int(len(k))}
    # Identitaeten
    sB = np.abs(B).max()
    out['kontr'] = {'B_herm': float(np.abs(B - np.conj(np.swapaxes(B, -1, -2))).max() / sB),
                    'BM_null': float(np.abs(B @ M).max() / (sB * np.abs(M).max())),
                    'cM_null': float(np.abs(np.einsum('...a,...aj->...j', np.conj(c), M)).max() / (np.abs(c).max() * np.abs(M).max())),
                    'rang_M_min': int(np.linalg.matrix_rank(M).min()),
                    'c_norm_min_rel': float((np.linalg.norm(c, axis=-1) / np.abs(c).max()).min())}
    S, s = phys_basis(M, c)
    out['kontr']['sing_Mc_min_rel'] = float((s.min(-1) / s.max(-1)).min())
    Ar = np.conj(np.swapaxes(S, -1, -2)) @ A @ S
    Br = np.conj(np.swapaxes(S, -1, -2)) @ B @ S
    eA = np.linalg.eigvalsh(Ar)
    eB = np.linalg.eigvalsh(Br)
    w2 = np.linalg.eigvals(Ar @ Br)
    skal = np.abs(eA).max(-1) * np.abs(eB).max(-1)
    skal = np.where(skal > 0, skal, 1.0)
    pos = ((w2.real > 1e-9 * skal[:, None]) & (np.abs(w2.imag) <= 1e-9 * skal[:, None])).sum(-1)
    out['phys'] = {'dim': int(S.shape[-1]), 'positiv_je_k': [int(x) for x in pos], 'm_je_k': mm.tolist(),
                   'positiv_je_k_verteilung': {str(int(x)): int((pos == x).sum()) for x in np.unique(pos)},
                   'A_phys_min_rel': float((eA.min(-1) / np.abs(eA).max(-1)).min()),
                   'B_phys_min_rel': float((eB.min(-1) / np.abs(eB).max(-1)).min()),
                   'A_phys_neg_anteil': float((eA.min(-1) < -1e-9 * np.abs(eA).max(-1)).mean()),
                   'B_phys_neg_anteil': float((eB.min(-1) < -1e-9 * np.abs(eB).max(-1)).mean()),
                   'w2_min_rel': float((w2.real / skal[:, None]).min()), 'w2_im_max_rel': float((np.abs(w2.imag) / skal[:, None]).max())}
    # Eichdefekt der Spur-Eichung: A c im Bild von M?
    Q, _ = np.linalg.qr(M)
    Ac = np.einsum('...ab,...b->...a', A, c)
    rest = Ac - np.einsum('...aj,...j->...a', Q, np.einsum('...ja,...j->...a', np.conj(Q), Ac))
    dA = np.linalg.norm(rest, axis=-1) / np.maximum(np.linalg.norm(Ac, axis=-1), 1e-300)
    K2 = (np.abs(np.exp(1j * (k @ AVm.T)) - 1) ** 2).sum(-1)
    out['spur_eichdefekt'] = {'max': float(dA.max()), 'median': float(np.median(dA)),
                              'klein_k_max': float(dA[K2 <= np.quantile(K2, 0.01)].max())}
    # freie Dynamik ohne Zwangsbedingungen (beschreibend)
    wf = np.linalg.eigvals(A @ B)
    sk = np.linalg.norm(A, 2, axis=(-2, -1)) * np.linalg.norm(B, 2, axis=(-2, -1))
    neg = (-wf.real / sk[:, None]).max(-1)
    im = (np.abs(wf.imag) / sk[:, None]).max(-1)
    gam = np.abs(np.sqrt(wf.astype(complex)).imag).max(-1)
    out['frei'] = {'neg_rel_max': float(neg.max()), 'im_rel_max': float(im.max()), 'gamma_max': float(gam.max()),
                   'wachsend_anteil': float(((neg > 1e-6) | (im > 1e-6)).mean()),
                   'A_neg_anteil': float((np.linalg.eigvalsh(A).min(-1) < -1e-9).mean()),
                   'B_neg_anteil': float((np.linalg.eigvalsh(B).min(-1) < -1e-9 * np.abs(B).max()).mean())}
    # kleines k: Helizitaet (TT-Anteil), Dispersion je Richtung
    rng = np.random.default_rng(seed)
    richt = [('100', np.array([1., 0, 0])), ('110', np.array([1., 1, 0]) / np.sqrt(2)), ('111', np.array([1., 1, 1]) / np.sqrt(3))]
    richt += [('z%d' % i, x / np.linalg.norm(x)) for i, x in enumerate(rng.normal(size=(20, 3)))]
    kl = []
    for nm, d in richt:
        z = {'richtung': nm}
        for eps in (1e-3, 2e-3):
            kk = eps * d
            oo = ops(name, kk[None, :])
            S1, _ = phys_basis(oo['M'], oo['c'])
            S1 = S1[0]
            Ar1 = np.conj(S1.T) @ oo['A'][0] @ S1
            Br1 = np.conj(S1.T) @ oo['B'][0] @ S1
            ww, vv = np.linalg.eig(Ar1 @ Br1)
            o_ = np.argsort(ww.real)
            ww, vv = ww[o_], vv[:, o_]
            tt = []
            for j in range(vv.shape[1]):
                a = S1 @ vv[:, j]
                H = tensor_aus(name, a, kk)
                tt.append(tt_anteil(H, kk)[0])
            z['eps_%g' % eps] = {'w2_ueber_k2': [float(x) for x in ww.real / eps ** 2], 'w2_im': [float(x) for x in ww.imag],
                                 'tt_anteil': tt, 'A_phys': [float(x) for x in np.linalg.eigvalsh(Ar1)],
                                 'B_phys_ueber_k2': [float(x) for x in np.linalg.eigvalsh(Br1) / eps ** 2]}
        # Kontinuum: B auf (TT + T) = Komplement des Eichbilds, ohne Skalarbedingung (Signatur)
        kk = 1e-3 * d
        oo = ops(name, kk[None, :])
        Uq, sq, _ = np.linalg.svd(oo['M'][0])
        Sg = Uq[:, 3:]
        eBg = np.linalg.eigvalsh(np.conj(Sg.T) @ oo['B'][0] @ Sg) / 1e-6
        z['B_eichfrei_ueber_k2'] = [float(x) for x in eBg]
        kl.append(z)
    out['klein_k'] = kl
    out['t_s'] = time.time() - t0
    return out


# ---- Ortsraum-Kontrolle der Kopie (fcc-Torus L = 4): Regge-Matrix, Eichung, Statik gegen Fourier
def ortsraum_pyro(L=4):
    t0 = time.time()
    N = L ** 3
    AVi = np.linalg.inv(AV)

    def idx(nvec):
        nvec = np.mod(np.rint(nvec).astype(int), L)
        return (nvec[0] * L + nvec[1]) * L + nvec[2]

    def ganz(x):
        return x @ AVi
    nE = 6 * N
    B = np.zeros((nE, nE))
    sites = np.stack(np.meshgrid(np.arange(L), np.arange(L), np.arange(L), indexing='ij'), -1).reshape(-1, 3)
    for s in sites:
        X0 = s @ AV
        for z in ZELLEN:
            gl = []
            for (m, S) in z['info']:
                gl.append(6 * idx(ganz(X0 + S)) + m)
            gl = np.array(gl)
            B[np.ix_(gl, gl)] += LBAR ** 2 * z['D']
    Mg = np.zeros((nE, 3 * N))
    for s in sites:
        X0 = s @ AV
        i0 = idx(ganz(X0))
        for m in range(6):
            i1 = idx(ganz(X0 + BM[m]))
            e = 6 * i0 + m
            Mg[e, 3 * i1:3 * i1 + 3] += NM[m] / LBAR
            Mg[e, 3 * i0:3 * i0 + 3] -= NM[m] / LBAR
    cg = np.zeros((N, nE))
    for s in sites:
        X0 = s @ AV
        v = idx(ganz(X0))
        for m in range(6):
            e_start = 6 * v + m
            e_end = 6 * idx(ganz(X0 - BM[m])) + m
            cg[v] -= B[e_start] + B[e_end]
    out = {'L': L, 'B_sym': float(np.abs(B - B.T).max()), 'BM_null': float(np.abs(B @ Mg).max() / np.abs(B).max()),
           'cM_null': float(np.abs(cg @ Mg).max() / np.abs(cg).max()), 'c_summe_null': float(np.abs(cg.sum(0)).max())}
    # Spektrum B: Ortsraum gegen Vereinigung der Bloch-Spektren
    g = np.arange(L)
    mm = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1).reshape(-1, 3)
    kf = (mm / L) @ BV
    o = ops_pyro(kf)
    ef = np.sort(np.linalg.eigvalsh(o['B']).reshape(-1))
    eo = np.sort(np.linalg.eigvalsh(B))
    out['spektrum_B_max_abw'] = float(np.abs(ef - eo).max())
    out['spektrum_B_skala'] = float(np.abs(eo).max())
    # Statik: Ortsraum-KKT gegen Fourierweg
    Mx = np.zeros((nE + N, nE + N))
    Mx[:nE, :nE] = B
    Mx[:nE, nE:] = cg.T
    Mx[nE:, :nE] = cg
    Mp = np.linalg.pinv(Mx, rcond=1e-10, hermitian=True)

    def energie(rho):
        rho = rho - rho.mean()
        x = (Mp @ np.concatenate([np.zeros(nE), rho]))[:nE]
        return 0.5 * x @ B @ x, float(np.abs(cg @ x - rho).max())
    e1, r1 = energie(np.eye(N)[0])
    kap = kern_statik_gen(o['B'], o['c'])['kap']
    kap = np.where(np.all(mm == 0, axis=-1), 0.0, kap)
    G = np.fft.ifftn(kap.reshape(L, L, L)).real
    rows = []
    rmax = r1
    for v in [(1, 0, 0), (0, 1, 0), (1, 1, 0), (1, 1, 1), (2, 0, 0), (2, 1, 0), (1, -1, 0), (2, 2, 1)]:
        rho = np.zeros(N)
        rho[0] += 1.0
        rho[idx(np.array(v))] += 1.0
        ep, rr = energie(rho)
        rmax = max(rmax, rr)
        rows.append({'n': list(v), 'U_ortsraum': float(ep - 2 * e1), 'U_fourier': float(G[v[0] % L, v[1] % L, v[2] % L])})
    out['statik'] = {'zeilen': rows, 'zwang_res_max': rmax, 'max_abw': max(abs(r['U_ortsraum'] - r['U_fourier']) for r in rows)}
    out['t_s'] = time.time() - t0
    return out


def kontrolle_zellen():
    out = {}
    for z in ZELLEN:
        D = z['D']
        out[z['name']] = {'D_sym': float(np.abs(D - D.T).max()), 'schlaefli_l_D': float(np.abs(np.ones(len(D)) @ D).max()),
                          'theta0_grad': sorted(set(round(float(np.degrees(x)), 6) for x in z['theta0'])),
                          'kanten': len(D), 'D_max': float(np.abs(D).max())}
    # Ebenheit: Summe der Diederwinkel je Stabtyp = 2 pi (je Stab 2 Tetraeder + 2 Oktaeder)
    summe = np.zeros(6)
    for z in ZELLEN:
        for (m, S), th in zip(z['info'], z['theta0']):
            summe[m] += th
    out['dieder_summe_minus_2pi'] = [float(x - 2 * np.pi) for x in summe]
    # komplexer Schritt gegen zentrale Differenzen (nur beschreibend)
    z = ZELLE['okt']
    X = z['X']
    i, j = z['paare'][0]
    gegen = [(0, 4), (1, 5), (2, 3)]
    p = [g for g in gegen if i not in g and j not in g][0]
    h = 1e-6
    Xp = X.copy(); Xp[2, 1] += h
    Xm = X.copy(); Xm[2, 1] -= h
    fd = (dieder(Xp, i, j, *p) - dieder(Xm, i, j, *p)) / (2 * h)
    out['komplexschritt_gegen_differenz'] = float(abs(fd - z['J'][0, 3 * 2 + 1]))
    return out


# ------------------------------------------------------------------------------------------------ main
def sha(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['zaehlung', 'statik', 'spektrum', 'kontrolle'])
    ap.add_argument('--L', type=int, action='append')
    ap.add_argument('--modell', default='pyro1')
    ap.add_argument('--chunk', type=int, default=4)
    ap.add_argument('--mitmin', action='store_true')
    ap.add_argument('--out', required=True)
    ap.add_argument('--npz')
    a = ap.parse_args()
    t0 = time.time()
    info = {'numpy': np.__version__, 'python': platform.python_version(), 'host': platform.node(),
            'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'argv': sys.argv,
            'skript_sha256': sha(os.path.abspath(__file__))}
    res = {'info': info}
    if a.modus == 'zaehlung':
        L = a.L[0] if a.L else 24
        t = time.time(); res['gleitkomma'] = zaehlung_gleitkomma(L=L); print('gleitkomma %.1f s' % (time.time() - t), flush=True)
        t = time.time(); res['exakt'] = zaehlung_exakt(); print('exakt %.1f s' % (time.time() - t), flush=True)
    elif a.modus == 'statik':
        res['laeufe'] = []
        arr = {}
        for L in a.L:
            r, n, U = lauf_statik_gen(a.modell, L, a.chunk, mit_min=a.mitmin)
            res['laeufe'].append(r)
            arr['n'] = n
            arr['U_L%d' % L] = U
            print('statik %s L=%d fertig nach %.1f s' % (a.modell, L, time.time() - t0), flush=True)
        if a.npz:
            np.savez_compressed(a.npz + '.tmp.npz', **arr)
            os.replace(a.npz + '.tmp.npz', a.npz)
    elif a.modus == 'spektrum':
        L = a.L[0] if a.L else 16
        res['spektren'] = {}
        for nm in a.modell.split(','):
            res['spektren'][nm] = spektrum_modell(nm, L=L)
            print('spektrum %s %.1f s' % (nm, time.time() - t0), flush=True)
    else:
        t = time.time(); res['zellen'] = kontrolle_zellen(); print('zellen %.1f s' % (time.time() - t), flush=True)
        t = time.time(); res['ortsraum'] = ortsraum_pyro(4); print('ortsraum %.1f s' % (time.time() - t), flush=True)
    res['laufzeit_s'] = time.time() - t0
    res['maxrss_MB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    res['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    with open(a.out + '.tmp', 'w') as f:
        json.dump(res, f, indent=1)
    os.replace(a.out + '.tmp', a.out)
    print('fertig', a.modus, 'laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
