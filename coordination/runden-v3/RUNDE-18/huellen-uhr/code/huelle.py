#!/usr/bin/env python3
"""huelle.py - Runde 18 HUELLEN-UHR. Eigener Zeitloeser des Code-Agenten (2026-10-02).
Plan: PLAN.md.eingefroren-20261002-125648, PLAN-NACHTRAG-1.md.eingefroren-20261002-130125.

Modell M2: psi komplex, chi reell, U = (1/4)(chi^2-1)^2 + (1+chi^2) S - S^2 + S^3/2, S = |psi|^2.
Radial, l = 0: u = r psi, v = r (chi - 1); D2 4. Ordnung mit ungerader Spiegelung an r = 0 und r = R (symmetrisch);
RK4, dt = h/4; Schwamm sig = 2 ((r - 60)/60)^3 ab r = 60; Messkugel r_m = 50.
Saat des Hintergrunds mit stille3.py (RUNDE-17/stille-zweifeld/code, unveraendert), danach eigener Newton.

Befehle:
  prep       <stelle Sa|Sb> <stufe 1|2> <aus.npz>
  lauf       <prep.npz> <zeilen z.B. 0,1,2> <perioden> <aus.npz>
  reflexion  <stufe> <tend> <aus.npz>
  auswertung <ausdir> <aus.json>
  bilder     <ausdir> <bilddir>
"""
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'
import sys
import json
import time
import math
import glob
import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
T0 = time.time()

STELLEN = {'Sa': (0.86085981, 1.06976351), 'Sb': (0.84743426, 1.33956049)}
DW2 = 0.01
HS = {1: 0.05, 2: 0.025}
R_GES = 120.0
R_A = 60.0
SIG0 = 2.0
R_M = 50.0
R_N = 25.0
R_BOX = 50.0
EPS = (0.002, 0.005)
SIGMA_K = 2.0
VIERPI = 4.0 * math.pi
ZEILEN_NAMEN = {0: 'null_i', 1: 'i_eps1', 2: 'i_eps2', 3: 'null_ii', 4: 'ii_eps1', 5: 'ii_eps2',
                6: 'iii_eps1', 7: 'iii_eps2'}


def log(*a):
    print('[%7.1fs]' % (time.time() - T0), *a, flush=True)


def schreibe_json(pfad, obj):
    with open(pfad + '.tmp', 'w') as fh:
        json.dump(obj, fh, indent=1)
    os.replace(pfad + '.tmp', pfad)


def speichere_npz(pfad, **arr):
    tmp = pfad[:-4] + '.tmp.npz' if pfad.endswith('.npz') else pfad + '.tmp.npz'
    np.savez(tmp, **arr)
    os.replace(tmp, pfad)


# ------------------------------------------------------------------ Gitter, Modell, Operatoren
def gitter(h):
    N = int(round(R_GES / h))
    return N, np.arange(N + 1) * h


def schwamm(r):
    x = np.clip((r - R_A) / (R_GES - R_A), 0.0, None)
    return SIG0 * x ** 3


def pot(S, chi):
    c2 = chi * chi
    US = 1.0 + c2 - 2.0 * S + 1.5 * S * S
    Uchi = chi * (c2 - 1.0) + 2.0 * chi * S
    return US, Uchi


def udichte(S, chi):
    return 0.25 * (chi * chi - 1.0) ** 2 + (1.0 + chi * chi) * S - S * S + 0.5 * S ** 3


class Lap:
    """D2 4. Ordnung auf (..., N+1); ungerade Spiegelung an beiden Enden; Randwerte 0."""

    def __init__(self, N, h, shape, dtype):
        self.N = N
        self.c = 1.0 / (12.0 * h * h)
        self.e = np.zeros(tuple(shape[:-1]) + (N + 3,), dtype=dtype)

    def __call__(self, u, out):
        N, e = self.N, self.e
        e[..., 1:N + 2] = u
        e[..., 0] = -u[..., 1]
        e[..., N + 2] = -u[..., N - 1]
        out[..., 1:N] = (16.0 * (e[..., 3:N + 2] + e[..., 1:N]) - 30.0 * e[..., 2:N + 1]
                         - (e[..., 4:N + 3] + e[..., 0:N - 1])) * self.c
        out[..., 0] = 0.0
        out[..., N] = 0.0
        return out


def d2_matrix(n, h):
    import scipy.sparse as sp
    main = np.full(n, -30.0)
    main[0] = -29.0
    main[-1] = -29.0
    return sp.diags([np.full(n - 2, -1.0), np.full(n - 1, 16.0), main, np.full(n - 1, 16.0), np.full(n - 2, -1.0)],
                    [-2, -1, 0, 1, 2], format='csr') / (12.0 * h * h)


def zentrum(U, h):
    p0 = (15.0 * U[..., 1] / h - 6.0 * U[..., 2] / (2 * h) + U[..., 3] / (3 * h)) / 10.0
    return p0.real ** 2 + p0.imag ** 2


def bilanz(U, Ut, V, Vt, h, r, m):
    """E_in, Q_in (i = 1..m) und E, Q gesamt; exakt diskrete Groessen."""
    N = U.shape[-1] - 1
    D2U = Lap(N, h, U.shape, complex)(U, np.empty_like(U))
    D2V = Lap(N, h, V.shape, float)(V, np.empty_like(V))
    ri = r[1:N]
    Ui, Uti, Vi, Vti = U[..., 1:N], Ut[..., 1:N], V[..., 1:N], Vt[..., 1:N]
    S = (Ui.real ** 2 + Ui.imag ** 2) / ri ** 2
    chi = 1.0 + Vi / ri
    e = ((Uti.real ** 2 + Uti.imag ** 2) - (Ui.real * D2U[..., 1:N].real + Ui.imag * D2U[..., 1:N].imag)
         + ri ** 2 * udichte(S, chi) + 0.5 * Vti ** 2 - 0.5 * Vi * D2V[..., 1:N])
    q = 2.0 * (Ui.real * Uti.imag - Ui.imag * Uti.real)
    fac = VIERPI * h
    return dict(E_in=fac * e[..., :m].sum(-1), Q_in=fac * q[..., :m].sum(-1),
                E=fac * e.sum(-1), Q=fac * q.sum(-1))


def fluss(U, Ut, V, Vt, m, c1, c2, fac):
    """Ausfluss aus {i <= m}: (F_E, F_Q) = -(dE_in/dt, dQ_in/dt), exakt aus den Kopplungen D2_ij, i <= m < j."""
    def g(i, j):
        return (Ut[:, i].real * U[:, j].real + Ut[:, i].imag * U[:, j].imag
                - U[:, i].real * Ut[:, j].real - U[:, i].imag * Ut[:, j].imag
                + 0.5 * (Vt[:, i] * V[:, j] - V[:, i] * Vt[:, j]))

    def q(i, j):
        return U[:, i].real * U[:, j].imag - U[:, i].imag * U[:, j].real

    dE = c1 * g(m, m + 1) + c2 * (g(m - 1, m + 1) + g(m, m + 2))
    dQ = 2.0 * (c1 * q(m, m + 1) + c2 * (q(m - 1, m + 1) + q(m, m + 2)))
    return -fac * dE, -fac * dQ


class System:
    def __init__(self, h, B, m=None):
        self.h = h
        self.N, self.r = gitter(h)
        N = self.N
        self.B = B
        self.inv_r = np.zeros(N + 1)
        self.inv_r[1:] = 1.0 / self.r[1:]
        self.inv_r2 = self.inv_r ** 2
        self.sig = schwamm(self.r)
        self.ka = int(np.argmax(self.sig > 0))
        self.sig_a = self.sig[self.ka:]
        self.lapU = Lap(N, h, (B, N + 1), complex)
        self.lapV = Lap(N, h, (B, N + 1), float)
        self.D2U = np.zeros((B, N + 1), complex)
        self.D2V = np.zeros((B, N + 1))
        self.m = int(round(R_M / h)) if m is None else m
        self.n = int(round(R_N / h))
        self.c1 = 16.0 / (12.0 * h * h)
        self.c2 = -1.0 / (12.0 * h * h)
        self.fac = VIERPI * h

    def rhs(self, U, Ut, V, Vt):
        D2U = self.lapU(U, self.D2U)
        D2V = self.lapV(V, self.D2V)
        S = (U.real ** 2 + U.imag ** 2) * self.inv_r2
        chi = 1.0 + V * self.inv_r
        US, Uchi = pot(S, chi)
        Utt = D2U - US * U
        Vtt = D2V - self.r * Uchi
        ka = self.ka
        Utt[:, ka:] -= self.sig_a * Ut[:, ka:]
        Vtt[:, ka:] -= self.sig_a * Vt[:, ka:]
        Utt[:, 0] = 0.0
        Utt[:, -1] = 0.0
        Vtt[:, 0] = 0.0
        Vtt[:, -1] = 0.0
        acc = np.empty((self.B, 6))
        acc[:, 0], acc[:, 1] = fluss(U, Ut, V, Vt, self.m, self.c1, self.c2, self.fac)
        acc[:, 2], acc[:, 3] = fluss(U, Ut, V, Vt, self.n, self.c1, self.c2, self.fac)
        Ua, Uta, Vta = U[:, ka:], Ut[:, ka:], Vt[:, ka:]
        acc[:, 4] = self.fac * np.sum(self.sig_a * (2.0 * (Uta.real ** 2 + Uta.imag ** 2) + Vta ** 2), axis=1)
        acc[:, 5] = self.fac * np.sum(self.sig_a * 2.0 * (Ua.real * Uta.imag - Ua.imag * Uta.real), axis=1)
        return Utt, Vtt, acc


def rk4(sy, U, Ut, V, Vt, A, dt):
    a1U, a1V, a1A = sy.rhs(U, Ut, V, Vt)
    hd = 0.5 * dt
    U2, Ut2, V2, Vt2 = U + hd * Ut, Ut + hd * a1U, V + hd * Vt, Vt + hd * a1V
    a2U, a2V, a2A = sy.rhs(U2, Ut2, V2, Vt2)
    U3, Ut3, V3, Vt3 = U + hd * Ut2, Ut + hd * a2U, V + hd * Vt2, Vt + hd * a2V
    a3U, a3V, a3A = sy.rhs(U3, Ut3, V3, Vt3)
    U4, Ut4, V4, Vt4 = U + dt * Ut3, Ut + dt * a3U, V + dt * Vt3, Vt + dt * a3V
    a4U, a4V, a4A = sy.rhs(U4, Ut4, V4, Vt4)
    s = dt / 6.0
    return (U + s * (Ut + 2.0 * (Ut2 + Ut3) + Ut4), Ut + s * (a1U + 2.0 * (a2U + a3U) + a4U),
            V + s * (Vt + 2.0 * (Vt2 + Vt3) + Vt4), Vt + s * (a1V + 2.0 * (a2V + a3V) + a4V),
            A + s * (a1A + 2.0 * (a2A + a3A) + a4A))


# ------------------------------------------------------------------ Hintergrund
def hintergrund_newton(w2, h, F0, H0, tol=1e-12, maxit=40):
    import scipy.sparse as sp
    from scipy.sparse.linalg import spsolve
    N, r = gitter(h)
    n = N - 1
    ri = r[1:N]
    D = d2_matrix(n, h)
    F = np.array(F0[1:N], float)
    H = np.array(H0[1:N], float)
    verl = []
    ok = False
    for it in range(maxit):
        f = F / ri
        S = f * f
        chi = 1.0 + H / ri
        US, Uchi = pot(S, chi)
        USS = -2.0 + 3.0 * S
        Ucc = 3.0 * chi * chi - 1.0 + 2.0 * S
        RF = D @ F - (US - w2) * F
        RH = D @ H - ri * Uchi
        J = sp.bmat([[D - sp.diags(US - w2 + 2.0 * S * USS), sp.diags(-2.0 * f * chi)],
                     [sp.diags(-4.0 * f * chi), D - sp.diags(Ucc)]], format='csc')
        dx = spsolve(J, -np.concatenate([RF, RH]))
        F = F + dx[:n]
        H = H + dx[n:]
        sch = float(np.abs(dx).max())
        verl.append(sch)
        if not np.isfinite(sch):
            break
        if sch < tol * max(1.0, float(np.abs(F).max())):
            ok = True
            break
    f = F / ri
    S = f * f
    chi = 1.0 + H / ri
    US, Uchi = pot(S, chi)
    res = max(float(np.abs(D @ F - (US - w2) * F).max()), float(np.abs(D @ H - ri * Uchi).max()))
    Fv = np.zeros(N + 1)
    Hv = np.zeros(N + 1)
    Fv[1:N] = F
    Hv[1:N] = H
    return Fv, Hv, ok, verl, res


def profil_info(w2, h, F, H):
    N, r = gitter(h)
    f = np.zeros(N + 1)
    g = np.ones(N + 1)
    f[1:] = F[1:] / r[1:]
    g[1:] = 1.0 + H[1:] / r[1:]
    f[0] = (15 * f[1] - 6 * f[2] + f[3]) / 10.0
    g[0] = (15 * g[1] - 6 * g[2] + g[3]) / 10.0
    w = math.sqrt(w2)
    k = int(np.argmax(f < 0.5 * f[0]))
    rhalf = float(r[k - 1] + (0.5 * f[0] - f[k - 1]) * h / (f[k] - f[k - 1]))
    U = F[None, :].astype(complex)
    b = bilanz(U, 1j * w * U, H[None, :], np.zeros((1, N + 1)), h, r, int(round(R_M / h)))
    return dict(w2=float(w2), f0=float(f[0]), chi0=float(g[0]), S0=float(f[0] ** 2), rhalf=rhalf,
                Q=float(b['Q'][0]), E=float(b['E'][0]), E_in=float(b['E_in'][0]), Q_in=float(b['Q_in'][0]),
                knoten=int(np.sum(f[1:N] < -1e-10 * f[0])), f_rm=float(abs(f[int(round(R_M / h))]) / f[0]))


# ------------------------------------------------------------------ Moden
def mode_suche(w2, F, H, h, rho0, rhalf, ref):
    import scipy.sparse as sp
    from scipy.sparse.linalg import eigsh
    nb = int(round(R_BOX / h)) - 1
    rr = np.arange(1, nb + 1) * h
    f = F[1:nb + 1] / rr
    S = f * f
    chi = 1.0 + H[1:nb + 1] / rr
    US, Uchi = pot(S, chi)
    USS = -2.0 + 3.0 * S
    Maa = US + S * USS
    Mab = S * USS
    Mac = 2.0 * f * chi
    Mcc = 3.0 * chi * chi - 1.0 + 2.0 * S
    D = d2_matrix(nb, h)
    w = math.sqrt(w2)
    dg = sp.diags

    def L(rho):
        return sp.bmat([[-D + dg(Maa - (w + rho) ** 2), dg(Mab), dg(Mac)],
                        [dg(Mab), -D + dg(Maa - (w - rho) ** 2), dg(Mac)],
                        [dg(Mac), dg(Mac), -D + dg(Mcc - rho ** 2)]], format='csc')

    innen = rr < rhalf + 10.0

    def lokal(v):
        q = v[:nb] ** 2 + v[nb:2 * nb] ** 2 + v[2 * nb:] ** 2
        return float(q[innen].sum() / q.sum())

    rho = float(rho0)
    verl = []
    ok = False
    v = None
    lam = None
    for it in range(20):
        vals, vecs = eigsh(L(rho), k=6, sigma=1e-4, which='LM')
        lok = [lokal(vecs[:, j]) for j in range(vecs.shape[1])]
        if ref is None:
            kand = [j for j in range(len(vals)) if lok[j] >= 0.9]
            if kand:
                k = min(kand, key=lambda j: abs(vals[j]))
            else:
                k = int(np.argmax(lok))
            wahl = lok[k]
        else:
            ov = [abs(float(vecs[:, j] @ ref)) for j in range(vecs.shape[1])]
            k = int(np.argmax(ov))
            wahl = ov[k]
        lam = float(vals[k])
        v = vecs[:, k].copy()
        A, B, C = v[:nb], v[nb:2 * nb], v[2 * nb:]
        dlam = -(2.0 * (w + rho) * float(A @ A) - 2.0 * (w - rho) * float(B @ B) + 2.0 * rho * float(C @ C))
        verl.append(dict(rho=rho, lam=lam, dlam=dlam, wahl=wahl, eigen=[float(x) for x in vals], lokal=lok))
        log('mode w2=%.8f it=%d rho=%.12f lam=%.3e wahl=%.6f eigen=%s lokal=%s' % (
            w2, it, rho, lam, wahl, ['%.4e' % x for x in vals], ['%.4f' % x for x in lok]))
        if abs(lam) < 1e-11:
            ok = True
            break
        rho = rho - lam / dlam
    A, B, C = v[:nb].copy(), v[nb:2 * nb].copy(), v[2 * nb:].copy()
    # Normierung: eps = max |delta S| / S(0), delta S = 2 f (a + b)
    dS = 2.0 * f * (A + B) / rr
    dS0 = (15 * dS[0] - 6 * dS[1] + dS[2]) / 10.0
    f0 = (15 * f[0] - 6 * f[1] + f[2]) / 10.0
    S0 = f0 * f0
    mx = max(float(np.abs(dS).max()), abs(dS0))
    skal = S0 / mx * (1.0 if dS0 >= 0 else -1.0)
    A *= skal
    B *= skal
    C *= skal
    c = 2.0 * C / rr
    # Lokalisierung: Betrag je Kanal in [r_half + 15, 45] relativ zum Maximum der Mode (u-Groessen)
    sel = (rr >= rhalf + 15.0) & (rr <= 45.0)
    mxall = max(float(np.abs(A).max()), float(np.abs(B).max()), float(np.abs(C).max()))
    schw = rr >= rhalf + 5.0
    # lineare Ladung (muss fuer eine Eigenmode verschwinden)
    Fb = F[1:nb + 1]
    q1 = float(np.sum(Fb * ((2 * w + rho) * A + (2 * w - rho) * B)))
    q1n = q1 / float(np.sqrt(np.sum(Fb ** 2) * np.sum(((2 * w + rho) * A) ** 2 + ((2 * w - rho) * B) ** 2)))
    N, r = gitter(h)
    Af = np.zeros(N + 1)
    Bf = np.zeros(N + 1)
    Cf = np.zeros(N + 1)
    Af[1:nb + 1] = A
    Bf[1:nb + 1] = B
    Cf[1:nb + 1] = C
    info = dict(w2=float(w2), rho=float(rho), lam=lam, konvergiert=ok, schritte=verl, nb=nb, R_box=R_BOX,
                zentrum_rel=abs(dS0) / mx, c_max_pro_eps=float(np.abs(c).max()),
                a_max_pro_eps=float(np.abs(A / rr).max()), b_max_pro_eps=float(np.abs(B / rr).max()),
                schwanz_a=float(np.abs(A[sel]).max() / mxall), schwanz_b=float(np.abs(B[sel]).max() / mxall),
                schwanz_c=float(np.abs(C[sel]).max() / mxall), schwanz_bereich=[rhalf + 15.0, 45.0],
                anteil_a_aussen=float(np.sum(A[schw] ** 2) / np.sum(A ** 2 + B ** 2 + C ** 2)),
                lokal=lokal(np.concatenate([A, B, C])), q1_rel=q1n)
    return Af, Bf, Cf, np.concatenate([v[:nb], v[nb:2 * nb], v[2 * nb:]]), info


# ------------------------------------------------------------------ Befehle
def cmd_prep(stelle, stufe, aus):
    h = HS[stufe]
    w2i, rho_k = STELLEN[stelle]
    w2ii = w2i + DW2
    N, r = gitter(h)
    sys.path.insert(0, HIER)
    import stille3 as S3
    mod = S3.modell_von('M2')
    hp = 0.05
    p = S3.saat(mod, 'M2', 200.0, hp)
    log('stille3-Saat w2=%.6f Q=%.3f' % (p['w2'], p['Q']))
    profs = {}
    for name, ziel in (('ii', w2ii), ('i', w2i)):
        ziele = [x for x in S3.ZEILEN if ziel < x < p['w2'] - 1e-9][::-1] + [ziel]
        for x in ziele:
            q = S3.fortsetzung(mod, p, x, hp)
            if q is None:
                raise RuntimeError('Fortsetzung gescheitert bei w2=%.8f' % x)
            p = q
        profs[name] = p
        log('stille3-Profil %s: w2=%.8f Q=%.4f rhalf=%.4f chi0=%.4e' % (name, p['w2'], p['Q'], p['rhalf'], p['chi0']))
    meta = dict(stelle=stelle, stufe=stufe, h=h, N=N, R=R_GES, R_A=R_A, SIG0=SIG0, R_M=R_M, R_N=R_N, R_BOX=R_BOX,
                w2_i=w2i, w2_ii=w2ii, rho_karte=rho_k, EPS=list(EPS), SIGMA_K=SIGMA_K)
    arr = dict(r=r)
    hg = {}
    for name, ziel in (('i', w2i), ('ii', w2ii)):
        p = profs[name]
        rs, fs, gs_ = S3.fg_aus(p['F'], p['H'], p['hp'], p['N'])
        f0 = np.interp(r, rs, fs, right=0.0)
        g0 = np.interp(r, rs, gs_, right=1.0)
        F, H, ok, verl, res = hintergrund_newton(ziel, h, r * f0, r * (g0 - 1.0))
        if not ok:
            raise RuntimeError('Newton Hintergrund %s nicht konvergiert: %s' % (name, verl))
        info = profil_info(ziel, h, F, H)
        info.update(newton=verl, residuum=res, stille3_Q=p['Q'], stille3_rhalf=p['rhalf'], stille3_chi0=p['chi0'],
                    dQ_rel_zu_stille3=abs(info['Q'] / p['Q'] - 1))
        log('Hintergrund %s: %s' % (name, json.dumps(info)))
        meta['bg_' + name] = info
        arr['F_' + name] = F
        arr['H_' + name] = H
        hg[name] = (F, H, info)
    ref = None
    for name, ziel in (('i', w2i), ('ii', w2ii)):
        F, H, info = hg[name]
        rho0 = rho_k if name == 'i' else meta['mode_i']['rho']
        Af, Bf, Cf, vec, minfo = mode_suche(ziel, F, H, h, rho0, info['rhalf'], ref)
        if name == 'i':
            ref = vec
        meta['mode_' + name] = minfo
        meta['rho_' + name] = minfo['rho']
        arr['A_' + name] = Af
        arr['B_' + name] = Bf
        arr['C_' + name] = Cf
        log('Mode %s: %s' % (name, json.dumps({k: v for k, v in minfo.items() if k != 'schritte'})))
    meta['sekunden'] = time.time() - T0
    speichere_npz(aus, meta=json.dumps(meta), **arr)
    schreibe_json(aus[:-4] + '.json', meta)
    log('prep fertig', aus)


def anfangsdaten(d, meta, z, h, r):
    N = len(r) - 1
    w_i = math.sqrt(meta['w2_i'])
    w_ii = math.sqrt(meta['w2_ii'])
    if z in (0, 1, 2, 6, 7):
        F, H, w = d['F_i'], d['H_i'], w_i
    else:
        F, H, w = d['F_ii'], d['H_ii'], w_ii
    u = F.astype(complex)
    ut = 1j * w * F
    v = H.astype(float).copy()
    vt = np.zeros(N + 1)
    if z in (1, 2, 4, 5):
        eps = EPS[0] if z in (1, 4) else EPS[1]
        sfx = 'i' if z in (1, 2) else 'ii'
        A, B, C = d['A_' + sfx], d['B_' + sfx], d['C_' + sfx]
        rho = meta['rho_' + sfx]
        u = u + eps * (A + B)
        ut = ut + 1j * eps * ((w + rho) * A + (w - rho) * B)
        v = v + eps * 2.0 * C
    return u, ut, v, vt


def cmd_lauf(prep, zeilen, perioden, aus):
    d = np.load(prep)
    meta = json.loads(str(d['meta']))
    h = meta['h']
    N = meta['N']
    r = d['r']
    m = int(round(R_M / h))
    zl = [int(z) for z in zeilen.split(',')]
    B = len(zl)
    U = np.zeros((B, N + 1), complex)
    Ut = np.zeros((B, N + 1), complex)
    V = np.zeros((B, N + 1))
    Vt = np.zeros((B, N + 1))
    # Anregungsenergie (i) je eps am Anfang (fuer (iii))
    tmp = [anfangsdaten(d, meta, z, h, r) for z in (0, 1, 2)]
    bt = bilanz(np.array([x[0] for x in tmp]), np.array([x[1] for x in tmp]), np.array([x[2] for x in tmp]),
                np.array([x[3] for x in tmp]), h, r, m)
    Eexc_i = [float(bt['E_in'][1] - bt['E_in'][0]), float(bt['E_in'][2] - bt['E_in'][0])]
    gk = r * np.exp(-r ** 2 / SIGMA_K ** 2)
    gk[0] = 0.0
    gk[N] = 0.0
    ek1 = VIERPI * h * float(np.sum(0.5 * gk[1:m + 1] ** 2))
    Ak = [math.sqrt(abs(e) / ek1) for e in Eexc_i]
    for b, z in enumerate(zl):
        if z in (6, 7):
            u, ut, v, vt = anfangsdaten(d, meta, 0, h, r)
            vt = Ak[z - 6] * gk
        else:
            u, ut, v, vt = anfangsdaten(d, meta, z, h, r)
        U[b], Ut[b], V[b], Vt[b] = u, ut, v, vt
    T = perioden * 2.0 * math.pi / meta['rho_karte']
    dt = h / 4.0
    ns = int(math.ceil(T / dt))
    sy = System(h, B)
    A = np.zeros((B, 6))
    lm = dict(prep=os.path.basename(prep), zeilen=zl, namen=[ZEILEN_NAMEN[z] for z in zl], h=h, N=N, dt=dt,
              T=ns * dt, schritte=ns, perioden=perioden, Eexc_i=Eexc_i, A_kick=Ak, m=m, n=sy.n,
              stelle=meta['stelle'], stufe=meta['stufe'])
    td, dz = [0.0], [zentrum(U, h)]
    b0 = bilanz(U, Ut, V, Vt, h, r, m)
    tb, Ein, Qin, Eg, Qg, Acc = [0.0], [b0['E_in']], [b0['Q_in']], [b0['E']], [b0['Q']], [A.copy()]
    lm['E_in0'] = b0['E_in'].tolist()
    lm['Q_in0'] = b0['Q_in'].tolist()
    log('lauf %s zeilen=%s T=%.3f dt=%.5f schritte=%d E_in0=%s' % (aus, zl, T, dt, ns, b0['E_in'].tolist()))
    t1 = time.time()
    abschnitt = max(1, ns // 10)

    def sichern(fertig, s):
        lm2 = dict(lm)
        lm2.update(fertig=fertig, schritt=s, sekunden=time.time() - T0, sek_lauf=time.time() - t1)
        speichere_npz(aus, meta=json.dumps(lm2), td=np.array(td), dz=np.array(dz), tb=np.array(tb),
                      E_in=np.array(Ein), Q_in=np.array(Qin), E=np.array(Eg), Q=np.array(Qg), acc=np.array(Acc))

    for s in range(1, ns + 1):
        U, Ut, V, Vt, A = rk4(sy, U, Ut, V, Vt, A, dt)
        if s % 2 == 0:
            td.append(s * dt)
            dz.append(zentrum(U, h))
        if s % 8 == 0 or s == ns:
            bb = bilanz(U, Ut, V, Vt, h, r, m)
            tb.append(s * dt)
            Ein.append(bb['E_in'])
            Qin.append(bb['Q_in'])
            Eg.append(bb['E'])
            Qg.append(bb['Q'])
            Acc.append(A.copy())
        if s == 200:
            log('200 Schritte: %.2f ms/Schritt, Prognose %.1f s' % (
                1e3 * (time.time() - t1) / 200, (time.time() - t1) / 200 * ns))
        if s % abschnitt == 0 and s < ns:
            sichern(False, s)
            log('schritt %d/%d t=%.2f' % (s, ns, s * dt))
    sichern(True, ns)
    log('lauf fertig %.1f s' % (time.time() - t1))


def cmd_reflexion(stufe, tend, aus):
    h = HS[stufe]
    N, r = gitter(h)
    B = 4
    U = np.zeros((B, N + 1), complex)
    Ut = np.zeros((B, N + 1), complex)
    V = np.zeros((B, N + 1))
    Vt = np.zeros((B, N + 1))
    G = 1e-3 * np.exp(-(r - 30.0) ** 2 / (2 * 6.0 ** 2))
    G[0] = 0.0
    G[N] = 0.0
    pakete = [('psi', 1.41), ('psi', 0.7), ('chi', 1.6), ('chi', 0.7)]
    for b, (art, k0) in enumerate(pakete):
        Om = math.sqrt(k0 * k0 + 2.0)
        if art == 'psi':
            U[b] = G * np.exp(-1j * k0 * r)
            Ut[b] = 1j * Om * U[b]
        else:
            V[b] = G * np.cos(k0 * r)
            Vt[b] = Om * G * np.sin(k0 * r)
    m55 = int(round(55.0 / h))
    sy = System(h, B)
    dt = h / 4.0
    ns = int(math.ceil(tend / dt))
    A = np.zeros((B, 6))
    b0 = bilanz(U, Ut, V, Vt, h, r, m55)
    tb, E55, Eg, Acc = [0.0], [b0['E_in']], [b0['E']], [A.copy()]
    t1 = time.time()
    for s in range(1, ns + 1):
        U, Ut, V, Vt, A = rk4(sy, U, Ut, V, Vt, A, dt)
        if s % 40 == 0 or s == ns:
            bb = bilanz(U, Ut, V, Vt, h, r, m55)
            tb.append(s * dt)
            E55.append(bb['E_in'])
            Eg.append(bb['E'])
            Acc.append(A.copy())
        if s == 200:
            log('200 Schritte: %.2f ms/Schritt, Prognose %.1f s' % (
                1e3 * (time.time() - t1) / 200, (time.time() - t1) / 200 * ns))
    tb = np.array(tb)
    E55 = np.array(E55)
    Eg = np.array(Eg)
    Acc = np.array(Acc)
    spaet = tb >= 0.8 * tend
    erg = dict(stufe=stufe, h=h, tend=tend, pakete=pakete, E0=E55[0].tolist(),
               reflexion_ende=(E55[-1] / E55[0]).tolist(), reflexion_max_spaet=(E55[spaet].max(0) / E55[0]).tolist(),
               bilanz_gesamt_rel=(np.abs(Eg + Acc[:, :, 4] - Eg[0]).max(0) / E55[0]).tolist(),
               sekunden=time.time() - t1)
    speichere_npz(aus, meta=json.dumps(erg), tb=tb, E55=E55, E=Eg, acc=Acc)
    schreibe_json(aus[:-4] + '.json', erg)
    log('reflexion', json.dumps(erg))


# ------------------------------------------------------------------ Auswertung
def ticks(t, x, aref):
    hi, lo = 0.5 * aref, -0.5 * aref
    scharf = False
    tk = []
    letzt = None
    for k in range(1, len(x)):
        if x[k - 1] < 0.0 <= x[k]:
            letzt = t[k - 1] + (0.0 - x[k - 1]) * (t[k] - t[k - 1]) / (x[k] - x[k - 1])
        if x[k] < lo:
            scharf = True
        if scharf and x[k] > hi:
            if letzt is not None:
                tk.append(letzt)
            scharf = False
    return np.array(tk)


def periode(tk):
    if len(tk) < 3:
        return None, None, None
    p = np.polyfit(np.arange(len(tk)), tk, 1)
    dd = np.diff(tk)
    return float(p[0]), float(dd.mean()), float(dd.std())


def huellkurve(t, x, P, t_ab):
    nf = int(t[-1] // P)
    tm, am = [], []
    for k in range(nf):
        sel = (t >= k * P) & (t < (k + 1) * P)
        if sel.sum() < 4:
            continue
        tm.append((k + 0.5) * P)
        am.append(0.5 * (x[sel].max() - x[sel].min()))
    tm = np.array(tm)
    am = np.array(am)
    sel = (tm >= t_ab) & (am > 0)
    if sel.sum() < 3:
        return None, None, tm, am
    p = np.polyfit(tm[sel], np.log(am[sel]), 1)
    res = np.log(am[sel]) - np.polyval(p, tm[sel])
    se = math.sqrt(float(np.sum(res ** 2)) / max(1, sel.sum() - 2) / float(np.sum((tm[sel] - tm[sel].mean()) ** 2)))
    return float(-p[0]), se, tm, am


def lade_laeufe(ausdir):
    """Liefert {(stelle, stufe): {zeile: dict(td, dz, tb, E_in, Q_in, E, Q, acc, meta)}}."""
    alle = {}
    for fn in sorted(glob.glob(os.path.join(ausdir, 'lauf-*.npz'))):
        if '.tmp.' in fn:
            continue
        d = np.load(fn)
        mt = json.loads(str(d['meta']))
        if not mt.get('fertig'):
            continue
        key = (mt['stelle'], mt['stufe'])
        for b, z in enumerate(mt['zeilen']):
            alle.setdefault(key, {})[z] = dict(td=d['td'], dz=d['dz'][:, b], tb=d['tb'], E_in=d['E_in'][:, b],
                                               Q_in=d['Q_in'][:, b], E=d['E'][:, b], Q=d['Q'][:, b],
                                               acc=d['acc'][:, b, :], meta=mt, datei=os.path.basename(fn))
    return alle


def werte_satz(rows, prepmeta):
    rho_k = prepmeta['rho_karte']
    rho = {'i': prepmeta['rho_i'], 'ii': prepmeta['rho_ii']}
    Pk = 2 * math.pi / rho_k
    erg = {}
    aref = {}
    for z in (1, 2, 4, 5, 6, 7):
        if z not in rows:
            continue
        nz = 0 if z in (1, 2, 6, 7) else 3
        R = rows[z]
        N0 = rows.get(nz)
        x = R['dz'] - (N0['dz'] if N0 is not None else R['dz'][0])
        t = R['td']
        rr = rho['ii'] if z in (4, 5) else rho['i']
        P = 2 * math.pi / rr
        a0 = float(np.abs(x[t <= 2 * P]).max())
        aref[z] = a0
        tk = ticks(t, x, a0)
        Pf, Pm, Ps = periode(tk)
        gam, gse, tm, am = huellkurve(t, x, P, 5 * P)
        E0 = R['E_in'][0]
        Eexc = float(E0 - N0['E_in'][0]) if N0 is not None else None
        if z in (6, 7):
            Eexc = abs(R['meta']['Eexc_i'][z - 6])
        Eaus = float(R['acc'][-1, 0])
        bilE = np.abs(R['E_in'] + R['acc'][:, 0] - R['E_in'][0])
        bilQ = np.abs(R['Q_in'] + R['acc'][:, 1] - R['Q_in'][0])
        bilG = np.abs(R['E'] + R['acc'][:, 4] - R['E'][0])
        e = dict(name=ZEILEN_NAMEN[z], E_exc=Eexc, E_aus_T=Eaus, f_rad=Eaus / Eexc if Eexc else None,
                 E_aus_n_T=float(R['acc'][-1, 2]), f_rad_n=float(R['acc'][-1, 2]) / Eexc if Eexc else None,
                 Q_aus_T=float(R['acc'][-1, 1]), E_abs_T=float(R['acc'][-1, 4]),
                 A_ref=a0, n_ticks=int(len(tk)), P_tick_fit=Pf, P_tick_mittel=Pm, P_tick_streu=Ps,
                 P_soll_karte=Pk, P_soll_mode=P,
                 dP_rel_karte=(abs(Pf - Pk) / Pk if Pf else None), dP_rel_mode=(abs(Pf - P) / P if Pf else None),
                 gamma=gam, gamma_se=gse, gammaT=(gam * R['tb'][-1] if gam is not None else None),
                 bilanz_E_rel=float(bilE.max() / abs(Eexc)) if Eexc else None,
                 bilanz_Q_rel=float(bilQ.max() / abs(R['Q_in'][0])),
                 bilanz_E_abs=float(bilE.max()), bilanz_gesamt_rel=float(bilG.max() / abs(Eexc)) if Eexc else None,
                 T=float(R['tb'][-1]), datei=R['datei'])
        if N0 is not None:
            bn = np.abs(N0['E_in'] + N0['acc'][:, 0] - N0['E_in'][0])
            e['bilanz_E_rel_nullkorr'] = float(np.abs((R['E_in'] + R['acc'][:, 0] - R['E_in'][0])
                                                      - (N0['E_in'] + N0['acc'][:, 0] - N0['E_in'][0])).max() / abs(Eexc))
            e['bilanz_null_E_abs'] = float(bn.max())
        erg[ZEILEN_NAMEN[z]] = e
    for z, zref in ((0, 1), (3, 4)):
        if z not in rows:
            continue
        R = rows[z]
        x = R['dz'] - R['dz'][0]
        a0 = aref.get(zref)
        tk = ticks(R['td'], x, a0) if a0 else np.array([])
        bilE = np.abs(R['E_in'] + R['acc'][:, 0] - R['E_in'][0])
        bilQ = np.abs(R['Q_in'] + R['acc'][:, 1] - R['Q_in'][0])
        bilG = np.abs(R['E'] + R['acc'][:, 4] - R['E'][0])
        erg[ZEILEN_NAMEN[z]] = dict(name=ZEILEN_NAMEN[z], n_ticks=int(len(tk)), schwelle=(0.5 * a0 if a0 else None),
                                    max_abw_dichte=float(np.abs(x).max()),
                                    max_abw_rel_zu_Aref=(float(np.abs(x).max()) / a0 if a0 else None),
                                    bilanz_E_rel=float(bilE.max() / abs(R['E_in'][0])),
                                    bilanz_Q_rel=float(bilQ.max() / abs(R['Q_in'][0])),
                                    bilanz_gesamt_rel=float(bilG.max() / abs(R['E'][0])),
                                    E_aus_T=float(R['acc'][-1, 0]), Q_aus_T=float(R['acc'][-1, 1]),
                                    E_in0=float(R['E_in'][0]), Q_in0=float(R['Q_in'][0]), T=float(R['tb'][-1]))
    return erg


def cmd_auswertung(ausdir, aus):
    alle = lade_laeufe(ausdir)
    prep = {}
    for fn in glob.glob(os.path.join(ausdir, 'prep-*.json')):
        mt = json.load(open(fn))
        prep[(mt['stelle'], mt['stufe'])] = mt
    erg = dict(saetze={}, H={})
    for key in sorted(alle):
        if key not in prep:
            continue
        s = werte_satz(alle[key], prep[key])
        for nm in ('i', 'ii', 'iii'):
            a, b = s.get(nm + '_eps1'), s.get(nm + '_eps2')
            if a and b and a['E_aus_T'] > 0 and b['E_aus_T'] > 0:
                s[nm + '_exponent_p'] = math.log(b['E_aus_T'] / a['E_aus_T']) / math.log(EPS[1] / EPS[0])
        for k in ('eps1', 'eps2'):
            a, b = s.get('i_' + k), s.get('ii_' + k)
            if a and b and a['f_rad'] and b['f_rad']:
                s['verhaeltnis_ii_i_' + k] = b['f_rad'] / a['f_rad']
        erg['saetze']['%s-st%d' % key] = s

    def urteil(stufe):
        ss = {k: v for k, v in erg['saetze'].items() if k.endswith('st%d' % stufe)}
        if len(ss) < 2:
            return None
        u = {}
        try:
            u['H1'] = all(s[n]['n_ticks'] == 0 and s[n]['bilanz_E_rel'] < 1e-6 and s[n]['bilanz_Q_rel'] < 1e-6
                          for s in ss.values() for n in ('null_i', 'null_ii'))
            u['H2'] = all(s[n]['P_tick_fit'] is not None and s[n]['n_ticks'] >= 30 and s[n]['dP_rel_karte'] < 1e-3
                          for s in ss.values() for n in ('i_eps1', 'i_eps2'))
            u['H3'] = all(s['verhaeltnis_ii_i_' + k] >= 30 for s in ss.values() for k in ('eps1', 'eps2'))
            u['H4'] = all(3.5 <= s['i_exponent_p'] <= 4.5 and 1.5 <= s['ii_exponent_p'] <= 2.5 for s in ss.values())
            u['H5'] = all(s[n]['f_rad'] > 0.5 for s in ss.values() for n in ('iii_eps1', 'iii_eps2'))
        except (KeyError, TypeError) as ex:
            u['fehler'] = repr(ex)
        return u

    u1, u2 = urteil(1), urteil(2)
    erg['urteil_grob'] = u1
    erg['urteil_fein'] = u2
    if u1 and u2:
        for k in ('H1', 'H2', 'H3', 'H4', 'H5'):
            if k in u1 and k in u2:
                erg['H'][k] = ('eingetroffen' if u2[k] else 'nicht eingetroffen') if u1[k] == u2[k] else (
                    'offen (Gitter)')
    erg['prep'] = {'%s-st%d' % k: v for k, v in prep.items()}
    schreibe_json(aus, erg)
    log(json.dumps(erg['H']), json.dumps(u1), json.dumps(u2))


def cmd_bilder(ausdir, bilddir):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    os.makedirs(bilddir, exist_ok=True)
    alle = lade_laeufe(ausdir)
    for (stelle, stufe), rows in sorted(alle.items()):
        fig, ax = plt.subplots(4, 1, figsize=(13, 13), sharex=True)
        for a, (zs, nz, titel) in zip(ax, [((1, 2), 0, '(i) BIC'), ((4, 5), 3, '(ii) omega^2 + 0,01'),
                                           ((6, 7), 0, '(iii) Gauss-Stoss in chi'), ((0, 3), None, '(iv) Nullarme')]):
            for z in zs:
                if z not in rows:
                    continue
                R = rows[z]
                if nz is None:
                    x = R['dz'] - R['dz'][0]
                else:
                    x = R['dz'] - rows[nz]['dz'] if nz in rows else R['dz'] - R['dz'][0]
                a.plot(R['td'], x, lw=0.6, label=ZEILEN_NAMEN[z])
            a.set_title('%s, %s, Stufe %d: |psi(0,t)|^2 minus Referenz' % (stelle, titel, stufe))
            a.legend(loc='upper right', fontsize=8)
        ax[-1].set_xlabel('t')
        fig.tight_layout()
        fig.savefig(os.path.join(bilddir, 'dichte-%s-st%d.png' % (stelle, stufe)), dpi=100)
        plt.close(fig)
        fig, a = plt.subplots(1, 1, figsize=(11, 6))
        for z in (1, 2, 4, 5, 6, 7):
            if z not in rows:
                continue
            R = rows[z]
            nz = 0 if z in (1, 2, 6, 7) else 3
            Eexc = abs(R['meta']['Eexc_i'][z - 6]) if z in (6, 7) else float(R['E_in'][0] - rows[nz]['E_in'][0])
            y = np.abs(R['acc'][:, 0]) / abs(Eexc)
            a.semilogy(R['tb'], np.maximum(y, 1e-16), label=ZEILEN_NAMEN[z])
        a.set_xlabel('t')
        a.set_ylabel('|E_aus(r_m = 50)| / E_exc')
        a.set_title('%s, Stufe %d: abgestrahlte Energie (Fluss durch r_m), log' % (stelle, stufe))
        a.legend(fontsize=8)
        fig.tight_layout()
        fig.savefig(os.path.join(bilddir, 'abstrahlung-%s-st%d.png' % (stelle, stufe)), dpi=100)
        plt.close(fig)
    preps = sorted(glob.glob(os.path.join(ausdir, 'prep-*.npz')))
    if preps:
        fig, ax = plt.subplots(len(preps), 2, figsize=(14, 3.6 * len(preps)), squeeze=False)
        for k, fn in enumerate(preps):
            d = np.load(fn)
            mt = json.loads(str(d['meta']))
            r = d['r']
            sel = (r > 0) & (r <= R_BOX)
            for j, sfx in enumerate(('i', 'ii')):
                a = ax[k, j]
                rr = r[sel]
                a.plot(rr, d['A_' + sfx][sel] / rr, label='a')
                a.plot(rr, d['B_' + sfx][sel] / rr, label='b')
                a.plot(rr, 2 * d['C_' + sfx][sel] / rr, label='c (chi)')
                f = d['F_' + sfx][sel] / rr
                a.plot(rr, f / np.abs(f).max() * np.abs(2 * d['C_' + sfx][sel] / rr).max(), 'k:', lw=0.8,
                       label='f (skaliert)')
                a.set_title('%s Stufe %d, Mode (%s): w2=%.8f rho=%.8f, Schwanz a=%.1e' % (
                    mt['stelle'], mt['stufe'], sfx, mt['mode_' + sfx]['w2'], mt['mode_' + sfx]['rho'],
                    mt['mode_' + sfx]['schwanz_a']), fontsize=9)
                a.legend(fontsize=7)
        fig.tight_layout()
        fig.savefig(os.path.join(bilddir, 'moden.png'), dpi=100)
        plt.close(fig)
    log('bilder fertig')


def main():
    c = sys.argv[1]
    if c == 'prep':
        cmd_prep(sys.argv[2], int(sys.argv[3]), sys.argv[4])
    elif c == 'lauf':
        cmd_lauf(sys.argv[2], sys.argv[3], float(sys.argv[4]), sys.argv[5])
    elif c == 'reflexion':
        cmd_reflexion(int(sys.argv[2]), float(sys.argv[3]), sys.argv[4])
    elif c == 'auswertung':
        cmd_auswertung(sys.argv[2], sys.argv[3])
    elif c == 'bilder':
        cmd_bilder(sys.argv[2], sys.argv[3])
    else:
        raise SystemExit('unbekannt: ' + c)
    log('fertig')


if __name__ == '__main__':
    main()
