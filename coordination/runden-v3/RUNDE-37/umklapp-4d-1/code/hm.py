#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""HODGE-MASSE-1 (Runde 48, fmhc-physics), Code-Agent fuer die Leitung claude-primary.

Fragen: (1) Ist die Reduktion R1 (bzw. R2) die horizontale? (2) TT-Spanne mit horizontaler Reduktion RH fuer A1, A2
(Kartenformel) und A2L (Lagrange-additive volumengewichtete DeWitt-Form) auf V, S (= C15), A15, Glas N = 128.
Modell wie tg.py / ew.py (Kantenwerte a = dl/l, B Regge, M Eckverschiebung, c skalare Regel, Hamilton-Form
H = 1/2 p^+ A p + 1/2 a^+ B a). Unveraendert importiert: tg.py, ew.py, tp.py, tti.py, dn.py.

Bewegungsenergien je Tetraeder t (Phi_t[p, s] = n_p^T B6_s n_p, TR_s = tr B6_s, Vref = Vbox / T):
  A1 : A_t = A0_t = Phi (1 - TR TR^T / 2) Phi^T            (Hamilton-additiv, J = 1; = tg A0)
  A2 : A_t = (Vref / V_t) A0_t                            (Hamilton-additiv; Kartenformel, TT-ISO-1 A2)
  A2L: K_t = (V_t / Vref) Phi^-T (1 - TR TR^T) Phi^-1     (Lagrange-additiv; = TT-ISO-1 A3 mit J = 1), A = K^-1
Reduktionen (S = orthonormales Komplement von Bild[M, c], Q = Basis Bild M, C = Basis Bild c):
  R1 : A_red = S^+ A S                                     (Code)
  RH : A_red = S^+ (A - A C (C^+ A C)^-1 C^+ A) S          (horizontal in der Eichung, Dirac fuer c)
       bzw. Lagrange: K_red = S^+ K S - S^+ K Q (Q^+ K Q)^-1 Q^+ K S
  R2 : K_red = S^+ K S                                     (Code, TT-ISO-1 A3R2)
Masselose Moden: 1/omega^2 = die zwei betragsgroessten Eigenwerte von Z = L^-1 K_red L^-+ mit B_red = L L^+.
"""
import argparse, json, sys, os, time, hashlib, platform, resource
import numpy as np
import scipy
import scipy.linalg as sla
import scipy.sparse as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tp  # noqa: E402
import ew  # noqa: E402
import tg  # noqa: E402
import tti  # noqa: E402
import dn  # noqa: E402

GL = np.eye(6) - np.outer(tp.TR, tp.TR)          # Lagrange-DeWitt (lambda = 1): |h|^2 - (tr h)^2
GH = np.eye(6) - 0.5 * np.outer(tp.TR, tp.TR)    # Hamilton-DeWitt: |p|^2 - (tr p)^2 / 2
VAR = ('A1R1', 'A1RH', 'A2R1', 'A2RH', 'A2LR2', 'A2LRH', 'A2LRHL', 'A2LR1')
LUECKE_MAX = 1e-2
GSAAT = (41, 43)                                 # Diagonal-Eichungen wie IMPULS-NETZ-1 (U(0,25; 4) je Kante)


def sha(p):
    with open(p, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def herm(X):
    return 0.5 * (X + np.conj(np.swapaxes(X, -1, -2)))


# ------------------------------------------------------------------------------------------------ Netze und Geometrie
def netz(name):
    if name in ('V', 'S'):
        LV, pos, G, O, info = dn.netz_ew(name)
        return LV, pos, G, O, {'quelle': 'dn.netz_ew(%s)' % name}
    if name == 'A15':
        LV, pos, typ, G, O, keys, info = dn.baue('A15', 'delaunay')
        return LV, pos, G, O, {'quelle': 'dn.baue(A15, delaunay)', 'info': info}
    if name.startswith('glas-s'):
        s = int(name[6:])
        LV, pos, G, O, pr = tg.zufallsnetz(128, s)
        return LV, pos, G, O, {'quelle': 'tg.zufallsnetz(128, %d)' % s, 'pruefung': pr}
    raise ValueError(name)


def tet_geo(LV, pos, G, O, mod):
    X = pos[G] + np.einsum('tai,ij->taj', O.astype(float), LV)
    et = np.stack([X[:, j] - X[:, i] for (i, j, _, _) in tg.PAARE], 1)
    nt = et / np.linalg.norm(et, axis=2)[..., None]
    vol = np.abs(np.linalg.det(X[:, 1:] - X[:, :1])) / 6.0
    Phi = np.einsum('tpi,sij,tpj->tps', nt, tp.B6, nt)
    Pi = np.linalg.inv(Phi)
    T = len(G)
    vref = mod['Vbox'] / T
    A0 = mod['A0']
    A0chk = np.einsum('tps,sr,tqr->tpq', Phi, GH, Phi)
    A2t = (vref / vol)[:, None, None] * A0
    Kt = (vol / vref)[:, None, None] * np.einsum('tsp,sr,trq->tpq', Pi, GL, Pi)
    I6 = np.eye(6)
    kontr = {'A0_gleich_Phi_GH_Phi': float(np.abs(A0chk - A0).max() / np.abs(A0).max()),
             'A2t_mal_Kt_minus_1': float(np.abs(np.einsum('tpq,tqr->tpr', A2t, Kt) - I6).max()),
             'vol_summe_rel_abw': float(abs(vol.sum() / mod['Vbox'] - 1.0)), 'vol_min_rel': float(vol.min() / vol.mean()),
             'Phi_cond_max': float(np.linalg.cond(Phi).max())}
    return {'X': X, 'nt': nt, 'vol': vol, 'Phi': Phi, 'Pi': Pi, 'vref': vref, 'A1t': A0, 'A2t': A2t, 'Kt': Kt,
            'kontr': kontr}


def assemble(mod, Mt, k):
    E, eidx = mod['E'], mod['eidx']
    ph = np.exp(1j * (mod['Tcopy'] @ k))
    f = np.conj(ph)[:, :, None] * ph[:, None, :]
    rows = np.repeat(eidx[:, :, None], 6, 2).ravel()
    cols = np.repeat(eidx[:, None, :], 6, 1).ravel()
    return sp.coo_matrix(((Mt * f).ravel(), (rows, cols)), shape=(E, E)).toarray()


def assemble_sp(mod, Mt, k):
    E, eidx = mod['E'], mod['eidx']
    ph = np.exp(1j * (mod['Tcopy'] @ k))
    f = np.conj(ph)[:, :, None] * ph[:, None, :]
    rows = np.repeat(eidx[:, :, None], 6, 2).ravel()
    cols = np.repeat(eidx[:, None, :], 6, 1).ravel()
    return sp.coo_matrix(((Mt * f).ravel(), (rows, cols)), shape=(E, E)).tocsr()


# ------------------------------------------------------------------------------------------------ Bausteine je k
def zerlege(M, c):
    """S (Komplement von Bild[M, c]), Q (Basis Bild M), C (Basis Bild c), orthonormal."""
    E = M.shape[0]
    X = np.concatenate([M, c], 1)
    nX, nM = X.shape[1], M.shape[1]
    Qf, R = np.linalg.qr(X, mode='complete')
    d = np.abs(np.diag(R[:nX]))
    if d.min() > 1e-9 * d.max():
        return Qf[:, nX:], Qf[:, :nM], Qf[:, nM:nX], 'qr', float(d.min() / d.max())
    U, s_, _ = np.linalg.svd(X)
    r = int((s_ > 1e-9 * s_.max()).sum())
    Um, sm, _ = np.linalg.svd(M)
    rm = int((sm > 1e-9 * sm.max()).sum())
    Q = Um[:, :rm]
    cp = c - Q @ (np.conj(Q.T) @ c)
    Uc, sc, _ = np.linalg.svd(cp)
    rc = int((sc > 1e-9 * sc.max()).sum())
    return U[:, r:], Q, Uc[:, :rc], 'svd', float(s_[r - 1] / s_[0])


def z_auswerten(Z, eps, Li=None, S=None, mit_vek=False):
    Z = herm(Z)
    if mit_vek:
        ev, U = np.linalg.eigh(Z)
    else:
        ev = np.linalg.eigvalsh(Z)
    o = np.argsort(-np.abs(ev))
    top = ev[o[:2]]
    out = {'w2k2': sorted(float(x) for x in (1.0 / top) / eps ** 2), 'luecke': float(abs(ev[o[2]]) / abs(ev[o[1]])),
           'n_neg': int((ev < 0).sum()), 'pos2': bool((top > 0).all())}
    out['ok'] = bool(out['pos2'] and out['luecke'] < LUECKE_MAX)
    if mit_vek:
        out['_x'] = [np.conj(Li.T) @ U[:, j] for j in o[:2]]
    return out


def Z_A(Li, Ared):
    return Li @ np.linalg.solve(herm(Ared), np.conj(Li.T))


def Z_K(Li, Kred):
    return Li @ herm(Kred) @ np.conj(Li.T)


def rh_A(A, S, C):
    AS = A @ S
    AC = A @ C
    CAC = herm(np.conj(C.T) @ AC)
    return np.conj(S.T) @ AS - np.conj(AS.T) @ C @ np.linalg.solve(CAC, np.conj(C.T) @ AS)


def rh_K(K, W, Q):
    """Stationaerwert von K(W q + Q x) ueber x (Schur-Komplement): horizontale Reduktion der Lagrange-Form."""
    WKQ = np.conj(W.T) @ (K @ Q)
    QKQ = herm(np.conj(Q.T) @ (K @ Q))
    return np.conj(W.T) @ (K @ W) - WKQ @ np.linalg.solve(QKQ, np.conj(WKQ.T))


def polarisationen(d):
    u = np.cross(d, [0.3, 0.5, 0.7])
    u = u / np.linalg.norm(u)
    v = np.cross(d, u)
    return [(np.outer(u, u) - np.outer(v, v)) / np.sqrt(2), (np.outer(u, v) + np.outer(v, u)) / np.sqrt(2)]


def punkt(mod, geo, k, mit_tt=False, mit_kontr=False, mit_vert=False):
    t0 = time.time()
    eps = float(np.linalg.norm(k))
    Bs, A1s, M, c = tg.ops(mod, k)
    B = Bs.tocsr()
    A1 = assemble_sp(mod, geo['A1t'], k)
    A2 = assemble_sp(mod, geo['A2t'], k)
    K = assemble_sp(mod, geo['Kt'], k)
    S, Q, C, weg, svrel = zerlege(M, c)
    Sh = np.conj(S.T)
    Br = herm(Sh @ (B @ S))
    z = {'eps': eps, 'dim': int(S.shape[1]), 'weg': weg, 'sv_rel_min': svrel}
    try:
        L = np.linalg.cholesky(Br)
    except np.linalg.LinAlgError:
        z['B_red_pd'] = False
        return z
    z['B_red_pd'] = True
    Li = sla.solve_triangular(L, np.eye(L.shape[0]), lower=True)
    A2L = np.linalg.inv(K.toarray())
    # RH = symplektische Reduktion (Impulse senkrecht auf Bild M, kanonisch) mit Dirac-Paar fuer c;
    # A2LRHL = dieselbe Reduktion als Lagrange-Minimum ueber die Eichung (nur bei vertikal regulaerem K sinnvoll)
    Ared = {'A1R1': Sh @ (A1 @ S), 'A1RH': rh_A(A1, S, C), 'A2R1': Sh @ (A2 @ S), 'A2RH': rh_A(A2, S, C),
            'A2LR1': Sh @ A2L @ S, 'A2LRH': rh_A(A2L, S, C)}
    Kred = {v: np.linalg.inv(herm(Ar)) for v, Ar in Ared.items()}
    Kred['A2LR2'] = Sh @ (K @ S)
    Kred['A2LRHL'] = rh_K(K, S, Q)
    # affine TT-Wellen (Ritz, wie TT-GLAS-2 (b)): z_i = S^+ a_i, a_e = n_e^T h_i n_e exp(i k . m_e)
    d = k / eps
    ph = np.exp(1j * (mod['mitte'] @ k))
    av = np.stack([np.einsum('ei,ij,ej->e', mod['n'], h, mod['n']) * ph for h in polarisationen(d)], 1)
    zc = Sh @ av
    B2 = herm(np.conj(zc.T) @ Br @ zc)
    for v in VAR:
        Kv = herm(Kred[v])
        r = z_auswerten(Li @ Kv @ np.conj(Li.T), eps, Li, S, mit_vek=mit_tt)
        K2 = herm(np.conj(zc.T) @ Kv @ zc)
        wr = np.linalg.eigvals(np.linalg.solve(K2, B2))
        r['ritz'] = sorted(float(x) for x in wr.real / eps ** 2)
        r['ritz_im'] = float(np.abs(wr.imag).max() / eps ** 2)
        if mit_tt:
            tt, rest = [], []
            for x in r.pop('_x'):
                H, rr = tg.tensor_fit(mod, S @ x, k, M)
                tt.append(float(tp.tt_anteil(H, k)[0]))
                rest.append(rr)
            r['tt_anteil'] = tt
            r['fit_rest'] = rest
        z[v] = r
    if mit_vert:
        # vertikale Positivitaet: K auf den Eichrichtungen (Q^+ K Q); Dirac-Bedingung: C^+ A C regulaer
        vt = {}
        for nm, Kf, Af in (('A1', np.linalg.inv(A1.toarray()), A1), ('A2', np.linalg.inv(A2.toarray()), A2), ('A2L', K, A2L)):
            ev = np.linalg.eigvalsh(herm(np.conj(Q.T) @ (Kf @ Q)))
            s = np.abs(ev).max()
            ec = np.linalg.eigvalsh(herm(np.conj(C.T) @ (Af @ C)))
            sc = np.abs(ec).max()
            vt[nm] = {'QKQ_n_neg': int((ev < -1e-12 * s).sum()), 'QKQ_min_rel': float(ev.min() / s),
                      'QKQ_absmin_rel': float(np.abs(ev).min() / s), 'CAC_n_neg': int((ec < -1e-12 * sc).sum()),
                      'CAC_absmin_rel': float(np.abs(ec).min() / sc)}
        z['vertikal'] = vt
    if mit_kontr:
        kk = {'A1_gleich_tg': float(np.abs((A1 - A1s).toarray()).max() / np.abs(A1.toarray()).max()),
              'cM_null': float(np.abs(np.conj(C.T) @ Q).max())}
        QC = np.concatenate([Q, C], 1)
        ev3 = np.sort(np.linalg.eigvalsh(herm(Li @ herm(rh_K(K, S, QC)) @ np.conj(Li.T))))
        ev4 = np.sort(np.linalg.eigvalsh(herm(Li @ herm(Kred['A2LR1']) @ np.conj(Li.T))))
        kk['A2LR1_gleich_K_schur_ueber_M_und_c'] = float(np.abs(ev3 - ev4).max() / np.abs(ev4).max())
        A1i = np.linalg.inv(A1.toarray())
        ev5 = np.sort(np.linalg.eigvalsh(herm(Li @ herm(rh_K(A1i, S, Q)) @ np.conj(Li.T))))
        ev6 = np.sort(np.linalg.eigvalsh(herm(Li @ herm(Kred['A1RH']) @ np.conj(Li.T))))
        kk['A1RH_hamilton_gegen_lagrange'] = float(np.abs(ev5 - ev6).max() / np.abs(ev6).max())
        ev7 = np.sort(np.linalg.eigvalsh(herm(Li @ herm(Kred['A2LRHL']) @ np.conj(Li.T))))
        ev8 = np.sort(np.linalg.eigvalsh(herm(Li @ herm(Kred['A2LRH']) @ np.conj(Li.T))))
        kk['A2LRH_hamilton_gegen_lagrange'] = float(np.abs(ev7 - ev8).max() / np.abs(ev8).max())
        kk['A1_cond'] = float(np.linalg.cond(A1.toarray()))
        kk['K_cond'] = float(np.linalg.cond(K.toarray()))
        z['kontr'] = kk
    z['t_s'] = time.time() - t0
    return z


# ------------------------------------------------------------------------------------------------ HM1: Eichflaechen (V)
def eichflaechen(mod, geo, k, gauges):
    """Zwei Routen und Eichflaechen: Sigma_E (Code, M^+ a = 0) gegen Sigma_G (M^+ G a = 0, G diagonal)."""
    eps = float(np.linalg.norm(k))
    Bs, A1s, M, c = tg.ops(mod, k)
    B = Bs.toarray()
    S, Q, C, weg, svrel = zerlege(M, c)
    Br = herm(np.conj(S.T) @ B @ S)
    Li = sla.solve_triangular(np.linalg.cholesky(Br), np.eye(S.shape[1]), lower=True)
    mats = {'A1': assemble(mod, geo['A1t'], k), 'A2': assemble(mod, geo['A2t'], k)}
    Kd = {'A1': np.linalg.inv(mats['A1']), 'A2': np.linalg.inv(mats['A2']), 'A2L': assemble(mod, geo['Kt'], k)}
    mats['A2L'] = np.linalg.inv(Kd['A2L'])
    out = {'eps': eps}
    for kin in ('A1', 'A2', 'A2L'):
        A, K = mats[kin], Kd[kin]
        Sh = np.conj(S.T)
        zz = {'E_R1': z_auswerten(Z_A(Li, Sh @ A @ S), eps)['w2k2'],
              'E_RH_hamilton': z_auswerten(Z_A(Li, rh_A(A, S, C)), eps)['w2k2'],
              'E_RH_lagrange': z_auswerten(Z_K(Li, rh_K(K, S, Q)), eps)['w2k2'],
              'E_R2': z_auswerten(Z_K(Li, Sh @ K @ S), eps)['w2k2']}
        for gi, G in enumerate(gauges):
            GM = G[:, None] * M
            W = S - M @ np.linalg.solve(herm(np.conj(M.T) @ GM), np.conj(GM.T) @ S)
            Wh = np.conj(W.T)
            BW = herm(Wh @ B @ W)
            LWi = sla.solve_triangular(np.linalg.cholesky(BW), np.eye(W.shape[1]), lower=True)
            g = 'G%d' % (gi + 1)
            zz[g + '_RH_lagrange'] = z_auswerten(Z_K(LWi, rh_K(K, W, Q)), eps)['w2k2']
            # RH symplektisch auf Sigma_G: Impulse senkrecht auf Bild[M, A C] (Eich- und Dirac-Bedingung), Paarung mit W
            Xh = np.concatenate([M, A @ C], 1)
            Th = np.linalg.qr(Xh, mode='complete')[0][:, Xh.shape[1]:]
            Gh = Wh @ Th
            KH = Gh @ np.linalg.solve(herm(np.conj(Th.T) @ A @ Th), np.conj(Gh.T))
            zz[g + '_RH_symplektisch'] = z_auswerten(Z_K(LWi, KH), eps)['w2k2']
            zz[g + '_R2'] = z_auswerten(Z_K(LWi, Wh @ K @ W), eps)['w2k2']
            # R1 in der G-Metrik (Definition G): Impulse senkrecht auf Bild[M, G^-1 c], Paarung mit W
            Xg = np.concatenate([M, c / G[:, None]], 1)
            Tg = np.linalg.qr(Xg, mode='complete')[0][:, Xg.shape[1]:]
            Gm = Wh @ Tg
            KG = Gm @ np.linalg.solve(herm(np.conj(Tg.T) @ A @ Tg), np.conj(Gm.T))
            zz[g + '_R1G'] = z_auswerten(Z_K(LWi, KG), eps)['w2k2']
            # R1 woertlich (Definition P): orthonormale Basis von Sigma_G, a und p auf Sigma_G
            SP = np.linalg.qr(W)[0]
            SPh = np.conj(SP.T)
            LPi = sla.solve_triangular(np.linalg.cholesky(herm(SPh @ B @ SP)), np.eye(SP.shape[1]), lower=True)
            zz[g + '_R1P'] = z_auswerten(Z_A(LPi, SPh @ A @ SP), eps)['w2k2']
        out[kin] = zz
    # ohne skalare Regel (nur Eichung): R1 auf Sigma_E (Hamilton) gegen RH-Lagrange auf Sigma_G1, alle omega^2
    S0, Q0 = zerlege(M, np.zeros((M.shape[0], 0), complex))[:2]
    S0h = np.conj(S0.T)
    A = mats['A1']
    w_r1 = np.linalg.eigvals((S0h @ A @ S0) @ herm(S0h @ B @ S0))
    G = gauges[0]
    GM = G[:, None] * M
    W0 = S0 - M @ np.linalg.solve(herm(np.conj(M.T) @ GM), np.conj(GM.T) @ S0)
    K0 = rh_K(Kd['A1'], W0, Q0)
    w_rh = np.linalg.eigvals(np.linalg.solve(herm(K0), herm(np.conj(W0.T) @ B @ W0)))
    a1 = np.sort_complex(w_r1)
    a2 = np.sort_complex(w_rh)
    out['ohne_c_A1'] = {'n': int(len(a1)), 'abw_rel_max': float(np.abs(a1 - a2).max() / np.abs(a1).max()),
                        'n_neg_re': int((a1.real < -1e-9 * np.abs(a1).max()).sum()),
                        'kleinste_abs_R1': [float(abs(x)) for x in sorted(a1, key=abs)[:4]]}
    return out


# ------------------------------------------------------------------------------------------------ HM0
def hm0(mod, geo):
    rng = np.random.default_rng(7)
    hs = [tp.B6[s] for s in range(6)]
    for _ in range(3):
        h = rng.normal(size=(3, 3))
        hs.append(0.5 * (h + h.T))
    k0 = np.zeros(3)
    Kz = assemble(mod, geo['Kt'], k0).real
    A2z = assemble(mod, geo['A2t'], k0).real
    A1z = assemble(mod, geo['A1t'], k0).real
    fak = mod['Vbox'] / geo['vref']
    out = {'A2_k0_cond': float(np.linalg.cond(A2z)), 'A1_k0_cond': float(np.linalg.cond(A1z)), 'zeilen': []}
    fA2L, fA2, rA2, rA1 = 0.0, 0.0, [], []
    for h in hs:
        v = np.einsum('ei,ij,ej->e', mod['n'], h, mod['n'])
        hn = float(np.sum(h * h))
        Gc = hn - float(np.trace(h)) ** 2
        cont = fak * Gc
        kL = float(v @ Kz @ v)
        k2 = float(v @ np.linalg.solve(A2z, v))
        k1 = float(v @ np.linalg.solve(A1z, v))
        fA2L = max(fA2L, abs(kL - cont) / (fak * hn))
        fA2 = max(fA2, abs(k2 - cont) / (fak * hn))
        out['zeilen'].append({'h_spur': float(np.trace(h)), 'kont': cont, 'A2L': kL, 'A2': k2, 'A1': k1})
    out['fehler_norm_A2L'] = fA2L
    out['fehler_norm_A2'] = fA2
    # TT-artige (spurfreie) Verhaeltnis A2 / Kontinuum (beschreibend)
    tt = [z for z in out['zeilen'] if abs(z['h_spur']) < 1e-12 and abs(z['kont']) > 0]
    out['A2_ueber_kont_spurfrei'] = [z['A2'] / z['kont'] for z in tt]
    out['A1_ueber_kont_spurfrei'] = [z['A1'] / z['kont'] for z in tt]
    return out


# ------------------------------------------------------------------------------------------------ Laeufe
def spannen(zeilen, epsl):
    out = {}
    for v in VAR:
        w_all, w_1, r_all, r_1, okall, nneg = [], [], [], [], True, 0
        for z in zeilen:
            for i, e in enumerate(epsl):
                p = z.get('eps%d' % (i + 1))
                if p is None:
                    continue
                if not p.get('B_red_pd') or v not in p:
                    okall = False
                    continue
                r = p[v]
                okall &= r['ok']
                nneg = max(nneg, r['n_neg'])
                w_all += r['w2k2']
                r_all += r['ritz']
                if i == 0:
                    w_1 += r['w2k2']
                    r_1 += r['ritz']
        wa, w1, ra, r1 = np.array(w_all), np.array(w_1), np.array(r_all), np.array(r_1)

        def sp_(x):
            return float(x.max() / x.min() - 1) if len(x) and x.min() > 0 else None
        out[v] = {'spanne_alle': sp_(wa), 'spanne_eps1': sp_(w1), 'ritz_spanne_alle': sp_(ra), 'ritz_spanne_eps1': sp_(r1),
                  'w_min': float(wa.min()) if len(wa) else None, 'w_max': float(wa.max()) if len(wa) else None,
                  'n_werte': int(len(wa)), 'alle_ok': bool(okall), 'n_neg_max': int(nneg)}
    return out


def lauf_spanne(name, rauch=False, ridx=None):
    t00 = time.time()
    LV, pos, G, O, info = netz(name)
    mod = tg.modell(LV, pos, G, O, {})
    geo = tet_geo(LV, pos, G, O, mod)
    glas = name.startswith('glas')
    richt = tg.richtungen13w() if glas else tti.richtungen13()
    epsl = (tg.EPS1, tg.EPS2) if glas else (1e-3, 2e-3)
    idx = list(range(len(richt))) if ridx is None else list(ridx)
    if rauch:
        idx = idx[:2]
    out = {'netz': name, 'info': info, 'E': int(mod['E']), 'T': int(mod['T']), 'nV': int(mod['nV']),
           'pruefung': mod['pruefung'], 'geo_kontr': geo['kontr'], 'vref': geo['vref'], 'eps': list(epsl), 'ridx': idx}
    zeilen = []
    for ir in idx:
        nm, d = richt[ir]
        tt3 = nm in ('100', '110', '111')
        z = {'ridx': int(ir), 'richtung': nm, 'd': d.tolist()}
        for i, e in enumerate(epsl):
            if glas and i == 1 and not tt3:
                continue                       # Glas: |k| = 2e-2 nur an den drei TT-Richtungen (wie TT-GLAS-1)
            z['eps%d' % (i + 1)] = punkt(mod, geo, e * d, mit_tt=(i == 0 and tt3), mit_kontr=(i == 0 and nm in ('100', '111')),
                                         mit_vert=(i == 0 and (tt3 or not glas)))
        zeilen.append(z)
    out['zeilen'] = zeilen
    out['spannen'] = spannen(zeilen, epsl)
    if 0 in idx:
        out['hm0'] = hm0(mod, geo)
        if not rauch:
            out['affin'] = tg.affin(mod)
    if name == 'V' and not rauch:
        gauges = []
        for s in GSAAT:
            rng = np.random.default_rng(s)
            gauges.append(rng.uniform(0.25, 4.0, mod['E']))
        ez = []
        for nm, d in tti.richtungen13():
            for e in (1e-3, 2e-3):
                r = eichflaechen(mod, geo, e * d, gauges)
                r['richtung'] = nm
                ez.append(r)
        out['eich'] = ez
    out['t_s'] = time.time() - t00
    return out


def nur_schluessel(x, tiefe=0):
    if isinstance(x, dict):
        return {k: nur_schluessel(v, tiefe + 1) for k, v in x.items()} if tiefe < 2 else sorted(x.keys())
    return type(x).__name__


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['spanne'])
    ap.add_argument('--netz', required=True)
    ap.add_argument('--rauch', action='store_true')
    ap.add_argument('--ridx', default=None, help='Richtungsindizes, z. B. 0-6')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    info = {'numpy': np.__version__, 'scipy': scipy.__version__, 'python': platform.python_version(), 'host': platform.node(),
            'argv': sys.argv, 'skript_sha256': sha(os.path.abspath(__file__)),
            'module_sha256': {m.__name__: sha(os.path.abspath(m.__file__)) for m in (tp, ew, tg, tti, dn)},
            'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    ridx = None
    if a.ridx:
        lo, hi = a.ridx.split('-')
        ridx = list(range(int(lo), int(hi) + 1))
    erg = lauf_spanne(a.netz, rauch=a.rauch, ridx=ridx)
    res = {'info': info, 'ergebnis': erg, 'laufzeit_s': time.time() - t0,
           'maxrss_MB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
           'ende_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    if a.rauch:
        kz = {}
        for z in erg['zeilen']:
            for key in ('eps1', 'eps2'):
                if 'kontr' in z.get(key, {}):
                    kz['%s_%s' % (z['richtung'], key)] = z[key]['kontr']
        res = {'info': info, 'laufzeit_s': res['laufzeit_s'], 'maxrss_MB': res['maxrss_MB'], 'schluessel': nur_schluessel(erg),
               't_punkt': [z['eps1'].get('t_s') for z in erg['zeilen']], 'geo_kontr': erg['geo_kontr'], 'code_kontr': kz,
               'E': erg['E'], 'T': erg['T']}
    tg.schreibe(a.out, res)
    print('fertig', a.modus, a.netz, 'laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
