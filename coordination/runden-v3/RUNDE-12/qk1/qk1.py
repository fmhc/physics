#!/usr/bin/env python3
"""QK-1 (Runde 12): Ueberlappintegral I(k) = int f (a + b) j0(k r) r^2 dr der stillen l = 0-Moden.

Quelle der chi-Abstrahlung bei Kopplung g chi |phi|^2: delta S = 2 f (a + b) cos(rho t).
Daten: PROFILE.json (RUNDE-09/krein1/profile). Nullstellen von I(k) im Fenster 0 < k < rho.
Kontrollen: K1 halbes Gitter (jeder zweite Punkt), K2 Abschneideradius 25 statt 30.
"""
import argparse
import json
import os

import numpy as np


def j0(x):
    out = np.ones_like(x)
    m = np.abs(x) > 1e-8
    out[m] = np.sin(x[m]) / x[m]
    return out


def ueberlapp(r, g, k_werte, r_max=None):
    if r_max is not None:
        sel = r <= r_max + 1e-12
        r, g = r[sel], g[sel]
    w = g * r * r
    return np.array([np.trapezoid(w * j0(k * r), r) for k in k_werte])


def nullstellen(k, I):
    s = np.sign(I)
    idx = np.where(s[:-1] * s[1:] < 0)[0]
    # lineare Interpolation der Nullstelle
    return [float(k[i] - I[i] * (k[i + 1] - k[i]) / (I[i + 1] - I[i])) for i in idx]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--profil", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--nk", type=int, default=4000)
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)
    with open(args.profil) as fh:
        P = json.load(fh)
    r = np.asarray(P["r"], dtype=float)
    stellen = P["stellen"]
    if isinstance(stellen, dict):
        stellen = list(stellen.values())
    erg = {"quelle": args.profil, "stellen": []}
    zeilen = []
    for s in stellen:
        if int(s["l"]) != 0:
            continue
        f = np.asarray(s["f"], dtype=float)
        a = np.asarray(s["a"], dtype=float)
        b = np.asarray(s["b"], dtype=float)
        rho = float(s["rho"])
        g = f * (a + b)
        k = np.linspace(0.0, rho, args.nk + 1)[1:-1]
        I = ueberlapp(r, g, k)
        I_halb = ueberlapp(r[::2], g[::2], k)
        I_r25 = ueberlapp(r, g, k, r_max=25.0)
        I0 = float(ueberlapp(r, g, np.array([0.0]))[0])
        n0, n0_h, n0_25 = nullstellen(k, I), nullstellen(k, I_halb), nullstellen(k, I_r25)
        vorzeichenwechsel_g = int(np.sum(np.sign(g[1:]) * np.sign(g[:-1]) < 0))
        eintrag = {"name": s.get("name"), "n": s.get("n"), "omega2": s.get("omega2"), "rho": rho, "I0": I0,
                   "nullstellen_k": n0, "nullstellen_k_halbgitter": n0_h, "nullstellen_k_r25": n0_25,
                   "m_chi_abgestimmt": [float(np.sqrt(max(rho * rho - kk * kk, 0.0))) for kk in n0],
                   "max_abs_I": float(np.max(np.abs(I))), "vorzeichenwechsel_f_a_plus_b": vorzeichenwechsel_g,
                   "I_bei_k": {f"{kk:.3f}": float(ii) for kk, ii in zip(k[::400], I[::400])}}
        erg["stellen"].append(eintrag)
        zeilen.append(f"{eintrag['name']}: rho = {rho:.6f}, I(0) = {I0:.6e}, Nullstellen k = "
                      f"{[round(x, 5) for x in n0]}, Halbgitter {[round(x, 5) for x in n0_h]}, r <= 25 "
                      f"{[round(x, 5) for x in n0_25]}, m_chi abgestimmt {[round(x, 5) for x in eintrag['m_chi_abgestimmt']]}, "
                      f"Vorzeichenwechsel f(a+b) in r: {vorzeichenwechsel_g}")
    with open(os.path.join(args.out, "qk1.json"), "w") as fh:
        json.dump(erg, fh, indent=1)
    text = "\n".join(zeilen)
    with open(os.path.join(args.out, "qk1_bericht.txt"), "w") as fh:
        fh.write(text + "\n")
    print(text, flush=True)


if __name__ == "__main__":
    main()
