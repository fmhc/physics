# -*- coding: utf-8 -*-
"""Komplexes Q-Ball-Feld auf den Ecken (netzgpu), Papier I wie SCHWERE-MASSE-V.

Q-Ball-Einheiten (Feldmasse m = 1); h = Finn-Kante l_P in Q-Einheiten; l_P = a / (2 sqrt 2).
Sterne in Q-Einheiten: *0 h^3 / l_P^3, *1 h / l_P (aus den a-Sternen des Netzes).
Mit Takt N (je Ecke) und metrischer Kopplung (Sterne aus den Kantenlaengen):
  L = sum_v (*0_v / N_v) |dphi/dt|^2 - sum_e (N_e *1_e) |d phi|_e^2 - sum_v N_v *0_v U(|phi_v|^2),  U(S) = S - S^2 + S^3/2
  H = sum m |phi'|^2 + sum k |d phi|^2 + sum n U = sum_v N_v h_v (der Takt multipliziert die ganze Energiedichte)
  Q = 2 sum_v m_v Im(conj(phi) phi'),  m = *0/N, k = N_e *1, n = N *0.
Stationaerer Gitter-Ball: Minimum von E_Q[f] = Q^2/(4 sum *0 f^2) + sum *1 (d f)^2 + sum *0 U(f^2) bei festem Q
(wie sm.modus_qball), hier mit torch L-BFGS auf der GPU in u = sqrt(*0) f.
Spannung je Ecke s_v = 3 K_v - 3 V_v - 1/2 sum G_e (SCHWERE-MASSE-V), aktive Masse metrisch E + S.
"""
import math

import numpy as np
import torch

from . import kopplung

BETA = 0.5
LP = 1.0 / (2.0 * math.sqrt(2.0))


def U(S):
    return S - S ** 2 + BETA * S ** 3


def Up(S):
    return 1.0 - 2.0 * S + 3.0 * BETA * S ** 2


def qball_kont(om, beta=BETA, rmax=80.0, nr=80001):
    """Kontinuums-Q-Ball (Schiessen, Bisektion), Kopie von sm.qball_kont (SCHWERE-MASSE-V), nur Profil und Kennzahlen."""
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
    return {'om': om, 'f0': f0, 'r': r_all, 'f': f_all, 'E': E, 'Q': Q, 'K': K, 'G': G, 'V': V,
            'bind': (Q - E) / E, 'S_rel': (3 * K - G - 3 * V) / E}


class Skalar:
    def __init__(self, netz, h=1.0, N=None, l=None, w=None):
        self.netz, self.h = netz, h
        st = netz.sterne(l=l, w=w)
        self.st = st
        self.s0 = st['s0'] / LP ** 3 * h ** 3
        self.s1 = st['s1'] / LP * h
        if N is None:
            N = torch.ones(netz.N_e, dtype=netz.dtype, device=netz.device)
        self.N = N
        self.m = self.s0 / N
        self.k = self.s1 * kopplung.takt_kante(netz, N)
        self.n = self.s0 * N
        self.d0 = netz.d0
        self.d0t = netz.d0.transpose(0, 1).to_sparse_csr()
        self.a, self.b = netz.kanten[:, 0], netz.kanten[:, 1]

    def lage_Q(self):
        return self.netz.x / LP * self.h

    def abstand_Q(self, x0_a):
        d = self.netz.ecken_minbild(x0_a)
        return torch.linalg.norm(d, dim=1) / LP * self.h

    # ------------------------------------------------------------------ stationaerer Ball bei festem Q (N = 1)
    def relaxieren(self, f0, Q, maxiter=3000, gtol=1e-9, s0=None, s1=None):
        s0 = self.s0 if s0 is None else s0
        s1 = self.s1 if s1 is None else s1
        w = torch.sqrt(s0)
        u = (w * f0).clone().requires_grad_(False)
        d0, d0t = self.d0, self.d0t

        def fg(u):
            f = u / w
            I2 = (u * u).sum()
            df = d0 @ f
            S = f * f
            E = Q * Q / (4 * I2) + (s1 * df * df).sum() + (s0 * U(S)).sum()
            gf = 2.0 * (d0t @ (s1 * df)) + 2.0 * s0 * Up(S) * f
            gu = gf / w - (Q * Q / (2 * I2 * I2)) * u
            return E, gu
        # L-BFGS (eigene Fassung, Armijo-Rueckschritt), alles auf der GPU
        m_hist = 30
        S_, Y_ = [], []
        E, g = fg(u)
        it = 0
        gn0 = float(torch.linalg.norm(g))
        for it in range(maxiter):
            q = g.clone()
            al = []
            for s_, y_ in zip(reversed(S_), reversed(Y_)):
                rho = 1.0 / (y_ * s_).sum()
                a_ = rho * (s_ * q).sum()
                q = q - a_ * y_
                al.append((rho, a_))
            if Y_:
                gam = (S_[-1] * Y_[-1]).sum() / (Y_[-1] * Y_[-1]).sum()
            else:
                gam = 1.0 / max(gn0, 1e-30) * 1e-1
            r = gam * q
            for (s_, y_), (rho, a_) in zip(zip(S_, Y_), reversed(al)):
                b_ = rho * (y_ * r).sum()
                r = r + s_ * (a_ - b_)
            p = -r
            gp = float((g * p).sum())
            if gp >= 0:
                p = -g
                gp = float((g * p).sum())
                S_, Y_ = [], []
            t = 1.0
            for _ in range(40):
                un = u + t * p
                En, gnw = fg(un)
                if float(En) <= float(E) + 1e-4 * t * gp:
                    break
                t *= 0.5
            s_ = un - u
            y_ = gnw - g
            if float((s_ * y_).sum()) > 1e-30:
                S_.append(s_)
                Y_.append(y_)
                if len(S_) > m_hist:
                    S_.pop(0)
                    Y_.pop(0)
            u, E, g = un, En, gnw
            I2 = float((u * u).sum())
            om = Q / (2 * I2)
            res = float(torch.linalg.norm(g)) / float(torch.linalg.norm(2 * om * om * u))
            if res < gtol:
                break
        f = u / w
        I2 = float((u * u).sum())
        om = Q / (2 * I2)
        return f, {'iter': it + 1, 'E': float(E), 'om': om, 'resid_rel': res}

    def teile(self, f, om, s0=None, s1=None):
        s0 = self.s0 if s0 is None else s0
        s1 = self.s1 if s1 is None else s1
        df = self.d0 @ f
        Kv = om ** 2 * s0 * f * f
        Vv = s0 * U(f * f)
        Ge = s1 * df * df
        Gv = torch.zeros_like(f)
        Gv.index_add_(0, self.a, 0.5 * Ge)
        Gv.index_add_(0, self.b, 0.5 * Ge)
        K, G, V = float(Kv.sum()), float(Ge.sum()), float(Vv.sum())
        return {'K': K, 'G': G, 'V': V, 'E': K + G + V, 'S': 3 * K - G - 3 * V, 'Q': 2 * om * float((s0 * f * f).sum()),
                'm': Kv + Vv + Gv, 's': 3 * Kv - 3 * Vv - Gv}

    # ------------------------------------------------------------------ Dynamik (komplex, Takt, Laengen)
    def kraft(self, phi):
        lap = self.d0t @ (self.k.to(phi.dtype) * (self.d0 @ phi)) if False else self._lap(phi)
        S = (phi.real ** 2 + phi.imag ** 2)
        return -(lap + (self.n * Up(S)) * phi)

    def _lap(self, phi):
        re = self.d0t @ (self.k * (self.d0 @ phi.real.contiguous()))
        im = self.d0t @ (self.k * (self.d0 @ phi.imag.contiguous()))
        return torch.complex(re, im)

    def energie(self, phi, pi_):
        dre = self.d0 @ phi.real.contiguous()
        dim = self.d0 @ phi.imag.contiguous()
        S = phi.real ** 2 + phi.imag ** 2
        return float((pi_.abs() ** 2 / self.m).sum() + (self.k * (dre ** 2 + dim ** 2)).sum() + (self.n * U(S)).sum())

    def energie_ecke(self, phi, pi_):
        dre = self.d0 @ phi.real.contiguous()
        dim = self.d0 @ phi.imag.contiguous()
        Ge = self.k * (dre ** 2 + dim ** 2)
        e = pi_.abs() ** 2 / self.m + self.n * U(phi.real ** 2 + phi.imag ** 2)
        e = e.clone()
        e.index_add_(0, self.a, 0.5 * Ge)
        e.index_add_(0, self.b, 0.5 * Ge)
        return e

    def ladung(self, phi, pi_):
        return float(2.0 * (phi.conj() * pi_).imag.sum())

    def omega_max(self, iters=60):
        x = torch.randn(self.netz.N_e, dtype=self.netz.dtype, device=self.netz.device)
        lam = 0.0
        for _ in range(iters):
            y = (self.d0t @ (self.k * (self.d0 @ x)) + 1.0 * self.n * x) / self.m
            lam = float((x * y * self.m).sum() / (x * x * self.m).sum())
            x = y / torch.linalg.norm(y)
        return math.sqrt(lam * 1.05)

    def schritt(self, phi, pi_, dt, n=1):
        """Stoermer-Verlet; pi = m dphi/dt (komplex). Erhaelt Q exakt (bilinear)."""
        F = self.kraft(phi)
        for _ in range(n):
            pi_ = pi_ + 0.5 * dt * F
            phi = phi + dt * pi_ / self.m
            F = self.kraft(phi)
            pi_ = pi_ + 0.5 * dt * F
        return phi, pi_
