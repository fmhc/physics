#!/usr/bin/env python3
"""INDUZIERT-WILSON-2D (Runde 40, Code-Agent): induzierte konforme Steifigkeit eines Fermions mit Wilson-Glied auf
Zufallsnetzen mit Punkten nach physikalischer Flaeche und Neuvernetzung ("Zahl = Volumen").

Netze, Laengen, Skalar und naiver Operator (A) unveraendert aus INDUZIERT-DIRAC-2D (dirac2d.py, dichte2d_grob.py,
zufall2d.py, eingefroren 20261004-102358); dieselben Saaten, damit Skalar und (A) bitgleich nachgerechnet werden.

Wilson-Operator je Netz (gleiche physikalische Laengen l, Kotangens-Gewichte w aus l):
  D_W = D_A + r eps (K x 1_2)
  D_A: (A) aus dirac2d.dirac_matrix (reell antisymmetrisch, 2N x 2N, Index 2 Knoten + Spin).
  K:   Kotangens-Steifigkeit des Skalars (K_ij = -w_ij, K_ii = sum_j w_ij), je Spinorkomponente.
  eps = sqrt(A/N) (mittlerer Netzabstand): r ist in Netzabstands-Einheiten gegeben; E2 (eps = 2) ist damit exakt das
       skalierte E1-Netz mit demselben r (D_W(E2) = 2 D_W(E1-Form)).
Gamma_W = -(1/2) log det'(D_W^T D_W) = -sum_{i>=3} log sigma_i(D_W), ohne die zwei kleinsten Singulaerwerte.
  s = 0 (Grundnetz, Delaunay, w >= 0): Kern exakt = die zwei konstanten Spinoren (rechts und links). Exakt
       (Cauchy-Binet fuer das (2N-2)-te Kompositum): prod' sigma = |det M_(0)| sqrt(det(V^T V) det(W^T W)), M_(0) ohne
       die zwei Zeilen/Spalten von Knoten 0, V/W rechte/linke Nullvektoren mit v(Knoten 0) = e_k.
  s != 0: D_W regulaer; log prod' sigma = log|det D_W| - log(sigma_1 sigma_2); sigma_1, sigma_2 aus
       Block-Inversiteration mit (D_W^T D_W)^-1 (gleiche LU) und Rayleigh-Ritz (Singulaerwerte von D_W Q).
Konvention (Grassmann) wie INDUZIERT-DIRAC-2D: c_eff = (Gamma''/(k^2 A))/P mit P = -1/(24 pi), Dirac +1, Skalar +1.
Messgroesse je k: D(S) = (Gamma(S) + Gamma(-S) - 2 Gamma(0))/S^2, y = D/A (A = L^2).

Aufruf (nur ueber kleintest.sh):
  python wilson2d.py kontrolle <aus.json> [teil=k1,k2] [k2N=4001,16001]
  python wilson2d.py dichte <N> <saat0> <anzahl> <aus.json> <n-Liste> <S> [A=<Torusflaeche>] [a_saaten=<anzahl>]
      a_saaten: fuer die ersten a_saaten Saaten des Blocks wird zusaetzlich (A) gerechnet (Bitvergleich W0).
"""
import json
import math
import os
import sys
import time

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dichte2d_grob as dg  # noqa: E402  (unveraendert, eingefroren 20261004-091915)
import dirac2d as dc        # noqa: E402  (unveraendert, eingefroren 20261004-102358)

POLYAKOV = -1.0 / (24.0 * math.pi)
R_WERTE = (("W1", 1.0), ("W05", 0.5))     # Karte: r = 1 und r = 1/2, vor dem Einfrieren gebunden
BLOCK = 4                                 # Breite der Block-Inversiteration
IT_MIN, IT_MAX = 3, 60
IT_TOL = 1e-13                            # Abbruch: Aenderung von log(sigma_1 sigma_2) zwischen zwei Schritten


# ---------------------------------------------------------------------- Operatoren
def k_matrix(nz, w):
    N = nz.N
    diag = np.bincount(nz.ki, w, N) + np.bincount(nz.kj, w, N)
    r = np.concatenate([nz.ki, nz.kj, np.arange(N)])
    c = np.concatenate([nz.kj, nz.ki, np.arange(N)])
    return sp.csc_matrix((np.concatenate([-w, -w, diag]), (r, c)), shape=(N, N))


def wilson_matrix(nz, l, w, r, eps):
    D = dc.dirac_matrix(nz, l, w)
    KW = sp.kron(k_matrix(nz, w), sp.identity(2, format="csc"), format="csc")
    return (D + (r * eps) * KW).tocsc()


def _start(n2):
    i = np.arange(n2)
    X = np.stack([(i % 2 == 0).astype(float), (i % 2 == 1).astype(float),
                  np.cos(0.37 * i) + 0.5 * np.sin(1.13 * i), np.sin(0.71 * i) + 0.3 * np.cos(2.03 * i)], axis=1)
    return X[:, :BLOCK]


def gamma_wilson(M, grundnetz):
    """Gamma_W = -log prod_{i>=3} sigma_i(M). grundnetz=True: exakt singulaer (Kern 2), Cauchy-Binet-Formel."""
    t0 = time.time()
    n2 = M.shape[0]
    info = {}
    if grundnetz:
        M0 = M[2:, 2:].tocsc()
        lu = spla.splu(M0, permc_spec="COLAMD")
        d = lu.U.diagonal()
        logabs = math.fsum(np.log(np.abs(d)).tolist())
        X = lu.solve(-M[2:, :2].toarray())
        Y = lu.solve(-(M[:2, 2:].toarray()).T, trans="T")
        V = np.vstack([np.eye(2), X])
        W = np.vstack([np.eye(2), Y])
        sv, ldv = np.linalg.slogdet(V.T @ V)
        sw, ldw = np.linalg.slogdet(W.T @ W)
        skal = max(float(np.max(np.abs(M.data))), 1e-300)
        res_r = np.linalg.norm(M @ V, axis=0) / (np.linalg.norm(V, axis=0) * skal)
        res_l = np.linalg.norm(M.T @ W, axis=0) / (np.linalg.norm(W, axis=0) * skal)
        ld = logabs + 0.5 * (ldv + ldw)
        info.update({"art": "grund", "logabs_M0": logabs, "log_det_VtV": float(ldv), "log_det_WtW": float(ldw),
                     "min_abs_U": float(np.min(np.abs(d))), "nullvektor_res_rechts": float(np.max(res_r)),
                     "nullvektor_res_links": float(np.max(res_l)),
                     "endlich": bool(np.isfinite(ld) and sv > 0 and sw > 0)})
    else:
        lu = spla.splu(M, permc_spec="COLAMD")
        d = lu.U.diagonal()
        logabs = math.fsum(np.log(np.abs(d)).tolist())
        Q, _ = np.linalg.qr(_start(n2))
        alt, it, verlauf = None, 0, []
        for it in range(1, IT_MAX + 1):
            Z = lu.solve(lu.solve(Q, trans="T"))
            Q, _ = np.linalg.qr(Z)
            s = np.linalg.svd(M @ Q, compute_uv=False)[::-1]          # aufsteigend
            neu = math.log(s[0]) + math.log(s[1])
            verlauf.append(neu)
            if alt is not None and it >= IT_MIN and abs(neu - alt) < IT_TOL:
                break
            alt = neu
        ld = logabs - verlauf[-1]
        info.update({"art": "regulaer", "logabs_M": logabs, "min_abs_U": float(np.min(np.abs(d))),
                     "sigma_ritz": s.tolist(), "iterationen": it,
                     "letzte_aenderung": float(abs(verlauf[-1] - verlauf[-2])) if len(verlauf) > 1 else None,
                     "luecke_s2_s3": float(s[1] / s[2]) if len(s) > 2 else None,
                     "endlich": bool(np.isfinite(ld))})
    info["sek"] = time.time() - t0
    return -ld, info


def alle(nz, l, eps, grundnetz, mit_A):
    w, AT = nz.gewichte(l)
    out = {"B": nz.gamma(l)}
    if mit_A:
        gA, ia = dc.gamma_dirac(nz, l, w)
        out["A"], out["info_A"] = gA, ia
    for name, r in R_WERTE:
        g, info = gamma_wilson(wilson_matrix(nz, l, w, r, eps), grundnetz)
        out[name], out["info_" + name] = g, info
    out["w_negativ"] = int(np.sum(w < 0))
    return out


# ---------------------------------------------------------------------- Modus dichte (wie INDUZIERT-DIRAC-2D)
def modus_dichte(N, saat0, anzahl, ziel, nlist, S, richtungen, protokoll, out, A_torus=None, a_saaten=0):
    A_torus = float(N) if A_torus is None else float(A_torus)
    eps = math.sqrt(A_torus / N)
    out.update({"N": N, "L": math.sqrt(A_torus), "A": A_torus, "eps": eps, "nlist": nlist, "S": [S],
                "richtungen": richtungen, "r_werte": dict(R_WERTE), "saaten": []})
    for saat in range(saat0, saat0 + anzahl):
        t0 = time.time()
        mit_A = (saat - saat0) < a_saaten
        ops = ("B", "W1", "W05") + (("A",) if mit_A else ())
        z, L = dg.grundpunkte(N, saat, math.sqrt(A_torus))
        n0 = dg.periodisches_netz(z, L, "basis")
        p0 = dg.netz_pruefen(n0, n0.l0)
        p0_z2 = n0.pruefen()
        g0 = alle(n0, n0.l0, eps, True, mit_A)
        sch0 = dg.kanten_schluessel(n0)
        pts = []
        for rn in richtungen:
            r = dg.RICHTUNGEN[rn]
            for n in nlist:
                kint = (n * r[0], n * r[1])
                kvec = 2 * np.pi * np.asarray(kint, dtype=float) / L
                kb = float(np.linalg.norm(kvec))
                seiten = {}
                for name, sv in (("plus", S), ("minus", -S)):
                    ts = time.time()
                    x, pinfo = dg.psi(z, kvec, sv, L)
                    nz = dg.periodisches_netz(x, L, "koord")
                    lk = dg.laengen_geo(nz, kvec, sv)
                    pk = dg.netz_pruefen(nz, lk)
                    g = alle(nz, lk, eps, False, mit_A)
                    g.update({"psi": pinfo, "pruefung": pk, "neue_kanten": dg.neue_kanten(nz, sch0),
                              "lu_B": dict(nz.lu_info), "sek": time.time() - ts})
                    seiten[name] = g
                e = {"S": S, "plus": seiten["plus"], "minus": seiten["minus"]}
                for op in ops:
                    Dv = (seiten["plus"][op] + seiten["minus"][op] - 2 * g0[op]) / (S * S)
                    e["D_" + op] = Dv
                    e["y_" + op] = Dv / A_torus
                pts.append({"richtung": rn, "n": n, "kint": list(kint), "betrag": kb, "k2A": kb * kb * A_torus,
                            "je_S": [e]})
                sp_ = seiten["plus"]
                protokoll(f"N={N} A={A_torus:.0f} saat={saat} {rn} n={n}: W1 sigma {sp_['info_W1']['sigma_ritz'][0]:.2e} "
                          f"{sp_['info_W1']['sigma_ritz'][1]:.2e} | {sp_['info_W1']['sigma_ritz'][2]:.2e} it "
                          f"{sp_['info_W1']['iterationen']}; W05 sigma {sp_['info_W05']['sigma_ritz'][0]:.2e} "
                          f"{sp_['info_W05']['sigma_ritz'][1]:.2e} | {sp_['info_W05']['sigma_ritz'][2]:.2e} it "
                          f"{sp_['info_W05']['iterationen']}; wneg {sp_['w_negativ']} {sp_['sek']:.1f}s")
        out["saaten"].append({"saat": saat, "gamma0": g0, "pruefung0": p0, "pruefung0_z2": p0_z2,
                              "lu0_B": dict(n0.lu_info), "punkte": pts, "mit_A": mit_A,
                              "sekunden": time.time() - t0})
        with open(ziel + ".tmp", "w") as f:
            json.dump(out, f)
        os.replace(ziel + ".tmp", ziel)
        protokoll(f"N={N} saat={saat} fertig in {time.time() - t0:.1f} s (A {'ja' if mit_A else 'nein'}); Grundnetz "
                  f"W1 Nullvektor-Res {g0['info_W1']['nullvektor_res_rechts']:.1e}/{g0['info_W1']['nullvektor_res_links']:.1e}")
    return out


# ---------------------------------------------------------------------- Modus kontrolle
def dicht_gamma(Md):
    s = np.linalg.svd(Md, compute_uv=False)[::-1]
    return -math.fsum(np.log(s[2:]).tolist()), s[:6].tolist()


def singulaer_klein(M, k, sigma0=1e-6):
    """Kleinste Singulaerwerte von M ueber die Jordan-Wielandt-Matrix [[0, M], [M^T, 0]] (Eigenwerte +-sigma_i),
    shift-invert um sigma0."""
    n = M.shape[0]
    H = sp.bmat([[None, M], [M.T, None]], format="csc")
    lu = spla.splu((H - sigma0 * sp.identity(2 * n, format="csc")).tocsc(), permc_spec="COLAMD")
    op = spla.LinearOperator(H.shape, matvec=lu.solve, dtype=float)
    ev = spla.eigsh(H, k=k, sigma=sigma0, OPinv=op, v0=dc._v0(2 * n), ncv=min(2 * n, 3 * k + 20), tol=1e-10,
                    maxiter=5000, return_eigenvectors=False)
    return np.sort(np.abs(ev))[::2]          # jedes sigma_i erscheint als +-sigma_i


def modus_kontrolle(protokoll, teile=("k1", "k2"), k2N=(4001, 16001)):
    out = {}
    if "k1" in teile:
        # (K1) Formel gegen dichte Singulaerwerte, N = 151, s = 0 und +-0,5, r = 1 und 1/2; dazu (A) und Skalar
        k1 = []
        for saat, s in ((990, 0.0), (991, 0.5), (992, -0.5), (993, 0.5)):
            N = 151
            z, L = dg.grundpunkte(N, saat)
            kvec = 2 * np.pi * np.array([1.0, 1.0]) / L
            if s != 0:
                x, _ = dg.psi(z, kvec, s, L)
                nz = dg.periodisches_netz(x, L, "koord")
                l = dg.laengen_geo(nz, kvec, s)
            else:
                nz = dg.periodisches_netz(z, L, "basis")
                l = nz.l0
            w, _ = nz.gewichte(l)
            for name, r in R_WERTE + (("W2", 2.0),):
                M = wilson_matrix(nz, l, w, r, 1.0)
                g, info = gamma_wilson(M, s == 0.0)
                gd, kl = dicht_gamma(M.toarray())
                k1.append({"N": N, "saat": saat, "s": s, "op": name, "r": r, "formel": g, "dicht": gd,
                           "abw": abs(g - gd), "kleinste_sigma_dicht": kl, "info": info,
                           "w_negativ": int(np.sum(w < 0))})
                protokoll(f"K1 N={N} s={s} {name}: Formel gegen dicht {abs(g - gd):.2e}; kleinste sigma dicht "
                          f"{np.array(kl[:4])}")
        out["K1_dicht"] = k1
    if "k2" in teile:
        # (K2) Spektrum nahe null (s = 0): kleinste Singulaerwerte von D_W fuer r = 0 (= (A)), 1/2, 1; gegen das
        #      Kontinuum eines Dirac-Fermions (sigma = 2 pi |m|/L, Vielfachheit 2 je Impuls m)
        k2 = []
        for N, saat in ((n_, s_) for n_, s_ in ((4001, 993), (16001, 994)) if n_ in k2N):
            z, L = dg.grundpunkte(N, saat)
            nz = dg.periodisches_netz(z, L, "basis")
            w, _ = nz.gewichte(nz.l0)
            mm = np.array([(i, j) for i in range(-4, 5) for j in range(-4, 5)])
            kont = np.sort(np.repeat(2 * np.pi * np.hypot(mm[:, 0], mm[:, 1]) / L, 2))[:40]
            for name, r in (("A", 0.0),) + R_WERTE:
                t0 = time.time()
                M = wilson_matrix(nz, nz.l0, w, r, 1.0)
                sv = singulaer_klein(M, 48)
                k2.append({"N": N, "saat": saat, "op": name, "r": r, "sigma": sv.tolist(),
                           "kontinuum_1_fermion": kont.tolist(), "sek": time.time() - t0})
                protokoll(f"K2 N={N} {name} (r={r}): kleinste sigma {np.round(sv[:12], 5)}; Kontinuum "
                          f"{np.round(kont[:12], 5)} ({time.time() - t0:.1f} s)")
        out["K2_spektrum"] = k2
    return out


def main():
    modus = sys.argv[1]
    t0 = time.time()
    log = []

    def protokoll(s):
        print(s, flush=True)
        log.append(s)

    import scipy
    out = {"modus": modus, "argv": sys.argv[1:], "numpy": np.__version__, "scipy": scipy.__version__}
    if modus == "kontrolle":
        ziel = sys.argv[2]
        opt = dict(a.split("=", 1) for a in sys.argv[3:])
        teile = tuple(opt.get("teil", "k1,k2").split(","))
        k2N = tuple(int(v) for v in opt.get("k2N", "4001,16001").split(","))
        out.update(modus_kontrolle(protokoll, teile, k2N))
    elif modus == "dichte":
        N, saat0, anzahl, ziel = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
        nlist = [int(x) for x in sys.argv[6].split(",")]
        S = float(sys.argv[7])
        opt = dict(a.split("=", 1) for a in sys.argv[8:])
        richt = opt.get("richtungen", "r000,r090").split(",")
        A_torus = float(opt["A"]) if "A" in opt else None
        modus_dichte(N, saat0, anzahl, ziel, nlist, S, richt, protokoll, out, A_torus, int(opt.get("a_saaten", "0")))
    else:
        raise SystemExit("unbekannter Modus")
    out["laufzeit_gesamt_s"] = time.time() - t0
    out["protokoll"] = log
    with open(ziel + ".tmp", "w") as f:
        json.dump(out, f)
    os.replace(ziel + ".tmp", ziel)
    print("geschrieben", ziel, f"{time.time() - t0:.1f} s", flush=True)


if __name__ == "__main__":
    main()
