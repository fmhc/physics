#!/usr/bin/env python3
"""WAND-BETA (Runde 24), Leitung claude-primary, 03.10.2026. Karte: RUNDE-24/wand-beta/KARTE.md.
Abgeleitet von RUNDE-23/tropfen-leiter/code/wand_transmission_v3.py (Verfahren unveraendert), Modell
U = S - S^2 + beta S^3 mit beliebigem beta, ebene Wand bei omega_min(beta); dazu nackte Wandzustaende des
geschlossenen Kanals (-A'' + W A = E A, E < 1).

Aufruf: python wand_beta.py <beta> <f_min> <f_max> <n> <aus.json>
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import json  # noqa: E402
import math  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import scipy.sparse as sp  # noqa: E402
from scipy.integrate import solve_ivp  # noqa: E402
from scipy.linalg import eigh_tridiagonal  # noqa: E402
from scipy.optimize import brentq, minimize_scalar  # noqa: E402
from scipy.sparse.linalg import spsolve  # noqa: E402
from scipy.special import expit  # noqa: E402

RTOL = 1e-11
ATOL = 1e-30
H_FD = (0.002, 0.004)
H_NACKT = 0.005


class MB:
    def __init__(self, beta):
        self.beta = float(beta)
        self.OM = math.sqrt(1.0 - 1.0 / (4.0 * self.beta))
        self.Sc = 1.0 / (2.0 * self.beta)
        sb = math.sqrt(self.beta)
        self.rate = 1.0 / sb
        self.xa, self.xb = -36.0 * sb, 43.0 * sb
        self.xa_fd, self.xb_fd = -29.0 * sb, 36.0 * sb
        self.W_in = 1.0 + 1.0 / (4.0 * self.beta)
        self.C_in = 1.0 / (2.0 * self.beta)
        self.W_min = 1.0 - 4.0 / (9.0 * self.beta)

    def S(self, x):
        return self.Sc * expit(-self.rate * x)

    def koeff(self, x):
        S = self.S(x)
        b = self.beta
        return 1.0 - 4.0 * S + 9.0 * b * S * S, -2.0 * S + 6.0 * b * S * S

    def P(self, x, f):
        W, C = self.koeff(x)
        return np.array([[W - (f - self.OM) ** 2, C], [C, W - (f + self.OM) ** 2]])

    def P_vek(self, x, f):
        W, C = self.koeff(x)
        return W - (f - self.OM) ** 2, C, W - (f + self.OM) ** 2

    def P_aussen(self, f):
        return np.array([[1.0 - (f - self.OM) ** 2, 0.0], [0.0, 1.0 - (f + self.OM) ** 2]])

    def P_innen(self, f):
        return np.array([[self.W_in - (f - self.OM) ** 2, self.C_in], [self.C_in, self.W_in - (f + self.OM) ** 2]])

    def k2_formel(self, f):
        return self.OM ** 2 + f * f - self.W_in + math.sqrt(4.0 * self.OM ** 2 * f * f + self.C_in ** 2)

    def rest(self, x):
        # f = sqrt(S): f' = -sqrt(beta) f (Sc - S), f'' = -sqrt(beta) f' (Sc - 3 S); Gleichung f'' = (U'(S) - omega^2) f
        S = self.S(x)
        fx = math.sqrt(S)
        sb = math.sqrt(self.beta)
        f1 = -sb * fx * (self.Sc - S)
        f2 = -sb * f1 * (self.Sc - 3.0 * S)
        return f2 - (1.0 - 2.0 * S + 3.0 * self.beta * S * S - self.OM ** 2) * fx


def innen_moden(mod, f):
    lam, vec = np.linalg.eigh(mod.P_innen(f))
    e1, e2 = vec[:, 0].copy(), vec[:, 1].copy()
    if e1[0] < 0:
        e1 = -e1
    if e2[0] < 0:
        e2 = -e2
    if not (lam[0] < 0.0 < lam[1]):
        raise ValueError(f"Innenmatrix nicht ein laufend / ein abklingend bei f = {f}: {lam}")
    return math.sqrt(-lam[0]), e1, math.sqrt(lam[1]), e2


def aussen_raten(mod, f):
    Pa = mod.P_aussen(f)
    if not (Pa[0, 0] > 0.0 and Pa[1, 1] < 0.0):
        raise ValueError(f"aussen nicht geschlossen/offen bei f = {f}: {np.diag(Pa)}")
    return math.sqrt(Pa[0, 0]), math.sqrt(-Pa[1, 1])


def c_in(mod, f, rtol=RTOL, xa=None, xb=None):
    xa = mod.xa if xa is None else xa
    xb = mod.xb if xb is None else xb
    q, _ = aussen_raten(mod, f)

    def rhs(x, z):
        P = mod.P(x, f)
        return np.concatenate([z[2:], P @ z[:2]])

    sol = solve_ivp(rhs, (xb, xa), np.array([1.0, 0.0, -q, 0.0]), method="DOP853", rtol=rtol, atol=ATOL)
    if not sol.success:
        raise RuntimeError(sol.message)
    z = sol.y[:, -1]
    k, e1, kap, e2 = innen_moden(mod, f)
    ye, ye1 = e2 @ z[:2], e2 @ z[2:]
    b = (kap * ye - ye1) / (2.0 * kap) * math.exp(kap * xa - q * xb)
    return b, sol.nfev


def transmission_fd(mod, f, h):
    q, ko = aussen_raten(mod, f)
    k, e1, kap, e2 = innen_moden(mod, f)
    N = int(round((mod.xb_fd - mod.xa_fd) / h))
    x = mod.xa_fd + h * np.arange(N + 1)
    p11, p12, p22 = mod.P_vek(x, f)
    th = math.acos(1.0 - 0.5 * h * h * k * k)
    eta_k = math.acosh(1.0 + 0.5 * h * h * kap * kap)
    th_o = math.acos(1.0 - 0.5 * h * h * ko * ko)
    eta_q = math.acosh(1.0 + 0.5 * h * h * q * q)
    n = 2 * (N + 1)
    rows, cols, vals = [], [], []
    j = np.arange(1, N)
    ih2 = 1.0 / (h * h)
    for c, (pcc, pco) in enumerate(((p11, p12), (p22, p12))):
        r = 2 * j + c
        rows += [r, r, r, r]
        cols += [2 * (j - 1) + c, 2 * j + c, 2 * j + (1 - c), 2 * (j + 1) + c]
        vals += [np.full(j.size, ih2), -2.0 * ih2 - pcc[j], -pco[j], np.full(j.size, ih2)]
    rows = np.concatenate(rows)
    cols = np.concatenate(cols)
    vals = np.concatenate(vals).astype(complex)
    br, bc, bv = [], [], []
    rhs = np.zeros(n, dtype=complex)
    for cc in (0, 1):
        br += [0, 0]
        bc += [2 * 1 + cc, 2 * 0 + cc]
        bv += [e2[cc], -math.exp(eta_k) * e2[cc]]
    for cc in (0, 1):
        br += [1, 1]
        bc += [2 * 1 + cc, 2 * 0 + cc]
        bv += [e1[cc], -complex(math.cos(th), -math.sin(th)) * e1[cc]]
    rhs[1] = 2j * math.sin(th)
    br += [2 * N, 2 * N]
    bc += [2 * N, 2 * (N - 1)]
    bv += [1.0, -math.exp(-eta_q)]
    br += [2 * N + 1, 2 * N + 1]
    bc += [2 * N + 1, 2 * (N - 1) + 1]
    bv += [1.0, -complex(math.cos(th_o), math.sin(th_o))]
    A = sp.csc_matrix((np.concatenate([vals, np.array(bv, dtype=complex)]),
                       (np.concatenate([rows, np.array(br)]), np.concatenate([cols, np.array(bc)]))), shape=(n, n))
    Y = spsolve(A, rhs)
    yp0 = e1[0] * Y[0] + e1[1] * Y[1]
    b_ref = yp0 - 1.0
    t2 = abs(Y[2 * N + 1]) ** 2
    T = math.sin(th_o) * t2 / math.sin(th)
    R = abs(b_ref) ** 2
    return T, R, R + T - 1.0


def fd_nullstelle(mod, fz, d, h):
    res = minimize_scalar(lambda f: transmission_fd(mod, f, h)[0], bounds=(fz - d, fz + d), method="bounded",
                          options={"xatol": 1e-12, "maxiter": 200})
    return float(res.x), float(res.fun), int(res.nfev)


def nackte_zustaende(mod, h=H_NACKT):
    N = int(round((mod.xb_fd - mod.xa_fd) / h))
    x = mod.xa_fd + h * np.arange(1, N)               # innere Knoten, Dirichlet an beiden Enden
    W, _ = mod.koeff(x)
    d = 2.0 / (h * h) + W
    e = np.full(x.size - 1, -1.0 / (h * h))
    lo = min(float(W.min()), mod.W_min) - 0.01
    try:
        ev = eigh_tridiagonal(d, e, eigvals_only=True, select="v", select_range=(lo, 1.0))
    except ValueError:
        ev = np.array([])
    return [float(v) for v in np.sort(ev)], float(W.min())


def main():
    beta, fmin, fmax, n, pfad = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), \
        sys.argv[5]
    mod = MB(beta)
    t0 = time.time()
    out = {"beta": beta, "omega": mod.OM, "Sc": mod.Sc, "W_min_formel": mod.W_min, "W_in": mod.W_in,
           "C_in": mod.C_in, "fenster": [fmin, fmax], "fenster_gueltig": [1.0 - mod.OM, 1.0 + mod.OM], "n": n,
           "rtol": RTOL, "xa": mod.xa, "xb": mod.xb, "xa_fd": mod.xa_fd, "xb_fd": mod.xb_fd, "version": 1}
    xs = np.linspace(mod.xa, mod.xb, 4001)
    out["k0_rest_max"] = float(max(abs(mod.rest(float(x))) for x in xs))
    fk = np.linspace(fmin, fmax, 21)
    out["k0_dispersion_max_abw"] = float(max(abs(innen_moden(mod, float(f))[0] ** 2 - mod.k2_formel(float(f)))
                                             for f in fk))
    nackt, wmin_num = nackte_zustaende(mod)
    out["nackt_E"] = nackt
    out["W_min_numerisch"] = wmin_num
    print(f"beta {beta}: K0 Rest {out['k0_rest_max']:.2e}, Dispersion {out['k0_dispersion_max_abw']:.2e}, "
          f"nackte Zustaende {nackt}", flush=True)

    fs = [float(f) for f in np.linspace(fmin, fmax, n)]
    werte, nfev = [], 0
    for f in fs:
        b, nf = c_in(mod, f)
        werte.append(b)
        nfev += nf
    out["abtastung"] = {"f": fs, "c_in": werte}
    print(f"beta {beta}: Abtastung fertig ({nfev} Auswertungen, {time.time() - t0:.1f} s)", flush=True)

    zlist = []
    for i in range(len(fs) - 1):
        a, b = werte[i], werte[i + 1]
        if not (a == 0.0 or a * b < 0.0):
            continue
        fz = brentq(lambda f: c_in(mod, f)[0], fs[i], fs[i + 1], xtol=1e-14, rtol=1e-15, maxiter=200)
        k, _, kap, _ = innen_moden(mod, fz)
        q, ko = aussen_raten(mod, fz)
        Ez = (fz - mod.OM) ** 2
        e = {"f_z": fz, "E_z": Ez, "k_in": k, "kappa_in": kap, "q_aussen": q, "k_aussen": ko,
             "b_inf": 2.0 * math.sqrt(beta) * math.pi / k,
             "E0_minus_Ez": (nackt[0] - Ez) if nackt else None}
        d = 2e-4 * max(1.0, abs(fz))
        for key, fn in (("f_z_rtol1e-9", lambda f: c_in(mod, f, 1e-9)[0]),
                        ("f_z_gebiet_plus10", lambda f: c_in(mod, f, RTOL, mod.xa - 10.0, mod.xb + 10.0)[0])):
            try:
                e[key] = brentq(fn, fz - d, fz + d, xtol=1e-14, rtol=1e-15, maxiter=200)
            except ValueError as ex:
                e[key] = f"kein Vorzeichenwechsel: {ex}"
        fd = {}
        for h in H_FD:
            fz_h, tmin, nfe = fd_nullstelle(mod, fz, d, h)
            fd[str(h)] = {"f_z": fz_h, "T_min": tmin, "nfev": nfe}
        fa, fb = fd[str(H_FD[0])]["f_z"], fd[str(H_FD[1])]["f_z"]
        fd["richardson"] = (4.0 * fa - fb) / 3.0
        e["fd"] = fd
        e["T_fd_bei_f_z"] = {str(s): transmission_fd(mod, fz + s, H_FD[0]) for s in (-1e-3, 0.0, 1e-3)}
        zlist.append(e)
        print(f"beta {beta}: Nullstelle f_z = {fz:.10f}, E_z = {Ez:.6f}, k_in = {k:.6f}, b_inf = {e['b_inf']:.6f}",
              flush=True)
    out["nullstellen"] = zlist
    tgrob = []
    for f in np.linspace(fmin, fmax, max(11, n // 25)):
        T, R, fl = transmission_fd(mod, float(f), H_FD[1])
        tgrob.append({"f": float(f), "T": T, "R": R, "fluss": fl})
    out["transmission_grob"] = tgrob
    out["fluss_max"] = max(abs(t["fluss"]) for t in tgrob)
    out["sek"] = time.time() - t0
    with open(pfad + ".tmp", "w") as fh:
        json.dump(out, fh, indent=1)
    os.replace(pfad + ".tmp", pfad)
    print(f"beta {beta}: fertig, {len(zlist)} Nullstellen, Fluss max {out['fluss_max']:.2e}, {out['sek']:.1f} s",
          flush=True)


if __name__ == "__main__":
    main()
