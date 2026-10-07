#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SCHWERE-MASSE-V (Versuch ohne Karte, GR-Pruefliste Nr. 9), Rechen-Agent fuer die Leitung claude-primary, 05.10.2026.

Frage: Ist die schwere (aktive) Masse eines gebundenen Q-Balls auf Finns gefuelltem Netz V, gelesen aus dem Fernfeld
des Takts, gleich seiner Gesamtenergie E, auch wenn der Bindungsanteil sich aendert?

Aufbau (synthetisch, keine Messdaten):
  Skalar (Papier I, U(S) = S - S^2 + S^3/2) auf den Ecken von V. DEC mit den gewichteten Sternen an der Kammermitte
  (rv.sterne an w_mid aus rv.lp_symmetrisch, wie LICHT-ABLENKUNG-V). h = Finn-Kante l_P in Q-Ball-Laengen (1/m).
    K = om^2 sum *0 h^3 f^2, G = h sum *1 (df)^2, V = sum *0 h^3 U(f^2), E = K + G + V, Q = 2 om sum *0 h^3 f^2.
  Stationaerer Gitter-Q-Ball: Minimum von E_Q[f] = Q^2/(4 I2) + G + V bei festem Q (L-BFGS-B), Start = Kontinuumsprofil
    (Schiessen wie mn.qball, hier mit f zurueck) um die Lochmitte C1.
  Spannungsspur bei gleichfoermiger Streckung aller Laengen (Sterne homogen, *0 ~ lambda^3, *1 ~ lambda):
    S = sum T^i_i = dL/dln(lambda) = 3K - G - 3V; im Kontinuum 0 fuer stationaere Loesungen (Virialsatz, von Laue).
  Quellen je Ecke: m_v = K_v + V_v + 1/2 sum_e G_e (Energie, wie MATERIE-NETZ-1);
    s_v = 3 K_v - 3 V_v - 1/2 sum_e G_e (Spannungsspur; Verteilung festgelegt, Summe = S).
  Takt: mu(k) = -P(k)^{-1} q(k), P = -W^H B W (MATERIE-NETZ-1: ew.ops, mn.W_of unveraendert), Fernfit
    -A/r - (2 pi/(3 V_tor)) A r^2 + C im Band; M_schwer = A / A_1 mit A_1 = 1/(8 sqrt2 pi).
Unveraendert importiert: ew.py, mn.py, rv.py (und tp.py, danzer_naeherung.py, licht_netz.py).
Aufruf nur ueber kleintest.sh auf der .69:
  python sm.py basis --out lauf/basis.json
  python sm.py qball --om 0.8 --h 1.0 --L 19 --out lauf/qb-...json [--npz lauf/qb-...npz] [--maxiter N] [--tmax s]
  python sm.py takt --LT 40 --band 10 20 --ein lauf/qb-a.npz ... --out lauf/takt.json
"""
import argparse, json, os, sys, time, math, hashlib, platform, resource
import numpy as np
import scipy
import scipy.sparse as sps
from scipy.optimize import minimize
from scipy.integrate import solve_ivp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ew  # noqa: E402
import mn  # noqa: E402
import rv  # noqa: E402

T0 = time.time()
LP = mn.LP                      # l_P in kubischen Einheiten a
VCELL = mn.VCELL                # primitive Zelle in a^3
BETA = 0.5
A1 = 1.0 / (8.0 * math.sqrt(2.0) * math.pi)
ZENTRUM = 4                     # Untergitter C1 (Lochmitte), Zelle (0, 0, 0)


def log(*a):
    print('[%7.1f s]' % (time.time() - T0), *a, flush=True)


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def U(S):
    return S - S ** 2 + BETA * S ** 3


def Up(S):
    return 1.0 - 2.0 * S + 3.0 * BETA * S ** 2


def cT(X):
    return np.conj(np.swapaxes(X, -1, -2))


def schreibe(pfad, res):
    res['_meta'] = {'argv': sys.argv, 'python': platform.python_version(), 'numpy': np.__version__,
                    'scipy': scipy.__version__, 'host': platform.node(), 'laufzeit_s': time.time() - T0,
                    'maxrss_MB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
                    'ende_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
                    'sha256': {f: sha(os.path.join(os.path.dirname(os.path.abspath(__file__)), f))
                               for f in ('sm.py', 'ew.py', 'mn.py', 'rv.py', 'tp.py', 'danzer_naeherung.py', 'licht_netz.py')}}
    with open(pfad + '.tmp', 'w') as f:
        json.dump(res, f, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
    os.replace(pfad + '.tmp', pfad)
    log('->', pfad)


# ------------------------------------------------------------------------------------------------ Sterne auf V
def stern_daten():
    net = rv.netz_V(1)
    topo = rv.topologie(net)
    rows, Am, G0 = rv.zeilen(net, topo)
    sy = rv.lp_symmetrisch(Am, G0, rv.bahnmatrix(net))
    w = rv.w_sym(net, sy['x'], sy['y'])
    st = rv.sterne(net, topo, w)
    mod = ew.baue('V')
    pos = np.array(mod['pos'])
    E, nV = mod['E'], mod['nV']
    D = np.array([pos[s2] + mod['T'][e] - pos[s] for e, (s, s2, n2) in enumerate(mod['kliste'])])
    s1 = np.full(E, np.nan)
    treffer = np.zeros(E, int)
    for m in range(len(st['s1'])):
        a, b = int(st['gt'][m]), int(st['gh'][m])
        d = st['xh'][m] - st['xt'][m]
        for e, (s, s2, n2) in enumerate(mod['kliste']):
            if (s, s2) == (a, b) and np.abs(D[e] - d).max() < 1e-9:
                s1[e] = st['s1'][m]
                treffer[e] += 1
            elif (s, s2) == (b, a) and np.abs(D[e] + d).max() < 1e-9:
                s1[e] = st['s1'][m]
                treffer[e] += 1
    assert np.all(treffer == 1) and len(st['s1']) == E, (treffer, len(st['s1']), E)
    s0 = np.asarray(st['s0'], float)
    # Kontrollen: Volumen, T1-Identitaet, Positivitaet, Dispersion des Skalar-Laplace bei kleinem k
    lv = mod['l']
    T1 = np.einsum('e,ei,ej->ij', s1 * lv ** 2, D / lv[:, None], D / lv[:, None]) / VCELL
    fab = rv.fabrik_skalar(net, st)
    disp = {}
    for nm, d in (('100', np.array([1.0, 0, 0])), ('110', np.array([1.0, 1, 0]) / math.sqrt(2)),
                  ('111', np.array([1.0, 1, 1]) / math.sqrt(3))):
        op = fab(d)
        disp[nm] = [float(op(kk * d)[0] / kk) for kk in (1e-3, 0.1, 0.3)]
    # M(k = 0)^H 1_E: Kraft einer gleichfoermigen Kantendehnung auf die Untergitter (soll 0 sein)
    o0 = ew.ops(mod, np.zeros((1, 3)))
    MH1 = np.abs(cT(o0['M'][0]) @ np.ones(E)).max() / np.abs(o0['M']).max()
    kontr = {'w_mid_xy': [sy['x'], sy['y']], 'marge_t': sy['t'], 'id_vol': st['id_vol'], 'id_T1': st['id_T1'],
             'T1_ew_gegen_I_max': float(np.abs(T1 - np.eye(3)).max()), 's0_summe_durch_Vzelle': float(s0.sum() / VCELL),
             's0_min': float(s0.min()), 's1_min': float(s1.min()), 'n_s1_nichtpos': int((s1 <= 0).sum()),
             'skalar_tempo_a_k_1e-3_0.1_0.3': disp, 'MH_1E_rel': float(MH1), 'E': E, 'nV': nV}
    return {'mod': mod, 'pos': pos, 's0_lP': s0 / LP ** 3, 's1_lP': s1 / LP, 'kontr': kontr,
            's0_a': s0, 's1_a': s1}


def gitter(L, sd):
    mod, pos = sd['mod'], sd['pos']
    E, nV = mod['E'], mod['nV']
    g = np.arange(L)
    nn = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1).reshape(-1, 3)
    N = L ** 3 * nV

    def vidx(c, s):
        c = np.mod(c, L)
        return ((c[:, 0] * L + c[:, 1]) * L + c[:, 2]) * nV + s
    tl, hd, w1 = [], [], []
    for e, (s, s2, n2) in enumerate(mod['kliste']):
        tl.append(vidx(nn, s))
        hd.append(vidx(nn + np.array(n2), s2))
        w1.append(np.full(len(nn), sd['s1_lP'][e]))
    tl, hd, w1 = np.concatenate(tl), np.concatenate(hd), np.concatenate(w1)
    ne = len(tl)
    rows = np.concatenate([np.arange(ne), np.arange(ne)])
    D = sps.csr_matrix((np.concatenate([np.ones(ne), -np.ones(ne)]), (rows, np.concatenate([hd, tl]))), shape=(ne, N))
    Dabs = sps.csr_matrix((np.ones(2 * ne), (rows, np.concatenate([hd, tl]))), shape=(ne, N))
    Rcell = (nn @ ew.AV).reshape(L, L, L, 3)
    X = Rcell[..., None, :] + pos[None, None, None]
    _, dist = mn.min_bild(X - pos[ZENTRUM], L)
    r = (dist / LP).reshape(-1)
    s0v = np.tile(sd['s0_lP'], L ** 3)
    return {'L': L, 'D': D, 'Dabs': Dabs, 's1e': w1, 's0v': s0v, 'r': r, 'N': N, 'ne': ne}


# ------------------------------------------------------------------------------------------------ Kontinuum
def qball_kont(om, beta=BETA, rmax=80.0, nr=80001):
    """Wie mn.qball (Schiessen auf f(0), Bisektion), aber mit f, f' und den Teilintegralen zurueck."""
    F = lambda f: (1 - om ** 2) * f - 2 * f ** 3 + 3 * beta * f ** 5
    disk = 1 - 4 * beta * (1 - om ** 2)
    S0 = (1 - math.sqrt(disk)) / (2 * beta)
    Sp = (2 + math.sqrt(4 - 12 * beta * (1 - om ** 2))) / (6 * beta)
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
            hi = mid
        else:
            lo = mid
    f0 = 0.5 * (lo + hi)
    s = schiess(f0, dense=True)
    rr = np.linspace(1e-4, s.t[-1], 20001)
    y = s.sol(rr)
    f, fp = y[0], y[1]
    icut = int(np.argmin(np.where(f > 0, f, np.inf)))
    kap = math.sqrt(1 - om ** 2)
    r_all = np.linspace(0.0, rmax, nr)
    f_all = np.interp(r_all, rr[:icut + 1], f[:icut + 1])
    fp_all = np.interp(r_all, rr[:icut + 1], fp[:icut + 1])
    rc = rr[icut]
    tail = r_all > rc
    f_all[tail] = f[icut] * np.exp(-kap * (r_all[tail] - rc)) * rc / r_all[tail]
    fp_all[tail] = -f_all[tail] * (kap + 1.0 / r_all[tail])
    S = f_all ** 2
    w4 = 4 * np.pi * r_all ** 2
    I2 = float(np.trapezoid(w4 * S, r_all))
    K = om ** 2 * I2
    G = float(np.trapezoid(w4 * fp_all ** 2, r_all))
    V = float(np.trapezoid(w4 * U(S), r_all))
    E = K + G + V
    Q = 2 * om * I2
    rho = om ** 2 * S + fp_all ** 2 + U(S)
    Mr = np.concatenate([[0.0], np.cumsum(0.5 * (w4[1:] * rho[1:] + w4[:-1] * rho[:-1]) * np.diff(r_all))])
    return {'om': om, 'f0': f0, 'r_cut': float(rc), 'r': r_all, 'f': f_all, 'I2': I2, 'K': K, 'G': G, 'V': V, 'E': E,
            'Q': Q, 'S': 3 * K - G - 3 * V, 'S_rel': (3 * K - G - 3 * V) / E, 'bind': (Q - E) / E,
            'r_halb': float(np.interp(0.5 * E, Mr, r_all)), 'r_99': float(np.interp(0.99 * E, Mr, r_all)),
            'kappa': kap, 'bisektion_breite': hi - lo}


def kont_kurz(k):
    return {x: k[x] for x in ('om', 'f0', 'r_cut', 'I2', 'K', 'G', 'V', 'E', 'Q', 'S', 'S_rel', 'bind', 'r_halb', 'r_99',
                              'kappa', 'bisektion_breite')}


# ------------------------------------------------------------------------------------------------ Gitter-Q-Ball
def teile(f, om, gi, h):
    s0h3 = gi['s0v'] * h ** 3
    s1h = gi['s1e'] * h
    df = gi['D'] @ f
    Kv = om ** 2 * s0h3 * f * f
    Vv = s0h3 * U(f * f)
    Ge = s1h * df * df
    Gv = 0.5 * (gi['Dabs'].T @ Ge)
    K, G, V = float(Kv.sum()), float(Ge.sum()), float(Vv.sum())
    m = Kv + Vv + Gv
    s = 3 * Kv - 3 * Vv - Gv
    return {'K': K, 'G': G, 'V': V, 'E': K + G + V, 'S': 3 * K - G - 3 * V, 'Q': 2 * om * float((s0h3 * f * f).sum()),
            'm': m, 's': s}


def modus_qball(a):
    sd = stern_daten()
    log('Sterne', sd['kontr'])
    k = qball_kont(a.om)
    log('Kontinuum', kont_kurz(k))
    gi = gitter(a.L, sd)
    h = a.h
    log('Gitter L=%d N=%d Kanten=%d, Inkreis %.2f l_P = %.2f Q-Einheiten' % (a.L, gi['N'], gi['ne'], a.L, a.L * h))
    rq = gi['r'] * h
    f0 = np.interp(rq, k['r'], k['f'], right=0.0)
    s0h3 = gi['s0v'] * h ** 3
    s1h = gi['s1e'] * h
    D = gi['D']
    Qz = k['Q']
    w = np.sqrt(s0h3)
    zaehl = {'n': 0}

    def fg(u):
        zaehl['n'] += 1
        f = u / w
        I2 = float(u @ u)
        df = D @ f
        S = f * f
        Ee = Qz * Qz / (4 * I2) + float(s1h @ (df * df)) + float(s0h3 @ U(S))
        gf = 2.0 * (D.T @ (s1h * df)) + 2.0 * s0h3 * Up(S) * f
        gu = gf / w - (Qz * Qz / (2 * I2 * I2)) * u
        return Ee, gu
    u0 = w * f0
    E0, g0 = fg(u0)
    om0 = Qz / (2 * float(u0 @ u0))
    res0 = float(np.linalg.norm(g0) / np.linalg.norm(2 * om0 ** 2 * u0))
    t_start = time.time()
    stop = {'zeit': False}
    kann_stop = tuple(int(x) for x in scipy.__version__.split('.')[:2]) >= (1, 11)

    def cb(xk):
        if kann_stop and time.time() - t_start > a.tmax:
            stop['zeit'] = True
            raise StopIteration
    r = minimize(fg, u0, jac=True, method='L-BFGS-B', callback=cb,
                 options={'maxiter': a.maxiter, 'maxfun': 3 * a.maxiter, 'ftol': 0.0, 'gtol': a.gtol, 'maxcor': 30})
    u = r.x
    t_min = time.time() - t_start
    Ee, gu = fg(u)
    I2 = float(u @ u)
    om_l = Qz / (2 * I2)
    resid = float(np.linalg.norm(gu) / np.linalg.norm(2 * om_l ** 2 * u))
    f = u / w
    tl = teile(f, om_l, gi, h)
    t0_ = teile(f0, om0, gi, h)
    rr = gi['r']
    o = np.argsort(rr)
    Mr = np.cumsum(tl['m'][o])
    r_halb = float(np.interp(0.5 * tl['E'], Mr, rr[o]))
    r_99 = float(np.interp(0.99 * tl['E'], Mr, rr[o]))
    # Rand des Torus: Energie in der aeussersten Schale (r > 0.85 L) relativ
    rand = float(tl['m'][rr > 0.85 * a.L].sum() / tl['E'])
    # Profil der Quellen in Schalen (l_P)
    kanten = np.arange(0.0, float(rr.max()) + 1.0, 1.0)
    prof = []
    for x0, x1 in zip(kanten[:-1], kanten[1:]):
        sel = (rr >= x0) & (rr < x1)
        if sel.any():
            prof.append([float(x0), float(x1), int(sel.sum()), float(tl['m'][sel].sum()), float(tl['s'][sel].sum())])
    out = {'om_kont': a.om, 'h': h, 'L': a.L, 'N': gi['N'], 'kontinuum': kont_kurz(k), 'sterne': sd['kontr'],
           'start': {'E': t0_['E'], 'S': t0_['S'], 'S_rel': t0_['S'] / t0_['E'], 'Q': t0_['Q'], 'om': om0, 'resid_rel': res0},
           'loesung': {'Q': tl['Q'], 'om': om_l, 'E': tl['E'], 'K': tl['K'], 'G': tl['G'], 'V': tl['V'], 'S': tl['S'],
                       'S_rel': tl['S'] / tl['E'], 'bind': (tl['Q'] - tl['E']) / tl['E'], 'E_minus_Q_rel': (tl['E'] - tl['Q']) / tl['E'],
                       'summe_m_rel': float(tl['m'].sum() / tl['E'] - 1), 'summe_s_minus_S': float(tl['s'].sum() - tl['S']),
                       'brutto_s_rel': float(np.abs(tl['s']).sum() / tl['E']), 'brutto_s_pos_rel': float(tl['s'][tl['s'] > 0].sum() / tl['E']),
                       'r_halb_lP': r_halb, 'r_99_lP': r_99, 'r_halb_Q': r_halb * h, 'rand_anteil': rand,
                       'f_max': float(f.max()), 'resid_rel': resid, 'E_minus_E0_rel': (tl['E'] - t0_['E']) / t0_['E']},
           'minimierer': {'nit': int(r.nit), 'nfev': int(r.nfev), 'status': int(r.status), 'meldung': str(r.message),
                          'zeit_s': t_min, 'zeitstopp': stop['zeit'], 'fg_aufrufe': zaehl['n']},
           'profil_schalen_lP': prof}
    log('Loesung', {kk: v for kk, v in out['loesung'].items()})
    log('Minimierer', out['minimierer'])
    if a.npz:
        np.savez_compressed(a.npz + '.tmp.npz', m=tl['m'].reshape(a.L, a.L, a.L, -1), s=tl['s'].reshape(a.L, a.L, a.L, -1),
                            f=f.reshape(a.L, a.L, a.L, -1), L=a.L, h=h, om=a.om, E=tl['E'], S=tl['S'], Q=tl['Q'])
        os.replace(a.npz + '.tmp.npz', a.npz)
        log('->', a.npz)
    schreibe(a.out, out)


# ------------------------------------------------------------------------------------------------ Takt (Fernfeld)
def einbetten(q, LQ, LT, mod):
    pos = np.array(mod['pos'])
    nV = mod['nV']
    g = np.arange(LQ)
    nn = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1)
    X = (nn @ ew.AV)[..., None, :] + pos[None, None, None]
    d, _ = mn.min_bild(X - pos[ZENTRUM], LQ)
    Y = pos[ZENTRUM] + d - pos[None, None, None]
    n = Y @ np.linalg.inv(ew.AV)
    ni = np.rint(n).astype(int)
    assert np.abs(n - ni).max() < 1e-6
    ni = np.mod(ni, LT)
    out = np.zeros((LT, LT, LT, nV))
    sidx = np.broadcast_to(np.arange(nV), (LQ, LQ, LQ, nV))
    np.add.at(out, (ni[..., 0], ni[..., 1], ni[..., 2], sidx), q)
    return out


def modus_takt(a):
    mod = ew.baue('V')
    E, nV = mod['E'], mod['nV']
    LT = a.LT
    pos = np.array(mod['pos'])
    quellen, namen, info = [], [], []
    p = np.zeros((LT, LT, LT, nV))
    p[0, 0, 0, ZENTRUM] = 1.0
    quellen.append(p)
    namen.append('punkt_C1')
    info.append({'summe': 1.0})
    for pf in a.ein:
        z = np.load(pf)
        LQ = int(z['L'])
        m = einbetten(z['m'], LQ, LT, mod)
        s = einbetten(z['s'], LQ, LT, mod)
        nm = os.path.basename(pf).replace('.npz', '')
        for art, q in (('E', m), ('S', s), ('E+S', m + s)):
            quellen.append(q)
            namen.append(nm + ':' + art)
            info.append({'summe': float(q.sum()), 'E': float(z['E']), 'S': float(z['S']), 'Q': float(z['Q']),
                         'h': float(z['h']), 'om': float(z['om']), 'LQ': LQ,
                         'einbett_rest': float(abs(q.sum() - (z['m'].sum() if art == 'E' else z['s'].sum() if art == 'S' else z['m'].sum() + z['s'].sum())))})
    nq = len(quellen)
    log('Quellen', nq, namen)
    N = LT ** 3
    g = np.arange(LT)
    nn = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1)
    kgrid = ((nn / LT) @ ew.BV).reshape(-1, 3)
    mk = np.stack([np.fft.fftn(q, axes=(0, 1, 2)).reshape(N, nV) for q in quellen], -1)
    mu_k = np.zeros((N, nV, nq), complex)
    chunk = 96
    pmin = np.inf
    for i0 in range(1, N, chunk):
        idx = np.arange(i0, min(i0 + chunk, N))
        k = kgrid[idx]
        o = ew.ops(mod, k)
        W = mn.W_of(mod, k)
        P = -cT(W) @ o['B'] @ W
        P = 0.5 * (P + cT(P))
        ev = np.linalg.eigvalsh(P)
        pmin = min(pmin, float((ev[:, 0] / np.abs(ev).max(-1)).min()))
        mu_k[idx] = -np.linalg.solve(P, mk[idx])
        if (i0 // chunk) % 100 == 0:
            log('k', i0, 'von', N)
    mu = np.fft.ifftn(mu_k.reshape((LT, LT, LT, nV, nq)), axes=(0, 1, 2))
    imag = float(np.abs(mu.imag).max() / np.abs(mu.real).max())
    mu = mu.real
    X = (nn @ ew.AV)[..., None, :] + pos[None, None, None]
    _, dist = mn.min_bild(X - pos[ZENTRUM], LT)
    r = (dist / LP).ravel()
    Vtor = LT ** 3 * VCELL / LP ** 3
    fr = lambda x: -1.0 / x - (2 * np.pi / (3 * Vtor)) * x ** 2
    res = {'LT': LT, 'band_lP': a.band, 'P_lmin_rel_min': pmin, 'imag_rel': imag, 'A1': A1, 'quellen': {}}
    for j, nm in enumerate(namen):
        mm = mu[..., j].ravel()
        zz = {'info': info[j]}
        for b0, b1 in ([a.band] + [list(x) for x in a.zusatzbaender]):
            fern = (r >= b0) & (r <= b1)
            Af = np.stack([fr(r[fern]), np.ones(fern.sum())], -1)
            (A, C), *_ = np.linalg.lstsq(Af, mm[fern], rcond=None)
            rms = float(np.sqrt(np.mean((Af @ np.array([A, C]) - mm[fern]) ** 2)) / np.abs(A * fr(r[fern])).mean())
            zz['band_%g_%g' % (b0, b1)] = {'A': float(A), 'C': float(C), 'rms_rel': rms, 'n': int(fern.sum()),
                                            'M_schwer': float(A / A1),
                                            'M_durch_summe': float(A / A1 / info[j]['summe']) if info[j]['summe'] != 0 else None}
        zz['mu_zentrum'] = float(mm[np.argmin(r)])
        res['quellen'][nm] = zz
        log(nm, {kk: v for kk, v in zz.items() if kk.startswith('band')})
    schreibe(a.out, res)


def modus_basis(a):
    sd = stern_daten()
    log('Sterne', sd['kontr'])
    fam = []
    for om in a.oms:
        k = qball_kont(om)
        fam.append(kont_kurz(k))
        log('om', om, kont_kurz(k))
    schreibe(a.out, {'sterne': sd['kontr'], 's0_lP': sd['s0_lP'].tolist(), 's1_lP': sd['s1_lP'].tolist(),
                     'kontinuum': fam})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['basis', 'qball', 'takt'])
    ap.add_argument('--om', type=float, default=0.8)
    ap.add_argument('--oms', type=float, nargs='*', default=[0.75, 0.8, 0.85, 0.9, 0.95])
    ap.add_argument('--h', type=float, default=1.0)
    ap.add_argument('--L', type=int, default=16)
    ap.add_argument('--LT', type=int, default=40)
    ap.add_argument('--band', type=float, nargs=2, default=[10.0, 20.0])
    ap.add_argument('--zusatzbaender', type=float, nargs='*', default=[])
    ap.add_argument('--ein', nargs='*', default=[])
    ap.add_argument('--maxiter', type=int, default=20000)
    ap.add_argument('--gtol', type=float, default=1e-11)
    ap.add_argument('--tmax', type=float, default=480.0)
    ap.add_argument('--npz')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    if a.zusatzbaender:
        a.zusatzbaender = [a.zusatzbaender[i:i + 2] for i in range(0, len(a.zusatzbaender), 2)]
    log('start', time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), sys.argv)
    {'basis': modus_basis, 'qball': modus_qball, 'takt': modus_takt}[a.modus](a)


if __name__ == '__main__':
    main()
