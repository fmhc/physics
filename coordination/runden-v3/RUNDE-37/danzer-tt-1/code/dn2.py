#!/usr/bin/env python3
"""DANZER-NAEHERUNG-2 (Runde 47, Code-Agent fuer die Leitung claude-primary).

Dieselben Ammann-Kramer-Naeherungen wie DANZER-NAEHERUNG-1 (Bau unveraendert aus danzer_naeherung.py: Fenster,
Saaten, Fenster-Stoerung gamma, Zitter, periodisches Delaunay), dazu 5/3. Neu sind die Gewichte: umkreisbasierte,
vorzeichenbehaftete Hodge-Sterne genau nach TAKT-UMKLAPP-1 (tu.py: umkreis_tet, umkreis_drei, einheit, hodge):
  S  Skalar:  d0^H *1 d0 phi = omega^2 *0 phi
  M  Maxwell: d1^H *2 d1 a   = omega^2 *1 a      (Coulomb-Phase)
Kanten mit *1 = 0 (Gleichstand) tragen keine Masse. Sie werden statisch kondensiert: Die aktiven Dreiecke (*2 != 0) an
einer solchen Kante liegen auf einem gemeinsamen Kreis und haben dieselbe duale Laenge L*; sie werden zum Vieleck
verschmolzen (*2 = L* / Vieleckflaeche). Das ist das exakte Minimum der Energie ueber die masselosen Kanten (Kontrolle
"kondensation" im Code). Dreiecke mit *2 = 0 fallen heraus.
Messung wie DANZER-NAEHERUNG-1: 40 Halbkugel-Richtungen, Fenster [0,03; 0,12] pi/L (8 Punkte), licht_netz.fit mit
geraden Potenzen bis 6, harmonische Zerlegung danzer_naeherung.zerlegen (beta = Koeffizient von S4).
Eigenwerte: Rayleigh-Ritz in einer k.p-Basis (Skalar bis Ordnung 6, Maxwell bis 4 wie DANZER-NAEHERUNG-1);
omega = Singulaerwert von B(k) S mit K = B^H B. Gegenprobe gegen exakte Eigenwerte.

Aufruf (nur ueber kleintest.sh):
  python dn2.py rauch <aus.json> <ordnungen, z.B. 1/1,2/1> [--saaten 0,1] [--zeit]
  python dn2.py rechnen <p/q> <ops: S,M> <saaten> <aus.json> [--probe] [--zitter-kontrolle] [--einheit] [--richtungen 40]
  python dn2.py auswerten <aus.json> <bild.png> <dn1-auswertung.json> <ein1.json> [<ein2.json> ...]
"""
import hashlib
import json
import math
import os
import sys
import time

import numpy as np
import scipy
import scipy.sparse as sps
import scipy.sparse.linalg as spla
from scipy.sparse.csgraph import connected_components
from scipy.spatial import Delaunay, cKDTree

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import licht_netz as ln  # noqa: E402  Bloch-Werkzeug LICHT-FINN-NETZ-1 (unveraendert)
import danzer_naeherung as dn  # noqa: E402  Bau und Messung DANZER-NAEHERUNG-1 (unveraendert)

REIHE = ["1/1", "2/1", "3/2", "5/3"]
TOL_NULL = 1e-9          # |*1| bzw. |*2| <= TOL_NULL * max = null (wie DANZER-NAEHERUNG-1)
S_LAENGS = 4.0           # Laengsmoden bei S_LAENGS * omega_skalar^2 (trennt sie von den Photonen, beide c = 1)
MMAX_S = 6               # k.p-Ordnung Skalar
MMAX_M = 4               # k.p-Ordnung Maxwell (wie DANZER-NAEHERUNG-1)
MU_RITZ = 1e-9
D20_SCHWELLE = 1e-10     # Karte D2-0
D21_DRITTEL = 1.0 / 3.0  # Karte D2-1
D22_FAKTOR = 0.6         # Karte D2-2
ORDNUNG_PERMC = "MMD_AT_PLUS_A"

# ------------------------------------------------------------------ aus TAKT-UMKLAPP-1 (tu.py, tg.py, uk.py), woertlich
PAARE = [(0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2), (1, 2, 0, 3), (1, 3, 0, 2), (2, 3, 0, 1)]   # tg.PAARE
FL = np.array([[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]])                                # uk.FL (gegenueber Ecke i)


def einheit(v):
    return v / np.linalg.norm(v, axis=-1)[..., None]


def umkreis_tet(X):
    Y = X - X[:, :1]
    A = 2.0 * Y[:, 1:]
    b = (Y[:, 1:] ** 2).sum(-1)
    return X[:, 0] + np.linalg.solve(A, b[..., None])[..., 0]


def umkreis_drei(P0, P1, P2):
    a, b = P0 - P2, P1 - P2
    axb = np.cross(a, b)
    num = np.cross((a * a).sum(-1)[..., None] * b - (b * b).sum(-1)[..., None] * a, axb)
    return P2 + num / (2.0 * (axb * axb).sum(-1))[..., None]


def hodge_tu(X, vid, eidx, fidx, E, F, V, laengen):
    """tu.hodge, Rechenweg woertlich; nur die Indizes (Kante je Paar, Flaeche je Gegenecke) kommen aus diesem Netz.
    *1 = duale Flaeche / Kantenlaenge, *2 = duale Laenge / Dreiecksflaeche, *0 = duales Volumen je Ecke."""
    T = len(X)
    ct = umkreis_tet(X)
    Ast = np.zeros((T, 6))
    lt = np.zeros((T, 6))
    for p, (i, j, k, l) in enumerate(PAARE):
        Xi, Xj, Xk, Xl = X[:, i], X[:, j], X[:, k], X[:, l]
        m = 0.5 * (Xi + Xj)
        e = einheit(Xj - Xi)
        hs, hh = [], []
        for Xo, Xa in ((Xk, Xl), (Xl, Xk)):
            u = (Xo - Xi) - ((Xo - Xi) * e).sum(-1)[:, None] * e
            u = einheit(u)
            cf = umkreis_drei(Xi, Xj, Xo)
            hs.append(((cf - m) * u).sum(-1))
            nrm = np.cross(Xj - Xi, Xo - Xi)
            nrm = einheit(nrm * np.sign((nrm * (Xa - Xi)).sum(-1))[:, None])
            hh.append(((ct - cf) * nrm).sum(-1))
        Ast[:, p] = 0.5 * (hs[0] * hh[0] + hs[1] * hh[1])
        lt[:, p] = np.linalg.norm(Xj - Xi, axis=1)
    A1 = np.bincount(eidx.ravel(), Ast.ravel(), E)
    s1 = A1 / laengen
    s0 = np.zeros(V)
    for p, (i, j, k, l) in enumerate(PAARE):
        w = lt[:, p] * Ast[:, p] / 6.0
        s0 += np.bincount(vid[:, i], w, V) + np.bincount(vid[:, j], w, V)
    hf = np.zeros((T, 4))
    af = np.zeros((T, 4))
    for i in range(4):
        a_, b_, c_ = [X[:, q] for q in FL[i]]
        cf = umkreis_drei(a_, b_, c_)
        nrm = np.cross(b_ - a_, c_ - a_)
        af[:, i] = 0.5 * np.linalg.norm(nrm, axis=1)
        nrm = einheit(nrm * np.sign((nrm * (X[:, i] - a_)).sum(-1))[:, None])
        hf[:, i] = ((ct - cf) * nrm).sum(-1)
    L2 = np.bincount(fidx.ravel(), hf.ravel(), F)            # Summe ueber die zwei Tetraeder je Flaeche (uk.flaechen)
    fa = np.zeros(F)
    fa[fidx.ravel()] = af.ravel()
    s2 = L2 / fa
    return s0, s1, s2, A1, L2, fa, Ast


# ------------------------------------------------------------------ Netz (Bau aus danzer_naeherung.netz, erweitert)
def sha_arr(a):
    return hashlib.sha256(np.ascontiguousarray(a).tobytes()).hexdigest()


def vorzeichen(x, rel):
    sk = max(float(np.max(np.abs(x))), 1e-300)
    return {"min": float(np.min(x)), "max": float(np.max(x)), "negativ": int(np.sum(x < -rel * sk)),
            "null": int(np.sum(np.abs(x) <= rel * sk)), "positiv": int(np.sum(x > rel * sk))}


def netz2(nh, saat, zitter_versatz=0, dn1_sterne=None):
    """Wie danzer_naeherung.netz (gleiche Saaten, gleicher Zufallsstrom, gleiche Kanten- und Flaechennummern), dazu
    Tetraeder-Indizes und Hodge-Sterne nach tu.py. zitter_versatz != 0: gleiche Fenster-Stoerung gamma (gleiche Ecken),
    anderer Zitter (andere Aufloesung der Kugel-Gleichstaende)."""
    t0 = time.time()
    p, q = nh["p"], nh["q"]
    rng = dn.saat_rng(nh["ordnung"], saat)
    xi = rng.normal(size=3)
    xi /= np.linalg.norm(xi)
    gamma = dn.ETA * xi
    ek = dn.ecken(nh, gamma)
    rh = dn.rhomboeder(nh, ek, gamma)
    r, L, N = ek["r"], nh["L"], ek["N"]
    rz = rng if zitter_versatz == 0 else np.random.default_rng([3746, p, q, int(saat), 1000 + int(zitter_versatz)])
    rj = r + dn.SIGMA_D * rz.normal(size=r.shape)
    big = (rj[None, :, :] + L * dn.OFFS[:, None, :]).reshape(-1, 3)
    tri = Delaunay(big)
    S = tri.simplices
    cent = big[S].mean(axis=1)
    S = S[np.all((cent >= 0.0) & (cent < L), axis=1)]
    vid, off = S % N, dn.OFFS[S // N]
    T = len(S)
    kanten, flaechen, fl_tet = {}, {}, {}
    eidx = np.zeros((T, 6), dtype=np.int64)
    fidx = np.zeros((T, 4), dtype=np.int64)
    X = r[vid] + L * off
    vols = np.einsum("ti,ti->t", np.cross(X[:, 1] - X[:, 0], X[:, 2] - X[:, 0]), X[:, 3] - X[:, 0]) / 6.0
    for t in range(T):
        vs, os_ = vid[t], off[t]
        for pnr, (u, w, _, _) in enumerate(PAARE):       # gleiche Reihenfolge wie itertools.combinations(range(4), 2)
            key = dn.kanten_key(vs[u], os_[u], vs[w], os_[w])[0]
            if key not in kanten:
                kanten[key] = len(kanten)
            eidx[t, pnr] = kanten[key]
        for i in (3, 2, 1, 0):                              # FL[3], FL[2], FL[1], FL[0] = combinations(range(4), 3)
            d3 = FL[i]
            key = dn.flaechen_key(vs[d3], os_[d3])
            if key not in flaechen:
                flaechen[key] = len(flaechen)
            fl_tet[key] = fl_tet.get(key, 0) + 1
            fidx[t, i] = flaechen[key]
    V, Ek, F = N, len(kanten), len(flaechen)
    kl = sorted(kanten.items(), key=lambda kv: kv[1])
    ei = np.array([k[0] for k, _ in kl])
    ej = np.array([k[1] for k, _ in kl])
    ed = np.array([k[2] for k, _ in kl], dtype=float)
    D = r[ej] + L * ed - r[ei]
    rmid = r[ei] + 0.5 * D
    laengen = np.linalg.norm(D, axis=1)
    bI = np.concatenate([ei, ej])
    bJ = np.concatenate([ej, ei])
    bD = np.concatenate([D, -D])
    deg = np.bincount(bI, minlength=V).astype(float)
    rowC, colC, sgnC, relC = [], [], [], []
    fl_area = np.zeros(F)
    fl_normal = np.zeros((F, 3))
    for key, f in flaechen.items():
        vs = [v for v, _ in key]
        os_ = [np.array(o, dtype=np.int64) for _, o in key]
        Q = np.array([r[vs[u]] + L * os_[u] for u in range(3)])
        rf = Q.mean(axis=0)
        nv = np.cross(Q[1] - Q[0], Q[2] - Q[0])
        fl_area[f] = 0.5 * np.linalg.norm(nv)
        fl_normal[f] = nv / np.linalg.norm(nv)
        for u, w in ((0, 1), (1, 2), (2, 0)):
            kk, sg, sh = dn.kanten_key(vs[u], os_[u], vs[w], os_[w])
            e = kanten[kk]
            rowC.append(f)
            colC.append(e)
            sgnC.append(sg)
            relC.append(rmid[e] + L * np.asarray(sh, float) - rf)
    rowG = np.concatenate([np.arange(Ek), np.arange(Ek)])
    colG = np.concatenate([ei, ej])
    sgnG = np.concatenate([-np.ones(Ek), np.ones(Ek)])
    relG = np.concatenate([r[ei] - rmid, r[ej] + L * ed - rmid])
    bau = {"V": V, "E": Ek, "F": F, "bI": bI, "bJ": bJ, "bD": bD, "deg": deg,
           "C": (np.array(rowC), np.array(colC), np.array(sgnC, float), np.array(relC)),
           "G": (rowG, colG, sgnG, relG),
           "ei": ei, "ej": ej, "ed": ed, "Dvec": D, "rmid": rmid, "laengen": laengen, "r": r, "L": L}
    # Kontrollen wie danzer_naeherung.netz; Delaunay-Leerkugel vektorisiert
    A = sps.coo_matrix((np.ones(Ek), (ei, ej)), shape=(V, V))
    ncomp = int(connected_components(A + A.T, directed=False)[0])
    voll = list(fl_tet.values())
    bigE = (r[None, :, :] + L * dn.OFFS[:, None, :]).reshape(-1, 3)
    baum = cKDTree(bigE)
    ct = umkreis_tet(X)
    R = np.linalg.norm(ct - X[:, 0], axis=1)
    idxs = baum.query_ball_point(ct, R * (1 + 1e-9))
    verletzt, kugel_entartet = 0, 0
    for t in range(T):
        dist = np.linalg.norm(bigE[idxs[t]] - ct[t], axis=1)
        verletzt += int(np.sum(dist < R[t] * (1 - 1e-9)))
        kugel_entartet += int(max(0, np.sum(np.abs(dist - R[t]) <= 1e-9 * R[t]) - 4))
    flach = int(np.sum(np.abs(vols) < 1e-10))
    # Hodge-Sterne nach tu.py
    s0, s1, s2, A1, L2, fa, Ast = hodge_tu(X, vid, eidx, fidx, Ek, F, V, laengen)
    Vol = L ** 3
    T1 = (s1[:, None, None] * D[:, :, None] * D[:, None, :]).sum(0)
    T2 = ((L2 * fa)[:, None, None] * fl_normal[:, :, None] * fl_normal[:, None, :]).sum(0)
    identitaet = {"T1_durch_Vol_minus_I_max": float(np.max(np.abs(T1 / Vol - np.eye(3)))),
                  "T2_durch_Vol_minus_I_max": float(np.max(np.abs(T2 / Vol - np.eye(3)))),
                  "sum_s0_durch_Vol": float(s0.sum() / Vol),
                  "sum_lA_durch_3Vol": float((laengen * A1).sum() / (3 * Vol)),
                  "sum_fL_durch_3Vol": float((fa * L2).sum() / (3 * Vol)),
                  "flaeche_gegen_tu_max": float(np.max(np.abs(fa - fl_area)))}
    # Abschluss der dualen Zellen (Voronoi-Schluss): sum_e *1_e (+-l_e) je Ecke = 0
    schluss = np.zeros((V, 3))
    np.add.at(schluss, ei, s1[:, None] * D)
    np.add.at(schluss, ej, -s1[:, None] * D)
    identitaet["dualzelle_schluss_max"] = float(np.max(np.abs(schluss)))
    pruef = {"N": V, "N_erwartet": ek["N_erwartet"], "E": Ek, "F": F, "T": T, "euler": V - Ek + F - T,
             "zusammenhang_komponenten": ncomp, "flaechen_mit_2_tetraedern": int(sum(1 for c in voll if c == 2)),
             "flaechen_sonst": int(sum(1 for c in voll if c != 2)),
             "vol_rel_abw": float(abs(np.sum(np.abs(vols)) - Vol) / Vol),
             "vol_min": float(np.min(np.abs(vols))), "vol_max": float(np.max(np.abs(vols))),
             "tetraeder_flach_1e-10": flach, "delaunay_verletzt": int(verletzt),
             "kugel_entartet_zusatzpunkte": int(kugel_entartet),
             "grad_min": int(deg.min()), "grad_max": int(deg.max()),
             "stern0": vorzeichen(s0, TOL_NULL), "stern1": vorzeichen(s1, TOL_NULL), "stern2": vorzeichen(s2, TOL_NULL),
             "stern1_tu_schwelle_1e-12": vorzeichen(s1, 1e-12), "stern2_tu_schwelle_1e-12": vorzeichen(s2, 1e-12),
             "identitaeten": identitaet, "gamma": gamma.tolist(), "zitter_versatz": int(zitter_versatz),
             "fenster": {k: v for k, v in ek.items() if k not in ("x6", "r")}, "rhomboeder": rh,
             "ecken_sha": sha_arr(ek["x6"]),
             "s0_sortiert_sha": sha_arr(np.round(np.sort(s0) / Vol * V, 9)),
             "s1_positiv_sortiert_sha": sha_arr(np.round(np.sort(s1[np.abs(s1) > TOL_NULL * np.abs(s1).max()]), 9)),
             "s0_min_max": [float(s0.min()), float(s0.max())]}
    # Gegenprobe: Sterne aus der Schleife von danzer_naeherung.netz (nur kleine Netze)
    if dn1_sterne and zitter_versatz == 0:
        st1 = dn1_stern_werte(nh, saat)
        if len(st1[0]) == Ek and len(st1[1]) == F:
            pruef["sterne_tu_gegen_dn1_schleife"] = {"s1_max_abw": float(np.max(np.abs(st1[0] - s1))),
                                                     "s2_max_abw": float(np.max(np.abs(st1[1] - s2)))}
        else:
            pruef["sterne_tu_gegen_dn1_schleife"] = {"fehler": "andere Kanten- oder Flaechenzahl"}
    pruef["zeit_s"] = time.time() - t0
    dec = {"s0": s0, "s1": s1, "s2": s2, "L2": L2, "fa": fa, "normal": fl_normal}
    return bau, pruef, dec, ek


def dn1_stern_werte(nh, saat):
    """Die Sterne der Schleife in danzer_naeherung.netz (dual_flaeche / Laenge, dual_len / Flaeche), neu gerechnet mit
    demselben Zufallsstrom; Rechenweg woertlich aus danzer_naeherung.netz."""
    import itertools
    rng = dn.saat_rng(nh["ordnung"], saat)
    xi = rng.normal(size=3)
    xi /= np.linalg.norm(xi)
    gamma = dn.ETA * xi
    ek = dn.ecken(nh, gamma)
    r, L, N = ek["r"], nh["L"], ek["N"]
    rj = r + dn.SIGMA_D * rng.normal(size=r.shape)
    big = (rj[None, :, :] + L * dn.OFFS[:, None, :]).reshape(-1, 3)
    S = Delaunay(big).simplices
    cent = big[S].mean(axis=1)
    S = S[np.all((cent >= 0.0) & (cent < L), axis=1)]
    vid, off = S % N, dn.OFFS[S // N]
    kanten, flaechen = {}, {}
    for t in range(len(S)):
        vs, os_ = vid[t], off[t]
        for u, w in itertools.combinations(range(4), 2):
            key = dn.kanten_key(vs[u], os_[u], vs[w], os_[w])[0]
            if key not in kanten:
                kanten[key] = len(kanten)
        for d3 in itertools.combinations(range(4), 3):
            key = dn.flaechen_key(vs[list(d3)], os_[list(d3)])
            if key not in flaechen:
                flaechen[key] = len(flaechen)
    kl = sorted(kanten.items(), key=lambda kv: kv[1])
    ei = np.array([k[0] for k, _ in kl])
    ej = np.array([k[1] for k, _ in kl])
    ed = np.array([k[2] for k, _ in kl], dtype=float)
    laengen = np.linalg.norm(r[ej] + L * ed - r[ei], axis=1)
    dual_len = np.zeros(len(flaechen))
    dual_flaeche = np.zeros(len(kanten))
    for t in range(len(S)):
        vs, os_ = vid[t], off[t]
        P = r[vs] + L * os_
        M3 = 2.0 * np.array([P[1] - P[0], P[2] - P[0], P[3] - P[0]])
        rhs = np.array([P[m] @ P[m] - P[0] @ P[0] for m in (1, 2, 3)])
        cT = np.linalg.solve(M3, rhs)
        for d3 in itertools.combinations(range(4), 3):
            opp = [m for m in range(4) if m not in d3][0]
            Q = P[list(d3)]
            cf = dn.umkreis_dreieck(Q[0], Q[1], Q[2])
            nv = np.cross(Q[1] - Q[0], Q[2] - Q[0])
            if np.dot(nv, P[opp] - Q[0]) < 0:
                nv = -nv
            nv /= np.linalg.norm(nv)
            hfT = float(np.dot(cT - cf, nv))
            fk = flaechen[dn.flaechen_key(vs[list(d3)], os_[list(d3)])]
            dual_len[fk] += hfT
            for u, w in ((0, 1), (1, 2), (0, 2)):
                z = [m for m in range(3) if m not in (u, w)][0]
                me = 0.5 * (Q[u] + Q[w])
                ev = Q[w] - Q[u]
                uv = Q[z] - me
                uv = uv - np.dot(uv, ev) / np.dot(ev, ev) * ev
                uv /= np.linalg.norm(uv)
                hef = float(np.dot(cf - me, uv))
                ek_ = kanten[dn.kanten_key(vs[d3[u]], os_[d3[u]], vs[d3[w]], os_[d3[w]])[0]]
                dual_flaeche[ek_] += 0.5 * hef * hfT
    fl_area = np.zeros(len(flaechen))
    for key, f in flaechen.items():
        Q = np.array([r[v] + L * np.array(o) for v, o in key])
        fl_area[f] = 0.5 * np.linalg.norm(np.cross(Q[1] - Q[0], Q[2] - Q[0]))
    return dual_flaeche / laengen, dual_len / fl_area


# ------------------------------------------------------------------ DEC-Operatoren
def flaechen_verschmelzen(bau, dec):
    """Statische Kondensation der masselosen Kanten (*1 = 0): aktive Dreiecke (*2 != 0), die eine masselose Kante teilen,
    werden zu einem Vieleck verschmolzen. Rueckgabe: Zeilen (Vieleck), Spalten (Kante), Vorzeichen, Lagen, Vieleck-*2."""
    rowC, colC, sgnC, relC = bau["C"]
    F, E = bau["F"], bau["E"]
    s1, s2, L2, fa = dec["s1"], dec["s2"], dec["L2"], dec["fa"]
    masselos = np.abs(s1) <= TOL_NULL * np.abs(s1).max()
    aktiv = np.abs(s2) > TOL_NULL * np.abs(s2).max()
    eintraege = [[] for _ in range(F)]
    for idx in range(len(rowC)):
        eintraege[rowC[idx]].append(idx)
    an_kante = {}
    for idx in range(len(rowC)):
        e, f = int(colC[idx]), int(rowC[idx])
        if masselos[e] and aktiv[f]:
            an_kante.setdefault(e, []).append((f, idx))
    hist = {}
    for e in np.where(masselos)[0]:
        n_ = len(an_kante.get(int(e), []))
        hist[n_] = hist.get(n_, 0) + 1
    nachbarn = {}
    abweichend = 0
    for e, lst in an_kante.items():
        if len(lst) == 2 and lst[0][0] != lst[1][0]:
            (f1, i1), (f2, i2) = lst
            nachbarn.setdefault(f1, []).append((f2, i1, i2))
            nachbarn.setdefault(f2, []).append((f1, i2, i1))
        else:
            abweichend += 1
    gruppe = -np.ones(F, dtype=np.int64)
    platz = {}
    gruppen = []
    zyklus_fehler = 0
    for f0 in np.where(aktiv)[0]:
        f0 = int(f0)
        if gruppe[f0] >= 0:
            continue
        g = len(gruppen)
        gruppe[f0] = g
        platz[f0] = (1.0, np.zeros(3))
        mitglieder, stapel = [f0], [f0]
        while stapel:
            f1 = stapel.pop()
            sg1, D1 = platz[f1]
            for f2, i1, i2 in nachbarn.get(f1, []):
                sg2 = -sg1 * sgnC[i1] / sgnC[i2]
                D2 = relC[i1] + D1 - relC[i2]
                if gruppe[f2] >= 0:
                    sg_alt, D_alt = platz[f2]
                    if sg_alt != sg2 or np.max(np.abs(D_alt - D2)) > 1e-8:
                        zyklus_fehler += 1
                    continue
                platz[f2] = (sg2, D2)
                gruppe[f2] = g
                mitglieder.append(f2)
                stapel.append(f2)
        gruppen.append(mitglieder)
    rows, cols, sgns, rels, s2m, Am, Lm = [], [], [], [], [], [], []
    rest_masselos, L2_abw, eben_abw = 0, 0.0, 0.0
    groessen = {}
    for g, mitglieder in enumerate(gruppen):
        groessen[len(mitglieder)] = groessen.get(len(mitglieder), 0) + 1
        sammel = {}
        for f in mitglieder:
            sg, Dv = platz[f]
            for idx in eintraege[f]:
                e = int(colC[idx])
                rr = relC[idx] + Dv
                liste = sammel.setdefault(e, [])
                for item in liste:
                    if np.max(np.abs(item[1] - rr)) < 1e-7:
                        item[0] += sg * sgnC[idx]
                        break
                else:
                    liste.append([sg * sgnC[idx], rr])
        for e, liste in sammel.items():
            for sv, rr in liste:
                if abs(sv) < 0.5:
                    continue
                if masselos[e]:
                    rest_masselos += 1
                    continue
                rows.append(g)
                cols.append(e)
                sgns.append(sv)
                rels.append(rr)
        Ls = L2[mitglieder]
        A_ = float(fa[mitglieder].sum())
        L2_abw = max(L2_abw, float(np.ptp(Ls) / max(np.abs(Ls).max(), 1e-300)))
        nrm = dec["normal"][mitglieder]
        eben_abw = max(eben_abw, float(1.0 - np.min(np.abs(nrm @ nrm[0]))))
        s2m.append(float(Ls.mean()) / A_)
        Am.append(A_)
        Lm.append(float(Ls.mean()))
    info = {"masselose_kanten": int(masselos.sum()), "aktive_flaechen": int(aktiv.sum()),
            "inaktive_flaechen": int((~aktiv).sum()), "vielecke": len(gruppen),
            "vieleck_groessen": {str(k): v for k, v in sorted(groessen.items())},
            "masselos_aktive_flaechen_hist": {str(k): v for k, v in sorted(hist.items())},
            "masselos_nicht_2_aktive": int(abweichend), "zyklus_fehler": int(zyklus_fehler),
            "rest_masselos_eintraege": int(rest_masselos), "L2_rel_abw_im_vieleck_max": L2_abw,
            "eben_abw_max": eben_abw,
            "s1_luecke": [float(np.abs(s1[masselos]).max()) if masselos.any() else 0.0,
                          float(np.abs(s1[~masselos]).min())],
            "s2_luecke": [float(np.abs(s2[~aktiv]).max()) if (~aktiv).any() else 0.0, float(np.abs(s2[aktiv]).min())]}
    return (np.array(rows), np.array(cols), np.array(sgns, float), np.array(rels)), np.array(s2m), info, masselos, aktiv


def dec_operatoren(bau, dec):
    """Skalar B_s = *1^(1/2) d0 *0^(-1/2) (massive Kanten), Maxwell C~ = *2^(1/2) d1 *1^(-1/2) (Vielecke x massive
    Kanten), G~ = sqrt(S_LAENGS) *1^(1/2) d0 *0^(-1/2); K' = C~^H C~ + G~ G~^H."""
    s0, s1 = dec["s0"], dec["s1"]
    Cm, s2m, info, masselos, aktiv = flaechen_verschmelzen(bau, dec)
    massiv = np.where(~masselos)[0]
    if np.any(s0 <= 0) or np.any(s1[massiv] < 0) or np.any(s2m < 0):
        raise RuntimeError(f"negative Sterne: s0<=0 {int(np.sum(s0 <= 0))}, s1<0 {int(np.sum(s1[massiv] < 0))}, "
                           f"s2m<0 {int(np.sum(s2m < 0))}")
    neu = -np.ones(bau["E"], dtype=np.int64)
    neu[massiv] = np.arange(len(massiv))
    EN, V, FM = len(massiv), bau["V"], len(s2m)
    rowG, colG, sgnG, relG = bau["G"]
    behalt = ~masselos[rowG]
    Bs = (neu[rowG[behalt]], colG[behalt],
          sgnG[behalt] * np.sqrt(s1[rowG[behalt]]) / np.sqrt(s0[colG[behalt]]), relG[behalt])
    Gt = (Bs[0], Bs[1], Bs[2] * math.sqrt(S_LAENGS), Bs[3])
    rC, cC, sC, lC = Cm
    Ct = (rC, neu[cC], sC * np.sqrt(s2m[rC]) / np.sqrt(s1[cC]), lC)
    Dt = np.sqrt(s1[massiv])[:, None] * bau["Dvec"][massiv]
    skalar = {"st": Bs, "E": EN, "V": V, "u0": np.sqrt(s0) / np.linalg.norm(np.sqrt(s0))}
    maxwell = {"V": V, "E": EN, "F": FM, "C": Ct, "G": Gt, "Dt": Dt, "C_roh": (rC, neu[cC], sC, lC), "s2m": s2m}
    info["massive_kanten"] = int(EN)
    return skalar, maxwell, info, masselos, aktiv


def einheit_operatoren(bau):
    """Einheitsgewichte wie DANZER-NAEHERUNG-1: Graph-Laplace (alle Delaunay-Kanten) und K = C^H C + G G^H."""
    rowG, colG, sgnG, relG = bau["G"]
    skalar = {"st": (rowG, colG, sgnG.copy(), relG), "E": bau["E"], "V": bau["V"],
              "u0": np.ones(bau["V"]) / math.sqrt(bau["V"])}
    maxwell = {"V": bau["V"], "E": bau["E"], "F": bau["F"], "C": bau["C"], "G": bau["G"], "Dt": bau["Dvec"]}
    return skalar, maxwell


def kondensation_kontrolle(bau, dec, maxwell, masselos, aktiv, rng):
    """Energie mit statischer Kondensation (alle Dreiecke, alle Kanten, Minimum ueber die masselosen) gegen die Energie
    der Vielecke, an einem Zufalls-k und Zufallsvektor auf den massiven Kanten."""
    E, F = bau["E"], bau["F"]
    k = rng.normal(size=3) * 0.7
    C = dn.bloch(bau["C"], k, (F, E)).tocsr()
    C = C[np.where(aktiv)[0]]
    W = sps.diags(dec["s2"][aktiv])
    K = (C.conj().T @ W @ C).tocsr()
    N_ = np.where(~masselos)[0]
    Zall = np.where(masselos)[0]
    an = np.asarray(abs(K[Zall][:, Zall]).sum(axis=1)).ravel() > 0
    Z = Zall[an]
    a = rng.normal(size=len(N_)) + 1j * rng.normal(size=len(N_))
    KNN = K[N_][:, N_]
    e_c = np.vdot(a, KNN @ a).real
    if len(Z):
        KZZ = K[Z][:, Z].tocsc()
        KZN = K[Z][:, N_]
        b = KZN @ a
        x = spla.splu(KZZ).solve(b)
        e_c -= np.vdot(b, x).real
    rC, cC, sC, lC = maxwell["C_roh"]
    Cm = dn.bloch((rC, cC, sC, lC), k, (maxwell["F"], maxwell["E"]))
    y = Cm @ a
    e_m = float(np.sum(maxwell["s2m"] * np.abs(y) ** 2))
    return {"energie_kondensiert": float(e_c), "energie_vielecke": e_m, "rel_abw": float(abs(e_c - e_m) / abs(e_m)),
            "masselos_entkoppelt": int(len(Zall) - len(Z))}


# ------------------------------------------------------------------ Rayleigh-Ritz in der k.p-Basis, omega aus SVD
def _lu(A):
    return spla.splu(A.tocsc(), permc_spec=ORDNUNG_PERMC, diag_pivot_thresh=0.0, options=dict(SymmetricMode=True))


def ritz_skalar_fabrik(sk, mmax=MMAX_S):
    st, E, V, u0 = sk["st"], sk["E"], sk["V"], sk["u0"]
    B0 = dn.bloch(st, np.zeros(3), (E, V)).real.tocsr()
    K0 = (B0.T @ B0).tocsc()
    lu = _lu(K0 + MU_RITZ * sps.identity(V, format="csc"))
    u = u0[:, None].astype(complex)

    def Rt(Y):
        Y = Y - u @ (u.conj().T @ Y)
        X = lu.solve(np.ascontiguousarray(Y.real)) + 1j * lu.solve(np.ascontiguousarray(Y.imag))
        return X - u @ (u.conj().T @ X)

    def fabrik(n):
        Bm = dn.taylor(st, n, mmax, (E, V))
        def Km_an(m, Y):
            return sum((Bm[a].conj().T @ (Bm[m - a] @ Y)) for a in range(m + 1))
        B = [u]
        for j in range(1, mmax + 1):
            B.append(np.hstack([Rt(Km_an(m, B[j - m])) for m in range(1, j + 1)]))
        Sr = np.hstack(B)
        Sr = Sr / np.linalg.norm(Sr, axis=0)
        U, s, _ = np.linalg.svd(Sr, full_matrices=False)
        S = U[:, s > 1e-12 * s[0]]

        def f(k):
            Y = dn.bloch(st, k, (E, V)) @ S
            sv = np.linalg.svd(Y, compute_uv=False)
            return [float(sv[-1])]
        f.basis_dim = S.shape[1]
        return f
    kontrolle = {"K0u0_max": float(np.max(np.abs(K0 @ u0)))}
    return fabrik, kontrolle


def ritz_maxwell_vorbereiten(mx):
    V, E, F = mx["V"], mx["E"], mx["F"]
    C0 = dn.bloch(mx["C"], np.zeros(3), (F, E)).real.tocsr()
    G0 = dn.bloch(mx["G"], np.zeros(3), (E, V)).real.tocsr()
    K0 = (C0.T @ C0 + G0 @ G0.T).tocsc()
    Dt = mx["Dt"]
    L0 = (G0.T @ G0).tocsc() + 1e-10 * sps.identity(V, format="csc")
    phi = _lu(L0).solve(np.ascontiguousarray(G0.T @ Dt))
    H = Dt - G0 @ phi
    H, _ = np.linalg.qr(H)
    lu = _lu(K0 + MU_RITZ * sps.identity(E, format="csc"))
    kontrolle = {"K0H_max": float(np.max(np.abs(K0 @ H))), "C0D_max": float(np.max(np.abs(C0 @ Dt)))}
    return {"H": H, "lu": lu, "kontrolle": kontrolle}


def ritz_maxwell_fabrik(mx, vor, mmax=MMAX_M):
    V, E, F = mx["V"], mx["E"], mx["F"]
    H, lu = vor["H"], vor["lu"]

    def Rt(Y):
        Y = Y - H @ (H.T @ Y)
        X = lu.solve(np.ascontiguousarray(Y.real)) + 1j * lu.solve(np.ascontiguousarray(Y.imag))
        return X - H @ (H.T @ X)

    def fabrik(n):
        Cm = dn.taylor(mx["C"], n, mmax, (F, E))
        Gm = dn.taylor(mx["G"], n, mmax, (E, V))
        def Km_an(m, Y):
            return sum((Cm[a].conj().T @ (Cm[m - a] @ Y) + Gm[a] @ (Gm[m - a].conj().T @ Y)) for a in range(m + 1))
        B = [H.astype(complex)]
        for j in range(1, mmax + 1):
            B.append(np.hstack([Rt(Km_an(m, B[j - m])) for m in range(1, j + 1)]))
        Sr = np.hstack(B)
        Sr = Sr / np.linalg.norm(Sr, axis=0)
        U, s, _ = np.linalg.svd(Sr, full_matrices=False)
        S = U[:, s > 1e-12 * s[0]]

        def f(k):
            C = dn.bloch(mx["C"], k, (F, E))
            G = dn.bloch(mx["G"], k, (E, V))
            Y = np.vstack([C @ S, G.conj().T @ S])
            _, sv, Vh = np.linalg.svd(Y, full_matrices=False)
            o = np.argsort(sv)
            sv = sv[o]
            Ux = S @ Vh.conj().T[:, o[:4]]
            GU = G.conj().T @ Ux
            rho = np.sum(np.abs(GU) ** 2, axis=0) / np.maximum(sv[:4] ** 2 * np.sum(np.abs(Ux) ** 2, axis=0), 1e-300)
            ph = sv[:4][rho < 0.5]
            lo, hi = float(ph[0]), float(ph[1])
            return [lo, hi, math.sqrt(0.5 * (lo * lo + hi * hi))]
        f.basis_dim = S.shape[1]
        return f
    return fabrik


def mit_speicher(fabrik):
    speicher = {}

    def g(n):
        key = tuple(float(v) for v in np.round(n, 14))
        if key not in speicher:
            speicher[key] = fabrik(n)
        return speicher[key]
    g.speicher = speicher
    return g


# ------------------------------------------------------------------ exakte Gegenproben
def skalar_exakt(sk, k):
    B = dn.bloch(sk["st"], k, (sk["E"], sk["V"]))
    if sk["V"] <= 700:
        ev = np.linalg.eigvalsh((B.conj().T @ B).toarray())
        return math.sqrt(max(ev[0], 0.0))
    K = (B.conj().T @ B).tocsc()
    lu = _lu(K)
    op = spla.LinearOperator(K.shape, matvec=lu.solve, dtype=complex)
    w = spla.eigsh(K, k=1, sigma=0.0, which="LM", OPinv=op, return_eigenvectors=False)
    return math.sqrt(max(float(np.real(w).min()), 0.0))


def maxwell_exakt(mx, k, nev=4):
    V, E, F = mx["V"], mx["E"], mx["F"]
    C = dn.bloch(mx["C"], k, (F, E))
    G = dn.bloch(mx["G"], k, (E, V))
    K = (C.conj().T @ C + G @ G.conj().T).tocsc()
    GH = G.conj().T.tocsr()
    lu = _lu(K)
    op = spla.LinearOperator(K.shape, matvec=lu.solve, dtype=complex)
    for m_ev in (nev, 2 * nev):
        w, v = spla.eigsh(K, k=m_ev, sigma=0.0, which="LM", OPinv=op)
        o = np.argsort(np.real(w))
        w, v = np.real(w[o]), v[:, o]
        rho = np.array([np.linalg.norm(GH @ v[:, m]) ** 2 / max(abs(w[m]) * np.linalg.norm(v[:, m]) ** 2, 1e-300)
                        for m in range(m_ev)])
        ph = w[rho < 1e-6]
        if len(ph) >= 2:
            return math.sqrt(max(ph[0], 0.0)), math.sqrt(max(ph[1], 0.0))
    raise RuntimeError("zu wenige Photonen")


def ritz_gegenprobe(art, op_obj, fab, nh, rng, n_richt=2):
    abw = []
    for _ in range(n_richt):
        n = rng.normal(size=3)
        n /= np.linalg.norm(n)
        f = fab(n)
        for fk in (dn.FENSTER_HAUPT[0], dn.FENSTER_HAUPT[1]):
            k = n * fk * math.pi / nh["L"]
            r_ = f(k)
            if art == "S":
                e = [skalar_exakt(op_obj, k)]
            else:
                lo, hi = maxwell_exakt(op_obj, k)
                e = [lo, hi]
            abw.append(max(abs(e[i] - r_[i]) / abs(e[i]) for i in range(len(e))))
    return {"ritz_gegen_exakt_rel_max": float(max(abw)), "basis_dim": int(f.basis_dim), "richtungen": n_richt}


def kreuz_kontrolle(mx, rng):
    out = []
    for _ in range(3):
        k = rng.normal(size=3) * 0.5
        C = dn.bloch(mx["C"], k, (mx["F"], mx["E"]))
        G = dn.bloch(mx["G"], k, (mx["E"], mx["V"]))
        CG = (C @ G).tocoo()
        out.append(float(np.max(np.abs(CG.data))) if CG.nnz else 0.0)
    return max(out)


# ------------------------------------------------------------------ Hauptteile
def messen_satz(name, fab, nd, nh, ref, probe):
    f = mit_speicher(fab) if probe else fab
    nzw = 1 if name == "S" else 3
    out = {"haupt": dn.operator_messen(name, f, nzw, nd, dn.FENSTER_HAUPT, nh["L"], ref)}
    if probe:
        out["probe"] = dn.operator_messen(name, f, nzw, nd, dn.FENSTER_PROBE, nh["L"], ref)
        f.speicher.clear()
    return out


def rechnen(ordnung, ops, saaten, aus, probe, zitter_kontrolle, einheit_auch, m_richt):
    t0 = time.time()
    nh = dn.naeherung(ordnung)
    ref = dn.referenzen()
    nd = dn.halbkugel(m_richt)
    erg = {"karte": "DANZER-NAEHERUNG-2", "ordnung": ordnung, "ops": ops, "saaten": saaten, "argv": sys.argv,
           "numpy": np.__version__, "scipy": scipy.__version__, "L": nh["L"], "eps": nh["eps"],
           "naeherung_kontrolle": nh["kontrolle"], "referenz_kontrolle": ref["kontrolle"],
           "fenster_haupt": dn.FENSTER_HAUPT, "fenster_probe": dn.FENSTER_PROBE, "richtungen": m_richt,
           "eta": dn.ETA, "sigma_d": dn.SIGMA_D, "s_laengs": S_LAENGS, "mmax_s": MMAX_S, "mmax_m": MMAX_M,
           "saat_ergebnisse": {}}

    def schreiben():
        erg["laufzeit_s"] = time.time() - t0
        tmp = aus + ".tmp"
        with open(tmp, "w") as fh:
            json.dump(ln.js(erg), fh, indent=1)
        os.replace(tmp, aus)

    def eine_saat(s, zv, mit_probe, mit_einheit, gegenprobe):
        bau, pruef, dec, _ = netz2(nh, s, zitter_versatz=zv)
        sk, mx, info, masselos, aktiv = dec_operatoren(bau, dec)
        rng = np.random.default_rng([3746, 99, int(s), int(zv)])
        se = {"netz": pruef, "dec_info": info,
              "kontrollen": {"CG_max": kreuz_kontrolle(mx, rng),
                             "kondensation": kondensation_kontrolle(bau, dec, mx, masselos, aktiv, rng)}}
        print(f"{ordnung} Saat {s} (Zitter {zv}): Netz V={pruef['N']} E={pruef['E']} F={pruef['F']} T={pruef['T']} "
              f"masselos={info['masselose_kanten']} vielecke={info['vielecke']} ({time.time() - t0:.1f} s)", flush=True)
        for o in ops:
            if o == "S":
                fab, kon = ritz_skalar_fabrik(sk)
                se["S_ritz"] = kon
                if gegenprobe:
                    se["S_ritz"].update(ritz_gegenprobe("S", sk, fab, nh, rng))
                m = messen_satz("S", fab, nd, nh, ref, mit_probe)
            else:
                vor = ritz_maxwell_vorbereiten(mx)
                fab = ritz_maxwell_fabrik(mx, vor)
                se["M_ritz"] = dict(vor["kontrolle"])
                if gegenprobe:
                    se["M_ritz"].update(ritz_gegenprobe("M", mx, fab, nh, rng,
                                                        n_richt=(1 if ordnung == "5/3" else 2)))
                m = messen_satz("M", fab, nd, nh, ref, mit_probe)
            se[o] = m["haupt"]
            if "probe" in m:
                se[o + "_probe"] = m["probe"]
            print(f"  {o}: fertig ({time.time() - t0:.1f} s)", flush=True)
        if mit_einheit:
            sku, mxu = einheit_operatoren(bau)
            for o in ops:
                if o == "S":
                    fab, _ = ritz_skalar_fabrik(sku)
                else:
                    vor = dn.ritz_vorbereiten(bau)
                    fab = ritz_maxwell_fabrik(mxu, vor)
                se[o + "_einheit"] = messen_satz(o, fab, nd, nh, ref, False)["haupt"]
                print(f"  {o} Einheit: fertig ({time.time() - t0:.1f} s)", flush=True)
        return se

    for s in saaten:
        ts = time.time()
        se = eine_saat(s, 0, probe and s == saaten[0], einheit_auch, True)
        if zitter_kontrolle and s == saaten[0]:
            se["zitter_kontrolle"] = eine_saat(s, 1, False, False, False)
        se["laufzeit_s"] = time.time() - ts
        erg["saat_ergebnisse"][str(s)] = se
        schreiben()
    print(f"fertig {time.time() - t0:.1f} s -> {aus}", flush=True)


def rauch(aus, ordnungen, saaten, zeit):
    """Rauchtest (<= 120 s): Bau, Sterne, Kondensation, Kontrollen, Zeiten; keine a2- oder beta-Werte."""
    t0 = time.time()
    out = {"ordnungen": {}}
    for ordnung in ordnungen:
        nh = dn.naeherung(ordnung)
        oo = {"saaten": {}}
        for s in saaten:
            ta = time.time()
            bau, pruef, dec, ek = netz2(nh, s, dn1_sterne=(nh["p"] <= 2))
            sk, mx, info, masselos, aktiv = dec_operatoren(bau, dec)
            rng = np.random.default_rng([3746, 98, s])
            z = {"netz": pruef, "dec_info": info, "CG_max": kreuz_kontrolle(mx, rng),
                 "kondensation": kondensation_kontrolle(bau, dec, mx, masselos, aktiv, rng),
                 "zeit_netz_s": time.time() - ta}
            print(f"{ordnung} Saat {s}: V={pruef['N']} E={pruef['E']} F={pruef['F']} T={pruef['T']} "
                  f"verletzt={pruef['delaunay_verletzt']} kugel={pruef['kugel_entartet_zusatzpunkte']} "
                  f"s1={pruef['stern1']} s2={pruef['stern2']} s0min={pruef['stern0']['min']:.3e} "
                  f"ident={pruef['identitaeten']} info={info} CG={z['CG_max']:.1e} "
                  f"kond={z['kondensation']['rel_abw']:.1e} ecken={pruef['ecken_sha'][:12]} "
                  f"s0sha={pruef['s0_sortiert_sha'][:12]} s1sha={pruef['s1_positiv_sortiert_sha'][:12]} "
                  f"dn1={pruef.get('sterne_tu_gegen_dn1_schleife')} (t_netz {z['zeit_netz_s']:.1f} s)", flush=True)
            if zeit and s == saaten[0]:
                n = np.array([0.3, 0.5, 0.81])
                n /= np.linalg.norm(n)
                ta = time.time()
                fab, kon = ritz_skalar_fabrik(sk)
                f = fab(n)
                z["zeit_skalar_basis_s"] = time.time() - ta
                ta = time.time()
                f(n * 0.05 * math.pi / nh["L"])
                z["zeit_skalar_k_s"] = time.time() - ta
                ta = time.time()
                z["S_gegenprobe"] = ritz_gegenprobe("S", sk, fab, nh, rng, n_richt=1)
                z["zeit_skalar_gegenprobe_s"] = time.time() - ta
                ta = time.time()
                vor = ritz_maxwell_vorbereiten(mx)
                z["zeit_maxwell_vor_s"] = time.time() - ta
                z["M_vor_kontrolle"] = vor["kontrolle"]
                ta = time.time()
                fm = ritz_maxwell_fabrik(mx, vor)(n)
                z["zeit_maxwell_basis_s"] = time.time() - ta
                ta = time.time()
                fm(n * 0.05 * math.pi / nh["L"])
                z["zeit_maxwell_k_s"] = time.time() - ta
                if True:
                    ta = time.time()
                    z["M_gegenprobe"] = ritz_gegenprobe("M", mx, ritz_maxwell_fabrik(mx, vor), nh, rng, n_richt=1)
                    z["zeit_maxwell_gegenprobe_s"] = time.time() - ta
                print(f"   zeiten: { {k: round(v, 3) for k, v in z.items() if k.startswith('zeit')} } "
                      f"S_gp={z['S_gegenprobe']} M_gp={z.get('M_gegenprobe')} Mvor={z['M_vor_kontrolle']} "
                      f"(gesamt {time.time() - t0:.1f} s)", flush=True)
            oo["saaten"][str(s)] = z
        out["ordnungen"][ordnung] = oo
    out["laufzeit_s"] = time.time() - t0
    with open(aus, "w") as fh:
        json.dump(ln.js(out), fh, indent=1)
    print(f"fertig {time.time() - t0:.1f} s", flush=True)


# ------------------------------------------------------------------ Auswertung und Urteile (PLAN Abschnitt 6)
def zusammenfassen(werte):
    z = {"saaten": len(werte)}
    for g in ("beta_S4", "th6_rms", "rms_l2", "nichtkub4_rms", "mittel", "rest_rms"):
        v = np.array([w["a2_zerlegung"][g] for w in werte])
        z["a2_" + g] = {"mittel": float(v.mean()), "sd": float(v.std()), "werte": v.tolist(),
                        "spanne": float(v.max() - v.min())}
    sp = np.array([w["c_spanne_rel"] for w in werte])
    z["c_spanne_rel"] = {"mittel": float(sp.mean()), "max": float(sp.max()), "werte": sp.tolist()}
    cm = np.array([w["c_mittel"] for w in werte])
    z["c_mittel"] = {"mittel": float(cm.mean()), "min": float(cm.min()), "max": float(cm.max())}
    z["fit_rms_rel_max"] = float(max(w["fit_rms_rel_max"] for w in werte))
    z["a1_voll_max_abs"] = float(max(w["a1_voll_max_abs"] for w in werte))
    return z


def auswerten(aus, png, dn1_pfad, eingaben):
    daten = {}
    for p in eingaben:
        d = json.load(open(p))
        o = d["ordnung"]
        daten.setdefault(o, {"L": d["L"], "eps": d["eps"], "saaten": {}})
        for s, se in d["saat_ergebnisse"].items():
            daten[o]["saaten"].setdefault(s, {}).update(se)
    dn1 = json.load(open(dn1_pfad))["tabelle"]
    zweige = ["skalar", "maxwell_lo", "maxwell_hi", "maxwell_mittel"]
    tab = {}
    for o in REIHE:
        if o not in daten:
            continue
        dd = daten[o]
        t = {"L": dd["L"], "eps": dd["eps"], "dec": {}, "einheit": {}, "dn1": {}, "zitter": {}, "probe": {}}
        for zw in zweige:
            key = "S" if zw == "skalar" else "M"
            w = [se[key][zw] for se in dd["saaten"].values() if key in se]
            if w:
                t["dec"][zw] = zusammenfassen(w)
            w = [se[key + "_einheit"][zw] for se in dd["saaten"].values() if key + "_einheit" in se]
            if w:
                t["einheit"][zw] = zusammenfassen(w)
            if o in dn1 and zw in dn1[o]["zweige"]:
                b = dn1[o]["zweige"][zw]["a2_beta_S4"]
                t["dn1"][zw] = {"mittel": b["mittel"], "sd": b["sd"], "saaten": len(b["werte"])}
            for s, se in dd["saaten"].items():
                zk = se.get("zitter_kontrolle")
                if zk and key in zk and key in se:
                    b0 = se[key][zw]["a2_zerlegung"]["beta_S4"]
                    b1 = zk[key][zw]["a2_zerlegung"]["beta_S4"]
                    t["zitter"][zw] = {"saat": s, "beta": b0, "beta_zitter": b1, "abw": abs(b1 - b0),
                                       "c_spanne_zitter": zk[key][zw]["c_spanne_rel"]}
                if key + "_probe" in se:
                    t["probe"][zw] = {"saat": s, "beta_probe": se[key + "_probe"][zw]["a2_zerlegung"]["beta_S4"],
                                      "beta_haupt": se[key][zw]["a2_zerlegung"]["beta_S4"]}
        t["netz"] = {s: se["netz"] for s, se in dd["saaten"].items()}
        t["dec_info"] = {s: se["dec_info"] for s, se in dd["saaten"].items()}
        t["kontrollen"] = {s: {"kontrollen": se.get("kontrollen"), "S_ritz": se.get("S_ritz"),
                               "M_ritz": se.get("M_ritz")} for s, se in dd["saaten"].items()}
        tab[o] = t
    urteile = urteilen(tab)
    out = {"karte": "DANZER-NAEHERUNG-2", "argv": sys.argv, "eingaben": eingaben, "dn1": dn1_pfad,
           "tabelle": tab, "urteile": urteile}
    with open(aus, "w") as fh:
        json.dump(ln.js(out), fh, indent=1)
    bild(tab, png)
    print(json.dumps(ln.js(urteile), indent=1), flush=True)


def urteil_menge(flags):
    if not flags:
        return "nicht auswertbar"
    if all(flags):
        return "eingetroffen"
    if not any(flags):
        return "nicht eingetroffen"
    return "geteilt"


def urteilen(tab):
    u = {}
    # D2-0: Spanne < 1e-10 je Ordnung, Saat, Zweig (skalar, lo, hi); beta-Spanne ueber Saaten < 1e-10 (skalar, mittel)
    je, alle = {}, []
    for o, t in tab.items():
        for zw in ("skalar", "maxwell_lo", "maxwell_hi"):
            if zw in t["dec"]:
                m = t["dec"][zw]["c_spanne_rel"]["max"]
                je[f"{o}/{zw}/c_spanne_max"] = {"wert": m, "ok": m < D20_SCHWELLE}
        for zw in ("skalar", "maxwell_mittel", "maxwell_lo", "maxwell_hi"):
            if zw in t["dec"] and t["dec"][zw]["saaten"] >= 2:
                sp = t["dec"][zw]["a2_beta_S4"]["spanne"]
                je[f"{o}/{zw}/beta_spanne"] = {"wert": sp, "ok": sp < D20_SCHWELLE,
                                               "haupt": zw in ("skalar", "maxwell_mittel")}
    plan = [v["ok"] for k, v in je.items() if v.get("haupt", True)]
    alle = [v["ok"] for v in je.values()]
    u["D2-0"] = {"urteil_plan": urteil_menge(plan), "urteil_karte_alle_zweige": urteil_menge(alle), "je": je}

    def b(o, zw):
        return abs(tab[o]["dec"][zw]["a2_beta_S4"]["mittel"])
    for nr, (o1, o2, schwelle) in {"D2-1": ("1/1", "3/2", D21_DRITTEL), "D2-2": ("3/2", "5/3", D22_FAKTOR)}.items():
        je = {}
        for zw in ("skalar", "maxwell_mittel", "maxwell_lo", "maxwell_hi"):
            if o1 in tab and o2 in tab and zw in tab[o1]["dec"] and zw in tab[o2]["dec"]:
                R = b(o2, zw) / b(o1, zw) if b(o1, zw) > 0 else None
                je[zw] = {"verhaeltnis": R, "schwelle": schwelle, "ok": (R is not None and R < schwelle),
                          "betrag_beta": {o1: b(o1, zw), o2: b(o2, zw)}}
        haupt = [je[z]["ok"] for z in ("skalar", "maxwell_mittel") if z in je]
        u[nr] = {"urteil_plan": urteil_menge(haupt) if len(haupt) == 2 else "nicht auswertbar",
                 "urteil_karte_alle_zweige": urteil_menge([v["ok"] for v in je.values()]), "je": je}
    je = {}
    for o in ("1/1", "2/1", "3/2"):
        for zw in ("skalar", "maxwell_mittel", "maxwell_lo", "maxwell_hi"):
            if o in tab and zw in tab[o]["dec"] and zw in tab[o]["dn1"]:
                bd, be = b(o, zw), abs(tab[o]["dn1"][zw]["mittel"])
                je[f"{o}/{zw}"] = {"dec": bd, "einheit_dn1": be, "verhaeltnis": bd / be if be > 0 else None,
                                   "ok": bd < be, "haupt": zw in ("skalar", "maxwell_mittel")}
    for o in tab:
        for zw in ("skalar", "maxwell_mittel"):
            if zw in tab[o]["einheit"] and zw in tab[o]["dec"]:
                je[f"{o}/{zw}/einheit_hier"] = {"dec": b(o, zw),
                                                "einheit_hier": abs(tab[o]["einheit"][zw]["a2_beta_S4"]["mittel"]),
                                                "beschreibend": True}
    haupt = [v["ok"] for v in je.values() if v.get("haupt")]
    u["D2-3"] = {"urteil_plan": urteil_menge(haupt) if len(haupt) == 6 else
                 ("nicht auswertbar" if not haupt else urteil_menge(haupt) + " (unvollstaendig)"),
                 "urteil_karte_alle_zweige": urteil_menge([v["ok"] for v in je.values() if "ok" in v]), "je": je}
    return u


def bild(tab, png):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    reihe = [o for o in REIHE if o in tab]
    x = np.arange(len(reihe))
    fig, ax = plt.subplots(1, 2, figsize=(15, 5.6))
    serien = [("dec", "skalar", "tab:blue", "-", "o", "Skalar, DEC (*0, *1)"),
              ("dec", "maxwell_mittel", "tab:red", "-", "s", "Maxwell-Mittel, DEC (*1, *2)"),
              ("dn1", "skalar", "tab:blue", "--", "^", "Skalar, Einheitsgewichte (DANZER-NAEHERUNG-1)"),
              ("dn1", "maxwell_mittel", "tab:red", "--", "v", "Maxwell-Mittel, Einheitsgewichte (DANZER-NAEHERUNG-1)"),
              ("einheit", "skalar", "tab:cyan", ":", "^", "Skalar, Einheitsgewichte (hier gerechnet)"),
              ("einheit", "maxwell_mittel", "tab:orange", ":", "v", "Maxwell-Mittel, Einheitsgewichte (hier gerechnet)")]
    for quelle, zw, fb, ls, mk, lab in serien:
        xs, ys, es = [], [], []
        for i, o in enumerate(reihe):
            z = tab[o][quelle].get(zw)
            if z is None:
                continue
            if quelle == "dn1":
                m_, sd = z["mittel"], z["sd"]
            else:
                m_, sd = z["a2_beta_S4"]["mittel"], z["a2_beta_S4"]["sd"]
                for v in z["a2_beta_S4"]["werte"]:
                    ax[0].plot(i, abs(v), ".", color=fb, alpha=0.3, ms=4)
            xs.append(i)
            ys.append(m_)
            es.append(sd)
        if not xs:
            continue
        ax[0].errorbar(xs, np.abs(ys), yerr=es, fmt=mk + ls, color=fb, label=lab, capsize=3)
        ax[1].errorbar(xs, ys, yerr=es, fmt=mk + ls, color=fb, label=lab, capsize=3)
    for zw, fb in (("skalar", "tab:blue"), ("maxwell_mittel", "tab:red")):
        if "1/1" in tab and zw in tab["1/1"]["dec"]:
            b0 = abs(tab["1/1"]["dec"][zw]["a2_beta_S4"]["mittel"])
            ax[0].axhline(b0 / 3.0, color=fb, lw=0.7, ls="-.", alpha=0.5)
    ax[0].set_yscale("log")
    ax[0].set_title("(a) |beta| (a2 ~ alpha + beta S4), Saatmittel +- SD; strichpunktiert: 1/3 des DEC-Startwerts")
    ax[1].axhline(0, color="k", lw=0.6)
    ax[1].set_title("(b) beta mit Vorzeichen")
    for a_ in ax:
        a_.set_xticks(x)
        a_.set_xticklabels([f"{o}\nL={tab[o]['L']:.2f}" for o in reihe])
        a_.set_xlabel("Naeherung")
        a_.legend(fontsize=7)
    fig.suptitle("DANZER-NAEHERUNG-2: kubischer l=4-Anteil von a2, DEC- gegen Einheitsgewichte (synthetische Rechnung)",
                 fontsize=10)
    fig.tight_layout()
    fig.savefig(png, dpi=110)
    print(f"bild -> {png}", flush=True)


if __name__ == "__main__":
    arg = sys.argv[1:]
    if len(arg) >= 3 and arg[0] == "rauch":
        saaten = [0]
        if "--saaten" in arg:
            saaten = [int(s) for s in arg[arg.index("--saaten") + 1].split(",")]
        rauch(arg[1], arg[2].split(","), saaten, "--zeit" in arg)
    elif len(arg) >= 5 and arg[0] == "rechnen":
        m = dn.RICHTUNGEN_STANDARD
        if "--richtungen" in arg:
            m = int(arg[arg.index("--richtungen") + 1])
        rechnen(arg[1], arg[2].split(","), [int(s) for s in arg[3].split(",")], arg[4], "--probe" in arg,
                "--zitter-kontrolle" in arg, "--einheit" in arg, m)
    elif len(arg) >= 5 and arg[0] == "auswerten":
        auswerten(arg[1], arg[2], arg[3], arg[4:])
    else:
        print(__doc__)
        sys.exit(2)
