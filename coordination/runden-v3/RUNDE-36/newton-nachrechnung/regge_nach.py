"""Unabhaengige Nachrechnung der Leitung (Runde 36): linearisierter Regge-Eckenoperator auf dem Kuhn-Tetraedergitter.

Prueft ohne den Code von REGGE-RAND-1:
  1. Flachheit des ungestoerten Kuhn-Gitters (alle Fehlwinkel 0).
  2. Lineare Antwort A_v = sum_{e an v} l_e eps_e auf eine Beule delta psi an einer Ecke (zentrale Differenz).
  3. Vergleich mit -8 mal 7-Punkt-Laplace (Kontinuum: R = -8 psi^-5 Laplace psi fuer g = psi^4 delta).
  4. Fourier-Symbol des Operators gegen 8 (6 - 2 sum cos q_i).
Kantenlaenge: l_e = l0_e * psi_mitte^2, psi_mitte als arithmetisches (Variante: geometrisches) Mittel der Endpunkte.
"""
import itertools
import json
import sys

import numpy as np

L = 6
PERMS = list(itertools.permutations(range(3)))
E = np.eye(3, dtype=int)


def idx(p):
    p = np.mod(p, L)
    return int(p[0] * L * L + p[1] * L + p[2])


def tetraeder():
    tets = []
    for x in itertools.product(range(L), repeat=3):
        x = np.array(x)
        for p in PERMS:
            v0 = x
            v1 = v0 + E[p[0]]
            v2 = v1 + E[p[1]]
            v3 = v2 + E[p[2]]
            tets.append((v0, v1, v2, v3))
    return tets


TETS = tetraeder()


def koordinaten(l):
    """Einbettung eines Tetraeders aus den sechs Kantenlaengen l[(i,j)]."""
    l01, l02, l03 = l[(0, 1)], l[(0, 2)], l[(0, 3)]
    l12, l13, l23 = l[(1, 2)], l[(1, 3)], l[(2, 3)]
    p0 = np.zeros(3)
    p1 = np.array([l01, 0.0, 0.0])
    x2 = (l01**2 + l02**2 - l12**2) / (2 * l01)
    y2 = np.sqrt(max(l02**2 - x2**2, 0.0))
    p2 = np.array([x2, y2, 0.0])
    x3 = (l01**2 + l03**2 - l13**2) / (2 * l01)
    y3 = (l02**2 + l03**2 - l23**2 - 2 * x2 * x3) / (2 * y2)
    z3 = np.sqrt(max(l03**2 - x3**2 - y3**2, 0.0))
    p3 = np.array([x3, y3, z3])
    return [p0, p1, p2, p3]


def dieder(P, a, b, c, d):
    ab = P[b] - P[a]
    ab = ab / np.linalg.norm(ab)
    u = P[c] - P[a]
    u = u - np.dot(u, ab) * ab
    w = P[d] - P[a]
    w = w - np.dot(w, ab) * ab
    cosv = np.dot(u, w) / (np.linalg.norm(u) * np.linalg.norm(w))
    return np.arccos(np.clip(cosv, -1.0, 1.0))


def eckensumme(psi, mittel="arith"):
    """A_v = sum_{e an v} l_e eps_e fuer alle Ecken."""
    winkel = {}
    laenge = {}
    for t in TETS:
        ids = [idx(v) for v in t]
        l = {}
        for i, j in itertools.combinations(range(4), 2):
            l0 = np.linalg.norm(t[j] - t[i])
            pa, pb = psi[ids[i]], psi[ids[j]]
            pm = 0.5 * (pa + pb) if mittel == "arith" else np.sqrt(pa * pb)
            l[(i, j)] = l0 * pm**2
        P = koordinaten(l)
        for i, j in itertools.combinations(range(4), 2):
            k, m = [q for q in range(4) if q not in (i, j)]
            key = tuple(sorted((ids[i], ids[j])))
            # Kanten auf dem Torus koennen zwischen denselben Ecken in verschiedene Richtungen laufen; Schluessel um die
            # Richtung ergaenzen
            dvec = tuple(np.mod(t[j] - t[i] if ids[i] <= ids[j] else t[i] - t[j], L))
            key = key + (dvec,)
            winkel[key] = winkel.get(key, 0.0) + dieder(P, i, j, k, m)
            laenge[key] = l[(i, j)]
    A = np.zeros(L**3)
    epsmax = 0.0
    for key, s in winkel.items():
        eps = 2 * np.pi - s
        epsmax = max(epsmax, abs(eps))
        a, b = key[0], key[1]
        A[a] += laenge[key] * eps
        A[b] += laenge[key] * eps
    return A, epsmax, len(winkel)


def main():
    mittel = sys.argv[1] if len(sys.argv) > 1 else "arith"
    psi0 = np.ones(L**3)
    A0, epsflach, nkanten = eckensumme(psi0, mittel)
    delta = 1e-5
    psip = psi0.copy()
    psip[idx(np.array([0, 0, 0]))] += delta
    psim = psi0.copy()
    psim[idx(np.array([0, 0, 0]))] -= delta
    Ap, _, _ = eckensumme(psip, mittel)
    Am, _, _ = eckensumme(psim, mittel)
    antwort = (Ap - Am) / (2 * delta)
    # Schablone nach Abstandsvektor
    schablone = {}
    for x in itertools.product(range(L), repeat=3):
        r = tuple(((np.array(x) + L // 2) % L) - L // 2)
        schablone[r] = antwort[idx(np.array(x))]
    soll = {}
    for r in schablone:
        n = sum(abs(c) for c in r)
        if r == (0, 0, 0):
            soll[r] = 48.0
        elif n == 1:
            soll[r] = -8.0
        else:
            soll[r] = 0.0
    abw = max(abs(schablone[r] - soll[r]) for r in schablone)
    # Fourier-Symbol
    qs = 2 * np.pi * np.arange(L) / L
    sym_abw = 0.0
    for qx in qs:
        for qy in qs:
            for qz in qs:
                S = sum(v * np.cos(qx * r[0] + qy * r[1] + qz * r[2]) for r, v in schablone.items())
                Ssoll = 8 * (6 - 2 * (np.cos(qx) + np.cos(qy) + np.cos(qz)))
                sym_abw = max(sym_abw, abs(S - Ssoll))
    werte = {
        "mittel": mittel,
        "kanten": nkanten,
        "kanten_erwartet": 7 * L**3,
        "max_fehlwinkel_flach": epsflach,
        "mitte": schablone[(0, 0, 0)],
        "achse": [schablone[r] for r in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0)]],
        "flaechendiagonalen": [schablone[r] for r in [(1, 1, 0), (1, -1, 0), (0, 1, 1), (1, 0, -1)]],
        "raumdiagonalen": [schablone[r] for r in [(1, 1, 1), (1, 1, -1), (-1, 1, 1), (-1, -1, -1)]],
        "groesste_abweichung_von_minus8_laplace": abw,
        "groesste_abweichung_symbol": sym_abw,
        "summe_antwort": float(antwort.sum()),
    }
    print(json.dumps(werte, indent=1))


if __name__ == "__main__":
    main()
