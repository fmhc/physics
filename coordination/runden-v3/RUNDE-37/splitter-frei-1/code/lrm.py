#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LUND-REGGE-MASSE-1 (Runde 48, fmhc-physics), Code-Agent fuer die Leitung claude-primary.

Frage: Wird die langwellige TT-Spanne klein und bleibt das Netz stabil, wenn die Bewegungsenergie die
geschwindigkeitsseitige Lund-Regge-Form ist (Summe ueber Tetraeder, danach invertiert), Reduktion R1 unveraendert?

Masse (Karte, PLAN 1):
  q_e = d(l_e^2) = 2 l_e^2 a_e (a_e = dl/l wie ew.py);  je Tetraeder dh_t = R_t q_t, R_t = P_t^-1,
  P_t[e, s] = x_e^T B6_s x_e (x_e Kantenvektor, B6 Frobenius-orthonormal, tp.B6);
  T = 1/2 Summe_t V_t G_1(dh_t', dh_t'),  G_1(X, Y) = X:Y - tr X tr Y  (lambda = 1, wie ew.py A0 / nachtrag_kinetik Ginv);
  K_karte(k) = Summe_t D_t R_t^T V_t G_1 R_t D_t (D_t = diag 2 l_e^2, Bloch-Phasen wie tg.ops_BA).
  Rechnung mit K = hm.tet_geo Kt (A2L von HODGE-MASSE-1 = TT-ISO-1 A3): K_karte = 4 V_ref K (Kontrolle K1).
  Legendre: A = K^-1 nur, wenn K regulaer ist (keine Pseudoinverse). R1: A_red = S^+ A S, B_red = S^+ B S.
Unveraendert importiert: tp, ew, tg, tti, dn, hm, nachtrag_kinetik, pn, inz, nachtrag_iso, smi (Herkunft PLAN 0).
Modi (nur ueber kleintest.sh auf der .69):
  rauch | lr0 | spanne --netz X | stabil --netz X | gang | bild --ein ... --bild ...
"""
import argparse, json, sys, os, time, hashlib, platform, resource, math
import numpy as np
import scipy.linalg as sla

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tp  # noqa: E402
import ew  # noqa: E402
import tg  # noqa: E402
import tti  # noqa: E402
import hm  # noqa: E402
import nachtrag_kinetik as nk  # noqa: E402
import pn  # noqa: E402
import inz  # noqa: E402
import nachtrag_iso as ni  # noqa: E402
import smi  # noqa: E402

KL = (0.005, 0.01, 0.02, 0.05, 0.1, 0.2)
KL_FIT = (0.005, 0.01, 0.02, 0.05, 0.1)
NETZE = ('V', 'S', 'A15', 'glas-s1', 'glas-s2', 'glas-s3', 'glas-s4')
NULL_REL = 1e-12          # Legendre: |Eigenwert von K| <= 1e-12 max gilt als null (dann keine Inverse)
NEG_REL = 1e-10           # Traegheit: Eigenwert < -1e-10 max gilt als negativ
TOL_W = 1e-9              # wachsend: Re omega^2 < -1e-9 s oder |Im omega^2| > 1e-9 s, s = max |omega^2|
GL = np.eye(6) - np.outer(tp.TR, tp.TR)
herm = hm.herm
T0 = time.time()


def sha(p):
    with open(p, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


# ------------------------------------------------------------------------------------------------ Netz und Masse
def bau(name):
    LV, pos, G, O, info = hm.netz(name)
    mod = tg.modell(LV, pos, G, O, {})
    geo = hm.tet_geo(LV, pos, G, O, mod)
    return {'name': name, 'LV': np.asarray(LV, float), 'mod': mod, 'geo': geo, 'info': info,
            'l_mittel': float(np.mean(mod['l'])), 'glas': name.startswith('glas')}


def k_karte(geo):
    """Kartenformel je Tetraeder (unabhaengig von hm.tet_geo): K_t^a = D R^T V G_1 R D."""
    X = geo['X']
    et = np.stack([X[:, j] - X[:, i] for (i, j, _, _) in tg.PAARE], 1)          # (T, 6, 3)
    P = np.einsum('tpi,sij,tpj->tps', et, tp.B6, et)                            # q = P y, dh = sum y_s B6_s
    R = np.linalg.inv(P)
    D = 2.0 * np.einsum('tpi,tpi->tp', et, et)                                  # 2 l_e^2
    Kq = geo['vol'][:, None, None] * np.einsum('tsp,su,tuq->tpq', R, GL, R)
    return D[:, :, None] * Kq * D[:, None, :]


def spec(ev):
    s = float(np.abs(ev).max())
    s = s if s > 0 else 1.0
    return {'n_neg': int((ev < -NEG_REL * s).sum()), 'n_null': int((np.abs(ev) <= NULL_REL * s).sum()),
            'absmin_rel': float(np.abs(ev).min() / s), 'min_rel': float(ev.min() / s), 'max': float(ev.max()),
            'min': float(ev.min())}


def tetra_dehnung(net, k, V):
    """Je Tetraeder Verzerrung eps_t = Phi_t^-1 u_t (B6-Koordinaten) fuer Kantenvektoren V (E, n)."""
    mod, geo = net['mod'], net['geo']
    ph = np.exp(1j * (mod['Tcopy'] @ k))                                        # (T, 6)
    U = ph[:, :, None] * V[mod['eidx']]                                         # (T, 6, n)
    return np.einsum('tsp,tpn->tsn', geo['Pi'], U)                              # (T, 6, n)


def spur_anteil(net, k, V):
    """K-gewichteter Spuranteil: Summe w |tr eps|^2/3 / Summe w |eps|^2 (rein konform = 1, gleichverteilt ~ 1/6)."""
    w = net['geo']['vol'] / net['geo']['vref']
    Y = tetra_dehnung(net, k, V)
    tr = np.einsum('s,tsn->tn', tp.TR, Y)
    num = (w[:, None] * np.abs(tr) ** 2 / 3.0).sum(0)
    den = (w[:, None] * (np.abs(Y) ** 2).sum(1)).sum(0)
    return num / np.maximum(den, 1e-300)


def weyl_anteil(net, k, V):
    """Euklidischer Anteil von V in Span{w_v} (oertliche Umskalierungen je Ecke, wie tg.ops Wh)."""
    mod = net['mod']
    E, nV = mod['E'], mod['nV']
    phe = np.exp(1j * (mod['Tedge'] @ k))
    Wh = np.zeros((E, nV), complex)
    rr = np.arange(E)
    np.add.at(Wh, (rr, mod['es']), 1.0)
    np.add.at(Wh, (rr, mod['es2']), phe)
    Qw, Rw = np.linalg.qr(Wh)
    d = np.abs(np.diag(Rw))
    Qw = Qw[:, d > 1e-9 * d.max()]
    P = Qw @ (np.conj(Qw.T) @ V)
    return (np.abs(P) ** 2).sum(0) / np.maximum((np.abs(V) ** 2).sum(0), 1e-300)


def omega2(Ar, Br, L):
    """omega^2 = Eigenwerte von A_red B_red. Mit B_red = L L^+ (pd) aehnlich zu L^+ A_red L: hermitesch, reell,
    Traegheit = Traegheit von A_red (Sylvester); sonst allgemeine Eigenwerte."""
    if L is not None:
        return np.linalg.eigvalsh(herm(np.conj(L.T) @ Ar @ L)).astype(complex)
    return np.linalg.eigvals(Ar @ Br)


def affin_paar(net, k):
    mod = net['mod']
    eps = float(np.linalg.norm(k))
    d = k / eps
    ph = np.exp(1j * (mod['mitte'] @ k))
    return np.stack([np.einsum('ei,ij,ej->e', mod['n'], h, mod['n']) * ph for h in hm.polarisationen(d)], 1)


def punkt(net, k, mit_a1=True, mit_tt=False, mit_kontr=False, mit_diag=False, mit_spektren=False, voll=True):
    """Ein Bloch-k: Masse, Legendre, R1, Spektrum; voll=False: nur Stabilitaetsgroessen."""
    t0 = time.time()
    mod, geo = net['mod'], net['geo']
    eps = float(np.linalg.norm(k))
    Bs, A1s, M, c = tg.ops(mod, k)
    B = Bs.toarray()
    K = herm(hm.assemble(mod, geo['Kt'], k))
    eK = np.linalg.eigvalsh(K)
    z = {'eps': eps, 'K': spec(eK)}
    S, Q, C, weg, svrel = hm.zerlege(M, c)
    Sh = np.conj(S.T)
    z.update({'dim': int(S.shape[1]), 'weg': weg, 'sv_rel_min': svrel})
    XQC = np.concatenate([Q, C], 1)
    KX = K @ XQC
    eQ = np.linalg.eigvalsh(herm(np.conj(Q.T) @ KX[:, :Q.shape[1]]))
    z['QKQ'] = spec(eQ)
    eX = np.linalg.eigvalsh(herm(np.conj(XQC.T) @ KX))
    z['XKX'] = spec(eX)
    if mit_spektren:
        z['K_eig'] = [float(x) for x in eK]
        z['QKQ_eig'] = [float(x) for x in eQ]
    Br = herm(Sh @ B @ S)
    eB = np.linalg.eigvalsh(Br)
    z['B_red'] = spec(eB)
    Li, L = None, None
    try:
        L = np.linalg.cholesky(Br)
        Li = sla.solve_triangular(L, np.eye(L.shape[0]), lower=True)
        z['B_red_pd'] = True
    except np.linalg.LinAlgError:
        z['B_red_pd'] = False
    if mit_a1:
        A1 = A1s.toarray()
        A1r = herm(Sh @ A1 @ S)
        eA1 = np.linalg.eigvalsh(A1r)
        w1 = omega2(A1r, Br, L)
        s1 = max(float(np.abs(w1).max()), 1e-300)
        z['A1R1'] = {'A_red': spec(eA1), 'n_wachsend': int(((w1.real < -TOL_W * s1) | (np.abs(w1.imag) > TOL_W * s1)).sum())}
        if Li is not None and voll:
            z['A1R1'].update(hm.z_auswerten(hm.Z_A(Li, A1r), eps))
    if z['K']['n_null'] > 0:
        z['legendre_regulaer'] = False
        z['t_s'] = time.time() - t0
        return z
    z['legendre_regulaer'] = True
    AS = np.linalg.solve(K, S)                                 # A S mit A = K^-1 (Legendre), ohne volle Inverse
    Ar = herm(Sh @ AS)
    eA = np.linalg.eigvalsh(Ar)
    z['A_red'] = spec(eA)
    w2 = omega2(Ar, Br, L)
    s = max(float(np.abs(w2).max()), 1e-300)
    wachs = (w2.real < -TOL_W * s) | (np.abs(w2.imag) > TOL_W * s)
    z['n_wachsend'] = int(wachs.sum())
    z['w2_min_rel'] = float(w2.real.min() / s)
    z['w2_im_max_rel'] = float(np.abs(w2.imag).max() / s)
    if mit_diag:
        ev, Y = np.linalg.eigh(Ar)
        sA = np.abs(ev).max()
        neg = ev < -NEG_REL * sA
        Vv = AS @ Y                                            # Geschwindigkeiten v = A S y der Impulsrichtungen
        fs = spur_anteil(net, k, Vv)
        fw = weyl_anteil(net, k, Vv)
        z['diag'] = {'n_neg': int(neg.sum()),
                     'spur_neg_mittel': float(fs[neg].mean()) if neg.any() else None,
                     'spur_neg_min': float(fs[neg].min()) if neg.any() else None,
                     'spur_pos_mittel': float(fs[~neg].mean()), 'spur_pos_max': float(fs[~neg].max()),
                     'weyl_neg_mittel': float(fw[neg].mean()) if neg.any() else None,
                     'weyl_pos_mittel': float(fw[~neg].mean()),
                     'Kform_neg_max': float((ev[neg] / sA).max()) if neg.any() else None}
    if voll and Li is not None and z["A_red"]["n_null"] == 0:
        r = hm.z_auswerten(hm.Z_A(Li, Ar), eps, Li, S, mit_vek=mit_tt)
        if mit_tt:
            tt = []
            for x in r.pop('_x'):
                H, rr = tg.tensor_fit(mod, S @ x, k, M)
                tt.append(float(tp.tt_anteil(H, k)[0]))
            r['tt_anteil'] = tt
        z['LR'] = r
        # affine Bezugswerte: unprojiziert (Ritz mit K, B) und auf S projiziert (Ritz mit K_red = A_red^-1, B_red)
        av = affin_paar(net, k)
        K2 = herm(np.conj(av.T) @ K @ av)
        B2 = herm(np.conj(av.T) @ B @ av)
        wa = np.linalg.eigvals(np.linalg.solve(K2, B2))
        z['affin_unproj'] = sorted(float(x) for x in wa.real / eps ** 2)
        zc = Sh @ av
        Kr = herm(np.linalg.solve(Ar, np.eye(Ar.shape[0])))
        K2p = herm(np.conj(zc.T) @ Kr @ zc)
        B2p = herm(np.conj(zc.T) @ Br @ zc)
        wp = np.linalg.eigvals(np.linalg.solve(K2p, B2p))
        z['affin_proj_ritz'] = sorted(float(x) for x in wp.real / eps ** 2)
        if mit_kontr:
            sB = np.abs(B).max()
            kk = {'BM_null': float(np.abs(B @ M).max() / (sB * np.abs(M).max())),
                  'cM_null': float(np.abs(np.conj(c.T) @ M).max() / (np.abs(c).max() * np.abs(M).max())),
                  'K_AS_minus_S': float(np.abs(K @ AS - S).max())}
            e1 = np.sort(np.linalg.eigvalsh(herm(Li @ herm(hm.rh_K(K, S, XQC)) @ np.conj(Li.T))))
            e2 = np.sort(np.linalg.eigvalsh(herm(Li @ Kr @ np.conj(Li.T))))
            kk['R1_gleich_K_schur_ueber_M_und_c'] = float(np.abs(e1 - e2).max() / np.abs(e2).max())
            kk['K_cond'] = float(np.abs(eK).max() / np.abs(eK).min())
            z['kontr'] = kk
    z['t_s'] = time.time() - t0
    return z


# ------------------------------------------------------------------------------------------------ LR0 und K1
def lauf_lr0():
    out = {}
    rng = np.random.default_rng(7)
    hs = [tp.B6[s] for s in range(6)]
    for _ in range(4):
        h = rng.normal(size=(3, 3))
        hs.append(0.5 * (h + h.T))
    for name in NETZE:
        t0 = time.time()
        net = bau(name)
        mod, geo = net['mod'], net['geo']
        Kc_t = k_karte(geo)
        k1 = float(np.abs(Kc_t / (4.0 * geo['vref']) - geo['Kt']).max() / np.abs(geo['Kt']).max())
        k0 = np.zeros(3)
        Kz = hm.assemble(mod, Kc_t, k0).real
        Vbox = mod['Vbox']
        fehler, zeilen = 0.0, []
        for h in hs:
            a = 0.5 * np.einsum('ei,ij,ej->e', mod['n'], h, mod['n'])     # a_e = dl/l bei dh = h
            kv = float(a @ Kz @ a)
            kont = Vbox * (float(np.sum(h * h)) - float(np.trace(h)) ** 2)
            f = abs(kv - kont) / (Vbox * float(np.sum(h * h)))
            fehler = max(fehler, f)
            zeilen.append({'spur': float(np.trace(h)), 'K': kv, 'kont': kont, 'fehler_rel': f})
        # Kasten k = 0 (beschreibend): Traegheit von K, Eichblock, A_red
        z0 = punkt(net, k0, mit_a1=True, voll=False, mit_diag=True, mit_spektren=False)
        out[name] = {'E': int(mod['E']), 'T': int(mod['T']), 'nV': int(mod['nV']), 'vref': geo['vref'], 'Vbox': Vbox,
                     'l_mittel': net['l_mittel'], 'geo_kontr': geo['kontr'], 'pruefung': mod['pruefung'],
                     'K1_karte_gleich_4vref_Kt': k1, 'LR0_fehler_max': fehler, 'LR0_zeilen': zeilen,
                     'kasten_k0': z0, 't_s': time.time() - t0}
    return out


# ------------------------------------------------------------------------------------------------ Spanne gegen kl
def richtungen(net):
    return tg.richtungen13w() if net['glas'] else tti.richtungen13()


def fit_kl(kls, ws):
    x = np.asarray(kls, float) ** 2
    Am = np.stack([np.ones_like(x), x, x ** 2], 1)
    cf, *_ = np.linalg.lstsq(Am, np.asarray(ws, float), rcond=None)
    return cf


def spannen_auswerten(zeilen, schl):
    """Spanne je kl, Extrapolation je Richtung und Zweig, (kl)^2-Koeffizient."""
    out = {'je_kl': {}}
    W = {}
    for z in zeilen:
        for kl in KL:
            p = z['kl%g' % kl]
            r = p.get(schl) if schl == 'LR' else p.get('A1R1')
            ok = bool(r is not None and r.get('ok') and len(r.get('w2k2', [])) == 2)
            W.setdefault(kl, []).append((ok, r['w2k2'] if ok else [np.nan, np.nan],
                                         int(r.get('n_neg', -1)) if r is not None else -1))
    for kl in KL:
        oks = [o for o, w, n in W[kl]]
        ww = np.array([w for o, w, n in W[kl]], float)
        sp = float(np.nanmax(ww) / np.nanmin(ww) - 1) if np.isfinite(ww).any() else None
        out['je_kl']['%g' % kl] = {'spanne': sp, 'alle_ok': bool(all(oks)), 'n_ok': int(sum(oks)),
                                   'n_neg_max': int(max(n for o, w, n in W[kl])),
                                   'w_min': float(np.nanmin(ww)) if sp is not None else None,
                                   'w_max': float(np.nanmax(ww)) if sp is not None else None}
    nz = len(zeilen)
    w0, w2r, alle_ok_fit = [], [], True
    for i in range(nz):
        for b in range(2):
            ws = [W[kl][i][1][b] for kl in KL_FIT]
            alle_ok_fit &= all(W[kl][i][0] for kl in KL_FIT)
            if np.all(np.isfinite(ws)):
                cf = fit_kl(KL_FIT, ws)
                w0.append(cf[0])
                w2r.append(cf[1] / cf[0])
    w0 = np.array(w0)
    sp_fit = [out['je_kl']['%g' % kl]['spanne'] for kl in KL_FIT]
    if len(w0) and all(s is not None for s in sp_fit):
        cs = fit_kl(KL_FIT, sp_fit)
        out['spanne_kl2_fit'] = {'s0': float(cs[0]), 's2': float(cs[1]), 's4': float(cs[2])}
    out['extrapolation'] = {'spanne0': float(w0.max() / w0.min() - 1) if len(w0) else None,
                            'w0_min': float(w0.min()) if len(w0) else None, 'w0_max': float(w0.max()) if len(w0) else None,
                            'w2_rel_min': float(min(w2r)) if w2r else None, 'w2_rel_max': float(max(w2r)) if w2r else None,
                            'n_zweige': int(len(w0)), 'alle_ok': bool(alle_ok_fit)}
    return out


def lauf_spanne(name, rauch=False, teil=None):
    t00 = time.time()
    net = bau(name)
    mod = net['mod']
    l = net['l_mittel']
    richt = richtungen(net)
    if rauch:
        richt = richt[:2]
    if teil is not None:                      # Glas: zwei Teillaeufe (Richtungen 0-6, 7-12), Zusammenfuehrung im Modus zusammen
        richt = richt[:7] if teil == 0 else richt[7:]
    kls = KL if not rauch else (0.01, 0.2)
    zeilen = []
    for nm, d in richt:
        z = {'richtung': nm, 'd': d.tolist()}
        for kl in kls:
            k = (kl / l) * d
            tt3 = nm in ('100', '110', '111')
            z['kl%g' % kl] = punkt(net, k, mit_a1=True, mit_tt=(tt3 and kl == 0.01),
                                   mit_kontr=(nm in ('100', '111') and kl == 0.01), mit_diag=(kl in (0.01, 0.2)),
                                   mit_spektren=(nm in ('100', '111') and kl == 0.01))
        zeilen.append(z)
    out = {'netz': name, 'E': int(mod['E']), 'T': int(mod['T']), 'nV': int(mod['nV']), 'l_mittel': l,
           'vref': net['geo']['vref'], 'info': net['info'], 'zeilen': zeilen, 'kl': list(kls), 'teil': teil}
    if not rauch and teil is None:
        out['LR'] = spannen_auswerten(zeilen, 'LR')
        out['A1R1'] = spannen_auswerten(zeilen, 'A1R1')
    out['t_s'] = time.time() - t00
    return out


# ------------------------------------------------------------------------------------------------ Stabilitaet
def k_gitter(net, rauch=False):
    LV = net['LV']
    BVc = 2 * np.pi * np.linalg.inv(LV).T
    if net['glas']:
        n = 4                                 # Glas: 4^3-Gitter der Superzelle, 36 k-Klassen mit Gamma (PLAN 5, Zeitbox)
        g = np.arange(n)
        mm = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1).reshape(-1, 3)
        rep = {}
        for m in mm:
            a = tuple(int(x) for x in m)
            b = tuple(int(x) for x in np.mod(-m, n))
            rep.setdefault(min(a, b), None)
        ms = np.array(sorted(rep.keys()), float)
        ks = (ms / n) @ BVc
    else:
        n = 8
        g = np.arange(n)
        mm = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1).reshape(-1, 3)
        ms = mm[np.any(mm != 0, axis=1)].astype(float)
        ks = (ms / n) @ BVc
    if rauch:
        ms, ks = ms[:6], ks[:6]
    return n, ms, ks


def lauf_stabil(name, rauch=False, teil=None):
    t00 = time.time()
    net = bau(name)
    n, ms, ks = k_gitter(net, rauch)
    if teil is not None:                      # Glas: zwei Teillaeufe (erste bzw. zweite Haelfte der k-Klassen)
        h = len(ms) // 2
        ms, ks = (ms[:h], ks[:h]) if teil == 0 else (ms[h:], ks[h:])
    zeilen = []
    for m, k in zip(ms, ks):
        p = punkt(net, k, mit_a1=True, voll=False, mit_diag=True)
        p['m'] = [int(x) for x in m]
        zeilen.append(p)
    gamma = None
    if not net['glas'] and not rauch:
        gamma = punkt(net, np.zeros(3), mit_a1=True, voll=False, mit_diag=True)
    out = {'netz': name, 'E': int(net['mod']['E']), 'T': int(net['mod']['T']), 'nV': int(net['mod']['nV']),
           'gitter_n': n, 'teil': teil, 'zusammen': stabil_zusammen(zeilen, n), 'gamma': gamma, 'zeilen': zeilen,
           't_s': time.time() - t00}
    return out


def stabil_zusammen(zeilen, n):
    def zaehl(f):
        return int(sum(1 for p in zeilen if f(p)))
    nicht_gamma = [p for p in zeilen if any(p['m'])]
    reg = [p for p in nicht_gamma if p['legendre_regulaer']]
    zus = {'nk': len(zeilen), 'nk_ohne_gamma': len(nicht_gamma), 'gitter_n': n,
           'k_K_singulaer': zaehl(lambda p: not p['legendre_regulaer']),
           'k_K_fast_singulaer_1e-8': zaehl(lambda p: p['K']['absmin_rel'] < 1e-8),
           'k_A_red_nicht_pd': int(sum(1 for p in reg if p['A_red']['n_neg'] > 0)),
           'k_wachsend': int(sum(1 for p in reg if p['n_wachsend'] > 0)),
           'summe_A_red_neg': int(sum(p['A_red']['n_neg'] for p in reg)),
           'summe_wachsend': int(sum(p['n_wachsend'] for p in reg)),
           'max_A_red_neg': int(max([p['A_red']['n_neg'] for p in reg], default=0)),
           'k_B_red_neg': int(sum(1 for p in nicht_gamma if p['B_red']['n_neg'] > 0)),
           'K_n_neg_bereich': [int(min(p['K']['n_neg'] for p in zeilen)), int(max(p['K']['n_neg'] for p in zeilen))],
           'QKQ_n_neg_bereich': [int(min(p['QKQ']['n_neg'] for p in zeilen)), int(max(p['QKQ']['n_neg'] for p in zeilen))],
           'QKQ_absmin_rel_min': float(min(p['QKQ']['absmin_rel'] for p in zeilen)),
           'XKX_n_neg_bereich': [int(min(p['XKX']['n_neg'] for p in zeilen)), int(max(p['XKX']['n_neg'] for p in zeilen))],
           'XKX_absmin_rel_min': float(min(p['XKX']['absmin_rel'] for p in zeilen)),
           'K_absmin_rel_min': float(min(p['K']['absmin_rel'] for p in zeilen)),
           'w2_min_rel': float(min([p['w2_min_rel'] for p in reg], default=np.nan)),
           'A1R1_k_wachsend': int(sum(1 for p in nicht_gamma if p['A1R1']['n_wachsend'] > 0)),
           'A1R1_k_A_red_nicht_pd': int(sum(1 for p in nicht_gamma if p['A1R1']['A_red']['n_neg'] > 0))}
    sn = [p['diag']['spur_neg_mittel'] for p in reg if p.get('diag') and p['diag']['n_neg'] > 0]
    sp = [p['diag']['spur_pos_mittel'] for p in reg if p.get('diag')]
    wn = [p['diag']['weyl_neg_mittel'] for p in reg if p.get('diag') and p['diag']['n_neg'] > 0]
    wp = [p['diag']['weyl_pos_mittel'] for p in reg if p.get('diag')]
    smin = [p['diag']['spur_neg_min'] for p in reg if p.get('diag') and p['diag']['n_neg'] > 0]
    zus['diag'] = {'spur_neg_mittel': float(np.mean(sn)) if sn else None, 'spur_neg_min': float(min(smin)) if smin else None,
                   'spur_pos_mittel': float(np.mean(sp)) if sp else None,
                   'weyl_neg_mittel': float(np.mean(wn)) if wn else None, 'weyl_pos_mittel': float(np.mean(wp)) if wp else None}
    return zus


def lauf_zusammen(pfade):
    teile = []
    for p in pfade:
        with open(p) as fh:
            teile.append(json.load(fh)['ergebnis'])
    return zusammen_aus(teile)


def zusammen_aus(teile):
    """Teillaeufe eines Netzes zusammenfuehren (Spanne: Zeilen in Richtungsfolge; Stabilitaet: alle k-Klassen)."""
    teile = sorted(teile, key=lambda d: d['teil'])
    d0 = teile[0]
    out = {k: v for k, v in d0.items() if k not in ('zeilen', 'zusammen', 't_s', 'teil')}
    out['teile'] = [d['teil'] for d in teile]
    out['t_s_teile'] = [d['t_s'] for d in teile]
    zeilen = [z for d in teile for z in d['zeilen']]
    out['zeilen'] = zeilen
    if 'kl' in d0:
        out['LR'] = spannen_auswerten(zeilen, 'LR')
        out['A1R1'] = spannen_auswerten(zeilen, 'A1R1')
    else:
        out['zusammen'] = stabil_zusammen(zeilen, d0['gitter_n'])
    return out


# ------------------------------------------------------------------------------------------------ Bahnlagen-Gang (V)
def vorbereiten_lr(mod, Q, ndir, s, mats, chunk=50):
    """wie smi.vorbereiten, aber A = K^-1 (Lund-Regge, nk.zell_matrizen Teil 3) statt Summe J_t A_t."""
    teile = []
    for i0 in range(0, len(ndir), chunk):
        nn = ndir[i0:i0 + chunk]
        k = s * nn
        o = ew.ops(mod, k)
        B, M, c = o['B'], o['M'], o['c']
        S, r = inz.basis(None, M, c)
        Sh = pn.cT(S)
        Bred = herm(Sh @ B @ S)
        lb, Vb = np.linalg.eigh(Bred)
        K = herm(nk.assemble(mod, k, mats, 3))
        eK = np.linalg.eigvalsh(K)
        sK = np.abs(eK).max(-1)
        Kinfo = np.stack([(eK < -NEG_REL * sK[:, None]).sum(-1), (np.abs(eK) <= NULL_REL * sK[:, None]).sum(-1)], 1)
        A = herm(np.linalg.inv(K))
        Ared = herm(Sh @ A @ S)
        ph = np.exp(1j * (k @ mod['mitte'].T))
        Tb = np.zeros((len(nn), 6, 3, 3))
        LD = np.zeros((len(nn), 2))
        for j, n in enumerate(nn):
            tens, e1, e2 = ni.basis_tt(n)
            for a, nm in enumerate(smi.NAMEN6):
                Tb[j, a] = tens[nm]
            Lam = inz.lam_proj(n, np.diag(n ** 2))
            LD[j] = [np.sum(Lam * tens['h+']), np.sum(Lam * tens['hx'])]
        aff = np.einsum('ei,kaij,ej->kae', mod['n'], Tb[:, :2], mod['n']) * ph[:, None, :]
        Y = np.einsum('ked,kae->kda', np.conj(S), aff)
        Mx = Tb - np.einsum('kaii->ka', Tb)[:, :, None, None] * np.eye(3)
        sig = np.einsum('eij,kaij->kae', Q, Mx) * ph[:, None, :]
        f0 = np.einsum('ked,kae->kad', np.conj(S), -sig)
        MhM = herm(pn.cT(M) @ M)
        zz = np.linalg.solve(MhM, np.einsum('kev,kae->kva', np.conj(M), sig))
        PMs = np.einsum('kev,kva->kae', M, zz)
        SAP = np.einsum('ked,kae->kad', np.conj(S), np.einsum('kef,kaf->kae', A, PMs))
        teile.append({'rang': r, 'Bred': Bred, 'lb': lb, 'Vs': Vb[:, :, :2], 'Ared': Ared, 'Tb': Tb, 'LD': LD, 'Y': Y,
                      'f0': f0, 'SAP': SAP, 'Kinfo': Kinfo})
    pre = {key: np.concatenate([d[key] for d in teile], axis=0) for key in teile[0]}
    pre['s'] = float(s)
    pre['n'] = np.asarray(ndir)
    return pre


def auswerten_lr(pre, kopplung=True):
    """wie smi.auswerten, mit A_red und S^+ A P_M sigma der Lund-Regge-Masse."""
    s = pre['s']
    Ared = pre['Ared']
    eA = np.linalg.eigvalsh(Ared)
    out = {'A_red_nicht_pd': int((eA.min(-1) <= 0).sum())}
    if out['A_red_nicht_pd'] > 0:
        return out
    L = np.linalg.cholesky(Ared)
    om2, U = np.linalg.eigh(herm(pn.cT(L) @ pre['Bred'] @ L))
    out.update({'w2': om2[:, :2] / s ** 2, 'luecke': om2[:, 2] / om2[:, 1]})
    if kopplung:
        X = L @ U[:, :, :2]
        fJ = -np.linalg.solve(Ared, np.swapaxes(pre['SAP'], 1, 2))
        f = pre['f0'] + np.swapaxes(fJ, 1, 2)
        g = np.einsum('kdj,kad->kja', np.conj(X), f)
        CE = 4 * smi.VCELL ** 2 / s ** 2
        out['Gn'] = g / np.sqrt(om2[:, :2, None] * CE)
        gs = np.einsum('kdj,kad->kja', np.conj(pre['Vs']), f)
        out['tau_dyn'] = np.linalg.solve(out['Gn'][:, :, :2], out['Gn'][:, :, 2:])
        out['tau_stat'] = np.linalg.solve(gs[:, :, :2], gs[:, :, 2:])
    return out


def lauf_gang(rauch=False):
    t00 = time.time()
    mod = ew.baue('V')
    tder = pn.tet_ableitungen(mod)
    Q = ni.Q_map(mod, tder)
    nd, wd = pn.richtungen(10, 20)
    if rauch:
        nd, wd = nd[:20], wd[:20]
    bl = smi.bahnen()
    m4 = np.array([float((m ** 4).sum()) for _, m, _ in bl])
    mats = nk.zell_matrizen(mod)
    s01 = smi.KL_GANG / smi.LP
    out = {'kl': smi.KL_GANG, 'LP': smi.LP, 's': s01, 'nd': int(len(nd)), 'bahnen': [b[0] for b in bl],
           'summe_m4': m4.tolist()}
    # Kontrollen: impulsseitig J_iso (smi.G_P) und J = 1 (IMPULS-NETZ-1 5.2)
    pre0 = smi.vorbereiten(mod, Q, nd, s01)
    for tag, w in (('J_iso', smi.W_ISO), ('J1', np.ones(len(smi.ARTEN)))):
        a = smi.auswerten(pre0, w)
        G = smi.G_exakt(a['Gn'], pre0['Tb'], wd, bl)
        out['kontr_' + tag] = {'G': G.tolist(), 'gang': smi.gang_fit(G, m4),
                               'w2_spanne': float(a['w2'].max() / a['w2'].min() - 1)}
    out['kontr_J_iso']['abw_gegen_G_P_max'] = float(max(abs(out['kontr_J_iso']['G'][i] - smi.G_P[b[0]])
                                                         for i, b in enumerate(bl)))
    # Lund-Regge, kl = 0,01
    pre = vorbereiten_lr(mod, Q, nd, s01, mats)
    out['K_n_neg_bereich'] = [int(pre['Kinfo'][:, 0].min()), int(pre['Kinfo'][:, 0].max())]
    out['K_n_null_max'] = int(pre['Kinfo'][:, 1].max())
    a = auswerten_lr(pre)
    out['A_red_nicht_pd'] = a['A_red_nicht_pd']
    if a['A_red_nicht_pd'] == 0:
        G = smi.G_exakt(a['Gn'], pre['Tb'], wd, bl)
        out['LR'] = {'G': G.tolist(), 'gang': smi.gang_fit(G, m4), 'w2_spanne': float(a['w2'].max() / a['w2'].min() - 1),
                     'luecke_max': float(a['luecke'].max())}
        kr, ki, rest = smi.kappa_fit(a['tau_dyn'][:, :, 2], pre['LD'], wd)
        out['LR']['kappa'] = {'re': kr, 'im': ki, 'rest': rest}
        Gtt = []
        for nm, m, T in bl:
            Ta = np.einsum('kaij,ij->ka', pre['Tb'], T)
            amp = np.einsum('kja,ka->kj', a['Gn'][:, :, :2], Ta[:, :2])
            Gtt.append(float((wd * (np.abs(amp) ** 2).sum(-1)).sum() / (wd * (np.abs(Ta[:, :2]) ** 2).sum(-1)).sum()))
        out['LR']['G_nur_TT'] = Gtt
    # beschreibend: k -> 0 (tau_stat, Lagrange in s^2 wie smi.gang_null)
    if not rauch:
        lw = smi.lagrange0(list(smi.S0_LISTE))
        Gs, ok = [], True
        for s0 in smi.S0_LISTE:
            p = vorbereiten_lr(mod, Q, nd, s0, mats)
            aa = auswerten_lr(p)
            if aa['A_red_nicht_pd'] > 0:
                ok = False
                break
            Gs.append(smi.G_tau(aa['tau_stat'], p['Tb'], wd, bl))
        if ok:
            G0 = sum(lw[i] * Gs[i] for i in range(len(Gs)))
            out['LR_null'] = {'G0': G0.tolist(), 'gang': smi.gang_fit(G0, m4)}
    out['t_s'] = time.time() - t00
    return out


# ------------------------------------------------------------------------------------------------ Bild
def lauf_bild(pfade, pfad_bild, daten=None):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    if daten is None:
        daten = {}
        for p in pfade:
            with open(p) as fh:
                d = json.load(fh)['ergebnis']
            daten[d['netz']] = d
    fig, axs = plt.subplots(1, 2, figsize=(12, 4.8))
    farben = {'V': '#1f77b4', 'S': '#d62728', 'A15': '#2ca02c'}
    for ax, glas in zip(axs, (False, True)):
        for nm, d in sorted(daten.items()):
            if nm.startswith('glas') != glas:
                continue
            col = farben.get(nm, '#7f7f7f') if not glas else None
            for schl, ls, mk in (('LR', '-', 'o'), ('A1R1', '--', 's')):
                kl = [float(x) for x in d[schl]['je_kl']]
                sp = [d[schl]['je_kl'][x]['spanne'] for x in d[schl]['je_kl']]
                ok = [d[schl]['je_kl'][x]['alle_ok'] for x in d[schl]['je_kl']]
                kx = [a for a, b in zip(kl, sp) if b is not None and b > 0]
                sy = [b for b in sp if b is not None and b > 0]
                lab = '%s %s' % (nm, 'Lund-Regge R1' if schl == 'LR' else 'impulsseitig A1R1 (J = 1)')
                ln = ax.plot(kx, sy, ls=ls, marker=mk, color=col, label=lab, mfc='none' if schl == 'A1R1' else None)
                nok = [a for a, b, o in zip(kl, sp, ok) if b is not None and b > 0 and not o]
                if nok:
                    ax.plot(nok, [b for a, b, o in zip(kl, sp, ok) if b is not None and b > 0 and not o], 'x', color=ln[0].get_color(), ms=10)
        ax.set_xscale('log')
        ax.set_yscale('log')
        ax.set_xlabel('kl (l = mittlere Kantenlaenge)')
        ax.set_ylabel('TT-Spanne max/min - 1 von omega^2/k^2')
        ax.set_title('Glas N = 128 (4 Saaten)' if glas else 'Kristalle V, S (= C15), A15')
        ax.grid(True, which='both', alpha=0.3)
        ax.legend(fontsize=6.5, ncol=1)
    fig.suptitle('LUND-REGGE-MASSE-1: geschwindigkeitsseitig (Lund-Regge, R1) gegen impulsseitig (A1R1); x = Punkt nicht regulaer')
    fig.tight_layout()
    fig.savefig(pfad_bild, dpi=130)
    return {'bild': pfad_bild, 'netze': sorted(daten.keys())}


# ------------------------------------------------------------------------------------------------ Rauchtest
def lauf_rauch():
    out = {}
    t = time.time()
    out['spanne_V'] = lauf_spanne('V', rauch=True)
    out['t_spanne_V'] = time.time() - t
    t = time.time()
    out['stabil_V'] = lauf_stabil('V', rauch=True)
    out['t_stabil_V'] = time.time() - t
    t = time.time()
    net = bau('glas-s1')
    out['t_bau_glas'] = time.time() - t
    t = time.time()
    p = punkt(net, (0.01 / net['l_mittel']) * np.array([1.0, 0, 0]), mit_a1=True, mit_diag=True)
    out['t_punkt_glas_voll'] = time.time() - t
    t = time.time()
    p = punkt(net, np.array([0.3, 0.1, 0.2]), mit_a1=True, voll=False, mit_diag=True)
    out['t_punkt_glas_stabil'] = time.time() - t
    t = time.time()
    out['gang'] = lauf_gang(rauch=True)
    out['t_gang_rauch20'] = time.time() - t
    # Codeprobe der Teillaeufe und der Zusammenfuehrung (Werte werden nicht ausgegeben)
    t = time.time()
    voll_V = lauf_spanne('V')
    tV = [lauf_spanne('V', teil=0), lauf_spanne('V', teil=1)]
    zV = zusammen_aus(tV)
    out['zusammen_spanne_V_gleich'] = bool(zV['LR']['je_kl'] == voll_V['LR']['je_kl'])
    out['t_spanne_V_voll_und_teile'] = time.time() - t
    t = time.time()
    sG = [lauf_stabil('glas-s1', rauch=True, teil=0), lauf_stabil('glas-s1', rauch=True, teil=1)]
    out['zusammen_stabil_glas'] = zusammen_aus(sG)['zusammen']
    out['t_stabil_glas_6k'] = time.time() - t
    t = time.time()
    lauf_bild(None, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rauch', 'rauch-bild.png'),
              daten={'V': voll_V})
    out['t_bild'] = time.time() - t
    return out


def nur_schluessel(x, tiefe=0):
    if isinstance(x, dict):
        return {k: nur_schluessel(v, tiefe + 1) for k, v in x.items()} if tiefe < 2 else sorted(x.keys())
    if isinstance(x, list):
        return 'list[%d]' % len(x)
    return type(x).__name__


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['rauch', 'lr0', 'spanne', 'stabil', 'gang', 'zusammen', 'bild'])
    ap.add_argument('--teil', type=int, choices=[0, 1])
    ap.add_argument('--netz', choices=list(NETZE))
    ap.add_argument('--ein', nargs='*')
    ap.add_argument('--bild')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    hier = os.path.dirname(os.path.abspath(__file__))
    info = {'numpy': np.__version__, 'python': platform.python_version(), 'host': platform.node(),
            'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'argv': sys.argv,
            'sha256': {f: sha(os.path.join(hier, f)) for f in sorted(os.listdir(hier)) if f.endswith('.py')}}
    if a.modus == 'rauch':
        erg = lauf_rauch()
    elif a.modus == 'lr0':
        erg = lauf_lr0()
    elif a.modus == 'spanne':
        erg = lauf_spanne(a.netz, teil=a.teil)
    elif a.modus == 'stabil':
        erg = lauf_stabil(a.netz, teil=a.teil)
    elif a.modus == 'gang':
        erg = lauf_gang()
    elif a.modus == 'zusammen':
        erg = lauf_zusammen(a.ein)
    else:
        erg = lauf_bild(a.ein, a.bild)
    res = {'info': info, 'ergebnis': erg, 'laufzeit_s': time.time() - t0,
           'maxrss_MB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
           'ende_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    if a.modus == 'rauch':
        res = {'info': info, 'schluessel': nur_schluessel(erg), 'zeiten': {k: v for k, v in erg.items() if k.startswith('t_')},
               'codeprobe_zusammen_gleich': erg.get('zusammen_spanne_V_gleich'),
               'laufzeit_s': res['laufzeit_s'], 'maxrss_MB': res['maxrss_MB']}
    with open(a.out + '.tmp', 'w') as fh:
        json.dump(res, fh, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else (o.tolist() if hasattr(o, 'tolist') else str(o)))
    os.replace(a.out + '.tmp', a.out)
    print('fertig', a.modus, a.netz or '', 'laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
