#!/usr/bin/env python3
"""SPIN-ZUFALLSNETZ-1 (Runde 39, Code-Agent): eingesetzter Weyl-Operator auf periodischen 3D-Poisson-Delaunay-Netzen
mit Voronoi-Gewichten und auf dem einfach-kubischen Gitter (Kontrolle SZ0).

Operator (PLAN Abschnitt 2):
  Block H0_ij = (i/2) A_ij (sigma . n_ij) exp(i theta . s_ij), H0_ji = H0_ij^dagger, H = V^-1/2 H0 V^-1/2.
  A_ij Voronoi-Facettenflaeche der Delaunay-Kante, n_ij Einheitsvektor von i zum Bild von j, s_ij ganzzahliger
  Bildversatz, theta Verdrillung (Bloch-Phase je Torusumlauf), V_i Voronoi-Volumen aus der Pyramidenzerlegung
  V_i = sum_j A_ij d_ij / 6. Kubisch: A = d = V = 1, H(k) = -sum_a sigma_a sin k_a.
  Langwellig gilt H ~ -sigma.k (Vorzeichenkonvention dieses Codes): E > 0 gehoert zu sigma.k^ = -1.

Aufruf (nur ueber kleintest.sh):
  python spinnetz.py kontrolle <aus.json>
  python spinnetz.py gitter <L> <aus.json> kpm=<M>,<T>,<B>
  python spinnetz.py netz <N> <saat0> <anzahl> <aus.json> [eig=<k>] [kpm=<M>,<T>,<B>]
    kpm: M Momente, T Verdrillungen (zufaellig), B Zufallsvektoren je Verdrillung.
"""
import json
import math
import os
import sys
import time

import numpy as np
import scipy
import scipy.linalg as sla
import scipy.sparse as sp
import scipy.sparse.linalg as spla
from scipy.spatial import Delaunay

SAAT_BASIS = 39
SAUM = 4.0
THETA_EIG = np.array([0.05, 0.08, 0.11])   # kleine feste Verdrillung fuer die Eigenpaare (hebt Kramers auf)
E_FENSTER = 0.35                            # unterstes Energiefenster fuer SZ2 (N = 1e4)
K_MAX = 0.75                                # Ebene-Wellen-Basis |k| <= K_MAX (m != 0)
EPS_GITTER = [0.20, 0.25, 0.30, 0.35, 0.40]  # Fenster fuer SZ0/SZ1
EPS0 = 0.05                                 # SZ3-Fenster |E| < EPS0
M_WAHL = [(1, 0, 0), (2, 0, 0), (3, 0, 0), (1, 1, 0), (2, 2, 0), (1, 1, 1), (2, 2, 2)]   # Wellen bei N >= 5e4
EPS_FEIN = np.round(np.arange(0.02, 1.0001, 0.01), 4)
E_RASTER = np.round(np.arange(-1.5, 1.50001, 0.005), 4)


def js(x):
    if isinstance(x, dict):
        return {str(k): js(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [js(v) for v in x]
    if isinstance(x, np.ndarray):
        return js(x.tolist())
    if isinstance(x, (np.integer,)):
        return int(x)
    if isinstance(x, (np.floating,)):
        return float(x)
    if isinstance(x, (np.bool_,)):
        return bool(x)
    if isinstance(x, complex):
        return [x.real, x.imag]
    return x


# ---------------------------------------------------------------------- Geometrie
def umkreis_tetra(X):
    a = X[:, 0]
    u, v, w = X[:, 1] - a, X[:, 2] - a, X[:, 3] - a
    vw, wu, uv = np.cross(v, w), np.cross(w, u), np.cross(u, v)
    det = np.einsum("ij,ij->i", u, vw)
    num = (u * u).sum(1)[:, None] * vw + (v * v).sum(1)[:, None] * wu + (w * w).sum(1)[:, None] * uv
    return a + num / (2.0 * det[:, None]), det


def umkreis_dreieck(a, b, c):
    u, v = b - a, c - a
    uxv = np.cross(u, v)
    num = np.cross((u * u).sum(1)[:, None] * v - (v * v).sum(1)[:, None] * u, uxv)
    return a + num / (2.0 * (uxv * uxv).sum(1)[:, None])


KANTEN_LOKAL = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2), (1, 2, 0, 3), (1, 3, 2, 0), (2, 3, 0, 1)]


def zufallsnetz(N, saat, saum=SAUM):
    """N Poisson-Punkte (Dichte 1) im Torus [0, L)^3; periodische Delaunay-Triangulierung ueber Saum-Kopien;
    Voronoi-Facettenflaechen aus Tetraeder- und Dreiecks-Umkreismittelpunkten (vorzeichenbehaftete Viereckstuecke)."""
    t0 = time.time()
    rng = np.random.default_rng([SAAT_BASIS, int(N), int(saat)])
    L = float(N) ** (1.0 / 3.0)
    pos = rng.uniform(0.0, L, size=(N, 3))
    offs = np.array([(a, b, c) for a in (-1, 0, 1) for b in (-1, 0, 1) for c in (-1, 0, 1)], dtype=np.int64)
    Pl, Il, Ol = [], [], []
    for o in offs:
        Q = pos + o * L
        m = np.all((Q >= -saum) & (Q <= L + saum), axis=1)
        Pl.append(Q[m])
        Il.append(np.nonzero(m)[0])
        Ol.append(np.repeat(o[None, :], int(m.sum()), axis=0))
    P = np.concatenate(Pl)
    gidx = np.concatenate(Il)
    goff = np.concatenate(Ol)
    S = Delaunay(P).simplices
    X = P[S]
    cen = X.mean(axis=1)
    halte = np.all((cen >= 0.0) & (cen < L), axis=1)
    S, X = S[halte], X[halte]
    C, det = umkreis_tetra(X)
    flip = det < 0
    S[flip] = S[flip][:, [0, 2, 1, 3]]
    X = P[S]
    C, det = umkreis_tetra(X)
    R = np.linalg.norm(C - X[:, 0], axis=1)
    box_verletzt = int(np.sum(np.any((C - R[:, None] < -saum) | (C + R[:, None] > L + saum), axis=1)))
    T = S.shape[0]
    G = gidx[S]          # gefaltete Knoten (T,4)
    O = goff[S]          # Bildversaetze (T,4,3)
    # Dreiecks-Umkreismittelpunkte: F[:, k] = Flaeche gegenueber Ecke k
    F = np.empty((T, 4, 3))
    for k in range(4):
        o = [j for j in range(4) if j != k]
        F[:, k] = umkreis_dreieck(X[:, o[0]], X[:, o[1]], X[:, o[2]])
    keys, Ast, dvec_l, sv_l = [], [], [], []
    for (a, b, c, d) in KANTEN_LOKAL:
        pa, pb, pc, pd = X[:, a], X[:, b], X[:, c], X[:, d]
        e = pb - pa
        s = np.sign(np.einsum("ij,ij->i", e, np.cross(pc - pa, pd - pa)))
        m = 0.5 * (pa + pb)
        fc, fd = F[:, d], F[:, c]          # Dreieck (a,b,c) liegt gegenueber d
        vec = 0.5 * (np.cross(fc - m, C - m) + np.cross(C - m, fd - m)) * s[:, None]
        el = np.linalg.norm(e, axis=1)
        Ast.append(np.einsum("ij,ij->i", vec, e) / el)
        gi, gj = G[:, a], G[:, b]
        lo = np.minimum(gi, gj)
        hi = np.maximum(gi, gj)
        keys.append(lo * N + hi)
        richt = np.where(gi < gj, 1.0, -1.0)
        dvec_l.append(e * richt[:, None])
        sv_l.append((O[:, b] - O[:, a]) * richt[:, None].astype(np.int64))
    keys = np.concatenate(keys)
    Ast = np.concatenate(Ast)
    dvec = np.concatenate(dvec_l)
    sv = np.concatenate(sv_l)
    uniq, first, inv = np.unique(keys, return_index=True, return_inverse=True)
    E = uniq.size
    A = np.bincount(inv, Ast, E)
    ei, ej = uniq // N, uniq % N
    drep = dvec[first]
    srep = sv[first]
    kons_d = float(np.max(np.abs(dvec - drep[inv])))
    kons_s = int(np.max(np.abs(sv - srep[inv])))
    dl = np.linalg.norm(drep, axis=1)
    n = drep / dl[:, None]
    # Dreiecke (Topologie)
    tris = []
    for k in range(4):
        o = [j for j in range(4) if j != k]
        tris.append(np.sort(G[:, o], axis=1))
    tris = np.concatenate(tris)
    tkey = (tris[:, 0] * N + tris[:, 1]) * N + tris[:, 2]
    _, tcnt = np.unique(tkey, return_counts=True)
    V = np.bincount(ei, A * dl, N) / 6.0 + np.bincount(ej, A * dl, N) / 6.0
    netz = {"art": "zufall", "N": N, "L": L, "pos": pos, "ei": ei, "ej": ej, "s": srep, "A": A, "d": dl, "n": n,
            "V": V}
    pr = geometrie_pruefung(netz)
    pr.update({"T": T, "F": int(tcnt.size), "E": int(E), "euler": int(N - E + tcnt.size - T),
               "dreiecke_genau_zwei": bool(np.all(tcnt == 2)), "tetra_volumen_summe_rel": float(
                   abs(np.sum(det) / 6.0 / L ** 3 - 1.0)), "tetra_det_min": float(np.min(det)),
               "umkugel_ausserhalb_saum": box_verletzt, "saum": saum, "punkte_erweitert": int(P.shape[0]),
               "kante_bild_konsistenz_d": kons_d, "kante_bild_konsistenz_s": kons_s,
               "knoten_benutzt": int(np.unique(G).size), "sek": time.time() - t0})
    netz["pruefung"] = pr
    return netz


def gitternetz(L):
    x, y, z = np.meshgrid(np.arange(L), np.arange(L), np.arange(L), indexing="ij")
    x, y, z = x.ravel(), y.ravel(), z.ravel()
    pos = np.stack([x, y, z], axis=1).astype(float)
    N = L ** 3
    ei, ej, sl, nl = [], [], [], []
    for a in range(3):
        e = np.zeros(3, dtype=np.int64)
        e[a] = 1
        q = np.stack([x, y, z], axis=1) + e
        s = q // L
        q = q % L
        ei.append(np.arange(N))
        ej.append((q[:, 0] * L + q[:, 1]) * L + q[:, 2])
        sl.append(s)
        nl.append(np.repeat(e[None, :].astype(float), N, axis=0))
    ei, ej, s, n = np.concatenate(ei), np.concatenate(ej), np.concatenate(sl), np.concatenate(nl)
    netz = {"art": "gitter", "N": N, "L": float(L), "pos": pos, "ei": ei, "ej": ej, "s": s, "A": np.ones(ei.size),
            "d": np.ones(ei.size), "n": n, "V": np.ones(N)}
    netz["pruefung"] = geometrie_pruefung(netz)
    return netz


def geometrie_pruefung(netz):
    N, ei, ej, A, d, n, V = netz["N"], netz["ei"], netz["ej"], netz["A"], netz["d"], netz["n"], netz["V"]
    clos = np.zeros((N, 3))
    for c in range(3):
        clos[:, c] = np.bincount(ei, A * n[:, c], N) - np.bincount(ej, A * n[:, c], N)
    asum = np.bincount(ei, A, N) + np.bincount(ej, A, N)
    # Geschwindigkeitstensor M_x/V_x = sum_j A d/2 n n^T / V_x
    Mt = np.zeros((N, 3, 3))
    for a in range(3):
        for b in range(3):
            w = A * d * 0.5 * n[:, a] * n[:, b]
            Mt[:, a, b] = (np.bincount(ei, w, N) + np.bincount(ej, w, N)) / V
    spur = np.trace(Mt, axis1=1, axis2=2)
    ev = np.linalg.eigvalsh(Mt)
    Mmit = Mt.mean(axis=0)
    Mvol = (Mt * V[:, None, None]).sum(axis=0) / V.sum()
    grad = np.bincount(ei, np.ones_like(A), N) + np.bincount(ej, np.ones_like(A), N)
    return {"N": N, "L": netz["L"], "kanten": int(ei.size), "grad_mittel": float(grad.mean()),
            "grad_min": int(grad.min()), "grad_max": int(grad.max()),
            "A_min": float(A.min()), "A_max": float(A.max()), "A_mittel": float(A.mean()),
            "A_nicht_positiv": int(np.sum(A <= 0)), "d_min": float(d.min()), "d_max": float(d.max()),
            "d_max_durch_L": float(d.max() / netz["L"]),
            "abschluss_max_rel": float(np.max(np.linalg.norm(clos, axis=1) / asum)),
            "volumen_summe_rel": float(abs(V.sum() / netz["L"] ** 3 - 1.0)), "V_min": float(V.min()),
            "V_max": float(V.max()), "spur_M_durch_V_abw_max": float(np.max(np.abs(spur - 3.0))),
            "M_durch_V_mittel": Mmit, "M_durch_V_volumengewichtet": Mvol,
            "M_eigen_streuung_rms": float(np.sqrt(np.mean((ev - 1.0) ** 2))),
            "M_eigen_min": float(ev.min()), "M_eigen_max": float(ev.max())}


# ---------------------------------------------------------------------- Operator
def matrix(netz, theta=None):
    N, ei, ej, n = netz["N"], netz["ei"], netz["ej"], netz["n"]
    w = 0.5 * netz["A"] / np.sqrt(netz["V"][ei] * netz["V"][ej])
    c = 1j * w
    if theta is not None:
        c = c * np.exp(1j * (netz["s"] @ np.asarray(theta, dtype=float)))
    b00, b01, b10, b11 = c * n[:, 2], c * (n[:, 0] - 1j * n[:, 1]), c * (n[:, 0] + 1j * n[:, 1]), -c * n[:, 2]
    r = np.concatenate([2 * ei, 2 * ei, 2 * ei + 1, 2 * ei + 1, 2 * ej, 2 * ej + 1, 2 * ej, 2 * ej + 1])
    q = np.concatenate([2 * ej, 2 * ej + 1, 2 * ej, 2 * ej + 1, 2 * ei, 2 * ei, 2 * ei + 1, 2 * ei + 1])
    v = np.concatenate([b00, b01, b10, b11, np.conj(b00), np.conj(b01), np.conj(b10), np.conj(b11)])
    return sp.csr_matrix((v, (r, q)), shape=(2 * N, 2 * N))


def nullmoden(netz):
    sq = np.sqrt(netz["V"] / netz["V"].sum())
    Z = np.zeros((2 * netz["N"], 2), dtype=complex)
    Z[0::2, 0] = sq
    Z[1::2, 1] = sq
    return Z


def operator_pruefung(netz, H):
    D = H - H.conj().T
    herm = float(np.max(np.abs(D.data))) if D.nnz else 0.0
    Z = nullmoden(netz)
    res = float(np.max(np.linalg.norm(H @ Z, axis=0)))
    return {"hermitesch_max": herm, "nullmoden_residuum": res, "nnz": int(H.nnz)}


def schranke(H):
    t0 = time.time()
    gersh = float(np.max(np.asarray(abs(H).sum(axis=1)).ravel()))
    try:
        lr = spla.eigs(H, k=1, which="LR", tol=1e-6, return_eigenvectors=False, maxiter=5000)
        sr = spla.eigs(H, k=1, which="SR", tol=1e-6, return_eigenvectors=False, maxiter=5000)
        lan = float(max(abs(lr[0].real), abs(sr[0].real)))
        lan_ok = True
    except Exception as ex:  # pragma: no cover
        lan, lan_ok = gersh, False
    a = min(1.05 * lan + 0.02, gersh * 1.0001)
    return {"gershgorin": gersh, "lanczos_max_betrag": lan, "lanczos_ok": lan_ok, "a": a, "sek": time.time() - t0}


# ---------------------------------------------------------------------- KPM
def jackson(M):
    n = np.arange(M)
    q = math.pi / (M + 1)
    return ((M - n + 1) * np.cos(q * n) + np.sin(q * n) / math.tan(q)) / (M + 1)


def kpm_block(Hs, V0, M):
    """mu[n, b] = <v_b|T_n(Hs)|v_b> / <v_b|v_b> fuer einen Block von Vektoren."""
    nb = V0.shape[1]
    mu = np.empty((M, nb))
    nrm = np.einsum("ij,ij->j", V0.conj(), V0).real
    v0 = V0.copy()
    v1 = Hs @ v0
    mu[0] = 1.0
    mu[1] = np.einsum("ij,ij->j", v0.conj(), v1).real / nrm
    for k in range(1, M // 2):
        v2 = 2.0 * (Hs @ v1) - v0
        mu[2 * k] = 2.0 * np.einsum("ij,ij->j", v1.conj(), v1).real / nrm - mu[0]
        mu[2 * k + 1] = 2.0 * np.einsum("ij,ij->j", v2.conj(), v1).real / nrm - mu[1]
        v0, v1 = v1, v2
    return mu


def kpm_anteil(mu, g, a, eps):
    """Anteil der Eigenwerte mit |E| < eps (je Spalte von mu), Jackson-gedaempft, exakt integriert."""
    M = mu.shape[0]
    eps = np.atleast_1d(np.asarray(eps, dtype=float))
    th1 = np.arccos(np.clip(-eps / a, -1, 1))
    th2 = np.arccos(np.clip(eps / a, -1, 1))
    nn = np.arange(1, M)
    S = (np.sin(np.outer(nn, th1)) - np.sin(np.outer(nn, th2))) / nn[:, None]     # (M-1, ne)
    gm = g[:, None] * mu                                                            # (M, nb)
    return ((th1 - th2)[:, None] * gm[0][None, :] + 2.0 * S.T @ gm[1:]) / math.pi   # (ne, nb)


def kpm_dichte(mu, g, a, E):
    x = np.clip(np.asarray(E) / a, -0.999999, 0.999999)
    th = np.arccos(x)
    M = mu.shape[0]
    Tn = np.cos(np.outer(np.arange(M), th))
    gm = g[:, None] * mu
    r = (gm[0][None, :] + 2.0 * Tn[1:].T @ gm[1:]) / (math.pi * np.sqrt(1 - x * x))[:, None]
    return r / a    # Dichte je Eigenwert-Anteil pro Energie (normiert auf 1)


def kpm_lauf(netz, M, T, B, rng, protokoll, exakt=None):
    """Verdrillungsgemittelte KPM: T zufaellige theta, je B Zufallsphasen-Vektoren."""
    t0 = time.time()
    N = netz["N"]
    dim = 2 * N
    H0 = matrix(netz, None)
    sch = schranke(H0)
    a = sch["a"]
    g = jackson(M)
    mus, thetas = [], []
    for t in range(T):
        th = rng.uniform(0, 2 * math.pi, size=3)
        Hs = matrix(netz, th) * (1.0 / a)
        V0 = np.exp(2j * math.pi * rng.random((dim, B)))
        mus.append(kpm_block(Hs, V0, M))
        thetas.append(th)
    mu = np.concatenate(mus, axis=1)     # (M, T*B)
    anteil = kpm_anteil(mu, g, a, EPS_FEIN)                 # (ne, R)
    n_je_knoten = 2.0 * anteil                              # Zustaende je Knoten mit |E| < eps
    dichte = 2.0 * kpm_dichte(mu, g, a, E_RASTER)          # Zustaende je Knoten und Energie
    R = mu.shape[1]
    out = {"M": M, "T": T, "B": B, "R": R, "schranke": sch, "a": a, "aufloesung_ca": math.pi * a / M,
           "mu_max_betrag": float(np.max(np.abs(mu))), "thetas": thetas,
           "eps": EPS_FEIN, "n_mittel": n_je_knoten.mean(axis=1),
           "n_se": n_je_knoten.std(axis=1, ddof=1) / math.sqrt(R) if R > 1 else np.zeros(len(EPS_FEIN)),
           "E": E_RASTER, "rho_mittel": dichte.mean(axis=1),
           "rho_se": dichte.std(axis=1, ddof=1) / math.sqrt(R) if R > 1 else np.zeros(len(E_RASTER)),
           "n_proben": n_je_knoten, "sek": time.time() - t0}
    if exakt is not None:
        ex = np.array([exakt(th, EPS_FEIN) for th in thetas])                 # (T, ne) je Knoten
        kp = n_je_knoten.reshape(len(EPS_FEIN), T, B).mean(axis=2).T         # (T, ne)
        out["exakt_je_theta"] = ex
        out["kpm_je_theta"] = kp
        out["kpm_minus_exakt_max"] = float(np.max(np.abs(kp - ex)))
    protokoll(f"KPM N={N}: M={M}, R={R}, a={a:.4f} (Gershgorin {sch['gershgorin']:.3f}), |mu|max "
              f"{out['mu_max_betrag']:.6f}, {out['sek']:.1f} s")
    return out


def kpm_intervall(mu, g, a, E1, E2):
    """Anteil des Spektralgewichts in [E1, E2] je Spalte von mu (Jackson, exakt integriert)."""
    M = mu.shape[0]
    th1 = math.acos(max(-1.0, min(1.0, E1 / a)))
    th2 = math.acos(max(-1.0, min(1.0, E2 / a)))
    nn = np.arange(1, M)
    S = (np.sin(nn * th1) - np.sin(nn * th2)) / nn
    gm = g[:, None] * mu
    return ((th1 - th2) * gm[0] + 2.0 * S @ gm[1:]) / math.pi


def spektral_lauf(netz, M, kmax, protokoll, theta=THETA_EIG, m_liste=None, fenster=E_FENSTER):
    """Spektralfunktion der Ebenen Wellen chi_{k,h} = sqrt(V/sum V) e^{ik.x} u_h(k^) (h = Eigenwert von sigma.k^),
    exakt (ein Vektor je Welle, keine Stichprobe), KPM mit M Momenten bei fester Verdrillung theta."""
    t0 = time.time()
    N = netz["N"]
    theta = np.asarray(theta, dtype=float)
    H = matrix(netz, theta)
    sch = schranke(H)
    a = sch["a"]
    if m_liste is None:
        m, kv, kb = wellen_basis(netz, theta, kmax)
        nicht0 = ~np.all(m == 0, axis=1)
        m, kv, kb = m[nicht0], kv[nicht0], kb[nicht0]
    else:
        m = np.asarray(m_liste, dtype=np.int64)
        kv = (2 * math.pi * m + theta[None, :]) / netz["L"]
        kb = np.linalg.norm(kv, axis=1)
    sq = np.sqrt(netz["V"] / netz["V"].sum())
    K = m.shape[0]
    Vb = np.zeros((2 * N, 2 * K), dtype=complex)
    hel = []
    for j in range(K):
        kh = kv[j] / kb[j]
        S = kh[0] * np.array([[0, 1], [1, 0]]) + kh[1] * np.array([[0, -1j], [1j, 0]]) + kh[2] * np.array(
            [[1, 0], [0, -1]])
        ew, U = np.linalg.eigh(S)          # ew = (-1, +1)
        ph = sq * np.exp(1j * (netz["pos"] @ kv[j]))
        for q in range(2):
            Vb[0::2, 2 * j + q] = ph * U[0, q]
            Vb[1::2, 2 * j + q] = ph * U[1, q]
            hel.append(int(round(ew[q])))
    mu = kpm_block(H * (1.0 / a), Vb, M)
    g = jackson(M)
    hel = np.array(hel)
    Wp = kpm_intervall(mu, g, a, 0.0, fenster)
    Wn = kpm_intervall(mu, g, a, -fenster, 0.0)
    Gp = kpm_intervall(mu, g, a, 0.0, a)
    Gn = kpm_intervall(mu, g, a, -a, 0.0)
    # richtige Helizitaet: E > 0 <-> h = -1 (H ~ -sigma.k)
    richtig_W = np.where(hel < 0, Wp, Wn)
    falsch_W = np.where(hel < 0, Wn, Wp)
    richtig_G = np.where(hel < 0, Gp, Gn)
    dichte = kpm_dichte(mu, g, a, E_RASTER)          # (nE, 2K) je Welle normiert auf 1
    # Spitzenlage je Welle im richtigen Vorzeichen
    Ep = np.array(E_RASTER)
    spitze = []
    for c in range(2 * K):
        msk = (Ep > 0) if hel[c] < 0 else (Ep < 0)
        i = np.argmax(np.where(msk, dichte[:, c], -1.0))
        spitze.append(abs(Ep[i]))
    spitze = np.array(spitze)
    kk = np.repeat(kb, 2)
    # Erwartungswerte <H> und <H^2> exakt
    HV = H @ Vb
    e1 = np.einsum("ij,ij->j", Vb.conj(), HV).real
    e2 = np.einsum("ij,ij->j", HV.conj(), HV).real
    out = {"M": M, "a": a, "schranke": sch, "theta": theta, "m": np.repeat(m, 2, axis=0), "k": kk, "h": hel,
           "W_richtig": richtig_W, "W_falsch": falsch_W, "G_richtig": richtig_G,
           "F_fenster": float(richtig_W.sum() / (richtig_W.sum() + falsch_W.sum())),
           "W_fenster_summe": float(richtig_W.sum() + falsch_W.sum()), "zahl_wellen": int(2 * K),
           "spitze_E": spitze, "v_spitze": spitze / kk, "E1": e1, "E2": e2,
           "mu_max_betrag": float(np.max(np.abs(mu))), "sek": time.time() - t0}
    # mittlere Spektralfunktion je Schale (|m|^2) und Helizitaet fuer Bilder
    schalen = {}
    m2 = (np.repeat(m, 2, axis=0) ** 2).sum(axis=1)
    for s2 in np.unique(m2):
        for hh in (-1, 1):
            sel = (m2 == s2) & (hel == hh)
            if np.any(sel):
                schalen[f"{int(s2)}_{hh}"] = {"k_mittel": float(kk[sel].mean()), "anzahl": int(sel.sum()),
                                              "A": dichte[:, sel].mean(axis=1)}
    out["schalen"] = schalen
    protokoll(f"Spektral N={N}: {2 * K} Wellen, M={M}, F_fenster {out['F_fenster']:.4f}, W_fenster "
              f"{out['W_fenster_summe']:.3f}, G_richtig mittel {richtig_G.mean():.4f}, v_spitze median "
              f"{np.median(out['v_spitze']):.3f}, {out['sek']:.1f} s")
    return out


# ---------------------------------------------------------------------- Eigenpaare nahe null
def wellen_basis(netz, theta, kmax=K_MAX):
    L = netz["L"]
    mm = int(math.ceil(kmax * L / (2 * math.pi))) + 1
    r = np.arange(-mm, mm + 1)
    m = np.stack(np.meshgrid(r, r, r, indexing="ij"), axis=-1).reshape(-1, 3)
    k = (2 * math.pi * m + theta[None, :]) / L
    kb = np.linalg.norm(k, axis=1)
    halte = (kb <= kmax) | np.all(m == 0, axis=1)
    return m[halte], k[halte], kb[halte]


def eigen_lauf(netz, kzahl, protokoll, theta=THETA_EIG, inertia=True):
    t0 = time.time()
    N = netz["N"]
    dim = 2 * N
    H = matrix(netz, theta).tocsc()
    out = {"theta": theta, "k": kzahl}
    lu = spla.splu(H, permc_spec="MMD_AT_PLUS_A")
    out["lu_nnz"] = int(lu.L.nnz + lu.U.nnz)
    out["sek_lu"] = time.time() - t0
    op = spla.LinearOperator(H.shape, matvec=lu.solve, dtype=complex)
    t1 = time.time()
    vals, vecs = spla.eigs(H.tocsr(), k=kzahl, sigma=0.0, which="LM", OPinv=op, tol=1e-10,
                           ncv=min(dim - 2, 2 * kzahl + 40), maxiter=20000)
    out["sek_arpack"] = time.time() - t1
    out["arpack_im_max"] = float(np.max(np.abs(vals.imag)))
    # Rayleigh-Ritz im gefundenen Unterraum (orthonormal, hermitesch)
    Q, _ = np.linalg.qr(vecs)
    Hq = Q.conj().T @ (H @ Q)
    out["ritz_herm"] = float(np.max(np.abs(Hq - Hq.conj().T)))
    w, U = np.linalg.eigh(0.5 * (Hq + Hq.conj().T))
    Psi = Q @ U
    res = np.linalg.norm(H @ Psi - Psi * w[None, :], axis=0)
    out["residuum_max"] = float(res.max())
    out["arpack_gegen_ritz_max"] = float(np.max(np.abs(np.sort(vals.real) - np.sort(w))))
    o = np.argsort(np.abs(w))
    w, Psi, res = w[o], Psi[:, o], res[o]
    # Ebene-Wellen-Gehalt und Helizitaet
    m, kv, kb = wellen_basis(netz, np.asarray(theta, dtype=float))
    sq = np.sqrt(netz["V"] / netz["V"].sum())
    Ph = sq[None, :] * np.exp(-1j * (kv @ netz["pos"].T))    # (K, N)
    c0 = Ph @ Psi[0::2]
    c1 = Ph @ Psi[1::2]
    khat = kv / kb[:, None]
    w2 = np.abs(c0) ** 2 + np.abs(c1) ** 2                    # (K, n)
    h = khat[:, 2:3] * (np.abs(c0) ** 2 - np.abs(c1) ** 2) + 2 * np.real(
        np.conj(c0) * c1 * (khat[:, 0:1] - 1j * khat[:, 1:2]))
    null = np.all(m == 0, axis=1)
    sgn = np.sign(w)
    richtig = 0.5 * (w2 - sgn[None, :] * h)                   # Gewicht der richtigen Helizitaet
    gehalt = w2[~null].sum(axis=0)
    gehalt0 = w2[null].sum(axis=0)
    richtig_sum = richtig[~null].sum(axis=0)
    krms = np.sqrt((w2[~null] * kb[~null, None] ** 2).sum(axis=0) / np.maximum(gehalt, 1e-300))
    dom = np.argmax(np.where(null[:, None], -1.0, w2), axis=0)
    out.update({"E": w, "residuum": res, "gehalt": gehalt, "gehalt_m0": gehalt0, "richtig": richtig_sum,
                "k_rms": krms, "m_dominant": m[dom], "k_dominant": kb[dom],
                "anteil_dominant": w2[dom, np.arange(w.size)] / np.maximum(gehalt, 1e-300),
                "basis_K": int(m.shape[0]), "E_max_gefunden": float(np.max(np.abs(w)))})
    if inertia:
        ti = time.time()
        zl = {}
        for sh in (-E_FENSTER, E_FENSTER):
            A = (H - sh * sp.identity(dim, dtype=complex, format="csc")).tocsc()
            try:
                lus = spla.splu(A, permc_spec="MMD_AT_PLUS_A", diag_pivot_thresh=0.0,
                                options={"SymmetricMode": True})
                d = lus.U.diagonal()
                zl[str(sh)] = {"neg": int(np.sum(d.real < 0)),
                               "perm_gleich": bool(np.array_equal(lus.perm_r, lus.perm_c)),
                               "im_rel_max": float(np.max(np.abs(d.imag) / np.abs(d)))}
            except Exception as ex:
                zl[str(sh)] = {"fehler": str(ex)}
        out["inertia"] = zl
        try:
            out["inertia_zahl_fenster"] = zl[str(E_FENSTER)]["neg"] - zl[str(-E_FENSTER)]["neg"]
        except Exception:
            out["inertia_zahl_fenster"] = None
        out["sek_inertia"] = time.time() - ti
    out["zahl_fenster_arpack"] = int(np.sum(np.abs(w) < E_FENSTER))
    out["sek"] = time.time() - t0
    protokoll(f"Eigen N={N}: {kzahl} Paare, |E|max {out['E_max_gefunden']:.4f}, Fenster {out['zahl_fenster_arpack']} "
              f"(Inertia {out.get('inertia_zahl_fenster')}), Residuum {out['residuum_max']:.1e}, LU nnz "
              f"{out['lu_nnz']}, {out['sek']:.1f} s")
    return out


# ---------------------------------------------------------------------- kubisch exakt
def kubisch_eigen(L, theta):
    r = np.arange(L)
    m = np.stack(np.meshgrid(r, r, r, indexing="ij"), axis=-1).reshape(-1, 3)
    k = (2 * math.pi * m + np.asarray(theta)[None, :]) / L
    e = np.sqrt((np.sin(k) ** 2).sum(axis=1))
    return np.sort(np.concatenate([e, -e]))


def kubisch_zahl(L):
    r = np.arange(L)
    m = np.stack(np.meshgrid(r, r, r, indexing="ij"), axis=-1).reshape(-1, 3)

    def f(theta, eps):
        k = (2 * math.pi * m + np.asarray(theta)[None, :]) / L
        e = np.sort(np.sqrt((np.sin(k) ** 2).sum(axis=1)))
        return 2.0 * np.searchsorted(e, np.atleast_1d(eps), side="left") / L ** 3
    return f


def dichte_dicht(netz, theta):
    H = matrix(netz, theta).toarray()
    return np.linalg.eigvalsh(H)


# ---------------------------------------------------------------------- Modi
def modus_kontrolle(protokoll):
    out = {}
    rng = np.random.default_rng([SAAT_BASIS, 1])
    # K1 kubisch L = 6 dicht gegen analytisch
    k1 = []
    for L in (6, 7):
        nz = gitternetz(L)
        for th in (np.zeros(3), rng.uniform(0, 2 * math.pi, 3)):
            ev = dichte_dicht(nz, th)
            ex = kubisch_eigen(L, th)
            k1.append({"L": L, "theta": th, "max_abw": float(np.max(np.abs(ev - ex))),
                       "null_1e-9": int(np.sum(np.abs(ev) < 1e-9)), "op": operator_pruefung(nz, matrix(nz, th))})
            protokoll(f"K1 kubisch L={L} theta={np.round(th, 3)}: max |dicht - analytisch| {k1[-1]['max_abw']:.2e}, "
                      f"Nullmoden {k1[-1]['null_1e-9']}")
    out["K1_kubisch_dicht"] = k1
    # K2 Zufallsnetz N = 1000, Saat 999: Geometrie, dicht (Kramers, Nullmoden), Eigenpaare und KPM gegen dicht
    nz = zufallsnetz(1000, 999)
    pr = nz["pruefung"]
    protokoll(f"K2 Netz N=1000: Euler {pr['euler']}, Dreiecke genau zwei {pr['dreiecke_genau_zwei']}, Umkugel "
              f"ausserhalb {pr['umkugel_ausserhalb_saum']}, Abschluss {pr['abschluss_max_rel']:.1e}, Volumen "
              f"{pr['volumen_summe_rel']:.1e}, Tetra-Volumen {pr['tetra_volumen_summe_rel']:.1e}")
    H0 = matrix(nz, None)
    ev0 = np.linalg.eigvalsh(H0.toarray())
    kr = float(np.max(np.abs(ev0[0::2] - ev0[1::2])))
    k2 = {"pruefung": pr, "op": operator_pruefung(nz, H0), "kramers_max_abw": kr,
          "null_1e-9": int(np.sum(np.abs(ev0) < 1e-9)), "spektrum_min": float(ev0[0]), "spektrum_max": float(ev0[-1]),
          "asymmetrie_spur_H3": float(np.sum(ev0 ** 3) / ev0.size), "spur_H": float(np.sum(ev0) / ev0.size)}
    protokoll(f"K2 dicht: Kramers {kr:.1e}, Nullmoden {k2['null_1e-9']}, Spektrum [{ev0[0]:.3f}, {ev0[-1]:.3f}], "
              f"<E^3> {k2['asymmetrie_spur_H3']:.4f}")
    evt = np.linalg.eigvalsh(matrix(nz, THETA_EIG).toarray())
    eg = eigen_lauf(nz, 60, protokoll, inertia=True)
    ref = evt[np.argsort(np.abs(evt))][:60]
    k2["eigen_gegen_dicht_max"] = float(np.max(np.abs(np.sort(eg["E"]) - np.sort(ref))))
    k2["eigen_inertia_gegen_dicht"] = [eg.get("inertia_zahl_fenster"), int(np.sum(np.abs(evt) < E_FENSTER))]
    k2["eigen"] = {x: eg[x] for x in ("residuum_max", "arpack_im_max", "ritz_herm", "lu_nnz", "inertia",
                                       "zahl_fenster_arpack", "sek")}
    protokoll(f"K2 Eigenpaare gegen dicht: {k2['eigen_gegen_dicht_max']:.1e}; Fenster Inertia/dicht "
              f"{k2['eigen_inertia_gegen_dicht']}")
    # KPM gegen dicht (Zahl je Verdrillung)
    cache = {}

    def exakt(th, e):
        key = tuple(np.round(th, 12))
        if key not in cache:
            cache[key] = np.sort(np.abs(np.linalg.eigvalsh(matrix(nz, th).toarray())))
        return np.searchsorted(cache[key], np.atleast_1d(e), side="left") / nz["N"]
    kp = kpm_lauf(nz, 512, 4, 2, np.random.default_rng([SAAT_BASIS, 2]), protokoll, exakt=exakt)
    k2["kpm"] = {x: kp[x] for x in ("a", "schranke", "kpm_minus_exakt_max", "mu_max_betrag", "sek")}
    sel = [i for i, e in enumerate(EPS_FEIN) if e in (0.2, 0.3, 0.4, 0.6, 0.8, 1.0)]
    k2["kpm_auszug"] = {"eps": EPS_FEIN[sel], "kpm": np.asarray(kp["kpm_je_theta"])[:, sel],
                        "exakt": np.asarray(kp["exakt_je_theta"])[:, sel]}
    protokoll(f"K2 KPM gegen dicht: max |n_kpm - n_exakt| je Knoten {kp['kpm_minus_exakt_max']:.2e}")
    out["K2_netz_1000"] = k2
    # K3 kubisch L = 12: KPM gegen analytisch je Verdrillung
    ng = gitternetz(12)
    kp = kpm_lauf(ng, 1024, 4, 2, np.random.default_rng([SAAT_BASIS, 3]), protokoll, exakt=kubisch_zahl(12))
    out["K3_kubisch_kpm"] = {x: kp[x] for x in ("a", "schranke", "kpm_minus_exakt_max", "mu_max_betrag", "sek")}
    protokoll(f"K3 kubisch L=12 KPM gegen analytisch: {kp['kpm_minus_exakt_max']:.2e}")
    out["K4_dicht_2000"] = eigen_dicht_probe(zufallsnetz(2000, 998), protokoll)
    return out


def eigen_dicht_probe(nz, protokoll, fenster=0.6, kmax=K_MAX, M=2048):
    """Alle Eigenpaare dicht (THETA_EIG): Ebene-Wellen-Gehalt, Helizitaet, IPR je Zustand; F im Fenster aus
    Eigenvektoren gegen F aus den KPM-Spektralfunktionen (gleiche Wellen, gleiches Fenster)."""
    t0 = time.time()
    N = nz["N"]
    H = matrix(nz, THETA_EIG)
    w, Psi = np.linalg.eigh(H.toarray())
    m, kv, kb = wellen_basis(nz, THETA_EIG, kmax)
    nicht0 = ~np.all(m == 0, axis=1)
    m, kv, kb = m[nicht0], kv[nicht0], kb[nicht0]
    sq = np.sqrt(nz["V"] / nz["V"].sum())
    Ph = sq[None, :] * np.exp(-1j * (kv @ nz["pos"].T))
    c0, c1 = Ph @ Psi[0::2], Ph @ Psi[1::2]
    khat = kv / kb[:, None]
    w2 = np.abs(c0) ** 2 + np.abs(c1) ** 2
    h = khat[:, 2:3] * (np.abs(c0) ** 2 - np.abs(c1) ** 2) + 2 * np.real(
        np.conj(c0) * c1 * (khat[:, 0:1] - 1j * khat[:, 1:2]))
    richtig = 0.5 * (w2 - np.sign(w)[None, :] * h)
    gehalt = w2.sum(axis=0)
    rsum = richtig.sum(axis=0)
    W = np.abs(w) <= fenster
    F_eig = float(rsum[W].sum() / gehalt[W].sum())
    ipr = N * ((np.abs(Psi[0::2]) ** 2 + np.abs(Psi[1::2]) ** 2) ** 2).sum(axis=0)
    sp_ = spektral_lauf(nz, M, kmax, protokoll, fenster=fenster)
    kanten = np.round(np.arange(-3.0, 3.0001, 0.1), 3)
    idx = np.digitize(w, kanten) - 1
    bins = []
    for b in range(len(kanten) - 1):
        s = idx == b
        if np.any(s):
            bins.append({"E": float(0.5 * (kanten[b] + kanten[b + 1])), "anzahl": int(s.sum()),
                         "ipr_median": float(np.median(ipr[s])), "gehalt_summe": float(gehalt[s].sum()),
                         "gehalt_max": float(gehalt[s].max())})
    tief = np.argsort(np.abs(w))[:20]
    out = {"N": N, "fenster": fenster, "kmax": kmax, "F_eigen": F_eig, "F_kpm": sp_["F_fenster"],
           "F_abw": abs(F_eig - sp_["F_fenster"]), "gehalt_fenster_summe": float(gehalt[W].sum()),
           "W_kpm_summe": sp_["W_fenster_summe"], "zahl_fenster": int(W.sum()), "bins": bins,
           "tiefste": {"E": w[tief], "gehalt": gehalt[tief], "ipr": ipr[tief]},
           "ipr_median_alle": float(np.median(ipr)), "zahl_wellen": int(2 * m.shape[0]),
           "spektrum": [float(w[0]), float(w[-1])], "sek": time.time() - t0}
    protokoll(f"K4 dicht N={N}: F aus Eigenvektoren {F_eig:.4f} gegen KPM {sp_['F_fenster']:.4f} (Fenster "
              f"{fenster}), Gehalt im Fenster {out['gehalt_fenster_summe']:.3f} gegen KPM {sp_['W_fenster_summe']:.3f}, "
              f"IPR median alle {out['ipr_median_alle']:.2f}, tiefste 20: IPR median {np.median(ipr[tief]):.2f}, Gehalt "
              f"max {gehalt[tief].max():.2e}, {out['sek']:.1f} s")
    return out


def modus_gitter(L, kpm, kzahl, protokoll, spek=None):
    nz = gitternetz(L)
    H0 = matrix(nz, None)
    out = {"L": L, "N": L ** 3, "pruefung": nz["pruefung"], "op": operator_pruefung(nz, H0)}
    if kzahl:
        out["eigen"] = eigen_lauf(nz, kzahl, protokoll)
    if kpm:
        M, T, B = kpm
        kp = kpm_lauf(nz, M, T, B, np.random.default_rng([SAAT_BASIS, L, 5]), protokoll, exakt=kubisch_zahl(L))
        out["kpm"] = kp
    if spek:
        out["spektral"] = spektral_lauf(nz, int(spek[0]), float(spek[1]), protokoll,
                                        m_liste=M_WAHL if L ** 3 >= 50000 else None)
    # analytische Verdrillungsmittel (200 theta) als Referenz
    rng = np.random.default_rng([SAAT_BASIS, L, 6])
    f = kubisch_zahl(L)
    ths = rng.uniform(0, 2 * math.pi, size=(200, 3))
    ref = np.array([f(th, EPS_GITTER) for th in ths])
    out["analytisch_mittel_eps"] = EPS_GITTER
    out["analytisch_n_mittel"] = ref.mean(axis=0)
    out["analytisch_n_se"] = ref.std(axis=0, ddof=1) / math.sqrt(ref.shape[0])
    # Nullmoden ohne Verdrillung (analytisch, gerades L: 16)
    ev = kubisch_eigen(L, np.zeros(3))
    out["nullmoden_analytisch_theta0"] = int(np.sum(np.abs(ev) < 1e-12))
    return out


def modus_netz(N, saat0, anzahl, ziel, kzahl, kpm, protokoll, out, spek=None):
    out.update({"N": N, "saaten": []})
    for saat in range(saat0, saat0 + anzahl):
        t0 = time.time()
        nz = zufallsnetz(N, saat)
        pr = nz["pruefung"]
        protokoll(f"N={N} saat={saat}: Netz {pr['sek']:.1f} s, T={pr['T']}, E={pr['E']}, Euler {pr['euler']}, "
                  f"Dreiecke2 {pr['dreiecke_genau_zwei']}, Umkugel {pr['umkugel_ausserhalb_saum']}, Abschluss "
                  f"{pr['abschluss_max_rel']:.1e}, Vol {pr['volumen_summe_rel']:.1e}, A<=0 {pr['A_nicht_positiv']}, "
                  f"Grad {pr['grad_mittel']:.3f}, M-Streuung {pr['M_eigen_streuung_rms']:.3f}")
        H0 = matrix(nz, None)
        eintrag = {"saat": saat, "pruefung": pr, "op": operator_pruefung(nz, H0)}
        if kzahl:
            eintrag["eigen"] = eigen_lauf(nz, kzahl, protokoll)
        if kpm:
            M, T, B = kpm
            eintrag["kpm"] = kpm_lauf(nz, M, T, B, np.random.default_rng([SAAT_BASIS, N, saat, 7]), protokoll)
            with open(ziel + ".tmp", "w") as f:
                json.dump(js({**out, "teil": eintrag}), f)
            os.replace(ziel + ".tmp", ziel)
        if spek:
            Ms, kms = int(spek[0]), float(spek[1])
            wahl = M_WAHL if N >= 50000 else None
            eintrag["spektral"] = spektral_lauf(nz, Ms, kms, protokoll, m_liste=wahl)
        eintrag["sekunden"] = time.time() - t0
        out["saaten"].append(eintrag)
        with open(ziel + ".tmp", "w") as f:
            json.dump(js(out), f)
        os.replace(ziel + ".tmp", ziel)
    return out


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
    kpm = tuple(int(x) for x in opts["kpm"].split(",")) if "kpm" in opts else None
    if modus == "kontrolle":
        ziel = pos[0]
        out.update(modus_kontrolle(protokoll))
    elif modus == "gitter":
        L, ziel = int(pos[0]), pos[1]
        out.update(modus_gitter(L, kpm, int(opts.get("eig", "0")), protokoll,
                                opts["spek"].split(",") if "spek" in opts else None))
    elif modus == "netz":
        N, saat0, anzahl, ziel = int(pos[0]), int(pos[1]), int(pos[2]), pos[3]
        kzahl = int(opts.get("eig", "0"))
        spek = opts["spek"].split(",") if "spek" in opts else None
        modus_netz(N, saat0, anzahl, ziel, kzahl, kpm, protokoll, out, spek)
    else:
        raise SystemExit("unbekannter Modus")
    out["laufzeit_gesamt_s"] = time.time() - t0
    out["protokoll"] = log
    with open(ziel + ".tmp", "w") as f:
        json.dump(js(out), f)
    os.replace(ziel + ".tmp", ziel)
    print("geschrieben", ziel, f"{time.time() - t0:.1f} s", flush=True)


if __name__ == "__main__":
    main()
