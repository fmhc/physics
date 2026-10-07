#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QUANT-1 (Runde 50, schlanke Karte), Rechen-Agent fuer die Leitung claude-primary, 05.10.2026.

Frage: Ist ein Q-Ball quantisch ein gebundener Zustand aus Q Feldquanten?

Aufbau (synthetisch, keine Messdaten):
  Euklidisches Pfadintegral des komplexen Skalars auf Graph x periodischer Zeit, Hybrid-Monte-Carlo (Omelyan 2MN).
  Gittereinheiten, hbar = 1. Ecken-Gewichte s0 (Volumen *0), Kanten-Gewichte s1 (Hodge *1), Zeitschritt dt:
    S = sum_t [ (1/dt) sum_v s0 |phi_v(t+1) - phi_v(t)|^2 + dt sum_e s1 |(D phi)_e|^2 + dt sum_v s0 U_g(|phi_v|^2) ]
    U_g(S) = m^2 S - lam S^2 + g6 S^3,  g6 = beta lam^2 / m^2   (Papier I: beta = 1/2).
  Umrechnung auf Q-Ball-Einheiten (Papier I, U(s) = s - s^2 + s^3/2): phi = (m / sqrt(lam)) psi, x = y / m.
    Dann S = (1/lam) S_QB[psi]: lam spielt die Rolle von hbar in Q-Ball-Einheiten, h = m a ist der Gitterabstand in
    Q-Ball-Laengen, die Zahl der Quanten ist N = Q_QB / lam, die Energie E = (m / lam) E_QB.
  Kubisches Kontrollgitter: s0 = 1, s1 = 1, dt = 1. Netz V: Sterne wie SCHWERE-MASSE-V (sm.stern_daten, sm.gitter,
    unveraendert importiert), Laengen in l_P.
  Operatoren bei Impuls null: O_1(t) = sum_v s0 phi_v(t); lokal O_Q = sum_v s0 phi_v^Q; Produkt P_Q = O_1^Q / Vol^(Q-1).
  Korrelatoren C(tau) = (1/T) sum_t Re <O(t+tau)^* O(t)> fuer Q = 1 und je Q >= 2 die 2x2-Matrix (lokal, Produkt).

Aufrufe (nur ueber kleintest.sh auf der .69):
  python q1.py netz --L 4 --out netz/V-L4.npz
  python q1.py frei --graph kubisch:8 --T 32 --m 0.5 --lams 0.1 0.25 1 --out aus/frei-k8.json
  python q1.py hmc --graph kubisch:8 --T 32 --m 0.5 --lam 0.25 --tmax 520 --seed 1 --out lauf/k8-l0.25-a
  python q1.py hmc ... --start lauf/k8-l0.25-a.npz --out lauf/k8-l0.25-b          (Fortsetzung der Kette)
  python q1.py aus --ein lauf/k8-l0.25-a.npz [lauf/k8-l0.25-b.npz ...] --out aus/k8-l0.25.json
  python q1.py klass --out aus/klassisch.json
"""
import argparse, json, os, sys, time, math, hashlib, platform, resource
import numpy as np
import scipy
import scipy.sparse as sps
import scipy.sparse.linalg as spla

T0 = time.time()
HIER = os.path.dirname(os.path.abspath(__file__))
LAM_O = 0.1931833275037836          # Omelyan 2MN


def log(*a):
    print('[%7.1f s]' % (time.time() - T0), *a, flush=True)


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def meta():
    return {'argv': sys.argv, 'python': platform.python_version(), 'numpy': np.__version__,
            'scipy': scipy.__version__, 'host': platform.node(), 'laufzeit_s': time.time() - T0,
            'maxrss_MB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
            'ende_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            'sha256_q1': sha(os.path.abspath(__file__))}


def schreibe_json(pfad, res):
    res['_meta'] = meta()
    with open(pfad + '.tmp', 'w') as f:
        json.dump(res, f, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
    os.replace(pfad + '.tmp', pfad)
    log('->', pfad)


# ------------------------------------------------------------------------------------------------ Graphen
def lap_aus(tl, hd, s1, N):
    ne = len(tl)
    rows = np.concatenate([np.arange(ne), np.arange(ne)])
    D = sps.csr_matrix((np.concatenate([np.ones(ne), -np.ones(ne)]), (rows, np.concatenate([hd, tl]))), shape=(ne, N))
    return (D.T @ sps.diags(s1) @ D).tocsr()


def graph_kubisch(L):
    N = L ** 3
    idx = np.arange(N).reshape(L, L, L)
    tl, hd = [], []
    for ax in range(3):
        tl.append(idx.ravel())
        hd.append(np.roll(idx, -1, axis=ax).ravel())
    tl, hd = np.concatenate(tl), np.concatenate(hd)
    return lap_aus(tl, hd, np.ones(len(tl)), N), np.ones(N), {'art': 'kubisch', 'L': L, 'Nv': N, 'Ne': len(tl)}


def graph_laden(spec):
    if spec.startswith('kubisch:'):
        return graph_kubisch(int(spec.split(':')[1]))
    z = np.load(spec)
    Lap = sps.csr_matrix((z['data'], z['indices'], z['indptr']), shape=tuple(int(x) for x in z['shape']))
    return Lap, np.array(z['s0'], float), {'art': 'V', 'L': int(z['L']), 'Nv': int(len(z['s0'])), 'Ne': int(z['Ne']),
                                           'datei': spec, 'sha256': sha(spec)}


def modus_netz(a):
    sys.path.insert(0, HIER)
    import sm  # noqa: E402  SCHWERE-MASSE-V, unveraendert
    sd = sm.stern_daten()
    log('Sterne', sd['kontr'])
    gi = sm.gitter(a.L, sd)
    D = gi['D'].tocsr()
    s1, s0 = np.asarray(gi['s1e'], float), np.asarray(gi['s0v'], float)
    Lap = (D.T @ sps.diags(s1) @ D).tocsr()
    np.savez(a.out, data=Lap.data, indices=Lap.indices, indptr=Lap.indptr, shape=np.array(Lap.shape), s0=s0, s1=s1,
             L=a.L, Ne=gi['ne'])
    # Kontrollen: Laplace mal konstant = 0, Volumen, kleinste Gewichte, groesster Eigenwert von s0^-1/2 Lap s0^-1/2
    e1 = np.abs(Lap @ np.ones(len(s0))).max()
    Mh = sps.diags(1 / np.sqrt(s0)) @ Lap @ sps.diags(1 / np.sqrt(s0))
    lmax = float(spla.eigsh(Mh, k=1, which='LA', return_eigenvectors=False)[0])
    res = {'L': a.L, 'Nv': len(s0), 'Ne': int(gi['ne']), 'Vol_lP3': float(s0.sum()), 'Vol_je_Zelle': float(s0.sum() / a.L ** 3),
           's0_min_max': [float(s0.min()), float(s0.max())], 's1_min_max': [float(s1.min()), float(s1.max())],
           'Lap_1_max': float(e1), 'lambda_max_s0Lap': lmax, 'sterne_kontr': sd['kontr'], 'sha256_npz': sha(a.out),
           'sha256_sm': sha(os.path.join(HIER, 'sm.py'))}
    log(res)
    schreibe_json(a.out.replace('.npz', '.json'), res)


# ------------------------------------------------------------------------------------------------ Modell, HMC
class Modell:
    def __init__(s, Lap, s0, T, dt, m, lam, beta):
        s.Lap, s.T, s.dt = Lap, T, dt
        s.s0 = np.asarray(s0, float)[:, None]
        s.m2, s.lam = m * m, lam
        s.g6 = beta * lam * lam / (m * m)
        s.invM = (dt / s.s0)
        s.sqM = np.sqrt(s.s0 / dt)

    def U(s, S):
        return s.m2 * S - s.lam * S * S + s.g6 * S ** 3

    def Up(s, S):
        return s.m2 - 2 * s.lam * S + 3 * s.g6 * S * S

    def S(s, phi):
        d = np.roll(phi, -1, axis=1) - phi
        kin_t = float((s.s0 * (d.real ** 2 + d.imag ** 2)).sum()) / s.dt
        Lp = s.Lap @ phi
        kin_x = s.dt * float((phi.real * Lp.real + phi.imag * Lp.imag).sum())
        SS = phi.real ** 2 + phi.imag ** 2
        pot = s.dt * float((s.s0 * s.U(SS)).sum())
        return kin_t + kin_x + pot

    def F(s, phi):
        """-(dS/dRe phi + i dS/dIm phi) = -2 dS/dphi^*."""
        SS = phi.real ** 2 + phi.imag ** 2
        g = (s.s0 / s.dt) * (2 * phi - np.roll(phi, -1, 1) - np.roll(phi, 1, 1)) + s.dt * (s.Lap @ phi) \
            + s.dt * s.s0 * s.Up(SS) * phi
        return -2.0 * g

    def H(s, phi, p):
        return 0.5 * float((s.invM * (p.real ** 2 + p.imag ** 2)).sum()) + s.S(phi)

    def md(s, phi, p, eps, n):
        p = p + LAM_O * eps * s.F(phi)
        for i in range(n):
            phi = phi + 0.5 * eps * s.invM * p
            p = p + (1 - 2 * LAM_O) * eps * s.F(phi)
            phi = phi + 0.5 * eps * s.invM * p
            p = p + (2 * LAM_O if i < n - 1 else LAM_O) * eps * s.F(phi)
        return phi, p

    def impulse(s, rng, shape):
        return s.sqM * (rng.standard_normal(shape) + 1j * rng.standard_normal(shape))


def trajektorie(mod, phi, rng, eps, n):
    p = mod.impulse(rng, phi.shape)
    H0 = mod.H(phi, p)
    phi1, p1 = mod.md(phi, p, eps, n)
    dH = mod.H(phi1, p1) - H0
    acc = bool(dH <= 0 or rng.random() < math.exp(-dH))
    return (phi1 if acc else phi), dH, acc


def reversibel(mod, phi, rng, eps, n):
    p = mod.impulse(rng, phi.shape)
    H0 = mod.H(phi, p)
    phi1, p1 = mod.md(phi, p, eps, n)
    H1 = mod.H(phi1, p1)
    phi2, p2 = mod.md(phi1, -p1, eps, n)
    H2 = mod.H(phi2, -p2)
    return {'dphi_max': float(np.abs(phi2 - phi).max()), 'dp_max': float(np.abs(-p2 - p).max()),
            'dH_hin': float(H1 - H0), 'dH_rueck_minus_start': float(H2 - H0), 'phi_max': float(np.abs(phi).max())}


def messen(mod, phi, qmax, vol):
    s0 = mod.s0[:, 0]
    T = phi.shape[1]
    O1 = s0 @ phi
    ops = [O1]
    pw = phi
    for Q in range(2, qmax + 1):
        pw = pw * phi
        ops.append(s0 @ pw)
        ops.append(O1 ** Q / vol ** (Q - 1))
    X = np.array(ops)
    Fx = np.fft.fft(X, axis=1)

    def corr(a, b):            # (1/T) sum_t O_a(t+tau)^* O_b(t)
        return np.conj(np.fft.ifft(Fx[a] * np.conj(Fx[b]))) / T
    out = [corr(0, 0).real]
    for Q in range(2, qmax + 1):
        il = 1 + 2 * (Q - 2)
        ip = il + 1
        out += [corr(il, il).real, corr(ip, ip).real, (0.5 * (corr(il, ip) + corr(ip, il))).real]
    C = np.array(out)
    C = 0.5 * (C + np.roll(C[:, ::-1], 1, axis=1))
    return C[:, :T // 2 + 1]


def modus_hmc(a):
    Lap, s0, ginfo = graph_laden(a.graph)
    mod = Modell(Lap, s0, a.T, a.dt, a.m, a.lam, a.beta)
    vol = float(s0.sum())
    Nv = len(s0)
    log('Graph', ginfo, 'Vol', vol, 'g6', mod.g6)
    df = os.statvfs(os.path.dirname(os.path.abspath(a.out)) or '.')
    frei_GB = df.f_bavail * df.f_frsize / 1e9
    log('Platte frei %.1f GB' % frei_GB)
    if frei_GB < 10:
        log('ABBRUCH: weniger als 10 GB frei')
        sys.exit(4)
    par = {'graph': a.graph, 'ginfo': ginfo, 'T': a.T, 'dt': a.dt, 'm': a.m, 'lam': a.lam, 'beta': a.beta,
           'g6': mod.g6, 'qmax': a.qmax, 'tau': a.tau, 'Vol': vol}
    if a.start:
        z = np.load(a.start, allow_pickle=False)
        alt = json.loads(str(z['par']))
        for k in ('graph', 'T', 'dt', 'm', 'lam', 'beta', 'qmax'):
            assert alt[k] == par[k], (k, alt[k], par[k])
        phi = np.array(z['phi_ende'])
        n, eps = int(z['n']), float(z['eps'])
        rng = np.random.default_rng()
        rng.bit_generator.state = json.loads(str(z['rng']))
        ntherm = a.ntherm_fort
        log('Fortsetzung von', a.start, 'n', n, 'eps', eps)
    else:
        rng = np.random.default_rng(a.seed)
        phi = 0.1 * (rng.standard_normal((Nv, a.T)) + 1j * rng.standard_normal((Nv, a.T)))
        n = a.nmd
        eps = a.tau / n
        ntherm = a.ntherm
    # Thermalisierung mit Schrittweiten-Anpassung (zaehlt nicht zur Messung)
    tune = []
    acc_bl = []
    for k in range(ntherm):
        phi, dH, acc = trajektorie(mod, phi, rng, eps, n)
        acc_bl.append(acc)
        if len(acc_bl) == 25:
            r = float(np.mean(acc_bl))
            tune.append((k, n, eps, r))
            if not a.start:
                if r < 0.75:
                    n = min(int(math.ceil(n * 1.3)) + 1, 400)
                elif r > 0.93 and n > 4:
                    n = max(4, int(n * 0.85))
                eps = a.tau / n
            acc_bl = []
    log('Thermalisierung', ntherm, 'Trajektorien; Anpassung', tune[-4:] if tune else None, 'n', n, 'eps', eps)
    rev = [reversibel(mod, phi, rng, eps, n) for _ in range(3)]
    log('Reversibilitaet', rev)
    # Produktion
    t_ende = T0 + a.tmax
    Cs, dHs, accs, p2s = [], [], [], []
    t_prod = time.time()
    while time.time() < t_ende and (a.ntraj <= 0 or len(dHs) < a.ntraj):
        phi, dH, acc = trajektorie(mod, phi, rng, eps, n)
        Cs.append(messen(mod, phi, a.qmax, vol).astype(np.float32))
        dHs.append(dH)
        accs.append(acc)
        p2s.append(float((mod.s0 * (phi.real ** 2 + phi.imag ** 2)).sum()) / (vol * a.T))
        if len(dHs) % 1000 == 0:
            log('Traj', len(dHs), 'Akz %.3f' % np.mean(accs[-1000:]), '<|phi|^2> %.5f' % np.mean(p2s[-1000:]))
    dHs = np.array(dHs)
    eDH = np.exp(-dHs)
    res = {'par': par, 'n': n, 'eps': eps, 'tune': tune, 'ntherm': ntherm, 'ntraj': len(dHs),
           's_je_traj': (time.time() - t_prod) / max(len(dHs), 1), 'akzeptanz': float(np.mean(accs)),
           'exp_mdH': float(eDH.mean()), 'exp_mdH_fehler_naiv': float(eDH.std() / math.sqrt(len(eDH))),
           'dH_mittel': float(dHs.mean()), 'dH_rms': float(np.sqrt((dHs ** 2).mean())), 'reversibel': rev,
           'phi2_mittel': float(np.mean(p2s)), 'start': a.start, 'seed': a.seed}
    np.savez(a.out + '.npz', C=np.array(Cs), dH=dHs, acc=np.array(accs), phi2=np.array(p2s), phi_ende=phi, n=n, eps=eps,
             rng=json.dumps(rng.bit_generator.state), par=json.dumps(par))
    res['sha256_npz'] = sha(a.out + '.npz')
    log({k: v for k, v in res.items() if k not in ('tune', 'reversibel')})
    schreibe_json(a.out + '.json', res)


# ------------------------------------------------------------------------------------------------ freie Theorie
def frei_exakt(Lap, s0, T, dt, m):
    """C_1(tau) = (1/T) sum_k cos(k tau) s0^T A_k^-1 s0 und G0 = <|phi|^2> (volumengewichtet), exakt."""
    Nv = len(s0)
    S0 = sps.diags(s0)
    ks = 2 * np.pi * np.arange(T) / T
    c = np.zeros(T)
    g0 = 0.0
    dense = Nv <= 2000
    for k in ks:
        A = (2 - 2 * math.cos(k)) / dt * S0 + dt * (Lap + m * m * S0)
        if dense:
            Ai = np.linalg.inv(A.toarray())
            x = Ai @ s0
            g0 += float((s0 * np.diag(Ai)).sum())
        else:
            x = spla.spsolve(A.tocsc(), s0)
        c += np.cos(k * np.arange(T)) * float(s0 @ x)
    c /= T
    G0 = g0 / (T * s0.sum()) if dense else float('nan')
    return c, G0


def einschleife(m, lam, beta, G0, vol, qmax):
    """Vorab [M]: Tadpole-Masse und normalgeordnete Quartik (U = m^2 S - lam S^2 + g6 S^3, Wick mit <|phi|^2> = G0);
    Energieverschiebung 1. Ordnung im Kasten fuer Q Quanten in Ruhe: dE_Q = -lam_eff Q(Q-1)/(4 m1^2 Vol)
    + g6 Q(Q-1)(Q-2)/(8 m1^3 Vol^2)."""
    g6 = beta * lam * lam / (m * m)
    m1q = m * m - 4 * lam * G0 + 18 * g6 * G0 * G0
    lam_eff = lam - 9 * g6 * G0
    m1 = math.sqrt(m1q) if m1q > 0 else float('nan')
    dE = {Q: -lam_eff * Q * (Q - 1) / (4 * m1q * vol) + g6 * Q * (Q - 1) * (Q - 2) / (8 * m1q ** 1.5 * vol ** 2)
          for Q in range(2, qmax + 1)} if m1q > 0 else {}
    return {'lam': lam, 'g6': g6, 'm1_quadrat_tadpole': m1q, 'm1_tadpole': m1,
            'm1_gitter_E': 2 * math.asinh(m1 / 2) if m1q > 0 else float('nan'), 'lam_eff_quartik': lam_eff,
            'anziehend': lam_eff > 0, 'dE_Q_erste_Ordnung': dE,
            'dE_je_Teilchen': {Q: v / Q for Q, v in dE.items()}}


def modus_frei(a):
    Lap, s0, ginfo = graph_laden(a.graph)
    c, G0 = frei_exakt(Lap, s0, a.T, a.dt, a.m)
    meff = [float(math.acosh((c[t + 1] + c[t - 1]) / (2 * c[t]))) for t in range(1, a.T // 2)]
    vol = float(s0.sum())
    res = {'graph': a.graph, 'ginfo': ginfo, 'T': a.T, 'dt': a.dt, 'm': a.m, 'Vol': vol, 'C1_exakt': c[:a.T // 2 + 1].tolist(),
           'm1_cosh_exakt': meff, 'G0': G0, 'E_kubisch_2asinh': 2 * math.asinh(a.m / 2),
           'einschleife': [einschleife(a.m, l, a.beta, G0, vol, a.qmax) for l in a.lams],
           'lam_stern_max_anziehung': a.m * a.m / (18 * a.beta * G0),
           'lam_eff_max': a.m * a.m / (36 * a.beta * G0)}
    log(res)
    schreibe_json(a.out, res)


# ------------------------------------------------------------------------------------------------ Auswertung
def tau_int(x, S=1.5):
    """Wolff (2004), automatisches Fenster."""
    x = np.asarray(x, float)
    N = len(x)
    x = x - x.mean()
    if x.var() == 0:
        return 0.5, 0, 0.0
    f = np.fft.rfft(x, 2 * N)
    acf = np.fft.irfft(f * np.conj(f))[:N] / (N - np.arange(N))
    rho = acf / acf[0]
    t = 0.5
    W = 1
    for W in range(1, N // 2):
        t += rho[W]
        if t <= 0.5:
            tW = 1e-6
        else:
            tW = S / math.log((2 * t + 1) / (2 * t - 1))
        g = math.exp(-W / tW) - tW / math.sqrt(W * N)
        if g < 0:
            break
    dt = t * math.sqrt(4 * (W + 0.5 - t) / N)
    return float(t), int(W), float(dt)


def abgeleitet(C, qmax, T):
    """Aus einem Mittel C (ncorr, T2): effektive Massen und Verschiebungen je tau."""
    T2 = C.shape[1]
    out = {}
    c1 = C[0]
    with np.errstate(all='ignore'):
        m1c = np.full(T2, np.nan)
        for t in range(1, T2 - 1):
            r = (c1[t + 1] + c1[t - 1]) / (2 * c1[t])
            m1c[t] = math.acosh(r) if r >= 1 else np.nan
        m1l = np.full(T2, np.nan)
        m1l[:-1] = np.log(c1[:-1] / c1[1:])
        out['m1_cosh'] = m1c
        out['m1_log'] = m1l
        for Q in range(2, qmax + 1):
            b = 1 + 3 * (Q - 2)
            cll, cpp, clp = C[b], C[b + 1], C[b + 2]
            for nm, cc in (('ll', cll), ('pp', cpp)):
                e = np.full(T2, np.nan)
                e[:-1] = np.log(cc[:-1] / cc[1:])
                out['E%d_%s' % (Q, nm)] = e
                out['dE%d_%s' % (Q, nm)] = e - Q * m1c
            # GEVP 2x2, t0 = 1
            t0 = 1
            M0 = np.array([[cll[t0], clp[t0]], [clp[t0], cpp[t0]]])
            lam = np.full((T2, 2), np.nan)
            try:
                w, V = np.linalg.eigh(M0)
                if w.min() > 0:
                    Wm = V @ np.diag(w ** -0.5) @ V.T
                    for t in range(T2):
                        Mt = Wm @ np.array([[cll[t], clp[t]], [clp[t], cpp[t]]]) @ Wm
                        lam[t] = np.sort(np.linalg.eigvalsh(Mt))[::-1]
            except np.linalg.LinAlgError:
                pass
            for i in range(2):
                e = np.full(T2, np.nan)
                e[:-1] = np.log(lam[:-1, i] / lam[1:, i])
                out['E%d_gevp%d' % (Q, i)] = e
                out['dE%d_gevp%d' % (Q, i)] = e - Q * m1c
    return out


def plateau(zentral, jk, tmin, emax, tmax=None):
    """Gewichtetes Mittel ueber tau in [tmin, letzte zusammenhaengende Stelle mit Fehler < emax]; Fehler per Jackknife."""
    nb = jk.shape[0]
    err = np.sqrt((nb - 1) / nb * ((jk - jk.mean(0)) ** 2).sum(0))
    ts = []
    for t in range(tmin, len(zentral) if tmax is None else min(tmax + 1, len(zentral))):
        if np.isfinite(zentral[t]) and np.isfinite(err[t]) and err[t] < emax and np.all(np.isfinite(jk[:, t])):
            ts.append(t)
        else:
            break
    if len(ts) == 0:
        return None
    w = 1 / err[ts] ** 2
    w /= w.sum()
    v = float((zentral[ts] * w).sum())
    vj = (jk[:, ts] * w).sum(1)
    e = float(math.sqrt((nb - 1) / nb * ((vj - vj.mean()) ** 2).sum()))
    return {'wert': v, 'fehler': e, 'fenster': [ts[0], ts[-1]], 'n_t': len(ts)}


def modus_aus(a):
    Cs, p2, dH, acc, info = [], [], [], [], []
    par = None
    for p in a.ein:
        z = np.load(p, allow_pickle=False)
        pp = json.loads(str(z['par']))
        if par is None:
            par = pp
        for k in ('graph', 'T', 'dt', 'm', 'lam', 'beta', 'qmax'):
            assert pp[k] == par[k], (p, k)
        Cs.append(np.array(z['C'], float))
        p2.append(z['phi2'])
        dH.append(z['dH'])
        acc.append(z['acc'])
        info.append({'datei': p, 'ntraj': int(len(z['dH'])), 'sha256': sha(p)})
    C = np.concatenate(Cs)
    p2, dH, acc = np.concatenate(p2), np.concatenate(dH), np.concatenate(acc)
    T, qmax = par['T'], par['qmax']
    N = len(C)
    log('Trajektorien', N, 'Teile', len(a.ein))
    # Autokorrelation
    beob = {'phi2': p2, 'C1_t0': C[:, 0, 0], 'C1_t2': C[:, 0, 2], 'C1_t4': C[:, 0, 4]}
    if qmax >= 2:
        beob['C2pp_t1'] = C[:, 2, 1]
        beob['C2ll_t1'] = C[:, 1, 1]
    taus = {k: tau_int(v) for k, v in beob.items()}
    tmax_int = max(t for t, W, e in taus.values())
    B = a.bin if a.bin > 0 else max(1, int(math.ceil(4 * tmax_int)))
    nb = N // B
    Cb = C[:nb * B].reshape(nb, B, *C.shape[1:]).mean(1)
    Cm = Cb.mean(0)
    jk = (Cb.sum(0)[None] - Cb) / (nb - 1)
    zen = abgeleitet(Cm, qmax, T)
    jks = [abgeleitet(jk[i], qmax, T) for i in range(nb)]
    keys = list(zen.keys())
    J = {k: np.array([j[k] for j in jks]) for k in keys}
    fehler = {k: np.sqrt((nb - 1) / nb * ((J[k] - J[k].mean(0)) ** 2).sum(0)) for k in keys}
    # Fehler gegen Binbreite (m1 bei tau = 4, dE2_pp bei tau = 2)
    bin_scan = []
    for Bs in (1, 2, 4, 8, 16, 32, 64, 128):
        nbs = N // Bs
        if nbs < 20:
            break
        Cbs = C[:nbs * Bs].reshape(nbs, Bs, *C.shape[1:]).mean(1)
        jks_ = (Cbs.sum(0)[None] - Cbs) / (nbs - 1)
        vals = np.array([[abgeleitet(jks_[i], qmax, T)['m1_cosh'][4],
                          abgeleitet(jks_[i], qmax, T)['dE2_pp'][2] if qmax >= 2 else np.nan] for i in range(nbs)])
        bin_scan.append({'B': Bs, 'nb': nbs, 'err_m1_t4': float(np.sqrt((nbs - 1) / nbs * ((vals[:, 0] - vals[:, 0].mean()) ** 2).sum())),
                         'err_dE2pp_t2': float(np.sqrt((nbs - 1) / nbs * ((vals[:, 1] - vals[:, 1].mean()) ** 2).sum()))})
    # Plateaus
    pl = {'m1_cosh': plateau(zen['m1_cosh'], J['m1_cosh'], a.tmin1, a.emax1)}
    for Q in range(2, qmax + 1):
        for nm in ('pp', 'll', 'gevp0'):
            pl['E%d_%s' % (Q, nm)] = plateau(zen['E%d_%s' % (Q, nm)], J['E%d_%s' % (Q, nm)], a.tminq, a.emaxq)
            pl['dE%d_%s' % (Q, nm)] = plateau(zen['dE%d_%s' % (Q, nm)], J['dE%d_%s' % (Q, nm)], a.tminq, a.emaxq)
    eff = {k: [[None if not np.isfinite(zen[k][t]) else float(zen[k][t]),
                None if not np.isfinite(fehler[k][t]) else float(fehler[k][t])] for t in range(len(zen[k]))] for k in keys}
    res = {'par': par, 'teile': info, 'ntraj': N, 'akzeptanz': float(acc.mean()), 'exp_mdH': float(np.exp(-dH).mean()),
           'exp_mdH_fehler': float(np.exp(-dH).std() / math.sqrt(N / max(1.0, 2 * tmax_int))),
           'phi2': float(p2.mean()), 'tau_int': taus, 'bin': B, 'nb': nb, 'bin_scan': bin_scan, 'plateau': pl,
           'eff': eff, 'C_mittel': Cm.tolist(), 'plateau_regel': {'tmin1': a.tmin1, 'emax1': a.emax1, 'tminq': a.tminq,
                                                                   'emaxq': a.emaxq}}
    if par['lam'] == 0 and a.frei:
        Lap, s0, _ = graph_laden(par['graph'])
        c, G0 = frei_exakt(Lap, s0, T, par['dt'], par['m'])
        T2 = T // 2 + 1
        res['frei'] = {'C1_exakt': c[:T2].tolist(), 'G0_exakt': G0,
                       'C1_mc_durch_exakt': [[float(Cm[0, t] / c[t]),
                                              float(np.sqrt((nb - 1) / nb * ((jk[:, 0, t] - jk[:, 0, t].mean()) ** 2).sum()) / c[t])]
                                             for t in range(T2)]}
    # kurze Zusammenfassung ins Log
    log('tau_int', taus, 'B', B, 'nb', nb)
    log('Akzeptanz %.3f, <exp(-dH)> %.4f' % (res['akzeptanz'], res['exp_mdH']))
    for k, v in pl.items():
        log(k, v)
    schreibe_json(a.out, res)


# ------------------------------------------------------------------------------------------------ klassisch
def qball_kont(om, beta=0.5, rmax=80.0):
    """Wie sm.qball_kont (Schiessen auf f(0), Bisektion), Papier I in Q-Ball-Einheiten; gibt Q, E zurueck."""
    from scipy.integrate import solve_ivp
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
    rr = np.linspace(1e-4, s.t[-1], 40001)
    y = s.sol(rr)
    f, fp = y[0], y[1]
    icut = int(np.argmin(np.where(f > 0, f, np.inf)))
    kap = math.sqrt(1 - om ** 2)
    r_all = np.linspace(0.0, rmax, 160001)
    f_all = np.interp(r_all, rr[:icut + 1], f[:icut + 1])
    fp_all = np.interp(r_all, rr[:icut + 1], fp[:icut + 1])
    rc = rr[icut]
    tail = r_all > rc
    f_all[tail] = f[icut] * np.exp(-kap * (r_all[tail] - rc)) * rc / r_all[tail]
    fp_all[tail] = -f_all[tail] * (kap + 1.0 / r_all[tail])
    S = f_all ** 2
    w4 = 4 * np.pi * r_all ** 2
    I2 = float(np.trapezoid(w4 * S, r_all))
    E = om ** 2 * I2 + float(np.trapezoid(w4 * fp_all ** 2, r_all)) + float(np.trapezoid(w4 * (S - S ** 2 + beta * S ** 3), r_all))
    Q = 2 * om * I2
    rho = om ** 2 * S + fp_all ** 2 + (S - S ** 2 + beta * S ** 3)
    Mr = np.concatenate([[0.0], np.cumsum(0.5 * (w4[1:] * rho[1:] + w4[:-1] * rho[:-1]) * np.diff(r_all))])
    return {'om': om, 'f0': f0, 'r_cut': float(rc), 'Q': Q, 'E': E, 'E_durch_Q': E / Q,
            'r_halb': float(np.interp(0.5 * E, Mr, r_all)), 'bisektion_breite': hi - lo, 'rmax': rmax}


def modus_klass(a):
    oms = [round(x, 4) for x in np.arange(a.om_von, a.om_bis + 1e-9, a.om_schritt)]
    fam = []
    for om in oms:
        rmax = 80.0 if om < 0.95 else 200.0
        k = qball_kont(om, a.beta, rmax)
        fam.append(k)
        log('om %.4f Q %.3f E %.3f E/Q %.5f r_halb %.2f r_cut %.1f' % (om, k['Q'], k['E'], k['E_durch_Q'], k['r_halb'], k['r_cut']))
    Qs = np.array([k['Q'] for k in fam])
    Es = np.array([k['E'] for k in fam])
    i = int(np.argmin(Qs))
    # stabiler Ast: om <= om(Q_min), dort faellt Q mit om
    stab = [k for k in fam if k['om'] <= fam[i]['om']]
    Qst = np.array([k['Q'] for k in stab])[::-1]
    Est = np.array([k['E'] for k in stab])[::-1]
    gebunden_ab = None
    bq = [(k['Q'], k['E'] / k['Q']) for k in stab]
    # Q, ab dem E < Q (Bindung) auf dem stabilen Ast
    for (q1, r1), (q2, r2) in zip(bq[::-1][:-1], bq[::-1][1:]):
        if r1 >= 1 > r2:
            gebunden_ab = q1 + (q2 - q1) * (r1 - 1) / (r1 - r2)
    tab = []
    for lam in a.lams:
        for N in range(1, a.nmax + 1):
            Q0 = lam * N
            if Q0 < Qs[i]:
                tab.append({'lam': lam, 'N': N, 'Q_QB': Q0, 'E_cl_durch_m_N': None, 'grund': 'Q_QB < Q_min'})
            elif Q0 > Qst.max():
                tab.append({'lam': lam, 'N': N, 'Q_QB': Q0, 'E_cl_durch_m_N': None, 'grund': 'jenseits der Tabelle'})
            else:
                E0 = float(np.interp(Q0, Qst, Est))
                tab.append({'lam': lam, 'N': N, 'Q_QB': Q0, 'E_QB': E0, 'E_cl_durch_m': E0 / lam,
                            'E_cl_durch_m_N': E0 / Q0})
    res = {'beta': a.beta, 'familie': fam, 'Q_min': float(Qs[i]), 'om_Q_min': fam[i]['om'], 'E_Q_min': float(Es[i]),
           'E_durch_Q_bei_Q_min': float(Es[i] / Qs[i]), 'gebunden_ab_Q_QB': gebunden_ab, 'tabelle': tab,
           'regel': 'E_cl(N) = (m/lam) E_QB(Q_QB = lam N), stabiler Ast (om <= om(Q_min)); Bindung je Teilchen 1 - E_QB/Q_QB'}
    log('Q_min', res['Q_min'], 'om', res['om_Q_min'], 'E/Q', res['E_durch_Q_bei_Q_min'], 'gebunden ab', gebunden_ab)
    schreibe_json(a.out, res)


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest='modus', required=True)
    p = sp.add_parser('netz')
    p.add_argument('--L', type=int, required=True)
    p.add_argument('--out', required=True)
    p = sp.add_parser('frei')
    p.add_argument('--graph', required=True)
    p.add_argument('--T', type=int, default=32)
    p.add_argument('--dt', type=float, default=1.0)
    p.add_argument('--m', type=float, default=0.5)
    p.add_argument('--beta', type=float, default=0.5)
    p.add_argument('--qmax', type=int, default=5)
    p.add_argument('--lams', type=float, nargs='+', default=[0.1, 0.25, 1.0, 10.0])
    p.add_argument('--out', required=True)
    p = sp.add_parser('hmc')
    p.add_argument('--graph', required=True)
    p.add_argument('--T', type=int, default=32)
    p.add_argument('--dt', type=float, default=1.0)
    p.add_argument('--m', type=float, default=0.5)
    p.add_argument('--lam', type=float, required=True)
    p.add_argument('--beta', type=float, default=0.5)
    p.add_argument('--qmax', type=int, default=5)
    p.add_argument('--tau', type=float, default=2.0)
    p.add_argument('--nmd', type=int, default=12)
    p.add_argument('--ntherm', type=int, default=500)
    p.add_argument('--ntherm_fort', type=int, default=0)
    p.add_argument('--ntraj', type=int, default=0)
    p.add_argument('--tmax', type=float, default=520.0)
    p.add_argument('--seed', type=int, default=1)
    p.add_argument('--start', default=None)
    p.add_argument('--out', required=True)
    p = sp.add_parser('aus')
    p.add_argument('--ein', nargs='+', required=True)
    p.add_argument('--bin', type=int, default=0)
    p.add_argument('--tmin1', type=int, default=3)
    p.add_argument('--emax1', type=float, default=0.02)
    p.add_argument('--tminq', type=int, default=2)
    p.add_argument('--emaxq', type=float, default=0.05)
    p.add_argument('--frei', action='store_true')
    p.add_argument('--out', required=True)
    p = sp.add_parser('klass')
    p.add_argument('--beta', type=float, default=0.5)
    p.add_argument('--om_von', type=float, default=0.80)
    p.add_argument('--om_bis', type=float, default=0.99)
    p.add_argument('--om_schritt', type=float, default=0.005)
    p.add_argument('--lams', type=float, nargs='+', default=[0.1, 0.25, 1.0, 2.0, 10.0, 30.0, 60.0])
    p.add_argument('--nmax', type=int, default=6)
    p.add_argument('--out', required=True)
    a = ap.parse_args()
    {'netz': modus_netz, 'frei': modus_frei, 'hmc': modus_hmc, 'aus': modus_aus, 'klass': modus_klass}[a.modus](a)


if __name__ == '__main__':
    main()
