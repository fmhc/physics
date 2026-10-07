#!/usr/bin/env python3
# DIAGNOSE nach dem Einfrieren (aendert kein Urteil). Anlass: In der Platte mit L = 16 sind die Randzustaende beider
# Raender bei gleichem k und gleicher Phase durch das Volumen schwach gekoppelt (Restmasse wie bei Domain-Wall-Fermionen,
# Kaplan Eq. 3.21); die Eigenvektoren sind dort halb oben, halb unten (diag_k0), und die eingefrorene Auswahl
# (Gewicht oben > 0,9 bzw. < 0,1) sieht sie nicht.
# Verfahren hier: Randprojektion. Alle Zustaende im Lueckenfenster werden so gedreht, dass sie P_oben diagonalisieren;
# der obere (untere) Teilraum gibt eine gestauchte Unitaere U_rand = Q^dag U Q, deren Eigenphasen das Spektrum des
# einzelnen Rands sind (Kopplung der Raender herausgenommen). Knoten = entartete Paare von U_rand; Newton auf den
# sigma-Anteil des Paares wie in takt4d.newton; Chiralitaet, Zaehlung je Rand und Luecke auf zwei Gittern, Isotropie,
# Restaufspaltung der vollen Platte am Knoten gegen L.
# Nutzt nur eingefrorene Bausteine aus takt4d.py. Aufruf ueber kleintest.sh: diag_proj.py --modell P4a --out DATEI.json
import argparse
import json
import sys
import time

import numpy as np
from scipy.linalg import schur

import takt4d as T


def rand_block(model, U, fn, rand):
    Tm, Z = schur(U, output="complex")
    ph = np.angle(np.diag(Tm))
    sel = np.where(fn(ph))[0]
    if len(sel) == 0:
        return None
    Zs = Z[:, sel]
    Pm = Zs.conj().T @ (model.ptop[:, None] * Zs)
    e, V = np.linalg.eigh(Pm)
    m = e > 0.5 if rand == "oben" else e < 0.5
    if not np.any(m):
        return None
    Q = Zs @ V[:, m]
    return Q, e[m]


def rand_spektrum(model, k, fn, rand):
    U = model.U(np.asarray(k, float)[None, :])[0]
    rb = rand_block(model, U, fn, rand)
    if rb is None:
        return None
    Q, reinheit = rb
    W = Q.conj().T @ U @ Q
    return np.angle(np.linalg.eigvals(W)), reinheit


def proj_paar(model, k, fn, rand, ziel):
    U, dU = model.UdU(np.asarray(k, float)[None, :])
    U = U[0]
    dU = [x[0] for x in dU]
    rb = rand_block(model, U, fn, rand)
    if rb is None or rb[0].shape[1] < 2:
        return None
    Q, reinheit = rb
    W = Q.conj().T @ U @ Q
    w, Vw = np.linalg.eig(W)
    phw = np.angle(w)
    o = np.argsort(np.abs(T.kreis(phw - ziel)))[:2]
    Qp, _ = np.linalg.qr(Q @ Vw[:, o])
    W2 = Qp.conj().T @ U @ Qp
    phc = float(np.angle(np.linalg.det(W2)) / 2)
    if abs(T.kreis(phc - ziel)) > np.pi / 2:
        phc = float(T.kreis(phc + np.pi))
    e = np.exp(-1j * phc)
    b = np.array([np.real(np.trace(e * W2 @ P) / 2j) for P in T.PAULI])
    G = [e * (Qp.conj().T @ dU[l] @ Qp) / 1j for l in range(3)]
    M = np.array([[np.real(np.trace(G[l] @ P)) / 2 for P in T.PAULI] for l in range(3)])
    spalt = float(abs(T.kreis(phw[o[0]] - phw[o[1]])))
    return {"phc": phc, "b": b, "M": M, "spalt": spalt, "reinheit_min": float(reinheit.min() if rand == "oben" else 1 - reinheit.max())}


def proj_newton(model, k0, fn, rand, ziel, maxit=40):
    k = np.array(k0, float)
    p = None
    for _ in range(maxit):
        p = proj_paar(model, k, fn, rand, ziel)
        if p is None:
            return None
        if np.linalg.norm(p["b"]) < 1e-13:
            break
        try:
            dk = -np.linalg.solve(p["M"].T, p["b"])
        except np.linalg.LinAlgError:
            return None
        st = float(np.linalg.norm(dk))
        if not np.isfinite(st):
            return None
        if st > 0.3:
            dk *= 0.3 / st
        k = k + dk
        ziel = p["phc"]
    p = proj_paar(model, k, fn, rand, ziel)
    if p is None or np.linalg.norm(p["b"]) > 1e-10:
        return None
    V = -p["M"]
    sv = np.linalg.svd(V, compute_uv=False)
    return {"k": T.kreis(k).tolist(), "phase": p["phc"], "chi": int(np.sign(np.linalg.det(V))), "sv": sv.tolist(),
            "b_rest": float(np.linalg.norm(p["b"])), "spalt_proj": p["spalt"], "reinheit": p["reinheit_min"]}


def suche_proj(model, fns, Ng, offset, smax=0.6, max_kand=60):
    t = (np.arange(Ng) + offset) / Ng
    K = -np.pi + 2 * np.pi * np.stack(np.meshgrid(t, t, t, indexing="ij"), -1).reshape(-1, 3)
    keys = [(r, g) for r in ("oben", "unten") for g in fns]
    s = {key: np.full(len(K), np.inf) for key in keys}
    mid = {key: np.zeros(len(K)) for key in keys}
    for i0 in range(0, len(K), 256):
        Ub = model.U(K[i0:i0 + 256])
        for j in range(len(Ub)):
            Tm, Z = schur(Ub[j], output="complex")
            ph = np.angle(np.diag(Tm))
            for g in fns:
                fn, c = fns[g]
                sel = np.where(fn(ph))[0]
                if len(sel) < 2:
                    continue
                Zs = Z[:, sel]
                e, V = np.linalg.eigh(Zs.conj().T @ (model.ptop[:, None] * Zs))
                for r in ("oben", "unten"):
                    m = e > 0.5 if r == "oben" else e < 0.5
                    if m.sum() < 2:
                        continue
                    Q = Zs @ V[:, m]
                    phw = np.sort(T.kreis(np.angle(np.linalg.eigvals(Q.conj().T @ Ub[j] @ Q)) - c))
                    dd = np.diff(phw)
                    q = int(np.argmin(dd))
                    s[(r, g)][i0 + j] = dd[q]
                    mid[(r, g)][i0 + j] = c + 0.5 * (phw[q] + phw[q + 1])
    funde = {f"{r}|{g}": [] for (r, g) in keys}
    for (r, g) in keys:
        fn, c = fns[g]
        S = s[(r, g)].reshape(Ng, Ng, Ng)
        loc = np.ones_like(S, dtype=bool)
        for ax in range(3):
            for sh in (1, -1):
                loc &= S <= np.roll(S, sh, axis=ax)
        idx = np.where((loc & (S < smax)).ravel())[0]
        idx = idx[np.argsort(s[(r, g)][idx])][:max_kand]
        for i in idx:
            res = proj_newton(model, K[i], fn, r, mid[(r, g)][i])
            if res is not None:
                funde[f"{r}|{g}"].append(res)
        funde[f"{r}|{g}"] = T.zusammenfassen(funde[f"{r}|{g}"])
    return funde


def isotropie_proj(model, node, fn, rand, qs=(0.01, 0.05, 0.2), n=400):
    dirs = T.fib_dirs(n)
    out = {}
    for q in qs:
        v = []
        for d in dirs:
            rs = rand_spektrum(model, np.array(node["k"]) + q * d, fn, rand)
            if rs is None or len(rs[0]) < 2:
                v.append(np.nan)
                continue
            phw = rs[0]
            o = np.argsort(np.abs(T.kreis(phw - node["phase"])))[:2]
            v.append(abs(T.kreis(phw[o[0]] - phw[o[1]])) / (2 * q))
        v = np.array(v)
        out[str(q)] = {"v_mittel": float(np.nanmean(v)), "spann_rel": float((np.nanmax(v) - np.nanmin(v)) / np.nanmean(v)),
                       "alle_gefunden": bool(np.all(np.isfinite(v)))}
    sv = np.array(node["sv"])
    out["linear_spann_rel"] = float((sv.max() - sv.min()) / sv.mean())
    return out


def restaufspaltung(name, knoten, Ls=(8, 12, 16, 20, 24)):
    tau, M, ordnung, _ = T.MODELLE[name]
    out = []
    for L in Ls:
        m = T.Plan4D(tau, M, ordnung, L)
        U = m.U(np.array(knoten["k"])[None, :])[0]
        ph, Z, wt = T.eigen_rand(U, m.ptop)
        o = np.argsort(np.abs(T.kreis(ph - knoten["phase"])))[:4]
        out.append({"L": L, "phasen": ph[o].tolist(), "wt_oben": wt[o].tolist(),
                    "aufspaltung": float(np.ptp(T.kreis(ph[o] - knoten["phase"])))})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--modell", default="P4a")
    ap.add_argument("--out", required=True)
    ap.add_argument("--gitter", default="20,17")
    a = ap.parse_args()
    t0 = time.time()
    tau, M, ordnung, L = T.MODELLE[a.modell]
    model = T.Plan4D(tau, M, ordnung, L)
    vol = T.volumen_4d(model, N=20)
    fns = T.fenster_fns(vol)
    NgA, NgB = [int(x) for x in a.gitter.split(",")]
    res = {"modell": a.modell, "volumen": vol, "luecken_offen": sorted(fns), "gitter": [NgA, NgB]}
    fA = suche_proj(model, fns, NgA, 0.0)
    fB = suche_proj(model, fns, NgB, 0.5)
    res["knoten_A"], res["knoten_B"] = fA, fB
    zus = {}
    for key in fA:
        chis = [f["chi"] for f in fA[key]]
        zus[key] = {"anzahl": len(chis), "netto": int(sum(chis)), "gleich_AB": T.gleich(fA[key], fB[key]),
                    "anzahl_B": len(fB[key]), "netto_B": int(sum(f["chi"] for f in fB[key]))}
    res["zaehlung"] = zus
    res["summenregel"] = {g: zus[f"oben|{g}"]["netto"] + zus[f"unten|{g}"]["netto"] for g in fns}
    tief = {}
    for r in ("oben", "unten"):
        kand = [(abs(T.kreis(f["phase"])), g, f) for g in fns for f in fA[f"{r}|{g}"]]
        if not kand:
            tief[r] = None
            continue
        kand.sort(key=lambda x: x[0])
        _, g, f = kand[0]
        tief[r] = {"luecke": g, "knoten": f, "iso": isotropie_proj(model, f, fns[g][0], r),
                   "rest_gegen_L": restaufspaltung(a.modell, f)}
    res["tiefster_kegel"] = tief
    res["laufzeit_s"] = time.time() - t0
    with open(a.out, "w") as fh:
        json.dump(res, fh, indent=1, default=lambda o: o.tolist() if hasattr(o, "tolist") else str(o))
    print(f"fertig {res['laufzeit_s']:.1f} s", flush=True)


if __name__ == "__main__":
    sys.exit(main())
