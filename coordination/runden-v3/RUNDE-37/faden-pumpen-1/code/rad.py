#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""FADEN-PUMPEN-1 (Runde 50), Rechen-Agent fuer die Leitung claude-primary, 05.10.2026.

Kontinuum (radial) fuer zwei gerade, unendlich lange Faeden laengs z:
 (a) Q-Schlauch: phi = f(r) exp(i om t), U(S) = S - S^2 + S^3/2 (Papier I, m = 1), 2D-Querschnitt.
     Kleine Schwingungen im mitdrehenden System: psi = f + u + i v, Ansatz u, v ~ g(r) cos(n theta) exp(i k z + lam t):
       u_tt = 2 om v_t - H+ u,  v_tt = -2 om u_t - H- v,
       H+ = -Lap_n + k^2 + U'(f^2) + 2 f^2 U''(f^2) - om^2,  H- = -Lap_n + k^2 + U'(f^2) - om^2.
     Eigenwerte lam der 4N-Matrix; Re lam > 0 = Wachstum, Im lam = Frequenz im mitdrehenden System.
     Kenngroessen je Laenge: I = Int f^2, G = Int |grad f|^2, V = Int U, q = 2 om I, mu = om^2 I + G + V, T = G.
     Erwartung aus dem Aufbau [M]: c_b^2 = T/mu (Biegen), c_s^2 = q / (om dq/dom) (Ladungsform).
 (b) Wirbelfaden: phi = f(r) exp(i theta), U_b(S) = (S - 1)^2 / 4 (Feldmasse der Betragsform m_h = 1, v = 1).
     Statisch, daher Omega^2(k) = Omega^2(0) + k^2 exakt; gerechnet nur Omega^2(0) je n (Kanaele |n+1|, |n-1|).
Diskretisierung: Finite Volumen, Zellmitten r_j = (j + 1/2) dr, Dirichlet hinter r_max.
Aufruf nur ueber kleintest.sh auf der .69:
  python rad.py qschlauch --oms 0.72 0.75 0.8 0.85 0.9 0.95 --dr 0.05 --rmax 60 --out lauf/rad-q.json
  python rad.py wirbel --rmaxs 20 40 80 --dr 0.05 --out lauf/rad-w.json
"""
import argparse, json, os, sys, time, math, hashlib, platform, resource
import numpy as np
import scipy
import scipy.sparse as sps
import scipy.sparse.linalg as spla
from scipy.integrate import solve_ivp
from scipy.linalg import solve_banded

T0 = time.time()
BETA = 0.5


def log(*a):
    print('[%7.1f s]' % (time.time() - T0), *a, flush=True)


def sha(p):
    with open(p, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def schreibe(pfad, res):
    res['_meta'] = {'argv': sys.argv, 'python': platform.python_version(), 'numpy': np.__version__,
                    'scipy': scipy.__version__, 'host': platform.node(), 'laufzeit_s': time.time() - T0,
                    'maxrss_MB': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
                    'ende_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
                    'sha256_rad': sha(os.path.abspath(__file__))}
    with open(pfad + '.tmp', 'w') as fh:
        json.dump(res, fh, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
    os.replace(pfad + '.tmp', pfad)
    log('->', pfad)


def U(S):
    return S - S ** 2 + BETA * S ** 3


def Up(S):
    return 1.0 - 2.0 * S + 3.0 * BETA * S ** 2


def Upp(S):
    return -2.0 + 6.0 * BETA * S


class Radial:
    def __init__(self, dr, rmax):
        self.dr = dr
        self.N = N = int(round(rmax / dr))
        self.r = (np.arange(N) + 0.5) * dr
        rf = np.arange(N + 1) * dr                 # Raender r_{j-1/2}, j = 0..N
        self.V = self.r * dr                        # Volumen je Zelle / (2 pi)
        self.Ap = rf[1:] / dr                       # Fluss nach aussen (j -> j+1), letzter: zur Randzelle
        self.Am = rf[:-1] / dr                      # Fluss nach innen (j -> j-1), erster = 0

    def lap(self, n):
        """-Lap_n als duenn besetzte Matrix (Dirichlet 0 hinter r_max); symmetrisch mit Gewicht V."""
        N = self.N
        d = (self.Ap + self.Am) / self.V + n * n / self.r ** 2
        o = -self.Ap[:-1]
        return sps.diags([d, o / self.V[:-1], o / self.V[1:]], [0, 1, -1], format='csr')

    def lap_sym(self, n):
        """V^{1/2} (-Lap_n) V^{-1/2}, symmetrisch."""
        N = self.N
        d = (self.Ap + self.Am) / self.V + n * n / self.r ** 2
        o = -self.Ap[:-1] / np.sqrt(self.V[:-1] * self.V[1:])
        return sps.diags([d, o, o], [0, 1, -1], format='csr')

    def integ(self, g):
        return float(2 * np.pi * np.sum(self.V * g))

    def grad2(self, f, rand=0.0):
        fp = np.append(f[1:], rand)
        return float(2 * np.pi * np.sum(self.Ap * self.dr * (fp - f) ** 2 / self.dr ** 2 * self.dr))


# ------------------------------------------------------------------------------------------------ (a) Q-Schlauch
def schuss2d(om, rmax=80.0):
    F = lambda f: (1 - om ** 2) * f - 2 * f ** 3 + 3 * BETA * f ** 5
    disk = 1 - 4 * BETA * (1 - om ** 2)
    S0 = (1 - math.sqrt(disk)) / (2 * BETA)
    Sp = (2 + math.sqrt(4 - 12 * BETA * (1 - om ** 2))) / (6 * BETA)
    lo, hi = math.sqrt(S0) * (1 + 1e-12), math.sqrt(Sp) * (1 - 1e-15)

    def rhs(r, y):
        return [y[1], F(y[0]) - 1.0 / r * y[1]]

    def ev0(r, y):
        return y[0]
    ev0.terminal = True
    ev0.direction = -1

    def ev1(r, y):
        return y[1]
    ev1.terminal = True
    ev1.direction = 1

    def schiess(f0, dense=False):
        r0 = 1e-5
        y0 = [f0 + F(f0) * r0 ** 2 / 4.0, F(f0) * r0 / 2.0]
        return solve_ivp(rhs, (r0, rmax), y0, method='DOP853', rtol=1e-12, atol=1e-14, events=(ev0, ev1),
                         dense_output=dense)
    for _ in range(90):
        mid = 0.5 * (lo + hi)
        s = schiess(mid)
        if len(s.t_events[0]):
            hi = mid
        else:
            lo = mid
        if hi - lo < 1e-16:
            break
    f0 = 0.5 * (lo + hi)
    s = schiess(f0, dense=True)
    return f0, s


def profil_q(om, R):
    f0, s = schuss2d(om)
    rr = np.linspace(1e-5, s.t[-1], 40001)
    y = s.sol(rr)
    f = y[0]
    pos = f > 0
    icut = int(np.argmin(np.where(pos, f, np.inf)))
    kap = math.sqrt(1 - om ** 2)
    rc = rr[icut]
    g = np.interp(R.r, rr[:icut + 1], f[:icut + 1])
    tail = R.r > rc
    g[tail] = f[icut] * np.exp(-kap * (R.r[tail] - rc)) * np.sqrt(rc / R.r[tail])
    # Newton auf dem diskreten Gitter (fester om)
    L0 = R.lap(0)
    for it in range(40):
        S = g * g
        Fv = L0 @ g + (Up(S) - om ** 2) * g
        nr = float(np.abs(Fv).max())
        if nr < 1e-12:
            break
        J = (L0 + sps.diags(Up(S) + 2 * S * Upp(S) - om ** 2)).tocsc()
        dg = spla.spsolve(J, -Fv)
        g = g + dg
    S = g * g
    Fv = L0 @ g + (Up(S) - om ** 2) * g
    return g, {'f0_schuss': f0, 'r_schuss_ende': float(rc), 'newton_it': it, 'rest_max': float(np.abs(Fv).max()),
               'f0_gitter': float(g[0])}


def kenn_q(om, R, f):
    S = f * f
    I = R.integ(S)
    G = R.grad2(f)
    Vp = R.integ(U(S))
    q = 2 * om * I
    mu = om ** 2 * I + G + Vp
    # dq/dom aus L+ f_om = 2 om f
    L0 = R.lap(0)
    J = (L0 + sps.diags(Up(S) + 2 * S * Upp(S) - om ** 2)).tocsc()
    fom = spla.spsolve(J, 2 * om * f)
    dI = 2 * R.integ(f * fom)
    dq = 2 * I + 2 * om * dI
    # Radien
    cum = np.cumsum(2 * np.pi * R.V * S)
    r_halb = float(np.interp(0.5 * I, cum, R.r))
    i_w = int(np.argmax(S < 0.5 * S[0]))
    r_wand = float(np.interp(0.5 * S[0], S[i_w::-1], R.r[i_w::-1])) if i_w > 0 else float('nan')
    r_rms = math.sqrt(R.integ(R.r ** 2 * S) / I)
    T = G
    return {'om': om, 'I': I, 'G': G, 'V': Vp, 'q': q, 'mu_E_je_Laenge': mu, 'T_Spannung': T,
            'derrick_V_minus_om2I_rel': (Vp - om ** 2 * I) / mu, 'dq_dom': dq, 'E_minus_q_rel': (mu - q) / mu,
            'cb2_T_durch_mu': T / mu, 'cs2_q_durch_om_dqdom': q / (om * dq), 'r_halb': r_halb, 'r_wand': r_wand,
            'r_rms': r_rms, 'S_mitte': float(S[0])}


def spektrum_q(om, R, f, n, k, nev=14, sigma=None):
    try:
        return _spektrum_q(om, R, f, n, k, nev, sigma)
    except Exception as ex:  # ARPACK-Fehler nicht den ganzen Lauf kosten lassen
        log("eigs-Fehler", om, n, k, repr(ex)[:200])
        return []


def _spektrum_q(om, R, f, n, k, nev=14, sigma=None):
    S = f * f
    N = R.N
    Ls = R.lap_sym(n)
    Hp = Ls + sps.diags(k * k + Up(S) + 2 * S * Upp(S) - om ** 2)
    Hm = Ls + sps.diags(k * k + Up(S) - om ** 2)
    I = sps.identity(N, format='csr')
    Z = sps.csr_matrix((N, N))
    A = sps.bmat([[Z, Z, I, Z], [Z, Z, Z, I], [-Hp, Z, Z, 2 * om * I], [Z, -Hm, -2 * om * I, Z]], format='csc')
    sig = sigma if sigma is not None else 1e-3
    w, vec = spla.eigs(A, k=nev, sigma=sig, which='LM', tol=1e-12)
    # Lokalisierung: Anteil der Norm von (u, v) in r < r_cut
    out = []
    for j in range(len(w)):
        x = vec[:, j]
        u, v = x[:N], x[N:2 * N]
        nn = np.abs(u) ** 2 + np.abs(v) ** 2
        tot = nn.sum()
        out.append({'re': float(w[j].real), 'im': float(w[j].imag),
                    'anteil_u': float((np.abs(u) ** 2).sum() / tot),
                    'r_schwer': float((nn * R.r).sum() / tot)})
    out.sort(key=lambda d: (abs(d['im']), -d['re']))
    return out


def auswerten_q(sp):
    """Groesste Wachstumsrate und kleinste positive Frequenzen (nur Moden mit |Re| < 1e-7)."""
    gam = max([d['re'] for d in sp] + [0.0])
    fr = sorted(set(round(d['im'], 10) for d in sp if d['im'] > 1e-9 and abs(d['re']) < 1e-7))
    return gam, fr


def modus_q(a):
    R = Radial(a.dr, a.rmax)
    res = {'dr': a.dr, 'rmax': a.rmax, 'familie': []}
    for om in a.oms:
        f, info = profil_q(om, R)
        kk = kenn_q(om, R, f)
        kk.update(info)
        log('om', om, kk)
        ks = list(a.ks)
        eintrag = {'kenn': kk, 'n': {}}
        for n in (0, 1, 2, 3):
            zeilen = []
            for k in ks:
                sp = spektrum_q(om, R, f, n, k)
                gam, fr = auswerten_q(sp)
                zeilen.append({'k': k, 'gamma': gam, 'omega_rot': fr[:6],
                               'moden': [d for d in sp if d['im'] >= -1e-12][:8]})
            eintrag['n'][str(n)] = zeilen
            log('  n', n, [(z['k'], round(z['gamma'], 6), [round(x, 5) for x in z['omega_rot'][:3]]) for z in zeilen])
        # Schwelle k_c (n = 0) per Bisektion zwischen dem letzten k mit gamma > 0 und dem ersten ohne
        z0 = eintrag['n']['0']
        kc = None
        for i in range(len(z0) - 1):
            if z0[i]['gamma'] > 1e-7 and z0[i + 1]['gamma'] <= 1e-7:
                lo, hi = z0[i]['k'], z0[i + 1]['k']
                for _ in range(22):
                    mid = 0.5 * (lo + hi)
                    g, _ = auswerten_q(spektrum_q(om, R, f, 0, mid))
                    if g > 1e-7:
                        lo = mid
                    else:
                        hi = mid
                kc = 0.5 * (lo + hi)
        # Maximum der Wachstumsrate (Gitter verfeinern)
        gmax, kmax = 0.0, None
        for z in z0:
            if z['gamma'] > gmax:
                gmax, kmax = z['gamma'], z['k']
        if kmax is not None and kc is not None:
            kf = np.linspace(max(kmax * 0.6, 1e-3), min(kmax * 1.4, kc), 15)
            for k in kf:
                g, _ = auswerten_q(spektrum_q(om, R, f, 0, float(k)))
                if g > gmax:
                    gmax, kmax = g, float(k)
        # Anfangssteigungen: gamma/k bei kleinem k (n = 0), Omega/k (n = 1)
        kl = [z for z in z0 if 0 < z['k'] <= 0.021]
        st0 = [z['gamma'] / z['k'] for z in kl]
        z1 = eintrag['n']['1']
        st1 = [(z['k'], z['omega_rot'][0] if z['omega_rot'] else None) for z in z1 if 0 < z['k'] <= 0.051]
        eintrag['auswertung'] = {'k_c': kc, 'gamma_max': gmax, 'k_max': kmax,
                                 'kc_r_halb': kc * kk['r_halb'] if kc else None,
                                 'kc_r_wand': kc * kk['r_wand'] if kc else None,
                                 'kmax_r_halb': kmax * kk['r_halb'] if kmax else None,
                                 'gamma_durch_k_klein': st0, 'cs_betrag_erwartet': math.sqrt(-kk['cs2_q_durch_om_dqdom'])
                                 if kk['cs2_q_durch_om_dqdom'] < 0 else None,
                                 'omega1_klein': st1, 'cb_erwartet': math.sqrt(kk['cb2_T_durch_mu']),
                                 'schwelle_kontinuum_rot': 1 - om}
        log('  auswertung', eintrag['auswertung'])
        res["familie"].append(eintrag)
        schreibe(a.out, res)
    schreibe(a.out, res)


# ------------------------------------------------------------------------------------------------ (b) Wirbel
def Ub(S):
    return 0.25 * (S - 1.0) ** 2


def Ubp(S):
    return 0.5 * (S - 1.0)


def Ubpp(S):
    return 0.5 + 0 * S


def profil_w(R):
    # -Lap_1 f + Ub'(f^2) f = 0, f(r_max) = 1 (Randwert in der Randzelle)
    L1 = R.lap(1)
    rand = np.zeros(R.N)
    rand[-1] = R.Ap[-1] / R.V[-1] * 1.0          # Beitrag des Randwerts f = 1
    g = np.tanh(R.r / 1.5)
    for it in range(60):
        S = g * g
        Fv = L1 @ g - rand + Ubp(S) * g
        nr = float(np.abs(Fv).max())
        if nr < 1e-12:
            break
        J = (L1 + sps.diags(Ubp(S) + 2 * S * Ubpp(S))).tocsc()
        g = g + spla.spsolve(J, -Fv)
    S = g * g
    Fv = L1 @ g - rand + Ubp(S) * g
    r_halb = float(np.interp(0.5, g, R.r))
    return g, {'newton_it': it, 'rest_max': float(np.abs(Fv).max()), 'r_f_halb': r_halb}


def spektrum_w(R, f, n, nev=10):
    S = f * f
    N = R.N
    W = Ubp(S) + Ubpp(S) * S
    C = Ubpp(S) * S
    if n == 0:
        Ha = R.lap_sym(1) + sps.diags(Ubp(S) + 2 * Ubpp(S) * S)       # Betrag
        Hp = R.lap_sym(1) + sps.diags(Ubp(S))                          # Phase
        res = {}
        for nm, H in (('betrag', Ha), ('phase', Hp)):
            w, vec = spla.eigsh(H.tocsc(), k=nev, sigma=-1e-3, which='LM')
            o = np.argsort(w)
            res[nm] = [{'omega2': float(w[j]), 'r_schwer': float((vec[:, j] ** 2 * R.r).sum() / (vec[:, j] ** 2).sum())}
                       for j in o]
        return res
    H = sps.bmat([[R.lap_sym(abs(n + 1)) + sps.diags(W), sps.diags(C)],
                  [sps.diags(C), R.lap_sym(abs(n - 1)) + sps.diags(W)]], format='csc')
    w, vec = spla.eigsh(H, k=nev, sigma=-1e-3, which='LM')
    o = np.argsort(w)
    out = []
    for j in o:
        x = vec[:, j]
        aa, bb = x[:N], x[N:]
        nn = aa ** 2 + bb ** 2
        # Betragsanteil: Re(chi) = a + b (fuer cos), Phasenanteil a - b
        out.append({'omega2': float(w[j]), 'r_schwer': float((nn * R.r).sum() / nn.sum()),
                    'betrag_anteil': float(((aa + bb) ** 2).sum() / (2 * nn.sum()))})
    return {'block': out}


def modus_w(a):
    res = {'dr': a.dr, 'laeufe': []}
    for rmax in a.rmaxs:
        R = Radial(a.dr, rmax)
        f, info = profil_w(R)
        S = f * f
        e_kern = R.integ(Ub(S))
        log('rmax', rmax, info, 'E_pot', e_kern)
        ein = {'rmax': rmax, 'profil': info, 'E_pot': e_kern, 'n': {}}
        for n in (0, 1, 2, 3):
            sp = spektrum_w(R, f, n)
            ein['n'][str(n)] = sp
            log('  n', n, json.dumps(sp)[:600])
        res['laeufe'].append(ein)
    schreibe(a.out, res)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('modus', choices=['qschlauch', 'wirbel'])
    ap.add_argument('--oms', type=float, nargs='*', default=[0.72, 0.75, 0.8, 0.85, 0.9, 0.95])
    ap.add_argument('--ks', type=float, nargs='*',
                    default=[0.0, 0.005, 0.01, 0.02, 0.03, 0.05, 0.075, 0.1, 0.125, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4,
                             0.5, 0.6, 0.7, 0.8, 1.0, 1.2, 1.5])
    ap.add_argument('--rmaxs', type=float, nargs='*', default=[20.0, 40.0, 80.0])
    ap.add_argument('--dr', type=float, default=0.05)
    ap.add_argument('--rmax', type=float, default=60.0)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    log('start', time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), sys.argv)
    {'qschlauch': modus_q, 'wirbel': modus_w}[a.modus](a)


if __name__ == '__main__':
    main()
