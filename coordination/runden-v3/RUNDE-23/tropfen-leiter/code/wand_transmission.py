#!/usr/bin/env python3
"""TROPFEN-LEITER (Runde 23), Leitung claude-primary, 02.10.2026. Karte: RUNDE-23/tropfen-leiter/KARTE.md.

Ebene Wand bei reeller Frequenz f. Zwei Komponenten Y = (y1, y2) mit Y'' = P(x, f) Y, P reell symmetrisch.
Kanal 1 ist aussen geschlossen, Kanal 2 aussen offen (im Fenster). Innen (x -> -unendlich) hat P_in einen negativen
Eigenwert (laufende Mode, Wellenzahl k) und einen positiven (abklingende Mode, kappa).

  c_in(f):  Loesung, die aussen nur im geschlossenen Kanal abklingt (Koeffizient 1 vor exp(-q x)), nach innen
            integriert; Koeffizient der ins Innere wachsenden Mode exp(-kappa x). Nullstelle = Transmissionsnullstelle.
  D_out(f): Gegenprobe von innen: drei innen erlaubte Loesungen (cos, sin, exp(+kappa x)) nach aussen integriert;
            Determinante ihrer Koeffizienten (aussen wachsend geschlossen, offen cos, offen sin).
  T(f):     Streuloesung (aussen auslaufend plus abklingend), Transmission aus dem Fluss J = Im(Y^H Y').

Modelle:
  m1: U = S - S^2 + S^3/2, omega^2 = 1/2, S(x) = 1/(1 + exp(sqrt2 x)); y1 = A (Seitenband rho - omega), y2 = B (rho + omega).
  d1: i psi_t = -psi_xx/2 + |psi|^2 psi - |psi| psi, mu0 = -2/9, phi = (2/3)/(1 + exp(2x/3)); y1 = v, y2 = u.
  d3: i psi_t = -psi_xx/2 - 3|psi|^2 psi + (5/2)|psi|^3 psi, mu0 = -1/2, phi' = -phi(1 - phi) sqrt(1 + 2 phi); y1 = v, y2 = u.

Aufruf: python wand_transmission.py <m1|d1|d3> <f_min> <f_max> <n> <aus.json> [rtol] [xa] [xb]
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import json  # noqa: E402
import math  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
from scipy.integrate import solve_ivp  # noqa: E402
from scipy.optimize import brentq  # noqa: E402
from scipy.special import expit  # noqa: E402

SQ2 = math.sqrt(2.0)
OM1 = 1.0 / SQ2  # Frequenz des M1-Q-Balls an der ebenen Wand (omega^2 = 1/2)


# ---------------------------------------------------------------- Modelle
class M1:
    name = "m1"
    xa, xb = -25.0, 30.0

    @staticmethod
    def S(x):
        return expit(-SQ2 * x)

    def P(self, x, f):
        S = self.S(x)
        W = 1.0 - 4.0 * S + 4.5 * S * S          # U' + U'' S
        C = -2.0 * S + 3.0 * S * S                # U'' S
        return np.array([[W - (f - OM1) ** 2, C], [C, W - (f + OM1) ** 2]])

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
    """Gemeinsamer Teil der NLS-Tropfen: u'' = 2(h - w)u + 2Mv, v'' = 2Mu + 2(h + w)v; Y = (v, u)."""

    def P(self, x, f):
        h, M = self.hM(x)
        return np.array([[2.0 * (h + f), 2.0 * M], [2.0 * M, 2.0 * (h - f)]])

    def P_aussen(self, f):
        return np.array([[2.0 * (-self.mu0 + f), 0.0], [0.0, 2.0 * (-self.mu0 - f)]])

    def P_innen(self, f):
        h, M = self.hM_innen
        return np.array([[2.0 * (h + f), 2.0 * M], [2.0 * M, 2.0 * (h - f)]])


class D1(Tropfen):
    name = "d1"
    xa, xb = -45.0, 60.0
    mu0 = -2.0 / 9.0
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
    mu0 = -0.5
    hM_innen = (0.75, 0.75)

    def __init__(self):
        # Knick phi' = g(phi), phi(0) = 1/2; je Seite in der stabilen Richtung integriert, aussen phi, innen psi = 1 - phi
        g = lambda x, y: [-y[0] * (1.0 - y[0]) * math.sqrt(1.0 + 2.0 * y[0])]          # noqa: E731
        gpsi = lambda x, y: [(1.0 - y[0]) * y[0] * math.sqrt(3.0 - 2.0 * y[0])]        # noqa: E731  psi' = -phi'
        self.rechts = solve_ivp(g, (0.0, 80.0), [0.5], method="DOP853", rtol=1e-13, atol=1e-300, dense_output=True)
        self.links = solve_ivp(gpsi, (0.0, -60.0), [0.5], method="DOP853", rtol=1e-13, atol=1e-300,
                               dense_output=True)

    def phi_psi(self, x):
        if x >= 0.0:
            p = float(self.rechts.sol(x)[0])
            return p, 1.0 - p
        q = float(self.links.sol(x)[0])
        return 1.0 - q, q

    def hM(self, x):
        p, _ = self.phi_psi(x)
        return -self.mu0 - 6.0 * p * p + 6.25 * p ** 3, -3.0 * p * p + 3.75 * p ** 3

    @staticmethod
    def k2_formel(f):
        return 2.0 * math.sqrt(f * f + 9.0 / 16.0) - 1.5

    def rest(self, x):
        p, _ = self.phi_psi(x)
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


def integriere(mod, f, y0, x0, x1, rtol, komplex=False):
    def rhs(x, z):
        P = mod.P(x, f)
        return np.concatenate([z[2:], P @ z[:2]])

    z0 = np.asarray(y0, dtype=complex if komplex else float)
    sol = solve_ivp(rhs, (x0, x1), z0, method="DOP853", rtol=rtol, atol=1e-300)
    if not sol.success:
        raise RuntimeError(sol.message)
    return sol.y[:, -1], sol.nfev


def c_in(mod, f, rtol, xa=None, xb=None):
    xa = mod.xa if xa is None else xa
    xb = mod.xb if xb is None else xb
    q, _ = aussen_raten(mod, f)
    e = math.exp(-q * xb)
    z, nf = integriere(mod, f, [e, 0.0, -q * e, 0.0], xb, xa, rtol)
    k, e1, kap, e2 = innen_moden(mod, f)
    ye, ye1 = e2 @ z[:2], e2 @ z[2:]
    b = (kap * ye - ye1) / (2.0 * kap) * math.exp(kap * xa)       # Koeffizient vor exp(-kappa x)
    yp, yp1 = e1 @ z[:2], e1 @ z[2:]
    amp_lauf = math.hypot(yp, yp1 / k)                              # Betrag der laufenden Mode bei xa
    return b, amp_lauf, nf


def d_out(mod, f, rtol):
    q, ko = aussen_raten(mod, f)
    k, e1, kap, e2 = innen_moden(mod, f)
    xa, xb = mod.xa, mod.xb
    starts = [np.concatenate([e1 * math.cos(k * xa), -k * e1 * math.sin(k * xa)]),
              np.concatenate([e1 * math.sin(k * xa), k * e1 * math.cos(k * xa)]),
              np.concatenate([e2 * math.exp(kap * xa), kap * e2 * math.exp(kap * xa)])]
    zeilen = []
    for s in starts:
        z, _ = integriere(mod, f, s, xa, xb, rtol)
        y1, y1p, y2, y2p = z[0], z[2], z[1], z[3]
        alpha = (q * y1 + y1p) / (2.0 * q) * math.exp(-q * xb)    # Koeffizient vor exp(+q x)
        gam = y2 * math.cos(ko * xb) - y2p / ko * math.sin(ko * xb)  # y2 = gam cos(ko x) + dlt sin(ko x)
        dlt = y2 * math.sin(ko * xb) + y2p / ko * math.cos(ko * xb)
        zeilen.append([alpha, gam, dlt])
    return float(np.linalg.det(np.array(zeilen)))


def transmission(mod, f, rtol):
    q, ko = aussen_raten(mod, f)
    k, e1, kap, e2 = innen_moden(mod, f)
    xa, xb = mod.xa, mod.xb
    e = math.exp(-q * xb)
    s1 = np.array([e, 0.0, -q * e, 0.0], dtype=complex)
    w = complex(math.cos(ko * xb), math.sin(ko * xb))
    s2 = np.array([0.0, w, 0.0, 1j * ko * w], dtype=complex)
    z1, _ = integriere(mod, f, s1, xb, xa, rtol, komplex=True)
    z2, _ = integriere(mod, f, s2, xb, xa, rtol, komplex=True)

    def bkoef(z):
        ye, ye1 = e2 @ z[:2], e2 @ z[2:]
        return (kap * ye - ye1) / (2.0 * kap)

    z = z2 - (bkoef(z2) / bkoef(z1)) * z1
    yp, yp1 = e1 @ z[:2], e1 @ z[2:]
    ap = 0.5 * (yp + yp1 / (1j * k)) * np.exp(-1j * k * xa)
    am = 0.5 * (yp - yp1 / (1j * k)) * np.exp(1j * k * xa)
    J_in = k * (abs(ap) ** 2 - abs(am) ** 2)
    J_aus = ko
    gross, klein = max(abs(ap), abs(am)), min(abs(ap), abs(am))
    T = ko / (k * gross ** 2)
    R = (klein / gross) ** 2
    return {"f": f, "T": T, "R": R, "R_plus_T": R + T, "fluss_rel_fehler": abs(abs(J_in) - J_aus) / J_aus}


def nullstellen(mod, fs, werte, rtol):
    out = []
    for i in range(len(fs) - 1):
        a, b = werte[i], werte[i + 1]
        if a == 0.0 or a * b < 0.0:
            g = lambda f: c_in(mod, f, rtol)[0]   # noqa: E731
            fz = brentq(g, fs[i], fs[i + 1], xtol=1e-14, rtol=1e-15, maxiter=200)
            out.append(fz)
    return out


# ---------------------------------------------------------------- Hauptteil
def main():
    mname, fmin, fmax, n, pfad = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
    rtol = float(sys.argv[6]) if len(sys.argv) > 6 else 1e-11
    mod = MODELLE[mname]()
    if len(sys.argv) > 7:
        mod.xa = float(sys.argv[7])
    if len(sys.argv) > 8:
        mod.xb = float(sys.argv[8])
    t0 = time.time()
    out = {"modell": mname, "fenster": [fmin, fmax], "n": n, "rtol": rtol, "xa": mod.xa, "xb": mod.xb, "version": 1}

    # K0: Hintergrund und Innen-Dispersion
    xs = np.linspace(mod.xa, mod.xb, 4001)
    out["k0_rest_max"] = float(max(abs(mod.rest(float(x))) for x in xs))
    fk = np.linspace(fmin, fmax, 21)
    out["k0_dispersion_max_abw"] = float(max(abs(innen_moden(mod, float(f))[0] ** 2 - mod.k2_formel(float(f)))
                                             for f in fk))
    print(f"{mname}: K0 Rest {out['k0_rest_max']:.2e}, Dispersion {out['k0_dispersion_max_abw']:.2e}", flush=True)

    # Abtastung c_in
    fs = np.linspace(fmin, fmax, n)
    werte, laeufe, nfev = [], [], 0
    for f in fs:
        b, amp, nf = c_in(mod, float(f), rtol)
        werte.append(b)
        laeufe.append(amp)
        nfev += nf
    out["abtastung"] = {"f": fs.tolist(), "c_in": werte, "amp_lauf": laeufe}
    print(f"{mname}: Abtastung fertig ({nfev} Auswertungen, {time.time() - t0:.1f} s)", flush=True)

    # Nullstellen und Gegenproben
    nz = nullstellen(mod, [float(f) for f in fs], werte, rtol)
    zlist = []
    for fz in nz:
        k, _, kap, _ = innen_moden(mod, fz)
        q, ko = aussen_raten(mod, fz)
        e = {"f_z": fz, "k_in": k, "kappa_in": kap, "q_aussen": q, "k_aussen": ko}
        # andere Toleranz
        g2 = lambda f: c_in(mod, f, 1e-9)[0]   # noqa: E731
        d = 2e-4 * max(1.0, abs(fz))
        try:
            e["f_z_rtol1e-9"] = brentq(g2, fz - d, fz + d, xtol=1e-14, rtol=1e-15, maxiter=200)
        except ValueError as ex:
            e["f_z_rtol1e-9"] = f"kein Vorzeichenwechsel: {ex}"
        # groesseres Gebiet
        g3 = lambda f: c_in(mod, f, rtol, mod.xa - 10.0, mod.xb + 10.0)[0]   # noqa: E731
        try:
            e["f_z_gebiet_plus10"] = brentq(g3, fz - d, fz + d, xtol=1e-14, rtol=1e-15, maxiter=200)
        except ValueError as ex:
            e["f_z_gebiet_plus10"] = f"kein Vorzeichenwechsel: {ex}"
        # Gegenprobe von innen
        try:
            e["f_z_d_out"] = brentq(lambda f: d_out(mod, f, rtol), fz - d, fz + d, xtol=1e-14, rtol=1e-15,
                                    maxiter=200)
        except ValueError as ex:
            e["f_z_d_out"] = f"kein Vorzeichenwechsel: {ex}"
        # Transmission an und neben der Nullstelle
        e["T_bei"] = [transmission(mod, fz + s, rtol) for s in (-1e-3, -1e-4, -1e-6, 0.0, 1e-6, 1e-4, 1e-3)]
        if mname == "m1":
            e["b_inf"] = SQ2 * math.pi / k                          # 2 sqrt(beta) pi / k mit beta = 1/2
        else:
            n0 = (-mod.mu0) * 2.0 if mname == "d1" else 1.0       # d1: n0 = 4/9 = 2 |mu0|; d3: n0 = 1
            e["n0"] = n0
            e["dN_je_paritaet_1d"] = 2.0 * math.pi * n0 / k
            e["dL_je_paritaet"] = 2.0 * math.pi / k
        zlist.append(e)
        print(f"{mname}: Nullstelle f_z = {fz:.10f}, k_in = {k:.6f}", flush=True)
    out["nullstellen"] = zlist

    # Transmission grob
    tgrob = []
    for f in np.linspace(fmin, fmax, max(11, n // 5)):
        try:
            tgrob.append(transmission(mod, float(f), rtol))
        except Exception as ex:  # noqa: BLE001
            tgrob.append({"f": float(f), "fehler": repr(ex)})
    out["transmission_grob"] = tgrob
    fl = [t["fluss_rel_fehler"] for t in tgrob if "fluss_rel_fehler" in t]
    out["fluss_rel_fehler_max"] = max(fl) if fl else None
    out["sek"] = time.time() - t0
    with open(pfad + ".tmp", "w") as fh:
        json.dump(out, fh, indent=1)
    os.replace(pfad + ".tmp", pfad)
    print(f"{mname}: fertig, {len(zlist)} Nullstellen, Fluss-Fehler max {out['fluss_rel_fehler_max']}, "
          f"{out['sek']:.1f} s", flush=True)


if __name__ == "__main__":
    main()
