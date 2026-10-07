#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MATERIE-NETZ-1, Nachtrag nach dem Einfrieren (beschreibend, kein Urteil). Geschrieben nach Sicht der Hauptlaeufe.

Frage: Kommen die Abweichungen von gamma_K (Zusatzlesart K) vom Gitter-Takt oder von der Referenz?
Zwei Referenzen fuer die Fehlwinkel der Metrik mit gamma = 1 (A, C aus dem Fernfit wie mn.py, gleiches Band):
  R_L (wie mn.py, eingefroren): a_ref = -(Linienmittel von f laengs der Kante)
  R_E (neu): a_ref = -(f(r_v) + f(r_w))/2, Kontinuum-Potential an den Ecken, also dieselbe Eck-Diskretisierung wie die
       Loesung (a_hat = -W mu).
Dazu je Ecke mit r < 3 das Newton-Verhaeltnis (mu_v - C)/(A f(r_v)) nach Untergitter.
mu aus der Formel mu = -P^{-1} m (in mn.py gegen das KKT-System auf <= 3e-13 geprueft); Fehlwinkel der Loesung bei
Einheitskopplung d_eps = (B W mu)/l. mn.py und ew.py werden unveraendert importiert.
"""
import argparse, json, os, sys, time, hashlib, resource
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ew  # noqa: E402
import mn  # noqa: E402  (eingefroren b36984d3...)


def sha(p):
    with open(p, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--L', type=int, default=24)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    L = a.L
    t0 = time.time()
    mod = ew.baue('V')
    E, nV = mod['E'], mod['nV']
    lv = mod['l']
    pos = np.array(mod['pos'])
    Vtor = L ** 3 * mn.VCELL / mn.LP ** 3
    g = np.arange(L)
    nn = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1)
    Rcell = nn @ ew.AV
    kgrid = ((nn / L) @ ew.BV).reshape(-1, 3)
    N = L ** 3
    X = Rcell[..., None, :] + pos[None, None, None]
    f = lambda x: -1.0 / x - (2 * np.pi / (3 * Vtor)) * x ** 2
    punkt = [(nm, v0) for nm, v0, art in mn.QUELLEN if art == 'punkt']
    npk = len(punkt)
    mk = np.zeros((N, nV, npk), complex)
    refL = np.zeros((N, E, npk), complex)
    refE = np.zeros((N, E, npk), complex)
    rv, rmid = {}, {}
    for j, (nm, v0) in enumerate(punkt):
        x0 = pos[v0]
        _, dist = mn.min_bild(X - x0, L)
        rv[nm] = dist / mn.LP
        m = np.zeros((L, L, L, nV))
        m[0, 0, 0, v0] = 1.0
        mk[:, :, j] = np.fft.fftn(m, axes=(0, 1, 2)).reshape(N, nV)
        aL = np.zeros((L, L, L, E))
        aE = np.zeros((L, L, L, E))
        rm = np.zeros((L, L, L, E))
        for e, (s, s2, n2) in enumerate(mod['kliste']):
            dvec = pos[s2] + mod['T'][e] - pos[s]
            mid = Rcell + pos[s] + 0.5 * dvec
            dm, nm_ = mn.min_bild(mid - x0, L)
            p = (dm - 0.5 * dvec) / mn.LP
            d = np.broadcast_to(dvec / mn.LP, p.shape)
            r1 = np.linalg.norm(p, axis=-1)
            r2 = np.linalg.norm(p + d, axis=-1)
            ber = (r1 < 1e-9) | (r2 < 1e-9)
            with np.errstate(divide='ignore', invalid='ignore'):
                vL = mn.zeile_mittel_1r(p, d) + (2 * np.pi / (3 * Vtor)) * mn.zeile_mittel_r2(p, d)
                vE = -0.5 * (f(r1) + f(r2))
            vL[ber] = 0.0
            vE[ber] = 0.0
            aL[..., e] = vL
            aE[..., e] = vE
            rm[..., e] = nm_ / mn.LP
        rmid[nm] = rm
        refL[:, :, j] = np.fft.fftn(aL, axes=(0, 1, 2)).reshape(N, E)
        refE[:, :, j] = np.fft.fftn(aE, axes=(0, 1, 2)).reshape(N, E)
    muk = np.zeros((N, nV, npk), complex)
    de = np.zeros((N, E, npk), complex)
    dL = np.zeros((N, E, npk), complex)
    dE = np.zeros((N, E, npk), complex)
    for i0 in range(1, N, 128):
        idx = np.arange(i0, min(i0 + 128, N))
        k = kgrid[idx]
        o = ew.ops(mod, k)
        B = o['B']
        W = mn.W_of(mod, k)
        P = -mn.cT(W) @ B @ W
        P = 0.5 * (P + mn.cT(P))
        mu = -np.linalg.solve(P, mk[idx])
        muk[idx] = mu
        de[idx] = (B @ (W @ mu)) / lv[None, :, None]
        dL[idx] = -(B @ refL[idx]) / lv[None, :, None]
        dE[idx] = -(B @ refE[idx]) / lv[None, :, None]

    def back(Z):
        return np.fft.ifftn(Z.reshape((L, L, L) + Z.shape[1:]), axes=(0, 1, 2)).real
    mur, der, dLr, dEr = back(muk), back(de), back(dL), back(dE)
    out = {'L': L, 'quellen': {}}
    rf1, rf2 = 0.25 * L, 0.5 * L
    for j, (nm, v0) in enumerate(punkt):
        r = rv[nm].ravel()
        mu = mur[..., j].ravel()
        sub = np.broadcast_to(np.arange(nV), (L, L, L, nV)).ravel()
        fern = (r >= rf1) & (r <= rf2)
        Af = np.stack([f(r[fern]), np.ones(fern.sum())], -1)
        (A, C), *_ = np.linalg.lstsq(Af, mu[fern], rcond=None)
        z = {'A': float(A), 'C': float(C)}
        s3 = (r > 0) & (r < 3.0)
        z['G_ratio_ecken_r_lt_3'] = [[int(u), round(float(x), 4), round(float((y - C) / (A * f(x))), 5)] for u, x, y in zip(sub[s3], r[s3], mu[s3])]
        rm = rmid[nm].ravel()
        d0 = der[..., j].ravel()
        for tag, dr_ in (('R_L', dLr[..., j].ravel()), ('R_E', dEr[..., j].ravel())):
            sch = []
            kk = np.arange(1.5, rf2 + 1e-9, 0.5)
            for a0, b0 in zip(kk[:-1], kk[1:]):
                s = (rm >= a0) & (rm < b0)
                if not s.any():
                    continue
                num, den = float((d0[s] * dr_[s]).sum()), float((dr_[s] ** 2).sum())
                gross = s & (np.abs(dr_) >= 0.3 * np.abs(dr_[s]).max())
                einz = 0.5 * d0[gross] / (A * dr_[gross])
                sch.append([float(a0), int(s.sum()), round(0.5 * num / (A * den), 5), round(float(einz.min()), 4), round(float(einz.max()), 4)])
            z['gamma_K_' + tag + '_schalen'] = sch
        out['quellen'][nm] = z
    out['spalten_schalen'] = ['r0', 'n_kanten', 'gamma_K (V1, Schalen-Steigung)', 'Einzelkanten min', 'Einzelkanten max']
    out['spalten_ecken'] = ['Untergitter', 'r/l_P', '(mu - C)/(A f(r))']
    out['info'] = {'skript_sha256': sha(os.path.abspath(__file__)), 'mn_sha256': sha(os.path.abspath(mn.__file__)),
                   'ew_sha256': sha(os.path.abspath(ew.__file__)), 'laufzeit_s': time.time() - t0,
                   'maxrss_MB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0}
    with open(a.out + '.tmp', 'w') as fh:
        json.dump(out, fh, indent=1)
    os.replace(a.out + '.tmp', a.out)
    print('fertig nachtrag_gk L=%d laufzeit %.1f s' % (L, out['info']['laufzeit_s']), flush=True)


if __name__ == '__main__':
    main()
