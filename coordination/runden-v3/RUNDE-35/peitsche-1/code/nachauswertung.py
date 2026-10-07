#!/usr/bin/env python3
"""RUNDE-35, PEITSCHE-1: beschreibende Nachauswertung (NACH dem Einfrieren geschrieben, kein Urteil).

- Teil A: Wandschnelle v_k der Nullstelle (zentrale Differenz wie im Plan) gegen R, verglichen mit der Duennwandformel,
  dazu das Verhaeltnis |T0r|/T00 im energietragenden Bereich; erstes R mit v_k > 1 vor t_c; Tabelle bei festen R.
- Teil B: v_E(r) fuer einige Zeilen.
- Bilder: v(R) gegen Duennwand (Teil A), v_E(r) (Teil B).
Aufruf: python3 nachauswertung.py --lauf lauf --out lauf/nachauswertung.json
"""
import argparse
import json
import math
import os

import numpy as np

LAEUFE = ("a_d2_R80", "a_d2_R40", "a_d2_R20", "a_d3_R40", "a_d3_R20")
R_FEST = (32.0, 16.0, 8.0, 6.0, 4.0, 3.0, 2.0, 1.5, 1.0, 0.5)


def v_duenn(d, R, R0):
    x = R / R0
    return np.sqrt(np.maximum(0.0, 1.0 - x ** 2)) if d == 2 else np.sqrt(np.maximum(0.0, 1.0 - x ** 4))


def lauf_auswerten(pfad):
    with open(os.path.join(pfad, "zusammenfassung.json")) as fh:
        Z = json.load(fh)
    meta, mess = Z["meta"], Z["messung"]
    D = np.load(os.path.join(pfad, "zeitreihe.npz"))
    t, R, sp = D["t"], D["R"], [str(s) for s in D["spalten"]]
    col = {k: D["Z"][:, j] for j, k in enumerate(sp)}
    tc = mess["t_c"]
    v = np.full(t.size, np.nan)
    for k in range(1, t.size - 1):
        if t[k + 1] < tc and R[k - 1] > 0 and R[k] > 0 and R[k + 1] > 0:
            v[k] = -(R[k + 1] - R[k - 1]) / (t[k + 1] - t[k - 1])
    ok = np.isfinite(v)
    d, R0 = meta["d"], meta["R0"]
    vd = v_duenn(d, R, R0)
    erstes = None
    for k in np.nonzero(ok)[0]:
        if v[k] > 1.0:
            erstes = dict(R=float(R[k]), t=float(t[k]), v=float(v[k]), v_duenn=float(vd[k]),
                          ratio_wand=float(col["ratio_wand"][k]))
            break
    fest = {}
    for Rz in R_FEST:
        if Rz >= R0:
            continue
        kk = [k for k in np.nonzero(ok)[0][1:] if R[k - 1] > Rz >= R[k] and np.isfinite(v[k - 1])]
        if not kk:
            continue
        k = kk[0]
        vv = float(v[k - 1] + (v[k] - v[k - 1]) * (Rz - R[k - 1]) / (R[k] - R[k - 1]))
        sd = float(v_duenn(d, Rz, R0))
        fest[str(Rz)] = dict(v=vv, v_duenn=sd, dv=vv - sd, dv_mal_R2=(vv - sd) * Rz * Rz,
                             ratio_wand=float(col["ratio_wand"][k]), v_mittel=float(col["v_mittel"][k]))
    return dict(d=d, R0=R0, dr=meta["dr"], t_c=tc, erstes_v_ueber_1=erstes, bei_R=fest), (t, R, v, vd, col, tc)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lauf", default="lauf")
    ap.add_argument("--out", default="lauf/nachauswertung.json")
    args = ap.parse_args()
    aus = {}
    reihen = {}
    for n in LAEUFE:
        for g in ("fein", "grob"):
            p = os.path.join(args.lauf, f"{n}_{g}")
            if os.path.exists(os.path.join(p, "zeitreihe.npz")):
                aus[f"{n}_{g}"], reihen[f"{n}_{g}"] = lauf_auswerten(p)
    with open(args.out, "w") as fh:
        json.dump(aus, fh, indent=1, ensure_ascii=False)
    for k, a in aus.items():
        e = a["erstes_v_ueber_1"]
        print(k, "t_c", round(a["t_c"], 4), "erstes v>1:", None if e is None else (round(e["R"], 3), round(e["v"], 4),
                                                                               round(e["ratio_wand"], 6)))
        for Rz, w in a["bei_R"].items():
            print(f"   R = {Rz:>5}: v = {w['v']:.5f}  duenn {w['v_duenn']:.5f}  dv*R^2 = {w['dv_mal_R2']:+.4f}  "
                  f"T0r/T00 (Wand) = {w['ratio_wand']:.6f}  gewichtet {w['v_mittel']:.5f}")
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as ex:  # Bilder sind optional
        print("keine Bilder:", ex)
        return
    fig, ax = plt.subplots(1, 2, figsize=(12, 4.6))
    for n, farbe in zip(LAEUFE, ("C0", "C1", "C2", "C3", "C4")):
        k = f"{n}_fein"
        if k not in reihen:
            continue
        t, R, v, vd, col, tc = reihen[k]
        ok = np.isfinite(v) & (R > 0)
        ax[0].plot(R[ok], 1.0 - v[ok], color=farbe, lw=1.2, label=f"{n} Nullstelle")
        ax[0].plot(R[ok], 1.0 - vd[ok], color=farbe, lw=0.8, ls="--")
        rw = col["ratio_wand"]
        ax[1].plot(R[ok], 1.0 - rw[ok], color=farbe, lw=1.0, label=f"{n}")
    ax[0].set_xscale("log")
    ax[0].set_yscale("symlog", linthresh=1e-4)
    ax[0].axhline(0.0, color="k", lw=0.6)
    ax[0].set_xlabel("R (Nullstelle)")
    ax[0].set_ylabel("1 - v  (unter 0: schneller als Licht)")
    ax[0].set_title("Wandschnelle der Nullstelle; gestrichelt Duennwand")
    ax[0].legend(fontsize=7)
    ax[1].set_xscale("log")
    ax[1].set_yscale("log")
    ax[1].set_xlabel("R (Nullstelle)")
    ax[1].set_ylabel("1 - max |T0r|/T00 (energietragend)")
    ax[1].set_title("Energiefluss bleibt unter c")
    ax[1].legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(os.path.join(args.lauf, "bild_a_v_gegen_R.png"), dpi=120)
    plt.close(fig)
    b = os.path.join(args.lauf, "b_h0005", "kurven.npz")
    if os.path.exists(b):
        K = np.load(b)
        fig, ax = plt.subplots(1, 2, figsize=(12, 4.6))
        for w2, farbe in zip((0.55, 0.65, 0.8, 0.99), ("C0", "C1", "C2", "C3")):
            for m, ls in ((3, "-"), (8, "--")):
                key = f"m{m}_w{w2:.3f}"
                if key + "_r" not in K:
                    continue
                r, vE, S = K[key + "_r"], K[key + "_vE"], K[key + "_S"]
                ax[0].plot(r, vE, color=farbe, ls=ls, lw=1.0, label=f"m={m}, w2={w2}")
                ax[1].plot(r, S / S.max(), color=farbe, ls=ls, lw=1.0)
        for w2, farbe in zip((0.55, 0.65, 0.8, 0.99), ("C0", "C1", "C2", "C3")):
            ax[0].axhline(math.sqrt(w2 / (w2 + 0.5)), color=farbe, lw=0.5, ls=":")
        ax[0].set_xscale("log")
        ax[0].set_xlabel("r")
        ax[0].set_ylabel("v_E(r)")
        ax[0].set_title("Energiefluss-Geschwindigkeit; punktiert Schranke")
        ax[0].legend(fontsize=7)
        ax[1].set_xscale("log")
        ax[1].set_xlabel("r")
        ax[1].set_ylabel("S/S_max")
        ax[1].set_title("Profil |psi|^2 (normiert)")
        fig.tight_layout()
        fig.savefig(os.path.join(args.lauf, "bild_b_vE.png"), dpi=120)
        plt.close(fig)
    print("Bilder geschrieben")


if __name__ == "__main__":
    main()
