#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PUMPE-NETZ-1, Runde 46 (fmhc-physics), Code-Agent fuer die Leitung claude-primary.

Strahlt Finns gefuelltes Hamilton-Netz (ew.py, V, Paarung A1R1) TT-Wellen ab, wenn Materie schwingt?
  V1: Energie der Materie nur in der skalaren Regel je Ecke (kappa' c^H a = m), kappa' = kappa_g/2.
  S : zusaetzlich Spannungskopplung eines Skalarfelds phi mit Hodge-Gewichten (P1-Form je Tetraeder) an alle Kanten.
Lineare Antwort im Frequenzbereich, R1 wie ew.py:
  a = S x + a_c, a_c = c (c^H c)^-1 m/kappa',  x' = A_red y/kappa_g,  y' = -kappa_g B_red x + S^H f,
  f_V1 = -(kappa_g/kappa') B c (c^H c)^-1 m,  f_S = -sigma (Kantenkraft der phi-Spannung).
Leistung per Goldener Regel auf der Massenschale der zwei TT-Zweige; Bezug: linearisierte Einstein-Theorie mit
derselben Quelle (P_E), statische TT-Kopplung (unabhaengig von A).
G = 1, kappa_g = 1/(8 pi), kappa' = kappa_g/2; Laengen kubisch (l_P = sqrt2/4), Zeit in ew-Einheiten (omega^2 = eig A_red B_red).
Aufruf nur ueber kleintest.sh auf der .69:
  python pn.py lauf --out lauf/pn.json [--rauch]
  python pn.py bild --ein lauf/pn.json --bild lauf/bild-pumpe-netz.png --out lauf/bild.json
"""
import argparse, json, sys, time, platform, os, resource, hashlib, math
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ew  # noqa: E402  (EINE-WELT-LOCH-1, unveraendert)
import mn  # noqa: E402  (MATERIE-NETZ-1, unveraendert; nur W_of, LP, VCELL)

LP = mn.LP
VCELL = mn.VCELL
GN = 1.0
KG = 1.0 / (8.0 * math.pi * GN)
KP = KG / 2.0
XK = -1.0453267293049897
XS = -0.0010098244011669793
J_ISO = {'finn_auf': 1.0, 'finn_ab': 1.0, 'kegel_T1': 10.0 ** XK, 'kegel_T2': 10.0 ** XK,
         'sechs_T1': 10.0 ** XS, 'sechs_T2': 10.0 ** XS}
ACHSEN = [('001', [0.0, 0.0, 1.0]), ('111', [1.0, 1.0, 1.0]), ('123', [1.0, 2.0, 3.0])]
W_LP, D_LP = 0.8, 0.8
KL_AUS = [0.01, 0.02, 0.05, 0.1, 0.15, 0.2, 0.3, 0.5, 0.8]


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def cT(X):
    return np.conj(np.swapaxes(X, -1, -2))


def herm(X):
    return 0.5 * (X + cT(X))


def richtungen(nt=10, nphi=20):
    mu, wmu = np.polynomial.legendre.leggauss(nt)
    ph = 2 * np.pi * (np.arange(nphi) + 0.5) / nphi
    Mu, Ph = np.meshgrid(mu, ph, indexing='ij')
    st = np.sqrt(1 - Mu ** 2)
    n = np.stack([st * np.cos(Ph), st * np.sin(Ph), Mu], -1).reshape(-1, 3)
    w = (wmu[:, None] * np.full(nphi, 2 * np.pi / nphi)[None, :]).reshape(-1)
    return n, w


def A_J(mod, k, J):
    """A1 mit Gewicht J je Tetraeder-Art (wie ew.ops, Teil A)."""
    sh = k.shape[:-1]
    E = mod['E']
    A = np.zeros(sh + (E, E), complex)
    for z in mod['zellen']:
        if not z['kin']:
            continue
        wz = J[z['art']]
        ph = [np.exp(1j * (k @ T)) for (e, T) in z['kanten']]
        idx = [e for (e, T) in z['kanten']]
        A0 = z['A0']
        for i in range(len(idx)):
            pci = np.conj(ph[i])
            for j in range(len(idx)):
                A[..., idx[i], idx[j]] += wz * A0[i, j] * pci * ph[j]
    return A


def eckvolumen(mod):
    vv = np.zeros(mod['nV'])
    for z in mod['zellen']:
        for (s, n) in z['ids']:
            vv[s] += z['vol'] / 4.0
    return vv


# ------------------------------------------------------------------------------------------------ P1 (Hodge) je Tetraeder
DMAT = np.array([[-1, 1, 0, 0], [-1, 0, 1, 0], [-1, 0, 0, 1]], float)


def K_aus_laengen(paare, lv):
    """P1-Steifigkeit K (4x4) eines Tetraeders aus 6 Kantenlaengen (komplex erlaubt): E = (1/2) phi^T K phi."""
    L2 = {}
    for p, (i, j) in enumerate(paare):
        L2[(i, j)] = lv[p] ** 2
        L2[(j, i)] = lv[p] ** 2
    g = np.zeros((3, 3), complex)
    for a in range(1, 4):
        for b in range(1, 4):
            lab = 0.0 if a == b else L2[(a, b)]
            g[a - 1, b - 1] = 0.5 * (L2[(0, a)] + L2[(0, b)] - lab)
    V = np.sqrt(np.linalg.det(g)) / 6.0
    return V * (DMAT.T @ np.linalg.inv(g) @ DMAT)


def tet_ableitungen(mod):
    """Je Tetraeder-Typ: K0 und dK/dl_p (komplexer Schritt)."""
    out = []
    h = 1e-20
    for z in mod['zellen']:
        l0 = np.array(z['l'], float)
        K0 = np.real(K_aus_laengen(z['paare'], l0.astype(complex)))
        dK = np.zeros((6, 4, 4))
        for p in range(6):
            lv = l0.astype(complex)
            lv[p] += 1j * h
            dK[p] = np.imag(K_aus_laengen(z['paare'], lv)) / h
        out.append((K0, dK))
    return out


def kontrolle_p1(mod, tder, seed=17):
    """Gleichfoermiges grad phi: Energie je Zelle und Summe sigma_e n_e n_e^T gegen -V_Zelle T."""
    rng = np.random.default_rng(seed)
    res = {'energie_rel_max': 0.0, 'spannung_rel_max': 0.0}
    for _ in range(3):
        G0 = rng.normal(size=3)
        Ez = 0.0
        sig = np.zeros(mod['E'])
        for z, (K0, dK) in zip(mod['zellen'], tder):
            X0 = np.array(z['X8'], float) / 8.0
            ph = X0 @ G0
            Ez += 0.5 * ph @ K0 @ ph
            for p, (e, T) in enumerate(z['kanten']):
                sig[e] += z['l'][p] * 0.5 * ph @ dK[p] @ ph
        Tm = np.outer(G0, G0) - 0.5 * (G0 @ G0) * np.eye(3)
        lhs = np.einsum('e,ei,ej->ij', sig, mod['n'], mod['n'])
        res['energie_rel_max'] = max(res['energie_rel_max'], abs(Ez - 0.5 * (G0 @ G0) * VCELL) / (0.5 * (G0 @ G0) * VCELL))
        res['spannung_rel_max'] = max(res['spannung_rel_max'], float(np.abs(lhs + VCELL * Tm).max() / np.abs(VCELL * Tm).max()))
    return res


def quelle(mod, tder, achse, w=W_LP * LP, d=D_LP * LP, rbox=3.2, nmax=8):
    """phi = g(x - x_c - d e) - g(x - x_c + d e) (zwei gegenphasige Klumpen); Kantenkraefte sigma_e(R) und Spannung je Tetraeder."""
    pos = np.array(mod['pos'])
    x_c = pos[0]
    e = np.array(achse, float)
    e /= np.linalg.norm(e)
    xp, xm = x_c + d * e, x_c - d * e

    def phi(X):
        return np.exp(-((X - xp) ** 2).sum(-1) / (2 * w * w)) - np.exp(-((X - xm) ** 2).sum(-1) / (2 * w * w))
    g = np.arange(-nmax, nmax + 1)
    nn = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1).reshape(-1, 3)
    R = nn @ ew.AV
    sel = np.linalg.norm(R - x_c, axis=1) <= rbox
    nn, R = nn[sel], R[sel]
    AVinv = np.linalg.inv(ew.AV)
    keys, es, vals = [], [], []
    xt, Vt, Tt = [], [], []
    for z, (K0, dK) in zip(mod['zellen'], tder):
        X0 = np.array(z['X8'], float) / 8.0
        Xall = R[:, None, :] + X0[None]
        ph = phi(Xall)
        sp = 0.5 * np.einsum('ca,pab,cb->cp', ph, dK, ph) * np.array(z['l'])[None, :]
        for p, (eidx, T) in enumerate(z['kanten']):
            nT = np.rint(T @ AVinv).astype(int)
            keys.append(nn + nT[None, :])
            es.append(np.full(len(nn), eidx))
            vals.append(sp[:, p])
        Ev = X0[1:] - X0[0]
        dphi = ph[:, 1:] - ph[:, :1]
        grad = np.linalg.solve(Ev, dphi.T).T
        T = grad[:, :, None] * grad[:, None, :] - 0.5 * (grad ** 2).sum(-1)[:, None, None] * np.eye(3)[None]
        xt.append(Xall.mean(1))
        Vt.append(np.full(len(nn), z['vol']))
        Tt.append(T)
    keys = np.concatenate(keys, 0)
    es = np.concatenate(es)
    vals = np.concatenate(vals)
    cells, inv = np.unique(keys, axis=0, return_inverse=True)
    sigR = np.zeros((len(cells), mod['E']))
    np.add.at(sigR, (inv.ravel(), es), vals)
    xt = np.concatenate(xt, 0)
    Vt = np.concatenate(Vt)
    Tt = np.concatenate(Tt, 0)
    S0 = np.einsum('t,tij->ij', Vt, Tt)
    # Rand: Anteil der Spannung in Tetraedern nahe am Kastenrand (Abschneidekontrolle)
    rr = np.linalg.norm(xt - x_c, axis=1)
    rand = float(np.abs(Vt[rr > rbox - 0.6, None, None] * Tt[rr > rbox - 0.6]).sum() / np.abs(Vt[:, None, None] * Tt).sum())
    return {'achse': e, 'Rcells': cells @ ew.AV, 'sigR': sigR, 'xt': xt, 'VT': (Vt[:, None, None] * Tt).reshape(-1, 9),
            'S0': S0, 'x_c': x_c, 'rand_anteil': rand, 'n_zellen': int(len(nn)), 'n_tet': int(len(Vt)),
            'phi_max': float(np.abs(phi(R[:, None, :] + pos[None])).max())}


def S_tilde(q, k):
    """Kontinuum-Spannung der Quelle bei k: Summe_t V_t T_t e^(-i k.x_t), (nk, 3, 3)."""
    ph = np.exp(-1j * (k @ q['xt'].T))
    return (ph @ q['VT']).reshape(-1, 3, 3)


def lam_kontrakt(n, S):
    """Lambda_n[S] : S^* je Richtung (n: (nk,3), S: (nk,3,3) komplex)."""
    P = np.eye(3)[None] - n[:, :, None] * n[:, None, :]
    PSP = P @ S @ P
    tr = np.einsum('kii->k', P @ S)
    return np.real(np.einsum('kij,kij->k', PSP, np.conj(PSP)) - 0.5 * np.abs(tr) ** 2)


def tf(S):
    return S - np.trace(S) / 3.0 * np.eye(3)


# ------------------------------------------------------------------------------------------------ Hauptlauf
def lauf(rauch=False, nt=10, nphi=20, w_lP=W_LP, d_lP=D_LP):
    t0 = time.time()
    mod = ew.baue('V')
    E, nV = mod['E'], mod['nV']
    pos = np.array(mod['pos'])
    vv = eckvolumen(mod)
    if rauch:
        ndir, wdir = richtungen(4, 6)
        kl_grid = np.geomspace(0.005, 1.0, 6)
    else:
        ndir, wdir = richtungen(nt, nphi)
        kl_grid = np.geomspace(0.005, 1.0, 28)
    nd = len(ndir)
    tder = tet_ableitungen(mod)
    out = {'nd': nd, 'kl_grid': kl_grid.tolist(), 'w_lP': w_lP, 'd_lP': d_lP, 'nt': nt, 'nphi': nphi, 'J_iso': J_ISO, 'G': GN, 'kappa_g': KG,
           'kappa_strich': KP, 'kontrollen': {'P1': kontrolle_p1(mod, tder)}}
    quellen = []
    for nm, ach in ACHSEN:
        q = quelle(mod, tder, ach, w=w_lP * LP, d=d_lP * LP)
        q['name'] = nm
        quellen.append(q)
    out['quellen'] = {q['name']: {'achse': q['achse'].tolist(), 'S0': q['S0'].tolist(), 'S0_TF_norm': float(np.linalg.norm(tf(q['S0']))),
                                  'S0_spur': float(np.trace(q['S0'])), 'rand_anteil': q['rand_anteil'], 'n_zellen': q['n_zellen'],
                                  'n_tet': q['n_tet'], 'n_sig_zellen': int(len(q['Rcells'])), 'phi_max': q['phi_max']} for q in quellen}
    t_quelle = time.time() - t0
    nq = len(quellen)
    Jvar = [('iso', J_ISO), ('eins', None)]
    nk = len(kl_grid)
    # Speicher
    lam = np.zeros((nk, nd, 3))
    Cst = {x: np.zeros((nk, nq, nd)) for x in ('S', 'V1', 'V1S', 'E')}
    dyn = {jn: {'Om2': np.zeros((nk, nd, 3)), 'gS': np.zeros((nk, nq, nd, 2), complex), 'gV': np.zeros((nk, nd, 2), complex)}
           for jn, _ in Jvar}
    nnS = np.zeros((nk, nq, nd), complex)
    rang = []
    kd = {'cM_rel_max': 0.0, 'A_J_eins_gegen_ew_max': 0.0, 'chol_ok': True}
    for ik, kl in enumerate(kl_grid):
        s = kl / LP
        k = s * ndir
        o = ew.ops(mod, k)
        B, A1, M, c = o['B'], o['A'], o['M'], o['c']
        kd['cM_rel_max'] = max(kd['cM_rel_max'], float(np.abs(cT(c) @ M).max() / (np.abs(c).max() * np.abs(M).max())))
        N = np.concatenate([M, c], -1)
        U, sv, _ = np.linalg.svd(N)
        r = (sv > 1e-9 * sv[:, :1]).sum(-1)
        rang += [int(x) for x in np.unique(r)]
        S = U[:, :, 40:]
        Bred = herm(cT(S) @ B @ S)
        lb, Vb = np.linalg.eigh(Bred)
        lam[ik] = lb[:, :3]
        # V1-Einheitskraft (eps~ = 1): m_v = (V_v/V_Zelle) e^{i k.p_v}
        m_u = (vv / VCELL)[None, :] * np.exp(1j * (k @ pos.T))
        cHc = cT(c) @ c
        ac = c @ np.linalg.solve(cHc, m_u[..., None])
        fV = -(KG / KP) * (B @ ac)[..., 0]
        frV = (cT(S) @ fV[..., None])[..., 0]
        frS = []
        for iq, q in enumerate(quellen):
            sig = np.exp(-1j * (k @ q['Rcells'].T)) @ q['sigR']
            frS.append((cT(S) @ (-sig)[..., None])[..., 0])
            St = S_tilde(q, k)
            nnS[ik, iq] = np.einsum('ki,kij,kj->k', ndir, St, ndir)
            Cst['E'][ik, iq] = 4.0 * lam_kontrakt(ndir, St) / s ** 2
            for x, f in (('S', frS[iq]), ('V1', nnS[ik, iq][:, None] * frV), ('V1S', frS[iq] + nnS[ik, iq][:, None] * frV)):
                pr = np.einsum('kaj,ka->kj', np.conj(Vb[:, :, :2]), f)
                Cst[x][ik, iq] = (np.abs(pr) ** 2 / lb[:, :2]).sum(-1)
        for jn, J in Jvar:
            A = A1 if J is None else A_J(mod, k, J)
            if J is not None and ik == 0:
                Aeins = A_J(mod, k, {a: 1.0 for a in J})
                kd['A_J_eins_gegen_ew_max'] = float(np.abs(Aeins - A1).max() / np.abs(A1).max())
            Ared = herm(cT(S) @ A @ S)
            try:
                L = np.linalg.cholesky(Ared)
            except np.linalg.LinAlgError:
                kd['chol_ok'] = False
                raise
            Dm = herm(cT(L) @ Bred @ L)
            om2, Uu = np.linalg.eigh(Dm)
            dyn[jn]['Om2'][ik] = om2[:, :3]
            X = L @ Uu[:, :, :2]
            dyn[jn]['gV'][ik] = np.einsum('kaj,ka->kj', np.conj(X), frV)
            for iq in range(nq):
                dyn[jn]['gS'][ik, iq] = np.einsum('kaj,ka->kj', np.conj(X), frS[iq])
    t_k = time.time() - t0 - t_quelle
    kd['rang_MC'] = sorted(set(rang))
    out['kontrollen'].update(kd)
    # c_0 je J (kleinstes kl, Mittel ueber Richtungen und beide Zweige)
    s0 = kl_grid[0] / LP
    c0 = {jn: float(np.sqrt(dyn[jn]['Om2'][0, :, :2].mean() / s0 ** 2)) for jn, _ in Jvar}
    out['c0'] = c0
    out['Om2_ueber_k2_kl0'] = {jn: {'min': float((dyn[jn]['Om2'][0, :, :2] / s0 ** 2).min()), 'max': float((dyn[jn]['Om2'][0, :, :2] / s0 ** 2).max()),
                                    'luecke_3_ueber_2_min': float((dyn[jn]['Om2'][0, :, 2] / dyn[jn]['Om2'][0, :, 1]).min())} for jn, _ in Jvar}
    out['B_red_weich_ueber_k2_kl0'] = {'min': float((lam[0, :, :2] / s0 ** 2).min()), 'max': float((lam[0, :, :2] / s0 ** 2).max()),
                                       'luecke_3_ueber_2_min': float((lam[0, :, 2] / lam[0, :, 1]).min())}
    # ---------------------------------------------------------------- Massenschale und Leistung
    ls = np.log(kl_grid / LP)
    pref = (math.pi / (4 * KG)) * VCELL / (2 * math.pi) ** 3

    def interp_log(xq, xs, ys):
        return np.interp(xq, xs, ys, left=np.nan, right=np.nan)
    tab = {}
    for jn, _ in Jvar:
        Om2 = dyn[jn]['Om2']
        tab[jn] = {}
        for iq, q in enumerate(quellen):
            zeilen = []
            for klt in KL_AUS:
                om = c0[jn] * klt / LP
                Pd = {'S': np.zeros(nd), 'V1': np.zeros(nd), 'V1S': np.zeros(nd)}
                bad = 0
                zw = range(1) if jn == 'iso' else range(2)
                for d_ in range(nd):
                    for jz in zw:
                        if jn == 'iso':
                            Om = np.sqrt(Om2[:, d_, :2].mean(-1))
                            eps = (c0[jn] ** 2) * (kl_grid / LP) ** 2 / Om ** 2 * nnS[:, iq, d_]
                            gS2 = (np.abs(dyn[jn]['gS'][:, iq, d_, :]) ** 2).sum(-1)
                            gV2 = (np.abs(eps[:, None] * dyn[jn]['gV'][:, d_, :]) ** 2).sum(-1)
                            gVS2 = (np.abs(dyn[jn]['gS'][:, iq, d_, :] + eps[:, None] * dyn[jn]['gV'][:, d_, :]) ** 2).sum(-1)
                        else:
                            Om = np.sqrt(Om2[:, d_, jz])
                            eps = (c0[jn] ** 2) * (kl_grid / LP) ** 2 / Om ** 2 * nnS[:, iq, d_]
                            gS2 = np.abs(dyn[jn]['gS'][:, iq, d_, jz]) ** 2
                            gV2 = np.abs(eps * dyn[jn]['gV'][:, d_, jz]) ** 2
                            gVS2 = np.abs(dyn[jn]['gS'][:, iq, d_, jz] + eps * dyn[jn]['gV'][:, d_, jz]) ** 2
                        lo = np.log(Om)
                        if np.any(np.diff(lo) <= 0):
                            bad += 1
                        so = interp_log(np.log(om), lo, ls)
                        if not np.isfinite(so):
                            bad += 1
                            continue
                        dlo = np.gradient(lo, ls)
                        slope = np.interp(so, ls, dlo)
                        s_on = math.exp(so)
                        v = om / s_on * slope
                        for x, gg in (('S', gS2), ('V1', gV2), ('V1S', gVS2)):
                            val = math.exp(np.interp(so, ls, np.log(np.maximum(gg, 1e-300))))
                            Pd[x][d_] += pref * s_on ** 2 / v * val
                P = {x: float((wdir * Pd[x]).sum()) for x in Pd}
                kE = klt / LP
                StE = S_tilde(q, kE * ndir)
                lamE = lam_kontrakt(ndir, StE)
                PE = float(GN * om ** 2 / (4 * math.pi * c0[jn]) * (wdir * lamE).sum())
                Pq = float(2 * GN * om ** 2 / (5 * c0[jn]) * np.linalg.norm(tf(q['S0'])) ** 2)
                z = {'kl': klt, 'omega': om, 'P_S': P['S'], 'P_V1': P['V1'], 'P_V1S': P['V1S'], 'P_E': PE, 'P_quad': Pq,
                     'P_V1S_ueber_P_E': P['V1S'] / PE, 'P_S_ueber_P_E': P['S'] / PE, 'P_V1_ueber_P_S': P['V1'] / P['S'],
                     'A_R': math.sqrt(P['V1'] / P['S']), 'P_V1S_ueber_P_quad': P['V1S'] / Pq,
                     'r_h_rms_V1S': 4 * math.sqrt(GN * P['V1S'] * c0[jn]) / om, 'r_h_rms_E': 4 * math.sqrt(GN * PE * c0[jn]) / om,
                     'r_h_rms_V1': 4 * math.sqrt(GN * P['V1'] * c0[jn]) / om, 'nicht_monoton_oder_aussen': bad,
                     'Pd_S_min_max': [float(Pd['S'].min()), float(Pd['S'].max())]}
                zeilen.append(z)
            tab[jn][q['name']] = zeilen
    out['tabelle'] = tab
    # statische Kopplung je kl (Interpolation in log s)
    stat = {}
    for iq, q in enumerate(quellen):
        zeilen = []
        for klt in KL_AUS:
            so = math.log(klt / LP)
            I = {}
            for x in ('S', 'V1', 'V1S', 'E'):
                vals = np.array([math.exp(np.interp(so, ls, np.log(np.maximum(Cst[x][:, iq, d_], 1e-300)))) for d_ in range(nd)])
                I[x] = float((wdir * vals).sum())
            zeilen.append({'kl': klt, 'C_S_ueber_C_E': I['S'] / I['E'], 'C_V1S_ueber_C_E': I['V1S'] / I['E'],
                           'C_V1_ueber_C_S': I['V1'] / I['S'], 'C_E': I['E']})
        stat[q['name']] = zeilen
    out['statisch'] = stat
    # Exponenten (log-log) ueber kl in {0,01; 0,02; 0,05; 0,1}
    fitk = [0.01, 0.02, 0.05, 0.1]
    ex = {}
    for jn, _ in Jvar:
        ex[jn] = {}
        for qn, zeilen in tab[jn].items():
            xx = np.log([z['kl'] for z in zeilen if z['kl'] in fitk])
            yA = np.log([z['A_R'] for z in zeilen if z['kl'] in fitk])
            yP = np.log([z['P_V1_ueber_P_S'] for z in zeilen if z['kl'] in fitk])
            ex[jn][qn] = {'p_amplitude': float(np.polyfit(xx, yA, 1)[0]), 'p_leistung': float(np.polyfit(xx, yP, 1)[0])}
    out['exponenten'] = ex
    # ---------------------------------------------------------------- Kontrollen an Einzelrichtungen (kl = 0,01)
    kl1 = 0.01
    s1 = kl1 / LP
    dirs3 = [('100', np.array([1.0, 0, 0])), ('110', np.array([1.0, 1, 0]) / math.sqrt(2)), ('111', np.array([1.0, 1, 1]) / math.sqrt(3))]
    ein = {}
    for nm, dvec in dirs3:
        kk = (s1 * dvec)[None, :]
        o = ew.ops(mod, kk)
        B, A1, M, c = o['B'][0], o['A'][0], o['M'][0], o['c'][0]
        U, sv, _ = np.linalg.svd(np.concatenate([M, c], -1))
        S = U[:, 40:]
        Bred = herm(np.conj(S.T) @ B @ S)
        # KA: affine TT-Steifigkeit
        e1 = np.cross(dvec, [0.3, 0.5, 0.7]); e1 /= np.linalg.norm(e1)
        e2 = np.cross(dvec, e1)
        h = (np.outer(e1, e1) - np.outer(e2, e2)) / math.sqrt(2)
        aaff = np.einsum('ei,ij,ej->e', mod['n'], h, mod['n']) * np.exp(1j * (mod['mitte'] @ kk[0]))
        KA = float(np.real(np.conj(aaff) @ B @ aaff) / s1 ** 2)
        # V1-Einheitskraft
        m_u = (vv / VCELL) * np.exp(1j * (pos @ kk[0]))
        ac = c @ np.linalg.solve(np.conj(c.T) @ c, m_u)
        frV = np.conj(S.T) @ (-(KG / KP) * (B @ ac))
        z = {'KA_affin_TT_ueber_k2': KA}
        for jn, J in Jvar:
            A = A1 if J is None else A_J(mod, kk, J)[0]
            Ared = herm(np.conj(S.T) @ A @ S)
            L = np.linalg.cholesky(Ared)
            om2, Uu = np.linalg.eigh(herm(np.conj(L.T) @ Bred @ L))
            tt = []
            gv = []
            for j in range(2):
                x = L @ Uu[:, j]
                Hm, rest = ew.tensor_fit(mod, S @ x, kk[0], M)
                tt.append([float(ew.tp.tt_anteil(Hm, kk[0])[0]), float(rest)])
                gv.append(float(abs(np.conj(x) @ frV) ** 2))
            z[jn] = {'Om2_ueber_k2': [float(x / s1 ** 2) for x in om2[:3]], 'tt_anteil_rest': tt, 'gV1_einheit_quadrat': gv}
        ein[nm] = z
    # KS: V1-Einheitskopplung an TT im Mittel ueber die 200 Richtungen bei kl = 0,01 (interpoliert)
    so = math.log(s1)
    for jn, _ in Jvar:
        gvm = np.array([math.exp(np.interp(so, ls, np.log(np.maximum((np.abs(dyn[jn]['gV'][:, d_, :]) ** 2).sum(-1), 1e-300)))) for d_ in range(nd)])
        ein['gV1_einheit_quadrat_richtungen_' + jn] = {'median': float(np.median(gvm)), 'min': float(gvm.min()), 'max': float(gvm.max())}
    out['einzelrichtungen_kl001'] = ein
    # KN: weiche Richtung von P bei kl = 0,01, alle Richtungen
    kk = s1 * ndir
    o = ew.ops(mod, kk)
    W = mn.W_of(mod, kk)
    Pm = herm(-cT(W) @ o['B'] @ W)
    evp = np.linalg.eigvalsh(Pm)[:, 0] / s1 ** 2
    out['kontrollen']['KN_P_weich_ueber_k2'] = {'min': float(evp.min()), 'max': float(evp.max()), 'mittel': float(evp.mean())}
    GN_rel = 0.2 / float(evp.mean())
    out['G_N_ueber_G'] = GN_rel
    # KG: P_E Winkelformel gegen kompakt bei kl = 0,01 (je Quelle, J_iso)
    out['kontrollen']['KG_PE_ueber_Pquad_kl001'] = {qn: tab['iso'][qn][0]['P_E'] / tab['iso'][qn][0]['P_quad'] for qn in tab['iso']}
    # KD: dynamisch gegen statisch bei kl = 0,01 (S allein)
    out['kontrollen']['KD_dyn_gegen_stat_kl001'] = {qn: {'dyn_P_S_ueber_P_E_iso': tab['iso'][qn][0]['P_S_ueber_P_E'],
                                                         'dyn_P_S_ueber_P_E_eins': tab['eins'][qn][0]['P_S_ueber_P_E'],
                                                         'stat_C_S_ueber_C_E': stat[qn][0]['C_S_ueber_C_E']} for qn in tab['iso']}
    # ---------------------------------------------------------------- Urteile (PLAN Abschnitt 5)
    urt = {}
    E_ = lambda b: 'eingetroffen' if b else 'nicht eingetroffen'
    # PN0
    plan, wort = True, True
    det = {}
    for qn, zeilen in tab['iso'].items():
        ar = [z['A_R'] for z in zeilen if z['kl'] <= 0.1 + 1e-12]
        pr = [z['P_V1_ueber_P_S'] for z in zeilen if z['kl'] <= 0.1 + 1e-12]
        pa, pl = ex['iso'][qn]['p_amplitude'], ex['iso'][qn]['p_leistung']
        okp = (max(ar) <= 1e-3) or (pa >= 1.8)
        okw = (max(pr) <= 1e-3) or (pl >= 1.8)
        det[qn] = {'A_R_max_kl_le_0_1': max(ar), 'p_amplitude': pa, 'P_V1_ueber_P_S_max': max(pr), 'p_leistung': pl}
        plan, wort = plan and okp, wort and okw
    urt['PN0'] = {'plan': E_(plan), 'kartenwortlaut': E_(wort), 'det': det}
    # PN1
    plan, wort = True, True
    det = {}
    for qn, zeilen in tab['iso'].items():
        z0 = zeilen[0]
        qv = {z['kl']: (z['P_V1S'] / z['omega'] ** 2) / (z0['P_V1S'] / z0['omega'] ** 2) for z in zeilen}
        a_ok = z0['P_V1S'] >= 0.1 * z0['P_E']
        b_ok = all(0.8 <= qv[x] <= 1.2 for x in (0.02, 0.05, 0.1, 0.15, 0.2))
        w_ok = all(0.8 <= z['P_V1S_ueber_P_quad'] <= 1.2 for z in zeilen if z['kl'] <= 0.2 + 1e-12)
        det[qn] = {'a_P_V1S_ueber_P_E_kl001': z0['P_V1S'] / z0['P_E'], 'Q_kl': qv,
                   'P_V1S_ueber_P_quad': {z['kl']: z['P_V1S_ueber_P_quad'] for z in zeilen}}
        plan, wort = plan and a_ok and b_ok, wort and w_ok
    urt['PN1'] = {'plan': E_(plan), 'kartenwortlaut': E_(wort), 'det': det}
    # PN2
    plan, wort = True, True
    det = {}
    for qn in tab['iso']:
        gd = tab['iso'][qn][0]['P_V1S_ueber_P_E'] / GN_rel
        gs = stat[qn][0]['C_S_ueber_C_E'] / GN_rel
        det[qn] = {'G_rad_dyn_ueber_G_N': gd, 'G_rad_stat_ueber_G_N': gs}
        plan, wort = plan and (0.9 <= gd <= 1.1), wort and (0.9 <= gs <= 1.1)
    urt['PN2'] = {'plan': E_(plan), 'kartenwortlaut': E_(wort), 'G_N_ueber_G': GN_rel, 'det': det}
    out['urteile'] = urt
    out['zeiten_s'] = {'quelle': t_quelle, 'k_schleife': t_k, 'gesamt': time.time() - t0}
    if rauch:
        out = {'rauch': True, 'schluessel': sorted(out.keys()), 'zeiten_s': out['zeiten_s']}
    return out


# ------------------------------------------------------------------------------------------------ Bild
def bild(pfad_ein, pfad_bild):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    with open(pfad_ein) as f:
        d = json.load(f)['lauf']
    tab = d['tabelle']
    fig, ax = plt.subplots(1, 2, figsize=(13, 5.2))
    a0 = ax[0]
    farben = {'001': '#1f77b4', '111': '#d62728', '123': '#2ca02c'}
    for qn, zeilen in tab['iso'].items():
        om = np.array([z['omega'] for z in zeilen])
        a0.loglog(om, [z['P_V1S'] for z in zeilen], 'o-', color=farben[qn], ms=4, label='mit S (V1+S), Achse %s' % qn)
        a0.loglog(om, [z['P_V1'] for z in zeilen], 's--', color=farben[qn], ms=3, label='V1 allein, Achse %s' % qn)
        a0.loglog(om, [z['P_E'] for z in zeilen], ':', color=farben[qn], lw=1.2, label='Einstein, gleiche Quelle (%s)' % qn)
    a0.set_xlabel('omega (ew-Zeiteinheit)'); a0.set_ylabel('TT-Leistung P (G = 1, Quelle T cos(omega t))')
    a0.set_title('TT-Leistung gegen omega, J_iso (feste Spannungsamplitude)')
    a0.legend(fontsize=6)
    a1 = ax[1]
    for qn, zeilen in tab['iso'].items():
        kl = [z['kl'] for z in zeilen]
        a1.loglog(kl, [z['P_V1S_ueber_P_E'] for z in zeilen], 'o-', color=farben[qn], ms=4, label='P(V1+S)/P_E %s, J_iso' % qn)
        a1.loglog(kl, [z['P_V1S_ueber_P_E'] for z in tab['eins'][qn]], 'x:', color=farben[qn], ms=4, label='P(V1+S)/P_E %s, J = 1 (naeherungsweise)' % qn)
        a1.loglog(kl, [z['A_R'] for z in zeilen], 's--', color=farben[qn], ms=3, label='Amplitude V1/S %s, J_iso' % qn)
    a1.axhline(1, color='k', lw=0.5); a1.axhline(1e-3, color='gray', lw=0.5, ls='--')
    a1.axvline(0.3, color='gray', lw=0.5, ls=':')
    a1.set_xlabel('k l (l = l_P, Massenschale)'); a1.set_ylabel('Verhaeltnis')
    a1.set_title('Gitter gegen Einstein; V1-Amplitude relativ zu S')
    a1.legend(fontsize=6)
    fig.suptitle('PUMPE-NETZ-1: gefuelltes Netz V, A1R1, zwei gegenphasige phi-Klumpen (synthetische Gitterrechnung)')
    fig.tight_layout()
    fig.savefig(pfad_bild + '.tmp.png', dpi=110)
    os.replace(pfad_bild + '.tmp.png', pfad_bild)
    return {'bild': pfad_bild}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['lauf', 'bild'])
    ap.add_argument('--rauch', action='store_true')
    ap.add_argument('--nt', type=int, default=10)
    ap.add_argument('--nphi', type=int, default=20)
    ap.add_argument('--w', type=float, default=W_LP)
    ap.add_argument('--d', type=float, default=D_LP)
    ap.add_argument('--ein')
    ap.add_argument('--bild')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    info = {'numpy': np.__version__, 'python': platform.python_version(), 'host': platform.node(),
            'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'argv': sys.argv,
            'skript_sha256': sha(os.path.abspath(__file__)), 'ew_sha256': sha(os.path.abspath(ew.__file__)),
            'mn_sha256': sha(os.path.abspath(mn.__file__)), 'tp_sha256': sha(os.path.abspath(ew.tp.__file__))}
    res = {'info': info}
    if a.modus == 'lauf':
        res['lauf'] = lauf(rauch=a.rauch, nt=a.nt, nphi=a.nphi, w_lP=a.w, d_lP=a.d)
    else:
        info['eingabe_sha256'] = sha(a.ein)
        res['bild'] = bild(a.ein, a.bild)
    res['laufzeit_s'] = time.time() - t0
    res['maxrss_MB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    res['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    with open(a.out + '.tmp', 'w') as f:
        json.dump(res, f, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
    os.replace(a.out + '.tmp', a.out)
    print('fertig', a.modus, 'laufzeit %.1f s' % res['laufzeit_s'], 'maxrss %.0f MB' % res['maxrss_MB'], flush=True)


if __name__ == '__main__':
    main()
