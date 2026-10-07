#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QUANT-3 Nachtrag S5 (fmhc-physics, 07.10.2026): Wilson-Gradient-Flow fuer SU(2) auf Hyperkubus und Zeltnetz.

Importiert su2b.py (Waermebad, Ueberrelaxation, Gitter; unveraendert) und qu2.py. Neue Datei, nichts Vorhandenes geaendert.
Flussgleichung (Luescher 2010): d V / dt = Z(V) V, Z = -g0^2 T^a d^a S_w; S_w = beta Summe_f w_f (1 - p0_f), g0^2 = 4/beta.
In Quaternionen (U -> e^z U): Z(l) = -(0, Vektorteil von U_l W_l), W_l = gewichteter Staple (Summe_f w_f Rest) wie im Waermebad.
Variante --metrik (nur Netz): Z(l) -> Z(l)/h_l mit h_l = |*e_l|/|e_l| (umkreismittiger DEC-Hodge-Stern der Kante, duales 3-Volumen
 durch Fahnen e < f < tau < sigma, wie hodge2 fuer Dreiecke). Auf dem Hyperkubus ist h_l = 1 und beide Formen sind gleich.
Integrator: Luescher-RK3 (Anhang C von arXiv:1006.4518), Schrittweite eps(t) = min(max(eps0, epsfrac t), epsmax).
Energiedichte (Plakette): E = (4 / V4) Summe_f w_f (1 - p0_f); aufgespalten in Scheibenanteil (Dreiecke in einer Zeitscheibe, E_s) und Rest (E_t).
V4 = L^3 Nt Vc, Vc = Zellvolumen (kubisch: 1; Netz: |det A| = 0,25 tau).
Aufruf nur ueber kleintest.sh auf der .69.
"""
import argparse
import itertools
import json
import os
import sys
import time

import numpy as np
import torch

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import su2b as S  # noqa: E402
import qu2  # noqa: E402

DEV, DT, log = S.DEV, S.DT, S.log
qmul = S.qmul_alt


def expq(z):
    """exp einer reinen Quaternion (Vektor z, (...,3)) -> (...,4)."""
    n = z.norm(dim=-1, keepdim=True)
    s = torch.where(n < 1e-10, 1.0 - n * n / 6.0, torch.sin(n) / n.clamp_min(1e-300))
    return torch.cat((torch.cos(n), s * z), -1)


def plan(eps0, frac, epsmax, tmax):
    ts, es, t = [], [], 0.0
    while t < tmax - 1e-12:
        e = min(max(eps0, frac * t), epsmax)
        if t + e > tmax:
            e = tmax - t
        es.append(e)
        t += e
        ts.append(t)
    return np.array(es), np.array(ts)


class Fluss:
    def __init__(self, G, K, V4, invh=None):
        self.G = G
        self.F = S.Inzidenz(K, np.ones(G.nE, bool))
        if self.F.ned != G.nE or not bool((self.F.ed == torch.arange(G.nE, device=DEV)).all()):
            raise RuntimeError('Inzidenz deckt nicht alle Links')
        self.V4 = V4
        self.invh = None if invh is None else torch.as_tensor(invh, dtype=DT, device=DEV)[None, :, None]

    def staple(self, Q):
        F = self.F
        A = Q[:, F.oth[0]] * F.om[0]
        for j in range(1, self.G.m - 1):
            A = qmul(A, Q[:, F.oth[j]] * F.om[j])
        A = A * F.spw
        W = torch.zeros((Q.shape[0], F.ned, 4), dtype=DT, device=DEV)
        W.index_add_(1, F.loc, A)
        del A
        return W

    def Zvek(self, Q):
        """Vektor z mit Z = (0, z) = -(0, Vektorteil U W) [/ h_l]."""
        W = self.staple(Q)
        M = qmul(Q, W)
        z = -M[..., 1:]
        if self.invh is not None:
            z = z * self.invh
        return z

    def schritt(self, Q, eps):
        Z0 = eps * self.Zvek(Q)
        Q1 = qmul(expq(Z0 / 4.0), Q)
        Z1 = eps * self.Zvek(Q1)
        Q2 = qmul(expq(8.0 / 9.0 * Z1 - 17.0 / 36.0 * Z0), Q1)
        Z2 = eps * self.Zvek(Q2)
        Q3 = qmul(expq(0.75 * Z2 - 8.0 / 9.0 * Z1 + 17.0 / 36.0 * Z0), Q2)
        zm = max(float(Z0.abs().max()), float(Z1.abs().max()), float(Z2.abs().max()))
        return Q3 / Q3.norm(dim=-1, keepdim=True), zm

    def energie(self, Q):
        G = self.G
        pw, pu, ps, pt = G.plaketten(Q)
        f = 4.0 / self.V4
        E = f * G.wsum * (1.0 - pw)
        Es = f * G.ws * (1.0 - ps)
        Et = f * G.wt * (1.0 - pt)
        return torch.stack((E, Es, Et), -1)[0].cpu().numpy()

    def wirkung(self, Q, beta):
        pw = self.G.plaketten(Q)[0]
        return float(beta * self.G.wsum * (1.0 - pw[0]))

    def fliesse(self, Q, es, rec=1):
        """Q (1,nE,4) bleibt unveraendert; es = Schrittweiten. Rueckgabe: E-Reihe (n_rec+1, 3), max |Z|/eps, Normabweichung, ok."""
        Q = Q.clone()
        er = [self.energie(Q)]
        zmax = 0.0
        ok = True
        for k, e in enumerate(es):
            Q, zm = self.schritt(Q, float(e))
            zmax = max(zmax, zm / float(e))
            if (k + 1) % rec == 0:
                x = self.energie(Q)
                er.append(x)
                if not np.isfinite(x).all() or abs(x[0]) > 1e12:
                    ok = False
                    break
        nrm = float((Q.norm(dim=-1) - 1.0).abs().max())
        return np.array(er), zmax, nrm, ok


# ================================================================================================ Netz: Hodge der Kanten
def umkreis(P):
    return qu2.umkreis(P)


def hodge1(g):
    """h_e = |*e| / |e| je Kantenklasse (g.ekeys), duales 3-Volumen = Summe ueber Fahnen e<f<tau<sigma von
    (1/6) s1|d1| s2|d2| s3|d3| (paarweise senkrecht)."""
    import rk
    dual = {}
    for s, Sv in enumerate(g.simp):
        X = g.Xs[s]
        cs = umkreis(X)
        for (i, j) in itertools.combinations(range(5), 2):
            ek, _ = rk.kanon_kante(Sv[i], Sv[j])
            ce = umkreis(X[[i, j]])
            rest = [x for x in range(5) if x not in (i, j)]
            tot = 0.0
            for (l, m, r) in itertools.permutations(rest):
                cf = umkreis(X[[i, j, l]])
                ct = umkreis(X[[i, j, l, m]])
                d1, d2, d3 = cf - ce, ct - cf, cs - ct
                s1 = np.sign(d1 @ (X[l] - ce))
                s2 = np.sign(d2 @ (X[m] - cf))
                s3 = np.sign(d3 @ (X[r] - ct))
                tot += s1 * np.linalg.norm(d1) * s2 * np.linalg.norm(d2) * s3 * np.linalg.norm(d3) / 6.0
            dual[ek] = dual.get(ek, 0.0) + tot
    eid = {k: i for i, k in enumerate(g.ekeys)}
    dv = np.zeros(len(g.ekeys))
    for k, v in dual.items():
        dv[eid[k]] = v
    laenge = np.linalg.norm(g.E, axis=1)
    return dv / laenge, dv, laenge


def link_klassen(L, Nt, g, nE):
    """Kantenklasse je Link (gleiche Reihenfolge wie qu2.netz)."""
    dims = np.array([L, L, L, Nt])
    cells = np.array(list(itertools.product(range(L), range(L), range(L), range(Nt))))
    nc = len(cells)
    NV = g.NV
    nV = NV * nc

    def vid(b, n):
        m = np.mod(n, dims)
        return (((m[..., 3] * L + m[..., 0]) * L + m[..., 1]) * L + m[..., 2]) * NV + b
    E1, E2, cl = [], [], []
    for k, (b1, b2, d) in enumerate(g.ekeys):
        E1.append(vid(np.full(nc, b1), cells))
        E2.append(vid(np.full(nc, b2), cells + np.array(d)))
        cl.append(np.full(nc, k))
    E1 = np.concatenate(E1)
    E2 = np.concatenate(E2)
    cl = np.concatenate(cl)
    lo, hi = np.minimum(E1, E2), np.maximum(E1, E2)
    code = lo.astype(np.int64) * nV + hi
    uc = np.unique(code)
    if len(uc) != nE:
        raise RuntimeError('Linkzahl passt nicht')
    out = np.empty(len(uc), int)
    out[np.searchsorted(uc, code)] = cl
    return out


def bau(a):
    if a.gitter == 'kubisch':
        return qu2.kubisch(a.L, a.Nt), 1.0, None
    K = qu2.netz(a.L, a.Nt, a.tau, a.gew)
    g = qu2.netz_gitter(a.tau)
    return K, float(g.Vc), g


def volcheck(a, g):
    h = qu2.hodge2(g)
    dat = np.load(a.gew[6:])
    w = np.asarray(dat['w'], float)
    Sb = h['S']
    M = np.einsum('f,fi,fj->ij', w, Sb, Sb)
    out = {'Vc': float(g.Vc), 'spur_M': float(np.trace(M)), 'spur_soll_6Vc': 6.0 * float(g.Vc),
           'max_abw_M_minus_VcI': float(np.abs(M - g.Vc * np.eye(6)).max()),
           'n_klassen': int(len(w)), 'n_neg_w_klassen': int((w < 0).sum()), 'w_min': float(w.min()), 'w_max': float(w.max())}
    hh, dv, ln = hodge1(g)
    out['kanten'] = {'n_klassen': int(len(hh)), 'summe_dual_mal_laenge': float((dv * ln).sum()),
                     'soll_4Vc_ueber_stern': 4.0 * float(g.Vc), 'h_min': float(hh.min()), 'h_max': float(hh.max()),
                     'h_mittel': float(hh.mean()), 'n_h_nichtpositiv': int((hh <= 0).sum()),
                     'laenge_min': float(ln.min()), 'laenge_max': float(ln.max()), 'h_liste': hh.tolist(), 'laenge_liste': ln.tolist()}
    return out


def lauf(a):
    t_start = time.time()
    K, Vc, g = bau(a)
    G = S.Gitter(K, False)
    V4 = float(a.L) ** 3 * a.Nt * Vc
    invh = None
    res = {'kopf': S.kopf(), 'gitter': a.gitter, 'L': a.L, 'Nt': a.Nt, 'tau': float(K.tau), 'gew': a.gew, 'nE': G.nE,
           'nF': G.nF, 'V4': V4, 'Vc': Vc, 'wsum': G.wsum, 'ws': G.ws, 'wt': G.wt, 'n_neg_w': int((K.w < 0).sum()),
           'eps0': a.eps, 'epsfrac': a.epsfrac, 'epsmax': a.epsmax, 'tmax': a.tmax, 'rec': a.rec, 'ntherm': a.ntherm,
           'mabst': a.mabst, 'nor': a.nor, 'seed': a.seed, 'betas': a.betas, 'ncfg_soll': a.ncfg, 'metrik': a.metrik,
           'je_beta': [], 'abbruch': None}
    if a.gitter == 'netz' and (a.volcheck or a.metrik):
        vc = volcheck(a, g)
        res['volcheck'] = vc
        log('volcheck', json.dumps({k: v for k, v in vc.items() if k != 'kanten'}))
        log('volcheck Kanten', json.dumps({k: v for k, v in vc['kanten'].items() if not k.endswith('liste')}))
        if a.metrik:
            hh = np.array(vc['kanten']['h_liste'])
            if (hh <= 0).any():
                raise RuntimeError('h_l nicht positiv fuer %d Klassen' % int((hh <= 0).sum()))
            invh = 1.0 / hh[link_klassen(a.L, a.Nt, g, G.nE)]
            res['invh_min_max'] = [float(invh.min()), float(invh.max())]
    FL = Fluss(G, K, V4, invh)
    log('Gitter', a.gitter, 'L', a.L, 'Nt', a.Nt, 'nE', G.nE, 'nF', G.nF, 'Farben', G.nfarb, 'V4', V4,
        'n_neg_w', int((K.w < 0).sum()), 'inz', FL.F.n_inz, 'metrik', a.metrik, 'Bau %.1f s' % (time.time() - t_start))
    es, tgrid = plan(a.eps, a.epsfrac, a.epsmax, a.tmax)
    res['n_schritte'] = int(len(es))
    log('Schrittplan', len(es), 'Schritte bis t', tgrid[-1])
    torch.manual_seed(a.seed)
    arr = {}
    rec = a.rec
    for ib, b in enumerate(a.betas):
        beta = torch.full((1, 1), float(b), dtype=DT, device=DEV)
        x = torch.randn((G.nE, 4), dtype=DT, device=DEV)
        Q = (x / x.norm(dim=-1, keepdim=True))[None].clone()
        t0 = time.time()
        for _ in range(a.ntherm):
            G.sweep(Q, beta, None, a.nor)
        torch.cuda.synchronize()
        info = {'beta': float(b), 'zeit_therm_s': time.time() - t0, 'cfg': 0, 'zmax': 0.0, 'norm_abw': 0.0, 'nichtendlich': 0}
        if a.test and ib == 0:
            tt = {}
            m = qmul(Q, FL.staple(Q))[..., 1:]
            if FL.invh is not None:
                soll = -float(b) * float((m * m * FL.invh).sum())
            else:
                soll = -float(b) * float((m * m).sum())
            e1 = 1e-5 if FL.invh is not None else 1e-4
            Q1, _ = FL.schritt(Q, e1)
            ist = (FL.wirkung(Q1, float(b)) - FL.wirkung(Q, float(b))) / e1
            tt['dSdt_ist'] = ist
            tt['dSdt_soll'] = soll
            tt['dSdt_rel_abw'] = abs(ist - soll) / abs(soll)
            ttest = min(a.tmax, a.ttest)
            es1, ts1 = plan(a.eps, a.epsfrac, a.epsmax, ttest)
            es2 = np.repeat(es1 / 2.0, 2)
            e_a, z_a, n_a, ok_a = FL.fliesse(Q, es1, 1)
            e_b, z_b, n_b, ok_b = FL.fliesse(Q, es2, 2)
            rel = np.abs(e_a[1:, 0] - e_b[1:, 0]) / np.abs(e_b[1:, 0])
            tt['eps_test_t'] = [0.0] + ts1.tolist()
            tt['E_eps'] = e_a[:, 0].tolist()
            tt['E_eps_halbe'] = e_b[:, 0].tolist()
            tt['E_rel_abw_max'] = float(rel.max())
            tt['E_rel_abw_ende'] = float(rel[-1])
            tt['zmax_eps'] = z_a
            tt['zmax_halbe'] = z_b
            tt['ok'] = [bool(ok_a), bool(ok_b)]
            tt['norm_abw'] = max(n_a, n_b)
            res['test'] = tt
            log('test', json.dumps({k: v for k, v in tt.items() if not isinstance(v, list)}))
        EA, stop = [], False
        for ic in range(a.ncfg):
            if time.time() - t_start > a.zeitlimit:
                stop = True
                break
            for _ in range(a.mabst):
                G.sweep(Q, beta, None, a.nor)
            er, zm, nrm, ok = FL.fliesse(Q, es, rec)
            if not ok:
                info['nichtendlich'] += 1
                continue
            EA.append(er)
            info['zmax'] = max(info['zmax'], zm)
            info['norm_abw'] = max(info['norm_abw'], nrm)
            info['cfg'] += 1
            if ic % 4 == 0:
                tr = np.r_[0.0, tgrid[rec - 1::rec]]
                t2 = tr ** 2 * er[:, 0]
                log('beta', b, 'cfg', ic, 'E0 %.4f' % er[0, 0], 't2E(tmax) %.4f' % t2[-1], 'max t2E %.4f' % t2.max(),
                    'zmax %.3f' % zm, 'zeit %.0f s' % (time.time() - t_start))
        info['zeit_s'] = time.time() - t0
        if EA:
            arr['E_%d' % ib] = np.array(EA)          # (ncfg, nt, 3)
        res['je_beta'].append(info)
        if stop:
            res['abbruch'] = 'Zeitlimit bei beta %g nach %d Konfigurationen' % (b, info['cfg'])
            break
    arr['t'] = np.r_[0.0, tgrid[rec - 1::rec]]
    res['zeit_gesamt_s'] = time.time() - t_start
    res['gpu_speicher_max_MB'] = torch.cuda.max_memory_allocated() / 1e6
    np.savez_compressed(a.out + '.npz', **arr)
    with open(a.out + '.json.tmp', 'w') as f:
        json.dump(res, f, indent=1)
    os.replace(a.out + '.json.tmp', a.out + '.json')
    log('fertig', a.out, 'Zeit %.1f s' % res['zeit_gesamt_s'], 'GPU max %.0f MB' % res['gpu_speicher_max_MB'])


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='modus', required=True)
    p = sub.add_parser('lauf')
    p.add_argument('--gitter', choices=['kubisch', 'netz'], required=True)
    p.add_argument('--L', type=int, required=True)
    p.add_argument('--Nt', type=int, required=True)
    p.add_argument('--tau', type=float, default=1.0)
    p.add_argument('--gew', default='eins')
    p.add_argument('--betas', type=float, nargs='+', required=True)
    p.add_argument('--ncfg', type=int, default=40)
    p.add_argument('--mabst', type=int, default=20)
    p.add_argument('--ntherm', type=int, default=200)
    p.add_argument('--nor', type=int, default=2)
    p.add_argument('--eps', type=float, default=0.02)
    p.add_argument('--epsfrac', type=float, default=0.0)
    p.add_argument('--epsmax', type=float, default=0.05)
    p.add_argument('--tmax', type=float, default=2.0)
    p.add_argument('--ttest', type=float, default=0.4)
    p.add_argument('--rec', type=int, default=1)
    p.add_argument('--seed', type=int, default=20261007)
    p.add_argument('--zeitlimit', type=float, default=480.0)
    p.add_argument('--test', action='store_true')
    p.add_argument('--volcheck', action='store_true')
    p.add_argument('--metrik', action='store_true')
    p.add_argument('--out', required=True)
    a = ap.parse_args()
    lauf(a)


if __name__ == '__main__':
    main()
