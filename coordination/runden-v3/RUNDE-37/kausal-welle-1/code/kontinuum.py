"""KAUSAL-WELLE-1: Kontinuumsloesung fuer die sechs Quellen und dieselbe Messung wie auf der Kausalmenge.

(Box + m^2) phi = J, Box = d_t^2 - d_x^2 [S: Johnston (3.17), (3.18)], retardiert. Je Fourier-Mode e^{ikx}:
phi_k'' + w_k^2 phi_k = J_k(t), phi_k(t) = int_{-inf}^t sin(w_k (t - t'))/w_k J_k(t') dt' (Duhamel), w_k = sqrt(k^2 + m^2).
Quelle J = exp(-(t^2 + x^2)/(2 s^2)) exp(-i(om t - p x)) (ungekappt), J_k(t) = g(t) e^{-i om t} h^(k - p),
h^(q) = s sqrt(2 pi) exp(-s^2 q^2/2). Daraus [M, eigene Rechnung]:
phi_k(t) = h^(k - p)/(2 i w_k) [e^{i w_k t} I(t; om + w_k) - e^{-i w_k t} I(t; om - w_k)],
I(t; W) = int_{-inf}^t exp(-t'^2/(2 s^2) - i W t') dt' = s sqrt(pi/2) exp(-t^2/(2 s^2) - i W t) w((W s^2 - i t)/(s sqrt2))
(t <= 0; Faddeeva w), fuer t > 0 ueber I(inf) - int_t^inf.
Gegenprobe an den Pruefpunkten: direkte Gauss-Legendre-Quadratur der Faltung mit (1/2) J0(m tau) [S: (3.23)] ueber die
gekappte Quelle (r <= 4,5 s), in Lichtkegelkoordinaten (Vergangenheitskegel = Rechteck).

Aufruf (nur ueber kleintest.sh): kontinuum.py <ausgabeordner>
"""
import hashlib
import json
import os
import sys
import time

import numpy as np
from scipy.special import j0, wofz

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kausal_welle as kw  # noqa: E402

SKRIPT_SHA = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
SQ2 = np.sqrt(2.0)
L_PER = 800.0
K_BREITE = 9.0
NT_FEIN = 10
DX_FEIN = 0.1


def I_int(t, W, s):
    t = np.asarray(t, dtype=float)
    W = np.asarray(W, dtype=float)
    with np.errstate(all="ignore"):
        pre = s * np.sqrt(np.pi / 2.0) * np.exp(-t ** 2 / (2 * s * s) - 1j * W * t)
        a = pre * wofz((W * s * s - 1j * t) / (s * SQ2))
        b = s * np.sqrt(2 * np.pi) * np.exp(-W ** 2 * s * s / 2.0) - pre * wofz((1j * t - W * s * s) / (s * SQ2))
    return np.where(t <= 0, a, b)


def phi_k(t, k, s, om, p):
    """t: (nt, 1), k: (1, nk) -> (nt, nk)."""
    wk = np.sqrt(k ** 2 + kw.MASSE ** 2)
    h = s * np.sqrt(2 * np.pi) * np.exp(-s * s * (k - p) ** 2 / 2.0)
    return h / (2j * wk) * (np.exp(1j * wk * t) * I_int(t, om + wk, s) - np.exp(-1j * wk * t) * I_int(t, om - wk, s))


def kgitter(s, p):
    dk = 2 * np.pi / L_PER
    n = int(np.ceil(K_BREITE / s / dk))
    return p + dk * np.arange(-n, n + 1), dk


def feld_punkte(t, x, s, om, p):
    """phi an einzelnen Punkten (t, x) (gleich lange Felder)."""
    k, dk = kgitter(s, p)
    out = np.zeros(t.size, dtype=np.complex128)
    for i in range(t.size):
        f = phi_k(np.array([[t[i]]]), k[None, :], s, om, p)[0]
        out[i] = (dk / (2 * np.pi)) * np.sum(np.exp(1j * k * x[i]) * f)
    return out


def quadratur(tt, xx, s, om, p, r0, n=500):
    """Faltung (1/2) J0(m tau) * J_gekappt am Punkt (tt, xx), Gauss-Legendre in (u', v')."""
    ut, vt = (tt - xx) / SQ2, (tt + xx) / SQ2
    g, wg = np.polynomial.legendre.leggauss(n)
    ua, ub = -r0, min(ut, r0)
    va, vb = -r0, min(vt, r0)
    uu = 0.5 * (ub - ua) * g + 0.5 * (ub + ua)
    vv = 0.5 * (vb - va) * g + 0.5 * (vb + va)
    wu = 0.5 * (ub - ua) * wg
    wv = 0.5 * (vb - va) * wg
    U, V = np.meshgrid(uu, vv, indexing="ij")
    T = (U + V) / SQ2
    X = (V - U) / SQ2
    r2 = T * T + X * X
    J = np.exp(-r2 / (2 * s * s) - 1j * (om * T - p * X)) * (r2 <= r0 * r0)
    tau = np.sqrt(np.maximum(2 * (ut - U) * (vt - V), 0.0))
    G = 0.5 * j0(kw.MASSE * tau)
    return complex(np.einsum("i,ij,j->", wu, G * J, wv))


def main():
    ordner = sys.argv[1]
    os.makedirs(ordner, exist_ok=True)
    t00 = time.time()
    nq = 7
    bins = np.zeros((kw.NC, kw.N_SCHEIBEN, kw.XB_N, nq))
    pp = kw.pruefpunkte()
    phi_p = np.zeros((kw.NC, pp.shape[1]), dtype=np.complex128)
    quad = np.zeros((kw.NC, 3), dtype=np.complex128)
    vbar = np.zeros(kw.NC)
    info = []
    dfein = kw.XB_MIN + DX_FEIN * (np.arange(int(kw.XB_N / DX_FEIN)) + 0.5)
    jbin = np.floor(dfein).astype(int) - kw.XB_MIN
    for c, (s, e) in enumerate(kw.CONFIGS):
        tc = time.time()
        om, p = np.cosh(e), np.sinh(e)
        k, dk = kgitter(s, p)
        # feines Zeitgitter: je Scheibe NT_FEIN Mittelpunkte
        dtf = kw.W_SCHEIBE / NT_FEIN
        tf = kw.TA[c] + dtf * (np.arange(kw.N_SCHEIBEN * NT_FEIN) + 0.5)
        F = phi_k(tf[:, None], k[None, :], s, om, p)                 # (nt, nk)
        F = F * np.exp(1j * k[None, :] * (kw.VN[c] * tf[:, None]))   # Verschiebung um x_n(t)
        E = np.exp(1j * dfein[:, None] * k[None, :])                  # (nx, nk)
        PH = (dk / (2 * np.pi)) * (E @ F.T)                           # (nx, nt): phi(t, x_n(t) + d)
        w = (PH.real ** 2 + PH.imag ** 2)
        X = kw.VN[c] * tf[None, :] + dfein[:, None]
        T = np.broadcast_to(tf[None, :], w.shape)
        dA = dtf * DX_FEIN
        groessen = [w, X * w, T * w, X * X * w, w * w, X * w * w, X * X * w * w]
        nsub = int(round(1.0 / DX_FEIN))
        assert np.all(jbin.reshape(kw.XB_N, nsub) == np.arange(kw.XB_N)[:, None])
        for qi, Gq in enumerate(groessen):
            acc = (Gq * dA).reshape(kw.XB_N, nsub, kw.N_SCHEIBEN, NT_FEIN).sum(axis=(1, 3))
            bins[c, :, :, qi] = acc.T
        # Pruefpunkte und Profil
        phi_p[c] = feld_punkte(pp[c, :, 0], pp[c, :, 1], s, om, p)
        for i in range(3):
            quad[c, i] = quadratur(pp[c, i, 0], pp[c, i, 1], s, om, p, kw.R0C[c])
        # analytische Schwerpunktgeschwindigkeit des auslaufenden Pakets (positive Frequenz)
        wk = np.sqrt(k ** 2 + 1.0)
        A2 = (np.exp(-s * s * ((k - p) ** 2 + (om - wk) ** 2) / 2.0) / (2 * wk)) ** 2
        vbar[c] = float(np.sum(k / wk * A2) / np.sum(A2))
        info.append({"sigma": s, "eta": e, "nk": int(k.size), "dk": dk, "zeit_s": round(time.time() - tc, 2),
                     "norm_rand_anteil": float((w[:20].sum() + w[-20:].sum()) / w.sum())})
        print(json.dumps(info[-1]), flush=True)
    np.savez_compressed(os.path.join(ordner, "kontinuum.npz"), bins=bins, phi_p=phi_p, quad=quad, vbar=vbar,
                        pruefpunkte=pp)
    kopf = {"modus": "kontinuum", "info": info, "vbar": vbar.tolist(),
            "quad_gegen_k_rel": [float(abs(quad[c, i] - phi_p[c, i]) / abs(phi_p[c, i])) for c in range(kw.NC) for i in range(3)],
            "zeit_gesamt_s": round(time.time() - t00, 2), "skript_sha256": SKRIPT_SHA,
            "kausal_welle_sha256": kw.SKRIPT_SHA, "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    with open(os.path.join(ordner, "kontinuum.json"), "w") as fh:
        json.dump(kopf, fh, indent=1)
    print(json.dumps({k: kopf[k] for k in ("vbar", "quad_gegen_k_rel", "zeit_gesamt_s")}))


if __name__ == "__main__":
    main()
