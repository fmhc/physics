#!/usr/bin/env python3
"""DANZER-NAEHERUNG-1 (Runde 46, Code-Agent fuer die Leitung claude-primary).

Kubische rationale Naeherungen 1/1, 2/1, 3/2 eines ikosaedrischen Tetraeder-Netzes, Bauweg 3 der Karte:
  Schnitt- und Projektionsmenge aus Z^6 (Ammann-Kramer-Ecken; Fenster = Projektion des 6D-Einheitswuerfels laengs des
  rationalen Schnittraums, fuer tau_n -> tau das rhombische Triakontaeder), kubisch periodisch, dann periodische
  Delaunay-Tetraederzerlegung der Eckenmenge.
Darauf exakte Bloch-Eigenwerte fuer
  S  Skalar: Graph-Laplace, Einheitsgewichte
  M  Maxwell in der Coulomb-Phase: A auf Kanten, Fluss auf Dreiecken, K = C^dag C, Einheitsgewichte
Fit je Richtung mit licht_netz.fit (Bloch-Werkzeug aus LICHT-FINN-NETZ-1, unveraendert importiert), dann harmonische
Zerlegung von a2(n) in l = 0, 2, 4, 6: kubischer Anteil (Koeffizient von S4), T_h-invarianter l = 6-Anteil,
ikosaedrische l = 6-Projektion.

Aufruf (nur ueber kleintest.sh):
  python danzer_naeherung.py rauch <aus.json>
  python danzer_naeherung.py rechnen <p/q> <ops: S | M | S,M> <saaten: 0,1,2,3> <aus.json> [--probe] [--richtungen 40]
  python danzer_naeherung.py auswerten <aus.json> <bild.png> <ein1.json> [<ein2.json> ...]
"""
import itertools
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
from scipy.special import sph_harm_y

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import licht_netz as ln  # noqa: E402  Bloch-Werkzeug LICHT-FINN-NETZ-1 (unveraendert)

TAU = (1.0 + 5.0 ** 0.5) / 2.0
ORDNUNGEN = {"1/1": (1, 1), "2/1": (2, 1), "3/2": (3, 2), "5/3": (5, 3)}
REIHE = ["1/1", "2/1", "3/2"]
ETA = 1e-7              # Fenster-Stoerung: gamma = ETA * xi_Saat (bricht Fenster-Entartungen bei gamma0 = 0)
SIGMA_D = 1e-6          # Zitter der Ecken, nur fuer die Delaunay-Kombinatorik (bricht Kugel-Entartungen)
TOL_ZELLE = 1e-9
FENSTER_HAUPT = (0.03, 0.12, 8, 6)    # k in Einheiten pi/L: von, bis, Punkte, Grad (nur gerade Potenzen)
FENSTER_PROBE = (0.015, 0.06, 8, 4)   # beschreibend, nur Saat 0
RICHTUNGEN_STANDARD = 40              # Halbkugel (a2(-n) = a2(n))
N1_SCHWELLE = 1e-6
N2_DRITTEL = 1.0 / 3.0
OFFS = np.array(list(itertools.product((-1, 0, 1), repeat=3)), dtype=np.int64)


def saat_rng(ordnung, saat):
    p, q = ORDNUNGEN[ordnung]
    return np.random.default_rng([3746, p, q, int(saat)])


# ------------------------------------------------------------------ Projektionen und Naeherung
def projektionen():
    n1 = math.sqrt(1.0 + TAU ** 2)
    a = np.array([[1, TAU, 0], [-1, TAU, 0], [0, 1, TAU], [0, -1, TAU], [TAU, 0, 1], [TAU, 0, -1]], float) / n1
    t = -1.0 / TAU
    n2 = math.sqrt(1.0 + t ** 2)
    b = np.array([[1, t, 0], [-1, t, 0], [0, 1, t], [0, -1, t], [t, 0, 1], [t, 0, -1]], float) / n2
    return a, b


def naeherung(ordnung):
    p, q = ORDNUNGEN[ordnung]
    a, b = projektionen()
    E = np.eye(6, dtype=np.int64)
    t = np.array([p * (E[4] + E[5]) + q * (E[0] - E[1]),
                  p * (E[0] + E[1]) + q * (E[2] - E[3]),
                  p * (E[2] + E[3]) + q * (E[4] - E[5])], dtype=np.int64)
    par = t @ a
    perp = t @ b
    L = float(par[0, 0])
    eps = float(perp[0, 0]) / L
    g = b - eps * a                      # P'(e_i): Projektion laengs des rationalen Schnittraums
    kontrolle = {"par_abw": float(np.max(np.abs(par - L * np.eye(3)))),
                 "perp_abw_isotrop": float(np.max(np.abs(perp - perp[0, 0] * np.eye(3)))),
                 "Pstrich_t_max": float(np.max(np.abs(t @ g))),
                 "orth_AAT": float(np.max(np.abs(a.T @ a - 2 * np.eye(3)))),
                 "orth_BBT": float(np.max(np.abs(b.T @ b - 2 * np.eye(3)))),
                 "orth_ABT": float(np.max(np.abs(a.T @ b)))}
    return {"ordnung": ordnung, "p": p, "q": q, "a": a, "b": b, "t": t, "L": L, "eps": eps, "g": g,
            "kontrolle": kontrolle}


def fenster(g):
    nrm = []
    for i, j in itertools.combinations(range(6), 2):
        n = np.cross(g[i], g[j])
        if np.linalg.norm(n) > 1e-12:
            nrm.append(n / np.linalg.norm(n))
    nrm = np.array(nrm)
    h = 0.5 * np.sum(np.abs(nrm @ g.T), axis=1)
    vol = float(sum(abs(np.linalg.det(g[list(c)])) for c in itertools.combinations(range(6), 3)))
    return nrm, h, vol


def kanon(nh, x):
    X = x @ nh["a"]
    f = np.floor((X + TOL_ZELLE) / nh["L"]).astype(np.int64)
    return x - f @ nh["t"]


def ecken(nh, gamma):
    g = nh["g"]
    nrm, h, vol = fenster(g)

    def marge(x):
        y = x @ g - gamma
        return float(np.min(h - np.abs(nrm @ y)))

    x0 = kanon(nh, np.zeros(6, dtype=np.int64))
    m0 = marge(x0)
    if not m0 > 0:
        raise RuntimeError("Startecke nicht im Fenster")
    E = np.eye(6, dtype=np.int64)
    ang, abg = {tuple(int(v) for v in x0): m0}, {}
    stapel = [x0]
    while stapel:
        x = stapel.pop()
        for i in range(6):
            for s in (1, -1):
                y = kanon(nh, x + s * E[i])
                ky = tuple(int(v) for v in y)
                if ky in ang or ky in abg:
                    continue
                m = marge(y)
                if m > 0:
                    ang[ky] = m
                    stapel.append(y)
                else:
                    abg[ky] = m
    X = np.array(sorted(ang.keys()), dtype=np.int64)
    marg = np.array([ang[tuple(int(v) for v in x)] for x in X])
    r = X @ nh["a"]
    alle = np.concatenate([marg, np.array(list(abg.values()))]) if abg else marg
    return {"x6": X, "r": r, "N": int(len(X)), "N_erwartet": float(nh["L"] ** 3 * vol / 8.0), "vol_fenster": vol,
            "marge_min_innen": float(marg.min()),
            "marge_min_aussen": (float(min(-m for m in abg.values())) if abg else None),
            "fenster_entartet_1e-5": int(np.sum(np.abs(alle) < 1e-5))}


def rhomboeder(nh, ek, gamma):
    a, g = nh["a"], nh["g"]
    keys = set(tuple(int(v) for v in x) for x in ek["x6"])
    P = ek["x6"] @ g - gamma
    E = np.eye(6, dtype=np.int64)
    vol_summe, je_typ, fehlen, anzahl = 0.0, {}, 0, 0
    for I in itertools.combinations(range(6), 3):
        J = [j for j in range(6) if j not in I]
        GJ = g[J].T
        name = "".join(str(i + 1) for i in I)
        if abs(np.linalg.det(GJ)) < 1e-12:
            je_typ[name] = "fehlt (Fenster flach)"
            continue
        y = P + 0.5 * g[list(I)].sum(axis=0)
        s = np.linalg.solve(GJ, y.T).T
        drin = np.max(np.abs(s), axis=1) < 0.5
        n_I = int(drin.sum())
        v_I = abs(float(np.linalg.det(a[list(I)])))
        je_typ[name] = n_I
        anzahl += n_I
        vol_summe += n_I * v_I
        for x in ek["x6"][drin]:
            for sub in itertools.product((0, 1), repeat=3):
                y6 = x + sum(sub[m] * E[I[m]] for m in range(3))
                if tuple(int(v) for v in kanon(nh, y6)) not in keys:
                    fehlen += 1
    L3 = nh["L"] ** 3
    return {"rhomboeder": anzahl, "vol_summe": vol_summe, "L3": L3, "rel_abw": abs(vol_summe - L3) / L3,
            "ecken_fehlen": fehlen, "je_typ": je_typ}


# ------------------------------------------------------------------ periodische Delaunay-Zerlegung und Komplex
def kanten_key(v1, o1, v2, o2):
    d = tuple(int(c) for c in (o2 - o1))
    md = tuple(-c for c in d)
    if v1 < v2:
        return (int(v1), int(v2), d), 1, o1
    if v1 > v2:
        return (int(v2), int(v1), md), -1, o2
    if d > md:
        return (int(v1), int(v1), d), 1, o1
    return (int(v1), int(v1), md), -1, o2


def flaechen_key(vs, os_):
    best = None
    for m in range(3):
        lst = tuple(sorted((int(vs[u]), tuple(int(c) for c in (os_[u] - os_[m]))) for u in range(3)))
        if best is None or lst < best:
            best = lst
    return best


def umkreis_dreieck(P0, P1, P2):
    u, v = P1 - P0, P2 - P0
    w = np.cross(u, v)
    return P0 + (np.dot(u, u) * np.cross(v, w) + np.dot(v, v) * np.cross(w, u)) / (2.0 * np.dot(w, w))


def netz(nh, saat):
    """Ecken, Delaunay, Komplex, Kontrollen; Bloch-Bausteine fuer S und M."""
    t0 = time.time()
    rng = saat_rng(nh["ordnung"], saat)
    xi = rng.normal(size=3)
    xi /= np.linalg.norm(xi)
    gamma = ETA * xi
    ek = ecken(nh, gamma)
    rh = rhomboeder(nh, ek, gamma)
    r, L, N = ek["r"], nh["L"], ek["N"]
    rj = r + SIGMA_D * rng.normal(size=r.shape)
    big = (rj[None, :, :] + L * OFFS[:, None, :]).reshape(-1, 3)
    tri = Delaunay(big)
    S = tri.simplices
    cent = big[S].mean(axis=1)
    S = S[np.all((cent >= 0.0) & (cent < L), axis=1)]
    vid, off = S % N, OFFS[S // N]
    kanten, flaechen, fl_tet = {}, {}, {}
    vols = np.empty(len(S))
    for t in range(len(S)):
        vs, os_ = vid[t], off[t]
        P = r[vs] + L * os_
        vols[t] = np.linalg.det(np.array([P[1] - P[0], P[2] - P[0], P[3] - P[0]])) / 6.0
        for u, w in itertools.combinations(range(4), 2):
            key = kanten_key(vs[u], os_[u], vs[w], os_[w])[0]
            if key not in kanten:
                kanten[key] = len(kanten)
        for d3 in itertools.combinations(range(4), 3):
            key = flaechen_key(vs[list(d3)], os_[list(d3)])
            if key not in flaechen:
                flaechen[key] = len(flaechen)
            fl_tet[key] = fl_tet.get(key, 0) + 1
    V, Ek, F, T = N, len(kanten), len(flaechen), len(S)
    kl = sorted(kanten.items(), key=lambda kv: kv[1])
    ei = np.array([k[0] for k, _ in kl])
    ej = np.array([k[1] for k, _ in kl])
    ed = np.array([k[2] for k, _ in kl], dtype=float)
    D = r[ej] + L * ed - r[ei]
    rmid = r[ei] + 0.5 * D
    laengen = np.linalg.norm(D, axis=1)
    # Skalar: gerichtete Bindungen
    bI = np.concatenate([ei, ej])
    bJ = np.concatenate([ej, ei])
    bD = np.concatenate([D, -D])
    deg = np.bincount(bI, minlength=V).astype(float)
    # Maxwell: C (Flaechen x Kanten) und G (Kanten x Ecken), Phasen relativ zur Lage
    rowC, colC, sgnC, relC = [], [], [], []
    for key, f in flaechen.items():
        vs = [v for v, _ in key]
        os_ = [np.array(o, dtype=np.int64) for _, o in key]
        rf = np.mean([r[vs[u]] + L * os_[u] for u in range(3)], axis=0)
        for u, w in ((0, 1), (1, 2), (2, 0)):
            kk, sg, sh = kanten_key(vs[u], os_[u], vs[w], os_[w])
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
           "G": (rowG, colG, sgnG, relG)}
    # Kontrollen: Zusammenhang, Euler, Mannigfaltigkeit, Volumen, Delaunay (leere Kugel), Hodge-Sterne
    A = sps.coo_matrix((np.ones(Ek), (ei, ej)), shape=(V, V))
    ncomp = int(connected_components(A + A.T, directed=False)[0])
    voll = list(fl_tet.values())
    bigE = (r[None, :, :] + L * OFFS[:, None, :]).reshape(-1, 3)
    baum = cKDTree(bigE)
    verletzt, kugel_entartet, flach = 0, 0, 0
    dual_len = np.zeros(F)
    dual_flaeche = np.zeros(Ek)
    for t in range(T):
        vs, os_ = vid[t], off[t]
        P = r[vs] + L * os_
        if abs(vols[t]) < 1e-10:
            flach += 1
            continue
        M3 = 2.0 * np.array([P[1] - P[0], P[2] - P[0], P[3] - P[0]])
        rhs = np.array([P[m] @ P[m] - P[0] @ P[0] for m in (1, 2, 3)])
        cT = np.linalg.solve(M3, rhs)
        R = np.linalg.norm(cT - P[0])
        idx = baum.query_ball_point(cT, R * (1 + 1e-9))
        dist = np.linalg.norm(bigE[idx] - cT, axis=1)
        verletzt += int(np.sum(dist < R * (1 - 1e-9)))
        kugel_entartet += int(max(0, np.sum(np.abs(dist - R) <= 1e-9 * R) - 4))
        for d3 in itertools.combinations(range(4), 3):
            opp = [m for m in range(4) if m not in d3][0]
            Q = P[list(d3)]
            cf = umkreis_dreieck(Q[0], Q[1], Q[2])
            nv = np.cross(Q[1] - Q[0], Q[2] - Q[0])
            if np.dot(nv, P[opp] - Q[0]) < 0:
                nv = -nv
            nv /= np.linalg.norm(nv)
            hfT = float(np.dot(cT - cf, nv))
            fk = flaechen[flaechen_key(vs[list(d3)], os_[list(d3)])]
            dual_len[fk] += hfT
            for u, w in ((0, 1), (1, 2), (0, 2)):
                z = [m for m in range(3) if m not in (u, w)][0]
                me = 0.5 * (Q[u] + Q[w])
                ev = Q[w] - Q[u]
                uv = Q[z] - me
                uv = uv - np.dot(uv, ev) / np.dot(ev, ev) * ev
                uv /= np.linalg.norm(uv)
                hef = float(np.dot(cf - me, uv))
                ek_ = kanten[kanten_key(vs[d3[u]], os_[d3[u]], vs[d3[w]], os_[d3[w]])[0]]
                dual_flaeche[ek_] += 0.5 * hef * hfT
    fl_area = np.zeros(F)
    for key, f in flaechen.items():
        Q = np.array([r[v] + L * np.array(o) for v, o in key])
        fl_area[f] = 0.5 * np.linalg.norm(np.cross(Q[1] - Q[0], Q[2] - Q[0]))
    stern1 = dual_flaeche / laengen
    stern2 = dual_len / fl_area

    def vorzeichen(x):
        sk = max(float(np.max(np.abs(x))), 1e-300)
        return {"min": float(np.min(x)), "max": float(np.max(x)), "negativ": int(np.sum(x < -1e-9 * sk)),
                "null": int(np.sum(np.abs(x) <= 1e-9 * sk)), "positiv": int(np.sum(x > 1e-9 * sk))}

    pruef = {"N": V, "N_erwartet": ek["N_erwartet"], "E": Ek, "F": F, "T": T, "euler": V - Ek + F - T,
             "zusammenhang_komponenten": ncomp, "flaechen_mit_2_tetraedern": int(sum(1 for c in voll if c == 2)),
             "flaechen_sonst": int(sum(1 for c in voll if c != 2)),
             "vol_summe": float(np.sum(np.abs(vols))), "L3": L ** 3,
             "vol_rel_abw": float(abs(np.sum(np.abs(vols)) - L ** 3) / L ** 3),
             "vol_min": float(np.min(np.abs(vols))), "vol_max": float(np.max(np.abs(vols))),
             "tetraeder_flach_1e-10": int(flach), "delaunay_verletzt": int(verletzt),
             "kugel_entartet_zusatzpunkte": int(kugel_entartet),
             "kantenlaenge_min": float(laengen.min()), "kantenlaenge_max": float(laengen.max()),
             "grad_min": int(deg.min()), "grad_max": int(deg.max()), "grad_mittel": float(deg.mean()),
             "stern1": vorzeichen(stern1), "stern2": vorzeichen(stern2),
             "gamma": gamma.tolist(), "fenster": {k: v for k, v in ek.items() if k not in ("x6", "r")},
             "rhomboeder": rh, "selbstbild_kanten": int(np.sum(ei == ej)), "zeit_s": time.time() - t0}
    return bau, pruef


# ------------------------------------------------------------------ Bloch-Operatoren
def bloch(st, k, form):
    row, col, sgn, rel = st
    return sps.csr_matrix((sgn * np.exp(1j * (rel @ k)), (row, col)), shape=form)


def op_skalar(bau):
    V, bI, bJ, bD, deg = bau["V"], bau["bI"], bau["bJ"], bau["bD"], bau["deg"]
    dia = np.arange(V)

    def f(k):
        M = np.zeros((V, V), dtype=complex)
        np.add.at(M, (bI, bJ), -np.exp(1j * (bD @ k)))
        M[dia, dia] += deg
        ev = np.linalg.eigvalsh(M)
        return [math.sqrt(max(ev[0], 0.0))]
    return f, 1


def maxwell_eigen(bau, k, nev=4, min_ph=2):
    """Kleinste Eigenwerte von K' = C^dag C + G G^dag (Shift-Invert bei 0); Photonen = Eigenvektoren mit G^dag v = 0
    (rho < 1e-6), Laengsmoden (rho = 1) werden verworfen. Das Photonspektrum ist das von C^dag C ohne Eichnullen."""
    V, E, F = bau["V"], bau["E"], bau["F"]
    C = bloch(bau["C"], k, (F, E))
    G = bloch(bau["G"], k, (E, V))
    K = (C.conj().T @ C + G @ G.conj().T).tocsc()
    GH = G.conj().T.tocsr()
    for m_ev in (nev, 2 * nev, 4 * nev):
        w, v = spla.eigsh(K, k=m_ev, sigma=0.0, which="LM")
        o = np.argsort(w)
        w, v = np.real(w[o]), v[:, o]
        rho = np.array([np.linalg.norm(GH @ v[:, m]) ** 2 / max(abs(w[m]) * np.linalg.norm(v[:, m]) ** 2, 1e-300)
                        for m in range(m_ev)])
        ph = w[rho < 1e-6]
        if len(ph) >= min_ph:
            return ph, w, rho
    raise RuntimeError(f"zu wenige Photonen: {len(ph)}")


def op_maxwell(bau):
    def f(k):
        ph = maxwell_eigen(bau, k)[0]
        lo, hi = math.sqrt(max(ph[0], 0.0)), math.sqrt(max(ph[1], 0.0))
        return [lo, hi, math.sqrt(0.5 * (lo * lo + hi * hi))]
    return f, 3


MU_RITZ = 1e-9


def taylor(st, n, mmax, form):
    row, col, sgn, rel = st
    x = rel @ n
    return [sps.csr_matrix((sgn * (1j * x) ** m / math.factorial(m), (row, col)), shape=form) for m in range(mmax + 1)]


def ritz_vorbereiten(bau):
    """k = 0: K0 = C^T C + G G^T (reell), harmonische Formen H (3 Spalten), LU von K0 + MU_RITZ (reell)."""
    V, E, F = bau["V"], bau["E"], bau["F"]
    C0 = bloch(bau["C"], np.zeros(3), (F, E)).real.tocsr()
    G0 = bloch(bau["G"], np.zeros(3), (E, V)).real.tocsr()
    K0 = (C0.T @ C0 + G0 @ G0.T).tocsc()
    rel = bau["G"][3]
    D = np.zeros((E, 3))
    np.add.at(D, bau["G"][0], bau["G"][2][:, None] * rel)    # Kantenvektor j - i je Kante (geschlossene 1-Formen)
    L0 = (G0.T @ G0).tocsc() + 1e-10 * sps.identity(V, format="csc")
    phi = spla.splu(L0).solve(G0.T @ D)
    H = D - G0 @ phi
    H, _ = np.linalg.qr(H)
    lu = spla.splu((K0 + MU_RITZ * sps.identity(E, format="csc")).tocsc())
    kontrolle = {"K0H_max": float(np.max(np.abs(K0 @ H))), "C0D_max": float(np.max(np.abs(C0 @ D)))}
    return {"H": H, "lu": lu, "kontrolle": kontrolle}


def op_maxwell_ritz_fabrik(bau, vor, mmax=4):
    """Rayleigh-Ritz in der k.p-Basis: B_0 = H, B_j = R (K_m B_(j-m)), m = 1..j, j <= mmax, mit
    R = Q (K0 + MU_RITZ)^-1 Q. Enthaelt die Taylor-Glieder der Eigenvektoren bis t^mmax; Ritz-Fehler ~ t^(2 mmax + 2)."""
    V, E, F = bau["V"], bau["E"], bau["F"]
    H, lu = vor["H"], vor["lu"]

    def Rt(Y):
        Y = Y - H @ (H.T @ Y)
        X = lu.solve(np.ascontiguousarray(Y.real)) + 1j * lu.solve(np.ascontiguousarray(Y.imag))
        return X - H @ (H.T @ X)

    def fabrik(n):
        Cm = taylor(bau["C"], n, mmax, (F, E))
        Gm = taylor(bau["G"], n, mmax, (E, V))
        Km = [sum((Cm[a].conj().T @ Cm[m - a] + Gm[a] @ Gm[m - a].conj().T) for a in range(m + 1))
              for m in range(mmax + 1)]
        B = [H.astype(complex)]
        for j in range(1, mmax + 1):
            B.append(np.hstack([Rt(Km[m] @ B[j - m]) for m in range(1, j + 1)]))
        Sr = np.hstack(B)
        Sr = Sr / np.linalg.norm(Sr, axis=0)
        U, s, _ = np.linalg.svd(Sr, full_matrices=False)
        S = U[:, s > 1e-12 * s[0]]

        def f(k):
            C = bloch(bau["C"], k, (F, E))
            G = bloch(bau["G"], k, (E, V))
            KS = C.conj().T @ (C @ S) + G @ (G.conj().T @ S)
            w, Y = np.linalg.eigh(S.conj().T @ KS)
            Ux = S @ Y[:, :4]
            GU = G.conj().T @ Ux
            rho = np.sum(np.abs(GU) ** 2, axis=0) / np.maximum(np.abs(w[:4]) * np.sum(np.abs(Ux) ** 2, axis=0), 1e-300)
            ph = w[:4][rho < 0.5]
            lo, hi = math.sqrt(max(ph[0], 0.0)), math.sqrt(max(ph[1], 0.0))
            return [lo, hi, math.sqrt(0.5 * (lo * lo + hi * hi))]
        f.basis_dim = S.shape[1]
        return f
    return fabrik


ZWEIGE = {"S": ["skalar"], "M": ["maxwell_lo", "maxwell_hi", "maxwell_mittel"]}


# ------------------------------------------------------------------ Richtungen und Kugelflaechenfunktionen
def halbkugel(m):
    return ln.fib(2 * m)[:m]


def harm(n, lmax=6):
    th = np.arccos(np.clip(n[:, 2], -1.0, 1.0))
    ph = np.arctan2(n[:, 1], n[:, 0])
    cols, lab = [], []
    for l in range(0, lmax + 1, 2):
        for m in range(-l, l + 1):
            Y = sph_harm_y(l, abs(m), th, ph)
            if m == 0:
                f = Y.real
            elif m > 0:
                f = math.sqrt(2.0) * (-1) ** m * Y.real
            else:
                f = math.sqrt(2.0) * (-1) ** m * Y.imag
            cols.append(f * math.sqrt(4.0 * math.pi))     # RMS-normiert (Mittel von Y^2 ueber die Kugel = 1)
            lab.append((l, m))
    return np.stack(cols, axis=1), lab


def referenzen():
    Q = ln.fib(20000)
    Yq, lab = harm(Q)
    gram = Yq.T @ Yq / len(Q)
    a, _ = projektionen()
    x, y, z = Q[:, 0], Q[:, 1], Q[:, 2]
    funk = {"K4": x ** 4 + y ** 4 + z ** 4 - 0.6,
            "S6": x ** 6 + y ** 6 + z ** 6,
            "A6": (x * x - y * y) * (y * y - z * z) * (z * z - x * x),
            "I6": np.sum((Q @ a.T) ** 6, axis=1)}
    koef, rest = {}, {}
    for k_, f in funk.items():
        c, *_ = np.linalg.lstsq(Yq, f, rcond=None)
        koef[k_] = c
        rest[k_] = float(np.sqrt(np.mean((Yq @ c - f) ** 2)))
    lab = np.array(lab)
    bl = {l: np.where(lab[:, 0] == l)[0] for l in (0, 2, 4, 6)}
    k4 = koef["K4"][bl[4]]
    o6 = koef["S6"][bl[6]]
    a6 = koef["A6"][bl[6]]
    j6 = koef["I6"][bl[6]]
    e1 = o6 / np.linalg.norm(o6)
    a6p = a6 - np.dot(a6, e1) * e1
    e2 = a6p / np.linalg.norm(a6p)
    j6h = j6 / np.linalg.norm(j6)
    kontrolle = {"gram_max_abw": float(np.max(np.abs(gram - np.eye(len(gram))))),
                 "rest_darstellung": rest,
                 "K4_nicht_l4": float(np.linalg.norm(np.delete(koef["K4"], bl[4]))),
                 "A6_nicht_l6": float(np.linalg.norm(np.delete(koef["A6"], bl[6]))),
                 "K4_rms": float(np.linalg.norm(k4)),
                 "I6_in_Th_ebene_rest": float(np.linalg.norm(j6h - np.dot(j6h, e1) * e1 - np.dot(j6h, e2) * e2)),
                 "I6_l2_l4": float(np.linalg.norm(koef["I6"][np.concatenate([bl[2], bl[4]])]))}
    return {"bl": bl, "k4": k4, "e1": e1, "e2": e2, "j6h": j6h, "kontrolle": kontrolle}


def zerlegen(nd, werte, ref):
    Y, _ = harm(nd)
    c, *_ = np.linalg.lstsq(Y, werte, rcond=None)
    rest = float(np.sqrt(np.mean((Y @ c - werte) ** 2)))
    bl = ref["bl"]
    c4, c6 = c[bl[4]], c[bl[6]]
    k4 = ref["k4"]
    p4 = float(np.dot(c4, k4) / np.linalg.norm(k4))
    t1, t2 = float(np.dot(c6, ref["e1"])), float(np.dot(c6, ref["e2"]))
    return {"mittel": float(c[bl[0]][0]), "rms_l2": float(np.linalg.norm(c[bl[2]])),
            "rms_l4": float(np.linalg.norm(c4)), "rms_l6": float(np.linalg.norm(c6)),
            "beta_S4": float(np.dot(c4, k4) / np.dot(k4, k4)), "kub4_rms": abs(p4),
            "nichtkub4_rms": float(math.sqrt(max(np.dot(c4, c4) - p4 * p4, 0.0))),
            "th6_O": t1, "th6_A": t2, "th6_rms": float(math.hypot(t1, t2)),
            "ikos6": float(np.dot(c6, ref["j6h"])),
            "nicht_th6_rms": float(math.sqrt(max(np.dot(c6, c6) - t1 * t1 - t2 * t2, 0.0))),
            "rest_rms": rest, "kondition": float(np.linalg.cond(Y))}


# ------------------------------------------------------------------ Dispersion je Richtung
def dispersion(fabrik, nzw, n, fen, L):
    f0, f1, nk, grad = fen
    kk = np.linspace(f0, f1, nk) * math.pi / L
    op = fabrik(n)
    om = np.array([op(k * n) for k in kk], dtype=float)
    aus = []
    for z in range(nzw):
        fg = ln.fit(kk, om[:, z], grad, gerade=True)
        fv = ln.fit(kk, om[:, z], grad, gerade=False)
        aus.append({"c": fg["c"], "a2": fg.get("a2"), "a4": fg.get("a4"), "rms_rel": fg.get("rms_rel"),
                    "a1_voll": fv.get("a1"), "a2_voll": fv.get("a2")})
    return aus


def operator_messen(name, fabrik, nzw, nd, fen, L, ref):
    t0 = time.time()
    je = [dispersion(fabrik, nzw, n, fen, L) for n in nd]
    out = {}
    for z, zw in enumerate(ZWEIGE[name]):
        c = np.array([e[z]["c"] for e in je])
        a2 = np.array([e[z]["a2"] for e in je])
        a4 = np.array([e[z]["a4"] for e in je])
        a1 = np.array([e[z]["a1_voll"] for e in je])
        out[zw] = {"c_mittel": float(c.mean()), "c_spanne_rel": float((c.max() - c.min()) / abs(c.mean())),
                   "c2_zerlegung": zerlegen(nd, c ** 2, ref),
                   "a2_zerlegung": zerlegen(nd, a2, ref), "a4_zerlegung": zerlegen(nd, a4, ref),
                   "a2_min": float(a2.min()), "a2_max": float(a2.max()),
                   "a1_voll_max_abs": float(np.max(np.abs(a1))),
                   "a2_voll_gegen_gerade_max": float(np.max(np.abs(np.array([e[z]["a2_voll"] for e in je]) - a2))),
                   "fit_rms_rel_max": float(max(e[z]["rms_rel"] for e in je)),
                   "je_richtung": [{"n": n, "c": e[z]["c"], "a2": e[z]["a2"], "a4": e[z]["a4"]}
                                   for n, e in zip(nd, je)]}
    out["_laufzeit_s"] = time.time() - t0
    return out


# ------------------------------------------------------------------ Hauptteile
def kontroll_proben(bau, nh, rng, mit_dicht):
    """Werkzeug-Gegenproben an Zufalls-k: Skalar gegen licht_netz.op_skalar, C G = 0, Maxwell gegen
    licht_netz.op_maxwell (dicht, nur kleine Netze)."""
    out = {}
    bonds = [(int(i), int(j), d) for i, j, d in zip(bau["bI"], bau["bJ"], bau["bD"])]
    ref_s, _ = ln.op_skalar(bau["V"], bonds)
    mein_s, _ = op_skalar(bau)
    abw, cg, mx, luecke = [], [], [], []
    for _ in range(3):
        k = rng.normal(size=3) * 0.5
        abw.append(abs(ref_s(k)[0] - mein_s(k)[0]))
        C = bloch(bau["C"], k, (bau["F"], bau["E"]))
        G = bloch(bau["G"], k, (bau["E"], bau["V"]))
        CG = (C @ G).tocoo()
        cg.append(float(np.max(np.abs(CG.data))) if CG.nnz else 0.0)
        if mit_dicht:
            refm, _ = ln.op_maxwell(lambda kk: bloch(bau["C"], kk, (bau["F"], bau["E"])).toarray(), bau["V"])
            dicht = refm(k)[:2]
            ph = maxwell_eigen(bau, k)[0]
            mx.append(max(abs(dicht[0] - math.sqrt(ph[0])), abs(dicht[1] - math.sqrt(ph[1]))))
    kk = np.array([1.0, 0.3, 0.2])
    kk = kk / np.linalg.norm(kk) * FENSTER_HAUPT[1] * math.pi / nh["L"]
    ph, w, rho = maxwell_eigen(bau, kk, min_ph=3)
    luecke = float(ph[2] / ph[1]) if len(ph) >= 3 else None
    out.update({"skalar_gegen_werkzeug_max": max(abw), "CG_max": max(cg),
                "maxwell_gegen_werkzeug_dicht_max": (max(mx) if mx else None),
                "maxwell_photonen_kmax": [float(v) for v in ph[:3]],
                "maxwell_dritter_durch_zweiter_kmax": luecke})
    return out


def ritz_kontrolle(bau, vor, fab, nh, rng):
    """Ritz gegen exakte Shift-Invert-Eigenwerte (maxwell_eigen) an 2 Zufallsrichtungen, k am Rand des Hauptfensters
    und am Anfang."""
    exakt, _ = op_maxwell(bau)
    abw = []
    for _ in range(2):
        n = rng.normal(size=3)
        n /= np.linalg.norm(n)
        f = fab(n)
        for fk in (FENSTER_HAUPT[0], FENSTER_HAUPT[1]):
            k = n * fk * math.pi / nh["L"]
            e, r_ = exakt(k), f(k)
            abw.append(max(abs(e[i] - r_[i]) / abs(e[i]) for i in range(3)))
    return {"ritz_gegen_exakt_rel_max": float(max(abw)), "basis_dim": int(f.basis_dim), **vor["kontrolle"]}


def rechnen(ordnung, ops, saaten, aus, probe, m_richt):
    t0 = time.time()
    nh = naeherung(ordnung)
    ref = referenzen()
    nd = halbkugel(m_richt)
    erg = {"karte": "DANZER-NAEHERUNG-1", "ordnung": ordnung, "ops": ops, "saaten": saaten, "argv": sys.argv,
           "numpy": np.__version__, "scipy": scipy.__version__, "L": nh["L"], "eps": nh["eps"],
           "naeherung_kontrolle": nh["kontrolle"], "referenz_kontrolle": ref["kontrolle"],
           "fenster_haupt": FENSTER_HAUPT, "fenster_probe": FENSTER_PROBE, "richtungen": m_richt,
           "eta": ETA, "sigma_d": SIGMA_D, "saat_ergebnisse": {}}

    def schreiben():
        erg["laufzeit_s"] = time.time() - t0
        tmp = aus + ".tmp"
        with open(tmp, "w") as fh:
            json.dump(ln.js(erg), fh, indent=1)
        os.replace(tmp, aus)

    for s in saaten:
        ts = time.time()
        bau, pruef = netz(nh, s)
        rng = np.random.default_rng([3746, 99, int(s)])
        se = {"netz": pruef, "kontrollen": kontroll_proben(bau, nh, rng, mit_dicht=(bau["E"] <= 400))}
        print(f"{ordnung} Saat {s}: Netz V={pruef['N']} E={pruef['E']} F={pruef['F']} T={pruef['T']} "
              f"({time.time() - t0:.1f} s)", flush=True)
        for o in ops:
            if o == "S":
                op_s, nzw = op_skalar(bau)
                fab = (lambda n, op_s=op_s: op_s)
            else:
                vor = ritz_vorbereiten(bau)
                fab = op_maxwell_ritz_fabrik(bau, vor)
                nzw = 3
                se["ritz_kontrolle"] = ritz_kontrolle(bau, vor, fab, nh, rng)
            se[o] = operator_messen(o, fab, nzw, nd, FENSTER_HAUPT, nh["L"], ref)
            if probe and s == saaten[0]:
                se[o + "_probe"] = operator_messen(o, fab, nzw, nd, FENSTER_PROBE, nh["L"], ref)
            print(f"  {o}: fertig ({time.time() - t0:.1f} s)", flush=True)
        se["laufzeit_s"] = time.time() - ts
        erg["saat_ergebnisse"][str(s)] = se
        schreiben()
    print(f"fertig {time.time() - t0:.1f} s -> {aus}", flush=True)


def rauch(aus):
    """Rauchtest (<= 120 s): nur Bau, Kontrollen und Zeiten; keine a2-Werte."""
    t0 = time.time()
    ref = referenzen()
    out = {"referenz_kontrolle": ref["kontrolle"], "ordnungen": {}}
    for ordnung in REIHE:
        nh = naeherung(ordnung)
        bau, pruef = netz(nh, 0)
        rng = np.random.default_rng([3746, 98])
        kp = kontroll_proben(bau, nh, rng, mit_dicht=(bau["E"] <= 400))
        op_s, _ = op_skalar(bau)
        op_m, _ = op_maxwell(bau)
        k = np.array([0.3, 0.2, 0.1]) * math.pi / nh["L"]
        ta = time.time()
        op_s(k)
        ts = time.time() - ta
        ta = time.time()
        op_m(k)
        tm = time.time() - ta
        ta = time.time()
        vor = ritz_vorbereiten(bau)
        t_vor = time.time() - ta
        fab = op_maxwell_ritz_fabrik(bau, vor)
        ta = time.time()
        fab(np.array([1.0, 0.0, 0.0]))
        t_fab = time.time() - ta
        rk = ritz_kontrolle(bau, vor, fab, nh, np.random.default_rng([3746, 97]))
        f1 = fab(k / np.linalg.norm(k))
        ta = time.time()
        f1(k)
        t_ritz = time.time() - ta
        out["ordnungen"][ordnung] = {"L": nh["L"], "eps": nh["eps"], "naeherung_kontrolle": nh["kontrolle"],
                                     "netz": pruef, "kontrollen": kp, "zeit_skalar_s": ts, "zeit_maxwell_s": tm,
                                     "ritz_kontrolle": rk, "zeit_ritz_vorbereiten_s": t_vor,
                                     "zeit_ritz_basis_je_richtung_s": t_fab, "zeit_ritz_je_k_s": t_ritz}
        print(f"   ritz: abw={rk['ritz_gegen_exakt_rel_max']:.2e} dim={rk['basis_dim']} K0H={rk['K0H_max']:.1e} "
              f"t_vor={t_vor:.2f} s t_basis={t_fab:.2f} s t_k={t_ritz:.4f} s", flush=True)
        print(f"{ordnung}: V={pruef['N']} (erwartet {pruef['N_erwartet']:.3f}) E={pruef['E']} F={pruef['F']} "
              f"T={pruef['T']} euler={pruef['euler']} vol_abw={pruef['vol_rel_abw']:.2e} "
              f"flach={pruef['tetraeder_flach_1e-10']} delaunay_verletzt={pruef['delaunay_verletzt']} "
              f"kugel_entartet={pruef['kugel_entartet_zusatzpunkte']} "
              f"fenster_entartet={pruef['fenster']['fenster_entartet_1e-5']} "
              f"rhomb_vol_abw={pruef['rhomboeder']['rel_abw']:.2e} rhomb_ecken_fehlen="
              f"{pruef['rhomboeder']['ecken_fehlen']} t_skalar={ts:.3f} s t_maxwell={tm:.3f} s "
              f"(gesamt {time.time() - t0:.1f} s)", flush=True)
    out["laufzeit_s"] = time.time() - t0
    with open(aus, "w") as fh:
        json.dump(ln.js(out), fh, indent=1)


# ------------------------------------------------------------------ Auswertung und Urteile (PLAN Abschnitt 6)
def auswerten(aus, png, eingaben):
    daten = {}
    for p in eingaben:
        d = json.load(open(p))
        o = d["ordnung"]
        daten.setdefault(o, {"L": d["L"], "eps": d["eps"], "saaten": {}})
        for s, se in d["saat_ergebnisse"].items():
            daten[o]["saaten"].setdefault(s, {}).update(se)
    tab = {}
    zweige = ["skalar", "maxwell_lo", "maxwell_hi", "maxwell_mittel"]
    for o, dd in daten.items():
        tab[o] = {"L": dd["L"], "eps": dd["eps"], "zweige": {}}
        for zw in zweige:
            key = "S" if zw == "skalar" else "M"
            werte = [se[key][zw] for se in dd["saaten"].values() if key in se]
            if not werte:
                continue
            z = {"saaten": len(werte)}
            for g in ("beta_S4", "th6_rms", "th6_O", "th6_A", "ikos6", "rms_l6", "rms_l2", "nichtkub4_rms",
                      "mittel", "rest_rms"):
                v = np.array([w["a2_zerlegung"][g] for w in werte])
                z["a2_" + g] = {"mittel": float(v.mean()), "sd": float(v.std()), "werte": v.tolist()}
            for g in ("beta_S4", "th6_rms", "ikos6", "mittel"):
                v = np.array([w["a4_zerlegung"][g] for w in werte])
                z["a4_" + g] = {"mittel": float(v.mean()), "sd": float(v.std())}
            sp = np.array([w["c_spanne_rel"] for w in werte])
            z["c_spanne_rel"] = {"mittel": float(sp.mean()), "max": float(sp.max()), "werte": sp.tolist()}
            z["c_mittel"] = float(np.mean([w["c_mittel"] for w in werte]))
            z["c2_rms_l2_rel"] = float(np.mean([w["c2_zerlegung"]["rms_l2"] / w["c2_zerlegung"]["mittel"]
                                                for w in werte]))
            z["a1_voll_max_abs"] = float(max(w["a1_voll_max_abs"] for w in werte))
            tab[o]["zweige"][zw] = z
        tab[o]["netz"] = {s: se["netz"] for s, se in dd["saaten"].items()}
        tab[o]["kontrollen"] = {s: se.get("kontrollen") for s, se in dd["saaten"].items()}
        tab[o]["probe"] = {}
        for s, se in dd["saaten"].items():
            for key in ("S_probe", "M_probe"):
                if key in se:
                    tab[o]["probe"][key] = {zw: {"beta_S4": se[key][zw]["a2_zerlegung"]["beta_S4"],
                                                 "th6_rms": se[key][zw]["a2_zerlegung"]["th6_rms"],
                                                 "beta_S4_haupt": se[key[0]][zw]["a2_zerlegung"]["beta_S4"],
                                                 "th6_rms_haupt": se[key[0]][zw]["a2_zerlegung"]["th6_rms"]}
                                            for zw in ZWEIGE[key[0]]}
    urteile = urteilen(tab)
    out = {"karte": "DANZER-NAEHERUNG-1", "argv": sys.argv, "eingaben": eingaben, "tabelle": tab, "urteile": urteile}
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
    # N1: Spanne des Grundtempos < 1e-6 je Saat, Ordnung und Zweig (Kartenwortlaut "auf jeder Naeherung")
    n1 = {}
    for o, t in tab.items():
        for zw, z in t["zweige"].items():
            if zw == "maxwell_mittel":
                continue
            n1[f"{o}/{zw}"] = {"max_spanne": z["c_spanne_rel"]["max"], "ok": z["c_spanne_rel"]["max"] < N1_SCHWELLE}
    u["N1"] = {"urteil": urteil_menge([v["ok"] for v in n1.values()]), "je": n1}
    # N2 und N3 je Hauptgroesse: Skalar und Maxwell-Mittel; beschreibend lo, hi
    for nr in ("N2", "N3"):
        je = {}
        for zw in ("skalar", "maxwell_mittel", "maxwell_lo", "maxwell_hi"):
            reihe = [o for o in REIHE if o in tab and zw in tab[o]["zweige"]]
            if "1/1" not in reihe or "3/2" not in reihe:
                je[zw] = {"urteil": "nicht auswertbar", "ordnungen": reihe}
                continue
            if nr == "N2":
                w = {o: abs(tab[o]["zweige"][zw]["a2_beta_S4"]["mittel"]) for o in reihe}
                R = w["3/2"] / w["1/1"] if w["1/1"] > 0 else None
                ok = (R is not None and R <= N2_DRITTEL)
                je[zw] = {"urteil": "eingetroffen" if ok else "nicht eingetroffen", "verhaeltnis_3/2_zu_1/1": R,
                          "betrag_beta": w}
            else:
                w = {o: tab[o]["zweige"][zw]["a2_th6_rms"]["mittel"] for o in reihe}
                boden = {o: max(1e-7, 3.0 * tab[o]["zweige"][zw]["a2_rest_rms"]["mittel"]) for o in reihe}
                ueber = all(w[o] > boden[o] for o in reihe)
                bleibt = w["3/2"] >= w["1/1"] / 3.0
                konv = ("2/1" in w) and abs(w["3/2"] - w["2/1"]) <= abs(w["2/1"] - w["1/1"])
                ok = ueber and bleibt and konv
                je[zw] = {"urteil": "eingetroffen" if ok else "nicht eingetroffen", "th6_rms": w, "boden": boden,
                          "ueber_boden": ueber, "bleibt_ueber_drittel": bleibt, "konvergiert": konv}
        haupt = [je[z]["urteil"] for z in ("skalar", "maxwell_mittel") if je[z]["urteil"] != "nicht auswertbar"]
        u[nr] = {"urteil_plan": urteil_menge([h == "eingetroffen" for h in haupt]) if haupt else "nicht auswertbar",
                 "urteil_karte_alle_zweige": urteil_menge([v["urteil"] == "eingetroffen" for v in je.values()
                                                           if v["urteil"] != "nicht auswertbar"]),
                 "je_zweig": je}
    return u


def bild(tab, png):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    farbe = {"skalar": "tab:blue", "maxwell_mittel": "tab:red", "maxwell_lo": "tab:orange", "maxwell_hi": "tab:green"}
    reihe = [o for o in REIHE if o in tab]
    x = np.arange(len(reihe))
    fig, ax = plt.subplots(1, 3, figsize=(17, 5.2))
    for zw, fb in farbe.items():
        xs, b, b_sd, t6, t6_sd, ik = [], [], [], [], [], []
        for i, o in enumerate(reihe):
            z = tab[o]["zweige"].get(zw)
            if z is None:
                continue
            xs.append(i)
            b.append(z["a2_beta_S4"]["mittel"])
            b_sd.append(z["a2_beta_S4"]["sd"])
            t6.append(z["a2_th6_rms"]["mittel"])
            t6_sd.append(z["a2_th6_rms"]["sd"])
            ik.append(z["a2_ikos6"]["mittel"])
            for v in z["a2_beta_S4"]["werte"]:
                ax[0].plot(i + 0.04 * (list(farbe).index(zw) - 1.5), abs(v), ".", color=fb, alpha=0.35, ms=5)
        if not xs:
            continue
        stil = "-" if zw in ("skalar", "maxwell_mittel") else ":"
        ax[0].errorbar(xs, np.abs(b), yerr=b_sd, fmt="o" + stil, color=fb, label=zw, capsize=3)
        ax[1].errorbar(xs, b, yerr=b_sd, fmt="o" + stil, color=fb, label=zw, capsize=3)
        ax[2].errorbar(xs, t6, yerr=t6_sd, fmt="s" + stil, color=fb, label=zw + " (T_h-l=6, RMS)", capsize=3)
        ax[2].plot(xs, np.abs(ik), "x--", color=fb, alpha=0.6)
    eps = np.array([abs(tab[o]["eps"]) for o in reihe])
    for zw in ("skalar", "maxwell_mittel"):
        if "1/1" in tab and zw in tab["1/1"]["zweige"]:
            b0 = abs(tab["1/1"]["zweige"][zw]["a2_beta_S4"]["mittel"])
            ax[0].plot(x, b0 * eps / eps[0], "k--", lw=0.8, alpha=0.6)
            ax[0].axhline(b0 / 3.0, color=farbe[zw], lw=0.6, ls="--", alpha=0.5)
    ax[0].set_yscale("log")
    ax[0].set_title("(a) |l=4-Anteil| = |beta| (a2 ~ alpha + beta S4); gestrichelt schwarz: ~|eps_n|; farbig: 1/3 Start")
    ax[1].axhline(0, color="k", lw=0.6)
    ax[1].set_title("(b) beta mit Vorzeichen (eps_n: +, -, +)")
    ax[2].set_yscale("log")
    ax[2].set_title("(c) l=6-Anteil von a2: T_h-invariant (RMS), x: |ikosaedrische Projektion|")
    for a_ in ax:
        a_.set_xticks(x)
        a_.set_xticklabels([f"{o}\neps={tab[o]['eps']:+.4f}" for o in reihe])
        a_.legend(fontsize=7)
    fig.suptitle("DANZER-NAEHERUNG-1: kubische Restanisotropie von a2 auf AK-Naeherungen (Delaunay), synthetische Rechnung")
    fig.tight_layout()
    fig.savefig(png, dpi=110)
    print(f"bild -> {png}", flush=True)


if __name__ == "__main__":
    arg = sys.argv[1:]
    if len(arg) >= 2 and arg[0] == "rauch":
        rauch(arg[1])
    elif len(arg) >= 5 and arg[0] == "rechnen":
        m = RICHTUNGEN_STANDARD
        if "--richtungen" in arg:
            m = int(arg[arg.index("--richtungen") + 1])
        rechnen(arg[1], arg[2].split(","), [int(s) for s in arg[3].split(",")], arg[4], "--probe" in arg, m)
    elif len(arg) >= 4 and arg[0] == "auswerten":
        auswerten(arg[1], arg[2], arg[3:])
    else:
        print(__doc__)
        sys.exit(2)
