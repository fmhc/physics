#!/usr/bin/env python3
"""AFM-KANAL-1 (Runde 12 nach v3, explorativ): nackter geschlossener Kanal um den praezedierenden AFM-Ball.

Neu geschrieben; nls2.py (RUNDE-10/nls-leiter) wird unveraendert als Kopie importiert, nur fuer die Profile der
Kontrollen K2 (KG-Q-Ball, beta = 0,5) und K4 (kubisch-quintisches NLS, 3D).

Modell (MESS-3A R1): L = (1/2)(d_t n)^2 - (1/2)|grad n|^2 - U, U = (1/2)(s + kappa s^2), s = sin^2 Theta; 3D radial, l = 0.
Profil: Theta'' + (2/r) Theta' = G = sin cos [1 - Omega^2 + 2 kappa sin^2]. Schiessen (RK4, Schritt 0,02) als Startwert,
dann Numerov-Newton fuer y = r Theta auf dem Rechengitter r_j = j hp, hp = h/2, Dirichlet bei 0 und R_max
(wie R10 "kanal": Eigenwertgitter = Profilgitter, Schritt h/2).
Nackter geschlossener Kanal (HERLEITUNG.md): H(rho) = -d^2/dr^2 + A + B rho - c2 rho^2 fuer y = r w, Dirichlet bei 0, R_max.
  AFM: A = (V_u + V_v)/2, B = 2 Omega cos Theta, c2 = 1.  KG (K2): A = dp - omega^2, B = 2 omega, c2 = 1.
  NLS (K4, Spektralparameter nu): A = 2 D, B = 1, c2 = 0 (E = -nu/2 wie R10).
Suche (kanal_suche, fuer alle Modelle gleich): Sturm-Zaehlung der negativen Eigenwerte von H(rho) auf einem rho-Raster und
zwei Verfeinerungen; jede Aenderung der Zahl ist eine Nullstelle lambda_k(rho_c) = 0, k = min(Zahl links, Zahl rechts).
Eigenvektor per eigh_tridiagonal; Wandanteil F_w = Gewicht in |r - R_w| < 2 delta.
Kommandos: familie | kontrollen | auswertung
"""
import argparse
import datetime
import glob
import json
import math
import os
import sys
import time

import numpy as np
from scipy.linalg import eigh_tridiagonal, solve_banded

HIER = os.path.dirname(os.path.abspath(__file__))
if HIER not in sys.path:
    sys.path.insert(0, HIER)

T0 = time.perf_counter()
PI = math.pi
KAPPAS = [-0.017, -0.05, -0.10, -0.19, -0.20]
FS = [0.1, 0.2, 0.35, 0.5, 0.7, 0.85, 0.95]


def jetzt():
    return datetime.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")


def uhr():
    return time.perf_counter() - T0


def jsonfest(x):
    if isinstance(x, dict):
        return {str(k): jsonfest(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [jsonfest(v) for v in x]
    if isinstance(x, np.ndarray):
        return jsonfest(x.tolist())
    if isinstance(x, (np.floating,)):
        x = float(x)
    if isinstance(x, (np.integer,)):
        return int(x)
    if isinstance(x, (np.bool_,)):
        return bool(x)
    if isinstance(x, float) and not math.isfinite(x):
        return str(x)
    return x


# ----------------------------------------------------------------------------------------------------------------------
# AFM-Modell
# ----------------------------------------------------------------------------------------------------------------------

def G_afm(t, a, kap):
    """Profil-Rechte-Seite, a = 1 - Omega^2."""
    s = np.sin(t)
    return s * np.cos(t) * (a + 2.0 * kap * s * s)


def Gs_afm(t, a, kap):
    """dG/dTheta = V_u."""
    s = np.sin(t)
    return np.cos(2.0 * t) * (a + 2.0 * kap * s * s) + kap * np.sin(2.0 * t) ** 2


def V_uv(t, dt, a, kap):
    s = np.sin(t)
    q = a + 2.0 * kap * s * s
    Vu = np.cos(2.0 * t) * q + kap * np.sin(2.0 * t) ** 2
    Vv = np.cos(t) ** 2 * q - dt * dt
    return Vu, Vv


def _rk4(r, t, p, hs, a, kap):
    def f(rr, x, y):
        return y, G_afm(x, a, kap) - 2.0 * y / rr
    k1a, k1b = f(r, t, p)
    k2a, k2b = f(r + 0.5 * hs, t + 0.5 * hs * k1a, p + 0.5 * hs * k1b)
    k3a, k3b = f(r + 0.5 * hs, t + 0.5 * hs * k2a, p + 0.5 * hs * k2b)
    k4a, k4b = f(r + hs, t + hs * k3a, p + hs * k3b)
    return (t + hs / 6.0 * (k1a + 2 * k2a + 2 * k3a + k4a), p + hs / 6.0 * (k1b + 2 * k2b + 2 * k3b + k4b))


def _start(c, a, kap, hs):
    A2 = G_afm(c, a, kap) / 6.0
    B4 = Gs_afm(c, a, kap) * A2 / 20.0
    return c + A2 * hs * hs + B4 * hs ** 4, 2.0 * A2 * hs + 4.0 * B4 * hs ** 3


def _klassen(c, a, kap, kinf, hs, r_max, f_lin):
    """+1 Ueberschuss (Theta < 0), -1 Unterschuss (Theta' > 0 bei Theta > 0); im linearen Schwanz nach dem
    Vorzeichen des wachsenden Anteils B = Theta' + Theta (kappa_inf + 1/r); 0 = unentschieden bis r_max."""
    t, p = _start(c, a, kap, hs)
    r = hs
    kl = np.zeros(c.shape, dtype=np.int8)
    offen = np.ones(c.shape, dtype=bool)
    n = int(r_max / hs)
    for _ in range(1, n):
        t, p = _rk4(r, t, p, hs, a, kap)
        r += hs
        ueber = offen & (t < 0)
        unter = offen & (p > 0) & (t > 0)
        lin = offen & ~ueber & ~unter & (t < f_lin * c)
        B = p + t * (kinf + 1.0 / r)
        kl[ueber] = 1
        kl[unter] = -1
        kl[lin & (B > 0)] = -1
        kl[lin & (B <= 0)] = 1
        offen &= ~(ueber | unter | lin)
        if not offen.any():
            break
    return kl


def schiessen(kaps, Om2s, hs=0.02, K=48, runden=14, r_max=3000.0, f_lin=1e-4, eps_lo=1e-14):
    """Klammer [lo, hi] fuer Theta(0). Runde 0 logarithmisch im Abstand zu pi/2 (Duennwand), dann linear."""
    M = len(kaps)
    kap = np.array(kaps, float)[:, None]
    a = (1.0 - np.array(Om2s, float))[:, None]
    kinf = np.sqrt(a)
    lo = np.empty(M)
    hi = np.empty(M)
    status = []
    for i in range(M):
        z = (1.0 - Om2s[i]) / (-kaps[i]) if kaps[i] < 0 else 2.0
        lo[i] = math.asin(math.sqrt(z)) if 0.0 < z < 1.0 else 1e-3
        status.append("offen" if 0.0 < z < 1.0 else "Fenster leer")
    e = np.geomspace(1.0, eps_lo, K)
    c = PI / 2 - (PI / 2 - lo)[:, None] * e[None, :]
    kl = _klassen(c, a, kap, kinf, hs, r_max, f_lin)
    klassen0 = []
    for i in range(M):
        k = kl[i]
        klassen0.append({"unter": int((k == -1).sum()), "ueber": int((k == 1).sum()), "offen": int((k == 0).sum())})
        io = np.where(k == 1)[0]
        iu = np.where(k == -1)[0]
        if len(io) == 0:
            status[i] = "keine Loesung (kein Ueberschuss in Runde 0)"
            continue
        j = io[0]
        ju = iu[iu < j]
        if len(ju) == 0:
            status[i] = "keine Klammer (kein Unterschuss unter dem ersten Ueberschuss)"
            continue
        lo[i], hi[i] = c[i, ju[-1]], c[i, j]
        status[i] = "Klammer"
    for rd in range(1, runden):
        idx = [i for i in range(M) if status[i] == "Klammer" and hi[i] - lo[i] > 4e-16 * hi[i]]
        if not idx:
            break
        t = np.arange(1, K + 1) / (K + 1.0)
        cc = lo[idx][:, None] + (hi[idx] - lo[idx])[:, None] * t[None, :]
        kl = _klassen(cc, a[idx], kap[idx], kinf[idx], hs, r_max, f_lin)
        for m, i in enumerate(idx):
            k = kl[m]
            io = np.where(k == 1)[0]
            iu = np.where(k == -1)[0]
            if len(io) == 0:
                lo[i] = cc[m, -1]
                continue
            j = io[0]
            ju = iu[iu < j]
            nlo = cc[m, ju[-1]] if len(ju) else lo[i]
            lo[i], hi[i] = nlo, cc[m, j]
    return lo, hi, status, klassen0


def startprofil(lo, hi, a, kap, hs, r_max=3000.0, f_lin=1e-4):
    """Klammerpaar gemeinsam integrieren bis zur Trennung; danach Schwanz A e^{-k r}/r. Gibt (r, Theta, jm, grund)."""
    kinf = math.sqrt(a)
    c = np.array([lo, hi])
    t, p = _start(c, a, kap, hs)
    r = hs
    PH = [c.copy(), t.copy()]
    n = int(r_max / hs)
    for _ in range(1, n):
        t, p = _rk4(r, t, p, hs, a, kap)
        r += hs
        PH.append(t.copy())
        mitte = 0.5 * (t[0] + t[1])
        if mitte < 1e-2 * f_lin * lo or abs(t[1] - t[0]) > 1e-3 * abs(mitte):
            break
    PH = np.array(PH)
    ph = 0.5 * (PH[:, 0] + PH[:, 1])
    dif = np.abs(PH[:, 1] - PH[:, 0])
    f0 = ph[0]
    jm, grund = len(ph) - 1, "Ende"
    for j in range(1, len(ph)):
        if dif[j] > 1e-6 * abs(ph[j]):
            jm, grund = j - 1, "Divergenz"
            break
        if ph[j] < f_lin * f0:
            jm, grund = j, "Schwanz"
            break
    rr = np.arange(len(ph)) * hs
    return rr[:jm + 1], ph[:jm + 1], grund, float(ph[jm] / f0)


def numerov_newton(r, y, a, kap, iters=40, tol=1e-12):
    """Numerov fuer y = r Theta: y'' = r G(y/r), y_0 = y_J = 0. Gibt (y, Iterationen, letzte Schrittnorm, konvergiert).
    Konvergiert: Schritt < tol oder Rundungsboden (Schritt < 1e-7 und nicht mehr um Faktor 3 kleiner als zuvor)."""
    hp = r[1] - r[0]
    c = hp * hp / 12.0
    x = y[1:-1].copy()
    rr = r[1:-1]
    n = len(x)
    schritt = float("inf")
    vorher = float("inf")
    for it in range(1, iters + 1):
        th = x / rr
        g = rr * G_afm(th, a, kap)
        gs = Gs_afm(th, a, kap)
        F = np.empty(n)
        xl = np.concatenate([[0.0], x[:-1]])
        xr = np.concatenate([x[1:], [0.0]])
        gl = np.concatenate([[0.0], g[:-1]])
        gr = np.concatenate([g[1:], [0.0]])
        F[:] = xr - 2.0 * x + xl - c * (gr + 10.0 * g + gl)
        ab = np.empty((3, n))
        ab[0, :] = 1.0 - c * gs
        ab[2, :] = 1.0 - c * gs
        ab[1, :] = -2.0 - 10.0 * c * gs
        d = solve_banded((1, 1), ab, -F)
        x = x + d
        schritt = float(np.max(np.abs(d)) / max(np.max(np.abs(x)), 1e-300))
        if schritt < tol or (schritt < 1e-7 and schritt > vorher / 3.0):
            yy = np.concatenate([[0.0], x, [0.0]])
            return yy, it, schritt, True
        vorher = schritt
    yy = np.concatenate([[0.0], x, [0.0]])
    return yy, iters, schritt, False


def d1_fd4(f, hp, gerade):
    """Erste Ableitung, 4. Ordnung; am Ursprung gerade (gerade=True) oder ungerade Fortsetzung, am Ende 2. Ordnung."""
    s = 1.0 if gerade else -1.0
    ext = np.concatenate([s * f[2:0:-1], f, [f[-1], f[-1]]])
    d = (ext[0:-4] - 8.0 * ext[1:-3] + 8.0 * ext[3:-1] - ext[4:]) / (12.0 * hp)
    d[-2:] = (f[-1] - f[-3]) / (2.0 * hp)
    return d


def d2_fd4(f, hp, gerade):
    s = 1.0 if gerade else -1.0
    ext = np.concatenate([s * f[2:0:-1], f, [f[-1], f[-1]]])
    d = (-ext[0:-4] + 16.0 * ext[1:-3] - 30.0 * ext[2:-2] + 16.0 * ext[3:-1] - ext[4:]) / (12.0 * hp * hp)
    d[-2:] = 0.0
    return d


def schnitt(r, f, wert):
    """Erster Radius mit f <= wert (lineare Interpolation)."""
    j = int(np.argmax(f <= wert))
    if j == 0 or f[j] > wert:
        return float("nan")
    return float(r[j - 1] + (f[j - 1] - wert) / (f[j - 1] - f[j]) * (r[j] - r[j - 1]))


def wandgeometrie(r, amp, dichte):
    """R_w: amp = amp(0)/2; delta: 10-90 %-Abstand der Dichte (sin^2 Theta bzw. f^2)."""
    Rw = schnitt(r, amp, 0.5 * amp[0])
    r90 = schnitt(r, dichte, 0.9 * dichte[0])
    r10 = schnitt(r, dichte, 0.1 * dichte[0])
    return Rw, r10 - r90, r90, r10


def afm_profile(kaps, fs, h, protokoll):
    """Profile fuer Familienmitglieder (kappa, f); Rechengitter hp = h/2 bis R_max (MESS-3A R6)."""
    hp = 0.5 * h
    Om2s = [1.0 + k + f * abs(k) for k, f in zip(kaps, fs)]
    t1 = uhr()
    lo, hi, status, kl0 = schiessen(kaps, Om2s)
    protokoll.append(f"Schiessen ({len(kaps)} Mitglieder): {uhr() - t1:.1f} s")
    aus = []
    for i, (kap, f, Om2) in enumerate(zip(kaps, fs, Om2s)):
        a = 1.0 - Om2
        e = {"kappa": kap, "f": f, "Omega2": Om2, "Omega": math.sqrt(Om2), "h": h, "hp": hp, "schiessen": status[i],
             "klassen_runde0": kl0[i]}
        if status[i] != "Klammer":
            e["gueltig"] = False
            aus.append(e)
            continue
        r_s, th_s, grund, f_ans = startprofil(lo[i], hi[i], a, kap, 0.02)
        kinf = math.sqrt(a)
        e.update({"theta0_schuss": float(0.5 * (lo[i] + hi[i])), "klammer_breite": float(hi[i] - lo[i]),
                  "anschluss_grund": grund, "f_anschluss": f_ans, "r_anschluss": float(r_s[-1]), "kappa_inf": kinf})
        Rw_s, dl_s, _, _ = wandgeometrie(r_s, th_s, np.sin(th_s) ** 2)
        if not math.isfinite(Rw_s):
            Rw_s = float(r_s[-1])
        R_max = max(3.0 * Rw_s, Rw_s + 25.0 / kinf)
        e["R_w_schuss"] = Rw_s
        e["R_max"] = R_max
        if R_max > 3000.0:
            e["gueltig"] = False
            e["ausgeschlossen"] = "R_max > 3000"
            aus.append(e)
            continue
        J = int(math.ceil(R_max / hp))
        r = np.arange(J + 1) * hp
        th0 = np.interp(r, r_s, th_s)
        rm = r_s[-1]
        Atl = th_s[-1] * rm * math.exp(kinf * rm)
        jenseits = r > rm
        th0[jenseits] = Atl * np.exp(-kinf * r[jenseits]) / r[jenseits]
        y, it, schritt, konv = numerov_newton(r, r * th0, a, kap)
        th = np.empty(J + 1)
        th[1:] = y[1:] / r[1:]
        th[0] = (4.0 * th[1] - th[2]) / 3.0
        dth = d1_fd4(th, hp, gerade=True)
        s2 = np.sin(th) ** 2
        Rw, dl, r90, r10 = wandgeometrie(r, th, s2)
        gq = s2 * r * r
        Nq = math.sqrt(Om2) * 4.0 * PI * float(0.5 * np.sum((gq[1:] + gq[:-1]) * np.diff(r)))
        # K3: Phasenmode v = sin Theta (l = 0), Translationsmode u = Theta' (l = 1)
        Vu, Vv = V_uv(th, dth, a, kap)
        Y = r * np.sin(th)
        Z = r * dth
        bereich = slice(3, J - 3)
        res_v = (-d2_fd4(Y, hp, gerade=False) + Vv * Y)[bereich] / r[bereich]
        Zpp = d2_fd4(Z, hp, gerade=True)
        res_u = (-Zpp[bereich] + (2.0 / r[bereich] ** 2) * Z[bereich] + Vu[bereich] * Z[bereich]) / r[bereich]
        e.update({"gueltig": bool(konv and th[0] > 1e-3 and math.isfinite(Rw) and math.isfinite(dl)),
                  "newton_konvergiert": bool(konv), "newton_iter": it, "newton_schritt": schritt, "theta0": float(th[0]),
                  "theta0_diff_schuss": float(th[0] - e["theta0_schuss"]), "R_w": Rw, "delta": dl, "r90": r90,
                  "r10": r10, "N": Nq, "J": J,
                  "K3_phase": float(np.max(np.abs(res_v)) / np.max(np.abs(np.sin(th)))),
                  "K3_transl": float(np.max(np.abs(res_u)) / np.max(np.abs(dth))),
                  "K3_phase_r": float(r[bereich][int(np.argmax(np.abs(res_v)))]),
                  "K3_transl_r": float(r[bereich][int(np.argmax(np.abs(res_u)))])})
        e["_r"] = r
        e["_th"] = th
        e["_A"] = 0.5 * (Vu + Vv)
        e["_B"] = 2.0 * math.sqrt(Om2) * np.cos(th)
        aus.append(e)
    return aus


# ----------------------------------------------------------------------------------------------------------------------
# Gemeinsamer Codepfad: nackter geschlossener Kanal, Nullstellen, Wandanteil
# ----------------------------------------------------------------------------------------------------------------------

def sturm(a0, bl, c2, off2, rhos):
    """Zahl der negativen Eigenwerte von H(rho) (Diagonale a0 + bl rho - c2 rho^2, Nebendiagonale^2 = off2)."""
    rh = np.asarray(rhos, dtype=float)
    mr2 = -c2 * rh * rh
    q = (a0[0] + bl[0] * rh) + mr2
    neg = (q < 0).astype(np.int32)
    with np.errstate(divide="ignore", invalid="ignore", over="ignore"):
        for i in range(1, len(a0)):
            q = ((a0[i] + bl[i] * rh) + mr2) - off2 / q
            neg += q < 0
    return neg


def kanal_suche(r, A, B, c2, rho_lo, rho_hi, offen, geschlossen, Rw, delta, M1=3000, M2=30, M3=30, k_max=None):
    """Alle Nullstellen lambda_k(rho_c) = 0 von H(rho) = -d^2/dr^2 + A + B rho - c2 rho^2 in (rho_lo, rho_hi)
    (Dirichlet bei r_0 = 0 und r_J = R_max). Eingebettet: offen < rho_c < geschlossen."""
    hp = r[1] - r[0]
    ri = r[1:-1]
    a0 = (2.0 / hp ** 2 + A[1:-1]).tolist()
    bl = np.asarray(B[1:-1] if np.ndim(B) else np.full(len(ri), B), dtype=float).tolist()
    off2 = 1.0 / hp ** 4
    x1 = np.linspace(rho_lo, rho_hi, M1)
    n1 = sturm(a0, bl, c2, off2, x1)
    zellen = np.nonzero(np.diff(n1))[0]
    kand = []
    if len(zellen):
        sub = np.concatenate([np.linspace(x1[j], x1[j + 1], M2 + 1)[1:-1] for j in zellen])
        n2 = sturm(a0, bl, c2, off2, sub)
        m = M2 - 1
        for q, j in enumerate(zellen):
            xs = np.concatenate([[x1[j]], sub[q * m:(q + 1) * m], [x1[j + 1]]])
            ns = np.concatenate([[n1[j]], n2[q * m:(q + 1) * m], [n1[j + 1]]])
            for t in np.nonzero(np.diff(ns))[0]:
                kand.append((xs[t], xs[t + 1], int(ns[t]), int(ns[t + 1])))
    wurzeln = []
    if kand:
        sub = np.concatenate([np.linspace(k[0], k[1], M3 + 1)[1:-1] for k in kand])
        n3 = sturm(a0, bl, c2, off2, sub)
        m = M3 - 1
        for q, (xa, xb, na, nb) in enumerate(kand):
            xs = np.concatenate([[xa], sub[q * m:(q + 1) * m], [xb]])
            ns = np.concatenate([[na], n3[q * m:(q + 1) * m], [nb]])
            for t in np.nonzero(np.diff(ns))[0]:
                n_a, n_b = int(ns[t]), int(ns[t + 1])
                for k in range(min(n_a, n_b), max(n_a, n_b)):
                    wurzeln.append({"k": k, "rho_c": float(0.5 * (xs[t] + xs[t + 1])),
                                    "breite": float(xs[t + 1] - xs[t]), "richtung": "ab" if n_b > n_a else "auf"})
    wurzeln.sort(key=lambda w: (w["rho_c"], w["k"]))
    off = -np.ones(len(ri) - 1) / hp ** 2
    fenster = np.abs(ri - Rw) < 2.0 * delta
    innen = ri < Rw - 2.0 * delta
    R_aussen = Rw + 2.0 * delta
    L_w = (R_aussen - max(0.0, Rw - 2.0 * delta)) / R_aussen
    for w in wurzeln:
        if k_max is not None and w["k"] > k_max:
            continue
        rc = w["rho_c"]
        d = 2.0 / hp ** 2 + A[1:-1] + np.asarray(B[1:-1] if np.ndim(B) else B) * rc - c2 * rc * rc
        lam, vec = eigh_tridiagonal(d, off, select="i", select_range=(w["k"], w["k"]))
        y2 = vec[:, 0] ** 2
        s = float(np.sum(y2))
        Fw = float(np.sum(y2[fenster]) / s)
        w.update({"lambda": float(lam[0]), "F_w": Fw, "F_innen": float(np.sum(y2[innen]) / s),
                  "F_aussen": float(np.sum(y2[ri >= R_aussen]) / s),
                  "P_laenge": float(s * s / np.sum(y2 * y2) * hp), "r_spitze": float(ri[int(np.argmax(y2))]),
                  "r_mittel": float(np.sum(ri * y2) / s), "eta": Fw / L_w,
                  "eingebettet": bool(offen < rc < geschlossen), "wand": bool(Fw > 0.5)})
    return wurzeln, {"N_neg_rand": int(n1[-1]), "N_neg_start": int(n1[0]), "L_w": L_w, "M1": M1, "M2": M2, "M3": M3,
                     "aufloesung": float((rho_hi - rho_lo) / ((M1 - 1) * M2 * M3))}


def zusammenfassung(wurzeln):
    """Tiefster Zustand (kleinstes rho_c), tiefster Wandzustand, eingebettete Wandzustaende; R4 (k <= 5) und alle k."""
    aus = {}
    for name, menge in (("R4", [w for w in wurzeln if w["k"] <= 5]), ("alle", wurzeln)):
        mit = [w for w in menge if "F_w" in w]
        tief = mit[0] if mit else None
        wand = [w for w in mit if w["wand"]]
        ew = [w for w in wand if w["eingebettet"]]
        aus[name] = {"anzahl": len(menge),
                     "tiefster": ({k: tief[k] for k in ("k", "rho_c", "F_w", "eingebettet", "eta", "P_laenge")}
                                  if tief else None),
                     "tiefster_wand": ({k: wand[0][k] for k in ("k", "rho_c", "F_w", "eingebettet", "eta", "P_laenge")}
                                       if wand else None),
                     "eingebettete_wand": [{k: w[k] for k in ("k", "rho_c", "F_w", "eta", "P_laenge", "r_spitze")}
                                           for w in ew],
                     "eingebettete_wand_eta_ueber_2": len([w for w in ew if w["eta"] > 2.0])}
    return aus


# ----------------------------------------------------------------------------------------------------------------------
# Kommandos
# ----------------------------------------------------------------------------------------------------------------------

def cmd_familie(a, erg, zeilen):
    kaps = [float(x) for x in a.kappa.split(",")]
    fs = [float(x) for x in a.f.split(",")] if a.f else FS
    paare = [(k, f) for k in kaps for f in fs]
    prot = []
    prs = afm_profile([p[0] for p in paare], [p[1] for p in paare], a.h, prot)
    zeilen += prot
    erg["mitglieder"] = []
    zeilen.append(f"AFM-Familie h = {a.h} (Rechengitter {0.5 * a.h}); Suche rho in (0, 1 + Omega), M1 = {a.m1}")
    zeilen.append("kappa | f | Omega | Theta0 | R_w | delta | R_max | Newton | K3 phase/transl | #Wurzeln (k<=5/alle) | "
                  "tiefster (rho_c, F_w, eing.) | tiefster Wand | eingeb. Wand (n, eta>2) | Zeit")
    for p in prs:
        t1 = uhr()
        if not p.get("gueltig"):
            erg["mitglieder"].append({k: v for k, v in p.items() if not k.startswith("_")})
            zeilen.append(f"{p['kappa']} | {p['f']} | {p['Omega']:.6f} | ungueltig: {p.get('schiessen')} "
                          f"{p.get('ausgeschlossen', '')} Newton {p.get('newton_iter', '-')}")
            continue
        Om = p["Omega"]
        wz, info = kanal_suche(p["_r"], p["_A"], p["_B"], 1.0, 1e-6, (1.0 + Om) * (1.0 - 1e-9), 1.0 - Om, 1.0 + Om,
                               p["R_w"], p["delta"], M1=a.m1)
        zf = zusammenfassung(wz)
        e = {k: v for k, v in p.items() if not k.startswith("_")}
        e.update({"wurzeln": wz, "suche": info, "zusammenfassung": zf, "zeit_kanal": uhr() - t1})
        erg["mitglieder"].append(e)

        def kurz(x):
            return "-" if x is None else f"({x['rho_c']:.6f}, {x['F_w']:.3f}, {'ja' if x['eingebettet'] else 'nein'})"
        zr, za = zf["R4"], zf["alle"]
        zeilen.append(f"{p['kappa']} | {p['f']} | {Om:.6f} | {p['theta0']:.10f} | {p['R_w']:.3f} | {p['delta']:.3f} | "
                      f"{p['R_max']:.1f} | {p['newton_iter']} ({p['newton_schritt']:.0e}) | {p['K3_phase']:.1e}/"
                      f"{p['K3_transl']:.1e} | {zr['anzahl']}/{za['anzahl']} | R4 {kurz(zr['tiefster'])} alle "
                      f"{kurz(za['tiefster'])} | R4 {kurz(zr['tiefster_wand'])} alle {kurz(za['tiefster_wand'])} | "
                      f"R4 {len(zr['eingebettete_wand'])},{zr['eingebettete_wand_eta_ueber_2']} alle "
                      f"{len(za['eingebettete_wand'])},{za['eingebettete_wand_eta_ueber_2']} | {uhr() - t1:.1f} s")


def nls2_profil(art, x, hp, beta=0.5):
    import nls2
    nls2.MODELL.clear()
    nls2.MODELL.update({"art": art, "beta": beta, "d": 3})
    return nls2.profile([x], hp)[0]


def verlaengern(pr, R_max):
    """nls2-Profil (Gitter bis R_aus) mit dem Schwanz A e^{-k r}/r bis R_max verlaengern."""
    r, phi = pr["r"], pr["phi"]
    hp = pr["hp"]
    J = int(math.ceil(R_max / hp))
    if J + 1 <= len(r):
        return r[:J + 1], phi[:J + 1]
    rr = np.arange(J + 1) * hp
    ph = np.empty(J + 1)
    ph[:len(r)] = phi
    kap = pr["kappa0"]
    Atl = phi[-1] * r[-1] * math.exp(kap * r[-1])
    ph[len(r):] = Atl * np.exp(-kap * rr[len(r):]) / rr[len(r):]
    return rr, ph


def cmd_kontrollen(a, erg, zeilen):
    hp = 0.5 * a.h
    # K0: kappa = 0, Profil-Loeser muss "keine Loesung" melden
    om2 = [0.90, 0.95, 0.99]
    lo, hi, st, kl0 = schiessen([0.0] * 3, om2)
    k0 = [{"Omega2": o, "status": s, "klassen_runde0": k} for o, s, k in zip(om2, st, kl0)]
    k0_ok = all(s.startswith("keine Loesung") for s in st)
    erg["K0"] = {"faelle": k0, "bestanden": k0_ok}
    zeilen.append(f"K0 kappa = 0, Omega^2 = 0,90/0,95/0,99: " + "; ".join(f"{s} {k}" for s, k in zip(st, kl0))
                  + f" -> {'bestanden' if k0_ok else 'VERFEHLT'}")
    # K1: Theta = 0 (Vakuum), Omega aus kappa = -0,10, f = 0,5; kein Zustand, Kante 1 - (rho - Omega)^2
    Om = math.sqrt(1.0 - 0.10 + 0.5 * 0.10)
    R = 500.0
    J = int(round(R / hp))
    r = np.arange(J + 1) * hp
    A = np.full(J + 1, 1.0 - Om * Om)
    B = np.full(J + 1, 2.0 * Om)
    wz, info = kanal_suche(r, A, B, 1.0, 1e-6, (1.0 + Om) * (1.0 - 1e-9), 1.0 - Om, 1.0 + Om, 50.0, 5.0, M1=a.m1)
    off = -np.ones(J - 2) / hp ** 2
    abw = []
    for rho in (0.5, 1.0, 1.9):
        d = 2.0 / hp ** 2 + A[1:-1] + B[1:-1] * rho - rho * rho
        lam = eigh_tridiagonal(d, off, select="i", select_range=(0, 0), eigvals_only=True)[0]
        ana = 4.0 / hp ** 2 * math.sin(PI / (2.0 * J)) ** 2 + 1.0 - (rho - Om) ** 2
        abw.append(float(lam - ana))
    k1_ok = (len(wz) == 0) and max(abs(x) for x in abw) < 1e-8
    erg["K1"] = {"Omega": Om, "R": R, "wurzeln": len(wz), "abw_lambda0": abw, "bestanden": k1_ok}
    zeilen.append(f"K1 Vakuum Omega = {Om:.6f}, R = {R}: Wurzeln {len(wz)}, lambda_0 - analytisch {abw} -> "
                  f"{'bestanden' if k1_ok else 'VERFEHLT'}")
    # K2: KG-Q-Ball (nls2 qball, beta = 0,5), omega^2 = 0,7977; R10: E = 0,706247 (h = 0,02)
    w2 = 0.7977
    pr = nls2_profil("qball", w2, hp)
    om = math.sqrt(w2)
    kinf = math.sqrt(1.0 - w2)
    f = pr["phi"]
    Rw, dl, _, _ = wandgeometrie(pr["r"], f, f * f)
    R_max = max(3.0 * Rw, Rw + 25.0 / kinf)
    rr, ph = verlaengern(pr, R_max)
    n0 = ph * ph
    dp = 1.0 - 4.0 * n0 + 9.0 * 0.5 * n0 * n0
    wz, info = kanal_suche(rr, dp - w2, np.full(len(rr), 2.0 * om), 1.0, 1e-6, (1.0 + om) * (1.0 - 1e-9), 1.0 - om,
                           1.0 + om, Rw, dl, M1=a.m1)
    ziel = om + math.sqrt(0.706247)
    treffer = [w for w in wz if abs(w["rho_c"] - ziel) < 0.01]
    k2_ok = any(w.get("eingebettet") and w.get("wand") for w in treffer)
    erg["K2"] = {"omega2": w2, "R_w": Rw, "delta": dl, "R_max": R_max, "ziel_rho": ziel, "wurzeln": wz, "suche": info,
                 "E_aequivalent": [(w["rho_c"] - om) ** 2 for w in wz], "bestanden": k2_ok}
    zeilen.append(f"K2 KG-Q-Ball omega^2 = {w2}: R_w = {Rw:.4f}, delta = {dl:.4f}, R_max = {R_max:.2f}; Wurzeln: " +
                  "; ".join(f"k={w['k']} rho_c={w['rho_c']:.6f} (E={(w['rho_c'] - om) ** 2:.6f}) F_w={w['F_w']:.3f} "
                            f"eing={w['eingebettet']}" for w in wz) + f"; Ziel rho = {ziel:.6f} -> "
                  f"{'bestanden' if k2_ok else 'VERFEHLT'}")
    # K4: kubisch-quintisches NLS (nls2 cqnls, 3D), Flachkuppen Omega = 0,16 und 0,17 (R10: E_0 = +0,0213 / +0,0236)
    erg["K4"] = []
    k4_ok = True
    for Omn in (0.16, 0.17):
        pr = nls2_profil("cqnls", -0.5 * Omn, hp)
        w = pr["phi"]
        Rw, dl, _, _ = wandgeometrie(pr["r"], w, w * w)
        kinf = math.sqrt(Omn)
        R_max = max(3.0 * Rw, Rw + 25.0 / kinf)
        rr, ph = verlaengern(pr, R_max)
        n0 = ph * ph
        D = -n0 + 1.5 * n0 * n0 + 0.5 * Omn
        wz, info = kanal_suche(rr, 2.0 * D, np.ones(len(rr)), 0.0, -Omn * (1.0 - 1e-6), 1.0, Omn, float("inf"), Rw, dl,
                               M1=a.m1)
        schlecht = [x for x in wz if x.get("eingebettet") and x.get("wand")]
        ok = len(schlecht) == 0
        k4_ok &= ok
        erg["K4"].append({"Omega": Omn, "R_w": Rw, "delta": dl, "R_max": R_max, "wurzeln": wz, "suche": info,
                          "E_aequivalent": [-0.5 * x["rho_c"] for x in wz], "bestanden": ok})
        zeilen.append(f"K4 NLS Omega = {Omn}: R_w = {Rw:.3f}, delta = {dl:.3f}, R_max = {R_max:.1f}; Wurzeln nu_c in "
                      f"(-Omega, 1): " + "; ".join(f"k={x['k']} nu_c={x['rho_c']:.6f} (E={-0.5 * x['rho_c']:+.6f}) "
                                                  f"F_w={x['F_w']:.3f} eing={x['eingebettet']}" for x in wz)
                      + f" -> {'bestanden' if ok else 'VERFEHLT'}")
    erg["K4_bestanden"] = k4_ok


def cmd_auswertung(a, erg, zeilen):
    """Bindende Regel (KARTE.md) und Regel 8 aus den Familien- und Kontrolldateien im Ordner a.aus."""
    fam = {}
    for pfad in sorted(glob.glob(os.path.join(a.aus, "fam-*.json"))):
        d = json.load(open(pfad))
        for m in d.get("mitglieder", []):
            fam[(m["kappa"], m["f"], m["h"])] = m
    kon = {}
    for pfad in sorted(glob.glob(os.path.join(a.aus, "kon-*.json"))):
        d = json.load(open(pfad))
        kon[d["argumente"]["h"]] = d
    hs = sorted({k[2] for k in fam})
    zeilen.append(f"Auswertung: {len(fam)} Mitglied-Gitter-Paare, Gitter {hs}, Kontrolldateien {sorted(kon)}")
    k3 = [(k, m.get("K3_phase"), m.get("K3_transl")) for k, m in fam.items() if m.get("gueltig")]
    k3_ok = all(p is not None and p < 1e-6 and t < 1e-6 for _, p, t in k3) and len(k3) > 0
    kontrollen = {"K3": k3_ok}
    for h, d in kon.items():
        kontrollen[f"K0 h={h}"] = d["K0"]["bestanden"]
        kontrollen[f"K1 h={h}"] = d["K1"]["bestanden"]
        kontrollen[f"K2 h={h}"] = d["K2"]["bestanden"]
        kontrollen[f"K4 h={h}"] = d["K4_bestanden"]
    erg["kontrollen"] = kontrollen
    erg["K3_max"] = [max((p for _, p, _ in k3), default=None), max((t for _, _, t in k3), default=None)]
    zeilen.append("Kontrollen: " + ", ".join(f"{k}: {'ja' if v else 'NEIN'}" for k, v in kontrollen.items())
                  + f"; K3 max phase/transl = {erg['K3_max']}")
    paare = sorted({(k[0], k[1]) for k in fam})
    for menge in ("R4", "alle"):
        tab = []
        weiter = []
        irgendwo = []
        regel8 = []
        for (kap, f) in paare:
            ms = [fam.get((kap, f, h)) for h in hs]
            if any(m is None or not m.get("gueltig") for m in ms):
                tab.append({"kappa": kap, "f": f, "status": "ungueltig/ausgeschlossen"})
                continue
            z = [m["zusammenfassung"][menge] for m in ms]
            ew = [zz["eingebettete_wand"] for zz in z]
            if any(len(x) for x in ew):
                irgendwo.append((kap, f))
            stimmt = []
            if len(hs) == 2:
                for w1 in ew[0]:
                    for w2 in ew[1]:
                        if abs(w1["rho_c"] - w2["rho_c"]) < 1e-3:
                            stimmt.append((w1["rho_c"], w2["rho_c"], w1["F_w"], w2["F_w"], w1["eta"], w2["eta"]))
            if stimmt:
                weiter.append((kap, f, stimmt[0]))
            t8 = [zz["tiefster"] for zz in z]
            regel8.append((kap, f, [bool(t and t["eingebettet"]) for t in t8]))
            tab.append({"kappa": kap, "f": f, "eingeb_wand_je_gitter": [len(x) for x in ew], "paare_1e-3": len(stimmt),
                        "tiefster": t8, "tiefster_wand": [zz["tiefster_wand"] for zz in z],
                        "erstes_paar": stimmt[0] if stimmt else None})
        alle_kontrollen = all(kontrollen.values()) and len(kon) == 2
        if not alle_kontrollen:
            ausgang = "nicht auswertbar"
        elif weiter:
            ausgang = "weiter"
        elif not irgendwo:
            ausgang = "verworfen"
        else:
            ausgang = "unentschieden (Regel-Luecke: eingebetteter Wandzustand nur auf einer Stufe oder Lage > 1e-3)"
        r8_besteht = any(any(x) for _, _, x in regel8)
        r8_beide = [(k, f) for k, f, x in regel8 if all(x)]
        erg[f"ausgang_{menge}"] = {"ausgang": ausgang, "weiter_mitglieder": weiter, "irgendwo": irgendwo,
                                   "tabelle": tab, "regel8_besteht": r8_besteht, "regel8_beide_stufen": r8_beide}
        zeilen.append(f"[{menge}] Ausgang nach der bindenden Regel: {ausgang}; Mitglieder mit eingebettetem Wandzustand "
                      f"auf beiden Stufen (Lage < 1e-3): {len(weiter)} von {len(paare)}; Regel 8 besteht: {r8_besteht} "
                      f"(auf beiden Stufen bei {len(r8_beide)} Mitgliedern)")
        for t in tab:
            zeilen.append(f"  [{menge}] {json.dumps(jsonfest(t))[:600]}")


def argumente():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("kommando", choices=["familie", "kontrollen", "auswertung"])
    ap.add_argument("--kappa", type=str, default="-0.2")
    ap.add_argument("--f", type=str, default="")
    ap.add_argument("--h", type=float, default=0.02)
    ap.add_argument("--m1", type=int, default=3000)
    ap.add_argument("--aus", type=str, default="aus")
    ap.add_argument("--name", type=str, default="")
    return ap.parse_args()


def main():
    a = argumente()
    name = a.name or a.kommando
    os.makedirs(a.aus, exist_ok=True)
    zeilen = [f"afm_kanal.py {a.kommando} ({name}), Start {jetzt()}", "Argumente: " + json.dumps(vars(a))]
    erg = {"argumente": vars(a), "start": jetzt()}
    rc = 0
    try:
        {"familie": cmd_familie, "kontrollen": cmd_kontrollen, "auswertung": cmd_auswertung}[a.kommando](a, erg, zeilen)
    except Exception:
        import traceback
        zeilen.append("FEHLER: " + traceback.format_exc())
        erg["fehler"] = traceback.format_exc()
        rc = 1
    zeilen.append(f"Ende {jetzt()}, Laufzeit {uhr():.1f} s")
    erg["ende"] = jetzt()
    erg["laufzeit"] = uhr()
    with open(os.path.join(a.aus, f"{name}.txt"), "w") as fh:
        fh.write("\n".join(zeilen) + "\n")
    with open(os.path.join(a.aus, f"{name}.json"), "w") as fh:
        json.dump(jsonfest(erg), fh, indent=1)
    print("\n".join(zeilen))
    return rc


if __name__ == "__main__":
    sys.exit(main())
