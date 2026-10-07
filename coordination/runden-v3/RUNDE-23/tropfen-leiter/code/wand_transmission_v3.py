#!/usr/bin/env python3
"""TROPFEN-LEITER (Runde 23), Leitung claude-primary, 02.10.2026, Fassung 3 (nach Rauchlauf 2).
Fassung 2 -> 3: d3-Knick robust ausgewertet (leere Teilmengen), in c_in fuer d3 im Zustandsvektor mitgefuehrt.
Karte: RUNDE-23/tropfen-leiter/KARTE.md.

Ebene Wand bei reeller Frequenz f. Zwei Komponenten Y = (y1, y2) mit Y'' = P(x, f) Y, P reell symmetrisch.
Kanal 1 ist aussen geschlossen, Kanal 2 aussen offen (im Fenster). Innen (x -> -unendlich) hat P_in einen negativen
Eigenwert (laufende Mode, Wellenzahl k) und einen positiven (abklingende Mode, kappa).

  c_in(f):   Schiessen nach innen. Start aussen rein abklingend im geschlossenen Kanal; Koeffizient der ins Innere
             wachsenden Mode exp(-kappa x). Nullstelle = Transmissionsnullstelle. Die verfolgte Loesung ist stets die
             dominante, daher gut konditioniert.
  T_fd(f):   unabhaengige Gegenprobe als Randwertproblem (3-Punkt-Differenzen, Schritt h) mit exakt diskreten
             Randbedingungen: links einlaufende Mode e1 mit Amplitude 1 plus erlaubte abklingende Mode, rechts
             auslaufend (offen) und abklingend (geschlossen). Der diskrete Fluss ist exakt erhalten (R + T = 1).
             Nullstelle von T_fd per Minimierung, zwei Schrittweiten, Richardson.

Fassung 1 -> 2 (Rauchlauf 1, 23:03 bis 23:07): Die Transmission aus zwei geschossenen Loesungen verlor durch
Ausloeschung alle Stellen (Flussfehler 0,4 bzw. 1e60), D_out (Schiessen nach aussen) ist aus demselben Grund
schlecht konditioniert. Beide ersetzt durch T_fd. Startwerte O(1), atol 1e-30.

Modelle:
  m1: U = S - S^2 + S^3/2, omega^2 = 1/2, S(x) = 1/(1 + exp(sqrt2 x)); y1 = A (Seitenband rho - omega), y2 = B (rho + omega).
  d1: i psi_t = -psi_xx/2 + |psi|^2 psi - |psi| psi, mu0 = -2/9, phi = (2/3)/(1 + exp(2x/3)); y1 = v, y2 = u.
  d3: i psi_t = -psi_xx/2 - 3|psi|^2 psi + (5/2)|psi|^3 psi, mu0 = -1/2, phi' = -phi(1 - phi) sqrt(1 + 2 phi); y1 = v, y2 = u.

Aufruf: python wand_transmission_v2.py <m1|d1|d3> <f_min> <f_max> <n> <aus.json>
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
from scipy.optimize import brentq, minimize_scalar  # noqa: E402
from scipy.sparse.linalg import spsolve  # noqa: E402
from scipy.special import expit  # noqa: E402

SQ2 = math.sqrt(2.0)
OM1 = 1.0 / SQ2  # Frequenz des M1-Q-Balls an der ebenen Wand (omega^2 = 1/2)
RTOL = 1e-11
ATOL = 1e-30
H_FD = (0.002, 0.004)


# ---------------------------------------------------------------- Modelle
class M1:
    name = "m1"
    xa, xb = -25.0, 30.0          # Schiessen
    xa_fd, xb_fd = -20.0, 25.0    # Randwertproblem

    @staticmethod
    def S(x):
        return expit(-SQ2 * x)

    def koeff(self, x):           # vektoriell: (P11 ohne f, P12, P22 ohne f) als Funktionen von x
        S = self.S(x)
        W = 1.0 - 4.0 * S + 4.5 * S * S           # U' + U'' S
        C = -2.0 * S + 3.0 * S * S                # U'' S
        return W, C

    def P(self, x, f):
        W, C = self.koeff(x)
        return np.array([[W - (f - OM1) ** 2, C], [C, W - (f + OM1) ** 2]])

    def P_vek(self, x, f):
        W, C = self.koeff(x)
        return W - (f - OM1) ** 2, C, W - (f + OM1) ** 2

    def P_aussen(self, f):
        return np.array([[1.0 - (f - OM1) ** 2, 0.0], [0.0, 1.0 - (f + OM1) ** 2]])

    def P_innen(self, f):
        return np.array([[1.5 - (f - OM1) ** 2, 1.0], [1.0, 1.5 - (f + OM1) ** 2]])

    @staticmethod
    def k2_formel(f):
        return OM1 ** 2 + f * f - 1.5 + math.sqrt(4.0 * OM1 ** 2 * f * f + 1.0)

    def rest(self, x):
        # f = sqrt(S): f' = -(f/sqrt2)(1 - f^2), f'' = -(f'/sqrt2)(1 - 3 f^2); Gleichung f'' = (U'(S) - omega^2) f
        S = self.S(x)
        fx = np.sqrt(S)
        f1 = -(fx / SQ2) * (1.0 - S)
        f2 = -(f1 / SQ2) * (1.0 - 3.0 * S)
        return f2 - (1.0 - 2.0 * S + 1.5 * S * S - 0.5) * fx


class Tropfen:
    """NLS-Tropfen: u'' = 2(h - w)u + 2Mv, v'' = 2Mu + 2(h + w)v; Y = (v, u)."""

    def P(self, x, f):
        h, M = self.hM(x)
        return np.array([[2.0 * (h + f), 2.0 * M], [2.0 * M, 2.0 * (h - f)]])

    def P_vek(self, x, f):
        h, M = self.hM(x)
        return 2.0 * (h + f), 2.0 * M, 2.0 * (h - f)

    def P_aussen(self, f):
        return np.array([[2.0 * (-self.mu0 + f), 0.0], [0.0, 2.0 * (-self.mu0 - f)]])

    def P_innen(self, f):
        h, M = self.hM_innen
        return np.array([[2.0 * (h + f), 2.0 * M], [2.0 * M, 2.0 * (h - f)]])


class D1(Tropfen):
    name = "d1"
    xa, xb = -45.0, 60.0
    xa_fd, xb_fd = -40.0, 55.0
    mu0 = -2.0 / 9.0
    n0 = 4.0 / 9.0
    hM_innen = (1.0 / 9.0, 1.0 / 9.0)

    @staticmethod
    def phi(x):
        return (2.0 / 3.0) * expit(-(2.0 / 3.0) * x)

    def hM(self, x):
        p = self.phi(x)
        return -self.mu0 + 2.0 * p * p - 1.5 * p, p * p - 0.5 * p

    @staticmethod
    def k2_formel(f):
        return 2.0 * math.sqrt(f * f + 1.0 / 81.0) - 2.0 / 9.0

    def rest(self, x):
        p = self.phi(x)
        p1 = -p * (2.0 / 3.0 - p)
        p2 = -p1 * (2.0 / 3.0 - 2.0 * p)
        return p2 - 2.0 * p * (p * p - p - self.mu0)


class D3(Tropfen):
    name = "d3"
    xa, xb = -22.0, 40.0
    xa_fd, xb_fd = -18.0, 35.0
    mu0 = -0.5
    n0 = 1.0
    hM_innen = (0.75, 0.75)

    def __init__(self):
        # Knick phi' = g(phi), phi(0) = 1/2; je Seite in der stabilen Richtung integriert, aussen phi, innen psi = 1 - phi
        g = lambda x, y: [-y[0] * (1.0 - y[0]) * math.sqrt(1.0 + 2.0 * y[0])]          # noqa: E731
        gpsi = lambda x, y: [(1.0 - y[0]) * y[0] * math.sqrt(3.0 - 2.0 * y[0])]        # noqa: E731  psi' = -phi'
        self.rechts = solve_ivp(g, (0.0, 80.0), [0.5], method="DOP853", rtol=1e-13, atol=1e-300, dense_output=True)
        self.links = solve_ivp(gpsi, (0.0, -60.0), [0.5], method="DOP853", rtol=1e-13, atol=1e-300,
                               dense_output=True)

    def phi(self, x):
        xv = np.atleast_1d(np.asarray(x, dtype=float))
        out = np.empty_like(xv)
        r = xv >= 0.0
        if r.any():
            out[r] = self.rechts.sol(xv[r])[0]
        if (~r).any():
            out[~r] = 1.0 - self.links.sol(xv[~r])[0]
        return out if np.ndim(x) else float(out[0])

    def hM(self, x):
        p = self.phi(x)
        return -self.mu0 - 6.0 * p * p + 6.25 * p ** 3, -3.0 * p * p + 3.75 * p ** 3

    @staticmethod
    def k2_formel(f):
        return 2.0 * math.sqrt(f * f + 9.0 / 16.0) - 1.5

    def rest(self, x):
        p = float(self.phi(np.array([x]))[0])
        g = -p * (1.0 - p) * math.sqrt(1.0 + 2.0 * p)
        dg = -((1.0 - 2.0 * p) * math.sqrt(1.0 + 2.0 * p) + p * (1.0 - p) / math.sqrt(1.0 + 2.0 * p))
        return dg * g - 2.0 * p * (-3.0 * p * p + 2.5 * p ** 3 - self.mu0)


MODELLE = {"m1": M1, "d1": D1, "d3": D3}


# ---------------------------------------------------------------- Werkzeuge
def innen_moden(mod, f):
    """Eigenzerlegung von P_in: (k, e_lauf, kappa, e_abkl), Vorzeichen fest (erste Komponente positiv)."""
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

    if mod.name == "d3":
        # Knick im Zustandsvektor mitfuehren (schneller als die dichte Ausgabe je Auswertung)
        mu0 = mod.mu0

        def rhs(x, z):
            p = z[4]
            h = -mu0 - 6.0 * p * p + 6.25 * p ** 3
            M = -3.0 * p * p + 3.75 * p ** 3
            return np.array([z[2], z[3], 2.0 * (h + f) * z[0] + 2.0 * M * z[1], 2.0 * M * z[0] + 2.0 * (h - f) * z[1],
                             -p * (1.0 - p) * math.sqrt(max(1.0 + 2.0 * p, 0.0))])

        start = np.array([1.0, 0.0, -q, 0.0, float(mod.phi(np.array([xb]))[0])])
    else:
        def rhs(x, z):
            P = mod.P(x, f)
            return np.concatenate([z[2:], P @ z[:2]])

        start = np.array([1.0, 0.0, -q, 0.0])

    sol = solve_ivp(rhs, (xb, xa), start, method="DOP853", rtol=rtol, atol=ATOL)
    if not sol.success:
        raise RuntimeError(sol.message)
    z = sol.y[:4, -1]
    k, e1, kap, e2 = innen_moden(mod, f)
    ye, ye1 = e2 @ z[:2], e2 @ z[2:]
    # Koeffizient vor exp(-kappa x) fuer die Startnormierung exp(-q (x - xb)) -> exp(-q x): Faktor exp(-q xb)
    b = (kap * ye - ye1) / (2.0 * kap) * math.exp(kap * xa - q * xb)
    return b, sol.nfev


def transmission_fd(mod, f, h):
    """Randwertproblem mit exakt diskreten Randbedingungen. Rueckgabe: T, R, R + T - 1."""
    q, ko = aussen_raten(mod, f)
    k, e1, kap, e2 = innen_moden(mod, f)
    N = int(round((mod.xb_fd - mod.xa_fd) / h))
    x = mod.xa_fd + h * np.arange(N + 1)
    p11, p12, p22 = mod.P_vek(x, f)
    p11 = np.broadcast_to(p11, x.shape)
    p12 = np.broadcast_to(p12, x.shape)
    p22 = np.broadcast_to(p22, x.shape)
    # diskrete Wellenzahlen / Abklingfaktoren
    th = math.acos(1.0 - 0.5 * h * h * k * k)              # innen laufend
    eta_k = math.acosh(1.0 + 0.5 * h * h * kap * kap)      # innen abklingend
    th_o = math.acos(1.0 - 0.5 * h * h * ko * ko)          # aussen offen
    eta_q = math.acosh(1.0 + 0.5 * h * h * q * q)          # aussen geschlossen
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
    # Randzeilen
    br, bc, bv = [], [], []
    rhs = np.zeros(n, dtype=complex)
    # links (j = 0, 1): abklingende Mode e2: y_e(1) = exp(eta_k) y_e(0)
    for cc in (0, 1):
        br += [0, 0]
        bc += [2 * 1 + cc, 2 * 0 + cc]
        bv += [e2[cc], -math.exp(eta_k) * e2[cc]]
    # links: laufende Mode e1 mit einlaufender Amplitude 1: y_p(1) - exp(-i th) y_p(0) = 2 i sin(th)
    for cc in (0, 1):
        br += [1, 1]
        bc += [2 * 1 + cc, 2 * 0 + cc]
        bv += [e1[cc], -complex(math.cos(th), -math.sin(th)) * e1[cc]]
    rhs[1] = 2j * math.sin(th)
    # rechts (j = N): geschlossen y1(N) = exp(-eta_q) y1(N-1); offen y2(N) = exp(i th_o) y2(N-1)
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
    b_ref = yp0 - 1.0                                       # reflektierte Amplitude bei j = 0
    t2 = abs(Y[2 * N + 1]) ** 2
    T = math.sin(th_o) * t2 / math.sin(th)
    R = abs(b_ref) ** 2
    return T, R, R + T - 1.0


def fd_nullstelle(mod, fz, d, h):
    res = minimize_scalar(lambda f: transmission_fd(mod, f, h)[0], bounds=(fz - d, fz + d), method="bounded",
                          options={"xatol": 1e-12, "maxiter": 200})
    return float(res.x), float(res.fun), int(res.nfev)


# ---------------------------------------------------------------- Hauptteil
def main():
    mname, fmin, fmax, n, pfad = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
    mod = MODELLE[mname]()
    t0 = time.time()
    out = {"modell": mname, "fenster": [fmin, fmax], "n": n, "rtol": RTOL, "atol": ATOL, "xa": mod.xa, "xb": mod.xb,
           "xa_fd": mod.xa_fd, "xb_fd": mod.xb_fd, "h_fd": list(H_FD), "version": 2}

    # K0: Hintergrund und Innen-Dispersion
    xs = np.linspace(mod.xa, mod.xb, 4001)
    out["k0_rest_max"] = float(max(abs(float(mod.rest(float(x)))) for x in xs))
    fk = np.linspace(fmin, fmax, 21)
    out["k0_dispersion_max_abw"] = float(max(abs(innen_moden(mod, float(f))[0] ** 2 - mod.k2_formel(float(f)))
                                             for f in fk))
    print(f"{mname}: K0 Rest {out['k0_rest_max']:.2e}, Dispersion {out['k0_dispersion_max_abw']:.2e}", flush=True)

    # Abtastung c_in
    fs = [float(f) for f in np.linspace(fmin, fmax, n)]
    werte, nfev = [], 0
    for f in fs:
        b, nf = c_in(mod, f)
        werte.append(b)
        nfev += nf
    out["abtastung"] = {"f": fs, "c_in": werte}
    print(f"{mname}: Abtastung fertig ({nfev} Auswertungen, {time.time() - t0:.1f} s)", flush=True)

    # Nullstellen und Gegenproben
    zlist = []
    for i in range(len(fs) - 1):
        a, b = werte[i], werte[i + 1]
        if not (a == 0.0 or a * b < 0.0):
            continue
        fz = brentq(lambda f: c_in(mod, f)[0], fs[i], fs[i + 1], xtol=1e-14, rtol=1e-15, maxiter=200)
        k, _, kap, _ = innen_moden(mod, fz)
        q, ko = aussen_raten(mod, fz)
        e = {"f_z": fz, "k_in": k, "kappa_in": kap, "q_aussen": q, "k_aussen": ko}
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
        e["T_fd_bei_f_z"] = {str(s): transmission_fd(mod, fz + s, H_FD[0]) for s in (-1e-3, -1e-4, 0.0, 1e-4, 1e-3)}
        if mname == "m1":
            e["b_inf"] = SQ2 * math.pi / k                          # 2 sqrt(beta) pi / k mit beta = 1/2
        else:
            e["n0"] = mod.n0
            e["dN_je_paritaet_1d"] = 2.0 * math.pi * mod.n0 / k
            e["dL_je_paritaet"] = 2.0 * math.pi / k
        zlist.append(e)
        print(f"{mname}: Nullstelle f_z = {fz:.10f} (FD Richardson {fd['richardson']:.10f}), k_in = {k:.6f}",
              flush=True)
    out["nullstellen"] = zlist

    # Transmission grob (FD, h = 0,004)
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
    print(f"{mname}: fertig, {len(zlist)} Nullstellen, Fluss max {out['fluss_max']:.2e}, {out['sek']:.1f} s",
          flush=True)


if __name__ == "__main__":
    main()
