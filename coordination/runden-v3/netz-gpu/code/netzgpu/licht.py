# -*- coding: utf-8 -*-
"""DEC-Maxwell auf dem Netz mit Takt und Laengen (netzgpu).

A auf den Kanten (1-Form), F = d1 A auf den Dreiecken. Hamiltonform (wie LICHT-ABLENKUNG-V, Takt je Kante/Dreieck):
  H = 1/2 sum_e P_e^2 / m_e + 1/2 sum_f k_f (d1 A)_f^2,  m_e = *1_e / N_e,  k_f = N_f *2_f
  dA/dt = P / m,  dP/dt = -d1^T (k (d1 A)),  Gauss: d0^T P = const (bei Stoermer-Verlet exakt, da d1 d0 = 0).
Sterne aus den Kantenlaengen (Regge-Einbettung je Tetraeder) und Gewichten, Takt N je Ecke. Ohne Masse N = 1 und
flache Laengen: Licht auf V mit c = 1 im Langwellengrenzfall (Nachweis ueber diagnose.bloch_licht).
"""
import math

import torch

from . import kopplung


class Licht:
    def __init__(self, netz, N=None, l=None, w=None):
        self.netz = netz
        st = netz.sterne(l=l, w=w)
        self.st = st
        if N is None:
            N = torch.ones(netz.N_e, dtype=netz.dtype, device=netz.device)
        self.N = N
        self.m = st['s1'] / kopplung.takt_kante(netz, N)
        self.k = st['s2'] * kopplung.takt_dreieck(netz, N)
        self.d1 = netz.d1
        self.d1t = netz.d1.transpose(0, 1).to_sparse_csr()
        self.d0t = netz.d0.transpose(0, 1).to_sparse_csr()

    def kraft(self, A):
        return -(self.d1t @ (self.k * (self.d1 @ A)))

    def energie(self, A, P):
        F = self.d1 @ A
        return float(0.5 * (P * P / self.m).sum() + 0.5 * (self.k * F * F).sum())

    def energie_ecke(self, A, P):
        """Energiedichte je Ecke: Kantenanteil zu gleichen Teilen auf 2 Ecken, Dreiecksanteil auf 3 Ecken; durch *0."""
        n = self.netz
        eE = 0.5 * P * P / self.m
        F = self.d1 @ A
        eB = 0.5 * self.k * F * F
        e = torch.zeros(n.N_e, dtype=n.dtype, device=n.device)
        e.index_add_(0, n.kanten[:, 0], 0.5 * eE)
        e.index_add_(0, n.kanten[:, 1], 0.5 * eE)
        for j in range(3):
            e.index_add_(0, n.dreiecke[:, j], eB / 3.0)
        return e

    def gauss(self, P):
        return self.d0t @ P

    def omega_max(self, iters=60):
        x = torch.randn(self.netz.N_k, dtype=self.netz.dtype, device=self.netz.device)
        lam = 0.0
        for _ in range(iters):
            y = -self.kraft(x) / self.m
            lam = float((x * y * self.m).sum() / (x * x * self.m).sum())
            x = y / torch.linalg.norm(y)
        return math.sqrt(lam * 1.02)

    def schritt(self, A, P, dt, n=1):
        """Stoermer-Verlet (kick-drift-kick), n Schritte."""
        F = self.kraft(A)
        for _ in range(n):
            P = P + 0.5 * dt * F
            A = A + dt * P / self.m
            F = self.kraft(A)
            P = P + 0.5 * dt * F
        return A, P

    def gauss_projektion(self, P, tol=1e-13):
        """Entfernt den Laengsanteil von P (Metrik 1/m): P - m d0 lam mit d0^T m d0 lam = d0^T P."""
        n = self.netz
        rhs = self.d0t @ P
        ap = lambda x: self.d0t @ (self.m * (n.d0 @ x))
        lam, info = kopplung.cg(ap, rhs, tol=tol, proj=lambda r: r - r.mean())
        return P - self.m * (n.d0 @ lam), info


def feld_auf_kanten(netz, feld):
    """Linienintegral eines glatten Vektorfelds (Funktion der Kantenmitte) naeherungsweise: A(x_mitte) . kvec."""
    xm = netz.x[netz.kanten[:, 0]] + 0.5 * netz.kvec
    return (feld(xm) * netz.kvec).sum(1)
