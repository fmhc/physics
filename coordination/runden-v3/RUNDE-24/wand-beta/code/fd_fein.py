#!/usr/bin/env python3
"""WAND-BETA, nachtraegliche Gegenprobe (Leitung, 03.10.2026, nach den Laeufen; aendert keine Urteile).
Feinabtastung von T_fd (Randwertproblem) um die geschossene Nullstelle, um sehr schmale Fano-Einbrueche zu finden,
die der beschraenkte Minimierer ueber +-4e-4 nicht trifft.
Aufruf: python fd_fein.py <beta> <f_z> <halbbreite> <n> <h> <aus.json>
"""
import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wand_beta as wb  # noqa: E402


def main():
    beta, fz, hb, n, h, pfad = (float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]),
                                float(sys.argv[5]), sys.argv[6])
    mod = wb.MB(beta)
    t0 = time.time()
    fs = np.linspace(fz - hb, fz + hb, n)
    T = [wb.transmission_fd(mod, float(f), h)[0] for f in fs]
    i = int(np.argmin(T))
    out = {"beta": beta, "f_z_schiessen": fz, "halbbreite": hb, "n": n, "h": h,
           "f_min": float(fs[i]), "T_min": float(T[i]), "abstand_zum_schiessen": float(fs[i] - fz),
           "T_rand": [float(T[0]), float(T[-1])], "f": [float(x) for x in fs], "T": [float(x) for x in T],
           "sek": time.time() - t0}
    with open(pfad + ".tmp", "w") as fh:
        json.dump(out, fh)
    os.replace(pfad + ".tmp", pfad)
    print(f"beta {beta} h {h}: T_min {T[i]:.3e} bei {fs[i]:.12f} (Abstand {fs[i] - fz:+.2e}), "
          f"Rand {T[0]:.6f}/{T[-1]:.6f}, {out['sek']:.1f} s", flush=True)


if __name__ == "__main__":
    main()
