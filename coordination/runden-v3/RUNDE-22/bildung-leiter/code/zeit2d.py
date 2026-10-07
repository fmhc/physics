#!/usr/bin/env python3
"""BILDUNG-LEITER (Runde 22), Leitung claude-primary, 02.10.2026. Karte: RUNDE-22/bildung-leiter/KARTE.md.

Radiale 2D-Zeitentwicklung (l = 0) des Einfeldmodells M1, U(S) = S - S^2 + S^3/2, mit Hilfsfunktionen aus
RUNDE-12/leiter2d-praez/bic2_2d_praez_v2.py (unveraendert importiert: profil, f_werte, r_halb, matrix_pencil).

- Gitter r_j = j dr, j = 0..N, Dirichlet bei r_max, Daempfungsschicht r > r_sd wie im Runde-12-Zeitlauf (SIGMA0,
  quadratisch), Leapfrog mit dt = 0,4 dr.
- 2D-Laplace direkt auf psi: (p[j+1] - 2 p[j] + p[j-1])/dr^2 + (p[j+1] - p[j-1])/(2 r_j dr), bei r = 0: 4 (p1 - p0)/dr^2.
- Profil: Runde-12-ODE-Profil (dim 2), danach Newton auf der diskreten Gleichung desselben Gitters (lap f + (w2 - U'(f^2)) f
  = 0), damit die ungestoerte Loesung im Zeitlauf stationaer ist.

Arme (je Aufruf ein omega^2, zwei Reihen gleichzeitig):
  lin : linearisiert um das diskrete Profil: Phi_tt = lap Phi - dp Phi - sp exp(-2 i w t) conj(Phi),
        dp = U' + S U'', sp = S U''. Reihen 'wand' (g = r f'(r), normiert) und 'kick' (Gauss, Breite 0,5, an r_halb).
        Phi(0) = g, Phi_t(0) = -i w g.
  nl  : nichtlinear psi_tt = lap psi - U'(|psi|^2) psi. Reihen 'gauss' (|psi|^2 Gauss mit Q = Q_F und
        rms-Radius = R_rms des Profils, psi_t = -i w psi) und 'exakt' (diskretes Profil, K0).
Aufruf: python zeit2d.py <lin|nl> <omega2> <dr> <T> <r_sd> <r_max> <aus.json>
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import cmath
import json
import math
import sys
import time

import numpy as np
import torch
from scipy.linalg import solve_banded

torch.set_num_threads(1)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bic2_2d_praez_v2 as m  # noqa: E402

F64, C128, PI, BETA, SIGMA0 = m.F64, m.C128, m.PI, m.BETA, m.SIGMA0
BIC_BAND = (1.45, 1.65)          # Frequenzband der stillen Mode bei n = 7 (Runde 12: Re rho ~ 1,556)


def u1(S):
    return 1.0 - 2.0 * S + 3.0 * BETA * S * S


def u2(S):
    return -2.0 + 6.0 * BETA * S


def lap2d(p, dr, r):
    a = torch.zeros_like(p)
    a[:, 1:-1] = (p[:, 2:] - 2.0 * p[:, 1:-1] + p[:, :-2]) / (dr * dr) + (p[:, 2:] - p[:, :-2]) / (2.0 * dr * r[1:-1])
    a[:, 0] = 4.0 * (p[:, 1] - p[:, 0]) / (dr * dr)
    return a                                   # a[:, -1] = 0: Dirichlet bei r_max


def diskretes_profil(f0, w2, dr, iters=30):
    """Newton auf F_j = lap f + (w2 - U'(f^2)) f = 0, j = 0..N-1, f_N = 0 (tridiagonal, scipy solve_banded)."""
    f = np.array(f0, dtype=np.float64)
    N = len(f) - 1
    r = np.arange(N + 1) * dr
    verlauf = []
    for _ in range(iters):
        lap = np.zeros(N + 1)
        lap[1:-1] = (f[2:] - 2.0 * f[1:-1] + f[:-2]) / dr ** 2 + (f[2:] - f[:-2]) / (2.0 * dr * r[1:-1])
        lap[0] = 4.0 * (f[1] - f[0]) / dr ** 2
        S = f * f
        F = lap + (w2 - u1(S)) * f
        F = F[:N]
        res = float(np.abs(F).max())
        verlauf.append(res)
        if res < 1e-13:
            break
        diag = -2.0 / dr ** 2 + w2 - u1(S[:N]) - 2.0 * S[:N] * u2(S[:N])
        diag[0] = -4.0 / dr ** 2 + w2 - u1(S[0]) - 2.0 * S[0] * u2(S[0])
        ober = np.zeros(N)                       # ober[j] = dF_j / df_{j+1}, j = 0..N-2 (f_N fest)
        unter = np.zeros(N)                      # unter[j] = dF_j / df_{j-1}, j = 1..N-1
        ober[0] = 4.0 / dr ** 2
        ober[1:N - 1] = 1.0 / dr ** 2 + 1.0 / (2.0 * dr * r[1:N - 1])
        unter[1:N] = 1.0 / dr ** 2 - 1.0 / (2.0 * dr * r[1:N])
        ab = np.zeros((3, N))
        ab[0, 1:] = ober[:N - 1]
        ab[1, :] = diag
        ab[2, :-1] = unter[1:]
        df = solve_banded((1, 1), ab, -F)
        f[:N] += df
    return f, verlauf


def fenster_pencil(y, mess, fenster):
    aus = []
    n = y.shape[0]
    for (t0, t1) in fenster:
        i0 = int(round(t0 / mess))
        i1 = min(n, int(round(t1 / mess)) + 1)
        p = m.matrix_pencil(y[i0:i1], mess)[:12] if i1 - i0 >= 12 else []
        aus.append({"t0": t0, "t1": t1, "pencil": p})
    return aus


def anteile(pencil, schwelle):
    """Amplitude^2-Anteile: gebunden (0,01 < |re| < schwelle), still (|re| im BIC_BAND), Rest; ohne Gleichanteil."""
    tot = sum(e["amp"] ** 2 for e in pencil if abs(e["re"]) > 0.01)
    if tot <= 0:
        return {"gebunden": None, "still": None}
    geb = sum(e["amp"] ** 2 for e in pencil if 0.01 < abs(e["re"]) < schwelle)
    sti = sum(e["amp"] ** 2 for e in pencil if BIC_BAND[0] <= abs(e["re"]) <= BIC_BAND[1])
    return {"gebunden": geb / tot, "still": sti / tot}


def main():
    arm, w2, dr, T, r_sd, r_max, pfad = (sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]),
                                         float(sys.argv[5]), float(sys.argv[6]), sys.argv[7])
    t_wand = time.time()
    dev = torch.device("cpu")
    prof = m.profil(w2, 2.0, BETA, dr, dev)
    om = math.sqrt(w2)
    N = int(round(r_max / dr))
    f_l, _ = m.f_werte(prof, N + 1)
    f_l[-1] = 0.0
    f_np, newton_verlauf = diskretes_profil(f_l, w2, dr)
    f = torch.tensor(f_np, dtype=F64)
    r = torch.arange(N + 1, dtype=F64) * dr
    fp = torch.zeros_like(f)
    fp[1:-1] = (f[2:] - f[:-2]) / (2.0 * dr)
    wfl = 2.0 * PI * r * dr
    wfl[0] = PI * dr * dr / 4.0
    S_p = f * f
    Q_F = float(2.0 * om * (S_p * wfl).sum())
    R_rms = math.sqrt(float((r * r * S_p * wfl).sum() / (S_p * wfl).sum()))
    rh = m.r_halb(prof)
    dt = 0.4 * dr
    n_mess = max(1, int(round(0.2 / dt)))
    mess = n_mess * dt
    n_schritte = int(round(T / dt))
    gam = torch.where(r > r_sd, SIGMA0 * ((r - r_sd) / (r_max - r_sd)) ** 2, torch.zeros_like(r))
    fak_p = 1.0 / (1.0 + 0.5 * dt * gam)
    fak_m = 1.0 - 0.5 * dt * gam
    dpot = u1(S_p) + S_p * u2(S_p)
    spot = S_p * u2(S_p)
    j_sd = int(round(r_sd / dr))
    orte = {"zentrum": 0, "halb": max(1, int(round(0.5 * rh / dr))), "wand": int(round(rh / dr)),
            "aussen": min(N - 1, int(round((rh + 10.0) / dr)))}
    if arm == "lin":
        namen = ["wand", "kick"]
        g_w = r * fp
        g_w = g_w / g_w.abs().max()
        g_k = torch.exp(-((r - rh) ** 2) / (2.0 * 0.25))
        G = torch.stack([g_w, g_k])
    elif arm == "nl":
        namen = ["gauss", "exakt"]
        s = R_rms
        A = math.sqrt(Q_F / (2.0 * om * PI * s * s))
        G = torch.stack([A * torch.exp(-(r * r) / (2.0 * s * s)), f])
    else:
        raise SystemExit("arm: lin | nl")
    phi = G.to(C128)
    vel = -1j * om * phi

    def beschl(p, t):
        a = lap2d(p, dr, r)
        if arm == "nl":
            S = p.real ** 2 + p.imag ** 2
            a = a - u1(S) * p
        else:
            a = a - dpot * p - (spot * cmath.exp(-2j * om * t)) * p.conj()
        a[:, -1] = 0.0
        return a

    phi_alt = phi - dt * vel + 0.5 * dt * dt * beschl(phi, 0.0)
    ts, sig, szen, ladung, proj = [], [], [], [], []
    for n in range(n_schritte + 1):
        t = n * dt
        a = beschl(phi, t)
        phi_neu = (2.0 * phi - fak_m * phi_alt + dt * dt * a) * fak_p
        if n % n_mess == 0:
            dreh = cmath.exp(1j * om * t)
            ts.append(t)
            sig.append(torch.stack([phi[:, j] for j in orte.values()], dim=1) * dreh)
            szen.append(phi[:, 0].abs() ** 2)
            v = (phi_neu - phi_alt) / (2.0 * dt)
            ladung.append(-2.0 * ((phi[:, :j_sd].conj() * v[:, :j_sd]).imag * wfl[:j_sd]).sum(1))
            if arm == "lin":
                proj.append(((phi[:, :j_sd] * dreh) * G[:, :j_sd] * wfl[:j_sd]).sum(1)
                            / (G[:, :j_sd] ** 2 * wfl[:j_sd]).sum(1))
        phi_alt, phi = phi, phi_neu
    sig = torch.stack(sig)            # (zeiten, reihen, orte)
    szen = torch.stack(szen)          # (zeiten, reihen)
    ladung = torch.stack(ladung)
    fenster = [(50.0, 400.0), (400.0, 1200.0), (1200.0, T), (200.0, T)]
    schwelle = 1.0 - om
    out = {"arm": arm, "w2": w2, "omega": om, "dr": dr, "dt": dt, "mess": mess, "T": T, "r_sd": r_sd, "r_max": r_max,
           "N": N, "Q_F": Q_F, "R_rms": R_rms, "r_halb": rh, "S0": float(S_p[0]), "schwelle_a": schwelle,
           "newton_residuen": newton_verlauf, "profil_ode_grund": prof.get("grund"),
           "f0_ode": prof["f0"], "f0_diskret": float(f[0]), "reihen": namen, "analyse": []}
    for i, name in enumerate(namen):
        e = {"reihe": name, "ladung_anfang": float(ladung[0, i]), "ladung_ende": float(ladung[-1, i])}
        if arm == "lin":
            p = torch.stack(proj)[:, i]
            e["projektion"] = fenster_pencil(p, mess, fenster)
            e["zentrum"] = fenster_pencil(sig[:, i, 0], mess, fenster)
            e["wand"] = fenster_pencil(sig[:, i, 2], mess, fenster)
        else:
            sz = szen[:, i]
            e["S_zentrum_anfang"] = float(sz[0])
            e["S_zentrum_rel_abw_max"] = float(((sz - sz[0]).abs() / sz[0]).max())
            mitte = []
            for (t0, t1) in [(100.0, 600.0), (600.0, 1300.0), (1300.0, T)]:
                i0, i1 = int(round(t0 / mess)), min(len(ts), int(round(t1 / mess)) + 1)
                y = (sz[i0:i1] - sz[i0:i1].mean()).to(C128)
                pen = m.matrix_pencil(y, mess)[:12] if i1 - i0 >= 12 else []
                mitte.append({"t0": t0, "t1": t1, "pencil": pen, "anteile": anteile(pen, schwelle),
                              "S_mittel": float(sz[i0:i1].mean()), "S_spanne": float(sz[i0:i1].max() - sz[i0:i1].min())})
            e["S_zentrum_spektrum"] = mitte
            sch = max(1, len(ts) // 4000)
            e["roh_t"] = ts[::sch]
            e["roh_S_zentrum"] = sz[::sch].tolist()
        out["analyse"].append(e)
    out["sek"] = time.time() - t_wand
    with open(pfad + ".tmp", "w") as fh:
        json.dump(out, fh, indent=1)
    os.replace(pfad + ".tmp", pfad)
    print(f"zeit2d fertig: arm {arm}, w2 {w2}, dr {dr}, T {T}, {out['sek']:.1f} s", flush=True)


if __name__ == "__main__":
    main()
