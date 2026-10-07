#!/usr/bin/env python3
# QCA-DIRAC-T-1, Runde 38 (fmhc-physics). Code-Agent fuer die Leitung claude-primary.
# Baut auf RUNDE-37/qca-diamant-4/code/qca_diamant.py auf (Gruppen T/2T, kovarianter Unterraum, exakte Defektformel,
# Einordnung), dazu: schneller Loeser (Residuen nur je Bahn der Differenzen, gewichtet), Vor-Ort-Term (Masse),
# Inversionsbedingung (Form P), Massen-Einordnung (Luecke, lineare Aufspaltung exakt, Kruemmung), Konstruktionen.
# Teil 0: Quell-Dirac-Automat (Eq. 24, 36, 37), Suchkontrolle T:2+2' (s = 4), Konstruktionen (Teil B-K).
# Teil A: BCC, s = 4, T:2+2, Formen N (8 Spruenge), N mit W(0) = I, O (8 Spruenge + Vor-Ort-Term).
# Teil B: BCC, s = 8, T-kovariant, Spinor-Zerlegungen K1..K5, Formen N, O, P (O + Inversion).
# Start nur auf der .69 ueber kleintest.sh.
import argparse
import json
import sys
import time

import numpy as np
from scipy.linalg import schur
from scipy.optimize import minimize

I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = [SX, SY, SZ]
TV = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]], dtype=int)  # t_a; h_a = t_a/sqrt3
SQ3 = np.sqrt(3.0)
OMEGA = np.exp(2j * np.pi / 3)
C2X = np.diag([1, -1, -1])
C2Y = np.diag([-1, 1, -1])
C2Z = np.diag([-1, -1, 1])
R3 = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])  # 120 Grad um (1,1,1)
S_BCC = np.concatenate([TV, -TV])
SLOTS_O = np.concatenate([S_BCC, np.zeros((1, 3), dtype=int)])
INV_PERM = [4, 5, 6, 7, 0, 1, 2, 3, 8]
IRR = {"2": 0, "2'": 1, "2''": 2}
KLASSEN8 = {"K1": "2+2+2+2", "K2": "2+2+2+2'", "K3": "2+2+2+2''", "K4": "2+2+2'+2'", "K5": "2+2+2'+2''"}


def key3(M):
    return tuple(int(x) for x in np.asarray(M).ravel())


# ---------------------------------------------------------------- Gruppen (aus qca_diamant.py)
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


def perm_on(vectors, R):
    keys = {tuple(int(x) for x in v): i for i, v in enumerate(vectors)}
    p = []
    for v in vectors:
        w = tuple(int(x) for x in R @ v)
        if w not in keys:
            return None
        p.append(keys[w])
    return p


def gruppen():
    T, fehler = closure_T()
    info = {"T_ordnung": len(T), "T_konsistenzfehler": fehler}
    su2 = su2_closure([-1j * SX, 0.5 * (I2 - 1j * (SX + SY + SZ))])
    info["2T_ordnung"] = len(su2)
    kern = [U for U in su2 if adjoint_dev(np.eye(3, dtype=int), U) < 1e-10]
    info["2T_kern_ist_pm_I"] = bool(len(kern) == 2 and all(min(np.abs(U - I2).max(), np.abs(U + I2).max()) < 1e-12 for U in kern))
    info["spinor_SO3_abw"] = max(adjoint_dev(R, U) for (R, U, _) in T)
    idx = {key3(R): i for i, (R, _, _) in enumerate(T)}
    info["idx_C2x"], info["idx_C2y"], info["idx_R3"] = idx[key3(C2X)], idx[key3(C2Y)], idx[key3(R3)]
    info["U_C2x_quadrat_plus_I"] = float(np.abs(T[idx[key3(C2X)]][1] @ T[idx[key3(C2X)]][1] + I2).max())
    info["U_R3_hoch3_plus_I"] = float(np.abs(np.linalg.matrix_power(T[idx[key3(R3)]][1], 3) + I2).max())
    info["wirkung_auf_slots_ok"] = all(perm_on(SLOTS_O, R) is not None for (R, _, _) in T)
    return T, info


def spinor_rep(T, teile):
    return [bdiag(*[OMEGA ** (IRR[p] * q) * U for p in teile]) for (_, U, q) in T]


def rep_info(T, Vs, ginfo):
    s = Vs[0].shape[0]
    Is = np.eye(s)
    idx = {key3(R): i for i, (R, _, _) in enumerate(T)}
    maxdev, unit = 0.0, 0.0
    for i, (A, _, _) in enumerate(T):
        unit = max(unit, float(np.abs(Vs[i].conj().T @ Vs[i] - Is).max()))
        for j, (B, _, _) in enumerate(T):
            k = idx[key3(A @ B)]
            prod = Vs[i] @ Vs[j]
            c = np.trace(Vs[k].conj().T @ prod) / s
            maxdev = max(maxdev, float(np.abs(prod - c * Vs[k]).max()))
    Vx, Vy, V3 = Vs[ginfo["idx_C2x"]], Vs[ginfo["idx_C2y"]], Vs[ginfo["idx_R3"]]
    K = Vx @ Vy @ Vx.conj().T @ Vy.conj().T
    return {"projektiv_abw": maxdev, "unitaer_abw": unit, "K_plus_I": float(np.abs(K + Is).max()),
            "Vx2_plus_I": float(np.abs(Vx @ Vx + Is).max()),
            "V3hoch3_plus_I": float(np.abs(np.linalg.matrix_power(V3, 3) + Is).max())}


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


# ---------------------------------------------------------------- Unitaritaet
class Unit:
    """W(u) = sum_f e^{i u.f} A_f; alle Koeffizienten von W^dagger W - I (exakt, Kontrolle)."""

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
        self.ii, self.jj, self.nk = np.array(ii), np.array(jj), len(keys)
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


class Fast:
    """Residuen nur fuer je eine Differenz d je Bahn unter T x {+-1}, gewichtet mit sqrt(Bahnlaenge).
    Gilt fuer exakt kovariante A (Parameter im kovarianten Unterraum): ||R_gd|| = ||R_d||, R_-d = R_d^dagger."""

    def __init__(self, E, freqs, s, rots, w0=False):
        self.E, self.m, self.s, self.w0 = E, E.shape[0], s, w0
        F = np.asarray(freqs, dtype=int)
        diffs = {}
        for i in range(len(F)):
            for j in range(len(F)):
                diffs.setdefault(tuple(int(x) for x in F[i] - F[j]), []).append((i, j))
        reps, seen = [], set()
        for d in diffs:
            if d in seen:
                continue
            orbit = {tuple(int(x) for x in sg * (R @ np.array(d))) for R in rots for sg in (1, -1)}
            if not all(o in diffs for o in orbit):
                raise RuntimeError("Bahn nicht in den Differenzen")
            seen |= orbit
            reps.append((d, len(orbit)))
        self.reps = reps
        self.n_diff = len(diffs)
        m = self.m
        K = np.zeros((len(reps), m, m, s, s), dtype=complex)
        for r, (d, _) in enumerate(reps):
            for (i, j) in diffs[d]:
                K[r] += np.einsum("lba,jbc->ljac", E[:, j].conj(), E[:, i])
        self.K = K
        self.sw = np.sqrt(np.array([w for (_, w) in reps], float))
        self.r0 = [r for r, (d, _) in enumerate(reps) if d == (0, 0, 0)][0]
        self.Esum = E.sum(1)
        self.Is = np.eye(s)

    def rj(self, p, jac=True):
        m, s = self.m, self.s
        x = p[:m] + 1j * p[m:]
        Y1 = np.tensordot(x.conj(), self.K, axes=([0], [1]))
        R = np.tensordot(x, Y1, axes=([0], [1]))
        R[self.r0] -= self.Is
        nd = R.shape[0]
        r = (np.concatenate([R.real.reshape(nd, -1), R.imag.reshape(nd, -1)], axis=1) * self.sw[:, None]).ravel()
        if self.w0:
            R0 = np.tensordot(x, self.Esum, axes=1) - self.Is
            r = np.concatenate([r, R0.real.ravel(), R0.imag.ravel()])
        if not jac:
            return r, None
        Y2 = np.tensordot(self.K, x, axes=([2], [0]))
        Jd = np.concatenate([Y1 + Y2, 1j * (Y1 - Y2)], axis=1)  # (nd, 2m, s, s)
        Jr = Jd.real.reshape(nd, 2 * m, s * s).transpose(0, 2, 1)
        Ji = Jd.imag.reshape(nd, 2 * m, s * s).transpose(0, 2, 1)
        J = (np.concatenate([Jr, Ji], axis=1) * self.sw[:, None, None]).reshape(-1, 2 * m)
        if self.w0:
            Jw = np.concatenate([self.Esum, 1j * self.Esum], axis=0).reshape(2 * m, s * s)
            J = np.concatenate([J, Jw.real.T, Jw.imag.T], axis=0)
        return r, J

    def defect(self, p):
        r, _ = self.rj(p, jac=False)
        return float(r @ r)

    def A_of(self, p):
        x = p[:self.m] + 1j * p[self.m:]
        return np.tensordot(x, self.E, axes=1)


def lm(prob, p0, maxit=300):
    p = p0.copy()
    r, J = prob.rj(p)
    f = float(r @ r)
    lam = 1e-2
    hist = [f]
    it = 0
    for it in range(maxit):
        if f < 1e-30:
            break
        g = J.T @ r
        H = J.T @ J
        dH = np.diag(H).copy() + 1e-14
        ok = False
        for _ in range(25):
            try:
                dp = np.linalg.solve(H + lam * np.diag(dH), -g)
            except np.linalg.LinAlgError:
                lam *= 10
                continue
            r2, _ = prob.rj(p + dp, jac=False)
            f2 = float(r2 @ r2)
            if f2 < f:
                p = p + dp
                r, J = prob.rj(p)
                f = float(r @ r)
                lam = max(lam / 5, 1e-12)
                ok = True
                break
            lam *= 5
        if not ok:
            break
        hist.append(f)
        if it > 60 and f > 1e-8 and hist[-41] - f < 1e-9 * hist[-41]:
            break
    return p, f, it + 1


def polieren(prob, p, n=30):
    best_D, best_p = prob.defect(p), p.copy()
    for _ in range(n):
        r, J = prob.rj(p)
        dp = np.linalg.lstsq(J, -r, rcond=1e-12)[0]
        p = p + dp
        D = prob.defect(p)
        if D < best_D:
            best_D, best_p = D, p.copy()
        if best_D < 1e-29:
            break
    return best_D, best_p


# ---------------------------------------------------------------- Spektrum und Einordnung
def W_at(freqs, A, u):
    s = A.shape[-1]
    ph = np.exp(1j * (np.atleast_2d(u) @ np.asarray(freqs).T))
    return (ph @ A.reshape(len(freqs), s * s)).reshape(-1, s, s)


def dW_at(freqs, A, u):
    # dW/dk_j bei u (k = sqrt3 u): sum_f (i f_j / sqrt3) e^{i u.f} A_f
    F = np.asarray(freqs, float)
    ph = np.exp(1j * (F @ np.asarray(u, float)))
    return [np.tensordot(1j * F[:, j] / SQ3 * ph, A, axes=1) for j in range(3)]


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


def kommutierend(freqs, A, n=6):
    U = np.random.default_rng(12345).uniform(0, 2 * np.pi, size=(2 * n, 3))
    W = W_at(freqs, A, U)
    return float(max(np.abs(W[2 * i] @ W[2 * i + 1] - W[2 * i + 1] @ W[2 * i]).max() for i in range(n)))


def rel_spectrum_span(freqs, A, N=12):
    ph = np.sort(np.angle(np.linalg.eigvals(W_at(freqs, A, grid_u(N)))), axis=1)
    gaps = np.sort(np.diff(np.concatenate([ph, ph[:, :1] + 2 * np.pi], axis=1), axis=1), axis=1)
    return float((gaps.max(0) - gaps.min(0)).max())


def cluster_branches(freqs, A, u_pts, phc, m):
    rel = np.angle(np.linalg.eigvals(W_at(freqs, A, u_pts)) * np.exp(-1j * phc))
    idx = np.argsort(np.abs(rel), axis=1)[:, :m]
    return np.sort(np.take_along_axis(rel, idx, axis=1), axis=1)


def cluster_zerlegung(W0, tol=1e-7):
    Tm, Z = schur(W0, output="complex")
    ph = np.angle(np.diag(Tm))
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
    out = []
    for g in groups.values():
        out.append((float(np.angle(np.mean(np.exp(1j * ph[g])))), Z[:, g]))
    return out, float(np.abs(Tm - np.diag(np.diag(Tm))).max())


def linear_analyse(freqs, A, u0, Q):
    # exakte erste Ordnung: G_j = Q^dagger W(u0)^dagger dW/dk_j Q / i auf dem Clusterraum
    W0 = W_at(freqs, A, u0[None, :])[0]
    dW = dW_at(freqs, A, u0)
    G = []
    for j in range(3):
        g = Q.conj().T @ W0.conj().T @ dW[j] @ Q / 1j
        G.append((g + g.conj().T) / 2)
    halb = []
    mitte = []
    for n in DIRS126:
        ev = np.linalg.eigvalsh(n[0] * G[0] + n[1] * G[1] + n[2] * G[2])
        halb.append((ev[-1] - ev[0]) / 2)
        mitte.append(abs(ev.mean()))
    nG = max(float(np.abs(g).max()) for g in G)
    kom = max(float(np.abs(G[i] @ G[j] - G[j] @ G[i]).max()) for i in range(3) for j in range(i + 1, 3))
    chir = None
    if Q.shape[1] == 2:
        Mv = np.array([[float(np.real(np.trace(G[i] @ PAULI[j]))) / 2 for j in range(3)] for i in range(3)])
        chir = float(np.linalg.det(Mv))
    return {"lin_min": float(min(halb)), "lin_max": float(max(halb)), "mitte_max": float(max(mitte)),
            "kom_rel": kom / max(nG ** 2, 1e-300), "chiral_det": chir}


def kruemmung(freqs, A, phc, m, h=1e-4, dirs=FIB400):
    # Richardson: kappa = 2 D(h) - D(2h), D(h) = [w(h n) + w(-h n) - 2 w(0)]/h^2, je sortiertem Zweig, k-Einheiten
    b0 = cluster_branches(freqs, A, np.zeros((1, 3)), phc, m)[0]

    def D(hh):
        bp = cluster_branches(freqs, A, hh * dirs / SQ3, phc, m)
        bm = cluster_branches(freqs, A, -hh * dirs / SQ3, phc, m)
        return (bp + bm - 2 * b0[None, :]) / hh ** 2

    kap = 2 * D(h) - D(2 * h)
    out = []
    for b in range(m):
        mu = float(kap[:, b].mean())
        out.append({"mittel": mu, "std_rel": float(kap[:, b].std() / max(abs(mu), 1e-300)),
                    "spannweite_rel": float((kap[:, b].max() - kap[:, b].min()) / max(abs(mu), 1e-300))})
    return out


def analyse_punkt(freqs, A, u0, lifts=None, mit_kruemmung=True):
    W0 = W_at(freqs, A, u0[None, :])[0]
    cl, schur_rest = cluster_zerlegung(W0)
    phs = [c for (c, _) in cl]
    res = {"schur_rest": schur_rest, "cluster": []}
    for i, (c, Q) in enumerate(cl):
        others = [abs(np.angle(np.exp(1j * (c - c2)))) for j, (c2, _) in enumerate(cl) if j != i]
        e = {"phase": c, "m": int(Q.shape[1]), "halbabstand": float(min(others) / 2) if others else float(np.pi)}
        e.update(linear_analyse(freqs, A, u0, Q))
        e["typ"] = "linear" if e["lin_min"] > 1e-6 else ("quadratisch" if e["lin_max"] <= 1e-6 else "gemischt")
        if lifts is not None:
            P = Q @ Q.conj().T
            Vx, Vy, V3 = lifts
            e["Vx2_plus_I"] = float(np.abs(P @ Vx @ Vx @ P + P).max())
            K = Vx @ Vy @ Vx.conj().T @ Vy.conj().T
            e["K_plus_I"] = float(np.abs(P @ K @ P + P).max())
            e["V3hoch3_plus_I"] = None if V3 is None else float(np.abs(P @ np.linalg.matrix_power(V3, 3) @ P + P).max())
        if mit_kruemmung and e["typ"] == "quadratisch":
            e["kruemmung"] = kruemmung(freqs, A, c, e["m"])
        res["cluster"].append(e)
    res["luecke"] = float(min(e["halbabstand"] for e in res["cluster"]))
    return res, phs


def implementing(A, perm, s):
    rows = []
    Is = np.eye(s)
    for i in range(len(A)):
        rows.append(np.kron(A[i].T, Is) - np.kron(Is, A[perm[i]]))
    _, sv, vh = np.linalg.svd(np.concatenate(rows))
    U = vh.conj()[-1].reshape(s, s, order="F")
    nrm = np.sqrt(max(np.trace(U.conj().T @ U).real / s, 1e-300))
    U = U / nrm
    return float(sv[-1]), float(sv[-2]), int(np.sum(sv < 1e-8)), U


def am_treffer(A, slots, s):
    out = {}
    Us = {}
    for lab, R in (("C2x", C2X), ("C2y", C2Y), ("C3", R3)):
        p = perm_on(slots, R)
        smin, s2, nnull, U = implementing(A, p, s)
        out[lab] = {"s_min": smin, "s_2": s2, "nullraum": nnull}
        Us[lab] = U
    K = Us["C2x"] @ Us["C2y"] @ Us["C2x"].conj().T @ Us["C2y"].conj().T
    out["K_plus_I"] = float(np.abs(K + np.eye(s)).max())
    out["K_minus_I"] = float(np.abs(K - np.eye(s)).max())
    eind = all(out[l]["s_min"] <= 1e-8 and out[l]["s_2"] >= 1e-4 for l in ("C2x", "C2y"))
    out["wirkung"] = ("projektiv" if out["K_plus_I"] <= 1e-8 else "linear" if out["K_minus_I"] <= 1e-8 else "mehrdeutig") if eind else "mehrdeutig"
    inv = [int(np.where((slots == -v).all(1))[0][0]) for v in slots]
    smin, s2, nnull, _ = implementing(A, inv, s)
    out["inversion"] = {"s_min": smin, "s_2": s2, "nullraum": nnull, "symmetrisch": bool(smin <= 1e-8)}
    return out


SPEZIAL = {"H": SQ3 * np.pi * np.array([1.0, 0, 0]), "P": SQ3 * np.pi / 2 * np.array([1.0, 1, 1]),
           "P'": -SQ3 * np.pi / 2 * np.array([1.0, 1, 1])}
PFAD_BCC = [("Γ", np.zeros(3)), ("H", SQ3 * np.pi * np.array([1.0, 0, 0])), ("N", SQ3 * np.pi * np.array([0.5, 0.5, 0])),
            ("Γ", np.zeros(3)), ("P", SQ3 * np.pi * np.array([0.5, 0.5, 0.5])), ("H", SQ3 * np.pi * np.array([1.0, 0, 0]))]


def einordnen(slots, A, s, lifts, voll=True):
    out = {}
    kom = kommutierend(slots, A)
    span = rel_spectrum_span(slots, A)
    out["kommutator_W"], out["rel_spektrum_spannweite"] = kom, span
    # trivial (nach Rauch 1 ergaenzt): Spruenge mit Gesamtgewicht < 1e-10 (nur Vor-Ort-Term, W fast konstant),
    # vertauschende W(k) oder konstantes relatives Spektrum
    out["gewicht_spruenge"] = float(np.sum(np.abs(A[:8]) ** 2))
    out["trivial"] = bool(kom < 1e-8 or span < 1e-8 or out["gewicht_spruenge"] < 1e-10)
    g, _ = analyse_punkt(slots, A, np.zeros(3), lifts)
    out["gamma"] = g
    cl = g["cluster"]
    out["alle_cluster_2fach"] = all(e["m"] == 2 for e in cl)
    out["alle_quadratisch"] = all(e["typ"] == "quadratisch" for e in cl)
    out["kegel_0"] = any(e["typ"] == "linear" for e in cl)
    out["luecke"] = g["luecke"]
    spin = all((e.get("K_plus_I", 1) <= 1e-10 and e.get("Vx2_plus_I", 1) <= 1e-10 and
                (e.get("V3hoch3_plus_I") is None or e["V3hoch3_plus_I"] <= 1e-10)) for e in cl)
    out["spin_halb_alle_cluster"] = bool(spin)
    out["massiv"] = bool((not out["trivial"]) and out["alle_cluster_2fach"] and out["alle_quadratisch"] and g["luecke"] > 1e-3)
    if out["massiv"]:
        out["kruemmung_streuung_max"] = float(max(b["std_rel"] for e in cl for b in e["kruemmung"]))
        out["isotrop"] = bool(out["kruemmung_streuung_max"] <= 1e-3)
    if out["trivial"]:
        out["klasse"] = "trivial"
    elif out["massiv"]:
        out["klasse"] = "massiv"
    elif out["kegel_0"]:
        out["klasse"] = "Kegel bei 0"
    else:
        out["klasse"] = "sonst"
    if voll and not out["trivial"]:
        out["am_treffer"] = am_treffer(A, slots, s)
        sp = {}
        for lab, kk in SPEZIAL.items():
            r, _ = analyse_punkt(slots, A, kk / SQ3, None, mit_kruemmung=False)
            sp[lab] = {"luecke": r["luecke"], "cluster": [{"phase": e["phase"], "m": e["m"], "typ": e["typ"],
                                                            "lin_min": e["lin_min"], "lin_max": e["lin_max"]} for e in r["cluster"]]}
        out["spezialpunkte"] = sp
    return out


def cplx(a):
    a = np.asarray(a)
    return {"re": a.real.round(15).tolist(), "im": a.imag.round(15).tolist()}


def kovarianz_abw(A, slots, T, Vs, Pi=None):
    dev = 0.0
    for (R, _, _), V in zip(T, Vs):
        p = perm_on(slots, R)
        for i in range(len(slots)):
            dev = max(dev, float(np.abs(V @ A[i] @ V.conj().T - A[p[i]]).max()))
    if Pi is not None:
        for i, v in enumerate(slots):
            j = int(np.where((slots == -v).all(1))[0][0])
            dev = max(dev, float(np.abs(Pi @ A[i] @ Pi.conj().T - A[j]).max()))
    return dev


# ---------------------------------------------------------------- Suche je Fall
def fall(name, form, Vs, T, lifts, s, nstarts, seed, w0=False, Pi=None, maxit=300, n_voll=60):
    t0 = time.time()
    slots = S_BCC if form == "N" else SLOTS_O
    rots = [R for (R, _, _) in T]
    perms = [perm_on(slots, R) for R in rots]
    Vg = list(Vs)
    if form == "P":
        perms = perms + [[INV_PERM[q] for q in p] for p in perms]
        Vg = Vg + [Pi @ V for V in Vs]
    E, perr = covariant_basis(len(slots), perms, Vg, s)
    st = {"form": form, "w0": w0, "dim_komplex": int(E.shape[0]), "projektor_abw": perr, "starts": nstarts,
          "treffer": 0, "hits": [], "repr": None}
    if E.shape[0] == 0:
        st.update({"leer": True, "D_min": None, "D_median": None, "laufzeit_s": time.time() - t0})
        return st
    prob = Fast(E, slots, s, rots, w0)
    st["bahnen"] = [[list(d), w] for (d, w) in prob.reps]
    st["n_differenzen"] = prob.n_diff
    full = Unit(slots, s)
    rng = np.random.default_rng(seed)
    res = []
    for _ in range(nstarts):
        x0 = rng.standard_normal(E.shape[0]) + 1j * rng.standard_normal(E.shape[0])
        x0 *= np.sqrt(s) / np.linalg.norm(x0)
        p, f, nit = lm(prob, np.concatenate([x0.real, x0.imag]), maxit)
        res.append((f, p, nit))
    D = np.array([r[0] for r in res])
    st.update({"D_min": float(D.min()), "D_median": float(np.median(D)), "D_max": float(D.max()),
               "treffer": int(np.sum(D < 1e-10)), "iter_median": float(np.median([r[2] for r in res])),
               "log10D_alle": np.log10(np.maximum(D, 1e-40)).round(3).tolist(), "t_suche_s": time.time() - t0})
    n_v = 0
    for (Dv, p, _) in res:
        if Dv >= 1e-10:
            continue
        D_pol = None
        if Dv > 1e-28:
            D_pol, p_pol = polieren(prob, p)
            if D_pol < Dv:
                p = p_pol
        A = prob.A_of(p)
        h = {"D": Dv, "D_poliert": D_pol, "D_voll": full.defect(A),
             "kovarianz_abw": kovarianz_abw(A, slots, T, Vs, Pi if form == "P" else None)}
        if form != "N":
            h["gewicht_vor_ort"] = float(np.sum(np.abs(A[8]) ** 2))
        h["gewicht_S+_S-"] = [float(np.sum(np.abs(A[:4]) ** 2)), float(np.sum(np.abs(A[4:8]) ** 2))]
        voll = n_v < n_voll
        h["klass"] = einordnen(slots, A, s, lifts, voll=voll)
        if voll and not h["klass"]["trivial"]:
            n_v += 1
        h["klasse"] = h["klass"]["klasse"]
        st["hits"].append(h)
        rang = {"massiv": 3, "Kegel bei 0": 2, "sonst": 1, "trivial": 0}[h["klasse"]]
        if st["repr"] is None or rang > st["repr"]["rang"]:
            st["repr"] = {"rang": rang, "klasse": h["klasse"], "freqs": slots.tolist(), "A": cplx(A)}
    st["klassen"] = {k: sum(1 for h in st["hits"] if h["klasse"] == k) for k in ("massiv", "Kegel bei 0", "sonst", "trivial")}
    st["laufzeit_s"] = time.time() - t0
    return st


# ---------------------------------------------------------------- Teil 0: Quelle und Konstruktionen
def weyl_quelle(sign):
    z = (1 + sign * 1j) / 4
    zc = np.conj(z)
    Ap = [np.array([[zc, 0], [zc, 0]]), np.array([[0, zc], [0, zc]]), np.array([[0, -zc], [0, zc]]),
          np.array([[zc, 0], [-zc, 0]])]
    Am = [np.array([[0, -z], [0, z]]), np.array([[z, 0], [-z, 0]]), np.array([[z, 0], [z, 0]]),
          np.array([[0, z], [0, z]])]
    return np.array(Ap + Am, dtype=complex)  # Slots S_BCC = (t_1..t_4, -t_1..-t_4), Eq. (24)


def dirac_quelle(sign, m):
    # Eq. (36): E_k = ((n A_k, i m I), (i m I, n A_k^dagger)); A_k^dagger traegt A_h^dagger in Slot -h
    n = np.sqrt(1 - m * m)
    Aw = weyl_quelle(sign)
    E = np.zeros((9, 4, 4), dtype=complex)
    for i in range(8):
        j = INV_PERM[i]
        E[i, :2, :2] = n * Aw[i]
        E[i, 2:, 2:] = n * Aw[j].conj().T
    E[8, :2, 2:] = 1j * m * I2
    E[8, 2:, :2] = 1j * m * I2
    return E


def monomial_basis(T, V4):
    # Ind chi (Stabilisator C_3 von t_1) in 2+2' = U + omega U: p_1 = (v_2 + v_2')/sqrt2, v Eigenvektoren zu e^{i pi/3}
    iR = [i for i, (R, _, _) in enumerate(T) if key3(R) == key3(R3)][0]
    VR = V4[iR]
    lam = np.exp(1j * np.pi / 3)
    vs = []
    for b in range(2):
        blk = VR[2 * b:2 * b + 2, 2 * b:2 * b + 2]
        w, v = np.linalg.eig(blk)
        k = int(np.argmin(np.abs(w - lam)))
        vec = np.zeros(4, dtype=complex)
        vec[2 * b:2 * b + 2] = v[:, k] / np.linalg.norm(v[:, k])
        vs.append(vec)
    p1 = (vs[0] + vs[1]) / np.sqrt(2)
    ps = []
    for a in range(4):
        g = [i for i, (R, _, _) in enumerate(T) if tuple(R @ TV[0]) == tuple(TV[a])][0]
        ps.append(V4[g] @ p1)
    Pm = np.array(ps).T
    return Pm, float(np.abs(Pm.conj().T @ Pm - np.eye(4)).max())


def konstruktionen(T, m, rng):
    V4 = spinor_rep(T, ["2", "2'"])
    Pm, gram = monomial_basis(T, V4)
    P2 = np.diag([1, 1, 0, 0]).astype(complex)
    P2s = np.diag([0, 0, 1, 1]).astype(complex)
    proj = [np.outer(Pm[:, a], Pm[:, a].conj()) for a in range(4)]
    n = np.sqrt(1 - m * m)
    out = {}

    def dirac_aus(C):
        E = np.zeros((9, 8, 8), dtype=complex)
        for a in range(4):
            E[a, :4, :4] = n * C @ proj[a]
            E[4 + a, 4:, 4:] = n * proj[a] @ C.conj().T
        E[8, :4, 4:] = 1j * m * np.eye(4)
        E[8, 4:, :4] = 1j * m * np.eye(4)
        return E

    out["a_spiegel"] = dirac_aus(P2 - P2s)
    al, be = rng.uniform(0, 2 * np.pi, 2)
    out["a_allgemein"] = dirac_aus(np.exp(1j * al) * P2 + np.exp(1j * be) * P2s)
    N = np.array([[n, 1j * m], [1j * m, n]])
    M = np.kron(N, P2 - P2s)
    Eb = np.zeros((9, 8, 8), dtype=complex)
    for a in range(4):
        D = np.zeros((8, 8), dtype=complex)
        D[:4, :4] = proj[a]
        Eb[a] = M @ D
        D = np.zeros((8, 8), dtype=complex)
        D[4:, 4:] = proj[a]
        Eb[4 + a] = M @ D
    out["b_muenze_verschiebung"] = Eb
    return out, gram, (al, be)


def lesepruefung_eq37(E, sign, m, rng):
    n = np.sqrt(1 - m * m)
    ks = rng.uniform(-3, 3, size=(50, 3))
    ph = np.sort(np.abs(np.angle(np.linalg.eigvals(W_at(SLOTS_O, E, ks / SQ3)))), axis=1)
    c, sn = np.cos(ks / SQ3), np.sin(ks / SQ3)
    out = {}
    for lab, sg in (("d_minus", -1), ("d_plus", 1)):
        d = c.prod(1) + sg * sn.prod(1)
        w = np.arccos(np.clip(n * d, -1, 1))
        out[lab] = float(np.abs(ph - w[:, None]).max())
    return out


def teil0(T, ginfo, nstarts, seed):
    out = {}
    lifts_L2 = (np.kron(I2, -1j * SX), np.kron(I2, -1j * SY), None)
    VL2 = [np.eye(4, dtype=complex), np.kron(I2, -1j * SX), np.kron(I2, -1j * SY), np.kron(I2, -1j * SZ)]
    rotsL2 = [np.eye(3, dtype=int), C2X, C2Y, C2Z]
    rng = np.random.default_rng(seed)
    q = {}
    for sign, lab in ((1, "E+"), (-1, "E-")):
        for m in (0.1, 0.3, 0.6):
            E = dirac_quelle(sign, m)
            u = Unit(SLOTS_O, 4)
            co = u.coeffs(E)
            Wg = W_at(SLOTS_O, E, grid_u(16))
            gdev = float(np.abs(np.einsum("nji,njk->nik", Wg.conj(), Wg) - np.eye(4)).max())
            kov = 0.0
            for R, V in zip(rotsL2, VL2):
                p = perm_on(SLOTS_O, R)
                for i in range(9):
                    kov = max(kov, float(np.abs(V @ E[i] @ V.conj().T - E[p[i]]).max()))
            kl = einordnen(SLOTS_O, E, 4, lifts_L2)
            n = np.sqrt(1 - m * m)
            soll = n / (3 * m)
            km = [b["mittel"] for e in kl["gamma"]["cluster"] if "kruemmung" in e for b in e["kruemmung"]]
            q[f"{lab}|m={m}"] = {"unitaer_koeff_max": float(np.abs(co).max()), "unitaer_gitter_max": gdev,
                                 "kovarianz_L2_abw": kov, "klass": kl, "luecke_soll_arcsin_m": float(np.arcsin(m)),
                                 "kruemmung_soll_n_durch_3m": soll,
                                 "kruemmung_abw_rel_max": float(max(abs(abs(x) - soll) / soll for x in km)) if km else None,
                                 "lesepruefung_eq37": lesepruefung_eq37(E, sign, m, rng),
                                 "repr": {"freqs": SLOTS_O.tolist(), "A": cplx(E)}}
    out["quelle_dirac"] = q
    # Suchkontrolle: T:2+2' (s = 4, Form N) wie QCA-DIAMANT-4 Teil B
    V4 = spinor_rep(T, ["2", "2'"])
    lifts4 = (V4[ginfo["idx_C2x"]], V4[ginfo["idx_C2y"]], V4[ginfo["idx_R3"]])
    st = fall("T:2+2'", "N", V4, T, lifts4, 4, nstarts, seed + 1)
    out["suchkontrolle_T:2+2'"] = st
    # Konstruktionen (Teil B-K), s = 8, V = (2+2') + (2+2')
    V8 = [bdiag(V, V) for V in V4]
    lifts8 = (V8[ginfo["idx_C2x"]], V8[ginfo["idx_C2y"]], V8[ginfo["idx_R3"]])
    kons = {}
    for m in (0.1, 0.3, 0.6):
        ks, gram, ab = konstruktionen(T, m, rng)
        for lab, E in ks.items():
            u = Unit(SLOTS_O, 8)
            kons[f"{lab}|m={m}"] = {"unitaer_koeff_max": float(np.abs(u.coeffs(E)).max()),
                                    "kovarianz_T_abw": kovarianz_abw(E, SLOTS_O, T, V8),
                                    "monomial_gram_abw": gram, "alpha_beta": list(ab) if lab == "a_allgemein" else None,
                                    "klass": einordnen(SLOTS_O, E, 8, lifts8),
                                    "repr": {"freqs": SLOTS_O.tolist(), "A": cplx(E)}}
            if lab == "a_spiegel":
                n = np.sqrt(1 - m * m)
                kons[f"{lab}|m={m}"]["kruemmung_soll_n_durch_9m"] = n / (9 * m)
    out["konstruktionen"] = kons
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--teil", choices=["0", "A", "B"], required=True)
    ap.add_argument("--modus", choices=["rauch", "haupt"], required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--formen", default="N,O,P")
    ap.add_argument("--faelle", default="alle")
    ap.add_argument("--starts", type=int, default=None)
    ap.add_argument("--maxit", type=int, default=300)
    args = ap.parse_args()
    t_start = time.time()
    seedbase = 3900 if args.modus == "rauch" else 39
    T, ginfo = gruppen()
    res = {"modus": args.modus, "teil": args.teil, "saat_basis": seedbase, "formen_arg": args.formen,
           "faelle_arg": args.faelle, "gruppen": ginfo, "numpy": np.__version__}
    rng = np.random.default_rng(seedbase)
    # Codepruefung: Fast gegen Unit (volle Differenzen) an zufaelligen kovarianten Punkten
    chk = []
    for teile, form in ((["2", "2'"], "O"), (["2", "2", "2'", "2'"], "P"), (["2", "2", "2'", "2''"], "N")):
        Vs = spinor_rep(T, teile)
        s = len(teile) * 2
        slots = S_BCC if form == "N" else SLOTS_O
        perms = [perm_on(slots, R) for (R, _, _) in T]
        Vg = list(Vs)
        if form == "P":
            Pi = bdiag(np.kron(SX, I2), np.kron(SX, I2)).real.astype(complex)
            perms = perms + [[INV_PERM[q] for q in p] for p in perms]
            Vg = Vg + [Pi @ V for V in Vs]
        E, _ = covariant_basis(len(slots), perms, Vg, s)
        fp = Fast(E, slots, s, [R for (R, _, _) in T])
        x = rng.standard_normal(2 * E.shape[0])
        A = fp.A_of(x)
        d1, d2 = fp.defect(x), Unit(slots, s).defect(A)
        r, J = fp.rj(x)
        eps = 1e-7
        k = int(rng.integers(len(x)))
        x2 = x.copy()
        x2[k] += eps
        r2, _ = fp.rj(x2, jac=False)
        jdev = float(np.abs((r2 - r) / eps - J[:, k]).max() / max(np.abs(J[:, k]).max(), 1e-300))
        chk.append({"fall": "+".join(teile) + "|" + form, "defekt_rel": abs(d1 - d2) / d2, "jacobi_rel": jdev})
    res["codepruefung"] = chk
    reps8 = {}
    for kk, nm in KLASSEN8.items():
        reps8[kk] = ("T:" + nm, spinor_rep(T, nm.split("+")))
    res["darstellungen"] = {kk: dict(name=nm, **rep_info(T, Vs, ginfo)) for kk, (nm, Vs) in reps8.items()}
    V22 = spinor_rep(T, ["2", "2"])
    res["darstellungen"]["A:T:2+2"] = dict(name="T:2+2", **rep_info(T, V22, ginfo))
    res["darstellungen"]["0:T:2+2'"] = dict(name="T:2+2'", **rep_info(T, spinor_rep(T, ["2", "2'"]), ginfo))
    faelle = {}
    if args.teil == "0":
        nst = args.starts if args.starts else (10 if args.modus == "rauch" else 40)
        res["teil0"] = teil0(T, ginfo, nst, seedbase * 10000 + 1)
    elif args.teil == "A":
        nst = args.starts if args.starts else (20 if args.modus == "rauch" else 200)
        lifts = (V22[ginfo["idx_C2x"]], V22[ginfo["idx_C2y"]], V22[ginfo["idx_R3"]])
        for i, (form, w0) in enumerate((("N", False), ("N", True), ("O", False))):
            lab = form + ("-w0" if w0 else "")
            if args.formen != "alle" and lab not in args.formen.split(","):
                continue
            st = fall("T:2+2", form, V22, T, lifts, 4, nst, seedbase * 10000 + 2000 + 10 * i, w0=w0, maxit=args.maxit)
            faelle["A|" + lab + "|T:2+2"] = st
            print(f"[A] {lab} T:2+2: dim={st['dim_komplex']} treffer={st['treffer']} klassen={st.get('klassen')} "
                  f"Dmin={st['D_min']} t={st['laufzeit_s']:.1f}s", flush=True)
    else:
        nst = args.starts if args.starts else (5 if args.modus == "rauch" else 40)
        wahl = list(KLASSEN8.keys()) if args.faelle == "alle" else args.faelle.split(",")
        for form in args.formen.split(","):
            for ci, kk in enumerate(KLASSEN8.keys()):
                if kk not in wahl:
                    continue
                nm, Vs = reps8[kk]
                Pi = None
                if form == "P":
                    if kk == "K4":
                        Pi = bdiag(np.kron(SX, I2), np.kron(SX, I2)).real.astype(complex)
                    elif kk == "K5":
                        Pi = bdiag(np.kron(SX, I2), np.eye(4)).real.astype(complex)
                    else:
                        continue
                lifts = (Vs[ginfo["idx_C2x"]], Vs[ginfo["idx_C2y"]], Vs[ginfo["idx_R3"]])
                seed = seedbase * 10000 + 3000 + 100 * "NOP".index(form) + ci
                st = fall(nm, form, Vs, T, lifts, 8, nst, seed, Pi=Pi, maxit=args.maxit)
                st["klasse_K"] = kk
                faelle["B|" + form + "|" + kk] = st
                print(f"[B] {form} {kk} {nm}: dim={st['dim_komplex']} treffer={st['treffer']} klassen={st.get('klassen')} "
                      f"Dmin={st['D_min']} iter={st.get('iter_median')} t={st['laufzeit_s']:.1f}s", flush=True)
    res["faelle"] = faelle
    res["laufzeit_s"] = time.time() - t_start
    with open(args.out, "w") as fh:
        json.dump(res, fh, indent=1, default=lambda o: o.tolist() if hasattr(o, "tolist") else str(o))
    print(f"fertig, {res['laufzeit_s']:.1f} s", flush=True)


if __name__ == "__main__":
    sys.exit(main())
