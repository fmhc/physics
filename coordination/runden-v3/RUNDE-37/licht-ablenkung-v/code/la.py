#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LICHT-ABLENKUNG-V (fmhc-physics, 05.10.2026), Rechen-Agent fuer die Leitung claude-primary. Versuch ohne Karte.

Frage: Spuert DEC-Licht auf Finns gefuelltem Netz V an einer statischen Masse den Brechungsindex n = 1 - 2 Phi
(gamma = 1), wenn Licht und Geometrie denselben Takt (Lapse) und dieselben Laengen benutzen?

Bausteine (unveraendert kopiert): ew.py, tp.py, mn.py (MATERIE-NETZ-1); rv.py, hi.py, danzer_naeherung.py,
licht_netz.py (HOEHE-ISOTROP-1).

1. Statik wie mn.py: Punktquelle (P0, C1), KKT mit Eichwahl M^H a = 0, Zerlegung a_hat = W psi + M xi.
   V1 (q = 1/2): Lapse N_v = 1 + mu_v. Laengen in isotroper Eichung (ohne Eckverschiebung M xi):
   dl_e / l_e = q (psi_v + psi_w) = (sigma_v + sigma_w) / 2, Eck-Skalierung sigma_v = 2 q psi_v.
2. Licht: DEC-Maxwell auf V, gewichtete Sterne an der Kammermitte (hi.sterne_licht).
   LAENGEN: *1 und *2 aus den gestoerten Kantenlaengen in linearer Ordnung, je Tetraeder: Jacobi-Matrix der
     Beitraege (duale Flaeche je Kante, duale Laenge je Dreieck, Dreiecksflaeche) nach den 4 Eck-Skalierungen;
     Kanten l (1 + (sigma_i + sigma_j)/2) ueber Eckverschiebung u = C^+ dl realisiert, Gewichte w_i (1 + 2 sigma_i),
     zentrale Differenzen (h = 1e-5).
   TAKT: Die Hamilton-Dichte des Lichts tickt im Ecktakt wie die Geometrie: elektrische Energie je Kante mit
     N_e = Mittel der 2 Ecken, magnetische je Dreieck mit N_f = Mittel der 3 Ecken:
     omega^2 (*1 / N_e) A = d1^T (N_f *2) d1 A.
3. Messung: lokale Dispersion (k -> 0) je primitiver Zelle R in erster Ordnung als Medium (Plebanski-Form):
     eps(R) = sum_e (*1_e / N_e) l_e^2 t_e t_e^T / V,  zeta(R) = sum_f (N_f *2_f) A_f^2 n_f n_f^T / V  (ungestoert I, I);
     d(omega^2)/omega^2 = b^T d_zeta b - e^T d_eps e (b = k^ x e),  n - 1 = -d(omega)/omega.
   Gegenprobe an Stichprobenzellen mit dem vollen Bloch-Eigenproblem (hi.licht_op, unveraendert).
   Eikonal laengs [100]: Laufzeit T(b) = sum (n - 1) dx je Saeule (geschlossene Schleife der Laenge L), Ablenkung
   = grad_b T.

Aufruf nur ueber kleintest.sh auf der .69:
  python la.py kontrolle <aus.json>
  python la.py haupt <L> <aus.json>
"""
import hashlib
import itertools
import json
import math
import os
import platform
import resource
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ew  # noqa: E402
import mn  # noqa: E402
import rv  # noqa: E402
import hi  # noqa: E402

T0 = time.time()
LP = mn.LP                 # Finn-Kante l_P in kubischen Einheiten
VCELL = mn.VCELL           # Volumen der primitiven Zelle (kubisch)
Q = mn.Q_V1                # q = 1/2 (V1)
S8 = 1.0 / 8.0
PAARE = list(itertools.combinations(range(4), 2))
QUELLEN = [('P0', 0), ('C1', 4)]
CODE = ('la.py', 'ew.py', 'tp.py', 'mn.py', 'rv.py', 'hi.py', 'danzer_naeherung.py', 'licht_netz.py')
RICHTUNGEN = (('100', (1.0, 0.0, 0.0)), ('110', (1.0, 1.0, 0.0)), ('111', (1.0, 1.0, 1.0)))


def log(*a):
    print('[%7.1f s]' % (time.time() - T0), *a, flush=True)


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def js(x):
    if isinstance(x, dict):
        return {str(k): js(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [js(v) for v in x]
    if isinstance(x, np.ndarray):
        return js(x.tolist())
    if isinstance(x, (np.floating, float)):
        v = float(x)
        return v if math.isfinite(v) else None
    if isinstance(x, (np.integer,)):
        return int(x)
    if isinstance(x, (np.bool_,)):
        return bool(x)
    return x


def schreiben(path, obj):
    d = os.path.dirname(os.path.abspath(__file__))
    obj = dict(obj)
    obj['_meta'] = {'argv': sys.argv, 'python': platform.python_version(), 'numpy': np.__version__,
                    'host': platform.node(), 'laufzeit_s': time.time() - T0,
                    'maxrss_MB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
                    'ende_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
                    'sha256': {f: sha(os.path.join(d, f)) for f in CODE}}
    with open(path + '.tmp', 'w') as f:
        json.dump(js(obj), f, indent=1)
    os.replace(path + '.tmp', path)
    log('->', path)


# ------------------------------------------------------------------------------------------------ Statik (wie mn.py)
def statik(L, chunk=64):
    mod = ew.baue('V')
    E, nV = mod['E'], mod['nV']
    g = np.arange(L)
    nn = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1)
    kgrid = ((nn / L) @ ew.BV).reshape(-1, 3)
    N = L ** 3
    nq = len(QUELLEN)
    m = np.zeros((L, L, L, nV, nq))
    for j, (nm, v0) in enumerate(QUELLEN):
        m[0, 0, 0, v0, j] = 1.0
    mk = np.fft.fftn(m, axes=(0, 1, 2)).reshape(N, nV, nq)
    mu_k = np.zeros((N, nV, nq), complex)
    psi_k = np.zeros((N, nV, nq), complex)
    kd = {'kkt_rest_rel_max': 0.0, 'zerlegung_rest_rel_max': 0.0, 'psi_plus_mu_rel_max': 0.0}
    nK = E + nV + 3 * nV
    idx_all = np.arange(1, N)
    for i0 in range(0, len(idx_all), chunk):
        idx = idx_all[i0:i0 + chunk]
        k = kgrid[idx]
        o = ew.ops(mod, k)
        B, M, c = o['B'], o['M'], o['c']
        W = mn.W_of(mod, k)
        K = np.zeros((len(idx), nK, nK), complex)
        K[:, :E, :E] = B
        K[:, :E, E:E + nV] = -c
        K[:, :E, E + nV:] = M
        K[:, E:E + nV, :E] = -mn.cT(c)
        K[:, E + nV:, :E] = mn.cT(M)
        rhs = np.zeros((len(idx), nK, nq), complex)
        rhs[:, E:E + nV, :] = -mk[idx]
        sol = np.linalg.solve(K, rhs)
        kd['kkt_rest_rel_max'] = max(kd['kkt_rest_rel_max'], float(np.abs(K @ sol - rhs).max() / np.abs(rhs).max()))
        ah = sol[:, :E]
        mu = sol[:, E:E + nV]
        WM = np.concatenate([W, M], -1)
        coef = np.linalg.pinv(WM) @ ah
        rest = ah - WM @ coef
        kd['zerlegung_rest_rel_max'] = max(kd['zerlegung_rest_rel_max'],
                                           float((np.linalg.norm(rest, axis=1) / np.linalg.norm(ah, axis=1)).max()))
        psi = coef[:, :nV]
        kd['psi_plus_mu_rel_max'] = max(kd['psi_plus_mu_rel_max'],
                                        float((np.linalg.norm(psi + mu, axis=1) / np.linalg.norm(mu, axis=1)).max()))
        mu_k[idx] = mu
        psi_k[idx] = psi
    mu_r = np.fft.ifftn(mu_k.reshape(L, L, L, nV, nq), axes=(0, 1, 2))
    psi_r = np.fft.ifftn(psi_k.reshape(L, L, L, nV, nq), axes=(0, 1, 2))
    kd['imag_rel_max'] = float(max(np.abs(mu_r.imag).max() / np.abs(mu_r.real).max(),
                                   np.abs(psi_r.imag).max() / np.abs(psi_r.real).max()))
    return mod, mu_r.real, psi_r.real, kd


def ecken_abstand(mod, L, x0):
    pos = np.array(mod['pos'])
    g = np.arange(L)
    nn = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1)
    X = (nn @ ew.AV)[..., None, :] + pos[None, None, None]
    _, d = mn.min_bild(X - x0, L)
    return d / LP                                     # (L, L, L, nV) in l_P


def newton_fit(mu, r, L):
    Vtor = L ** 3 * VCELL / LP ** 3
    fr = lambda x: -1.0 / x - (2 * np.pi / (3 * Vtor)) * x ** 2
    rr, mm = r.ravel(), mu.ravel()
    fern = (rr >= 0.25 * L) & (rr <= 0.5 * L)
    Af = np.stack([fr(rr[fern]), np.ones(fern.sum())], -1)
    (A, C), *_ = np.linalg.lstsq(Af, mm[fern], rcond=None)
    rms = float(np.sqrt(np.mean((Af @ np.array([A, C]) - mm[fern]) ** 2)) / np.abs(A * fr(rr[fern])).mean())
    phiN = np.full(r.shape, np.nan)
    ok = r > 1e-9
    phiN[ok] = A * fr(r[ok]) + C
    return float(A), float(C), rms, phiN


# ------------------------------------------------------------------------------------------------ Licht-Bausteine
def licht_basis():
    net1 = rv.netz_V(1)
    topo1 = rv.topologie(net1)
    rows1, A1, G01 = rv.zeilen(net1, topo1)
    sy = rv.lp_symmetrisch(A1, G01, rv.bahnmatrix(net1))
    w_mid = rv.w_sym(net1, sy['x'], sy['y'])
    mb = hi.maxwell_bau(net1, topo1)
    st = hi.sterne_licht(net1, topo1, mb, w_mid)
    return {'net': net1, 'topo': topo1, 'w': w_mid, 'mb': mb, 'st': st, 'xy_mid': (sy['x'], sy['y']),
            'marge_mid': float((G01 + A1 @ w_mid).min())}


def tet_beitraege(X, wt):
    """Wie rv.sterne je Tetraeder: duale Flaeche je Kante (6, Reihenfolge PAARE), duale Laenge je Dreieck j (gegenueber
    Ecke j) und Dreiecksflaeche je j. X (4, 3) in a, wt (4,) in a^2."""
    q = (X * X).sum(1) - wt
    z = np.linalg.solve(2.0 * (X[1:] - X[0]), q[1:] - q[0])
    cf, nu = {}, {}
    dl = np.zeros(4)
    af = np.zeros(4)
    for j in range(4):
        i0, i1, i2 = [i for i in range(4) if i != j]
        e1, e2 = X[i1] - X[i0], X[i2] - X[i0]
        G = np.array([[e1 @ e1, e1 @ e2], [e1 @ e2, e2 @ e2]])
        rhs = 0.5 * np.array([e1 @ e1 + wt[i0] - wt[i1], e2 @ e2 + wt[i0] - wt[i2]])
        ab = np.linalg.solve(G, rhs)
        c = X[i0] + ab[0] * e1 + ab[1] * e2
        nv = np.cross(e1, e2)
        af[j] = 0.5 * np.linalg.norm(nv)
        nv = nv / np.linalg.norm(nv)
        if nv @ (X[j] - X[i0]) < 0:
            nv = -nv
        cf[j] = c
        nu[j] = nv
        dl[j] = (z - c) @ nv
    A = np.zeros(6)
    for r, (i, j) in enumerate(PAARE):
        k, l = [m for m in range(4) if m not in (i, j)]
        e = X[j] - X[i]
        le = np.linalg.norm(e)
        eh = e / le
        cij = X[i] + (le * le + wt[i] - wt[j]) / (2 * le) * eh
        tot = 0.0
        for (a, b) in ((k, l), (l, k)):
            u = (X[a] - X[i]) - ((X[a] - X[i]) @ eh) * eh
            u /= np.linalg.norm(u)
            h1 = (cf[b] - cij) @ u
            h2 = (z - cf[b]) @ nu[b]
            tot += 0.5 * h1 * h2
        A[r] = tot
    return A, dl, af


def tet_jacobi(X, wt, h=1e-5, w_regel='ecke'):
    """w_regel: 'ecke' w_i (1 + 2 sigma_i); 'tet' w_i (1 + 2 sigma_tet), sigma_tet = Mittel der 4 Ecken
    (eichinvariant gegen w + const); 'fest' Gewichte bleiben (nicht skalierungstreu)."""
    l = np.array([np.linalg.norm(X[j] - X[i]) for (i, j) in PAARE])
    C = np.zeros((6, 12))
    for r, (i, j) in enumerate(PAARE):
        n = (X[j] - X[i]) / l[r]
        C[r, 3 * j:3 * j + 3] += n
        C[r, 3 * i:3 * i + 3] -= n
    Cp = C.T @ np.linalg.inv(C @ C.T)
    JA, JD, JF = np.zeros((6, 4)), np.zeros((4, 4)), np.zeros((4, 4))
    for m in range(4):
        dlv = np.array([l[r] * ((i == m) + (j == m)) / 2.0 for r, (i, j) in enumerate(PAARE)])
        u = (Cp @ dlv).reshape(4, 3)
        dw = np.zeros(4)
        if w_regel == 'ecke':
            dw[m] = 2.0 * wt[m]
        elif w_regel == 'tet':
            dw = 0.5 * wt
        ap, dp, fp = tet_beitraege(X + h * u, wt + h * dw)
        am, dm, fm = tet_beitraege(X - h * u, wt - h * dw)
        JA[:, m] = (ap - am) / (2 * h)
        JD[:, m] = (dp - dm) / (2 * h)
        JF[:, m] = (fp - fm) / (2 * h)
    a0, d0, f0 = tet_beitraege(X, wt)
    return JA, JD, JF, a0, d0, f0


def zelle_off(x8, home_s):
    return tuple(int(v) for v in np.rint((np.asarray(x8, float) - home_s) @ ew.AV8INV))


def elemente(lb, w_regel='ecke', w_offset=0.0):
    net, topo, mb, st = lb['net'], lb['topo'], lb['mb'], lb['st']
    home = net['home']
    w = lb['w'] + w_offset
    tets = []
    for t, (g, X8) in enumerate(net['tets']):
        X = np.asarray(X8, float) * S8
        wt = w[g] * S8 * S8
        JA, JD, JF, a0, d0, f0 = tet_jacobi(X, wt, w_regel=w_regel)
        noff = [zelle_off(X8[q], home[g[q]]) for q in range(4)]
        tets.append({'g': [int(x) for x in g], 'n': noff, 'JA': JA, 'JD': JD, 'JF': JF, 'a0': a0, 'd0': d0, 'f0': f0})
    kant = []
    E1, F1 = mb['E'], mb['F']
    l = np.zeros(E1)
    tv = np.zeros((E1, 3))
    xm = np.zeros((E1, 3))
    for m, key in enumerate(mb['ke']):
        (ga, pa), (gb, pb) = key
        pa, pb = np.array(pa, float), np.array(pb, float)
        d = (pb - pa) * S8
        l[m] = np.linalg.norm(d)
        tv[m] = d / l[m]
        xm[m] = 0.5 * (pa + pb) * S8
        terme = {}
        a_sum = 0.0
        for (t, (i, j), T) in topo['kanten'][key]:
            Tc = np.rint(np.asarray(T, float) @ ew.AV8INV).astype(int)
            r = PAARE.index((i, j))
            a_sum += tets[t]['a0'][r]
            for q in range(4):
                sh = tuple(int(v) for v in (np.array(tets[t]['n'][q]) - Tc))
                kk = (tets[t]['g'][q], sh)
                terme[kk] = terme.get(kk, 0.0) + tets[t]['JA'][r, q]
        kant.append({'ecken': [(int(ga), zelle_off(pa, home[ga])), (int(gb), zelle_off(pb, home[gb]))],
                     'terme': terme, 'a_sum': a_sum})
    flae = []
    xf = np.zeros((F1, 3))
    for f, key in enumerate(mb['kf']):
        ecken = []
        P = []
        for (gq, pq) in key:
            ecken.append((int(gq), zelle_off(pq, home[gq])))
            P.append(np.array(pq, float))
        xf[f] = np.mean(P, 0) * S8
        tD, tF = {}, {}
        d_sum = 0.0
        f_area = None
        for ie, (t, j, T) in enumerate(topo['flaechen'][key]):
            Tc = np.rint(np.asarray(T, float) @ ew.AV8INV).astype(int)
            d_sum += tets[t]['d0'][j]
            if ie == 0:
                f_area = tets[t]['f0'][j]
            for q in range(4):
                sh = tuple(int(v) for v in (np.array(tets[t]['n'][q]) - Tc))
                kk = (tets[t]['g'][q], sh)
                tD[kk] = tD.get(kk, 0.0) + tets[t]['JD'][j, q]
                if ie == 0:
                    tF[kk] = tF.get(kk, 0.0) + tets[t]['JF'][j, q]
        flae.append({'ecken': ecken, 'tD': tD, 'tF': tF, 'd_sum': d_sum, 'f_area': f_area})
    a_sum = np.array([k['a_sum'] for k in kant])
    d_sum = np.array([f['d_sum'] for f in flae])
    f_ar = np.array([f['f_area'] for f in flae])
    wE = st['s1'] * l ** 2 / VCELL
    wF = st['S2'] * mb['A_f'] ** 2 / VCELL
    pr = {'a_sum_gegen_s1l_rel': float(np.abs(a_sum - st['s1'] * l).max() / np.abs(st['s1'] * l).max()),
          'd_sum_gegen_S2A_rel': float(np.abs(d_sum - st['S2'] * mb['A_f']).max() / np.abs(st['S2'] * mb['A_f']).max()),
          'f_area_gegen_A_f_rel': float(np.abs(f_ar - mb['A_f']).max() / mb['A_f'].max()),
          'T1_minus_I': float(np.abs(np.einsum('m,mi,mj->ij', wE, tv, tv) - np.eye(3)).max()),
          'T2_minus_I': float(np.abs(np.einsum('f,fi,fj->ij', wF, mb['n_f'], mb['n_f']) - np.eye(3)).max()),
          'n_terme_kante_max': max(len(k['terme']) for k in kant), 'min_s1': float(st['s1'].min()),
          'min_S2': float(st['S2'].min()), 'id_T2': st['id_T2']}
    # Uniform-Probe der Jacobi-Summen: sum_q J = (2 a0, d0, 2 f0) je Tetraeder
    uni = 0.0
    for t in tets:
        uni = max(uni, float(np.abs(t['JA'].sum(1) - 2 * t['a0']).max() / np.abs(t['a0']).max()),
                  float(np.abs(t['JD'].sum(1) - t['d0']).max() / np.abs(t['d0']).max()),
                  float(np.abs(t['JF'].sum(1) - 2 * t['f0']).max() / np.abs(t['f0']).max()))
    pr['jacobi_uniform_rel_max'] = uni
    xE = (wE[:, None] * xm).sum(0) / wE.sum()
    xB = (wF[:, None] * xf).sum(0) / wF.sum()
    return {'kant': kant, 'flae': flae, 'tets': tets, 'l': l, 't': tv, 'xm': xm, 'xf': xf, 'wE': wE, 'wF': wF,
            'nf': mb['n_f'], 'A_f': mb['A_f'], 'x_zelle': 0.5 * (xE + xB), 'xE': xE, 'xB': xB, 'pruefung': pr}


def roll_at(F, s, sh):
    return np.roll(F[s], (-sh[0], -sh[1], -sh[2]), axis=(0, 1, 2))


def stoerung(el, sig, mu, roh=False):
    """sig, mu: (nV, L, L, L). Relative Stoerungen der Sterne (Laengen) und Takt je Element und Zelle."""
    E1, F1 = len(el['kant']), len(el['flae'])
    sh = sig.shape[1:]
    s1rel = np.zeros((E1,) + sh)
    nuE = np.zeros((E1,) + sh)
    dAr = np.zeros((E1,) + sh) if roh else None
    for m, k in enumerate(el['kant']):
        dA = np.zeros(sh)
        for (s, d), cf in k['terme'].items():
            dA += cf * roll_at(sig, s, d)
        (sa, na), (sb, nb) = k['ecken']
        dl = 0.5 * (roll_at(sig, sa, na) + roll_at(sig, sb, nb))
        s1rel[m] = dA / k['a_sum'] - dl
        nuE[m] = 0.5 * (roll_at(mu, sa, na) + roll_at(mu, sb, nb))
        if roh:
            dAr[m] = dA
    s2rel = np.zeros((F1,) + sh)
    nuF = np.zeros((F1,) + sh)
    dDr = np.zeros((F1,) + sh) if roh else None
    for f, fl in enumerate(el['flae']):
        dD = np.zeros(sh)
        for (s, d), cf in fl['tD'].items():
            dD += cf * roll_at(sig, s, d)
        dF = np.zeros(sh)
        for (s, d), cf in fl['tF'].items():
            dF += cf * roll_at(sig, s, d)
        s2rel[f] = dD / fl['d_sum'] - dF / fl['f_area']
        nuF[f] = sum(roll_at(mu, s, d) for (s, d) in fl['ecken']) / 3.0
        if roh:
            dDr[f] = dD
    return s1rel, nuE, s2rel, nuF, dAr, dDr


def tensoren(el, s1rel, nuE, s2rel, nuF):
    tt = np.einsum('mi,mj->mij', el['t'], el['t'])
    nn_ = np.einsum('fi,fj->fij', el['nf'], el['nf'])
    epsT = -np.einsum('m,m...,mij->...ij', el['wE'], nuE, tt)
    epsL = np.einsum('m,m...,mij->...ij', el['wE'], s1rel, tt)
    zetT = np.einsum('f,f...,fij->...ij', el['wF'], nuF, nn_)
    zetL = np.einsum('f,f...,fij->...ij', el['wF'], s2rel, nn_)
    return epsT, epsL, zetT, zetL


def n_iso(deps, dzet):
    return (np.trace(deps, axis1=-2, axis2=-1) - np.trace(dzet, axis1=-2, axis2=-1)) / 6.0


def basis(d):
    d = np.asarray(d, float)
    d = d / np.linalg.norm(d)
    a = np.array([1.0, 0, 0]) if abs(d[0]) < 0.9 else np.array([0, 1.0, 0])
    e1 = np.cross(d, a)
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(d, e1)
    return d, np.stack([e1, e2]), np.stack([np.cross(d, e1), np.cross(d, e2)])


def Pi_mat(deps, dzet, d):
    d, Eb, Bb = basis(d)
    return np.einsum('ai,...ij,bj->...ab', Bb, dzet, Bb) - np.einsum('ai,...ij,bj->...ab', Eb, deps, Eb)


def n_richtung(deps, dzet, d):
    lam = np.linalg.eigvalsh(Pi_mat(deps, dzet, d))
    return np.sort(-lam / 2.0, axis=-1)              # (..., 2): n - 1 der zwei Eigenpolarisationen


# ------------------------------------------------------------------------------------------------ Kontrollen
def kontrolle_roll(L, lb, el, rng):
    """Explizites Torus-Netz (rv.netz_V(L)) gegen die roll-Zusammensetzung, zufaelliges sigma."""
    netL = rv.netz_V(L)
    topoL = rv.topologie(netL)
    nV = 10
    N = L ** 3
    nT1 = len(lb['net']['tets'])
    sig = rng.standard_normal((nV, L, L, L))
    sig_g = sig.reshape(nV, N).reshape(-1)
    dA_exp, dD_exp = {}, {}
    for tt, (g, X) in enumerate(netL['tets']):
        typ = tt % nT1
        T = el['tets'][typ]
        for r, (i, j) in enumerate(PAARE):
            key = topoL['tk'][tt][(i, j)]
            dA_exp[key] = dA_exp.get(key, 0.0) + float(T['JA'][r] @ sig_g[np.asarray(g)])
        for j in range(4):
            key = topoL['tf'][tt][j]
            dD_exp[key] = dD_exp.get(key, 0.0) + float(T['JD'][j] @ sig_g[np.asarray(g)])
    _, _, _, _, dAr, dDr = stoerung(el, sig, np.zeros_like(sig), roh=True)
    k1e = {key: m for m, key in enumerate(lb['mb']['ke'])}
    k1f = {key: f for f, key in enumerate(lb['mb']['kf'])}

    def abb(key, tab):
        ga = key[0][0]
        Ra = np.unravel_index(ga % N, (L, L, L))
        R8v = np.array(Ra) @ ew.AV8
        k1 = tuple((int(gq // N), tuple(float(v) for v in np.round(np.asarray(pq, float) - R8v, 6))) for (gq, pq) in key)
        return tab.get(k1), Ra

    out = {'L': L, 'kanten': len(dA_exp), 'flaechen': len(dD_exp), 'nicht_zugeordnet': 0}
    da, dd, sa, sd = 0.0, 0.0, 0.0, 0.0
    for key, v in dA_exp.items():
        m, Ra = abb(key, k1e)
        if m is None:
            out['nicht_zugeordnet'] += 1
            continue
        da = max(da, abs(v - dAr[(m,) + tuple(Ra)]))
        sa = max(sa, abs(v))
    for key, v in dD_exp.items():
        f, Ra = abb(key, k1f)
        if f is None:
            out['nicht_zugeordnet'] += 1
            continue
        dd = max(dd, abs(v - dDr[(f,) + tuple(Ra)]))
        sd = max(sd, abs(v))
    out['dA_abw_rel'] = da / sa
    out['dD_abw_rel'] = dd / sd
    return out


def c_ohne_masse(lb, kappa=0.05):
    st, mb = lb['st'], lb['mb']
    res = {}
    for nm, d in RICHTUNGEN:
        dg = hi.neue_diag()
        k = kappa * np.array(d) / np.linalg.norm(d)
        w = hi.licht_op(mb, st['s1'], st['S2'], dg)(k)
        res[nm] = {'c_lo': w[0] / kappa, 'c_hi': w[1] / kappa, 'null_rel': dg['null_rel'], 'luecke': dg['luecke']}
    return res


def modus_kontrolle(aus):
    lb = licht_basis()
    log('Licht-Basis: E F nV', lb['mb']['E'], lb['mb']['F'], lb['mb']['nV'], 'Marge', lb['marge_mid'])
    el = elemente(lb)
    log('Elemente fertig', el['pruefung'])
    rng = np.random.default_rng([2026, 10, 5])
    kr = kontrolle_roll(4, lb, el, rng)
    log('roll-Kontrolle', kr)
    # Uniform: sigma = 1 -> s1rel = 1, s2rel = -1; mu = 1 -> nT = -1
    L = 3
    one = np.ones((10, L, L, L))
    zero = np.zeros((10, L, L, L))
    s1rel, nuE, s2rel, nuF, _, _ = stoerung(el, one, zero)
    eT, eL, zT, zL = tensoren(el, s1rel, nuE, s2rel, nuF)
    uni = {'s1rel_minus_1': float(np.abs(s1rel - 1).max()), 's2rel_plus_1': float(np.abs(s2rel + 1).max()),
           'nL_minus_1': float(np.abs(n_iso(eL, zL) - 1).max())}
    s1rel, nuE, s2rel, nuF, _, _ = stoerung(el, zero, one)
    eT, eL, zT, zL = tensoren(el, s1rel, nuE, s2rel, nuF)
    uni['nT_plus_1'] = float(np.abs(n_iso(eT, zT) + 1).max())
    uni['richtung_max_abw'] = float(max(np.abs(n_richtung(eT, zT, d) + 1).max() for _, d in RICHTUNGEN))
    log('uniform', uni)
    # Gewichts-Eichung: Konstante 1 a^2 (= 64 (a/8)^2) auf alle Gewichte vor dem Skalieren
    el2 = elemente(lb, w_offset=64.0)
    rng2 = np.random.default_rng([2026, 10, 6])
    sig = rng2.standard_normal((10, L, L, L))
    a1 = stoerung(el, sig, zero)
    a2 = stoerung(el2, sig, zero)
    eich = {'s1rel_abw_max': float(np.abs(a1[0] - a2[0]).max()), 's2rel_abw_max': float(np.abs(a1[2] - a2[2]).max()),
            's1rel_skala': float(np.abs(a1[0]).max()), 'uniform_bleibt': float(np.abs(stoerung(el2, one, zero)[0] - 1).max()),
            'pruefung_el2': el2['pruefung']}
    log('Gewichts-Eichung', eich)
    co = c_ohne_masse(lb)
    log('c ohne Masse', co)
    schreiben(aus, {'pruefung_elemente': el['pruefung'], 'roll': kr, 'uniform': uni, 'gewichts_eichung': eich,
                    'c_ohne_masse': co, 'x_zelle': el['x_zelle'], 'w_mid': lb['w'], 'xy_mid': lb['xy_mid'],
                    'marge_mid': lb['marge_mid']})


# ------------------------------------------------------------------------------------------------ Hauptlauf
SCHALEN = [0.0, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 20.0, 24.0]


def eigen_probe(lb, s1rel, nuE, s2rel, nuF, deps, dzet, zellen, kappa=0.05, ziel=1e-4):
    st, mb = lb['st'], lb['mb']
    out = []
    for nm, d in (('100', (1.0, 0, 0)), ('111', (1.0, 1.0, 1.0))):
        k = kappa * np.array(d) / np.linalg.norm(d)
        w0 = hi.licht_op(mb, st['s1'], st['S2'], hi.neue_diag())(k)
        om2 = np.array([w0[0] ** 2, w0[1] ** 2])
        ref = om2.mean()
        for c in zellen:
            ix = (slice(None),) + tuple(int(v) for v in c)
            pE = s1rel[ix] - nuE[ix]
            pF = s2rel[ix] + nuF[ix]
            amp = ziel / max(np.abs(pE).max(), np.abs(pF).max())
            dg = hi.neue_diag()
            w = hi.licht_op(mb, st['s1'] * (1 + amp * pE), st['S2'] * (1 + amp * pF), dg)(k)
            gem = np.sort((np.array([w[0] ** 2, w[1] ** 2]) - ref) / ref / amp)
            vor = np.sort(np.linalg.eigvalsh(Pi_mat(deps[tuple(int(v) for v in c)], dzet[tuple(int(v) for v in c)], d)))
            out.append({'richtung': nm, 'zelle': [int(v) for v in c], 'gemessen_domega2': gem, 'vorhergesagt_domega2': vor,
                        'abw': float(np.abs(gem - vor).max()), 'skala': float(np.abs(vor).max()),
                        'grundaufspaltung': float((om2[1] - om2[0]) / ref / amp), 'amp': amp,
                        'null_rel': dg['null_rel']})
    return out


def schalen_tab(rc, rhat, A, ntot, nT, nLn, ziel, eT, eL, zT, zL, dopp=None, aniso=None):
    deps, dzet = eT + eL, zT + zL
    tr = lambda X: np.trace(X, axis1=-2, axis2=-1)
    rr = lambda X: np.einsum('...i,...ij,...j->...', rhat, X, rhat)
    # Doppelbrechung fuer Strahlen quer zu r: n_r - n_t = [(eps_rr - eps_tt) + (zeta_rr - zeta_tt)] / 2
    e_rt = rr(deps) - 0.5 * (tr(deps) - rr(deps))
    z_rt = rr(dzet) - 0.5 * (tr(dzet) - rr(dzet))
    dn_rt = 0.5 * (e_rt + z_rt)
    epsL_iso, muL_iso = tr(eL) / 3.0, -tr(zL) / 3.0
    sch = []
    for a, b in zip(SCHALEN[:-1], SCHALEN[1:]):
        s = (rc >= a) & (rc < b)
        if not s.any():
            continue
        ok = s & np.isfinite(ziel)
        z = {'r0': a, 'r1': b, 'n': int(s.sum()), 'n_minus_1': float(ntot[s].mean()), 'takt': float(nT[s].mean()),
             'laengen': float(nLn[s].mean()),
             'ziel_ART': float(ziel[ok].mean()) if ok.any() else None,
             'ART_2A_ueber_r': float((2 * A / rc[s]).mean()),
             'gesamt_ueber_ziel': float(ntot[ok].mean() / ziel[ok].mean()) if ok.any() else None,
             'takt_ueber_halbziel': float(nT[ok].mean() / (0.5 * ziel[ok].mean())) if ok.any() else None,
             'laengen_ueber_takt': float(nLn[s].mean() / nT[s].mean()),
             'laengen_ueber_takt_zelle_min': float((nLn[s] / nT[s]).min()),
             'laengen_ueber_takt_zelle_max': float((nLn[s] / nT[s]).max()),
             'gesamt_ueber_ziel_zelle_min': float((ntot[ok] / ziel[ok]).min()) if ok.any() else None,
             'gesamt_ueber_ziel_zelle_max': float((ntot[ok] / ziel[ok]).max()) if ok.any() else None,
             'dn_radial_tangential_mittel_rel': float(dn_rt[s].mean() / ntot[s].mean()),
             'epsL_iso': float(epsL_iso[s].mean()), 'muL_iso': float(muL_iso[s].mean())}
        if dopp is not None:
            z['doppelbrechung_zelle_rel_max'] = float((dopp[s] / np.abs(ntot[s])).max())
            z['anisotropie_zelle_rel_max'] = float((aniso[s] / np.abs(ntot[s])).max())
        sch.append(z)
    return sch


def kern(el, sig, mu, phN):
    s1rel, nuE, s2rel, nuF, _, _ = stoerung(el, sig, mu)
    eT, eL, zT, zL = tensoren(el, s1rel, nuE, s2rel, nuF)
    nT = n_iso(eT, zT)
    nLn = n_iso(eL, zL)
    _, nuE_N, _, nuF_N, _, _ = stoerung(el, np.zeros_like(sig), phN)
    nT_N = -(np.einsum('m,m...->...', el['wE'], nuE_N) + np.einsum('f,f...->...', el['wF'], nuF_N)) / 6.0
    return {'s1rel': s1rel, 'nuE': nuE, 's2rel': s2rel, 'nuF': nuF, 'eT': eT, 'eL': eL, 'zT': zT, 'zL': zL,
            'nT': nT, 'nL': nLn, 'ntot': nT + nLn, 'ziel': 2.0 * nT_N, 'nuE_N': nuE_N, 'nuF_N': nuF_N}


def auswerten_quelle(L, mod, lb, els, mu_v, psi_v, nm, v0):
    """mu_v, psi_v: (L, L, L, nV) einer Quelle; els: {Variante: Elemente}, Hauptvariante 'ecke'."""
    pos = np.array(mod['pos'])
    x0 = pos[v0]
    r_v = ecken_abstand(mod, L, x0)
    A, C, rms, phiN = newton_fit(mu_v, r_v, L)
    sig = np.moveaxis(2 * Q * psi_v, -1, 0)
    mu = np.moveaxis(mu_v, -1, 0)
    phN = np.moveaxis(phiN, -1, 0)
    el = els['ecke']
    t = time.time()
    kk = kern(el, sig, mu, phN)
    log(nm, 'Stoerung', '%.1f s' % (time.time() - t))
    s1rel, nuE, s2rel, nuF = kk['s1rel'], kk['nuE'], kk['s2rel'], kk['nuF']
    eT, eL, zT, zL = kk['eT'], kk['eL'], kk['zT'], kk['zL']
    nT, nLn, ntot, ziel = kk['nT'], kk['nL'], kk['ntot'], kk['ziel']
    nuE_N, nuF_N = kk['nuE_N'], kk['nuF_N']
    # Zellorte
    g = np.arange(L)
    nn = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1)
    Xc = nn @ ew.AV + el['x_zelle']
    dvec, rc = mn.min_bild(Xc - x0, L)
    rhat = dvec / rc[..., None]
    rc = rc / LP
    # Richtungen, Doppelbrechung (je Zelle, mit Zuordnungs-Artefakt)
    deps, dzet = eT + eL, zT + zL
    nr = {dn_: n_richtung(deps, dzet, d) for dn_, d in RICHTUNGEN}
    nrT = {dn_: n_richtung(eT, zT, d) for dn_, d in RICHTUNGEN}
    nrL = {dn_: n_richtung(eL, zL, d) for dn_, d in RICHTUNGEN}
    dopp = np.max(np.stack([v[..., 1] - v[..., 0] for v in nr.values()]), 0)
    aniso = np.max(np.stack([np.abs(v.mean(-1) - ntot) for v in nr.values()]), 0)
    sch = schalen_tab(rc, rhat, A, ntot, nT, nLn, ziel, eT, eL, zT, zL, dopp, aniso)
    varianten = {}
    for vn, elv in els.items():
        if vn == 'ecke':
            continue
        kv = kern(elv, sig, mu, phN)
        varianten[vn] = schalen_tab(rc, rhat, A, kv['ntot'], kv['nT'], kv['nL'], kv['ziel'], kv['eT'], kv['eL'],
                                    kv['zT'], kv['zL'])
    # naechste Zellen einzeln
    order = np.argsort(rc.ravel())
    nah = []
    for i in order[:16]:
        c = np.unravel_index(i, (L, L, L))
        nah.append({'zelle': [int(v) for v in c], 'r': float(rc[c]), 'n_minus_1': float(ntot[c]), 'takt': float(nT[c]),
                    'laengen': float(nLn[c]), 'ziel_ART': float(ziel[c]) if np.isfinite(ziel[c]) else None,
                    'n100': nr['100'][c], 'n111': nr['111'][c], 'takt100': nrT['100'][c], 'laengen100': nrL['100'][c]})
    # Eigenwert-Gegenprobe
    zl = [np.unravel_index(i, (L, L, L)) for i in list(order[:10]) + list(order[len(order) // 50::len(order) // 8][:8])]
    ep = eigen_probe(lb, s1rel, nuE, s2rel, nuF, deps, dzet, zl)
    # Eikonal laengs [100]: Saeulen (Y, Z) = (n1 + n3, n1 + n2) mod L, Laenge L (kubisch), dx = 1 je Zelle
    n1, n2, n3 = nn[..., 0], nn[..., 1], nn[..., 2]
    Y, Z = (n1 + n3) % L, (n1 + n2) % L

    def nx(de, dz):
        return -(np.trace(dz, axis1=-2, axis2=-1) - dz[..., 0, 0] - np.trace(de, axis1=-2, axis2=-1) + de[..., 0, 0]) / 4.0

    def saeule(f):
        T = np.zeros((L, L))
        np.add.at(T, (Y.ravel(), Z.ravel()), f.ravel())
        return T / LP                                    # Integral (n - 1) dx in l_P

    # Ziel fuer die Saeule: Takt-Anteil der Richtung [100] mit Phi_N, mal 2 (Tensorform wie oben)
    eTN = -np.einsum('m,m...,mij->...ij', el['wE'], nuE_N, np.einsum('mi,mj->mij', el['t'], el['t']))
    zTN = np.einsum('f,f...,fij->...ij', el['wF'], nuF_N, np.einsum('fi,fj->fij', el['nf'], el['nf']))
    Tg = {'gesamt': saeule(nx(deps, dzet)), 'takt': saeule(nx(eT, zT)), 'laengen': saeule(nx(eL, zL))}
    zielx = 2 * nx(eTN, zTN)
    Tg['ziel'] = saeule(np.where(np.isfinite(zielx), zielx, 0.0))
    ziel_nan = np.zeros((L, L), bool)
    np.logical_or.at(ziel_nan, (Y.ravel(), Z.ravel()), ~np.isfinite(zielx).ravel())
    # Querlage der Saeulen relativ zur Quelle (kubisch), Torusquadrat der Seite L/2
    yc = 0.5 * np.arange(L)[:, None] + el['x_zelle'][1] - x0[1] + 0.0 * np.arange(L)[None, :]
    zc = 0.5 * np.arange(L)[None, :] + el['x_zelle'][2] - x0[2] + 0.0 * np.arange(L)[:, None]
    hw = 0.5 * L
    yc = (yc + 0.5 * hw) % hw - 0.5 * hw
    zc = (zc + 0.5 * hw) % hw - 0.5 * hw
    b = np.sqrt(yc ** 2 + zc ** 2) / LP

    def grad(T):
        gy = (np.roll(T, -1, 0) - np.roll(T, 1, 0)) / (1.0 / LP)     # Schritt 2 x 1/2 kubisch = 1 kubisch, T in l_P
        gz = (np.roll(T, -1, 1) - np.roll(T, 1, 1)) / (1.0 / LP)
        return gy, gz

    G = {k_: grad(v) for k_, v in Tg.items()}
    nanb = ziel_nan | np.roll(ziel_nan, 1, 0) | np.roll(ziel_nan, -1, 0) | np.roll(ziel_nan, 1, 1) | np.roll(ziel_nan, -1, 1)
    sae = []
    ob = np.argsort(b.ravel())
    for i in ob[:40]:
        c = np.unravel_index(i, (L, L))
        uy, uz = -yc[c] / (b[c] * LP), -zc[c] / (b[c] * LP)            # Einheitsvektor zur Masse
        rad = {k_: float(G[k_][0][c] * uy + G[k_][1][c] * uz) for k_ in G}
        tan = {k_: float(-G[k_][0][c] * uz + G[k_][1][c] * uy) for k_ in G}
        sae.append({'Y': int(c[0]), 'Z': int(c[1]), 'b': float(b[c]), 'T': {k_: float(v[c]) for k_, v in Tg.items()},
                    'alpha_zur_masse': rad, 'alpha_quer': tan, 'ART_4A_ueber_b': float(4 * A / b[c]),
                    'ziel_mit_quellecke': bool(nanb[c])})
    # Laufzeit-Unterschiede (Shapiro) zwischen Saeulenpaaren gegen 2 (1 + gamma) A ln(b2/b1) (unendliche Gerade)
    shap = []
    ref_i = [i for i in ob if not nanb[np.unravel_index(i, (L, L))]]
    if ref_i:
        far = [i for i in ref_i if 0.2 * L <= b.ravel()[i] <= 0.3 * L]
        if far:
            jf = np.unravel_index(far[0], (L, L))
            for i in ref_i[:12]:
                c = np.unravel_index(i, (L, L))
                shap.append({'b1': float(b[c]), 'b2': float(b[jf]),
                             'dT': {k_: float(v[c] - v[jf]) for k_, v in Tg.items()},
                             'ART_gerade_4A_ln': float(4 * A * math.log(b[jf] / b[c]))})
    res = {'quelle': nm, 'ecke': v0, 'fit': {'A': A, 'C': C, 'rms_rel': rms, 'A_soll': 1 / (8 * math.sqrt(2) * math.pi)},
           'schalen': sch, 'varianten_schalen': varianten, 'nah': nah, 'eigen_probe': ep, 'saeulen': sae,
           'shapiro_paare': shap,
           'eigen_probe_abw_rel_max': float(max(e['abw'] / e['skala'] for e in ep)),
           'mu_min': float(mu_v.min()), 'sigma_max': float((2 * Q * psi_v).max())}
    return res


def modus_haupt(L, aus):
    t = time.time()
    lb = licht_basis()
    els = {'ecke': elemente(lb), 'tet': elemente(lb, w_regel='tet'), 'ecke_w+1a2': elemente(lb, w_offset=64.0),
           'fest': elemente(lb, w_regel='fest')}
    el = els['ecke']
    log('Licht-Basis und Elemente: %.1f s' % (time.time() - t), {k: v['pruefung']['jacobi_uniform_rel_max'] for k, v in els.items()})
    t = time.time()
    mod, mu_r, psi_r, kd = statik(L)
    log('Statik L=%d: %.1f s' % (L, time.time() - t), kd)
    res = {'L': L, 'statik_kontrollen': kd, 'pruefung_elemente': {k: v['pruefung'] for k, v in els.items()},
           'x_zelle': el['x_zelle'], 'quellen': {}}
    for j, (nm, v0) in enumerate(QUELLEN):
        res['quellen'][nm] = auswerten_quelle(L, mod, lb, els, mu_r[..., j], psi_r[..., j], nm, v0)
        log(nm, 'fertig; Schalen (Variante ecke):')
        for z in res['quellen'][nm]['schalen']:
            log('  [%5.1f,%5.1f) n=%5d  n-1=% .3e takt=% .3e laengen=% .3e  ges/ziel=%s  L/T=%.4f  rt=% .1e  dopp=%.1e' % (
                z['r0'], z['r1'], z['n'], z['n_minus_1'], z['takt'], z['laengen'],
                ('%.4f' % z['gesamt_ueber_ziel']) if z['gesamt_ueber_ziel'] is not None else '-',
                z['laengen_ueber_takt'], z['dn_radial_tangential_mittel_rel'], z['doppelbrechung_zelle_rel_max']))
        for vn, sv in res['quellen'][nm]['varianten_schalen'].items():
            log(nm, 'Variante', vn, 'L/T je Schale:', ' '.join('%.3f' % z['laengen_ueber_takt'] for z in sv))
        log(nm, 'Eigen-Probe max rel Abw', res['quellen'][nm]['eigen_probe_abw_rel_max'])
    schreiben(aus, res)


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__)
        return 2
    if a[0] == 'kontrolle':
        modus_kontrolle(a[1])
    elif a[0] == 'haupt':
        modus_haupt(int(a[1]), a[2])
    else:
        print(__doc__)
        return 2
    log('fertig')
    return 0


if __name__ == '__main__':
    sys.exit(main())
