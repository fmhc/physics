#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""V1-AUFHEBUNG-1 (Runde 48, fmhc-physics), Code-Agent fuer die Leitung claude-primary.

Unabhaengige Nachrechnung der Kreisbahn-Abstrahlung auf Finns Netz V mit Spannung S, Impuls J und Energiekanal V1,
an mehreren Gewichtspunkten (Bewegungsgewichte je Tetraeder-Art) und mehreren kl.
Eigener Rechenweg (nicht gs.py): Netz und Operatoren aus ew.baue/ew.ops, Gewichte ueber pn.A_J, W aus mn.W_of
(alle unveraendert importiert); Reduktion R1, Moden, Spannungsquelle (eigene Q-Abbildung), Impulskraft, V1-Kraft und
Auswertung hier neu, numpy, volle Kugel (keine k -> -k-Symmetrie benutzt).

Je Richtung n (Gauss-Legendre nt x nphi, volle Kugel) und k = (kl/l_P) n:
  S = Komplement von Bild [M, c];  A_red = S^H A S = L L^H;  Moden X = L U (zwei weichste von L^H B_red L), om2.
  Spannung (Basis T_b, 6 Stueck): sigma_e = Q_e : (T_b - tr T_b 1) e^(i k.m_e), Q_e = Summe_{Tetraeder, p -> e} 0,5 l_p X^T dK_p X
  (P1-Gewichte pn.K_aus_laengen, dK per komplexem Schritt aus pn.tet_ableitungen).
  f0 = -S^H sigma;  fJ = -A_red^-1 S^H A P_M sigma (Impulsbilanz J' = -M^H sigma, IMPULS-NETZ-1);
  V1-Einheitskraft (Energie 1 je Zelle, baryzentrisch): m_v = (V_v/V) e^(i k.x_v), a_c = c (c^H c)^-1 m,
  fV = -(kappa_g/kappa') S^H B a_c.
  Kopplungen g0 = X^H f0, gJ = X^H (f0 + fJ), gV = X^H fV.
Auswertung je Kreisbahn S (Bahnnormale m, S = (u + i w)(u + i w)^T):
  A_j(n) = Summe_b koef_b(T) gJ_jb + eps_j V (n.S.n) gV_j,  eps_j = (c0/c_j)^2  (Energie aus der Kontinuums-Erhaltung
  eps = c0^2 k^2 (n.S.n)/omega^2 auf der Massenschale omega = c_j k),
  P/P_E = Summe_n w Summe_j |A_j|^2/om2_j (c0/c_j) / Summe_n w V Lambda_n[S]:S^*/k^2,  c0^2 = Raumwinkelmittel om2/k^2,
  G_N/G = (8 V/nV)/(Raumwinkelmittel lambda_min(W^H c)/k^2),  G = (P/P_E)/(G_N/G).
Aufruf nur ueber kleintest.sh auf der .69:
  python va.py netz --punkte haupt --kl 0.0025,0.005,0.01,0.02 --out lauf/haupt.json [--nt 10 --nphi 20] [--rauch]
  python va.py aus --haupt lauf/haupt.json --kurve lauf/kurve.json --quad lauf/quad.json --ref code/referenz.json
                   --out aus/urteile.json --bild aus/bild-v1-aufhebung.png
"""
import argparse, json, os, sys, time, hashlib, platform, resource, math
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ew  # noqa: E402  (unveraendert)
import pn  # noqa: E402  (unveraendert)
import mn  # noqa: E402  (unveraendert)

LP, VCELL, KG, KP = pn.LP, pn.VCELL, pn.KG, pn.KP
ARTEN = ['finn_auf', 'finn_ab', 'kegel_T1', 'kegel_T2', 'sechs_T1', 'sechs_T2']
BASIS = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]
TB = []
for (_a, _b) in BASIS:
    _T = np.zeros((3, 3))
    _T[_a, _b] = _T[_b, _a] = 1.0
    TB.append(_T)
HERE = os.path.dirname(os.path.abspath(__file__))


def sha(p):
    with open(p, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def cT(X):
    return np.conj(np.swapaxes(X, -1, -2))


def herm(X):
    return 0.5 * (X + cT(X))


def koef(T):
    return np.stack([T[..., 0, 0], T[..., 1, 1], T[..., 2, 2], T[..., 0, 1], T[..., 0, 2], T[..., 1, 2]], -1)


# ------------------------------------------------------------------------------------------------ Gewichtspunkte
def lade_ref():
    with open(os.path.join(HERE, 'referenz.json')) as fh:
        return json.load(fh)


def gewichtspunkte(wahl):
    """Gewichte je Art (finn_auf, finn_ab, kegel_T1, kegel_T2, sechs_T1, sechs_T2)."""
    ref = lade_ref()
    pkt = {}
    if wahl in ('haupt', 'alle', 'rauch'):
        pkt['J_iso'] = [pn.J_ISO[a] for a in ARTEN]
        pkt['F1_exakt'] = list(ref['smi_F1_exakt']['w'])
        pkt['J1'] = [1.0] * 6
    if wahl in ('kurve', 'alle'):
        for z in ref['smi_kurve_dTT0']:
            x0, x1 = z['x']
            pkt['K%+.1f' % x0] = [1.0, 1.0, 10.0 ** x0, 10.0 ** x0, 10.0 ** x1, 10.0 ** x1]
        pkt['F1_exakt'] = list(ref['smi_F1_exakt']['w'])
    if wahl == 'rauch':
        pkt = {'J_iso': pkt['J_iso']}
    return pkt


# ------------------------------------------------------------------------------------------------ Kreisbahnen
def bahnnormalen():
    """24 Lagen wie GLAS-STRAHLUNG-1 PLAN 1.5: [001], [111], [110], (1,2,3); 8 Normalen Saat 31; 12 Normalen Saat 47."""
    roh = [('001', [0, 0, 1]), ('111', [1, 1, 1]), ('110', [1, 1, 0]), ('123', [1, 2, 3])]
    r31 = np.random.default_rng(31).normal(size=(8, 3))
    roh += [('z%d' % i, v) for i, v in enumerate(r31)]
    r47 = np.random.default_rng(47).normal(size=(12, 3))
    roh += [('y%d' % i, v) for i, v in enumerate(r47)]
    out = []
    for nm, v in roh:
        m = np.asarray(v, float)
        m = m / np.linalg.norm(m)
        u = np.cross(m, [0.3, 0.5, 0.7])
        u = u / np.linalg.norm(u)
        w = np.cross(m, u)
        out.append((nm, m, np.outer(u + 1j * w, u + 1j * w)))
    return out


def zerlege(n, S):
    """S je Richtung n (nd,3): TT = Lambda_n[S], L = P S nn + nn S P, Rest = S - TT - L."""
    Nn = n[:, :, None] * n[:, None, :]
    P = np.eye(3)[None] - Nn
    PSP = P @ S @ P
    TT = PSP - 0.5 * P * np.einsum('dii->d', PSP)[:, None, None]
    L = P @ S @ Nn + Nn @ S @ P
    return TT, L, S[None] - TT - L


# ------------------------------------------------------------------------------------------------ Netz
def netz():
    mod = ew.baue('V')
    tder = pn.tet_ableitungen(mod)
    Q = np.zeros((mod['E'], 3, 3))
    for z, (K0, dK) in zip(mod['zellen'], tder):
        X0 = np.array(z['X8'], float) / 8.0
        for p, (e, T) in enumerate(z['kanten']):
            Q[e] += 0.5 * z['l'][p] * (X0.T @ dK[p] @ X0)
    SIG0 = np.stack([np.einsum('eij,ij->e', Q, T - np.trace(T) * np.eye(3)) for T in TB], 1)     # (E, 6)
    # KP1: Summe_e sigma_e n_e n_e^T = -V T fuer gleichfoermige Spannung (k = 0)
    kp1 = 0.0
    for b, T in enumerate(TB):
        lhs = np.einsum('e,ei,ej->ij', SIG0[:, b], mod['n'], mod['n'])
        kp1 = max(kp1, float(np.abs(lhs + VCELL * T).max()))
    vv = pn.eckvolumen(mod)
    return mod, SIG0, vv, kp1


def richtungen(nt, nphi):
    return pn.richtungen(nt, nphi)


def kl_lauf(mod, SIG0, vv, kl, ndir, punkte, chunk=50):
    """Alle Groessen bei festem kl fuer alle Richtungen und Gewichtspunkte."""
    s = kl / LP
    pos = np.array(mod['pos'])
    nd = len(ndir)
    E = mod['E']
    res = {'lamP': np.zeros(nd), 'newton': np.zeros(nd), 'summe_m_abs2': np.zeros(nd), 'sV1_konform': np.zeros(nd), 'rang': [], 'nV': mod['nV'],
           'KF_MB': 0.0, 'KR_cM': 0.0, 'KJ': 0.0}
    per = {nm: {'om2': np.zeros((nd, 3)), 'g0': np.zeros((nd, 2, 6), complex), 'gJ': np.zeros((nd, 2, 6), complex),
                'gV': np.zeros((nd, 2), complex), 'chol_ok': True} for nm in punkte}
    for i0 in range(0, nd, chunk):
        nn = ndir[i0:i0 + chunk]
        sl = slice(i0, i0 + len(nn))
        k = s * nn
        o = ew.ops(mod, k)
        B, M, c = o['B'], o['M'], o['c']
        res['KF_MB'] = max(res['KF_MB'], float(np.abs(cT(M) @ B).max() / (np.abs(M).max() * np.abs(B).max())))
        res['KR_cM'] = max(res['KR_cM'], float(np.abs(cT(c) @ M).max() / (np.abs(c).max() * np.abs(M).max())))
        U, sv, _ = np.linalg.svd(np.concatenate([M, c], -1))
        res['rang'] += [int(x) for x in np.unique((sv > 1e-9 * sv[..., :1]).sum(-1))]
        S = U[..., :, 40:]
        Bred = herm(cT(S) @ B @ S)
        # Takt P = W^H c = -W^H B W (Newton)
        W = mn.W_of(mod, k)
        P = herm(cT(W) @ c)
        res['lamP'][sl] = np.linalg.eigvalsh(P)[:, 0]
        m_u = (vv / VCELL)[None, :] * np.exp(1j * (k @ pos.T))                      # Energie 1 je Zelle
        res['newton'][sl] = np.real(np.einsum('kv,kv->k', np.conj(m_u), np.linalg.solve(P, m_u[..., None])[..., 0]))
        res['summe_m_abs2'][sl] = np.abs(m_u.sum(-1)) ** 2
        # V1-Einheitskraft
        cHc = cT(c) @ c
        ac = c @ np.linalg.solve(cHc, m_u[..., None])                                 # (k, E, 1)
        res['sV1_konform'][sl] = np.real(np.einsum('kv,kv->k', np.conj(m_u), (cT(W) @ ac)[..., 0]))
        fV = -(KG / KP) * (B @ ac)
        frV = cT(S) @ fV                                                               # (k, 28, 1)
        # Spannung, Impuls
        ph = np.exp(1j * (k @ mod['mitte'].T))                                         # (k, E)
        sig = ph[:, :, None] * SIG0[None]                                              # (k, E, 6)
        f0 = -(cT(S) @ sig)                                                            # (k, 28, 6)
        MhS = cT(M) @ sig
        PMsig = M @ np.linalg.solve(cT(M) @ M, MhS)
        res['KJ'] = max(res['KJ'], float(np.abs(cT(M) @ PMsig - MhS).max() / np.abs(MhS).max()))
        for nm, wv in punkte.items():
            J = dict(zip(ARTEN, wv))
            A = pn.A_J(mod, k, J)
            Ared = herm(cT(S) @ A @ S)
            try:
                L = np.linalg.cholesky(Ared)
            except np.linalg.LinAlgError:
                per[nm]['chol_ok'] = False
                continue
            om2, Uu = np.linalg.eigh(herm(cT(L) @ Bred @ L))
            X = L @ Uu[..., :2]
            fJ = -np.linalg.solve(Ared, cT(S) @ (A @ PMsig))
            XH = cT(X)
            per[nm]['om2'][sl] = om2[:, :3]
            per[nm]['g0'][sl] = XH @ f0
            per[nm]['gJ'][sl] = XH @ (f0 + fJ)
            per[nm]['gV'][sl] = (XH @ frV)[..., 0]
    res['rang'] = sorted(set(res['rang']))
    return res, per


def auswerten(ndir, wdir, kl, gem, pp):
    """G je Lage und Kanal, Gang, Spanne, Diagnosen fuer einen Gewichtspunkt bei einem kl."""
    k = kl / LP
    V = VCELL
    n, w = ndir, wdir
    om2 = pp['om2'][:, :2]
    c2 = om2 / k ** 2
    c0sq = float((w[:, None] * c2).sum() / (2.0 * w.sum()))
    eps = c0sq / c2
    fac = np.sqrt(c0sq / c2)
    GN = (8.0 * V / gem['nV']) / float((w * gem['lamP'] / k ** 2).sum() / w.sum())
    GN_direkt = float((w * (gem['newton'] * 8.0 * V * k ** 2 / gem['summe_m_abs2'])).sum() / w.sum())
    gJ, g0, gV = pp['gJ'], pp['g0'], pp['gV']

    def leistung(Amp):
        return float((w[:, None] * np.abs(Amp) ** 2 / om2 * fac).sum())

    lagen = []
    for nm, m, Sc in bahnnormalen():
        nSn = np.einsum('di,ij,dj->d', n, Sc, n)
        TT, L, Rn = zerlege(n, Sc)
        den = float((w * V * np.real(np.sum(TT * np.conj(TT), axis=(1, 2))) / k ** 2).sum())
        aTT = np.einsum('db,djb->dj', koef(TT), gJ)
        aL = np.einsum('db,djb->dj', koef(L), gJ)
        aR = np.einsum('db,djb->dj', koef(Rn), gJ)
        aV = eps * V * nSn[:, None] * gV
        a0 = np.einsum('db,djb->dj', koef(np.broadcast_to(Sc, TT.shape)), g0)
        z = {'name': nm, 'summe_m4': float((m ** 4).sum()),
             'TT': leistung(aTT) / den / GN, 'TTL': leistung(aTT + aL) / den / GN, 'S': leistung(aTT + aL + aR) / den / GN,
             'SV1': leistung(aTT + aL + aR + aV) / den / GN, 'ohneJ_S': leistung(a0) / den / GN,
             'ohneJ_SV1': leistung(a0 + aV) / den / GN,
             'SV1_lam2': leistung(aTT + aL + aR + 2.0 * aV) / den / GN, 'nurV1': leistung(aV) / den / GN}
        lagen.append(z)
    m4 = np.array([z['summe_m4'] for z in lagen])
    out = {'kl': kl, 'c0_quadrat': c0sq, 'tempo2_spanne': float(c2.max() / c2.min() - 1), 'G_N_ueber_G': GN,
           'G_N_ueber_G_direkt': GN_direkt, 'om2_luecke_min': float((pp['om2'][:, 2] / pp['om2'][:, 1]).min()),
           'lagen': lagen}
    st = {}
    for key in ('TT', 'TTL', 'S', 'SV1', 'ohneJ_S', 'ohneJ_SV1', 'SV1_lam2', 'nurV1'):
        G = np.array([z[key] for z in lagen])
        Am = np.stack([np.ones_like(m4), m4], 1)
        co, *_ = np.linalg.lstsq(Am, G, rcond=None)
        st[key] = {'min': float(G.min()), 'max': float(G.max()), 'spanne': float(G.max() - G.min()), 'sd': float(G.std(ddof=1)),
                   'mittel': float(G.mean()), 'gang': float(-co[1]), 'achse_a': float(co[0]),
                   'fitrest_max': float(np.abs(Am @ co - G).max()), 'max_abs_G_minus_1': float(np.abs(G - 1).max())}
    out['statistik'] = st
    # Gang als Funktion der V1-Skalierung lambda: b(lam) = b0 + b1 lam + b2 lam^2 aus lam = 0, 1, 2 (beschreibend)
    b0, b1_, b2_ = -st['S']['gang'], -st['SV1']['gang'], -st['SV1_lam2']['gang']
    q2 = 0.5 * (b2_ - 2 * b1_ + b0)
    q1 = b1_ - b0 - q2
    wurzeln = np.roots([q2, q1, b0]) if abs(q2) > 0 else np.array([-b0 / q1])
    reell = [float(np.real(r)) for r in wurzeln if abs(np.imag(r)) < 1e-9 * max(1.0, abs(np.real(r)))]
    out['lambda_gang_null'] = min(reell, key=lambda r: abs(r - 1.0)) if reell else None
    # Diagnose je Richtung: Einheitsquelle N = nn - P/2 (nn-Teil einer spurfreien Quelle mit n.S.n = 1)
    Nn = n[:, :, None] * n[:, None, :]
    Nq = Nn - 0.5 * (np.eye(3)[None] - Nn)
    a_nn = np.einsum('db,djb->dj', koef(Nq), gJ)
    a_v = eps * V * gV
    p_nn = (np.abs(a_nn) ** 2 / om2 * fac).sum(-1)
    p_res = (np.abs(a_nn + a_v) ** 2 / om2 * fac).sum(-1)
    p_v = (np.abs(a_v) ** 2 / om2 * fac).sum(-1)
    kreuz = (np.real(np.conj(a_v) * a_nn) / om2 * fac).sum(-1)
    out['nn_V1_diagnose'] = {'rest_anteil_leistung': float((w * p_res).sum() / (w * p_nn).sum()),
                             'lambda_opt': float(-(w * kreuz).sum() / (w * p_v).sum()),
                             'nn_leistung_mittel': float((w * p_nn).sum() / w.sum()),
                             'rest_leistung_mittel': float((w * p_res).sum() / w.sum()),
                             'imag_anteil_kreuz': float((w * (np.imag(np.conj(a_v) * a_nn) / om2 * fac).sum(-1)).sum() / (w * p_nn).sum())}
    return out


def netz_lauf(a):
    t0 = time.time()
    mod, SIG0, vv, kp1 = netz()
    ndir, wdir = richtungen(a.nt, a.nphi)
    punkte = gewichtspunkte(a.punkte)
    if a.nur:
        punkte = {k_: v for k_, v in punkte.items() if k_ in a.nur.split(',')}
    kls = [float(x) for x in a.kl.split(',')]
    out = {'E': mod['E'], 'nV': mod['nV'], 'nd': int(len(ndir)), 'nt': a.nt, 'nphi': a.nphi, 'punkte': punkte,
           'summe_eckvolumen': float(vv.sum()), 'KP1_affin_max': kp1, 'kl': {}}
    for kl in kls:
        t1 = time.time()
        gem, per = kl_lauf(mod, SIG0, vv, kl, ndir, punkte)
        z = {'rang': gem['rang'], 'KF_MB': gem['KF_MB'], 'KR_cM': gem['KR_cM'], 'KJ': gem['KJ'],
             'sV1_konform_min_max_k2': [float((gem['sV1_konform'] * (kl / LP) ** 2).min()), float((gem['sV1_konform'] * (kl / LP) ** 2).max())],
             'lamP_ueber_k2_min_max': [float((gem['lamP'] / (kl / LP) ** 2).min()), float((gem['lamP'] / (kl / LP) ** 2).max())],
             'punkte': {}}
        for nm in punkte:
            if not per[nm]['chol_ok']:
                z['punkte'][nm] = {'chol_ok': False}
                continue
            r = auswerten(ndir, wdir, kl, gem, per[nm])
            r['chol_ok'] = True
            z['punkte'][nm] = r
        z['t_s'] = time.time() - t1
        out['kl']['%g' % kl] = z
        print('kl %g fertig, %.1f s' % (kl, z['t_s']), flush=True)
    out['t_s'] = time.time() - t0
    return out


# ------------------------------------------------------------------------------------------------ Urteile und Bild
def pearson(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    return float(np.corrcoef(x, y)[0, 1])


def aus(a):
    with open(a.haupt) as fh:
        H = json.load(fh)['ergebnis']
    with open(a.kurve) as fh:
        K = json.load(fh)['ergebnis']
    Qd = None
    if a.quad:
        with open(a.quad) as fh:
            Qd = json.load(fh)['ergebnis']
    with open(a.ref) as fh:
        ref = json.load(fh)
    res = {'eingaben': {os.path.basename(p): sha(p) for p in [a.haupt, a.kurve, a.ref] + ([a.quad] if a.quad else [])}}
    U = {}
    NE = 'nicht entscheidbar'
    # VA0
    h01 = H['kl']['0.01']['punkte']['J_iso']
    G = {z['name']: z['SV1'] for z in h01['lagen']}
    abw = {nm: G[nm] - ref['glas_V_Jiso_kl001'][nm]['SV1J'] for nm in G}
    gmin, gmax = min(G.values()), max(G.values())
    plan0 = max(abs(x) for x in abw.values()) <= 2e-6
    wort0 = abs(gmin - 0.999985) <= 2e-6 and abs(gmax - 1.000003) <= 2e-6
    U['VA0'] = {'min': gmin, 'max': gmax, 'abw_je_lage_max': max(abs(x) for x in abw.values()), 'abw_je_lage': abw,
                'plan': 'eingetroffen' if plan0 else 'nicht eingetroffen', 'kartenwortlaut': 'eingetroffen' if wort0 else 'nicht eingetroffen'}
    # VA1
    sp = {kl: H['kl'][kl]['punkte']['F1_exakt']['statistik']['SV1']['spanne'] for kl in H['kl'] if 'F1_exakt' in H['kl'][kl]['punkte']}
    gang = {kl: H['kl'][kl]['punkte']['F1_exakt']['statistik']['SV1']['gang'] for kl in H['kl'] if 'F1_exakt' in H['kl'][kl]['punkte']}
    b0 = (4.0 * gang['0.005'] - gang['0.01']) / 3.0 if ('0.005' in gang and '0.01' in gang) else None
    quad_ok = True
    dq = None
    if Qd is not None and 'F1_exakt' in Qd['kl']['0.01']['punkte']:
        dq = abs(Qd['kl']['0.01']['punkte']['F1_exakt']['statistik']['SV1']['spanne'] - sp['0.01'])
        quad_ok = dq <= 5e-7
    wort1 = sp['0.01'] < 1e-6
    plan1 = (b0 is not None) and (2.0 / 3.0 * abs(b0) < 1e-6) and wort1
    U['VA1'] = {'spanne_je_kl': sp, 'gang_je_kl': gang, 'gang_k0_extrapoliert': b0,
                'spanne_k0_extrapoliert': (2.0 / 3.0 * abs(b0)) if b0 is not None else None, 'quadratur_diff_spanne': dq,
                'kartenwortlaut': ('eingetroffen' if wort1 else 'nicht eingetroffen') if quad_ok else NE,
                'plan': ('eingetroffen' if plan1 else 'nicht eingetroffen') if quad_ok else NE}
    # VA2
    sp2 = {kl: H['kl'][kl]['punkte']['J1']['statistik']['SV1']['spanne'] for kl in H['kl'] if 'J1' in H['kl'][kl]['punkte']}
    wort2 = sp2['0.01'] > 1e-3
    plan2 = all(sp2[kl] > 1e-3 for kl in ('0.005', '0.01', '0.02') if kl in sp2) and wort2
    G1 = {z['name']: z['SV1'] for z in H['kl']['0.01']['punkte']['J1']['lagen']}
    U['VA2'] = {'spanne_je_kl': sp2, 'sd_kl001': H['kl']['0.01']['punkte']['J1']['statistik']['SV1']['sd'],
                'abw_glas_je_lage_max': max(abs(G1[nm] - ref['glas_V_J1_kl001'][nm]) for nm in G1),
                'kartenwortlaut': 'eingetroffen' if wort2 else 'nicht eingetroffen', 'plan': 'eingetroffen' if plan2 else 'nicht eingetroffen'}
    # VA3: Kurve dTT = 0 (18 Gitterpunkte + exakter Punkt), kl = 0.01
    tt0 = {('K%+.1f' % z['x'][0]): z['tt_spanne0'] for z in ref['smi_kurve_dTT0']}
    tt0['F1_exakt'] = ref['smi_F1_exakt']['tt_spanne0']
    kp = K['kl']['0.01']['punkte']
    namen = [nm for nm in tt0 if nm in kp and kp[nm].get('chol_ok')]
    rest = [kp[nm]['statistik']['SV1']['spanne'] for nm in namen]
    xs = [tt0[nm] for nm in namen]
    if len(namen) >= 5:
        r_lin = pearson(xs, rest)
        r_log = pearson(np.log10(xs), np.log10(rest))
        stg = float(np.polyfit(np.log10(xs), np.log10(rest), 1)[0])
        wort3 = r_lin >= 0.9
        plan3 = wort3 and r_log >= 0.9 and 0.5 <= stg <= 1.5
        U['VA3'] = {'punkte': namen, 'tt_spanne0': xs, 'rest_spanne_SV1': rest, 'pearson_lin': r_lin, 'pearson_log': r_log,
                    'steigung_loglog': stg, 'kartenwortlaut': 'eingetroffen' if wort3 else 'nicht eingetroffen',
                    'plan': 'eingetroffen' if plan3 else 'nicht eingetroffen'}
        # beschreibend: ohne den exakten Punkt
        n2 = [nm for nm in namen if nm != 'F1_exakt']
        U['VA3']['ohne_exakt'] = {'pearson_lin': pearson([tt0[x] for x in n2], [kp[x]['statistik']['SV1']['spanne'] for x in n2]),
                                  'pearson_log': pearson(np.log10([tt0[x] for x in n2]), np.log10([kp[x]['statistik']['SV1']['spanne'] for x in n2]))}
    else:
        U['VA3'] = {'plan': NE, 'kartenwortlaut': NE, 'punkte': namen}
    res['urteile'] = U
    # Tabellen
    tab = {}
    for quelle, D in (('haupt', H), ('kurve', K)):
        for kl, z in D['kl'].items():
            for nm, r in z['punkte'].items():
                if not r.get('chol_ok'):
                    continue
                st = r['statistik']
                tab.setdefault(nm, {})[kl] = {'quelle': quelle, 'SV1': st['SV1'], 'S': st['S'], 'TT': st['TT'], 'TTL': st['TTL'],
                                              'ohneJ_S': st['ohneJ_S'], 'c0_quadrat': r['c0_quadrat'],
                                              'tempo2_spanne': r['tempo2_spanne'], 'G_N_ueber_G': r['G_N_ueber_G'],
                                              'G_N_ueber_G_direkt': r['G_N_ueber_G_direkt'], 'lambda_gang_null': r['lambda_gang_null'],
                                              'nn_V1_diagnose': r['nn_V1_diagnose'], 'om2_luecke_min': r['om2_luecke_min']}
    res['tabelle'] = tab
    if Qd is not None:
        res['quadratur'] = {nm: {'spanne_SV1': r['statistik']['SV1']['spanne'], 'gang_SV1': r['statistik']['SV1']['gang'],
                                 'gang_S': r['statistik']['S']['gang'], 'TT_mittel': r['statistik']['TT']['mittel']}
                            for nm, r in Qd['kl']['0.01']['punkte'].items() if r.get('chol_ok')}
    res['kontrollen'] = {D_n: {kl: {k_: z[k_] for k_ in ('rang', 'KF_MB', 'KR_cM', 'KJ', 'sV1_konform_min_max_k2', 'lamP_ueber_k2_min_max')}
                               for kl, z in D['kl'].items()} for D_n, D in (('haupt', H), ('kurve', K))}
    res['kontrollen']['KP1_affin_max'] = H['KP1_affin_max']
    if a.bild:
        bild(H, K, ref, U, a.bild)
        res['bild'] = os.path.basename(a.bild)
    with open(a.out + '.tmp', 'w') as fh:
        json.dump(res, fh, indent=1)
    os.replace(a.out + '.tmp', a.out)
    return res


def bild(H, K, ref, U, pfad):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(1, 3, figsize=(19, 5.8))
    farbe = {'J_iso': '#1f77b4', 'F1_exakt': '#2ca02c', 'J1': '#d62728'}
    nameL = {'J_iso': 'J_iso (TT-ISO-1)', 'F1_exakt': 'exakter TT-Punkt (SKALAR-MISCH-1)', 'J1': 'J = 1'}
    for nm in ('J_iso', 'F1_exakt', 'J1'):
        r = H['kl']['0.01']['punkte'][nm]
        m4 = np.array([z['summe_m4'] for z in r['lagen']])
        o = np.argsort(m4)
        ax[0].plot(m4[o], (np.array([z['S'] for z in r['lagen']])[o] - 1) * 1e3, 'o--', ms=3, color=farbe[nm], alpha=0.6,
                   label='%s, ohne V1 (S+J)' % nameL[nm])
        ax[0].plot(m4[o], (np.array([z['SV1'] for z in r['lagen']])[o] - 1) * 1e3, 's-', ms=3, color=farbe[nm],
                   label='%s, mit V1 (V1+S+J)' % nameL[nm])
    ax[0].axhspan(-0.13, 0.13, color='gray', alpha=0.2, label='Doppelpulsar +-1,3e-4')
    ax[0].axhline(0, color='k', lw=0.6)
    ax[0].set_xlabel('Summe m_i^4 der Bahnnormale (24 Lagen)')
    ax[0].set_ylabel('(G_rad/G_N - 1) x 1e3   (kl = 0,01)')
    ax[0].set_title('G_rad/G_N je Bahnlage, mit und ohne V1')
    ax[0].legend(fontsize=6.5)
    for nm in ('J_iso', 'F1_exakt'):
        for kl, mk in (('0.005', 'o'), ('0.01', 's'), ('0.02', '^')):
            if kl not in H['kl'] or nm not in H['kl'][kl]['punkte']:
                continue
            r = H['kl'][kl]['punkte'][nm]
            m4 = np.array([z['summe_m4'] for z in r['lagen']])
            G = np.array([z['SV1'] for z in r['lagen']])
            o = np.argsort(m4)
            ax[1].plot(m4[o], (G[o] - G.mean()) * 1e6, mk + '-', ms=3, color=farbe[nm], alpha=0.8,
                       label='%s, kl = %s' % (nameL[nm], kl))
    ax[1].axhspan(-0.5, 0.5, color='orange', alpha=0.25, label='Spanne 1e-6 (VA1-Schwelle)')
    ax[1].set_xlabel('Summe m_i^4')
    ax[1].set_ylabel('(G - Lagenmittel) x 1e6, mit V1')
    ax[1].set_title('Lagengang mit V1 (Ausschnitt)')
    ax[1].legend(fontsize=6.5)
    tt0 = {('K%+.1f' % z['x'][0]): z['tt_spanne0'] for z in ref['smi_kurve_dTT0']}
    tt0['F1_exakt'] = ref['smi_F1_exakt']['tt_spanne0']
    kp = K['kl']['0.01']['punkte']
    nm_ = [x for x in tt0 if x in kp and kp[x].get('chol_ok')]
    ax[2].loglog([tt0[x] for x in nm_], [kp[x]['statistik']['SV1']['spanne'] for x in nm_], 'ko', ms=5,
                 label='Kurve E = T2, mit V1 (Spanne 24 Lagen)')
    ax[2].loglog([tt0[x] for x in nm_], [kp[x]['statistik']['S']['spanne'] for x in nm_], 'x', color='gray', ms=5,
                 label='Kurve E = T2, ohne V1')
    ja = H['kl']['0.01']['punkte']['J_iso']['statistik']
    ax[2].loglog([ref['smi_J_iso']['tt_spanne0']], [ja['SV1']['spanne']], 'D', color=farbe['J_iso'], ms=7, label='J_iso, mit V1')
    xx = np.array([1e-11, 1e-3])
    ax[2].loglog(xx, xx, 'b:', lw=1, label='Rest = TT-Spanne')
    ax[2].axhline(1.3e-4, color='#d62728', ls='--', lw=0.8, label='1,3e-4 (Doppelpulsar)')
    ax[2].set_xlabel('TT-Spanne langwellig (SKALAR-MISCH-1, TT_0)')
    ax[2].set_ylabel('Lagen-Spanne von G_rad/G_N (kl = 0,01)')
    ax[2].set_title('Rest gegen TT-Spanne (VA3)')
    ax[2].legend(fontsize=6.5)
    fig.suptitle('V1-AUFHEBUNG-1: Kreisbahnen auf Netz V mit Energiekanal V1 (synthetische Gitterrechnung, keine Messdaten)')
    fig.tight_layout()
    fig.savefig(pfad + '.tmp.png', dpi=110)
    os.replace(pfad + '.tmp.png', pfad)


# ------------------------------------------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['netz', 'aus'])
    ap.add_argument('--punkte', default='haupt')
    ap.add_argument('--nur', default='')
    ap.add_argument('--kl', default='0.01')
    ap.add_argument('--nt', type=int, default=10)
    ap.add_argument('--nphi', type=int, default=20)
    ap.add_argument('--rauch', action='store_true')
    ap.add_argument('--haupt')
    ap.add_argument('--kurve')
    ap.add_argument('--quad')
    ap.add_argument('--ref')
    ap.add_argument('--bild')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    info = {'numpy': np.__version__, 'python': platform.python_version(), 'host': platform.node(), 'argv': sys.argv,
            'skript_sha256': sha(os.path.abspath(__file__)), 'ew_sha256': sha(os.path.abspath(ew.__file__)),
            'pn_sha256': sha(os.path.abspath(pn.__file__)), 'mn_sha256': sha(os.path.abspath(mn.__file__)),
            'tp_sha256': sha(os.path.abspath(ew.tp.__file__)), 'referenz_sha256': sha(os.path.join(HERE, 'referenz.json')),
            'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    if a.modus == 'aus':
        aus(a)
        print('fertig aus, %.1f s' % (time.time() - t0), flush=True)
        return
    erg = netz_lauf(a)
    res = {'info': info, 'ergebnis': erg, 'laufzeit_s': time.time() - t0,
           'maxrss_MB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
           'ende_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    if a.rauch:
        res['rauch'] = True          # Rauchtest: Werte werden nicht gelesen (nur rc, Laufzeit, Speicher, Schluessel)
    with open(a.out + '.tmp', 'w') as fh:
        json.dump(res, fh, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
    os.replace(a.out + '.tmp', a.out)
    print('fertig netz, %.1f s' % (time.time() - t0), flush=True)


if __name__ == '__main__':
    main()
