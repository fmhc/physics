"""SCHACHBRETT-KAUSAL-1: Kontinuumsloesung der Dirac-Pakete und dieselbe Messung wie auf der Kausalmenge.

Dirac-Operator D = d_t + alpha d_x + i m beta (alpha = diag(1, -1), beta = [[0, 1], [1, 0]]), Komponenten (R, L).
D D'' = Box + m^2 mit D'' = d_t - alpha d_x - i m beta [M]; also S = D'' G, G = retardierter KG-Propagator (1/2) J0(m tau)
[S: Johnston 0806.3083 (3.23)]. Fuer j_a = c_a g(t, x), g = exp(-(t^2+x^2)/(2 s^2)) exp(-i(om t - p x)):
psi_R = c_R (d_t - d_x) phi - i m c_L phi,  psi_L = c_L (d_t + d_x) phi - i m c_R phi,  phi = G * g (skalar).
Je Fourier-Mode (wie KAUSAL-WELLE-1 kontinuum.py, Duhamel exakt mit Faddeeva):
  phi_k = h/(2 i w) [e^{iwt} I(t; om+w) - e^{-iwt} I(t; om-w)],  phi_k' = (h/2) [e^{iwt} I(t; om+w) + e^{-iwt} I(t; om-w)].
Gegenprobe an den Pruefpunkten: direkte Faltung mit dem analytischen Dirac-Propagator (delta-Teil als Strahlintegral,
glatte Teile -(m^2/4) dV (2 J1(z)/z), -(i m/2) J0(z), z = m sqrt(dU dV)) per Gauss-Legendre.

Aufruf (nur ueber kleintest.sh): kontinuum_dirac.py <ausgabeordner>
"""
import hashlib
import json
import os
import sys
import time

import numpy as np
from scipy.special import j0, j1

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kausal_dirac as kd  # noqa: E402

SKRIPT_SHA = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
M = kd.M
L_PER = 800.0
K_BREITE = 9.0
NT_FEIN = 10
DX_FEIN = 0.1


def kgitter(s, p):
    dk = 2 * np.pi / L_PER
    n = int(np.ceil(K_BREITE / s / dk))
    return p + dk * np.arange(-n, n + 1), dk


def psi_k(t, k, P):
    """t: (nt, 1), k: (1, nk) -> (psi_R,k, psi_L,k), je (nt, nk)."""
    s, om, p = P["sigma"], P["omega"], P["p"]
    wk = np.sqrt(k ** 2 + M ** 2)
    h = s * np.sqrt(2 * np.pi) * np.exp(-s * s * (k - p) ** 2 / 2.0)
    e = np.exp(1j * wk * t)
    Ip = kd.I_int(t, om + wk, s)
    Im = kd.I_int(t, om - wk, s)
    ph = h / (2j * wk) * (e * Ip - Im / e)
    dph = 0.5 * h * (e * Ip + Im / e)
    pR = P["cR"] * (dph - 1j * k * ph) - 1j * M * P["cL"] * ph
    pL = P["cL"] * (dph + 1j * k * ph) - 1j * M * P["cR"] * ph
    return pR, pL


def feld_punkte(t, x, P):
    k, dk = kgitter(P["sigma"], P["p"])
    out = np.zeros((t.size, 2), dtype=np.complex128)
    for i in range(t.size):
        pR, pL = psi_k(np.array([[t[i]]]), k[None, :], P)
        ex = np.exp(1j * k * x[i])
        out[i, 0] = (dk / (2 * np.pi)) * np.sum(ex * pR[0])
        out[i, 1] = (dk / (2 * np.pi)) * np.sum(ex * pL[0])
    return out


def quadratur(tt, xx, P, n=700):
    """Direkte Faltung psi = S * j mit dem analytischen retardierten Dirac-Propagator."""
    s, om, p = P["sigma"], P["omega"], P["p"]

    def g(T, X):
        return np.exp(-(T * T + X * X) / (2 * s * s) - 1j * (om * T - p * X))
    Ux, Vx = tt - xx, tt + xx
    lo = -12.0 * s
    gg, wg = np.polynomial.legendre.leggauss(n)
    # delta-Teile: int_0^inf j_R(t - s', x - s') ds' und int_0^inf j_L(t - s', x + s') ds'
    smax = tt + 12.0 * s
    sv = 0.5 * smax * (gg + 1.0)
    sw = 0.5 * smax * wg
    dR = np.sum(sw * g(tt - sv, xx - sv))
    dL = np.sum(sw * g(tt - sv, xx + sv))
    # glatte Teile ueber die Vergangenheit (U < Ux, V < Vx), dt dx = dU dV / 2
    uu = 0.5 * (Ux - lo) * gg + 0.5 * (Ux + lo)
    wu = 0.5 * (Ux - lo) * wg
    vv = 0.5 * (Vx - lo) * gg + 0.5 * (Vx + lo)
    wv = 0.5 * (Vx - lo) * wg
    UU, VV = np.meshgrid(uu, vv, indexing="ij")
    dU = Ux - UU
    dV = Vx - VV
    z = M * np.sqrt(np.maximum(dU * dV, 0.0))
    with np.errstate(all="ignore"):
        q = np.where(z > 1e-8, 2.0 * j1(z) / np.where(z > 1e-8, z, 1.0), 1.0)
    G0 = j0(z)
    J = g((UU + VV) / 2, (VV - UU) / 2)
    srr = -(M * M / 4.0) * dV * q
    sll = -(M * M / 4.0) * dU * q
    soff = -0.5j * M * G0
    A = 0.5 * wu[:, None] * wv[None, :]
    psiR = P["cR"] * (dR + np.sum(A * srr * J)) + P["cL"] * np.sum(A * soff * J)
    psiL = P["cL"] * (dL + np.sum(A * sll * J)) + P["cR"] * np.sum(A * soff * J)
    return np.array([psiR, psiL])


def main():
    ordner = sys.argv[1]
    os.makedirs(ordner, exist_ok=True)
    t00 = time.time()
    nq = 5
    bins = np.zeros((kd.NP, kd.N_SCHEIBEN, kd.XB_N, nq))
    pp = kd.pruefpunkte_paket()
    psi_p = np.zeros((kd.NP, pp.shape[1], 2), dtype=np.complex128)
    quad = np.zeros((kd.NP, 3, 2), dtype=np.complex128)
    info = []
    dfein = kd.XB_MIN + DX_FEIN * (np.arange(int(kd.XB_N / DX_FEIN)) + 0.5)
    nsub = int(round(1.0 / DX_FEIN))
    for c, P in enumerate(kd.PAKETE):
        tc = time.time()
        k, dk = kgitter(P["sigma"], P["p"])
        dtf = kd.W_SCHEIBE / NT_FEIN
        tf = kd.TA[c] + dtf * (np.arange(kd.N_SCHEIBEN * NT_FEIN) + 0.5)
        pR, pL = psi_k(tf[:, None], k[None, :], P)
        sh = np.exp(1j * k[None, :] * (kd.VX[c] * tf[:, None]))
        E = np.exp(1j * dfein[:, None] * k[None, :])
        FR = (dk / (2 * np.pi)) * (E @ (pR * sh).T)
        FL = (dk / (2 * np.pi)) * (E @ (pL * sh).T)
        wR = FR.real ** 2 + FR.imag ** 2
        wL = FL.real ** 2 + FL.imag ** 2
        X = kd.VX[c] * tf[None, :] + dfein[:, None]
        dA = dtf * DX_FEIN
        for qi, Gq in enumerate([wR, wL, X * (wR + wL), X * X * (wR + wL), np.ones_like(wR)]):
            acc = (Gq * dA).reshape(kd.XB_N, nsub, kd.N_SCHEIBEN, NT_FEIN).sum(axis=(1, 3))
            bins[c, :, :, qi] = acc.T
        psi_p[c] = feld_punkte(pp[c, :, 0], pp[c, :, 1], P)
        for i in range(3):
            quad[c, i] = quadratur(pp[c, i, 0], pp[c, i, 1], P)
        w = wR + wL
        info.append({"paket": P["name"], "nk": int(k.size), "dk": dk, "zeit_s": round(time.time() - tc, 2),
                     "norm_rand_anteil": float((w[:20].sum() + w[-20:].sum()) / w.sum()),
                     "quad_gegen_k_rel": [float(np.max(np.abs(quad[c, i] - psi_p[c, i])) / np.max(np.abs(psi_p[c, i])))
                                          for i in range(3)]})
        print(json.dumps(info[-1]), flush=True)
    np.savez_compressed(os.path.join(ordner, "kontinuum.npz"), bins=bins, psi_p=psi_p, quad=quad, pruefpunkte=pp)
    kopf = {"modus": "kontinuum", "info": info, "zeit_gesamt_s": round(time.time() - t00, 2), "skript_sha256": SKRIPT_SHA,
            "kausal_dirac_sha256": kd.SKRIPT_SHA, "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    with open(os.path.join(ordner, "kontinuum.json"), "w") as fh:
        json.dump(kopf, fh, indent=1)
    print(json.dumps({"zeit_gesamt_s": kopf["zeit_gesamt_s"]}))


if __name__ == "__main__":
    main()
