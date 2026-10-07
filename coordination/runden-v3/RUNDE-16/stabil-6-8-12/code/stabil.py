#!/usr/bin/env python3
"""STABIL-6-8-12 (Runde 16), Leitung claude-primary, 02.10.2026. Karte: ../KARTE.md

Aufruf ueber kleintest.sh auf der .69:
  python stabil.py s1s5 <aus.json>                                 Federnetze (S1) und Rotor-Perioden (S5)
  python stabil.py s3 <seed1> <seed2> <starts> <aus.json>          Thomson-Problem N = 2..25, Wuerfel-Hesse
  python stabil.py s4 <seed> <Nmin> <Nmax> <schritte> <aus.json>   Lennard-Jones-Cluster per Basin-Hopping
  python stabil.py bild <s3.json> <aus.png> <s4-json ...>          Abbildung D2(N)
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import itertools
import json
import sys
import time

import numpy as np
from scipy.optimize import minimize


def speichern(pfad, obj):
    tmp = pfad + ".tmp"
    with open(tmp, "w") as f:
        json.dump(obj, f, indent=1)
    os.replace(tmp, pfad)


# ---------------------------------------------------------------- S1 Federnetze
def nachbarn(name):
    """Nachbarvektoren (beide Vorzeichen) und Teilchendichte rho (m = 1, kubische Kante bzw. Kante 1)."""
    if name == "sc":
        R = [v for v in itertools.product((-1, 0, 1), repeat=3) if sum(map(abs, v)) == 1]
        return np.array(R, float), 1.0
    if name == "bcc":
        return np.array(list(itertools.product((-0.5, 0.5), repeat=3)), float), 2.0
    if name == "fcc":
        R = [v for v in itertools.product((-0.5, 0.0, 0.5), repeat=3) if sum(1 for x in v if x != 0) == 2]
        return np.array(R, float), 4.0
    if name == "bcc2":
        R1 = list(itertools.product((-0.5, 0.5), repeat=3))
        R2 = [v for v in itertools.product((-1, 0, 1), repeat=3) if sum(map(abs, v)) == 1]
        return np.array(R1 + R2, float), 2.0
    if name == "quadrat":
        return np.array([(1, 0), (-1, 0), (0, 1), (0, -1)], float), 1.0
    if name == "dreieck":
        w = np.arange(6) * np.pi / 3
        return np.stack([np.cos(w), np.sin(w)], 1), 2.0 / np.sqrt(3.0)
    raise ValueError(name)


def akustik(R, n):
    """Langwelliger Grenzfall: D(q) ~ |q|^2 A(n), A = 1/2 Sum_b (n.R_b)^2 e_b e_b^T (k = 1)."""
    e = R / np.linalg.norm(R, axis=1)[:, None]
    p = R @ n
    return 0.5 * np.einsum("b,bi,bj->ij", p * p, e, e)


def dynmat(R, q):
    e = R / np.linalg.norm(R, axis=1)[:, None]
    w = 1.0 - np.cos(R @ q)
    return np.einsum("b,bi,bj->ij", w, e, e)


def s1(rng):
    aus = {}
    for name in ("sc", "bcc", "fcc", "bcc2", "quadrat", "dreieck"):
        R, rho = nachbarn(name)
        dim = R.shape[1]
        d = {"nachbarn": int(len(R)), "rho": rho}
        if dim == 3:
            A = akustik(R, np.array([1.0, 0, 0]))
            C11, C44 = rho * A[0, 0], rho * A[1, 1]
            A2 = akustik(R, np.array([1.0, 1, 0]) / np.sqrt(2))
            pL = np.array([1.0, 1, 0]) / np.sqrt(2)
            pT = np.array([1.0, -1, 0]) / np.sqrt(2)
            C12 = 2 * rho * (pL @ A2 @ pL) - C11 - 2 * C44
            d.update(C11=C11, C12=C12, C44=C44, Cstrich=rho * (pT @ A2 @ pT))
            spez = [np.array(v, float) / np.linalg.norm(v) for v in ((1, 0, 0), (1, 1, 0), (1, 1, 1))]
            linie = np.array([1.0, 1, 0])
        else:
            A = akustik(R, np.array([1.0, 0]))
            d.update(C11=rho * A[0, 0], C66=rho * A[1, 1])
            spez = [np.array(v, float) / np.linalg.norm(v) for v in ((1, 0), (1, 1))]
            linie = np.array([1.0, 1])
        d["min_speziell"] = min(float(np.linalg.eigvalsh(akustik(R, n))[0]) for n in spez)
        for tag, anz in (("min_zufall_a", 20000), ("min_zufall_b", 20000)):
            n = rng.normal(size=(anz, dim))
            n /= np.linalg.norm(n, axis=1)[:, None]
            d[tag] = min(float(np.linalg.eigvalsh(akustik(R, v))[0]) for v in n)
        # volles Spektrum entlang der Linie q = t 2 pi (1,1,0) bzw. (1,1)
        lmin = [float(np.linalg.eigvalsh(dynmat(R, t * 2 * np.pi * linie))[0]) for t in np.linspace(0.02, 1.0, 50)]
        d["linie110_max_von_lambda_min"] = max(lmin)
        d["linie110_min_von_lambda_min"] = min(lmin)
        aus[name] = d
    return aus


# ---------------------------------------------------------------- S5 Rotor-Router
def kanten_aus_abstand(P):
    D = np.linalg.norm(P[:, None] - P[None], axis=2)
    dmin = np.min(D[D > 1e-9])
    n = len(P)
    return [(i, j) for i in range(n) for j in range(i + 1, n) if abs(D[i, j] - dmin) < 1e-9]


def graphen():
    G = {
        "K3": [(0, 1), (1, 2), (0, 2)],
        "C4": [(0, 1), (1, 2), (2, 3), (3, 0)],
        "K4": [(i, j) for i in range(4) for j in range(i + 1, 4)],
    }
    G["Oktaeder"] = kanten_aus_abstand(np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]], float))
    G["Wuerfel"] = kanten_aus_abstand(np.array(list(itertools.product((0, 1), repeat=3)), float))
    phi = (1 + np.sqrt(5)) / 2
    P = []
    for s1_ in (-1, 1):
        for s2_ in (-1, 1):
            P += [(0, s1_, s2_ * phi), (s1_, s2_ * phi, 0), (s2_ * phi, 0, s1_)]
    G["Ikosaeder"] = kanten_aus_abstand(np.array(P, float))
    return G


def rotor_periode(kanten, rng):
    n = 1 + max(max(e) for e in kanten)
    nb = [[] for _ in range(n)]
    for a, b in kanten:
        nb[a].append(b)
        nb[b].append(a)
    nb = [sorted(x) for x in nb]
    r = [int(rng.integers(len(nb[v]))) for v in range(n)]
    v = int(rng.integers(n))
    gesehen, t = {}, 0
    while True:
        z = (v, tuple(r))
        if z in gesehen:
            return t - gesehen[z], gesehen[z]
        gesehen[z] = t
        r[v] = (r[v] + 1) % len(nb[v])  # erst drehen, dann gehen (wie Codex FSM-43)
        v = nb[v][r[v]]
        t += 1


def s5(rng):
    aus = {}
    for name, kanten in graphen().items():
        per, trans = zip(*(rotor_periode(kanten, rng) for _ in range(50)))
        aus[name] = {"kanten": len(kanten), "zwei_E": 2 * len(kanten), "perioden": sorted(set(per)),
                     "max_transient": int(max(trans))}
    return aus


# ---------------------------------------------------------------- S3 Thomson
def thomson_eg(y):
    N = y.size // 3
    Y = y.reshape(N, 3)
    r = np.linalg.norm(Y, axis=1)
    X = Y / r[:, None]
    D = X[:, None, :] - X[None, :, :]
    d = np.linalg.norm(D, axis=2)
    np.fill_diagonal(d, np.inf)
    inv = 1.0 / d
    E = 0.5 * inv.sum()
    G = -np.einsum("ij,ijk->ik", inv ** 3, D)
    G = (G - np.sum(G * X, axis=1)[:, None] * X) / r[:, None]
    return E, G.ravel()


def thomson_min(N, rng, starts):
    best, werte = None, []
    for _ in range(starts):
        y0 = rng.normal(size=3 * N)
        res = minimize(thomson_eg, y0, jac=True, method="L-BFGS-B",
                       options=dict(maxiter=20000, gtol=1e-12, ftol=1e-16))
        werte.append(res.fun)
        if best is None or res.fun < best[0]:
            Y = res.x.reshape(N, 3)
            best = (res.fun, (Y / np.linalg.norm(Y, axis=1)[:, None]).tolist())
    werte = np.array(werte)
    return best[0], best[1], int(np.sum(werte < best[0] + 1e-7)), sorted(set(np.round(werte, 6).tolist()))[:6]


def hesse_tangential(X):
    X = np.asarray(X, float)
    N = len(X)
    T = []
    for x in X:
        a = np.array([1.0, 0, 0]) if abs(x[0]) < 0.9 else np.array([0, 1.0, 0])
        t1 = a - (a @ x) * x
        t1 /= np.linalg.norm(t1)
        T.append((t1, np.cross(x, t1)))

    def E_von(w):
        P = np.array([X[i] + w[2 * i] * T[i][0] + w[2 * i + 1] * T[i][1] for i in range(N)])
        return thomson_eg(P.ravel())[0]

    h, n = 1e-4, 2 * N
    H = np.zeros((n, n))
    for a in range(n):
        for b in range(a, n):
            ea, eb = np.zeros(n), np.zeros(n)
            ea[a], eb[b] = h, h
            H[a, b] = H[b, a] = (E_von(ea + eb) - E_von(ea - eb) - E_von(-ea + eb) + E_von(-ea - eb)) / (4 * h * h)
    return np.linalg.eigvalsh(H)


def s3(seeds, starts, pfad):
    aus = {"seeds": seeds, "starts": starts, "E": {}, "laeufe": {}}
    for seed in seeds:
        rng = np.random.default_rng(seed)
        lauf = {}
        for N in range(2, 26):
            t0 = time.time()
            E, X, treffer, niveaus = thomson_min(N, rng, starts)
            lauf[str(N)] = {"E": E, "treffer": treffer, "niveaus": niveaus, "sek": time.time() - t0,
                            "X": X if N in (6, 8, 12) else None}
            aus["laeufe"][str(seed)] = lauf
            speichern(pfad, aus)
    a, b = (aus["laeufe"][str(s)] for s in seeds)
    aus["E"] = {N: min(a[N]["E"], b[N]["E"]) for N in a}
    aus["seed_abweichung_max"] = max(abs(a[N]["E"] - b[N]["E"]) for N in a)
    E = {int(k): v for k, v in aus["E"].items()}
    aus["D2"] = {N: E[N + 1] - 2 * E[N] + E[N - 1] for N in range(3, 25)}
    wuerfel = np.array(list(itertools.product((-1, 1), repeat=3)), float) / np.sqrt(3)
    ew = hesse_tangential(wuerfel)
    aus["wuerfel"] = {"E": thomson_eg(wuerfel.ravel())[0], "hesse_eigen": ew.tolist()}
    aus["n8_minimum_hesse_eigen"] = hesse_tangential(np.array(a["8"]["X"] if a["8"]["E"] <= b["8"]["E"] else b["8"]["X"])).tolist()
    speichern(pfad, aus)


# ---------------------------------------------------------------- S4 Lennard-Jones
def lj_eg(x):
    N = x.size // 3
    X = x.reshape(N, 3)
    D = X[:, None, :] - X[None, :, :]
    r2 = np.sum(D * D, axis=2)
    np.fill_diagonal(r2, np.inf)
    ir2 = 1.0 / r2
    ir6 = ir2 ** 3
    ir12 = ir6 * ir6
    E = 2.0 * np.sum(ir12 - ir6)
    f = (-48.0 * ir12 + 24.0 * ir6) * ir2
    G = np.einsum("ij,ijk->ik", f, D)
    return E, G.ravel()


def lj_lokal(x):
    res = minimize(lj_eg, x, jac=True, method="L-BFGS-B", options=dict(maxiter=10000, gtol=1e-9, ftol=1e-15))
    return res.x, float(res.fun)


def lj_binden(x, rng):
    X = x.reshape(-1, 3).copy()
    for _ in range(3):
        D = np.linalg.norm(X[:, None] - X[None], axis=2)
        np.fill_diagonal(D, np.inf)
        frei = np.where(D.min(axis=1) > 1.8)[0]
        if len(frei) == 0:
            break
        geb = np.setdiff1d(np.arange(len(X)), frei)
        if len(geb) == 0:  # alle getrennt: Teilchen 0 als Anker
            geb, frei = np.array([0]), frei[frei != 0]
        c = X[geb].mean(axis=0)
        rmax = np.max(np.linalg.norm(X[geb] - c, axis=1)) if len(geb) else 0.0
        for i in frei:
            u = rng.normal(size=3)
            X[i] = c + (rmax + 0.9) * u / np.linalg.norm(u)
        X = lj_lokal(X.ravel())[0].reshape(-1, 3)
    return X.ravel()


def lj_bh(N, rng, schritte, T=0.8, schritt=0.36):
    if N == 2:
        return -1.0, 0
    R0 = 0.6 * N ** (1 / 3) + 0.4
    x0 = rng.uniform(-R0, R0, size=3 * N)
    x, e = lj_lokal(x0)
    x = lj_binden(x, rng)
    e = lj_eg(x)[0]
    eb, sb = e, 0
    for s in range(1, schritte + 1):
        y, ey = lj_lokal(x + rng.uniform(-schritt, schritt, size=x.shape))
        y = lj_binden(y, rng)
        ey = lj_eg(y)[0]
        if ey < e or rng.random() < np.exp(-(ey - e) / T):
            x, e = y, ey
        if ey < eb - 1e-9:
            eb, sb = ey, s
    return eb, sb


def s4(seed, nmin, nmax, schritte, pfad):
    rng = np.random.default_rng(seed)
    aus = {"seed": seed, "schritte": schritte, "E": {}, "erster_schritt_bestwert": {}, "sek": {}}
    for N in range(nmin, nmax + 1):
        t0 = time.time()
        e, s = lj_bh(N, rng, schritte)
        aus["E"][str(N)] = e
        aus["erster_schritt_bestwert"][str(N)] = s
        aus["sek"][str(N)] = time.time() - t0
        speichern(pfad, aus)


# ---------------------------------------------------------------- Abbildung
def bild(s3pfad, aus, s4pfade):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    t = json.load(open(s3pfad))
    D3 = {int(k): v for k, v in t["D2"].items()}
    E4 = {}
    for p in s4pfade:
        for k, v in json.load(open(p))["E"].items():
            E4[int(k)] = min(v, E4.get(int(k), np.inf))
    D4 = {N: E4[N + 1] - 2 * E4[N] + E4[N - 1] for N in sorted(E4) if N - 1 in E4 and N + 1 in E4}
    fig, ax = plt.subplots(1, 2, figsize=(11, 4))
    for a, D, titel, mark in ((ax[0], D3, "Ladungen auf der Kugel (Thomson)", (6, 8, 11, 12)),
                              (ax[1], D4, "Lennard-Jones-Cluster", (7, 8, 12, 13, 19, 20))):
        N = sorted(D)
        a.plot(N, [D[n] for n in N], "o-", color="0.3")
        for m in mark:
            if m in D:
                a.annotate(str(m), (m, D[m]), textcoords="offset points", xytext=(0, 7), ha="center", color="C3")
        a.set_title(titel)
        a.set_xlabel("Teilchenzahl N")
        a.set_ylabel("D2(N) = E(N+1) - 2E(N) + E(N-1)   (gross = stabil)")
        a.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(aus, dpi=130)


if __name__ == "__main__":
    cmd = sys.argv[1]
    t0 = time.time()
    if cmd == "s1s5":
        rng = np.random.default_rng(20261002)
        speichern(sys.argv[2], {"S1": s1(rng), "S5": s5(rng), "sek": time.time() - t0})
    elif cmd == "s3":
        s3([int(sys.argv[2]), int(sys.argv[3])], int(sys.argv[4]), sys.argv[5])
    elif cmd == "s4":
        s4(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6])
    elif cmd == "bild":
        bild(sys.argv[2], sys.argv[3], sys.argv[4:])
    else:
        raise SystemExit("unbekannt: " + cmd)
    print(cmd, "fertig", round(time.time() - t0, 1), "s")
