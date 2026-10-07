#!/usr/bin/env python3
"""HAGEDORN-1, Nachauswertung (nach dem Einfrieren geschrieben, rein beschreibend, kein Urteil haengt daran).

Fuer die angegebenen Zeilen je l = 0..12 alle ringlokalisierten reellen Eigenwerte beider Vorzeichen
(|Im| <= 1e-6, Ringanteil >= 0,6, 1e-3 < |Re| <= OMAX), auf demselben Basisgitter wie der Hauptlauf.
Negative Re Omega in Sektor l sind die positiven von Sektor -l (Spektrum -Omega*), also der gegenlaeufige Ast.

Aufruf: nachauswertung.py --profile lauf/profile/profile.npz --zeilen 2:0.55,... --out ORDNER
"""
import os

for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import argparse
import json
import math
import sys
import time

import numpy as np
import scipy.linalg as sla

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hagedorn as hg  # noqa: E402

OMAX = 0.6


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--profile", required=True)
    ap.add_argument("--zeilen", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--budget", type=float, default=540.0)
    args = ap.parse_args()
    t_start = time.perf_counter()
    dat = np.load(args.profile)
    with open(os.path.join(os.path.dirname(args.profile), "zeilen.json")) as fh:
        zrows = {(z["m"], hg.wkey(z["w2"])): z for z in json.load(fh)["zeilen"]}
    os.makedirs(args.out, exist_ok=True)
    for teil in args.zeilen.split(","):
        a, b = teil.split(":")
        m, w2 = int(a), float(b)
        pfad = os.path.join(args.out, f"aeste_m{m}_w{hg.wkey(w2)}.json")
        if os.path.exists(pfad):
            continue
        if time.perf_counter() - t_start > args.budget:
            print("Budget erschoepft vor", teil)
            break
        z = zrows[(m, hg.wkey(w2))]
        tab = (dat[f"f_{m}_{hg.wkey(w2)}"], dat[f"fp_{m}_{hg.wkey(w2)}"], float(dat[f"h_{m}_{hg.wkey(w2)}"][0]))
        kappa = math.sqrt(1.0 - w2)
        R_aus = float(z["R_aussen"])
        h = hg.H_BASIS[round(w2, 2)]
        prof = hg.gitter_profil(tab, m, w2, h, R_aus + hg.SCHWANZ / kappa)
        f, r, N, L = prof["f"], prof["r"], prof["N"], prof["L"]
        r_rand = R_aus + 0.75 * (L - R_aus)
        aeste = []
        for l in range(13):
            M, _A, _G = hg.bdg(f, m, l, w2, N, h)
            ev = sla.eigvals(M.toarray(), check_finite=False, overwrite_a=True)
            sel = np.nonzero((np.abs(ev.imag) <= hg.IM_STABIL) & (np.abs(ev.real) > 1e-3) &
                             (np.abs(ev.real) <= OMAX))[0]
            moden = []
            for i in sel[np.argsort(ev.real[sel])]:
                x = hg.eigvec(M, ev[i])
                ra, ri = hg.anteile(x, r, h, f, r_rand)
                if ri >= hg.RING_MIN and ra <= hg.RAND_MAX:
                    moden.append(dict(re=float(ev[i].real), ringanteil=ri))
            pos = [e["re"] for e in moden if e["re"] > 0]
            neg = [e["re"] for e in moden if e["re"] < 0]
            aeste.append(dict(l=l, moden=moden, kleinste_positive=min(pos) if pos else None,
                              groesste_negative=max(neg) if neg else None))
            print(f"m = {m}, w2 = {w2}, l = {l}: {len(moden)} Ringmoden; +: {min(pos) if pos else None}; "
                  f"-: {max(neg) if neg else None}", flush=True)
        hg.json_schreiben(pfad, dict(m=m, w2=w2, R_max=z["R_max"], N=N, h=h, L=L, omax=OMAX, aeste=aeste))
    print(f"Dauer {time.perf_counter() - t_start:.1f} s")


if __name__ == "__main__":
    main()
