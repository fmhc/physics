#!/usr/bin/env python3
"""zweifeld.py - Runde 17 ZWEIFELD-NACHBAU. Eigener Code des Code-Agenten (frischer Kontext, 2026-10-02).

Stille Stellen der radialen Mode l = 0 im Zweifeldmodell M2; Kontrolle K1 im Einfeldmodell M1.
Verfahren und Herleitung: PLAN.md im Kartenordner.

Kanaele (u = r a, r b, r ct mit ct = c/2, symmetrische Form):
  u'' = P(r) u,  P = [[Va - Ea, gs, hh], [gs, Va - Eb, hh], [hh, hh, Wc - Ec]]
  Va = U_S + S U_SS, gs = S U_SS, hh = f U_Schi, Wc = U_chichi; Ea = (w+rho)^2, Eb = (w-rho)^2, Ec = rho^2.
Hintergrund: Saat mit BEUTEL-1-Code (beutel_v2.py, unveraendert), dann eigener Numerov-Newton (4. Ordnung).

Unterbefehle:
  profile <modell> <aus-praefix>
  scan    <modell> <stufe> <npz> <ausdir> <w2 ...>
  kand    <modell> <stufe> <npz> <ausdatei> <zeilendateien ...>
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

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

STUFEN = {1: 0.01, 2: 0.005}          # Profilschritt hp; RK4-Schritt h = 2 hp
GS_DR = 1.0                            # Orthonormierung bei r = 1, 2, 3, ...
RAND = 2e-3                            # Abstand des gleichmaessigen rho-Gitters von den E1-Grenzen
NRHO = 401
RAND_PUNKTE = [1e-5, 2e-5, 5e-5, 1e-4, 2e-4, 5e-4, 1e-3, 1.5e-3]
HALB = 1e-3                            # Halbbreite des Umlauf-Rechtecks (w2 und rho)
NKANTE = 16
SPRUNG = 0.4
VERF_RUNDEN = 40

MODELLE = {
    'M1': dict(nch=2, m2=1.0, Qsaat=300.0, dR=40.0,
               zeilen=[round(0.786 + 0.002 * j, 6) for j in range(13)]),
    'M2': dict(nch=3, m2=2.0, Qsaat=3000.0, dR=35.0,
               zeilen=[round(0.830 + 0.002 * j, 6) for j in range(41)]),
}
K2_ZEILEN = [0.83, 0.85, 0.87, 0.89, 0.91]


def log(s):
    print(time.strftime('%H:%M:%S'), s, flush=True)


def speichere_json(pfad, d):
    with open(pfad + '.tmp', 'w') as fh:
        json.dump(d, fh)
    os.replace(pfad + '.tmp', pfad)


# ------------------------------------------------------------------ Hintergrund (Numerov, u = r f, v = r (g - 1))
def _terme(modell, w2, r, u, v):
    f = np.zeros_like(u)
    f[1:] = u[1:] / r[1:]
    S = f * f
    if modell == 'M1':
        US = 1.0 - 2.0 * S + 1.5 * S * S
        USS = -2.0 + 3.0 * S
        F = (US - w2) * u
        Fu = US - w2 + 2.0 * S * USS
        F[0] = 0.0
        return F, Fu, None, None, None, None
    wg = np.zeros_like(u)
    wg[1:] = v[1:] / r[1:]
    g = 1.0 + wg
    g2m1 = wg * (2.0 + wg)
    US = 1.0 + g * g - 2.0 * S + 1.5 * S * S
    USS = -2.0 + 3.0 * S
    Uchi = g * g2m1 + 2.0 * g * S
    Ucc = 3.0 * g * g - 1.0 + 2.0 * S
    F = (US - w2) * u
    G = r * Uchi
    Fu = US - w2 + 2.0 * S * USS
    Fv = 2.0 * f * g
    Gu = 4.0 * f * g
    Gv = Ucc
    F[0] = 0.0
    G[0] = 0.0
    return F, Fu, Fv, G, Gu, Gv


def numerov_newton(modell, w2, hp, u, v, tol=1e-13, maxit=40):
    N = len(u) - 1
    r = np.arange(N + 1) * hp
    c = hp * hp / 12.0
    u = u.copy()
    u[0] = 0.0
    u[-1] = 0.0
    if v is not None:
        v = v.copy()
        v[0] = 0.0
        v[-1] = 0.0
    K = N - 1
    sch = np.inf
    sch_vor = np.inf
    for it in range(maxit):
        F, Fu, Fv, G, Gu, Gv = _terme(modell, w2, r, u, v)
        Ru = u[2:] - 2.0 * u[1:-1] + u[:-2] - c * (F[2:] + 10.0 * F[1:-1] + F[:-2])
        if modell == 'M1':
            fu = Fu[1:-1]
            ab = np.zeros((3, K))
            ab[1] = -2.0 - 10.0 * c * fu
            ab[0, 1:] = 1.0 - c * fu[1:]
            ab[2, :-1] = 1.0 - c * fu[:-1]
            du = solve_banded((1, 1), ab, -Ru, check_finite=False)
            u[1:-1] += du
            sch = float(np.max(np.abs(du)))
        else:
            Rv = v[2:] - 2.0 * v[1:-1] + v[:-2] - c * (G[2:] + 10.0 * G[1:-1] + G[:-2])
            fu, fv, gu, gv = Fu[1:-1], Fv[1:-1], Gu[1:-1], Gv[1:-1]
            ab = np.zeros((7, 2 * K))
            ab[3, 0::2] = -2.0 - 10.0 * c * fu
            ab[2, 1::2] = -10.0 * c * fv
            ab[4, 0::2] = -10.0 * c * gu
            ab[3, 1::2] = -2.0 - 10.0 * c * gv
            ab[5, 0:2 * K - 2:2] = 1.0 - c * fu[:-1]
            ab[4, 1:2 * K - 2:2] = -c * fv[:-1]
            ab[6, 0:2 * K - 2:2] = -c * gu[:-1]
            ab[5, 1:2 * K - 2:2] = 1.0 - c * gv[:-1]
            ab[1, 2::2] = 1.0 - c * fu[1:]
            ab[0, 3::2] = -c * fv[1:]
            ab[2, 2::2] = -c * gu[1:]
            ab[1, 3::2] = 1.0 - c * gv[1:]
            rhs = np.empty(2 * K)
            rhs[0::2] = -Ru
            rhs[1::2] = -Rv
            d = solve_banded((3, 3), ab, rhs, check_finite=False)
            u[1:-1] += d[0::2]
            v[1:-1] += d[1::2]
            sch = float(np.max(np.abs(d)))
        if not np.isfinite(sch):
            return u, v, it + 1, sch, False
        skala = max(1.0, float(np.max(np.abs(u))))
        if sch < tol * skala:
            return u, v, it + 1, sch, True
        # NACHTRAG-1: Rauschgrenze (Schritt < 1e-9 relativ und keine Halbierung mehr gegenueber dem Vorschritt)
        if it >= 6 and sch < 1e-9 * skala and sch > 0.5 * sch_vor:
            return u, v, it + 1, sch, True
        sch_vor = sch
    return u, v, maxit, sch, False


def laufe(modell, hp, w2a, u, v, ziele, maxschritt=0.005):
    """Fortsetzung in w2 von (w2a, u, v) nacheinander zu allen Zielen; Rueckgabe [(w2, u, v, iterationen)]."""
    it = 0
    out = []
    for z in ziele:
        while abs(z - w2a) > 0.0:
            schritt = z - w2a if abs(z - w2a) <= maxschritt else math.copysign(maxschritt, z - w2a)
            for _ in range(10):
                w2n = z if schritt == z - w2a else w2a + schritt
                un, vn, it, sch, ok = numerov_newton(modell, w2n, hp, u, v)
                if ok and float(np.min(un[1:-1])) > -1e-10 * float(np.max(un)):
                    break
                schritt *= 0.5
            else:
                raise RuntimeError('Fortsetzung gescheitert bei w2=%.8f' % w2n)
            w2a, u, v = w2n, un, vn
        out.append((z, u.copy(), None if v is None else v.copy(), it))
    return out


def _ext0(x):
    """Wert bei r = 0 einer geraden Funktion aus x[1], x[2], x[3] (4. Ordnung)."""
    return (15.0 * x[1] - 6.0 * x[2] + x[3]) / 10.0


def profil_groessen(modell, w2, hp, u, v):
    N = len(u) - 1
    r = np.arange(N + 1) * hp
    f = np.empty(N + 1)
    f[1:] = u[1:] / r[1:]
    f[0] = _ext0(f)
    S = f * f
    wS = np.ones(N + 1)
    wS[1:-1:2] = 4.0
    wS[2:-1:2] = 2.0
    wS *= hp / 3.0

    def abl(x):
        xe = np.concatenate([-x[2:0:-1], x, [0.0, 0.0]])
        return (xe[0:-4] - 8.0 * xe[1:-3] + 8.0 * xe[3:-1] - xe[4:]) / (12.0 * hp)

    up = abl(u)
    Tf = 4 * np.pi * np.sum(wS * (up - f) ** 2)
    N2 = 4 * np.pi * np.sum(wS * u * u)
    if modell == 'M1':
        Ur2 = u * u - S * u * u + 0.5 * S * S * u * u
        Tg = 0.0
        chi0 = 1.0
    else:
        wg = np.empty(N + 1)
        wg[1:] = v[1:] / r[1:]
        wg[0] = _ext0(wg)
        g = 1.0 + wg
        g2m1 = wg * (2.0 + wg)
        vp = abl(v)
        Tg = 4 * np.pi * np.sum(wS * 0.5 * (vp - wg) ** 2)
        Ur2 = 0.25 * g2m1 ** 2 * r * r + (1.0 + g * g) * u * u - S * u * u + 0.5 * S * S * u * u
        chi0 = float(g[0])
    Upot = 4 * np.pi * np.sum(wS * Ur2)
    T = Tf + Tg
    w = math.sqrt(w2)
    Q = 2.0 * w * N2
    E = w2 * N2 + T + Upot
    P = w2 * N2 - Upot
    k = int(np.argmax(f < 0.5 * f[0]))
    Rh = float(r[k - 1] + (0.5 * f[0] - f[k - 1]) * hp / (f[k] - f[k - 1]))
    knoten = int(np.sum(f[1:-1] < -1e-10 * f[0]))
    return dict(w2=float(w2), Q=float(Q), E=float(E), f0=float(f[0]), chi0=chi0, R_half=Rh,
                virial=float(abs(T - 3 * P) / T), knoten=knoten, f_R_rel=float(abs(f[-2]) / f[0]))


def tabellen(modell, hp, u, v):
    """Kanal-Koeffizienten relativ zur Schwelle m2: dVa = Va - m2, gs, (hh, dWc = Wc - m2)."""
    N = len(u) - 1
    r = np.arange(N + 1) * hp
    f = np.empty(N + 1)
    f[1:] = u[1:] / r[1:]
    f[0] = _ext0(f)
    S = f * f
    gs = S * (3.0 * S - 2.0)
    if modell == 'M1':
        return np.stack([-4.0 * S + 4.5 * S * S, gs])
    wg = np.empty(N + 1)
    wg[1:] = v[1:] / r[1:]
    wg[0] = _ext0(wg)
    g = 1.0 + wg
    g2m1 = wg * (2.0 + wg)
    return np.stack([g2m1 - 4.0 * S + 4.5 * S * S, gs, 2.0 * f * g, 3.0 * g2m1 + 2.0 * S])


def saat(modell, hp, N):
    import beutel_v2 as BV
    M = BV.Model(modell)
    Q = MODELLE[modell]['Qsaat']
    Gs = BV.Grid(0.04, 40.0)
    f, g = BV.initial_profile(M, Gs, Q)
    f, g, lam, ferr, nfl = BV.flow(M, Gs, f, g, Q)
    f, g, lam, it, err, ok = BV.newton_Q(M, Gs, f, g, lam, Q)
    r = np.arange(N + 1) * hp
    u = r * np.interp(r, Gs.r, f, right=0.0)
    u[-1] = 0.0
    v = None
    if modell == 'M2':
        v = r * (np.interp(r, Gs.r, g, right=1.0) - 1.0)
        v[-1] = 0.0
    info = dict(Q=Q, fluss_schritte=int(nfl), fluss_err=float(ferr), newton_ok=bool(ok), newton_err=float(err),
                w2=float(lam))
    un, vn, it2, sch, ok2 = numerov_newton(modell, float(lam), hp, u, v)
    if not ok2:
        raise RuntimeError('Saat: Numerov-Newton nicht konvergiert')
    info['numerov_it'] = it2
    return float(lam), un, vn, info


def umgittern(hp_alt, u, v, hp_neu, N_neu):
    r_alt = np.arange(len(u)) * hp_alt
    r = np.arange(N_neu + 1) * hp_neu
    f = np.empty(len(u))
    f[1:] = u[1:] / r_alt[1:]
    f[0] = _ext0(f)
    un = r * np.interp(r, r_alt, f, right=0.0)
    un[-1] = 0.0
    vn = None
    if v is not None:
        wg = np.empty(len(v))
        wg[1:] = v[1:] / r_alt[1:]
        wg[0] = _ext0(wg)
        vn = r * np.interp(r, r_alt, wg, right=0.0)
        vn[-1] = 0.0
    return un, vn


def profile_lauf(modell, aus):
    t0 = time.time()
    cfg = MODELLE[modell]
    zeilen = np.array(cfg['zeilen'])
    hp1 = STUFEN[1]
    Rprov = 90.0
    N1 = int(round(Rprov / hp1))
    w2s, u, v, sinfo = saat(modell, hp1, N1)
    log('Saat %s: %s' % (modell, json.dumps(sinfo)))
    unten = sorted([z for z in zeilen if z < w2s], reverse=True)
    oben = sorted([z for z in zeilen if z >= w2s])
    prov = {}
    for liste in (unten, oben):
        for (z, uu, vv, it) in laufe(modell, hp1, w2s, u, v, liste):
            prov[round(z, 6)] = (uu, vv)
    log('vorlaeufige Profile fertig %.1fs' % (time.time() - t0))
    gr = profil_groessen(modell, float(zeilen.min()), hp1, *prov[round(float(zeilen.min()), 6)])
    R_lin = 5.0 * math.ceil((gr['R_half'] + cfg['dR']) / 5.0)
    r_m = float(round(gr['R_half']) + 3)
    log('R_half(%.3f) = %.4f -> R_lin = %.1f, r_m = %.1f' % (zeilen.min(), gr['R_half'], R_lin, r_m))
    erg = dict(modell=modell, saat=sinfo, R_lin=R_lin, r_m=r_m, zeilen=zeilen.tolist(), stufen={})
    arrays = dict(zeilen=zeilen, R_lin=R_lin, r_m=r_m)
    for st in (1, 2):
        hp = STUFEN[st]
        N = int(round(R_lin / hp))
        UU, VV, gro = [], [], []
        for z in zeilen:
            uu, vv = prov[round(float(z), 6)]
            u0, v0 = umgittern(hp1, uu, vv, hp, N)
            un, vn, it, sch, ok = numerov_newton(modell, float(z), hp, u0, v0)
            if not ok:
                raise RuntimeError('Newton Stufe %d w2=%.4f' % (st, z))
            g = profil_groessen(modell, float(z), hp, un, vn)
            g['newton_it'] = it
            g['newton_schritt'] = sch
            gro.append(g)
            UU.append(un)
            if vn is not None:
                VV.append(vn)
        arrays['U_st%d' % st] = np.array(UU)
        if VV:
            arrays['V_st%d' % st] = np.array(VV)
        arrays['hp_st%d' % st] = hp
        erg['stufen'][st] = gro
        log('Stufe %d fertig %.1fs' % (st, time.time() - t0))
    # K2: Q, E auf beiden Stufen und gegen BEUTEL-1-Code (newton_w, dr 0,02 und 0,01, Richardson)
    if modell == 'M2':
        import beutel_v2 as BV
        M = BV.Model('M2')
        k2 = []
        hp = STUFEN[1]
        r1 = np.arange(int(round(R_lin / hp)) + 1) * hp
        for z in K2_ZEILEN:
            j = int(np.argmin(np.abs(zeilen - z)))
            g1, g2 = erg['stufen'][1][j], erg['stufen'][2][j]
            uu = arrays['U_st1'][j]
            vv = arrays['V_st1'][j]
            f = np.empty(len(uu)); f[1:] = uu[1:] / r1[1:]; f[0] = _ext0(f)
            wg = np.empty(len(vv)); wg[1:] = vv[1:] / r1[1:]; wg[0] = _ext0(wg)
            bt = {}
            for dr in (0.02, 0.01):
                Gb = BV.Grid(dr, R_lin)
                fb = np.interp(Gb.r, r1, f, right=0.0)
                gb = np.interp(Gb.r, r1, 1.0 + wg, right=1.0)
                fn, gn, it, err, ok = BV.newton_w(M, Gb, fb, gb, float(z))
                o = BV.observables(M, Gb, fn, gn, float(z))
                bt[dr] = dict(ok=bool(ok), Q=o['Q'], E=o['E'], chi0=o['chi0'], S0=o['S0'])
            QR = (4 * bt[0.01]['Q'] - bt[0.02]['Q']) / 3.0
            ER = (4 * bt[0.01]['E'] - bt[0.02]['E']) / 3.0
            k2.append(dict(w2=z, Q_st1=g1['Q'], Q_st2=g2['Q'], E_st1=g1['E'], E_st2=g2['E'],
                           dQ_rel=abs(g1['Q'] - g2['Q']) / g2['Q'], dE_rel=abs(g1['E'] - g2['E']) / g2['E'],
                           beutel=bt, Q_richardson=QR, E_richardson=ER,
                           dQ_beutel_rel=abs(g2['Q'] - QR) / QR, dE_beutel_rel=abs(g2['E'] - ER) / ER,
                           chi0_st2=g2['chi0'], f0_st2=g2['f0'], R_half_st2=g2['R_half']))
            log('K2 w2=%.3f: Q %.10g / %.10g (Beutel-R %.10g), E %.10g / %.10g (Beutel-R %.10g)' % (
                z, g1['Q'], g2['Q'], QR, g1['E'], g2['E'], ER))
        erg['K2'] = k2
    erg['sekunden'] = time.time() - t0
    np.savez(aus + '.npz', **arrays)
    speichere_json(aus + '.json', erg)
    log('profile fertig %.1fs' % (time.time() - t0))


# ------------------------------------------------------------------ linearisierte Kanaele
def _wr(UA, UpA, UB, UpB):
    return np.sum(UA * UpB - UpA * UB, axis=0)


def _gs(U, Up, ordnung, proj):
    """Orthonormierung im Zustandsraum (u, u') in fester Reihenfolge; proj: nur Anteile entfernen."""
    nch = U.shape[0]
    X = np.concatenate([U, Up], axis=0)
    Q = []
    for s in ordnung:
        x = X[..., s]
        for q in Q:
            x = x - np.sum(q * x, axis=0) * q
        x = x / np.sqrt(np.sum(x * x, axis=0))
        X[..., s] = x
        Q.append(x)
    for s in proj:
        x = X[..., s]
        for q in Q:
            x = x - np.sum(q * x, axis=0) * q
        X[..., s] = x
    return X[:nch], X[nch:]


def energien(modell, w2, rho):
    m2 = MODELLE[modell]['m2']
    w = np.sqrt(w2)
    k2 = (w + rho) ** 2 - m2
    kb2 = m2 - (w - rho) ** 2
    kc2 = m2 - rho ** 2 if MODELLE[modell]['nch'] == 3 else None
    return k2, kb2, kc2


class Lin:
    def __init__(self, modell, hp, R_lin, r_m):
        self.modell = modell
        self.nch = MODELLE[modell]['nch']
        self.hp = hp
        self.h = 2.0 * hp
        self.R = R_lin
        self.r_m = r_m
        self.N = int(round(R_lin / hp))
        self.i_m = int(round(r_m / hp))
        self.i_m2 = int(round((r_m + 4.0) / hp))
        self.gs_i = int(round(GS_DR / hp))

    def _acc(self, T, i, k2, kb2, kc2, U):
        dVa = T[0][i][:, None, None]
        gs = T[1][i][:, None, None]
        if self.nch == 2:
            return np.stack([(dVa - k2) * U[0] + gs * U[1], gs * U[0] + (dVa + kb2) * U[1]])
        hh = T[2][i][:, None, None]
        dWc = T[3][i][:, None, None]
        return np.stack([(dVa - k2) * U[0] + gs * U[1] + hh * U[2],
                         gs * U[0] + (dVa + kb2) * U[1] + hh * U[2],
                         hh * (U[0] + U[1]) + (dWc + kc2) * U[2]])

    def _rk4(self, T, i, di, h, k2, kb2, kc2, U, Up):
        a1 = self._acc(T, i, k2, kb2, kc2, U)
        U2 = U + 0.5 * h * Up
        P2 = Up + 0.5 * h * a1
        a2 = self._acc(T, i + di // 2, k2, kb2, kc2, U2)
        U3 = U + 0.5 * h * P2
        P3 = Up + 0.5 * h * a2
        a3 = self._acc(T, i + di // 2, k2, kb2, kc2, U3)
        U4 = U + h * P3
        P4 = Up + h * a3
        a4 = self._acc(T, i + di, k2, kb2, kc2, U4)
        return (U + (h / 6.0) * (Up + 2.0 * P2 + 2.0 * P3 + P4),
                Up + (h / 6.0) * (a1 + 2.0 * a2 + 2.0 * a3 + a4))

    def werte(self, T, k2, kb2, kc2):
        """T: (ntab, N+1, B); k2, kb2, kc2: (B, P). Rueckgabe: Groessen (B, P, ...)."""
        nch = self.nch
        B, P = k2.shape
        k2_ = k2[..., None]
        kb2_ = kb2[..., None]
        kc2_ = None if kc2 is None else kc2[..., None]
        h = self.h
        U = np.zeros((nch, B, P, nch))
        Up = np.zeros((nch, B, P, nch))
        for x in range(nch):
            Up[x, :, :, x] = 1.0
        ordY = list(range(1, nch)) + [0]
        sp = {}
        i = 0
        while i < self.i_m2:
            U, Up = self._rk4(T, i, 2, h, k2_, kb2_, kc2_, U, Up)
            i += 2
            if i % self.gs_i == 0:
                U, Up = _gs(U, Up, ordY, [])
            if i == self.i_m:
                sp['Ym'] = (U.copy(), Up.copy())
        sp['Ym2'] = (U, Up)
        nz = nch + 1
        Z = np.zeros((nch, B, P, nz))
        Zp = np.zeros((nch, B, P, nz))
        kap = [None, np.sqrt(kb2)] + ([np.sqrt(kc2)] if nch == 3 else [])
        for j in range(1, nch):
            amp = np.exp(-kap[j] * (self.R - self.r_m))
            Z[j, :, :, j - 1] = amp
            Zp[j, :, :, j - 1] = -kap[j] * amp
        Z[0, :, :, nch - 1] = 1.0
        Zp[0, :, :, nch] = 1.0
        ordZ = list(range(nch - 1))
        proj = [nch - 1, nch]
        i = self.N
        while i > self.i_m:
            Z, Zp = self._rk4(T, i, -2, -h, k2_, kb2_, kc2_, Z, Zp)
            i -= 2
            if i % self.gs_i == 0:
                Z, Zp = _gs(Z, Zp, ordZ, proj)
            if i == self.i_m2:
                sp['Zm2'] = (Z.copy(), Zp.copy())
        sp['Zm'] = (Z, Zp)
        a = self._auswertung(sp['Ym'], sp['Zm'], k2)
        b = self._auswertung(sp['Ym2'], sp['Zm2'], k2)
        a['phase_r2'] = np.abs(np.angle(a['W1'] * np.conj(b['W1'])))
        return a

    def _auswertung(self, Yp, Zp_, k2):
        U, Up = Yp
        Z, Zp = Zp_
        nch = self.nch
        G = np.empty(U.shape[1:3] + (nch, nch - 1))
        for x in range(nch):
            for j in range(nch - 1):
                G[..., x, j] = _wr(U[..., x], Up[..., x], Z[..., j], Zp[..., j])
        P1 = np.stack([_wr(U[..., x], Up[..., x], Z[..., nch - 1], Zp[..., nch - 1]) for x in range(nch)], -1)
        P2 = np.stack([_wr(U[..., x], Up[..., x], Z[..., nch], Zp[..., nch]) for x in range(nch)], -1)
        Pi = np.sqrt(k2)[..., None] * P2 - 1j * P1
        if nch == 2:
            c = np.stack([G[..., 1, 0], -G[..., 0, 0]], -1)
            ma = G[..., 1, 0]
            s = G[..., 0, 0]
            eta = np.ones(G.shape[:2] + (1,))
        else:
            c0 = G[..., 1, 0] * G[..., 2, 1] - G[..., 1, 1] * G[..., 2, 0]
            c1 = -(G[..., 0, 0] * G[..., 2, 1] - G[..., 0, 1] * G[..., 2, 0])
            c2 = G[..., 0, 0] * G[..., 1, 1] - G[..., 0, 1] * G[..., 1, 0]
            c = np.stack([c0, c1, c2], -1)
            ma = c0
            n1 = np.hypot(G[..., 1, 0], G[..., 1, 1])
            n2 = np.hypot(G[..., 2, 0], G[..., 2, 1])
            use1 = n1 >= n2
            e0 = np.where(use1, -G[..., 1, 1] / n1, -G[..., 2, 1] / n2)
            e1 = np.where(use1, G[..., 1, 0] / n1, G[..., 2, 0] / n2)
            eta = np.stack([e0, e1], -1)
            s = G[..., 0, 0] * e0 + G[..., 0, 1] * e1
        W1 = np.sum(c * Pi, -1)
        nY = [np.sqrt(np.sum(U[..., x] ** 2 + Up[..., x] ** 2, axis=0)) for x in range(nch)]
        isoY = np.zeros(ma.shape)
        for x in range(nch):
            for y in range(x + 1, nch):
                isoY = np.maximum(isoY, np.abs(_wr(U[..., x], Up[..., x], U[..., y], Up[..., y])) / (nY[x] * nY[y]))
        nZ = [np.sqrt(np.sum(Z[..., j] ** 2 + Zp[..., j] ** 2, axis=0)) for j in range(nch + 1)]
        isoZ = np.zeros(ma.shape)
        for j in range(nch - 1):
            for l in range(j + 1, nch + 1):
                isoZ = np.maximum(isoZ, np.abs(_wr(Z[..., j], Zp[..., j], Z[..., l], Zp[..., l])) / (nZ[j] * nZ[l]))
        wz12 = np.abs(_wr(Z[..., nch - 1], Zp[..., nch - 1], Z[..., nch], Zp[..., nch]) - 1.0)
        return dict(G=G, ma=ma, s=s, eta=eta, W1=W1, c=c, isoY=isoY, isoZ=isoZ, wz12=wz12)


class ProfilCache:
    def __init__(self, modell, stufe, npz):
        d = np.load(npz)
        self.modell = modell
        self.hp = float(d['hp_st%d' % stufe])
        self.R_lin = float(d['R_lin'])
        self.r_m = float(d['r_m'])
        self.zeilen = np.array(d['zeilen'], float)
        self.U = d['U_st%d' % stufe]
        self.V = d['V_st%d' % stufe] if modell == 'M2' else None
        self.tab = {}
        self.info = {}

    def profil(self, w2):
        j = int(np.argmin(np.abs(self.zeilen - w2)))
        u = self.U[j]
        v = None if self.V is None else self.V[j]
        if abs(self.zeilen[j] - w2) < 1e-13:
            return u, v
        out = laufe(self.modell, self.hp, float(self.zeilen[j]), u, v, [float(w2)])
        return out[0][1], out[0][2]

    def hole(self, w2):
        key = round(float(w2), 13)
        if key not in self.tab:
            u, v = self.profil(float(w2))
            self.tab[key] = tabellen(self.modell, self.hp, u, v)
            self.info[key] = profil_groessen(self.modell, float(w2), self.hp, u, v)
        return self.tab[key]


def punkte(modell, lin, cache, w2, rho):
    """Auswertung an Einzelpunkten (je Punkt ein eigenes Profil)."""
    w2 = np.asarray(w2, float)
    rho = np.asarray(rho, float)
    T = np.stack([cache.hole(x) for x in w2], axis=-1)
    k2, kb2, kc2 = energien(modell, w2[:, None], rho[:, None])
    res = lin.werte(T, k2, kb2, kc2)
    return {k: v[:, 0] for k, v in res.items()}


def e1_grenzen(modell, w2):
    w = math.sqrt(w2)
    if modell == 'M1':
        return 1.0 - w, 1.0 + w
    return math.sqrt(2.0) - w, math.sqrt(2.0)


def rho_gitter(modell, w2):
    lo, hi = e1_grenzen(modell, w2)
    rp = np.array(RAND_PUNKTE)
    return np.concatenate([lo + rp, np.linspace(lo + RAND, hi - RAND, NRHO), (hi - rp)[::-1]])


def illinois(f_eval, rl, rr, fl, fr, iters=30, tol=1e-11):
    seite = np.zeros(len(rl), int)
    for _ in range(iters):
        rm = (rl * fr - rr * fl) / (fr - fl)
        gm = f_eval(rm)
        links = np.sign(gm) == np.sign(fl)
        rl = np.where(links, rm, rl)
        fl = np.where(links, gm, fl)
        rr = np.where(~links, rm, rr)
        fr = np.where(~links, gm, fr)
        fr = np.where(links & (seite == 1), fr * 0.5, fr)
        fl = np.where(~links & (seite == -1), fl * 0.5, fl)
        seite = np.where(links, 1, -1)
        if np.max(rr - rl) < tol:
            break
    return (rl * fr - rr * fl) / (fr - fl), rr - rl


def scan(modell, stufe, npz, ausdir, w2liste, nb=10):
    cache = ProfilCache(modell, stufe, npz)
    lin = Lin(modell, cache.hp, cache.R_lin, cache.r_m)
    os.makedirs(ausdir, exist_ok=True)
    for j0 in range(0, len(w2liste), nb):
        t0 = time.time()
        wb = np.array(w2liste[j0:j0 + nb], float)
        T = np.stack([cache.hole(x) for x in wb], axis=-1)
        rh = np.stack([rho_gitter(modell, x) for x in wb])
        k2, kb2, kc2 = energien(modell, wb[:, None], rh)
        e1a = (k2, kb2, kc2)
        res = lin.werte(T, k2, kb2, kc2)
        ma = res['ma']
        jb, jr = np.nonzero(np.sign(ma[:, :-1]) * np.sign(ma[:, 1:]) < 0)
        if len(jb):
            Tb = T[:, :, jb]
            wbb = wb[jb]

            def fe(r):
                kk = energien(modell, wbb[:, None], r[:, None])
                return lin.werte(Tb, *kk)['ma'][:, 0]

            wur, br = illinois(fe, rh[jb, jr], rh[jb, jr + 1], ma[jb, jr], ma[jb, jr + 1])
            kk = energien(modell, wbb[:, None], wur[:, None])
            rz = {k: v[:, 0] for k, v in lin.werte(Tb, *kk).items()}
        dt = time.time() - t0
        for b, w2 in enumerate(wb):
            m = np.nonzero(jb == b)[0]
            info = cache.info[round(float(w2), 13)]
            e1 = dict(k2_min=float(np.min(k2[b])), kb2_min=float(np.min(kb2[b])),
                      kc2_min=None if kc2 is None else float(np.min(kc2[b])))
            d = dict(modell=modell, stufe=stufe, w2=float(w2), hp=cache.hp, R_lin=cache.R_lin, r_m=cache.r_m,
                     profil=info, e1=e1, rho=rh[b].tolist(), ma=ma[b].tolist(),
                     W1_re=res['W1'][b].real.tolist(), W1_im=res['W1'][b].imag.tolist(),
                     isoY_max=float(np.max(res['isoY'][b])), isoZ_max=float(np.max(res['isoZ'][b])),
                     wz12_max=float(np.max(res['wz12'][b])), phase_r2_max=float(np.max(res['phase_r2'][b])),
                     nullstellen=[], sekunden_block=dt)
            if len(m):
                d['nullstellen'] = wur[m].tolist()
                d['klammer'] = br[m].tolist()
                d['s'] = rz['s'][m].tolist()
                d['eta'] = rz['eta'][m].tolist()
                d['ma_an_null'] = rz['ma'][m].tolist()
                d['W1_an_null'] = [[float(z.real), float(z.imag)] for z in rz['W1'][m]]
                d['G_an_null'] = rz['G'][m].tolist()
            fn = os.path.join(ausdir, 'zeile-%s-st%d-w2_%.4f.json' % (modell, stufe, w2))
            speichere_json(fn, d)
            log('zeile w2=%.4f st=%d null=%d s=%s isoY=%.1e isoZ=%.1e wz12=%.1e ph2=%.1e chi0=%.3e' % (
                w2, stufe, len(m), ''.join('+' if x > 0 else '-' for x in d.get('s', [])), d['isoY_max'],
                d['isoZ_max'], d['wz12_max'], d['phase_r2_max'], info['chi0']))
        log('block %d zeilen %.1fs' % (len(wb), dt))


# ------------------------------------------------------------------ Kandidaten
def _orient(eta):
    eta = np.asarray(eta, float)
    i = int(np.argmax(np.abs(eta)))
    return 1.0 if eta[i] >= 0 else -1.0


def detektoren(zeilen):
    """zeilen: dicts einer Stufe, nach w2 sortiert. Detektor 1 (s-Wechsel auf gepaarten Nullstellen mit
    stetig ausgerichtetem eta) und Detektor 2 (Zellen-Umlauf von W1 aus den Eckwerten)."""
    kand, paare = [], []
    vor_eta = None
    for j, A in enumerate(zeilen):
        ra = np.array(A['nullstellen'])
        sa = np.array(A.get('s', []))
        ea = [np.array(e) for e in A.get('eta', [])]
        flip = np.ones(len(ra))
        if j == 0:
            for i in range(len(ra)):
                flip[i] = _orient(ea[i])
        else:
            P = zeilen[j - 1]
            rp = np.array(P['nullstellen'])
            for i in range(len(ra)):
                flip[i] = _orient(ea[i])
                if len(rp):
                    k = int(np.argmin(np.abs(rp - ra[i])))
                    i2 = int(np.argmin(np.abs(ra - rp[k])))
                    if i2 == i and abs(rp[k] - ra[i]) <= 0.03:
                        dot = float(np.dot(ea[i], vor_eta[k]))
                        flip[i] = 1.0 if dot >= 0 else -1.0
                        so_alt = P['s_orient'][k]
                        so_neu = flip[i] * sa[i]
                        wechsel = bool(np.sign(so_alt) != np.sign(so_neu))
                        unsicher = bool(abs(dot) < 0.5)
                        paare.append(dict(w2a=P['w2'], w2b=A['w2'], ra=float(rp[k]), rb=float(ra[i]),
                                          sa=float(so_alt), sb=float(so_neu), dot=dot, wechsel=wechsel,
                                          unsicher=unsicher))
                        if wechsel or unsicher:
                            t = abs(so_alt) / (abs(so_alt) + abs(so_neu)) if wechsel else 0.5
                            kand.append(dict(w2=P['w2'] + t * (A['w2'] - P['w2']),
                                             rho=float(rp[k] + t * (ra[i] - rp[k])),
                                             quelle='s-wechsel' if wechsel else 'eta-unsicher'))
        A['s_orient'] = (flip * sa).tolist() if len(ra) else []
        vor_eta = [flip[i] * ea[i] for i in range(len(ra))]
        if j > 0:
            P = zeilen[j - 1]
            WA = np.array(P['W1_re']) + 1j * np.array(P['W1_im'])
            WB = np.array(A['W1_re']) + 1j * np.array(A['W1_im'])
            wrap = lambda x: (x + np.pi) % (2 * np.pi) - np.pi
            d1 = wrap(np.angle(WA[1:]) - np.angle(WA[:-1]))
            d2 = wrap(np.angle(WB[1:]) - np.angle(WA[1:]))
            d3 = wrap(np.angle(WB[:-1]) - np.angle(WB[1:]))
            d4 = wrap(np.angle(WA[:-1]) - np.angle(WB[:-1]))
            n = np.rint((d1 + d2 + d3 + d4) / (2 * np.pi)).astype(int)
            for i in np.nonzero(n != 0)[0]:
                kand.append(dict(w2=0.5 * (P['w2'] + A['w2']),
                                 rho=0.25 * (P['rho'][i] + P['rho'][i + 1] + A['rho'][i] + A['rho'][i + 1]),
                                 quelle='zelle', n_zelle=int(n[i])))
    return kand, paare


def _in_e1(modell, w2, rho, rand=1e-7):
    lo, hi = e1_grenzen(modell, w2)
    return lo + rand < rho < hi - rand


def newton2d(modell, lin, cache, w2, rho, iters=15, dw=1e-6, dr=1e-6):
    w2 = np.array(w2, float)
    rho = np.array(rho, float)
    K = len(w2)
    verlauf = []
    ok = np.zeros(K, bool)
    for it in range(iters):
        W2 = np.concatenate([w2, w2 + dw, w2])
        RH = np.concatenate([rho, rho, rho + dr])
        W = punkte(modell, lin, cache, W2, RH)['W1']
        g0 = W[:K]
        Jw = (W[K:2 * K] - g0) / dw
        Jr = (W[2 * K:] - g0) / dr
        a11, a12, a21, a22 = Jw.real, Jr.real, Jw.imag, Jr.imag
        det = a11 * a22 - a12 * a21
        dx = -(a22 * g0.real - a12 * g0.imag) / det
        dy = -(-a21 * g0.real + a11 * g0.imag) / det
        dx = np.where(np.isfinite(dx), dx, 0.0)
        dy = np.where(np.isfinite(dy), dy, 0.0)
        schritt = np.maximum(np.abs(dx), np.abs(dy))
        fak = np.where(schritt > 0.01, 0.01 / np.maximum(schritt, 1e-300), 1.0)
        w2n = w2 + fak * dx
        rhon = rho + fak * dy
        for k in range(K):
            lo, hi = e1_grenzen(modell, w2n[k])
            rhon[k] = min(max(rhon[k], lo + 1e-6), hi - 1e-6)
        w2, rho = w2n, rhon
        verlauf.append(schritt.tolist())
        ok = schritt < 1e-11
        if ok.all():
            break
    return w2, rho, ok, verlauf


def rechteck(t, w2c, rc):
    t = np.asarray(t, float)
    k = np.floor(t).astype(int) % 4
    x = t - np.floor(t)
    s = -1.0 + 2.0 * x
    e = np.ones_like(s)
    w = np.select([k == 0, k == 1, k == 2, k == 3], [s, e, -s, -e])
    r = np.select([k == 0, k == 1, k == 2, k == 3], [-e, s, e, -s])
    return w2c + HALB * w, rc + HALB * r


def umlaeufe(modell, lin, cache, w2c, rc):
    """Phasenumlauf von W1 gegen den Uhrzeigersinn in (w2, rho), adaptiv bis aufgeloest, hoechstens VERF_RUNDEN."""
    K = len(w2c)
    werte = [dict() for _ in range(K)]
    neu = [np.arange(4 * NKANTE) / NKANTE for _ in range(K)]
    erg = [None] * K
    e1min = [np.inf] * K
    for rnd in range(VERF_RUNDEN + 1):
        W2, RH, wer = [], [], []
        for k in range(K):
            if len(neu[k]):
                w, r = rechteck(neu[k], w2c[k], rc[k])
                W2.append(w)
                RH.append(r)
                wer += [(k, t) for t in neu[k].tolist()]
                k2, kb2, kc2 = energien(modell, w, r)
                mins = [np.min(k2), np.min(kb2)] + ([] if kc2 is None else [np.min(kc2)])
                e1min[k] = min(e1min[k], float(min(mins)))
        if wer:
            W = punkte(modell, lin, cache, np.concatenate(W2), np.concatenate(RH))['W1']
            for (k, t), z in zip(wer, W.tolist()):
                werte[k][t] = z
        for k in range(K):
            tt = np.array(sorted(werte[k]))
            z = np.array([werte[k][t] for t in tt])
            ph = np.angle(z)
            d = (np.roll(ph, -1) - ph + np.pi) % (2 * np.pi) - np.pi
            groesst = float(np.max(np.abs(d)))
            n = float(np.sum(d) / (2 * np.pi))
            erg[k] = dict(umlauf=int(round(n)), umlauf_roh=n, groesster_sprung=groesst, punkte=int(len(tt)),
                          aufgeloest=bool(groesst < SPRUNG), min_absW=float(np.min(np.abs(z))),
                          max_absW=float(np.max(np.abs(z))), runden=rnd, e1_min_schwelle=e1min[k])
            tneu = []
            if rnd < VERF_RUNDEN:
                for i in np.nonzero(np.abs(d) >= SPRUNG)[0]:
                    t1 = tt[i]
                    t2 = tt[(i + 1) % len(tt)]
                    if t2 <= t1:
                        t2 += 4.0
                    tneu.append((0.5 * (t1 + t2)) % 4.0)
            neu[k] = np.array(tneu)
        if all(len(x) == 0 for x in neu):
            break
    return erg


def kand_lauf(modell, stufe, npz, ausdatei, dateien):
    t0 = time.time()
    cache = ProfilCache(modell, stufe, npz)
    lin = Lin(modell, cache.hp, cache.R_lin, cache.r_m)
    alle = [json.load(open(f)) for f in dateien]
    kand, paare_alle = [], {}
    for st in sorted(set(z['stufe'] for z in alle)):
        zs = sorted([z for z in alle if z['stufe'] == st], key=lambda d: d['w2'])
        k, p = detektoren(zs)
        for x in k:
            x['stufe_detektor'] = st
        kand += k
        paare_alle[st] = p
        log('Stufe %d: %d Zeilen, %d Rohkandidaten' % (st, len(zs), len(k)))
    uniq = []
    for k in kand:
        tr = [u for u in uniq if abs(k['w2'] - u['w2']) < 2e-3 and abs(k['rho'] - u['rho']) < 2e-3]
        if tr:
            tag = '%s@st%d' % (k['quelle'], k['stufe_detektor'])
            if tag not in tr[0]['quellen']:
                tr[0]['quellen'].append(tag)
        else:
            u = dict(k)
            u['quellen'] = ['%s@st%d' % (k['quelle'], k['stufe_detektor'])]
            uniq.append(u)
    log('Kandidaten nach Zusammenlegen: %d %s' % (len(uniq), json.dumps(uniq)))
    erg = []
    if uniq:
        w2l, rl, ok, verl = newton2d(modell, lin, cache, [u['w2'] for u in uniq], [u['rho'] for u in uniq])
        log('Newton fertig %.1fs' % (time.time() - t0))
        zmin, zmax = min(MODELLE[modell]['zeilen']), max(MODELLE[modell]['zeilen'])
        for i in range(len(uniq)):
            e = dict(start=uniq[i], w2=float(w2l[i]), rho=float(rl[i]), konvergiert=bool(ok[i]),
                     newton=[v[i] for v in verl], im_fenster=bool(zmin - 1e-9 <= w2l[i] <= zmax + 1e-9),
                     in_e1=_in_e1(modell, float(w2l[i]), float(rl[i])), doppelt_von=None)
            for j, f in enumerate(erg):
                if f['konvergiert'] and e['konvergiert'] and abs(f['w2'] - e['w2']) < 1e-7 and \
                        abs(f['rho'] - e['rho']) < 1e-7:
                    e['doppelt_von'] = j
                    break
            erg.append(e)
        # Umlauf: konvergierte, eindeutige Punkte um den Newton-Punkt; sonst um den Startpunkt
        idx = [i for i, e in enumerate(erg) if e['doppelt_von'] is None]
        zc = [(erg[i]['w2'], erg[i]['rho']) if erg[i]['konvergiert'] else (uniq[i]['w2'], uniq[i]['rho'])
              for i in idx]
        if idx:
            ul = umlaeufe(modell, lin, cache, np.array([z[0] for z in zc]), np.array([z[1] for z in zc]))
            pk = punkte(modell, lin, cache, np.array([z[0] for z in zc]), np.array([z[1] for z in zc]))
            for j, i in enumerate(idx):
                erg[i]['umlauf_um'] = 'newton' if erg[i]['konvergiert'] else 'start'
                erg[i].update(ul[j])
                erg[i]['W1_am_punkt'] = [float(pk['W1'][j].real), float(pk['W1'][j].imag)]
                erg[i]['ma_am_punkt'] = float(pk['ma'][j])
                inf = cache.info[round(float(zc[j][0]), 13)]
                erg[i]['chi0'] = inf['chi0']
                erg[i]['profil'] = inf
        for i, e in enumerate(erg):
            log('kand %d %s' % (i, json.dumps({k: v for k, v in e.items() if k not in ('newton', 'profil')})))
    out = dict(modell=modell, stufe=stufe, dateien=len(dateien), paare=paare_alle, kandidaten=erg,
               R_lin=cache.R_lin, r_m=cache.r_m, sekunden=time.time() - t0)
    speichere_json(ausdatei, out)
    log('kand fertig %.1fs' % (time.time() - t0))


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'profile':
        profile_lauf(sys.argv[2], sys.argv[3])
    elif cmd == 'scan':
        scan(sys.argv[2], int(sys.argv[3]), sys.argv[4], sys.argv[5], [float(x) for x in sys.argv[6:]])
    elif cmd == 'kand':
        kand_lauf(sys.argv[2], int(sys.argv[3]), sys.argv[4], sys.argv[5], sys.argv[6:])
    else:
        raise SystemExit('unbekannt: ' + cmd)
