"""SCHACHBRETT-KAUSAL-1 (Runde 38, Code-Agent): Kontrolle SK0, Feynmans Schachbrett auf dem regelmaessigen Lichtkegelgitter.

Konvention [M]: (d_t + d_x) psi_R = -i m psi_L, (d_t - d_x) psi_L = -i m psi_R; U = t - x, V = t + x.
Gitter: Knoten (i, j) bei U = 2 eps i, V = 2 eps j (Zeitschritt eps, Ortsschritt eps).
  psi_R(i, j+1) = psi_R(i, j) - i m eps psi_L(i, j)      (R-Schritt; Richtungswechsel L->R kostet -i m eps)
  psi_L(i+1, j) = psi_L(i, j) - i m eps psi_R(i, j)      (L-Schritt; Richtungswechsel R->L kostet -i m eps)
Start: am Ursprung als R-Laeufer, psi_R(0, 0) = 1. Dichte im Kontinuum: psi / (2 eps).
Kontinuum (retardiert, R-Quelle am Ursprung, innerhalb des Kegels, tau = sqrt(U V)) [M, Herleitung in PLAN.md]:
  S_LR = -(i m/2) J0(m tau),  S_RR (glatter Teil) = -(m/2) sqrt(V/U) J1(m tau)  (dazu delta(U) auf dem R-Strahl).
Pruefpunkte: tau in {0,5; 1; 2; 3; 5; 8; 12; 16}, Rapiditaet zeta in {-1; -0,5; 0; 0,5; 1}; Gitterwerte bilinear interpoliert.
Gegenprobe: geschlossene Binomialsummen (Pfadzaehlung) an Gitterknoten, eps = 0,05.

Aufruf (nur ueber kleintest.sh auf der .69): schachbrett.py <ausgabeordner>
"""
import hashlib
import json
import math
import os
import sys
import time

import numpy as np
from scipy.special import j0, j1

SKRIPT_SHA = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
M = 1.0
TAUS = np.array([0.5, 1.0, 2.0, 3.0, 5.0, 8.0, 12.0, 16.0])
ZETAS = np.array([-1.0, -0.5, 0.0, 0.5, 1.0])
EPS = [0.02, 0.01, 0.005, 0.0025]


def kontinuum_punkte():
    """(nz, nt) Felder S_RR (glatt), S_LR an den Pruefpunkten."""
    tau = TAUS[None, :] * np.ones((ZETAS.size, 1))
    z = ZETAS[:, None] * np.ones((1, TAUS.size))
    srr = -(M / 2.0) * np.exp(z) * j1(M * tau)
    slr = -0.5j * M * j0(M * tau)
    return srr.astype(np.complex128), slr


def gitter(eps):
    """Gitterwerte psi/(2 eps) an den Pruefpunkten, bilinear in (i, j)."""
    U = TAUS[None, :] * np.exp(-ZETAS[:, None])
    V = TAUS[None, :] * np.exp(ZETAS[:, None])
    fi = U / (2 * eps)
    fj = V / (2 * eps)
    i0 = np.floor(fi).astype(int)
    j0_ = np.floor(fj).astype(int)
    imax = int(i0.max()) + 2
    jmax = int(j0_.max()) + 2
    brauche = set(i0.ravel().tolist()) | set((i0 + 1).ravel().tolist())
    zeilen = {}
    psiL = np.zeros(jmax + 1, dtype=np.complex128)
    c = -1j * M * eps
    for i in range(imax + 1):
        if i == 0:
            R = np.ones(jmax + 1, dtype=np.complex128)
        else:
            R = np.empty(jmax + 1, dtype=np.complex128)
            R[0] = 0.0
            np.cumsum(c * psiL[:-1], out=R[1:])
        if i in brauche:
            zeilen[i] = (R.copy(), psiL.copy())
        psiL = psiL + c * R
    srr = np.zeros(U.shape, dtype=np.complex128)
    slr = np.zeros(U.shape, dtype=np.complex128)
    for a in range(U.shape[0]):
        for b in range(U.shape[1]):
            ii, jj = i0[a, b], j0_[a, b]
            di, dj = fi[a, b] - ii, fj[a, b] - jj
            w = [(ii, jj, (1 - di) * (1 - dj)), (ii + 1, jj, di * (1 - dj)), (ii, jj + 1, (1 - di) * dj),
                 (ii + 1, jj + 1, di * dj)]
            srr[a, b] = sum(ww * zeilen[x][0][y] for x, y, ww in w) / (2 * eps)
            slr[a, b] = sum(ww * zeilen[x][1][y] for x, y, ww in w) / (2 * eps)
    return srr, slr


def binom_probe(eps=0.05):
    """Geschlossene Pfadzaehlung gegen die Rekursion an einigen Gitterknoten (exakte ganze Binomialzahlen)."""
    a = -(M * eps) ** 2
    knoten = [(1, 1), (3, 7), (10, 4), (20, 20), (40, 15), (15, 45)]
    imax = max(k[0] for k in knoten) + 1
    jmax = max(k[1] for k in knoten) + 1
    psiL = np.zeros(jmax + 1, dtype=np.complex128)
    c = -1j * M * eps
    rek = {}
    for i in range(imax + 1):
        if i == 0:
            R = np.ones(jmax + 1, dtype=np.complex128)
        else:
            R = np.empty(jmax + 1, dtype=np.complex128)
            R[0] = 0.0
            np.cumsum(c * psiL[:-1], out=R[1:])
        for (ki, kj) in knoten:
            if ki == i:
                rek[(ki, kj)] = (complex(R[kj]), complex(psiL[kj]))
        psiL = psiL + c * R
    out = []
    for (i, j) in knoten:
        # psi_L(i, j) = -i m eps sum_k C(j, k) C(i-1, k) (-m^2 eps^2)^k ; psi_R(i, j) = sum_{k>=1} C(j, k) C(i-1, k-1) (-m^2 eps^2)^k
        sl = sum(math.comb(j, k) * math.comb(i - 1, k) * a ** k for k in range(0, min(j, i - 1) + 1))
        sl = -1j * M * eps * sl
        sr = sum(math.comb(j, k) * math.comb(i - 1, k - 1) * a ** k for k in range(1, min(j, i) + 1))
        r = rek[(i, j)]
        out.append({"knoten": [i, j], "abw_R": abs(r[0] - sr) / max(abs(sr), 1e-300),
                    "abw_L": abs(r[1] - sl) / max(abs(sl), 1e-300)})
    return out


def main():
    ordner = sys.argv[1]
    os.makedirs(ordner, exist_ok=True)
    t0 = time.time()
    krr, klr = kontinuum_punkte()
    res = {"eps": EPS, "taus": TAUS.tolist(), "zetas": ZETAS.tolist(),
           "kontinuum_RR": {"re": krr.real.tolist(), "im": krr.imag.tolist()},
           "kontinuum_LR": {"re": klr.real.tolist(), "im": klr.imag.tolist()},
           "gitter": {}}
    for eps in EPS:
        te = time.time()
        grr, glr = gitter(eps)
        drr = np.abs(grr - krr)
        dlr = np.abs(glr - klr)
        res["gitter"][str(eps)] = {"RR_re": grr.real.tolist(), "RR_im": grr.imag.tolist(), "LR_re": glr.real.tolist(),
                                   "LR_im": glr.imag.tolist(), "abw_RR": drr.tolist(), "abw_LR": dlr.tolist(),
                                   "E_max": float(max(drr.max(), dlr.max())), "zeit_s": round(time.time() - te, 2)}
        print(json.dumps({"eps": eps, "E_max": res["gitter"][str(eps)]["E_max"], "zeit_s": round(time.time() - te, 2)}),
              flush=True)
    res["binom_probe"] = binom_probe()
    res["skript_sha256"] = SKRIPT_SHA
    res["zeit_gesamt_s"] = round(time.time() - t0, 2)
    res["zeit_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    with open(os.path.join(ordner, "schachbrett.json"), "w") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps({"binom_probe_max": max(max(b["abw_R"], b["abw_L"]) for b in res["binom_probe"]),
                      "zeit_gesamt_s": res["zeit_gesamt_s"]}))


if __name__ == "__main__":
    main()
