#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BETA-NETZ-V (Runde 37, ohne Karte; Finn 05.10.: einfach machen), Code-Agent fuer die Leitung claude-primary.

Nichtlineare Statik auf Finns gefuelltem Netz V (ew.py aus EINE-WELT-LOCH-1 und mn.py aus MATERIE-NETZ-1, beide
unveraendert kopiert und nur importiert).
  H_v(l) = sum_{e an v} l_e eps_e(l)        Eckenregel R1, eps = 2 pi - Summe der exakten Diederwinkel
  G_v    = H_v(l) - sigma_v = 0              Zwang, Punktquelle sigma an einer Ecke (k = 0 wird nicht geloest)
  F_e    = sum_v N_v dH_v/dl_e = 0           statische Gleichung, Takt N = 1 + mu (Materie ruht: kein l in sigma)
Skaliert: R_F = -(l0/2) F (linear: B a - q c mu mit q = 1/2 wie MATERIE-NETZ-1 V1), R_G = G (linear: c^H a);
a = (l - l0)/l0 exakt (keine Linearisierung in der Parametrisierung).
Eichung: M^H (a + q W mu) = 0 -> erste Ordnung a1 = -q W mu1 exakt (isotrope Koordinaten); Rest der Gleichungen in
Eichrichtungen ueber M lam (wie die KKT in mn.py), lam wird berichtet.
Modi:
  test : Schlaefli an krummen Tetraedern, Ebenheit, Linearisierung des exakten Rests gegen die KKT-Bloecke
  pert : erste Ordnung (KKT je k), zweite Ordnung: Q2 = [R(+h x1) + R(-h x1)]/(2 h^2) (Richardson h, 2h), ein Solve
  nl   : volle nichtlineare Loesung je Staerke s (Quasi-Newton mit flacher KKT), mu2 = [mu(s) + mu(-s)]/(2 s^2)
Aufruf nur ueber kleintest.sh auf der .69.
"""
import argparse, json, sys, time, os, math, hashlib, platform, resource
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ew  # noqa: E402
import mn  # noqa: E402

LP, VCELL, Q = mn.LP, mn.VCELL, 0.5
QUELLEN = {'P0': 0, 'C1': 4, 'H0': 6}
PAARE = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
ANDERE = [(2, 3), (1, 3), (1, 2), (0, 3), (0, 2), (0, 1)]
HC = 1e-20


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def cT(X):
    return np.conj(np.swapaxes(X, -1, -2))


# ------------------------------------------------------------------------------------------------ Tetraeder exakt
def dieder_cos(l):
    """l (..., 6) Kantenlaengen in PAARE-Ordnung (komplex erlaubt) -> cos der 6 inneren Diederwinkel."""
    d = l * l
    d01, d02, d03, d12, d13, d23 = (d[..., i] for i in range(6))
    x1 = np.sqrt(d01)
    x2 = (d01 + d02 - d12) / (2 * x1)
    y2 = np.sqrt(d02 - x2 * x2)
    x3 = (d01 + d03 - d13) / (2 * x1)
    y3 = (d02 + d03 - d23 - 2 * x2 * x3) / (2 * y2)
    z3 = np.sqrt(d03 - x3 * x3 - y3 * y3)
    z = np.zeros_like(x1)
    P = [np.stack([z, z, z], -1), np.stack([x1, z, z], -1), np.stack([x2, y2, z], -1), np.stack([x3, y3, z3], -1)]
    out = []
    for (i, j), (k, m) in zip(PAARE, ANDERE):
        e = P[j] - P[i]
        u = P[k] - P[i]
        w = P[m] - P[i]
        ee = (e * e).sum(-1)
        up = u - ((u * e).sum(-1) / ee)[..., None] * e
        wp = w - ((w * e).sum(-1) / ee)[..., None] * e
        out.append((up * wp).sum(-1) / np.sqrt((up * up).sum(-1) * (wp * wp).sum(-1)))
    return np.stack(out, -1)


def dieder_jac(l):
    """theta (..., 6) und J[..., i, j] = d theta_i/d l_j (komplexer Schritt auf cos theta, arccos nur reell)."""
    J = np.empty(l.shape + (6,))
    th = sn = None
    for j in range(6):
        lc = l.astype(complex)
        lc[..., j] += 1j * HC
        c = dieder_cos(lc)
        if th is None:
            th = np.arccos(np.clip(c.real, -1.0, 1.0))
            sn = np.sin(th)
        J[..., :, j] = -c.imag / (HC * sn)
    return th, J


def rollv(X, n):
    """Y[R] = X[R + n]."""
    return np.roll(X, shift=(-n[0], -n[1], -n[2]), axis=(0, 1, 2))


def rollz(X, n):
    """Y[R + n] = X[R]."""
    return np.roll(X, shift=(n[0], n[1], n[2]), axis=(0, 1, 2))


# ------------------------------------------------------------------------------------------------ Netz auf dem Torus
class Netz:
    def __init__(self, L):
        self.mod = mod = ew.baue('V')
        self.L, self.E, self.nV = L, mod['E'], mod['nV']
        self.l0 = np.array(mod['l'], float)
        AVinv = np.linalg.inv(ew.AV)
        self.tets = []
        for z in mod['zellen']:
            assert [tuple(p) for p in z['paare']] == PAARE
            kant = []
            for (e, T) in z['kanten']:
                n = np.rint(np.asarray(T, float) @ AVinv).astype(int)
                assert np.allclose(n @ ew.AV, T)
                kant.append((int(e), tuple(int(x) for x in n)))
            self.tets.append(kant)
        self.kl = [(int(s), int(s2), tuple(int(x) for x in d)) for (s, s2, d) in mod['kliste']]
        g = np.arange(L)
        nn = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1)
        self.kgrid = ((nn / L) @ ew.BV).reshape(-1, 3)
        self.Nk = L ** 3
        self.pos = np.array(mod['pos'], float)
        self.X = (nn @ ew.AV)[..., None, :] + self.pos[None, None, None]
        self.Vtor = L ** 3 * VCELL / LP ** 3

    def r_von(self, v0):
        _, dist = mn.min_bild(self.X - self.pos[v0], self.L)
        return dist / LP

    def hin(self, Xr):
        return np.fft.fftn(Xr, axes=(0, 1, 2)).reshape((self.Nk,) + Xr.shape[3:])

    def zurueck(self, Xk):
        L = self.L
        Xr = np.fft.ifftn(Xk.reshape((L, L, L) + Xk.shape[1:]), axes=(0, 1, 2))
        return Xr.real, float(np.abs(Xr.imag).max() / max(np.abs(Xr.real).max(), 1e-300))

    def rest(self, a, mu, sigma, eps_aus=False):
        """Exakter Rest (R_F, R_G) fuer a (L,L,L,E), mu (L,L,L,nV), sigma (L,L,L,nV)."""
        l = self.l0 * (1.0 + a)
        N = 1.0 + mu
        Nsum = np.empty_like(l)
        for e, (s, s2, d) in enumerate(self.kl):
            Nsum[..., e] = N[..., s] + rollv(N[..., s2], d)
        w = Nsum * l
        thsum = np.zeros_like(l)
        Fk = np.zeros_like(l)
        for kant in self.tets:
            lt = np.stack([rollv(l[..., e], n) for (e, n) in kant], -1)
            wt = np.stack([rollv(w[..., e], n) for (e, n) in kant], -1)
            th, J = dieder_jac(lt)
            g = np.einsum('...i,...ij->...j', wt, J)
            for i, (e, n) in enumerate(kant):
                thsum[..., e] += rollz(th[..., i], n)
                Fk[..., e] -= rollz(g[..., i], n)
        eps = 2 * np.pi - thsum
        F = Nsum * eps + Fk
        RF = -(self.l0 / 2.0) * F
        le = l * eps
        H = np.zeros(N.shape)
        for e, (s, s2, d) in enumerate(self.kl):
            H[..., s] += le[..., e]
            H[..., s2] += rollz(le[..., e], d)
        RG = H - sigma
        if eps_aus:
            return RF, RG, eps
        return RF, RG

    def K_chunk(self, k):
        o = ew.ops(self.mod, k)
        B, M, c = o['B'], o['M'], o['c']
        W = mn.W_of(self.mod, k)
        E, nV = self.E, self.nV
        n = E + 4 * nV
        K = np.zeros(k.shape[:-1] + (n, n), complex)
        K[..., :E, :E] = B
        K[..., :E, E:E + nV] = -Q * c
        K[..., :E, E + nV:] = M
        K[..., E:E + nV, :E] = cT(c)
        K[..., E + nV:, :E] = cT(M)
        K[..., E + nV:, E:E + nV] = Q * (cT(M) @ W)
        return K, M, W, B, c

    def loese(self, bF, bG, chunk=64, zerlege=False):
        """K x = b je k != 0 (b: (Nk, ., nq)); x[0] = 0. Optional a = W psi + M xi + Rest und M lam."""
        E, nV, Nk = self.E, self.nV, self.Nk
        nq = bF.shape[-1]
        n = E + 4 * nV
        x = np.zeros((Nk, n, nq), complex)
        psi = np.zeros((Nk, nV, nq), complex)
        rst = np.zeros((Nk, E, nq), complex)
        mlam = np.zeros((Nk, E, nq), complex)
        wmsv = np.inf
        for i0 in range(1, Nk, chunk):
            idx = np.arange(i0, min(i0 + chunk, Nk))
            K, M, W, B, c = self.K_chunk(self.kgrid[idx])
            rhs = np.zeros((len(idx), n, nq), complex)
            rhs[:, :E] = bF[idx]
            rhs[:, E:E + nV] = bG[idx]
            xi = np.linalg.solve(K, rhs)
            x[idx] = xi
            mlam[idx] = M @ xi[:, E + nV:]
            if zerlege:
                WM = np.concatenate([W, M], -1)
                sv = np.linalg.svd(WM, compute_uv=False)
                wmsv = min(wmsv, float((sv[:, -1] / sv[:, 0]).min()))
                coef = np.linalg.pinv(WM) @ xi[:, :E]
                psi[idx] = coef[:, :nV]
                rst[idx] = xi[:, :E] - WM @ coef
        return x, psi, rst, mlam, wmsv


# ------------------------------------------------------------------------------------------------ Auswertung
def schalen(r, felder, breite=0.5, rmax=None):
    rmax = rmax if rmax is not None else r.max()
    kanten = np.arange(0.0, rmax + 1e-9, breite)
    out = []
    for a0, b0 in zip(kanten[:-1], kanten[1:]):
        s = (r >= a0) & (r < b0)
        if not s.any():
            continue
        z = {'r0': float(a0), 'r1': float(b0), 'n': int(s.sum()), 'r_mittel': float(r[s].mean())}
        for nm, y in felder.items():
            z[nm] = float(y[s].mean())
        out.append(z)
    return out


def fit(r, y, rmin, rmax, terme, breite=0.5):
    """Gewichtete kleinste Quadrate auf Eckebene, jede 0,5-Schale mit gleichem Gesamtgewicht."""
    sel = (r >= rmin) & (r <= rmax)
    rs, ys = r[sel], y[sel]
    sh = np.floor(rs / breite).astype(int)
    _, inv, cnt = np.unique(sh, return_inverse=True, return_counts=True)
    w = 1.0 / np.sqrt(cnt[inv])
    basis = {'1/r': 1 / rs, '1/r2': 1 / rs ** 2, '1': np.ones_like(rs), 'r': rs, 'r2': rs ** 2}
    X = np.stack([basis[t] for t in terme], -1)
    coef, *_ = np.linalg.lstsq(X * w[:, None], ys * w, rcond=None)
    res = ys - X @ coef
    return {t: float(c) for t, c in zip(terme, coef)}, float(np.sqrt(np.mean(res ** 2)) / max(np.abs(ys).mean(), 1e-300)), int(sel.sum())


def auswerten(net, v0, mu1, mu2, psi2=None, extra=None):
    """mu1, mu2, psi2: (L,L,L,nV) reell. Gibt A, Schalen und Fits fuer nu2 = mu2 - mu1^2/2 usw."""
    L = net.L
    r = net.r_von(v0).ravel()
    m1, m2 = mu1.ravel(), mu2.ravel()
    fern = (r >= 0.25 * L) & (r <= 0.5 * L)
    fr = lambda x: -1.0 / x - (2 * np.pi / (3 * net.Vtor)) * x ** 2
    Af = np.stack([fr(r[fern]), np.ones(fern.sum())], -1)
    (A, C), *_ = np.linalg.lstsq(Af, m1[fern], rcond=None)
    nu2 = m2 - 0.5 * m1 ** 2
    felder = {'mu1': m1, 'mu2': m2, 'nu2': nu2}
    if psi2 is not None:
        p1 = -Q * m1
        p2 = psi2.ravel()
        felder.update({'psi2': p2, 'Psi2': p2 - 0.5 * p1 ** 2})
    if extra:
        felder.update({k: v.ravel() for k, v in extra.items()})
    out = {'v0': int(v0), 'A': float(A), 'C': float(C), 'mu_quelle': float(m1[r < 1e-9][0]), 'mu2_quelle': float(m2[r < 1e-9][0]),
           'schalen': schalen(r, felder, rmax=0.5 * L)}
    fits = []
    rmaxs = sorted(set([round(0.25 * L, 3), round(0.375 * L, 3), round(0.5 * L, 3)]))
    modelle = {'M0': ['1/r', '1/r2', '1'], 'M1': ['1/r', '1/r2', '1', 'r'], 'M2': ['1/r', '1/r2', '1', 'r', 'r2']}
    for rmin in (2.0, 3.0, 4.0):
        for rmax in rmaxs:
            if rmax - rmin < 2.0:
                continue
            for mname, terme in modelle.items():
                z = {'rmin': rmin, 'rmax': rmax, 'modell': mname}
                c, rr, n = fit(r, nu2, rmin, rmax, terme)
                z.update({'n': n, 'nu2_koef': c, 'nu2_rest': rr, 'beta_minus_1': c['1/r2'] / A ** 2})
                c2, rr2, _ = fit(r, m2, rmin, rmax, terme)
                z.update({'mu2_koef': c2, 'beta_direkt': 0.5 + c2['1/r2'] / A ** 2})
                if psi2 is not None:
                    c3, rr3, _ = fit(r, felder['Psi2'], rmin, rmax, terme)
                    z.update({'Psi2_koef': c3, 'delta_minus_1': (8.0 / 3.0) * c3['1/r2'] / A ** 2})
                fits.append(z)
    out['fits'] = fits
    return out


# ------------------------------------------------------------------------------------------------ Modi
def modus_test(L, seed=5):
    t0 = time.time()
    net = Netz(L)
    rng = np.random.default_rng(seed)
    out = {'L': L, 'E': net.E, 'nV': net.nV, 'n_tet_typen': len(net.tets)}
    # Schlaefli und Symmetrie an krummen Tetraedern
    smax, symmax = 0.0, 0.0
    for kant in net.tets[:10]:
        l0 = np.array([net.l0[e] for (e, n) in kant])
        lt = l0[None, :] * (1 + 0.05 * rng.normal(size=(50, 6)))
        th, J = dieder_jac(lt)
        smax = max(smax, float(np.abs(np.einsum('...i,...ij->...j', lt, J)).max() / np.abs(J).max()))
        symmax = max(symmax, float(np.abs(J - np.swapaxes(J, -1, -2)).max() / np.abs(J).max()))
    out['schlaefli_lJ_rel_max'] = smax
    out['J_sym_rel_max'] = symmax
    # Ebenheit
    z0 = np.zeros((L, L, L, net.E))
    m0 = np.zeros((L, L, L, net.nV))
    RF, RG, eps = net.rest(z0, m0, m0, eps_aus=True)
    out['eben_eps_max'] = float(np.abs(eps).max())
    out['eben_RF_max'] = float(np.abs(RF).max())
    out['eben_RG_max'] = float(np.abs(RG).max())
    # Linearisierung gegen KKT-Bloecke (alle k inkl. 0)
    a = rng.normal(size=z0.shape)
    mu = rng.normal(size=m0.shape)
    h = 1e-4
    RFp, RGp = net.rest(h * a, h * mu, m0)
    RFm, RGm = net.rest(-h * a, -h * mu, m0)
    linF = net.hin((RFp - RFm) / (2 * h))
    linG = net.hin((RGp - RGm) / (2 * h))
    ak, muk = net.hin(a), net.hin(mu)
    dF, dG, nF, nG = 0.0, 0.0, 0.0, 0.0
    for i0 in range(0, net.Nk, 64):
        idx = np.arange(i0, min(i0 + 64, net.Nk))
        K, M, W, B, c = net.K_chunk(net.kgrid[idx])
        kF = (B @ ak[idx][..., None])[..., 0] - Q * (c @ muk[idx][..., None])[..., 0]
        kG = (cT(c) @ ak[idx][..., None])[..., 0]
        dF = max(dF, float(np.abs(linF[idx] - kF).max()))
        dG = max(dG, float(np.abs(linG[idx] - kG).max()))
        nF = max(nF, float(np.abs(kF).max()))
        nG = max(nG, float(np.abs(kG).max()))
    out['lin_F_rel'] = dF / nF
    out['lin_G_rel'] = dG / nG
    # zweite Ordnung: Symmetrie der Differenzen (Groesse)
    out['zeit_s'] = time.time() - t0
    return out


def erste_ordnung(net, quellen):
    nq = len(quellen)
    sig = np.zeros((net.L, net.L, net.L, net.nV, nq))
    for j, v0 in enumerate(quellen):
        sig[0, 0, 0, v0, j] = 1.0
    bG = net.hin(sig)
    bF = np.zeros((net.Nk, net.E, nq), complex)
    x1, _, _, mlam1, _ = net.loese(bF, bG)
    E, nV = net.E, net.nV
    a1, im1 = net.zurueck(x1[:, :E])
    mu1, im2 = net.zurueck(x1[:, E:E + nV])
    lam1 = float(np.abs(x1[:, E + nV:]).max())
    return sig, a1, mu1, lam1, max(im1, im2)


def zweite_quelle(net, a1, mu1, sig, h):
    RFp, RGp = net.rest(h * a1, h * mu1, h * sig)
    RFm, RGm = net.rest(-h * a1, -h * mu1, -h * sig)
    q2F, q2G = (RFp + RFm) / (2 * h * h), (RGp + RGm) / (2 * h * h)
    oF, oG = (RFp - RFm) / (2 * h), (RGp - RGm) / (2 * h)
    oF = oF - oF.mean(axis=(0, 1, 2))
    oG = oG - oG.mean(axis=(0, 1, 2))
    return q2F, q2G, float(np.abs(oF).max()), float(np.abs(oG).max())


def modus_pert(L, namen, h=1e-2):
    t0 = time.time()
    net = Netz(L)
    quellen = [QUELLEN[n] for n in namen]
    nq = len(quellen)
    E, nV = net.E, net.nV
    sig, a1, mu1, lam1, im1 = erste_ordnung(net, quellen)
    t1 = time.time()
    out = {'L': L, 'E': E, 'nV': nV, 'Vtor_lP3': net.Vtor, 'h': h, 'quellen': namen,
           'kontrollen': {'lam1_max': lam1, 'imag1_rel': im1}}
    # isotrope Eichung: a1 = -q W mu1 je Kante
    iso = 0.0
    for e, (s, s2, d) in enumerate(net.kl):
        soll = -Q * (mu1[..., s, :] + rollv(mu1[..., s2, :], d))
        iso = max(iso, float(np.abs(a1[..., e, :] - soll).max()))
    out['kontrollen']['a1_minus_qWmu1_max'] = iso
    out['kontrollen']['a1_max'] = float(np.abs(a1).max())
    Q2F = np.zeros((L, L, L, E, nq))
    Q2G = np.zeros((L, L, L, nV, nq))
    rich = []
    for j in range(nq):
        f1, g1, oF1, oG1 = zweite_quelle(net, a1[..., j], mu1[..., j], sig[..., j], h)
        f2, g2, oF2, oG2 = zweite_quelle(net, a1[..., j], mu1[..., j], sig[..., j], 2 * h)
        Q2F[..., j] = (4 * f1 - f2) / 3
        Q2G[..., j] = (4 * g1 - g2) / 3
        rich.append({'quelle': namen[j], 'richardson_F_rel': float(np.abs(f1 - f2).max() / np.abs(Q2F[..., j]).max()),
                     'richardson_G_rel': float(np.abs(g1 - g2).max() / np.abs(Q2G[..., j]).max()),
                     'ungerade_rest_F_h': oF1, 'ungerade_rest_G_h': oG1, 'ungerade_rest_F_2h': oF2, 'ungerade_rest_G_2h': oG2,
                     'Q2F_max': float(np.abs(Q2F[..., j]).max()), 'Q2G_max': float(np.abs(Q2G[..., j]).max())})
    out['kontrollen']['zweite_quelle'] = rich
    t2 = time.time()
    x2, psi2k, rst2k, mlam2k, wmsv = net.loese(-net.hin(Q2F), -net.hin(Q2G), zerlege=True)
    t3 = time.time()
    a2, im_a = net.zurueck(x2[:, :E])
    mu2, im_m = net.zurueck(x2[:, E:E + nV])
    psi2, im_p = net.zurueck(psi2k)
    rst2, _ = net.zurueck(rst2k)
    mlam2, _ = net.zurueck(mlam2k)
    lam2, _ = net.zurueck(x2[:, E + nV:])
    out['kontrollen'].update({'imag2_rel': max(im_a, im_m, im_p), 'WM_sv_rel_min': wmsv})
    res = {}
    for j, nm in enumerate(namen):
        v0 = quellen[j]
        # Kantenmitten-Abstand fuer kantenbezogene Groessen
        rkan = np.zeros((L, L, L, E))
        rv = net.r_von(v0)
        for e, (s, s2, d) in enumerate(net.kl):
            rkan[..., e] = 0.5 * (rv[..., s] + rollv(rv[..., s2], d))
        Q2Fz = Q2F[..., j] - Q2F[..., j].mean(axis=(0, 1, 2))
        kan = {'Q2F_abs': np.abs(Q2Fz), 'Mlam2_abs': np.abs(mlam2[..., j]), 'rest2_abs': np.abs(rst2[..., j]),
               'a2_abs': np.abs(a2[..., j]), 'a2': a2[..., j], 'a1': a1[..., j]}
        z = auswerten(net, v0, mu1[..., j], mu2[..., j], psi2[..., j])
        z['kanten_schalen'] = schalen(rkan.ravel(), {k: v.ravel() for k, v in kan.items()}, breite=1.0, rmax=0.5 * L)
        lv = np.linalg.norm(lam2[..., j].reshape(L, L, L, nV, 3), axis=-1)
        z['lam2_ecke_schalen'] = schalen(rv.ravel(), {'lam2_betrag': lv.ravel()}, breite=1.0, rmax=0.5 * L)
        z['Mlam2_ueber_Q2F_gesamt'] = float(np.linalg.norm(mlam2[..., j]) / np.linalg.norm(Q2Fz))
        z['rest2_ueber_a2_gesamt'] = float(np.linalg.norm(rst2[..., j]) / np.linalg.norm(a2[..., j]))
        res[nm] = z
    out['quellen_aus'] = res
    out['zeiten_s'] = {'erste': t1 - t0, 'quelle2': t2 - t1, 'solve2': t3 - t2, 'gesamt': time.time() - t0}
    return out, (mu1, mu2, psi2)


def modus_nl(L, name, staerken, tol=1e-13, maxit=60, h=1e-2):
    t0 = time.time()
    net = Netz(L)
    v0 = QUELLEN[name]
    E, nV, Nk = net.E, net.nV, net.Nk
    n = E + 4 * nV
    Kinv = np.zeros((Nk, n, n), complex)
    Ms = np.zeros((Nk, E, 3 * nV), complex)
    MHW = np.zeros((Nk, 3 * nV, nV), complex)
    for i0 in range(1, Nk, 64):
        idx = np.arange(i0, min(i0 + 64, Nk))
        K, M, W, B, c = net.K_chunk(net.kgrid[idx])
        Kinv[idx] = np.linalg.inv(K)
        Ms[idx] = M
        MHW[idx] = cT(M) @ W
    tK = time.time() - t0
    sig1 = np.zeros((L, L, L, nV))
    sig1[0, 0, 0, v0] = 1.0
    rhs = np.zeros((Nk, n), complex)
    rhs[:, E:E + nV] = net.hin(sig1)
    rhs[0] = 0
    x1 = (Kinv @ rhs[..., None])[..., 0]
    a1, _ = net.zurueck(x1[:, :E])
    mu1, _ = net.zurueck(x1[:, E:E + nV])
    laeufe = {}
    for s in staerken:
        a, mu = s * a1, s * mu1
        lam = np.zeros((Nk, 3 * nV), complex)
        verlauf = []
        for it in range(maxit):
            RF, RG = net.rest(a, mu, s * sig1)
            Fk = net.hin(RF) + (Ms @ lam[..., None])[..., 0]
            Gk = net.hin(RG)
            Ek = (cT(Ms) @ net.hin(a)[..., None])[..., 0] + Q * (MHW @ net.hin(mu)[..., None])[..., 0]
            rr = np.concatenate([Fk, Gk, Ek], -1)
            rr[0] = 0
            dx = -(Kinv @ rr[..., None])[..., 0]
            da, _ = net.zurueck(dx[:, :E])
            dmu, _ = net.zurueck(dx[:, E:E + nV])
            lam += dx[:, E + nV:]
            a += da
            mu += dmu
            fr_ = float(np.abs(rr[1:, :E]).max()) / Nk
            gr_ = float(np.abs(rr[1:, E:E + nV]).max()) / Nk
            schritt = float(max(np.abs(da).max(), np.abs(dmu).max()))
            verlauf.append([it, fr_, gr_, schritt])
            if schritt < tol:
                break
        lr, _ = net.zurueck(lam)
        laeufe[s] = {'mu': mu.copy(), 'a': a.copy(), 'lam_max': float(np.abs(lr).max()), 'verlauf': verlauf,
                     'mu_quelle': float(mu[0, 0, 0, v0]), 'a_max': float(np.abs(a).max())}
    tN = time.time() - t0 - tK
    out = {'L': L, 'quelle': name, 'staerken': staerken, 'tol': tol, 'zeiten_s': {'Kinv': tK, 'iteration': tN}}
    out['laeufe'] = {str(s): {k: v for k, v in z.items() if k not in ('mu', 'a')} for s, z in laeufe.items()}
    # zweite Ordnung aus den Staerken: symmetrisch, Richardson
    pos = sorted(s for s in staerken if s > 0)
    m2 = {}
    for s in pos:
        if -s in laeufe:
            m2[s] = (laeufe[s]['mu'] + laeufe[-s]['mu']) / (2 * s * s)
    out['mu2_aus_staerken'] = {}
    if len(pos) >= 2:
        s1, s2 = pos[0], pos[1]
        r_ = (s2 / s1) ** 2
        mu2R = (r_ * m2[s1] - m2[s2]) / (r_ - 1)
        out['mu2_aus_staerken']['richardson_aus'] = [s1, s2]
    else:
        mu2R = m2[pos[0]]
    for s in m2:
        out['mu2_aus_staerken'][str(s)] = {'abw_zu_R_rel': float(np.abs(m2[s] - mu2R).max() / np.abs(mu2R).max())}
        ung = (laeufe[s]['mu'] - laeufe[-s]['mu']) / (2 * s)
        out['mu2_aus_staerken'][str(s)]['ungerade_minus_mu1_rel'] = float(np.abs(ung - mu1).max() / np.abs(mu1).max())
    # Vergleich mit der Stoerungsrechnung am selben Netz
    sig, a1p, mu1p, _, _ = erste_ordnung(net, [v0])
    f1, g1, _, _ = zweite_quelle(net, a1p[..., 0], mu1p[..., 0], sig[..., 0], h)
    f2, g2, _, _ = zweite_quelle(net, a1p[..., 0], mu1p[..., 0], sig[..., 0], 2 * h)
    x2, _, _, _, _ = net.loese(-net.hin(((4 * f1 - f2) / 3)[..., None]), -net.hin(((4 * g1 - g2) / 3)[..., None]))
    mu2p, _ = net.zurueck(x2[:, E:E + nV, 0])
    rv = net.r_von(v0)
    d = np.abs(mu2R - mu2p)
    out['vergleich_pert'] = {'max_abw_rel': float(d.max() / np.abs(mu2p).max()),
                             'schalen': schalen(rv.ravel(), {'mu2_nl': mu2R.ravel(), 'mu2_pert': mu2p.ravel(),
                                                             'abw_abs': d.ravel()}, breite=1.0, rmax=0.5 * L)}
    out['auswertung_nl'] = auswerten(net, v0, mu1, mu2R)
    out['zeiten_s']['gesamt'] = time.time() - t0
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['test', 'pert', 'nl'])
    ap.add_argument('--L', type=int, default=8)
    ap.add_argument('--quellen', nargs='+', default=['P0'])
    ap.add_argument('--staerken', nargs='+', type=float, default=[0.25, -0.25, 0.5, -0.5])
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    if a.modus == 'test':
        res = modus_test(a.L)
    elif a.modus == 'pert':
        res, _ = modus_pert(a.L, a.quellen)
    else:
        res = modus_nl(a.L, a.quellen[0], a.staerken)
    meta = {'modus': a.modus, 'argv': sys.argv, 'python': platform.python_version(), 'numpy': np.__version__,
            'sha256': {f: sha(os.path.join(os.path.dirname(os.path.abspath(__file__)), f)) for f in ('bn.py', 'ew.py', 'mn.py', 'tp.py')},
            'laufzeit_s': time.time() - t0, 'max_rss_MB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
            'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(t0))}
    with open(a.out, 'w') as f:
        json.dump({'meta': meta, 'ergebnis': res}, f, indent=1)
    print(json.dumps(meta))


if __name__ == '__main__':
    main()
