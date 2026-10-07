#!/usr/bin/env python3
"""stille3.py - Runde 17 STILLE-ZWEIFELD, eigener Code des Code-Agenten (2026-10-02).

Stille Stellen der radialen Atmungsmode l = 0 im Zweifeldmodell M2, drei Kanaele (a, b, c' = c/2).
Methode und Wertung: PLAN.md (eingefroren). Profil: Numerov-Newton fuer F = r f, H = r (g - 1).
Kanaele: u'' = (M - E) u mit symmetrischem M, RK4, Gram-Schmidt, Abgleich bei r_m (Wronski-Matrix G).
"""
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'
import sys
import json
import time
import math
import numpy as np
from scipy.linalg import solve_banded

HIER = os.path.dirname(os.path.abspath(__file__))
STUFEN = {0: 0.02, 1: 0.01, 2: 0.005}   # hp; Kanalschritt h = 2 hp. Stufe 0 nur Rauchtest.
RAND = 1e-3
N_E1, N_E2, N_E3 = 301, 301, 151
RHO_MAX = 3.0
SQ2 = math.sqrt(2.0)
GS_LEN = 0.5
SPRUNG = 0.4
HALB = 1e-3
NKANTE = 16
RUNDEN = 24
MAXPKT = 3000
ZEILEN = [round(0.75 + 0.02 * j, 10) for j in range(61)]
K2_W2 = [0.76, 0.90, 1.10, 1.30, 1.50, 1.70, 1.84, 1.94]
EICH_W2 = [0.85, 1.25, 1.65, 1.93]
K1_W2 = [0.78, 0.79, 0.80, 0.81, 0.82]
K1_STELLE = (0.797677, 1.744618)
T0 = time.time()


def log(*a):
    print('[%7.1fs]' % (time.time() - T0), *a, flush=True)


def schreibe(pfad, obj):
    d = os.path.dirname(pfad)
    if d:
        os.makedirs(d, exist_ok=True)
    with open(pfad + '.tmp', 'w') as fh:
        json.dump(obj, fh, indent=1)
    os.replace(pfad + '.tmp', pfad)


# ------------------------------------------------------------------ Modell
class Modell:
    """U = cpot (g^2-1)^2 + (1 + lam g^2) S - S^2 + S^3/2. M2: lam = 1, cpot = 1/4."""

    def __init__(self, lam=1.0, cpot=0.25):
        self.lam = float(lam)
        self.cpot = float(cpot)
        self.m2 = 1.0 + self.lam
        self.mc2 = 8.0 * self.cpot

    def U(self, S, g):
        return self.cpot * (g * g - 1) ** 2 + (1 + self.lam * g * g) * S - S * S + 0.5 * S ** 3

    def d(self, S, g):
        US = 1 + self.lam * g * g - 2 * S + 1.5 * S * S
        USS = -2 + 3 * S
        Ug = 4 * self.cpot * g * (g * g - 1) + 2 * self.lam * g * S
        Ugg = 4 * self.cpot * (3 * g * g - 1) + 2 * self.lam * S
        USg = 2 * self.lam * g
        return US, USS, Ug, Ugg, USg


def modell_von(tag):
    if tag == 'M2':
        return Modell(1.0, 0.25)
    if tag == 'K1E1':
        return Modell(0.0, 0.5)
    if tag == 'K1E2':
        return Modell(0.0, 0.25)
    raise ValueError(tag)


# ------------------------------------------------------------------ Profil (Numerov-Newton)
def simpson(N, hp):
    w = np.ones(N + 1)
    w[1:-1:2] = 4.0
    w[2:-1:2] = 2.0
    return w * hp / 3.0


def newton_profil(mod, w2, hp, N, F, H, maxit=60, tol=1e-11):
    r = np.arange(N + 1) * hp
    c = hp * hp / 12.0
    ri = r[1:-1]
    F = F.copy()
    H = H.copy()
    F[0] = F[-1] = H[0] = H[-1] = 0.0
    M = N - 1

    def resid(F, H):
        Fi, Hi = F[1:-1], H[1:-1]
        f = Fi / ri
        S = f * f
        g = 1.0 + Hi / ri
        US, USS, Ug, Ugg, USg = mod.d(S, g)
        A = np.zeros(N + 1)
        B = np.zeros(N + 1)
        A[1:-1] = (US - w2) * Fi
        B[1:-1] = ri * Ug
        RF = F[2:] - 2 * Fi + F[:-2] - c * (A[2:] + 10 * A[1:-1] + A[:-2])
        RH = H[2:] - 2 * Hi + H[:-2] - c * (B[2:] + 10 * B[1:-1] + B[:-2])
        return RF, RH, (f, S, g, US, USS, Ug, Ugg, USg)

    RF, RH, aux = resid(F, H)
    rn = max(np.abs(RF).max(), np.abs(RH).max())
    hist = []
    ok = False
    for it in range(maxit):
        f, S, g, US, USS, Ug, Ugg, USg = aux
        AF = US - w2 + 2 * S * USS
        AH = f * USg
        BF = 2 * f * USg
        BH = Ugg
        ab = np.zeros((7, 2 * M))
        ab[3, 0::2] = -2 - 10 * c * AF
        ab[3, 1::2] = -2 - 10 * c * BH
        ab[2, 1::2] = -10 * c * AH
        ab[4, 0::2] = -10 * c * BF
        ab[1, 2::2] = 1 - c * AF[1:]
        ab[0, 3::2] = -c * AH[1:]
        ab[2, 2::2] = -c * BF[1:]
        ab[1, 3::2] = 1 - c * BH[1:]
        ab[5, 0:-2:2] = 1 - c * AF[:-1]
        ab[4, 1:-2:2] = -c * AH[:-1]
        ab[6, 0:-2:2] = -c * BF[:-1]
        ab[5, 1:-2:2] = 1 - c * BH[:-1]
        rhs = np.empty(2 * M)
        rhs[0::2] = -RF
        rhs[1::2] = -RH
        try:
            dx = solve_banded((3, 3), ab, rhs, check_finite=False)
        except Exception:
            return F, H, False, hist, rn
        if not np.all(np.isfinite(dx)):
            return F, H, False, hist, rn
        t = 1.0
        for _ in range(10):
            Fn = F.copy()
            Hn = H.copy()
            Fn[1:-1] += t * dx[0::2]
            Hn[1:-1] += t * dx[1::2]
            RFn, RHn, auxn = resid(Fn, Hn)
            rnn = max(np.abs(RFn).max(), np.abs(RHn).max())
            if np.isfinite(rnn) and rnn <= 1.5 * rn + 1e-14:
                break
            t *= 0.5
        F, H, RF, RH, aux, rn = Fn, Hn, RFn, RHn, auxn, rnn
        sch = t * float(np.abs(dx).max())
        hist.append(sch)
        if not np.isfinite(sch):
            return F, H, False, hist, rn
        if sch < tol * max(1.0, float(np.abs(F).max())) and t == 1.0:
            ok = True
            break
    return F, H, ok, hist, rn


def fg_aus(F, H, hp, N):
    r = np.arange(N + 1) * hp
    f = np.empty(N + 1)
    h = np.empty(N + 1)
    f[1:] = F[1:] / r[1:]
    h[1:] = H[1:] / r[1:]
    f[0] = (4 * f[1] - f[2]) / 3.0
    h[0] = (4 * h[1] - h[2]) / 3.0
    return r, f, 1.0 + h


def profil_info(mod, w2, hp, N, F, H):
    r, f, g = fg_aus(F, H, hp, N)
    S = f * f
    US, USS, Ug, Ugg, USg = mod.d(S, g)
    U = mod.U(S, g)
    wS = simpson(N, hp)
    Q = 8 * math.pi * math.sqrt(w2) * float(np.sum(wS * F * F))
    E = 4 * math.pi * float(np.sum(wS * (2 * w2 * F * F - US * F * F - 0.5 * r * H * Ug + r * r * U)))
    f0 = float(f[0])
    k = int(np.argmax(f < 0.5 * f0))
    rhalf = float(r[k - 1] + (0.5 * f0 - f[k - 1]) * (r[k] - r[k - 1]) / (f[k] - f[k - 1])) if k > 0 else float('nan')
    knoten = int(np.sum(np.diff(np.sign(f[1:-1])) != 0))
    return dict(f0=f0, chi0=float(g[0]), Q=Q, E=E, EQ=E / Q, rhalf=rhalf, knoten=knoten,
                f_rand=float(abs(f[-2]) / f0), g_rand=float(abs(1 - g[-2])), Rbg=float(N * hp))


def gebiet_N(mod, w2, rhalf, hp):
    mu = math.sqrt(mod.m2 - w2)
    R = 0.02 * math.ceil((1.5 * rhalf + 25.0 / mu + 5.0) / 0.02 - 1e-9)
    N = int(round(R / hp))
    return N + (N % 2)


def uebertrage(prof, hp, N):
    r_alt = np.arange(prof['N'] + 1) * prof['hp']
    r = np.arange(N + 1) * hp
    return (np.interp(r, r_alt, prof['F'], right=0.0), np.interp(r, r_alt, prof['H'], right=0.0))


def loese(mod, w2, hp, N, F, H):
    F, H, ok, hist, res = newton_profil(mod, w2, hp, N, F, H)
    if not ok:
        return None
    if not (abs(F[1] / hp) > 0.2):      # triviale Loesung F = 0 verwerfen
        return None
    info = profil_info(mod, w2, hp, N, F, H)
    if info['knoten'] > 0 or info['f0'] <= 0 or not np.isfinite(info['rhalf']):
        return None
    p = dict(w2=float(w2), hp=float(hp), N=int(N), F=F, H=H, lam=mod.lam, cpot=mod.cpot, newton=hist, res=float(res))
    p.update(info)
    return p


def fortsetzung(mod, prof, w2z, hp, N=None, tiefe=0):
    NN = gebiet_N(mod, w2z, prof['rhalf'], hp) if N is None else N
    F, H = uebertrage(prof, hp, NN)
    if mod.lam == 1.0 and w2z < prof['w2'] and w2z < 1.2 and abs(prof['w2'] - w2z) > 1e-4:
        # Praediktor zur Duennwand-Seite: radiale Streckung r_half ~ 1/(w2 - 0,7281)
        s = (prof['w2'] - 0.7281) / (w2z - 0.7281)
        NN = gebiet_N(mod, w2z, prof['rhalf'] * s, hp) if N is None else N
        r = np.arange(NN + 1) * hp
        r_alt = np.arange(prof['N'] + 1) * prof['hp']
        fa = np.zeros(prof['N'] + 1)
        ha = np.zeros(prof['N'] + 1)
        fa[1:] = prof['F'][1:] / r_alt[1:]
        ha[1:] = prof['H'][1:] / r_alt[1:]
        fa[0] = fa[1]
        ha[0] = ha[1]
        F = r * np.interp(r / s, r_alt, fa, right=0.0)
        H = r * np.interp(r / s, r_alt, ha, right=0.0)
    p = loese(mod, w2z, hp, NN, F, H)
    if p is None:
        if tiefe >= 8:
            return None
        mid = 0.5 * (prof['w2'] + w2z)
        pm = fortsetzung(mod, prof, mid, hp, N, tiefe + 1)
        if pm is None:
            return None
        return fortsetzung(mod, pm, w2z, hp, N, tiefe + 1)
    if N is None:
        # Gebiet nur aus dem eigenen Halbwertsradius (stufenunabhaengig)
        N2 = gebiet_N(mod, w2z, p['rhalf'], hp)
        if N2 != NN:
            F, H = uebertrage(p, hp, N2)
            p2 = loese(mod, w2z, hp, N2, F, H)
            if p2 is not None:
                p = p2
    return p


def saat(mod, mname, Qs, hp):
    sys.path.insert(0, HIER)
    import beutel as b
    M = b.Model(mname)
    Gs = b.Grid(0.04, 40.0)
    f, g = b.initial_profile(M, Gs, Qs)
    f, g, lam, ferr, nfl = b.flow(M, Gs, f, g, Qs)
    f, g, lam, it, err, ok = b.newton_Q(M, Gs, f, g, lam, Qs)
    log('Saat %s Q=%g: Fluss %d Schritte, Newton ok=%s, omega2=%.8f' % (mname, Qs, nfl, ok, lam))
    k = int(np.argmax(f < 0.5 * f[0]))
    rh = float(Gs.r[k])
    N = gebiet_N(mod, lam, rh, hp)
    r = np.arange(N + 1) * hp
    fi = np.interp(r, Gs.r, f, right=0.0)
    gi = np.interp(r, Gs.r, g, right=1.0)
    p = loese(mod, lam, hp, N, r * fi, r * (gi - 1.0))
    if p is None:
        raise RuntimeError('Saat-Newton gescheitert')
    return fortsetzung(mod, p, lam, hp)


def speichere_profil(pfad, p):
    meta = {k: v for k, v in p.items() if k not in ('F', 'H')}
    os.makedirs(os.path.dirname(pfad), exist_ok=True)
    np.savez(pfad + '.tmp.npz', F=p['F'], H=p['H'], meta=json.dumps(meta))
    os.replace(pfad + '.tmp.npz', pfad)


def lade_profil(pfad):
    d = np.load(pfad)
    p = json.loads(str(d['meta']))
    p['F'] = d['F']
    p['H'] = d['H']
    return p


def profil_pfad(pdir, w2):
    return os.path.join(pdir, 'p-%.4f.npz' % w2)


def n_mitte(p):
    rm = 0.02 * round(p['rhalf'] / 0.02)
    rm = max(rm, 0.2)
    return 2 * int(round(rm / (2 * p['hp'])))


# ------------------------------------------------------------------ Kanaele
class Pot:
    def __init__(self, mod, profs):
        self.hp = profs[0]['hp']
        self.N = profs[0]['N']
        K = len(profs)
        self.K = K
        self.Maa = np.empty((K, self.N + 1))
        self.Mab = np.empty((K, self.N + 1))
        self.Mac = np.empty((K, self.N + 1))
        self.Mcc = np.empty((K, self.N + 1))
        for q, p in enumerate(profs):
            assert p['N'] == self.N and abs(p['hp'] - self.hp) < 1e-15
            r, f, g = fg_aus(p['F'], p['H'], self.hp, self.N)
            S = f * f
            US, USS, Ug, Ugg, USg = mod.d(S, g)
            self.Maa[q] = US + S * USS
            self.Mab[q] = S * USS
            self.Mac[q] = f * USg
            self.Mcc[q] = Ugg

    def an(self, qidx, k):
        if self.K == 1:
            return self.Maa[0, k], self.Mab[0, k], self.Mac[0, k], self.Mcc[0, k]
        return (self.Maa[qidx, k][:, None], self.Mab[qidx, k][:, None],
                self.Mac[qidx, k][:, None], self.Mcc[qidx, k][:, None])


def gs(Y, ordnung):
    for _ in range(2):
        fertig = []
        for j in ordnung:
            v = Y[:, :, j]
            for k in fertig:
                w = Y[:, :, k]
                v = v - np.sum(v * w, axis=1, keepdims=True) * w
            Y[:, :, j] = v / np.sqrt(np.sum(v * v, axis=1, keepdims=True))
            fertig.append(j)
    return Y


def integriere(pot, qidx, Ea, Eb, Ec, Y, n0, n1, ordnung):
    hp = pot.hp
    d = 2 if n1 > n0 else -2
    h = d * hp
    gsn = int(round(GS_LEN / hp))

    def acc(u, k):
        a, b, c, e = pot.an(qidx, k)
        out = np.empty_like(u)
        u0, u1, u2 = u[:, 0], u[:, 1], u[:, 2]
        out[:, 0] = (a - Ea) * u0 + b * u1 + c * u2
        out[:, 1] = b * u0 + (a - Eb) * u1 + c * u2
        out[:, 2] = c * (u0 + u1) + (e - Ec) * u2
        return out

    assert (n1 - n0) % 2 == 0, 'ungerade Knotenzahl'
    n = n0
    Y = Y.copy()
    while n != n1:
        u = Y[:, 0:3]
        p = Y[:, 3:6]
        k1p = acc(u, n)
        k2u = p + (0.5 * h) * k1p
        k2p = acc(u + (0.5 * h) * p, n + d // 2)
        k3u = p + (0.5 * h) * k2p
        k3p = acc(u + (0.5 * h) * k2u, n + d // 2)
        k4u = p + h * k3p
        k4p = acc(u + h * k3u, n + d)
        Yn = np.empty_like(Y)
        Yn[:, 0:3] = u + (h / 6.0) * (p + 2 * k2u + 2 * k3u + k4u)
        Yn[:, 3:6] = p + (h / 6.0) * (k1p + 2 * k2p + 2 * k3p + k4p)
        Y = Yn
        n += d
        if n % gsn == 0:
            Y = gs(Y, ordnung)
    return gs(Y, ordnung)


def paar(Y, Z):
    return (np.einsum('pcx,pcy->pxy', Y[:, 0:3], Z[:, 3:6]) - np.einsum('pcx,pcy->pxy', Y[:, 3:6], Z[:, 0:3]))


def energien(w2, rho):
    w = np.sqrt(w2)
    return ((w + rho) ** 2)[:, None], ((w - rho) ** 2)[:, None], (rho ** 2)[:, None]


def isotropie(Y):
    I = paar(Y, Y)
    Ic = (np.einsum('px,py->pxy', Y[:, 2], Y[:, 5]) - np.einsum('px,py->pxy', Y[:, 5], Y[:, 2]))
    return np.max(np.abs(I), axis=(1, 2)), np.max(np.abs(I + 3.0 * Ic), axis=(1, 2))


def regulaer(pot, qidx, E, n_m, ordnung):
    P = E[0].shape[0]
    Y = np.zeros((P, 6, 3))
    for j in range(3):
        Y[:, 3 + j, j] = 1.0
    return integriere(pot, qidx, E[0], E[1], E[2], Y, 0, n_m, ordnung)


def abklingend(mod, pot, qidx, E, n_m, kanaele):
    P = E[0].shape[0]
    Z = np.zeros((P, 6, len(kanaele)))
    mm = (mod.m2, mod.m2, mod.mc2)
    for j, ch in enumerate(kanaele):
        kap = np.sqrt(np.maximum(mm[ch] - E[ch][:, 0], 0.0))
        Z[:, ch, j] = 1.0
        Z[:, 3 + ch, j] = -kap
    return integriere(pot, qidx, E[0], E[1], E[2], Z, pot.N, n_m, list(range(len(kanaele))))


def werte_E1(mod, pot, qidx, w2, rho, n_m):
    w2 = np.atleast_1d(np.asarray(w2, float))
    rho = np.atleast_1d(np.asarray(rho, float))
    E = energien(w2, rho)
    Y = regulaer(pot, qidx, E, n_m, [2, 1, 0])
    Z = abklingend(mod, pot, qidx, E, n_m, [1, 2])
    G = paar(Y, Z)
    m_ac = G[:, 0, 0] * G[:, 2, 1] - G[:, 0, 1] * G[:, 2, 0]
    m_bc = G[:, 1, 0] * G[:, 2, 1] - G[:, 1, 1] * G[:, 2, 0]
    m_ab = G[:, 0, 0] * G[:, 1, 1] - G[:, 0, 1] * G[:, 1, 0]
    sv = np.linalg.svd(G, compute_uv=False)
    iso, iso4 = isotropie(Y)
    return dict(W=m_ac + 1j * m_bc, m_ab=m_ab, svr=sv[:, 1] / sv[:, 0], iso=iso, iso4=iso4)


def werte_E2(mod, pot, qidx, w2, rho, n_m):
    w2 = np.atleast_1d(np.asarray(w2, float))
    rho = np.atleast_1d(np.asarray(rho, float))
    E = energien(w2, rho)
    Y = regulaer(pot, qidx, E, n_m, [1, 2, 0])
    Z = abklingend(mod, pot, qidx, E, n_m, [1])
    G = paar(Y, Z)[:, :, 0]
    iso, iso4 = isotropie(Y)
    return dict(G=G, T=np.sqrt(np.sum(G * G, axis=1)), Wab=G[:, 0] + 1j * G[:, 1], iso=iso, iso4=iso4)


def werte_E3(mod, pot, qidx, w2, rho, n_m=None):
    w2 = np.atleast_1d(np.asarray(w2, float))
    rho = np.atleast_1d(np.asarray(rho, float))
    E = energien(w2, rho)
    Y = regulaer(pot, qidx, E, pot.N, [0, 1, 2])
    R = pot.N * pot.hp
    mm = (mod.m2, mod.m2, mod.mc2)
    A = np.empty((len(rho), 6, 3))
    for ch in range(3):
        k = np.sqrt(E[ch][:, 0] - mm[ch])[:, None]
        u, p = Y[:, ch], Y[:, 3 + ch]
        al = u * np.sin(k * R) + p / k * np.cos(k * R)
        be = u * np.cos(k * R) - p / k * np.sin(k * R)
        A[:, 2 * ch] = np.sqrt(k) * al
        A[:, 2 * ch + 1] = np.sqrt(k) * be
    sv = np.linalg.svd(A, compute_uv=False)
    iso, iso4 = isotropie(Y)
    return dict(T3=sv[:, -1] / sv[:, 0], iso=iso, iso4=iso4)


def bereich(mod, w2, rho):
    w = math.sqrt(w2)
    a = (w + rho) ** 2 > mod.m2
    b = (w - rho) ** 2 > mod.m2
    c = rho ** 2 > mod.mc2
    if a and not b and not c:
        return 'E1'
    if a and c and not b:
        return 'E2'
    if a and b and c:
        return 'E3'
    if not a and not b and not c:
        return 'E0'
    return 'sonst'


# ------------------------------------------------------------------ Hilfen: Nullstellen, Umgebung
def nullstellen(x, y, zs):
    out = []
    idx = np.nonzero(np.sign(y[:-1]) * np.sign(y[1:]) < 0)[0]
    for i in idx:
        lo = max(0, i - 1)
        hi = min(len(x), lo + 4)
        lo = max(0, hi - 4)
        t = (x[lo:hi] - x[i]) / (x[i + 1] - x[i])
        deg = min(3, len(t) - 1)
        cy = np.polyfit(t, y[lo:hi], deg)
        a, b = 0.0, 1.0
        fa = np.polyval(cy, a)
        for _ in range(60):
            m = 0.5 * (a + b)
            fm = np.polyval(cy, m)
            if np.sign(fm) == np.sign(fa):
                a, fa = m, fm
            else:
                b = m
        tr = 0.5 * (a + b)
        vals = [float(np.polyval(np.polyfit(t, z[lo:hi], deg), tr)) for z in zs]
        out.append(dict(rho=float(x[i] + tr * (x[i + 1] - x[i])), i=int(i), werte=vals))
    return out


class Umgebung:
    """Profile auf dem festen Gitter eines Ankerprofils; Cache je omega^2."""

    def __init__(self, mod, anker, n_m=None):
        self.mod = mod
        self.anker = anker
        self.cache = {round(anker['w2'], 13): anker}
        self.n_m = n_mitte(anker) if n_m is None else n_m

    def profil(self, w2):
        key = round(float(w2), 13)
        if key not in self.cache:
            best = min(self.cache.values(), key=lambda p: abs(p['w2'] - w2))
            p = fortsetzung(self.mod, best, float(w2), best['hp'], N=self.anker['N'])
            if p is None:
                raise RuntimeError('Profil bei w2=%.10f gescheitert' % w2)
            self.cache[key] = p
        return self.cache[key]

    def werte(self, fn, w2s, rhos):
        w2s = np.atleast_1d(np.asarray(w2s, float))
        keys = [round(float(x), 13) for x in w2s]
        uniq = sorted(set(keys))
        profs = [self.profil(k) for k in uniq]
        pos = {k: i for i, k in enumerate(uniq)}
        qidx = np.array([pos[k] for k in keys])
        return fn(self.mod, Pot(self.mod, profs), qidx, w2s, np.atleast_1d(np.asarray(rhos, float)), self.n_m)


def rechteck(t, w2c, rhoc, hw, hr):
    t = np.asarray(t, float)
    k = np.floor(t).astype(int) % 4
    x = t - np.floor(t)
    s = -1 + 2 * x
    w = np.select([k == 0, k == 1, k == 2, k == 3], [s, 1 + 0 * s, -s, -1 + 0 * s])
    r = np.select([k == 0, k == 1, k == 2, k == 3], [-1 + 0 * s, s, 1 + 0 * s, -s])
    return w2c + hw * w, rhoc + hr * r


def umlauf(U, fn, schluessel, w2c, rhoc, hw, hr):
    """Phasenumlauf von fn[schluessel] um das Rechteck, gegen den Uhrzeigersinn in (w2, rho)."""
    werte = {}
    neu = np.arange(4 * NKANTE) / NKANTE
    erg = None
    for rnd in range(RUNDEN + 1):
        if len(neu):
            w, r = rechteck(neu, w2c, rhoc, hw, hr)
            z = U.werte(fn, w, r)[schluessel]
            for t, zz in zip(neu.tolist(), np.asarray(z).tolist()):
                werte[t] = zz
        tt = np.array(sorted(werte))
        z = np.array([werte[t] for t in tt])
        ph = np.angle(z)
        d = (np.roll(ph, -1) - ph + np.pi) % (2 * np.pi) - np.pi
        groesst = float(np.max(np.abs(d)))
        n = float(np.sum(d) / (2 * np.pi))
        erg = dict(umlauf=int(round(n)), umlauf_roh=n, groesster_sprung=groesst, punkte=int(len(tt)),
                   aufgeloest=bool(groesst < SPRUNG), runden=rnd, halb_w=hw, halb_r=hr,
                   min_abs=float(np.min(np.abs(z))), max_abs=float(np.max(np.abs(z))))
        if groesst < SPRUNG or rnd == RUNDEN or len(tt) >= MAXPKT:
            break
        tneu = []
        for i in np.nonzero(np.abs(d) >= SPRUNG)[0]:
            t1 = tt[i]
            t2 = tt[(i + 1) % len(tt)]
            if t2 <= t1:
                t2 += 4.0
            tneu.append((0.5 * (t1 + t2)) % 4.0)
        neu = np.array(tneu)
    return erg


def umlauf_mit_rueckfall(U, fn, schl, w2c, rhoc, hmax):
    e = umlauf(U, fn, schl, w2c, rhoc, hmax, hmax)
    e['versuch'] = 1
    if not e['aufgeloest']:
        e2 = umlauf(U, fn, schl, w2c, rhoc, min(hmax, 1e-4), min(hmax, 1e-4))
        e2['versuch'] = 2
        e2['versuch1'] = e
        return e2
    return e


def newton_E1(U, w2, rho, iters=12, dw=1e-6, dr=1e-6):
    verl = []
    ok = False
    for it in range(iters):
        W = U.werte(werte_E1, [w2, w2 + dw, w2], [rho, rho, rho + dr])['W']
        J11 = (W[1].real - W[0].real) / dw
        J21 = (W[1].imag - W[0].imag) / dw
        J12 = (W[2].real - W[0].real) / dr
        J22 = (W[2].imag - W[0].imag) / dr
        det = J11 * J22 - J12 * J21
        dx = -(J22 * W[0].real - J12 * W[0].imag) / det
        dy = -(-J21 * W[0].real + J11 * W[0].imag) / det
        if not (np.isfinite(dx) and np.isfinite(dy)):
            break
        s = max(abs(dx), abs(dy))
        fak = min(1.0, 0.01 / s) if s > 0 else 1.0
        w2 += fak * dx
        rho += fak * dy
        verl.append(float(s))
        if s < 1e-10:
            ok = True
            break
    return float(w2), float(rho), ok, verl


def gn_E2(U, w2, rho, grenze, iters=25, dw=1e-6, dr=1e-6):
    """Gauss-Newton mit Daempfung (Levenberg-Marquardt) auf G (3 Komponenten); nur Schritte, die |G| senken.
    grenze(w2, rho) -> (w2, rho) geklemmt."""
    verl = []
    G0 = U.werte(werte_E2, [w2], [rho])['G'][0]
    T0 = float(np.sqrt(np.sum(G0 * G0)))
    lam = 1e-3
    for it in range(iters):
        G = U.werte(werte_E2, [w2 + dw, w2], [rho, rho + dr])['G']
        J = np.stack([(G[0] - G0) / dw, (G[1] - G0) / dr], axis=1)
        A = J.T @ J
        g = J.T @ G0
        ok = False
        for _ in range(12):
            st = -np.linalg.solve(A + lam * np.diag(np.diag(A) + 1e-30), g)
            s = float(np.max(np.abs(st)))
            fak = min(1.0, 0.01 / s) if s > 0 else 1.0
            w2n, rhon = grenze(w2 + fak * st[0], rho + fak * st[1])
            Gn = U.werte(werte_E2, [w2n], [rhon])['G'][0]
            Tn = float(np.sqrt(np.sum(Gn * Gn)))
            if np.isfinite(Tn) and Tn < T0:
                ok = True
                break
            lam *= 10.0
        if not ok:
            verl.append(0.0)
            break
        sch = max(abs(w2n - w2), abs(rhon - rho))
        verl.append(float(sch))
        w2, rho, G0, rel = w2n, rhon, Gn, (T0 - Tn) / max(T0, 1e-300)
        T0 = Tn
        lam = max(lam / 10.0, 1e-9)
        if sch < 1e-10 or rel < 1e-12:
            break
    v = U.werte(werte_E2, [w2], [rho])
    return float(w2), float(rho), v, verl


# ------------------------------------------------------------------ Befehle
def cmd_profile(tag, stufe, pdir, w2liste):
    mod = modell_von(tag)
    hp = STUFEN[stufe]
    if tag == 'M2':
        p0 = saat(mod, 'M2', 200.0, hp)
    else:
        p0 = saat(mod, 'M1', 200.0, hp)
    log('Saat: w2=%.8f Q=%.6f N=%d rhalf=%.3f chi0=%.4f' % (p0['w2'], p0['Q'], p0['N'], p0['rhalf'], p0['chi0']))
    ziele = sorted(set(float(x) for x in w2liste))
    oben = [x for x in ziele if x >= p0['w2']]
    unten = [x for x in ziele if x < p0['w2']][::-1]
    info = []
    for folge in (oben, unten):
        p = p0
        for x in folge:
            t1 = time.time()
            q = fortsetzung(mod, p, x, hp)
            if q is None:
                log('FEHLER Profil w2=%.4f' % x)
                break
            speichere_profil(profil_pfad(pdir, x), q)
            d = {k: v for k, v in q.items() if k not in ('F', 'H')}
            d['sekunden'] = time.time() - t1
            info.append(d)
            log('w2=%.4f Q=%.6f E/Q=%.8f chi0=%.6f f0=%.6f rhalf=%.3f N=%d Rbg=%.2f f_rand=%.1e it=%d' % (
                x, q['Q'], q['EQ'], q['chi0'], q['f0'], q['rhalf'], q['N'], q['Rbg'], q['f_rand'], len(q['newton'])))
            p = q
    schreibe(os.path.join(pdir, 'profile-info.json'), sorted(info, key=lambda d: d['w2']))


def zeile_rechnen(mod, p, mit=('E1', 'E2', 'E3')):
    pot = Pot(mod, [p])
    n_m = n_mitte(p)
    w2 = p['w2']
    w = math.sqrt(w2)
    m, mc = math.sqrt(mod.m2), math.sqrt(mod.mc2)
    d = {k: v for k, v in p.items() if k not in ('F', 'H')}
    d['n_m'] = n_m
    d['r_m'] = n_m * p['hp']
    if 'E1' in mit:
        rho = np.linspace(m - w + RAND, min(mc, w + m) - RAND, N_E1)
        v = werte_E1(mod, pot, np.zeros(len(rho), int), np.full(len(rho), w2), rho, n_m)
        nz = nullstellen(rho, v['W'].imag, [v['W'].real, v['svr']])
        d['e1'] = dict(rho=rho.tolist(), reW=v['W'].real.tolist(), imW=v['W'].imag.tolist(), m_ab=v['m_ab'].tolist(),
                       svr=v['svr'].tolist(), iso=float(v['iso'].max()), iso4=float(v['iso4'].max()),
                       null=[dict(rho=z['rho'], s=z['werte'][0], svr=z['werte'][1]) for z in nz])
    if 'E2' in mit:
        rho = np.linspace(mc + RAND, w + m - RAND, N_E2)
        v = werte_E2(mod, pot, np.zeros(len(rho), int), np.full(len(rho), w2), rho, n_m)
        G = v['G']
        nz = nullstellen(rho, G[:, 1], [G[:, 0], G[:, 2], v['T']])
        d['e2'] = dict(rho=rho.tolist(), Ga=G[:, 0].tolist(), Gb=G[:, 1].tolist(), Gc=G[:, 2].tolist(),
                       T=v['T'].tolist(), iso=float(v['iso'].max()), iso4=float(v['iso4'].max()),
                       null=[dict(rho=z['rho'], s_a=z['werte'][0], s_c=z['werte'][1], T=z['werte'][2]) for z in nz])
    if 'E3' in mit:
        lo = w + m + RAND
        if lo < RHO_MAX:
            rho = np.linspace(lo, RHO_MAX, N_E3)
            v = werte_E3(mod, pot, np.zeros(len(rho), int), np.full(len(rho), w2), rho)
            d['e3'] = dict(rho=rho.tolist(), T3=v['T3'].tolist(), iso=float(v['iso'].max()), iso4=float(v['iso4'].max()))
    return d


def cmd_zeilen(stufe, pdir, adir, w2liste):
    mod = modell_von('M2')
    for x in w2liste:
        t1 = time.time()
        p = lade_profil(profil_pfad(pdir, x))
        assert abs(p['hp'] - STUFEN[stufe]) < 1e-15
        d = zeile_rechnen(mod, p)
        d['sekunden'] = time.time() - t1
        schreibe(os.path.join(adir, 'zeile-st%d-w2_%.4f.json' % (stufe, x)), d)
        log('zeile w2=%.4f: E1 null=%d s=%s | E2 null=%d Tmin_null=%s | E3 T3min=%s | iso=%.1e iso4=%.1e | %.1fs' % (
            x, len(d['e1']['null']), ''.join('+' if z['s'] > 0 else '-' for z in d['e1']['null']),
            len(d['e2']['null']), ('%.2e' % min(z['T'] for z in d['e2']['null'])) if d['e2']['null'] else '-',
            ('%.2e' % min(d['e3']['T3'])) if 'e3' in d else '-', max(d['e1']['iso'], d['e2']['iso']),
            max(d['e1']['iso4'], d['e2']['iso4']), d['sekunden']))


def cmd_eichung(d1, d2, aus):
    nu2, nu3, n2, n3 = [], [], 0, 0
    for x in EICH_W2:
        a = json.load(open(os.path.join(d1, 'zeile-st1-w2_%.4f.json' % x)))
        b = json.load(open(os.path.join(d2, 'zeile-st2-w2_%.4f.json' % x)))
        nu2 += list(np.abs(np.array(a['e2']['T']) - np.array(b['e2']['T'])))
        if 'e3' in a and 'e3' in b:
            nu3 += list(np.abs(np.array(a['e3']['T3']) - np.array(b['e3']['T3'])))
    nu2 = np.array(nu2)
    nu3 = np.array(nu3)
    erg = dict(zeilen=EICH_W2, nu_E2=float(nu2.max()), nu_E2_median=float(np.median(nu2)), n_E2=int(nu2.size),
               nu_E3=float(nu3.max()), nu_E3_median=float(np.median(nu3)), n_E3=int(nu3.size),
               tau_E2=float(max(10 * nu2.max(), 1e-10)), tau_E3=float(max(10 * nu3.max(), 1e-10)),
               regel='tau = max(10 nu, 1e-10), nu = max |T_St1 - T_St2| ueber Eichzeilen (PLAN 5)')
    schreibe(aus, erg)
    log(json.dumps(erg))


def cmd_k2(pdir, aus):
    sys.path.insert(0, HIER)
    import beutel as b
    mod = modell_von('M2')
    M = b.Model('M2')
    zeilen = []
    for x in K2_W2:
        p = lade_profil(profil_pfad(pdir, x))
        r, f, g = fg_aus(p['F'], p['H'], p['hp'], p['N'])
        z = dict(w2=x, Q=p['Q'], EQ=p['EQ'], chi0=p['chi0'], Rbg=p['Rbg'])
        for dr in (0.02, 0.01):
            G = b.Grid(dr, p['Rbg'])
            fi = np.interp(G.r, r, f, right=0.0)
            gi = np.interp(G.r, r, g, right=1.0)
            fn, gn, it, err, ok = b.newton_w(M, G, fi, gi, x)
            o = b.observables(M, G, fn, gn, x)
            z['beutel_dr%.2f' % dr] = dict(ok=bool(ok), it=it, err=err, Q=o['Q'], EQ=o['EQ'], chi0=o['chi0'],
                                           dQ_rel=abs(p['Q'] / o['Q'] - 1), dEQ_rel=abs(p['EQ'] / o['EQ'] - 1))
        zeilen.append(z)
        log('K2 w2=%.2f Q=%.6f EQ=%.8f | B0.01 Q=%.6f EQ=%.8f dQ=%.1e dEQ=%.1e | B0.02 dQ=%.1e dEQ=%.1e' % (
            x, p['Q'], p['EQ'], z['beutel_dr0.01']['Q'], z['beutel_dr0.01']['EQ'], z['beutel_dr0.01']['dQ_rel'],
            z['beutel_dr0.01']['dEQ_rel'], z['beutel_dr0.02']['dQ_rel'], z['beutel_dr0.02']['dEQ_rel']))
    mx = max(max(z['beutel_dr0.01']['dQ_rel'], z['beutel_dr0.01']['dEQ_rel']) for z in zeilen)
    schreibe(aus, dict(zeilen=zeilen, max_rel_dr001=mx, bestanden=bool(mx <= 1e-4)))
    log('K2 max rel (dr 0,01) = %.2e, bestanden=%s' % (mx, mx <= 1e-4))


def lade_zeilen(adir, stufe):
    out = []
    for fn in sorted(os.listdir(adir)):
        if fn.startswith('zeile-st%d-' % stufe) and fn.endswith('.json'):
            out.append(json.load(open(os.path.join(adir, fn))))
    return sorted(out, key=lambda d: d['w2'])


def detektoren_E1(zeilen, schl='e1'):
    kand, paare = [], []
    for A, B in zip(zeilen[:-1], zeilen[1:]):
        ra = np.array([z['rho'] for z in A[schl]['null']])
        sa = np.array([z['s'] for z in A[schl]['null']])
        rb = np.array([z['rho'] for z in B[schl]['null']])
        sb = np.array([z['s'] for z in B[schl]['null']])
        if len(ra) and len(rb):
            for i in range(len(ra)):
                k = int(np.argmin(np.abs(rb - ra[i])))
                i2 = int(np.argmin(np.abs(ra - rb[k])))
                if i2 == i and abs(rb[k] - ra[i]) <= 0.1:
                    wech = bool(np.sign(sa[i]) != np.sign(sb[k]))
                    paare.append(dict(w2a=A['w2'], w2b=B['w2'], ra=float(ra[i]), rb=float(rb[k]), sa=float(sa[i]),
                                      sb=float(sb[k]), wechsel=wech))
                    if wech:
                        t = abs(sa[i]) / (abs(sa[i]) + abs(sb[k]))
                        kand.append(dict(w2=A['w2'] + t * (B['w2'] - A['w2']), rho=float(ra[i] + t * (rb[k] - ra[i])),
                                         quelle='s-wechsel'))
        WA = np.array(A[schl]['reW']) + 1j * np.array(A[schl]['imW'])
        WB = np.array(B[schl]['reW']) + 1j * np.array(B[schl]['imW'])
        wrap = lambda x: (x + np.pi) % (2 * np.pi) - np.pi
        d1 = wrap(np.angle(WA[1:]) - np.angle(WA[:-1]))
        d2 = wrap(np.angle(WB[1:]) - np.angle(WA[1:]))
        d3 = wrap(np.angle(WB[:-1]) - np.angle(WB[1:]))
        d4 = wrap(np.angle(WA[:-1]) - np.angle(WB[:-1]))
        n = np.rint((d1 + d2 + d3 + d4) / (2 * np.pi)).astype(int)
        for i in np.nonzero(n != 0)[0]:
            rA = 0.5 * (A[schl]['rho'][i] + A[schl]['rho'][i + 1])
            rB = 0.5 * (B[schl]['rho'][i] + B[schl]['rho'][i + 1])
            kand.append(dict(w2=0.5 * (A['w2'] + B['w2']), rho=0.5 * (rA + rB), quelle='zelle', n_zelle=int(n[i])))
    uniq = []
    for k in kand:
        tr = [u for u in uniq if abs(k['w2'] - u['w2']) < 5e-3 and abs(k['rho'] - u['rho']) < 5e-3]
        if tr:
            if k['quelle'] not in tr[0]['quelle']:
                tr[0]['quelle'] += '+' + k['quelle']
        else:
            uniq.append(dict(k))
    return uniq, paare


def e1_kandidat(mod, anker, k, m_lo, m_hi):
    """Newton + Umlauf fuer einen E1-Kandidaten auf dem Gitter des Ankerprofils."""
    U = Umgebung(mod, anker)
    w2, rho, ok, verl = newton_E1(U, k['w2'], k['rho'])
    e = dict(start=k, w2=w2, rho=rho, konvergiert=ok, newton=verl, anker_w2=anker['w2'], r_m=U.n_m * anker['hp'])
    w = math.sqrt(w2) if w2 > 0 else 0.0
    e['bereich'] = bereich(mod, w2, rho) if w2 > 0 else 'aus'
    e['im_fenster'] = bool(m_lo - 0.01 <= w2 <= m_hi + 0.01 and e['bereich'] == 'E1')
    if ok and e['bereich'] == 'E1':
        v = U.werte(werte_E1, [w2], [rho])
        e['W_am_punkt'] = [float(v['W'][0].real), float(v['W'][0].imag)]
        e['svr'] = float(v['svr'][0])
        e['m_ab'] = float(v['m_ab'][0])
        p = U.profil(w2)
        e['chi0'] = p['chi0']
        e['Q'] = p['Q']
        abst = min(rho - (math.sqrt(mod.m2) - w), math.sqrt(mod.mc2) - rho, w + math.sqrt(mod.m2) - rho)
        hmax = min(HALB, 0.4 * abst)
        e['umlauf'] = umlauf_mit_rueckfall(U, werte_E1, 'W', w2, rho, hmax)
    return e


def cmd_kand(stufe, pdir, adir, schwelle, aus, teil):
    mod = modell_von('M2')
    zeilen = lade_zeilen(adir, stufe)
    tau = json.load(open(schwelle))
    log("zeilen", len(zeilen), "teil", teil)
    ab, bis = 0, 10**9
    if ":" in teil:
        teil, ab, bis = teil.split(":")[0], int(teil.split(":")[1]), int(teil.split(":")[2])
    erg_ab_bis = (ab, bis)
    erg = dict(stufe=stufe, teil=teil, tau=tau)
    if teil == 'E1':
        uniq, paare = detektoren_E1(zeilen)
        erg['paare'] = paare
        erg['kandidaten_roh'] = uniq
        log('E1-Kandidaten:', json.dumps(uniq))
        res = []
        for k in uniq[ab:bis]:
            j = int(np.argmin([abs(z['w2'] - k['w2']) for z in zeilen]))
            anker = lade_profil(profil_pfad(pdir, zeilen[j]['w2']))
            try:
                e = e1_kandidat(mod, anker, k, ZEILEN[0], ZEILEN[-1])
            except Exception as ex:
                e = dict(start=k, fehler=repr(ex))
            res.append(e)
            log('E1 kand', json.dumps(e))
            erg['kandidaten'] = res
            schreibe(aus, erg)
        erg['kandidaten'] = res
    elif teil == 'E2':
        T = np.array([z['e2']['T'] for z in zeilen])
        mins = sorted(gitter_minima(T), key=lambda ji: T[ji[0], ji[1]])   # aufsteigend nach T
        erg['gitter_minima'] = [dict(w2=zeilen[j]['w2'], rho=zeilen[j]['e2']['rho'][i], T=float(T[j, i]), j=j, i=i)
                                for j, i in mins]
        log('E2-Gitterminima:', len(mins))
        res = []
        for j, i in mins[ab:bis]:
            anker = lade_profil(profil_pfad(pdir, zeilen[j]['w2']))
            U = Umgebung(mod, anker)
            w2c = zeilen[j]['w2']

            def grenze(w2, rho, w2c=w2c):
                w2 = min(max(w2, w2c - 0.03, ZEILEN[0] - 0.005), w2c + 0.03, ZEILEN[-1] + 0.005)
                w = math.sqrt(w2)
                rho = min(max(rho, SQ2 + RAND), w + SQ2 - RAND)
                return w2, rho
            try:
                w2, rho, v, verl = gn_E2(U, w2c, zeilen[j]['e2']['rho'][i], grenze)
                p = U.profil(w2)
                e = dict(start=dict(w2=w2c, rho=zeilen[j]['e2']['rho'][i], T=float(T[j, i])), w2=w2, rho=rho,
                         T=float(v['T'][0]), G=v['G'][0].tolist(), gn=verl, chi0=p['chi0'],
                         bereich=bereich(mod, w2, rho), r_m=U.n_m * anker['hp'],
                         beide_null=bool(v['T'][0] < tau['tau_E2']))
            except Exception as ex:
                e = dict(start=dict(w2=w2c, rho=zeilen[j]['e2']['rho'][i]), fehler=repr(ex))
            res.append(e)
            log('E2 min', json.dumps(e))
            erg['minima'] = res
            schreibe(aus, erg)
        erg['minima'] = res
    elif teil == 'E3':
        T = np.array([z['e3']['T3'] for z in zeilen if 'e3' in z])
        zz = [z for z in zeilen if 'e3' in z]
        mins = gitter_minima(T)
        erg['gitter_minima'] = [dict(w2=zz[j]['w2'], rho=zz[j]['e3']['rho'][i], T3=float(T[j, i]), j=j, i=i)
                                for j, i in mins]
        res = []
        qual = [m for m in erg['gitter_minima'] if m['T3'] < 100 * tau['tau_E3']]
        erg['n_qualifiziert'] = len(qual)
        log('E3: %d Gitterminima, %d unter 100 tau' % (len(mins), len(qual)))
        for m in qual[ab:bis]:
            if True:
                from scipy.optimize import minimize
                anker = lade_profil(profil_pfad(pdir, m['w2']))
                U = Umgebung(mod, anker)
                def f(x, U=U, w2a=m['w2']):
                    if abs(x[0] - w2a) > 0.03 or bereich(mod, x[0], x[1]) != 'E3' or x[1] > RHO_MAX:
                        return 1.0
                    return float(U.werte(werte_E3, [x[0]], [x[1]])['T3'][0])
                o = minimize(f, [m['w2'], m['rho']], method='Nelder-Mead',
                             options=dict(xatol=1e-9, fatol=1e-15, maxiter=150))
                res.append(dict(start=m, w2=float(o.x[0]), rho=float(o.x[1]), T3=float(o.fun),
                                beide_null=bool(o.fun < tau['tau_E3'])))
                erg['verfeinert'] = res
                schreibe(aus, erg)
                log('E3 verfeinert', json.dumps(res[-1]))
        erg['verfeinert'] = res
        log('E3: %d Gitterminima, kleinstes T3=%.3e, verfeinert %d' % (
            len(mins), min(m['T3'] for m in erg['gitter_minima']) if mins else float('nan'), len(res)))
    erg['sekunden'] = time.time() - T0
    schreibe(aus, erg)


def gitter_minima(T):
    J, I = T.shape
    out = []
    for j in range(J):
        for i in range(I):
            nb = T[max(0, j - 1):j + 2, max(0, i - 1):i + 2]
            if T[j, i] <= nb.min():
                out.append((j, i))
    return out


def cmd_k1(var, stufe, pdir, aus):
    mod = modell_von(var)
    rho = np.linspace(1.70, 1.79, 91)
    zeilen = []
    for x in K1_W2:
        p = lade_profil(profil_pfad(pdir, x))
        pot = Pot(mod, [p])
        n_m = n_mitte(p)
        z = dict(w2=x, Q=p['Q'], f0=p['f0'], rhalf=p['rhalf'], n_m=n_m, rho=rho.tolist())
        if var == 'K1E1':
            v = werte_E1(mod, pot, np.zeros(91, int), np.full(91, x), rho, n_m)
            nz = nullstellen(rho, v['W'].imag, [v['W'].real])
            z['k1'] = dict(rho=rho.tolist(), reW=v['W'].real.tolist(), imW=v['W'].imag.tolist(),
                           null=[dict(rho=q['rho'], s=q['werte'][0]) for q in nz])
            z['iso'] = float(v['iso'].max())
            z['iso4'] = float(v['iso4'].max())
        else:
            v = werte_E2(mod, pot, np.zeros(91, int), np.full(91, x), rho, n_m)
            z['T'] = v['T'].tolist()
            z['Gc_max'] = float(np.abs(v['G'][:, 2]).max())
            z['iso'] = float(v['iso'].max())
            z['iso4'] = float(v['iso4'].max())
        zeilen.append(z)
        log('K1 %s w2=%.2f iso=%.1e iso4=%.1e' % (var, x, z['iso'], z['iso4']))
    erg = dict(variante=var, stufe=stufe, zeilen=zeilen)
    if var == 'K1E1':
        uniq, paare = detektoren_E1(zeilen, 'k1')
        erg['kandidaten_roh'] = uniq
        res = []
        for k in uniq:
            j = int(np.argmin([abs(z['w2'] - k['w2']) for z in zeilen]))
            anker = lade_profil(profil_pfad(pdir, zeilen[j]['w2']))
            res.append(e1_kandidat(mod, anker, k, 0.75, 0.85))
            log('K1E1 kand', json.dumps(res[-1]))
        erg['kandidaten'] = res
    else:
        T = np.array([z['T'] for z in zeilen])
        mins = gitter_minima(T)
        res = []
        for j, i in mins:
            anker = lade_profil(profil_pfad(pdir, zeilen[j]['w2']))
            U = Umgebung(mod, anker)
            grenze = lambda w2, rho: (min(max(w2, 0.76), 0.84), min(max(rho, 1.66), 1.83))
            w2, rho, v, verl = gn_E2(U, zeilen[j]['w2'], float(rho_i(zeilen[j], i)), grenze)
            e = dict(start=dict(w2=zeilen[j]['w2'], rho=float(rho_i(zeilen[j], i)), T=float(T[j, i])), w2=w2, rho=rho,
                     T=float(v['T'][0]), G=v['G'][0].tolist(), gn=verl, r_m=U.n_m * anker['hp'])
            e['umlauf_Gab'] = umlauf_mit_rueckfall(U, werte_E2, 'Wab', w2, rho, HALB)
            res.append(e)
            log('K1E2 min', json.dumps(e))
        erg['minima'] = res
    erg['sekunden'] = time.time() - T0
    schreibe(aus, erg)


def rho_i(z, i):
    return z['rho'][i]


def cmd_e2ziel(stufe, pdir, aus, punkte):
    """PLAN-NACHTRAG-1: gedaempfte Minimierung von T ab vorgegebenen Startpunkten (w2:rho)."""
    mod = modell_von('M2')
    erg = dict(stufe=stufe, nachtrag=1, punkte=[])
    for pk in punkte:
        w2s, rhos = (float(x) for x in pk.split(':'))
        za = min(ZEILEN, key=lambda z: abs(z - w2s))
        anker = lade_profil(profil_pfad(pdir, za))
        U = Umgebung(mod, anker)

        def grenze(w2, rho, w2c=za):
            w2 = min(max(w2, w2c - 0.03, ZEILEN[0] - 0.005), w2c + 0.03, ZEILEN[-1] + 0.005)
            w = math.sqrt(w2)
            rho = min(max(rho, SQ2 + RAND), w + SQ2 - RAND)
            return w2, rho
        w2, rho, v, verl = gn_E2(U, w2s, rhos, grenze)
        p = U.profil(w2)
        e = dict(start=dict(w2=w2s, rho=rhos), anker=za, w2=w2, rho=rho, T=float(v['T'][0]), G=v['G'][0].tolist(),
                 gn=verl, chi0=p['chi0'], bereich=bereich(mod, w2, rho), r_m=U.n_m * anker['hp'])
        erg['punkte'].append(e)
        log('E2ziel', json.dumps(e))
        schreibe(aus, erg)


def cmd_homotopie(stufe, k1json, aus):
    hp = STUFEN[stufe]
    k1 = json.load(open(k1json))
    best = min(k1['minima'], key=lambda e: e['T'])
    w2, rho = best['w2'], best['rho']
    mod0 = Modell(0.0, 0.25)
    p = saat(mod0, 'M1', 200.0, hp)
    p = fortsetzung(mod0, p, w2, hp)
    N = p['N']
    n_m = n_mitte(p)
    tau = None
    if len(sys.argv) > 5:
        tau = json.load(open(sys.argv[5]))
    lams = [round(0.05 * k, 10) for k in range(21)]
    erg = dict(stufe=stufe, start=dict(w2=w2, rho=rho), N=N, r_m=n_m * hp, schritte=[])
    for lam in lams:
        mod = Modell(lam, 0.25)
        q = loese(mod, w2, hp, N, p['F'], p['H'])
        if q is None:
            # Teilschritte in lam
            lam0 = mod_lam_vorher = erg['schritte'][-1]['lam'] if erg['schritte'] else 0.0
            q = p
            for t in np.linspace(lam0, lam, 9)[1:]:
                q2 = loese(Modell(t, 0.25), w2, hp, N, q['F'], q['H'])
                if q2 is None:
                    q = None
                    break
                q = q2
        if q is None:
            erg['abbruch'] = 'Profil bei lam=%.2f gescheitert' % lam
            break
        U = Umgebung(mod, q, n_m=n_m)
        ber = bereich(mod, w2, rho)
        s = dict(lam=lam, bereich_start=ber)
        if ber == 'E1':
            w2n, rhon, ok, verl = newton_E1(U, w2, rho)
            v = U.werte(werte_E1, [w2n], [rhon])
            s.update(art='E1', w2=w2n, rho=rhon, ok=ok, svr=float(v['svr'][0]),
                     lebt=bool(ok and v['svr'][0] < 1e-6))
        else:
            def grenze(a, b, mod=mod):
                a = min(max(a, 0.70), mod.m2 - 0.02)
                w = math.sqrt(a)
                b = min(max(b, math.sqrt(mod.mc2) + RAND), w + math.sqrt(mod.m2) - RAND)
                return a, b
            w2n, rhon, v, verl = gn_E2(U, w2, rho, grenze)
            s.update(art='E2', w2=w2n, rho=rhon, T=float(v['T'][0]), G=v['G'][0].tolist(), gn=verl)
            if tau is not None:
                s['lebt'] = bool(v['T'][0] < tau['tau_E2'])
        pq = U.profil(w2n)
        s['chi0'] = pq['chi0']
        s['bereich_ende'] = bereich(mod, w2n, rhon)
        erg['schritte'].append(s)
        log('Homotopie', json.dumps(s))
        schreibe(aus, erg)
        w2, rho, p = w2n, rhon, pq
    erg['sekunden'] = time.time() - T0
    schreibe(aus, erg)


def cmd_rauch():
    hp = STUFEN[0]
    mod = modell_von('M2')
    p = saat(mod, 'M2', 200.0, hp)
    log('M2 Saat w2=%.6f Q=%.4f EQ=%.6f chi0=%.4f rhalf=%.3f N=%d' % (p['w2'], p['Q'], p['EQ'], p['chi0'], p['rhalf'], p['N']))
    q = fortsetzung(mod, p, 1.2, hp)
    log('w2=1.2 Q=%.4f chi0=%.4f rhalf=%.3f N=%d' % (q['Q'], q['chi0'], q['rhalf'], q['N']))
    t = time.time()
    d = zeile_rechnen(mod, q)
    log('zeile 1.2: %.1fs; E1 null %s; E2 null %d; iso %.1e iso4 %.1e; T3min %.2e' % (
        time.time() - t, [(round(z['rho'], 4), '%.2e' % z['s']) for z in d['e1']['null']], len(d['e2']['null']),
        d['e1']['iso'], d['e1']['iso4'], min(d['e3']['T3'])))
    mk = modell_von('K1E1')
    p1 = saat(mk, 'M1', 200.0, hp)
    p1 = fortsetzung(mk, p1, K1_STELLE[0], hp)
    v = werte_E1(mk, Pot(mk, [p1]), np.zeros(3, int), np.full(3, K1_STELLE[0]),
                 np.array([1.70, K1_STELLE[1], 1.78]), n_mitte(p1))
    log('K1E1 grob: W=%s svr=%s iso=%s' % (v['W'], v['svr'], v['iso']))
    mk2 = modell_von('K1E2')
    v2 = werte_E2(mk2, Pot(mk2, [p1]), np.zeros(3, int), np.full(3, K1_STELLE[0]),
                  np.array([1.70, K1_STELLE[1], 1.78]), n_mitte(p1))
    log('K1E2 grob: T=%s G=%s' % (v2['T'], v2['G'].tolist()))


def cmd_bild(adir2, kdir, aus):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    zeilen = lade_zeilen(adir2, 2)
    fig, ax = plt.subplots(1, 2, figsize=(15, 7))
    w2 = np.linspace(0.728, 2.0, 400)
    w = np.sqrt(w2)
    a = ax[0]
    a.fill_between(w2, 0, SQ2 - w, color='0.85', label='E0 (alle zu)')
    a.fill_between(w2, SQ2 - w, SQ2, color='#dbe9f6', label='E1 (a offen)')
    a.fill_between(w2, SQ2, SQ2 + w, color='#fde7d2', label='E2 (a, c offen)')
    a.fill_between(w2, SQ2 + w, 3.0, color='#e5f2df', label='E3 (a, b, c offen)')
    for z in zeilen:
        for q in z['e1']['null']:
            a.plot(z['w2'], q['rho'], '.', ms=3, color='tab:blue' if q['s'] > 0 else 'tab:red')
        for q in z['e2']['null']:
            a.plot(z['w2'], q['rho'], '.', ms=3, color='0.3')
    for fn in sorted(os.listdir(kdir)):
        if not fn.endswith('.json'):
            continue
        d = json.load(open(os.path.join(kdir, fn)))
        for e in d.get('kandidaten', []):
            if e.get('konvergiert') and e.get('bereich') == 'E1':
                gef = e.get('umlauf', {}).get('aufgeloest') and abs(e.get('umlauf', {}).get('umlauf', 0)) == 1
                a.plot(e['w2'], e['rho'], '*' if gef else 'x', ms=14, color='k', mfc='gold' if gef else 'none')
        for e in d.get('minima', []):
            if 'T' in e:
                a.plot(e['w2'], e['rho'], 'v', ms=7, color='purple', mfc='none')
    a.set_xlim(0.728, 2.0)
    a.set_ylim(0, 3.0)
    a.set_xlabel('omega^2')
    a.set_ylabel('rho')
    a.set_title('M2: Bereiche, Nullstellenkurven (E1: blau s>0, rot s<0; E2: grau G_b=0), Funde')
    a.legend(loc='upper left', fontsize=8)
    b = ax[1]
    for z in zeilen:
        for q in z['e2']['null']:
            b.semilogy(z['w2'], q['T'], '.', ms=3, color='0.3')
        if 'e3' in z:
            b.semilogy(z['w2'], min(z['e3']['T3']), 'g.', ms=3)
    for fn in sorted(os.listdir(kdir)):
        if fn.endswith('.json') and 'E2' in fn and 'st2' in fn:
            d = json.load(open(os.path.join(kdir, fn)))
            for e in d.get('minima', []):
                if 'T' in e:
                    b.semilogy(e['w2'], e['T'], 'v', ms=6, color='purple', mfc='none')
            if 'tau' in d:
                b.axhline(d['tau']['tau_E2'], color='purple', ls='--', lw=1)
                b.axhline(d['tau']['tau_E3'], color='green', ls=':', lw=1)
    b.set_xlabel('omega^2')
    b.set_ylabel('T auf G_b=0 (grau), verfeinerte E2-Minima (lila), min T3 (gruen); tau gestrichelt')
    b.set_title('Gesamtabstrahlung E2 / E3')
    fig.tight_layout()
    fig.savefig(aus, dpi=110)
    log('Bild', aus)


def main():
    c = sys.argv[1]
    if c == 'rauch':
        cmd_rauch()
    elif c == 'profile':
        cmd_profile(sys.argv[2], int(sys.argv[3]), sys.argv[4], [float(x) for x in sys.argv[5:]])
    elif c == 'zeilen':
        cmd_zeilen(int(sys.argv[2]), sys.argv[3], sys.argv[4], [float(x) for x in sys.argv[5:]])
    elif c == 'eichung':
        cmd_eichung(sys.argv[2], sys.argv[3], sys.argv[4])
    elif c == 'k2':
        cmd_k2(sys.argv[2], sys.argv[3])
    elif c == 'k1':
        cmd_k1(sys.argv[2], int(sys.argv[3]), sys.argv[4], sys.argv[5])
    elif c == 'kand':
        cmd_kand(int(sys.argv[2]), sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])
    elif c == 'homotopie':
        cmd_homotopie(int(sys.argv[2]), sys.argv[3], sys.argv[4])
    elif c == 'e2ziel':
        cmd_e2ziel(int(sys.argv[2]), sys.argv[3], sys.argv[4], sys.argv[5:])
    elif c == 'bild':
        cmd_bild(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        raise SystemExit('unbekannt: ' + c)
    log('fertig')


if __name__ == '__main__':
    main()
