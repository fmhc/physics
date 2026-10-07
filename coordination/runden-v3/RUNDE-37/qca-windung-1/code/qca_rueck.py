#!/usr/bin/env python3
# QCA-BCC-RUECK-1 (Runde 38/39, fmhc-physics). Code-Agent fuer die Leitung claude-primary.
# Frage: Gibt es T-kovariante unitaere Automaten auf BCC (4 und 8 Zustaende), die in beide Richtungen springen
# (A_h != 0 <=> A_-h != 0, Quelle Abschn. II; D'Ariano/Erba/Perinotti 2017, S. 2: "A_h != 0 for all h in S")?
# Baut auf RUNDE-37/qca-dirac-t-1/code/qca_dirac.py (Gruppen T/2T, kovarianter Unterraum, Bahn-Residuen, LM-Loeser,
# Einordnung) und RUNDE-37/qca-diamant-4/code/qca_diamant.py (Isotropie) auf. Neu:
#   - Nebenbedingung Rueckspruenge als fester Gewichtsanteil w = J+/(J+ + J-) (Varianten r50, r20, r05),
#     bei Form O zusaetzlich Sprunggewicht J+ + J- = s/2 (schliesst reine Vor-Ort-Loesungen aus)
#   - Rueckspruung-Pruefung je Matrix und je Block (Kommutant der A_h: unzerlegbare Teilautomaten)
#   - Spektralvergleich mit dem Weyl-Automaten der Quelle (Kontrolle QR0)
#   - Konstruktion "Muenze x (S+ + S-)" mit 8 Zustaenden (Teil 0, beschreibend)
# Teil 0: QR0 (L2:Pauli, s = 2), Weyl-Referenz, Konstruktionen. Teil 4: s = 4, alle Darstellungsklassen von T/2T
# (ohne gemischte; Schreibtisch). Teil 8: s = 8, Spinorklassen K1..K5.
# Start nur auf der .69 ueber kleintest.sh.
import argparse
import json
import sys
import time

import numpy as np
from scipy.linalg import expm, schur

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
INV8 = [4, 5, 6, 7, 0, 1, 2, 3]
IRR = {"2": 0, "2'": 1, "2''": 2}
KLASSEN8 = {"K1": "2+2+2+2", "K2": "2+2+2+2'", "K3": "2+2+2+2''", "K4": "2+2+2'+2'", "K5": "2+2+2'+2''"}
PAULI_V4 = [I2.copy(), 1j * SX, 1j * SY, 1j * SZ]
L2_ROTS = [np.eye(3, dtype=int), C2X, C2Y, C2Z]
VARIANTEN = {"frei": None, "r50": 0.5, "r20": 0.2, "r05": 0.05}
FORMEN = {"N": S_BCC, "O": SLOTS_O}
NORM_SCHWELLE = 1e-3      # Mindestnorm (Frobenius) relativ zum groessten A_h (PLAN.md Abschnitt 1)
GUELTIG_D = 1e-20         # gueltiger Treffer: voller Defekt nach Nachpolitur (PLAN.md Abschnitt 1)


def key3(M):
    return tuple(int(x) for x in np.asarray(M).ravel())


# ---------------------------------------------------------------- Gruppen (aus qca_dirac.py)
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
    info = {"T_ordnung": len(T), "T_konsistenzfehler": fehler, "L2_ordnung": 4}
    su2 = su2_closure([-1j * SX, 0.5 * (I2 - 1j * (SX + SY + SZ))])
    info["2T_ordnung"] = len(su2)
    kern = [U for U in su2 if adjoint_dev(np.eye(3, dtype=int), U) < 1e-10]
    info["2T_kern_ist_pm_I"] = bool(len(kern) == 2 and all(min(np.abs(U - I2).max(), np.abs(U + I2).max()) < 1e-12 for U in kern))
    info["spinor_SO3_abw"] = max(adjoint_dev(R, U) for (R, U, _) in T)
    idx = {key3(R): i for i, (R, _, _) in enumerate(T)}
    info["idx_C2x"], info["idx_C2y"], info["idx_R3"] = idx[key3(C2X)], idx[key3(C2Y)], idx[key3(R3)]
    info["U_C2x_quadrat_plus_I"] = float(np.abs(T[idx[key3(C2X)]][1] @ T[idx[key3(C2X)]][1] + I2).max())
    info["U_R3_hoch3_plus_I"] = float(np.abs(np.linalg.matrix_power(T[idx[key3(R3)]][1], 3) + I2).max())
    info["wirkung_auf_slots_ok"] = all(perm_on(SLOTS_O, R) is not None for (R, _, _) in T) and \
        all(perm_on(SLOTS_O, R) is not None for R in L2_ROTS)
    return T, info


def spinor_rep(T, teile):
    return [bdiag(*[OMEGA ** (IRR[p] * q) * U for p in teile]) for (_, U, q) in T]


def darstellungen(T):
    reps = {}
    einsdim = {"1+1+1+1": [0, 0, 0, 0], "1+1+1+1'": [0, 0, 0, 1], "1+1+1+1''": [0, 0, 0, 2],
               "1+1+1'+1'": [0, 0, 1, 1], "1+1+1'+1''": [0, 0, 1, 2]}
    for nm, ms in einsdim.items():
        reps["T:" + nm] = ("linear", [np.diag([OMEGA ** (m * q) for m in ms]).astype(complex) for (_, _, q) in T])
    reps["T:1+3"] = ("linear", [bdiag(np.eye(1, dtype=complex), R.astype(complex)) for (R, _, _) in T])
    reps["T:1'+3"] = ("linear", [bdiag(np.array([[OMEGA ** q]]), R.astype(complex)) for (R, _, q) in T])
    reps["T:2+2"] = ("projektiv", spinor_rep(T, ["2", "2"]))
    reps["T:2+2'"] = ("projektiv", spinor_rep(T, ["2", "2'"]))
    reps["T:2+2''"] = ("projektiv", spinor_rep(T, ["2", "2''"]))
    for kk, nm in KLASSEN8.items():
        reps[kk] = ("projektiv", spinor_rep(T, nm.split("+")))
    return reps


FAELLE4 = ["T:1+1+1+1", "T:1+1+1+1'", "T:1+1+1+1''", "T:1+1+1'+1'", "T:1+1+1'+1''", "T:1+3", "T:1'+3", "T:2+2",
           "T:2+2'", "T:2+2''"]
FAELLE8 = list(KLASSEN8.keys())


def rep_check(rots, Vs):
    s = Vs[0].shape[0]
    Is = np.eye(s)
    idx = {key3(R): i for i, R in enumerate(rots)}
    maxdev, unit = 0.0, 0.0
    for i, A in enumerate(rots):
        unit = max(unit, float(np.abs(Vs[i].conj().T @ Vs[i] - Is).max()))
        for j, B in enumerate(rots):
            k = idx[key3(A @ B)]
            prod = Vs[i] @ Vs[j]
            c = np.trace(Vs[k].conj().T @ prod) / s
            maxdev = max(maxdev, float(np.abs(prod - c * Vs[k]).max()))
    Vx, Vy = Vs[idx[key3(C2X)]], Vs[idx[key3(C2Y)]]
    K = Vx @ Vy @ Vx.conj().T @ Vy.conj().T
    kl = "-I" if np.abs(K + Is).max() < 1e-12 else ("+I" if np.abs(K - Is).max() < 1e-12 else "anders")
    return {"projektiv_abw": maxdev, "unitaer_abw": unit, "kommutator": kl}


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


# ---------------------------------------------------------------- Unitaritaet und Nebenbedingung
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
    """Residuen je Bahn der Differenzen unter rots x {+-1} (gewichtet, wie qca_dirac.py), dazu die Nebenbedingungen
    (1 - w) J+ - w J- = 0 (Rueckspruenge mit festem Anteil w) und J+ + J- = rho s (Form O)."""

    def __init__(self, E, freqs, s, rots, w=None, rho=None):
        self.E, self.m, self.s = E, E.shape[0], s
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
        self.sw = np.sqrt(np.array([wt for (_, wt) in reps], float))
        self.r0 = [r for r, (d, _) in enumerate(reps) if d == (0, 0, 0)][0]
        self.Is = np.eye(s)
        G = np.einsum("lnab,jnab->nlj", E.conj(), E)
        self.Gp, self.Gm = G[:4].sum(0), G[4:8].sum(0)
        self.extra = []
        if w is not None:
            self.extra.append(((1 - w) * self.Gp - w * self.Gm, 0.0))
        if rho is not None:
            self.extra.append((self.Gp + self.Gm, rho * s))

    def rj(self, p, jac=True):
        m, s = self.m, self.s
        x = p[:m] + 1j * p[m:]
        Y1 = np.tensordot(x.conj(), self.K, axes=([0], [1]))
        R = np.tensordot(x, Y1, axes=([0], [1]))
        R[self.r0] -= self.Is
        nd = R.shape[0]
        r = (np.concatenate([R.real.reshape(nd, -1), R.imag.reshape(nd, -1)], axis=1) * self.sw[:, None]).ravel()
        ex_r, ex_j = [], []
        for (Q, t) in self.extra:
            Qx = Q @ x
            ex_r.append(float(np.real(np.vdot(x, Qx))) - t)
            ex_j.append(np.concatenate([2 * Qx.real, 2 * Qx.imag]))
        if ex_r:
            r = np.concatenate([r, np.array(ex_r)])
        if not jac:
            return r, None
        Y2 = np.tensordot(self.K, x, axes=([2], [0]))
        Jd = np.concatenate([Y1 + Y2, 1j * (Y1 - Y2)], axis=1)  # (nd, 2m, s, s)
        Jr = Jd.real.reshape(nd, 2 * m, s * s).transpose(0, 2, 1)
        Ji = Jd.imag.reshape(nd, 2 * m, s * s).transpose(0, 2, 1)
        J = (np.concatenate([Jr, Ji], axis=1) * self.sw[:, None, None]).reshape(-1, 2 * m)
        if ex_j:
            J = np.concatenate([J, np.array(ex_j)], axis=0)
        return r, J

    def defect(self, p):
        r, _ = self.rj(p, jac=False)
        return float(r @ r)

    def nebenbed(self, p):
        x = p[:self.m] + 1j * p[self.m:]
        return [float(abs(np.real(np.vdot(x, Q @ x)) - t)) for (Q, t) in self.extra]

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


# ---------------------------------------------------------------- Spektrum und Einordnung (aus qca_dirac.py)
def W_at(freqs, A, u):
    s = A.shape[-1]
    ph = np.exp(1j * (np.atleast_2d(u) @ np.asarray(freqs).T))
    return (ph @ A.reshape(len(freqs), s * s)).reshape(-1, s, s)


def dW_at(freqs, A, u):
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
    b0 = cluster_branches(freqs, A, np.zeros((1, 3)), phc, m)[0]

    def D(hh):
        bp = cluster_branches(freqs, A, hh * dirs / SQ3, phc, m)
        bm = cluster_branches(freqs, A, -hh * dirs / SQ3, phc, m)
        return (bp + bm - 2 * b0[None, :]) / hh ** 2

    kap = 2 * D(h) - D(2 * h)
    out = []
    for b in range(m):
        mu = float(kap[:, b].mean())
        out.append({"mittel": mu, "std_rel": float(kap[:, b].std() / max(abs(mu), 1e-300))})
    return out


def analyse_punkt(freqs, A, u0, lifts=None, mit_kruemmung=True):
    W0 = W_at(freqs, A, u0[None, :])[0]
    cl, schur_rest = cluster_zerlegung(W0)
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
        if mit_kruemmung and e["typ"] == "quadratisch" and e["m"] <= 4:
            e["kruemmung"] = kruemmung(freqs, A, c, e["m"])
        res["cluster"].append(e)
    res["luecke"] = float(min(e["halbabstand"] for e in res["cluster"]))
    return res


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
    out["C3_implementierbar"] = bool(out["C3"]["s_min"] <= 1e-8)
    inv = [int(np.where((slots == -v).all(1))[0][0]) for v in slots]
    smin, s2, nnull, _ = implementing(A, inv, s)
    out["inversion"] = {"s_min": smin, "s_2": s2, "nullraum": nnull, "symmetrisch": bool(smin <= 1e-8)}
    return out


SPEZIAL = {"H": SQ3 * np.pi * np.array([1.0, 0, 0]), "P": SQ3 * np.pi / 2 * np.array([1.0, 1, 1]),
           "P'": -SQ3 * np.pi / 2 * np.array([1.0, 1, 1])}
PFAD_BCC = [("Γ", np.zeros(3)), ("H", SQ3 * np.pi * np.array([1.0, 0, 0])), ("N", SQ3 * np.pi * np.array([0.5, 0.5, 0])),
            ("Γ", np.zeros(3)), ("P", SQ3 * np.pi * np.array([0.5, 0.5, 0.5])), ("H", SQ3 * np.pi * np.array([1.0, 0, 0]))]


def isotropie(freqs, A, phc, m, kabs):
    # aus qca_diamant.py: v(k^) = Spreizung des Clusters / (2 |k|) ueber 400 Fibonacci-Richtungen
    b = cluster_branches(freqs, A, kabs * FIB400 / SQ3, phc, m)
    v = (b[:, -1] - b[:, 0]) / (2 * kabs)
    return {"v_mittel": float(v.mean()), "std_rel": float(v.std() / max(v.mean(), 1e-300)),
            "spannweite_rel": float((v.max() - v.min()) / max(v.mean(), 1e-300))}


def bloecke(A, s, rng, tol=1e-8):
    # Kommutant der *-Algebra der A_h: unzerlegbare Teilautomaten (gemeinsame invariante Unterraeume)
    Is = np.eye(s)
    rows = []
    for Ah in A:
        for M in (Ah, Ah.conj().T):
            rows.append(np.kron(M.T, Is) - np.kron(Is, M))
    _, sv, vh = np.linalg.svd(np.concatenate(rows))
    nullidx = [i for i in range(len(sv)) if sv[i] <= tol]
    luecke = float(min([sv[i] for i in range(len(sv)) if sv[i] > tol], default=float("nan")))
    null = [vh.conj()[i].reshape(s, s, order="F") for i in nullidx]
    if len(null) <= 1:
        Qs = [np.eye(s, dtype=complex)]
    else:
        coef = rng.standard_normal(len(null))
        H = sum(c * (X + X.conj().T) / 2 for c, X in zip(coef, null))
        ev, U = np.linalg.eigh(H)
        sc = max(1.0, float(np.abs(ev).max()))
        groups, cur = [], [0]
        for i in range(1, s):
            if ev[i] - ev[i - 1] < 1e-6 * sc:
                cur.append(i)
            else:
                groups.append(cur)
                cur = [i]
        groups.append(cur)
        Qs = [U[:, g] for g in groups]
    inv_abw = 0.0
    for Q in Qs:
        Pc = np.eye(s) - Q @ Q.conj().T
        for Ah in A:
            inv_abw = max(inv_abw, float(np.abs(Pc @ Ah @ Q).max()))
    return {"kommutant_dim": len(null), "sv_luecke": luecke, "Q": Qs, "invarianz_abw": inv_abw}


def rueck_pruefung(A, s, rng):
    nh = np.array([float(np.linalg.norm(A[i])) for i in range(8)])
    nmax = float(nh.max())
    occ = nh >= NORM_SCHWELLE * nmax
    matrix_ok = bool(nmax > 0 and all(occ[i] == occ[INV8[i]] for i in range(8)))
    Jp, Jm = float((nh[:4] ** 2).sum()), float((nh[4:] ** 2).sum())
    J0 = float(np.sum(np.abs(A[8]) ** 2)) if len(A) > 8 else 0.0
    bl = bloecke(A, s, rng)
    je = []
    block_ok = matrix_ok
    for Q in bl["Q"]:
        nb = np.array([float(np.linalg.norm(Q.conj().T @ A[i] @ Q)) for i in range(8)])
        mb = float(nb.max())
        e = {"dim": int(Q.shape[1]), "J+": float((nb[:4] ** 2).sum()), "J-": float((nb[4:] ** 2).sum())}
        if mb <= 1e-6 * max(nmax, 1e-300):
            e.update({"spruenge": False, "ok": True})
        else:
            ob = nb >= NORM_SCHWELLE * mb
            e.update({"spruenge": True, "ok": bool(all(ob[i] == ob[INV8[i]] for i in range(8))),
                      "alle8": bool(ob.all()), "norm_verh": float(nb.min() / mb)})
            block_ok = block_ok and e["ok"]
        je.append(e)
    return {"normen_h": nh.round(12).tolist(), "J+": Jp, "J-": Jm, "J0": J0, "rueck_matrix": matrix_ok,
            "alle8_matrix": bool(occ.all()), "norm_verh_matrix": float(nh.min() / max(nmax, 1e-300)),
            "kommutant_dim": bl["kommutant_dim"], "sv_luecke": bl["sv_luecke"], "block_invarianz_abw": bl["invarianz_abw"],
            "bloecke": je, "rueck_block": bool(block_ok)}


def homogenitaet(A):
    # Eq. (2) der Arbeit von 2017: verschiedene Generatoren haben verschiedene Matrizen (beschreibend)
    nmax = max(float(np.linalg.norm(A[i])) for i in range(8))
    d = [float(np.linalg.norm(A[i] - A[j])) for g in (range(4), range(4, 8)) for i in g for j in g if i < j]
    return float(min(d) / max(nmax, 1e-300))


def cplx(a):
    a = np.asarray(a)
    return {"re": a.real.round(15).tolist(), "im": a.imag.round(15).tolist()}


def kovarianz_abw(A, slots, rots, Vs):
    dev = 0.0
    for R, V in zip(rots, Vs):
        p = perm_on(slots, R)
        for i in range(len(slots)):
            dev = max(dev, float(np.abs(V @ A[i] @ V.conj().T - A[p[i]]).max()))
    return dev


def einordnen(slots, A, s, lifts, rng, voll=True):
    out = {}
    kom = kommutierend(slots, A)
    span = rel_spectrum_span(slots, A)
    out["kommutator_W"], out["rel_spektrum_spannweite"] = kom, span
    out["gewicht_spruenge"] = float(np.sum(np.abs(A[:8]) ** 2))
    out["trivial"] = bool(kom < 1e-8 or span < 1e-8 or out["gewicht_spruenge"] < 1e-10)
    g = analyse_punkt(slots, A, np.zeros(3), lifts)
    out["gamma"] = g
    cl = g["cluster"]
    out["alle_quadratisch"] = all(e["typ"] == "quadratisch" for e in cl)
    out["luecke"] = g["luecke"]
    out["massiv"] = bool((not out["trivial"]) and all(e["m"] == 2 for e in cl) and out["alle_quadratisch"]
                         and g["luecke"] > 1e-3)
    kegel = []
    for e in cl:
        if e["typ"] == "linear" and e["kom_rel"] > 1e-2:
            c = {"phase": e["phase"], "m": e["m"], "lin_min": e["lin_min"], "lin_max": e["lin_max"],
                 "kom_rel": e["kom_rel"], "chiral_det": e["chiral_det"],
                 "spin_rep": bool(e.get("K_plus_I", 1) <= 1e-10 and e.get("Vx2_plus_I", 1) <= 1e-10 and
                                  (e.get("V3hoch3_plus_I") is None or e["V3hoch3_plus_I"] <= 1e-10))}
            if voll:
                c["iso_1e-5"] = isotropie(slots, A, e["phase"], e["m"], 1e-5)
                c["iso_0.05"] = isotropie(slots, A, e["phase"], e["m"], 0.05)
                c["isotrop"] = bool(c["iso_1e-5"]["std_rel"] <= 1e-3 and c["iso_0.05"]["std_rel"] <= 1e-2)
                c["isotrop_streng"] = bool(c["iso_1e-5"]["std_rel"] <= 1e-3 and c["iso_0.05"]["std_rel"] <= 1e-3)
            kegel.append(c)
    out["kegel_cluster"] = kegel
    out["kegel_0"] = bool(kegel) and not out["trivial"]
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
            r = analyse_punkt(slots, A, kk / SQ3, None, mit_kruemmung=False)
            sp[lab] = {"luecke": r["luecke"], "cluster": [{"phase": e["phase"], "m": e["m"], "typ": e["typ"],
                                                            "lin_min": e["lin_min"], "lin_max": e["lin_max"]} for e in r["cluster"]]}
        out["spezialpunkte"] = sp
        out["homogenitaet_min"] = homogenitaet(A)
    return out


def weyl_vergleich(freqs, A, rng):
    # Spektrum gegen Eq. (29) der Quelle bzw. Prop. 5c (2017): cos(omega) = c_x c_y c_z -+ s_x s_y s_z
    ks = rng.uniform(-3, 3, size=(50, 3))
    u = ks / SQ3
    ev = np.linalg.eigvals(W_at(freqs, A, u))
    dl = np.angle(ev[:, 0] / ev[:, 1])
    cc = np.abs(np.cos(dl / 2))
    c, sn = np.cos(u), np.sin(u)
    out = {}
    for lab, sg in (("d_minus", -1), ("d_plus", 1)):
        out[lab] = float(np.abs(cc - np.abs(c.prod(1) + sg * sn.prod(1))).max())
    out["best"] = min(out["d_minus"], out["d_plus"])
    return out


def weyl_quelle(sign):
    z = (1 + sign * 1j) / 4
    zc = np.conj(z)
    Ap = [np.array([[zc, 0], [zc, 0]]), np.array([[0, zc], [0, zc]]), np.array([[0, -zc], [0, zc]]),
          np.array([[zc, 0], [-zc, 0]])]
    Am = [np.array([[0, -z], [0, z]]), np.array([[z, 0], [-z, 0]]), np.array([[z, 0], [z, 0]]),
          np.array([[0, z], [0, z]])]
    return np.array(Ap + Am, dtype=complex)  # Slots S_BCC, Eq. (24) der Quelle 2014


def kategorie(h):
    if not h.get("gueltig", False):
        return "ungueltig"
    kl = h["klass"]
    if kl["trivial"]:
        return "trivial"
    r = h["rueck"]
    if not r["rueck_matrix"]:
        return "einseitig"
    if not r["rueck_block"]:
        return "rueck nur Matrix"
    if kl["kegel_0"]:
        iso = any(c.get("isotrop", False) and c["spin_rep"] for c in kl["kegel_cluster"])
        proj = kl.get("am_treffer", {}).get("wirkung") == "projektiv"
        return "rueck+Kegel iso proj" if (iso and proj) else "rueck+Kegel"
    return "rueck ohne Kegel"


RANG = {"rueck+Kegel iso proj": 7, "rueck+Kegel": 6, "rueck ohne Kegel": 5, "rueck nur Matrix": 4, "einseitig": 3,
        "trivial": 1, "ungueltig": 0}


# ---------------------------------------------------------------- ein Fall
def fall(name, Vs, rots, lifts, s, form, variante, nstarts, seed, maxit=300, n_voll=30):
    t0 = time.time()
    slots = FORMEN[form]
    w = VARIANTEN[variante]
    rho = 0.5 if (form == "O" and w is not None) else None
    perms = [perm_on(slots, R) for R in rots]
    E, perr = covariant_basis(len(slots), perms, Vs, s)
    st = {"name": name, "form": form, "variante": variante, "w": w, "rho": rho, "s": s,
          "dim_komplex": int(E.shape[0]), "projektor_abw": perr, "starts": nstarts, "treffer": 0, "hits": [], "repr": None}
    if E.shape[0] == 0:
        st.update({"leer": True, "D_min": None, "D_median": None, "laufzeit_s": time.time() - t0, "kategorien": {}})
        return st
    prob = Fast(E, slots, s, rots, w, rho)
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
    rk = np.random.default_rng(seed + 7)
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
        h = {"D": Dv, "D_poliert": D_pol, "D_voll": full.defect(A), "nebenbed_rest": prob.nebenbed(p),
             "kovarianz_abw": kovarianz_abw(A, slots, rots, Vs)}
        h["gueltig"] = bool(h["D_voll"] <= GUELTIG_D and h["kovarianz_abw"] <= 1e-10 and
                            all(x <= 1e-9 for x in h["nebenbed_rest"]))
        h["rueck"] = rueck_pruefung(A, s, rk)
        if s == 2:
            h["weyl_vergleich"] = weyl_vergleich(slots, A, rk)
        voll = n_v < n_voll
        h["klass"] = einordnen(slots, A, s, lifts, rk, voll=voll)
        h["voll_eingeordnet"] = voll
        if voll and not h["klass"]["trivial"]:
            n_v += 1
        h["kategorie"] = kategorie(h)
        st["hits"].append(h)
        if st["repr"] is None or RANG[h["kategorie"]] > st["repr"]["rang"]:
            st["repr"] = {"rang": RANG[h["kategorie"]], "kategorie": h["kategorie"], "freqs": slots.tolist(), "A": cplx(A)}
    kat = {}
    for h in st["hits"]:
        kat[h["kategorie"]] = kat.get(h["kategorie"], 0) + 1
    st["kategorien"] = kat
    st["laufzeit_s"] = time.time() - t0
    return st


# ---------------------------------------------------------------- Teil 0: Kontrolle, Referenz, Konstruktionen
def monomial_basis_allg(T, V4):
    # Ind chi (Stabilisator C_3 von t_1) in einer Spinordarstellung 2^(a) + 2^(b): gemeinsamer Eigenwert von V(R3)
    iR = [i for i, (R, _, _) in enumerate(T) if key3(R) == key3(R3)][0]
    VR = V4[iR]
    w1, v1 = np.linalg.eig(VR[:2, :2])
    w2, v2 = np.linalg.eig(VR[2:, 2:])
    d = np.abs(w1[:, None] - w2[None, :])
    i, j = np.unravel_index(np.argmin(d), d.shape)
    vec1 = np.zeros(4, dtype=complex)
    vec1[:2] = v1[:, i] / np.linalg.norm(v1[:, i])
    vec2 = np.zeros(4, dtype=complex)
    vec2[2:] = v2[:, j] / np.linalg.norm(v2[:, j])
    p1 = (vec1 + vec2) / np.sqrt(2)
    ps = []
    for a in range(4):
        g = [k for k, (R, _, _) in enumerate(T) if tuple(R @ TV[0]) == tuple(TV[a])][0]
        ps.append(V4[g] @ p1)
    Pm = np.array(ps).T
    mono = 0.0
    for (R, _, _), V in zip(T, V4):
        p = perm_on(TV, R)
        for a in range(4):
            mono = max(mono, abs(1 - abs(np.vdot(Pm[:, p[a]], V @ Pm[:, a]))))
    return Pm, float(np.abs(Pm.conj().T @ Pm - np.eye(4)).max()), float(d.min()), mono


def muenze_verschiebung_8(T, teile_p, teile_m, rng, mischen=True):
    Vp, Vm = spinor_rep(T, teile_p), spinor_rep(T, teile_m)
    Pp, gp, dp, mp = monomial_basis_allg(T, Vp)
    Pn, gn, dn, mn = monomial_basis_allg(T, Vm)
    V8 = [bdiag(a, b) for a, b in zip(Vp, Vm)]
    al = rng.uniform(0, 2 * np.pi, 4)
    C1 = np.diag(np.exp(1j * np.array([al[0], al[0], al[1], al[1]])))
    C2 = np.diag(np.exp(1j * np.array([al[2], al[2], al[3], al[3]])))
    if mischen:
        H = rng.standard_normal((8, 8)) + 1j * rng.standard_normal((8, 8))
        H = (H + H.conj().T) / 2
        Hb = sum(V @ H @ V.conj().T for V in V8) / len(V8)
        X = expm(1j * Hb)
    else:
        X = np.eye(8, dtype=complex)
    A = np.zeros((8, 8, 8), dtype=complex)
    for a in range(4):
        Z = np.zeros((8, 8), dtype=complex)
        Z[:4, :4] = C1 @ np.outer(Pp[:, a], Pp[:, a].conj())
        A[a] = X @ Z
        Z = np.zeros((8, 8), dtype=complex)
        Z[4:, 4:] = C2 @ np.outer(Pn[:, a], Pn[:, a].conj())
        A[4 + a] = X @ Z
    info = {"gram_abw": max(gp, gn), "eigenwert_abstand": max(dp, dn), "monomial_abw": max(mp, mn),
            "X_kommutant_abw": float(max(np.abs(V @ X - X @ V).max() for V in V8))}
    return A, V8, info


def teil0(T, ginfo, nstarts, seedbase, starts_var):
    out = {}
    rots_T = [R for (R, _, _) in T]
    lifts2 = (1j * SX, 1j * SY, None)
    # QR0: L2:Pauli, s = 2, Form N, mit und ohne Rueckspruung-Nebenbedingung
    such = {}
    for vi, var in enumerate(starts_var):
        st = fall("L2:Pauli", PAULI_V4, L2_ROTS, lifts2, 2, "N", var, nstarts, seedbase * 10000 + 10 * vi)
        such["L2:Pauli|N|" + var] = st
        print(f"[0] L2:Pauli N {var}: dim={st['dim_komplex']} treffer={st['treffer']} kat={st.get('kategorien')} "
              f"Dmin={st['D_min']} t={st['laufzeit_s']:.1f}s", flush=True)
    out["qr0_suche"] = such
    # Referenz: Weyl-Automaten der Quelle (Eq. 24), Rueckspruenge, Spektrum, Isotropie
    ref = {}
    rng = np.random.default_rng(seedbase * 10000 + 900)
    for sign, lab in ((1, "A+"), (-1, "A-")):
        A = weyl_quelle(sign)
        ref[lab] = {"unitaer_defekt": Unit(S_BCC, 2).defect(A), "kovarianz_L2_abw": kovarianz_abw(A, S_BCC, L2_ROTS, PAULI_V4),
                    "rueck": rueck_pruefung(A, 2, rng), "weyl_vergleich": weyl_vergleich(S_BCC, A, rng),
                    "klass": einordnen(S_BCC, A, 2, lifts2, rng)}
    out["weyl_quelle"] = ref
    # Konstruktionen: Muenze x (S+ + S-) mit 8 Zustaenden (beschreibend, Vermerk zu QR2)
    kons = {}
    for lab, tp, tm, mi, nrep in (("K4_gemischt", ["2", "2'"], ["2", "2'"], True, 3),
                                  ("K4_direkte_Summe", ["2", "2'"], ["2", "2'"], False, 1),
                                  ("K5_gemischt", ["2", "2'"], ["2", "2''"], True, 2)):
        for r in range(nrep):
            A, V8, info = muenze_verschiebung_8(T, tp, tm, rng, mischen=mi)
            lifts8 = (V8[ginfo["idx_C2x"]], V8[ginfo["idx_C2y"]], V8[ginfo["idx_R3"]])
            kl = einordnen(S_BCC, A, 8, lifts8, rng)
            e = {"teile": tp + tm, "info": info, "unitaer_defekt": Unit(S_BCC, 8).defect(A),
                 "kovarianz_T_abw": kovarianz_abw(A, S_BCC, rots_T, V8), "rueck": rueck_pruefung(A, 8, rng), "klass": kl,
                 "repr": {"freqs": S_BCC.tolist(), "A": cplx(A)}}
            e["gueltig"] = bool(e["unitaer_defekt"] <= GUELTIG_D and e["kovarianz_T_abw"] <= 1e-10)
            e["kategorie"] = kategorie(e)
            kons[f"{lab}_{r}"] = e
            print(f"[0] Konstruktion {lab}_{r}: D={e['unitaer_defekt']:.2e} kov={e['kovarianz_T_abw']:.1e} "
                  f"kat={e['kategorie']} J+={e['rueck']['J+']:.3f} J-={e['rueck']['J-']:.3f} "
                  f"kommutant={e['rueck']['kommutant_dim']}", flush=True)
    out["konstruktionen"] = kons
    return out


def codepruefung(T, rng):
    chk = []
    rots_T = [R for (R, _, _) in T]
    for teile, form, w, rho in ((["2", "2'"], "O", 0.2, 0.5), (["2", "2", "2'", "2'"], "N", 0.5, None),
                                (["2", "2'"], "N", None, None)):
        Vs = spinor_rep(T, teile)
        s = 2 * len(teile)
        slots = FORMEN[form]
        perms = [perm_on(slots, R) for R in rots_T]
        E, _ = covariant_basis(len(slots), perms, Vs, s)
        fp = Fast(E, slots, s, rots_T, w, rho)
        x = rng.standard_normal(2 * E.shape[0])
        A = fp.A_of(x)
        r, J = fp.rj(x)
        n_ex = len(fp.extra)
        d1 = float(r[:len(r) - n_ex] @ r[:len(r) - n_ex])
        d2 = Unit(slots, s).defect(A)
        xc = x[:E.shape[0]] + 1j * x[E.shape[0]:]
        Jp = float(np.real(np.vdot(xc, fp.Gp @ xc)))
        Jp_dir = float(np.sum(np.abs(A[:4]) ** 2))
        eps = 1e-7
        jdev = 0.0
        for k in rng.integers(len(x), size=3):
            x2 = x.copy()
            x2[k] += eps
            r2, _ = fp.rj(x2, jac=False)
            jdev = max(jdev, float(np.abs((r2 - r) / eps - J[:, k]).max() / max(np.abs(J[:, k]).max(), 1e-300)))
        chk.append({"fall": "+".join(teile) + "|" + form + f"|w={w}|rho={rho}", "defekt_rel": abs(d1 - d2) / d2,
                    "J+_rel": abs(Jp - Jp_dir) / Jp_dir, "jacobi_rel": jdev})
    return chk


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--teil", choices=["0", "4", "8"], required=True)
    ap.add_argument("--modus", choices=["rauch", "haupt"], required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--formen", default="N,O")
    ap.add_argument("--varianten", default="frei,r50,r20,r05")
    ap.add_argument("--faelle", default="alle")
    ap.add_argument("--starts", type=int, default=None)
    ap.add_argument("--maxit", type=int, default=300)
    args = ap.parse_args()
    t_start = time.time()
    seedbase = 3990 if args.modus == "rauch" else 399
    T, ginfo = gruppen()
    rots_T = [R for (R, _, _) in T]
    res = {"modus": args.modus, "teil": args.teil, "saat_basis": seedbase, "formen_arg": args.formen,
           "varianten_arg": args.varianten, "faelle_arg": args.faelle, "gruppen": ginfo, "numpy": np.__version__,
           "norm_schwelle": NORM_SCHWELLE, "gueltig_D": GUELTIG_D}
    rng = np.random.default_rng(seedbase)
    res["codepruefung"] = codepruefung(T, rng)
    reps = darstellungen(T)
    res["darstellungen"] = {nm: dict(art=art, **rep_check(rots_T, Vs)) for nm, (art, Vs) in reps.items()}
    res["darstellungen"]["L2:Pauli"] = dict(art="projektiv", **rep_check(L2_ROTS, PAULI_V4))
    varianten = args.varianten.split(",")
    faelle = {}
    if args.teil == "0":
        nst = args.starts if args.starts else (10 if args.modus == "rauch" else 40)
        res["teil0"] = teil0(T, ginfo, nst, seedbase, varianten)
    else:
        liste = FAELLE4 if args.teil == "4" else FAELLE8
        wahl = liste if args.faelle == "alle" else [liste[int(i)] for i in args.faelle.split(",")]
        nst = args.starts if args.starts else (5 if args.modus == "rauch" else 30)
        for fi, form in enumerate(args.formen.split(",")):
            for var in varianten:
                vi = list(VARIANTEN.keys()).index(var)
                for nm in wahl:
                    ci = liste.index(nm)
                    art, Vs = reps[nm]
                    lifts = (Vs[ginfo["idx_C2x"]], Vs[ginfo["idx_C2y"]], Vs[ginfo["idx_R3"]])
                    s = Vs[0].shape[0]
                    seed = seedbase * 10000 + (1000 if args.teil == "4" else 2000) + 100 * "NO".index(form) + 10 * vi + ci
                    st = fall(nm, Vs, rots_T, lifts, s, form, var, nst, seed, maxit=args.maxit)
                    st["art"] = art
                    faelle[f"{args.teil}|{nm}|{form}|{var}"] = st
                    print(f"[{args.teil}] {nm} {form} {var}: dim={st['dim_komplex']} treffer={st['treffer']} "
                          f"kat={st.get('kategorien')} Dmin={st['D_min']} t={st['laufzeit_s']:.1f}s", flush=True)
    res["faelle"] = faelle
    res["laufzeit_s"] = time.time() - t_start
    with open(args.out, "w") as fh:
        json.dump(res, fh, indent=1, default=lambda o: o.tolist() if hasattr(o, "tolist") else str(o))
    print(f"fertig, {res['laufzeit_s']:.1f} s", flush=True)


if __name__ == "__main__":
    sys.exit(main())
