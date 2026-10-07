#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BETA-NETZ-V, Folgeauftrag SCHWARZES-LOCH (ohne Karte), Code-Agent fuer die Leitung claude-primary.

Dieselbe nichtlineare Statik wie bn.py (bn.py unveraendert importiert): Eckenregel R1, exakte Diederwinkel, Takt je Ecke,
Eichung M^H (a + q W mu) = 0, Rest in Eichrichtungen ueber M lam, k = 0 nicht geloest.
Neu:
  - Quelle: Kugel um die Ecke C1 (Untergitter 4) mit Radius R0 (l_P), sigma_v = s vol_v / Summe vol (alle Ecken mit
    r <= R0), also gleichfoermige Koordinaten-Energiedichte, Gesamtstaerke s, ohne Druck.
  - Rest per Index-Sammlung (schneller als bn.Netz.rest, Gleichheit im Modus test geprueft).
  - Loeser: Anderson-Beschleunigung (m = 8) auf dem Quasi-Newton-Schritt mit flacher KKT; Fortsetzung in s mit
    linearem Praediktor; Schritt verworfen bei nicht endlichen Werten, entarteten Tetraedern oder Wachstum (dann
    Daempfung beta/2, Neustart vom besten Stand).
Je Staerke: N_min, N in der Mitte, Psi^2 = 1 + Mittel(a) je Ecke, Fernfit Psi = c0 + c1/r + c2 r^2 und
N = d0 + d1/(r + c1/c0) + d2 r^2 fuer r in [R0 + 1,5; L/2]; M'/2 = c1/c0 (isotrop, Koordinatenlaenge),
x = M'/(2 R0), Kompaktheit 2M/R_Flaeche = 4x/(1 + x)^2, K = -d1/d0 (Tolman-artig), Flaechenradius r Psi^2 je Schale.
Aufruf nur ueber kleintest.sh auf der .69.
"""
import argparse, json, sys, os, time, resource, hashlib
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bn  # noqa: E402

Q = bn.Q
HC = 1e-20


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def dieder_jac_q(l):
    d = l * l
    d01, d02, d03, d12, d13, d23 = (d[:, i] for i in range(6))
    x1 = np.sqrt(d01)
    x2 = (d01 + d02 - d12) / (2 * x1)
    y2s = d02 - x2 * x2
    x3 = (d01 + d03 - d13) / (2 * x1)
    y3 = (d02 + d03 - d23 - 2 * x2 * x3) / (2 * np.sqrt(np.maximum(y2s, 1e-300)))
    z3s = d03 - x3 * x3 - y3 * y3
    ok = (y2s > 0) & (z3s > 0)
    J = np.empty(l.shape + (6,))
    th = sn = None
    for j in range(6):
        lc = l.astype(complex)
        lc[:, j] += 1j * HC
        c = bn.dieder_cos(lc)
        if th is None:
            th = np.arccos(np.clip(c.real, -1.0, 1.0))
            sn = np.sin(th)
        with np.errstate(divide='ignore', invalid='ignore'):
            J[:, :, j] = -c.imag / (HC * sn)
    return th, J, sn, ok


class Schnell:
    def __init__(self, L):
        net = bn.Netz(L)
        self.net, self.L = net, L
        E, nV = net.E, net.nV
        self.E, self.nV, self.Nk = E, nV, net.Nk
        n3 = L ** 3
        self.nE, self.nVt = n3 * E, n3 * nV
        base = np.arange(n3 * E).reshape(L, L, L, E)
        tidx = np.empty((len(net.tets), n3, 6), dtype=np.int64)
        for t, kant in enumerate(net.tets):
            for i, (e, n) in enumerate(kant):
                tidx[t, :, i] = bn.rollv(base[..., e], n).ravel()
        self.tidx = tidx.reshape(-1, 6)
        self.tflat = self.tidx.ravel()
        vb = np.arange(n3 * nV).reshape(L, L, L, nV)
        ea = np.empty((L, L, L, E), dtype=np.int64)
        eb = np.empty_like(ea)
        for e, (s, s2, d) in enumerate(net.kl):
            ea[..., e] = vb[..., s]
            eb[..., e] = bn.rollv(vb[..., s2], d)
        self.ea, self.eb = ea.ravel(), eb.ravel()
        self.l0f = np.broadcast_to(net.l0, (L, L, L, E)).ravel().copy()
        self.cnt = np.bincount(self.ea, minlength=self.nVt) + np.bincount(self.eb, minlength=self.nVt)
        vv = np.zeros(nV)
        for z in net.mod['zellen']:
            for (s, n) in z['ids']:
                vv[s] += z['vol'] / 4.0
        self.vv = vv

    def rest(self, a, mu, sigma):
        l = self.l0f * (1.0 + a)
        N = 1.0 + mu
        Nsum = N[self.ea] + N[self.eb]
        w = Nsum * l
        th, J, sn, ok = dieder_jac_q(l[self.tidx])
        g = np.einsum('ki,kij->kj', w[self.tidx], J)
        thsum = np.bincount(self.tflat, weights=th.ravel(), minlength=self.nE)
        Fk = -np.bincount(self.tflat, weights=g.ravel(), minlength=self.nE)
        eps = 2 * np.pi - thsum
        F = Nsum * eps + Fk
        RF = -(self.l0f / 2.0) * F
        le = l * eps
        H = np.bincount(self.ea, weights=le, minlength=self.nVt) + np.bincount(self.eb, weights=le, minlength=self.nVt)
        RG = H - sigma
        diag = {'sin_min': float(np.nanmin(sn)), 'ungueltig': int((~ok).sum()), 'eps_max': float(np.nanmax(eps)),
                'eps_min': float(np.nanmin(eps))}
        return RF, RG, diag

    def bereite_K(self):
        E, nV, Nk = self.E, self.nV, self.Nk
        n = E + 4 * nV
        self.Kinv = np.zeros((Nk, n, n), complex)
        self.Mk = np.zeros((Nk, E, 3 * nV), complex)
        self.MHW = np.zeros((Nk, 3 * nV, nV), complex)
        for i0 in range(1, Nk, 64):
            idx = np.arange(i0, min(i0 + 64, Nk))
            K, M, W, B, c = self.net.K_chunk(self.net.kgrid[idx])
            self.Kinv[idx] = np.linalg.inv(K)
            self.Mk[idx] = M
            self.MHW[idx] = bn.cT(M) @ W

    def hin(self, x, m):
        L = self.L
        return np.fft.fftn(x.reshape(L, L, L, m), axes=(0, 1, 2)).reshape(self.Nk, m)

    def zur(self, xk, m):
        L = self.L
        return np.fft.ifftn(xk.reshape(L, L, L, m), axes=(0, 1, 2)).real.ravel()

    def schritt(self, X, sigma):
        E, nV, nE, nVt = self.E, self.nV, self.nE, self.nVt
        a, mu, lam = X[:nE], X[nE:nE + nVt], X[nE + nVt:]
        RF, RG, dg = self.rest(a, mu, sigma)
        Fk = self.hin(RF, E) + np.einsum('kij,kj->ki', self.Mk, self.hin(lam, 3 * nV))
        Gk = self.hin(RG, nV)
        Ek = np.einsum('kji,kj->ki', np.conj(self.Mk), self.hin(a, E)) + Q * np.einsum('kij,kj->ki', self.MHW, self.hin(mu, nV))
        rhs = np.concatenate([Fk, Gk, Ek], -1)
        rhs[0] = 0
        dg['RF_k'] = float(np.abs(rhs[:, :E]).max() / self.Nk)
        dg['RG_k'] = float(np.abs(rhs[:, E:E + nV]).max() / self.Nk)
        dx = -np.einsum('kij,kj->ki', self.Kinv, rhs)
        G = np.concatenate([self.zur(dx[:, :E], E), self.zur(dx[:, E:E + nV], nV), self.zur(dx[:, E + nV:], 3 * nV)])
        return G, dg


def anderson(f, X0, tol, maxit, t_ende, m=8):
    X = X0.copy()
    G, dg = f(X)
    beta = 1.0
    DX, DG = [], []
    gm = float(np.abs(G).max()) if np.all(np.isfinite(G)) else np.inf
    best = (gm, X.copy(), G.copy(), dg)
    verlauf, verworfen = [], 0
    for it in range(maxit):
        gm = float(np.abs(G).max())
        verlauf.append([it, gm, dg['RF_k'], dg['RG_k'], dg['sin_min'], dg['ungueltig'], beta])
        if gm < tol:
            return X, True, verlauf, dg, verworfen
        if time.time() > t_ende:
            break
        if DX:
            dXm, dGm = np.stack(DX, 1), np.stack(DG, 1)
            gam, *_ = np.linalg.lstsq(dGm, G, rcond=None)
            Xn = X + beta * G - (dXm + beta * dGm) @ gam
        else:
            Xn = X + beta * G
        Gn, dgn = f(Xn)
        schlecht = (not np.all(np.isfinite(Gn))) or dgn['ungueltig'] > 0 or float(np.abs(Gn).max()) > 50 * best[0]
        if schlecht:
            verworfen += 1
            DX, DG = [], []
            beta *= 0.5
            X, G, dg = best[1].copy(), best[2].copy(), best[3]
            if beta < 1.0 / 64:
                break
            continue
        DX.append(Xn - X)
        DG.append(Gn - G)
        if len(DX) > m:
            DX.pop(0)
            DG.pop(0)
        X, G, dg = Xn, Gn, dgn
        g2 = float(np.abs(G).max())
        if g2 < best[0]:
            best = (g2, X.copy(), G.copy(), dg)
    return best[1], False, verlauf, best[3], verworfen


def fitw(r, y, terme, breite=0.5):
    sh = np.floor(r / breite).astype(int)
    _, inv, cnt = np.unique(sh, return_inverse=True, return_counts=True)
    w = 1.0 / np.sqrt(cnt[inv])
    X = np.stack(terme, -1)
    coef, *_ = np.linalg.lstsq(X * w[:, None], y * w, rcond=None)
    rest = float(np.sqrt(np.mean((X @ coef - y) ** 2)) / max(np.abs(y).mean(), 1e-300))
    return coef, rest


def auswerten(S, X, r, R0):
    nE, nVt, L = S.nE, S.nVt, S.L
    a, mu, lam = X[:nE], X[nE:nE + nVt], X[nE + nVt:]
    N = 1.0 + mu
    Psi2 = (np.bincount(S.ea, weights=1 + a, minlength=nVt) + np.bincount(S.eb, weights=1 + a, minlength=nVt)) / S.cnt
    Psi = np.sqrt(Psi2)
    rr = r.ravel()
    sel = (rr >= R0 + 1.5) & (rr <= 0.5 * L)
    rs = rr[sel]
    (c0, c1, c2), rp = fitw(rs, Psi[sel], [np.ones_like(rs), 1 / rs, rs ** 2])
    m2 = c1 / c0
    (d0, d1, d2), rn = fitw(rs, N[sel], [np.ones_like(rs), 1 / (rs + m2), rs ** 2])
    x = m2 / R0
    i_min = int(np.argmin(N))
    i_c = int(np.argmin(rr))
    out = {'c0': float(c0), 'c1': float(c1), 'c2': float(c2), 'fit_rest_Psi': rp, 'd0': float(d0), 'd1': float(d1), 'd2': float(d2),
           'fit_rest_N': rn, 'M_iso_lP': float(2 * m2), 'x': float(x), 'kompakt': float(4 * x / (1 + x) ** 2),
           'K_ueber_M': float((-d1 / d0) / (2 * m2)) if m2 != 0 else None,
           'N_min_rel': float(N[i_min] / d0), 'r_N_min': float(rr[i_min]), 'N_mitte_rel': float(N[i_c] / d0),
           'N_min_roh': float(N[i_min]), 'Psi2_mitte_rel': float(Psi2[i_c] / c0 ** 2), 'a_max': float(a.max()), 'a_min': float(a.min()),
           'mu_mittel': float(mu.mean()), 'lam_max': float(np.abs(lam).max()), 'N_negativ': int((N <= 0).sum())}
    sch = []
    for a0 in np.arange(0.0, 0.5 * L, 0.5):
        s = (rr >= a0) & (rr < a0 + 0.5)
        if not s.any():
            continue
        rm = float(rr[s].mean())
        sch.append([round(rm, 4), int(s.sum()), float(N[s].mean() / d0), float(N[s].min() / d0), float(Psi2[s].mean() / c0 ** 2),
                    float(rm * Psi2[s].mean() / c0 ** 2)])
    out['schalen'] = sch
    ra = [z[5] for z in sch if z[0] > 0]
    out['flaechenradius_monoton'] = bool(all(b > a_ for a_, b in zip(ra[:-1], ra[1:])))
    j = int(np.argmin(ra)) if ra else -1
    out['flaechenradius_min_bei_r'] = float([z[0] for z in sch if z[0] > 0][j]) if ra else None
    return out


def modus_test(L):
    S = Schnell(L)
    rng = np.random.default_rng(3)
    E, nV = S.E, S.nV
    a = 0.05 * rng.normal(size=(L, L, L, E))
    mu = 0.2 * rng.normal(size=(L, L, L, nV))
    sig = rng.normal(size=(L, L, L, nV))
    t0 = time.time()
    RF1, RG1 = S.net.rest(a, mu, sig)
    t1 = time.time()
    RF2, RG2, dg = S.rest(a.ravel(), mu.ravel(), sig.ravel())
    t2 = time.time()
    return {'L': L, 'RF_abw': float(np.abs(RF1.ravel() - RF2).max() / np.abs(RF1).max()),
            'RG_abw': float(np.abs(RG1.ravel() - RG2).max() / np.abs(RG1).max()), 'zeit_alt': t1 - t0, 'zeit_neu': t2 - t1, 'diag': dg}


def modus_lauf(L, R0, staerken, zustand_ein, zustand_aus, tmax, tol, maxit, v0=4):
    t0 = time.time()
    t_ende = t0 + tmax
    S = Schnell(L)
    S.bereite_K()
    tK = time.time() - t0
    r = S.net.r_von(v0)
    innen = (r <= R0 + 1e-9)
    w = S.vv[None, None, None, :] * innen
    w = (w / w.sum()).ravel()
    out = {'L': L, 'R0': R0, 'quelle_mitte': 'C1', 'n_ecken_quelle': int(innen.sum()), 'zeit_K': tK, 'staerken': []}
    n = S.nE + S.nVt + S.nVt * 3
    hist = []
    if zustand_ein:
        z = np.load(zustand_ein)
        hist = [(float(s), z['X%d' % i]) for i, s in enumerate(z['s'])]
    f_aus = None
    for s in staerken:
        if hist and s <= hist[-1][0] + 1e-12:
            continue
        if time.time() > t_ende - 30:
            out['abbruch'] = 'zeit'
            break
        if len(hist) >= 2:
            (s1, X1), (s2, X2) = hist[-2], hist[-1]
            X0 = X2 + (s - s2) / (s2 - s1) * (X2 - X1)
        elif len(hist) == 1:
            X0 = hist[-1][1] * (s / hist[-1][0])
        else:
            X0 = np.zeros(n)
        f = lambda X: S.schritt(X, s * w)
        ts = time.time()
        X, ok, verlauf, dg, verw = anderson(f, X0, tol, maxit, t_ende)
        z = {'s': s, 'konvergiert': bool(ok), 'schritte': len(verlauf), 'verworfen': verw, 'zeit_s': time.time() - ts,
             'letzter_schritt': verlauf[-1] if verlauf else None, 'diag': dg}
        z.update(auswerten(S, X, r, R0))
        z['verlauf_kurz'] = verlauf[:3] + verlauf[-3:]
        out['staerken'].append(z)
        print(json.dumps({k: z[k] for k in ('s', 'konvergiert', 'schritte', 'verworfen', 'x', 'kompakt', 'N_min_rel', 'N_mitte_rel', 'K_ueber_M')}), flush=True)
        if not ok:
            if time.time() > t_ende:
                z['zeit_abgelaufen'] = True
                out['abbruch'] = 'zeit bei s = %g (Stand nicht gespeichert)' % s
            else:
                out['abbruch'] = 'keine Konvergenz bei s = %g' % s
            break
        hist = (hist + [(s, X)])[-2:]
        f_aus = zustand_aus
        if f_aus:
            np.savez(f_aus + '.neu.npz', s=np.array([h[0] for h in hist]), **{'X%d' % i: h[1] for i, h in enumerate(hist)})
            os.replace(f_aus + '.neu.npz', f_aus)
    out['zeit_gesamt'] = time.time() - t0
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['test', 'lauf'])
    ap.add_argument('--L', type=int, default=8)
    ap.add_argument('--R0', type=float, default=2.0)
    ap.add_argument('--staerken', nargs='+', type=float, default=[1, 2, 4])
    ap.add_argument('--zustand-ein', default=None)
    ap.add_argument('--zustand-aus', default=None)
    ap.add_argument('--tmax', type=float, default=540.0)
    ap.add_argument('--tol', type=float, default=1e-10)
    ap.add_argument('--maxit', type=int, default=150)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    if a.modus == 'test':
        res = modus_test(a.L)
    else:
        res = modus_lauf(a.L, a.R0, a.staerken, a.zustand_ein, a.zustand_aus, a.tmax, a.tol, a.maxit)
    d = os.path.dirname(os.path.abspath(__file__))
    meta = {'argv': sys.argv, 'numpy': np.__version__, 'sha256': {f: sha(os.path.join(d, f)) for f in ('bn_sl.py', 'bn.py', 'ew.py', 'mn.py', 'tp.py')},
            'laufzeit_s': time.time() - t0, 'max_rss_MB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
            'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(t0))}
    with open(a.out + '.neu', 'w') as f:
        json.dump({'meta': meta, 'ergebnis': res}, f, indent=1)
    os.replace(a.out + '.neu', a.out)
    print(json.dumps(meta))


if __name__ == '__main__':
    main()
