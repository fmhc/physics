#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TAKT-UMKLAPP-1 (Runde 47, fmhc-physics), Code-Agent fuer die Leitung claude-primary.

Teil A (HODGE-TAKT-1 aus HODGE-L, Abschnitt 7):
  Finns Takt-Operator P = -W^H B W (MATERIE-NETZ-1, mn.py) gegen c mal den umkreisbasierten Hodge-Laplace
  L1 = d0^H *1 d0 (Glickenstein), auf V, S, V_D, S_D, Glasnetzen (TT-GLAS-1) und UMKLAPP-1-Netzen nach zufaelligen
  2-3-Zuegen. Vorzeichen von *0, *1, *2 (umkreisbasiert, vorzeichenbehaftet wie Hirani/Kalyanaraman/VanderZee 2013).
  P positiv semidefinit an allen gerechneten k? Traegheitsidentitaet (Sylvester/Haynsworth):
  n_-(B) = n_+(P) + n_-(B_red), B_red = B auf dem Komplement von Bild[M, c] (wie tg.punkt).
Teil B (Zusatz Leitung): Ecken um a (Effektivwert a * mittlere Kantenlaenge) verschieben, in 10 Teilschritten nur
  Delaunay-wiederherstellende 2-3/3-2-Zuege (D-Arm, staerkste Verletzung zuerst); Vergleich: gleich viele zufaellige
  Zuege gleicher Typen auf dem Ausgangsnetz (Z-Arm, Volumenschwelle wie UMKLAPP-1). TT-Spektrum mit tg.spektrum
  (unveraendert), Kennzahlen mit tg_auswertung.netz_kennzahlen (unveraendert).
Unveraendert importiert: tg.py, tg_auswertung.py, tp.py (TT-GLAS-1), uk.py (UMKLAPP-1), ew.py (EINE-WELT-LOCH-1),
  mn.py (MATERIE-NETZ-1; nur W_of fuer die Gegenprobe der Bauweise von P).
"""
import argparse, json, os, sys, time, hashlib, platform, resource, glob
import numpy as np
import scipy
import scipy.sparse as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tg  # noqa: E402
import uk  # noqa: E402
import ew  # noqa: E402
import mn  # noqa: E402
import tg_auswertung as tga  # noqa: E402

TOL_MU = 1e-9          # Delaunay: mu < -TOL_MU = verletzt (wie UMKLAPP-1 Nachtrag V)
TOL_PSD = 1e-10        # P psd: lambda_min >= -TOL_PSD * max|lambda|
TOL_TR = 1e-9          # Vorzeichenzaehlung von B, P, B_red: |lambda| <= TOL_TR * max|lambda| = null (wie tg.punkt)
TOL_HT0 = 1e-10        # HT0: max|P - c L1| / max|P| <= 1e-10
SAAT_VERSCH, SAAT_ZUF, SAAT_K = 4540, 4541, 4542
A_LISTE = [1e-3, 1e-2]
TEILSCHRITTE = 10
PQR = [(0, 1, 2), (1, 2, 0), (2, 0, 1)]


def sha(p):
    with open(p, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


# ------------------------------------------------------------------------------------------------ Netze
def netz_aus_ew(fuellung):
    """Wie tg.netz_V, fuer jede Fuellung von ew.geometrie (V, S)."""
    pos8, zellen = ew.geometrie(fuellung)
    G, O = [], []
    for z in zellen:
        assert len(z['X8']) == 4 and z['kin']
        ids = [ew.zerlege(x, pos8) for x in z['X8']]
        G.append([s for (s, n) in ids])
        O.append([list(n) for (s, n) in ids])
    pos = np.array([np.asarray(p, float) / 8.0 for p in pos8])
    return np.array(ew.AV, float), pos, np.array(G, np.int64), np.array(O, np.int64), {}


def superzelle(LV, pos, G, O, n):
    """n x n x n Superzelle; Ecke (q, s) -> Index q nV + s, q = (i n + j) n + k."""
    nV = len(pos)
    zel = np.array([(i, j, k) for i in range(n) for j in range(n) for k in range(n)], np.int64)
    pos2 = np.concatenate([pos + m.astype(float) @ LV for m in zel])
    G2, O2 = [], []
    for m in zel:
        A = m[None, None, :] + O
        Q = np.mod(A, n)
        F = np.floor_divide(A, n)
        qi = (Q[..., 0] * n + Q[..., 1]) * n + Q[..., 2]
        G2.append(qi * nV + G)
        O2.append(F)
    return n * LV, pos2, np.concatenate(G2).astype(np.int64), np.concatenate(O2).astype(np.int64), {}


# ------------------------------------------------------------------------------------------------ Geometrie
def einheit(v):
    return v / np.linalg.norm(v, axis=-1)[..., None]


def umkreis_tet(X):
    Y = X - X[:, :1]
    A = 2.0 * Y[:, 1:]
    b = (Y[:, 1:] ** 2).sum(-1)
    return X[:, 0] + np.linalg.solve(A, b[..., None])[..., 0]


def umkreis_drei(P0, P1, P2):
    a, b = P0 - P2, P1 - P2
    axb = np.cross(a, b)
    num = np.cross((a * a).sum(-1)[..., None] * b - (b * b).sum(-1)[..., None] * a, axb)
    return P2 + num / (2.0 * (axb * axb).sum(-1))[..., None]


def tet_X(LV, pos, G, O):
    return pos[G] + np.einsum('tai,ij->taj', O.astype(float), LV)


def hodge(LV, pos, G, O, mod):
    """Umkreisbasierte, vorzeichenbehaftete Hodge-Sterne. *1 je Kante (Reihenfolge wie mod), *2 je Flaeche
    (uk.flaechen), *0 je Ecke; Kontrollen sum l A* = 3 V, sum *0 = V, sum |f| L* = 3 V."""
    X = tet_X(LV, pos, G, O)
    T = len(X)
    ct = umkreis_tet(X)
    Ast = np.zeros((T, 6))
    lt = np.zeros((T, 6))
    for p, (i, j, k, l) in enumerate(tg.PAARE):
        Xi, Xj, Xk, Xl = X[:, i], X[:, j], X[:, k], X[:, l]
        m = 0.5 * (Xi + Xj)
        e = einheit(Xj - Xi)
        hs, hh = [], []
        for Xo, Xa in ((Xk, Xl), (Xl, Xk)):
            u = (Xo - Xi) - ((Xo - Xi) * e).sum(-1)[:, None] * e
            u = einheit(u)
            cf = umkreis_drei(Xi, Xj, Xo)
            hs.append(((cf - m) * u).sum(-1))                      # Kantenmitte -> Flaechenumkreismitte, + zur Ecke Xo
            nrm = np.cross(Xj - Xi, Xo - Xi)
            nrm = einheit(nrm * np.sign((nrm * (Xa - Xi)).sum(-1))[:, None])
            hh.append(((ct - cf) * nrm).sum(-1))                   # Flaechenumkreismitte -> Umkugelmitte, + zur Ecke Xa
        Ast[:, p] = 0.5 * (hs[0] * hh[0] + hs[1] * hh[1])
        lt[:, p] = np.linalg.norm(Xj - Xi, axis=1)
    E, nV = mod['E'], mod['nV']
    A1 = np.bincount(mod['eidx'].ravel(), Ast.ravel(), E)
    s1 = A1 / mod['l']
    s0 = np.zeros(nV)
    for p, (i, j, k, l) in enumerate(tg.PAARE):
        w = lt[:, p] * Ast[:, p] / 6.0
        s0 += np.bincount(G[:, i], w, nV) + np.bincount(G[:, j], w, nV)
    hf = np.zeros((T, 4))
    af = np.zeros((T, 4))
    for i in range(4):
        a_, b_, c_ = [X[:, q] for q in uk.FL[i]]
        cf = umkreis_drei(a_, b_, c_)
        nrm = np.cross(b_ - a_, c_ - a_)
        af[:, i] = 0.5 * np.linalg.norm(nrm, axis=1)
        nrm = einheit(nrm * np.sign((nrm * (X[:, i] - a_)).sum(-1))[:, None])
        hf[:, i] = ((ct - cf) * nrm).sum(-1)
    fl = uk.flaechen(G, O)
    L2 = hf[fl['t1'], fl['i1']] + hf[fl['t2'], fl['i2']]
    fa = af[fl['t1'], fl['i1']]
    s2 = L2 / fa
    vol = np.abs(uk.vol6(X[:, 0], X[:, 1], X[:, 2], X[:, 3])) / 6.0
    Vt = float(vol.sum())
    mu = uk.raender(LV, pos, G, O, fl)
    s1n = float(np.abs(s1).max())
    s2n = float(np.abs(s2).max())
    w = np.abs(mu) > TOL_MU
    out = {'E': int(E), 'F': int(fl['F']), 'nV': int(nV), 'T': int(T),
           'stern1_min': float(s1.min()), 'stern1_max': float(s1.max()), 'stern1_n_neg': int((s1 < -1e-12 * s1n).sum()),
           'stern1_n_null': int((np.abs(s1) <= 1e-12 * s1n).sum()),
           'stern2_min': float(s2.min()), 'stern2_max': float(s2.max()), 'stern2_n_neg': int((s2 < -1e-12 * s2n).sum()),
           'stern2_n_null': int((np.abs(s2) <= 1e-12 * s2n).sum()),
           'stern0_min': float(s0.min()), 'stern0_n_neg': int((s0 < 0).sum()),
           'stern1_neg_werte': sorted(set(round(float(x), 9) for x in s1[s1 < -1e-12 * s1n]))[:12],
           'stern2_neg_werte': sorted(set(round(float(x), 9) for x in s2[s2 < -1e-12 * s2n]))[:12],
           'mu_min': float(mu.min()), 'mu_n_verletzt': int((mu < -TOL_MU).sum()), 'mu_n_kugel': int((~w).sum()),
           'mu_gegen_stern2_widerspruch': int(np.sum(w & (np.sign(mu) != np.sign(s2)))),
           'kontrolle': {'sum_lA_durch_3V': float((mod['l'] * A1).sum() / (3 * Vt)), 'sum_s0_durch_V': float(s0.sum() / Vt),
                         'sum_fL_durch_3V': float((fa * L2).sum() / (3 * Vt)), 'V': Vt,
                         'Vbox': float(abs(np.linalg.det(LV)))}}
    return out, s1, s2, Ast


# ------------------------------------------------------------------------------------------------ Takt-Operator
def takt_mats(mod, k, s1):
    """P = -W^H B W (W wie tg.ops / mn.W_of: a_e = phi_s + e^{ik.T_e} phi_s2) und L1 = d0^H *1 d0."""
    E, nV = mod['E'], mod['nV']
    B, _ = tg.ops_BA(mod, k)
    phe = np.exp(1j * (mod['Tedge'] @ k))
    rr = np.arange(E)
    rows = np.concatenate([rr, rr])
    cols = np.concatenate([mod['es'], mod['es2']])
    W = sp.coo_matrix((np.concatenate([np.ones(E), phe]), (rows, cols)), shape=(E, nV)).tocsr()
    D0 = sp.coo_matrix((np.concatenate([-np.ones(E), phe]), (rows, cols)), shape=(E, nV)).tocsr()
    P = -(W.conj().T @ (B @ W)).toarray()
    P = 0.5 * (P + P.conj().T)
    L1 = (D0.conj().T @ sp.diags(s1) @ D0).toarray()
    L1 = 0.5 * (L1 + L1.conj().T)
    return P, L1


def k_satz(LV, n_gitter, n_zuf, saat):
    rez = 2 * np.pi * np.linalg.inv(LV).T
    ks = [('klein-%s-1' % nm, tg.EPS1 * d) for nm, d in tg.richtungen13w()]
    ks += [('klein-%s-2' % nm, tg.EPS2 * d) for nm, d in tg.richtungen13w() if nm in tg.TT_RICHT]
    g = np.arange(n_gitter)
    mm = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1).reshape(-1, 3)
    ks += [('gitter-%d-%d-%d' % tuple(m), (m / n_gitter) @ rez) for m in mm]
    rng = np.random.default_rng([SAAT_K, int(saat)])
    ks += [('zufall-%d' % q, rng.uniform(0.0, 1.0, 3) @ rez) for q in range(n_zuf)]
    return ks


def takt(mod, s1, ks, eigen_speichern=False):
    cs, rows = [], []
    for nm, k in ks:
        P, L1 = takt_mats(mod, k, s1)
        nL = np.vdot(L1, L1).real
        c = float(np.vdot(L1, P).real / nL) if nL > 0 else float('nan')
        eP = np.linalg.eigvalsh(P)
        sP = float(np.abs(eP).max())
        z = {'k': nm, 'c': c, 'P_lmin': float(eP[0]), 'P_lmax': float(eP[-1]), 'P_lmin_rel': float(eP[0] / sP) if sP > 0 else 0.0,
             'P_n_neg': int((eP < -TOL_PSD * sP).sum())}
        if eigen_speichern:
            z['eP'] = eP.tolist()
            z['eL1'] = np.linalg.eigvalsh(L1).tolist()
        rows.append((z, P, L1))
        cs.append(c)
    cs = np.array(cs)
    c_med = float(np.nanmedian(cs))
    rest = []
    for z, P, L1 in rows:
        sP = np.abs(P).max()
        z['rest_cmed'] = float(np.abs(P - c_med * L1).max() / sP) if sP > 0 else 0.0
        z['rest_ck'] = float(np.abs(P - z['c'] * L1).max() / sP) if sP > 0 else 0.0
        rest.append(z['rest_cmed'])
    zeilen = [z for z, _, _ in rows]
    return {'n_k': len(ks), 'c_median': c_med, 'c_min': float(np.nanmin(cs)), 'c_max': float(np.nanmax(cs)),
            'rest_max': float(max(rest)), 'P_psd_alle': bool(all(z['P_n_neg'] == 0 for z in zeilen)),
            'P_lmin_rel_min': float(min(z['P_lmin_rel'] for z in zeilen)), 'P_n_neg_max': int(max(z['P_n_neg'] for z in zeilen)),
            'k_mit_P_neg': [z['k'] for z in zeilen if z['P_n_neg'] > 0][:20], 'zeilen': zeilen}


def takt_je_tet(mod, Ast):
    """Je Tetraeder bei k = 0: P_t = -W_t^T (l D l)_t W_t gegen L_t = d0_t^T diag(A*_t / l_t) d0_t (4 x 4)."""
    T = mod['T']
    Wt = np.zeros((6, 4))
    Dt = np.zeros((6, 4))
    for p, (i, j, _, _) in enumerate(tg.PAARE):
        Wt[p, i] = Wt[p, j] = 1.0
        Dt[p, i], Dt[p, j] = -1.0, 1.0
    lt = mod['l'][mod['eidx']]
    Pt = -np.einsum('pa,tpq,qb->tab', Wt, mod['Dl'], Wt)
    Lt = np.einsum('pa,tp,pb->tab', Dt, Ast / lt, Dt)
    c = float((Pt * Lt).sum() / (Lt * Lt).sum())
    rest = np.abs(Pt - c * Lt).max(axis=(1, 2)) / np.abs(Pt).max(axis=(1, 2))
    return {'T': int(T), 'c': c, 'rest_max': float(rest.max()), 'rest_median': float(np.median(rest))}


def traegheit(mod, k):
    """Sylvester/Haynsworth: n_-(B) = n_+(P) + n_-(B_red), wenn P nicht entartet; B_red wie tg.punkt."""
    t0 = time.time()
    B, A, M, c = tg.ops(mod, k)
    Bd = B.toarray()
    Bd = 0.5 * (Bd + Bd.conj().T)
    eB = np.linalg.eigvalsh(Bd)
    sB = np.abs(eB).max()
    nul = np.abs(eB) <= TOL_TR * sB
    E, nV = mod['E'], mod['nV']
    phe = np.exp(1j * (mod['Tedge'] @ k))
    rr = np.arange(E)
    W = np.zeros((E, nV), complex)
    np.add.at(W, (rr, mod['es']), 1.0)
    np.add.at(W, (rr, mod['es2']), phe)
    P = -(W.conj().T @ (Bd @ W))
    P = 0.5 * (P + P.conj().T)
    eP = np.linalg.eigvalsh(P)
    sP = np.abs(eP).max()
    X = np.concatenate([M, c], 1)
    nX = X.shape[1]
    Q, R = np.linalg.qr(X, mode='complete')
    sv = np.linalg.svd(R[:nX], compute_uv=False)
    r = int((sv > 1e-9 * sv.max()).sum())
    if r < nX:
        U, s_, _ = np.linalg.svd(X)
        r = int((s_ > 1e-9 * s_.max()).sum())
        S = U[:, r:]
    else:
        S = Q[:, nX:]
    Br = S.conj().T @ (Bd @ S)
    Br = 0.5 * (Br + Br.conj().T)
    eBr = np.linalg.eigvalsh(Br)
    sBr = np.abs(eBr).max()
    z = {'n_B_neg': int((eB < -TOL_TR * sB).sum()), 'n_B_null': int(nul.sum()), 'n_B_pos': int((eB > TOL_TR * sB).sum()),
         'B_null_groesst_rel': float(np.abs(eB[nul]).max() / sB) if nul.any() else None,
         'B_nichtnull_kleinst_rel': float(np.abs(eB[~nul]).min() / sB),
         'n_P_neg': int((eP < -TOL_TR * sP).sum()), 'n_P_null': int((np.abs(eP) <= TOL_TR * sP).sum()),
         'n_P_pos': int((eP > TOL_TR * sP).sum()), 'P_lmin_rel': float(eP[0] / sP),
         'n_Bred_neg': int((eBr < -TOL_TR * sBr).sum()), 'dim_red': int(S.shape[1]), 'rang_Mc': r, 'nX': int(nX), 'nV': int(nV),
         'E': int(E), 't_s': time.time() - t0}
    z['identitaet'] = (z['n_B_neg'] == z['n_P_pos'] + z['n_Bred_neg']) if z['n_P_null'] == 0 else None
    z['ueberschuss'] = z['n_Bred_neg'] - (z['n_B_neg'] - nV)
    return z


def p_mn_gegen_tg(fuellung, mod, ks):
    """Gegenprobe der Bauweise: P aus ew.ops + mn.W_of (MATERIE-NETZ-1) gegen P aus tg.ops_BA + W (gleiche Ecken)."""
    me = ew.baue(fuellung)
    kk = np.array([k for _, k in ks])
    o = ew.ops(me, kk)
    Wm = mn.W_of(me, kk)
    Pm = -mn.cT(Wm) @ o['B'] @ Wm
    Pm = 0.5 * (Pm + mn.cT(Pm))
    d = []
    for j, (nm, k) in enumerate(ks):
        P, _ = takt_mats(mod, k, np.ones(mod['E']))
        d.append(float(np.abs(Pm[j] - P).max() / np.abs(Pm[j]).max()))
    return {'E_ew': int(me['E']), 'nV_ew': int(me['nV']), 'abw_max': float(max(d)), 'n_k': len(ks)}, Pm


# ------------------------------------------------------------------------------------------------ Zuege
def tet_dict(G, O):
    K = uk.tetra_schluessel(G, O)
    return {tuple(r): t for t, r in enumerate(K.tolist())}


def zentriere(LV, pos, Gn, On):
    cen = uk.absolut(LV, pos, Gn, On).mean(1)
    return On - np.floor(cen @ np.linalg.inv(LV)).astype(np.int64)[:, None, :]


def flaechen_geo(LV, pos, G, O):
    fl = uk.flaechen(G, O)
    t1, i1, t2, i2, sh = fl['t1'], fl['i1'], fl['t2'], fl['i2'], fl['sh']
    fv = G[t1[:, None], uk.FL[i1]]
    fo = O[t1[:, None], uk.FL[i1]]
    dv, do = G[t1, i1], O[t1, i1]
    ev, eo = G[t2, i2], O[t2, i2] + sh

    def P(v, o):
        return pos[v] + o.astype(float) @ LV
    Xf = [P(fv[:, q], fo[:, q]) for q in range(3)]
    D_, E_ = P(dv, do), P(ev, eo)
    v = np.stack([uk.vol6(Xf[0], Xf[1], D_, E_), uk.vol6(Xf[1], Xf[2], D_, E_), uk.vol6(Xf[2], Xf[0], D_, E_)], 1) / 6.0
    return fl, {'fv': fv, 'fo': fo, 'dv': dv, 'do': do, 'ev': ev, 'eo': eo, 'v': v}


def ungerade(v):
    """Index der einen Flaechenkante, hinter der die Gerade d-e die Flaechenebene trifft (genau ein Vorzeichen anders)."""
    s = np.sign(v)
    if np.any(s == 0) or abs(s.sum()) != 1:
        return None
    return int(np.nonzero(s != np.sign(s.sum()))[0][0])


def zug32_vorbereiten(LV, pos, G, O, fl, geo, j, r, tdict, vmin, vrel_summe=1e-9):
    p, q, s = PQR[r]
    fv, fo = geo['fv'][j], geo['fo'][j]
    Pv, Po, Qv, Qo, Rv, Ro = fv[p], fo[p], fv[q], fo[q], fv[s], fo[s]
    Dv, Do, Ev, Eo = geo['dv'][j], geo['do'][j], geo['ev'][j], geo['eo'][j]
    if Dv == Ev:
        return None
    key3 = tuple(uk.tetra_schluessel(np.array([[Pv, Qv, Dv, Ev]]), np.array([[Po, Qo, Do, Eo]]))[0].tolist())
    t3 = tdict.get(key3)
    t1, t2 = int(fl['t1'][j]), int(fl['t2'][j])
    if t3 is None or t3 in (t1, t2):
        return None
    Gn = np.array([[Pv, Rv, Dv, Ev], [Qv, Rv, Dv, Ev]], np.int64)
    On = np.array([[Po, Ro, Do, Eo], [Qo, Ro, Do, Eo]], np.int64)
    vn = uk.tet_vol(LV, pos, Gn, On)
    va = float(uk.tet_vol(LV, pos, G[[t1, t2, t3]], O[[t1, t2, t3]]).sum())
    if abs(vn.sum() - va) > vrel_summe * va or vn.min() < vmin:
        return None
    ek = int(uk.kanten_schluessel(np.array([Pv]), np.array([Po]), np.array([Qv]), np.array([Qo]), len(pos))[0])
    return {'t': (t1, t2, t3), 'Gn': Gn, 'On': On, 'kante': ek}


def zug32(LV, pos, G, O, info):
    keep = np.ones(len(G), bool)
    keep[list(info['t'])] = False
    On = zentriere(LV, pos, info['Gn'], info['On'])
    return np.concatenate([G[keep], info['Gn']]), np.concatenate([O[keep], On])


def zug23_ok(LV, pos, G, O, geo, j, kmenge, vmin):
    v = geo['v'][j]
    if not ((v > 0).all() or (v < 0).all()) or np.abs(v).min() < vmin:
        return False
    if geo['dv'][j] == geo['ev'][j]:
        return False
    ek = int(uk.kanten_schluessel(np.array([geo['dv'][j]]), np.array([geo['do'][j]]), np.array([geo['ev'][j]]),
                                  np.array([geo['eo'][j]]), len(pos))[0])
    return ek not in kmenge


def reparatur(LV, pos, G, O, maxit=5000):
    """Delaunay-Wiederherstellung durch Zuege: verletzte Flaechen (mu < -TOL_MU), staerkste zuerst; 2-3 wenn die
    Doppelpyramide konvex ist, 3-2 wenn d-e hinter genau einer Kante liegt und diese Kante Grad 3 hat."""
    nV = len(pos)
    vbar = float(uk.tet_vol(LV, pos, G, O).mean())
    vmin = 1e-10 * vbar
    n23 = n32 = 0
    for it in range(maxit):
        fl, geo = flaechen_geo(LV, pos, G, O)
        mu = uk.raender(LV, pos, G, O, fl)
        verl = np.nonzero(mu < -TOL_MU)[0]
        if len(verl) == 0:
            return G, O, {'n23': n23, 'n32': n32, 'ok': True, 'stecken': False}
        verl = verl[np.argsort(mu[verl])]
        kmenge = set(uk.kanten(LV, pos, G, O, nV)[0].tolist())
        tdict = None
        gemacht = False
        for j in verl:
            if zug23_ok(LV, pos, G, O, geo, j, kmenge, vmin):
                G, O = uk.zug23(LV, pos, G, O, fl, j)
                n23 += 1
                gemacht = True
                break
            r = ungerade(geo['v'][j])
            if r is not None:
                if tdict is None:
                    tdict = tet_dict(G, O)
                info = zug32_vorbereiten(LV, pos, G, O, fl, geo, j, r, tdict, vmin)
                if info is not None:
                    G, O = zug32(LV, pos, G, O, info)
                    n32 += 1
                    gemacht = True
                    break
        if not gemacht:
            return G, O, {'n23': n23, 'n32': n32, 'ok': False, 'stecken': True, 'n_verletzt': int(len(verl)),
                          'mu_min': float(mu.min())}
    return G, O, {'n23': n23, 'n32': n32, 'ok': False, 'stecken': False, 'maxit': True}


def vorzeichen_vol(LV, pos, G, O):
    X = tet_X(LV, pos, G, O)
    return np.sign(uk.vol6(X[:, 0], X[:, 1], X[:, 2], X[:, 3]))


def kinetisch(LV, pos0, delta, G, O, S=TEILSCHRITTE):
    st = {'n23': 0, 'n32': 0, 'teilschritte': S, 'invertiert': 0, 'stecken': 0, 'je_schritt': []}
    pos_alt = pos0
    for s in range(1, S + 1):
        pos = pos0 + delta * (s / S)
        st['invertiert'] += int(np.sum(vorzeichen_vol(LV, pos_alt, G, O) != vorzeichen_vol(LV, pos, G, O)))
        G, O, r = reparatur(LV, pos, G, O)
        st['n23'] += r['n23']
        st['n32'] += r['n32']
        st['stecken'] += int(not r['ok'])
        st['je_schritt'].append([r['n23'], r['n32'], bool(r['ok'])])
        pos_alt = pos
    return G, O, st


def kandidaten32(LV, pos, G, O, vmin):
    fl, geo = flaechen_geo(LV, pos, G, O)
    tdict = tet_dict(G, O)
    out, seen = [], set()
    for j in range(fl['F']):
        r = ungerade(geo['v'][j])
        if r is None:
            continue
        info = zug32_vorbereiten(LV, pos, G, O, fl, geo, j, r, tdict, vmin, vrel_summe=1e-9)
        if info is None or info['kante'] in seen:
            continue
        seen.add(info['kante'])
        out.append(info)
    return out


def zufall_arm(LV, pos, G, O, n23, n32, rng):
    """Gleich viele zufaellige Zuege gleicher Typen (Reihenfolge der Typen zufaellig); je Schritt gleichverteilt unter den
    erlaubten Zuegen des Typs (2-3: uk.kandidaten, Volumenschwelle 1e-3 des Mittels; 3-2: Kante Grad 3, konvex, gleiche
    Schwelle)."""
    nV = len(pos)
    vbar = float(uk.tet_vol(LV, pos, G, O).mean())
    vmin = uk.VMIN_REL * vbar
    typen = np.array([23] * n23 + [32] * n32, int)
    rng.shuffle(typen)
    st = {'n23': 0, 'n32': 0, 'fehl23': 0, 'fehl32': 0, 'kand23_start': None, 'kand32_start': None}
    for typ in typen:
        if typ == 23:
            k = uk.kandidaten(LV, pos, G, O, nV, vmin)
            idx = np.nonzero(k['ok'])[0]
            if st['kand23_start'] is None:
                st['kand23_start'] = int(len(idx))
            if len(idx) == 0:
                st['fehl23'] += 1
                continue
            G, O = uk.zug23(LV, pos, G, O, k['fl'], idx[rng.integers(len(idx))])
            st['n23'] += 1
        else:
            c = kandidaten32(LV, pos, G, O, vmin)
            if st['kand32_start'] is None:
                st['kand32_start'] = int(len(c))
            if not c:
                st['fehl32'] += 1
                continue
            G, O = zug32(LV, pos, G, O, c[rng.integers(len(c))])
            st['n32'] += 1
    return G, O, st


# ------------------------------------------------------------------------------------------------ Teil A
def netz_bauen(name):
    """V, S, VD, SD, glas-N128-s3, uk-N128-s1-f0.2 (UMKLAPP-1-Zugfolge, unveraendert)."""
    info = {'name': name}
    if name in ('V', 'S'):
        LV, pos, G, O, pr = tg.netz_V() if name == 'V' else netz_aus_ew('S')
        if name == 'V':
            L2, p2, G2, O2, _ = netz_aus_ew('V')
            info['gleich_tg_netz_V'] = bool(np.array_equal(G, G2) and np.array_equal(O, O2) and np.allclose(pos, p2))
    elif name in ('VD', 'SD'):
        LV, pos, G, O, pr = tg.netz_V() if name == 'VD' else netz_aus_ew('S')
        G, O, st = reparatur(LV, pos, G, O)
        info['reparatur'] = st
    elif name.startswith('glas-'):
        _, nN, ns = name.split('-')
        LV, pos, G, O, pr = tg.zufallsnetz(int(nN[1:]), int(ns[1:]))
    elif name.startswith('uk-'):
        _, nN, ns, nf = name.split('-')
        N, saat, f = int(nN[1:]), int(ns[1:]), float(nf[1:])
        LV, pos, G, O, pr = tg.zufallsnetz(N, saat)
        zust, st = uk.zugfolge(LV, pos, G, O, len(pos), [f], np.random.default_rng([uk.SAAT_ZUG, N, saat]))
        _, G, O, sf = zust[-1]
        info['zuege'] = {k: sf[k] for k in ('n_ziel', 'n_zuege', 'f_eff', 'T')}
    else:
        raise ValueError(name)
    return LV, pos, G, O, pr, info


def teil_a(name, rauch=False):
    t0 = time.time()
    LV, pos, G, O, pr, info = netz_bauen(name)
    mod = tg.modell(LV, pos, G, O, pr)
    h, s1, s2, Ast = hodge(LV, pos, G, O, mod)
    zelle = name in ('V', 'S', 'VD', 'SD')
    ks = k_satz(LV, 6 if zelle else 4, 20, 1 if zelle else 2)
    tk = takt(mod, s1, ks, eigen_speichern=zelle)
    z = {'netz': info, 'pruefung': mod['pruefung'], 'hodge': h, 'takt_je_tet': takt_je_tet(mod, Ast)}
    z['takt'] = {k: v for k, v in tk.items() if k != 'zeilen'}
    z['takt_zeilen'] = tk['zeilen'] if zelle else [{kk: r[kk] for kk in ('k', 'c', 'P_lmin_rel', 'P_n_neg', 'rest_cmed')} for r in tk['zeilen']]
    if name in ('V', 'S'):
        gp, _ = p_mn_gegen_tg(name, mod, ks)
        z['P_mn_gegen_tg'] = gp
    if zelle:
        hk = [(nm, k) for nm, k in ks if np.linalg.norm(k) > 0]
    else:
        nk = 2 if mod['nV'] > 200 else 3
        hk = [ks[0]] + [x for x in ks if x[0].startswith('zufall-')][:nk - 1]
    if rauch:
        hk = hk[:1]
    z['traegheit'] = []
    for nm, k in hk:
        tr = traegheit(mod, k)
        tr['k'] = nm
        z['traegheit'].append(tr)
    z['t_s'] = time.time() - t0
    return z


# ------------------------------------------------------------------------------------------------ Teil B
def basisnetz_b(name):
    if name.startswith('glas-'):
        _, nN, ns = name.split('-')
        N, saat = int(nN[1:]), int(ns[1:])
        LV, pos, G, O, pr = tg.zufallsnetz(N, saat)
        return LV, pos, G, O, pr, [N, saat]
    if name == 'V2':
        LV1, pos1, G1, O1, _ = tg.netz_V()
        LV, pos, G, O, pr = superzelle(LV1, pos1, G1, O1, 2)
        return LV, pos, G, O, {}, [0, 2]
    raise ValueError(name)


def arm_auswerten(LV, pos, G, O, pr, ridx, rauch):
    t0 = time.time()
    mod = tg.modell(LV, pos, G, O, pr)
    h, s1, s2, Ast = hodge(LV, pos, G, O, mod)
    ks = k_satz(LV, 0, 8, 3)
    tk = takt(mod, s1, ks)
    z = {'pruefung': mod['pruefung'], 'hodge': h, 'takt': {k: v for k, v in tk.items() if k != 'zeilen'}}
    tr = traegheit(mod, ks[0][1])
    tr['k'] = ks[0][0]
    z['traegheit'] = tr
    z['spektrum'] = tg.spektrum(mod, ridx)
    if sorted(ridx) == list(range(13)):
        z['kennzahlen'] = tga.netz_kennzahlen(z['spektrum'])
    z['t_s'] = time.time() - t0
    return z


def teil_b(name, ridx, rauch=False, a_liste=A_LISTE):
    t0 = time.time()
    LV, pos0, G0, O0, pr, nid = basisnetz_b(name)
    nV = len(pos0)
    lbar = float(uk.kanten(LV, pos0, G0, O0, nV)[2].mean())
    xi = np.random.default_rng([SAAT_VERSCH] + nid).normal(size=(nV, 3))
    out = {'netz': name, 'nid': nid, 'nV': nV, 'T0': int(len(G0)), 'lbar': lbar, 'faelle': []}
    for ia, a in enumerate(a_liste):
        fa = {'a': a}
        delta = xi * (a * lbar / np.sqrt(3.0))
        GD, OD, stD = kinetisch(LV, pos0, delta, G0.copy(), O0.copy())
        posD = pos0 + delta
        k0 = set(map(tuple, uk.tetra_schluessel(G0, O0).tolist()))
        kD = uk.tetra_schluessel(GD, OD)
        kDl = list(map(tuple, kD.tolist()))
        KD = set(kDl)
        rem = np.array([i for i, t in enumerate(map(tuple, uk.tetra_schluessel(G0, O0).tolist())) if t not in KD], np.int64)
        add = np.array([i for i, t in enumerate(kDl) if t not in k0], np.int64)
        if len(rem) or len(add):
            stD['netto'] = uk.cluster(G0[rem], O0[rem], GD[add] if len(add) else GD[:0], OD[add] if len(add) else OD[:0])
        else:
            stD['netto'] = {'n_cluster': 0, 'n_23': 0, 'n_32': 0, 'n_sonst': 0, 'typen': {}}
        stD['n_weg'], stD['n_neu'] = int(len(rem)), int(len(add))
        if np.allclose(LV, LV[0, 0] * np.eye(3)):
            Gs, Os, v = uk.delaunay_periodisch(posD, float(LV[0, 0]))
            stD['gleich_scipy'] = bool(set(map(tuple, uk.tetra_schluessel(Gs, Os).tolist())) == KD)
            stD['scipy_saum_verletzt'] = int(v)
        fa['D_zuege'] = stD
        rngz = np.random.default_rng([SAAT_ZUF] + nid + [ia])
        GZ, OZ, stZ = zufall_arm(LV, pos0, G0.copy(), O0.copy(), stD['n23'], stD['n32'], rngz)
        fa['Z_zuege'] = stZ
        fa['D'] = arm_auswerten(LV, posD, GD, OD, pr, ridx, rauch)
        fa['Z'] = arm_auswerten(LV, pos0, GZ, OZ, pr, ridx, rauch)
        out['faelle'].append(fa)
        print('teilB', name, 'a=%g' % a, 'D %d/%d' % (stD['n23'], stD['n32']), '%.1f s' % (time.time() - t0), flush=True)
    out['t_s'] = time.time() - t0
    return out


# ------------------------------------------------------------------------------------------------ Auswertung
def urteil(b):
    return 'eingetroffen' if b else 'verfehlt'


def auswertung(ordner):
    A, B = {}, {}
    ein = {}
    for p in sorted(glob.glob(os.path.join(ordner, 'teilA-*.json'))):
        d = json.load(open(p))
        ein[os.path.basename(p)] = sha(p)
        for z in d['ergebnis']:
            A[z['netz']['name']] = z
    for p in sorted(glob.glob(os.path.join(ordner, 'teilB-*.json'))):
        d = json.load(open(p))
        ein[os.path.basename(p)] = sha(p)
        for z in d['ergebnis']:
            B[z['netz']] = z
    res = {'eingaben_sha256': ein, 'netze_A': sorted(A), 'netze_B': sorted(B), 'urteile': {}}
    U = res['urteile']
    # ---- HT0
    if 'V' in A and 'S' in A:
        cV, cS = A['V']['takt']['c_median'], A['S']['takt']['c_median']
        rV, rS = A['V']['takt']['rest_max'], A['S']['takt']['rest_max']
        cvar = max(abs(A[n]['takt'][q] / A[n]['takt']['c_median'] - 1) for n in ('V', 'S') for q in ('c_min', 'c_max'))
        gp = max(A[n]['P_mn_gegen_tg']['abw_max'] for n in ('V', 'S'))
        wort = (rV <= TOL_HT0) and (rS <= TOL_HT0)
        plan = wort and abs(cV / cS - 1) <= TOL_HT0 and cvar <= TOL_HT0 and gp <= TOL_HT0
        U['HT0'] = {'wortlaut': urteil(wort), 'plan': urteil(plan), 'c_V': cV, 'c_S': cS, 'c_V_durch_c_S_minus_1': cV / cS - 1,
                    'rest_max_V': rV, 'rest_max_S': rS, 'c_streuung_rel_max': cvar, 'P_mn_gegen_tg_abw_max': gp,
                    'n_k_V': A['V']['takt']['n_k'], 'n_k_S': A['S']['takt']['n_k']}
    else:
        U['HT0'] = {'wortlaut': 'nicht entscheidbar', 'plan': 'nicht entscheidbar'}
    # ---- HT1'
    if 'V' in A and 'VD' in A:
        hV, hD = A['V']['hodge'], A['VD']['hodge']
        nzel = A['VD']['netz']['reparatur']
        a_ = hV['stern2_n_neg'] > 0
        b_ = hV['stern1_n_neg'] == 0 and hV['stern1_n_null'] == 0
        c_ = hD['stern2_n_neg'] == 0 and hD['stern2_n_null'] == 0 and hD['mu_n_verletzt'] == 0
        d_ = nzel['ok'] and nzel['n23'] == 12 and nzel['n32'] == 0
        U["HT1'"] = {'wortlaut': urteil(a_ and b_ and c_), 'plan': urteil(a_ and b_ and c_ and d_),
                     'V_stern2_neg': hV['stern2_n_neg'], 'V_stern1_neg': hV['stern1_n_neg'], 'V_stern1_min': hV['stern1_min'],
                     'VD_stern2_neg': hD['stern2_n_neg'], 'VD_stern2_min': hD['stern2_min'], 'VD_mu_verletzt': hD['mu_n_verletzt'],
                     'VD_zuege': nzel, 'S': {k: A['S']['hodge'][k] for k in ('stern1_n_neg', 'stern2_n_neg', 'mu_n_verletzt', 'stern1_min', 'stern2_min')} if 'S' in A else None}
    else:
        U["HT1'"] = {'wortlaut': 'nicht entscheidbar', 'plan': 'nicht entscheidbar'}
    # ---- HT2
    f02 = [n for n in A if n.startswith('uk-') and n.endswith('-f0.2')]
    if f02:
        neg = {n: A[n]['hodge']['stern2_n_neg'] for n in f02}
        psd = {n: A[n]['takt']['P_psd_alle'] for n in f02}
        wort = any(v > 0 for v in neg.values()) and all(psd.values())
        plan = all(v > 0 for v in neg.values()) and all(psd.values())
        U['HT2'] = {'wortlaut': urteil(wort), 'plan': urteil(plan), 'netze': sorted(f02), 'stern2_neg': neg, 'P_psd': psd,
                    'P_lmin_rel_min': {n: A[n]['takt']['P_lmin_rel_min'] for n in f02},
                    'stern1_neg': {n: A[n]['hodge']['stern1_n_neg'] for n in f02},
                    'vermerk': None if len(f02) == 7 else 'nur %d von 7 Netzen' % len(f02)}
    else:
        U['HT2'] = {'wortlaut': 'nicht entscheidbar', 'plan': 'nicht entscheidbar'}
    # ---- HT3
    pts = []
    for n, z in A.items():
        for t in z['traegheit']:
            pts.append((n, t))
    for n, z in B.items():
        for fa in z['faelle']:
            for arm in ('D', 'Z'):
                pts.append(('%s-a%g-%s' % (n, fa['a'], arm), fa[arm]['traegheit']))
    gueltig = [(n, t) for n, t in pts if t['identitaet'] is not None]
    ident = all(t['identitaet'] for n, t in gueltig)
    praem = [(n, t) for n, t in gueltig if t['n_P_neg'] > 0]
    U['HT3'] = {'plan': urteil(ident) if gueltig else 'nicht entscheidbar',
                'wortlaut': (urteil(all(t['ueberschuss'] == t['n_P_neg'] + t['n_P_null'] for n, t in praem)) if praem
                             else 'nicht entscheidbar (Praemisse in keinem Netz eingetreten)'),
                'n_punkte': len(pts), 'n_gueltig': len(gueltig), 'n_identitaet_verletzt': sum(1 for n, t in gueltig if not t['identitaet']),
                'n_P_negativ': len(praem), 'P_negativ_bei': [n for n, t in praem][:20],
                'B_null_groesst_rel_max': max((t['B_null_groesst_rel'] or 0.0) for n, t in pts),
                'B_nichtnull_kleinst_rel_min': min(t['B_nichtnull_kleinst_rel'] for n, t in pts)}
    # ---- TU1
    faelle = []
    for n, z in sorted(B.items()):
        for fa in z['faelle']:
            if 'kennzahlen' not in fa['D'] or 'kennzahlen' not in fa['Z']:
                continue
            nD = fa['D_zuege']['n23'] + fa['D_zuege']['n32']
            faelle.append({'netz': n, 'a': fa['a'], 'n23': fa['D_zuege']['n23'], 'n32': fa['D_zuege']['n32'], 'n': nD,
                           'D_stabil': fa['D']['kennzahlen']['n_wachsend_max'] == 0, 'Z_stabil': fa['Z']['kennzahlen']['n_wachsend_max'] == 0,
                           'D_regulaer': fa['D']['kennzahlen']['regulaer'], 'Z_regulaer': fa['Z']['kennzahlen']['regulaer'],
                           'D_wachsend': fa['D']['kennzahlen']['n_wachsend_max'], 'Z_wachsend': fa['Z']['kennzahlen']['n_wachsend_max'],
                           'D_Bred_neg': fa['D']['kennzahlen']['B_red_neg_max'], 'Z_Bred_neg': fa['Z']['kennzahlen']['B_red_neg_max'],
                           'D_ok': bool(fa['D_zuege']['stecken'] == 0 and fa['D_zuege']['invertiert'] == 0 and fa['D_zuege'].get('gleich_scipy', True)),
                           'Z_fehl': fa['Z_zuege']['fehl23'] + fa['Z_zuege']['fehl32']})
    res['faelle_B'] = faelle
    if faelle:
        def anteil(L, key):
            return float(np.mean([f[key] for f in L])) if L else float('nan')
        alle = faelle
        mitz = [f for f in faelle if f['n'] >= 1]
        dW, zW = anteil(alle, 'D_stabil'), anteil(alle, 'Z_stabil')
        dP, zP = anteil(mitz, 'D_stabil'), anteil(mitz, 'Z_stabil')
        U['TU1'] = {'wortlaut': urteil(dW >= 0.9 and zW < 0.9), 'plan': urteil(bool(mitz) and dP >= 0.9 and zP <= 0.5),
                    'n_faelle': len(alle), 'n_faelle_mit_zug': len(mitz), 'D_stabil_alle': dW, 'Z_stabil_alle': zW,
                    'D_stabil_mit_zug': dP, 'Z_stabil_mit_zug': zP,
                    'vermerk': None if len(alle) == 26 else 'nur %d von 26 Faellen' % len(alle)}
    else:
        U['TU1'] = {'wortlaut': 'nicht entscheidbar', 'plan': 'nicht entscheidbar'}
    # ---- Vorzeichentabelle
    tab = []
    for n, z in sorted(A.items()):
        h = z['hodge']
        tab.append({'netz': n, 'E': h['E'], 'F': h['F'], 'stern1_neg': h['stern1_n_neg'], 'stern2_neg': h['stern2_n_neg'],
                    'stern0_neg': h['stern0_n_neg'], 'stern1_min': h['stern1_min'], 'stern2_min': h['stern2_min'],
                    'mu_verletzt': h['mu_n_verletzt'], 'widerspruch_mu_s2': h['mu_gegen_stern2_widerspruch'],
                    'P_psd': z['takt']['P_psd_alle'], 'P_lmin_rel_min': z['takt']['P_lmin_rel_min'], 'c': z['takt']['c_median'],
                    'rest_max': z['takt']['rest_max'], 'je_tet_rest_max': z['takt_je_tet']['rest_max'],
                    'kontrolle': h['kontrolle'], 'zuege': z['netz'].get('zuege') or z['netz'].get('reparatur')})
    res['tabelle_A'] = tab
    tabB = []
    for n, z in sorted(B.items()):
        for fa in z['faelle']:
            for arm in ('D', 'Z'):
                h = fa[arm]['hodge']
                tabB.append({'netz': n, 'a': fa['a'], 'arm': arm, 'T': h['T'], 'E': h['E'], 'stern1_neg': h['stern1_n_neg'],
                             'stern2_neg': h['stern2_n_neg'], 'mu_verletzt': h['mu_n_verletzt'], 'P_psd': fa[arm]['takt']['P_psd_alle'],
                             'rest_max': fa[arm]['takt']['rest_max'], 'c': fa[arm]['takt']['c_median'],
                             'traegheit': {k: fa[arm]['traegheit'][k] for k in ('n_B_neg', 'n_P_pos', 'n_P_neg', 'n_Bred_neg', 'ueberschuss', 'identitaet')},
                             'kennzahlen': {k: fa[arm].get('kennzahlen', {}).get(k) for k in ('regulaer', 'n_wachsend_max', 'B_red_neg_max', 'A_red_pd_alle', 'spanne', 'w_mittel', 'n_masselos', 'tt_min')}})
    res['tabelle_B'] = tabB
    return res


def g(x, n=4):
    return 'None' if x is None else ('%.*g' % (n, x) if isinstance(x, float) else str(x))


def tabellen_md(res):
    U = res['urteile']
    L = ['| Nr | Kartenwortlaut | Plan |', '|---|---|---|']
    L += ['| %s | %s | %s |' % (k, U[k]['wortlaut'], U[k]['plan']) for k in ('HT0', "HT1'", 'HT2', 'HT3', 'TU1')]
    L += ['', '| Netz | T/E/F | *1 < 0 | *2 < 0 | *0 < 0 | min *1 | min *2 | mu < 0 | P psd | min lmin/lmax | c | Rest P - cL1 | Rest je Tet | Kontrollen lA/3V, s0/V, fL/3V |',
          '|---|---|---|---|---|---|---|---|---|---|---|---|---|---|']
    for t in res['tabelle_A']:
        k = t['kontrolle']
        L.append('| %s | -/%d/%d | %d | %d | %d | %s | %s | %d | %s | %s | %s | %s | %s | %s, %s, %s |' % (
            t['netz'], t['E'], t['F'], t['stern1_neg'], t['stern2_neg'], t['stern0_neg'], g(t['stern1_min']), g(t['stern2_min']),
            t['mu_verletzt'], t['P_psd'], g(t['P_lmin_rel_min'], 3), g(t['c'], 12), g(t['rest_max'], 3), g(t['je_tet_rest_max'], 3),
            g(k['sum_lA_durch_3V'], 13), g(k['sum_s0_durch_V'], 13), g(k['sum_fL_durch_3V'], 13)))
    L += ['', '| Netz | a | n 2-3 / 3-2 | D stabil | Z stabil | D wachsend | Z wachsend | D B_red neg | Z B_red neg | D regulaer | Z regulaer | D ok | Z fehlend |',
          '|---|---|---|---|---|---|---|---|---|---|---|---|---|']
    for f in res['faelle_B']:
        L.append('| %s | %g | %d / %d | %s | %s | %d | %d | %d | %d | %s | %s | %s | %d |' % (
            f['netz'], f['a'], f['n23'], f['n32'], f['D_stabil'], f['Z_stabil'], f['D_wachsend'], f['Z_wachsend'], f['D_Bred_neg'],
            f['Z_Bred_neg'], f['D_regulaer'], f['Z_regulaer'], f['D_ok'], f['Z_fehl']))
    L += ['', '| Netz | a | Arm | T | E | *1 < 0 | *2 < 0 | mu < 0 | P psd | c | Rest | n_-(B) | n_+(P) | n_-(P) | n_-(B_red) | Ueberschuss | Identitaet | Spanne | w_mittel |',
          '|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|']
    for t in res['tabelle_B']:
        tr, kz = t['traegheit'], t['kennzahlen']
        L.append('| %s | %g | %s | %d | %d | %d | %d | %d | %s | %s | %s | %d | %d | %d | %d | %d | %s | %s | %s |' % (
            t['netz'], t['a'], t['arm'], t['T'], t['E'], t['stern1_neg'], t['stern2_neg'], t['mu_verletzt'], t['P_psd'], g(t['c'], 12),
            g(t['rest_max'], 3), tr['n_B_neg'], tr['n_P_pos'], tr['n_P_neg'], tr['n_Bred_neg'], tr['ueberschuss'], tr['identitaet'],
            g(kz.get('spanne'), 4), g(kz.get('w_mittel'), 5)))
    return '\n'.join(L) + '\n'


def bild(aw, ordner, pfad):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    A = {}
    for p in sorted(glob.glob(os.path.join(ordner, 'teilA-*.json'))):
        for z in json.load(open(p))['ergebnis']:
            A[z['netz']['name']] = z
    fig, ax = plt.subplots(1, 3, figsize=(17, 5.4))
    a0 = ax[0]
    for nm, col in (('V', '#1f77b4'), ('S', '#d62728'), ('VD', '#2ca02c')):
        if nm not in A:
            continue
        c = A[nm]['takt']['c_median']
        xs, ys = [], []
        for r in A[nm]['takt_zeilen']:
            xs += list(c * np.array(r['eL1']))
            ys += list(r['eP'])
        a0.plot(xs, ys, '.', ms=2.5, color=col, label='%s (c = %.6g)' % (nm, c))
    lim = a0.get_xlim()
    a0.plot(lim, lim, 'k-', lw=0.5)
    a0.set_xlabel('Eigenwerte von c * d0^H *1 d0 (umkreisbasiert)')
    a0.set_ylabel('Eigenwerte von P = -W^H B W')
    a0.set_title('Takt-Operator gegen Hodge-Laplace (alle k)')
    a0.legend(fontsize=8)
    a1 = ax[1]
    tab = aw['tabelle_A']
    namen = [t['netz'] for t in tab]
    x = np.arange(len(namen))
    a1.bar(x - 0.2, [t['stern1_neg'] / t['E'] for t in tab], 0.4, label='Anteil *1 < 0', color='#ff7f0e')
    a1.bar(x + 0.2, [t['stern2_neg'] / t['F'] for t in tab], 0.4, label='Anteil *2 < 0', color='#9467bd')
    for i, t in enumerate(tab):
        a1.text(i, 0.002, 'P psd' if t['P_psd'] else 'P NICHT psd', rotation=90, fontsize=6, ha='center', va='bottom')
    a1.set_xticks(x)
    a1.set_xticklabels(namen, rotation=75, fontsize=6)
    a1.set_ylabel('Anteil negativer Eintraege')
    a1.set_title('Vorzeichen der Hodge-Sterne je Netz')
    a1.legend(fontsize=8)
    a2 = ax[2]
    for f in aw.get('faelle_B', []):
        col = '#1f77b4' if f['a'] < 5e-3 else '#d62728'
        a2.plot(f['n'] + 0.5, f['D_Bred_neg'] + 0.5, 'o', mfc='none', color=col, ms=6)
        a2.plot(f['n'] + 0.5, f['Z_Bred_neg'] + 0.5, 'x', color=col, ms=6)
    a2.plot([], [], 'ko', mfc='none', label='Delaunay-gesteuert (D)')
    a2.plot([], [], 'kx', label='gleich viele zufaellige (Z)')
    a2.plot([], [], 's', color='#1f77b4', label='a = 1e-3')
    a2.plot([], [], 's', color='#d62728', label='a = 1e-2')
    a2.set_xscale('log')
    a2.set_yscale('log')
    a2.set_xlabel('Zahl der Zuege + 0,5')
    a2.set_ylabel('negative Richtungen von B_red (max ueber k) + 0,5')
    a2.set_title('Stabilitaet: gesteuerte gegen zufaellige Zuege')
    a2.legend(fontsize=8)
    fig.suptitle('TAKT-UMKLAPP-1 (synthetische Gitterrechnung, keine Messdaten)')
    fig.tight_layout()
    fig.savefig(pfad + '.tmp.png', dpi=110)
    os.replace(pfad + '.tmp.png', pfad)


# ------------------------------------------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['teilA', 'teilB', 'auswertung', 'bild'])
    ap.add_argument('--netze', default='V,S')
    ap.add_argument('--ridx', default='0-12')
    ap.add_argument('--a', default='1e-3,1e-2')
    ap.add_argument('--ordner', default='lauf')
    ap.add_argument('--aw')
    ap.add_argument('--rauch', action='store_true', help='nur Schluessel, Laufzeiten, Speicher speichern')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    info = {'numpy': np.__version__, 'scipy': scipy.__version__, 'python': platform.python_version(), 'host': platform.node(),
            'argv': sys.argv, 'skript_sha256': sha(os.path.abspath(__file__)),
            'module_sha256': {m.__name__: sha(os.path.abspath(m.__file__)) for m in (tg, uk, ew, mn, tga)},
            'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    if a.modus == 'teilA':
        erg = []
        for n in a.netze.split(','):
            erg.append(teil_a(n, a.rauch))
            print('teilA', n, '%.1f s' % erg[-1]['t_s'], flush=True)
    elif a.modus == 'teilB':
        if '-' in a.ridx:
            i0, i1 = a.ridx.split('-')
            ridx = list(range(int(i0), int(i1) + 1))
        else:
            ridx = [int(x) for x in a.ridx.split(',')]
        al = [float(x) for x in a.a.split(',')]
        erg = [teil_b(n, ridx, a.rauch, al) for n in a.netze.split(',')]
    elif a.modus == 'auswertung':
        erg = auswertung(a.ordner)
        md = tabellen_md(erg)
        with open(a.out[:-5] + '.md.tmp', 'w') as fh:
            fh.write(md)
        os.replace(a.out[:-5] + '.md.tmp', a.out[:-5] + '.md')
    else:
        bild(json.load(open(a.aw))['ergebnis'], a.ordner, a.out)
        print('fertig bild', flush=True)
        return
    res = {'info': info, 'ergebnis': erg, 'laufzeit_s': time.time() - t0,
           'maxrss_MB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
           'ende_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    if a.rauch:
        res = {'info': info, 'schluessel': tg.nur_schluessel(erg[0]) if erg else None, 'laufzeit_s': res['laufzeit_s'],
               'maxrss_MB': res['maxrss_MB'], 't_je_netz': [e.get('t_s') for e in erg]}
    tg.schreibe(a.out, res)
    print('fertig', a.modus, a.netze, 'laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
