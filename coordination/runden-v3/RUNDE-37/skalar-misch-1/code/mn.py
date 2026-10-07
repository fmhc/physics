#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MATERIE-NETZ-1, Runde 45 (fmhc-physics), Code-Agent fuer die Leitung claude-primary.

Statische Antwort von Finns Hamilton-Netz (gefuellt, V; ew.py aus EINE-WELT-LOCH-1 unveraendert importiert) auf eine
ruhende Energiequelle, zwei Varianten (Finn: "Teste beide Varianten"):
  V1: Energie in der Regel je Ecke, Materie und Regge-Anteil ticken im Ecktakt: q = kappa'/kappa_g = 1/2.
  V2: Materie tickt nur im Ecktakt, Regel ohne Quelle (kappa' = 0); umgesetzt als Grenzfall q -> 0 bei fester
      Newton-Kopplung G = kappa_g/kappa'^2 (Raum unendlich steif, Takt aus derselben Regel), PLAN Abschnitt 2.
Statik mit Einheitskopplung (G = 1), fuer jedes Gitter-k != 0 (Bloch, Konvention ew.py):
  KKT  [B, -c, M; -c^H, 0, 0; M^H, 0, 0] [a_hat; mu; lam] = [0; -m; 0]     (Eichwahl M^H a = 0)
  Formel (GAMMA-NETZ-L 5.2): P = -W^H B W, mu = -P^{-1} m, a_hat = -W mu + Eichung; physikalisch a = q a_hat.
Messgroessen: mu (Lapse-Stoerung), psi aus a_hat = W psi + M xi (Eck-Skalierung), Fehlwinkel d_eps = -(B a)/l,
  gamma_S = -2 q psi/mu (je Ecke), gamma_K = Fehlwinkel gegen Kontinuum-Referenz mit gamma = 1 (je Kante, Schale).
Quellen: Punkt auf P0 (Finn-Ecke), C1 (Lochmitte), H0 (Sechseckmitte); Q-Ball (Papier I, U = S - S^2 + S^3/2,
  omega = 0,8, 1 Q-Ball-Laengeneinheit = 1 Finn-Kante l_P) um C1, nur als Energieprofil.
Maxwell (beschreibend): licht_netz.py (LICHT-FINN-NETZ-1, unveraendert) maxwell_diamant, Einheitsgewichte gegen
  Gewichte aus Laengen (Hodge-Form), gleichmaessige Streckung lambda bei gleichem Takt.
Aufruf nur ueber kleintest.sh auf der .69:
  python mn.py statik --L 24 --out lauf/statik-L24.json
  python mn.py maxwell --out lauf/maxwell.json
  python mn.py auswertung --ein lauf/statik-L16.json lauf/statik-L24.json [lauf/statik-L32.json] --maxwell lauf/maxwell.json
      --primaer 24 --out lauf/auswertung.json --bild lauf/bild-materie-netz.png
"""
import argparse, json, sys, time, platform, os, resource, hashlib, itertools, math
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ew  # noqa: E402  (EINE-WELT-LOCH-1, sha256 fa7b6417..., unveraendert)

LP = math.sqrt(2.0) / 4.0          # Finn-Kante l_P in kubischen Einheiten = Gitterabstand
VCELL = 0.25                       # Volumen der primitiven Zelle (kubisch)
Q_V1, Q_V2 = 0.5, 0.0              # q = kappa'/kappa_g
OMEGA_QB = 0.8
QUELLEN = [('P0', 0, 'punkt'), ('C1', 4, 'punkt'), ('H0', 6, 'punkt'), ('QB', 4, 'qball')]


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def cT(X):
    return np.conj(np.swapaxes(X, -1, -2))


# ------------------------------------------------------------------------------------------------ Bausteine
def W_of(mod, k):
    """Eck-Skalierung -> Kantendehnung, gleiche Phasen wie crow in ew.ops: a_e = phi_s + e^{ik.T_e} phi_s2."""
    sh = k.shape[:-1]
    W = np.zeros(sh + (mod['E'], mod['nV']), complex)
    for e, (s, s2, n2) in enumerate(mod['kliste']):
        ph = np.exp(1j * (k @ mod['T'][e]))
        W[..., e, s] += 1.0
        W[..., e, s2] += ph
    return W


def min_bild(d, L):
    """Kuerzestes Bild von d (..., 3, kubisch) auf dem Torus mit Superzelle L * a_i."""
    S = L * ew.AV
    f = d @ np.linalg.inv(S)
    d0 = (f - np.rint(f)) @ S
    best = d0.copy()
    bn = np.linalg.norm(d0, axis=-1)
    for s in itertools.product((-1, 0, 1), repeat=3):
        if s == (0, 0, 0):
            continue
        dd = d0 + np.array(s, float) @ S
        nn = np.linalg.norm(dd, axis=-1)
        sel = nn < bn - 1e-12
        best[sel] = dd[sel]
        bn[sel] = nn[sel]
    return best, bn


def qball(om=OMEGA_QB, beta=0.5, rmax=40.0):
    """Papier I: f'' + 2/r f' = (1 - om^2) f - 2 f^3 + 3 beta f^5; Schiessen auf f(0) (Bisektion)."""
    from scipy.integrate import solve_ivp
    F = lambda f: (1 - om ** 2) * f - 2 * f ** 3 + 3 * beta * f ** 5
    disk = 1 - 4 * beta * (1 - om ** 2)
    S0 = (1 - math.sqrt(disk)) / (2 * beta)                     # V(f) = 0 (nichttrivial)
    Sp = (2 + math.sqrt(4 - 12 * beta * (1 - om ** 2))) / (6 * beta)   # Minimum von V
    lo, hi = math.sqrt(S0) * (1 + 1e-9), math.sqrt(Sp) * (1 - 1e-9)

    def rhs(r, y):
        return [y[1], F(y[0]) - 2.0 / r * y[1]]

    def ev_null(r, y):
        return y[0]
    ev_null.terminal = True
    ev_null.direction = -1

    def ev_umkehr(r, y):
        return y[1]
    ev_umkehr.terminal = True
    ev_umkehr.direction = 1

    def schiess(f0, dense=False):
        r0 = 1e-4
        y0 = [f0 + F(f0) * r0 ** 2 / 6.0, F(f0) * r0 / 3.0]
        return solve_ivp(rhs, (r0, rmax), y0, method='DOP853', rtol=1e-12, atol=1e-14, events=(ev_null, ev_umkehr),
                         dense_output=dense)
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        s = schiess(mid)
        if len(s.t_events[0]):
            hi = mid          # Ueberschuss
        else:
            lo = mid          # Unterschuss (oder unentschieden)
    f0 = 0.5 * (lo + hi)
    s = schiess(f0, dense=True)
    rr = np.linspace(1e-4, s.t[-1], 20001)
    y = s.sol(rr)
    f, fp = y[0], y[1]
    # bis zum kleinsten positiven f vor dem Abweichen; danach Schwanz e^{-kappa r}/r
    icut = int(np.argmin(np.where(f > 0, f, np.inf)))
    kap = math.sqrt(1 - om ** 2)
    r_all = np.linspace(0.0, rmax, 40001)
    f_all = np.interp(r_all, rr[:icut + 1], f[:icut + 1])
    fp_all = np.interp(r_all, rr[:icut + 1], fp[:icut + 1])
    rc = rr[icut]
    tail = r_all > rc
    f_all[tail] = f[icut] * np.exp(-kap * (r_all[tail] - rc)) * rc / r_all[tail]
    fp_all[tail] = -f_all[tail] * (kap + 1.0 / r_all[tail])
    S = f_all ** 2
    rho = om ** 2 * S + fp_all ** 2 + (S - S ** 2 + beta * S ** 3)
    Etot = float(np.trapezoid(4 * np.pi * rho * r_all ** 2, r_all))
    Mr = np.concatenate([[0.0], np.cumsum(0.5 * (4 * np.pi * rho[1:] * r_all[1:] ** 2 + 4 * np.pi * rho[:-1] * r_all[:-1] ** 2) * np.diff(r_all))])
    g = 4 * np.pi * rho * r_all
    Ir = np.concatenate([[0.0], np.cumsum(0.5 * (g[1:] + g[:-1]) * np.diff(r_all))])
    aussen = Ir[-1] - Ir
    with np.errstate(divide='ignore', invalid='ignore'):
        phi = -(np.where(r_all > 0, Mr / np.where(r_all > 0, r_all, 1.0), 0.0) + aussen) / Etot   # Kontinuum, Gesamtenergie 1
    r_halb = float(np.interp(0.5 * Etot, Mr, r_all))
    r_99 = float(np.interp(0.99 * Etot, Mr, r_all))
    return {'om': om, 'f0': f0, 'r_cut': float(rc), 'Etot': Etot, 'r_halb': r_halb, 'r_99': r_99,
            'r': r_all, 'rho': rho, 'phi': phi, 'bisektion_breite': hi - lo}


def zeile_mittel_1r(p, d):
    """Mittel von 1/|x| laengs x = p + s d, s in [0, 1] (p, d: (..., 3))."""
    dl = np.linalg.norm(d, axis=-1)
    dh = d / dl[..., None]
    t1 = np.einsum('...i,...i->...', p, dh)
    t2 = t1 + dl
    b = np.linalg.norm(np.cross(p, dh), axis=-1)
    with np.errstate(divide='ignore', invalid='ignore'):
        I = np.where(b > 1e-12, np.arcsinh(t2 / np.where(b > 1e-12, b, 1.0)) - np.arcsinh(t1 / np.where(b > 1e-12, b, 1.0)),
                     np.sign(t2) * np.log(np.abs(t2) / np.abs(t1)))
    return I / dl


def zeile_mittel_r2(p, d):
    return np.einsum('...i,...i->...', p, p) + np.einsum('...i,...i->...', p, d) + np.einsum('...i,...i->...', d, d) / 3.0


# ------------------------------------------------------------------------------------------------ Statik
def statik(L, chunk=96, r_nah=6.0):
    t0 = time.time()
    mod = ew.baue('V')
    E, nV = mod['E'], mod['nV']
    lv = mod['l']
    pos = np.array(mod['pos'])
    vv = np.zeros(nV)
    for z in mod['zellen']:
        for (s, n) in z['ids']:
            vv[s] += z['vol'] / 4.0
    Vtor = L ** 3 * VCELL / LP ** 3                     # in l_P^3
    g = np.arange(L)
    nn = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1)
    Rcell = nn @ ew.AV                                   # (L,L,L,3)
    kgrid = ((nn / L) @ ew.BV).reshape(-1, 3)           # flacher Index = (m1, m2, m3) in C-Ordnung
    N = L ** 3
    X = Rcell[..., None, :] + pos[None, None, None]      # (L,L,L,nV,3)
    out = {'L': L, 'N': N, 'E': E, 'nV': nV, 'Vtor_lP3': Vtor, 'R_in_lP': float(L),
           'eckvolumen_lP3': (vv / LP ** 3).tolist(), 'kantenlaengen_lP': sorted(set(round(float(x) / LP, 9) for x in lv))}
    # Quellen im Ortsraum
    qb = qball()
    out['qball'] = {k: (float(v) if not isinstance(v, np.ndarray) else None) for k, v in qb.items() if not isinstance(v, np.ndarray)}
    m_r, r_v = {}, {}
    for name, v0, art in QUELLEN:
        x0 = pos[v0]
        _, dist = min_bild(X - x0, L)
        r_v[name] = dist / LP
        m = np.zeros((L, L, L, nV))
        if art == 'punkt':
            m[0, 0, 0, v0] = 1.0
        else:
            rho = np.interp(r_v[name], qb['r'], qb['rho'], right=0.0)
            m = rho * (vv / LP ** 3)[None, None, None, :]
            out['qball']['gitter_summe_rel_Etot'] = float(m.sum() / qb['Etot'])
            m = m / m.sum()
        m_r[name] = m
    nq = len(QUELLEN)
    mk = np.stack([np.fft.fftn(m_r[nm], axes=(0, 1, 2)).reshape(N, nV) for nm, _, _ in QUELLEN], -1)   # (N, nV, nq)
    # Referenzdehnung (gamma = 1, A = 1): a_ref = -<f> laengs der Kante, f = -1/r - (2 pi/(3 V)) r^2 (r in l_P)
    punkt = [i for i, q in enumerate(QUELLEN) if q[2] == 'punkt']
    aref_k = np.zeros((N, E, len(punkt)), complex)
    r_mid = {}
    for j, iq in enumerate(punkt):
        name, v0, _ = QUELLEN[iq]
        x0 = pos[v0]
        ar = np.zeros((L, L, L, E))
        rm = np.zeros((L, L, L, E))
        for e, (s, s2, n2) in enumerate(mod['kliste']):
            dvec = pos[s2] + mod['T'][e] - pos[s]
            mid = Rcell + pos[s] + 0.5 * dvec
            dm, nm_ = min_bild(mid - x0, L)
            p = (dm - 0.5 * dvec) / LP
            d = np.broadcast_to(dvec / LP, p.shape)
            beruehrt = (np.linalg.norm(p, axis=-1) < 1e-9) | (np.linalg.norm(p + d, axis=-1) < 1e-9)
            with np.errstate(divide='ignore', invalid='ignore'):
                val = zeile_mittel_1r(p, d) + (2 * np.pi / (3 * Vtor)) * zeile_mittel_r2(p, d)
            val[beruehrt] = 0.0
            ar[..., e] = val
            rm[..., e] = nm_ / LP
        r_mid[name] = rm
        aref_k[:, :, j] = np.fft.fftn(ar, axes=(0, 1, 2)).reshape(N, E)
    t_vor = time.time() - t0
    # k-Schleife
    mu_k = np.zeros((N, nV, nq), complex)
    psi_k = np.zeros((N, nV, nq), complex)
    de_k = np.zeros((N, E, nq), complex)
    dr_k = np.zeros((N, E, len(punkt)), complex)
    kd = {'cBW_rel_max': 0.0, 'mu_kkt_gegen_formel_rel_max': 0.0, 'zerlegung_rest_rel_max': 0.0, 'psi_plus_mu_rel_max': 0.0,
          'kkt_rest_rel_max': 0.0, 'eich_MHa_rel_max': 0.0, 'P_lmin_rel_min': np.inf, 'P_k_mit_lmin_le_0': 0,
          'WM_sv_rel_min': np.inf}
    idx_all = np.arange(1, N)
    nK = E + nV + 3 * nV
    for i0 in range(0, len(idx_all), chunk):
        idx = idx_all[i0:i0 + chunk]
        k = kgrid[idx]
        o = ew.ops(mod, k)
        B, M, c = o['B'], o['M'], o['c']
        W = W_of(mod, k)
        BW = B @ W
        kd['cBW_rel_max'] = max(kd['cBW_rel_max'], float(np.abs(c + BW).max() / np.abs(c).max()))
        P = -cT(W) @ BW
        P = 0.5 * (P + cT(P))
        ev = np.linalg.eigvalsh(P)
        lrel = ev[:, 0] / np.abs(ev).max(-1)
        kd['P_lmin_rel_min'] = min(kd['P_lmin_rel_min'], float(lrel.min()))
        kd['P_k_mit_lmin_le_0'] += int((ev[:, 0] <= 0).sum())
        m = mk[idx]
        mu_f = -np.linalg.solve(P, m)
        K = np.zeros((len(idx), nK, nK), complex)
        K[:, :E, :E] = B
        K[:, :E, E:E + nV] = -c
        K[:, :E, E + nV:] = M
        K[:, E:E + nV, :E] = -cT(c)
        K[:, E + nV:, :E] = cT(M)
        rhs = np.zeros((len(idx), nK, nq), complex)
        rhs[:, E:E + nV, :] = -m
        sol = np.linalg.solve(K, rhs)
        kd['kkt_rest_rel_max'] = max(kd['kkt_rest_rel_max'], float(np.abs(K @ sol - rhs).max() / np.abs(rhs).max()))
        ah = sol[:, :E]
        mu = sol[:, E:E + nV]
        kd['mu_kkt_gegen_formel_rel_max'] = max(kd['mu_kkt_gegen_formel_rel_max'],
                                                float((np.linalg.norm(mu - mu_f, axis=1) / np.linalg.norm(mu_f, axis=1)).max()))
        kd['eich_MHa_rel_max'] = max(kd['eich_MHa_rel_max'], float((np.linalg.norm(cT(M) @ ah, axis=1) /
                                                                    (np.linalg.norm(M, axis=(1, 2))[:, None] * np.linalg.norm(ah, axis=1))).max()))
        WM = np.concatenate([W, M], -1)
        svw = np.linalg.svd(WM, compute_uv=False)
        kd['WM_sv_rel_min'] = min(kd['WM_sv_rel_min'], float((svw[:, -1] / svw[:, 0]).min()))
        coef = np.linalg.pinv(WM) @ ah
        rest = ah - WM @ coef
        kd['zerlegung_rest_rel_max'] = max(kd['zerlegung_rest_rel_max'], float((np.linalg.norm(rest, axis=1) / np.linalg.norm(ah, axis=1)).max()))
        psi = coef[:, :nV]
        kd['psi_plus_mu_rel_max'] = max(kd['psi_plus_mu_rel_max'], float((np.linalg.norm(psi + mu, axis=1) / np.linalg.norm(mu, axis=1)).max()))
        mu_k[idx] = mu
        psi_k[idx] = psi
        de_k[idx] = -(B @ ah) / lv[None, :, None]
        dr_k[idx] = -(B @ aref_k[idx]) / lv[None, :, None]
    t_k = time.time() - t0 - t_vor
    out['kontrollen'] = kd
    # weiche Richtung von P bei kleinem k (Newton-Normierung, Isotropie) und Luecken bei k -> 0
    kl = []
    for nm, d in ew.richtungen()[:3]:
        for eps in (1e-3, 2e-3):
            kk = (eps * d)[None, :]
            o = ew.ops(mod, kk)
            W = W_of(mod, kk)
            P = -cT(W) @ o['B'] @ W
            evp = np.linalg.eigvalsh(0.5 * (P + cT(P)))[0]
            kl.append({'richtung': nm, 'eps': eps, 'weich_ueber_k2': float(evp[0] / eps ** 2), 'rest': [float(x) for x in evp[1:]]})
    out['P_klein_k'] = kl

    # Ortsraum
    def zurueck(Xk, last):
        Xr = np.fft.ifftn(Xk.reshape((L, L, L) + Xk.shape[1:]), axes=(0, 1, 2))
        return Xr.real, float(np.abs(Xr.imag).max() / max(np.abs(Xr.real).max(), 1e-300))
    mu_r, im1 = zurueck(mu_k, None)
    psi_r, im2 = zurueck(psi_k, None)
    de_r, im3 = zurueck(de_k, None)
    dr_r, im4 = zurueck(dr_k, None)
    kd['imag_rel_max'] = max(im1, im2, im3, im4)
    # Auswertung je Quelle
    rf1, rf2 = 0.25 * L, 0.5 * L
    res = {}
    for iq, (name, v0, art) in enumerate(QUELLEN):
        r = r_v[name].ravel()
        mu = mu_r[..., iq].ravel()
        ps = psi_r[..., iq].ravel()
        sub = np.broadcast_to(np.arange(nV), (L, L, L, nV)).ravel()
        fern = (r >= rf1) & (r <= rf2)
        fr = lambda x: -1.0 / x - (2 * np.pi / (3 * Vtor)) * x ** 2
        Af = np.stack([fr(r[fern]), np.ones(fern.sum())], -1)
        (A, C), *_ = np.linalg.lstsq(Af, mu[fern], rcond=None)
        rms = float(np.sqrt(np.mean((Af @ np.array([A, C]) - mu[fern]) ** 2)) / np.abs(A * fr(r[fern])).mean())
        Af2 = np.stack([-1.0 / r[fern], r[fern] ** 2, np.ones(fern.sum())], -1)
        (A2, b2, C2), *_ = np.linalg.lstsq(Af2, mu[fern], rcond=None)
        z = {'art': art, 'ecke': v0, 'fit': {'band_lP': [rf1, rf2], 'n': int(fern.sum()), 'A': float(A), 'C': float(C), 'rms_rel': rms,
                                              'frei_A': float(A2), 'frei_beta': float(b2), 'beta_soll': float(-(2 * np.pi / (3 * Vtor)) * A),
                                              'frei_C': float(C2)}}
        # gamma_S je Ecke (Einheitskopplung: t = -psi/mu, gamma_S = 2 q t)
        gut = np.abs(mu) > 1e-6 * np.abs(mu).max()
        t = np.full_like(mu, np.nan)
        t[gut] = -ps[gut] / mu[gut]
        z['t_S_fern'] = {'min': float(np.nanmin(t[fern & gut])), 'max': float(np.nanmax(t[fern & gut])),
                         'median': float(np.nanmedian(t[fern & gut])), 'n': int((fern & gut).sum())}
        nah3 = r < 3.0
        z['t_S_nah3'] = {'min': float(np.nanmin(t[nah3 & gut])), 'max': float(np.nanmax(t[nah3 & gut])), 'n': int((nah3 & gut).sum())}
        z['mu_nah3_max'] = float(mu[nah3].max())
        z['mu_fern_median'] = float(np.median(mu[fern]))
        z['psi_nah3_min'] = float(ps[nah3].min())
        # Schalen
        sch = []
        kanten = np.arange(0.0, rf2 + 1e-9, 0.5)
        for a, b in zip(kanten[:-1], kanten[1:]):
            s = (r >= a) & (r < b)
            if not s.any():
                continue
            mm, pp = mu[s], ps[s]
            sch.append({'r0': float(a), 'r1': float(b), 'n': int(s.sum()), 'mu_mittel': float(mm.mean()), 'mu_min': float(mm.min()),
                        'mu_max': float(mm.max()), 'psi_mittel': float(pp.mean()),
                        't_S_steigung': float(-(pp * mm).sum() / (mm * mm).sum()) if (mm * mm).sum() > 0 else None,
                        'G_ratio_mittel': float(((mm - C) / (A * fr(np.maximum(r[s], 1e-9)))).mean()) if a > 0 else None})
        z['schalen'] = sch
        # Ecken nah (r <= r_nah) einzeln
        s = r <= r_nah
        z['nah_ecken'] = [[int(u), round(float(x), 6), float(y), float(w)] for u, x, y, w in zip(sub[s], r[s], mu[s], ps[s])]
        # Q-Ball: Kontinuum-Potential des Profils (Gesamtenergie 1) zum Vergleich
        if art == 'qball':
            phi_c = np.interp(r, qb['r'], qb['phi']) - (2 * np.pi / (3 * Vtor)) * r ** 2
            z['qball_vergleich'] = [{'r0': float(a), 'r1': float(b),
                                     'mu_minus_C_ueber_A_phi': float(((mu[(r >= a) & (r < b)] - C) / (A * phi_c[(r >= a) & (r < b)])).mean())}
                                    for a, b in zip(kanten[:-1], kanten[1:]) if ((r >= a) & (r < b)).any()]
        # gamma_K (Punktquellen): je Schale Steigung t_K = sum de dr / (A sum dr^2); gamma_K = q t_K
        if art == 'punkt':
            j = punkt.index(iq)
            rm = r_mid[name].ravel()
            de = de_r[..., iq].ravel()
            dr = dr_r[..., j].ravel()
            sk = []
            kk_ = np.arange(2.0, rf2 + 1e-9, 0.5)
            for a, b in zip(kk_[:-1], kk_[1:]):
                s = (rm >= a) & (rm < b)
                if not s.any():
                    continue
                num, den = float((de[s] * dr[s]).sum()), float((dr[s] ** 2).sum())
                gross = s & (np.abs(dr) >= 0.3 * np.abs(dr[s]).max())
                einz = de[gross] / (A * dr[gross])
                sk.append({'r0': float(a), 'r1': float(b), 'n': int(s.sum()), 't_K': num / (A * den) if den > 0 else None,
                           't_K_einzeln_min': float(einz.min()), 't_K_einzeln_max': float(einz.max())})
            z['schalen_K'] = sk
            sf = (rm >= rf1) & (rm <= rf2)
            z['t_K_fern'] = float((de[sf] * dr[sf]).sum() / (A * (dr[sf] ** 2).sum()))
            # Vorzeichen der Fehlwinkel am naechsten Ring (beschreibend)
        res[name] = z
    out['quellen'] = res
    out['zeiten_s'] = {'vorbereitung': t_vor, 'k_schleife': t_k, 'gesamt': time.time() - t0}
    return out


# ------------------------------------------------------------------------------------------------ Maxwell
def maxwell():
    import licht_netz as ln
    C_of, G_of, nknoten, nringe = ln.maxwell_diamant()
    # Geometrie fuer Hodge-Gewichte: Bindungslaenge, Ringflaeche, Volumen je Bindung und je Ring (ganzes Netz homogen)
    ringe = ln.sechsringe()
    E8 = ln.AC / 8.0
    out = {'nringe': nringe, 'zeilen': []}
    vzelle = ln.AC ** 3 / 4.0
    for lam in (1.0, 1.01, 1.1):
        b = lam * ln.B_LEN
        flaechen = []
        for kant, posr in ringe:
            P = lam * np.array(posr[:-1], float) * E8
            cpt = P.mean(0)
            A = 0.5 * np.linalg.norm(sum(np.cross(P[i] - cpt, P[(i + 1) % 6] - cpt) for i in range(6)))
            flaechen.append(A)
        Ar = float(np.mean(flaechen))
        V = lam ** 3 * vzelle
        w_link = (3.0 * V / 4.0) / b ** 2          # |*e|/|e| mit |*e| = 3 V_e/|e|, V_e = V/4 (4 Bindungen je Zelle)
        u_ring = (3.0 * V / nringe) / Ar ** 2      # |*f|/|f| mit |*f| = 3 V_f/|f|
        if lam == 1.0:
            w0, u0 = w_link, u_ring
        for nm, d in (('100', np.array([1., 0, 0])), ('110', np.array([1., 1, 0]) / math.sqrt(2)), ('111', np.array([1., 1, 1]) / math.sqrt(3))):
            for eps in (1e-3,):
                kl = eps * d                           # Gitter-k (in 1/PU des ungestreckten Netzes)
                C = C_of(kl)
                e1 = np.linalg.eigvalsh(cT(C) @ C)[nknoten:]
                e2 = np.linalg.eigvalsh((u_ring / u0) / (w_link / w0) * (cT(C) @ C))[nknoten:]
                for kop, ee in (('einheit', e1), ('laengen', e2)):
                    om = np.sqrt(np.maximum(ee, 0))
                    out['zeilen'].append({'lambda': lam, 'richtung': nm, 'kopplung': kop,
                                          'c_gitter': [float(x / eps) for x in om],
                                          'c_physikalisch': [float(x / (eps / lam)) for x in om]})
        out.setdefault('gewichte', []).append({'lambda': lam, 'w_rel': w_link / w0, 'u_rel': u_ring / u0, 'ringflaeche': Ar, 'bindung': b})
    return out


# ------------------------------------------------------------------------------------------------ Auswertung
def auswertung(pfade, pfad_mx, primaer, pfad_bild):
    lauf = {}
    for p in pfade:
        with open(p) as f:
            d = json.load(f)
        lauf[d['statik']['L']] = d['statik']
    P = lauf[primaer]
    q = P['quellen']
    out = {'primaer_L': primaer, 'urteile': {}, 'kennzahlen': {}}
    tol0 = 0.05
    # MN0
    def mn0(var_q, ziel):
        plan, wort, K = True, True, True
        det = {}
        for nm, z in q.items():
            lo, hi = 2 * var_q * z['t_S_fern']['min'], 2 * var_q * z['t_S_fern']['max']
            ok_p = (abs(lo - ziel) <= tol0) and (abs(hi - ziel) <= tol0)
            fs = [s for s in z['schalen'] if s['r0'] >= z['fit']['band_lP'][0] and s['r1'] <= z['fit']['band_lP'][1] + 1e-9]
            gs = [2 * var_q * s['t_S_steigung'] for s in fs]
            ok_w = all(abs(g - ziel) <= tol0 for g in gs)
            det[nm] = {'gamma_S_fern_min': lo, 'gamma_S_fern_max': hi, 'gamma_S_schalen_min': min(gs), 'gamma_S_schalen_max': max(gs)}
            if 'schalen_K' in z:
                gK = var_q * z['t_K_fern']
                det[nm]['gamma_K_fern'] = gK
                K = K and abs(gK - ziel) <= tol0
            plan, wort = plan and ok_p, wort and ok_w
        return plan, wort, K, det
    p1, w1, k1, d1 = mn0(Q_V1, 1.0)
    p2, w2, k2, d2 = mn0(Q_V2, 0.0)
    E = lambda b: 'eingetroffen' if b else 'nicht eingetroffen'
    out['urteile']['MN0'] = {'plan': E(p1 and p2), 'kartenwortlaut': E(w1 and w2), 'lesart_K': E(k1 and k2),
                             'V1': d1, 'V2': d2}
    # MN1 (V1)
    plan, wort, K = False, False, False
    det = {}
    for nm, z in q.items():
        gf = 2 * Q_V1 * z['t_S_fern']['median']
        gn = [2 * Q_V1 * z['t_S_nah3']['min'], 2 * Q_V1 * z['t_S_nah3']['max']]
        dev_p = max(abs(x - gf) / abs(gf) for x in gn)
        gfs = np.median([2 * Q_V1 * s['t_S_steigung'] for s in z['schalen'] if s['r0'] >= z['fit']['band_lP'][0] and s['r1'] <= z['fit']['band_lP'][1] + 1e-9])
        nahs = [2 * Q_V1 * s['t_S_steigung'] for s in z['schalen'] if s['r1'] <= 3.0 + 1e-9]
        dev_w = max(abs(x - gfs) / abs(gfs) for x in nahs)
        det[nm] = {'gamma_S_fern': gf, 'gamma_S_nah_min': gn[0], 'gamma_S_nah_max': gn[1], 'abw_plan': dev_p, 'abw_wort': dev_w}
        plan, wort = plan or dev_p > 0.10, wort or dev_w > 0.10
        if 'schalen_K' in z:
            gKf = Q_V1 * z['t_K_fern']
            nk = [Q_V1 * s['t_K'] for s in z['schalen_K'] if s['r1'] <= 3.0 + 1e-9 and s['t_K'] is not None]
            dk = max(abs(x - gKf) / abs(gKf) for x in nk) if nk else None
            det[nm].update({'gamma_K_fern': gKf, 'gamma_K_nah_schalen': nk, 'abw_K': dk})
            K = K or (dk is not None and dk > 0.10)
    out['urteile']['MN1'] = {'plan': E(plan), 'kartenwortlaut': E(wort), 'lesart_K': E(K), 'det': det}
    # MN2 (beide Varianten; Takt identisch nach Festlegung F)
    plan, wort = True, True
    det = {}
    for nm, z in q.items():
        A, C = z['fit']['A'], z['fit']['C']
        ok_p = (A > 0) and (z['mu_nah3_max'] < C)
        ok_w = z['mu_nah3_max'] < z['mu_fern_median']
        det[nm] = {'A': A, 'C': C, 'mu_nah3_max': z['mu_nah3_max'], 'mu_fern_median': z['mu_fern_median'],
                   'raum_V1_psi_nah3_min_mal_q': Q_V1 * z['psi_nah3_min']}
        plan, wort = plan and ok_p, wort and ok_w
    out['urteile']['MN2'] = {'plan': E(plan), 'kartenwortlaut': E(wort), 'det': det}
    # Kennzahlen ueber alle L
    for L, d in sorted(lauf.items()):
        out['kennzahlen'][str(L)] = {'kontrollen': d['kontrollen'], 'A': {nm: z['fit']['A'] for nm, z in d['quellen'].items()},
                                     'rms_rel': {nm: z['fit']['rms_rel'] for nm, z in d['quellen'].items()},
                                     'P_klein_k': d['P_klein_k']}
    if pfad_mx:
        with open(pfad_mx) as f:
            out['maxwell'] = json.load(f)['maxwell']
    if pfad_bild:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(2, 2, figsize=(13, 9.5))
        farben = {'P0': '#1f77b4', 'C1': '#d62728', 'H0': '#2ca02c', 'QB': '#9467bd'}
        a0 = ax[0, 0]
        for nm, z in q.items():
            ee = np.array(z['nah_ecken'])
            a0.plot(ee[:, 1], ee[:, 2] - z['fit']['C'], '.', ms=3, color=farben[nm], label='%s Ecken' % nm)
            rr = np.linspace(0.3, 6, 200)
            a0.plot(rr, z['fit']['A'] * (-1 / rr), '-', lw=0.8, color=farben[nm])
        a0.set_xlabel('r / l_P'); a0.set_ylabel('mu - C (Takt-Stoerung, G = 1)'); a0.set_title('Lapse je Ecke; Linien: -A/r (Fernfit)')
        a0.set_ylim(-1.2 * max(z['fit']['A'] for z in q.values()), 0.05 * max(z['fit']['A'] for z in q.values())); a0.legend(fontsize=7)
        a1 = ax[0, 1]
        for nm, z in q.items():
            rs = [0.5 * (s['r0'] + s['r1']) for s in z['schalen'] if s['r0'] > 0]
            gr = [s['G_ratio_mittel'] for s in z['schalen'] if s['r0'] > 0]
            a1.plot(rs, gr, 'o-', ms=3, color=farben[nm], label=nm)
        a1.axhline(1, color='k', lw=0.5); a1.set_xlabel('r / l_P'); a1.set_ylabel('(mu - C) / (A f(r)), Schalenmittel')
        a1.set_title('Newton-Verhaeltnis G(r)/G_fern'); a1.legend(fontsize=7)
        a2 = ax[1, 0]
        for nm, z in q.items():
            rs = [0.5 * (s['r0'] + s['r1']) for s in z['schalen']]
            a2.plot(rs, [2 * Q_V1 * s['t_S_steigung'] for s in z['schalen']], 'o-', ms=3, color=farben[nm], label='V1 ' + nm)
            a2.plot(rs, [2 * Q_V2 * s['t_S_steigung'] for s in z['schalen']], 'x--', ms=3, color=farben[nm], label='V2 ' + nm)
        a2.set_xlabel('r / l_P'); a2.set_ylabel('gamma_S (Eck-Skalierung)'); a2.set_title('gamma_S(r): V1 (o), V2 (x)')
        a2.set_ylim(-0.2, 1.3); a2.legend(fontsize=6, ncol=2)
        a3 = ax[1, 1]
        for nm, z in q.items():
            if 'schalen_K' not in z:
                continue
            rs = [0.5 * (s['r0'] + s['r1']) for s in z['schalen_K']]
            a3.plot(rs, [Q_V1 * s['t_K'] for s in z['schalen_K']], 'o-', ms=3, color=farben[nm], label='V1 ' + nm)
        a3.axhline(1, color='k', lw=0.5); a3.set_xlabel('r / l_P (Kantenmitte)'); a3.set_ylabel('gamma_K (Fehlwinkel gegen Kontinuum)')
        a3.set_title('gamma_K(r), V1, Punktquellen (V2: 0)'); a3.legend(fontsize=7)
        fig.suptitle('MATERIE-NETZ-1, gefuelltes Netz V, L = %d (synthetische Gitterrechnung)' % primaer)
        fig.tight_layout()
        fig.savefig(pfad_bild + '.tmp.png', dpi=110)
        os.replace(pfad_bild + '.tmp.png', pfad_bild)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['statik', 'maxwell', 'auswertung'])
    ap.add_argument('--L', type=int, default=24)
    ap.add_argument('--ein', nargs='*')
    ap.add_argument('--maxwell')
    ap.add_argument('--primaer', type=int, default=24)
    ap.add_argument('--bild')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    info = {'numpy': np.__version__, 'python': platform.python_version(), 'host': platform.node(),
            'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'argv': sys.argv,
            'skript_sha256': sha(os.path.abspath(__file__)), 'ew_sha256': sha(os.path.abspath(ew.__file__))}
    res = {'info': info}
    if a.modus == 'statik':
        res['statik'] = statik(a.L)
    elif a.modus == 'maxwell':
        import licht_netz
        info['licht_netz_sha256'] = sha(os.path.abspath(licht_netz.__file__))
        res['maxwell'] = maxwell()
    else:
        info['eingaben_sha256'] = {p: sha(p) for p in a.ein + ([a.maxwell] if a.maxwell else [])}
        res['auswertung'] = auswertung(a.ein, a.maxwell, a.primaer, a.bild)
    res['laufzeit_s'] = time.time() - t0
    res['maxrss_MB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    res['ende_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    with open(a.out + '.tmp', 'w') as f:
        json.dump(res, f, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
    os.replace(a.out + '.tmp', a.out)
    print('fertig', a.modus, 'L=%d' % a.L if a.modus == 'statik' else '', 'laufzeit %.1f s' % res['laufzeit_s'],
          'maxrss %.0f MB' % res['maxrss_MB'], flush=True)


if __name__ == '__main__':
    main()
