#!/usr/bin/env python3
# QCA-DIAMANT-4, Runde 38 (fmhc-physics). Code-Agent fuer die Leitung claude-primary.
# Baut auf RUNDE-37/qca-tetra-1/code/qca_tetra.py auf (Gruppen, exakte Defektformel, Suche), verallgemeinert auf
# s Zustaende je Knoten.
# Teil 0 (QD0): Kontrolle mit s = 2: BCC (L2:Pauli, L2:1+chi_x, T:2) und Diamant Fassung 1 (alle zwoelf 2-dim Darst.).
# Teil A (QD1, QD2): Diamantnetz, s = 4. Fassung 1: Halbschritte A -> B (+e_a) und B -> A (-e_a) je unitaer
#   (= gleichzeitiger Sprung U = ((0, X), (Y, 0))). Fassung 2: Cayley-Graph-Fassung, dieselben Matrizen auf beiden
#   Untergittern (C_a = B_a). Je Variante "frei" und "w0" (W(0) = I, Eq. 19 der Quelle).
# Teil B (QD3): BCC, s = 4, volle Tetraedergruppe T, Varianten frei und w0.
# Start nur auf der .69 ueber kleintest.sh.
# Aufruf: qca_diamant.py --teil 0|A|B --modus rauch|haupt --out DATEI.json [--fassung 1|2] [--variante frei|w0]
#         [--faelle alle|T|L2|Kommaliste] [--starts N]
import argparse
import json
import sys
import time

import numpy as np
from scipy.optimize import least_squares, minimize

I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = [SX, SY, SZ]
TV = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]], dtype=int)  # t_a; h = t/sqrt3, e_a = t_a/sqrt3
SQ3 = np.sqrt(3.0)
OMEGA = np.exp(2j * np.pi / 3)
C2X = np.diag([1, -1, -1])
C2Y = np.diag([-1, 1, -1])
C2Z = np.diag([-1, -1, 1])
R3 = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])  # e_x -> e_y -> e_z, 120 Grad um (1,1,1)
S_BCC = np.concatenate([TV, -TV])
FCC_GENS = TV[1:] - TV[0]
CHI_V4 = {"1": [1, 1, 1, 1], "x": [1, 1, -1, -1], "y": [1, -1, 1, -1], "z": [1, -1, -1, 1]}
PAULI_V4 = [I2, 1j * SX, 1j * SY, 1j * SZ]


def key3(M):
    return tuple(int(x) for x in np.asarray(M).ravel())


# ---------------------------------------------------------------- Gruppen (aus qca_tetra.py)
def closure_T():
    gens = [(C2X, -1j * SX, 0), (R3, 0.5 * (I2 - 1j * (SX + SY + SZ)), 1)]
    start = (np.eye(3, dtype=int), I2.copy(), 0)
    elems = {key3(start[0]): start}
    order = [key3(start[0])]
    frontier = [start]
    fehler = 0
    while frontier:
        new = []
        for (M, U, n) in frontier:
            for (G, V, m) in gens:
                P, W, q = G @ M, V @ U, (m + n) % 3
                k = key3(P)
                if k in elems:
                    P0, U0, n0 = elems[k]
                    if not (np.allclose(W, U0, atol=1e-12) or np.allclose(W, -U0, atol=1e-12)):
                        fehler += 1
                    if n0 != q:
                        fehler += 1
                else:
                    elems[k] = (P, W, q)
                    order.append(k)
                    new.append((P, W, q))
        frontier = new
    return [elems[k] for k in order], fehler


def su2_closure(gensU):
    els = [I2.copy()]
    frontier = [I2.copy()]
    while frontier and len(els) < 200:
        new = []
        for U in frontier:
            for V in gensU:
                W = V @ U
                if not any(np.allclose(W, X, atol=1e-10) for X in els):
                    els.append(W)
                    new.append(W)
        frontier = new
    return els


def adjoint_dev(R, U):
    dev = 0.0
    for j in range(3):
        lhs = U @ PAULI[j] @ U.conj().T
        rhs = sum(R[i, j] * PAULI[i] for i in range(3))
        dev = max(dev, float(np.abs(lhs - rhs).max()))
    return dev


def bdiag(*blocks):
    n = sum(b.shape[0] for b in blocks)
    M = np.zeros((n, n), dtype=complex)
    i = 0
    for b in blocks:
        k = b.shape[0]
        M[i:i + k, i:i + k] = b
        i += k
    return M


def gruppen(s):
    T, fehler = closure_T()
    rots = {"T": [e[0] for e in T], "L2": [np.eye(3, dtype=int), C2X, C2Y, C2Z]}
    info = {"T_ordnung": len(T), "T_konsistenzfehler": fehler, "L2_ordnung": 4}
    su2 = su2_closure([-1j * SX, 0.5 * (I2 - 1j * (SX + SY + SZ))])
    info["2T_ordnung"] = len(su2)
    kern = [U for U in su2 if adjoint_dev(np.eye(3, dtype=int), U) < 1e-10]
    info["2T_kern_ist_pm_I"] = bool(len(kern) == 2 and all(min(np.abs(U - I2).max(), np.abs(U + I2).max()) < 1e-12 for U in kern))
    info["spinor_SO3_abw"] = max(adjoint_dev(R, U) for (R, U, _) in T)
    U_R = 0.5 * (I2 - 1j * (SX + SY + SZ))
    info["V_C3_hoch3_plus_I"] = float(np.abs(np.linalg.matrix_power(U_R, 3) + I2).max())
    reps = {}
    if s == 2:
        reps["T:1+1"] = ("T", "linear", [I2.copy() for _ in T])
        reps["T:1+1'"] = ("T", "linear", [np.diag([1, OMEGA ** n]).astype(complex) for (_, _, n) in T])
        reps["T:1+1''"] = ("T", "linear", [np.diag([1, OMEGA ** (2 * n)]).astype(complex) for (_, _, n) in T])
        reps["T:1'+1''"] = ("T", "linear", [np.diag([OMEGA ** n, OMEGA ** (2 * n)]).astype(complex) for (_, _, n) in T])
        reps["T:2"] = ("T", "projektiv", [U.copy() for (_, U, _) in T])
        reps["T:2'"] = ("T", "projektiv", [OMEGA ** n * U for (_, U, n) in T])
        reps["T:2''"] = ("T", "projektiv", [OMEGA ** (2 * n) * U for (_, U, n) in T])
        reps["L2:Pauli"] = ("L2", "projektiv", [M.copy() for M in PAULI_V4])
        reps["L2:1+1"] = ("L2", "linear", [I2.copy() for _ in range(4)])
        for c in "xyz":
            reps["L2:1+chi_" + c] = ("L2", "linear", [np.diag([1, CHI_V4[c][i]]).astype(complex) for i in range(4)])
    else:
        einsdim = {"1+1+1+1": [0, 0, 0, 0], "1+1+1+1'": [0, 0, 0, 1], "1+1+1+1''": [0, 0, 0, 2],
                   "1+1+1'+1'": [0, 0, 1, 1], "1+1+1'+1''": [0, 0, 1, 2]}
        for nm, ms in einsdim.items():
            reps["T:" + nm] = ("T", "linear", [np.diag([OMEGA ** (m * n) for m in ms]).astype(complex) for (_, _, n) in T])
        reps["T:1+3"] = ("T", "linear", [bdiag(np.eye(1, dtype=complex), R.astype(complex)) for (R, _, _) in T])
        reps["T:1'+3"] = ("T", "linear", [bdiag(np.array([[OMEGA ** n]]), R.astype(complex)) for (R, _, n) in T])
        reps["T:2+2"] = ("T", "projektiv", [bdiag(U, U) for (_, U, _) in T])
        reps["T:2+2'"] = ("T", "projektiv", [bdiag(U, OMEGA ** n * U) for (_, U, n) in T])
        reps["T:2+2''"] = ("T", "projektiv", [bdiag(U, OMEGA ** (2 * n) * U) for (_, U, n) in T])
        v4lin = {"1+1+1+1": "1111", "1+1+1+x": "111x", "1+1+x+x": "11xx", "1+1+x+y": "11xy", "1+1+y+z": "11yz",
                 "1+1+x+z": "11xz", "1+x+y+z": "1xyz"}
        for nm, code in v4lin.items():
            reps["L2:" + nm] = ("L2", "linear", [np.diag([CHI_V4[c][i] for c in code]).astype(complex) for i in range(4)])
        reps["L2:P+P"] = ("L2", "projektiv", [bdiag(M, M) for M in PAULI_V4])
    rinfo = {}
    Is = np.eye(s)
    for name, (grp, art, Vs) in reps.items():
        R = rots[grp]
        idx = {key3(M): i for i, M in enumerate(R)}
        maxdev, maxlin, unit = 0.0, 0.0, 0.0
        for i, A in enumerate(R):
            unit = max(unit, float(np.abs(Vs[i].conj().T @ Vs[i] - Is).max()))
            for j, B in enumerate(R):
                k = idx[key3(A @ B)]
                prod = Vs[i] @ Vs[j]
                c = np.trace(Vs[k].conj().T @ prod) / s
                maxdev = max(maxdev, float(np.abs(prod - c * Vs[k]).max()))
                maxlin = max(maxlin, float(abs(c - 1)))
        ix, iy = idx[key3(C2X)], idx[key3(C2Y)]
        K = Vs[ix] @ Vs[iy] @ Vs[ix].conj().T @ Vs[iy].conj().T
        kl = "-I" if np.abs(K + Is).max() < 1e-12 else ("+I" if np.abs(K - Is).max() < 1e-12 else "anders")
        kern = sum(1 for V in Vs if np.abs(V - V[0, 0] * Is).max() < 1e-12)
        rinfo[name] = {"gruppe": grp, "art": art, "projektiv_abw": maxdev, "linear_abw": maxlin, "unitaer_abw": unit,
                       "kommutator_C2x_C2y": kl, "konjugationskern": int(kern)}
    return rots, reps, info, rinfo


def perm_on(vectors, R):
    keys = {tuple(int(x) for x in v): i for i, v in enumerate(vectors)}
    p = []
    for v in vectors:
        w = tuple(int(x) for x in R @ v)
        if w not in keys:
            return None
        p.append(keys[w])
    return p


def covariant_basis(nslots, perms, Vs, s):
    dim = nslots * s * s
    P = np.zeros((dim, dim), dtype=complex)
    Eb = np.eye(dim, dtype=complex).reshape(dim, nslots, s, s)
    for p, V in zip(perms, Vs):
        B = np.einsum("ij,cnjk,lk->cnil", V, Eb, V.conj())
        Bp = np.zeros_like(B)
        Bp[:, p, :, :] = B
        P += Bp.reshape(dim, dim).T
    P /= len(perms)
    proj_err = float(np.abs(P @ P - P).max())
    Ph = (P + P.conj().T) / 2
    w, vecs = np.linalg.eigh(Ph)
    sel = w > 0.5
    E = vecs[:, sel].T.reshape(-1, nslots, s, s)
    return E, proj_err


# ---------------------------------------------------------------- Unitaritaet (exakte Koeffizienten)
class Unit:
    """W(u) = sum_f e^{i u.f} A_f; Koeffizienten von W^dagger W - I (exakt)."""

    def __init__(self, freqs, s):
        self.s = s
        self.freqs = np.asarray(freqs, dtype=int)
        nf = len(self.freqs)
        keys = {}
        ii, jj, kk = [], [], []
        for i in range(nf):
            for j in range(nf):
                d = tuple(int(x) for x in self.freqs[i] - self.freqs[j])
                if d not in keys:
                    keys[d] = len(keys)
                ii.append(i)
                jj.append(j)
                kk.append(keys[d])
        self.ii = np.array(ii)
        self.jj = np.array(jj)
        self.nk = len(keys)
        self.k0 = keys[(0, 0, 0)]
        self.M = np.zeros((self.nk, len(ii)))
        self.M[kk, np.arange(len(ii))] = 1.0
        self.target = np.zeros((self.nk, s * s), dtype=complex)
        self.target[self.k0] = np.eye(s).ravel()

    def coeffs(self, A):
        Q = np.einsum("pji,pjk->pik", A[self.jj].conj(), A[self.ii])
        return self.M @ Q.reshape(-1, self.s * self.s) - self.target

    def defect(self, A):
        return float(np.sum(np.abs(self.coeffs(A)) ** 2))

    def resid(self, A):
        C = self.coeffs(A)
        return np.concatenate([C.real.ravel(), C.imag.ravel()])

    def jac(self, A, dA):
        F = np.einsum("mpji,pjk->mpik", dA[:, self.jj].conj(), A[self.ii])
        G = np.einsum("pji,mpjk->mpik", A[self.jj].conj(), dA[:, self.ii])
        dQ = (F + G).reshape(dA.shape[0], -1, self.s * self.s)
        dC = np.einsum("kp,mpq->mkq", self.M, dQ)
        return np.concatenate([dC.real.reshape(dA.shape[0], -1), dC.imag.reshape(dA.shape[0], -1)], axis=1).T


class Composite:
    """Diamant: W(u) = X^(u) Y^(u) = sum_{a,b} e^{iu.(t_b - t_a)} C_b B_a (Zweischritt auf dem A-Untergitter)."""

    def __init__(self, s):
        self.s = s
        fr = {}
        pa, pb, pk = [], [], []
        for a in range(4):
            for b in range(4):
                d = tuple(int(x) for x in TV[b] - TV[a])
                if d not in fr:
                    fr[d] = len(fr)
                pa.append(a)
                pb.append(b)
                pk.append(fr[d])
        self.freqs = np.array(list(fr.keys()), dtype=int)
        self.pa = np.array(pa)
        self.pb = np.array(pb)
        self.Mc = np.zeros((len(fr), 16))
        self.Mc[pk, np.arange(16)] = 1.0

    def A_of(self, B, C):
        Pm = np.einsum("pij,pjk->pik", C[self.pb], B[self.pa])
        return (self.Mc @ Pm.reshape(16, -1)).reshape(-1, self.s, self.s)


class Problem:
    """art: 'bcc' (A_h, 8 Richtungen), 'd1' (Diamant Fassung 1: B_a, C_a frei), 'cayley' (Fassung 2: C_a = B_a)."""

    def __init__(self, art, E, s, w0):
        self.art, self.E, self.m, self.s, self.w0 = art, E, E.shape[0], s, w0
        if art == "bcc":
            self.units = [Unit(S_BCC, s)]
            self.nb = 1
        elif art == "d1":
            self.units = [Unit(-TV, s), Unit(TV, s)]
            self.nb = 2
        else:
            self.units = [Unit(-TV, s)]
            self.nb = 1
        m = self.m
        self.npar = 2 * m * self.nb
        self.dM = []
        for k in range(self.nb):
            d = np.zeros((self.npar,) + E.shape[1:], dtype=complex)
            d[2 * m * k:2 * m * k + m] = E
            d[2 * m * k + m:2 * m * (k + 1)] = 1j * E
            self.dM.append(d)

    def blocks(self, x):
        m = self.m
        return [np.tensordot(x[2 * m * k:2 * m * k + m] + 1j * x[2 * m * k + m:2 * m * (k + 1)], self.E, axes=1)
                for k in range(self.nb)]

    def BC(self, bl):
        if self.art == "d1":
            return bl[0], bl[1]
        return bl[0], bl[0]

    def resid(self, x):
        bl = self.blocks(x)
        r = [u.resid(b) for u, b in zip(self.units, bl)]
        if self.w0:
            if self.art == "bcc":
                R0 = bl[0].sum(0) - np.eye(self.s)
            else:
                B, C = self.BC(bl)
                R0 = C.sum(0) @ B.sum(0) - np.eye(self.s)
            r.append(np.concatenate([R0.real.ravel(), R0.imag.ravel()]))
        return np.concatenate(r)

    def jac(self, x):
        bl = self.blocks(x)
        J = [u.jac(b, d) for u, b, d in zip(self.units, bl, self.dM)]
        if self.w0:
            if self.art == "bcc":
                dR = self.dM[0].sum(1)
            else:
                B, C = self.BC(bl)
                dB = self.dM[0]
                dC = self.dM[1] if self.art == "d1" else self.dM[0]
                dR = np.einsum("pij,jk->pik", dC.sum(1), B.sum(0)) + np.einsum("ij,pjk->pik", C.sum(0), dB.sum(1))
            J.append(np.concatenate([dR.real.reshape(self.npar, -1), dR.imag.reshape(self.npar, -1)], axis=1).T)
        return np.concatenate(J, axis=0)

    def defect(self, x):
        r = self.resid(x)
        return float(r @ r)

    def walk(self, x, comp):
        """(freqs, Koeffizienten) des Schritts W (BCC) bzw. Zweischritts W = X^ Y^ (Diamant); dazu die Bloecke."""
        bl = self.blocks(x)
        if self.art == "bcc":
            return S_BCC, bl[0], [bl[0]]
        B, C = self.BC(bl)
        return comp.freqs, comp.A_of(B, C), ([B, C] if self.art == "d1" else [B])


def search(prob, nstarts, seed, maxnfev=400):
    rng = np.random.default_rng(seed)
    out = []
    m, s = prob.m, prob.s
    for _ in range(nstarts):
        xs = []
        for _k in range(prob.nb):
            t0 = rng.standard_normal(m) + 1j * rng.standard_normal(m)
            t0 *= np.sqrt(s) / np.linalg.norm(t0)
            xs += [t0.real, t0.imag]
        x0 = np.concatenate(xs)
        try:
            sol = least_squares(prob.resid, x0, jac=prob.jac, method="lm", xtol=1e-15, ftol=1e-15, gtol=1e-15,
                                max_nfev=maxnfev)
            x, nfev = sol.x, int(sol.nfev)
        except Exception:
            x, nfev = x0, -1
        out.append((prob.defect(x), x, nfev))
    return out


# ---------------------------------------------------------------- Spektrum, Kegel, Verdoppler
def W_at(freqs, A, u):
    s = A.shape[-1]
    ph = np.exp(1j * (np.atleast_2d(u) @ np.asarray(freqs).T))
    return (ph @ A.reshape(len(freqs), s * s)).reshape(-1, s, s)


def fib_dirs(n):
    i = np.arange(n) + 0.5
    phi = np.arccos(1 - 2 * i / n)
    th = np.pi * (1 + 5 ** 0.5) * i
    return np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi), np.cos(phi)], -1)


LAT26 = np.array([[i, j, k] for i in (-1, 0, 1) for j in (-1, 0, 1) for k in (-1, 0, 1) if (i, j, k) != (0, 0, 0)], float)
LAT26 /= np.linalg.norm(LAT26, axis=1)[:, None]
DIRS126 = np.concatenate([LAT26, fib_dirs(100)])
FIB400 = fib_dirs(400)


def grid_u(N, period=2 * np.pi):
    g = period * np.arange(N) / N
    return np.stack(np.meshgrid(g, g, g, indexing="ij"), -1).reshape(-1, 3)


def clusters_at(W0, tol=1e-7):
    ph = np.angle(np.linalg.eigvals(W0))
    s = len(ph)
    lab = list(range(s))

    def find(i):
        while lab[i] != i:
            i = lab[i]
        return i

    for i in range(s):
        for j in range(i + 1, s):
            if abs(np.angle(np.exp(1j * (ph[i] - ph[j])))) < tol:
                lab[find(i)] = find(j)
    groups = {}
    for i in range(s):
        groups.setdefault(find(i), []).append(i)
    out = [(float(np.angle(np.mean(np.exp(1j * ph[g])))), len(g)) for g in groups.values() if len(g) >= 2]
    return out, ph


def cluster_branches(freqs, A, u_pts, phc, m):
    rel = np.angle(np.linalg.eigvals(W_at(freqs, A, u_pts)) * np.exp(-1j * phc))
    idx = np.argsort(np.abs(rel), axis=1)[:, :m]
    return np.sort(np.take_along_axis(rel, idx, axis=1), axis=1)


def cone_test(freqs, A, u0, phc, m, eps_k=1e-5, dirs=DIRS126):
    e = eps_k / SQ3
    b1 = cluster_branches(freqs, A, u0[None, :] + e * dirs, phc, m)
    b2 = cluster_branches(freqs, A, u0[None, :] + 2 * e * dirs, phc, m)
    sp1 = b1[:, -1] - b1[:, 0]
    sp2 = b2[:, -1] - b2[:, 0]
    slope = sp1 / (2 * eps_k)
    ratio = sp2 / np.maximum(sp1, 1e-300)
    ok = bool(slope.min() > 1e-3 and ratio.min() > 1.9 and ratio.max() < 2.1)
    br = (b1 - b1.mean(1, keepdims=True)) / eps_k
    flach = np.sum(np.abs(br) < 1e-3, axis=1)
    return {"kegel": ok, "v_min": float(slope.min()), "v_max": float(slope.max()), "ratio_min": float(ratio.min()),
            "ratio_max": float(ratio.max()), "flache_zweige_min": int(flach.min()), "flache_zweige_max": int(flach.max()),
            "zweige_bsp": [round(float(v), 6) for v in br[0]]}


def rel_spectrum_span(freqs, A, N=12):
    ph = np.sort(np.angle(np.linalg.eigvals(W_at(freqs, A, grid_u(N)))), axis=1)
    gaps = np.sort(np.diff(np.concatenate([ph, ph[:, :1] + 2 * np.pi], axis=1), axis=1), axis=1)
    return float((gaps.max(0) - gaps.min(0)).max())


def kommutierend(freqs, A, n=6):
    # max ||[W(u), W(u')]|| ueber n feste Zufallspaare; ~0 heisst: alle W(k) gleichzeitig diagonalisierbar, also
    # direkte Summe von Ein-Zustands-Verschiebungen (trivial, PLAN.md Abschnitt 7)
    U = np.random.default_rng(12345).uniform(0, 2 * np.pi, size=(2 * n, 3))
    W = W_at(freqs, A, U)
    return float(max(np.abs(W[2 * i] @ W[2 * i + 1] - W[2 * i + 1] @ W[2 * i]).max() for i in range(n)))


def erste_ordnung(freqs, A, u0, phc, m, eps_k=1e-4):
    # G_j = Q^† (W(u0)^† W(u0 + eps e_j) - I) Q / (-i eps) auf dem Clusterraum Q; relative Kommutatornorm der G_j.
    # ~0: die Zweige kreuzen nur (entkoppelt); O(1): echte Kopplung (Weyl, Dirac, Mehrfachpunkt).
    W0 = W_at(freqs, A, u0[None, :])[0]
    lam, vec = np.linalg.eig(W0)
    idx = np.argsort(np.abs(np.angle(lam * np.exp(-1j * phc))))[:m]
    Q, _ = np.linalg.qr(vec[:, idx])
    G = []
    for j in range(3):
        e = np.zeros(3)
        e[j] = eps_k / SQ3
        W1 = W_at(freqs, A, (u0 + e)[None, :])[0]
        G.append(Q.conj().T @ (W0.conj().T @ W1 - np.eye(len(W0))) @ Q / (-1j * eps_k))
    nG = max(float(np.abs(g).max()) for g in G)
    kom = max(float(np.abs(G[i] @ G[j] - G[j] @ G[i]).max()) for i in range(3) for j in range(i + 1, 3))
    chir = None
    if m == 2:
        Mv = np.array([[float(np.real(np.trace(G[i] @ PAULI[j]))) / 2 for j in range(3)] for i in range(3)])
        chir = float(np.linalg.det(Mv))
    return kom / max(nG ** 2, 1e-300), chir


def klassifiziere(freqs, A):
    res = {}
    span = rel_spectrum_span(freqs, A)
    kom = kommutierend(freqs, A)
    res["rel_spektrum_spannweite"] = span
    res["kommutator_W"] = kom
    triv_alt = span < 1e-8
    triv = triv_alt or kom < 1e-8
    res["trivial_alt"] = bool(triv_alt)
    W0 = W_at(freqs, A, np.zeros((1, 3)))[0]
    cl, ph0 = clusters_at(W0)
    res["W0_eigenphasen"] = sorted(round(float(p), 9) for p in ph0)
    res["cluster0"] = []
    kegel, kegel_alt = False, False
    for (c, m) in cl:
        ct = cone_test(freqs, A, np.zeros(3), c, m)
        ct["kom_rel"], ct["chiral_det"] = erste_ordnung(freqs, A, np.zeros(3), c, m)
        ct["kegel_alt"] = ct["kegel"]
        ct["kegel"] = bool(ct["kegel_alt"] and ct["kom_rel"] > 1e-2)
        res["cluster0"].append({"phase": c, "m": int(m), **ct})
        kegel = kegel or ct["kegel"]
        kegel_alt = kegel_alt or ct["kegel_alt"]
    res["kegel_0_alt"] = bool(kegel_alt and not triv_alt)
    res["kegel_0"] = bool(kegel and not triv)
    if triv:
        res["klasse"] = "trivial"
    else:
        res["klasse"] = "Kegel bei 0" if kegel else ("Entartung bei 0 ohne Kegel" if cl else "keine Entartung bei 0")
    return res


def isotropie(freqs, A, phc, m, kabs):
    b = cluster_branches(freqs, A, kabs * FIB400 / SQ3, phc, m)
    v = (b[:, -1] - b[:, 0]) / (2 * kabs)
    return {"v_mittel": float(v.mean()), "std_rel": float(v.std() / v.mean()), "spannweite_rel": float((v.max() - v.min()) / v.mean())}


def min_gap(W):
    ph = np.sort(np.angle(np.linalg.eigvals(W)), axis=-1)
    return np.diff(np.concatenate([ph, ph[..., :1] + 2 * np.pi], axis=-1), axis=-1).min(-1)


def entartungssuche(freqs, A, equiv, special_u, N=16, nmax=16):
    U = grid_u(N)
    g = min_gap(W_at(freqs, A, U)).reshape(N, N, N)
    loc = np.ones_like(g, dtype=bool)
    for ax in range(3):
        for sh in (1, -1):
            loc &= g <= np.roll(g, sh, axis=ax)
    cand = sorted(np.argwhere(loc).tolist(), key=lambda c: g[tuple(c)])[:nmax]
    starts = [2 * np.pi * np.array(c, float) / N for c in cand] + [np.array(u, float) for u in special_u]

    def f(u):
        return float(min_gap(W_at(freqs, A, u[None, :]))[0])

    simplex0 = 0.3 * np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]], float)
    pts = []
    for u0 in starts:
        try:
            sol = minimize(f, u0, method="Nelder-Mead",
                           options={"xatol": 1e-12, "fatol": 1e-14, "maxiter": 500, "initial_simplex": u0 + simplex0})
            u1 = sol.x
        except Exception:
            continue
        if f(u1) < 1e-6:
            ph = np.exp(1j * (np.asarray(equiv, float) @ u1))
            if not any(np.abs(ph - q).max() < 1e-4 for (q, _) in pts):
                pts.append((ph, u1))
    out = []
    for ph, u1 in pts:
        W1 = W_at(freqs, A, u1[None, :])[0]
        cl, _ = clusters_at(W1, tol=1e-5)
        kegel, kegel_alt, info = False, False, []
        for (c, m) in cl:
            ct = cone_test(freqs, A, u1, c, m, eps_k=1e-4)
            ct["kom_rel"], ct["chiral_det"] = erste_ordnung(freqs, A, u1, c, m)
            ct["kegel_alt"] = ct["kegel"]
            ct["kegel"] = bool(ct["kegel_alt"] and ct["kom_rel"] > 1e-2)
            info.append({"phase": c, "m": int(m), **ct})
            kegel = kegel or ct["kegel"]
            kegel_alt = kegel_alt or ct["kegel_alt"]
        out.append({"u": [round(float(x), 6) for x in u1], "k": [round(float(x), 6) for x in SQ3 * u1],
                    "gamma_aequivalent": bool(np.abs(ph - 1).max() < 1e-4), "luecke": f(u1), "kegel": kegel,
                    "kegel_alt": kegel_alt, "cluster": info})
    return out


def polieren(prob, x, n=30):
    # Gauss-Newton mit lstsq ab einem Treffer (Diagnose: echte Loesung oder nur Beinahe-Loesung?)
    best_D, best_x = prob.defect(x), x.copy()
    for _ in range(n):
        r = prob.resid(x)
        J = prob.jac(x)
        dx = np.linalg.lstsq(J, -r, rcond=1e-12)[0]
        x = x + dx
        D = prob.defect(x)
        if D < best_D:
            best_D, best_x = D, x.copy()
        if best_D < 1e-29:
            break
    return best_D, best_x


def implementing(blocks, perm, s):
    rows = []
    Is = np.eye(s)
    for Bk in blocks:
        for i in range(len(Bk)):
            rows.append(np.kron(Bk[i].T, Is) - np.kron(Is, Bk[perm[i]]))
    _, sv, vh = np.linalg.svd(np.concatenate(rows))
    U = vh.conj()[-1].reshape(s, s, order="F")
    U = U / np.sqrt(np.trace(U.conj().T @ U).real / s)
    return float(sv[-1]), float(sv[-2]), int(np.sum(sv < 1e-8)), U


def dreihundertsechzig(blocks, slotvecs, s):
    out = {}
    Us = {}
    for lab, R in (("C2x", C2X), ("C2y", C2Y), ("C3", R3)):
        p = perm_on(slotvecs, R)
        smin, s2, nnull, U = implementing(blocks, p, s)
        out[lab] = {"s_min": smin, "s_2": s2, "nullraum": nnull,
                    "unitaer_abw": float(np.abs(U.conj().T @ U - np.eye(s)).max())}
        Us[lab] = U
    K = Us["C2x"] @ Us["C2y"] @ Us["C2x"].conj().T @ Us["C2y"].conj().T
    out["K_plus_I"] = float(np.abs(K + np.eye(s)).max())
    out["K_minus_I"] = float(np.abs(K - np.eye(s)).max())
    eind = all(out[l]["s_min"] <= 1e-8 and out[l]["s_2"] >= 1e-4 for l in ("C2x", "C2y"))
    if eind and out["K_plus_I"] <= 1e-8:
        out["wirkung"] = "projektiv"
    elif eind and out["K_minus_I"] <= 1e-8:
        out["wirkung"] = "linear"
    else:
        out["wirkung"] = "mehrdeutig"
    out["C3_implementierbar"] = bool(out["C3"]["s_min"] <= 1e-8)
    return out


def cplx(a):
    a = np.asarray(a)
    return {"re": a.real.round(15).tolist(), "im": a.imag.round(15).tolist()}


# ---------------------------------------------------------------- Pfade (u = k/sqrt3)
G_FCC = 2 * np.pi / (4 / SQ3)
PFAD_FCC = [("Γ", np.zeros(3)), ("X", G_FCC * np.array([1.0, 0, 0])), ("W", G_FCC * np.array([1.0, 0.5, 0])),
            ("L", G_FCC * np.array([0.5, 0.5, 0.5])), ("Γ", np.zeros(3)), ("K", G_FCC * np.array([0.75, 0.75, 0]))]
PFAD_BCC = [("Γ", np.zeros(3)), ("H", SQ3 * np.pi * np.array([1.0, 0, 0])), ("N", SQ3 * np.pi * np.array([0.5, 0.5, 0])),
            ("Γ", np.zeros(3)), ("P", SQ3 * np.pi * np.array([0.5, 0.5, 0.5])), ("H", SQ3 * np.pi * np.array([1.0, 0, 0]))]
SPECIAL_U = {"fcc": [p / SQ3 for (_, p) in PFAD_FCC[1:4]] + [PFAD_FCC[5][1] / SQ3],
             "bcc": [PFAD_BCC[1][1] / SQ3, PFAD_BCC[2][1] / SQ3, PFAD_BCC[4][1] / SQ3, -PFAD_BCC[4][1] / SQ3]}


# ---------------------------------------------------------------- ein Fall
def fall(name, grp, art_rep, Vs, rots, s, art, w0, nstarts, seed, comp, nrep_ent=3):
    t0 = time.time()
    if art == "bcc":
        slotvecs, nslots, equiv, special = S_BCC, 8, TV, SPECIAL_U["bcc"]
    else:
        slotvecs, nslots, equiv, special = TV, 4, FCC_GENS, SPECIAL_U["fcc"]
    perms = [perm_on(slotvecs, R) for R in rots[grp]]
    E, perr = covariant_basis(nslots, perms, Vs, s)
    st = {"gruppe": grp, "art": art_rep, "dim_komplex_je_block": int(E.shape[0]), "projektor_abw": perr,
          "starts": nstarts, "treffer": 0, "hits": [], "repr": None}
    if E.shape[0] == 0:
        st.update({"D_min": None, "D_median": None, "leer": True, "laufzeit_s": time.time() - t0})
        return st
    prob = Problem(art, E, s, w0)
    res = search(prob, nstarts, seed)
    D = np.array([r[0] for r in res])
    nfev = np.array([r[2] for r in res])
    st.update({"D_min": float(D.min()), "D_median": float(np.median(D)), "D_max": float(D.max()),
               "treffer": int(np.sum(D < 1e-10)), "nfev_median": float(np.median(nfev)), "nfev_max": int(nfev.max()),
               "log10D_alle": np.log10(np.maximum(D, 1e-40)).round(3).tolist()})
    n_ent = 0
    for (Dv, x, _) in res:
        if Dv >= 1e-10:
            continue
        D_pol = None
        if Dv > 1e-26:
            D_pol, x_pol = polieren(prob, x)
            if D_pol < Dv:
                x = x_pol
        freqs, Ac, blocks = prob.walk(x, comp)
        cl = klassifiziere(freqs, Ac)
        h = {"D": Dv, "D_poliert": D_pol, "klasse": cl["klasse"], "kegel_0": cl["kegel_0"], "klass": cl}
        if art == "bcc":
            h["gewicht_S+_S-"] = [float(np.sum(np.abs(Ac[:4]) ** 2)), float(np.sum(np.abs(Ac[4:]) ** 2))]
        if cl["klasse"] != "trivial":
            h["dreihundertsechzig"] = dreihundertsechzig(blocks, slotvecs, s)
        if cl["kegel_0"]:
            big = max(cl["cluster0"], key=lambda q: q["m"] if q["kegel"] else -1)
            h["isotropie_1e-5"] = isotropie(freqs, Ac, big["phase"], big["m"], 1e-5)
            h["isotropie_0.05"] = isotropie(freqs, Ac, big["phase"], big["m"], 0.05)
        if n_ent < nrep_ent and cl["klasse"] != "trivial":
            h["entartungen"] = entartungssuche(freqs, Ac, equiv, special)
            n_ent += 1
        st["hits"].append(h)
        if st["repr"] is None or (cl["kegel_0"] and not st["repr"]["kegel_0"]):
            st["repr"] = {"kegel_0": cl["kegel_0"], "freqs": np.asarray(freqs).tolist(), "A": cplx(Ac)}
    st["kegel_0"] = sum(1 for h in st["hits"] if h["kegel_0"])
    st["trivial"] = sum(1 for h in st["hits"] if h["klasse"] == "trivial")
    st["laufzeit_s"] = time.time() - t0
    return st


def codepruefung(rng, s, comp):
    chk = []
    uS = Unit(S_BCC, s)
    Ug = grid_u(12)
    for _ in range(2):
        A = rng.standard_normal((8, s, s)) + 1j * rng.standard_normal((8, s, s))
        Wg = W_at(S_BCC, A, Ug)
        dev = np.einsum("nji,njk->nik", Wg.conj(), Wg) - np.eye(s)
        chk.append(abs(float(np.mean(np.sum(np.abs(dev) ** 2, axis=(1, 2)))) - uS.defect(A)) / uS.defect(A))
    cu = Unit(comp.freqs, s)
    Ug = grid_u(20)
    for _ in range(2):
        B = rng.standard_normal((4, s, s)) + 1j * rng.standard_normal((4, s, s))
        C = rng.standard_normal((4, s, s)) + 1j * rng.standard_normal((4, s, s))
        A = comp.A_of(B, C)
        Wg = W_at(comp.freqs, A, Ug)
        Wd = W_at(TV, C, Ug) @ W_at(-TV, B, Ug)
        dev = np.einsum("nji,njk->nik", Wg.conj(), Wg) - np.eye(s)
        chk.append(max(abs(float(np.mean(np.sum(np.abs(dev) ** 2, axis=(1, 2)))) - cu.defect(A)) / cu.defect(A),
                       float(np.abs(Wg - Wd).max())))
    return float(max(chk))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--teil", choices=["0", "A", "B"], required=True)
    ap.add_argument("--modus", choices=["rauch", "haupt"], required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--fassung", choices=["1", "2"], default="1")
    ap.add_argument("--variante", choices=["frei", "w0"], default="frei")
    ap.add_argument("--faelle", default="alle")
    ap.add_argument("--starts", type=int, default=None)
    args = ap.parse_args()
    t_start = time.time()
    nstarts = args.starts if args.starts else (10 if args.modus == "rauch" else 100)
    seedbase = 3800 if args.modus == "rauch" else 38
    rng = np.random.default_rng(seedbase)
    s = 2 if args.teil == "0" else 4
    rots, reps, ginfo, rinfo = gruppen(s)
    perms_ok = all(perm_on(S_BCC, R) is not None and perm_on(TV, R) is not None for g in rots for R in rots[g])
    ginfo["wirkung_auf_S_ok"] = perms_ok
    comp = Composite(s)
    res = {"modus": args.modus, "teil": args.teil, "s": s, "starts_je_fall": nstarts, "saat_basis": seedbase,
           "fassung": args.fassung, "variante": args.variante, "faelle_arg": args.faelle,
           "gruppen": ginfo, "darstellungen": rinfo, "numpy": np.__version__,
           "defekt_codepruefung_rel": codepruefung(rng, s, comp)}
    names = list(reps.keys())
    if args.faelle in ("T", "L2"):
        wahl = [n for n in names if n.startswith(args.faelle + ":")]
    elif args.faelle == "alle":
        wahl = names
    elif args.faelle.startswith("idx:"):
        wahl = [names[int(i)] for i in args.faelle[4:].split(",")]
    else:
        wahl = args.faelle.split(",")
    faelle = {}
    if args.teil == "0":
        auftraege = [("bcc", n) for n in ("L2:Pauli", "L2:1+chi_x", "T:2")] + [("d1", n) for n in names]
        w0 = False
    elif args.teil == "A":
        art = "d1" if args.fassung == "1" else "cayley"
        auftraege = [(art, n) for n in names if n in wahl]
        w0 = args.variante == "w0"
    else:
        auftraege = [("bcc", n) for n in names if n.startswith("T:") and n in wahl]
        w0 = args.variante == "w0"
    for (art, name) in auftraege:
        grp, art_rep, Vs = reps[name]
        ci = names.index(name)
        seed = seedbase * 10000 + {"bcc": 1000, "d1": 2000, "cayley": 3000}[art] + 100 * int(w0) + ci
        st = fall(name, grp, art_rep, Vs, rots, s, art, w0, nstarts, seed, comp)
        st["geometrie"] = art
        faelle[art + "|" + name] = st
        print(f"[{args.teil}] {art} {'w0' if w0 else 'frei'} {name}: dim={st['dim_komplex_je_block']} "
              f"treffer={st['treffer']} kegel0={st.get('kegel_0', 0)} Dmin={st['D_min']} t={st['laufzeit_s']:.1f}s",
              flush=True)
    res["faelle"] = faelle
    res["laufzeit_s"] = time.time() - t_start
    with open(args.out, "w") as fh:
        json.dump(res, fh, indent=1, default=lambda o: o.tolist() if hasattr(o, "tolist") else str(o))
    print(f"fertig, {res['laufzeit_s']:.1f} s", flush=True)


if __name__ == "__main__":
    sys.exit(main())
