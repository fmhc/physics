#!/usr/bin/env python3
"""INDUZIERT-KUGEL-1 (Runde 39, Code-Agent): Vorzeichen des induzierten Regge-Glieds eines masselosen P1-Skalars
auf Poisson-Netzen der Kugel S^n (n = 4; Kontrolle n = 2) gegen den flachen Torus T^n gleicher Dichte und Punktzahl.

Kugel: N Punkte gleichverteilt auf S^n vom Radius a, omega_n a^n = N (Dichte 1; omega_2 = 4 pi, omega_4 = 8 pi^2/3).
  Konvexe Huelle in R^(n+1) (Qhull ueber scipy ConvexHull) = sphaerisches Delaunay. Orientierung: Normale aus dem
  verallgemeinerten Kreuzprodukt der Kantenvektoren zeigt nach aussen (n.c > 0).
  Regel C (Sehne): Kantenlaengen = Sehnen (echte euklidische Simplizes).
  Regel S (sp-Analog): je Simplex alle Laengen mal f_T = J_T^(1/n), J_T = a^n d0/|c_T|^(n+1) = Jacobi-Faktor der
  Radialprojektion x -> a x/|x| am Schwerpunkt c_T (d0 = Abstand der Facettenebene vom Ursprung).
Torus: n = 4 dichte4d.periodisches_netz (isotrop, L = N^(1/4), s = 0, Grundnetz wie dort); n = 2 zufall2d.zufallsnetz
  (L = N^(1/2)). Beide Dateien unveraendert.
P1: K_T = V P^T G^-1 P aus den Kantenlaengenquadraten (wie induziert.lokal_K_batch und dichte4d.p1_lokal, m^2 = 0).
Gamma = 1/2 log det' K = 1/2 (log det K_(0) + log N), duenne LU wie dichte4d.gamma (MMD_AT_PLUS_A, SymmetricMode,
  diag_pivot_thresh 0, keine Equilibrierung, Summe log U_ii mit math.fsum).
Gamma_M = 1/2 log det'(M^-1 K) = Gamma - 1/2 sum_i log m_i + 1/2 log(sum_i m_i/N), m_i = sum_(T an i) V_T/(n+1).
Volumenkorrektur (exakt, K vom Grad n - 2, M vom Grad n in den Laengen), auf V_R = Summe der Simplexvolumina der Regel:
  Gamma_korr = Gamma + (n-2)/(2n) (N-1) log(V_K/V_R),  Gamma_M_korr = Gamma_M - (N-1)/n log(V_K/V_R).

Aufruf (nur ueber kleintest.sh):
  python kugel.py kontrolle <aus.json>
  python kugel.py messung <aus.json> <n> <N-Liste> <saat0> <anzahl> [blind=0/1]
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
import scipy.linalg as sla
import scipy.sparse as sp
import scipy.sparse.linalg as spla
from scipy.spatial import ConvexHull, cKDTree

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import induziert as ind  # noqa: E402  (unveraendert aus INDUZIERT-1)
import dichte4d as d4    # noqa: E402  (unveraendert aus INDUZIERT-DICHTE-4D)
import zufall2d as z2    # noqa: E402  (unveraendert aus INDUZIERT-ZUFALL-2D / -DICHTE-2D)

SAAT_BASIS = 20261004
KARTE = 39
TORUS_SAAT_OFFSET = 39000
OMEGA = {2: 4.0 * math.pi, 4: 8.0 * math.pi ** 2 / 3.0}
GRAM_E = {n: ind.gram_E(n) for n in (2, 4)}
PMAT = {n: np.hstack([-np.ones((n, 1)), np.eye(n)]) for n in (2, 4)}
PAARE = {n: list(itertools.combinations(range(n + 1), 2)) for n in (2, 4)}


def rss_mb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0


def speichern(ziel, out):
    with open(ziel + ".tmp", "w") as f:
        json.dump(out, f)
    os.replace(ziel + ".tmp", ziel)


def radius(n, N):
    return (N / OMEGA[n]) ** (1.0 / n)


def halb_int_R(n, a):
    """1/2 Int sqrt(g) R auf S^n vom Radius a (R = n(n-1)/a^2); Regge-Summe sum_h A_h delta_h soll dagegen gehen."""
    return 0.5 * n * (n - 1) / a ** 2 * OMEGA[n] * a ** n


# ---------------------------------------------------------------------- P1, LU, Masse
def p1(sq, n):
    """Lokale P1-Steifigkeit aus Kantenlaengenquadraten sq (F, n(n+1)/2), Reihenfolge combinations(range(n+1), 2)."""
    G = np.einsum("fe,eab->fab", sq, GRAM_E[n])
    lam = np.linalg.eigvalsh(G)[:, 0]
    Ginv = np.linalg.inv(G)
    V = np.sqrt(np.maximum(np.linalg.det(G), 0.0)) / math.factorial(n)
    P = PMAT[n]
    Gam = np.matmul(P.T[None, :, :], np.matmul(Ginv, P[None, :, :]))
    Gam = 0.5 * (Gam + np.swapaxes(Gam, 1, 2))
    return V[:, None, None] * Gam, V, lam, Gam


def matrix(tri, N, Kl):
    m = tri.shape[1]
    r = np.repeat(tri, m, axis=1).ravel()
    c = np.tile(tri, (1, m)).ravel()
    K = sp.coo_matrix((Kl.ravel(), (r, c)), shape=(N, N)).tocsc()
    K.sum_duplicates()
    return K


def gamma_lu(K, N):
    """1/2 log det' K per LU der geerdeten Matrix (Knoten 0), wie dichte4d.gamma."""
    t1 = time.time()
    K0 = K[1:, 1:].tocsc()
    K0.sort_indices()
    lu = spla.splu(K0, permc_spec="MMD_AT_PLUS_A", diag_pivot_thresh=0.0,
                   options={"SymmetricMode": True, "Equil": False})
    d = lu.U.diagonal()
    info = {"sek_lu": time.time() - t1, "nnz_K0": int(K0.nnz), "nnz_LU": int(lu.L.nnz + lu.U.nnz),
            "min_U": float(np.min(d)), "neg_U": int(np.sum(d < 0)),
            "perm_gleich": bool(np.array_equal(lu.perm_r, lu.perm_c))}
    g = 0.5 * (math.fsum(np.log(np.abs(d)).tolist()) + math.log(N))
    return g, info


def lu_ok(info):
    return bool(info.get("nicht_einbettbar", 1) == 0 and info.get("neg_U", 1) == 0 and info.get("perm_gleich", False)
                and info.get("min_U", -1.0) > 0)


def auswerten(tri, N, n, sq, V_ziel, dicht=False):
    """Gamma, Gamma_M, Masse, Volumen und Korrekturglieder eines Netzes mit Laengen sq je Simplex."""
    t0 = time.time()
    Kl, V, lam, _ = p1(sq, n)
    out = {"nicht_einbettbar": int(np.sum(~(lam > 0))), "lam_min": float(lam.min())}
    K = matrix(tri, N, Kl)
    out["zeilensumme_rel"] = float(np.abs(np.asarray(K.sum(axis=1))).max() / np.abs(K.data).max())
    if out["nicht_einbettbar"] > 0:
        out["lu"] = dict(out)
        return out
    g, info = gamma_lu(K, N)
    info["nicht_einbettbar"] = out["nicht_einbettbar"]
    m = np.bincount(tri.ravel(), np.repeat(V / (n + 1), n + 1), N)
    VR = math.fsum(V.tolist())
    slm = math.fsum(np.log(m).tolist())
    lnv = math.log(V_ziel / VR)
    out.update({"gamma": g, "gamma_M": g - 0.5 * slm + 0.5 * math.log(VR / N), "sum_log_m": slm, "V": VR,
                "m_min": float(m.min()), "log_VK_VR": lnv,
                "korr": (n - 2) / (2.0 * n) * (N - 1) * lnv, "korr_M": -(N - 1) / float(n) * lnv,
                "lu": info, "sek": time.time() - t0})
    if dicht:
        out["_K"] = K
        out["_m"] = m
    return out


# ---------------------------------------------------------------------- Kugelnetz
def kugelpunkte(n, N, saat, a):
    rng = np.random.default_rng([SAAT_BASIS, KARTE, n, int(N), int(saat)])
    x = rng.standard_normal((N, n + 1))
    return a * x / np.linalg.norm(x, axis=1)[:, None]


def kreuz(E):
    """Verallgemeinertes Kreuzprodukt der n Zeilen von E (F, n, n+1); Ergebnis (F, n+1), Betrag n! V."""
    m = E.shape[2]
    nv = np.empty((E.shape[0], m))
    for k in range(m):
        cols = [c for c in range(m) if c != k]
        nv[:, k] = (-1) ** k * np.linalg.det(E[:, :, cols])
    return nv


def paritaet(A):
    """Paritaet (0/1) der Permutation, die jede Zeile von A aufsteigend sortiert (Inversionen mod 2)."""
    inv = np.zeros(A.shape[0], dtype=np.int64)
    for i in range(A.shape[1]):
        for j in range(i + 1, A.shape[1]):
            inv += (A[:, i] > A[:, j]).astype(np.int64)
    return inv % 2


def topologie(tri, N, n):
    """Ecken verschieden, alle Punkte benutzt, f-Vektor, Euler-Charakteristik, jede Facette (n Ecken) in genau zwei
    Simplizes mit entgegengesetzter induzierter Orientierung."""
    ts = np.sort(tri, axis=1)
    out = {"verschieden": bool(np.all(np.diff(ts, axis=1) > 0)), "alle_knoten": bool(np.unique(tri).size == N)}
    f = {0: int(N), n: int(tri.shape[0])}
    for k in range(2, n + 1):
        idx = np.array(list(itertools.combinations(range(n + 1), k)))
        f[k - 1] = int(np.unique(d4.schluessel(ts, idx, N)).size)
    out["f"] = [f[d] for d in range(n + 1)]
    out["euler"] = int(sum((-1) ** d * f[d] for d in range(n + 1)))
    keys, sig = [], []
    for i in range(n + 1):
        rest = [c for c in range(n + 1) if c != i]
        face = tri[:, rest]
        keys.append(d4.schluessel(np.sort(face, axis=1), np.arange(n)[None, :], N))
        sig.append((-1) ** i * (1 - 2 * paritaet(face)))
    keys = np.concatenate(keys)
    sig = np.concatenate(sig)
    u, inv, cnt = np.unique(keys, return_inverse=True, return_counts=True)
    out["facetten_genau_zwei"] = bool(np.all(cnt == 2))
    out["orientierung_gepaart"] = bool(np.all(np.bincount(inv, sig, u.size) == 0))
    return out


def regge(tri, sq, Gam, n, N):
    """Regge-Summe sum_h A_h (2 pi - sum theta) ueber die Gelenke ((n-2)-Seiten); n = 2: Gauss-Bonnet (A_h = 1).
    Diederwinkel am Gelenk gegenueber dem Eckpaar (i, j): cos theta = -Gam_ij/sqrt(Gam_ii Gam_jj)."""
    ts_keys, theta, flaeche = [], [], []
    for (i, j) in PAARE[n]:
        h = [c for c in range(n + 1) if c not in (i, j)]
        th = np.arccos(np.clip(-Gam[:, i, j] / np.sqrt(Gam[:, i, i] * Gam[:, j, j]), -1.0, 1.0))
        hk = np.sort(tri[:, h], axis=1)
        ts_keys.append(d4.schluessel(hk, np.arange(len(h))[None, :], N))
        theta.append(th)
        if n == 2:
            flaeche.append(np.ones_like(th))
        else:
            e = {p: q for q, p in enumerate(PAARE[n])}
            la = np.sqrt(sq[:, e[(h[0], h[1])]])
            lb = np.sqrt(sq[:, e[(h[0], h[2])]])
            lc = np.sqrt(sq[:, e[(h[1], h[2])]])
            flaeche.append(z2.flaeche_kahan(la, lb, lc))
    keys = np.concatenate(ts_keys)
    theta = np.concatenate(theta)
    flaeche = np.concatenate(flaeche)
    u, inv = np.unique(keys, return_inverse=True)
    summe = np.bincount(inv, theta, u.size)
    A = np.zeros(u.size)
    A[inv] = flaeche
    defizit = 2.0 * math.pi - summe
    return math.fsum((A * defizit).tolist()), int(u.size), float(defizit.min()), float(defizit.max())


def kugelnetz(n, N, saat, nur_punkte=None):
    """Huelle, Orientierung, Pruefungen, Laengen beider Regeln. nur_punkte: Index-Teilmenge fuer die Negativprobe."""
    a = radius(n, N)
    P = kugelpunkte(n, N, saat, a)
    Ph = P if nur_punkte is None else P[nur_punkte]
    Nh = Ph.shape[0]
    t0 = time.time()
    hull = ConvexHull(Ph)
    t_qh = time.time() - t0
    tri = np.ascontiguousarray(hull.simplices, dtype=np.int64)
    eqn = hull.equations[:, :n + 1]
    X = Ph[tri]
    c = X.mean(axis=1)
    nv = kreuz(X[:, 1:, :] - X[:, :1, :])
    flip = np.einsum("fi,fi->f", nv, c) < 0
    tri[flip] = tri[flip][:, [1, 0] + list(range(2, n + 1))]
    X = Ph[tri]
    nv = kreuz(X[:, 1:, :] - X[:, :1, :])
    nn = np.linalg.norm(nv, axis=1)
    nh = nv / nn[:, None]
    d0 = np.einsum("fi,fi->f", nh, c)
    cnorm = np.linalg.norm(c, axis=1)
    # leere Kappen: kein Punkt im Inneren der Kugelkappe ueber der Facette (Kugel um a nh mit Sehnenradius r)
    q = a * nh
    r = np.min(np.linalg.norm(X - q[:, None, :], axis=2), axis=1)
    baum = cKDTree(P)
    innen = baum.query_ball_point(q, r * (1.0 - 1e-9), return_length=True)
    # Laengen
    sqC = np.stack([np.einsum("fi,fi->f", X[:, j] - X[:, i], X[:, j] - X[:, i]) for (i, j) in PAARE[n]], axis=1)
    J = a ** n * d0 / cnorm ** (n + 1)
    sqS = sqC * (J ** (2.0 / n))[:, None]
    # Volumen: Gram, Kreuzprodukt, Quadratur zweiten Grades fuer Int_T J (Summe = Kugelvolumen exakt)
    tq = 1.0 / math.sqrt(n + 2.0)
    Jq = np.zeros(tri.shape[0])
    for i in range(n + 1):
        xq = c + tq * (X[:, i] - c)
        Jq += a ** n * d0 / np.linalg.norm(xq, axis=1) ** (n + 1)
    Jq /= n + 1
    VC_kreuz = nn / math.factorial(n)
    top = topologie(tri, Nh, n)
    pr = dict(top)
    pr.update({"N_huelle": int(Nh), "F": int(tri.shape[0]), "F_je_N": tri.shape[0] / Nh, "sek_qhull": t_qh,
               "orient_umgedreht": int(np.sum(flip)), "d0_min": float(d0.min()),
               "normale_gegen_qhull_min_cos": float(np.min(np.einsum("fi,fi->f", nh, eqn))),
               "kappen_mit_punkt_innen": int(np.sum(innen > 0)), "vol_min": float(VC_kreuz.min()),
               "J_min": float(J.min()), "J_max": float(J.max()),
               "sigma_mittel": float(np.mean(np.log(J)) / n)})
    V_K = OMEGA[n] * a ** n
    geo = {"a": a, "V_K": V_K, "V_C_kreuz": math.fsum(VC_kreuz.tolist()),
           "V_S_mittelpunkt": math.fsum((VC_kreuz * J).tolist()), "V_Q_quadratur": math.fsum((VC_kreuz * Jq).tolist()),
           "halb_int_R": halb_int_R(n, a)}
    return {"tri": tri, "sqC": sqC, "sqS": sqS, "J": J, "pruefung": pr, "geo": geo, "N": Nh, "P": P}


def kugel_gueltig(pr, n):
    return bool(pr["verschieden"] and pr["alle_knoten"] and pr["facetten_genau_zwei"] and pr["orientierung_gepaart"]
                and pr["euler"] == 2 and pr["kappen_mit_punkt_innen"] == 0 and pr["d0_min"] > 0
                and pr["vol_min"] > 0 and pr["normale_gegen_qhull_min_cos"] > 1 - 1e-9
                and (n != 2 or abs(pr.get("gauss_bonnet_abw", 1.0)) <= 1e-8))


# ---------------------------------------------------------------------- Torus
def torusnetz(n, N, saat):
    t0 = time.time()
    if n == 4:
        L = N ** 0.25
        Lv, V, h0 = d4.geometrie(N, L, L)
        z = d4.grundpunkte(N, Lv, TORUS_SAAT_OFFSET + saat)
        nz = d4.periodisches_netz(z, Lv, d4.kvektor(1, Lv), 0.0, h0, "basis")
        pr = nz.pruefen()
        ok = d4.gueltig(pr)
        d = nz.X[:, d4.PB, :] - nz.X[:, d4.PA, :]
        sq = np.einsum("fei,fei->fe", d, d)
        tri = nz.tri
        obj = nz
    else:
        nz = z2.zufallsnetz(N, TORUS_SAAT_OFFSET + saat)
        pr = nz.pruefen()
        ok = bool(pr["euler"] == 0 and pr["kanten_genau_zwei"] and pr["ecken_verschieden"] and pr["orient_min"] > 0
                  and pr["flaeche_summe_rel_abw"] <= 1e-9 and pr["delaunay_verletzt_1e-9"] == 0)
        sq = nz.l0[nz.tk[:, [2, 1, 0]]] ** 2          # Paare (0,1), (0,2), (1,2) liegen den Ecken 2, 1, 0 gegenueber
        tri = nz.tri
        V = nz.A
        obj = nz
    return {"tri": np.ascontiguousarray(tri, dtype=np.int64), "sq": sq, "pruefung": pr, "gueltig": ok, "V": V,
            "sek_netz": time.time() - t0, "obj": obj}


# ---------------------------------------------------------------------- eine Messung (Saat, N)
def eine_messung(n, N, saat, protokoll):
    t0 = time.time()
    kn = kugelnetz(n, N, saat)
    tri = kn["tri"]
    V_K = kn["geo"]["V_K"]
    regeln = {}
    Gam_C = None
    for r, sq in (("C", kn["sqC"]), ("S", kn["sqS"])):
        regeln[r] = auswerten(tri, N, n, sq, V_K)
    _, _, _, Gam_C = p1(kn["sqC"], n)
    rg, n_gelenke, dmin, dmax = regge(tri, kn["sqC"], Gam_C, n, N)
    del Gam_C
    pr = kn["pruefung"]
    pr["regge_C"] = rg
    pr["regge_rel"] = rg / kn["geo"]["halb_int_R"]
    pr["gelenke"] = n_gelenke
    pr["defizit_min"], pr["defizit_max"] = dmin, dmax
    if n == 2:
        pr["gauss_bonnet_abw"] = rg - 4.0 * math.pi
    kg = kugel_gueltig(pr, n)
    t_kugel = time.time() - t0
    t1 = time.time()
    tn = torusnetz(n, N, saat)
    torus = auswerten(tn["tri"], N, n, tn["sq"], float(tn["V"]))
    torus.update({"pruefung": tn["pruefung"], "gueltig": tn["gueltig"], "V_torus": float(tn["V"]),
                  "sek_netz": tn["sek_netz"]})
    lus = [regeln["C"]["lu"], regeln["S"]["lu"], torus["lu"]]
    rec = {"n": n, "N": N, "saat": saat, "kugel": {"geo": kn["geo"], "pruefung": pr, "gueltig": kg, "regeln": regeln},
           "torus": torus, "lu_ok": [lu_ok(x) for x in lus],
           "gueltig": bool(kg and tn["gueltig"] and all(lu_ok(x) for x in lus)),
           "sek_kugel": t_kugel, "sek_torus": time.time() - t1, "sekunden": time.time() - t0, "rss_mb": rss_mb()}
    g = kn["geo"]
    protokoll(f"n={n} N={N} saat={saat}: gueltig {rec['gueltig']} (Kugel {kg}, Torus {tn['gueltig']}, LU "
              f"{rec['lu_ok']}); F/N {pr['F_je_N']:.2f}, Euler {pr['euler']}, Kappen {pr['kappen_mit_punkt_innen']}, "
              f"V_C/V_K {regeln['C'].get('V', float('nan')) / V_K:.5f}, "
              f"V_S/V_K {regeln['S'].get('V', float('nan')) / V_K:.5f}, V_Q/V_K "
              f"{g['V_Q_quadratur'] / V_K:.6f}, Regge/(1/2 Int R) {pr['regge_rel']:.4f}; Qhull {pr['sek_qhull']:.1f} s, "
              f"LU {regeln['C']['lu'].get('sek_lu', -1):.1f}/{regeln['S']['lu'].get('sek_lu', -1):.1f}/"
              f"{torus['lu'].get('sek_lu', -1):.1f} s, Torusnetz {tn['sek_netz']:.1f} s, gesamt "
              f"{rec['sekunden']:.1f} s, RSS {rss_mb():.0f} MB")
    return rec


MESSWERTE = ("gamma", "gamma_M", "sum_log_m")


def modus_messung(n, Nlist, saat0, anzahl, blind, protokoll, out, ziel):
    out.update({"n": n, "Nlist": Nlist, "saat0": saat0, "anzahl": anzahl, "blind": blind, "messungen": []})
    werte = {}
    for saat in range(saat0, saat0 + anzahl):
        for N in Nlist:
            rec = eine_messung(n, N, saat, protokoll)
            if blind:
                sN = math.sqrt(N)
                k = rec["kugel"]["regeln"]
                t = rec["torus"]
                if rec["gueltig"]:
                    for r in ("C", "S"):
                        for q, kq in (("gamma", "korr"), ("gamma_M", "korr_M")):
                            werte.setdefault(f"N{N}/{r}/{q}/diff_korr", []).append(
                                (k[r][q] + k[r][kq] - t[q] - t[kq]) / sN)
                            werte.setdefault(f"N{N}/{r}/{q}/diff_roh", []).append((k[r][q] - t[q]) / sN)
                            werte.setdefault(f"N{N}/{r}/{q}/kugel_allein", []).append(k[r][q] / sN)
                        werte.setdefault(f"N{N}/{r}/gamma_minus_gamma_M_korr", []).append(
                            (k[r]["gamma"] + k[r]["korr"] - k[r]["gamma_M"] - k[r]["korr_M"]
                             - t["gamma"] + t["gamma_M"]) / sN)
                    for q in ("gamma", "gamma_M"):
                        werte.setdefault(f"N{N}/torus/{q}/torus_allein", []).append(t[q] / sN)
                for r in ("C", "S"):
                    for q in MESSWERTE:
                        k[r].pop(q, None)
                for q in MESSWERTE:
                    t.pop(q, None)
                out["blind_streuung"] = {key: {"std_je_wurzelN": float(np.std(v, ddof=1)) if len(v) > 1 else None,
                                               "anzahl": len(v)} for key, v in werte.items()}
            out["messungen"].append(rec)
            speichern(ziel, out)
    return out


# ---------------------------------------------------------------------- Kontrollen
def modus_kontrolle(protokoll, out, ziel):
    rng = np.random.default_rng([SAAT_BASIS, KARTE, 7])
    # (KA) P1 gegen dichte4d.p1_lokal und induziert.lokal_K_batch (n = 4); gegen Kotangens (n = 2)
    X = rng.standard_normal((500, 5, 4))
    sq4 = np.stack([np.sum((X[:, j] - X[:, i]) ** 2, axis=1) for (i, j) in PAARE[4]], axis=1)
    Kl, V, lam, _ = p1(sq4, 4)
    Kd4 = d4.p1_lokal(sq4)[0]
    Kind = ind.lokal_K_batch(4, 0.0, sq4)
    X2 = rng.uniform(0, 1, size=(500, 3, 2))
    sq2 = np.stack([np.sum((X2[:, j] - X2[:, i]) ** 2, axis=1) for (i, j) in PAARE[2]], axis=1)
    Kl2, V2, _, _ = p1(sq2, 2)
    a_, b_, c_ = np.sqrt(sq2[:, 2]), np.sqrt(sq2[:, 1]), np.sqrt(sq2[:, 0])   # Kanten gegenueber Ecke 0, 1, 2
    A = z2.flaeche_kahan(a_, b_, c_)
    w = {(1, 2): (b_ ** 2 + c_ ** 2 - a_ ** 2) / (8 * A), (0, 2): (c_ ** 2 + a_ ** 2 - b_ ** 2) / (8 * A),
         (0, 1): (a_ ** 2 + b_ ** 2 - c_ ** 2) / (8 * A)}
    Kc = np.zeros_like(Kl2)
    for (i, j), wij in w.items():
        Kc[:, i, j] -= wij
        Kc[:, j, i] -= wij
        Kc[:, i, i] += wij
        Kc[:, j, j] += wij
    out["KA_p1"] = {"n4_gegen_dichte4d_max_rel": float(np.max(np.abs(Kl - Kd4)) / np.max(np.abs(Kd4))),
                    "n4_gegen_induziert_max_rel": float(np.max(np.abs(Kl - Kind)) / np.max(np.abs(Kind))),
                    "n2_gegen_kotangens_max_rel": float(np.max(np.abs(Kl2 - Kc)) / np.max(np.abs(Kc))),
                    "n2_flaeche_gegen_heron_max_rel": float(np.max(np.abs(V2 - A) / A))}
    protokoll(f"KA P1: {out['KA_p1']}")
    speichern(ziel, out)
    # (KB, KC) LU gegen dicht (Eigenwerte, slogdet(K + 1 1^T/N)); Gamma_M gegen verallgemeinerte Eigenwerte
    kb = []
    faelle = [("kugel", 4, 400, 990), ("kugel", 2, 400, 990), ("torus", 4, 600, 990), ("torus", 2, 400, 990)]
    for art, n, N, saat in faelle:
        if art == "kugel":
            kn = kugelnetz(n, N, saat)
            netze = [("C", kn["tri"], kn["sqC"], kn["geo"]["V_K"]), ("S", kn["tri"], kn["sqS"], kn["geo"]["V_K"])]
            gueltig = kugel_gueltig(kn["pruefung"] | {"gauss_bonnet_abw": 0.0}, n)
        else:
            tn = torusnetz(n, N, saat)
            netze = [("T", tn["tri"], tn["sq"], float(tn["V"]))]
            gueltig = tn["gueltig"]
        for r, tri, sq, Vz in netze:
            e = auswerten(tri, N, n, sq, Vz, dicht=True)
            Kd = e["_K"].toarray()
            m = e["_m"]
            ev = np.linalg.eigvalsh(Kd)
            sgn, ld = np.linalg.slogdet(Kd + 1.0 / N)
            gev = sla.eigh(Kd, np.diag(m), eigvals_only=True)
            gM_dicht = 0.5 * math.fsum(np.log(np.sort(gev)[1:]).tolist())
            rec = {"art": art, "n": n, "N": N, "regel": r, "gueltig": bool(gueltig), "lu_ok": lu_ok(e["lu"]),
                   "abw_eigen": abs(e["gamma"] - 0.5 * math.fsum(np.log(ev[1:]).tolist())),
                   "abw_slogdet": abs(e["gamma"] - 0.5 * ld), "vorzeichen": float(sgn),
                   "eigen_0": float(ev[0]), "eigen_1": float(ev[1]),
                   "gammaM_abw_dicht": abs(e["gamma_M"] - gM_dicht), "gev_0": float(np.sort(gev)[0])}
            # (KE) Skalierung: Gamma(lambda l) - Gamma(l) = (n-2)/2 (N-1) log lambda, Gamma_M: -(N-1) log lambda
            lamb = 1.37
            e2 = auswerten(tri, N, n, sq * lamb ** 2, Vz)
            rec["skal_gamma_abw"] = abs(e2["gamma"] - e["gamma"] - (n - 2) / 2.0 * (N - 1) * math.log(lamb))
            rec["skal_gammaM_abw"] = abs(e2["gamma_M"] - e["gamma_M"] + (N - 1) * math.log(lamb))
            rec["skal_korr_abw"] = abs((e2["gamma"] + e2["korr"]) - (e["gamma"] + e["korr"]))
            rec["skal_korrM_abw"] = abs((e2["gamma_M"] + e2["korr_M"]) - (e["gamma_M"] + e["korr_M"]))
            if art == "torus" and n == 4:
                g_d4, info_d4 = d4.gamma(tn["obj"], np.sqrt(sq))
                rec["gegen_dichte4d_gamma"] = abs(g_d4 - e["gamma"])
            if art == "torus" and n == 2:
                rec["gegen_zufall2d_gamma"] = abs(tn["obj"].gamma(tn["obj"].l0) - e["gamma"])
            kb.append(rec)
            protokoll(f"KB/KC/KE {art} n={n} N={N} {r}: {rec}")
        if art == "kugel" and n == 2:
            gC = auswerten(netze[0][1], N, n, netze[0][2], netze[0][3])["gamma"]
            gS = auswerten(netze[1][1], N, n, netze[1][2], netze[1][3])["gamma"]
            out["KH_2d_regel_S_gleich_C"] = abs(gC - gS)
            protokoll(f"KH 2D Gamma Regel S gegen C: {abs(gC - gS):.2e}")
        speichern(ziel, out | {"KB": kb})
    out["KB"] = kb
    speichern(ziel, out)
    # (KF) Volumina und Regge-Summe gegen N (beschreibend), Kugel n = 4 und n = 2
    kf = []
    for n, Ns in ((4, (1000, 2000, 4000)), (2, (4000, 16000))):
        for N in Ns:
            kn = kugelnetz(n, N, 991)
            _, V, _, Gam = p1(kn["sqC"], n)
            rg, nh, dmin, dmax = regge(kn["tri"], kn["sqC"], Gam, n, N)
            _, VS, _, _ = p1(kn["sqS"], n)
            g = kn["geo"]
            rec = {"n": n, "N": N, "a": g["a"], "V_C/V_K": math.fsum(V.tolist()) / g["V_K"],
                   "V_C_kreuz/V_K": g["V_C_kreuz"] / g["V_K"], "V_S/V_K": math.fsum(VS.tolist()) / g["V_K"],
                   "V_S_mittelpunkt/V_K": g["V_S_mittelpunkt"] / g["V_K"], "V_Q/V_K": g["V_Q_quadratur"] / g["V_K"],
                   "regge_rel": rg / g["halb_int_R"], "gelenke": nh, "defizit_min": dmin, "defizit_max": dmax,
                   "pruefung": kn["pruefung"]}
            kf.append(rec)
            protokoll(f"KF n={n} N={N}: V_C/V_K {rec['V_C/V_K']:.6f}, V_S/V_K {rec['V_S/V_K']:.6f}, V_Q/V_K "
                      f"{rec['V_Q/V_K']:.7f}, Regge/(1/2 Int R) {rec['regge_rel']:.5f}, Euler "
                      f"{kn['pruefung']['euler']}, Kappen {kn['pruefung']['kappen_mit_punkt_innen']}")
            speichern(ziel, out | {"KF": kf})
    out["KF"] = kf
    # (KG) Negativproben: Huelle ohne einen Punkt gegen alle Punkte (Kappentest muss anschlagen); ein Simplex
    # entfernt (Facettenpaarung und Euler muessen anschlagen)
    kg = []
    for n, N in ((4, 1000), (2, 1000)):
        kn = kugelnetz(n, N, 992, nur_punkte=np.arange(1, N))
        top = topologie(kn["tri"][1:], N - 1, n)
        kg.append({"n": n, "N": N, "kappen_mit_punkt_innen_ohne_punkt0": kn["pruefung"]["kappen_mit_punkt_innen"],
                   "simplex_entfernt_facetten_genau_zwei": top["facetten_genau_zwei"],
                   "simplex_entfernt_euler": top["euler"]})
        protokoll(f"KG n={n}: {kg[-1]}")
    out["KG"] = kg
    speichern(ziel, out)
    return out


def main():
    modus = sys.argv[1]
    t0 = time.time()
    log = []

    def protokoll(s):
        print(s, flush=True)
        log.append(s)

    out = {"modus": modus, "argv": sys.argv[1:], "numpy": np.__version__, "scipy": scipy.__version__}
    ziel = sys.argv[2]
    if modus == "kontrolle":
        modus_kontrolle(protokoll, out, ziel)
    elif modus == "messung":
        n = int(sys.argv[3])
        Nlist = [int(x) for x in sys.argv[4].split(",")]
        saat0, anzahl = int(sys.argv[5]), int(sys.argv[6])
        opt = dict(a.split("=", 1) for a in sys.argv[7:])
        modus_messung(n, Nlist, saat0, anzahl, opt.get("blind", "0") == "1", protokoll, out, ziel)
    else:
        raise SystemExit("unbekannter Modus")
    out["laufzeit_gesamt_s"] = time.time() - t0
    out["rss_mb_ende"] = rss_mb()
    out["protokoll"] = log
    speichern(ziel, out)
    print("geschrieben", ziel, f"{time.time() - t0:.1f} s", flush=True)


if __name__ == "__main__":
    main()
