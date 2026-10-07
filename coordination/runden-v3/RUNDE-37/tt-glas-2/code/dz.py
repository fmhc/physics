#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TT-GLAS-2: gemeinsame dichte Bausteine (torch; GPU, falls sichtbar, sonst CPU mit 1 Thread).

basis      : S = orthonormales Komplement von Bild[M, c] (wie tg.punkt). Nicht-Gamma: Householder-QR (torch.geqrf) und
             Anwendung von Q auf [0; I] (torch.ormqr), Rang aus |diag R| (Schwelle 1e-9 wie tg); sonst oder bei Rangverlust
             volle SVD (wie tg).
reduziert  : S^+ H S fuer duenn besetztes H (scipy).
k3_tetra   : Lagrange-Masse A3 je Tetraeder (EINE-WELT-LOCH-1/TT-ISO-1): (V_t / mittleres V) Phi_t^-T (1 - TR TR^T) Phi_t^-1.
assemble   : Bloch-Assemblierung je Tetraeder (wie tg.ops_BA).
affin_wellen, ritz: affine TT-Wellen (wie tg.affin) und 2x2-Rayleigh-Ritz.
"""
import os, sys
import numpy as np
import scipy.sparse as sp
import torch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tg  # noqa: E402
import tp  # noqa: E402

RANG_REL = 1e-9
GINV = np.eye(6) - np.outer(tp.TR, tp.TR)   # |h|^2 - (tr h)^2 in der B6-Basis (orthonormal, Frobenius)


def geraet():
    torch.set_num_threads(1)
    return torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')


def herm(X):
    return 0.5 * (X + X.conj().T)


def basis(Xnp, dev, gamma=False):
    E, nX = Xnp.shape
    if not gamma:
        X = torch.from_numpy(np.ascontiguousarray(Xnp)).to(dev)
        a, tau = torch.geqrf(X)
        del X                                   # Speicher (N = 1024 auf der P4000)
        dR = a.diagonal().abs()
        rel = float((dR.min() / dR.max()).item())
        if rel > RANG_REL:
            C = torch.zeros((E, E - nX), dtype=a.dtype, device=dev)
            C[nX:, :] = torch.eye(E - nX, dtype=a.dtype, device=dev)
            S = torch.ormqr(a, tau, C, left=True, transpose=False)
            del a, C
            return S, {'weg': 'qr', 'rang_Mc': int(nX), 'nX': int(nX), 'diag_rel_min': rel}
        del a
    X = torch.from_numpy(np.ascontiguousarray(Xnp)).to(dev)
    U, s, _ = torch.linalg.svd(X, full_matrices=True)
    r = int((s > RANG_REL * s.max()).sum().item())
    return U[:, r:].contiguous(), {'weg': 'svd', 'rang_Mc': r, 'nX': int(nX), 'sv_rel_min': float((s.min() / s.max()).item())}


E_DICHT_MAX = 6000   # bis zu dieser Kantenzahl H dicht auf die GPU; darueber H @ S duenn auf der CPU (Speicher)


def reduziert(H, S, dev):
    if dev.type == 'cuda' and H.shape[0] <= E_DICHT_MAX:
        Hd = torch.from_numpy(H.toarray()).to(dev)
        R = S.conj().T @ (Hd @ S)
        del Hd
    elif dev.type == 'cuda':
        HS = torch.from_numpy(np.ascontiguousarray(H @ S.cpu().numpy())).to(dev)
        R = S.conj().T @ HS
        del HS
    else:
        HS = torch.from_numpy(np.ascontiguousarray(H @ S.numpy()))
        R = S.conj().T @ HS
    return herm(R)


def k3_tetra(mod, X):
    et = np.stack([X[:, j] - X[:, i] for (i, j, _, _) in tg.PAARE], 1)
    nt = et / np.linalg.norm(et, axis=2)[..., None]
    Phi = np.einsum('tpi,sij,tpj->tps', nt, tp.B6, nt)
    Pi = np.linalg.inv(Phi)
    vol = np.abs(np.linalg.det(X[:, 1:] - X[:, :1])) / 6.0
    w = vol / vol.mean()
    K = w[:, None, None] * np.einsum('tsp,su,tuq->tpq', Pi, GINV, Pi)
    return K, {'phi_cond_max': float(np.linalg.cond(Phi).max()), 'K3_absmax': float(np.abs(K).max()), 'vol_mittel': float(vol.mean())}


def assemble(mod, Kt, k):
    E, eidx = mod['E'], mod['eidx']
    ph = np.exp(1j * (mod['Tcopy'] @ k))
    f = np.conj(ph)[:, :, None] * ph[:, None, :]
    rows = np.repeat(eidx[:, :, None], 6, 2).ravel()
    cols = np.repeat(eidx[:, None, :], 6, 1).ravel()
    return sp.coo_matrix(((Kt * f).ravel(), (rows, cols)), shape=(E, E)).tocsr()


def affin_wellen(mod, kk):
    dvec = kk / np.linalg.norm(kk)
    u = np.cross(dvec, [0.3, 0.5, 0.7])
    u = u / np.linalg.norm(u)
    v = np.cross(dvec, u)
    hs = [(np.outer(u, u) - np.outer(v, v)) / np.sqrt(2), (np.outer(u, v) + np.outer(v, u)) / np.sqrt(2)]
    ph = np.exp(1j * (mod['mitte'] @ kk))
    return np.stack([np.einsum('ei,ij,ej->e', mod['n'], h, mod['n']) * ph for h in hs], 1)


def ritz(Kz, Gz):
    """2x2 Rayleigh-Ritz: Eigenwerte von Gz^-1 Kz (Steifigkeit Kz, Masse Gz), aufsteigend nach Realteil."""
    Kz = 0.5 * (Kz + Kz.conj().T)
    Gz = 0.5 * (Gz + Gz.conj().T)
    w = np.linalg.eigvals(np.linalg.solve(Gz, Kz))
    w = w[np.argsort(w.real)]
    return [float(x) for x in w.real], float(np.abs(w.imag).max()), [float(x) for x in np.linalg.eigvalsh(Gz)]
