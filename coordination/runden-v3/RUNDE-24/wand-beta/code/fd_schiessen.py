#!/usr/bin/env python3
"""WAND-BETA, nachtraegliche Gegenprobe 3 (Leitung, 03.10.2026, nach den Laeufen; aendert keine Urteile).
Diskretes Schiessen im Randwertmodell: Die 3-Punkt-Rekursion Y_{j-1} = (2 + h^2 P_j) Y_j - Y_{j+1} laeuft von aussen
(rein abklingend im geschlossenen Kanal, offener Kanal null) nach innen. Gemessen wird der Koeffizient der ins Innere
wachsenden diskreten Mode. Seine Nullstellen sind die exakten Transmissionsnullstellen des diskreten Modells. Sie haengen
nicht von der Breite des Fano-Einbruchs ab, anders als die Minimierung von T.
Aufruf: python fd_schiessen.py <beta> <f_mitte> <halbbreite> <n> <h> <aus.json>
"""
import json
import math
import os
import sys
import time

import numpy as np
from scipy.optimize import brentq

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wand_beta as wb  # noqa: E402


class Diskret:
    def __init__(self, mod, h):
        self.mod, self.h = mod, h
        N = int(round((mod.xb_fd - mod.xa_fd) / h))
        self.N = N
        x = mod.xa_fd + h * np.arange(N + 1)
        W, C = mod.koeff(x)
        self.W = [float(v) for v in W]
        self.C = [float(v) for v in C]

    def koeffizient(self, f):
        mod, h, N = self.mod, self.h, self.N
        q, _ = wb.aussen_raten(mod, f)
        k, e1, kap, e2 = wb.innen_moden(mod, f)
        eta_q = math.acosh(1.0 + 0.5 * h * h * q * q)
        eta_k = math.acosh(1.0 + 0.5 * h * h * kap * kap)
        am, ap = (f - mod.OM) ** 2, (f + mod.OM) ** 2
        h2 = h * h
        a1, b1 = math.exp(-eta_q), 0.0         # Y_{N+1}
        a0, b0 = 1.0, 0.0                       # Y_N
        W, C = self.W, self.C
        for j in range(N, 0, -1):
            w, c = W[j], C[j]
            an = (2.0 + h2 * (w - am)) * a0 + h2 * c * b0 - a1
            bn = h2 * c * a0 + (2.0 + h2 * (w - ap)) * b0 - b1
            a1, b1, a0, b0 = a0, b0, an, bn
            if abs(a0) > 1e250 or abs(b0) > 1e250:   # gemeinsame Skalierung, aendert keine Nullstelle
                a0, b0, a1, b1 = a0 * 1e-200, b0 * 1e-200, a1 * 1e-200, b1 * 1e-200
        # jetzt (a0, b0) = Y_0, (a1, b1) = Y_1; abklingende Richtung e2: y_e,j = A z^j + B z^-j mit z = exp(eta_k)
        ye0 = e2[0] * a0 + e2[1] * b0
        ye1 = e2[0] * a1 + e2[1] * b1
        z = math.exp(eta_k)
        B = (ye1 - z * ye0) / (1.0 / z - z)    # Koeffizient der ins Innere wachsenden Mode (z^-j)
        nrm = math.hypot(a0, b0) + math.hypot(a1, b1)
        return B / nrm


def main():
    beta, fm, hb, n, h, pfad = (float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]),
                                float(sys.argv[5]), sys.argv[6])
    mod = wb.MB(beta)
    d = Diskret(mod, h)
    t0 = time.time()
    fs = np.linspace(fm - hb, fm + hb, n)
    vals = [d.koeffizient(float(f)) for f in fs]
    null = []
    for i in range(n - 1):
        if vals[i] == 0.0 or vals[i] * vals[i + 1] < 0.0:
            null.append(brentq(d.koeffizient, float(fs[i]), float(fs[i + 1]), xtol=1e-15, rtol=1e-15, maxiter=200))
    out = {"beta": beta, "f_mitte": fm, "halbbreite": hb, "n": n, "h": h, "nullstellen": null,
           "abstaende_zur_mitte": [z - fm for z in null], "werte": [float(v) for v in vals],
           "f": [float(v) for v in fs], "sek": time.time() - t0}
    with open(pfad + ".tmp", "w") as fh:
        json.dump(out, fh)
    os.replace(pfad + ".tmp", pfad)
    print(f"beta {beta} h {h}: Nullstellen {['%.12f' % z for z in null]}, Abstaende "
          f"{['%+.2e' % (z - fm) for z in null]}, {out['sek']:.1f} s", flush=True)


if __name__ == "__main__":
    main()
