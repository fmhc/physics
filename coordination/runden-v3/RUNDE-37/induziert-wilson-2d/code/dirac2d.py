#!/usr/bin/env python3
"""INDUZIERT-DIRAC-2D (Runde 39, Code-Agent): induzierte konforme Steifigkeit eines Fermions auf Zufallsnetzen mit
Punkten nach physikalischer Flaeche und Neuvernetzung ("Zahl = Volumen"), in zwei Bauweisen, dazu der Skalar auf
denselben Netzen und das regelmaessige Quadratnetz.

Geometrie, Abbildung psi, Netz und Laengen unveraendert aus dichte2d_grob.py (INDUZIERT-DICHTE-2D-GROB, eingefroren
20261004-091915): Torus [0, L)^2, g = e^(2 sigma) delta, sigma = s cos(k.x), Punkte nach physikalischer Flaeche,
Delaunay in Koordinaten (koord), physikalische Laengen l (geo).

Operatoren je Netz (gleiche Laengen l, Kotangens-Gewichte w aus l, Dreiecksflaechen A_T aus l):
  Skalar (B):   Gamma_B = +1/2 log det' K, K = Kotangens-Steifigkeit (wie -GROB, bitgleich: zufall2d.Netz.gamma).
  (A) naiv:     D_ij = (1/2) w_ij l_ij (gamma . n_ij) fuer jede Kante ij, D_ji = -D_ij, D_ii = 0. n_ij = Richtung der
                Kante in Koordinaten (Sehne) = Richtung im eingesetzten Rahmen e_a = e^(-sigma) d_a. (1/2) w l ist die
                halbe Voronoi-Kante (Gauss ueber die Dualzelle). gamma_1 = sigma_x, gamma_2 = sigma_z (reell) ->
                D reell antisymmetrisch, 2N x 2N.
                log|det' D| exakt ueber den geschuetzten Nullvektor (nur ungerades N, siehe gamma_dirac):
                log|det D_(0)| + log det(Gram) (Knoten 0 gestrichen, Gram der zwei Nullvektoren). Bei geradem N
                erzwingt die Antisymmetrie eine zweite exakte Nullmode; daher N = 16 001 und L ungerade.
  (B) Kaehler-Dirac: d + delta auf 0-, 1-, 2-Formen (DEC), *0 = m_i = sum_j w_ij l_ij^2/4 (zirkumzentrische
                Dualflaeche), *1 = w_e, *2 = 1/A_T. Exakt (Hodge-Zerlegung): |det'(d+delta)| = det'Delta_0 |det'Delta_2|,
                Delta_0 = *0^-1 K, Delta_2 = K_2 *2 mit K_2 = Laplace des Dualgraphen (Leitwerte 1/w_e).
                log det'Delta_0 = log det K_(0) + log sum m - sum log m = 2 Gamma_B - log N + log sum m - sum log m
                log det'Delta_2 = log|det K_2,(0)| + log sum A_T - sum log A_T
Konvention (Grassmann): Gamma_F = -log|det' D_F|. Damit hat ein Dirac-Fermion im Kontinuum dieselbe konforme
Steifigkeit wie der Skalar: c_eff = (Gamma''/(k^2 A))/P mit P = -1/(24 pi), Dirac +1, Skalar +1.
Messgroesse je k wie -GROB: D(S) = (Gamma(S) + Gamma(-S) - 2 Gamma(0))/S^2, y = D/A (A = L^2).

Aufruf (nur ueber kleintest.sh):
  python dirac2d.py kontrolle <aus.json>
  python dirac2d.py regulaer <L> <aus.json> <n-Liste> [S=0.5]
  python dirac2d.py dichte <N> <saat0> <anzahl> <aus.json> <n-Liste> <S> [A=<Torusflaeche>] [richtungen=r000,r090]
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
import zufall2d as z2      # noqa: E402  (unveraendert)

POLYAKOV = -1.0 / (24.0 * math.pi)
H_REG = 1e-2                    # Schritt (Richardson) auf dem festen regelmaessigen Netz, wie INDUZIERT-ZUFALL-2D
EIGS_K = 6                      # betragskleinste Eigenwerte von D je Netz (s != 0)
TRENN_MAX = 0.1                 # Tor: |lambda_1| = |lambda_2| <= 0,1 |lambda_3|
W_NULL = 1e-12                  # Tor (B): |w_e| > W_NULL


# ---------------------------------------------------------------------- (A) naiver Dirac-Operator
def dirac_matrix(nz, l, w):
    """Reell antisymmetrisch, 2N x 2N; Block der Kante (i, j): (1/2) w l [[n_y, n_x], [n_x, -n_y]]."""
    N = nz.N
    n = nz.ev / nz.l0[:, None]
    f = 0.5 * w * l
    nx, ny = f * n[:, 0], f * n[:, 1]
    i, j = nz.ki, nz.kj
    r = np.concatenate([2 * i, 2 * i, 2 * i + 1, 2 * i + 1, 2 * j, 2 * j, 2 * j + 1, 2 * j + 1])
    c = np.concatenate([2 * j, 2 * j + 1, 2 * j, 2 * j + 1, 2 * i, 2 * i + 1, 2 * i, 2 * i + 1])
    v = np.concatenate([ny, nx, nx, -ny, -ny, -nx, -nx, ny])
    return sp.csc_matrix((v, (r, c)), shape=(2 * N, 2 * N))


def _v0(n):
    return 1.0 + np.cos(0.37 * np.arange(n)) + 0.5 * np.sin(1.13 * np.arange(n))


def gamma_dirac(nz, l, w):
    """Gamma_A = -log|det' D| [M]: In der Darstellung zeta = a + i b je Knoten wirkt D antilinear,
    zeta -> (i/2) conj(G zeta) mit G_ij = w_ij d_ij (komplexer Kantenvektor), G komplex antisymmetrisch (N x N).
    Bei ungeradem N hat G fuer jedes s genau einen (geschuetzten) Nullvektor, die Fortsetzung der konstanten Spinoren;
    D hat dann genau zwei reelle Nullmoden. Exakt (Jacobi, D normal): |det' D| = |det D_(0)| det(Gram), D_(0) ohne die
    zwei Zeilen und Spalten von Knoten 0, Gram = V^T V der Nullvektoren v_k mit v_k(Knoten 0) = e_k."""
    t0 = time.time()
    N = nz.N
    if N % 2 == 0:
        raise SystemExit("N muss ungerade sein (bei geradem N erzwingt die Antisymmetrie von G eine zweite Nullmode)")
    D = dirac_matrix(nz, l, w)
    D0 = D[2:, 2:].tocsc()
    lu = spla.splu(D0, permc_spec="COLAMD")
    d = lu.U.diagonal()
    logabs = math.fsum(np.log(np.abs(d)).tolist())
    B = D[2:, :2].toarray()
    X = lu.solve(-B)
    V = np.vstack([np.eye(2), X])
    gram = V.T @ V
    sgn, ldg = np.linalg.slogdet(gram)
    res = np.linalg.norm(D @ V, axis=0) / (np.linalg.norm(V, axis=0) * max(float(np.max(np.abs(D.data))), 1e-300))
    ld = logabs + ldg
    info = {"min_abs_U": float(np.min(np.abs(d))), "logabs_D0": logabs, "log_det_gram": float(ldg),
            "gram": gram.tolist(), "gram_komplex_abw": float(abs(gram[0, 0] - gram[1, 1]) + abs(gram[0, 1])),
            "nullvektor_residuum": float(np.max(res)), "endlich": bool(np.isfinite(ld) and sgn > 0),
            "sek": time.time() - t0}
    return -ld, info


# ---------------------------------------------------------------------- (B) Kaehler-Dirac (DEC)
def dual_paare(nz):
    order = np.argsort(nz.tk.ravel(), kind="stable")
    tr = (order // 3).reshape(-1, 2)
    return tr[:, 0], tr[:, 1]


def gamma_kd(nz, l, w, AT, gB):
    """Gamma_KD = -log|det'(d + delta)| = -log det'Delta_0 - log|det'Delta_2| (exakte Zerlegung)."""
    t0 = time.time()
    N, F = nz.N, nz.F
    m = np.bincount(nz.ki, 0.25 * w * l * l, N) + np.bincount(nz.kj, 0.25 * w * l * l, N)
    info = {"m_min": float(np.min(m)), "w_betrag_min": float(np.min(np.abs(w))), "w_negativ": int(np.sum(w < 0))}
    ok = bool(np.all(m > 0) and np.all(np.abs(w) > W_NULL) and np.all(AT > 0))
    info["ok_eingang"] = ok
    sum_log_m = math.fsum(np.log(np.abs(m)).tolist())
    sum_log_A = math.fsum(np.log(np.abs(AT)).tolist())
    ld0 = 2.0 * gB - math.log(N) + math.log(math.fsum(m.tolist())) - sum_log_m
    t1, t2 = dual_paare(nz)
    g = 1.0 / w
    diag = np.bincount(t1, g, F) + np.bincount(t2, g, F)
    K2 = sp.csc_matrix((np.concatenate([-g, -g, diag]),
                        (np.concatenate([t1, t2, np.arange(F)]), np.concatenate([t2, t1, np.arange(F)]))),
                       shape=(F, F))
    lu = spla.splu(K2[1:, 1:].tocsc(), permc_spec="COLAMD")
    d = lu.U.diagonal()
    ld2 = math.fsum(np.log(np.abs(d)).tolist()) + math.log(math.fsum(AT.tolist())) - sum_log_A
    info.update({"min_abs_U2": float(np.min(np.abs(d))), "sum_log_m": sum_log_m, "sum_log_A": sum_log_A,
                 "logdet_Delta0": ld0, "logdet_Delta2": ld2, "endlich": bool(np.isfinite(ld0 + ld2)),
                 "sek": time.time() - t0})
    return {"KD": -(ld0 + ld2), "KD0": -ld0, "KD2": -ld2, "lokal_m": sum_log_m, "lokal_A": sum_log_A}, info


# ---------------------------------------------------------------------- alle Operatoren auf einem Netz
def alle(nz, l, s0, mit_kd=True):
    w, AT = nz.gewichte(l)
    gB = nz.gamma(l)
    gA, ia = gamma_dirac(nz, l, w)
    out = {"B": gB, "A": gA, "info_A": ia}
    if mit_kd:
        kd, ik = gamma_kd(nz, l, w, AT, gB)
        out.update(kd)
        out["info_KD"] = ik
    return out


OPS = ("B", "A", "KD", "KD0", "KD2", "lokal_m", "lokal_A")


# ---------------------------------------------------------------------- Modus dichte (Zufallsnetze, Neuvernetzung)
def modus_dichte(N, saat0, anzahl, ziel, nlist, S, richtungen, protokoll, out, A_torus=None):
    A_torus = float(N) if A_torus is None else float(A_torus)
    out.update({"N": N, "L": math.sqrt(A_torus), "A": A_torus, "nlist": nlist, "S": [S], "richtungen": richtungen,
                "saaten": []})
    for saat in range(saat0, saat0 + anzahl):
        t0 = time.time()
        z, L = dg.grundpunkte(N, saat, math.sqrt(A_torus))
        n0 = dg.periodisches_netz(z, L, "basis")
        p0 = dg.netz_pruefen(n0, n0.l0)
        p0_z2 = n0.pruefen()
        g0 = alle(n0, n0.l0, True)
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
                    g = alle(nz, lk, False)
                    g.update({"psi": pinfo, "pruefung": pk, "neue_kanten": dg.neue_kanten(nz, sch0),
                              "lu_B": dict(nz.lu_info), "sek": time.time() - ts})
                    seiten[name] = g
                e = {"S": S, "plus": seiten["plus"], "minus": seiten["minus"]}
                for op in OPS:
                    Dv = (seiten["plus"][op] + seiten["minus"][op] - 2 * g0[op]) / (S * S)
                    e["D_" + op] = Dv
                    e["y_" + op] = Dv / A_torus
                pts.append({"richtung": rn, "n": n, "kint": list(kint), "betrag": kb, "k2A": kb * kb * A_torus,
                            "je_S": [e]})
                protokoll(f"N={N} A={A_torus:.0f} saat={saat} {rn} n={n}: Nullvektor-Residuum "
                          f"{max(seiten['plus']['info_A']['nullvektor_residuum'], seiten['minus']['info_A']['nullvektor_residuum']):.1e}"
                          f" Gram-Abw {max(seiten['plus']['info_A']['gram_komplex_abw'], seiten['minus']['info_A']['gram_komplex_abw']):.1e}"
                          f" wneg {seiten['plus']['info_KD']['w_negativ']} {seiten['plus']['sek']:.1f}s")
        out["saaten"].append({"saat": saat, "gamma0": g0, "pruefung0": p0, "pruefung0_z2": p0_z2,
                              "lu0_B": dict(n0.lu_info), "punkte": pts, "sekunden": time.time() - t0})
        with open(ziel + ".tmp", "w") as f:
            json.dump(out, f)
        os.replace(ziel + ".tmp", ziel)
        protokoll(f"N={N} saat={saat} fertig in {time.time() - t0:.1f} s")
    return out


# ---------------------------------------------------------------------- Modus regulaer (festes Quadratnetz)
def modus_regulaer(L, nlist, S, protokoll, out):
    """Festes regelmaessiges Netz (Quadrate mit (1,1)-Diagonale, L ungerade: Doppler ohne Nullmoden), konforme Mode
    ueber die physikalischen Laengen (geo) auf festem Netz; Richardson h = 0,01 (Urteil) und S-Schema (beschreibend)."""
    nr = z2.regulaeres_netz(L)
    pr = nr.pruefen()
    A = float(L * L)
    g0 = alle(nr, nr.l0, True, mit_kd=False)
    pts = []
    for rn in ("r000", "r090"):
        r = dg.RICHTUNGEN[rn]
        for n in nlist:
            kvec = 2 * np.pi * np.array([n * r[0], n * r[1]], dtype=float) / L
            kb = float(np.linalg.norm(kvec))
            werte = {}
            for sv in (H_REG, -H_REG, 2 * H_REG, -2 * H_REG, S, -S):
                werte[sv] = alle(nr, dg.laengen_geo(nr, kvec, sv), False, mit_kd=False)
            pt = {"richtung": rn, "n": n, "betrag": kb, "k2A": kb * kb * A}
            for op in ("B", "A"):
                f = {sv: werte[sv][op] for sv in werte}
                D1 = (f[H_REG] + f[-H_REG] - 2 * g0[op]) / H_REG ** 2
                D2 = (f[2 * H_REG] + f[-2 * H_REG] - 2 * g0[op]) / (4 * H_REG ** 2)
                R = (4 * D1 - D2) / 3.0
                DS = (f[S] + f[-S] - 2 * g0[op]) / S ** 2
                pt[op] = {"gamma2": R, "D_h": D1, "D_2h": D2, "richardson_abw_rel": abs(D1 - R) / max(abs(R), 1e-300),
                          "c": R / (kb * kb * A), "c_eff": R / (kb * kb * A) / POLYAKOV,
                          "D_S": DS, "c_S": DS / (kb * kb * A), "c_eff_S": DS / (kb * kb * A) / POLYAKOV}
            pt["info_A"] = {str(sv): werte[sv]["info_A"] for sv in werte}
            pts.append(pt)
            protokoll(f"regulaer L={L} {rn} n={n}: c_eff B {pt['B']['c_eff']:+.4f} A {pt['A']['c_eff']:+.4f} "
                      f"(S-Schema B {pt['B']['c_eff_S']:+.4f} A {pt['A']['c_eff_S']:+.4f}); Richardson-Abw "
                      f"{pt['A']['richardson_abw_rel']:.1e}; Nullvektor-Residuum "
                      f"{max(werte[sv]['info_A']['nullvektor_residuum'] for sv in werte):.1e}")
    out.update({"L": L, "N": L * L, "A": A, "pruefung": pr, "gamma0": g0, "punkte": pts, "S": S, "h": H_REG,
                "lu_B": dict(nr.lu_info)})
    return out


# ---------------------------------------------------------------------- Modus kontrolle (dichte Pruefungen)
def dichte_formen(nz, l):
    """Dichte Matrizen d0 (E x N), d1 (F x E) und Hodge-Sterne fuer kleine Netze."""
    N, E, F = nz.N, nz.E, nz.F
    d0 = np.zeros((E, N))
    d0[np.arange(E), nz.ki] = -1.0
    d0[np.arange(E), nz.kj] = 1.0
    d1 = np.zeros((F, E))
    tri = nz.tri
    for loc, (u, v) in enumerate(((1, 2), (2, 0), (0, 1))):     # Kante gegenueber Ecke loc: tri[u] -> tri[v]
        e = nz.tk[:, loc]
        sgn = np.where(nz.ki[e] == tri[:, u], 1.0, -1.0)
        d1[np.arange(F), e] = sgn
    w, AT = nz.gewichte(l)
    m = np.bincount(nz.ki, 0.25 * w * l * l, N) + np.bincount(nz.kj, 0.25 * w * l * l, N)
    return d0, d1, w, AT, m


def modus_kontrolle(protokoll):
    out = {}
    # (K1) KD-Zerlegung und (A)-Erdung gegen dichte Eigenwerte, kleine Netze (N = 150), s = 0 und s = 0,5
    k1 = []
    for saat, s in ((990, 0.0), (991, 0.5), (992, -0.5)):
        N = 151
        z, L = dg.grundpunkte(N, saat)
        kvec = 2 * np.pi * np.array([1.0, 1.0]) / L
        x, _ = dg.psi(z, kvec, s, L) if s != 0 else (z, None)
        nz = dg.periodisches_netz(x, L, "koord")
        l = dg.laengen_geo(nz, kvec, s) if s != 0 else nz.l0
        d0, d1, w, AT, m = dichte_formen(nz, l)
        g = alle(nz, l, s == 0.0)
        # d + delta dicht
        s0, s1, s2 = np.diag(m), np.diag(w), np.diag(1.0 / AT)
        de1 = np.linalg.solve(s0, d0.T @ s1)                 # delta_1 = *0^-1 d0^T *1
        de2 = np.linalg.solve(s1, d1.T @ s2)                 # delta_2 = *1^-1 d1^T *2
        Ntot = nz.N + nz.E + nz.F
        KD = np.zeros((Ntot, Ntot))
        a, b = nz.N, nz.N + nz.E
        KD[:a, a:b] = de1
        KD[a:b, :a] = d0
        KD[a:b, b:] = de2
        KD[b:, a:b] = d1
        ev = np.linalg.eigvals(KD)
        ev = ev[np.argsort(np.abs(ev))]
        ld_dicht = math.fsum(np.log(np.abs(ev[4:])).tolist())
        Q = KD @ KD
        blockfehler = max(np.max(np.abs(Q[:a, a:])), np.max(np.abs(Q[a:b, :a])), np.max(np.abs(Q[a:b, b:])),
                          np.max(np.abs(Q[b:, :b])))
        d1d0 = float(np.max(np.abs(d1 @ d0)))
        # (A) dicht
        Dd = dirac_matrix(nz, l, w).toarray()
        eva = np.linalg.eigvals(Dd)
        eva = eva[np.argsort(np.abs(eva))]
        ldA_dicht = math.fsum(np.log(np.abs(eva[2:])).tolist())
        k1.append({"N": nz.N, "saat": saat, "s": s, "kd_formel": -g["KD"], "kd_dicht": ld_dicht,
                   "kd_abw": abs(-g["KD"] - ld_dicht), "kd_nullmoden_betrag": np.abs(ev[:5]).tolist(),
                   "quadrat_blockfehler": float(blockfehler), "d1d0": d1d0,
                   "A_formel": -g["A"], "A_dicht": ldA_dicht, "A_abw": abs(-g["A"] - ldA_dicht),
                   "A_kleinste": np.abs(eva[:6]).tolist(), "antisym": float(np.max(np.abs(Dd + Dd.T))),
                   "w_negativ": int(np.sum(w < 0))})
        protokoll(f"K1 N={nz.N} s={s}: KD Formel gegen dicht {k1[-1]['kd_abw']:.2e} (Nullmoden "
                  f"{np.abs(ev[:5])}), (d+delta)^2 Blockfehler {blockfehler:.1e}, d1 d0 {d1d0:.0e}; A Formel gegen "
                  f"dicht {k1[-1]['A_abw']:.2e}, kleinste |lambda| {np.abs(eva[:4])}")
    out["K1_dicht"] = k1
    # (K1b) Paritaet: bei geradem N hat D (s = 0) vier exakte Nullmoden, bei ungeradem zwei
    k1b = []
    for N, saat in ((150, 990), (151, 990), (152, 995), (153, 995)):
        z, L = dg.grundpunkte(N, saat)
        nz = dg.periodisches_netz(z, L, "koord")
        w, _ = nz.gewichte(nz.l0)
        eva = np.sort(np.abs(np.linalg.eigvals(dirac_matrix(nz, nz.l0, w).toarray())))
        k1b.append({"N": N, "nullmoden_1e-9": int(np.sum(eva < 1e-9)), "kleinste": eva[:6].tolist()})
        protokoll(f"K1b N={N}: Nullmoden von D (|lambda| < 1e-9): {k1b[-1]['nullmoden_1e-9']}")
    out["K1b_paritaet"] = k1b
    # (K2) regelmaessiges Netz: naive Doppler im Spektrum (L gerade: 8 Nullmoden; L ungerade: 2), gegen sin-Formel
    k2 = []
    for L in (8, 9):
        nr = z2.regulaeres_netz(L)
        w, _ = nr.gewichte(nr.l0)
        Dd = dirac_matrix(nr, nr.l0, w).toarray()
        ev = np.sort(np.abs(np.linalg.eigvals(Dd)))
        p = 2 * np.pi * np.arange(L) / L
        px, py = np.meshgrid(p, p, indexing="ij")
        soll = np.sort(np.repeat(np.sqrt(np.sin(px) ** 2 + np.sin(py) ** 2).ravel(), 2))
        k2.append({"L": L, "max_abw_sin": float(np.max(np.abs(ev - soll))), "nullmoden": int(np.sum(ev < 1e-9)),
                   "w_diagonal_max": float(np.max(np.abs(w[np.abs(np.abs(nr.ev[:, 0]) - np.abs(nr.ev[:, 1])) < 1e-9])))})
        protokoll(f"K2 regulaer L={L}: Spektrum gegen sqrt(sin^2 px + sin^2 py) {k2[-1]['max_abw_sin']:.1e}, "
                  f"Nullmoden {k2[-1]['nullmoden']}")
    out["K2_regulaer"] = k2
    # (K3) Zufallsnetz N = 4000: tiefstes Spektrum von D (s = 0, geerdet ueber Verschiebung) gegen das Kontinuum eines
    #      einzelnen Dirac-Fermions (|lambda| = (A/N) 2 pi |m|/L, Vielfachheit 2 je Impuls m) -- Doppler-Zaehler
    k3 = []
    for N, saat in ((4001, 993), (16001, 994)):
        z, L = dg.grundpunkte(N, saat)
        nz = dg.periodisches_netz(z, L, "basis")
        w, _ = nz.gewichte(nz.l0)
        D = dirac_matrix(nz, nz.l0, w)
        sig = 1e-3
        lu = spla.splu((D - sig * sp.identity(2 * N, format="csc")).tocsc(), permc_spec="COLAMD")
        op = spla.LinearOperator(D.shape, matvec=lu.solve, dtype=float)
        ev = spla.eigs(D, k=40, sigma=sig, OPinv=op, v0=_v0(2 * N), ncv=100, tol=1e-10, maxiter=5000,
                       return_eigenvectors=False)
        a = np.sort(np.abs(ev))
        mm = np.array([(i, j) for i in range(-4, 5) for j in range(-4, 5)])
        kont = np.sort(np.repeat(2 * np.pi * np.hypot(mm[:, 0], mm[:, 1]) / L, 2))[:40]
        k3.append({"N": N, "saat": saat, "betrag": a.tolist(), "kontinuum_1_fermion": kont.tolist(),
                   "verhaeltnis": (a[2:24] / kont[2:24]).tolist()})
        protokoll(f"K3 Zufallsnetz N={N}: |lambda|/Kontinuum (ein Fermion) fuer die Stufen 1 bis 2: "
                  f"{np.round(a[2:24] / kont[2:24], 3)}")
    out["K3_spektrum"] = k3
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
        out.update(modus_kontrolle(protokoll))
    elif modus == "regulaer":
        L, ziel = int(sys.argv[2]), sys.argv[3]
        nlist = [int(x) for x in sys.argv[4].split(",")]
        opt = dict(a.split("=", 1) for a in sys.argv[5:])
        modus_regulaer(L, nlist, float(opt.get("S", "0.5")), protokoll, out)
    elif modus == "dichte":
        N, saat0, anzahl, ziel = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
        nlist = [int(x) for x in sys.argv[6].split(",")]
        S = float(sys.argv[7])
        opt = dict(a.split("=", 1) for a in sys.argv[8:])
        richt = opt.get("richtungen", "r000,r090").split(",")
        A_torus = float(opt["A"]) if "A" in opt else None
        modus_dichte(N, saat0, anzahl, ziel, nlist, S, richt, protokoll, out, A_torus)
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
