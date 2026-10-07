#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QUANT-2, Gewichtssuche: orthogonaler (Potenz-)Dual des 4D-Zeltnetzes V mal Zeit.

Hodge-Stern auf Dreiecken *2_f = |*f| / |f| mit gewichteten Umkreismitten (Ortho-Zentren, Eckgewichte omega_b je
Untergitter, zeitlich konstant) und Zeltstangenhoehe tau. omega = 0 ist der umkreismittige DEC-Stern.
Prueft: Identitaet Summe w S S^T = Vol I (Maxwell fuer konstantes F), Vorzeichen der w, und ob die Gauss-Form
K(q) = d1^+ W d1 auf dem eichfreien Raum positiv ist (Bloch, q zufaellig in der Zone).
Sucht (Nelder-Mead) omega, tau mit groesstem min_q lambda_min / lambda_max.
"""
import argparse, json, os, sys, time
import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import qu2  # noqa: E402
import rk, pt  # noqa: E402


class Vorlage:
    def __init__(self, nq=16, seed=11):
        g = qu2.netz_gitter(1.0)
        self.g = g
        self.X1 = g.Xs.copy()                                   # tau = 1: Zeitkoordinate = hb + n_t
        self.sub = np.array([[v[0] for v in Sv] for Sv in g.simp])
        keys = set()
        lab = np.zeros((g.S, 10), int)
        kl = []
        for s, Sv in enumerate(g.simp):
            for k, tri in enumerate(pt.DREI5):
                kl.append(rk.kanon_menge([Sv[x] for x in tri]))
        self.keys = sorted(set(kl))
        kid = {k: i for i, k in enumerate(self.keys)}
        self.lab = np.array([kid[k] for k in kl]).reshape(g.S, 10)
        self.NF = len(self.keys)
        # Repraesentanten (b, d) der Dreiecksklassen
        self.rep_sub = np.array([[b for (b, d) in key] for key in self.keys])
        self.rep_d = np.array([[d for (b, d) in key] for key in self.keys], float)   # (NF, 3, 4)
        # Bloch: d1 und d0 in reduzierten Koordinaten q (Phase exp(i q . T))
        eid = {key: i for i, key in enumerate(g.ekeys)}
        rows, cols, sg, T = [], [], [], []
        for f, key in enumerate(self.keys):
            vs = list(key)
            for a, b in ((0, 1), (1, 2), (2, 0)):
                ek, Tn = rk.kanon_kante(vs[a], vs[b])
                s_ = 1.0 if (ek[0] == vs[a][0] and tuple(Tn) == tuple(int(x) for x in vs[a][1])) else -1.0
                rows.append(f); cols.append(eid[ek]); sg.append(s_); T.append(Tn)
        rows, cols, sg, T = map(np.array, (rows, cols, sg, T))
        rng = np.random.default_rng(seed)
        self.qs = rng.uniform(-np.pi, np.pi, (nq, 4))
        self.DQ = []
        self.d1d0 = 0.0
        for q in self.qs:
            D = np.zeros((self.NF, g.NE), complex)
            np.add.at(D, (rows, cols), sg * np.exp(1j * (T @ q)))
            d0 = np.zeros((g.NE, g.NV), complex)
            for e, (b1, b2, d) in enumerate(g.ekeys):
                d0[e, b2] += np.exp(1j * (np.array(d, float) @ q))
                d0[e, b1] -= 1.0
            self.d1d0 = max(self.d1d0, float(np.abs(D @ d0).max()))
            U, sv, _ = np.linalg.svd(d0, full_matrices=True)
            r = int((sv > 1e-10 * sv[0]).sum())
            Q = U[:, r:]
            self.DQ.append(D @ Q)

    def X(self, tau):
        X = self.X1.copy()
        X[:, :, 3] *= tau
        return X

    def sterne(self, tau, om):
        """om: Gewichte je Untergitter (10). Gibt w (NF), area, S (NF x 6)."""
        X = self.X(tau)
        W = om[self.sub]                                       # (S, 5)
        cs = ortho(X, W)                                       # (S, 4)
        cT = np.stack([ortho(np.delete(X, m, 1), np.delete(W, m, 1)) for m in range(5)], 1)   # (S, 5, 4)
        cF = np.stack([ortho(X[:, list(tri)], W[:, list(tri)]) for tri in pt.DREI5], 1)        # (S, 10, 4)
        dual = np.zeros(self.NF)
        for k, (l0, m0) in enumerate(pt.PAARE5):
            for (l, m) in ((l0, m0), (m0, l0)):
                ct = cT[:, m]
                d1 = ct - cF[:, k]
                d2 = cs - ct
                s1 = np.sign(np.einsum('si,si->s', d1, X[:, l] - cF[:, k]))
                s2 = np.sign(np.einsum('si,si->s', d2, X[:, m] - ct))
                pc = 0.5 * s1 * s2 * np.linalg.norm(d1, axis=1) * np.linalg.norm(d2, axis=1)
                dual += np.bincount(self.lab[:, k], pc, minlength=self.NF)
        P = self.rep_pos(tau)
        a = P[:, 1] - P[:, 0]; b = P[:, 2] - P[:, 0]
        S = 0.5 * np.stack([a[:, m] * b[:, n] - a[:, n] * b[:, m] for (m, n) in qu2.IU], 1)
        area = np.linalg.norm(S, axis=1)
        return dual / area, area, S

    def rep_pos(self, tau):
        g = self.g
        xb = np.c_[g.xb, tau * g.hb]
        A = g.A.copy(); A[3, 3] = tau
        return xb[self.rep_sub] + self.rep_d @ A.T

    def bloch(self, w):
        lmin = []
        for DQ in self.DQ:
            K = np.conj(DQ.T) @ (w[:, None] * DQ)
            ev = np.linalg.eigvalsh(0.5 * (K + np.conj(K.T)))
            lmin.append(ev[0] / np.abs(ev).max())
        return float(min(lmin)), int(sum(1 for x in lmin if x < 0))


def ortho(P, W):
    """Gewichtete Umkreismitte (Ortho-Zentrum) je Zeile: |c - p_i|^2 - W_i gleich fuer alle i."""
    E = P[:, 1:] - P[:, :1]
    G = np.einsum('smi,sni->smn', E, E)
    rhs = np.einsum('smm->sm', G) - (W[:, 1:] - W[:, :1])
    a = np.linalg.solve(2.0 * G, rhs[..., None])[..., 0]
    return P[:, 0] + np.einsum('sm,smi->si', a, E)


def bewerte(V, tau, om):
    w, area, S = V.sterne(tau, om)
    Vc = 0.25 * tau
    M = np.einsum('f,fa,fb->ab', w, S, S)
    lm, nq_neg = V.bloch(w)
    return {'tau': float(tau), 'omega': [float(x) for x in om], 'identitaet_rel': float(np.abs(M - Vc * np.eye(6)).max() / Vc),
            'n_neg_w': int((w < 0).sum()), 'w_min_rel': float(w.min() / w.max()),
            'neg_anteil': float(np.abs(w[w < 0]).sum() / np.abs(w).sum()),
            'bloch_lmin_rel': lm, 'bloch_q_neg': nq_neg}, w


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--taus', type=float, nargs='+', default=[0.1, 0.15, 0.2, 0.25, 0.2924, 0.35, 0.45, 0.6, 0.8, 1.0])
    ap.add_argument('--nm_iter', type=int, default=600)
    ap.add_argument('--nstart', type=int, default=3)
    ap.add_argument('--zeitlimit', type=float, default=500.0)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    V = Vorlage()
    out = {'kopf': qu2.kopf(), 'd1d0_max': V.d1d0, 'NF': V.NF, 'nq': len(V.qs), 'scan_omega0': [], 'suche': []}
    for tau in a.taus:
        e, _ = bewerte(V, tau, np.zeros(10))
        out['scan_omega0'].append(e)
        print(json.dumps(e), flush=True)
    # Zufallsprobe in omega (Skala ~ (Kante)^2) bei tau = 0.2924, Kontrolle der Identitaet fuer omega != 0
    rng = np.random.default_rng(5)
    e, _ = bewerte(V, 0.2924, rng.normal(0, 0.02, 10))
    out['probe_omega_zufall'] = e
    print('probe', json.dumps(e), flush=True)
    from scipy.optimize import minimize

    def ziel(x):
        tau = float(np.exp(x[0]))
        om = np.r_[0.0, x[1:]]
        w, area, S = V.sterne(tau, om)
        lm, _ = V.bloch(w)
        return -lm
    beste = None
    starts = sorted(out['scan_omega0'], key=lambda e: -e['bloch_lmin_rel'])[:a.nstart]
    for st in starts:
        if time.time() - t0 > a.zeitlimit:
            break
        x0 = np.r_[np.log(st['tau']), np.zeros(9)]
        r = minimize(ziel, x0, method='Nelder-Mead',
                     options={'maxiter': a.nm_iter, 'xatol': 1e-6, 'fatol': 1e-9, 'initial_simplex':
                              np.vstack([x0] + [x0 + 0.15 * np.eye(10)[i] * (1.0 if i == 0 else 0.1) for i in range(10)])})
        e, w = bewerte(V, float(np.exp(r.x[0])), np.r_[0.0, r.x[1:]])
        e['start_tau'] = st['tau']; e['nfev'] = int(r.nfev)
        out['suche'].append(e)
        print('suche', json.dumps(e), flush=True)
        if beste is None or e['bloch_lmin_rel'] > beste[0]['bloch_lmin_rel']:
            beste = (e, w)
    if beste is not None:
        np.savez(a.out + '.beste.npz', tau=beste[0]['tau'], omega=np.array(beste[0]['omega']), w=beste[1])
        out['beste'] = beste[0]
        # dichte Nachpruefung mit 96 anderen q (und omega = 0 bei gleichem tau zum Vergleich)
        V2 = Vorlage(nq=96, seed=99)
        out['beste_dicht'] = {'bloch': V2.bloch(beste[1]),
                              'omega0_gleiches_tau': V2.bloch(V2.sterne(beste[0]['tau'], np.zeros(10))[0])}
        print('dicht', json.dumps(out['beste_dicht']), flush=True)
    out['zeit_s'] = time.time() - t0
    with open(a.out, 'w') as f:
        json.dump(out, f, indent=1)


if __name__ == '__main__':
    main()
