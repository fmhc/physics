#!/usr/bin/env python3
"""WAND-BETA, nachtraegliche Gegenprobe 2 (Leitung, 03.10.2026, nach den Laeufen; aendert keine Urteile).
Nullstelle der komplexen Transmissionsamplitude t(f) des Randwertproblems per Sekantenverfahren (reelles f,
komplexe Werte). Die Phase ist auf beide Gebietsenden bezogen; in kleinen Fenstern ist t(f) nahezu linear.
Aufruf: python fd_sekante.py <beta> <f_start> <h> <aus.json>
"""
import json
import math
import os
import sys
import time

import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import spsolve

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wand_beta as wb  # noqa: E402


def t_komplex(mod, f, h):
    q, ko = wb.aussen_raten(mod, f)
    k, e1, kap, e2 = wb.innen_moden(mod, f)
    N = int(round((mod.xb_fd - mod.xa_fd) / h))
    x = mod.xa_fd + h * np.arange(N + 1)
    p11, p12, p22 = mod.P_vek(x, f)
    th = math.acos(1.0 - 0.5 * h * h * k * k)
    eta_k = math.acosh(1.0 + 0.5 * h * h * kap * kap)
    th_o = math.acos(1.0 - 0.5 * h * h * ko * ko)
    eta_q = math.acosh(1.0 + 0.5 * h * h * q * q)
    n = 2 * (N + 1)
    rows, cols, vals = [], [], []
    j = np.arange(1, N)
    ih2 = 1.0 / (h * h)
    for c, (pcc, pco) in enumerate(((p11, p12), (p22, p12))):
        r = 2 * j + c
        rows += [r, r, r, r]
        cols += [2 * (j - 1) + c, 2 * j + c, 2 * j + (1 - c), 2 * (j + 1) + c]
        vals += [np.full(j.size, ih2), -2.0 * ih2 - pcc[j], -pco[j], np.full(j.size, ih2)]
    rows = np.concatenate(rows)
    cols = np.concatenate(cols)
    vals = np.concatenate(vals).astype(complex)
    br, bc, bv = [], [], []
    rhs = np.zeros(n, dtype=complex)
    for cc in (0, 1):
        br += [0, 0]
        bc += [2 + cc, cc]
        bv += [e2[cc], -math.exp(eta_k) * e2[cc]]
    for cc in (0, 1):
        br += [1, 1]
        bc += [2 + cc, cc]
        bv += [e1[cc], -complex(math.cos(th), -math.sin(th)) * e1[cc]]
    rhs[1] = 2j * math.sin(th)
    br += [2 * N, 2 * N]
    bc += [2 * N, 2 * (N - 1)]
    bv += [1.0, -math.exp(-eta_q)]
    br += [2 * N + 1, 2 * N + 1]
    bc += [2 * N + 1, 2 * (N - 1) + 1]
    bv += [1.0, -complex(math.cos(th_o), math.sin(th_o))]
    A = sp.csc_matrix((np.concatenate([vals, np.array(bv, dtype=complex)]),
                       (np.concatenate([rows, np.array(br)]), np.concatenate([cols, np.array(bc)]))), shape=(n, n))
    Y = spsolve(A, rhs)
    # Phasenbezug: einlaufende Welle bei j = 0, auslaufende bei j = N
    return complex(Y[2 * N + 1] * np.exp(-1j * th_o * N)) * math.sqrt(math.sin(th_o) / math.sin(th))


def main():
    beta, f0, h, pfad = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
    mod = wb.MB(beta)
    t0 = time.time()
    f1, f2 = f0 - 1e-6, f0 + 1e-6
    t1, t2 = t_komplex(mod, f1, h), t_komplex(mod, f2, h)
    verlauf = [{"f": f1, "t": [t1.real, t1.imag]}, {"f": f2, "t": [t2.real, t2.imag]}]
    for _ in range(12):
        fn = f2 - (t2 * (f2 - f1) / (t2 - t1)).real
        tn = t_komplex(mod, fn, h)
        verlauf.append({"f": fn, "t": [tn.real, tn.imag]})
        f1, t1, f2, t2 = f2, t2, fn, tn
        if abs(f2 - f1) < 1e-14:
            break
    out = {"beta": beta, "f_start": f0, "h": h, "f_null": f2, "abs_t2": abs(t2) ** 2, "abstand_zum_start": f2 - f0,
           "verlauf": verlauf, "sek": time.time() - t0}
    with open(pfad + ".tmp", "w") as fh:
        json.dump(out, fh)
    os.replace(pfad + ".tmp", pfad)
    print(f"beta {beta} h {h}: Nullstelle {f2:.12f}, |t|^2 = {abs(t2) ** 2:.3e}, Abstand {f2 - f0:+.3e}, "
          f"{out['sek']:.1f} s", flush=True)


if __name__ == "__main__":
    main()
