#!/usr/bin/env python3
# QCA-TETRA-1, Runde 37 (fmhc-physics). Code-Agent fuer die Leitung claude-primary.
# Teil A: Weyl-Automat nach D'Ariano/Perinotti, PRA 90, 062106 (2014), arXiv:1306.1934v2, Eq. (24).
# Teil B: Suche isotroper unitaerer 2-Zustands-Automaten auf BCC (8 Richtungen), je Gruppe (L_2, L_3) und Darstellung.
# Teil C: dieselbe Frage auf dem Diamantnetz, Fassungen C-1 und C-2 (PLAN.md Abschnitt 1, Punkt 5).
# Start nur auf der .69 ueber kleintest.sh. Aufruf: qca_tetra.py --teil AB|C --modus rauch|haupt --out DATEI.json
import argparse
import json
import sys
import time

import numpy as np
from scipy.optimize import least_squares

I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = [SX, SY, SZ]
TV = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]], dtype=int)  # t_a, h = t/sqrt3, e_a = t_a/sqrt3
SQ3 = np.sqrt(3.0)
OMEGA = np.exp(2j * np.pi / 3)
C2X = np.diag([1, -1, -1])
C2Y = np.diag([-1, 1, -1])
C2Z = np.diag([-1, -1, 1])
R3 = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])  # e_x -> e_y -> e_z, 120 Grad um (1,1,1)
S_BCC = np.concatenate([TV, -TV])  # Reihenfolge h1..h4, -h1..-h4


def key3(M):
    return tuple(int(x) for x in np.asarray(M).ravel())


# ---------------------------------------------------------------- Gruppen und Darstellungen
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


def gruppen():
    T, fehler = closure_T()
    rotsT = [e[0] for e in T]
    rotsV = [np.eye(3, dtype=int), C2X, C2Y, C2Z]
    info = {"T_ordnung": len(T), "T_konsistenzfehler": fehler}
    su2 = su2_closure([-1j * SX, 0.5 * (I2 - 1j * (SX + SY + SZ))])
    info["2T_ordnung"] = len(su2)
    kern = [U for U in su2 if adjoint_dev(np.eye(3, dtype=int), U) < 1e-10]
    info["2T_kern"] = len(kern)
    info["2T_kern_ist_pm_I"] = bool(len(kern) == 2 and all(min(np.abs(U - I2).max(), np.abs(U + I2).max()) < 1e-12 for U in kern))
    info["spinor_SO3_abw"] = max(adjoint_dev(R, U) for (R, U, _) in T)
    U_R = 0.5 * (I2 - 1j * (SX + SY + SZ))
    info["V_C3_hoch3_plus_I"] = float(np.abs(np.linalg.matrix_power(U_R, 3) + I2).max())
    info["V_C2x_hoch2_plus_I"] = float(np.abs((-1j * SX) @ (-1j * SX) + I2).max())
    # Darstellungen
    reps = {}
    reps["L3:1+1"] = ("L3", "linear", [I2.copy() for _ in T])
    reps["L3:1+1'"] = ("L3", "linear", [np.diag([1, OMEGA ** n]).astype(complex) for (_, _, n) in T])
    reps["L3:1+1''"] = ("L3", "linear", [np.diag([1, OMEGA ** (2 * n)]).astype(complex) for (_, _, n) in T])
    reps["L3:1'+1''"] = ("L3", "linear", [np.diag([OMEGA ** n, OMEGA ** (2 * n)]).astype(complex) for (_, _, n) in T])
    reps["L3:2"] = ("L3", "projektiv", [U.copy() for (_, U, _) in T])
    reps["L3:2'"] = ("L3", "projektiv", [OMEGA ** n * U for (_, U, n) in T])
    reps["L3:2''"] = ("L3", "projektiv", [OMEGA ** (2 * n) * U for (_, U, n) in T])
    chi = {"x": [1, 1, -1, -1], "y": [1, -1, 1, -1], "z": [1, -1, -1, 1]}
    reps["L2:Pauli"] = ("L2", "projektiv", [I2.copy(), 1j * SX, 1j * SY, 1j * SZ])
    reps["L2:1+1"] = ("L2", "linear", [I2.copy() for _ in range(4)])
    for c in "xyz":
        reps["L2:1+chi_" + c] = ("L2", "linear", [np.diag([1, chi[c][i]]).astype(complex) for i in range(4)])
    rots = {"L3": rotsT, "L2": rotsV}
    # Darstellungseigenschaften
    rinfo = {}
    for name, (grp, art, Vs) in reps.items():
        R = rots[grp]
        idx = {key3(M): i for i, M in enumerate(R)}
        maxdev, maxlin = 0.0, 0.0
        for i, A in enumerate(R):
            for j, B in enumerate(R):
                k = idx[key3(A @ B)]
                prod = Vs[i] @ Vs[j]
                c = np.trace(Vs[k].conj().T @ prod) / 2
                maxdev = max(maxdev, float(np.abs(prod - c * Vs[k]).max()))
                maxlin = max(maxlin, float(abs(c - 1)))
        ix, iy = idx[key3(C2X)], idx[key3(C2Y)]
        K = Vs[ix] @ Vs[iy] @ Vs[ix].conj().T @ Vs[iy].conj().T
        kern = sum(1 for i, V in enumerate(Vs) if np.abs(V - V[0, 0] * I2).max() < 1e-12)
        rinfo[name] = {"gruppe": grp, "art": art, "projektiv_abw": maxdev, "linear_abw": maxlin,
                       "kommutator_C2x_C2y": "-I" if np.abs(K + I2).max() < 1e-12 else ("+I" if np.abs(K - I2).max() < 1e-12 else "anders"),
                       "konjugationskern": int(kern)}
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


def covariant_basis(nslots, perms, Vs):
    dim = nslots * 4
    P = np.zeros((dim, dim), dtype=complex)
    for p, V in zip(perms, Vs):
        Vd = V.conj().T
        for col in range(dim):
            e = np.zeros(dim, dtype=complex)
            e[col] = 1
            A = e.reshape(nslots, 2, 2)
            B = np.zeros_like(A)
            for i in range(nslots):
                B[p[i]] = V @ A[i] @ Vd
            P[:, col] += B.ravel()
    P /= len(perms)
    proj_err = float(np.abs(P @ P - P).max())
    Ph = (P + P.conj().T) / 2
    w, vecs = np.linalg.eigh(Ph)
    sel = w > 0.5
    E = vecs[:, sel].T.reshape(-1, nslots, 2, 2)
    return E, proj_err


# ---------------------------------------------------------------- Unitaritaet
class Unit:
    """W(u) = sum_f e^{i u.f} A_f; Koeffizienten von W^dagger W - I (exakt)."""

    def __init__(self, freqs):
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
        self.target = np.zeros((self.nk, 4), dtype=complex)
        self.target[self.k0] = I2.ravel()

    def coeffs(self, A):
        Q = np.einsum("pji,pjk->pik", A[self.jj].conj(), A[self.ii])
        return self.M @ Q.reshape(-1, 4) - self.target

    def defect(self, A):
        return float(np.sum(np.abs(self.coeffs(A)) ** 2))

    def maxabs(self, A):
        return float(np.abs(self.coeffs(A)).max())

    def resid(self, A):
        C = self.coeffs(A)
        return np.concatenate([C.real.ravel(), C.imag.ravel()])

    def jac(self, A, dA):
        F = np.einsum("mpji,pjk->mpik", dA[:, self.jj].conj(), A[self.ii])
        G = np.einsum("pji,mpjk->mpik", A[self.jj].conj(), dA[:, self.ii])
        dQ = (F + G).reshape(dA.shape[0], -1, 4)
        dC = np.einsum("kp,mpq->mkq", self.M, dQ)
        return np.concatenate([dC.real.reshape(dA.shape[0], -1), dC.imag.reshape(dA.shape[0], -1)], axis=1).T


class Composite:
    """Diamant C-2: W(u) = C^(u) B^(u) = sum_{a,b} e^{iu.(t_b - t_a)} C_b B_a."""

    def __init__(self):
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
        self.unit = Unit(self.freqs)

    def A_of(self, B, C):
        Pm = np.einsum("pij,pjk->pik", C[self.pb], B[self.pa])
        return (self.Mc @ Pm.reshape(16, 4)).reshape(-1, 2, 2)

    def dA_of(self, B, C, dB, dC):
        t1 = np.einsum("pij,mpjk->mpik", C[self.pb], dB[:, self.pa])
        t2 = np.einsum("mpij,pjk->mpik", dC[:, self.pb], B[self.pa])
        S = (t1 + t2).reshape(dB.shape[0], 16, 4)
        return np.einsum("fp,mpq->mfq", self.Mc, S).reshape(dB.shape[0], -1, 2, 2)


def W_at(freqs, A, u):
    ph = np.exp(1j * (np.atleast_2d(u) @ np.asarray(freqs).T))
    return (ph @ A.reshape(len(freqs), 4)).reshape(-1, 2, 2)


def beta(W):
    T00 = (W[:, 0, 0] - W[:, 1, 1]) / 2
    n2 = 2 * np.abs(T00) ** 2 + np.abs(W[:, 0, 1]) ** 2 + np.abs(W[:, 1, 0]) ** 2
    return np.sqrt(n2 / 2)


def fib_dirs(n):
    i = np.arange(n) + 0.5
    phi = np.arccos(1 - 2 * i / n)
    th = np.pi * (1 + 5 ** 0.5) * i
    return np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi), np.cos(phi)], -1)


LAT26 = np.array([[i, j, k] for i in (-1, 0, 1) for j in (-1, 0, 1) for k in (-1, 0, 1) if (i, j, k) != (0, 0, 0)], float)
LAT26 /= np.linalg.norm(LAT26, axis=1)[:, None]
DIRS426 = np.concatenate([LAT26, fib_dirs(400)])
DIRS126 = np.concatenate([LAT26, fib_dirs(100)])


def grid_u(N, period=2 * np.pi):
    g = period * np.arange(N) / N
    return np.stack(np.meshgrid(g, g, g, indexing="ij"), -1).reshape(-1, 3)


def speeds(freqs, A, kabs, dirs):
    # Phasengeschwindigkeit omega/|k| (k-Einheiten, u = k/sqrt3), omega = halber Eigenphasenabstand
    W = W_at(freqs, A, kabs * dirs / SQ3)
    return np.arcsin(np.minimum(beta(W), 1.0)) / kabs


def cone_test(freqs, A, u0, eps_k=1e-5):
    e = eps_k / SQ3
    b1 = beta(W_at(freqs, A, u0[None, :] + e * DIRS126))
    b2 = beta(W_at(freqs, A, u0[None, :] + 2 * e * DIRS126))
    slope = np.arcsin(np.minimum(b1, 1.0)) / eps_k
    ratio = b2 / np.maximum(b1, 1e-300)
    ok = bool(slope.min() > 1e-3 and ratio.min() > 1.9 and ratio.max() < 2.1)
    return {"kegel": ok, "v_min": float(slope.min()), "v_max": float(slope.max()),
            "ratio_min": float(ratio.min()), "ratio_max": float(ratio.max())}


def find_degeneracies(freqs, A, equiv_gens, N=16, nmax=64):
    U = grid_u(N)
    b = beta(W_at(freqs, A, U)).reshape(N, N, N)
    loc = np.ones_like(b, dtype=bool)
    for ax in range(3):
        for sh in (1, -1):
            loc &= b <= np.roll(b, sh, axis=ax)
    cand = np.argwhere(loc)
    cand = sorted(cand.tolist(), key=lambda c: b[tuple(c)])[:nmax]

    def r(u):
        W = W_at(freqs, A, u[None, :])[0]
        T = W - np.trace(W) / 2 * I2
        return np.concatenate([T.real.ravel(), T.imag.ravel()])

    pts = []
    for c in cand:
        u_start = 2 * np.pi * np.array(c, float) / N
        try:
            sol = least_squares(r, u_start, method="lm", xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=300)
            u0 = sol.x
        except Exception:
            continue
        bb = float(beta(W_at(freqs, A, u0[None, :]))[0])
        if bb < 1e-7:
            ph = np.exp(1j * (np.asarray(equiv_gens, float) @ u0))
            if not any(np.abs(ph - q).max() < 1e-6 for (q, _) in pts):
                pts.append((ph, u0))
    out = []
    for ph, u0 in pts:
        W0 = W_at(freqs, A, u0[None, :])[0]
        lam = np.trace(W0) / 2
        gamma = bool(np.abs(ph - 1).max() < 1e-6)
        ct = cone_test(freqs, A, u0)
        out.append({"u": u0.tolist(), "k": (SQ3 * u0).tolist(), "gamma_aequivalent": gamma,
                    "W_wert": [float(lam.real), float(lam.imag)], "beta": float(beta(W0[None])[0]), **ct})
    return out


def classify(freqs, A, equiv_gens, full=True):
    U = grid_u(16)
    b = beta(W_at(freqs, A, U))
    delta = 2 * np.arcsin(np.minimum(b, 1.0))
    spread = float(delta.max() - delta.min())
    res = {"delta_spannweite": spread}
    if spread < 1e-8:
        res["klasse"] = "trivial"
        return res
    b0 = float(beta(W_at(freqs, A, np.zeros((1, 3))))[0])
    res["beta_0"] = b0
    if b0 < 1e-7:
        ct = cone_test(freqs, A, np.zeros(3))
        res["kegel_0"] = ct
        if ct["kegel"]:
            res["klasse"] = "Kegel"
            return res
    if full:
        deg = find_degeneracies(freqs, A, equiv_gens)
        res["entartungen"] = deg
        res["klasse"] = "Kegel" if any(d["kegel"] for d in deg) else "andere"
    else:
        res["klasse"] = "andere (ungeprueft)"
    return res


def signature(freqs, A, upts):
    return tuple(np.round(beta(W_at(freqs, A, upts)), 6).tolist())


# ---------------------------------------------------------------- Suche
def search_linear(unit, E, nstarts, seed, maxnfev=400):
    m = E.shape[0]
    dA = np.concatenate([E, 1j * E])
    rng = np.random.default_rng(seed)
    out = []

    def A_of(x):
        return np.tensordot(x[:m] + 1j * x[m:], E, axes=1)

    for _ in range(nstarts):
        t0 = rng.standard_normal(m) + 1j * rng.standard_normal(m)
        t0 *= np.sqrt(2.0) / np.linalg.norm(t0)
        x0 = np.concatenate([t0.real, t0.imag])
        try:
            sol = least_squares(lambda x: unit.resid(A_of(x)), x0, jac=lambda x: unit.jac(A_of(x), dA),
                                method="lm", xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=maxnfev)
            x, nfev = sol.x, int(sol.nfev)
        except Exception:
            x, nfev = x0, -1
        A = A_of(x)
        out.append((unit.defect(A), A, nfev))
    return out


def search_c2(comp, EB, EC, nstarts, seed, maxnfev=400):
    mB, mC = EB.shape[0], EC.shape[0]
    P = 2 * (mB + mC)
    dB = np.zeros((P, 4, 2, 2), dtype=complex)
    dC = np.zeros((P, 4, 2, 2), dtype=complex)
    dB[:mB] = EB
    dB[mB:2 * mB] = 1j * EB
    dC[2 * mB:2 * mB + mC] = EC
    dC[2 * mB + mC:] = 1j * EC
    rng = np.random.default_rng(seed)

    def BC(x):
        tB = x[:mB] + 1j * x[mB:2 * mB]
        tC = x[2 * mB:2 * mB + mC] + 1j * x[2 * mB + mC:]
        return np.tensordot(tB, EB, axes=1), np.tensordot(tC, EC, axes=1)

    def f(x):
        B, C = BC(x)
        return comp.unit.resid(comp.A_of(B, C))

    def J(x):
        B, C = BC(x)
        return comp.unit.jac(comp.A_of(B, C), comp.dA_of(B, C, dB, dC))

    out = []
    for _ in range(nstarts):
        tB = rng.standard_normal(mB) + 1j * rng.standard_normal(mB)
        tC = rng.standard_normal(mC) + 1j * rng.standard_normal(mC)
        tB *= np.sqrt(2.0) / np.linalg.norm(tB)
        tC *= np.sqrt(2.0) / np.linalg.norm(tC)
        x0 = np.concatenate([tB.real, tB.imag, tC.real, tC.imag])
        try:
            sol = least_squares(f, x0, jac=J, method="lm", xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=maxnfev)
            x, nfev = sol.x, int(sol.nfev)
        except Exception:
            x, nfev = x0, -1
        B, C = BC(x)
        A = comp.A_of(B, C)
        out.append((comp.unit.defect(A), (B, C, A), nfev))
    return out


def summarize(results, hits_classify, maxklass=60):
    D = np.array([r[0] for r in results])
    nfev = np.array([r[2] for r in results])
    s = {"starts": int(len(D)), "D_min": float(D.min()), "D_median": float(np.median(D)), "D_max": float(D.max()),
         "treffer": int(np.sum(D < 1e-10)), "nfev_median": float(np.median(nfev)), "nfev_max": int(nfev.max()),
         "log10D_hist": np.histogram(np.log10(np.maximum(D, 1e-40)), bins=np.arange(-40, 3, 2))[0].tolist(),
         "log10D_alle": np.log10(np.maximum(D, 1e-40)).round(3).tolist()}
    return s


# ---------------------------------------------------------------- Teil A
def weyl_A(sign):
    z = (1 + sign * 1j) / 4
    zc = np.conj(z)
    d = {"h1": [[zc, 0], [zc, 0]], "-h1": [[0, -z], [0, z]],
         "h2": [[0, zc], [0, zc]], "-h2": [[z, 0], [-z, 0]],
         "h3": [[0, -zc], [0, zc]], "-h3": [[z, 0], [z, 0]],
         "h4": [[zc, 0], [-zc, 0]], "-h4": [[0, z], [0, z]]}
    order = ["h1", "h2", "h3", "h4", "-h1", "-h2", "-h3", "-h4"]
    return np.array([d[k] for k in order], dtype=complex)


def W_conv(A, k, conv):
    # conv=+1: Eq. (16) e^{+ik.h}; conv=-1: e^{-ik.h} (Eq. 10/11)
    u = conv * np.atleast_2d(k) / SQ3
    return W_at(S_BCC, A, u)


def var_25(k, sign, quarter, conv_phase):
    z = (1 + sign * 1j) / 4
    zc = np.conj(z)
    kk = [conv_phase * float(k @ (TV[i] / SQ3)) for i in range(4)]
    e = np.exp
    zf = zc * e(1j * kk[0]) + z * e(-1j * kk[1]) + z * e(-1j * kk[2]) + zc * e(1j * kk[3])
    wf = zc * e(1j * kk[0]) + z * e(-1j * kk[1]) - z * e(-1j * kk[2]) - zc * e(1j * kk[3])
    M = np.array([[zf, -np.conj(wf)], [wf, np.conj(zf)]])
    return M / 4 if quarter else M


def _cs(k):
    a = np.asarray(k, float) / SQ3
    return np.cos(a), np.sin(a)


def var_main(k, s):
    c, sn = _cs(k)
    ax = sn[0] * c[1] * c[2] + s * c[0] * sn[1] * sn[2]
    ay = c[0] * sn[1] * c[2] - s * sn[0] * c[1] * sn[2]
    az = c[0] * c[1] * sn[2] + s * sn[0] * sn[1] * c[2]
    d = c[0] * c[1] * c[2] - s * sn[0] * sn[1] * sn[2]
    return d * I2 - 1j * (ax * SX - s * ay * SY + az * SZ)


def var_app(k, s):
    c, sn = _cs(k)
    ax = sn[0] * c[1] * c[2] - s * c[0] * sn[1] * sn[2]
    ay = c[0] * sn[1] * c[2] + s * sn[0] * c[1] * sn[2]
    az = c[0] * c[1] * sn[2] - s * sn[0] * sn[1] * c[2]
    d = c[0] * c[1] * c[2] + s * sn[0] * sn[1] * sn[2]
    return d * I2 - 1j * (ax * SX - s * ay * SY + az * SZ)


def var_33(k, s):
    c, sn = _cs(k)
    return (c[0] * I2 - 1j * sn[0] * SX) @ (c[1] * I2 - 1j * s * sn[1] * SY) @ (c[2] * I2 - 1j * sn[2] * SZ)


def implementing_unitary(A, perm):
    rows = []
    for i in range(len(A)):
        Ah, Ag = A[i], A[perm[i]]
        rows.append(np.kron(Ah.T, I2) - np.kron(I2, Ag))
    Msys = np.concatenate(rows)
    _, s, vh = np.linalg.svd(Msys)
    v = vh.conj()[-1]
    U = v.reshape(2, 2, order="F")
    dt = np.linalg.det(U)
    if abs(dt) < 1e-12:
        return {"s_min": float(s[-1]), "s_2": float(s[-2]), "unitaer_abw": None, "det_null": True}, U
    U1 = U / np.sqrt(dt)
    return {"s_min": float(s[-1]), "s_2": float(s[-2]), "unitaer_abw": float(np.abs(U1.conj().T @ U1 - I2).max())}, U1


def teil_A(rots, reps, rng):
    out = {}
    unitS = Unit(S_BCC)
    autos = {"A+": weyl_A(+1), "A-": weyl_A(-1)}
    kr = rng.uniform(-4, 4, size=(50, 3))
    Ugrid = grid_u(24)
    for name, A in autos.items():
        r = {}
        r["koeff_maxabs"] = unitS.maxabs(A)
        r["defekt"] = unitS.defect(A)
        Wg = W_at(S_BCC, A, Ugrid)
        dev = np.einsum("nji,njk->nik", Wg.conj(), Wg) - I2
        r["gitter_max_norm"] = float(np.linalg.norm(dev, ord=2, axis=(1, 2)).max())
        r["det_minus_1_max"] = float(np.abs(np.linalg.det(Wg) - 1).max())
        r["summe_A_minus_I"] = float(np.abs(A.sum(0) - I2).max())
        r["W0_minus_I"] = float(np.abs(W_at(S_BCC, A, np.zeros((1, 3)))[0] - I2).max())
        # Lesepruefung (beschreibend)
        les = {}
        for conv in (+1, -1):
            for tr in ("", "T"):
                Wk = np.array([W_conv(A, k, conv)[0] for k in kr])
                if tr == "T":
                    Wk = np.transpose(Wk, (0, 2, 1))
                for s in (+1, -1):
                    les[f"conv{conv:+d}{tr}_Eq26-28_s{s:+d}"] = float(max(np.abs(Wk[i] - var_main(kr[i], s)).max() for i in range(len(kr))))
                    les[f"conv{conv:+d}{tr}_EqA81-A82_s{s:+d}"] = float(max(np.abs(Wk[i] - var_app(kr[i], s)).max() for i in range(len(kr))))
                    les[f"conv{conv:+d}{tr}_Eq33_s{s:+d}"] = float(max(np.abs(Wk[i] - var_33(kr[i], s)).max() for i in range(len(kr))))
                sign = +1 if name == "A+" else -1
                for quarter in (True, False):
                    for cp in (+1, -1):
                        les[f"conv{conv:+d}{tr}_Eq25_viertel{int(quarter)}_phase{cp:+d}"] = float(max(
                            np.abs(Wk[i] - var_25(kr[i], sign, quarter, cp)).max() for i in range(len(kr))))
        r["lesepruefung"] = les
        # Verschiebungen (S. 5), Konvention Eq. (16)
        other = autos["A-" if name == "A+" else "A+"]
        sh = {}
        for lab, vec in (("sqrt3pi_ex", SQ3 * np.pi * np.array([1.0, 0, 0])), ("P_111", SQ3 * np.pi / 2 * np.array([1.0, 1, 1])),
                         ("minusP_111", -SQ3 * np.pi / 2 * np.array([1.0, 1, 1]))):
            d = {}
            for cand in ("+W", "-W", "+W^T", "-W^T", "+W_ander", "-W_ander", "+W_ander^T", "-W_ander^T"):
                devs = []
                for k in kr[:20]:
                    W1 = W_conv(A, k + vec, +1)[0]
                    base = W_conv(other if "ander" in cand else A, k, +1)[0]
                    if cand.endswith("^T"):
                        base = base.T
                    sg = -1 if cand.startswith("-") else 1
                    devs.append(np.abs(W1 - sg * base).max())
                d[cand] = float(max(devs))
            sh[lab] = d
        r["verschiebungen"] = sh
        # linearer Teil
        H = S_BCC / SQ3
        Mj = [-sum(H[i, j] * A[i] for i in range(8)) for j in range(3)]
        r["M_herm_abw"] = float(max(np.abs(M - M.conj().T).max() for M in Mj))
        r["M_antikomm_abw"] = float(max(np.abs(Mj[i] @ Mj[j] + Mj[j] @ Mj[i] - (2.0 / 3.0) * (i == j) * I2).max()
                                        for i in range(3) for j in range(3)))
        v = speeds(S_BCC, A, 1e-7, DIRS426)
        r["v_1e-7_abw_max"] = float(np.abs(v - 1 / SQ3).max())
        r["v_1e-7_min"] = float(v.min())
        r["v_1e-7_max"] = float(v.max())
        v5 = speeds(S_BCC, A, 0.05, fib_dirs(400))
        r["v_0.05_mittel"] = float(v5.mean())
        r["v_0.05_streuung_std_rel"] = float(v5.std() / v5.mean())
        r["v_0.05_spannweite_rel"] = float((v5.max() - v5.min()) / v5.mean())
        # implementierende Unitaere
        impl = {}
        Uc2 = {}
        for gi, R in enumerate(rots["L3"]):
            p = perm_on(S_BCC, R)
            info, U1 = implementing_unitary(A, p)
            lab = ("E" if np.array_equal(R, np.eye(3, dtype=int)) else
                   "C2x" if np.array_equal(R, C2X) else "C2y" if np.array_equal(R, C2Y) else
                   "C2z" if np.array_equal(R, C2Z) else f"C3_{gi}")
            if lab in ("C2x", "C2y", "C2z"):
                info["U_hoch2_plus_I"] = float(np.abs(U1 @ U1 + I2).max())
                info["U"] = [[ [float(x.real), float(x.imag)] for x in row] for row in U1]
                Uc2[lab] = U1
            impl[lab] = info
        K = Uc2["C2x"] @ Uc2["C2y"] @ Uc2["C2x"].conj().T @ Uc2["C2y"].conj().T
        r["kommutator_plus_I"] = float(np.abs(K + I2).max())
        r["kommutator_minus_I"] = float(np.abs(K - I2).max())
        r["implementierung"] = impl
        # Kegelsuche (QT3)
        r["entartungen"] = find_degeneracies(S_BCC, A, TV)
        out[name] = r
    out["_A"] = autos
    return out


# ---------------------------------------------------------------- Bilder
def bild_A(autos, pfad):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    G = np.zeros(3)
    H = SQ3 * np.pi * np.array([1.0, 0, 0])
    Np = SQ3 * np.pi * np.array([0.5, 0.5, 0])
    P = SQ3 * np.pi * np.array([0.5, 0.5, 0.5])
    segs = [(G, H, "Γ", "H"), (H, Np, "H", "N"), (Np, G, "N", "Γ"), (G, P, "Γ", "P"), (P, H, "P", "H"), (-P, G, "P'", "Γ")]
    fig, ax = plt.subplots(figsize=(10, 4.6))
    x0 = 0.0
    ticks, labs = [], []
    for (a, b, la, lb) in segs:
        t = np.linspace(0, 1, 300)
        ks = a[None, :] + t[:, None] * (b - a)[None, :]
        L = np.linalg.norm(b - a)
        xs = x0 + t * L
        for name, sty in (("A+", "-"), ("A-", "--")):
            W = W_at(S_BCC, autos[name], ks / SQ3)
            om = np.arccos(np.clip(np.real(np.trace(W, axis1=1, axis2=2)) / 2, -1, 1))
            col = "C0" if name == "A+" else "C3"
            ax.plot(xs, om, sty, color=col, lw=1.4, label=name if (la == "Γ" and lb == "H") else None)
            ax.plot(xs, -om, sty, color=col, lw=1.4)
        if not ticks or abs(ticks[-1] - x0) > 1e-9:
            ticks.append(x0)
            labs.append(la)
        else:
            labs[-1] = labs[-1] + "|" + la if labs[-1] != la else la
        x0 += L
        ticks.append(x0)
        labs.append(lb)
        ax.axvline(x0, color="0.8", lw=0.6)
    ax.set_xticks(ticks)
    ax.set_xticklabels(labs)
    ax.set_ylabel("Eigenphase ±ω(k)")
    ax.set_ylim(-np.pi * 1.05, np.pi * 1.05)
    ax.axhline(0, color="0.6", lw=0.5)
    ax.set_title("Teil A: Weyl-Automat (D'Ariano/Perinotti Eq. 24), BCC; Kegel an Γ, H, P, P'")
    ax.legend(loc="upper right")
    fig.tight_layout()
    fig.savefig(pfad, dpi=130)
    plt.close(fig)


def bild_B(stats, pfad):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    names = list(stats.keys())
    fig, axs = plt.subplots(1, 2, figsize=(13, 4.8))
    hk = [stats[n]["kegel"] for n in names]
    ht = [stats[n]["trivial"] for n in names]
    ha = [stats[n]["andere"] for n in names]
    x = np.arange(len(names))
    axs[0].bar(x, hk, color="C2", label="Treffer mit Kegel")
    axs[0].bar(x, ht, bottom=hk, color="C7", label="trivial")
    axs[0].bar(x, ha, bottom=np.array(hk) + np.array(ht), color="C1", label="andere")
    axs[0].set_xticks(x)
    axs[0].set_xticklabels(names, rotation=60, ha="right", fontsize=8)
    axs[0].set_ylabel(f"Treffer (Defekt < 1e-10) von {stats[names[0]]['starts']} Starts")
    axs[0].legend(fontsize=8)
    for i, n in enumerate(names):
        vals = np.array(stats[n]["log10D_alle"])
        axs[1].scatter(np.full(len(vals), i) + np.random.default_rng(i).uniform(-0.25, 0.25, len(vals)), vals, s=4, alpha=0.5)
    axs[1].axhline(-10, color="k", lw=0.8, ls="--")
    axs[1].set_xticks(x)
    axs[1].set_xticklabels(names, rotation=60, ha="right", fontsize=8)
    axs[1].set_ylabel("log10 Defekt am Ende jedes Starts")
    axs[1].set_title("Schwelle 1e-10 gestrichelt")
    fig.suptitle("Teil B: isotrope 2-Zustands-Automaten auf BCC, je Gruppe und Darstellung")
    fig.tight_layout()
    fig.savefig(pfad, dpi=130)
    plt.close(fig)


def bild_C(statsC, bestC1, bestC2, comp, pfad):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, axs = plt.subplots(1, 3, figsize=(16, 4.8))
    names = list(statsC["C1"].keys())
    x = np.arange(len(names))
    axs[0].semilogy(x, [statsC["C1"][n]["D_min"] for n in names], "o", label="C-1 (jeder Halbschritt unitaer)")
    axs[0].semilogy(x, [statsC["C2"][n]["D_min"] for n in names], "s", label="C-2 (nur Zweischritt unitaer)")
    axs[0].axhline(1e-10, color="k", ls="--", lw=0.8)
    axs[0].set_xticks(x)
    axs[0].set_xticklabels(names, rotation=60, ha="right", fontsize=8)
    axs[0].set_ylabel("kleinster Defekt ueber alle Starts")
    axs[0].legend(fontsize=8)
    a4 = 4 / SQ3
    g = 2 * np.pi / a4
    G = np.zeros(3)
    X = g * np.array([1.0, 0, 0])
    Wp = g * np.array([1.0, 0.5, 0])
    L = g * np.array([0.5, 0.5, 0.5])
    K = g * np.array([0.75, 0.75, 0])
    segs = [(G, X, "Γ", "X"), (X, Wp, "X", "W"), (Wp, L, "W", "L"), (L, G, "L", "Γ"), (G, K, "Γ", "K")]
    for axi, (titel, kind) in zip(axs[1:], (("C-1: Singulaerwerte von B^(k), bester Kandidat", "C1"),
                                             ("C-2: |Eigenwerte| von W(k), bester Kandidat", "C2"))):
        x0 = 0.0
        ticks, labs = [0.0], ["Γ"]
        for (a, b, la, lb) in segs:
            t = np.linspace(0, 1, 200)
            ks = a[None, :] + t[:, None] * (b - a)[None, :]
            Lg = np.linalg.norm(b - a)
            if kind == "C1":
                if bestC1 is None:
                    continue
                Wk = W_at(-TV, bestC1, ks / SQ3)
                vals = np.linalg.svd(Wk, compute_uv=False)
            else:
                if bestC2 is None:
                    continue
                Wk = W_at(comp.freqs, bestC2, ks / SQ3)
                vals = np.abs(np.linalg.eigvals(Wk))
            sv = np.sort(vals, axis=1)
            axi.plot(x0 + t * Lg, sv[:, 0], "-", color="C0", lw=1.2)
            axi.plot(x0 + t * Lg, sv[:, 1], "-", color="C1", lw=1.2)
            x0 += Lg
            ticks.append(x0)
            labs.append(lb)
            axi.axvline(x0, color="0.8", lw=0.6)
        axi.axhline(1.0, color="k", ls="--", lw=0.8)
        axi.set_xticks(ticks)
        axi.set_xticklabels(labs)
        axi.set_title(titel, fontsize=10)
    fig.suptitle("Teil C: Diamantnetz, 2 Zustaende je Knoten; fuer einen unitaeren Automaten laegen alle Kurven bei 1")
    fig.tight_layout()
    fig.savefig(pfad, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------- Haupt
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--teil", choices=["AB", "C"], required=True)
    ap.add_argument("--modus", choices=["rauch", "haupt"], required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--fassung", choices=["C1", "C2", "beide"], default="beide")
    ap.add_argument("--faelle", default="alle", help="alle, L3, L2 oder Kommaliste von Fallnamen")
    args = ap.parse_args()
    t_start = time.time()
    nstarts = 20 if args.modus == "rauch" else 200
    seedbase = 3700 if args.modus == "rauch" else 37
    rng = np.random.default_rng(seedbase)
    rots, reps, ginfo, rinfo = gruppen()
    res = {"modus": args.modus, "teil": args.teil, "starts_je_fall": nstarts, "saat_basis": seedbase,
           "gruppen": ginfo, "darstellungen": rinfo, "numpy": np.__version__}
    # Wirkung auf S
    perms_ok = True
    for grp in ("L3", "L2"):
        for R in rots[grp]:
            if perm_on(S_BCC, R) is None or perm_on(TV, R) is None:
                perms_ok = False
    res["gruppen"]["wirkung_auf_S_ok"] = perms_ok
    res["gruppen"]["L2_ordnung"] = len(rots["L2"])
    upts = rng.uniform(0, 2 * np.pi, size=(20, 3))
    if args.teil == "AB":
        # Codepruefung Defekt: Gittermittel gegen exakt (N = 12, exakt fuer |Frequenz| <= 4 je Achse)
        unitS = Unit(S_BCC)
        Ug = grid_u(12)
        chk = []
        for _ in range(3):
            A = rng.standard_normal((8, 2, 2)) + 1j * rng.standard_normal((8, 2, 2))
            Wg = W_at(S_BCC, A, Ug)
            dev = np.einsum("nji,njk->nik", Wg.conj(), Wg) - I2
            gm = float(np.mean(np.sum(np.abs(dev) ** 2, axis=(1, 2))))
            chk.append(abs(gm - unitS.defect(A)) / unitS.defect(A))
        res["defekt_codepruefung_rel"] = float(max(chk))
        # Teil A
        tA = teil_A(rots, reps, rng)
        autos = tA.pop("_A")
        res["teil_A"] = tA
        # Teil B
        statsB = {}
        for ci, (name, (grp, art, Vs)) in enumerate(reps.items()):
            perms = [perm_on(S_BCC, R) for R in rots[grp]]
            E, perr = covariant_basis(8, perms, Vs)
            results = search_linear(unitS, E, nstarts, seedbase * 100 + ci)
            st = summarize(results, True)
            st.update({"gruppe": grp, "art": art, "dim_komplex": int(E.shape[0]), "projektor_abw": perr})
            hits = [r for r in results if r[0] < 1e-10]
            st["kegel"] = st["trivial"] = st["andere"] = 0
            klassen = {}
            for (D, A, _) in hits:
                cl = classify(S_BCC, A, TV, full=False)
                if cl["klasse"] == "andere (ungeprueft)":
                    cl = classify(S_BCC, A, TV, full=True)
                key = "kegel" if cl["klasse"] == "Kegel" else ("trivial" if cl["klasse"] == "trivial" else "andere")
                st[key] += 1
                sig = signature(S_BCC, A, upts)
                if sig not in klassen:
                    v = speeds(S_BCC, A, 1e-7, DIRS426)
                    gleich = {}
                    for nm, Aref in autos.items():
                        for tr in ("", "T", "refl", "conj"):
                            Ar = Aref.copy()
                            if tr == "T":
                                Ar = np.transpose(Ar, (0, 2, 1))
                            elif tr == "refl":
                                Ar = np.concatenate([Ar[4:], Ar[:4]])
                            elif tr == "conj":
                                Ar = Ar.conj()
                            gleich[nm + tr] = bool(signature(S_BCC, Ar, upts) == sig)
                    deg = find_degeneracies(S_BCC, A, TV) if len(klassen) < 8 else None
                    klassen[sig] = {"anzahl": 0, "klasse": cl["klasse"], "v0_min": float(v.min()), "v0_max": float(v.max()),
                                    "spektral_gleich_wie": gleich,
                                    "kegelpunkte": None if deg is None else int(sum(1 for d in deg if d["kegel"])),
                                    "W0_phase": float(np.angle(np.trace(W_at(S_BCC, A, np.zeros((1, 3)))[0]) / 2))}
                klassen[sig]["anzahl"] += 1
            st["klassen"] = list(klassen.values())
            statsB[name] = st
            print(f"[B] {name}: dim={E.shape[0]} treffer={st['treffer']} kegel={st['kegel']} Dmin={st['D_min']:.3e}", flush=True)
        res["teil_B"] = statsB
        pfad = args.out.rsplit("/", 1)[0] if "/" in args.out else "."
        bild_A(autos, pfad + "/omega_A.png")
        bild_B(statsB, pfad + "/suche_B.png")
    else:
        # Teil C
        unitC1 = Unit(-TV)
        comp = Composite()
        Ug = grid_u(20)
        chk = []
        for _ in range(3):
            B = rng.standard_normal((4, 2, 2)) + 1j * rng.standard_normal((4, 2, 2))
            C = rng.standard_normal((4, 2, 2)) + 1j * rng.standard_normal((4, 2, 2))
            A = comp.A_of(B, C)
            Wg = W_at(comp.freqs, A, Ug)
            Wd = W_at(TV, C, Ug) @ W_at(-TV, B, Ug)
            dev = np.einsum("nji,njk->nik", Wg.conj(), Wg) - I2
            gm = float(np.mean(np.sum(np.abs(dev) ** 2, axis=(1, 2))))
            chk.append(max(abs(gm - comp.unit.defect(A)) / comp.unit.defect(A), float(np.abs(Wg - Wd).max())))
        res["defekt_codepruefung_rel"] = float(max(chk))
        res["C2_frequenzen"] = int(len(comp.freqs))
        res["fassung"] = args.fassung
        res["faelle"] = args.faelle
        statsC = {"C1": {}, "C2": {}}
        bestC1, bestC2, bestD1, bestD2 = None, None, np.inf, np.inf
        if args.faelle == "alle":
            wahl = list(reps.keys())
        elif args.faelle in ("L3", "L2"):
            wahl = [n for n in reps if n.startswith(args.faelle + ":")]
        else:
            wahl = args.faelle.split(",")
        for ci, (name, (grp, art, Vs)) in enumerate(reps.items()):
            if name not in wahl:
                continue
            perms = [perm_on(TV, R) for R in rots[grp]]
            E, perr = covariant_basis(4, perms, Vs)
            if args.fassung in ("C1", "beide"):
                t0 = time.time()
                r1 = search_linear(unitC1, E, nstarts, seedbase * 1000 + ci)
                st1 = summarize(r1, True)
                st1.update({"gruppe": grp, "art": art, "dim_komplex": int(E.shape[0]), "projektor_abw": perr})
                st1["klassen"] = []
                for (D, A, _) in r1:
                    if D < 1e-10:
                        cl = classify(-TV, A, TV, full=True)
                        v5 = speeds(-TV, A, 0.05, fib_dirs(400))
                        st1["klassen"].append({"klasse": cl["klasse"], "beta_0": cl.get("beta_0"),
                                               "kegel_0": cl.get("kegel_0", {}).get("kegel", False),
                                               "streuung_std_rel": float(v5.std() / v5.mean())})
                j = int(np.argmin([r[0] for r in r1]))
                if r1[j][0] < bestD1:
                    bestD1, bestC1 = r1[j][0], r1[j][1]
                st1["laufzeit_s"] = time.time() - t0
                statsC["C1"][name] = st1
                print(f"[C1] {name}: dim={E.shape[0]} treffer={st1['treffer']} Dmin={st1['D_min']:.3e} "
                      f"t={st1['laufzeit_s']:.1f}s", flush=True)
            if args.fassung in ("C2", "beide"):
                t0 = time.time()
                r2 = search_c2(comp, E, E, nstarts, seedbase * 2000 + ci)
                st2 = summarize(r2, True)
                st2.update({"gruppe": grp, "art": art, "dim_komplex": int(2 * E.shape[0])})
                st2["klassen"] = []
                for (D, (B, C, A), _) in r2:
                    if D < 1e-10:
                        cl = classify(comp.freqs, A, TV[1:] - TV[0], full=True)
                        v5 = speeds(comp.freqs, A, 0.05, fib_dirs(400))
                        st2["klassen"].append({"klasse": cl["klasse"], "beta_0": cl.get("beta_0"),
                                               "kegel_0": cl.get("kegel_0", {}).get("kegel", False),
                                               "streuung_std_rel": float(v5.std() / v5.mean())})
                j = int(np.argmin([r[0] for r in r2]))
                if r2[j][0] < bestD2:
                    bestD2, bestC2 = r2[j][0], r2[j][1][2]
                st2["laufzeit_s"] = time.time() - t0
                statsC["C2"][name] = st2
                print(f"[C2] {name}: dim={2 * E.shape[0]} treffer={st2['treffer']} Dmin={st2['D_min']:.3e} "
                      f"t={st2['laufzeit_s']:.1f}s", flush=True)
        res["teil_C"] = statsC
        res["teil_C_bester"] = {
            "C1": None if bestC1 is None else {"D": float(bestD1), "A_re": bestC1.real.tolist(), "A_im": bestC1.imag.tolist()},
            "C2": None if bestC2 is None else {"D": float(bestD2), "A_re": bestC2.real.tolist(), "A_im": bestC2.imag.tolist()}}
    res["laufzeit_s"] = time.time() - t_start
    with open(args.out, "w") as fh:
        json.dump(res, fh, indent=1, default=lambda o: o.tolist() if hasattr(o, "tolist") else str(o))
    print(f"fertig, {res['laufzeit_s']:.1f} s", flush=True)


if __name__ == "__main__":
    sys.exit(main())
