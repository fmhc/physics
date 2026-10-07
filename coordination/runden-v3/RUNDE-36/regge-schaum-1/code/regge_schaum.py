"""REGGE-SCHAUM-1 (Runde 36, Leitung claude-primary): linearer Regge-Eckenoperator auf Kuhn-, Wackel- und
Poisson-Delaunay-Netzen in einer Kugel. Ansatz wie REGGE-RAND-1: l_e = l0_e psi_mitte^2, psi_mitte = Mittel der Enden,
linear delta l_e = l0_e (delta psi_a + delta psi_b). Operator L = B^T J B mit J_ef = d eps_e / d l_f.

Aufruf (nur ueber kleintest.sh auf der .69): regge_schaum.py <netz K|J|P> <R0> <saat> <ausgabe.json>
"""
import hashlib
import itertools
import json
import os
import sys
import time

import numpy as np
import scipy
import scipy.sparse as sp
import scipy.sparse.linalg as spla
from scipy.spatial import Delaunay

PAARE = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
ANDERE = [(2, 3), (1, 3), (1, 2), (0, 3), (0, 2), (0, 1)]
WACKEL = 0.25          # Breite des Wackelintervalls je Koordinate (Netz J)
H_KOMPLEX = 1e-20      # komplexer Schritt
SKRIPT_SHA = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()


# ---------------------------------------------------------------- Netze
def gitter(n):
    g = np.arange(-n, n + 1)
    return np.stack(np.meshgrid(g, g, g, indexing="ij"), -1).reshape(-1, 3)


def kuhn_kugel(R0):
    n = int(np.ceil(R0)) + 1
    M = 2 * n + 1
    X = gitter(n)

    def nummer(P):
        return ((P[:, 0] + n) * M + (P[:, 1] + n)) * M + (P[:, 2] + n)

    E = np.eye(3, dtype=np.int64)
    basis = X[np.all(X < n, axis=1)]
    tets = []
    for p in itertools.permutations(range(3)):
        v0 = basis
        v1 = v0 + E[p[0]]
        v2 = v1 + E[p[1]]
        v3 = v2 + E[p[2]]
        drin = np.ones(len(v0), bool)
        for v in (v0, v1, v2, v3):
            drin &= (v ** 2).sum(1) <= R0 * R0
        tets.append(np.stack([nummer(v[drin]) for v in (v0, v1, v2, v3)], 1))
    tets = np.vstack(tets)
    benutzt = np.unique(tets)
    neu = -np.ones(len(X), dtype=np.int64)
    neu[benutzt] = np.arange(len(benutzt))
    return X[benutzt].astype(float), neu[tets], 0


def delaunay_kugel(X, R0):
    X = X[(X ** 2).sum(1) < R0 * R0]
    tri = Delaunay(X)
    return X, tri.simplices.astype(np.int64), int(len(tri.coplanar))


def netz(art, R0, saat):
    rng = np.random.default_rng(np.random.SeedSequence([20261004, 36, int(saat), ord(art)]))
    if art == "K":
        return kuhn_kugel(R0)
    if art == "J":
        X = gitter(int(np.ceil(R0)) + 2).astype(float)
        X = X + WACKEL * (rng.random(X.shape) - 0.5)
        return delaunay_kugel(X, R0)
    if art == "P":
        N = int(round(4.0 / 3.0 * np.pi * R0 ** 3))
        teile, n = [], 0
        while n < N:
            Y = (rng.random((2 * N, 3)) * 2.0 - 1.0) * R0
            Y = Y[(Y ** 2).sum(1) < R0 * R0]
            teile.append(Y)
            n += len(Y)
        return delaunay_kugel(np.vstack(teile)[:N], R0)
    raise SystemExit("unbekanntes Netz: " + art)


# ---------------------------------------------------------------- Diederwinkel aus sechs Laengen (komplex tauglich)
def kosinus(l):
    """Kosinus der sechs Diederwinkel; analytisch in l, daher fuer den komplexen Schritt geeignet."""
    l01, l02, l03, l12, l13, l23 = (l[:, k] for k in range(6))
    x2 = (l01 ** 2 + l02 ** 2 - l12 ** 2) / (2 * l01)
    y2 = np.sqrt(l02 ** 2 - x2 ** 2)
    x3 = (l01 ** 2 + l03 ** 2 - l13 ** 2) / (2 * l01)
    y3 = (l02 ** 2 + l03 ** 2 - l23 ** 2 - 2 * x2 * x3) / (2 * y2)
    z3 = np.sqrt(l03 ** 2 - x3 ** 2 - y3 ** 2)
    null = np.zeros_like(l01)
    P = [np.stack([null, null, null], 1), np.stack([l01, null, null], 1),
         np.stack([x2, y2, null], 1), np.stack([x3, y3, z3], 1)]
    th = []
    for k, (i, j) in enumerate(PAARE):
        a, b = ANDERE[k]
        ab = P[j] - P[i]
        ab = ab / np.sqrt((ab * ab).sum(1))[:, None]
        u = P[a] - P[i]
        u = u - (u * ab).sum(1)[:, None] * ab
        w = P[b] - P[i]
        w = w - (w * ab).sum(1)[:, None] * ab
        th.append((u * w).sum(1) / np.sqrt((u * u).sum(1) * (w * w).sum(1)))
    return np.stack(th, 1)


def dieder(l):
    return np.arccos(kosinus(l))


def ableitungen(l0):
    """D[t, e, f] = d theta_e / d l_f je Tetraeder: komplexer Schritt im Kosinus, dann d arccos = -dc/sqrt(1 - c^2)."""
    D = np.empty((len(l0), 6, 6))
    for f in range(6):
        lc = l0.astype(complex)
        lc[:, f] += 1j * H_KOMPLEX
        c = kosinus(lc)
        D[:, :, f] = -(c.imag / H_KOMPLEX) / np.sqrt(1.0 - c.real ** 2)
    return D


# ---------------------------------------------------------------- Auswertung
def main():
    art, R0, saat, ausgabe = sys.argv[1], float(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    t0 = time.time()
    X, T, koplanar = netz(art, R0, saat)
    NV, NT = len(X), len(T)
    ia = np.array([i for i, j in PAARE])
    ib = np.array([j for i, j in PAARE])
    l0 = np.linalg.norm(X[T[:, ib]] - X[T[:, ia]], axis=2)                      # (T, 6)
    d1, d2, d3 = (X[T[:, k]] - X[T[:, 0]] for k in (1, 2, 3))
    Vt = np.abs(np.einsum("ij,ij->i", d1, np.cross(d2, d3))) / 6.0
    # Kanten
    a, b = T[:, ia], T[:, ib]
    schl = np.minimum(a, b) * NV + np.maximum(a, b)
    kanten, kid = np.unique(schl.ravel(), return_inverse=True)
    kid = kid.reshape(-1, 6)
    NE = len(kanten)
    ka, kb = kanten // NV, kanten % NV
    l0k = np.linalg.norm(X[kb] - X[ka], axis=1)
    # Rand ueber Dreiecke, die nur einmal vorkommen
    F = np.sort(np.concatenate([T[:, [0, 1, 2]], T[:, [0, 1, 3]], T[:, [0, 2, 3]], T[:, [1, 2, 3]]]), axis=1)
    fs = (F[:, 0] * NV + F[:, 1]) * NV + F[:, 2]
    fu, fc = np.unique(fs, return_counts=True)
    rf = fu[fc == 1]
    rf3 = np.stack([rf // (NV * NV), (rf // NV) % NV, rf % NV], 1)
    rand = np.zeros(NV, bool)
    rand[rf3.ravel()] = True
    im_netz = np.zeros(NV, bool)
    im_netz[T.ravel()] = True
    innen = im_netz & ~rand
    randkante = np.zeros(NE, bool)
    for p, q in ((0, 1), (0, 2), (1, 2)):
        s = np.minimum(rf3[:, p], rf3[:, q]) * NV + np.maximum(rf3[:, p], rf3[:, q])
        randkante[np.searchsorted(kanten, s)] = True
    # Flachheit
    th0 = dieder(l0)
    summe = np.zeros(NE)
    np.add.at(summe, kid.ravel(), th0.ravel())
    eps_flach = float(np.max(np.abs(2 * np.pi - summe[~randkante]))) if np.any(~randkante) else None
    # Ableitungen und Operator
    t1 = time.time()
    D = ableitungen(l0)
    S = np.einsum("te,tef->tf", l0, D)
    Sabs = np.einsum("te,tef->tf", l0, np.abs(D))
    schlaefli = float(np.max(np.abs(S) / Sabs))
    R = np.broadcast_to(kid[:, :, None], D.shape).ravel()
    C = np.broadcast_to(kid[:, None, :], D.shape).ravel()
    J = sp.coo_matrix((-D.ravel(), (R, C)), shape=(NE, NE)).tocsr()
    zeilen = np.concatenate([np.arange(NE), np.arange(NE)])
    B = sp.coo_matrix((np.concatenate([l0k, l0k]), (zeilen, np.concatenate([ka, kb]))), shape=(NE, NV)).tocsr()
    L = (B.T @ (J @ B)).tocsr()
    del D, J, R, C
    t2 = time.time()
    Lc = L.tocoo()
    lr, lc_, ld = Lc.row, Lc.col, Lc.data
    symmetrie = float(abs(L - L.T).max() / abs(L).max())
    # Kontrollen L 1 und L x auf inneren Zeilen
    zeile_abs = np.bincount(lr, weights=np.abs(ld), minlength=NV)
    l_eins = float(np.max(np.abs(L @ np.ones(NV))[innen] / zeile_abs[innen]))
    l_lin = []
    for i in range(3):
        xi = X[:, i]
        skala = np.bincount(lr, weights=np.abs(ld) * np.abs(xi[lc_] - xi[lr]), minlength=NV)
        l_lin.append(float(np.max(np.abs(L @ xi)[innen] / skala[innen])))
    # Eckenvolumen
    Vv = np.zeros(NV)
    np.add.at(Vv, T.ravel(), np.repeat(Vt / 4.0, 4))
    rabs = np.linalg.norm(X, axis=1)
    werte = {
        "netz": art, "R0": R0, "saat": saat, "ecken": int(NV), "tetraeder": int(NT), "kanten": int(NE),
        "ecken_innen": int(innen.sum()), "ecken_rand": int(rand.sum()), "koplanar_unbenutzt": koplanar,
        "volumen_min": float(Vt.min()), "volumen_mittel": float(Vt.mean()),
        "kontrollen": {"max_fehlwinkel_flach_innen": eps_flach, "schlaefli_rel": schlaefli,
                       "symmetrie_rel": symmetrie, "L_eins_rel": l_eins, "L_linear_rel": l_lin},
    }
    # Kuhn-Schablone
    if art == "K":
        tief = innen[lr] & (rabs[lr] < R0 - 3)
        dvec = X[lc_] - X[lr]
        dist1 = np.abs(dvec).sum(1)
        soll = np.where(lr == lc_, 48.0, np.where((dist1 == 1) & (np.abs(dvec).max(1) == 1), -8.0, 0.0))
        zahl_achse = np.bincount(lr[tief & (soll == -8.0)], minlength=NV)
        werte["kontrollen"]["kuhn_schablone_max_abw"] = float(np.max(np.abs(ld[tief] - soll[tief])))
        werte["kontrollen"]["kuhn_achsnachbarn_min"] = int(zahl_achse[innen & (rabs < R0 - 3)].min())
    # Quadrattest und Tensor K
    sel = innen & (rabs < R0 - 2)
    quad = {}
    for i, name in enumerate("xyz"):
        q = X[:, i] ** 2
        Lq = L @ q
        rat = Lq[sel] / (-16.0 * Vv[sel])
        quad[name] = {"gewichtet": float(Lq[sel].sum() / (-16.0 * Vv[sel].sum())), "mittel": float(rat.mean()),
                      "std": float(rat.std()), "q05": float(np.quantile(rat, 0.05)),
                      "q50": float(np.quantile(rat, 0.5)), "q95": float(np.quantile(rat, 0.95))}
    werte["quadrattest"] = quad
    selk = innen & (rabs < 0.7 * R0)
    m = selk[lr] & (lr != lc_)
    dx = X[lc_[m]] - X[lr[m]]
    K = -(ld[m][:, None, None] * dx[:, :, None] * dx[:, None, :]).sum(0) / (2.0 * Vv[selk].sum())
    werte["K_durch_8"] = (K / 8.0).tolist()
    werte["K_durch_8_eigenwerte"] = np.linalg.eigvalsh(K / 8.0).tolist()
    # Newton
    t3 = time.time()
    kand = np.nonzero(innen)[0]
    quelle = int(kand[np.argmin(rabs[kand])])
    r = np.linalg.norm(X - X[quelle], axis=1)
    Iidx = np.nonzero(innen)[0]
    Bidx = np.nonzero(rand)[0]
    psi = np.zeros(NV)
    psi[Bidx] = 1.0 / (2.0 * r[Bidx])
    L_II = L[Iidx][:, Iidx].tocsc()
    rhs = -(L[Iidx][:, Bidx] @ psi[Bidx])
    rhs[np.searchsorted(Iidx, quelle)] += 16.0 * np.pi
    psiI = spla.spsolve(L_II, rhs)
    resid = float(np.linalg.norm(L_II @ psiI - rhs) / np.linalg.norm(rhs))
    psi[Iidx] = psiI
    f = 2.0 * r * psi
    schalen = []
    for k in range(2, int(0.9 * R0)):
        mm = innen & (r >= k) & (r < k + 1)
        if mm.sum() > 0:
            schalen.append({"r": k + 0.5, "n": int(mm.sum()), "f_mittel": float(f[mm].mean()),
                            "f_std": float(f[mm].std())})
    mm = innen & (r >= 4) & (r <= 14)
    b_fit, a_fit = np.polyfit(r[mm], f[mm], 1)
    werte["newton"] = {"quelle": quelle, "quelle_ort": X[quelle].tolist(), "residuum_rel": resid,
                       "a": float(a_fit), "b": float(b_fit), "schalen": schalen}
    # Kleinste Eigenwerte des inneren Blocks
    t4 = time.time()
    try:
        ew0 = spla.eigsh(L_II, k=4, sigma=0.0, which="LM", return_eigenvectors=False)
        werte["eigen_nahe_null"] = sorted(float(x) for x in ew0)
    except Exception as err:  # noqa: BLE001
        werte["eigen_nahe_null"] = "Fehler: " + repr(err)[:200]
    try:
        ewsa = spla.eigsh(L_II.tocsr(), k=2, which="SA", tol=1e-6, ncv=64, maxiter=1500,
                          return_eigenvectors=False)
        werte["eigen_kleinste_algebraisch"] = sorted(float(x) for x in ewsa)
    except spla.ArpackNoConvergence as err:
        werte["eigen_kleinste_algebraisch"] = {"nicht_konvergiert": [float(x) for x in err.eigenvalues]}
    t5 = time.time()
    werte["zeiten_s"] = {"netz": round(t1 - t0, 2), "operator": round(t2 - t1, 2), "pruefungen": round(t3 - t2, 2),
                         "newton": round(t4 - t3, 2), "eigenwerte": round(t5 - t4, 2)}
    werte["skript_sha256"] = SKRIPT_SHA
    werte["numpy"] = np.__version__
    werte["scipy"] = scipy.__version__
    werte["zeit_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    with open(ausgabe, "w") as fh:
        json.dump(werte, fh, indent=1)
    kurz = {k: werte[k] for k in ("netz", "R0", "ecken", "ecken_innen", "kontrollen", "K_durch_8_eigenwerte", "zeiten_s")}
    kurz["quadrat_gewichtet"] = [quad[c]["gewichtet"] for c in "xyz"]
    kurz["quadrat_std"] = [quad[c]["std"] for c in "xyz"]
    kurz["newton_a_b"] = [werte["newton"]["a"], werte["newton"]["b"]]
    kurz["eigen_nahe_null"] = werte["eigen_nahe_null"]
    kurz["eigen_kleinste_algebraisch"] = werte["eigen_kleinste_algebraisch"]
    print(json.dumps(kurz))


if __name__ == "__main__":
    main()
