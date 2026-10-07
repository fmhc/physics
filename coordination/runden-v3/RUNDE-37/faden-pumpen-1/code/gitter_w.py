#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""FADEN-PUMPEN-1 (Runde 50), Rechen-Agent fuer die Leitung claude-primary, 05.10.2026.

Gerader Faden laengs einer Gitterachse auf Finns Netz V (Sterne wie SCHWERE-MASSE-V: sm.stern_daten, unveraendert
importiert) oder auf einem einfachen kubischen Gitter SC (Kontrolle). Superzelle: L x L Zellen quer, 1 Zelle laengs
(Achse = Gittervektor b3; V: [100], b1 = a1, b2 = a2, b3 = (1,0,0) a; SC: z). Stoerungen laengs per Bloch-Phase
exp(i k d_e.z) je Kante (d_e = Kantenvektor), also jedes k ohne lange Kiste.
h = Kantenlaenge (V: l_P, SC: Gitterabstand) in Feldeinheiten (m = 1).

 (a) Q-Schlauch: U(S) = S - S^2 + S^3/2. Stationaer: Minimum von q^2/(4 I2) + G + V bei fester Ladung je Periode
     (wie sm.py, L-BFGS-B). Linear: *0 u_tt = 2 om *0 v_t - K+ u, *0 v_tt = -2 om *0 u_t - K- v; 4N-Matrix, eigs nahe 0.
 (b) Wirbel: U_b(S) = (S - 1)^2 / 4, Phase dreht einmal um die Achse; Ecken mit r > R_D fest (Dirichlet).
     Linear: *0 x_tt = -Hess x, Omega^2 = Eigenwerte (eigsh nahe 0).
Formen: Zerlegung jeder Eigenform in Betrag (Re(psi0* dpsi)/|psi0|) und Phase (Im(...)/|psi0|), Winkelanteile n = 0..4
in Radialschalen.
Aufruf nur ueber kleintest.sh auf der .69:
  python gitter.py q --geo V --om 0.8 --h 1.5 --L 19 --out lauf/q-V-h1.5.json
  python gitter.py w --geo V --h 1.5 --L 19 --RD 14 --out lauf/w-V-h1.5.json
"""
import argparse, json, os, sys, time, math, hashlib, platform, resource
import numpy as np
import scipy
import scipy.sparse as sps
import scipy.sparse.linalg as spla
from scipy.optimize import minimize

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rad  # noqa: E402

T0 = time.time()


def log(*a):
    print('[%7.1f s]' % (time.time() - T0), *a, flush=True)


def sha(p):
    with open(p, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def schreibe(pfad, res):
    d = os.path.dirname(os.path.abspath(__file__))
    res['_meta'] = {'argv': sys.argv, 'python': platform.python_version(), 'numpy': np.__version__,
                    'scipy': scipy.__version__, 'host': platform.node(), 'laufzeit_s': time.time() - T0,
                    'maxrss_MB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
                    'ende_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
                    'sha256': {f: sha(os.path.join(d, f)) for f in ('gitter_w.py', 'gitter_z.py', 'gitter.py', 'rad.py', 'sm.py', 'ew.py', 'mn.py', 'rv.py')}}
    with open(pfad + '.tmp', 'w') as fh:
        json.dump(res, fh, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
    os.replace(pfad + '.tmp', pfad)
    log('->', pfad)


# ------------------------------------------------------------------------------------------------ Netz
def netz(geo):
    if geo == 'V':
        import sm
        sd = sm.stern_daten()
        mod = sd['mod']
        pos = np.array(mod['pos'], float)
        AV = sm.ew.AV
        kanten = []
        for e, (s, s2, n2) in enumerate(mod['kliste']):
            kanten.append((s, s2, np.array(n2, float) @ AV, float(sd['s1_lP'][e])))
        B = np.array([AV[0], AV[1], [1.0, 0.0, 0.0]])
        return {'geo': 'V', 'pos': pos, 'kanten': kanten, 's0': np.asarray(sd['s0_lP'], float), 'lp': sm.LP, 'B': B,
                'zentrum': pos[4].copy(), 'kontr': sd['kontr']}
    if geo == 'SC':
        pos = np.zeros((1, 3))
        kanten = [(0, 0, np.array(v, float), 1.0) for v in ((1, 0, 0), (0, 1, 0), (0, 0, 1))]
        return {'geo': 'SC', 'pos': pos, 'kanten': kanten, 's0': np.array([1.0]), 'lp': 1.0, 'B': np.eye(3),
                'zentrum': np.array([0.5, 0.5, 0.0])}
    raise ValueError(geo)


def superzelle(nz, L, h):
    pos, B = nz['pos'], nz['B']
    nV = len(pos)
    Binv = np.linalg.inv(B)
    ach = B[2] / np.linalg.norm(B[2])
    g = np.arange(L)
    nn = np.stack(np.meshgrid(g, g, indexing='ij'), -1).reshape(-1, 2)
    N = L * L * nV

    def idx(c1, c2, s):
        return (np.mod(c1, L) * L + np.mod(c2, L)) * nV + s
    tl, hd, w1, dz = [], [], [], []
    for (s, s2, T, w) in nz['kanten']:
        c = T @ Binv
        ci = np.rint(c).astype(int)
        assert np.abs(c - ci).max() < 1e-9, (T, c)
        d = pos[s2] + T - pos[s]
        tl.append(idx(nn[:, 0], nn[:, 1], s))
        hd.append(idx(nn[:, 0] + ci[0], nn[:, 1] + ci[1], s2))
        w1.append(np.full(len(nn), w))
        dz.append(np.full(len(nn), float(d @ ach)))
    tl, hd, w1, dz = map(np.concatenate, (tl, hd, w1, dz))
    # Ortsvektoren, Abstand zur Achse (kleinstes Bild quer), Winkel
    X = (nn[:, None, :] @ B[None, :2, :])[:, 0, :][:, None, :] + pos[None, :, :]
    X = X.reshape(-1, 3)
    P0 = nz['zentrum'] + (L // 2) * B[0] + (L // 2) * B[1]
    dX = X - P0
    dX = dX - np.outer(dX @ ach, ach)
    Bq = np.array([B[0] - (B[0] @ ach) * ach, B[1] - (B[1] @ ach) * ach]) * L
    G2 = Bq @ Bq.T
    best = None
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            Y = dX + i * Bq[0] + j * Bq[1]
            # vorab reduzieren
            if best is None:
                best = Y.copy()
            else:
                sel = np.linalg.norm(Y, axis=1) < np.linalg.norm(best, axis=1) - 1e-12
                best[sel] = Y[sel]
    e1 = Bq[0] / np.linalg.norm(Bq[0])
    e2 = np.cross(ach, e1)
    xq, yq = best @ e1, best @ e2
    r = np.hypot(xq, yq) / nz['lp'] * h          # Feldeinheiten
    th = np.arctan2(yq, xq)
    s0v = np.tile(nz['s0'], L * L) * h ** 3
    s1e = w1 * h
    dzq = dz / nz['lp'] * h                       # Laengsanteil der Kante in Feldeinheiten
    perz = float(np.linalg.norm(B[2])) / nz['lp'] * h
    breite = float(min(np.linalg.norm(Bq[0]), np.linalg.norm(Bq[1]))) / nz['lp'] * h
    return {'N': N, 'tl': tl, 'hd': hd, 's1e': s1e, 's0v': s0v, 'dz': dzq, 'r': r, 'th': th, 'periode': perz,
            'kiste_quer': breite, 'nV': nV, 'L': L}


def Dmat(sz, k, frei=None):
    ne = len(sz['tl'])
    ph = np.exp(1j * k * sz['dz'])
    rows = np.concatenate([np.arange(ne), np.arange(ne)])
    cols = np.concatenate([sz['hd'], sz['tl']])
    vals = np.concatenate([ph, -np.ones(ne)])
    D = sps.csr_matrix((vals, (rows, cols)), shape=(ne, sz['N']))
    if frei is not None:
        D = D[:, frei]
    return D


def lap(sz, k, frei=None):
    D = Dmat(sz, k, frei)
    return (D.conj().T @ sps.diags(sz['s1e']) @ D).tocsr()


# ------------------------------------------------------------------------------------------------ Formen
def formen(sz, psi0, du, dv, frei, nmax=4):
    """Winkelanteile von Betrag und Phase der Stoerung (komplexe Bloch-Amplituden du, dv der reellen Felder)."""
    a, b = psi0.real[frei], psi0.imag[frei]
    rho = np.sqrt(a * a + b * b) + 1e-300
    dr_ = (a * du + b * dv) / rho
    dth = (a * dv - b * du) / rho
    r, th, w = sz['r'][frei], sz['th'][frei], sz['s0v'][frei]
    sh = np.floor(r / max(0.5 * sz['periode'] / 2.0, 0.25)).astype(int)
    p = np.zeros(nmax + 1)
    for s in np.unique(sh):
        m = sh == s
        for n in range(nmax + 1):
            for q in (dr_, dth):
                cp = np.sum(w[m] * q[m] * np.exp(-1j * n * th[m]))
                cm = np.sum(w[m] * q[m] * np.exp(1j * n * th[m]))
                p[n] += abs(cp) ** 2 + (abs(cm) ** 2 if n > 0 else 0.0)
    p = p / max(p.sum(), 1e-300)
    nb = float(np.sum(w * np.abs(dr_) ** 2))
    nph = float(np.sum(w * np.abs(dth) ** 2))
    tot = float(np.sum(w * (np.abs(du) ** 2 + np.abs(dv) ** 2)))
    return {'n_anteile': [float(x) for x in p], 'n_dominant': int(np.argmax(p)), 'betrag_anteil': nb / max(nb + nph, 1e-300),
            'r_schwer': float(np.sum(w * (np.abs(du) ** 2 + np.abs(dv) ** 2) * r) / max(tot, 1e-300))}


# ------------------------------------------------------------------------------------------------ (a) Q-Schlauch
def stationaer_q(sz, om, h, qlaenge, f_start, maxiter, tmax):
    D = Dmat(sz, 0.0).real.tocsr()
    s0, s1 = sz['s0v'], sz['s1e']
    Qz = qlaenge * sz['periode']
    w = np.sqrt(s0)
    t0 = time.time()

    def fg(u):
        f = u / w
        I2 = float(u @ u)
        df = D @ f
        S = f * f
        E = Qz * Qz / (4 * I2) + float(s1 @ (df * df)) + float(s0 @ rad.U(S))
        gf = 2.0 * (D.T @ (s1 * df)) + 2.0 * s0 * rad.Up(S) * f
        return E, gf / w - (Qz * Qz / (2 * I2 * I2)) * u

    def cb(xk):
        if time.time() - t0 > tmax:
            raise StopIteration
    r = minimize(fg, w * f_start, jac=True, method='L-BFGS-B', callback=cb,
                 options={'maxiter': maxiter, 'maxfun': 3 * maxiter, 'ftol': 0.0, 'gtol': 1e-12, 'maxcor': 30})
    u = r.x
    E, gu = fg(u)
    I2 = float(u @ u)
    om_l = Qz / (2 * I2)
    f = u / w
    S = f * f
    df = D @ f
    G = float(s1 @ (df * df))
    V = float(s0 @ rad.U(S))
    # Feldgleichungsrest bei om_l
    Fv = (D.T @ (s1 * df)) + s0 * (rad.Up(S) - om_l ** 2) * f
    rest = float(np.linalg.norm(Fv) / np.linalg.norm(s0 * om_l ** 2 * f))
    cum = np.cumsum((s0 * S)[np.argsort(sz['r'])])
    r_halb = float(np.interp(0.5 * I2, cum, np.sort(sz['r'])))
    return f, {'Q_periode': Qz, 'om_gitter': om_l, 'E_periode': E, 'E_je_Laenge': E / sz['periode'],
               'q_je_Laenge': Qz / sz['periode'], 'G_je_Laenge': G / sz['periode'], 'V_je_Laenge': V / sz['periode'],
               'I_je_Laenge': I2 / sz['periode'], 'cb2_T_durch_mu_naiv': (G / sz['periode']) / (E / sz['periode']),
               'rest_rel': rest, 'r_halb': r_halb, 'f_max': float(f.max()),
               'rand_anteil': float((s0 * S)[sz['r'] > 0.45 * sz['kiste_quer']].sum() / I2),
               'nit': int(r.nit), 'status': int(r.status), 'meldung': str(r.message), 'zeit_s': time.time() - t0}


def spektrum_q(sz, f, om, k, nev=24, sigma=1e-3):
    N = sz['N']
    S = f * f
    s0 = sz['s0v']
    Lk = lap(sz, k)
    mi = sps.diags(1.0 / np.sqrt(s0))
    Hp = (mi @ (Lk + sps.diags(s0 * (rad.Up(S) + 2 * S * rad.Upp(S) - om ** 2))) @ mi).tocsr()
    Hm = (mi @ (Lk + sps.diags(s0 * (rad.Up(S) - om ** 2))) @ mi).tocsr()
    I = sps.identity(N, format='csr', dtype=complex)
    Z = sps.csr_matrix((N, N), dtype=complex)
    A = sps.bmat([[Z, Z, I, Z], [Z, Z, Z, I], [-Hp, Z, Z, 2 * om * I], [Z, -Hm, -2 * om * I, Z]], format='csc')
    w, vec = spla.eigs(A, k=nev, sigma=sigma, which='LM', tol=1e-10)
    out = []
    psi0 = f.astype(complex)
    frei = np.arange(N)
    for j in range(len(w)):
        if w[j].imag < -1e-9:
            continue
        x = vec[:, j]
        du, dv = x[:N] / np.sqrt(s0), x[N:2 * N] / np.sqrt(s0)
        d = {'re': float(w[j].real), 'im': float(w[j].imag)}
        d.update(formen(sz, psi0, du, dv, frei))
        out.append(d)
    out.sort(key=lambda d: (d['im'], -d['re']))
    return out


def modus_q(a):
    nz = netz(a.geo)
    if a.zentrum is not None:
        nz['zentrum'] = np.array(a.zentrum, float)
        log('Zentrum (kubische Einheiten des Netzes) gesetzt auf', a.zentrum)
    h = a.h
    sz = superzelle(nz, a.L, h)
    log('Superzelle', a.geo, 'L', a.L, 'N', sz['N'], 'Periode', sz['periode'], 'Kiste quer', sz['kiste_quer'], 'h', h)
    R = rad.Radial(0.02, 60.0)
    fk, info = rad.profil_q(a.om, R)
    kk = rad.kenn_q(a.om, R, fk)
    f_start = np.interp(sz['r'], R.r, fk, right=0.0)
    f, st = stationaer_q(sz, a.om, h, kk['q'], f_start, a.maxiter, a.tmax)
    log('stationaer', st)
    res = {'geo': a.geo, 'h': h, 'L': a.L, 'N': sz['N'], 'om_kont': a.om, 'kont': kk, 'stationaer': st,
           'periode': sz['periode'], 'kiste_quer': sz['kiste_quer'], 'durchmesser_kanten': 2 * kk['r_halb'] / h,
           'k_bz_rand': math.pi / sz['periode'], 'spektren': []}
    om = st['om_gitter']
    kbz = math.pi / sz['periode']
    ks = sorted(set([x for x in a.ks if x <= kbz + 1e-12] + [kbz]))
    for k in ks:
        try:
            sp = spektrum_q(sz, f, om, k)
        except Exception as ex:
            log('eigs-Fehler', k, repr(ex)[:200])
            continue
        gam = max([d['re'] for d in sp] + [0.0])
        res['spektren'].append({'k': k, 'gamma': gam, 'moden': sp[:16]})
        log('k', round(k, 5), 'gamma', round(gam, 7), [(round(d['re'], 6), round(d['im'], 5), d['n_dominant'],
                                                         round(d['betrag_anteil'], 2)) for d in sp[:10]])
        schreibe(a.out, res)
    # k_c per Bisektion
    sp_ = res['spektren']
    for i in range(len(sp_) - 1):
        if sp_[i]['gamma'] > 1e-6 and sp_[i + 1]['gamma'] <= 1e-6:
            lo, hi = sp_[i]['k'], sp_[i + 1]['k']
            for _ in range(14):
                mid = 0.5 * (lo + hi)
                g = max([d['re'] for d in spektrum_q(sz, f, om, mid)] + [0.0])
                if g > 1e-6:
                    lo = mid
                else:
                    hi = mid
            res['k_c'] = 0.5 * (lo + hi)
            break
    if a.npz:
        np.savez_compressed(a.npz + '.tmp.npz', f=f, r=sz['r'], th=sz['th'], s0=sz['s0v'])
        os.replace(a.npz + '.tmp.npz', a.npz)
    schreibe(a.out, res)


# ------------------------------------------------------------------------------------------------ (b) Wirbel
def modus_w(a):
    nz = netz(a.geo)
    if a.zentrum is not None:
        nz['zentrum'] = np.array(a.zentrum, float)
        log('Zentrum (kubische Einheiten des Netzes) gesetzt auf', a.zentrum)
    h = a.h
    sz = superzelle(nz, a.L, h)
    log('Superzelle', a.geo, 'L', a.L, 'N', sz['N'], 'Periode', sz['periode'], 'Kiste quer', sz['kiste_quer'], 'h', h,
        'R_D', a.RD)
    R = rad.Radial(0.02, 80.0)
    fk, info = rad.profil_w(R)
    fr = np.interp(sz['r'], R.r, fk)
    psi_s = fr * np.exp(1j * sz['th'])
    frei = np.nonzero(sz['r'] < a.RD)[0]
    fest = np.nonzero(sz['r'] >= a.RD)[0]
    assert a.RD < 0.5 * sz['kiste_quer'] - 1.5 * sz['periode'], 'R_D zu gross fuer die Kiste'
    D = Dmat(sz, 0.0).real.tocsr()
    s0, s1 = sz['s0v'], sz['s1e']
    nf = len(frei)
    t0 = time.time()

    def voll(x):
        p = psi_s.copy()
        p[frei] = x[:nf] + 1j * x[nf:]
        return p

    def fg(x):
        p = voll(x)
        dp = D @ p
        S = (p * p.conj()).real
        E = float(s1 @ (np.abs(dp) ** 2)) + float(s0 @ rad_Ub(S))
        g = 2.0 * (D.T @ (s1 * dp)) + 2.0 * s0 * rad_Ubp(S) * p
        g = g[frei]
        return E, np.concatenate([g.real, g.imag])

    def cb(xk):
        if time.time() - t0 > a.tmax:
            raise StopIteration
    x0 = np.concatenate([psi_s[frei].real, psi_s[frei].imag])
    r = minimize(fg, x0, jac=True, method='L-BFGS-B', callback=cb,
                 options={'maxiter': a.maxiter, 'maxfun': 3 * a.maxiter, 'ftol': 0.0, 'gtol': 1e-11, 'maxcor': 30})
    psi = voll(r.x)
    E, g = fg(r.x)
    S = np.abs(psi) ** 2
    rest = float(np.linalg.norm(g) / np.linalg.norm(np.concatenate([(s0 * psi)[frei].real, (s0 * psi)[frei].imag])))
    # Kernlage: Schwerpunkt von (1 - |psi|^2) in der Kernzone
    kern = (sz['r'] < 3.0)
    wk = s0 * np.clip(1 - S, 0, None) * kern
    st = {'E_periode': E, 'rest_rel': rest, 'nit': int(r.nit), 'status': int(r.status), 'meldung': str(r.message),
          'zeit_s': time.time() - t0, 'min_betrag': float(np.sqrt(S[frei].min())), 'n_frei': nf}
    log('stationaer', st)
    res = {'geo': a.geo, 'h': h, 'L': a.L, 'N': sz['N'], 'R_D': a.RD, 'stationaer': st, 'periode': sz['periode'],
           'kiste_quer': sz['kiste_quer'], 'kont_r_f_halb': info['r_f_halb'],
           'durchmesser_kanten': 2 * info['r_f_halb'] / h, 'k_bz_rand': math.pi / sz['periode'], 'spektren': []}
    kbz = math.pi / sz['periode']
    ks = sorted(set([x for x in a.ks if x <= kbz + 1e-12] + [kbz]))
    pa, pb = psi.real[frei], psi.imag[frei]
    mi = sps.diags(1.0 / np.sqrt(s0[frei]))
    for k in ks:
        Lk = lap(sz, k, frei)
        Sf = S[frei]
        A11 = Lk + sps.diags(s0[frei] * (rad_Ubp(Sf) + 2 * rad_Ubpp(Sf) * pa * pa))
        A22 = Lk + sps.diags(s0[frei] * (rad_Ubp(Sf) + 2 * rad_Ubpp(Sf) * pb * pb))
        A12 = sps.diags(s0[frei] * 2 * rad_Ubpp(Sf) * pa * pb)
        H = sps.bmat([[mi @ A11 @ mi, mi @ A12 @ mi], [mi @ A12 @ mi, mi @ A22 @ mi]], format='csc')
        try:
            w, vec = spla.eigsh(H, k=a.nev, sigma=a.sigma, which='LM', tol=1e-10)
        except Exception as ex:
            log('eigsh-Fehler', k, repr(ex)[:200])
            continue
        o = np.argsort(w)
        moden = []
        for j in o:
            x = vec[:, j]
            du, dv = x[:nf] / np.sqrt(s0[frei]), x[nf:] / np.sqrt(s0[frei])
            d = {'omega2': float(w[j])}
            d.update(formen(sz, psi, du, dv, frei))
            moden.append(d)
        res['spektren'].append({'k': k, 'moden': moden})
        log('k', round(k, 5), [(round(d['omega2'], 6), d['n_dominant'], round(d['betrag_anteil'], 2), round(d['r_schwer'], 2))
                               for d in moden[:10]])
        schreibe(a.out, res)
    schreibe(a.out, res)


def rad_Ub(S):
    return rad.Ub(S)


def rad_Ubp(S):
    return rad.Ubp(S)


def rad_Ubpp(S):
    return rad.Ubpp(S)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['q', 'w'])
    ap.add_argument('--geo', default='V')
    ap.add_argument('--om', type=float, default=0.8)
    ap.add_argument('--h', type=float, default=1.5)
    ap.add_argument('--L', type=int, default=16)
    ap.add_argument('--RD', type=float, default=12.0)
    ap.add_argument('--nev', type=int, default=16)
    ap.add_argument('--ks', type=float, nargs='*',
                    default=[0.0, 0.01, 0.02, 0.04, 0.06, 0.08, 0.1, 0.13, 0.16, 0.2, 0.25, 0.3, 0.4, 0.5, 0.7, 1.0])
    ap.add_argument('--maxiter', type=int, default=20000)
    ap.add_argument('--tmax', type=float, default=240.0)
    ap.add_argument('--npz')
    ap.add_argument('--zentrum', type=float, nargs=3, default=None)
    ap.add_argument('--sigma', type=float, default=-0.05)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    log('start', time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), sys.argv)
    {'q': modus_q, 'w': modus_w}[a.modus](a)


if __name__ == '__main__':
    main()
