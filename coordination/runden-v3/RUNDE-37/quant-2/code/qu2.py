#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QUANT-2 (fmhc-physics, Runde 50), Code-Agent fuer die Leitung claude-primary (Finn: "quantisier mal los").

Kompakte U(1)-Eichtheorie mit Wilson-Wirkung S = Summe_f beta w_f (1 - cos theta_f), euklidisch, Monte Carlo:
von-Mises-Waermebad (fuer U(1) exakt: die lokale Verteilung eines Links ist exp(kappa cos(theta - mu))) plus
Ueberrelaxation theta -> 2 mu - theta. Links derselben Farbe teilen keine Plakette und werden gemeinsam erneuert.
Gitter:
  kubisch : hyperkubisch L^3 x Nt, Plaketten = Quadrate, w = 1 (Kontrolle, beta_c ~ 1,01 [L])
  netz    : Finns 4D-Zeltnetz V mal Zeit (REGIME-K-2: Netz V, Hubfolge A, Hoehen b/10 mal tau, Zeltstange tau),
            Links = Kanten, Plaketten = Dreiecke; Gewicht w_f = |*f| / |f| (umkreismittiger DEC-Hodge-Stern des
            4D-Netzes, vorzeichenbehaftet) oder w = 1 ('eins')
Normierung: fuer kleine Felder S -> (beta/2) Summe_f w_f theta_f^2; fuer konstantes F ist theta_f = F . S_f
(S_f Flaechen-Bivektor), und Summe_f w_f S_f S_f^T = Vol I_6 (gerechnet in 'netz') gibt (beta/2) Int |F|^2, also
dieselbe Bedeutung von beta (= 1/e^2) wie auf dem kubischen Gitter (dort w = 1).
Modi: netz | scan | auswertung
Importiert unveraendert: rk.py, rk2.py, ew.py, tp.py, pt.py (Kopien aus RUNDE-37/ueberleitung-v-1/code).
"""
import argparse, json, os, sys, time, hashlib, platform, itertools
import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
IU = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def kopf():
    return {'python': platform.python_version(), 'numpy': np.__version__, 'host': platform.node(),
            'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'argv': sys.argv,
            'skript_sha256': sha(os.path.abspath(__file__))}


def wrap(x):
    return np.remainder(x + np.pi, 2.0 * np.pi) - np.pi


# ================================================================================================ Netz (Vorlage)
def netz_gitter(tau):
    import rk, rk2, tp
    xb, tets, arten = rk2.netz_raum('V')
    NV = len(xb)
    rang = {b: b for b in range(NV)}                      # Hubfolge A wie rk2.baue2('V-A')
    hb = [b / float(NV) for b in range(NV)]
    g = rk.Gitter('V-A', xb, hb, tp.AV.T, tets, rk2.ord_rang(rang), tau)
    return g


def umkreis(P):
    P = np.asarray(P, float)
    E = P[1:] - P[0]
    G = E @ E.T
    a = np.linalg.solve(2.0 * G, np.diag(G).copy())
    return P[0] + E.T @ a


def bivektor(P):
    a = P[1] - P[0]
    b = P[2] - P[1] + a
    w = 0.5 * (np.outer(a, b) - np.outer(b, a))
    return np.array([w[m, n] for (m, n) in IU])


def hodge2(g):
    """Umkreismittiger Hodge-Stern auf Dreiecken des 4D-Netzes: |*f| = Summe ueber Fahnen f < tau < sigma der
    vorzeichenbehafteten Flaechen (c_f, c_tau, c_sigma) (rechter Winkel bei c_tau; Vorzeichen nach Hirani)."""
    import rk, pt
    dual, rep, nsig = {}, {}, {}
    for s, Sv in enumerate(g.simp):
        X = g.Xs[s]
        cs = umkreis(X)
        for k, tri in enumerate(pt.DREI5):
            key = rk.kanon_menge([Sv[x] for x in tri])
            if key not in rep:
                rep[key] = key
            cf = umkreis(X[list(tri)])
            rest = list(pt.PAARE5[k])
            for l in rest:
                m = rest[1] if l == rest[0] else rest[0]
                ct = umkreis(X[list(tri) + [l]])
                d1 = ct - cf
                d2 = cs - ct
                s1 = np.sign(d1 @ (X[l] - cf))
                s2 = np.sign(d2 @ (X[m] - ct))
                dual[key] = dual.get(key, 0.0) + 0.5 * s1 * np.linalg.norm(d1) * s2 * np.linalg.norm(d2)
            nsig[key] = nsig.get(key, 0) + 1
    keys = sorted(dual)
    area, S, w, P3 = [], [], [], []
    for key in keys:
        P = np.array([g.pos(b, d) for (b, d) in key])
        Sb = bivektor(P)
        A = float(np.linalg.norm(Sb))
        area.append(A); S.append(Sb); w.append(dual[key] / A); P3.append(P)
    return {'keys': keys, 'area': np.array(area), 'S': np.array(S), 'w': np.array(w), 'P': np.array(P3),
            'dual': np.array([dual[k] for k in keys]), 'nsig': np.array([nsig[k] for k in keys])}


def bloch_d1(g, keys, k4):
    import rk
    eid = {key: i for i, key in enumerate(g.ekeys)}
    D = np.zeros((len(keys), g.NE), complex)
    for f, key in enumerate(keys):
        vs = list(key)
        for a, b in ((0, 1), (1, 2), (2, 0)):
            ek, T = rk.kanon_kante(vs[a], vs[b])
            sg = 1.0 if (ek[0] == vs[a][0] and tuple(T) == tuple(int(x) for x in vs[a][1])) else -1.0
            D[f, eid[ek]] += sg * np.exp(1j * (k4 @ (g.A @ np.array(T, float))))
    return D


def lauf_netz(a):
    out = {'kopf': kopf(), 'tau': []}
    rng = np.random.default_rng(20261005)
    for tau in a.taus:
        t0 = time.time()
        g = netz_gitter(tau)
        h = hodge2(g)
        w, S = h['w'], h['S']
        M = np.einsum('f,fa,fb->ab', w, S, S)
        Vc = g.Vc
        vol = np.abs(np.linalg.det(g.Xs[:, 1:, :] - g.Xs[:, :1, :])) / 24.0
        # Bloch-Probe der Gauss-Form K(k) = d1^+ W d1 (Eichnullmoden NV erwartet)
        ev_min, nneg, n0 = [], [], []
        for _ in range(a.nk):
            k4 = rng.uniform(-np.pi, np.pi, 4) * np.array([8.0, 8.0, 8.0, 1.0 / tau])
            D = bloch_d1(g, h['keys'], k4)
            K = np.conj(D.T) @ (w[:, None] * D)
            ev = np.linalg.eigvalsh(0.5 * (K + np.conj(K.T)))
            sc = np.abs(ev).max()
            n0.append(int((np.abs(ev) <= 1e-10 * sc).sum()))
            nneg.append(int((ev < -1e-10 * sc).sum()))
            ev_min.append(float(ev.min() / sc))
        # Zeitartige / raeumliche Dreiecke (Zeitindex gleich -> 'Scheibe')
        tsl = np.array([len(set(d[3] for (_, d) in key)) == 1 for key in h['keys']])
        e = {'tau': tau, 'NV': g.NV, 'NE': g.NE, 'S': g.S, 'NF': len(h['keys']), 'Vc': Vc,
             'vol_summe_rel': float(vol.sum() / Vc - 1.0),
             'identitaet_rel': float(np.abs(M - Vc * np.eye(6)).max() / Vc),
             'M_diag': [float(x) for x in np.diag(M) / Vc],
             'w_min': float(w.min()), 'w_max': float(w.max()), 'w_mittel': float(w.mean()),
             'n_negativ': int((w < 0).sum()), 'n_null': int((np.abs(w) < 1e-12).sum()),
             'anteil_neg_an_sum_abs': float(np.abs(w[w < 0]).sum() / np.abs(w).sum()),
             'w_scheibe_mittel': float(w[tsl].mean()), 'w_zeit_mittel': float(w[~tsl].mean()),
             'n_scheibe': int(tsl.sum()),
             'kanten_l': [float(x) for x in np.percentile(g.l, [0, 50, 100])],
             'bloch_nk': a.nk, 'bloch_null_min_max': [min(n0), max(n0)], 'bloch_neg_max': max(nneg),
             'bloch_evmin_rel_min': min(ev_min), 'zeit_s': time.time() - t0}
        # Histogramm der Gewichte
        e['w_quantile'] = [float(x) for x in np.percentile(w, [1, 5, 25, 50, 75, 95, 99])]
        out['tau'].append(e)
        print(json.dumps(e), flush=True)
    with open(a.out, 'w') as f:
        json.dump(out, f, indent=1)


# ================================================================================================ Komplexe
class Komplex:
    pass


def kubisch(L, Nt):
    K = Komplex()
    dims = np.array([L, L, L, Nt])
    co = np.array(list(itertools.product(range(L), range(L), range(L), range(Nt))))
    nV = len(co)

    def vid(c):
        c = np.mod(c, dims)
        return ((c[..., 0] * L + c[..., 1]) * L + c[..., 2]) * Nt + c[..., 3]

    def lid(c, mu):
        return vid(c) * 4 + mu
    E4 = np.eye(4, dtype=int)
    Pe, Ps, ft, fN, fx = [], [], [], [], []
    for mu, nu in IU:
        Pe.append(np.stack([lid(co, mu), lid(co + E4[mu], nu), lid(co + E4[nu], mu), lid(co, nu)], 1))
        Ps.append(np.tile([1, 1, -1, -1], (nV, 1)))
        if nu < 3:
            ft.append(co[:, 3].copy())
            N = np.cross(np.eye(3)[mu], np.eye(3)[nu])
            fN.append(np.tile(N, (nV, 1)).astype(float))
        else:
            ft.append(-np.ones(nV, int))
            fN.append(np.zeros((nV, 3)))
        fx.append(co[:, :3] + 0.5 * (E4[mu][:3] + E4[nu][:3]))
    K.Pe = np.concatenate(Pe); K.Ps = np.concatenate(Ps).astype(float)
    K.fl_t = np.concatenate(ft); K.fl_N = np.concatenate(fN); K.fl_x = np.concatenate(fx).astype(float)
    K.nE = 4 * nV; K.nV = nV; K.w = np.ones(len(K.Pe))
    sp = np.array(list(itertools.product(range(L), range(L), range(L))))
    K.rpos = sp.astype(float)
    K.rsub = np.zeros(len(sp), int)
    K.poly_e = np.stack([lid(np.c_[sp, np.full(len(sp), t)], 3) for t in range(Nt)], 1)
    K.poly_s = np.ones_like(K.poly_e, dtype=float)
    K.box = L * np.eye(3)
    K.tau = 1.0; K.Nt = Nt; K.L = L
    ks = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1), (1, 1, 1)]
    K.kvek = np.array(ks, float) * 2 * np.pi / L
    K.kname = ['100a', '100b', '100c', '110a', '110b', '110c', '111a']
    K.zeitkante = np.zeros(K.nE, bool); K.zeitkante[3::4] = True
    return K


def netz(L, Nt, tau, gew):
    import tp
    g = netz_gitter(tau)
    h = hodge2(g)
    if gew.startswith('datei:'):
        dat = np.load(gew[6:])
        if abs(float(dat['tau']) - tau) > 1e-9 or len(dat['w']) != len(h['keys']):
            raise RuntimeError('Gewichtsdatei passt nicht')
        wcls = np.asarray(dat['w'], float)
    elif gew == 'dec':
        wcls = h['w']
    else:
        wcls = np.ones(len(h['keys']))
    NV = g.NV
    K = Komplex()
    dims = np.array([L, L, L, Nt])
    cells = np.array(list(itertools.product(range(L), range(L), range(L), range(Nt))))
    nc = len(cells)
    nV = NV * nc

    def vid(b, n):
        m = np.mod(n, dims)
        return (((m[..., 3] * L + m[..., 0]) * L + m[..., 1]) * L + m[..., 2]) * NV + b
    E1, E2 = [], []
    for (b1, b2, d) in g.ekeys:
        E1.append(vid(np.full(nc, b1), cells)); E2.append(vid(np.full(nc, b2), cells + np.array(d)))
    E1 = np.concatenate(E1); E2 = np.concatenate(E2)
    lo, hi = np.minimum(E1, E2), np.maximum(E1, E2)
    code = lo.astype(np.int64) * nV + hi
    uc = np.unique(code)
    if len(uc) != len(code) or (lo == hi).any():
        raise RuntimeError('Kantenkollision bei L=%d, Nt=%d' % (L, Nt))
    TV, TP, TT, WW = [], [], [], []
    cphys = cells @ g.A.T
    for f, key in enumerate(h['keys']):
        TV.append(np.stack([vid(np.full(nc, b), cells + np.array(d)) for (b, d) in key], 1))
        TP.append(np.stack([g.pos(b, d)[None, :] + cphys for (b, d) in key], 1))
        dts = [d[3] for (_, d) in key]
        TT.append((cells[:, 3] + dts[0]) % Nt if len(set(dts)) == 1 else -np.ones(nc, int))
        WW.append(np.full(nc, wcls[f]))
    TV = np.concatenate(TV); TP = np.concatenate(TP); TT = np.concatenate(TT); WW = np.concatenate(WW)
    o = np.argsort(TV, axis=1)
    TV = np.take_along_axis(TV, o, 1)
    TP = np.take_along_axis(TP, o[:, :, None], 1)
    tc = (TV[:, 0].astype(np.int64) * nV + TV[:, 1]) * nV + TV[:, 2]
    if len(np.unique(tc)) != len(tc) or (TV[:, 0] == TV[:, 1]).any() or (TV[:, 1] == TV[:, 2]).any():
        raise RuntimeError('Dreieckskollision')

    def eidx(i, j):
        c = i.astype(np.int64) * nV + j
        p = np.searchsorted(uc, c)
        assert (uc[p] == c).all()
        return p
    K.Pe = np.stack([eidx(TV[:, 0], TV[:, 1]), eidx(TV[:, 1], TV[:, 2]), eidx(TV[:, 0], TV[:, 2])], 1)
    K.Ps = np.tile(np.array([1.0, 1.0, -1.0]), (len(TV), 1))
    K.w = WW
    K.fl_t = TT
    X3 = TP[:, :, :3]
    K.fl_N = 0.5 * np.cross(X3[:, 1] - X3[:, 0], X3[:, 2] - X3[:, 0])
    K.fl_x = X3.mean(1)
    K.nE = len(uc); K.nV = nV
    # Zeitlinien (Zeltstangen) je Raumecke
    sp = np.array(list(itertools.product(range(L), range(L), range(L))))
    rs, rb, pe, ps = [], [], [], []
    AV = tp.AV
    for n in sp:
        for b in range(NV):
            rs.append(g.xb[b] + n @ AV); rb.append(b)
            e_row, s_row = [], []
            for t in range(Nt):
                v0 = vid(np.array(b), np.r_[n, t]); v1 = vid(np.array(b), np.r_[n, t + 1])
                e_row.append(eidx(np.array([min(v0, v1)]), np.array([max(v0, v1)]))[0])
                s_row.append(1.0 if v0 < v1 else -1.0)
            pe.append(e_row); ps.append(s_row)
    K.rpos = np.array(rs); K.rsub = np.array(rb); K.poly_e = np.array(pe); K.poly_s = np.array(ps)
    K.box = L * AV
    K.tau = tau; K.Nt = Nt; K.L = L
    BV = 2 * np.pi * np.linalg.inv(K.box).T
    b1, b2, b3 = BV
    K.kvek = np.array([b1, b2, b3, b1 + b2 + b3, b1 + b2, b1 + b3, b2 + b3])
    K.kname = ['111a', '111b', '111c', '111d', '100a', '100b', '100c']
    zk = np.zeros(K.nE, bool)
    zk[np.unique(K.poly_e)] = True
    K.zeitkante = zk
    K.hodge = {'identitaet': None}
    return K


def faerben(nE, Pe):
    m = Pe.shape[1]
    a = np.repeat(Pe, m, axis=1).ravel()
    b = np.tile(Pe, (1, m)).ravel()
    sel = a != b
    a, b = a[sel], b[sel]
    o = np.argsort(a, kind='stable')
    a, b = a[o], b[o]
    st = np.searchsorted(a, np.arange(nE + 1))
    farbe = -np.ones(nE, int)
    for e in range(nE):
        nb = farbe[b[st[e]:st[e + 1]]]
        used = set(nb[nb >= 0].tolist())
        c = 0
        while c in used:
            c += 1
        farbe[e] = c
    return farbe


def vorbereiten(K):
    m = K.Pe.shape[1]
    srt = np.sort(K.Pe, axis=1)
    if (srt[:, 1:] == srt[:, :-1]).any():
        raise RuntimeError('Plakette mit doppeltem Link')
    K.farbe = faerben(K.nE, K.Pe)
    nf = len(K.Pe)
    inc_f = np.repeat(np.arange(nf), m); inc_e = K.Pe.ravel(); inc_s = K.Ps.ravel()
    K.kl = []
    for c in range(K.farbe.max() + 1):
        sel = K.farbe[inc_e] == c
        f, e, s = inc_f[sel], inc_e[sel], inc_s[sel]
        ed = np.unique(e)
        loc = np.searchsorted(ed, e)
        K.kl.append((K.Pe[f], K.Ps[f], e, s, K.w[f], loc, ed))
    # Multihit fuer Zeitlinien: erlaubt, wenn keine Plakette zwei Zeitlinien-Links enthaelt (dann sind alle
    # Zeitlinien-Links bei festem Rest bedingt unabhaengig, <e^{i theta}> = I1/I0(kappa) e^{i mu} exakt)
    zk = np.unique(K.poly_e)
    is_z = np.zeros(K.nE, bool); is_z[zk] = True
    K.mh_max_je_plakette = int(is_z[K.Pe].sum(1).max())
    if K.mh_max_je_plakette <= 1:
        sel = is_z[inc_e]
        f, e, s = inc_f[sel], inc_e[sel], inc_s[sel]
        K.mh = (K.Pe[f], K.Ps[f], e, s, K.w[f], np.searchsorted(zk, e), zk)
        K.mh_pos = np.searchsorted(zk, K.poly_e)
    else:
        K.mh = None
    # Abstandsklassen der Polyakov-Paare (Mindestbild), Klassen (b, b', r)
    R = K.rpos
    Binv = np.linalg.inv(K.box)
    iu, ju = np.triu_indices(len(R), 1)
    d = R[ju] - R[iu]
    fr = d @ Binv
    fr = fr - np.round(fr)
    best = None
    for sh in itertools.product((-1, 0, 1), repeat=3):
        x = (fr + np.array(sh)) @ K.box
        nr = np.linalg.norm(x, axis=1)
        best = nr if best is None else np.minimum(best, nr)
    sb = np.minimum(K.rsub[iu], K.rsub[ju]); tb = np.maximum(K.rsub[iu], K.rsub[ju])
    rr = np.round(best, 6)
    keys = np.stack([sb, tb, np.round(rr * 1e6).astype(np.int64)], 1)
    uk, lab = np.unique(keys, axis=0, return_inverse=True)
    K.p_i, K.p_j, K.p_lab = iu, ju, lab.ravel()
    K.p_klassen = uk
    K.p_r = uk[:, 2] / 1e6
    K.p_n = np.bincount(K.p_lab, minlength=len(uk))
    # Photon-Operatoren: raeumliche Plaketten, zwei Polarisationen je k
    sp = K.fl_t >= 0
    K.ph_f = np.where(sp)[0]
    K.ph_t = K.fl_t[sp]
    co = []
    for kv in K.kvek:
        kh = kv / np.linalg.norm(kv)
        hilf = np.array([1.0, 0.0, 0.0]) if abs(kh[0]) < 0.9 else np.array([0.0, 1.0, 0.0])
        e1 = np.cross(kh, hilf); e1 /= np.linalg.norm(e1)
        e2 = np.cross(kh, e1)
        ph = np.exp(1j * (K.fl_x[sp] @ kv))
        co.append([(K.fl_N[sp] @ e1) * ph, (K.fl_N[sp] @ e2) * ph])
    K.ph_co = co
    return K


# ================================================================================================ Monte Carlo
def sweep(K, th, beta, rng, art):
    for (Pf, Sf, e, s, wf, loc, ed) in K.kl:
        tf = (Sf * th[Pf]).sum(1)
        ph = s * tf - th[e]
        wb = beta * wf
        re = np.bincount(loc, wb * np.cos(ph), minlength=len(ed))
        im = np.bincount(loc, wb * np.sin(ph), minlength=len(ed))
        mu = -np.arctan2(im, re)
        if art == 'hb':
            th[ed] = rng.vonmises(mu, np.hypot(re, im))
        else:
            th[ed] = wrap(2.0 * mu - th[ed])


def plaketten(K, th):
    return (K.Ps * th[K.Pe]).sum(1)


def messen(K, th, beta):
    tf = plaketten(K, th)
    c = np.cos(tf)
    pw = float((K.w * c).sum() / K.w.sum())
    pu = float(c.mean())
    pl = (K.poly_s * th[K.poly_e]).sum(1)
    z = np.exp(1j * pl)
    pab = float(abs(z.mean()))
    cc = (z[K.p_i] * np.conj(z[K.p_j])).real
    kor = np.bincount(K.p_lab, cc, minlength=len(K.p_r)) / K.p_n
    if K.mh is not None:
        from scipy import special
        Pf, Sf, e, s, wf, loc, ed = K.mh
        ph = s * (Sf * th[Pf]).sum(1) - th[e]
        re = np.bincount(loc, wf * np.cos(ph), minlength=len(ed))
        im = np.bincount(loc, wf * np.sin(ph), minlength=len(ed))
        kap = beta * np.hypot(re, im)
        u = (special.i1e(kap) / special.i0e(kap)) * np.exp(-1j * np.arctan2(im, re))
        uu = u[K.mh_pos]
        uu = np.where(K.poly_s > 0, uu, np.conj(uu))
        zm = np.prod(uu, axis=1)
        korm = np.bincount(K.p_lab, (zm[K.p_i] * np.conj(zm[K.p_j])).real, minlength=len(K.p_r)) / K.p_n
        pabm = float(abs(zm.mean()))
    else:
        korm, pabm = kor, pab
    sn = np.sin(tf[K.ph_f])
    Nt = K.Nt
    phc = np.zeros((len(K.kvek), Nt))
    for ik, (c1, c2) in enumerate(K.ph_co):
        for co in (c1, c2):
            O = (np.bincount(K.ph_t, (co * sn).real, minlength=Nt)
                 + 1j * np.bincount(K.ph_t, (co * sn).imag, minlength=Nt))
            for dt in range(Nt):
                phc[ik, dt] += 0.5 * float((O * np.conj(np.roll(O, -dt))).real.mean())
    return pw, pu, pab, kor, phc, korm, pabm


def lauf_scan(a):
    t_start = time.time()
    rng = np.random.default_rng(a.seed)
    if a.gitter == 'kubisch':
        K = kubisch(a.L, a.Nt)
    else:
        K = netz(a.L, a.Nt, a.tau, a.gew)
    vorbereiten(K)
    t_bau = time.time() - t_start
    if a.start == 'kalt':
        th = np.zeros(K.nE)
    elif a.start == 'heiss':
        th = rng.uniform(-np.pi, np.pi, K.nE)
    else:
        th = np.load(a.start)
        assert th.shape == (K.nE,)
    betas = [float(x) for x in a.betas]
    res = {'kopf': kopf(), 'gitter': a.gitter, 'L': a.L, 'Nt': a.Nt, 'tau': K.tau, 'gew': a.gew,
           'nE': int(K.nE), 'nF': int(len(K.Pe)), 'nV': int(K.nV), 'farben': int(K.farbe.max() + 1),
           'w_summe': float(K.w.sum()), 'n_neg_w': int((K.w < 0).sum()), 'start': a.start, 'nor': a.nor,
           'ntherm': a.ntherm, 'nmess': a.nmess, 'mabst': a.mabst, 'nbin': a.nbin, 'zeit_bau_s': t_bau, 'betas': [], 'abbruch': None,
           'p_r': K.p_r.tolist(), 'p_klassen': K.p_klassen.tolist(), 'p_n': K.p_n.tolist(),
           'kname': K.kname, 'kvek': K.kvek.tolist(), 'n_scheibe_plak': int(len(K.ph_f)), 'multihit': K.mh is not None, 'mh_max_je_plakette': K.mh_max_je_plakette}
    arr = {}
    for ib, beta in enumerate(betas):
        t0 = time.time()
        for _ in range(a.ntherm):
            sweep(K, th, beta, rng, 'hb')
            for _ in range(a.nor):
                sweep(K, th, beta, rng, 'or')
        B = a.nmess // a.nbin
        pw_s, pu_s, pa_s = [], [], []
        kor_b = np.zeros((a.nbin, len(K.p_r))); ph_b = np.zeros((a.nbin, len(K.kvek), K.Nt)); korm_b = np.zeros_like(kor_b); pam_s = []
        nb_eff = a.nbin
        for im in range(a.nbin * B):
            if im > 0 and im % B == 0 and time.time() - t_start > a.zeitlimit:
                nb_eff = im // B
                break
            for _ in range(a.mabst):
                sweep(K, th, beta, rng, 'hb')
                for _ in range(a.nor):
                    sweep(K, th, beta, rng, 'or')
            pw, pu, pab, kor, phc, korm, pabm = messen(K, th, beta)
            pw_s.append(pw); pu_s.append(pu); pa_s.append(pab); pam_s.append(pabm)
            kor_b[im // B] += kor / B; korm_b[im // B] += korm / B
            ph_b[im // B] += phc / B
        kor_b = kor_b[:nb_eff]; ph_b = ph_b[:nb_eff]; korm_b = korm_b[:nb_eff]
        arr['pw_%d' % ib] = np.array(pw_s); arr['pu_%d' % ib] = np.array(pu_s); arr['pa_%d' % ib] = np.array(pa_s)
        arr['kor_%d' % ib] = kor_b; arr['ph_%d' % ib] = ph_b; arr['korm_%d' % ib] = korm_b; arr['pam_%d' % ib] = np.array(pam_s)
        pw_s = np.array(pw_s)
        bm = pw_s.reshape(nb_eff, B).mean(1)
        e = {'beta': beta, 'pw': float(pw_s.mean()), 'pw_err': float(bm.std(ddof=1) / np.sqrt(nb_eff)),
             'pu': float(np.mean(pu_s)), 'chi': float(len(K.Pe) * pw_s.var()), 'pabs': float(np.mean(pa_s)),
             'zeit_s': time.time() - t0, 'nbin': nb_eff, 'pabs_mh': float(np.mean(pam_s))}
        res['betas'].append(e)
        print(json.dumps(e), flush=True)
        if nb_eff < a.nbin:
            res['abbruch'] = 'Zeitlimit in beta-Index %d nach %d von %d Bins' % (ib, nb_eff, a.nbin)
            break
        if time.time() - t_start > a.zeitlimit and ib < len(betas) - 1:
            res['abbruch'] = 'Zeitlimit nach beta-Index %d' % ib
            break
    np.save(a.out + '.ende.npy', th)
    np.savez_compressed(a.out + '.npz', **arr)
    res['zeit_gesamt_s'] = time.time() - t_start
    with open(a.out + '.json', 'w') as f:
        json.dump(res, f, indent=1)


# ================================================================================================ Auswertung
def jk(bins, fun):
    n = len(bins)
    full = fun(bins.mean(0))
    js = np.array([fun(np.delete(bins, i, 0).mean(0)) for i in range(n)])
    err = np.sqrt((n - 1) / n * ((js - js.mean(0)) ** 2).sum(0))
    return full, err, js


def nn1(x):
    x = float(x)
    return None if not np.isfinite(x) else x


def nn(A):
    return [[nn1(v) for v in row] for row in np.asarray(A, float)]


def eeff_arr(C, Nt):
    """Effektive Energie (Gittereinheiten der Zeit) aus C(t)/C(t+1) mit cosh-Form, je k; nan wenn nicht definiert."""
    nk = C.shape[0]
    out = np.full((nk, Nt // 2), np.nan)
    for t in range(Nt // 2):
        a, b = C[:, t], C[:, t + 1]
        ok = (a > 0) & (b > 0) & (a > b)
        q = np.where(ok, a / np.where(b > 0, b, 1.0), 2.0)
        lo = np.full(nk, 1e-9); hi = np.full(nk, 30.0)
        for _ in range(80):
            mid = 0.5 * (lo + hi)
            f = np.cosh(mid * (Nt / 2 - t)) / np.cosh(mid * (Nt / 2 - t - 1))
            lo = np.where(f < q, mid, lo); hi = np.where(f < q, hi, mid)
        out[:, t] = np.where(ok, 0.5 * (lo + hi), np.nan)
    return out


def chi_jk(pw, nF, nbin):
    B = len(pw) // nbin
    x = pw[:nbin * B].reshape(nbin, B)
    m1 = x.mean(1); m2 = (x ** 2).mean(1)
    st = np.stack([m1, m2], 1)
    f = lambda v: nF * (v[1] - v[0] ** 2)
    c, ce, _ = jk(st, f)
    return float(c), float(ce)


def fit_V(r, sub, y, ey, nsub, form, c_fest=None):
    """y = u_b + u_b' + sigma r - c/r (form 'sc'), oder ohne sigma ('c'), oder c fest; linear, gewichtet."""
    cols = []
    for b in range(nsub):
        cols.append((sub[:, 0] == b).astype(float) + (sub[:, 1] == b).astype(float))
    names = ['u%d' % b for b in range(nsub)]
    rhs = y.copy()
    if form in ('sc', 's_cfest'):
        cols.append(r); names.append('sigma')
    if form in ('sc', 'c'):
        cols.append(-1.0 / r); names.append('c')
    if form == 's_cfest':
        rhs = rhs + c_fest / r
    X = np.stack(cols, 1)
    Wt = 1.0 / ey
    p, *_ = np.linalg.lstsq(X * Wt[:, None], rhs * Wt, rcond=None)
    chi2 = float((((X @ p - rhs) * Wt) ** 2).sum())
    return dict(zip(names, p.tolist())), chi2, len(y) - len(p)


def lauf_auswertung(a):
    out = {'kopf': kopf(), 'dateien': []}
    for pfad in a.ein:
        with open(pfad + '.json') as f:
            res = json.load(f)
        z = np.load(pfad + '.npz')
        nF = res['nF']; nbin = res['nbin']; Nt = res['Nt']; tau = res['tau']
        T = Nt * tau
        r = np.array(res['p_r']); kl = np.array(res['p_klassen']); pn = np.array(res['p_n'])
        nsub = int(kl[:, :2].max()) + 1
        d = {'datei': os.path.basename(pfad), 'gitter': res['gitter'], 'L': res['L'], 'Nt': Nt, 'tau': tau,
             'gew': res['gew'], 'start': res['start'], 'betas': []}
        for ib, eb in enumerate(res['betas']):
            pw = z['pw_%d' % ib]
            c, ce = chi_jk(pw, nF, eb.get('nbin', nbin))
            e = {'beta': eb['beta'], 'pw': eb['pw'], 'pw_err': eb['pw_err'], 'chi': c, 'chi_err': ce,
                 'pabs': eb['pabs'], 'pu': eb['pu'], 'pabs_mh': eb.get('pabs_mh')}
            # Polyakov-Korrelator -> V(r) mit Untergitter-Offsets (plain und Multihit)
            e['poly'] = {}
            for var, schl in (('plain', 'kor_%d'), ('mh', 'korm_%d')):
                if (schl % ib) not in z.files:
                    continue
                kb = z[schl % ib]
                mC, eC, jsC = jk(kb, lambda v: v)
                ok = (mC > a.sig * eC) & (r > a.rmin) & (pn > 0)
                pe = {'n_klassen_ok': int(ok.sum()), 'n_klassen': int(len(r)),
                      'C_mittel_gross_r': float(mC[r > 0.4 * r.max()].mean())}
                if ok.sum() > nsub + 3:
                    y = -np.log(mC[ok]) / T
                    ey = eC[ok] / mC[ok] / T
                    fits = {}
                    for form in ('sc', 'c', 's_cfest'):
                        p, chi2, dof = fit_V(r[ok], kl[ok, :2], y, ey, nsub, form, c_fest=np.pi / 12)
                        pj = []
                        for jsamp in jsC:
                            if (jsamp[ok] <= 0).any():
                                continue
                            yj = -np.log(jsamp[ok]) / T
                            pj.append(fit_V(r[ok], kl[ok, :2], yj, ey, nsub, form, c_fest=np.pi / 12)[0])
                        errs = {}
                        if len(pj) > 2:
                            for k in p:
                                v = np.array([q[k] for q in pj])
                                errs[k] = float(np.sqrt((len(v) - 1) / len(v) * ((v - v.mean()) ** 2).sum()))
                        fits[form] = {'par': {k: p[k] for k in p if not k.startswith('u')},
                                      'err': {k: errs.get(k) for k in p if not k.startswith('u')},
                                      'chi2': chi2, 'dof': dof, 'n_jk': len(pj)}
                    pe['V_fits'] = fits
                    pe['r_bereich'] = [float(r[ok].min()), float(r[ok].max())]
                edges = np.linspace(0, r.max() + 1e-9, 9)
                vb = []
                for i in range(8):
                    s = (r >= edges[i]) & (r < edges[i + 1])
                    if s.any():
                        Cm = float((mC[s] * pn[s]).sum() / pn[s].sum())
                        Ce = float(np.sqrt(((eC[s] * pn[s]) ** 2).sum()) / pn[s].sum())
                        vb.append([float(0.5 * (edges[i] + edges[i + 1])), Cm, Ce])
                pe['C_rbins'] = vb
                e['poly'][var] = pe
            # Photon: effektive Energie aus cosh
            ph = z['ph_%d' % ib]
            mP, eP, _ = jk(ph, lambda v: v)
            eff = []
            for ik in range(mP.shape[0]):
                Ck = mP[ik]
                row = []
                for t in range(Nt // 2):
                    if Ck[t] > 0 and Ck[t + 1] > 0 and Ck[t] > 2 * eP[ik, t] and Ck[t + 1] > 2 * eP[ik, t + 1]:
                        q = Ck[t] / Ck[t + 1]
                        lo, hi = 1e-6, 20.0
                        for _ in range(100):
                            mid = 0.5 * (lo + hi)
                            f = np.cosh(mid * (Nt / 2 - t)) / np.cosh(mid * (Nt / 2 - t - 1))
                            if f < q:
                                lo = mid
                            else:
                                hi = mid
                        row.append(0.5 * (lo + hi) / tau)
                    else:
                        row.append(None)
                eff.append(row)
            e['photon_C'] = mP.tolist(); e['photon_C_err'] = eP.tolist(); e['photon_Eeff'] = eff
            # Photon mit Jackknife-Fehlern (ohne Signifikanzschnitt), E in physikalischen Einheiten (/tau)
            ph_all = z['ph_%d' % ib]
            mP2, _, jsP = jk(ph_all, lambda v: v)
            E0 = eeff_arr(mP2, Nt) / tau
            Ej = np.array([eeff_arr(j, Nt) for j in jsP]) / tau
            nj = len(Ej)
            with np.errstate(invalid='ignore'):
                Eerr = np.sqrt((nj - 1) / nj * np.nansum((Ej - np.nanmean(Ej, 0)) ** 2, 0))
                Eerr[np.isnan(Ej).any(0)] = np.nan
            e['photon_E'] = nn(E0); e['photon_E_err'] = nn(Eerr)
            kb_ = np.array([float(np.linalg.norm(k)) for k in res['kvek']])
            fam = {}
            for nm in sorted(set(x[:3] for x in res['kname'])):
                idx = [i for i, x in enumerate(res['kname']) if x[:3] == nm]
                fam[nm] = {'k': float(kb_[idx[0]]),
                           'E_durch_k_t1': nn1(np.nanmean(E0[idx, 1]) / kb_[idx[0]]) if E0.shape[1] > 1 else None,
                           'E_durch_k_t2': nn1(np.nanmean(E0[idx, 2]) / kb_[idx[0]]) if E0.shape[1] > 2 else None,
                           'spanne_t1': nn1(np.nanmax(E0[idx, 1]) - np.nanmin(E0[idx, 1])) if E0.shape[1] > 1 else None}
            e['photon_familien'] = fam
            e['k_betrag'] = [float(np.linalg.norm(k)) for k in res['kvek']]
            d['betas'].append(e)
        # Uebergang: Maximum der Suszeptibilitaet (Parabel durch 3 Punkte)
        bs = np.array([e['beta'] for e in d['betas']]); cs = np.array([e['chi'] for e in d['betas']])
        if len(bs) >= 3:
            o = np.argsort(bs); bs, cs = bs[o], cs[o]
            i = int(np.argmax(cs))
            d['chi_max_beta_gitter'] = float(bs[i])
            if 0 < i < len(bs) - 1:
                x = bs[i - 1:i + 2]; yv = cs[i - 1:i + 2]
                A = np.polyfit(x, yv, 2)
                if A[0] < 0:
                    d['chi_max_beta_parabel'] = float(-A[1] / (2 * A[0]))
        out['dateien'].append(d)
    with open(a.out, 'w') as f:
        json.dump(out, f, indent=1)


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='modus', required=True)
    p = sub.add_parser('netz')
    p.add_argument('--taus', type=float, nargs='+', default=[0.2924, 1.0])
    p.add_argument('--nk', type=int, default=20)
    p.add_argument('--out', required=True)
    p = sub.add_parser('scan')
    p.add_argument('--gitter', choices=['kubisch', 'netz'], required=True)
    p.add_argument('--L', type=int, required=True)
    p.add_argument('--Nt', type=int, required=True)
    p.add_argument('--tau', type=float, default=1.0)
    p.add_argument('--gew', default='dec')
    p.add_argument('--betas', nargs='+', required=True)
    p.add_argument('--start', default='heiss')
    p.add_argument('--ntherm', type=int, default=200)
    p.add_argument('--nmess', type=int, default=1000)
    p.add_argument('--nbin', type=int, default=20)
    p.add_argument('--nor', type=int, default=2)
    p.add_argument('--mabst', type=int, default=1)
    p.add_argument('--seed', type=int, default=20261005)
    p.add_argument('--zeitlimit', type=float, default=540.0)
    p.add_argument('--out', required=True)
    p = sub.add_parser('auswertung')
    p.add_argument('--ein', nargs='+', required=True)
    p.add_argument('--sig', type=float, default=3.0)
    p.add_argument('--rmin', type=float, default=0.0)
    p.add_argument('--out', required=True)
    a = ap.parse_args()
    if a.modus == 'netz':
        lauf_netz(a)
    elif a.modus == 'scan':
        lauf_scan(a)
    else:
        lauf_auswertung(a)


if __name__ == '__main__':
    main()
