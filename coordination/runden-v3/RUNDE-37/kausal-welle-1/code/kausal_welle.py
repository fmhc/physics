"""KAUSAL-WELLE-1 (Runde 37, Code-Agent): massive Wellenpakete auf 1+1-Kausalmengen, Johnstons retardierter Propagator.

Quelle [S]: S. Johnston, "Particle propagators on discrete spacetime", Class. Quantum Grav. 25 (2008) 202001,
arXiv:0806.3083v2: (2.1) (A_C)_ij = 1 wenn v_i < v_j; (3.1) Phi = a A_C; (3.3)/(3.5) K = I + Phi (I - b Phi)^-1;
(3.31) in 1+1: a = 1/2, b = -m^2/rho; (3.23) Kontinuum K_m = (1/2) J0(m tau) im Vorwaertskegel; (3.17) (Box + m^2) K = delta.

Feld (ohne den Konventionsterm I): phi(x) = (1/rho) sum_{y<x} (K - I)(y, x) J(y) = (1/(2 rho)) (C psi)(x),
psi = (I + (m^2/(2 rho)) C)^-1 J, (C f)(x) = sum_{y<x} f(y). Vorwaertsrekursion psi(x) = J(x) - a (C psi)(x), a = m^2/(2 rho).

Rechenweg: Punkte nach u sortiert; CDQ-Teilung in u (Beitrag linke -> rechte Haelfte als 1D-Praefixsumme in v), Blaetter mit
<= B Punkten dicht geloest (Dreieckssystem). Sechs Quellen (sigma in 2, 4, 8; eta in 0, 1) laufen als Spalten auf derselben
Streuung.

Koordinaten: u = (t - x)/sqrt2, v = (t + x)/sqrt2, dt dx = du dv, tau^2 = 2 du dv. Dichte rho je Flaecheneinheit in (t, x).
Gebiet: D = J+(Scheibe r0) geschnitten {t <= tb}, r0 = 4,5 sigma_max, tb = 3 sigma_max + 20. D ist kausal konvex und enthaelt
den Traeger aller Quellen; phi ist daher an jedem Punkt von D exakt (keine Randpunkte mit unvollstaendiger Vergangenheit).

Aufruf (nur ueber kleintest.sh auf der .69):
  kausal_welle.py feld  <rho> <saat_von> <saat_bis> <ausgabeordner> [zeitgrenze_s]
  kausal_welle.py punkt <rho> <saat_von> <saat_bis> <ausgabeordner>
  kausal_welle.py probe <rho> <saat> <ausgabeordner>
"""
import hashlib
import json
import os
import sys
import time

import numpy as np
from scipy.linalg import solve_triangular
from scipy.special import j0

SKRIPT_SHA = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
SQ2 = np.sqrt(2.0)
MASSE = 1.0
SIGMAS = (2.0, 4.0, 8.0)
ETAS = (0.0, 1.0)
CONFIGS = [(s, e) for s in SIGMAS for e in ETAS]
NC = len(CONFIGS)
SIG = np.array([c[0] for c in CONFIGS])
OM = np.cosh(np.array([c[1] for c in CONFIGS])) * MASSE
PP = np.sinh(np.array([c[1] for c in CONFIGS])) * MASSE
VN = np.tanh(np.array([c[1] for c in CONFIGS]))
R0_FAKTOR = 4.5
R0C = R0_FAKTOR * SIG
T_LAUF = 20.0
TA = 3.0 * SIG
W_SCHEIBE = 0.5
N_SCHEIBEN = 40
XB_MIN = -140
XB_N = 280
B_BLATT = 128
# Pruefpunkte (KW0): t in {ta, ta + 10, ta + 20}, x = tanh(eta) t; Profilpunkte bei t = tb: x = tanh(eta) tb + 2 j
PRUEF_DT = (0.0, 10.0, 20.0)
PROFIL_J = np.arange(-10, 11)


def pruefpunkte():
    """(NC, 24, 2) Feld (t, x): 3 Pruefpunkte, dann 21 Profilpunkte."""
    out = np.zeros((NC, 3 + PROFIL_J.size, 2))
    for c in range(NC):
        for i, dt in enumerate(PRUEF_DT):
            t = TA[c] + dt
            out[c, i] = (t, VN[c] * t)
        tb = TA[c] + T_LAUF
        out[c, 3:, 0] = tb
        out[c, 3:, 1] = VN[c] * tb + 2.0 * PROFIL_J
    return out


class Loeser:
    """Vorwaertsrekursion psi = J - a C psi auf nach u sortierten Punkten (CDQ + dichte Blaetter)."""

    def __init__(self, u, v, rho, quelle, ncol):
        self.U = u
        self.V = v
        self.rho = rho
        self.a = MASSE ** 2 / (2.0 * rho)
        self.quelle = quelle
        self.PSI = np.zeros((u.size, ncol), dtype=np.complex128)
        self.S = np.zeros((u.size, ncol), dtype=np.complex128)

    def blatt(self, lo, hi):
        vb = self.V[lo:hi]
        Jb = self.quelle(lo, hi)
        r = np.ascontiguousarray(Jb - self.a * self.S[lo:hi])
        Mb = np.tril(vb[None, :] < vb[:, None], -1).astype(np.float64)
        rr = r.view(np.float64)
        ps = solve_triangular(self.a * Mb, rr, lower=True, unit_diagonal=True, check_finite=False)
        ps = np.ascontiguousarray(ps)
        self.PSI[lo:hi] = ps.view(np.complex128)
        self.S[lo:hi] += (Mb @ ps).view(np.complex128)

    def cdq(self, lo, hi):
        if hi - lo <= B_BLATT:
            self.blatt(lo, hi)
            return
        mid = (lo + hi) >> 1
        self.cdq(lo, mid)
        vl = self.V[lo:mid]
        o = np.argsort(vl)
        cs = np.empty((mid - lo + 1, self.PSI.shape[1]), dtype=np.complex128)
        cs[0] = 0.0
        np.cumsum(self.PSI[lo:mid][o], axis=0, out=cs[1:])
        pos = np.searchsorted(vl[o], self.V[mid:hi])
        self.S[mid:hi] += cs[pos]
        del cs, o
        self.cdq(mid, hi)

    def loesen(self):
        sys.setrecursionlimit(10000)
        self.cdq(0, self.U.size)

    def zuschauer(self, ut, vt, c):
        """phi an einem Punkt ausserhalb der Menge (Palm-Lesart): (1/(2 rho)) sum_{u<ut, v<vt} psi."""
        k = np.searchsorted(self.U, ut)
        m = self.V[:k] < vt
        return complex(self.PSI[:k, c][m].sum() / (2.0 * self.rho))


def streuen_kegel(rng, rho, r0, tb):
    """Poisson-Streuung in D = J+(Scheibe r0 um 0) geschnitten {t <= tb}; Rueckgabe nach u sortiert."""
    L = SQ2 * tb + 2.0 * r0
    n = rng.poisson(rho * L * L / 2.0)
    a = rng.random(n) * L
    b = rng.random(n) * L
    f = a + b > L
    a[f] = L - a[f]
    b[f] = L - b[f]
    u = a - r0
    v = b - r0
    del a, b, f
    ecke = (u < 0) & (v < 0) & (u * u + v * v > r0 * r0)
    u = u[~ecke]
    v = v[~ecke]
    o = np.argsort(u, kind="stable")
    return np.ascontiguousarray(u[o]), np.ascontiguousarray(v[o])


def quelle_feld(U, V):
    def q(lo, hi):
        u = U[lo:hi]
        v = V[lo:hi]
        t = (u + v) / SQ2
        x = (v - u) / SQ2
        r2 = (t * t + x * x)[:, None]
        ph = -r2 / (2.0 * SIG ** 2) - 1j * (OM * t[:, None] - PP * x[:, None])
        J = np.exp(ph)
        J *= (r2 <= R0C ** 2)
        return J
    return q


def messen(L, rho):
    """Summen je (Konfiguration, Scheibe, x-Klasse relativ zu tanh(eta) t): |phi|^2, x|phi|^2, t|phi|^2, x^2|phi|^2, Zahl."""
    t = (L.U + L.V) / SQ2
    x = (L.V - L.U) / SQ2
    out = np.zeros((NC, N_SCHEIBEN, XB_N, 5))
    for c in range(NC):
        k = np.floor((t - TA[c]) / W_SCHEIBE).astype(np.int64)
        d = x - VN[c] * t
        j = np.floor(d).astype(np.int64) - XB_MIN
        ok = (k >= 0) & (k < N_SCHEIBEN) & (j >= 0) & (j < XB_N)
        idx = k[ok] * XB_N + j[ok]
        ph = L.S[ok, c] / (2.0 * rho)
        w2 = ph.real ** 2 + ph.imag ** 2
        nb = N_SCHEIBEN * XB_N
        out[c, :, :, 0] = np.bincount(idx, weights=w2, minlength=nb).reshape(N_SCHEIBEN, XB_N)
        out[c, :, :, 1] = np.bincount(idx, weights=w2 * x[ok], minlength=nb).reshape(N_SCHEIBEN, XB_N)
        out[c, :, :, 2] = np.bincount(idx, weights=w2 * t[ok], minlength=nb).reshape(N_SCHEIBEN, XB_N)
        out[c, :, :, 3] = np.bincount(idx, weights=w2 * x[ok] ** 2, minlength=nb).reshape(N_SCHEIBEN, XB_N)
        out[c, :, :, 4] = np.bincount(idx, minlength=nb).reshape(N_SCHEIBEN, XB_N)
    return out


def lauf_feld(rho, saat):
    t0 = time.time()
    rng = np.random.default_rng(np.random.SeedSequence([20261004, 37, 71, int(rho), int(saat)]))
    r0 = R0_FAKTOR * max(SIGMAS)
    tb = 3.0 * max(SIGMAS) + T_LAUF
    U, V = streuen_kegel(rng, rho, r0, tb)
    t1 = time.time()
    L = Loeser(U, V, rho, quelle_feld(U, V), NC)
    L.loesen()
    t2 = time.time()
    summen = messen(L, rho)
    pp = pruefpunkte()
    phi_p = np.zeros((NC, pp.shape[1]), dtype=np.complex128)
    for c in range(NC):
        for i in range(pp.shape[1]):
            tt, xx = pp[c, i]
            phi_p[c, i] = L.zuschauer((tt - xx) / SQ2, (tt + xx) / SQ2, c)
    t3 = time.time()
    kopf = {"modus": "feld", "rho": rho, "saat": saat, "N": int(U.size), "r0": r0, "tb": tb,
            "zeit_streuen_s": round(t1 - t0, 2), "zeit_loesen_s": round(t2 - t1, 2),
            "zeit_messen_s": round(t3 - t2, 2), "zeit_gesamt_s": round(t3 - t0, 2),
            "max_abs_psi": float(np.abs(L.PSI).max()), "endlich": bool(np.isfinite(L.S).all()),
            "skript_sha256": SKRIPT_SHA, "numpy": np.__version__,
            "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    return kopf, summen, phi_p


def lauf_punkt(rho, saat):
    """Normierungsprobe: Punktquelle J = rho am Ursprung (eingefuegt), Erwartung phi = K = (1/2) J0(m tau)."""
    t0 = time.time()
    rng = np.random.default_rng(np.random.SeedSequence([20261004, 37, 72, int(rho), int(saat)]))
    Tp = 25.0
    Lk = SQ2 * Tp
    n = rng.poisson(rho * Lk * Lk / 2.0)
    a = rng.random(n) * Lk
    b = rng.random(n) * Lk
    f = a + b > Lk
    a[f] = Lk - a[f]
    b[f] = Lk - b[f]
    u = np.concatenate([[0.0], a])
    v = np.concatenate([[0.0], b])
    o = np.argsort(u, kind="stable")
    U = np.ascontiguousarray(u[o])
    V = np.ascontiguousarray(v[o])

    def q(lo, hi):
        J = np.zeros((hi - lo, 1), dtype=np.complex128)
        if lo == 0:
            J[0, 0] = rho
        return J

    L = Loeser(U, V, rho, q, 1)
    L.loesen()
    taus = np.array([0.5, 1.0, 2.0, 3.0, 5.0, 8.0, 12.0, 16.0])
    zetas = np.array([0.0, 0.5, 1.0])
    werte = np.zeros((zetas.size, taus.size))
    for i, z in enumerate(zetas):
        for k, ta in enumerate(taus):
            tt, xx = ta * np.cosh(z), ta * np.sinh(z)
            werte[i, k] = L.zuschauer((tt - xx) / SQ2, (tt + xx) / SQ2, 0).real
    kopf = {"modus": "punkt", "rho": rho, "saat": saat, "N": int(U.size), "taus": taus.tolist(),
            "zetas": zetas.tolist(), "soll": (0.5 * j0(MASSE * taus)).tolist(), "werte": werte.tolist(),
            "zeit_gesamt_s": round(time.time() - t0, 2), "skript_sha256": SKRIPT_SHA,
            "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    return kopf


def lauf_probe(rho, saat):
    """Codeprobe: CDQ gegen dichte Loesung (I + a A) psi = J auf einer kleinen Streuung; Zuschauer gegen Maskensumme."""
    rng = np.random.default_rng(np.random.SeedSequence([20261004, 37, 73, int(rho), int(saat)]))
    U, V = streuen_kegel(rng, rho, 9.0, 8.0)
    L = Loeser(U, V, rho, quelle_feld(U, V), NC)
    L.loesen()
    N = U.size
    A = ((U[None, :] < U[:, None]) & (V[None, :] < V[:, None])).astype(np.float64)
    J = quelle_feld(U, V)(0, N)
    a = MASSE ** 2 / (2.0 * rho)
    psi = solve_triangular(np.eye(N) + a * A, J, lower=True)
    S = A @ psi
    d_psi = float(np.abs(psi - L.PSI).max() / np.abs(psi).max())
    d_S = float(np.abs(S - L.S).max() / np.abs(S).max())
    # Reihe: K - I = (1/2) A sum_k (-a A)^k, abgebrochen, gegen die Rekursion
    reihe = np.zeros_like(J)
    term = J.copy()
    for _ in range(60):
        reihe += term
        term = -a * (A @ term)
    S_reihe = A @ reihe
    d_reihe = float(np.abs(S_reihe - L.S).max() / np.abs(S).max())
    zz = []
    for (tt, xx) in [(3.0, 0.5), (6.0, -2.0), (7.5, 1.0)]:
        ut, vt = (tt - xx) / SQ2, (tt + xx) / SQ2
        m = (U < ut) & (V < vt)
        for c in range(NC):
            ref = psi[m, c].sum() / (2.0 * rho)
            zz.append(abs(L.zuschauer(ut, vt, c) - ref) / max(abs(ref), 1e-300))
    return {"modus": "probe", "rho": rho, "saat": saat, "N": int(N), "rel_abw_psi": d_psi, "rel_abw_S": d_S,
            "rel_abw_reihe": d_reihe, "rel_abw_zuschauer_max": float(max(zz)), "skript_sha256": SKRIPT_SHA,
            "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}


def main():
    modus = sys.argv[1]
    rho = float(sys.argv[2])
    if modus == "probe":
        saat, ordner = int(sys.argv[3]), sys.argv[4]
        os.makedirs(ordner, exist_ok=True)
        kopf = lauf_probe(rho, saat)
        with open(os.path.join(ordner, f"probe-r{int(rho)}-s{saat}.json"), "w") as fh:
            json.dump(kopf, fh, indent=1)
        print(json.dumps(kopf))
        return
    s0, s1, ordner = int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
    grenze = float(sys.argv[6]) if len(sys.argv) > 6 else 540.0
    os.makedirs(ordner, exist_ok=True)
    start = time.time()
    dauer_max = 0.0
    for saat in range(s0, s1 + 1):
        if time.time() - start + 1.3 * dauer_max > grenze:
            print(json.dumps({"abbruch_vor_saat": saat, "grund": "zeitgrenze", "verstrichen_s": round(time.time() - start, 1)}))
            break
        ts = time.time()
        if modus == "feld":
            kopf, summen, phi_p = lauf_feld(rho, saat)
            np.savez_compressed(os.path.join(ordner, f"feld-r{int(rho)}-s{saat}.npz"), summen=summen, phi_p=phi_p,
                                pruefpunkte=pruefpunkte())
            with open(os.path.join(ordner, f"feld-r{int(rho)}-s{saat}.json"), "w") as fh:
                json.dump(kopf, fh, indent=1)
        elif modus == "punkt":
            kopf = lauf_punkt(rho, saat)
            with open(os.path.join(ordner, f"punkt-r{int(rho)}-s{saat}.json"), "w") as fh:
                json.dump(kopf, fh, indent=1)
        else:
            raise SystemExit("unbekannter Modus")
        dauer_max = max(dauer_max, time.time() - ts)
        print(json.dumps({k: kopf[k] for k in kopf if k not in ("werte", "soll", "taus", "zetas")}), flush=True)


if __name__ == "__main__":
    main()
