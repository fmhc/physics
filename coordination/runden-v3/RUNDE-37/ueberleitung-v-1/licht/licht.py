#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UEBERLEITUNG-V-1, Folgeauftrag ohne Karte (Leitung, Finn: "einfach machen und ausprobieren"):
Laufen Licht und Schwerewellen auf V mit derselben Uhr gleich schnell?

Uhr: Eigenzeit T der Zeltstangen im 4D-Zeltnetz V mal Zeit (Arm V-A, Hoehe tau = h, Hintergrund-Lapse N = 1 in T).
  GW   : stetige Grenzform aus nachtrag2_uv.py (h = 2^-8 ... 2^-14, M_eff, B, R1), Datei nt3r.json (Einlesen in 'aw').
  W4D  : Licht als 4D-Maxwell auf DEMSELBEN Zeltnetz (Whitney-1-Formen, F = dA je 4-Simplex konstant,
         S = Summe_s Vol_s |F_s|^2 / 2, euklidisch), gleiche 3+1-Zerlegung wie die Schwerkraft (Schichtkanten a,
         Zeltstangen phi = A_T, Diagonal-Reste L per Schur), gleiche Grenze h = 2^-8 ... 2^-14, dann phi per Schur,
         Eichung d0 heraus, omega^2 = Eigenwerte von K^-1 V.
  DEC  : Licht wie HOEHE-ISOTROP-1 (hi.licht_op, Kammermitte), 3+1 mit Lapse 1 in derselben Zeit T.
Importiert unveraendert: uv.py (mit rk, rk2, tg, hm, ...), hi.py (mit rv, danzer_naeherung, licht_netz).
Modi: kontrolle | dec | w4d | aw
"""
import argparse, json, sys, os, time, platform, types
import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import uv  # noqa: E402
import rk  # noqa: E402
import rk2  # noqa: E402
import tg  # noqa: E402

H_F = [2.0 ** -j for j in range(8, 15)]
H_G = [2.0 ** -j for j in range(4, 11)]        # Folge "grob": 2^-4 ... 2^-10 (weniger Rundung), quartisch durch 5
EXTRA = {"fein": (H_F, 3), "grob": (H_G, 5)}
W_Q = uv.lagrange0(H_F[-3:])
W_L = uv.lagrange0(H_F[-2:])
IU = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


def herm(X):
    return 0.5 * (X + np.conj(X.T))


# ------------------------------------------------------------------------------------------------ 4D-Maxwell
def maxwell_lokal(g):
    """Je 4-Simplex: G6 (6 x 10) bildet die Kantenwerte (kanonische Richtung) auf F_{mu<nu} ab; H_s = Vol_s G6^T G6."""
    S = g.S
    G = np.zeros((S, 6, 10))
    vol = np.zeros(S)
    for s, Sv in enumerate(g.simp):
        X = g.Xs[s]
        M = X[1:] - X[0]
        grad = np.zeros((5, 4))
        grad[1:] = np.linalg.inv(M).T
        grad[0] = -grad[1:].sum(0)
        vol[s] = abs(np.linalg.det(M)) / 24.0
        for i, (a, c) in enumerate(rk.PAARE5):
            key, T = rk.kanon_kante(Sv[a], Sv[c])
            sg = 1.0 if (key[0] == Sv[a][0] and tuple(T) == tuple(int(x) for x in Sv[a][1])) else -1.0
            w = np.outer(grad[a], grad[c]) - np.outer(grad[c], grad[a])
            G[s, :, i] = sg * 2.0 * np.array([w[m, n] for (m, n) in IU])
    H = vol[:, None, None] * np.einsum('sai,saj->sij', G, G)
    return G, H, vol


class Licht4:
    def __init__(self, h):
        self.V = uv.Vier('V', h)
        self.h = float(h)
        g = self.V.g
        self.G, self.Hl, self.vol = maxwell_lokal(g)
        ns = types.SimpleNamespace(egid=g.egid, eT=g.eT, Tphys=g.Tphys, Hloc=self.Hl, NE=g.NE)
        self.lau = rk2.Laurent(ns)

    def J_mats(self, ks, w1=0.5, w2=0.5):
        V = self.V
        nq, NV, nd = V.nq, V.NV, len(V.diag)
        ncol = nq + NV + nd
        J = {m: np.zeros((V.NE, ncol), complex) for m in (-1, 0, 1)}

        def zeitteil(e, b1, b2, phb2, dT, dt):
            s1, s2 = V.schichten(dT, dt)
            J[s1][e, nq + b1] += w1 * dT
            J[s2][e, nq + b2] += w2 * phb2 * dT

        rph = np.exp(1j * (V.r_Rd @ ks))
        for i, e in enumerate(V.raum):
            J[0][e, i] = 1.0
            zeitteil(e, V.r_b1[i], V.r_b2[i], rph[i], V.r_dT[i], 0)
        for b, e in V.zelt.items():
            J[0][e, nq + b] = self.h
        ph = np.exp(1j * (V.Rd @ ks))
        for j, e in enumerate(V.diag):
            p = V.partner[j]
            J[0][e, p] += 0.5
            J[int(V.dt[j])][e, p] += 0.5
            zeitteil(e, V.b1[j], V.b2[j], ph[j], V.dT[j], int(V.dt[j]))
            J[0][e, nq + NV + j] = 1.0
        return J

    def bloecke(self, ks, pmax=2):
        h = self.h
        C = self.lau.koeff(np.asarray(ks, float))
        fak = [1.0, 1.0, 2.0, 6.0, 24.0]
        Hp = [sum(C[m] * (1j * m * h) ** p for m in C) / fak[p] for p in range(pmax + 1)]
        Jm = self.J_mats(ks)
        Jp = [sum(Jm[m] * (1j * m * h) ** p for m in Jm) / fak[p] for p in range(pmax + 1)]
        JpH = [np.conj(X.T) for X in Jp]
        P = []
        for p in range(pmax + 1):
            X = 0.0
            for a in range(p + 1):
                for b in range(p + 1 - a):
                    X = X + JpH[a] @ Hp[b] @ Jp[p - a - b]
            P.append(X / h)
        V = self.V
        nK = V.nq + V.NV
        IK = list(range(nK))
        IL = list(range(nK, nK + len(V.diag)))
        S, kond = uv.schur_reihe(np.array(P), IK, IL)
        return S, kond


def d0_raum(V, ks):
    """Raeumliche Eichung auf den Schichtkanten: (d0 chi)_e = chi_b2 exp(i k.R_d) - chi_b1."""
    D = np.zeros((V.nq, V.NV), complex)
    ph = np.exp(1j * (V.r_Rd @ ks))
    for i in range(V.nq):
        D[i, V.r_b2[i]] += ph[i]
        D[i, V.r_b1[i]] -= 1.0
    return D


def w4d_punkt(L4, ks):
    eps = float(np.linalg.norm(ks))
    V0 = L4[0].V
    nq, NV = V0.nq, V0.NV
    IA = list(range(nq)); IP = list(range(nq, nq + NV))
    Sh, kond = [], []
    for L in L4:
        S, kd = L.bloecke(ks)
        if S is None:
            return {'definiert': False, 'grund': 'D0'}
        Sh.append(S); kond.append(kd)
    Sh = np.array(Sh)
    hs, nf = L4[-1].hset
    Q = np.einsum("j,jpab->pab", uv.lagrange0(hs[-nf:]), Sh[-nf:])
    Ql = np.einsum("j,jpab->pab", uv.lagrange0(hs[-(nf - 1):]), Sh[-(nf - 1):])
    out = {'eps': eps, 'L_kond_max': float(max(kond)),
           'e_K': float(np.linalg.norm(Q[2][np.ix_(IA, IA)] - Ql[2][np.ix_(IA, IA)]) / np.linalg.norm(Q[2][np.ix_(IA, IA)])),
           'aend_K': float(np.linalg.norm(Sh[-1][2][np.ix_(IA, IA)] - Sh[-2][2][np.ix_(IA, IA)])
                           / np.linalg.norm(Sh[-1][2][np.ix_(IA, IA)]))}
    Sa, kp = uv.schur_reihe(Q, IA, IP)
    out['phi_kond'] = kp
    if Sa is None:
        out.update({'definiert': False, 'grund': 'phi'})
        return out
    D = d0_raum(V0, ks)
    out['eich_rest'] = [float(np.linalg.norm(Sa[p] @ D) / max(np.linalg.norm(Sa[p]) * np.linalg.norm(D), 1e-300))
                        for p in range(3)]
    U, sv, _ = np.linalg.svd(D, full_matrices=True)
    r = int((sv > 1e-9 * sv[0]).sum())
    Qc = U[:, r:]
    K = herm(np.conj(Qc.T) @ Sa[2] @ Qc)
    Vp = herm(np.conj(Qc.T) @ Sa[0] @ Qc)
    G1 = np.conj(Qc.T) @ Sa[1] @ Qc
    out['ungerade_rel'] = float(np.linalg.norm(G1) * eps / max(np.linalg.norm(Vp), 1e-300))
    eK = np.linalg.eigvalsh(K)
    out['K_min_rel'] = float(eK.min() / np.abs(eK).max())
    out['K_n_neg'] = int((eK < 0).sum())
    try:
        Lc = np.linalg.cholesky(K)
        Li = np.linalg.inv(Lc)
        w2 = np.linalg.eigvalsh(herm(Li @ Vp @ np.conj(Li.T)))
        out['K_pd'] = True
    except np.linalg.LinAlgError:
        w2 = np.sort(np.linalg.eigvals(np.linalg.solve(K, Vp)).real)
        out['K_pd'] = False
    s = float(np.abs(w2).max())
    out['n_wachsend'] = int((w2 < -1e-9 * s).sum())
    o = np.argsort(np.abs(w2))
    out['w2k2'] = sorted(float(w2[j]) / eps ** 2 for j in o[:2])
    out['luecke'] = float(abs(w2[o[1]]) / abs(w2[o[2]]))
    out['ok'] = bool(min(out['w2k2']) > 0 and out['luecke'] < 1e-2)
    out['dim'] = int(Qc.shape[1])
    out['definiert'] = True
    return out


# ------------------------------------------------------------------------------------------------ DEC (hi.py)
def dec_operator():
    import hi
    ctx = hi.kontext(1)
    st = hi.sterne_licht(ctx['net'], ctx['topo'], ctx['mb'], ctx['w_mid'])
    diag = hi.neue_diag()
    op = hi.licht_op(ctx['mb'], st['s1'], st['S2'], diag)
    return op, diag, {'id_T2': st.get('id_T2'), 'sterne_positiv': bool(hi.sterne_positiv(st))}


# ------------------------------------------------------------------------------------------------ Laeufe
def raster_pts(lm):
    pts = []
    for p in uv.raster(lm):
        if p['art'] == 'kl':
            pts.append(p)
    return pts


def modus_kontrolle():
    out = {}
    rng = np.random.default_rng(20261005)
    for h in (1.0, H_F[-1]):
        L = Licht4(h)
        g = L.V.g
        # Whitney-Exaktheit: lineares A -> F je Simplex exakt
        F = rng.normal(size=(4, 4)); F = F - F.T
        Avec = lambda x: 0.5 * x @ F                                   # A_nu = 1/2 x^mu F_mu,nu
        mx = 0.0
        for s in range(0, g.S, 7):
            Sv = g.simp[s]
            Ae = np.zeros(10)
            for i, (a, c) in enumerate(rk.PAARE5):
                key, T = rk.kanon_kante(Sv[a], Sv[c])
                sg = 1.0 if (key[0] == Sv[a][0] and tuple(T) == tuple(int(x) for x in Sv[a][1])) else -1.0
                xa, xc = g.Xs[s, a], g.Xs[s, c]
                Ae[i] = sg * Avec(0.5 * (xa + xc)) @ (xc - xa)
            Fs = L.G[s] @ Ae
            mx = max(mx, float(np.abs(Fs - np.array([F[m, n] for (m, n) in IU])).max() / np.abs(F).max()))
        # Laurent gegen direkte Bloch-Summe, Eichnullvektoren bei komplexem k_t
        k1 = k2 = 0.0
        for _ in range(4):
            k = rng.uniform(-np.pi, np.pi, 4); k[3] = rng.uniform(-np.pi, np.pi) / h
            C = L.lau.koeff(k[:3])
            Hl = sum(Cm * np.exp(1j * k[3] * h) ** m for m, Cm in C.items())
            ph = np.exp(1j * (g.Tphys @ k))
            W = L.Hl * (np.conj(ph)[:, :, None] * ph[:, None, :])
            idx = (g.egid[:, :, None] * g.NE + g.egid[:, None, :]).ravel()
            Hd = (np.bincount(idx, W.real.ravel(), minlength=g.NE ** 2)
                  + 1j * np.bincount(idx, W.imag.ravel(), minlength=g.NE ** 2)).reshape(g.NE, g.NE)
            k1 = max(k1, float(np.abs(Hl - Hd).max() / np.abs(Hd).max()))
            kt = k[3] + 1j * rng.uniform(-2, 2) / h
            Hc = sum(Cm * np.exp(1j * kt * h) ** m for m, Cm in C.items())
            kk = np.r_[k[:3], kt]
            D = np.zeros((g.NE, g.NV), complex)
            ph2 = np.exp(1j * (g.Rd @ kk))
            for e in range(g.NE):
                D[e, g.b2[e]] += ph2[e]
                D[e, g.b1[e]] -= 1.0
            k2 = max(k2, float(np.linalg.norm(Hc @ D) / (np.linalg.norm(Hc) * np.linalg.norm(D))))
        out['h=%g' % h] = {'whitney_exakt': mx, 'laurent': k1, 'eich': k2, 'vol_summe_rel': float(abs(L.vol.sum() / g.Vc - 1))}
    op, diag, info = dec_operator()
    lm = 0.3589683417646019
    kv = (0.01 / lm) * np.array([1.0, 0.0, 0.0])
    om = op(kv)
    out['dec_probe'] = {'w2k2_lo': float(om[0] ** 2 / np.dot(kv, kv)), 'info': info}
    return out


def modus_dec(lm):
    op, diag, info = dec_operator()
    pts = []
    for p in raster_pts(lm):
        ks = p['ks']
        om = op(ks)
        e2 = float(np.dot(ks, ks))
        pts.append({'ridx': p['ridx'], 'richtung': p['richtung'], 'kl': p['kl'],
                    'w2k2': sorted([float(om[0] ** 2 / e2), float(om[1] ** 2 / e2)])})
    return {'punkte': pts, 'diagnose': diag, 'info': info}


def modus_w4d(lm, teil, hset="fein"):
    hs, nf = EXTRA[hset]
    L4 = [Licht4(h) for h in hs]
    for L in L4:
        L.hset = (hs, nf)
    pts = raster_pts(lm)
    if teil is not None:
        pts = pts[teil::2]
    out = []
    for p in pts:
        r = w4d_punkt(L4, p['ks'])
        r.update({'ridx': p['ridx'], 'richtung': p['richtung'], 'kl': p['kl']})
        out.append(r)
    return {'punkte': out, 'h': hs, 'n_fit': nf, 'hset': hset}


def fit(kls, ws, masse=False):
    """y = omega^2/k^2 gegen x = (kl)^2: y = w0 + w2 x + w4 x^2 (ohne Masse) bzw. y = mu/x + w0 + w2 x + w4 x^2
    (mit Massenterm mu = m^2 l^2, faengt eine Scheinmasse aus Extrapolation oder Rundung ab)."""
    x = np.asarray(kls, float) ** 2
    cols = [np.ones_like(x), x, x ** 2]
    if masse:
        cols = [1.0 / x] + cols
    Am = np.stack(cols, 1)
    cf, *_ = np.linalg.lstsq(Am, np.asarray(ws, float), rcond=None)
    if masse:
        return {'w0': float(cf[1]), 'w2': float(cf[2]), 'mu': float(cf[0])}
    return {'w0': float(cf[0]), 'w2': float(cf[1]), 'mu': 0.0}


def tabelle(W, masse=False):
    """je Richtung und Zweig: w0, c = sqrt(w0), b = w2/(2 w0) (relative Tempoaenderung je (kl)^2), mu."""
    out = {}
    for i in range(13):
        zw = []
        for b in range(2):
            f = fit(uv.KL_FIT, [W[(i, kl)][b] for kl in uv.KL_FIT], masse)
            zw.append({'w0': f['w0'], 'c': float(np.sqrt(f['w0'])) if f['w0'] > 0 else None,
                       'b': f['w2'] / (2 * f['w0']), 'mu': f['mu']})
        out[i] = zw
    return out


def zusammen(T):
    c = np.array([T[i][b]['c'] for i in range(13) for b in range(2)])
    bb = np.array([T[i][b]['b'] for i in range(13) for b in range(2)])
    mu = np.array([T[i][b]['mu'] for i in range(13) for b in range(2)])
    dop = [abs(T[i][1]['b'] - T[i][0]['b']) for i in range(13)]
    return {'c_min': float(c.min()), 'c_max': float(c.max()), 'c_spanne': float(c.max() / c.min() - 1),
            'b_min': float(bb.min()), 'b_max': float(bb.max()), 'b_mittel': float(bb.mean()),
            'doppelbrechung_b_max': float(max(dop)), 'mu_min': float(mu.min()), 'mu_max': float(mu.max())}


def modus_aw(pf):
    import tti
    R = dict((i, nm) for i, (nm, d) in enumerate(tti.richtungen13()))
    gw = json.load(open(pf['gw']))['ergebnis']['punkte']
    dec = json.load(open(pf['dec']))['ergebnis']['punkte']
    W = {'gw': {(p['ridx'], p['kl']): p['a_tol1e-10']['w2k2'] for p in gw if p.get('definiert')},
         'dec': {(p['ridx'], p['kl']): p['w2k2'] for p in dec}}
    ok = {'gw': all(p.get('definiert') and p['a_tol1e-10'].get('ok') for p in gw)}
    diag = {}
    for nm, (fa, fb) in (('w4f', ('w4a', 'w4b')), ('w4g', ('g4a', 'g4b'))):
        if fa not in pf:
            continue
        w4 = json.load(open(pf[fa]))['ergebnis']['punkte'] + json.load(open(pf[fb]))['ergebnis']['punkte']
        W[nm] = {(p['ridx'], p['kl']): p['w2k2'] for p in w4 if p.get('definiert')}
        ok[nm] = all(p.get('definiert') and p.get('ok') for p in w4)
        d = [p for p in w4 if p.get('definiert')]
        diag[nm] = {'e_K_max': float(max(p['e_K'] for p in d)), 'aend_K_max': float(max(p['aend_K'] for p in d)),
                    'ungerade_rel_max': float(max(p['ungerade_rel'] for p in d)),
                    'K_n_neg_max': int(max(p['K_n_neg'] for p in d)), 'n_wachsend_max': int(max(p['n_wachsend'] for p in d)),
                    'luecke_max': float(max(p['luecke'] for p in d)), 'L_kond_max': float(max(p['L_kond_max'] for p in d)),
                    'definiert': len(d), 'anzahl': len(w4)}
    out = {'ok': ok, 'diag_w4d': diag, 'richtungen': [R[i] for i in range(13)]}
    for masse in (False, True):
        T = {nm: tabelle(Wn, masse) for nm, Wn in W.items()}
        key = 'mit_masse' if masse else 'ohne_masse'
        res = {'zusammen': {nm: zusammen(Tn) for nm, Tn in T.items()}, 'zeilen': []}
        for i in range(13):
            cg = 0.5 * (T['gw'][i][0]['c'] + T['gw'][i][1]['c'])
            z = {'richtung': R[i], 'c_gw': [T['gw'][i][b]['c'] for b in range(2)], 'b_gw': [T['gw'][i][b]['b'] for b in range(2)]}
            for nm in T:
                if nm == 'gw':
                    continue
                z['c_' + nm] = [T[nm][i][b]['c'] for b in range(2)]
                z['b_' + nm] = [T[nm][i][b]['b'] for b in range(2)]
                z['verh_' + nm] = [T[nm][i][b]['c'] / cg for b in range(2)]
            res['zeilen'].append(z)
        for nm in T:
            if nm == 'gw':
                continue
            v = np.array([x for z in res['zeilen'] for x in z['verh_' + nm]])
            res['zusammen']['verh_' + nm] = [float(v.min()), float(v.max())]
            res['zusammen']['b_mittel_diff_' + nm] = res['zusammen'][nm]['b_mittel'] - res['zusammen']['gw']['b_mittel']
            # Tempounterschied je Richtung bei gleichem kl: Mittel der Zweige
            dd = [0.5 * (z['b_' + nm][0] + z['b_' + nm][1]) - 0.5 * (z['b_gw'][0] + z['b_gw'][1]) for z in res['zeilen']]
            res['zusammen']['b_diff_je_richtung_' + nm] = [float(min(dd)), float(max(dd))]
        out[key] = res
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['kontrolle', 'dec', 'w4d', 'aw'])
    ap.add_argument('--teil', type=int, default=None)
    ap.add_argument('--hset', default='fein', choices=['fein', 'grob'])
    ap.add_argument('--ein', nargs='*', default=[])
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    lm = 0.3589683417646019            # mittlere Kantenlaenge von V (tg), wie uv.py / nachtrag2_uv.py
    if a.modus == 'kontrolle':
        erg = modus_kontrolle()
    elif a.modus == 'dec':
        erg = modus_dec(lm)
    elif a.modus == 'w4d':
        erg = modus_w4d(lm, a.teil, a.hset)
    else:
        erg = modus_aw(dict(x.split('=', 1) for x in a.ein))
    res = {'info': {'argv': sys.argv, 'python': platform.python_version(), 'numpy': np.__version__,
                    'skript_sha256': uv.sha(os.path.abspath(__file__)),
                    'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(t0))},
           'ergebnis': erg, 'laufzeit_s': time.time() - t0}
    tg.schreibe(a.out, res)
    print('fertig licht', a.modus, 'laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
