# -*- coding: utf-8 -*-
"""Drehrahmen-Feld (netzgpu): Einheitsquaternion q je Ecke, Energie 4 (1 - (q_a . q_b)^2) je Kante (Guertel-Energie wie
Z2-SCHUTZ-2 / GPU-Z2-1, dort auf Finns Diamant-Netz; hier auf jedem Netz des Rechenkerns, z. B. V).

Die Energie haengt nur von (q_a . q_b)^2 ab: q und -q sind derselbe Rahmen (SO(3)). Ein Kern, der um 360 Grad gedreht
ist (q = -1), ist als Rahmen wieder die Eins; das Feld dazwischen traegt dann die nichttriviale Klasse von pi_1(SO(3)) = Z2.
Relaxation: FIRE mit Tangentialprojektion und Normierung (wie finn.fire_feld, hier kompakt neu geschrieben).
Die Barrieren-Rechnung des Projekts (Bisektion, 25,028 bei r0 = 10, R = 20) laeuft mit dem kopierten Code in alt_rahmen/.
"""
import math

import torch


def qmul(a, b):
    aw, ax, ay, az = a.unbind(-1)
    bw, bx, by, bz = b.unbind(-1)
    return torch.stack([aw * bw - ax * bx - ay * by - az * bz,
                        aw * bx + ax * bw + ay * bz - az * by,
                        aw * by - ax * bz + ay * bw + az * bx,
                        aw * bz + ax * by - ay * bx + az * bw], -1)


def qachse(n, theta):
    """Quaternion zur Drehung um die Achse n (3,) um theta (Tensor beliebiger Form)."""
    theta = torch.as_tensor(theta)
    n = torch.as_tensor(n, dtype=theta.dtype, device=theta.device)
    n = n / torch.linalg.norm(n)
    c, s = torch.cos(0.5 * theta), torch.sin(0.5 * theta)
    return torch.cat([c[..., None], s[..., None] * n], -1)


class Rahmen:
    def __init__(self, netz, zentrum, r0, R):
        self.netz = netz
        d = netz.ecken_minbild(zentrum)
        r = torch.linalg.norm(d, dim=1)
        self.r = r
        self.kern = r <= r0 + 1e-9
        self.rand = r > R + 1e-9
        self.frei = ~self.kern & ~self.rand
        rc = torch.clamp(r, min=r0)
        h = (1.0 / rc - 1.0 / R) / (1.0 / r0 - 1.0 / R)
        self.h = torch.clamp(h, 0.0, 1.0)
        self.h[self.kern] = 1.0
        self.h[self.rand] = 0.0
        self.a, self.b = netz.kanten[:, 0], netz.kanten[:, 1]
        self.r0, self.R = r0, R

    def eins(self):
        q = torch.zeros((self.netz.N_e, 4), dtype=self.netz.dtype, device=self.netz.device)
        q[:, 0] = 1.0
        return q

    def energie(self, q, grad=True):
        c = (q[self.a] * q[self.b]).sum(-1)
        E = (4.0 * (1.0 - c * c)).sum()
        if not grad:
            return E, None, c
        f = (-8.0 * c)[:, None]
        G = torch.zeros_like(q)
        G.index_add_(0, self.a, f * q[self.b])
        G.index_add_(0, self.b, f * q[self.a])
        return E, G, c

    def energie_ecke(self, q):
        c = (q[self.a] * q[self.b]).sum(-1)
        e = 4.0 * (1.0 - c * c)
        out = torch.zeros(self.netz.N_e, dtype=q.dtype, device=q.device)
        out.index_add_(0, self.a, 0.5 * e)
        out.index_add_(0, self.b, 0.5 * e)
        return out

    def setze(self, q, theta):
        q = q.clone()
        q[self.kern] = qachse([0.0, 0.0, 1.0], torch.tensor(theta, dtype=q.dtype, device=q.device))
        q[self.rand] = torch.tensor([1.0, 0, 0, 0], dtype=q.dtype, device=q.device)
        return q

    def praediktor(self, q, dth):
        dq = qachse([0.0, 0.0, 1.0], dth * self.h)
        y = qmul(dq, q)
        return torch.where(self.frei[:, None], y, q)

    def tang(self, G, q):
        G = G - (G * q).sum(-1, keepdim=True) * q
        return G * self.frei[:, None]

    def fire(self, q, nmax=20000, ftol=1e-7, dtmax=0.1, dt=0.02):
        """FIRE (Bitzek et al.) auf der Einheitssphaere je Ecke; Kern und Rand fest."""
        v = torch.zeros_like(q)
        alpha, npos = 0.1, 0
        it = 0
        fmax = float('inf')
        for it in range(nmax):
            E, G, _ = self.energie(q)
            F = -self.tang(G, q)
            fmax = float(torch.linalg.norm(F, dim=1).max())
            if fmax < ftol:
                break
            P = float((F * v).sum())
            if P > 0:
                vn = torch.linalg.norm(v)
                fn = torch.linalg.norm(F)
                v = (1 - alpha) * v + alpha * vn * F / fn
                npos += 1
                if npos > 5:
                    dt = min(dt * 1.1, dtmax)
                    alpha *= 0.99
            else:
                v = torch.zeros_like(v)
                dt *= 0.5
                alpha = 0.1
                npos = 0
            v = v + dt * F
            q = q + dt * v
            q = q / torch.linalg.norm(q, dim=1, keepdim=True)
            v = self.tang(v, q)
        E, _, c = self.energie(q, grad=False)
        return q, {'E': float(E), 'iter': it + 1, 'fmax': fmax, 'c_min': float(c.min())}
