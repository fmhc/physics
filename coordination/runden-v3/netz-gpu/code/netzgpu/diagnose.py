# -*- coding: utf-8 -*-
"""Diagnose (netzgpu): Bloch-Reduktion der Ortsraum-Operatoren des Rechenkerns auf eine primitive Zelle.

Aus den Eintraegen eines periodischen Operators K (COO auf dem Superzellen-Netz) wird K(k) je Klasse gebildet:
  K(k)[t(r), t(c)] += v_rc * s_r * s_c * exp(i k . (x_c - x_r)) / n_prim
(t = Klasse modulo Gittertranslation, s = Vorzeichen gegen die Klassenrichtung, x = Ort des Freiheitsgrads, minimales
Bild). Fuer beliebiges k (nicht nur Superzellen-k). Damit: Lichttempo auf V (zwei Photonen nach Abzug der Eichnullen
ueber einen Strafterm) und Tempo des Skalars.
"""
import math

import numpy as np
import torch


def _minbild(netz, d):
    B = torch.tensor(netz.box, dtype=netz.dtype, device=netz.device)
    return d - B * torch.round(d / B)


def bloch(netz, r, c, v, typ_r, typ_c, s_r, s_c, x_r, x_c, n_r, n_c, ks):
    """K(k) fuer mehrere k (K, 3): Rueckgabe (K, n_r, n_c) complex128."""
    dev = netz.device
    d = _minbild(netz, x_c[c] - x_r[r])                       # (nnz, 3)
    ks = torch.as_tensor(ks, dtype=torch.float64, device=dev)
    ph = torch.exp(1j * (d @ ks.T))                            # (nnz, K)
    w = (v * s_r[r] * s_c[c]).to(torch.complex128)
    idx = typ_r[r] * n_c + typ_c[c]
    out = torch.zeros((n_r * n_c, ks.shape[0]), dtype=torch.complex128, device=dev)
    out.index_add_(0, idx, w[:, None] * ph)
    return (out / netz.n_prim).T.reshape(ks.shape[0], n_r, n_c)


def _t(netz, a, dt=torch.int64):
    return torch.as_tensor(np.asarray(a), dtype=dt, device=netz.device)


def licht_tempo(netz, st, ks, lam=1.0):
    """omega^2 / k^2 der zwei Photonen je k (K, 3) aus K = d1^T *2 d1, M = *1, Eichstrafe lam M G (G^H M G)^-1 G^H M."""
    n = netz
    dev = n.device
    kt = _t(n, n.kanten_typ)
    ks_ = _t(n, n.kanten_vz, torch.float64)
    xm = n.x[n.kanten[:, 0]] + 0.5 * n.kvec
    nK = n.n_kanten_typ
    # K = d1^T diag(s2) d1: je Dreieck 3 Kanten mit Vorzeichen
    d1 = n.d1.to_sparse_coo().coalesce()
    fi, ei = d1.indices()
    sv = d1.values()
    o = torch.argsort(fi * n.N_k + ei)
    fi, ei, sv = fi[o], ei[o], sv[o]
    E3 = ei.reshape(-1, 3)
    S3 = sv.reshape(-1, 3)
    F3 = fi.reshape(-1, 3)[:, 0]
    r = E3[:, :, None].expand(-1, 3, 3).reshape(-1)
    c = E3[:, None, :].expand(-1, 3, 3).reshape(-1)
    v = (S3[:, :, None] * S3[:, None, :] * st['s2'][F3][:, None, None]).reshape(-1)
    Kk = bloch(n, r, c, v, kt, kt, ks_, ks_, xm, xm, nK, nK, ks)
    # Masse je Klasse
    m = torch.zeros(nK, dtype=torch.float64, device=dev)
    cnt = torch.zeros(nK, dtype=torch.float64, device=dev)
    m.index_add_(0, kt, st['s1'])
    cnt.index_add_(0, kt, torch.ones_like(st['s1']))
    m = m / cnt
    # G = d0(k): Kante (Klasse) x Ecke (Klasse)
    et = _t(n, n.ecken_typ)
    nV = n.n_ecken_typ
    d0 = n.d0.to_sparse_coo().coalesce()
    r0, c0 = d0.indices()
    v0 = d0.values()
    one = torch.ones(n.N_e, dtype=torch.float64, device=dev)
    Gk = bloch(n, r0, c0, v0, kt, et, ks_, one, xm, n.x, nK, nV, ks)
    Mh = torch.diag(m).to(torch.complex128)
    MG = Mh @ Gk
    GMG = Gk.conj().transpose(-1, -2) @ MG
    P = MG @ torch.linalg.solve(GMG, MG.conj().transpose(-1, -2))
    A = Kk + lam * P
    A = 0.5 * (A + A.conj().transpose(-1, -2))
    mi = (1.0 / torch.sqrt(m)).to(torch.complex128)
    Hs = mi[None, :, None] * A * mi[None, None, :]
    ev = torch.linalg.eigvalsh(Hs)
    k2 = (torch.as_tensor(ks, dtype=torch.float64, device=dev) ** 2).sum(1)
    herm_rest = float((Kk - Kk.conj().transpose(-1, -2)).abs().max())
    return ev[:, :3] / k2[:, None], herm_rest


def skalar_tempo(netz, st, ks):
    """omega^2/k^2 des Skalars (K = d0^T *1 d0, M = *0), kleinster Eigenwert je k."""
    n = netz
    dev = n.device
    et = _t(n, n.ecken_typ)
    nV = n.n_ecken_typ
    a, b = n.kanten[:, 0], n.kanten[:, 1]
    s1 = st['s1']
    r = torch.cat([a, b, a, b])
    c = torch.cat([a, b, b, a])
    v = torch.cat([s1, s1, -s1, -s1])
    one = torch.ones(n.N_e, dtype=torch.float64, device=dev)
    Kk = bloch(n, r, c, v, et, et, one, one, n.x, n.x, nV, nV, ks)
    m = torch.zeros(nV, dtype=torch.float64, device=dev)
    cnt = torch.zeros(nV, dtype=torch.float64, device=dev)
    m.index_add_(0, et, st['s0'])
    cnt.index_add_(0, et, one)
    m = m / cnt
    mi = (1.0 / torch.sqrt(m)).to(torch.complex128)
    Hs = mi[None, :, None] * Kk * mi[None, None, :]
    Hs = 0.5 * (Hs + Hs.conj().transpose(-1, -2))
    ev = torch.linalg.eigvalsh(Hs)
    k2 = (torch.as_tensor(ks, dtype=torch.float64, device=dev) ** 2).sum(1)
    return ev[:, :1] / k2[:, None]


def richtungen(n=40, saat=7):
    """Feste Achsen [100], [110], [111] und weitere Fibonacci-Richtungen."""
    R = [np.array([1.0, 0, 0]), np.array([1.0, 1, 0]) / math.sqrt(2), np.array([1.0, 1, 1]) / math.sqrt(3)]
    g = (1 + 5 ** 0.5) / 2
    for i in range(n):
        z = 1 - (i + 0.5) / n * 2
        rr = math.sqrt(max(0.0, 1 - z * z))
        ph = 2 * math.pi * i / g
        R.append(np.array([rr * math.cos(ph), rr * math.sin(ph), z]))
    return np.array(R)
