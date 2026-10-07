#!/usr/bin/env python3
"""QBALL-HADRON-1, Teil 2: drehende Q-Baelle bei festem Q, E(m) direkt (ohne omega-Interpolation).

Modell wie RG-1/HAGEDORN/DIM-LEITER: L = |phi_t|^2 - |grad phi|^2 - U(S), U(S) = S - S^2 + S^3/2, S = |phi|^2.
Ansatz phi = f(x) exp(i omega t + i m.theta). Mit Q = 2 omega N, N = Int f^2, gilt omega^2 N = Q^2/(4N) und
    E = Int [|grad f|^2 + Zentrifugalterm + U(f^2)] + Q^2/(4 N)  =: E_Q[f].
Stationaere Punkte von E_Q sind die Q-Baelle zu omega = Q/(2N) (Lagrange-Form). Der Ball auf dem unteren Ast ist ein
Minimum von E_Q innerhalb des Ansatzes. Wir minimieren E_Q mit L-BFGS (scipy), Variablen g = f sqrt(W) (Diagonal-
skalierung), zuerst auf dem Gitter 2h, dann auf h (Start aus 2h interpoliert); Richardson E_R = (4 E_h - E_2h)/3.

Modi:
  radial : 1D, Dimension D (2, 3, 4), Windung m nur fuer D = 2 (Zentrifugalterm m^2 f^2/r^2).
  axi3   : 3D achsensymmetrisch, f(rho, z), gerade Paritaet in z (Halbraum z >= 0), Windung m.
  dop4   : 4D doppelt drehend, f(rho1, rho2), Windungen (m1, m2) in zwei senkrechten Ebenen.
Diskretisierung: zellzentriert x_i = (i + 1/2) h, Dirichlet f = 0 am Aussenrand (L = n h), Achsen und z = 0 ohne
Fluss (Gewicht rho = 0 bzw. Spiegelung). Das diskrete Funktional wird exakt minimiert; der Gradient ist analytisch.

Gegenproben je Loesung: Virial E = omega Q + (2/D) K (K = Gradient + Zentrifugal), Rest der diskreten Feldgleichung,
Randwert von f, E < Q (gebunden), Lage und Form (Halbwertsradien der Ladungsdichte, Energiedichte auf der Achse).

Aufruf: python3 festq.py --modus radial --D 2 --m 0,1,2,3,4 --Q 1000 --h 0.05 --L 60 --out datei.json
        python3 festq.py --modus axi3 --m 0,1,2,3 --Q 3000 --h 0.2 --Lx 40 --Ly 25 --out datei.json
        python3 festq.py --modus dop4 --mm 0:0,1:0,1:1,2:0 --Q 10000 --h 0.25 --Lx 25 --Ly 25 --out datei.json
"""
import os

for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import argparse
import datetime
import json
import math
import platform
import sys
import time

import numpy as np
from scipy.optimize import minimize

FL_D = {2: 2.0 * math.pi, 3: 4.0 * math.pi, 4: 2.0 * math.pi ** 2}   # Oberflaeche der Einheitssphaere S^(D-1)
OMEGA_C = 1.0 / math.sqrt(2.0)


def U(S):
    return S - S * S + 0.5 * S ** 3


def dU(S):
    return 1.0 - 2.0 * S + 1.5 * S * S


def jetzt():
    return datetime.datetime.now(datetime.timezone.utc).astimezone().isoformat(timespec="seconds")


# ------------------------------------------------------------------ Gitter

class Radial:
    """1D radial, Dimension D, Windung m (nur D = 2)."""

    def __init__(self, D, m, h, L):
        self.D, self.m, self.h = D, m, h
        n = int(round(L / h))
        self.n = n
        self.x = (np.arange(n) + 0.5) * h
        c = FL_D[D]
        self.W = c * self.x ** (D - 1) * h                       # Volumengewicht je Zelle
        xl = (np.arange(n) + 1.0) * h                            # Kante i -> i+1 (letzte zum Rand f = 0)
        self.A = c * xl ** (D - 1) / h                           # Gewicht von (f_{i+1} - f_i)^2
        self.C = self.W * (m * m / self.x ** 2 if (D == 2 and m) else 0.0)
        self.Ddim = D
        self.shape = (n,)

    def grad_terme(self, f):
        d = np.empty_like(f)
        d[:-1] = f[1:] - f[:-1]
        d[-1] = -f[-1]
        K = float(np.sum(self.A * d * d) + np.sum(self.C * f * f))
        g = -2.0 * self.A * d
        g[1:] += 2.0 * self.A[:-1] * d[:-1]
        g += 2.0 * self.C * f
        return K, g

    def koordinaten(self):
        return dict(x=self.x)


class Gitter2:
    """2D-Gitter: axi3 (x = rho radial, y = z eben, gerade Paritaet) oder dop4 (x = rho1, y = rho2, beide radial)."""

    def __init__(self, modus, mx, my, h, Lx, Ly):
        self.modus, self.mx, self.my, self.h = modus, mx, my, h
        nx, ny = int(round(Lx / h)), int(round(Ly / h))
        self.shape = (nx, ny)
        x = (np.arange(nx) + 0.5) * h
        y = (np.arange(ny) + 0.5) * h
        xl = (np.arange(nx) + 1.0) * h
        yl = (np.arange(ny) + 1.0) * h
        self.x, self.y = x, y
        if modus == "axi3":
            c = 2.0 * 2.0 * math.pi                               # zwei z-Haelften, 2 pi aus theta
            wx, wy, wxl, wyl = x, np.ones(ny), xl, np.ones(ny)
            self.Ddim = 3
            cent = (mx * mx / x ** 2)[:, None] * np.ones(ny)[None, :]
        elif modus == "dop4":
            c = (2.0 * math.pi) ** 2
            wx, wy, wxl, wyl = x, y, xl, yl
            self.Ddim = 4
            cent = (mx * mx / x ** 2)[:, None] + (my * my / y ** 2)[None, :]
        else:
            raise ValueError(modus)
        self.W = c * h * h * wx[:, None] * wy[None, :]
        self.Ax = c * wxl[:, None] * wy[None, :]                  # x-Kanten (i -> i+1), letzte zum Rand
        self.Ay = c * wx[:, None] * wyl[None, :]                  # y-Kanten (j -> j+1), letzte zum Rand
        self.C = self.W * cent

    def grad_terme(self, f):
        dx = np.empty_like(f)
        dx[:-1, :] = f[1:, :] - f[:-1, :]
        dx[-1, :] = -f[-1, :]
        dy = np.empty_like(f)
        dy[:, :-1] = f[:, 1:] - f[:, :-1]
        dy[:, -1] = -f[:, -1]
        K = float(np.sum(self.Ax * dx * dx) + np.sum(self.Ay * dy * dy) + np.sum(self.C * f * f))
        g = -2.0 * self.Ax * dx - 2.0 * self.Ay * dy
        g[1:, :] += 2.0 * self.Ax[:-1, :] * dx[:-1, :]
        g[:, 1:] += 2.0 * self.Ay[:, :-1] * dy[:, :-1]
        g += 2.0 * self.C * f
        return K, g

    def koordinaten(self):
        return dict(x=self.x, y=self.y)


# ------------------------------------------------------------------ Funktional

def funktional(gt, f, Q):
    K, gK = gt.grad_terme(f)
    S = f * f
    N = float(np.sum(gt.W * S))
    V = float(np.sum(gt.W * U(S)))
    E = K + V + Q * Q / (4.0 * N)
    g = gK + 2.0 * gt.W * dU(S) * f - (Q * Q / (2.0 * N * N)) * gt.W * f
    return E, g, dict(K=K, V=V, N=N)


def loesen(gt, f0, Q, maxiter, gtol_rel):
    sw = np.sqrt(gt.W)
    z0 = (f0 * sw).ravel()
    zahl = [0]

    def fun(z):
        f = z.reshape(gt.shape) / sw
        E, g, _ = funktional(gt, f, Q)
        zahl[0] += 1
        return E, (g / sw).ravel()

    t0 = time.perf_counter()
    r = minimize(fun, z0, jac=True, method="L-BFGS-B",
                 options=dict(maxiter=maxiter, maxfun=4 * maxiter, maxcor=40, ftol=1e-16, gtol=gtol_rel * Q))
    f = r.x.reshape(gt.shape) / sw
    return f, dict(nit=int(r.nit), nfev=int(zahl[0]), status=int(r.status), msg=str(r.message),
                   dauer_s=time.perf_counter() - t0)


def diagnose(gt, f, Q):
    E, g, t = funktional(gt, f, Q)
    N, K, V = t["N"], t["K"], t["V"]
    omega = Q / (2.0 * N)
    D = gt.Ddim
    virial = (E - omega * Q - 2.0 * K / D) / E
    res = g / (2.0 * gt.W)                                         # diskrete Feldgleichung (= 0 im Minimum)
    fmax = float(np.max(np.abs(f)))
    rand = 0.0
    if f.ndim == 1:
        rand = float(abs(f[-1]) / fmax)
    else:
        rand = float(max(np.max(np.abs(f[-1, :])), np.max(np.abs(f[:, -1]))) / fmax)
    return dict(E=E, N=N, K=K, V=V, omega=omega, E_durch_Q=E / Q, gebunden=bool(E < Q), virial_rest=virial,
                feld_rest_max=float(np.max(np.abs(res)) / max(fmax, 1e-300)),
                feld_rest_rms=float(math.sqrt(np.sum(gt.W * res * res) / np.sum(gt.W)) / max(fmax, 1e-300)),
                f_max=fmax, rand_rel=rand)


def halbwert_1d(x, s):
    """Innen- und Aussenradius, bei denen s die halbe Hoehe kreuzt (lineare Interpolation)."""
    i = int(np.argmax(s))
    smax = float(s[i])
    hw = 0.5 * smax
    r_in = 0.0
    for k in range(i, 0, -1):
        if s[k - 1] < hw <= s[k]:
            r_in = float(x[k - 1] + (hw - s[k - 1]) * (x[k] - x[k - 1]) / (s[k] - s[k - 1]))
            break
    r_aus = float(x[-1])
    for k in range(i, len(s) - 1):
        if s[k] >= hw > s[k + 1]:
            r_aus = float(x[k] + (s[k] - hw) * (x[k + 1] - x[k]) / (s[k] - s[k + 1]))
            break
    return float(x[i]), r_in, r_aus, smax


def form(gt, f, Q, omega):
    S = f * f
    out = {}
    if f.ndim == 1:
        xm, ri, ra, smax = halbwert_1d(gt.x, S)
        out.update(R_max=xm, R_innen=ri, R_aussen=ra, S_max=smax,
                   A=((ri + ra) / 2.0) / (ra - ri) if ri > 0 else None)
        return out
    i, j = np.unravel_index(int(np.argmax(S)), S.shape)
    out.update(S_max=float(S[i, j]), x_max=float(gt.x[i]), y_max=float(gt.y[j]))
    # Schnitt durch das Maximum laengs x (bei y = y_max) und laengs y (bei x = x_max)
    _, xi, xa, _ = halbwert_1d(gt.x, S[:, j])
    _, yi, ya, _ = halbwert_1d(gt.y, S[i, :])
    out.update(x_halb_innen=xi, x_halb_aussen=xa, y_halb_innen=yi, y_halb_aussen=ya)
    if xi > 0:
        out["A_x"] = ((xi + xa) / 2.0) / (xa - xi)
    # Energiedichte (zentrierte Differenzen, Rand 0 bzw. gespiegelt)
    h = gt.h
    fp = np.pad(f, ((1, 1), (1, 1)), mode="constant")
    # Geisterzellen an x = 0 bzw. y = 0: Feld im kartesischen Schnitt hat dort das Vorzeichen (-1)^m (Achse) bzw. +1
    # (Spiegelung z -> -z bei gerader Paritaet). Nur fuer die beschreibende Energiedichte.
    sx = -1.0 if (gt.mx % 2) else 1.0
    sy = (-1.0 if (gt.my % 2) else 1.0) if gt.modus == "dop4" else 1.0
    fp[0, 1:-1] = sx * f[0, :]
    fp[1:-1, 0] = sy * f[:, 0]
    fx = (fp[2:, 1:-1] - fp[:-2, 1:-1]) / (2 * h)
    fy = (fp[1:-1, 2:] - fp[1:-1, :-2]) / (2 * h)
    T = omega * omega * S + fx * fx + fy * fy + gt.C / gt.W * S + U(S)
    a, b = np.unravel_index(int(np.argmax(T)), T.shape)
    out.update(T_max=float(T[a, b]), T_x_max=float(gt.x[a]), T_y_max=float(gt.y[b]),
               T_mitte_durch_max=float(T[0, 0] / T[a, b]), S_mitte_durch_max=float(S[0, 0] / S[i, j]))
    return out


# ------------------------------------------------------------------ Startprofile

def r_kugel(D, Q):
    # duenne Wand: Q = 2 omega_c f0^2 Vol(R), f0^2 = 1
    if D == 2:
        return math.sqrt(Q / (2.0 * OMEGA_C * math.pi))
    if D == 3:
        return (3.0 * Q / (8.0 * math.pi * OMEGA_C)) ** (1.0 / 3.0)
    return (Q / (math.pi ** 2 * OMEGA_C)) ** 0.25


def stufe(d, R, w=1.0):
    return 0.95 / (1.0 + np.exp(np.clip((d - R) / w, -60, 60)))


def start_radial(gt, Q):
    R = r_kugel(gt.D, Q)
    x = gt.x
    m = gt.m
    if m == 0:
        return stufe(x, R)
    Rr = math.sqrt(R * R + (1.5 * m) ** 2)
    rh = min(0.8 * Rr, 1.2 * m)
    prof = stufe(x, Rr) * (1.0 - stufe(x, rh, 0.7) / 0.95)
    return prof * (1.0 - np.exp(-(x / 1.5) ** (2 * m)))


def start_2(gt, Q):
    D = gt.Ddim
    R = r_kugel(D, Q)
    X, Y = np.meshgrid(gt.x, gt.y, indexing="ij")
    mx, my = gt.mx, gt.my
    if gt.modus == "axi3":
        if mx == 0:
            return stufe(np.sqrt(X * X + Y * Y), R)
        Rr = 0.6 * R + 1.2 * mx
        a = 0.8 * R
        f = stufe(np.sqrt((X - Rr) ** 2 + Y * Y), a)
        return f * (1.0 - np.exp(-(X / 1.5) ** (2 * mx)))
    # dop4
    R1 = 0.6 * R + 1.2 * mx if mx else 0.0
    R2 = 0.6 * R + 1.2 * my if my else 0.0
    a = 0.8 * R if (mx or my) else R
    f = stufe(np.sqrt((X - R1) ** 2 + (Y - R2) ** 2), a)
    if mx:
        f = f * (1.0 - np.exp(-(X / 1.5) ** (2 * mx)))
    if my:
        f = f * (1.0 - np.exp(-(Y / 1.5) ** (2 * my)))
    return f


def verfeinern(f_grob, gt_grob, gt_fein):
    """Separable lineare Interpolation vom Gitter 2h auf h (zellzentriert)."""
    if f_grob.ndim == 1:
        return np.interp(gt_fein.x, gt_grob.x, f_grob, right=0.0)
    tmp = np.empty((gt_fein.shape[0], gt_grob.shape[1]))
    for j in range(gt_grob.shape[1]):
        tmp[:, j] = np.interp(gt_fein.x, gt_grob.x, f_grob[:, j], right=0.0)
    out = np.empty(gt_fein.shape)
    for i in range(gt_fein.shape[0]):
        out[i, :] = np.interp(gt_fein.y, gt_grob.y, tmp[i, :], right=0.0)
    return out


# ------------------------------------------------------------------ Hauptteil

def ein_fall(modus, D, mx, my, Q, h, Lx, Ly, maxiter, gtol_rel):
    def baue(hh):
        if modus == "radial":
            return Radial(D, mx, hh, Lx)
        return Gitter2(modus, mx, my, hh, Lx, Ly)

    erg = dict(modus=modus, D=(D if modus == "radial" else (3 if modus == "axi3" else 4)), m1=mx, m2=my, Q=Q,
               Lx=Lx, Ly=Ly)
    gg = baue(2.0 * h)
    f0 = start_radial(gg, Q) if modus == "radial" else start_2(gg, Q)
    fg, lg = loesen(gg, f0, Q, maxiter, gtol_rel)
    dg = diagnose(gg, fg, Q)
    dg.update(form(gg, fg, Q, dg["omega"]), h=2.0 * h, loeser=lg, n=list(gg.shape))
    gf = baue(h)
    ff, lf = loesen(gf, verfeinern(fg, gg, gf), Q, maxiter, gtol_rel)
    df = diagnose(gf, ff, Q)
    df.update(form(gf, ff, Q, df["omega"]), h=h, loeser=lf, n=list(gf.shape))
    erg["grob"] = dg
    erg["fein"] = df
    erg["E_richardson"] = (4.0 * df["E"] - dg["E"]) / 3.0
    erg["omega_richardson"] = (4.0 * df["omega"] - dg["omega"]) / 3.0
    erg["dE_fein_grob_rel"] = (df["E"] - dg["E"]) / df["E"]
    erg["J1"] = mx * Q
    erg["J2"] = my * Q
    return erg


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--modus", required=True, choices=["radial", "axi3", "dop4"])
    ap.add_argument("--D", type=int, default=2)
    ap.add_argument("--m", default="0")
    ap.add_argument("--mm", default="0:0")
    ap.add_argument("--Q", required=True, help="Kommaliste")
    ap.add_argument("--h", type=float, required=True)
    ap.add_argument("--L", type=float, default=None, help="radial: Kastenlaenge; sonst --Lx/--Ly")
    ap.add_argument("--Lx", type=float, default=None)
    ap.add_argument("--Ly", type=float, default=None)
    ap.add_argument("--L_pro_R", type=float, default=None, help="Kasten = L_pro_R * r_kugel(Q) + L_plus (je Q)")
    ap.add_argument("--L_plus", type=float, default=0.0)
    ap.add_argument("--maxiter", type=int, default=60000)
    ap.add_argument("--gtol_rel", type=float, default=1e-13)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    start = jetzt()
    t0 = time.perf_counter()
    if a.modus == "dop4":
        faelle = [tuple(int(v) for v in s.split(":")) for s in a.mm.split(",")]
    else:
        faelle = [(int(s), 0) for s in a.m.split(",")]
    qs = [float(s) for s in a.Q.split(",")]
    D = a.D if a.modus == "radial" else (3 if a.modus == "axi3" else 4)
    ergebnisse = []
    for Q in qs:
        for (mx, my) in faelle:
            if a.L_pro_R is not None:
                Lx = Ly = a.L_pro_R * r_kugel(D, Q) + a.L_plus
            else:
                Lx = a.L if a.modus == "radial" else a.Lx
                Ly = a.L if a.modus == "radial" else a.Ly
            e = ein_fall(a.modus, a.D, mx, my, Q, a.h, Lx, Ly, a.maxiter, a.gtol_rel)
            ergebnisse.append(e)
            df, dg = e["fein"], e["grob"]
            print(f"{jetzt()} Q = {Q:g} m = ({mx},{my}) h = {a.h:g}: E = {df['E']:.10g} (2h {dg['E']:.10g}, "
                  f"Richardson {e['E_richardson']:.10g}), omega = {df['omega']:.8f}, E/Q = {df['E_durch_Q']:.6f}, "
                  f"virial {df['virial_rest']:.1e}, feld {df['feld_rest_max']:.1e}, rand {df['rand_rel']:.1e}, "
                  f"it {df['loeser']['nit']}/{dg['loeser']['nit']}, {df['loeser']['dauer_s'] + dg['loeser']['dauer_s']:.1f} s",
                  flush=True)
    aus = dict(befehl=" ".join(sys.argv), start=start, ende=jetzt(), dauer_s=time.perf_counter() - t0,
               rechner=platform.node(), python=platform.python_version(), numpy=np.__version__,
               ergebnisse=ergebnisse)
    tmp = a.out + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(aus, fh, indent=1)
    os.replace(tmp, a.out)


if __name__ == "__main__":
    main()
