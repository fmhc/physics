#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""KOPPLUNG-TETRA-1 (Runde 42, fmhc-physics), Code-Agent fuer die Leitung claude-primary.

Modi:
  kontrolle : KT0 (Einzel-Federtetraeder, Paar mit gemeinsamer Ecke, gekoppeltes Paar), Werkzeugprobe W, Ringgeometrie
  rum       : RUM-Karte im k-Raum: Modell (a) Split-Atom gegen Modell (b) Federnetz (tp.C_A), Kernabbildung,
              Spektren an Symmetriepunkten, T2-reiche Baender, Bild
  eich      : Eichprobe am Sechsring (Bloch-Weg auf L-Superzellen), Varianten V0..V3, dichte Gegenprobe
Geometrie und C_A aus tp.py (TENSOR-EIS-PYRO-1, unveraendert, sha256 419d7da6...).
Bloch-Konvention Modell (a): x(n) = x e^{i k.R_n} je Zelle n (Auf U(n) bei R_n, Ab D(n) bei R_n + 2 r_0).
"""
import argparse, json, sys, os, time, platform, resource, hashlib, itertools
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tp  # noqa: E402  (TENSOR-EIS-PYRO-1, unveraendert)

AV = tp.AV                                   # Zeilen a1, a2, a3
BV = tp.BV                                   # Zeilen b1, b2, b3
RA = tp.R8.astype(float) / 8.0               # r_a: Auf-Ecken relativ zur Auf-Mitte
SL = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]])   # s_a in Gitterkoordinaten
SR = SL @ AV                                 # s_a wirklich: 0, a1, a2, a3
ZWEI_R0 = 2.0 * RA[0]                        # Ab-Mitte relativ zur Auf-Mitte derselben Zelle
PAARE = tp.PAARE
KETTEN = tp.KETTEN                           # sechs a_m (wirklich)
TOL_RANG = 1e-9
MT, IT = 2.0, (8.0 / 3.0) * 0.5 * float(RA[0] @ RA[0])   # Masse und Traegheit je starrem Tetraeder (Modell a)


def kreuz(r):
    return np.array([[0., -r[2], r[1]], [r[2], 0., -r[0]], [-r[1], r[0], 0.]])


XA = np.array([kreuz(r) for r in RA])        # [r_a]x


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def jdef(o):
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.floating,)):
        return None if not np.isfinite(o) else float(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    if isinstance(o, (np.bool_,)):
        return bool(o)
    if isinstance(o, complex):
        return [o.real, o.imag]
    raise TypeError(str(type(o)))


def sauber(x):
    """NaN/inf -> None, rekursiv (JSON)."""
    if isinstance(x, dict):
        return {k: sauber(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [sauber(v) for v in x]
    if isinstance(x, (float, np.floating)):
        return float(x) if np.isfinite(x) else None
    return x


# ------------------------------------------------------------------------------------------- Operatoren
def K_split(k):
    """Modell (a): Fehlpass m_a = (t_U - [r_a]x w_U) - p_a (t_D + [r_a]x w_D), p_a = exp(-i k.s_a). Form (...,12,12);
    Spalten (t_U, w_U, t_D, w_D), Zeilen (Ecke a, Komponente)."""
    k = np.asarray(k, float)
    sh = k.shape[:-1]
    K = np.zeros(sh + (12, 12), complex)
    for a in range(4):
        p = np.exp(-1j * (k @ SR[a]))[..., None, None]
        r = slice(3 * a, 3 * a + 3)
        K[..., r, 0:3] = np.eye(3)
        K[..., r, 3:6] = -XA[a]
        K[..., r, 6:9] = -p * np.eye(3)
        K[..., r, 9:12] = -p * XA[a]
    return K


def C_b(k):
    """Modell (b): Kantendehnung mit Einheitsvektoren (tp.C_A nutzt Laenge sqrt2), tp-Konvention e^{i k.x}."""
    return tp.C_A(np.asarray(k, float)) / np.sqrt(2.0)


def M_inv_halb():
    return np.diag(1.0 / np.sqrt(np.array([MT] * 3 + [IT] * 3 + [MT] * 3 + [IT] * 3)))


def rang(M, tol=TOL_RANG):
    s = np.linalg.svd(M, compute_uv=False)
    smax = s.max(-1, keepdims=True)
    smax = np.where(smax > 0, smax, 1.0)
    return (s > tol * smax).sum(-1), s / smax


def n_fam_num(k, tol=1e-9):
    x = np.asarray(k, float) @ KETTEN.T / (2 * np.pi)
    return (np.abs(x - np.round(x)) < tol).sum(-1)


def D_feder(pos, kanten, kopplung=None):
    """Zentralkraft-Federnetz, Federn 1, Massen 1; kopplung = (i, j, kappa) isotrope Split-Feder."""
    n = len(pos)
    D = np.zeros((3 * n, 3 * n))
    for i, j in kanten:
        d = pos[j] - pos[i]
        e = d / np.linalg.norm(d)
        P = np.outer(e, e)
        D[3 * i:3 * i + 3, 3 * i:3 * i + 3] += P
        D[3 * j:3 * j + 3, 3 * j:3 * j + 3] += P
        D[3 * i:3 * i + 3, 3 * j:3 * j + 3] -= P
        D[3 * j:3 * j + 3, 3 * i:3 * i + 3] -= P
    if kopplung is not None:
        i, j, kap = kopplung
        I3 = np.eye(3) * kap
        D[3 * i:3 * i + 3, 3 * i:3 * i + 3] += I3
        D[3 * j:3 * j + 3, 3 * j:3 * j + 3] += I3
        D[3 * i:3 * i + 3, 3 * j:3 * j + 3] -= I3
        D[3 * j:3 * j + 3, 3 * i:3 * i + 3] -= I3
    return D


def T2_einzel():
    D = D_feder(RA, PAARE)
    w, v = np.linalg.eigh(D)
    idx = np.where(np.abs(w - 2.0) < 1e-8)[0]
    assert len(idx) == 3
    return v[:, idx]


T2V = T2_einzel()                            # (12, 3), Ecken a = 0..3 (Ab-Tetraeder gleiche Matrix in Eckmarke b)


def stufen(werte, tol=1e-9):
    """Gruppiert aufsteigend sortierte Werte in Stufen (relativer Abstand <= tol)."""
    w = np.sort(np.asarray(werte, float))
    gr = [[w[0]]]
    for x in w[1:]:
        if abs(x - gr[-1][-1]) <= tol * max(1.0, abs(x)):
            gr[-1].append(x)
        else:
            gr.append([x])
    return [(float(np.mean(g)), len(g)) for g in gr]


def orth(B, tol=1e-8):
    U, s, _ = np.linalg.svd(B, full_matrices=False)
    if s.size == 0 or s.max() == 0:
        return B[:, :0]
    return U[:, s > tol * s.max()]


# ------------------------------------------------------------------------------------------- kontrolle
def paar_analyse(pos, kanten, t2_ecken, kopplung=None, paritaet=None):
    D = D_feder(pos, kanten, kopplung)
    w, v = np.linalg.eigh(D)
    n = len(pos)
    B = []
    for ecken in t2_ecken:
        for c in range(3):
            x = np.zeros(3 * n)
            for lab, site in enumerate(ecken):
                x[3 * site:3 * site + 3] = T2V[3 * lab:3 * lab + 3, c]
            B.append(x)
    Q = orth(np.array(B).T)
    gew = (np.abs(Q.T @ v) ** 2).sum(0)
    wproj = np.linalg.eigvalsh(Q.T @ D @ Q)               # T2-Block, auf die T2-Spanne projiziert
    proj = {'werte': wproj.tolist(), 'stufen': stufen(wproj), 'delta_rel': float((wproj.max() - wproj.min()) / 2.0)}
    null = w <= 1e-10
    pos_idx = np.where(~null)[0]
    wpos = w[pos_idx]
    # Stufen der positiven Werte mit mittlerem T2-Anteil und Paritaet
    st = []
    i = 0
    srt = np.argsort(wpos)
    wpos_s = wpos[srt]
    idx_s = pos_idx[srt]
    while i < len(wpos_s):
        j = i + 1
        while j < len(wpos_s) and abs(wpos_s[j] - wpos_s[j - 1]) <= 1e-9 * max(1.0, abs(wpos_s[j])):
            j += 1
        ids = idx_s[i:j]
        e = {'omega2': float(wpos_s[i:j].mean()), 'vielfach': int(j - i), 't2_anteil': float(gew[ids].mean())}
        if paritaet is not None:
            e['paritaet'] = float(np.mean([v[:, q] @ paritaet @ v[:, q] for q in ids]))
        st.append(e)
        i = j
    # T2-reichste Stufen bis 6 Moden
    order = sorted(range(len(st)), key=lambda q: -st[q]['t2_anteil'])
    gewaehlt, summe = [], 0
    for q in order:
        if summe >= 6:
            break
        gewaehlt.append(q)
        summe += st[q]['vielfach']
    t2_stufen = sorted([st[q] for q in gewaehlt], key=lambda e: e['omega2'])
    vals = [e['omega2'] for e in t2_stufen]
    return {'n_null': int(null.sum()), 'groesster_nullwert': float(np.abs(w[null]).max()) if null.any() else None,
            'stufen_positiv': st, 'dim_T2_spanne': int(Q.shape[1]),
            't2_stufen': t2_stufen, 't2_summe_vielfach': int(summe),
            't2_muster': sorted(e['vielfach'] for e in t2_stufen),
            'delta_T2_rel': float((max(vals) - min(vals)) / 2.0) if vals else None,
            'T2_projiziert': proj,
            'dreifach_positiv': bool(any(e['vielfach'] >= 3 for e in st))}


def ring(abc=(1, 2, 3)):
    """Sechsring: Tetraeder (Zelle, Typ 0 = Auf / 1 = Ab) und gemeinsame Ecken (Zelle, Platz)."""
    a, b, c = abc
    s = SL
    z0 = np.zeros(3, int)
    T = [(z0, 0), (-s[a], 1), (-s[a] + s[b], 0), (-s[a] + s[b] - s[c], 1), (s[b] - s[c], 0), (-s[c], 1)]
    E = [(z0, a), (-s[a] + s[b], b), (-s[a] + s[b], c), (s[b] - s[c], a), (s[b] - s[c], b), (z0, c)]
    return [(np.array(n), t) for n, t in T], [(np.array(n), p) for n, p in E]


def ecken_von(n, t):
    if t == 0:
        return [(tuple(n), a) for a in range(4)]
    return [(tuple(n + SL[b]), b) for b in range(4)]


def mitte(n, t):
    return n @ AV + (ZWEI_R0 if t == 1 else 0.0)


def ring_geometrie(abc=(1, 2, 3)):
    T, E = ring(abc)
    ok = True
    for i in range(6):
        e = (tuple(E[i][0]), E[i][1])
        ok &= e in ecken_von(*T[i]) and e in ecken_von(*T[(i + 1) % 6])
    P = np.array([n @ AV + RA[p] for n, p in E])
    c = P.mean(0)
    _, s, vt = np.linalg.svd(P - c)
    nvec = vt[2]
    if nvec.sum() < 0:
        nvec = -nvec
    e1 = P[0] - c
    e1 = e1 - (e1 @ nvec) * nvec
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(nvec, e1)
    seiten = [float(np.linalg.norm(P[(i + 1) % 6] - P[i])) for i in range(6)]
    radien = [float(np.linalg.norm(p - c)) for p in P]
    hoehen = [float((mitte(n, t) - c) @ nvec) for n, t in T]
    zellen_versch = len(set((tuple(n), t) for n, t in T)) == 6 and len(set((tuple(n), p) for n, p in E)) == 6
    return {'abc': list(abc), 'ecken_passen': bool(ok), 'verschieden': bool(zellen_versch),
            'ebenen_rest': float(s[2]), 'seiten': seiten, 'radien': radien, 'l_P': float(np.sqrt(2) / 4),
            'hoehen_mitten': hoehen, 'normale': nvec.tolist(), 'e1': e1.tolist(), 'e2': e2.tolist(),
            'mitte': c.tolist(), 'typen': [int(t) for _, t in T]}


def holonomie_matrix(gestaffelt=False):
    s = np.array([1, -1, 1, -1, 1, -1]) if gestaffelt else np.ones(6)
    return np.hstack([si * np.eye(3) for si in s]), s


def verteilungen(H, s, seed_s=7, seed_v=8):
    """32 Verteilungen phi (6,3) mit Summe phi = H; theta_i = s_i phi_i (s = +1 fuer H+)."""
    out = []
    for j in range(6):
        ph = np.zeros((6, 3))
        ph[j] = H
        out.append(('konz%d' % (j + 1), ph))
    out.append(('gleich', np.tile(H / 6.0, (6, 1))))
    for j in range(3):
        ph = np.zeros((6, 3))
        ph[j] = ph[j + 3] = H / 2.0
        out.append(('paar%d' % (j + 1), ph))
    for name, idx in (('auf', [0, 2, 4]), ('ab', [1, 3, 5])):
        ph = np.zeros((6, 3))
        ph[idx] = H / 3.0
        out.append((name, ph))
    rs = np.random.default_rng(seed_s)
    for r in range(10):
        w = rs.dirichlet(np.ones(6))
        out.append(('zs%d' % r, w[:, None] * H[None, :]))
    rv = np.random.default_rng(seed_v)
    for r in range(10):
        eta = rv.normal(0.0, 1.0 / 6.0, (6, 3))
        eta -= eta.mean(0)
        out.append(('zv%d' % r, H[None, :] / 6.0 + eta))
    return [(nm, (s[:, None] * ph).reshape(18)) for nm, ph in out]


def eich_kennzahlen(S, geo, gestaffelt=False):
    Hm, s = holonomie_matrix(gestaffelt)
    lam = np.linalg.eigvalsh(0.5 * (S + S.T))
    lmax = float(lam.max())
    rich = {'n': np.array(geo['normale']), 'e1': np.array(geo['e1']), 'e2': np.array(geo['e2'])}
    out = {'eigenwerte_S': lam.tolist(), 'lambda_max': lmax, 'je_richtung': {}}
    Us, UKs = [], []
    for rn, H in rich.items():
        vs = verteilungen(H, s)
        E = {nm: float(0.5 * th @ S @ th) for nm, th in vs}
        hol = max(float(np.abs(Hm @ th - H).max()) for _, th in vs)
        vals = np.array(list(E.values()))
        emax, emin = vals.max(), vals.min()
        U = (emax - emin) / emax if emax > 0 else float('nan')
        ek, eg = E['konz1'], E['gleich']
        UK = abs(ek - eg) / max(ek, eg) if max(ek, eg) > 0 else float('nan')
        Us.append(U)
        UKs.append(UK)
        out['je_richtung'][rn] = {'E': E, 'E_max': float(emax), 'E_min': float(emin), 'U': U, 'U_K': UK,
                                  'holonomie_fehler': hol}
    out['U'] = float(np.max(Us)) if np.all(np.isfinite(Us)) else float('nan')
    out['U_K'] = float(np.max(UKs)) if np.all(np.isfinite(UKs)) else float('nan')
    # Eichverletzung G
    _, sv, vt = np.linalg.svd(Hm)
    Qk = vt[3:].T                              # 18 x 15, ker H
    gk = np.linalg.eigvalsh(Qk.T @ (0.5 * (S + S.T)) @ Qk).max()
    out['G'] = float(gk / lmax) if lmax > 0 else float('nan')
    out['lambda_max_kerH'] = float(gk)
    return out


def modus_kontrolle(a):
    res = {}
    # 1. Einzeltetraeder
    w = np.linalg.eigvalsh(D_feder(RA, PAARE))
    soll = np.array([0.] * 6 + [1., 1., 2., 2., 2., 4.])
    res['einzel'] = {'omega2': w.tolist(), 'max_abw': float(np.abs(np.sort(w) - soll).max())}
    # 2. Paar mit gemeinsamer Ecke 0 (Inversion durch r_0)
    pos7 = np.array([RA[0], RA[1], RA[2], RA[3], 2 * RA[0] - RA[1], 2 * RA[0] - RA[2], 2 * RA[0] - RA[3]])
    ab = [0, 4, 5, 6]
    kanten7 = list(PAARE) + [(ab[i], ab[j]) for i, j in PAARE]
    perm = [0, 4, 5, 6, 1, 2, 3]
    P = np.zeros((21, 21))
    for i, j in enumerate(perm):
        P[3 * j:3 * j + 3, 3 * i:3 * i + 3] = -np.eye(3)
    res['paar'] = paar_analyse(pos7, kanten7, [[0, 1, 2, 3], ab], paritaet=P)
    res['paar']['inversion_symmetrie_D'] = float(np.abs(P @ D_feder(pos7, kanten7) @ P.T - D_feder(pos7, kanten7)).max())
    # 3. gekoppeltes Paar (8 Massen, Split-Feder kappa zwischen Ecke 0 und ihrer Kopie 4)
    pos8 = np.array([RA[0], RA[1], RA[2], RA[3], RA[0], 2 * RA[0] - RA[1], 2 * RA[0] - RA[2], 2 * RA[0] - RA[3]])
    ab8 = [4, 5, 6, 7]
    kanten8 = list(PAARE) + [(ab8[i], ab8[j]) for i, j in PAARE]
    res['gekoppelt'] = {}
    for kap in (1e-3, 1e-2, 0.1, 1.0, 10.0, 100.0, 1e4):
        r = paar_analyse(pos8, kanten8, [[0, 1, 2, 3], ab8], kopplung=(0, 4, kap))
        res['gekoppelt']['%g' % kap] = {'n_null': r['n_null'], 't2_stufen': r['t2_stufen'],
                                       'delta_T2_rel': r['delta_T2_rel'], 't2_muster': r['t2_muster'],
                                       'T2_projiziert': r['T2_projiziert']}
    # 4. Ringgeometrie und Werkzeugprobe W
    g1 = ring_geometrie((1, 2, 3))
    g2 = ring_geometrie((0, 1, 2))
    res['ring'] = {'haupt': g1, 'gegen': g2}
    Hp, _ = holonomie_matrix(False)
    W = {}
    for nm, S in (('eichform', Hp.T @ Hp), ('massenform', np.eye(18))):
        W[nm] = {'H+': eich_kennzahlen(S, g1, False), 'H-': eich_kennzahlen(S, g1, True)}
        for h in ('H+', 'H-'):
            for rn in W[nm][h]['je_richtung']:
                W[nm][h]['je_richtung'][rn].pop('E')
    res['werkzeug'] = W
    return res


# ------------------------------------------------------------------------------------------- rum
SYMPUNKTE = {'Gamma': [0, 0, 0], 'X': [1, 0, 0], 'L': [.5, .5, .5], 'W': [1, .5, 0], 'K': [.75, .75, 0],
             'U': [1, .25, .25]}


def T2_bloch(k):
    """(N,12,6): T2-Moden von Auf- (Spalten 0..2) und Ab-Tetraeder (3..5) als Bloch-Vektoren in tp-Konvention."""
    k = np.atleast_2d(k)
    B = np.zeros((k.shape[0], 12, 6), complex)
    for a in range(4):
        pu = np.exp(-1j * (k @ RA[a]))
        pd = np.exp(-1j * (k @ (ZWEI_R0 - RA[a])))
        for j in range(3):
            for c in range(3):
                B[:, 3 * a + j, c] = T2V[3 * a + j, c] * pu
                B[:, 3 * a + j, 3 + c] = T2V[3 * a + j, c] * pd
    return B


def t2_gewichte(k, vecs):
    """vecs (N,12,m) orthonormale Eigenvektoren; Anteil in der T2-Spanne je Spalte."""
    B = T2_bloch(k)
    out = np.zeros(vecs.shape[0::2])
    for i in range(B.shape[0]):
        Q = orth(B[i])
        out[i] = (np.abs(Q.conj().T @ vecs[i]) ** 2).sum(0)
    return out


def kern_vergleich(k):
    """Je Punkt: Kern von K -> Eckverschiebungen (tp-Konvention); Residuum mit C_A, Hauptwinkel zu ker C_A."""
    Ka = K_split(k)
    Cb = tp.C_A(k)
    _, sa, vha = np.linalg.svd(Ka)
    _, sb, vhb = np.linalg.svd(Cb)
    res_max, winkel_max, dim_ungleich = 0.0, 0.0, 0
    for i in range(k.shape[0]):
        na = int((sa[i] <= TOL_RANG * sa[i, 0]).sum())
        nb = int((sb[i] <= TOL_RANG * sb[i, 0]).sum())
        if na == 0 and nb == 0:
            continue
        if na != nb:
            dim_ungleich += 1
            continue
        X = vha[i, 12 - na:].conj().T                       # (12, na) Kern von K
        U = np.zeros((12, na), complex)
        for a in range(4):
            u = X[0:3] - XA[a] @ X[3:6]
            U[3 * a:3 * a + 3] = u * np.exp(-1j * (k[i] @ RA[a]))
        r = np.linalg.norm(Cb[i] @ U, axis=0) / (sb[i, 0] * np.linalg.norm(U, axis=0))
        res_max = max(res_max, float(r.max()))
        Q1 = orth(U)
        Q2 = vhb[i, 12 - nb:].conj().T
        sv = np.linalg.svd(Q1.conj().T @ Q2, compute_uv=False)
        winkel_max = max(winkel_max, float(1.0 - sv.min()))
    return {'residuum_max': res_max, 'hauptwinkel_1_minus_cos_max': winkel_max, 'dim_ungleich': dim_ungleich}


def vergleich_satz(name, k, nfam):
    na, sa = rang(K_split(k))
    nb, sb = rang(tp.C_A(k))
    na, nb = 12 - na, 12 - nb
    out = {'punkte': int(k.shape[0]),
           'n_a_verteilung': {str(int(x)): int((na == x).sum()) for x in np.unique(na)},
           'n_fam_verteilung': {str(int(x)): int((nfam == x).sum()) for x in np.unique(nfam)},
           'n_a_ungleich_n_b': int((na != nb).sum()),
           'n_a_ungleich_n_fam': int((na != np.where(nfam > 0, np.minimum(nfam, 99), 0)).sum()),
           'tabelle_n_fam_n_a': {str(int(f)): sorted(set(int(x) for x in na[nfam == f])) for f in np.unique(nfam)},
           'n_a_ge1_ausserhalb': int(((na >= 1) & (nfam == 0)).sum()),
           'n_a_0_auf_ebene': int(((na == 0) & (nfam >= 1)).sum()),
           'menge_ungleich_ab': int(((na >= 1) != (nb >= 1)).sum()),
           'menge_ungleich_fam': int(((na >= 1) != (nfam >= 1)).sum())}
    # Abstand der Singulaerwerte (relativ): groesster "Null"-Wert und kleinster "Nicht-Null"-Wert
    ar = np.arange(len(na))
    out['sa_kleinster_ungleich_null'] = float(np.min(np.where(na < 12, sa[ar, np.maximum(11 - na, 0)], np.inf)))
    out['sa_groesster_null'] = float(np.max(np.where(na > 0, sa[ar, np.minimum(12 - na, 11)], 0.0)))
    return out, na, nb


def modus_rum(a):
    rng = np.random.default_rng(5)
    res = {}
    # Gitter
    m, kg = tp.gitter_k(a.L)
    nf = tp.n_fam_gitter(m, a.L)
    nf_eff = np.where(np.all(m == 0, axis=1), 6, nf)          # k = 0: alle sechs Scharen
    g, na_g, nb_g = vergleich_satz('gitter', kg, nf_eff)
    g['k0_n_a'] = int(na_g[np.all(m == 0, axis=1)][0])
    res['gitter'] = g
    # Zufall
    kz = rng.uniform(0, 1, (a.nzuf, 3)) @ BV
    res['zufall'], _, _ = vergleich_satz('zufall', kz, n_fam_num(kz))
    # Ebenen
    res['ebenen'] = {}
    kp_all = []
    for j, am in enumerate(KETTEN):
        v = rng.uniform(0, 1, (a.nebene, 3)) @ BV
        ah = am / (am @ am)
        v = v - (v @ am)[:, None] * ah[None, :]
        n = rng.integers(0, 2, a.nebene)
        v = v + (2 * np.pi * n)[:, None] * ah[None, :]
        kp_all.append(v)
        res['ebenen']['schar%d' % j], _, _ = vergleich_satz('ebene', v, n_fam_num(v))
    # Linien zweier und dreier Scharen
    res['linien'] = {}
    kl_all = []
    for nm, d in (('100', [1, 0, 0]), ('010', [0, 1, 0]), ('001', [0, 0, 1]), ('111', [1, 1, 1]),
                  ('1-1-1', [1, -1, -1]), ('-11-1', [-1, 1, -1]), ('-1-11', [-1, -1, 1])):
        t = rng.uniform(0.05, 0.95, a.nlinie)
        kl = 2 * np.pi * t[:, None] * np.array(d, float)[None, :]
        kl_all.append(kl)
        res['linien'][nm], _, _ = vergleich_satz('linie', kl, n_fam_num(kl))
    # Kernabbildung an allen Punkten mit RUM
    kk = np.vstack([kg[na_g >= 1]] + kp_all + kl_all)
    res['kernabbildung'] = kern_vergleich(kk)
    res['kernabbildung']['punkte'] = int(kk.shape[0])
    # Symmetriepunkte: Spektren (a) und (b), T2-Anteile (b)
    sp = {}
    for nm, x in SYMPUNKTE.items():
        k = 2 * np.pi * np.array(x, float)[None, :]
        C = C_b(k)
        Db = np.einsum('nji,njk->nik', C.conj(), C)
        wb, vb = np.linalg.eigh(Db)
        gw = t2_gewichte(k, vb)
        Ka = K_split(k)
        Mh = M_inv_halb()
        Pa = Mh @ np.einsum('nji,njk->nik', Ka.conj(), Ka)[0] @ Mh
        wa = np.linalg.eigvalsh(Pa)
        sp[nm] = {'k_2pi': x, 'n_fam': int(n_fam_num(k)[0]),
                  'b_omega2': wb[0].tolist(), 'b_t2_anteil': gw[0].tolist(),
                  'b_stufen': stufen(np.where(np.abs(wb[0]) < 1e-12, 0.0, wb[0])),
                  'b_t2_reich': [float(x_) for x_, g_ in zip(wb[0], gw[0]) if g_ > 0.5],
                  'a_omega2': wa.tolist(), 'a_n_null': int((wa <= 1e-10 * wa.max()).sum()),
                  'a_rum': int(12 - rang(Ka)[0][0])}
    res['sympunkte'] = sp
    # T2-reiche Baender (b) auf dem Gitter Lband
    mb, kb = tp.gitter_k(a.Lband)
    C = C_b(kb)
    Db = np.einsum('nji,njk->nik', C.conj(), C)
    wb, vb = np.linalg.eigh(Db)
    gw = t2_gewichte(kb, vb)
    reich = gw > 0.5
    res['t2_baender'] = {'L': a.Lband, 'omega2_min': float(wb[reich].min()), 'omega2_max': float(wb[reich].max()),
                         'zahl_je_k': {str(int(x)): int((reich.sum(1) == x).sum()) for x in np.unique(reich.sum(1))},
                         'gewicht_summe_je_k_min': float(gw.sum(1).min()), 'gewicht_summe_je_k_max': float(gw.sum(1).max())}
    # Bild
    if a.bild:
        res['bild'] = bild(a.bild)
    return res


def bild(pfad):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig = plt.figure(figsize=(13, 6))
    ax1 = fig.add_subplot(1, 2, 1)
    n = 241
    x = np.linspace(-1.5, 1.5, n)
    X, Y = np.meshgrid(x, x, indexing='xy')
    kz = 0.3
    k = 2 * np.pi * np.stack([X.ravel(), Y.ravel(), np.full(X.size, kz)], -1)
    _, s = rang(K_split(k))
    smin = np.log10(np.maximum(s[:, -1], 1e-17)).reshape(n, n)
    im = ax1.imshow(smin, origin='lower', extent=[-1.5, 1.5, -1.5, 1.5], cmap='viridis', vmin=-4, vmax=0)
    fig.colorbar(im, ax=ax1, label='log10 kleinster Singulaerwert von K(k) (relativ)')
    for am in KETTEN:
        for nn in range(-4, 5):
            # a_m . (x, y, kz) = nn
            if abs(am[1]) > 1e-12:
                yy = (nn - am[0] * x - am[2] * kz) / am[1]
                ax1.plot(x, yy, 'w--', lw=0.6, alpha=0.8)
            elif abs(am[0]) > 1e-12:
                xx = (nn - am[2] * kz) / am[0]
                ax1.axvline(xx, color='w', ls='--', lw=0.6, alpha=0.8)
    ax1.set_xlim(-1.5, 1.5)
    ax1.set_ylim(-1.5, 1.5)
    ax1.set_xlabel('k_x / 2 pi')
    ax1.set_ylabel('k_y / 2 pi')
    ax1.set_title('Schnitt k_z = 0,3 . 2 pi; gestrichelt: k . a_m = 2 pi n')
    ax2 = fig.add_subplot(1, 2, 2, projection='3d')
    g = np.linspace(-1, 1, 25)
    G = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1).reshape(-1, 3)
    r, _ = rang(K_split(2 * np.pi * G))
    nr = 12 - r
    sel = nr >= 1
    farben = {1: 'tab:blue', 2: 'tab:orange', 3: 'tab:red', 6: 'k'}
    for v_ in sorted(set(nr[sel].tolist())):
        q = nr == v_
        ax2.scatter(G[q, 0], G[q, 1], G[q, 2], s=2 if v_ == 1 else 6, c=farben.get(v_, 'm'), label='%d RUM' % v_,
                    alpha=0.5 if v_ == 1 else 0.9)
    ax2.set_xlabel('k_x / 2 pi')
    ax2.set_ylabel('k_y / 2 pi')
    ax2.set_zlabel('k_z / 2 pi')
    ax2.set_title('Gitterpunkte mit RUM (Modell a), Wuerfel [-1, 1]^3')
    ax2.legend(loc='upper left', fontsize=8)
    fig.tight_layout()
    fig.savefig(pfad, dpi=110)
    return {'pfad': pfad, 'punkte_3d': int(G.shape[0]), 'punkte_mit_rum': int(sel.sum())}


# ------------------------------------------------------------------------------------------- eich
def bloch_daten(L):
    m, k = tp.gitter_k(L)
    K = K_split(k)
    _, s, vh = np.linalg.svd(K)
    nz = s > TOL_RANG * s[:, :1]
    V = vh.conj().transpose(0, 2, 1)
    inv2 = np.where(nz, 1.0 / np.where(nz, s, 1.0) ** 2, 0.0)
    Phip = np.einsum('nij,nj,nkj->nik', V, inv2, V.conj())
    Phi = np.einsum('nji,njk->nik', K.conj(), K)
    return {'k': k, 'nz': nz, 'V': V, 'Phip': Phip, 'Phi': Phi, 'N': k.shape[0]}


def eich_bloch(bd, L, abc):
    geo = ring_geometrie(abc)
    T, _ = ring(abc)
    k, nz, V, Phip, Phi, N = bd['k'], bd['nz'], bd['V'], bd['Phip'], bd['Phi'], bd['N']
    Rz = np.array([n @ AV for n, _ in T])                    # Zellorte der Ringtetraeder
    rot = [(i, 6 * T[i][1] + 3 + al) for i in range(6) for al in range(3)]
    tra = [(i, 6 * T[i][1] + al) for i in range(6) for al in range(3)]

    def block(Mk, coords):
        cs = [c for _, c in coords]
        Rc = Rz[[i for i, _ in coords]]
        Mr = np.zeros((len(cs), len(cs)), complex)
        for q0 in range(0, N, 2048):
            q1 = min(N, q0 + 2048)
            ph = np.exp(1j * (k[q0:q1] @ Rc.T))
            sub = Mk[q0:q1][:, cs][:, :, cs]
            Mr += np.einsum('na,nab,nb->ab', ph, sub, ph.conj())
        Mr /= N
        return Mr.real, float(np.abs(Mr.imag).max())

    def W_basis(coords):
        cs = [c for _, c in coords]
        Rc = Rz[[i for i, _ in coords]]
        Z = []
        for q in np.where((~nz).any(1))[0]:
            ph = np.exp(1j * (k[q] @ Rc.T))
            for j in np.where(~nz[q])[0]:
                Z.append(V[q][cs, j] * ph)
        nn = len(cs)
        if not Z:
            return np.zeros((nn, 0)), np.eye(nn), [], 0
        Z = np.array(Z).T
        Zr = np.hstack([Z.real, Z.imag])
        U, sv, _ = np.linalg.svd(Zr, full_matrices=False)
        r = int((sv > 1e-9 * sv.max()).sum())
        Wb = U[:, :r]
        ew, ev = np.linalg.eigh(np.eye(nn) - Wb @ Wb.T)
        Wp = ev[:, ew > 0.5]
        return Wb, Wp, (sv / sv.max()).tolist(), int(Z.shape[1])

    def schur_W(M, Qp):
        if Qp.shape[1] == 0:
            return np.zeros_like(M), None
        A = Qp.T @ M @ Qp
        A = 0.5 * (A + A.T)
        ew = np.linalg.eigvalsh(A)
        S = Qp @ np.linalg.inv(A) @ Qp.T
        return 0.5 * (S + S.T), float(ew.min() / ew.max())

    out = {'L': L, 'abc': list(abc), 'k_punkte': int(N), 'zahl_nullmoden': int((~nz).sum())}
    # V0, V1 (Realraumbloecke von Phi)
    P36, im36 = block(Phi, rot + tra)
    S0 = P36[:18, :18]
    Ptt = P36[18:, 18:]
    S1 = S0 - P36[:18, 18:] @ np.linalg.solve(Ptt, P36[18:, :18])
    out['phi_block_imag_max'] = im36
    out['phi_tt_eigen_min'] = float(np.linalg.eigvalsh(Ptt).min())
    # V3
    M18, im18 = block(Phip, rot)
    Wb, Wp, svW, nz18 = W_basis(rot)
    S3, kond3 = schur_W(M18, Wp)
    out['V3_dim_W'] = int(Wb.shape[1])
    out['V3_W_sv_rel'] = svW
    out['V3_kond'] = kond3
    out['M18_imag_max'] = im18
    # V2
    M36, im36p = block(Phip, rot + tra)
    Wb36, Wp36, svW36, _ = W_basis(rot + tra)
    S36, kond2 = schur_W(M36, Wp36)
    S2 = S36[:18, :18]
    out['V2_dim_W36'] = int(Wb36.shape[1])
    out['V2_kond'] = kond2
    out['S'] = {'V0': S0, 'V1': S1, 'V2': S2, 'V3': S3}
    return out, geo


def eich_dicht(L, abc):
    """Gegenprobe: Superzelle L dicht, verallgemeinertes Schur-Komplement von Phi = A^T A."""
    T, _ = ring(abc)
    Nz = L ** 3
    N = 12 * Nz

    def zelle(n):
        n = np.mod(n, L)
        return int((n[0] * L + n[1]) * L + n[2])

    A = np.zeros((N, N))
    for n in itertools.product(range(L), repeat=3):
        n = np.array(n)
        cu = zelle(n)
        for a_ in range(4):
            row = 12 * cu + 3 * a_
            cd = zelle(n - SL[a_])
            A[row:row + 3, 12 * cu:12 * cu + 3] += np.eye(3)
            A[row:row + 3, 12 * cu + 3:12 * cu + 6] += -XA[a_]
            A[row:row + 3, 12 * cd + 6:12 * cd + 9] += -np.eye(3)
            A[row:row + 3, 12 * cd + 9:12 * cd + 12] += -XA[a_]
    Phi = A.T @ A
    rot = [12 * zelle(T[i][0]) + 6 * T[i][1] + 3 + al for i in range(6) for al in range(3)]
    tra = [12 * zelle(T[i][0]) + 6 * T[i][1] + al for i in range(6) for al in range(3)]

    def schur(keep, frei):
        Pk = Phi[np.ix_(keep, keep)]
        if not frei:
            return Pk
        Pf = Phi[np.ix_(frei, frei)]
        Pkf = Phi[np.ix_(keep, frei)]
        S = Pk - Pkf @ np.linalg.pinv(Pf, rcond=1e-10, hermitian=True) @ Pkf.T
        return 0.5 * (S + S.T)

    alle = set(range(N))
    S0 = schur(rot, [])
    S1 = schur(rot, tra)
    S2 = schur(rot, sorted(alle - set(rot) - set(tra)))
    S3 = schur(rot, sorted(alle - set(rot)))
    return {'V0': S0, 'V1': S1, 'V2': S2, 'V3': S3}


def modus_eich(a):
    res = {'L_liste': a.L_liste, 'dicht_L': a.dicht, 'haupt': {}, 'gegen': {}}
    e_ref = None
    for L in a.L_liste:
        t0 = time.time()
        bd = bloch_daten(L)
        for abc, rn in (((1, 2, 3), 'haupt'), ((0, 1, 2), 'gegen')):
            t1 = time.time()
            out, geo = eich_bloch(bd, L, abc)
            S = out.pop('S')
            if e_ref is None and rn == 'haupt':
                e_ref = float(np.linalg.eigvalsh(S['V0']).max())
            var = {}
            for v in ('V0', 'V1', 'V2', 'V3'):
                var[v] = {'H+': eich_kennzahlen(S[v], geo, False), 'H-': eich_kennzahlen(S[v], geo, True),
                          'symmetrie': float(np.abs(S[v] - S[v].T).max())}
            out['varianten'] = var
            out['S_matrizen'] = {v: S[v].tolist() for v in S}
            out['laufzeit_s'] = time.time() - t1
            res[rn]['L%d' % L] = out
            if L == a.dicht:
                Sd = eich_dicht(L, abc)
                res[rn]['dicht_L%d' % L] = {v: {'max_abw': float(np.abs(Sd[v] - S[v]).max()),
                                               'skala': float(np.abs(Sd[v]).max()),
                                               'eigen_dicht': np.linalg.eigvalsh(Sd[v]).tolist()}
                                           for v in Sd}
        res['laufzeit_L%d_s' % L] = time.time() - t0
        del bd
    res['e_ref'] = e_ref
    return res


# ------------------------------------------------------------------------------------------- main
def main():
    p = argparse.ArgumentParser()
    p.add_argument('modus', choices=['kontrolle', 'rum', 'eich'])
    p.add_argument('--out', required=True)
    p.add_argument('--L', type=int, default=24)
    p.add_argument('--nzuf', type=int, default=20000)
    p.add_argument('--nebene', type=int, default=2000)
    p.add_argument('--nlinie', type=int, default=200)
    p.add_argument('--Lband', type=int, default=16)
    p.add_argument('--bild', default=None)
    p.add_argument('--L_liste', type=int, nargs='+', default=[8, 16, 24, 32])
    p.add_argument('--dicht', type=int, default=4)
    a = p.parse_args()
    t0 = time.time()
    if a.modus == 'kontrolle':
        res = modus_kontrolle(a)
    elif a.modus == 'rum':
        res = modus_rum(a)
    else:
        if a.dicht not in a.L_liste:
            a.L_liste = sorted(set(a.L_liste + [a.dicht]))
        res = modus_eich(a)
    res['laufinfo'] = {'modus': a.modus, 'argv': sys.argv, 'laufzeit_s': time.time() - t0,
                       'max_rss_mb': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
                       'python': platform.python_version(), 'numpy': np.__version__, 'host': platform.node(),
                       'zeit_utc': time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()),
                       'sha256_kt': sha(os.path.abspath(__file__)),
                       'sha256_tp': sha(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tp.py'))}
    with open(a.out, 'w') as f:
        json.dump(sauber(json.loads(json.dumps(res, default=jdef))), f, indent=1)
    print('fertig', a.modus, 'laufzeit %.1f s' % res['laufinfo']['laufzeit_s'],
          'rss %.0f MB' % res['laufinfo']['max_rss_mb'], flush=True)


if __name__ == '__main__':
    main()
