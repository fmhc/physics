#!/usr/bin/env python3
"""REGGE-RAND-1, RR5 (wahlweise): nichtlineare Eckenregel F_v(psi) = 16 pi G m_v im Dirichlet-Kasten,
zwei Gitterkugeln (Eigenmasse), Randmasse aus dem Fluss des linearen Regge-Operators, DeltaM gegen -G M+ M- / d.
Nur auf der .69 ueber kleintest.sh (Spur p4000a). Siehe PLAN.md, Abschnitt 7."""
import argparse
import json
import math
import time

import numpy as np
from scipy.fft import dstn, idstn

import rr


def solve(m, L, tol_rel=1e-10, maxit=300):
    psi = np.ones((L, L, L))
    j = np.arange(1, L)
    lam1 = 2.0 - 2.0 * np.cos(np.pi * j / L)
    lam = 8.0 * (lam1[:, None, None] + lam1[None, :, None] + lam1[None, None, :])
    src = 16 * np.pi * rr.G * m
    tol = tol_rel * float(src.max())
    omega = 1.0
    prev = np.inf
    hist = []
    nr = np.inf
    for it in range(maxit):
        F, _, _ = rr.F_psi(psi)
        ri = (F - src)[1:, 1:, 1:]
        nr = float(np.abs(ri).max())
        hist.append(nr)
        if nr <= tol:
            return psi, it, nr, True, hist
        if nr > prev:
            omega *= 0.5
        prev = nr
        psi[1:, 1:, 1:] -= omega * idstn(dstn(ri, type=1) / lam, type=1)
    return psi, maxit, nr, False, hist


def dirichlet_poisson(f, L):
    """u = (-Laplace_7)^-1 f im selben Dirichlet-Kasten (Naht u = 0), DST-I."""
    j = np.arange(1, L)
    lam1 = 2.0 - 2.0 * np.cos(np.pi * j / L)
    lam = lam1[:, None, None] + lam1[None, :, None] + lam1[None, None, :]
    u = np.zeros((L, L, L))
    u[1:, 1:, 1:] = idstn(dstn(f[1:, 1:, 1:], type=1) / lam, type=1)
    return u


def kugel(L, c, a):
    n = np.arange(L)
    X, Y, Z = np.meshgrid(n, n, n, indexing="ij")
    return (X - c[0]) ** 2 + (Y - c[1]) ** 2 + (Z - c[2]) ** 2 <= a * a


def randmassen(psi, m, st, L, c, R_list):
    n = np.arange(L)
    X, Y, Z = np.meshgrid(n, n, n, indexing="ij")
    dpsi = psi - 1.0
    out = {}
    for R in R_list:
        inD = (np.abs(X - c[0]) <= R) & (np.abs(Y - c[1]) <= R) & (np.abs(Z - c[2]) <= R)
        out[str(R)] = rr.flux(dpsi, list(st.items()), inD) / (16 * np.pi * rr.G)
    out["summe_m_durch_psi"] = float((m / psi).sum())
    out["eigenmasse"] = float(m.sum())
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--L", type=int, default=64)
    ap.add_argument("--a", type=int, default=3)
    ap.add_argument("--d", default="12,16,20")
    ap.add_argument("--mdurchd", default="0.025,0.05,0.1")
    ap.add_argument("--extra_m", default="0.01")  # Kontrolle m -> 0 bei d = erstes d (kein Urteil)
    ap.add_argument("--R", default="16,18,20")
    a = ap.parse_args()
    t0 = time.time()
    L = a.L
    c = (L // 2, L // 2, L // 2)
    Js = rr.local_jacobians()
    st, rest = rr.stencil(Js, 8)
    R_list = [int(x) for x in a.R.split(",")]
    ds = [int(x) for x in a.d.split(",")]
    confs = [(d, float(q) * d, float(q)) for d in ds for q in a.mdurchd.split(",")]
    if a.extra_m:
        for mm in a.extra_m.split(","):
            confs.append((ds[0], float(mm), float(mm) / ds[0]))
    res = {"L": L, "a": a.a, "c": list(c), "R": R_list, "schablone_rest": rest, "paare": []}
    for (d, mtot, q) in confs:
        cp = (c[0] + d // 2, c[1], c[2])
        cm = (c[0] - d // 2, c[1], c[2])
        bp = kugel(L, cp, a.a)
        bm = kugel(L, cm, a.a)
        mp = np.where(bp, mtot / bp.sum(), 0.0)
        mm_ = np.where(bm, mtot / bm.sum(), 0.0)
        e = {"d": d, "m": mtot, "m_durch_d": q, "N_kugel": int(bp.sum())}
        # Randkorrektur [A, nach Rauchlauf 3]: Newton-Kern im selben Kasten, gemittelt ueber beide Kugeln.
        # Im freien Raum (Schalensatz) waere <K> = 1/d.
        u = dirichlet_poisson(mm_, L)
        e["K_kasten"] = float(4 * np.pi * (mp * u).sum() / (mp.sum() * mm_.sum()))
        e["d_mal_K_kasten"] = e["K_kasten"] * d
        for lab, mass in (("paar", mp + mm_), ("plus", mp), ("minus", mm_)):
            psi, it, nr, ok, hist = solve(mass, L)
            e[lab] = {"iter": it, "residuum": nr, "konvergiert": bool(ok), "psi_max": float(psi.max()),
                      "rand": randmassen(psi, mass, st, L, c, R_list)}
            if lab != "paar":
                e[lab]["phi_selbst_mittel"] = float((mass * (psi - 1.0)).sum() / mass.sum())
            print(f"d={d} m={mtot:.4g} {lab} it={it} res={nr:.2e} ok={ok} {time.time() - t0:.1f}s", flush=True)
        res["paare"].append(e)
    res["zeit_s"] = time.time() - t0
    with open(a.out, "w") as fh:
        json.dump(res, fh, indent=1)
    print("fertig", res["zeit_s"])


if __name__ == "__main__":
    main()
