# -*- coding: utf-8 -*-
"""Takt (Lapse) und metrische Kopplung (netzgpu).

Newton-Grenzfall auf dem Netz: Takt N = 1 + Phi mit  d0^T *1 d0 Phi = -4 pi G (m - M *0 / V)  (periodisch, Mittel 0),
m = Masse (Energie) je Ecke. Laengen in isotroper Eichung (gamma = 1): delta l / l = -(Phi_a + Phi_b) / 2 je Kante,
Gewichte w (1 - 2 Phi) je Ecke (wie LICHT-ABLENKUNG-V, Regel 'ecke'), hier nichtlinear ueber die Regge-Einbettung.
Metrische Kopplung der Materie: Sterne aus diesen Laengen, Takt als Faktor (siehe skalar.py, licht.py).
Spannungsterm (SCHWERE-MASSE-V): aktive Masse = E + S mit S = 3K - G - 3V; quelle_spannung() liefert s_v.
"""
import math

import torch


def cg(apply, b, x0=None, tol=1e-12, maxiter=20000, proj=None):
    """Konjugierte Gradienten fuer symmetrisch positiv (semi)definite Operatoren (GPU)."""
    x = torch.zeros_like(b) if x0 is None else x0.clone()
    r = b - apply(x)
    if proj is not None:
        r = proj(r)
    p = r.clone()
    rr = (r * r).sum()
    bn = math.sqrt(float((b * b).sum())) + 1e-300
    it = 0
    for it in range(maxiter):
        Ap = apply(p)
        alpha = rr / (p * Ap).sum()
        x = x + alpha * p
        r = r - alpha * Ap
        if proj is not None:
            r = proj(r)
        rn = (r * r).sum()
        if math.sqrt(float(rn)) < tol * bn:
            break
        p = r + (rn / rr) * p
        rr = rn
    return x, {'iter': it + 1, 'rest_rel': math.sqrt(float(rn)) / bn}


def laplace_op(netz, s1):
    d0 = netz.d0
    d0t = netz.d0.transpose(0, 1).to_sparse_csr() if not hasattr(netz, '_d0t') else netz._d0t
    netz._d0t = d0t

    def apply(phi):
        return d0t @ (s1 * (d0 @ phi))
    return apply


def takt_poisson(netz, st, m, G=1.0, tol=1e-12):
    """Phi aus der Massenverteilung m (je Ecke). Rueckgabe Phi (Mittel 0) und Info."""
    V = netz.volumen()
    M = float(m.sum())
    rhs = -4.0 * math.pi * G * (m - M * st['s0'] / V)
    ap = laplace_op(netz, st['s1'])
    mean0 = lambda r: r - r.mean()
    phi, info = cg(ap, rhs, tol=tol, proj=mean0)
    phi = phi - phi.mean()
    info['rest_gleichung'] = float((ap(phi) - rhs).abs().max() / rhs.abs().max())
    info['M'] = M
    return phi, info


def gauss_masse(netz, x0, M, breite):
    """Gauss-Blob der Gesamtmasse M um x0 (minimales Bild), verteilt mit den dualen Volumina."""
    st = netz.sterne()
    d = netz.ecken_minbild(x0)
    r2 = (d * d).sum(1)
    rho = torch.exp(-0.5 * r2 / breite ** 2)
    m = rho * st['s0']
    return m * (M / m.sum()), st


def metrik_aus_takt(netz, phi, gamma=1.0):
    """Kantenlaengen und Gewichte zur isotropen Eichung: l (1 - gamma (Phi_a + Phi_b)/2), w (1 - 2 gamma Phi)."""
    a, b = netz.kanten[:, 0], netz.kanten[:, 1]
    sig = -gamma * phi
    l = netz.laengen() * (1.0 + 0.5 * (sig[a] + sig[b]))
    w = netz.w * (1.0 + 2.0 * sig)
    return l, w


def takt_kante(netz, N):
    return 0.5 * (N[netz.kanten[:, 0]] + N[netz.kanten[:, 1]])


def takt_dreieck(netz, N):
    t = netz.dreiecke
    return (N[t[:, 0]] + N[t[:, 1]] + N[t[:, 2]]) / 3.0
