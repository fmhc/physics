#!/usr/bin/env python3
"""STRICH-NETZ-1 (Runde 41, Code-Agent fuer claude-primary).

Teil A: 20 Zufallspunkte im Einheitswuerfel. Lesarten alle, gabriel, delaunay, beruehrung (NN-Graph, Kartenlesart),
  wachstum (gleichzeitiges Aufblasen mit Anhalten, beschreibend). Zaehlungen, Kreuzungen und Punkt-nahe-Strich-
  Beruehrungen in Zufallsansichten, Probe der 3420-Regel, Federnetz (Nullmoden, Eigenspannungen), Skalarmoden,
  Stoss (exakt ueber die Eigenzerlegung).
Teil B/C: periodisches Poisson-Delaunay-Netz (Dichte 1) aus spinnetz.zufallsnetz (unveraendert, SPIN-ZUFALLSNETZ-1),
  Tetraeder mit demselben Verfahren neu trianguliert, P1-FEM aus induziert.lokal_K_batch (unveraendert, INDUZIERT-1).
  Felder: fem (P1, konzentrierte Masse V_T/4), voronoi (w = A/d, Masse V), ungew (w = kappa, Masse 1),
  laenge (w = kappa/d^2, Masse 1), weyl (spinnetz.matrix), kuerzeste Wege (Kantenzeit d/c).

Aufruf (nur ueber kleintest.sh):
  python strichnetz.py teilA <saat0> <anzahl> <aus.json> [ansichten=2000] [beruehr=2000] [stoss=200]
  python strichnetz.py netz <N> <saat> <aus.npz>
  python strichnetz.py dicht <netz.npz> <aus.json>
  python strichnetz.py klein <N> <saat0> <anzahl> <aus.json>
  python strichnetz.py eigen <netz.npz> <aus.json> [felder=fem,voronoi,ungew,laenge] [k=40]
  python strichnetz.py weyl <netz.npz> <aus.json> <M> <0|x|d>
  python strichnetz.py welle <netz.npz> <aus> <lesart> <feld> <quellen> [tmax=16]
  python strichnetz.py kontrolle <aus.json> [M=4096]
"""
import itertools
import json
import math
import os
import resource
import sys
import time

import numpy as np
import scipy
import scipy.sparse as sp
import scipy.sparse.linalg as spla
from scipy.sparse.csgraph import breadth_first_order, connected_components, dijkstra, shortest_path
from scipy.spatial import ConvexHull, Delaunay, cKDTree

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import spinnetz as sz  # noqa: E402  (unveraendert aus SPIN-ZUFALLSNETZ-1, sha256 460c0af6...)
import induziert as ind  # noqa: E402  (unveraendert aus INDUZIERT-1, sha256 b3867eac...)

SAAT = 41
N_A = 20
EPS_BER = (0.01, 0.02)
T_STOSS_A = np.round(np.arange(0.0, 8.0001, 0.02), 4)
BILD_ZEITEN_A = (0.6, 1.5, 3.0)
BILD_ZEITEN_B = (4.0, 8.0, 12.0)
_r = np.array([(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1), (1, -1, 0), (1, 0, -1), (0, 1, -1),
               (1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1)], dtype=float)
RICHT13 = _r / np.linalg.norm(_r, axis=1)[:, None]
RICHT7 = RICHT13[[0, 1, 2, 9, 10, 11, 12]]
M_SCHALEN = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1), (1, -1, 0), (1, 0, -1), (0, 1, -1),
             (1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1), (2, 0, 0), (0, 2, 0), (0, 0, 2)]
M_VERDRILLT = {"x": [(0, 0, 0), (1, 0, 0), (-1, 0, 0)], "d": [(0, 0, 0), (1, 1, 1), (-1, -1, -1)]}
THETA0 = (0.8, 1.6, 2.4)
_k = [(s * a, 0, 0) for a in (1,) for s in (1, -1)] + [(0, s, 0) for s in (1, -1)] + [(0, 0, s) for s in (1, -1)]
_k += [(a, b, c) for a in (1, -1) for b in (1, -1) for c in (1, -1)]
KEGEL14 = np.array(_k, dtype=float)
KEGEL14 /= np.linalg.norm(KEGEL14, axis=1)[:, None]
js = sz.js


def rss_mb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0


def speichern(ziel, out):
    with open(ziel + ".tmp", "w") as f:
        json.dump(js(out), f)
    os.replace(ziel + ".tmp", ziel)


# ============================================================================ Teil A: 20 Punkte im Wuerfel
TRI = np.array(list(itertools.combinations(range(N_A), 3)))
TI = -np.ones((N_A, N_A, N_A), dtype=np.int64)
TI[TRI[:, 0], TRI[:, 1], TRI[:, 2]] = np.arange(len(TRI))
QUAD = np.array(list(itertools.combinations(range(N_A), 4)))
Q_BCD = TI[QUAD[:, 1], QUAD[:, 2], QUAD[:, 3]]
Q_ACD = TI[QUAD[:, 0], QUAD[:, 2], QUAD[:, 3]]
Q_ABD = TI[QUAD[:, 0], QUAD[:, 1], QUAD[:, 3]]
Q_ABC = TI[QUAD[:, 0], QUAD[:, 1], QUAD[:, 2]]


def orient_index(p, q, r):
    """Index des sortierten Tripels und Paritaet der Permutation: orient(p,q,r) = par * S[t]."""
    P = np.stack([p, q, r], 1)
    o = np.argsort(P, axis=1)
    s = np.take_along_axis(P, o, 1)
    inv = (o[:, 0] > o[:, 1]).astype(int) + (o[:, 0] > o[:, 2]) + (o[:, 1] > o[:, 2])
    return TI[s[:, 0], s[:, 1], s[:, 2]], (1 - 2 * (inv % 2)).astype(np.int8)


def wachstum(D):
    """Alle Kugeln wachsen gleich schnell; jede haelt bei der ersten Beruehrung an (beschreibende Variante)."""
    n = len(D)
    wachsend = np.ones(n, bool)
    r = np.zeros(n)
    kanten = []
    while wachsend.any():
        T = np.where(wachsend[None, :], 0.5 * D, D - r[None, :])
        np.fill_diagonal(T, np.inf)
        T[~wachsend, :] = np.inf
        a, b = divmod(int(np.argmin(T)), n)
        t = T[a, b]
        if wachsend[b]:
            wachsend[a] = wachsend[b] = False
            r[a] = r[b] = t
        else:
            wachsend[a] = False
            r[a] = t
        kanten.append((min(a, b), max(a, b)))
    return np.array(sorted(set(kanten)), dtype=np.int64)


def lesarten_klein(X):
    n = len(X)
    i, j = np.triu_indices(n, 1)
    alle = np.stack([i, j], 1)
    D = np.linalg.norm(X[:, None, :] - X[None, :, :], axis=2)
    mid = 0.5 * (X[i] + X[j])
    r2 = 0.25 * D[i, j] ** 2
    d2 = ((X[None, :, :] - mid[:, None, :]) ** 2).sum(2)
    d2[np.arange(len(i)), i] = np.inf
    d2[np.arange(len(i)), j] = np.inf
    gab = alle[np.all(d2 > r2[:, None], axis=1)]
    tri = Delaunay(X)
    S = np.sort(tri.simplices, axis=1)
    de = set()
    for s in S:
        for a, b in itertools.combinations(s, 2):
            de.add((int(a), int(b)))
    dele = np.array(sorted(de), dtype=np.int64)
    Dm = D + np.diag(np.full(n, np.inf))
    nn = Dm.argmin(1)
    ber = np.array(sorted(set((min(a, int(b)), max(a, int(b))) for a, b in zip(range(n), nn))), dtype=np.int64)
    return {"alle": alle, "gabriel": gab, "delaunay": dele, "beruehrung": ber, "wachstum": wachstum(D)}, D, S, nn, tri


def inseln(n, E):
    if len(E) == 0:
        return n
    A = sp.coo_matrix((np.ones(len(E)), (E[:, 0], E[:, 1])), shape=(n, n))
    return int(connected_components(A, directed=False)[0])


def paar_index(E):
    m = len(E)
    pa, pb = np.triu_indices(m, 1)
    A, B = E[pa], E[pb]
    dis = (A[:, 0] != B[:, 0]) & (A[:, 0] != B[:, 1]) & (A[:, 1] != B[:, 0]) & (A[:, 1] != B[:, 1])
    A, B = A[dis], B[dis]
    return (orient_index(A[:, 0], A[:, 1], B[:, 0]) + orient_index(A[:, 0], A[:, 1], B[:, 1])
            + orient_index(B[:, 0], B[:, 1], A[:, 0]) + orient_index(B[:, 0], B[:, 1], A[:, 1]))


def kreuzungen_paare(S, idx):
    t1, p1, t2, p2, t3, p3, t4, p4 = idx
    o1, o2, o3, o4 = S[:, t1] * p1, S[:, t2] * p2, S[:, t3] * p3, S[:, t4] * p4
    return ((o1 != o2) & (o3 != o4)).sum(1)


def kreuzungen_alle(S):
    pos = ((S[:, Q_BCD] > 0).astype(np.int8) + (S[:, Q_ACD] < 0) + (S[:, Q_ABD] > 0) + (S[:, Q_ABC] < 0))
    return (pos == 2).sum(1)


def basis(U):
    a = np.where(np.abs(U[:, 0:1]) < 0.9, np.array([[1.0, 0.0, 0.0]]), np.array([[0.0, 1.0, 0.0]]))
    e1 = np.cross(U, a)
    e1 /= np.linalg.norm(e1, axis=1)[:, None]
    return e1, np.cross(U, e1)


def beruehrungen(X, U, E, eps_list, block=250):
    """Zahl der Paare (Punkt C, Strich AB), C nicht A, B, mit projiziertem Abstand < eps, je Ansicht."""
    e1, e2 = basis(U)
    m = len(E)
    out = np.zeros((len(U), len(eps_list)), dtype=np.int64)
    ar = np.arange(m)
    for s0 in range(0, len(U), block):
        Q = np.stack([e1[s0:s0 + block] @ X.T, e2[s0:s0 + block] @ X.T], -1)     # (B, n, 2)
        A = Q[:, E[:, 0]]
        Bv = Q[:, E[:, 1]] - A
        C = Q[:, None, :, :] - A[:, :, None, :]
        L2 = (Bv ** 2).sum(-1)
        t = np.clip((C * Bv[:, :, None, :]).sum(-1) / L2[:, :, None], 0.0, 1.0)
        dd = ((C - t[..., None] * Bv[:, :, None, :]) ** 2).sum(-1)
        dd[:, ar, E[:, 0]] = np.inf
        dd[:, ar, E[:, 1]] = np.inf
        for k, eps in enumerate(eps_list):
            out[s0:s0 + block, k] = (dd < eps * eps).sum((1, 2))
    return out


def winkel(P, Q, R):
    a, b = Q - P, R - P
    return float(math.acos(max(-1.0, min(1.0, a @ b / (np.linalg.norm(a) * np.linalg.norm(b))))))


def probe_3420(X, rng, ntri=10, K=200000):
    res = []
    phi = 2 * math.pi * (np.arange(K) + 0.5) / K
    for _ in range(ntri):
        a, b, c = rng.choice(N_A, 3, replace=False)
        A, B, C = X[a], X[b], X[c]
        nr = np.cross(B - A, C - A)
        nr /= np.linalg.norm(nr)
        e1 = (B - A) / np.linalg.norm(B - A)
        e2 = np.cross(nr, e1)
        u = np.cos(phi)[:, None] * e1 + np.sin(phi)[:, None] * e2
        w = np.cross(nr[None, :], u)
        tA, tB, tC = w @ A, w @ B, w @ C

        def bogen(tp, t1, t2):
            return float(np.sum((tp - t1) * (tp - t2) < 0) * 2 * math.pi / K)
        arcs = [bogen(tC, tA, tB), bogen(tA, tB, tC), bogen(tB, tA, tC)]
        gam = [winkel(C, A, B), winkel(A, B, C), winkel(B, A, C)]
        res.append({"tripel": [int(a), int(b), int(c)], "bogen": arcs, "zwei_gamma": [2 * g for g in gam],
                    "abw_max": float(max(abs(x - 2 * g) for x, g in zip(arcs, gam))), "summe": float(sum(arcs))})
    return res


def federnetz(X, E):
    n, m = len(X), len(E)
    dv = X[E[:, 1]] - X[E[:, 0]]
    nv = dv / np.linalg.norm(dv, axis=1)[:, None]
    R = np.zeros((m, 3 * n))
    rows = np.arange(m)
    for c in range(3):
        R[rows, 3 * E[:, 0] + c] = -nv[:, c]
        R[rows, 3 * E[:, 1] + c] = nv[:, c]
    sv = np.linalg.svd(R, compute_uv=False)
    tol = 1e-8 * sv.max()
    rang = int(np.sum(sv > tol))
    Z, S = 3 * n - rang, m - rang
    ev, V = np.linalg.eigh(R.T @ R)
    modes = V[:, Z:Z + 3].reshape(n, 3, -1)
    p = (modes ** 2).sum(1)
    pr = (1.0 / (n * (p ** 2).sum(0))).tolist() if modes.shape[2] else []
    nz_sv = sv[sv > tol]
    return {"E": m, "Z": Z, "S": S, "maxwell": 3 * n - 6 - m, "abw": (Z - 6) - max(0, 3 * n - 6 - m),
            "calladine": (Z - S) - (3 * n - m), "sv_min_nichtnull_rel": float(nz_sv.min() / sv.max()),
            "sv_max_null_rel": float(sv[sv <= tol].max() / sv.max()) if np.any(sv <= tol) else 0.0,
            "pr_tief": pr}


def laplace(n, E, w):
    i, j = E[:, 0], E[:, 1]
    r = np.concatenate([i, j, i, j])
    c = np.concatenate([j, i, i, j])
    v = np.concatenate([-w, -w, w, w])
    return sp.coo_matrix((v, (r, c)), shape=(n, n)).tocsr()


def fem_lokal(X, S):
    """P1-Steifigkeit je Tetraeder aus induziert.lokal_K_batch (Kantenquadrate, Reihenfolge combinations)."""
    T = X[S]
    sq = np.stack([((T[:, b] - T[:, a]) ** 2).sum(1) for a, b in itertools.combinations(range(4), 2)], 1)
    Kl = ind.lokal_K_batch(3, 0.0, sq)
    J = T[:, 1:] - T[:, :1]
    Vt = np.abs(np.linalg.det(J)) / 6.0
    return Kl, Vt, J


def fem_klein(X, S):
    Kl, Vt, J = fem_lokal(X, S)
    gut = Vt > 1e-12
    S2, Kl = S[gut], Kl[gut]
    n = len(X)
    K = sp.coo_matrix((Kl.ravel(), (np.repeat(S2, 4, axis=1).ravel(), np.tile(S2, (1, 4)).ravel())),
                      shape=(n, n)).toarray()
    m = np.bincount(S2.ravel(), np.repeat(Vt[gut] / 4.0, 4), n)
    return K, m, int((~gut).sum()), float(Vt.sum())


def skalar_klein(X, K, m):
    n = len(X)
    s = 1.0 / np.sqrt(m)
    ev, W = np.linalg.eigh(K * s[:, None] * s[None, :])
    phi = W * s[:, None]
    nnull = int(np.sum(ev < 1e-9 * max(ev.max(), 1e-300)))
    p = m[:, None] * phi ** 2
    pr = 1.0 / (n * (p ** 2).sum(0))
    F = X - (m @ X) / m.sum()
    Lc = np.linalg.cholesky(F.T @ (m[:, None] * F))
    Fo = np.linalg.solve(Lc, F.T).T
    proj = Fo.T @ (m[:, None] * phi[:, nnull:nnull + 3])
    return {"null": nnull, "ev": ev, "pr_tief": pr[nnull:nnull + 3], "pr_median": float(np.median(pr[nnull:])),
            "affin_tief": (proj ** 2).sum(0)}, ev, phi


def stoss_klein(ev, phi, m, quelle, zeiten):
    """Geschwindigkeitsstoss v(0) = e_s/m_s, u(0) = 0; exakt ueber Eigenmoden."""
    w = np.sqrt(np.maximum(ev, 0.0))
    a = phi[quelle]
    t = np.asarray(zeiten)[:, None]
    with np.errstate(invalid="ignore", divide="ignore"):
        sinw = np.where(w[None, :] > 1e-12, np.sin(w[None, :] * t) / np.where(w > 1e-12, w, 1.0)[None, :], t)
    u = (sinw * a[None, :]) @ phi.T
    v = (np.cos(w[None, :] * t) * a[None, :]) @ phi.T
    return u, v


def hops(n, E, s):
    if len(E) == 0:
        return np.full(n, np.inf)
    A = sp.coo_matrix((np.ones(len(E)), (E[:, 0], E[:, 1])), shape=(n, n)).tocsr()
    return shortest_path(A, unweighted=True, directed=False, indices=s)


def teilA(saat0, anzahl, nans, nber, nstoss, protokoll):
    t0 = time.time()
    proben, saaten = [], []
    hist = {"alle": np.zeros(4846, dtype=np.int64), "gabriel": np.zeros(4846, dtype=np.int64)}
    bild = None
    for saat in range(saat0, saat0 + anzahl):
        X = np.random.default_rng([SAAT, N_A, saat]).random((N_A, 3))
        E, D, S, nn, tri = lesarten_klein(X)
        e = {"saat": saat}
        for la, Ek in E.items():
            deg = np.bincount(Ek.ravel(), minlength=N_A)
            e[la] = {"E": len(Ek), "grad_mittel": float(deg.mean()), "grad_min": int(deg.min()),
                     "grad_max": int(deg.max()), "inseln": inseln(N_A, Ek)}
        e["gabriel_in_delaunay"] = bool(set(map(tuple, E["gabriel"].tolist())) <= set(map(tuple, E["delaunay"].tolist())))
        e["nn_gegenseitig"] = float(np.mean(nn[nn] == np.arange(N_A)))
        e["delaunay_tetra"] = int(len(S))
        e["huellpunkte"] = int(len(np.unique(tri.convex_hull)))
        # Ansichten
        U = np.random.default_rng([SAAT, N_A, saat, 1]).normal(size=(nans, 3))
        U /= np.linalg.norm(U, axis=1)[:, None]
        Nt = np.cross(X[TRI[:, 1]] - X[TRI[:, 0]], X[TRI[:, 2]] - X[TRI[:, 0]])
        Sg = np.sign(U @ Nt.T).astype(np.int8)
        kr = {"alle": kreuzungen_alle(Sg)}
        for la in ("gabriel", "delaunay", "beruehrung", "wachstum"):
            kr[la] = kreuzungen_paare(Sg, paar_index(E[la])) if len(E[la]) > 1 else np.zeros(nans, dtype=np.int64)
        if saat < saat0 + 3:
            e["kontrolle_kreuz_paare_gleich_konvex"] = bool(np.array_equal(kreuzungen_paare(Sg, paar_index(E["alle"])),
                                                                           kr["alle"]))
        e["kreuz"] = {la: {"mittel": float(v.mean()), "min": int(v.min()), "max": int(v.max())} for la, v in kr.items()}
        hist["alle"] += np.bincount(kr["alle"], minlength=4846)[:4846]
        hist["gabriel"] += np.bincount(kr["gabriel"], minlength=4846)[:4846]
        if nber:
            e["beruehr"] = {}
            for la in ("alle", "gabriel", "delaunay"):
                b = beruehrungen(X, U[:nber], E[la], EPS_BER)
                e["beruehr"][la] = {"eps": list(EPS_BER), "mittel": b.mean(0).tolist(),
                                    "anteil_ansichten_mit": (b > 0).mean(0).tolist()}
        # Federnetz und Skalare
        e["feder"] = {la: federnetz(X, E[la]) for la in E}
        e["skalar"] = {}
        Kf, mf, nflach, vsum = fem_klein(X, S)
        e["fem_flache_tetra"] = nflach
        e["fem_volumen_rel"] = float(vsum / ConvexHull(X).volume - 1.0)
        for la, Ek in E.items():
            dl = D[Ek[:, 0], Ek[:, 1]]
            for feld, w in (("ungew", np.ones(len(Ek))), ("laenge", 1.0 / dl ** 2)):
                K = laplace(N_A, Ek, w).toarray()
                r, ev, phi = skalar_klein(X, K, np.ones(N_A))
                e["skalar"][f"{la}/{feld}"] = {"null": r["null"], "pr_tief": r["pr_tief"], "pr_median": r["pr_median"],
                                               "affin_tief": r["affin_tief"], "ev_max": float(ev.max())}
        r, evf, phif = skalar_klein(X, Kf, mf)
        e["skalar"]["delaunay/fem"] = {"null": r["null"], "pr_tief": r["pr_tief"], "pr_median": r["pr_median"],
                                       "affin_tief": r["affin_tief"], "ev_max": float(evf.max())}
        # Stoss (ungewichtet), exakt
        if saat < saat0 + nstoss:
            s0 = int(np.argmin(((X - 0.5) ** 2).sum(1)))
            e["stoss"] = {}
            for la, Ek in E.items():
                K = laplace(N_A, Ek, np.ones(len(Ek))).toarray()
                _, ev, phi = skalar_klein(X, K, np.ones(N_A))
                u, v = stoss_klein(ev, phi, np.ones(N_A), s0, T_STOSS_A)
                andere = np.arange(N_A) != s0
                spread = float(np.max(u[:, andere].max(1) - u[:, andere].min(1)))
                kin = 0.5 * v ** 2
                ta = np.array([T_STOSS_A[np.argmax(kin[:, j] >= 0.5 * kin[1:, j].max())] if kin[1:, j].max() > 0
                               else np.nan for j in range(N_A)])
                r_echt = np.linalg.norm(X - X[s0], axis=1)
                h = hops(N_A, Ek, s0)
                ok = andere & np.isfinite(ta) & np.isfinite(h)
                kor = lambda a, b: float(np.corrcoef(a, b)[0, 1]) if ok.sum() > 2 and np.std(a) > 0 and np.std(b) > 0 else None
                ein = {"spread_andere_max": spread, "kor_ankunft_abstand": kor(ta[ok], r_echt[ok]),
                       "kor_ankunft_hops": kor(ta[ok], h[ok])}
                if la == "alle":
                    n = N_A
                    ana = T_STOSS_A / n - np.sin(math.sqrt(n) * T_STOSS_A) / (n * math.sqrt(n))
                    j0 = int(np.nonzero(andere)[0][0])
                    ein["alle_gegen_analytisch_max"] = float(np.max(np.abs(u[:, j0] - ana)))
                e["stoss"][la] = ein
                if bild is None or (bild["saat"] == saat and la not in bild["u"]):
                    if bild is None:
                        bild = {"saat": saat, "X": X, "quelle": s0, "zeiten": BILD_ZEITEN_A, "kanten": {}, "u": {}}
                    ub, _ = stoss_klein(ev, phi, np.ones(N_A), s0, BILD_ZEITEN_A)
                    bild["kanten"][la] = Ek
                    bild["u"][la] = ub
        if saat < saat0 + 10:
            proben += [dict(p, saat=saat) for p in probe_3420(X, np.random.default_rng([SAAT, N_A, saat, 2]))]
        saaten.append(e)
        if (saat - saat0) % 100 == 0:
            protokoll(f"teilA saat {saat}: alle-Kreuzungen {e['kreuz']['alle']['mittel']:.1f}, Gabriel E "
                      f"{e['gabriel']['E']}, {time.time() - t0:.1f} s, RSS {rss_mb():.0f} MB")
    return {"saaten": saaten, "proben_3420": proben, "hist_kreuz": hist, "bild": bild, "sek": time.time() - t0,
            "ansichten": nans, "ansichten_beruehr": nber}


# ============================================================================ periodisches Netz (Teil B/C)
def tetraeder_periodisch(N, saat, pos, L):
    """Wie spinnetz.zufallsnetz (Saum-Kopien, Qhull, Bild mit Schwerpunkt im Grundwuerfel); gibt Tetraeder."""
    saum = sz.SAUM
    offs = np.array([(a, b, c) for a in (-1, 0, 1) for b in (-1, 0, 1) for c in (-1, 0, 1)], dtype=np.int64)
    Pl, Il = [], []
    for o in offs:
        Q = pos + o * L
        m = np.all((Q >= -saum) & (Q <= L + saum), axis=1)
        Pl.append(Q[m])
        Il.append(np.nonzero(m)[0])
    P = np.concatenate(Pl)
    gidx = np.concatenate(Il)
    S = Delaunay(P).simplices
    X = P[S]
    cen = X.mean(axis=1)
    halte = np.all((cen >= 0.0) & (cen < L), axis=1)
    return gidx[S[halte]], X[halte]


def netz_bauen(N, saat, protokoll):
    t0 = time.time()
    nz = sz.zufallsnetz(N, saat)
    L, pos = nz["L"], nz["pos"]
    G, X = tetraeder_periodisch(N, saat, pos, L)
    T = len(G)
    sq = np.stack([((X[:, b] - X[:, a]) ** 2).sum(1) for a, b in itertools.combinations(range(4), 2)], 1)
    Kl = ind.lokal_K_batch(3, 0.0, sq)
    J = X[:, 1:] - X[:, :1]
    Vt = np.abs(np.linalg.det(J)) / 6.0
    Ji = np.linalg.inv(J)
    gr = np.empty((T, 4, 3))
    gr[:, 1:, :] = np.transpose(Ji, (0, 2, 1))
    gr[:, 0, :] = -gr[:, 1:, :].sum(1)
    Kg = Vt[:, None, None] * np.einsum("tai,tbi->tab", gr, gr)
    kopie_abw = float(np.max(np.abs(Kg - Kl)) / np.max(np.abs(Kl)))
    pa = list(itertools.combinations(range(4), 2))
    lo = np.concatenate([np.minimum(G[:, a], G[:, b]) for a, b in pa])
    hi = np.concatenate([np.maximum(G[:, a], G[:, b]) for a, b in pa])
    kt = np.unique(lo.astype(np.int64) * N + hi)
    kn = nz["ei"].astype(np.int64) * N + nz["ej"]
    kanten_gleich = bool(np.array_equal(kt, np.sort(kn)))
    K = sp.coo_matrix((Kl.ravel(), (np.repeat(G, 4, axis=1).ravel(), np.tile(G, (1, 4)).ravel())),
                      shape=(N, N)).tocsr()
    K.sum_duplicates()
    w_fem = -np.asarray(K[nz["ei"], nz["ej"]]).ravel()
    m_fem = np.bincount(G.ravel(), np.repeat(Vt / 4.0, 4), N)
    # Gabriel (Teilmenge der Delaunay-Kanten) und naechste Nachbarn, periodisch
    tree = cKDTree(pos, boxsize=L)
    mid = np.mod(pos[nz["ei"]] + 0.5 * nz["n"] * nz["d"][:, None], L)
    mid = np.where(mid >= L, 0.0, mid)
    cnt = tree.query_ball_point(mid, r=0.5 * nz["d"] * (1 - 1e-9), return_length=True)
    gab = np.asarray(cnt) == 0
    dnn, nn = tree.query(pos, k=2)
    nn = nn[:, 1]
    pr = dict(nz["pruefung"])
    pr.update({"tetra": int(T), "fem_kopie_gegen_gradient_rel": kopie_abw, "kanten_tetra_gleich_spinnetz": kanten_gleich,
               "fem_zeilensumme_max": float(np.max(np.abs(np.asarray(K.sum(axis=1)).ravel()))),
               "fem_gewicht_negativ_anteil": float(np.mean(w_fem < 0)), "Vt_min": float(Vt.min()),
               "Vt_mittel": float(Vt.mean()), "fem_masse_summe_rel": float(abs(m_fem.sum() / L ** 3 - 1)),
               "sek_netz": time.time() - t0})
    protokoll(f"Netz N={N} saat={saat}: T={T}, E={len(nz['ei'])}, Kanten gleich {kanten_gleich}, FEM-Kopie "
              f"{kopie_abw:.1e}, FEM-Gewichte negativ {pr['fem_gewicht_negativ_anteil']:.4f}, Gabriel {gab.sum()}, "
              f"{time.time() - t0:.1f} s, RSS {rss_mb():.0f} MB")
    return {"N": N, "saat": saat, "L": L, "pos": pos, "ei": nz["ei"], "ej": nz["ej"], "s": nz["s"], "A": nz["A"],
            "d": nz["d"], "n": nz["n"], "V": nz["V"], "G": G, "Kl": Kl, "Vt": Vt, "w_fem": w_fem, "m_fem": m_fem,
            "gab": gab, "nn": nn, "dnn": dnn[:, 1], "pruefung": json.dumps(js(pr))}


def netz_laden(pfad):
    z = np.load(pfad)
    net = {k: z[k] for k in z.files}
    net["N"] = int(net["N"])
    net["L"] = float(net["L"])
    net["pruefung"] = json.loads(str(net["pruefung"]))
    return net


def spin_netz(net):
    return {"art": "zufall", "N": net["N"], "L": net["L"], "pos": net["pos"], "ei": net["ei"], "ej": net["ej"],
            "s": net["s"], "A": net["A"], "d": net["d"], "n": net["n"], "V": net["V"]}


def kanten(net, lesart):
    """(ei, ej, dvec) einer Lesart; dvec = Bildvektor von ei nach ej."""
    if lesart == "delaunay":
        return net["ei"], net["ej"], net["n"] * net["d"][:, None]
    if lesart == "gabriel":
        g = net["gab"]
        return net["ei"][g], net["ej"][g], (net["n"] * net["d"][:, None])[g]
    if lesart == "beruehrung":
        N, L, pos, nn = net["N"], net["L"], net["pos"], net["nn"]
        i = np.arange(N)
        lo, hi = np.minimum(i, nn), np.maximum(i, nn)
        key = np.unique(lo.astype(np.int64) * N + hi)
        ei, ej = key // N, key % N
        dv = pos[ej] - pos[ei]
        dv -= L * np.round(dv / L)
        return ei, ej, dv
    raise ValueError(lesart)


def feld(net, lesart, name):
    """(K csr, Masse m, ei, ej, dvec, w) eines Skalarfelds; w = Kantengewichte (FEM: -K_ij)."""
    N = net["N"]
    ei, ej, dv = kanten(net, lesart)
    d = np.linalg.norm(dv, axis=1)
    if name == "fem":
        assert lesart == "delaunay"
        G, Kl = net["G"], net["Kl"]
        K = sp.coo_matrix((Kl.ravel(), (np.repeat(G, 4, axis=1).ravel(), np.tile(G, (1, 4)).ravel())),
                          shape=(N, N)).tocsr()
        K.sum_duplicates()
        return K, net["m_fem"], ei, ej, dv, net["w_fem"]
    if name == "voronoi":
        assert lesart == "delaunay"
        w, m = net["A"] / net["d"], net["V"]
    elif name == "ungew":
        w, m = np.full(len(ei), 3.0 * N / np.sum(d ** 2)), np.ones(N)
    elif name == "laenge":
        w, m = 3.0 * N / len(ei) / d ** 2, np.ones(N)
    else:
        raise ValueError(name)
    return laplace(N, np.stack([ei, ej], 1), w), m, ei, ej, dv, w


def homogen(N, K, m, ei, ej, dv, w, vol, protokoll, name=""):
    """Exakte Langwellen-Grenze: A_eff = Mittelwert-Tensor - (1/vol) B^T K^+ B (Korrektor per CG, Jacobi)."""
    t0 = time.time()
    voigt = np.einsum("e,ea,eb->ab", w, dv, dv) / vol
    B = np.zeros((N, 3))
    for a in range(3):
        B[:, a] = np.bincount(ei, w * dv[:, a], N) - np.bincount(ej, w * dv[:, a], N)
    bnorm = float(np.max(np.abs(B)) / max(np.max(np.abs(w * np.linalg.norm(dv, axis=1))), 1e-300))
    diag = K.diagonal()
    Mi = sp.diags(1.0 / diag)
    chi = np.zeros((N, 3))
    info, res = [], []
    for a in range(3):
        rhs = B[:, a] - B[:, a].mean()
        if np.linalg.norm(rhs) < 1e-12 * max(1.0, np.abs(w).sum()):
            info.append(0)
            res.append(0.0)
            continue
        x, inf = spla.cg(K, rhs, M=Mi, rtol=1e-11, maxiter=50000)
        chi[:, a] = x
        info.append(int(inf))
        res.append(float(np.linalg.norm(K @ x - rhs) / np.linalg.norm(rhs)))
    korr = B.T @ chi / vol
    korr = 0.5 * (korr + korr.T)
    A = voigt - korr
    rho = m.sum() / vol
    c2 = np.einsum("ra,ab,rb->r", RICHT13, A, RICHT13) / rho
    ew = np.linalg.eigvalsh(A / rho)
    out = {"voigt": voigt, "korrektor": korr, "A_eff": A, "rho": rho, "c_richt13": np.sqrt(np.maximum(c2, 0)),
           "c_eig": np.sqrt(np.maximum(ew, 0)), "c_mittel": float(math.sqrt(max(np.trace(A) / 3 / rho, 0))),
           "c_voigt_mittel": float(math.sqrt(np.trace(voigt) / 3 / rho)), "drift_rel": bnorm, "cg_info": info,
           "cg_residuum": res, "sek": time.time() - t0}
    out["anisotropie"] = float((out["c_richt13"].max() - out["c_richt13"].min()) / out["c_richt13"].mean())
    protokoll(f"homogen {name}: c_mittel {out['c_mittel']:.5f} (Voigt {out['c_voigt_mittel']:.5f}), Anisotropie "
              f"{out['anisotropie']:.2e}, Drift {bnorm:.1e}, CG {info} {max(res):.1e}, {out['sek']:.1f} s")
    return out


def lokal_streuung(net, ei, ej, dv, w, m, zellen=(2, 4, 8)):
    """[Z] Lokale Mittelwert-Tempi: Knotentensor T_i = 1/2 sum_j w d d^T, Zellmittel; c^2(n) = n^T T n / m."""
    N, L, pos = net["N"], net["L"], net["pos"]
    T = np.zeros((N, 3, 3))
    for a in range(3):
        for b in range(a, 3):
            x = 0.5 * w * dv[:, a] * dv[:, b]
            T[:, a, b] = np.bincount(ei, x, N) + np.bincount(ej, x, N)
            T[:, b, a] = T[:, a, b]
    out = {}

    def stat(Tc, mc):
        c2 = np.einsum("ra,cab,rb->cr", RICHT7, Tc, RICHT7) / mc[:, None]
        c = np.sqrt(np.maximum(c2, 0))
        return {"zahl": int(len(mc)), "c2_mittel": float(c2.mean()), "c2_rel_std": float(c2.std() / c2.mean()),
                "c_rel_std": float(c.std() / c.mean()), "c2_negativ_anteil": float(np.mean(c2 < 0)),
                "c_rel_std_ueber_zellen_je_richtung": (c.std(0) / c.mean(0)).tolist(),
                "c_rel_std_ueber_richtungen_mittel": float(np.mean(c.std(1) / np.maximum(c.mean(1), 1e-300))),
                "c2_quantile": np.quantile(c2, [0.01, 0.1, 0.5, 0.9, 0.99]).tolist()}
    out["knoten"] = stat(T, m)
    for s in zellen:
        idx = np.minimum((pos * s / L).astype(int), s - 1)
        cid = (idx[:, 0] * s + idx[:, 1]) * s + idx[:, 2]
        Tc = np.zeros((s ** 3, 3, 3))
        for a in range(3):
            for b in range(3):
                Tc[:, a, b] = np.bincount(cid, T[:, a, b], s ** 3)
        out[f"zellen_{s}"] = stat(Tc, np.bincount(cid, m, s ** 3))
    return out


def min_bild(dv, L):
    return dv - L * np.round(dv / L)


def kuerzeste(net, lesart, nq, protokoll):
    t0 = time.time()
    N, L, pos = net["N"], net["L"], net["pos"]
    ei, ej, dv = kanten(net, lesart)
    d = np.linalg.norm(dv, axis=1)
    A = sp.coo_matrix((d, (ei, ej)), shape=(N, N)).tocsr()
    q = np.random.default_rng([SAAT, N, 7]).choice(N, nq, replace=False)
    T = dijkstra(A, directed=False, indices=q)
    v_q, v_kegel, umweg = [], [], []
    for k, s in enumerate(q):
        rv = min_bild(pos - pos[s], L)
        r = np.linalg.norm(rv, axis=1)
        sel = (r >= 8.0) & (r <= L / 2 - 1.0)
        p = np.polyfit(r[sel], T[k, sel], 1)
        v_q.append(1.0 / p[0])
        far = (r >= L / 2 - 3.0) & (r <= L / 2 - 1.0)
        umweg.append(float(np.mean(T[k, far] / r[far])))
        kz = np.argmax(rv @ KEGEL14.T, axis=1)
        vk = []
        for c in range(14):
            s2 = sel & (kz == c)
            vk.append(1.0 / np.polyfit(r[s2], T[k, s2], 1)[0] if s2.sum() > 20 else np.nan)
        v_kegel.append(vk)
    v_q, v_kegel = np.array(v_q), np.array(v_kegel)
    vk_m = np.nanmean(v_kegel, axis=0)
    out = {"quellen": nq, "v_mittel": float(v_q.mean()), "v_se": float(v_q.std(ddof=1) / math.sqrt(nq)),
           "v_quellen": v_q, "umweg_fern_mittel": float(np.mean(umweg)), "v_kegel_mittel": vk_m,
           "v_kegel_rel_std": float(np.nanstd(vk_m) / np.nanmean(vk_m)),
           "v_quelle_kegel_rel_std_mittel": float(np.nanmean(np.nanstd(v_kegel, 1) / np.nanmean(v_kegel, 1))),
           "sek": time.time() - t0}
    protokoll(f"kuerzeste Wege {lesart}: v = {out['v_mittel']:.4f} +- {out['v_se']:.4f}, Umweg fern "
              f"{out['umweg_fern_mittel']:.4f}, Kegel-Streuung {out['v_kegel_rel_std']:.3f}, {out['sek']:.1f} s")
    return out


def modus_dicht(net, protokoll):
    out = {"N": net["N"], "saat": int(net["saat"]), "pruefung": net["pruefung"]}
    N = net["N"]
    gab = net["gab"]
    nn = net["nn"]
    out["sn7"] = {"grad_gabriel": float(2 * gab.sum() / N), "grad_delaunay": float(2 * len(net["ei"]) / N),
                  "nn_gegenseitig": float(np.mean(nn[nn] == np.arange(N)))}
    ei, ej, dv = kanten(net, "beruehrung")
    out["beruehrung"] = {"E_durch_N": float(len(ei) / N),
                         "inseln_durch_N": inseln(N, np.stack([ei, ej], 1)) / N}
    out["gabriel_inseln"] = inseln(N, np.stack([net["ei"][gab], net["ej"][gab]], 1))
    protokoll(f"SN7: Gabriel {out['sn7']['grad_gabriel']:.4f}, Delaunay {out['sn7']['grad_delaunay']:.4f}, NN "
              f"gegenseitig {out['sn7']['nn_gegenseitig']:.4f}; Beruehrung E/N {out['beruehrung']['E_durch_N']:.4f}")
    vol = net["L"] ** 3
    out["homogen"], out["lokal"] = {}, {}
    for la, fe in (("delaunay", "fem"), ("delaunay", "voronoi"), ("delaunay", "ungew"), ("delaunay", "laenge"),
                   ("gabriel", "ungew"), ("gabriel", "laenge")):
        K, m, ei, ej, dv, w = feld(net, la, fe)
        h = homogen(N, K, m, ei, ej, dv, w, vol, protokoll, f"{la}/{fe}")
        if fe == "ungew":
            d = np.linalg.norm(dv, axis=1)
            fak = math.sqrt((1.0 / d.mean() ** 2) / w[0])
            h["alternativ_takt_mittlere_laenge"] = {"faktor": fak, "c_mittel": h["c_mittel"] * fak,
                                                    "mittlere_laenge": float(d.mean()),
                                                    "mittleres_quadrat": float((d ** 2).mean())}
        out["homogen"][f"{la}/{fe}"] = h
        out["lokal"][f"{la}/{fe}"] = lokal_streuung(net, ei, ej, dv, w, m)
    # Weyl: Mittelwert-Tensor (erste Ordnung der entarteten Stoerungsrechnung)
    Mt = np.zeros((3, 3))
    for a in range(3):
        for b in range(3):
            Mt[a, b] = np.sum(net["A"] * net["d"] * net["n"][:, a] * net["n"][:, b]) / vol
    out["homogen"]["weyl"] = {"M_vol": Mt, "v_richt13": np.linalg.norm(RICHT13 @ Mt, axis=1),
                              "v_mittel": float(np.trace(Mt) / 3)}
    ei, ej, dv = kanten(net, "delaunay")
    out["lokal"]["weyl"] = lokal_streuung(net, ei, ej, dv, net["A"] / net["d"], net["V"])
    out["kuerzeste"] = {la: kuerzeste(net, la, 16, protokoll) for la in ("delaunay", "gabriel")}
    return out


def modus_klein(N, saat0, anzahl, protokoll):
    res = []
    for saat in range(saat0, saat0 + anzahl):
        net = netz_bauen(N, saat, protokoll)
        vol = net["L"] ** 3
        e = {"saat": saat, "pruefung": json.loads(net["pruefung"]),
             "sn7": {"grad_gabriel": float(2 * net["gab"].sum() / N), "grad_delaunay": float(2 * len(net["ei"]) / N),
                     "nn_gegenseitig": float(np.mean(net["nn"][net["nn"]] == np.arange(N)))}, "homogen": {}}
        for la, fe in (("delaunay", "fem"), ("delaunay", "voronoi"), ("delaunay", "ungew"), ("delaunay", "laenge")):
            K, m, ei, ej, dv, w = feld(net, la, fe)
            h = homogen(N, K, m, ei, ej, dv, w, vol, protokoll, f"N={N} s={saat} {fe}")
            e["homogen"][fe] = {x: h[x] for x in ("c_mittel", "c_voigt_mittel", "c_richt13", "c_eig", "anisotropie",
                                                  "drift_rel")}
        res.append(e)
    return {"N": N, "saaten": res}


# ---------------------------------------------------------------------------- Skalar: tiefe Eigenpaare (theta = 0)
def ebene_welle(net, m_vec, masse):
    kv = 2 * math.pi * np.asarray(m_vec, float) / net["L"]
    return kv, np.exp(1j * (net["pos"] @ kv)) / math.sqrt(masse.sum())


def modus_eigen(net, felder, kzahl, protokoll):
    out = {"N": net["N"], "saat": int(net["saat"]), "felder": {}}
    N, L = net["N"], net["L"]
    k1 = 2 * math.pi / L
    for fe in felder:
        t0 = time.time()
        K, m, ei, ej, dv, w = feld(net, "delaunay", fe)
        sig = -1e-3
        A = (K - sig * sp.diags(m)).tocsc()
        lu = spla.splu(A, permc_spec="MMD_AT_PLUS_A", diag_pivot_thresh=0.0, options={"SymmetricMode": True})
        t_lu = time.time() - t0
        op = spla.LinearOperator(A.shape, matvec=lu.solve, dtype=float)
        ev, phi = spla.eigsh(K, k=kzahl, M=sp.diags(m), sigma=sig, which="LM", OPinv=op, tol=1e-10)
        o = np.argsort(ev)
        ev, phi = ev[o], phi[:, o]
        nrm = np.sqrt(np.einsum("in,i,in->n", phi, m, phi))
        phi = phi / nrm[None, :]
        res = np.linalg.norm(K @ phi - (m[:, None] * phi) * ev[None, :], axis=0) / np.maximum(np.abs(ev), 1e-12)
        vol = L ** 3
        c2h = float(np.trace(homogen(N, K, m, ei, ej, dv, w, vol, protokoll, f"eigen {fe}")["A_eff"]) / 3
                    / (m.sum() / vol))
        schale = np.rint(ev / (c2h * k1 ** 2)).astype(int)
        wellen = []
        aehnl = np.zeros(kzahl)
        for mv in M_SCHALEN:
            kv, chi = ebene_welle(net, mv, m)
            c = phi.T @ (m * chi)
            wt = np.abs(c) ** 2
            s2 = int(np.dot(mv, mv))
            sel = schale == s2
            lam = float(np.sum(wt[sel] * ev[sel]) / np.sum(wt[sel])) if wt[sel].sum() > 0 else float("nan")
            kb = float(np.linalg.norm(kv))
            wellen.append({"m": mv, "k": kb, "lambda_zentrum": lam, "c": math.sqrt(lam) / kb if lam > 0 else None,
                           "gewicht_schale": float(wt[sel].sum()), "gewicht_tief": float(wt.sum())})
            aehnl += 2 * wt
        out["felder"][fe] = {"ev": ev, "residuum_max": float(res[1:].max()), "schale": schale, "wellen": wellen,
                             "c2_homogen": c2h, "ebene_welle_anteil_je_mode": aehnl, "sek_lu": t_lu,
                             "lu_nnz": int(lu.L.nnz + lu.U.nnz), "sek": time.time() - t0, "rss_mb": rss_mb()}
        cs = [x["c"] for x in wellen]
        protokoll(f"eigen {fe}: LU {t_lu:.1f} s nnz {out['felder'][fe]['lu_nnz']}, Residuum "
                  f"{out['felder'][fe]['residuum_max']:.1e}, c(k=0,171) {np.round(cs[:3], 5)}, "
                  f"{time.time() - t0:.1f} s, RSS {rss_mb():.0f} MB")
    return out


# ---------------------------------------------------------------------------- Weyl: KPM-Spektralzentren
def weyl_zentren(snz, theta, m_liste, M, protokoll, etikett=""):
    t0 = time.time()
    N, L = snz["N"], snz["L"]
    th = np.zeros(3) if theta is None else np.asarray(theta, float)
    H = sz.matrix(snz, None if theta is None else th)
    sch = sz.schranke(H)
    a = sch["a"]
    sq = np.sqrt(snz["V"] / snz["V"].sum())
    K = len(m_liste)
    Vb = np.zeros((2 * N, K), dtype=complex)
    kv_l = []
    for j, mv in enumerate(m_liste):
        kv = (2 * math.pi * np.asarray(mv, float) + th) / L
        kh = kv / np.linalg.norm(kv)
        S = kh[0] * np.array([[0, 1], [1, 0]]) + kh[1] * np.array([[0, -1j], [1j, 0]]) + kh[2] * np.array(
            [[1, 0], [0, -1]])
        ew, U = np.linalg.eigh(S)
        ph = sq * np.exp(1j * (snz["pos"] @ kv))
        Vb[0::2, j] = ph * U[0, 0]
        Vb[1::2, j] = ph * U[1, 0]
        kv_l.append(kv)
    mu = sz.kpm_block(H * (1.0 / a), Vb, M)
    t_kpm = time.time() - t0
    erg = []
    for j, mv in enumerate(m_liste):
        kb = float(np.linalg.norm(kv_l[j]))
        z = {}
        for MM in (M, M // 2):
            g = sz.jackson(MM)
            Eg = np.linspace(0.3 * kb, 1.7 * kb, 3001)
            rho = sz.kpm_dichte(mu[:MM, j:j + 1], g, a, Eg)[:, 0]
            Em = float(Eg[np.argmax(rho)])
            sE = math.pi * a / MM
            Ew = np.linspace(max(Em - 4 * sE, 1e-6), Em + 4 * sE, 1601)
            rw = sz.kpm_dichte(mu[:MM, j:j + 1], g, a, Ew)[:, 0]
            W = float(np.trapezoid(rw, Ew))
            z[MM] = {"E_max": Em, "E_zentrum": float(np.trapezoid(rw * Ew, Ew) / W), "gewicht_fenster": W,
                     "sigma_E": sE}
        Ec = z[M]["E_zentrum"]
        erg.append({"m": mv, "theta": th, "k": kb, "k_vec": kv_l[j], "E_zentrum": Ec, "v": Ec / kb,
                    "v_halbM": z[M // 2]["E_zentrum"] / kb, "v_max": z[M]["E_max"] / kb,
                    "gewicht_fenster": z[M]["gewicht_fenster"], "erstes_moment": float(mu[1, j] * a),
                    "sigma_E": z[M]["sigma_E"]})
    protokoll(f"weyl {etikett} theta={np.round(th, 3)}: a={a:.3f}, {K} Wellen, M={M}, KPM {t_kpm:.1f} s, v "
              f"{np.round([e['v'] for e in erg], 4)}, |mu|max {np.max(np.abs(mu)):.6f}")
    return {"theta": th, "a": a, "schranke": sch, "M": M, "wellen": erg, "mu_max": float(np.max(np.abs(mu))),
            "sek_kpm": t_kpm, "sek": time.time() - t0}


def modus_weyl(net, M, richtung, protokoll):
    snz = spin_netz(net)
    out = {"N": net["N"], "saat": int(net["saat"]), "M": M, "richtung": richtung, "laeufe": []}
    if richtung == "0":
        out["laeufe"].append(weyl_zentren(snz, None, M_SCHALEN, M, protokoll, "theta0"))
    else:
        e = np.array([1.0, 0, 0]) if richtung == "x" else np.ones(3) / math.sqrt(3)
        for t0 in THETA0:
            out["laeufe"].append(weyl_zentren(snz, t0 * e, M_VERDRILLT[richtung], M, protokoll, f"{richtung}{t0}"))
    return out


# ---------------------------------------------------------------------------- Stoss auf dem grossen Netz
def modus_welle(net, lesart, name, nq, tmax, protokoll):
    t0 = time.time()
    N, L, pos = net["N"], net["L"], net["pos"]
    out = {"N": N, "saat": int(net["saat"]), "lesart": lesart, "feld": name, "tmax": tmax}
    if lesart == "alle":
        m = np.ones(N)
        lam_max = float(N)

        def Ku(u):
            return N * u - u.sum()
        ei = ej = np.zeros(0, dtype=np.int64)
        w = np.zeros(0)
    else:
        K, m, ei, ej, dv, w = feld(net, lesart, name)
        s = 1.0 / np.sqrt(m)
        As = sp.diags(s) @ K @ sp.diags(s)
        lam_max = float(spla.eigsh(As, k=1, which="LA", tol=1e-4, return_eigenvectors=False)[0])

        def Ku(u):
            return K @ u
    dt = min(0.5 / math.sqrt(lam_max), 0.05)
    nschritte = int(math.ceil(tmax / dt))
    if nschritte > 400000:
        dt = tmax / 400000
        nschritte = 400000
        if dt * math.sqrt(lam_max) > 1.9:
            raise SystemExit(f"Zeitschritt instabil: omega_max dt = {dt * math.sqrt(lam_max):.2f}")
    out.update({"lambda_max": lam_max, "dt": dt, "schritte": nschritte, "omega_dt": dt * math.sqrt(lam_max)})
    q = np.random.default_rng([SAAT, N, 9]).choice(N, nq, replace=False)
    if lesart != "alle":
        A = sp.coo_matrix((np.ones(len(ei)), (ei, ej)), shape=(N, N)).tocsr()
        A = A + A.T
    proben = []
    tz = np.round(np.arange(0.25, tmax + 1e-9, 0.25), 6)
    zei = set(np.rint(tz / dt).astype(int).tolist())
    schnapp = {}
    mittel_l = float(np.mean(np.linalg.norm(kanten(net, lesart)[2], axis=1))) if lesart != "alle" else float("nan")
    for qi, s in enumerate(q):
        rv = min_bild(pos - pos[s], L)
        r = np.linalg.norm(rv, axis=1)
        kz = np.argmax(rv @ KEGEL14.T, axis=1)
        kz[s] = -1
        if lesart != "alle":
            h = shortest_path(A, unweighted=True, directed=False, indices=int(s))
            insel = np.isfinite(h)
        else:
            h = np.where(np.arange(N) == s, 0.0, 1.0)
            insel = np.ones(N, bool)
        ord_r = np.argsort(r)
        u_prev = np.zeros(N)
        v0 = np.zeros(N)
        v0[s] = 1.0 / m[s]
        u = dt * v0
        reihe = []
        nbild = 0
        for n in range(1, nschritte + 1):
            u_next = 2 * u - u_prev - dt * dt * Ku(u) / m
            if n in zei:
                t = n * dt
                v = (u_next - u_prev) / (2 * dt)
                e = 0.5 * m * v * v
                if lesart == "alle":
                    epot = np.zeros(N)
                elif name == "fem":
                    uT = u[net["G"]]
                    et = 0.5 * np.einsum("ta,tab,tb->t", uT, net["Kl"], uT)
                    epot = np.bincount(net["G"].ravel(), np.repeat(et / 4.0, 4), N)
                else:
                    ee = 0.5 * w * (u[ei] - u[ej]) ** 2
                    epot = 0.5 * (np.bincount(ei, ee, N) + np.bincount(ej, ee, N))
                e = e + epot
                Et = e.sum()
                ce = np.cumsum(e[ord_r]) / Et
                R50 = float(r[ord_r][np.searchsorted(ce, 0.5)])
                R90 = float(r[ord_r][min(np.searchsorted(ce, 0.9), N - 1)])
                rk = []
                for c in range(14):
                    sel = kz == c
                    es = e[sel]
                    if es.sum() <= 0:
                        rk.append(float("nan"))
                        continue
                    o2 = np.argsort(r[sel])
                    cc = np.cumsum(es[o2]) / es.sum()
                    rk.append(float(r[sel][o2][min(np.searchsorted(cc, 0.9), len(o2) - 1)]))
                hf = np.isfinite(h)
                hm = float(np.sum(e[hf] * h[hf]) / Et)
                oh = np.argsort(h[hf])
                ch = np.cumsum(e[hf][oh]) / Et
                H90 = float(h[hf][oh][min(np.searchsorted(ch, 0.9), hf.sum() - 1)])
                ein = {"t": t, "E": float(Et), "R50": R50, "R90": R90, "R90_kegel": rk, "hop_mittel": hm, "H90": H90,
                       "E_ausserhalb_insel": float(e[~insel].sum() / Et), "E_quelle": float(e[s] / Et)}
                if lesart == "alle":
                    andere = np.arange(N) != s
                    ein["spread_andere"] = float(u[andere].max() - u[andere].min())
                reihe.append(ein)
                if qi == 0 and nbild < len(BILD_ZEITEN_B) and abs(t - BILD_ZEITEN_B[nbild]) < 0.5 * dt + 1e-9:
                    slab = np.abs(rv[:, 2]) < 1.0
                    schnapp[f"u{nbild}"] = u[slab]
                    if nbild == 0:
                        schnapp["xy"] = rv[slab, :2]
                        idx = -np.ones(N, dtype=np.int64)
                        idx[slab] = np.arange(slab.sum())
                        if lesart != "alle":
                            ks = slab[ei] & slab[ej]
                            ka, kb_ = idx[ei[ks]], idx[ej[ks]]
                            lang = np.linalg.norm(schnapp["xy"][ka] - schnapp["xy"][kb_], axis=1) < 6.0
                            schnapp["kanten"] = np.stack([ka[lang], kb_[lang]], 1)
                    nbild += 1
            u_prev, u = u, u_next
        proben.append({"quelle": int(s), "reihe": reihe})
        protokoll(f"welle {lesart}/{name} Quelle {qi}: R90(t=8) {next((x['R90'] for x in reihe if abs(x['t'] - 8) < 1e-6), None)}, "
                  f"E-Drift {reihe[-1]['E'] / reihe[0]['E'] - 1:.1e}, {time.time() - t0:.1f} s")
    out.update({"proben": proben, "mittlere_kantenlaenge": mittel_l, "sek": time.time() - t0, "rss_mb": rss_mb()})
    return out, schnapp


# ---------------------------------------------------------------------------- Kontrollen
def modus_kontrolle(M, protokoll):
    out = {}
    # K1: Weyl-KPM-Zentren gegen analytisch auf dem kubischen Gitter
    Lg = 37
    gz = sz.gitternetz(Lg)
    k1 = []
    for theta, ml in ((None, M_SCHALEN), (np.array([0.8, 0.0, 0.0]), [(0, 0, 0)])):
        r = weyl_zentren(gz, theta, ml, M, protokoll, "gitter")
        for w in r["wellen"]:
            kv = np.asarray(w["k_vec"])
            Eex = float(np.sqrt(np.sum(np.sin(kv) ** 2)))
            k1.append({"m": w["m"], "k": w["k"], "v_kpm": w["v"], "v_exakt": Eex / w["k"], "abw": w["v"] - Eex / w["k"],
                       "v_halbM": w["v_halbM"]})
    out["K1_weyl_gitter"] = k1
    protokoll(f"K1 Weyl-Gitter: max |v_kpm - v_exakt| {max(abs(x['abw']) for x in k1):.2e}")
    # K2: Skalar-Eigenpaare (7-Punkt-Laplace) gegen analytisch
    net_g = {"N": gz["N"], "L": gz["L"], "pos": gz["pos"]}
    K = laplace(gz["N"], np.stack([gz["ei"], gz["ej"]], 1), np.ones(len(gz["ei"])))
    m = np.ones(gz["N"])
    t0 = time.time()
    A = (K + 1e-3 * sp.identity(gz["N"])).tocsc()
    lu = spla.splu(A, permc_spec="MMD_AT_PLUS_A", diag_pivot_thresh=0.0, options={"SymmetricMode": True})
    op = spla.LinearOperator(A.shape, matvec=lu.solve, dtype=float)
    ev, phi = spla.eigsh(K, k=40, sigma=-1e-3, which="LM", OPinv=op, tol=1e-10)
    o = np.argsort(ev)
    ev, phi = ev[o], phi[:, o]
    k1g = 2 * math.pi / Lg
    schale = np.rint(ev / k1g ** 2).astype(int)
    k2 = []
    for mv in M_SCHALEN:
        kv, chi = ebene_welle(net_g, mv, m)
        wt = np.abs(phi.T @ chi) ** 2
        sel = schale == int(np.dot(mv, mv))
        lam = float(np.sum(wt[sel] * ev[sel]) / np.sum(wt[sel]))
        lex = float(np.sum(4 * np.sin(kv / 2) ** 2))
        k2.append({"m": mv, "c_eigen": math.sqrt(lam) / np.linalg.norm(kv), "c_exakt": math.sqrt(lex) / np.linalg.norm(kv),
                   "gewicht": float(wt[sel].sum())})
    out["K2_skalar_gitter"] = {"wellen": k2, "sek": time.time() - t0, "lu_nnz": int(lu.L.nnz + lu.U.nnz)}
    protokoll(f"K2 Skalar-Gitter: max |c_eigen - c_exakt| {max(abs(x['c_eigen'] - x['c_exakt']) for x in k2):.2e}, "
              f"{time.time() - t0:.1f} s")
    # K3: Homogenisierung, geschichtetes Gitter (x-Federn abwechselnd 1 und 3): A_xx = 1,5 exakt
    Lh = 12
    gh = sz.gitternetz(Lh)
    ei, ej = gh["ei"], gh["ej"]
    dv = gh["n"].copy()
    xa = gh["pos"][ei, 0].astype(int)
    w = np.where(dv[:, 0] > 0.5, np.where(xa % 2 == 0, 1.0, 3.0), 1.0)
    Kh = laplace(gh["N"], np.stack([ei, ej], 1), w)
    h = homogen(gh["N"], Kh, np.ones(gh["N"]), ei, ej, dv, w, float(Lh ** 3), protokoll, "K3 geschichtet")
    out["K3_homogen_geschichtet"] = {"A_eff": h["A_eff"], "voigt": h["voigt"], "soll_xx": 1.5,
                                     "abw": float(abs(h["A_eff"][0, 0] - 1.5))}
    # K4: kleines Zufallsnetz: Kanten, FEM-Kopie, Patch-Test, Mittelwert-Tensoren
    net = netz_bauen(1000, 999, protokoll)
    pr = json.loads(net["pruefung"])
    vol = net["L"] ** 3
    k4 = {"pruefung": pr}
    for fe in ("fem", "voronoi", "ungew", "laenge"):
        K, m, ei, ej, dv, w = feld(net, "delaunay", fe)
        hh = homogen(net["N"], K, m, ei, ej, dv, w, vol, protokoll, f"K4 {fe}")
        k4[fe] = {"drift_rel": hh["drift_rel"], "voigt": hh["voigt"], "c_mittel": hh["c_mittel"],
                  "zeilensumme": float(np.max(np.abs(np.asarray(K.sum(axis=1)).ravel())))}
    out["K4_netz_1000"] = k4
    return out


# ---------------------------------------------------------------------------- main
def main():
    modus = sys.argv[1]
    t0 = time.time()
    log = []

    def protokoll(s):
        print(s, flush=True)
        log.append(s)

    out = {"modus": modus, "argv": sys.argv[1:], "numpy": np.__version__, "scipy": scipy.__version__}
    opts = {a.split("=")[0]: a.split("=")[1] for a in sys.argv[2:] if "=" in a}
    pos = [a for a in sys.argv[2:] if "=" not in a]
    if modus == "teilA":
        saat0, anzahl, ziel = int(pos[0]), int(pos[1]), pos[2]
        out.update(teilA(saat0, anzahl, int(opts.get("ansichten", 2000)), int(opts.get("beruehr", 500)),
                         int(opts.get("stoss", 200)), protokoll))
    elif modus == "netz":
        N, saat, ziel = int(pos[0]), int(pos[1]), pos[2]
        net = netz_bauen(N, saat, protokoll)
        np.savez(ziel + ".tmp.npz", **net)
        os.replace(ziel + ".tmp.npz", ziel)
        out.update({"N": N, "saat": saat, "pruefung": json.loads(net["pruefung"]), "rss_mb": rss_mb()})
        ziel = ziel + ".json"
    elif modus == "dicht":
        ziel = pos[1]
        out.update(modus_dicht(netz_laden(pos[0]), protokoll))
    elif modus == "klein":
        N, saat0, anzahl, ziel = int(pos[0]), int(pos[1]), int(pos[2]), pos[3]
        out.update(modus_klein(N, saat0, anzahl, protokoll))
    elif modus == "eigen":
        ziel = pos[1]
        felder = opts.get("felder", "fem,voronoi,ungew,laenge").split(",")
        out.update(modus_eigen(netz_laden(pos[0]), felder, int(opts.get("k", 40)), protokoll))
    elif modus == "weyl":
        ziel = pos[1]
        out.update(modus_weyl(netz_laden(pos[0]), int(pos[2]), pos[3], protokoll))
    elif modus == "welle":
        ziel = pos[1]
        r, schnapp = modus_welle(netz_laden(pos[0]), pos[2], pos[3], int(pos[4]), float(opts.get("tmax", 16.0)),
                                 protokoll)
        out.update(r)
        if schnapp:
            np.savez(ziel + ".tmp.npz", **schnapp)
            os.replace(ziel + ".tmp.npz", ziel + ".npz")
        ziel = ziel + ".json"
    elif modus == "kontrolle":
        ziel = pos[0]
        out.update(modus_kontrolle(int(opts.get("M", 4096)), protokoll))
    else:
        raise SystemExit("unbekannter Modus")
    out["laufzeit_gesamt_s"] = time.time() - t0
    out["rss_mb"] = rss_mb()
    out["protokoll"] = log
    speichern(ziel, out)
    print("geschrieben", ziel, f"{time.time() - t0:.1f} s, RSS {rss_mb():.0f} MB", flush=True)


if __name__ == "__main__":
    main()
