#!/usr/bin/env python3
# ZZZ-ABGLEICH Zusatz (Runde 22): Kopfrechnungen aus ARBEITSFELD.md nachrechnen.
# (1) ZZZ Gl. (14) f_max^2, f_z^2 an unseren Leiterstellen (g = beta = 1/2) gegen S0.
# (2) Existenzbedingungen ZZZ Gl. (8), (14)-(16) fuer die g = 1/2-Felder ihrer Abb. 2.
# (3) Abb.-3-Parameter (omega_Q = 0,52, f0 = 1,2, g = 1/3): Nullstelle von -rho_2(omega), Schwelle 1 + omega_Q,
#     sigma_+- und pi/sigma_+- bei einigen omega.
# Nur Standardbibliothek.
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_v] = "1"
import json
import math
import sys


def fpunkte(g, wq2):
    """ZZZ Gl. (14): f_min^2, f_z^2, f_max^2 (None, wenn die Wurzel negativ ist)."""
    a = 1.0 - 3.0 * g * (1.0 - wq2)
    b = 1.0 - 4.0 * g * (1.0 - wq2)
    fmin2 = (1.0 - math.sqrt(a)) / (3.0 * g) if a >= 0 else None
    fmax2 = (1.0 + math.sqrt(a)) / (3.0 * g) if a >= 0 else None
    fz2 = (1.0 - math.sqrt(b)) / (2.0 * g) if b >= 0 else None
    return fmin2, fz2, fmax2


def m2(wq, w, f0, g):
    f2 = f0 * f0
    U = -4.0 * f2 + 9.0 * g * f2 * f2
    W = -2.0 * f2 + 6.0 * g * f2 * f2
    wurzel = math.sqrt(W * W + 4.0 * wq * wq * w * w)
    return wq * wq + w * w + wurzel - (1.0 + U), wq * wq + w * w - wurzel - (1.0 + U)


def main():
    ein = json.load(open(sys.argv[1] if len(sys.argv) > 1 else "eingabe.json"))
    g = ein["beta"]
    print("=== (1) S0 gegen ZZZ f_max^2 (g = 1/2)")
    for gruppe in ("d3_h002", "d2"):
        for sp in ein[gruppe]:
            x = sp["x"]
            # S0 an x_stern linear in u = 1/(x - 1/2) interpolieren (wie zzz_abgleich.py)
            t = [1.0 / (a - 0.5) for a in x]
            z = 1.0 / (sp["x_stern"] - 0.5)
            pa = sorted(zip(t, sp["S0"]))
            s0 = None
            for (t0, y0), (t1, y1) in zip(pa[:-1], pa[1:]):
                if t0 <= z <= t1:
                    s0 = y0 + (y1 - y0) * (z - t0) / (t1 - t0)
            fmin2, fz2, fmax2 = fpunkte(g, sp["x_stern"])
            print(f"  {gruppe} n={sp['n']:2d} omega^2={sp['x_stern']:.7f} S0={s0:.6f} f_max^2={fmax2:.6f} "
                  f"S0-f_max^2={s0 - fmax2:+.2e} f_z^2={fz2:.6f}")
    print("=== (2) Abb. 2, g = 1/2: omega_Q,min und f-Bereich")
    print(f"  omega_Q,min (Gl. 8) = {math.sqrt(1.0 - 1.0 / (4.0 * 0.5)):.5f}")
    for wq in (0.55, 0.65, 0.75):
        fmin2, fz2, fmax2 = fpunkte(0.5, wq * wq)
        gmax = 1.0 / (4.0 * (1.0 - wq * wq))
        print(f"  omega_Q={wq}: g_max (Gl. 16) = {gmax:.4f}; f_z={math.sqrt(fz2) if fz2 is not None else None}; "
              f"f_max={math.sqrt(fmax2) if fmax2 is not None else None}")
    print("=== (3) Abb.-3-Parameter omega_Q = 0,52, f0 = 1,2, g = 1/3")
    wq, f0, g3 = 0.52, 1.2, 1.0 / 3.0
    fmin2, fz2, fmax2 = fpunkte(g3, wq * wq)
    print(f"  f_z = {math.sqrt(fz2):.5f}, f_max = {math.sqrt(fmax2):.5f}; Schwelle 1 + omega_Q = {1 + wq:.4f}")
    lo, hi = 1.0 + wq, 4.0
    print(f"  -rho_2 an der Schwelle: {m2(wq, lo, f0, g3)[1]:+.5f}; bei 4: {m2(wq, hi, f0, g3)[1]:+.5f}")
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if m2(wq, mid, f0, g3)[1] < 0:
            lo = mid
        else:
            hi = mid
    print(f"  -rho_2 = 0 bei omega = {0.5 * (lo + hi):.6f}")
    for w in (1.6, 1.8, 2.0, 2.5, 3.0, 3.5):
        a, b = m2(wq, w, f0, g3)
        k1 = math.sqrt(a)
        if b > 0:
            k2 = math.sqrt(b)
            print(f"  omega={w}: -rho1={a:.4f} -rho2={b:+.4f} k1={k1:.4f} k2={k2:.4f} sigma+={k1 + k2:.4f} sigma-={k1 - k2:.4f} "
                  f"pi/sigma+={math.pi / (k1 + k2):.4f} pi/sigma-={math.pi / (k1 - k2):.4f} pi/k1={math.pi / k1:.4f} "
                  f"(gross-omega: pi/(2 omega)={math.pi / (2 * w):.4f}, pi/(2 omega_Q)={math.pi / (2 * wq):.4f})")
        else:
            print(f"  omega={w}: -rho1={a:.4f} -rho2={b:+.4f} k1={k1:.4f} kappa2={math.sqrt(-b):.4f} (Regime II) "
                  f"pi/k1={math.pi / k1:.4f}")


if __name__ == "__main__":
    main()
