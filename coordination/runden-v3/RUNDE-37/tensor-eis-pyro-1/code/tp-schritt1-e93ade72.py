#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TENSOR-EIS-PYRO-1, Runde 40 (fmhc-physics), Code-Agent fuer die Leitung claude-primary.

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


# ------------------------------------------------------------------------------------------------ main
def sha(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['zaehlung'])
    ap.add_argument('--L', type=int, default=24)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    info = {'numpy': np.__version__, 'python': platform.python_version(), 'host': platform.node(),
            'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'argv': sys.argv,
            'skript_sha256': sha(os.path.abspath(__file__))}
    res = {'info': info}
    if a.modus == 'zaehlung':
        t = time.time(); res['gleitkomma'] = zaehlung_gleitkomma(L=a.L); print('gleitkomma %.1f s' % (time.time() - t), flush=True)
        t = time.time(); res['exakt'] = zaehlung_exakt(); print('exakt %.1f s' % (time.time() - t), flush=True)
    res['laufzeit_s'] = time.time() - t0
    res['maxrss_MB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    res['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    with open(a.out + '.tmp', 'w') as f:
        json.dump(res, f, indent=1)
    os.replace(a.out + '.tmp', a.out)
    print('fertig', a.modus, 'laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
