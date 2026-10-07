#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TENSOR-EIS-0, Runde 35 (fmhc-physics), Code-Agent.

Mindestnorm-Loesung des Tensor-Gauss-Gesetzes auf dem periodischen kubischen Gitter, je Wellenvektor
per Pseudoinverse (numpy.linalg.pinv), OHNE Benutzung der Schreibtischformeln der Karte.

Gitter (gestaffelt, Yee-artig, offengelegt im PLAN):
  E_xx, E_yy, E_zz auf Knoten n; E_xy auf Plakette n+(1/2,1/2,0); E_yz auf n+(0,1/2,1/2); E_zx auf n+(1/2,0,1/2).
  Vektorladung rho_j auf dem j-Link n + e_j/2; Skalarladung auf dem Knoten n.
  Ableitung = Differenz naechster Nachbarn im Abstand 1 (zentriert auf dem Zwischenort),
  Fourier-Symbol i*k_i mit k_i = 2 sin(q_i/2) (physikalische FT mit Ort n+delta).
Energie F = (K/2) sum_n sum_ij E_ij^2 (Frobenius, Nebendiagonale doppelt), K = 1, |p| = 1.
q = 0 wird nicht geloest (pinv der Nullmatrix = 0): gleichfoermiger Neutralisierungshintergrund.

Aufrufe:
  te0.py rauch    --out X.json
  te0.py explizit --L 64 --out X.json
  te0.py kern     --L 128 [--L 192 ...] --out X.json
  te0.py pinch    --out X.json --npz Y.npz
"""
import argparse, json, sys, time, platform, os, resource
import numpy as np

S2 = 1.0 / np.sqrt(2.0)
S6 = 1.0 / np.sqrt(6.0)
KOMP = ['xx', 'yy', 'zz', 'xy', 'yz', 'zx']
IDX = {'xx': (0, 0), 'yy': (1, 1), 'zz': (2, 2), 'xy': (0, 1), 'yz': (1, 2), 'zx': (2, 0)}
GEW = {'xx': 1.0, 'yy': 1.0, 'zz': 1.0, 'xy': 2.0, 'yz': 2.0, 'zx': 2.0}
DELTA = {'xx': (0., 0., 0.), 'yy': (0., 0., 0.), 'zz': (0., 0., 0.),
         'xy': (.5, .5, 0.), 'yz': (0., .5, .5), 'zx': (.5, 0., .5)}
LINK = [(.5, 0., 0.), (0., .5, 0.), (0., 0., .5)]


def basis5():
    """Orthonormalbasis (Frobenius) der symmetrischen spurfreien 3x3-Matrizen."""
    B = np.zeros((5, 3, 3))
    B[0, 0, 1] = B[0, 1, 0] = S2          # xy
    B[1, 1, 2] = B[1, 2, 1] = S2          # yz
    B[2, 2, 0] = B[2, 0, 2] = S2          # zx
    B[3, 0, 0] = S2; B[3, 1, 1] = -S2     # (xx - yy)/sqrt2
    B[4, 0, 0] = S6; B[4, 1, 1] = S6; B[4, 2, 2] = -2 * S6
    return B


def basis6():
    """Orthonormalbasis (Frobenius) der symmetrischen 3x3-Matrizen (ohne Spurbedingung)."""
    B = np.zeros((6, 3, 3))
    B[0, 0, 0] = 1; B[1, 1, 1] = 1; B[2, 2, 2] = 1
    B[3, 0, 1] = B[3, 1, 0] = S2
    B[4, 1, 2] = B[4, 2, 1] = S2
    B[5, 2, 0] = B[5, 0, 2] = S2
    return B


def gram_abw(B):
    G = np.einsum('aij,bij->ab', B, B)
    return float(np.abs(G - np.eye(len(B))).max())


def vek_matrix(k, B):
    """Gauss-Gesetz sum_i (i k_i) E_ij = rho_j mit E = sum_a e_a B_a: A = i*Bm, Bm[j,a] = sum_i k_i B_a[i,j]."""
    return np.einsum('...i,aij->...ja', k, B)


def skal_zeile(k, B):
    """sum_ij (i k_i)(i k_j) E_ij = rho: Zeile b_a = -sum_ij k_i k_j B_a[i,j]."""
    return -np.einsum('...i,...j,aij->...a', k, k, B)[..., None, :]


def kvek(qx, qy, qz):
    return np.stack([2 * np.sin(qx / 2), 2 * np.sin(qy / 2), 2 * np.sin(qz / 2)], axis=-1)


# ---------------------------------------------------------------- Geometrie (vor dem Einfrieren festgelegt)
RICHTUNGEN = [(0, 0, 1), (1, 0, 4), (1, 0, 3), (1, 0, 2), (1, 1, 2), (1, 0, 1), (1, 1, 1), (2, 0, 1),
              (2, 1, 1), (2, 2, 1), (3, 0, 1), (4, 0, 1), (1, 0, 0), (1, 1, 0), (2, 1, 0)]


def vek_par():
    S = set()
    for d in RICHTUNGEN:
        dn = np.array(d, float) / np.linalg.norm(d)
        for r in range(2, 17):
            v = tuple(int(x) for x in np.rint(r * dn))
            if 1.5 <= np.linalg.norm(v) <= 16.5:
                S.add(v)
    return sorted(S, key=lambda v: (round(float(np.linalg.norm(v)), 9), v))


VEK_ANTI = [(0, 0, 2), (0, 0, 4), (0, 0, 8), (0, 0, 16), (2, 0, 0), (4, 0, 0), (8, 0, 0), (16, 0, 0),
            (2, 2, 2), (4, 4, 4), (8, 8, 8)]
VEK_SENK = [tuple(m * c for c in d) for d in [(1, 0, 1), (1, 0, -1), (1, 0, 0), (0, 0, 1), (0, 1, 0), (1, 1, 1)]
            for m in (2, 4, 8)]
VEK_SKAL = [(m, 0, 0) for m in range(1, 17)] + [(m, m, 0) for m in range(1, 12)] + [(m, m, m) for m in range(1, 10)]
VEK_KONTR6 = [(0, 0, 2), (0, 0, 8), (8, 0, 0), (2, 2, 2), (3, 0, 4), (0, 0, 16)]
VEK_SKAL5 = [(1, 0, 0), (4, 0, 0), (8, 0, 0), (16, 0, 0), (4, 4, 0), (5, 5, 5)]


def div_vek(E):
    r = np.roll
    xx, yy, zz, xy, yz, zx = (E[c] for c in KOMP)
    rx = (r(xx, -1, 0) - xx) + (xy - r(xy, 1, 1)) + (zx - r(zx, 1, 2))
    ry = (xy - r(xy, 1, 0)) + (r(yy, -1, 1) - yy) + (yz - r(yz, 1, 2))
    rz = (zx - r(zx, 1, 0)) + (yz - r(yz, 1, 1)) + (r(zz, -1, 2) - zz)
    return rx, ry, rz


def divdiv(E):
    r = np.roll
    xx, yy, zz, xy, yz, zx = (E[c] for c in KOMP)
    s = (r(xx, -1, 0) - 2 * xx + r(xx, 1, 0)) + (r(yy, -1, 1) - 2 * yy + r(yy, 1, 1)) + (r(zz, -1, 2) - 2 * zz + r(zz, 1, 2))

    def dd(a, a1, a2):
        return a - r(a, 1, a1) - r(a, 1, a2) + r(r(a, 1, a1), 1, a2)
    return s + 2 * (dd(xy, 0, 1) + dd(yz, 1, 2) + dd(zx, 2, 0))


class Explizit:
    def __init__(self, L):
        self.L = L; self.N = L ** 3
        q1 = 2 * np.pi * np.fft.fftfreq(L)
        self.q = np.meshgrid(q1, q1, q1, indexing='ij')
        self.k = kvek(*self.q)
        self.B5 = basis5(); self.B6 = basis6()
        t = time.time()
        self.Pv = np.linalg.pinv(vek_matrix(self.k, self.B5))                  # (L,L,L,5,3)
        Bm6 = vek_matrix(self.k, self.B6)                                         # (L,L,L,3,6)
        tr = np.broadcast_to(np.array([1., 1., 1., 0., 0., 0.]), Bm6.shape[:-2] + (1, 6))
        self.Pv6 = np.linalg.pinv(np.concatenate([Bm6, tr], axis=-2))           # (L,L,L,6,4)
        self.Ps6 = np.linalg.pinv(skal_zeile(self.k, self.B6))                  # (L,L,L,6,1)
        self.Ps5 = np.linalg.pinv(skal_zeile(self.k, self.B5))                  # (L,L,L,5,1)
        self.t_pinv = time.time() - t
        # q = 0: Gauss-Spalten muessen 0 sein (die Spurzeile der 6er-Kontrolle ist dort nicht null, Rhs aber 0)
        self.pinv_q0 = float(max(np.abs(self.Pv[0, 0, 0]).max(), np.abs(self.Pv6[0, 0, 0][:, :3]).max(),
                                 np.abs(self.Ps6[0, 0, 0]).max(), np.abs(self.Ps5[0, 0, 0]).max()))
        self.phase = {c: np.exp(1j * (self.q[0] * d[0] + self.q[1] * d[1] + self.q[2] * d[2])) for c, d in DELTA.items()}

    def welle(self, P):
        return np.exp(-1j * (self.q[0] * P[0] + self.q[1] * P[1] + self.q[2] * P[2]))

    def realraum(self, e, B):
        E = {}; im = 0.0
        for c in KOMP:
            i, j = IDX[c]
            x = np.fft.ifftn(np.einsum('...a,a->...', e, B[:, i, j]) * self.phase[c])
            im = max(im, float(np.abs(x.imag).max()))
            E[c] = x.real
        return E, im

    def energie(self, E):
        return 0.5 * sum(GEW[c] * float((E[c] ** 2).sum()) for c in KOMP)

    def vektor(self, ladungen, variante=5):
        rho = np.zeros(self.k.shape, complex)
        for j, n, w in ladungen:
            rho[..., j] += w * self.welle(np.asarray(n, float) + np.asarray(LINK[j]))
        if variante == 5:
            e = -1j * np.einsum('...aj,...j->...a', self.Pv, rho); B = self.B5
        else:
            rhs = np.concatenate([-1j * rho, np.zeros(rho.shape[:-1] + (1,), complex)], axis=-1)
            e = np.einsum('...aj,...j->...a', self.Pv6, rhs); B = self.B6
        Fq = 0.5 * float((np.abs(e) ** 2).sum()) / self.N
        E, im = self.realraum(e, B)
        F = self.energie(E)
        soll = [np.zeros((self.L,) * 3) for _ in range(3)]
        for j, n, w in ladungen:
            soll[j][tuple(int(x) % self.L for x in n)] += w
        div = div_vek(E)
        gres = max(float(np.abs(d - (s - s.sum() / self.N)).max()) for d, s in zip(div, soll))
        spur = float(np.abs(E['xx'] + E['yy'] + E['zz']).max())
        emax = max(float(np.abs(E[c]).max()) for c in KOMP)
        return {'F': F, 'F_parseval': Fq, 'imag_max': im, 'gauss_res': gres, 'spur_res': spur, 'E_max': emax}, E

    def skalar(self, ladungen, variante=6):
        rho = np.zeros(self.k.shape[:-1], complex)
        for n, w in ladungen:
            rho += w * self.welle(np.asarray(n, float))
        P, B = (self.Ps6, self.B6) if variante == 6 else (self.Ps5, self.B5)
        e = P[..., :, 0] * rho[..., None]
        Fq = 0.5 * float((np.abs(e) ** 2).sum()) / self.N
        E, im = self.realraum(e, B)
        F = self.energie(E)
        soll = np.zeros((self.L,) * 3)
        for n, w in ladungen:
            soll[tuple(int(x) % self.L for x in n)] += w
        gres = float(np.abs(divdiv(E) - (soll - soll.sum() / self.N)).max())
        spur = float(np.abs(E['xx'] + E['yy'] + E['zz']).max())
        emax = max(float(np.abs(E[c]).max()) for c in KOMP)
        return {'F': F, 'F_parseval': Fq, 'imag_max': im, 'gauss_res': gres, 'spur_res': spur, 'E_max': emax}, E

    def kern_zz(self):
        Mzz = np.einsum('...a,...a->...', self.Pv[..., :, 2], self.Pv[..., :, 2])
        G = np.fft.ifftn(Mzz)
        return G.real, float(np.abs(G.imag).max())


def lauf_explizit(L, nur=None):
    t0 = time.time()
    X = Explizit(L)
    out = {'L': L, 't_pinv_s': X.t_pinv, 'pinv_q0_max': X.pinv_q0,
           'gram5': gram_abw(X.B5), 'gram6': gram_abw(X.B6), 'records': []}
    rec = out['records']
    # Einzelladungen (Selbstenergien inkl. Hintergrund)
    e1z, _ = X.vektor([(2, (0, 0, 0), 1.0)])
    e1x, _ = X.vektor([(0, (0, 0, 0), 1.0)])
    es6, _ = X.skalar([((0, 0, 0), 1.0)], 6)
    es5, _ = X.skalar([((0, 0, 0), 1.0)], 5)
    out['einzel'] = {'vz': e1z, 'vx': e1x, 's6': es6, 's5': es5}
    par = vek_par() if nur is None else nur.get('par', [])
    for v in par:
        d, _ = X.vektor([(2, (0, 0, 0), 1.0), (2, v, 1.0)])
        d.update({'typ': 'vek_par', 'v': list(v), 's': list(map(float, v)), 'U': d['F'] - 2 * e1z['F']})
        rec.append(d)
    for v in (VEK_ANTI if nur is None else nur.get('anti', [])):
        d, _ = X.vektor([(2, (0, 0, 0), 1.0), (2, v, -1.0)])
        d.update({'typ': 'vek_anti', 'v': list(v), 's': list(map(float, v)), 'U': d['F'] - 2 * e1z['F']})
        rec.append(d)
    for v in (VEK_SENK if nur is None else nur.get('senk', [])):
        d, _ = X.vektor([(2, (0, 0, 0), 1.0), (0, v, 1.0)])
        s = (np.asarray(v, float) + np.asarray(LINK[0]) - np.asarray(LINK[2])).tolist()
        d.update({'typ': 'vek_senk', 'v': list(v), 's': s, 'U': d['F'] - e1z['F'] - e1x['F']})
        rec.append(d)
    for v in (VEK_KONTR6 if nur is None else nur.get('kontr6', [])):
        d5, E5 = X.vektor([(2, (0, 0, 0), 1.0), (2, v, 1.0)], 5)
        d6, E6 = X.vektor([(2, (0, 0, 0), 1.0), (2, v, 1.0)], 6)
        dE = max(float(np.abs(E5[c] - E6[c]).max()) for c in KOMP)
        d6.update({'typ': 'vek_par_6dof_spurzeile', 'v': list(v), 's': list(map(float, v)),
                   'F5': d5['F'], 'max_abs_E5_minus_E6': dE})
        rec.append(d6)
    for v in (VEK_SKAL if nur is None else nur.get('skal', [])):
        for sgn, typ in ((-1.0, 'skal_ungleich'), (1.0, 'skal_gleich')):
            d, _ = X.skalar([((0, 0, 0), 1.0), (v, sgn)], 6)
            d.update({'typ': typ, 'v': list(v), 's': list(map(float, v)), 'U': d['F'] - 2 * es6['F'], 'variante': 6})
            rec.append(d)
    for v in (VEK_SKAL5 if nur is None else nur.get('skal5', [])):
        d, _ = X.skalar([((0, 0, 0), 1.0), (v, -1.0)], 5)
        d.update({'typ': 'skal_ungleich_5dof', 'v': list(v), 's': list(map(float, v)), 'U': d['F'] - 2 * es5['F'], 'variante': 5})
        rec.append(d)
    # Kreuzprobe Kernweg (gleiche pinv, Parseval) fuer parallele Ladungen
    G, gim = X.kern_zz()
    out['kern_imag_max'] = gim
    dmax = 0.0
    for d in rec:
        if d['typ'] == 'vek_par':
            v = d['v']
            d['U_kern'] = float(G[v[0] % L, v[1] % L, v[2] % L])
            dmax = max(dmax, abs(d['U_kern'] - d['U']))
    out['einzel_kern_halbG0'] = 0.5 * float(G[0, 0, 0])
    out['max_abs_U_minus_Ukern'] = dmax
    out['t_gesamt_s'] = time.time() - t0
    return out


def lauf_kern(L, chunk):
    """Kernweg auf dem halben Gitter (irfftn): G_zz = IFT[(pinv Bm)^T pinv Bm]_zz, Gs6/Gs5 = IFT[|pinv b|^2]."""
    t0 = time.time()
    B5, B6 = basis5(), basis6()
    q1 = 2 * np.pi * np.fft.fftfreq(L)
    q3 = 2 * np.pi * np.fft.rfftfreq(L)
    nz = len(q3)
    Mzz = np.empty((L, L, nz)); m6 = np.empty((L, L, nz)); m5 = np.empty((L, L, nz))
    for i0 in range(0, L, chunk):
        qx, qy, qz = np.meshgrid(q1[i0:i0 + chunk], q1, q3, indexing='ij')
        k = kvek(qx, qy, qz)
        Pv = np.linalg.pinv(vek_matrix(k, B5))
        Mzz[i0:i0 + chunk] = np.einsum('...a,...a->...', Pv[..., :, 2], Pv[..., :, 2])
        del Pv
        P6 = np.linalg.pinv(skal_zeile(k, B6)); m6[i0:i0 + chunk] = (P6[..., :, 0] ** 2).sum(-1); del P6
        P5 = np.linalg.pinv(skal_zeile(k, B5)); m5[i0:i0 + chunk] = (P5[..., :, 0] ** 2).sum(-1); del P5
    t_pinv = time.time() - t0
    res = {'L': L, 't_pinv_s': t_pinv, 'Mzz_q0': float(Mzz[0, 0, 0]), 'm6_q0': float(m6[0, 0, 0])}
    Gzz = np.fft.irfftn(Mzz, s=(L, L, L), axes=(0, 1, 2)); del Mzz
    res['zz'] = {str(tuple(v)): float(Gzz[v[0] % L, v[1] % L, v[2] % L]) for v in vek_par() + [(0, 0, 0)]}
    del Gzz
    for name, m in (('s6', m6), ('s5', m5)):
        Gs = np.fft.irfftn(m, s=(L, L, L), axes=(0, 1, 2))
        res[name] = {str(tuple(v)): float(Gs[v[0] % L, v[1] % L, v[2] % L]) for v in VEK_SKAL + [(0, 0, 0)]}
        del Gs
    del m6, m5
    res['t_gesamt_s'] = time.time() - t0
    res['maxrss_MB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    return res


def lauf_pinch(n, qmax):
    B5 = basis5()
    g = np.linspace(-qmax, qmax, n)
    out = {'n': n, 'qmax': qmax, 'ebenen': {}}
    karten = {}
    for ebene in ('hk0', '0kl'):
        a, b = np.meshgrid(g, g, indexing='ij')
        z = np.zeros_like(a)
        qx, qy, qz = (a, b, z) if ebene == 'hk0' else (z, a, b)
        Bm = vek_matrix(kvek(qx, qy, qz), B5)
        PT = np.eye(5) - np.linalg.pinv(Bm) @ Bm
        karten[ebene] = 0.5 * PT[..., 0, 0]          # <E_xy E_xy>, E_xy = e_0/sqrt2
        prof = {}
        phi = np.linspace(0, 2 * np.pi, 720, endpoint=False)
        for eps in (0.02, 0.05, 0.1):
            c, s = eps * np.cos(phi), eps * np.sin(phi)
            z1 = np.zeros_like(c)
            px, py, pz = (c, s, z1) if ebene == 'hk0' else (z1, c, s)
            B1 = vek_matrix(kvek(px, py, pz), B5)
            P1 = np.eye(5) - np.linalg.pinv(B1) @ B1
            prof[str(eps)] = (0.5 * P1[:, 0, 0]).tolist()
        out['ebenen'][ebene] = {'phi': phi.tolist(), 'profile': prof}
    return out, karten


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['rauch', 'explizit', 'kern', 'pinch'])
    ap.add_argument('--L', type=int, action='append')
    ap.add_argument('--chunk', type=int, default=16)
    ap.add_argument('--out', required=True)
    ap.add_argument('--npz')
    a = ap.parse_args()
    t0 = time.time()
    info = {'numpy': np.__version__, 'python': platform.python_version(), 'host': platform.node(),
            'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'argv': sys.argv}
    if a.modus == 'rauch':
        try:
            import matplotlib; info['matplotlib'] = matplotlib.__version__
        except Exception as ex:
            info['matplotlib'] = 'FEHLT: %r' % (ex,)
        nur = {'par': [(0, 0, 2), (2, 0, 0), (1, 1, 1)], 'anti': [(0, 0, 2)], 'senk': [(2, 0, 2)],
               'kontr6': [(0, 0, 2)], 'skal': [(2, 0, 0), (4, 0, 0)], 'skal5': [(2, 0, 0)]}
        res = {'info': info, 'explizit_L12': lauf_explizit(12, nur)}
        t = time.time(); X = Explizit(32); res['zeit_init_L32_s'] = time.time() - t
        t = time.time(); X.vektor([(2, (0, 0, 0), 1.0), (2, (0, 0, 4), 1.0)]); res['zeit_vektor_L32_s'] = time.time() - t
        del X
        t = time.time(); X = Explizit(64); res['zeit_init_L64_s'] = time.time() - t
        t = time.time(); X.vektor([(2, (0, 0, 0), 1.0), (2, (0, 0, 4), 1.0)]); res['zeit_vektor_L64_s'] = time.time() - t
        t = time.time(); X.skalar([((0, 0, 0), 1.0), ((4, 0, 0), -1.0)]); res['zeit_skalar_L64_s'] = time.time() - t
        del X
        k = lauf_kern(64, 16); res['kern_L64_zeit_s'] = k['t_gesamt_s']; res['kern_L64_rss_MB'] = k['maxrss_MB']
        p, _ = lauf_pinch(41, 2 * np.pi); res['pinch_klein_ok'] = True
        res['anzahl_vek_par'] = len(vek_par())
    elif a.modus == 'explizit':
        res = {'info': info, 'laeufe': [lauf_explizit(L) for L in a.L]}
    elif a.modus == 'kern':
        res = {'info': info, 'laeufe': []}
        for L in a.L:
            res['laeufe'].append(lauf_kern(L, a.chunk))
            print('kern L=%d fertig nach %.1f s' % (L, time.time() - t0), flush=True)
    else:
        res, karten = lauf_pinch(401, 2 * np.pi)
        res['info'] = info
        np.savez_compressed(a.npz, hk0=karten['hk0'], okl=karten['0kl'], g=np.linspace(-2 * np.pi, 2 * np.pi, 401))
    res['laufzeit_s'] = time.time() - t0
    res['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    with open(a.out + '.tmp', 'w') as f:
        json.dump(res, f, indent=1)
    os.replace(a.out + '.tmp', a.out)
    print('fertig', a.modus, 'laufzeit %.1f s' % res['laufzeit_s'], flush=True)


if __name__ == '__main__':
    main()
