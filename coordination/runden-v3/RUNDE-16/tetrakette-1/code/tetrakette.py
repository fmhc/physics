#!/usr/bin/env python3
"""TETRAKETTE-1 (Runde 16), Leitung claude-primary, 02.10.2026. Karte: ../KARTE.md

Aufruf ueber kleintest.sh auf der .69 (stabil.py, stabil_s6.py und lj-21.json im selben Ordner):
  python tetrakette.py schnell <aus.json>                 K0, K1, K3, K4 fuer N = 4..33
  python tetrakette.py schnitte <seed> <M> <aus.json>     K2 (M zufaellige Ebenen je N)
  python tetrakette.py auswertung <schnell.json> <schnitte1.json> <schnitte2.json> <aus.json>
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import json
import sys
import time

import numpy as np
from scipy.optimize import minimize

from stabil import lj_eg
from stabil_s6 import newton, s_branch, stab

NMIN, NMAX = 4, 33


def speichern(pfad, obj):
    with open(pfad + ".tmp", "w") as f:
        json.dump(obj, f, indent=1)
    os.replace(pfad + ".tmp", pfad)


def kette(N):
    """Regulaere Tetraeder, Kante 1: v_n = Spiegelung von v_(n-4) an der Ebene durch v_(n-3), v_(n-2), v_(n-1)."""
    v = [np.array([0.0, 0, 0]), np.array([1.0, 0, 0]), np.array([0.5, np.sqrt(3) / 2, 0]),
         np.array([0.5, np.sqrt(3) / 6, np.sqrt(2.0 / 3.0)])]
    while len(v) < N:
        a, b, c, p = v[-3], v[-2], v[-1], v[-4]
        n = np.cross(b - a, c - a)
        n /= np.linalg.norm(n)
        v.append(p - 2 * np.dot(p - a, n) * n)
    return np.array(v[:N])


def kanten(N):
    return [(i, j) for i in range(N) for j in range(i + 1, min(N, i + 4))]


# ---------------------------------------------------------------- K0 Geometrie
def schraube(X):
    P, Q = X[0:4], X[1:5]
    pm, qm = P.mean(0), Q.mean(0)
    H = (P - pm).T @ (Q - qm)
    U, _, Vt = np.linalg.svd(H)
    d = np.sign(np.linalg.det(Vt.T @ U.T))
    R = Vt.T @ np.diag([1, 1, d]) @ U.T
    t = qm - R @ pm
    rest = float(np.max(np.abs((R @ P.T).T + t - Q)))
    w, V = np.linalg.eig(R)
    u = np.real(V[:, np.argmin(np.abs(w - 1))])
    u /= np.linalg.norm(u)
    theta = float(np.degrees(np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))))
    h = float(t @ u)
    p0 = np.linalg.lstsq(np.eye(3) - R, t - h * u, rcond=None)[0]
    return u, p0, theta, abs(h), rest


def k0(Xmax):
    u, p0, theta, h, rest = schraube(Xmax)
    e1 = np.cross(u, [1.0, 0, 0]) if abs(u[0]) < 0.9 else np.cross(u, [0, 1.0, 0])
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(u, e1)
    Y = Xmax - p0
    Y = Y - np.outer(Y @ u, u)
    radius = np.linalg.norm(Y, axis=1)
    phi = np.degrees(np.arctan2(Y @ e2, Y @ e1))
    aus = {"theta_grad": theta, "theta_soll": float(np.degrees(np.arccos(-2 / 3))), "steigung": h,
           "steigung_soll": 1 / np.sqrt(10), "radius_mittel": float(radius.mean()), "radius_streu": float(radius.std()),
           "radius_soll": 3 * np.sqrt(3) / 10, "schraub_rest": rest, "N": {}}
    for N in range(NMIN, NMAX + 1):
        best = {}
        for mod in (360.0, 180.0):
            g, paar = 999.0, None
            for i in range(N):
                for j in range(i + 1, N):
                    d = (phi[j] - phi[i]) % mod
                    d = min(d, mod - d)
                    if d < g - 1e-12:
                        g, paar = d, (i, j)
            best["mod%d" % mod] = {"abstand_grad": g, "k": paar[1] - paar[0]}
        aus["N"][str(N)] = best
    return aus


# ---------------------------------------------------------------- K1 Federn
def k1(N):
    X = kette(N)
    H = np.zeros((3 * N, 3 * N))
    for i, j in kanten(N):
        e = X[j] - X[i]
        e /= np.linalg.norm(e)
        B = np.outer(e, e)
        for a, b, s in ((i, i, 1), (j, j, 1), (i, j, -1), (j, i, -1)):
            H[3 * a:3 * a + 3, 3 * b:3 * b + 3] += s * B
    ev = np.linalg.eigvalsh(H)
    null = int(np.sum(ev < 1e-9))
    pos = ev[ev > 1e-9]
    return {"nullmoden": null, "omega1": float(np.sqrt(pos[0])), "omega2": float(np.sqrt(pos[1])),
            "omega_max": float(np.sqrt(ev[-1]))}


# ---------------------------------------------------------------- K3 Feldklumpen
def laplace(N, J):
    A = np.zeros((N, N))
    for i, j in kanten(N):
        A[i, j] = A[j, i] = 1
    return J * (np.diag(A.sum(1)) - A)


def fortsetzen(N, w2, site, J, schritte=200):
    phi = np.zeros(N)
    phi[site] = np.sqrt(s_branch(w2, True))
    for Jk in np.linspace(0, J, schritte + 1)[1:]:
        neu, ok = newton(laplace(N, Jk), w2, phi)
        if not ok or np.max(np.abs(neu - phi)) > 0.3:
            return None
        s = neu * neu
        if s[site] / s.sum() < 0.5:
            return None
        phi = neu
    return phi


def jmax(N, w2, site, obergrenze=1.0):
    if fortsetzen(N, w2, site, obergrenze) is not None:
        return obergrenze
    lo, hi = 0.0, obergrenze
    for _ in range(24):
        mid = 0.5 * (lo + hi)
        if fortsetzen(N, w2, site, mid) is not None:
            lo = mid
        else:
            hi = mid
    return lo


def k3(N, w2=0.8):
    aus = {}
    for rolle, site in (("mitte", N // 2), ("ende", 0)):
        jm = jmax(N, w2, site)
        e = {"J_max": jm}
        phi = fortsetzen(N, w2, site, 0.5 * jm)
        if phi is not None:
            mr, art, dQ, nneg = stab(laplace(N, 0.5 * jm), w2, phi)
            e.update(stab_halb=art, maxRe=mr, n_neg=nneg)
        aus[rolle] = e
    return aus


# ---------------------------------------------------------------- K4 Lennard-Jones
def lj_hesse(x, h):
    n = x.size
    H = np.zeros((n, n))
    for b in range(n):
        e = np.zeros(n)
        e[b] = h
        H[:, b] = (lj_eg(x + e)[1] - lj_eg(x - e)[1]) / (2 * h)
    return np.linalg.eigvalsh(0.5 * (H + H.T))


def kabsch_rmsd(A, B):
    A0, B0 = A - A.mean(0), B - B.mean(0)
    U, _, Vt = np.linalg.svd(A0.T @ B0)
    d = np.sign(np.linalg.det(Vt.T @ U.T))
    R = Vt.T @ np.diag([1, 1, d]) @ U.T
    return float(np.sqrt(np.mean(np.sum(((R @ A0.T).T - B0) ** 2, axis=1))))


def k4(N, egm):
    X0 = kette(N) * 2 ** (1 / 6)
    e0 = lj_eg(X0.ravel())[0]
    res = minimize(lj_eg, X0.ravel(), jac=True, method="L-BFGS-B", options=dict(maxiter=20000, gtol=1e-10, ftol=1e-16))
    X = res.x.reshape(N, 3)
    aus = {"E_start": e0, "E_kette": float(res.fun), "rmsd_zur_helix": kabsch_rmsd(X, X0),
           "gradnorm": float(np.max(np.abs(lj_eg(res.x)[1])))}
    for h in (1e-4, 1e-5):
        ev = lj_hesse(res.x, h)
        aus["hesse_%g" % h] = {"neg": int(np.sum(ev < -1e-6)), "null": int(np.sum(np.abs(ev) <= 1e-6)),
                               "kleinster_pos": float(ev[ev > 1e-6][0]), "kleinster": float(ev[0])}
    if str(N) in egm:
        aus["E_GM"] = egm[str(N)]
        aus["abstand_GM"] = float(res.fun - egm[str(N)])
    return aus


def schnell(pfad):
    t0 = time.time()
    egm = json.load(open("lj-21.json"))
    aus = {"K0": k0(kette(NMAX)), "N": {}}
    for N in range(NMIN, NMAX + 1):
        t1 = time.time()
        aus["N"][str(N)] = {"K1": k1(N), "K3": k3(N), "K4": k4(N, egm), "sek": time.time() - t1}
        speichern(pfad, aus)
    aus["sek"] = time.time() - t0
    speichern(pfad, aus)


# ---------------------------------------------------------------- K2 Schnitte
def schnitte(seed, M, pfad):
    rng = np.random.default_rng(seed)
    aus = {"seed": seed, "M": M, "N": {}}
    for N in range(NMIN, NMAX + 1):
        X = kette(N)
        Xc = X - X.mean(0)
        E = np.array(kanten(N))
        T = np.array([(k, k + 1, k + 2, k + 3) for k in range(N - 3)])
        F = np.array([(k + 1, k + 2, k + 3) for k in range(N - 4)]) if N >= 5 else None
        sP = sP2 = nC2 = ident = 0
        hist = {}
        Pmax = 0
        rest = M
        while rest > 0:
            m = min(50000, rest)
            rest -= m
            n = rng.normal(size=(m, 3))
            n /= np.linalg.norm(n, axis=1)[:, None]
            sg = (Xc @ n.T) > 0
            P = (sg[E[:, 0]] != sg[E[:, 1]]).sum(0)
            pos = sg[T].sum(1)
            cutT = (pos > 0) & (pos < 4)
            T3 = ((pos == 1) | (pos == 3)).sum(0)
            T4 = (pos == 2).sum(0)
            start = cutT.copy()
            if F is not None:
                pf = sg[F].sum(1)
                cutF = (pf > 0) & (pf < 3)
                start[1:] &= ~(cutT[:-1] & cutF)
            C = start.sum(0)
            ident += int(np.sum(P != T3 + 2 * T4 + 2 * C))
            sP += float(P.sum())
            sP2 += float((P.astype(float) ** 2).sum())
            nC2 += int(np.sum(C > 1))
            Pmax = max(Pmax, int(P.max()))
            for v, c in zip(*np.unique(P, return_counts=True)):
                hist[str(int(v))] = hist.get(str(int(v)), 0) + int(c)
        mP = sP / M
        aus["N"][str(N)] = {"P_mittel": mP, "P_var": sP2 / M - mP * mP, "P_C_gr_1": nC2 / M, "P_max": Pmax,
                            "identitaet_verletzt": ident, "hist": hist}
        speichern(pfad, aus)


# ---------------------------------------------------------------- Auswertung
def auffaellig(Ns, X, boden=0.0):
    Ns = np.asarray(Ns)
    X = np.asarray(X, float)
    r = {}
    for k, N in enumerate(Ns):
        idx = [i for i, M in enumerate(Ns) if abs(M - N) <= 4 and M != N]
        if len(idx) < 8:
            continue
        A = np.vander(Ns[idx] - N, 3).astype(float)
        coef = np.linalg.lstsq(A, X[idx], rcond=None)[0]
        r[int(N)] = float(X[k] - coef[-1])
    werte = np.array([v for N, v in r.items() if 8 <= N <= 29])
    sigma = 1.4826 * np.median(np.abs(werte - np.median(werte)))
    sigma = max(sigma, boden, 1e-12 * (np.max(np.abs(X)) + 1e-300))
    z = {N: v / sigma for N, v in r.items()}
    return {"sigma": sigma, "z": z, "markiert": [N for N, v in z.items() if abs(v) > 3]}


def auswertung(p_schnell, p_s1, p_s2, pfad):
    s = json.load(open(p_schnell))
    a, b = json.load(open(p_s1)), json.load(open(p_s2))
    Ns = list(range(NMIN, NMAX + 1))
    reihen = {
        "log_omega1": [np.log(s["N"][str(N)]["K1"]["omega1"]) for N in Ns],
        "P_mittel": [0.5 * (a["N"][str(N)]["P_mittel"] + b["N"][str(N)]["P_mittel"]) for N in Ns],
        "P_var": [0.5 * (a["N"][str(N)]["P_var"] + b["N"][str(N)]["P_var"]) for N in Ns],
        "P_C_gr_1": [0.5 * (a["N"][str(N)]["P_C_gr_1"] + b["N"][str(N)]["P_C_gr_1"]) for N in Ns],
        "J_max_mitte": [s["N"][str(N)]["K3"]["mitte"]["J_max"] for N in Ns],
        "E_kette_pro_N": [s["N"][str(N)]["K4"]["E_kette"] / N for N in Ns],
    }
    E = [s["N"][str(N)]["K4"]["E_kette"] for N in Ns]
    D2N = Ns[1:-1]
    D2 = [E[k + 1] + E[k - 1] - 2 * E[k] for k in range(1, len(Ns) - 1)]
    aus = {name: auffaellig(Ns, X, 1e-6 if name == "J_max_mitte" else 0.0) for name, X in reihen.items()}
    aus["D2_E_kette"] = auffaellig(D2N, D2)
    aus["D2_E_kette"]["werte"] = dict(zip(map(str, D2N), D2))
    aus["seedvergleich_P_mittel_max"] = max(abs(a["N"][str(N)]["P_mittel"] - b["N"][str(N)]["P_mittel"]) for N in Ns)
    speichern(pfad, aus)


if __name__ == "__main__":
    cmd = sys.argv[1]
    t0 = time.time()
    if cmd == "schnell":
        schnell(sys.argv[2])
    elif cmd == "schnitte":
        schnitte(int(sys.argv[2]), int(sys.argv[3]), sys.argv[4])
    elif cmd == "auswertung":
        auswertung(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    else:
        raise SystemExit("unbekannt: " + cmd)
    print(cmd, "fertig", round(time.time() - t0, 1), "s")
