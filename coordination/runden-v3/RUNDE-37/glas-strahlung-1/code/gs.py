#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GLAS-STRAHLUNG-1 (Runde 48, fmhc-physics), Code-Agent fuer die Leitung claude-primary.

IMPULS-NETZ-1-Aufbau (Impulskopplung J, schwingender phi-Quadrupol, Kreisbahnen) auf den periodischen Glasnetzen von
TT-GLAS-1/2 (tg.zufallsnetz, tg.modell, dichte Bausteine dz, unveraendert importiert) und als Kontrolle GS0 auf Netz V
(tg.netz_V mit den J_iso-Gewichten aus pn.py).

Je Netz: Bloch-k = kabs n fuer die Richtungen n der oberen Halbkugel eines Gauss-Legendre-Gitters (nt x nphi); die
untere Halbkugel folgt aus k -> -k (alle Operatoren reell bis auf Bloch-Phasen: Groessen bei -k sind konjugiert).
Je k (R1 wie inz.py): S = Komplement von Bild[M, c]; A_red = L L^H (Cholesky), Moden X = L U (zwei weichste von
L^H B_red L). Kraefte (Kantenkraefte sigma):
  - gleichfoermige Spannung T_a e^(i k.m_e), 6 Basistensoren, Materie-Gewichte P1 (pn.K_aus_laengen, je Tetraeder) und
    umkreisbasiert (nachtrag_umkreis.K_umkreis): sigma_e = Q_e : (T - tr T 1), Q_e = Summe 0,5 l_p X^T dK_p X;
  - phi-Quadrupol (zwei gegenphasige Gauss-Klumpen um pos[0], Achsen [001], [111], (1,2,3)), Bloch-Summe ueber alle
    Bilder der Superzelle (wie pn.quelle);
  - V1-Einheitskraft (Energie in der skalaren Regel, m_v = V_v/V e^(i k.x_v)).
  f0 = -S^H sigma; Impulskopplung fJ = -A_red^-1 S^H A P_M sigma (P_M = M (M^H M)^-1 M^H); g = X^H f.
Auswertung (Modus aus), Goldene Regel bei linearer Dispersion (wie pn.py bei kleinem k, je Mode):
  P/P_E = Summe_n w Summe_j |A_j|^2/om2_j (c0/c_j) / Summe_n w Lambda_n[S~]:S~^*/(V k^2),
  A_j = g_j(S oder S+J) + (c0/c_j)^2 (n.S~.n) g_j(V1),  c0^2 = Raumwinkelmittel von om2/k^2 (beide Zweige),
  G_N/G = (8 V/nV)/(Mittel lambda_min(P)/k^2), P = -W^H B W;  G_rad/G_N = (P/P_E)/(G_N/G).
Aufruf nur ueber kleintest.sh auf der .69:
  python gs.py netz --N 128 --saaten 1,2 --out lauf/gs   [--nt 6 --nphi 12 --kabs 0.01 --frist 540 --rauch]
  python gs.py netz --N 0 --out lauf/v.json --nt 10 --nphi 20      (N = 0: Netz V, kabs = 0,01/l_P)
  python gs.py aus --v lauf/v.json --ein lauf/gs-N*.json --out aus/auswertung.json --bild aus/bild-glas-strahlung.png
"""
import argparse, json, os, sys, time, hashlib, platform, resource, math, glob
import numpy as np
import scipy
import scipy.sparse as sp
import torch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tg  # noqa: E402  (TT-GLAS-1, unveraendert)
import dz  # noqa: E402  (TT-GLAS-2, unveraendert)
import ew  # noqa: E402  (EINE-WELT-LOCH-1, unveraendert)
import pn  # noqa: E402  (PUMPE-NETZ-1, unveraendert)
import nachtrag_umkreis as nu  # noqa: E402  (IMPULS-NETZ-1, unveraendert; nur K_umkreis)

LP, KG, KP = pn.LP, pn.KG, pn.KP
J_ISO = pn.J_ISO
SKAL = 40.0 ** (1.0 / 3.0)          # Laengenmass Glas gegen V: Eckdichte V = 10 / 0,25 = 40, Glas = 1
IJ = [(p[0], p[1]) for p in tg.PAARE]
H_CS = 1e-20
BASIS = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]
G_REF = {'001': 1.0296610138393512, '111': 1.0040051253222577, '123': 0.9674684345785949}   # IMPULS-NETZ-1 h1.json
G_KARTE = {'001': 1.030, '111': 1.004, '123': 0.967}
BAHN_REF_SJ = {'001': 0.9985035624546907, '111': 1.0012214250603886, '110': 1.000541959252857, '123': 1.0005419594652303}


def sha(p):
    with open(p, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def kx(z):
    """komplexes Feld -> [re, im] (JSON)."""
    z = np.asarray(z)
    return np.stack([z.real, z.imag], -1).tolist()


def xk(a):
    a = np.asarray(a, float)
    return a[..., 0] + 1j * a[..., 1]


# ------------------------------------------------------------------------------------------------ Netz und Gewichte
def baue_netz(N, saat):
    if N == 0:
        LV, pos, G, O, pr = tg.netz_V()
        arten = [z['art'] for z in ew.geometrie('V')[1]]
        wkin = np.array([J_ISO[a] for a in arten])
    else:
        LV, pos, G, O, pr = tg.zufallsnetz(N, saat)
        wkin = np.ones(len(G))
    mod = tg.modell(LV, pos, G, O, pr)
    X = pos[G] + np.einsum('tai,ij->taj', O.astype(float), np.asarray(LV, float))
    vol = np.abs(np.linalg.det(X[:, 1:] - X[:, :1])) / 6.0
    vv = np.zeros(len(pos))
    np.add.at(vv, G.ravel(), np.repeat(vol / 4.0, 4))
    mod.update({'X': X, 'pos': np.asarray(pos, float), 'LV': np.asarray(LV, float), 'G': G, 'wkin': wkin, 'vol': vol, 'vv': vv})
    return mod


def L2_aus(lv):
    L2 = np.zeros((lv.shape[0], 4, 4), dtype=lv.dtype)
    for p, (i, j) in enumerate(IJ):
        L2[:, i, j] = lv[:, p] ** 2
        L2[:, j, i] = lv[:, p] ** 2
    return L2


def gram(L2):
    return 0.5 * (L2[:, 0, 1:, None] + L2[:, 0, None, 1:] - L2[:, 1:, 1:])


def K_p1(lv):
    """wie pn.K_aus_laengen, je Tetraeder gebuendelt (Kantenfolge tg.PAARE)."""
    g = gram(L2_aus(lv))
    V = np.sqrt(np.linalg.det(g)) / 6.0
    return V[:, None, None] * (pn.DMAT.T[None] @ np.linalg.inv(g) @ pn.DMAT[None])


def K_umk(lv):
    """wie nachtrag_umkreis.K_umkreis, gebuendelt."""
    L2 = L2_aus(lv)
    g = gram(L2)
    V = np.sqrt(np.linalg.det(g)) / 6.0
    dg = np.diagonal(g, axis1=1, axis2=2)
    lam = 0.5 * np.linalg.solve(g, dg[..., None])[..., 0]
    beta = np.concatenate([1.0 - lam.sum(1, keepdims=True), lam], 1)
    K = np.zeros((lv.shape[0], 4, 4), dtype=lv.dtype)
    for (i, j) in IJ:
        k_, l_ = [m for m in range(4) if m not in (i, j)]
        w = 0.0
        for m, o in ((k_, l_), (l_, k_)):
            uu, vv_ = L2[:, o, i], L2[:, o, j]
            uv = 0.5 * (L2[:, o, i] + L2[:, o, j] - L2[:, i, j])
            Af = 0.5 * np.sqrt(uu * vv_ - uv * uv)
            w = w + (uv / (2.0 * Af)) * beta[:, m] * 3.0 * V / Af
        w = 0.25 * w
        K[:, i, i] += w
        K[:, j, j] += w
        K[:, i, j] -= w
        K[:, j, i] -= w
    return K


def ableitungen(mod, Kfun):
    X = mod['X']
    lt = np.stack([np.linalg.norm(X[:, j] - X[:, i], axis=1) for (i, j) in IJ], 1)
    dK = np.zeros((len(X), 6, 4, 4))
    for p in range(6):
        lv = lt.astype(complex)
        lv[:, p] += 1j * H_CS
        dK[:, p] = np.imag(Kfun(lv)) / H_CS
    return lt, dK


def Q_map(mod, lt, dK):
    Xr = mod['X'] - mod['X'][:, :1]
    q = 0.5 * lt[:, :, None, None] * np.einsum('tai,tpab,tbj->tpij', Xr, dK, Xr)
    Q = np.zeros((mod['E'], 3, 3))
    np.add.at(Q, mod['eidx'].ravel(), q.reshape(-1, 3, 3))
    return Q


def sig_basis(mod, Q):
    out = []
    for (a, b) in BASIS:
        T = np.zeros((3, 3))
        T[a, b] = T[b, a] = 1.0
        out.append(np.einsum('eij,ij->e', Q, T - np.trace(T) * np.eye(3)))
    return np.stack(out, 1)                                      # (E, 6)


def kontrolle_affin(mod, Q):
    dev = 0.0
    for (a, b) in BASIS:
        T = np.zeros((3, 3))
        T[a, b] = T[b, a] = 1.0
        s = np.einsum('eij,ij->e', Q, T - np.trace(T) * np.eye(3))
        lhs = np.einsum('e,ei,ej->ij', s, mod['n'], mod['n'])
        dev = max(dev, float(np.abs(lhs + mod['Vbox'] * T).max()))
    return dev


# ------------------------------------------------------------------------------------------------ phi-Quadrupol
def phi_quellen(mod, dKs, lt, w, d, rbox, chunk=64):
    """Je Achse: Eintraege (Kante, Bloch-Versatz, Kraft je Gewichtsart) und Spannung je Tetraeder-Bild (wie pn.quelle)."""
    X, LV = mod['X'], mod['LV']
    x_c = mod['pos'][0]
    cen = X.mean(1)
    h = 1.0 / np.linalg.norm(np.linalg.inv(LV), axis=0).max()
    nmax = int(math.ceil(rbox / h)) + 2
    g = np.arange(-nmax, nmax + 1)
    nn = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1).reshape(-1, 3)
    R = nn @ LV
    ti, ri = [], []
    for i0 in range(0, len(R), chunk):
        dd = np.linalg.norm(cen[None, :, :] + R[i0:i0 + chunk, None, :] - x_c, axis=2)
        a_, b_ = np.nonzero(dd <= rbox)
        ri.append(a_ + i0)
        ti.append(b_)
    ri = np.concatenate(ri)
    ti = np.concatenate(ti)
    Xs = X[ti] + R[ri][:, None, :]
    off = mod['Tcopy'][ti] + R[ri][:, None, :]
    ed = mod['eidx'][ti]
    Ev = Xs[:, 1:] - Xs[:, :1]
    vt = mod['vol'][ti]
    xt = Xs.mean(1)
    rr = np.linalg.norm(xt - x_c, axis=1)
    out = {}
    for nm, ach in pn.ACHSEN:
        e = np.array(ach, float)
        e /= np.linalg.norm(e)
        xp, xm = x_c + d * e, x_c - d * e
        ph = np.exp(-((Xs - xp) ** 2).sum(-1) / (2 * w * w)) - np.exp(-((Xs - xm) ** 2).sum(-1) / (2 * w * w))
        sp_ = {}
        for art, dK in dKs.items():
            sp_[art] = 0.5 * np.einsum('ca,cpab,cb->cp', ph, dK[ti], ph) * lt[ti]
        grad = np.linalg.solve(Ev, (ph[:, 1:] - ph[:, :1])[..., None])[..., 0]
        T = grad[:, :, None] * grad[:, None, :] - 0.5 * (grad ** 2).sum(-1)[:, None, None] * np.eye(3)[None]
        VT = vt[:, None, None] * T
        rand = float(np.abs(VT[rr > rbox - 0.6 * rbox / 3.2]).sum() / max(np.abs(VT).sum(), 1e-300))
        out[nm] = {'sp': sp_, 'VT': VT.reshape(-1, 9), 'S0': VT.sum(0), 'rand_anteil': rand}
    return {'achsen': out, 'ed': ed, 'off': off, 'xt': xt, 'n_eintraege': int(len(ti)), 'nmax': nmax}


def phi_bloch(pq, kk, E):
    ph = np.exp(-1j * np.einsum('cpi,i->cp', pq['off'], kk)).ravel()
    edf = pq['ed'].ravel()
    res = {}
    for nm, q in pq['achsen'].items():
        for art, s in q['sp'].items():
            v = s.ravel() * ph
            res[(nm, art)] = np.bincount(edf, v.real, E) + 1j * np.bincount(edf, v.imag, E)
    return res


def S_tilde(pq, nm, kk):
    return (np.exp(-1j * (pq['xt'] @ kk)) @ pq['achsen'][nm]['VT']).reshape(3, 3)


def lam_TT(n, S):
    P = np.eye(3) - np.outer(n, n)
    PSP = P @ S @ P
    TT = PSP - 0.5 * P * np.trace(PSP)
    return float(np.real(np.sum(TT * np.conj(TT))))


# ------------------------------------------------------------------------------------------------ ein Bloch-k
def k_punkt(mod, kk, dev, SIG0, pq, nfo):
    E, nV, Vbox = mod['E'], mod['nV'], mod['Vbox']
    t0 = time.time()
    B, A1, M, c = tg.ops(mod, kk)
    A = A1 if nfo['glas'] else dz.assemble(mod, mod['wkin'][:, None, None] * mod['A0'], kk)
    z = {}
    # Takt P = -W^H B W = W^H c (c = -B W), Newton
    phe = np.exp(1j * (mod['Tedge'] @ kk))
    rr = np.arange(E)
    Wh = sp.coo_matrix((np.concatenate([np.ones(E), phe]), (np.concatenate([rr, rr]), np.concatenate([mod['es'], mod['es2']]))),
                       shape=(E, nV)).tocsr()
    P = np.asarray(Wh.conj().T @ c)
    P = 0.5 * (P + P.conj().T)
    z['lamP'] = float(np.linalg.eigvalsh(P)[0])
    m_u = (mod['vv'] / Vbox) * np.exp(1j * (mod['pos'] @ kk))
    z['newton_resp'] = float(np.real(np.conj(m_u) @ np.linalg.solve(P, m_u)))
    z['summe_m_abs2'] = float(abs(m_u.sum()) ** 2)
    # Kontrollen (Operatoren), nur am ersten k je Netz (Laufzeit)
    if nfo.get('kontr'):
        BM = B @ M
        z['KF_MB'] = float(np.abs(BM).max() / (abs(B).max() * np.abs(M).max()))
        del BM
        Mt_ = torch.from_numpy(np.ascontiguousarray(M)).to(dev)
        ct_ = torch.from_numpy(np.ascontiguousarray(c)).to(dev)
        z['KR_cM'] = float(((ct_.conj().T @ Mt_).abs().max() / (ct_.abs().max() * Mt_.abs().max())).item())
        del Mt_, ct_
    # R1
    S, binfo = dz.basis(np.concatenate([M, c], 1), dev)
    z['basis'] = binfo
    Ared = dz.reduziert(A, S, dev)
    Bred = dz.reduziert(B, S, dev)
    Lc, info = torch.linalg.cholesky_ex(Ared)
    z['chol_ok'] = int(info.item()) == 0
    if not z['chol_ok']:
        z['t_s'] = time.time() - t0
        return z
    om2, U = torch.linalg.eigh(dz.herm(Lc.conj().T @ Bred @ Lc))
    del Bred, Ared
    Xm = Lc @ U[:, :2]
    del U
    z['om2'] = [float(x) for x in om2[:4].cpu().numpy()]
    # Kraefte
    ph_m = np.exp(1j * (mod['mitte'] @ kk))
    cols = [SIG0[:, i] * ph_m for i in range(SIG0.shape[1])]
    pb = phi_bloch(pq, kk, E)
    for key in nfo['phi_keys']:
        cols.append(pb[tuple(key)])
    SIG = np.stack(cols, 1)
    Mt = torch.from_numpy(np.ascontiguousarray(M)).to(dev)
    SIGt = torch.from_numpy(SIG).to(dev)
    MhS = Mt.conj().T @ SIGt
    PMs = Mt @ torch.linalg.solve(Mt.conj().T @ Mt, MhS)
    z['KJ'] = float(((Mt.conj().T @ PMs - MhS).abs().max() / MhS.abs().max()).item())
    del Mt
    APM = torch.from_numpy(np.ascontiguousarray(A @ PMs.cpu().numpy())).to(dev)
    del PMs
    fJ = -torch.cholesky_solve(S.conj().T @ APM, Lc)
    del APM
    f0 = -(S.conj().T @ SIGt)
    ct = torch.from_numpy(np.ascontiguousarray(c)).to(dev)
    mt = torch.from_numpy(np.ascontiguousarray(m_u)).to(dev)
    ac = (ct @ torch.linalg.solve(ct.conj().T @ ct, mt)).cpu().numpy()
    del ct, mt
    fV = -(KG / KP) * (B @ ac)
    frV = S.conj().T @ torch.from_numpy(np.ascontiguousarray(fV)).to(dev)
    XmH = Xm.conj().T
    z['g0'] = kx((XmH @ f0).cpu().numpy())
    z['gJ'] = kx((XmH @ (f0 + fJ)).cpu().numpy())
    z['gV'] = kx((XmH @ frV).cpu().numpy())
    z['J_kraft_rel_median'] = float(torch.median(torch.linalg.norm(fJ, dim=0) / torch.linalg.norm(f0, dim=0)).item())
    # phi: Kontinuum-Spannung bei k
    z['phi_nnS'] = {}
    z['phi_lamE'] = {}
    n = kk / np.linalg.norm(kk)
    for nm, _ in pn.ACHSEN:
        St = S_tilde(pq, nm, kk)
        z['phi_nnS'][nm] = kx(n @ St @ n)
        z['phi_lamE'][nm] = lam_TT(n, St)
    del S, Lc, Xm, f0, fJ, SIGt, frV
    if dev.type == 'cuda':
        torch.cuda.synchronize()
    z['t_s'] = time.time() - t0
    return z


def richtungen_oben(nt, nphi):
    n, w = pn.richtungen(nt, nphi)
    sel = n[:, 2] > 0
    return n[sel], w[sel], int(len(n))


def netz_lauf(N, saat, a, dev, t_start):
    t0 = time.time()
    glas = N != 0
    mod = baue_netz(N, saat)
    kabs = a.kabs if glas else 0.01 / LP
    skal = SKAL if glas else 1.0
    w_, d_, rbox = 0.8 * LP * skal, 0.8 * LP * skal, 3.2 * skal
    lt, dKp = ableitungen(mod, K_p1)
    _, dKu = ableitungen(mod, K_umk)
    Qp, Qu = Q_map(mod, lt, dKp), Q_map(mod, lt, dKu)
    SIG0 = np.concatenate([sig_basis(mod, Qp), sig_basis(mod, Qu)], 1)
    pq = phi_quellen(mod, {'P1': dKp, 'umkreis': dKu}, lt, w_, d_, rbox)
    phi_keys = [[nm, art] for nm, _ in pn.ACHSEN for art in ('P1', 'umkreis')]
    spalten = ['bahn_P1_%d%d' % b for b in BASIS] + ['bahn_umkreis_%d%d' % b for b in BASIS] + ['phi_%s_%s' % tuple(k) for k in phi_keys]
    nfo = {'glas': glas, 'phi_keys': phi_keys}
    ndir, wdir, nvoll = richtungen_oben(a.nt, a.nphi)
    if a.rauch:
        ndir, wdir = ndir[:a.rauch_k], wdir[:a.rauch_k]
    zeilen = []
    abgebrochen = False
    for i, n in enumerate(ndir):
        if time.time() - t_start > a.frist:
            abgebrochen = True
            break
        nfo['kontr'] = (i == 0)
        z = k_punkt(mod, kabs * n, dev, SIG0, pq, nfo)
        z['n'] = n.tolist()
        z['w'] = float(wdir[i])
        zeilen.append(z)
    pr = dict(mod['pruefung'])
    erg = {'N': N, 'saat': saat, 'glas': glas, 'kabs': kabs, 'E': mod['E'], 'nV': mod['nV'], 'T': mod['T'], 'Vbox': mod['Vbox'],
           'nt': a.nt, 'nphi': a.nphi, 'n_richtungen_voll': nvoll, 'n_oben_geplant': int(len(ndir)), 'n_oben_fertig': len(zeilen),
           'abgebrochen_frist': abgebrochen, 'spalten': spalten, 'quelle_w_d_rbox': [w_, d_, rbox],
           'quellen': {nm: {'S0': np.asarray(q['S0']).tolist(), 'rand_anteil': q['rand_anteil']} for nm, q in pq['achsen'].items()},
           'phi_eintraege': pq['n_eintraege'], 'phi_nmax': pq['nmax'],
           'KP1_affin': {'P1': kontrolle_affin(mod, Qp), 'umkreis': kontrolle_affin(mod, Qu)},
           'summe_eckvolumen_rel': float(mod['vv'].sum() / mod['Vbox'] - 1), 'pruefung': pr, 'zeilen': zeilen,
           't_netz_s': time.time() - t0}
    return erg


def nur_schluessel(x, tiefe=0):
    if isinstance(x, dict):
        return {k: nur_schluessel(v, tiefe + 1) for k, v in x.items()} if tiefe < 3 else sorted(x.keys())
    if isinstance(x, list) and x and isinstance(x[0], dict):
        return [nur_schluessel(x[0], tiefe + 1)]
    return type(x).__name__


def schreibe(pfad, res):
    with open(pfad + '.tmp', 'w') as fh:
        json.dump(res, fh, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
    os.replace(pfad + '.tmp', pfad)


# ------------------------------------------------------------------------------------------------ Auswertung
NAMEN_BAHN = [('001', [0, 0, 1]), ('111', [1, 1, 1]), ('110', [1, 1, 0]), ('123', [1, 2, 3])]


def bahnnormalen():
    out = list(NAMEN_BAHN)
    rng = np.random.default_rng(31)
    for i, v in enumerate(rng.normal(size=(8, 3))):
        out.append(('z%d' % i, v.tolist()))
    rng = np.random.default_rng(47)
    for i, v in enumerate(rng.normal(size=(12, 3))):
        out.append(('y%d' % i, v.tolist()))
    res = []
    for nm, v in out:
        m = np.array(v, float) / np.linalg.norm(v)
        u = np.cross(m, [0.3, 0.5, 0.7])
        u /= np.linalg.norm(u)
        w = np.cross(m, u)
        res.append((nm, m, np.outer(u + 1j * w, u + 1j * w)))
    return res


def koef(T):
    return np.stack([T[..., 0, 0], T[..., 1, 1], T[..., 2, 2], T[..., 0, 1], T[..., 0, 2], T[..., 1, 2]], -1)


def zerlege(n, S):
    """S (3x3) je Richtung n (nd,3): TT, L (laengs-quer), Rest (nn-Teil) als (nd,3,3)."""
    Nn = n[:, :, None] * n[:, None, :]
    P = np.eye(3)[None] - Nn
    PSP = P @ S @ P
    TT = PSP - 0.5 * P * np.einsum('dii->d', PSP)[:, None, None]
    L = P @ S @ Nn + Nn @ S @ P
    return TT, L, S[None] - TT - L


def netz_auswerten(r):
    Z = [z for z in r['zeilen'] if z.get('chol_ok')]
    k = r['kabs']
    V = r['Vbox']
    n = np.array([z['n'] for z in Z])
    w = np.array([z['w'] for z in Z])
    om2 = np.array([z['om2'] for z in Z])[:, :2]
    g0 = xk([z['g0'] for z in Z])            # (nd, 2, nf)
    gJ = xk([z['gJ'] for z in Z])
    gV = xk([z['gV'] for z in Z]).reshape(len(Z), 2)
    c2 = om2 / k ** 2
    c0sq = float((w[:, None] * c2).sum() / (2 * w.sum()))
    facP = np.sqrt(c0sq / c2)
    eps = c0sq / c2
    lamP = np.array([z['lamP'] for z in Z]) / k ** 2
    GN = (8.0 * V / r['nV']) / float((w * lamP).sum() / w.sum())
    nres = np.array([z['newton_resp'] * 8 * V * k ** 2 / z['summe_m_abs2'] for z in Z])
    GN_direkt = float((w * nres).sum() / w.sum())
    sp_ = r['spalten']
    ib = {'P1': [sp_.index('bahn_P1_%d%d' % b) for b in BASIS], 'umkreis': [sp_.index('bahn_umkreis_%d%d' % b) for b in BASIS]}

    def amp(g, cols, T):          # T (nd,3,3) komplex -> (nd,2)
        return np.einsum('da,dja->dj', koef(T), g[:, :, cols])


    out = {'c0_quadrat': c0sq, 'tempo2_spanne': float(c2.max() / c2.min() - 1), 'G_N_ueber_G': GN, 'G_N_ueber_G_direkt': GN_direkt,
           'n_richtungen_oben': int(len(Z)), 'om2_luecke_min': float(min(z['om2'][2] / z['om2'][1] for z in Z)),
           'kontrollen': {'KF_MB_erstes_k': max(z.get('KF_MB', 0.0) for z in Z), 'KR_cM_erstes_k': max(z.get('KR_cM', 0.0) for z in Z),
                          'KJ_max': max(z['KJ'] for z in Z),
                          'chol_alle': all(z.get('chol_ok') for z in r['zeilen']), 'rang_wege': sorted(set(z['basis']['weg'] for z in Z)),
                          'rang_voll': all(z['basis']['rang_Mc'] == z['basis']['nX'] for z in Z),
                          'J_kraft_rel_median': [min(z['J_kraft_rel_median'] for z in Z), max(z['J_kraft_rel_median'] for z in Z)]}}
    # Kreisbahnen
    bahnen = {}
    for nm, m, Sc in bahnnormalen():
        nSn = np.einsum('di,ij,dj->d', n, Sc, n)
        TT, L, Rn = zerlege(n, Sc)
        den = 2.0 * float((w * V * np.real(np.sum(TT * np.conj(TT), axis=(1, 2))) / k ** 2).sum())
        zb = {'m': m.tolist(), 'summe_m4': float((m ** 4).sum())}
        for art in ('P1', 'umkreis'):
            cols = ib[art]
            for jn, g in (('J', gJ), ('ohneJ', g0)):
                teile = {'TT': TT, 'TTL': TT + L, 'S': TT + L + Rn}
                for tn, Tp in teile.items():
                    for vn in (('', False), ('V1', True)):
                        if vn[1] and tn != 'S':
                            continue
                        for mass in ('P', 'K'):
                            num = 0.0
                            for konj in (False, True):
                                Tq = np.conj(Tp) if konj else Tp
                                A = amp(g, cols, Tq)
                                if vn[1]:
                                    e_ = eps if mass == 'P' else np.ones_like(eps)
                                    A = A + e_ * V * (np.conj(nSn) if konj else nSn)[:, None] * gV
                                f_ = facP if mass == 'P' else 1.0
                                num += float((w[:, None] * np.abs(A) ** 2 / om2 * f_).sum())
                            zb['%s_%s_%s%s_%s' % (mass, art, tn, vn[0], jn)] = num / den / GN
        bahnen[nm] = zb
    out['bahnen'] = bahnen
    # phi-Quadrupol
    phi = {}
    for nm, _ in pn.ACHSEN:
        nnS = np.array([xk(z['phi_nnS'][nm]) for z in Z])
        lamE = np.array([z['phi_lamE'][nm] for z in Z])
        den = float((w * lamE / (V * k ** 2)).sum())
        zp = {}
        for art in ('P1', 'umkreis'):
            col = sp_.index('phi_%s_%s' % (nm, art))
            for jn, g in (('J', gJ), ('ohneJ', g0)):
                for v1 in (False, True):
                    A = g[:, :, col].copy()
                    if v1:
                        A = A + eps * nnS[:, None] * gV
                    zp['P_%s_%s%s_%s' % (art, 'S', 'V1' if v1 else '', jn)] = float((w[:, None] * np.abs(A) ** 2 / om2 * facP).sum()) / den / GN
        phi[nm] = zp
    out['phi'] = phi
    return out


def stat(x):
    x = np.asarray(x, float)
    return {'mittel': float(x.mean()), 'sd': float(x.std(ddof=1)) if len(x) > 1 else None, 'min': float(x.min()), 'max': float(x.max()),
            'n': int(len(x))}


def auswertung(pfad_v, pfade, pfad_out, pfad_bild):
    with open(pfad_v) as fh:
        rv = json.load(fh)
    av = netz_auswerten(rv['ergebnis'])
    res = {'eingaben': {os.path.basename(p): sha(p) for p in [pfad_v] + pfade}}
    # GS0
    gv = {nm: av['phi'][nm]['P_P1_SV1_J'] for nm in G_REF}
    res['GS0'] = {'G_V1SJ': gv, 'abw_ref': {nm: gv[nm] - G_REF[nm] for nm in G_REF}, 'abw_karte': {nm: gv[nm] - G_KARTE[nm] for nm in G_REF},
                  'plan': 'eingetroffen' if all(abs(gv[nm] - G_REF[nm]) <= 1e-3 for nm in G_REF) else 'nicht eingetroffen',
                  'kartenwortlaut': 'eingetroffen' if all(abs(gv[nm] - G_KARTE[nm]) <= 1e-3 for nm in G_REF) else 'nicht eingetroffen',
                  'G_N_ueber_G': av['G_N_ueber_G'], 'bahnen_SJ_gegen_IN1': {nm: [av['bahnen'][nm]['P_P1_S_J'], BAHN_REF_SJ[nm]] for nm in BAHN_REF_SJ},
                  'V_voll': av}
    # Glas je Netz
    netze = []
    for p in pfade:
        with open(p) as fh:
            r = json.load(fh)['ergebnis']
        if not r['glas'] or r['abgebrochen_frist'] or r['n_oben_fertig'] < r['n_oben_geplant']:
            netze.append({'datei': os.path.basename(p), 'N': r['N'], 'saat': r['saat'], 'unvollstaendig': True})
            continue
        a = netz_auswerten(r)
        a.update({'datei': os.path.basename(p), 'N': r['N'], 'saat': r['saat'], 'E': r['E'], 'nV': r['nV'], 'T': r['T'],
                  'KP1_affin': r['KP1_affin'], 'quellen_rand': {k_: v['rand_anteil'] for k_, v in r['quellen'].items()},
                  'unvollstaendig': False})
        G = np.array([b['P_P1_SV1_J'] for b in a['bahnen'].values()])
        a['lagen'] = stat(G)
        netze.append(a)
    gut = [x for x in netze if not x['unvollstaendig']]
    res['netze'] = netze
    Ns = sorted(set(x['N'] for x in gut))
    jeN = {}
    groessen = ['P_P1_SV1_J', 'P_P1_S_J', 'P_P1_TT_J', 'P_P1_TTL_J', 'K_P1_SV1_J', 'P_P1_SV1_ohneJ', 'P_umkreis_SV1_J', 'P_umkreis_S_J']
    for N in Ns:
        xs = [x for x in gut if x['N'] == N]
        zN = {'netze': len(xs), 'saaten': [x['saat'] for x in xs]}
        for gname in groessen:
            mit = [np.mean([b[gname] for b in x['bahnen'].values()]) for x in xs]
            sds = [np.std([b[gname] for b in x['bahnen'].values()], ddof=1) for x in xs]
            zN[gname] = {'mittel_lagen_saaten': float(np.mean(mit)), 'sd_der_netzmittel': float(np.std(mit, ddof=1)) if len(mit) > 1 else None,
                         'sd_lagen_mittel': float(np.mean(sds)), 'sd_lagen_je_netz': [float(s) for s in sds], 'mittel_je_netz': [float(m) for m in mit]}
        # Kanaele (Zuwachs, Mittel ueber Lagen und Saaten)
        kan = {}
        for art in ('P1', 'umkreis'):
            dTT = [np.mean([b['P_%s_TT_J' % art] - 1 for b in x['bahnen'].values()]) for x in xs]
            dL = [np.mean([b['P_%s_TTL_J' % art] - b['P_%s_TT_J' % art] for b in x['bahnen'].values()]) for x in xs]
            dnn = [np.mean([b['P_%s_S_J' % art] - b['P_%s_TTL_J' % art] for b in x['bahnen'].values()]) for x in xs]
            dV = [np.mean([b['P_%s_SV1_J' % art] - b['P_%s_S_J' % art] for b in x['bahnen'].values()]) for x in xs]
            sTT = [np.std([b['P_%s_TT_J' % art] for b in x['bahnen'].values()], ddof=1) for x in xs]
            sS = [np.std([b['P_%s_S_J' % art] for b in x['bahnen'].values()], ddof=1) for x in xs]
            kan[art] = {'TT': stat(dTT), 'L': stat(dL), 'nn': stat(dnn), 'V1': stat(dV), 'sd_lagen_TT': stat(sTT), 'sd_lagen_S': stat(sS)}
        zN['kanaele'] = kan
        zN['G_N_ueber_G'] = stat([x['G_N_ueber_G'] for x in xs])
        zN['G_N_ueber_G_direkt'] = stat([x['G_N_ueber_G_direkt'] for x in xs])
        zN['tempo2_spanne'] = stat([x['tempo2_spanne'] for x in xs])
        zN['phi'] = {nm: {k_: stat([x['phi'][nm][k_] for x in xs]) for k_ in ('P_P1_SV1_J', 'P_P1_S_J', 'P_P1_SV1_ohneJ', 'P_umkreis_SV1_J')}
                     for nm, _ in pn.ACHSEN}
        jeN[str(N)] = zN
    res['je_N'] = jeN
    # Exponent der Lagenstreuung (Hauptgroesse)
    xN = np.array([x['N'] for x in gut], float)
    ySD = np.array([x['lagen']['sd'] for x in gut], float)
    ex = {}
    if len(Ns) >= 2:
        p_alle = float(np.polyfit(np.log(xN), np.log(ySD), 1)[0])
        mN = np.array([np.mean(ySD[xN == N]) for N in Ns])
        p_mittel = float(np.polyfit(np.log(np.array(Ns, float)), np.log(mN), 1)[0])
        rng = np.random.default_rng(2026)
        bs = []
        for _ in range(2000):
            xx, yy = [], []
            for N in Ns:
                idx = np.nonzero(xN == N)[0]
                pick = rng.choice(idx, len(idx), replace=True)
                xx += list(xN[pick])
                yy += list(ySD[pick])
            bs.append(np.polyfit(np.log(xx), np.log(yy), 1)[0])
        bs = np.array(bs)
        ex = {'p_alle_netze': p_alle, 'p_durch_mittel': p_mittel, 'bootstrap_68': [float(np.percentile(bs, 16)), float(np.percentile(bs, 84))],
              'bootstrap_95': [float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5))], 'N': Ns, 'sd_mittel_je_N': mN.tolist()}
        # beschreibend: weitere Groessen
        for gname in ('K_P1_SV1_J', 'P_P1_S_J', 'P_P1_TT_J', 'P_umkreis_SV1_J'):
            yy = np.array([np.std([b[gname] for b in x['bahnen'].values()], ddof=1) for x in gut])
            ex['p_alle_' + gname] = float(np.polyfit(np.log(xN), np.log(yy), 1)[0])
        yy = np.array([x['tempo2_spanne'] for x in gut])
        ex['p_alle_tempo2_spanne'] = float(np.polyfit(np.log(xN), np.log(yy), 1)[0])
    res['exponent'] = ex
    # Urteile GS1 bis GS3
    U = {}
    nz = {N: len([x for x in gut if x['N'] == N]) for N in (128, 256, 512)}
    U['netze_vollstaendig'] = {str(N): v for N, v in nz.items()}
    entsch1 = all(v >= 2 for v in nz.values())
    entsch23 = nz[128] >= 2 and nz[512] >= 2
    NE = 'nicht entscheidbar'
    if ex:
        U['GS1'] = {'plan': ('eingetroffen' if ex['p_alle_netze'] <= -0.4 else 'nicht eingetroffen') if entsch1 else NE,
                    'kartenwortlaut': ('eingetroffen' if ex['p_durch_mittel'] <= -0.4 else 'nicht eingetroffen') if entsch1 else NE,
                    'p_alle_netze': ex['p_alle_netze'], 'p_durch_mittel': ex['p_durch_mittel']}
    else:
        U['GS1'] = {'plan': NE, 'kartenwortlaut': NE}
    U['GS2'] = {'plan': NE, 'kartenwortlaut': NE}
    U['GS3'] = {'plan': NE, 'kartenwortlaut': NE}
    if '512' in jeN and nz[512] >= 2:
        m512 = jeN['512']['P_P1_SV1_J']['mittel_lagen_saaten']
        U['GS2'] = {'M512': m512, 'abw': m512 - 1, 'plan': 'eingetroffen' if abs(m512 - 1) <= 1e-3 else 'nicht eingetroffen'}
        U['GS2']['kartenwortlaut'] = U['GS2']['plan']
    if '128' in jeN and '512' in jeN and entsch23:
        D128 = jeN['128']['P_P1_SV1_J']['mittel_lagen_saaten'] - 1
        D512 = jeN['512']['P_P1_SV1_J']['mittel_lagen_saaten'] - 1
        v128 = jeN['128']['kanaele']['P1']['V1']
        v512 = jeN['512']['kanaele']['P1']['V1']
        se512 = (v512['sd'] or 0.0) / math.sqrt(v512['n'])
        q_v = v512['mittel'] / v128['mittel'] if v128['mittel'] != 0 else float('inf')
        q_D = D512 / D128 if D128 != 0 else float('inf')
        plan = (v128['mittel'] * v512['mittel'] > 0) and abs(q_v - 1) <= 0.3 and abs(v512['mittel']) > 2 * se512
        wort = (D128 * D512 > 0) and abs(q_D - 1) <= 0.3 and abs(v128['mittel']) >= 0.5 * abs(D128) and abs(v512['mittel']) >= 0.5 * abs(D512)
        U['GS3'] = {'D128': D128, 'D512': D512, 'q_D': q_D, 'V1_128': v128['mittel'], 'V1_512': v512['mittel'], 'q_V1': q_v,
                    'se_V1_512': se512, 'plan': 'eingetroffen' if plan else 'nicht eingetroffen',
                    'kartenwortlaut': 'eingetroffen' if wort else 'nicht eingetroffen'}
    res['urteile'] = U
    # Bild
    if pfad_bild:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(1, 3, figsize=(18, 5.6))
        farben = {128: '#1f77b4', 256: '#ff7f0e', 512: '#2ca02c'}
        namen = [nm for nm, _, _ in bahnnormalen()]
        xi = np.arange(len(namen))
        off = {128: -0.22, 256: 0.0, 512: 0.22}
        for x in gut:
            G = [x['bahnen'][nm]['P_P1_SV1_J'] for nm in namen]
            ax[0].plot(xi + off.get(x['N'], 0), G, 'o', ms=3, color=farben.get(x['N'], 'k'), alpha=0.75)
        for N in Ns:
            ax[0].plot([], [], 'o', color=farben.get(N, 'k'), label='N = %d (%d Netze)' % (N, jeN[str(N)]['netze']))
        Gv = [av['bahnen'][nm]['P_P1_SV1_J'] for nm in namen]
        ax[0].plot(xi, Gv, 'k_', ms=9, mew=1.5, label='Netz V (J_iso), Kontrolle')
        ax[0].axhline(1, color='k', lw=0.7)
        ax[0].axhspan(1 - 1.3e-4, 1 + 1.3e-4, color='#d62728', alpha=0.25, label='Doppelpulsar +- 1,3e-4')
        ax[0].set_xticks(xi)
        ax[0].set_xticklabels(namen, rotation=90, fontsize=7)
        ax[0].set_xlabel('Bahnlage (Bahnnormale)')
        ax[0].set_ylabel('G_rad/G_N (V1+S+J, P1, Goldene Regel)')
        ax[0].set_title('Kreisbahnen: G_rad/G_N je Bahnlage und Netz')
        ax[0].legend(fontsize=7)
        a1 = ax[1]
        a1.loglog(xN, ySD, 'o', color='gray', ms=4, alpha=0.7, label='SD ueber 24 Lagen, je Netz')
        if ex:
            a1.loglog(Ns, ex['sd_mittel_je_N'], 'ks-', ms=6, label='Mittel je N')
            xx = np.array([100, 650.0])
            c_ = math.exp(np.polyfit(np.log(xN), np.log(ySD), 1)[1])
            a1.loglog(xx, c_ * xx ** ex['p_alle_netze'], 'b-', lw=1.2, label='Gerade ueber alle Netze, p = %.2f' % ex['p_alle_netze'])
            r0 = ex['sd_mittel_je_N'][0] * (xx / Ns[0]) ** (-0.4)
            a1.loglog(xx, r0, 'r:', lw=1.2, label='N^-0,4 (GS1-Schwelle)')
        a1.axhline(1.3e-4, color='#d62728', lw=0.8, ls='--', label='1,3e-4 (Doppelpulsar)')
        a1.set_xlabel('N (Punkte je Superzelle)')
        a1.set_ylabel('Streuung von G_rad/G_N ueber die Bahnlagen')
        a1.set_title('Lagenstreuung gegen N (doppellogarithmisch)')
        a1.legend(fontsize=7)
        a2 = ax[2]
        for kn, mk in (('TT', 'o-'), ('L', 's-'), ('nn', '^-'), ('V1', 'v-')):
            a2.plot(Ns, [jeN[str(N)]['kanaele']['P1'][kn]['mittel'] for N in Ns], mk, label='Zuwachs %s' % kn)
        a2.plot(Ns, [jeN[str(N)]['P_P1_SV1_J']['mittel_lagen_saaten'] - 1 for N in Ns], 'k*-', ms=9, label='Summe: Mittel - 1')
        a2.axhline(0, color='k', lw=0.6)
        a2.set_xscale('log')
        a2.set_xlabel('N')
        a2.set_ylabel('Mittel ueber Lagen und Saaten')
        a2.set_title('Kanalanteile (Zuwaechse TT, L, nn, V1)')
        a2.legend(fontsize=7)
        fig.suptitle('GLAS-STRAHLUNG-1: Kreisbahnen auf periodischen Glasnetzen (synthetische Gitterrechnung, keine Messdaten)')
        fig.tight_layout()
        fig.savefig(pfad_bild + '.tmp.png', dpi=110)
        os.replace(pfad_bild + '.tmp.png', pfad_bild)
        res['bild'] = os.path.basename(pfad_bild)
    schreibe(pfad_out, res)
    return res


# ------------------------------------------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['netz', 'aus'])
    ap.add_argument('--N', type=int, default=128)
    ap.add_argument('--saaten', default='1')
    ap.add_argument('--nt', type=int, default=6)
    ap.add_argument('--nphi', type=int, default=12)
    ap.add_argument('--kabs', type=float, default=0.01)
    ap.add_argument('--frist', type=float, default=540.0)
    ap.add_argument('--rauch', action='store_true')
    ap.add_argument('--rauch_k', type=int, default=2)
    ap.add_argument('--v')
    ap.add_argument('--ein', nargs='*')
    ap.add_argument('--bild')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t_start = time.time()
    info = {'numpy': np.__version__, 'scipy': scipy.__version__, 'torch': torch.__version__, 'python': platform.python_version(),
            'host': platform.node(), 'argv': sys.argv, 'skript_sha256': sha(os.path.abspath(__file__)),
            'tg_sha256': sha(os.path.abspath(tg.__file__)), 'dz_sha256': sha(os.path.abspath(dz.__file__)),
            'ew_sha256': sha(os.path.abspath(ew.__file__)), 'pn_sha256': sha(os.path.abspath(pn.__file__)),
            'nu_sha256': sha(os.path.abspath(nu.__file__)), 'tp_sha256': sha(os.path.abspath(tg.tp.__file__)),
            'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    if a.modus == 'aus':
        res = auswertung(a.v, sorted(a.ein), a.out, a.bild)
        print('fertig aus', 'laufzeit %.1f s' % (time.time() - t_start), flush=True)
        return
    dev = dz.geraet()
    info['geraet'] = str(dev)
    info['gpu'] = torch.cuda.get_device_name(0) if dev.type == 'cuda' else None
    saaten = [int(s) for s in a.saaten.split(',')]
    for saat in saaten:
        if time.time() - t_start > a.frist:
            print('saat %d nicht begonnen (Frist)' % saat, flush=True)
            break
        t0 = time.time()
        erg = netz_lauf(a.N, saat, a, dev, t_start)
        res = {'info': info, 'ergebnis': erg, 'laufzeit_s': time.time() - t0,
               'maxrss_MB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
               'gpu_max_MB': (torch.cuda.max_memory_allocated() / 2 ** 20) if dev.type == 'cuda' else None,
               'ende_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
        if a.rauch:
            res = {'info': info, 'schluessel': nur_schluessel(erg), 'laufzeit_s': res['laufzeit_s'], 'maxrss_MB': res['maxrss_MB'],
                   'gpu_max_MB': res['gpu_max_MB'], 't_k_s': [z['t_s'] for z in erg['zeilen']], 't_netz_s': erg['t_netz_s'],
                   'E': erg['E'], 'nV': erg['nV'], 'T': erg['T'], 'phi_eintraege': erg['phi_eintraege'],
                   'n_oben_geplant': erg['n_oben_geplant'], 'n_oben_fertig': erg['n_oben_fertig']}
        pfad = a.out if (len(saaten) == 1 and a.out.endswith('.json')) else '%s-N%d-s%d.json' % (a.out, a.N, saat)
        schreibe(pfad, res)
        print('fertig netz N=%d saat=%d richtungen=%d laufzeit %.1f s geraet %s' % (a.N, saat, len(erg['zeilen']), time.time() - t0, dev),
              flush=True)
        if erg['abgebrochen_frist']:
            break


if __name__ == '__main__':
    main()
