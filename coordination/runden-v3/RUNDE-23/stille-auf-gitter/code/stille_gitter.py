#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
STILLE-AUF-GITTER (RUNDE-23): Restbreite der stillen Mode (Sprosse n = 7) eines 2D-Q-Balls
im Modell M1 auf dem Quadratgitter.

- Modell: U(S) = S - S^2 + S^3/2, S = |phi|^2. Q-Ball phi = f e^{i omega t}, f reell.
- Gitter-Q-Ball: Newton bei festem omega auf dem A1-Achtelgebiet (C4v), Start = radiales Profil.
- Linearisierung psi = u e^{-i rho t} + conj(v) e^{i conj(rho) t}:
    [-Lap + V1 - (omega - rho)^2] u + W v = 0     (geschlossen, kappa ~ 0,56)
    [-Lap + V1 - (omega + rho)^2] v + W u = 0     (offen, k ~ 2,05, auslaufend ~ e^{+ikr})
  V1 = U'(f^2) + U''(f^2) f^2, W = U''(f^2) f^2.
- Auslaufender Rand: komplexe Koordinatenstreckung s(x) = 1 + i sig0 ((|x| - Lin)/Lpml)^p in x und y
  (gleiche 1D-Matrix in beiden Richtungen, damit C4v exakt bleibt), Dirichlet ausserhalb.
- Stern A: 5 Punkte. Stern B: isotroper 9-Punkt-Stern = D_xx + D_yy + (h^2/6) D_xx D_yy
  (= (1/(6h^2)) [4 (N+S+O+W) + (NO+NW+SO+SW) - 20 Z] ohne Streckung).
- Eigenwert per Shift-Invert-Arnoldi (lineare Einbettung des quadratischen Problems), danach
  zweiseitiges Rayleigh-Funktional mit Rechts- und Linksvektor aus inverser Iteration.
- Gamma = -Im rho (Konvention RUNDE-12: Breite = |Im rho|, ohne Faktor 2).
"""
import os
for _k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_k, "1")
import sys
import json
import time
import math
import argparse
import hashlib
import numpy as np
import scipy
import scipy.sparse as sp
import scipy.sparse.linalg as spla
from scipy.ndimage import map_coordinates, spline_filter

T0 = time.time()
RHO_STEIGUNG = 5.9  # d Re rho / d omega^2 an der Sprosse (RUNDE-12 FEIN), nur fuer die Shift-Vorhersage


def log(*a):
    print("[%7.1fs]" % (time.time() - T0), *a, flush=True)


def U1(S):  # dU/dS
    return 1.0 - 2.0 * S + 1.5 * S * S


def U2(S):  # d2U/dS2
    return -2.0 + 3.0 * S


# ---------------------------------------------------------------- radiales Kontinuumsprofil (nur Startwert)
def radial_profil(om2, dr=0.02, rmax=60.0):
    J = int(round(rmax / dr))
    r = (np.arange(J) + 0.5) * dr
    rp = r + 0.5 * dr
    rm = r - 0.5 * dr
    main = -(rp + rm) / (r * dr * dr)
    up = rp[:-1] / (r[:-1] * dr * dr)
    lo = rm[1:] / (r[1:] * dr * dr)
    Lr = sp.diags([lo, main, up], [-1, 0, 1], format="csc")
    eps = om2 - 0.5
    Sin = (2.0 + math.sqrt(4.0 - 6.0 * (1.0 - om2))) / 3.0
    fin = math.sqrt(Sin)
    R00 = 0.3536 / eps
    for dR in (0.0, -0.7, 0.7, -1.5, 1.5, -2.5, 2.5):
        R0 = R00 + dR
        f = fin / np.sqrt(1.0 + np.exp(np.clip(math.sqrt(2.0) * (r - R0), -700.0, 700.0)))
        nF = np.inf
        for it in range(100):
            S = f * f
            F = -(Lr @ f) + (U1(S) - om2) * f
            nF = float(np.max(np.abs(F)))
            if nF < 1e-10:
                break
            Jm = (-Lr + sp.diags(U1(S) + 2.0 * U2(S) * S - om2)).tocsc()
            df = spla.spsolve(Jm, -F)
            lam = 1.0
            while True:
                fn = f + lam * df
                Sn = fn * fn
                nFn = float(np.max(np.abs(-(Lr @ fn) + (U1(Sn) - om2) * fn)))
                if nFn < (1.0 - 0.25 * lam) * nF or lam < 1e-4:
                    break
                lam *= 0.5
            f = fn
        if nF < 1e-9 and f[0] > 0.8:
            return r, f, dict(R0=R0, it=it, res=nF, f0=float(f[0]))
    raise RuntimeError("radiales Profil: kein Q-Ball gefunden")


# ---------------------------------------------------------------- Gitter
class Gitter:
    def __init__(self, h, stern, Lin, Lpml, sig0, pexp):
        self.h = float(h)
        self.stern = stern
        self.Lin, self.Lpml, self.sig0, self.pexp = float(Lin), float(Lpml), float(sig0), float(pexp)
        M = int(math.ceil((Lin + Lpml) / h - 1e-9))
        self.M = M
        n = 2 * M + 1
        self.n = n
        self.Lout = M * h
        a = np.repeat(np.arange(M + 1), np.arange(1, M + 2))
        b = np.concatenate([np.arange(k + 1) for k in range(M + 1)])
        self.a, self.b = a, b
        self.N = len(a)
        self.r = h * np.sqrt(a.astype(float) ** 2 + b.astype(float) ** 2)
        I = np.arange(n) - M
        IX, IY = np.meshgrid(I, I)  # [iy, ix]
        AX, AY = np.abs(IX), np.abs(IY)
        A_ = np.maximum(AX, AY)
        B_ = np.minimum(AX, AY)
        e = (A_ * (A_ + 1)) // 2 + B_
        self.P = sp.csr_matrix((np.ones(n * n), (np.arange(n * n), e.ravel())), shape=(n * n, self.N))
        self.rows = (b + M) * n + (a + M)  # kanonischer Punkt x = a h >= y = b h >= 0
        self.L8r = self._lap(0.0).real.tocsr()
        self.L8c = self._lap(self.sig0).tocsr()
        self.idx_achse = (np.arange(M + 1) * (np.arange(M + 1) + 1)) // 2
        self.idx_diag = self.idx_achse + np.arange(M + 1)

    def _d1(self, sig0):
        n, M, h = self.n, self.M, self.h
        x = (np.arange(n) - M) * h

        def s(xx):
            if sig0 == 0.0:
                return np.ones_like(xx)
            t = np.clip((np.abs(xx) - self.Lin) / self.Lpml, 0.0, None)
            return 1.0 + 1j * sig0 * t ** self.pexp

        si, spl, smi = s(x), s(x + 0.5 * h), s(x - 0.5 * h)
        main = -(1.0 / spl + 1.0 / smi) / (si * h * h)
        up = 1.0 / (si[:-1] * spl[:-1] * h * h)
        lo = 1.0 / (si[1:] * smi[1:] * h * h)
        return sp.diags([lo, main, up], [-1, 0, 1], format="csr")

    def _lap(self, sig0):
        D = self._d1(sig0)
        I = sp.identity(self.n, format="csr", dtype=D.dtype)
        Lf = sp.kron(I, D, format="csr") + sp.kron(D, I, format="csr")
        if self.stern == "B":
            Lf = Lf + (self.h * self.h / 6.0) * sp.kron(D, D, format="csr")
        elif self.stern != "A":
            raise ValueError("Stern A oder B")
        return (Lf[self.rows, :] @ self.P).tocsr()

    # ------------------------------------------------ Hintergrund
    def qball(self, om2, f0, tol=1e-11, maxit=40):
        f = f0.copy()
        L = self.L8r
        hist = []
        it = 0
        nF = np.inf
        for it in range(maxit):
            S = f * f
            F = -(L @ f) + (U1(S) - om2) * f
            nF = float(np.max(np.abs(F)))
            hist.append(nF)
            if nF < tol:
                break
            if len(hist) >= 3 and nF < 1e-8 and nF > 0.3 * hist[-2]:
                break  # Rundungsboden
            J = (-L + sp.diags(U1(S) + 2.0 * U2(S) * S - om2)).tocsc()
            df = spla.splu(J).solve(-F)
            lam = 1.0
            while True:
                fn = f + lam * df
                Sn = fn * fn
                nFn = float(np.max(np.abs(-(L @ fn) + (U1(Sn) - om2) * fn)))
                if nFn < (1.0 - 0.25 * lam) * nF or lam < 1e-4:
                    break
                lam *= 0.5
            f = fn
        return f, nF, it

    def radien(self, f):
        """Halbwertsradius (f = f(0)/2) entlang Achse und Diagonale."""
        f0 = f[0]
        out = {}
        for name, idx, fak in (("achse", self.idx_achse, 1.0), ("diag", self.idx_diag, math.sqrt(2.0))):
            fa = f[idx]
            k = int(np.argmax(fa < 0.5 * f0))
            if k == 0:
                out[name] = float("nan")
                continue
            t = (fa[k - 1] - 0.5 * f0) / (fa[k - 1] - fa[k])
            out[name] = float((k - 1 + t) * self.h * fak)
        return out

    # ------------------------------------------------ Linearisierung
    def lin(self, f, om2):
        S = f * f
        V1 = U1(S) + U2(S) * S
        W = U2(S) * S
        A = (-self.L8c + sp.diags((V1 - om2).astype(complex))).tocsr()
        Wd = sp.diags(W.astype(complex))
        K = sp.bmat([[A, Wd], [Wd, A]], format="csc")
        om = math.sqrt(om2)
        cd = np.concatenate([np.full(self.N, 2.0 * om), np.full(self.N, -2.0 * om)]).astype(complex)
        return K, cd

    # ------------------------------------------------ Winkelzerlegung
    def _koef(self, v8):
        full = (self.P @ v8).reshape(self.n, self.n)
        return spline_filter(full.real, order=3), spline_filter(full.imag, order=3)

    def _kreis(self, koef, r, Nth=512, jmax=6):
        th = 2.0 * np.pi * np.arange(Nth) / Nth
        X = r * np.cos(th)
        Y = r * np.sin(th)
        co = [Y / self.h + self.M, X / self.h + self.M]
        vals = (map_coordinates(koef[0], co, order=3, mode="nearest", prefilter=False)
                + 1j * map_coordinates(koef[1], co, order=3, mode="nearest", prefilter=False))
        c = np.fft.fft(vals) / Nth
        return np.array([c[0]] + [c[4 * j] + c[-4 * j] for j in range(1, jmax + 1)])

    def l0_anteil(self, x, R):
        """Anteil von l = 0 an der Norm von u und v auf zwei Innenkreisen (0,4 R und 0,7 R)."""
        N = self.N
        num = 0.0
        den = 0.0
        for comp in (x[:N], x[N:]):
            koef = self._koef(comp)
            for rr in (0.4 * R, 0.7 * R):
                aj = self._kreis(koef, rr)
                num += 2.0 * abs(aj[0]) ** 2
                den += 2.0 * abs(aj[0]) ** 2 + float(np.sum(np.abs(aj[1:]) ** 2))
        return num / den if den > 0 else float("nan")

    def fluss(self, x, rc, dr=0.25, jmax=6):
        """Radialer Fluss des offenen Kanals v je Winkelkanal cos(4 j theta) auf dem Kreis rc."""
        v = x[self.N:]
        koef = self._koef(v)
        a0 = self._kreis(koef, rc, jmax=jmax)
        ap = self._kreis(koef, rc + dr, jmax=jmax)
        am = self._kreis(koef, rc - dr, jmax=jmax)
        da = (ap - am) / (2.0 * dr)
        Nj = np.array([2.0 * np.pi] + [np.pi] * jmax)
        F = Nj * rc * np.imag(np.conj(a0) * da)
        tot = float(np.sum(F))
        return dict(rc=rc, F=[float(q) for q in F], F_ges=tot,
                    anteil=[float(q / tot) if tot != 0 else float("nan") for q in F],
                    betrag=[float(abs(q)) for q in a0])


# ---------------------------------------------------------------- Eigenwerte
def eig_sinv(K, cd, sigma, nev, ncv=None, tol=1e-13):
    n2 = K.shape[0]
    Q = (K + sp.diags(sigma * cd - sigma * sigma)).tocsc()
    lu = spla.splu(Q)
    cms = cd - sigma

    def mv(z):
        z = np.asarray(z).ravel()
        a = z[:n2]
        b = z[n2:]
        x = lu.solve(b - cms * a)
        return np.concatenate([x, a + sigma * x])

    Op = spla.LinearOperator((2 * n2, 2 * n2), matvec=mv, dtype=complex)
    if ncv is None:
        ncv = max(2 * nev + 6, 16)
    mu, V = spla.eigs(Op, k=nev, which="LM", ncv=ncv, tol=tol, maxiter=5000)
    return sigma + 1.0 / mu, V[:n2, :], lu


def resid(K, cd, rho, x):
    x = x / np.linalg.norm(x)
    return float(np.linalg.norm(K @ x + (rho * cd - rho * rho) * x))


def rayleigh2(K, cd, rho, x, nit=2):
    """LU bei sigma = rho (komplex, Arnoldi-Wert), Rechts- und Linksvektor per inverser Iteration,
    dann Nullstelle des zweiseitigen Rayleigh-Funktionals y^T Q(r) x = 0 (naechste an rho)."""
    Q = (K + sp.diags(rho * cd - rho * rho)).tocsc()
    lu = spla.splu(Q)
    xr = x / np.linalg.norm(x)
    y = np.conj(xr)
    for _ in range(nit):
        xn = lu.solve(xr)
        if not np.all(np.isfinite(xn)):
            break
        xr = xn / np.linalg.norm(xn)
    for _ in range(nit + 1):
        yn = lu.solve(y, trans="T")
        if not np.all(np.isfinite(yn)):
            break
        y = yn / np.linalg.norm(yn)
    a2 = -(y @ xr)
    a1 = y @ (cd * xr)
    a0 = y @ (K @ xr)
    wur = np.roots([a2, a1, a0])
    r_neu = wur[np.argmin(np.abs(wur - rho))]
    return r_neu, xr, resid(K, cd, r_neu, xr)


# ---------------------------------------------------------------- ein omega^2-Punkt
def punkt(g, om2, f0, rho_pred, nev=3, sig_off=0.0, mit_fluss=True, rc=(20.0, 22.5)):
    t = time.time()
    f, nF, itq = g.qball(om2, f0)
    rad = g.radien(f)
    R = rad["achse"]
    K, cd = g.lin(f, om2)
    sigma = float(np.real(rho_pred)) + sig_off
    rhos, X, lu = eig_sinv(K, cd, sigma, nev)
    del lu
    kand = []
    for k in range(len(rhos)):
        kand.append(dict(rho_re=float(rhos[k].real), rho_im=float(rhos[k].imag), l0=g.l0_anteil(X[:, k], R)))
    gute = [k for k in range(len(rhos)) if kand[k]["l0"] >= 0.5]
    pool = gute if gute else list(range(len(rhos)))
    kk = min(pool, key=lambda k: abs(rhos[k] - rho_pred))
    rho1 = rhos[kk]
    res1 = resid(K, cd, rho1, X[:, kk])
    rho2, x2, res = rayleigh2(K, cd, rho1, X[:, kk])
    d = dict(om2=float(om2), rho_re=float(rho2.real), rho_im=float(rho2.imag), Gamma=float(-rho2.imag),
             rho_arnoldi_re=float(rho1.real), rho_arnoldi_im=float(rho1.imag), residuum_arnoldi=res1,
             korrektur=float(abs(rho2 - rho1)), residuum=res, sigma=sigma, l0=kand[kk]["l0"],
             auswahl_ok=bool(gute), kandidaten=kand, qball_res=nF, qball_it=itq, f0=float(f[0]),
             R_achse=rad["achse"], R_diag=rad["diag"], N=g.N, sek=time.time() - t)
    if mit_fluss:
        d["fluss"] = [g.fluss(x2, q) for q in rc]
    return d, f, x2, rho2


# ---------------------------------------------------------------- Fit Gamma = Gmin + a (x - xr)^2
def parabel(xs, gs):
    xs = np.asarray(xs, float)
    gs = np.asarray(gs, float)
    if len(xs) < 3:
        return None
    xm = float(np.mean(xs))
    sc = float(np.max(np.abs(xs - xm)))
    t = (xs - xm) / sc
    A = np.vstack([np.ones_like(t), t, t * t]).T
    c, *_ = np.linalg.lstsq(A, gs, rcond=None)
    c0, c1, c2 = c
    if c2 <= 0:
        return None
    xr = xm - c1 * sc / (2.0 * c2)
    gmin = c0 - c1 * c1 / (4.0 * c2)
    res = gs - A @ c
    dof = len(xs) - 3
    out = dict(xr=float(xr), gmin=float(gmin), a=float(c2 / sc ** 2), n=len(xs),
               rms=float(np.sqrt(np.mean(res ** 2))), max_rel_rest=float(np.max(np.abs(res)) / max(np.max(np.abs(gs)), 1e-300)))
    if dof > 0:
        s2 = float(np.sum(res ** 2)) / dof
        cov = s2 * np.linalg.inv(A.T @ A)
        gr = np.array([1.0, -c1 / (2.0 * c2), c1 * c1 / (4.0 * c2 * c2)])
        out["sigma_gmin"] = float(np.sqrt(max(gr @ cov @ gr, 0.0)))
        gx = np.array([0.0, -sc / (2.0 * c2), c1 * sc / (2.0 * c2 * c2)])
        out["sigma_xr"] = float(np.sqrt(max(gx @ cov @ gx, 0.0)))
    return out


# ---------------------------------------------------------------- Hauptablauf
def sha_self():
    with open(os.path.abspath(__file__), "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--modus", choices=["scan", "punkt", "rauch"], default="scan")
    ap.add_argument("--stern", choices=["A", "B"], required=True)
    ap.add_argument("--h", type=float, required=True)
    ap.add_argument("--x0", type=float, required=True, help="Start omega^2 (Mitte Stufe 1 bzw. Punkt)")
    ap.add_argument("--rho0", type=float, default=1.5565)
    ap.add_argument("--lin", type=float, default=24.0)
    ap.add_argument("--lpml", type=float, default=16.0)
    ap.add_argument("--sig0", type=float, default=1.5)
    ap.add_argument("--pexp", type=float, default=2.0)
    ap.add_argument("--lpml2", type=float, default=22.0)
    ap.add_argument("--sig02", type=float, default=3.0)
    ap.add_argument("--pexp2", type=float, default=3.0)
    ap.add_argument("--n1", type=int, default=5)
    ap.add_argument("--d1", type=float, default=2e-4)
    ap.add_argument("--d2", type=float, default=4e-5)
    ap.add_argument("--d3max", type=float, default=2e-5)
    ap.add_argument("--d3min", type=float, default=1e-7)
    ap.add_argument("--budget", type=float, default=560.0)
    ap.add_argument("--sig-off", type=float, default=2e-3)
    ap.add_argument("--punkt-sigoff", type=float, default=0.0)
    ap.add_argument("--ohne-p2", action="store_true")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    erg = dict(karte="STILLE-AUF-GITTER", args=vars(args), sha256_skript=sha_self(),
               numpy=np.__version__, scipy=scipy.__version__, start_utc=time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()),
               punkte=[], stufen={}, fehlt=[])

    def speichern():
        erg["sek"] = time.time() - T0
        tmp = args.out + ".tmp"
        with open(tmp, "w") as fh:
            json.dump(erg, fh, indent=1)
        os.replace(tmp, args.out)

    g1 = Gitter(args.h, args.stern, args.lin, args.lpml, args.sig0, args.pexp)
    erg["gitter1"] = dict(M=g1.M, N=g1.N, Lout=g1.Lout, Lin=g1.Lin, Lpml=g1.Lpml, sig0=g1.sig0, pexp=g1.pexp)
    log("Gitter 1: stern", args.stern, "h", args.h, "M", g1.M, "N8", g1.N, "Lout", g1.Lout)
    r_rad, f_rad, info = radial_profil(args.x0)
    erg["radial"] = info
    log("radiales Profil", info)
    f_start = np.interp(g1.r, r_rad, f_rad, right=0.0)

    cache = {}

    def ev(x, nev=3, sig_off=0.0, merken=True, stufe=""):
        x = float(x)
        if cache:
            xn = min(cache, key=lambda q: abs(q - x))
            f0, rho_n = cache[xn]
            rho_pred = rho_n + RHO_STEIGUNG * (x - xn)
        else:
            f0, rho_pred = f_start, complex(args.rho0, 0.0)
            nev = max(nev, 6)
        d, f, xv, rho = punkt(g1, x, f0, rho_pred, nev=nev, sig_off=sig_off)
        d["stufe"] = stufe
        if merken:
            cache[x] = (f, rho)
        erg["punkte"].append(d)
        speichern()
        fl = d["fluss"][0]["anteil"]
        log("%s x=%.9f rho=%.10f %+.4e i  G=%.5e l0=%.3f korr=%.1e res=%.1e/%.1e qb=%.1e  F0=%.3f F4=%.3f F8=%.3f  R=%.3f/%.3f  %.1fs"
            % (stufe, x, d["rho_re"], d["rho_im"], d["Gamma"], d["l0"], d["korrektur"], d["residuum_arnoldi"],
               d["residuum"], d["qball_res"], fl[0], fl[1], fl[2], d["R_achse"], d["R_diag"], d["sek"]))
        return d, f, xv, rho

    def zeit_ok(n_punkte=1):
        pro = max([p["sek"] for p in erg["punkte"]] + [1.0])
        return (time.time() - T0) + n_punkte * pro * 1.3 < args.budget

    if args.modus == "punkt":
        d, f, xv, rho = ev(args.x0, nev=6, sig_off=args.punkt_sigoff, stufe="punkt")
        speichern()
        log("fertig")
        return

    # Stufe 1: n1 Punkte im Abstand d1 um x0; am Rand erweitern; Scheitel der 3 Punkte um das Stichprobenminimum
    G1 = {}
    for x in args.x0 + args.d1 * (np.arange(args.n1) - (args.n1 - 1) // 2):
        G1[float(x)] = ev(x, stufe="S1")[0]["Gamma"]
    for _ in range(6):
        xs = sorted(G1)
        i = int(np.argmin([G1[x] for x in xs]))
        if 0 < i < len(xs) - 1:
            break
        if not zeit_ok(1):
            break
        xneu = xs[0] - args.d1 if i == 0 else xs[-1] + args.d1
        G1[float(xneu)] = ev(xneu, stufe="S1+")[0]["Gamma"]
    xs = sorted(G1)
    gs = [G1[x] for x in xs]
    i = int(np.argmin(gs))
    erg["stufen"]["S1"] = dict(xs=xs, G=gs)
    if not (0 < i < len(xs) - 1):
        erg["fehlt"].append("Stufe 1: Minimum am Rand")
        speichern()
        return
    x3 = np.array(xs[i - 1:i + 2])
    g3 = np.array(gs[i - 1:i + 2])
    c2, c1, c0 = np.polyfit(x3 - x3[1], g3, 2)
    x1 = float(x3[1] - c1 / (2.0 * c2)) if c2 > 0 else float(x3[1])
    x1 = float(np.clip(x1, x3[0], x3[2]))
    erg["stufen"]["S1"]["x1"] = x1
    log("Stufe 1: Scheitel", x1)
    if args.modus == "rauch":
        speichern()
        log("Rauchlauf fertig")
        return
    # Stufe 2: 5 Punkte im Abstand d2 um x1, Parabel
    if not zeit_ok(5):
        erg["fehlt"].append("Stufe 2 Zeit")
        speichern()
        return
    xs2 = x1 + args.d2 * np.arange(-2, 3)
    gs2 = [ev(x, stufe="S2")[0]["Gamma"] for x in xs2]
    fit2 = parabel(xs2, gs2)
    erg["stufen"]["S2"] = dict(xs=[float(q) for q in xs2], G=gs2, fit=fit2)
    log("Stufe 2 fit", fit2)
    if fit2 is None:
        erg["fehlt"].append("Stufe 2 ohne Parabel")
        speichern()
        return
    # Stufe 3: enges Fenster aus Gamma_min und Kruemmung von Stufe 2; einmal neu zentrieren, wenn der Scheitel ausserhalb liegt
    d3 = float(np.clip(1.2 * math.sqrt(max(fit2["gmin"], 0.0) / fit2["a"]), args.d3min, args.d3max))
    xc = fit2["xr"]
    fit3 = None
    for runde in range(2):
        if not zeit_ok(5):
            erg["fehlt"].append("Stufe 3 Zeit")
            break
        xs3 = xc + d3 * np.arange(-2, 3)
        gs3 = [ev(x, stufe="S3.%d" % runde)[0]["Gamma"] for x in xs3]
        fit3 = parabel(xs3, gs3)
        erg["stufen"]["S3.%d" % runde] = dict(xs=[float(q) for q in xs3], G=gs3, fit=fit3, d3=d3)
        log("Stufe 3.%d fit" % runde, fit3)
        if fit3 is None or (xs3[0] <= fit3["xr"] <= xs3[-1]):
            break
        xc = fit3["xr"]
    if fit3 is None:
        erg["fehlt"].append("Stufe 3 ohne Parabel")
        speichern()
        return
    xs_ = fit3["xr"]
    if not zeit_ok(1):
        erg["fehlt"].append("Minimum Zeit")
        speichern()
        return
    dmin, fmin, xvmin, rhomin = ev(xs_, stufe="MIN")
    erg["minimum"] = dict(x=xs_, Gamma_fit=fit3["gmin"], sigma_fit=fit3.get("sigma_gmin"), sigma_x=fit3.get("sigma_xr"),
                          Gamma_direkt=dmin["Gamma"], rho_re=dmin["rho_re"], a=fit3["a"], fluss=dmin["fluss"],
                          R_achse=dmin["R_achse"], R_diag=dmin["R_diag"])
    speichern()
    # Doppelrechnung: anderer Shift (anderer Krylov-Weg)
    if zeit_ok(1):
        dd, *_ = ev(xs_, sig_off=args.sig_off, merken=False, stufe="DOPPEL")
        erg["minimum"]["Gamma_doppel"] = dd["Gamma"]
        erg["minimum"]["rho_re_doppel"] = dd["rho_re"]
    else:
        erg["fehlt"].append("Doppelrechnung Zeit")
    speichern()
    # PML-Probe: zweite Einstellung (dicker und staerker, Rand weiter aussen)
    if args.ohne_p2:
        erg["fehlt"].append("P2 getrennt")
    else:
        pro = max(p["sek"] for p in erg["punkte"])
        g2 = Gitter(args.h, args.stern, args.lin, args.lpml2, args.sig02, args.pexp2)
        fak = (g2.N / g1.N) ** 1.4
        if (time.time() - T0) + 1.5 * pro * fak + 20 < args.budget:
            f0 = np.concatenate([fmin, np.zeros(g2.N - g1.N)])
            d2_, f2_, x2_, r2_ = punkt(g2, float(xs_), f0, rhomin, nev=3)
            d2_["stufe"] = "P2"
            erg["punkte"].append(d2_)
            erg["gitter2"] = dict(M=g2.M, N=g2.N, Lout=g2.Lout, Lin=g2.Lin, Lpml=g2.Lpml, sig0=g2.sig0, pexp=g2.pexp)
            erg["minimum"]["Gamma_P2"] = d2_["Gamma"]
            erg["minimum"]["rho_re_P2"] = d2_["rho_re"]
            log("P2 G=%.5e rho=%.10f res=%.1e (%.1fs)" % (d2_["Gamma"], d2_["rho_re"], d2_["residuum"], d2_["sek"]))
        else:
            erg["fehlt"].append("P2 Zeit")
    m = erg["minimum"]
    if "Gamma_doppel" in m and "Gamma_P2" in m:
        boden = abs(m["Gamma_direkt"] - m["Gamma_doppel"]) + abs(m["Gamma_direkt"] - m["Gamma_P2"])
        m["boden"] = boden
        m["ueber_boden"] = bool(m["Gamma_fit"] > 0 and m["Gamma_fit"] >= 10.0 * boden)
    speichern()
    log("fertig", json.dumps({k: v for k, v in m.items() if k != "fluss"}))


if __name__ == "__main__":
    main()
