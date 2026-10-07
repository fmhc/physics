#!/usr/bin/env python3
"""STABIL-6-8-12, Teil S6 (Leitung claude-primary, 02.10.2026): Feldklumpen auf Polyeder-Graphen.

Gleichung wie AUSPROBIEREN V5 (Kernfunktionen von dort uebernommen):
  Sum_j J (phi_i - phi_j) + (V'(phi_i^2) - w2) phi_i = 0,  V'(S) = 1 - 2S + 1,5 S^2.
Ein Knoten wird bei J = 0 besetzt (Einzelplatzloesung, kleiner oder grosser Ast) und in J fortgesetzt.
J_max = groesstes J, bis zu dem die Fortsetzung traegt (Bisektion); Stabilitaet bei J_max/2.
Aufruf: python stabil_s6.py <aus.json>
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import itertools
import json
import sys
import time

import numpy as np

TOL = 1e-9


def Vp(s):
    return 1 - 2 * s + 1.5 * s * s


def Vpp(s):
    return -2 + 3 * s


def newton(L, w2, phi, tol=1e-12, itmax=60):
    for _ in range(itmax):
        s = phi * phi
        F = L @ phi + (Vp(s) - w2) * phi
        if np.max(np.abs(F)) < tol:
            return phi, True
        JF = L + np.diag(Vp(s) + 2 * s * Vpp(s) - w2)
        try:
            phi = phi - np.linalg.solve(JF, F)
        except np.linalg.LinAlgError:
            return phi, False
        if not np.all(np.isfinite(phi)) or np.max(np.abs(phi)) > 10:
            return phi, False
    s = phi * phi
    return phi, bool(np.max(np.abs(L @ phi + (Vp(s) - w2) * phi)) < tol)


def stab(L, w2, phi):
    """Wie V5: mitrotierendes Phasenbild, gyroskopisch durch omega; Rueckgabe max Re, Art, dQ/domega, n_neg(K_u)."""
    n = phi.size
    w = np.sqrt(w2)
    s = phi * phi
    Ku = L + np.diag(Vp(s) + 2 * s * Vpp(s) - w2)
    Kv = L + np.diag(Vp(s) - w2)
    K = np.block([[Ku, np.zeros((n, n))], [np.zeros((n, n)), Kv]])
    G = np.block([[np.zeros((n, n)), -2 * w * np.eye(n)], [2 * w * np.eye(n), np.zeros((n, n))]])
    A = np.zeros((4 * n, 4 * n))
    A[:2 * n, 2 * n:] = np.eye(2 * n)
    A[2 * n:, :2 * n] = -K
    A[2 * n:, 2 * n:] = -G
    ev = np.linalg.eigvals(A)
    mr = float(np.max(ev.real))
    big = ev[ev.real > TOL]
    art = "stabil" if mr <= TOL else ("reell" if np.all(np.abs(big.imag) < 1e-8) else "oszillatorisch")
    dphi = 2 * w * np.linalg.solve(Ku, phi)
    dQ = 2 * np.sum(s) + 4 * w * phi @ dphi
    nneg = int(np.sum(np.linalg.eigvalsh(Ku) < -TOL))
    return mr, art, float(dQ), nneg


def s_branch(w2, big):
    disc = 4 - 6 * (1 - w2)
    if disc < 0:
        return None
    return (2 + np.sqrt(disc)) / 3 if big else (2 - np.sqrt(disc)) / 3


def laplace(n, kanten, J):
    A = np.zeros((n, n))
    for a, b in kanten:
        A[a, b] = A[b, a] = 1
    return J * (np.diag(A.sum(1)) - A)


def fortsetzen(n, kanten, w2, site, big, J, schritte=60):
    sb = s_branch(w2, big)
    phi = np.zeros(n)
    phi[site] = np.sqrt(sb)
    for Jk in np.linspace(0, J, schritte + 1)[1:]:
        neu, ok = newton(laplace(n, kanten, Jk), w2, phi)
        if not ok or np.max(np.abs(neu)) < 1e-3 or np.max(np.abs(neu - phi)) > 0.3:
            return None
        phi = neu
    return phi


def jmax(n, kanten, w2, site, big, jobergrenze=2.0):
    if fortsetzen(n, kanten, w2, site, big, jobergrenze) is not None:
        return jobergrenze
    lo, hi = 0.0, jobergrenze
    for _ in range(26):
        mid = 0.5 * (lo + hi)
        if fortsetzen(n, kanten, w2, site, big, mid) is not None:
            lo = mid
        else:
            hi = mid
    return lo


def kanten_aus_abstand(P):
    D = np.linalg.norm(P[:, None] - P[None], axis=2)
    dmin = np.min(D[D > 1e-9])
    n = len(P)
    return [(i, j) for i in range(n) for j in range(i + 1, n) if abs(D[i, j] - dmin) < 1e-9]


def graphen():
    G = {"Tetraeder": (4, [(i, j) for i in range(4) for j in range(i + 1, 4)], [(0, "Ecke")])}
    P = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]], float)
    G["Oktaeder"] = (6, kanten_aus_abstand(P), [(0, "Ecke")])
    P = np.array(list(itertools.product((0, 1), repeat=3)), float)
    G["Wuerfel"] = (8, kanten_aus_abstand(P), [(0, "Ecke")])
    phi = (1 + np.sqrt(5)) / 2
    P = []
    for a in (-1, 1):
        for b in (-1, 1):
            P += [(0, a, b * phi), (a, b * phi, 0), (b * phi, 0, a)]
    G["Ikosaeder"] = (12, kanten_aus_abstand(np.array(P, float)), [(0, "Ecke")])
    for N in range(4, 13):
        k = [(i, (i + 1) % N) for i in range(N)] + [(i, N) for i in range(N)]
        G["Rad%d" % N] = (N + 1, k, [(N, "Nabe"), (0, "Ring")])
    return G


def main(pfad):
    t0 = time.time()
    aus = {}
    for name, (n, kanten, orte) in graphen().items():
        grad = np.zeros(n, int)
        for a, b in kanten:
            grad[a] += 1
            grad[b] += 1
        for site, rolle in orte:
            for w2 in (0.6, 0.8, 0.9):
                for big in (False, True):
                    if s_branch(w2, big) is None:
                        continue
                    jm = jmax(n, kanten, w2, site, big)
                    eintrag = {"graph": name, "ecken": n, "rolle": rolle, "grad": int(grad[site]), "w2": w2,
                               "ast": "gross" if big else "klein", "J_max": jm, "J_max_mal_grad": jm * int(grad[site])}
                    phi = fortsetzen(n, kanten, w2, site, big, 0.5 * jm) if jm > 0 else None
                    if phi is not None:
                        mr, art, dQ, nneg = stab(laplace(n, kanten, 0.5 * jm), w2, phi)
                        s = phi * phi
                        eintrag.update(stab_halb=art, maxRe=mr, dQdw=dQ, n_neg=nneg,
                                       anteil_ort=float(s[site] / s.sum()))
                    aus["%s|%s|%.2f|%s" % (name, rolle, w2, eintrag["ast"])] = eintrag
        with open(pfad + ".tmp", "w") as f:
            json.dump(aus, f, indent=1)
        os.replace(pfad + ".tmp", pfad)
    print("s6 fertig", round(time.time() - t0, 1), "s")


if __name__ == "__main__":
    main(sys.argv[1])
