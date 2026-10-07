#!/usr/bin/env python3
"""QBALL-HADRON-1, Rohdatenprobe: nur Auswertung vorhandener RG-1-Daten (RUNDE-06/regge, Tabellen h001 und h0005).

Keine neue Feldrechnung. Liest die alten ergebnis.json, bildet E_m(Q) bei festem Q auf drei Arten und daraus R2, R3:
  A  wie RG-1: lineare Interpolation von ln E gegen ln Q (np.interp) -> muss die Rotorprobe 0,899 / 0,924 treffen (QH0)
  B  kubisch Hermite in Q mit der exakten Steigung dE/dQ = omega an beiden Stuetzstellen
  C  kubisch Hermite in u = ln Q mit dE/du = omega Q
Spanne A/B/C = grobe Fehlermarke der Interpolation. Dazu die omega^2-Lage je (m, Q) und die Halbwertsradien
(Seitenverhaeltnis A wie HAGEDORN-2) durch lineare Interpolation in omega^2, nur beschreibend.
Ausserdem: R2, R3 der rho-a2-rho3-a4-Bahn aus PDG 2024 (mass_width_2024.txt) und R2 aus KKL 2005 Tabelle III.

Aufruf: python3 rohdaten.py --h001 PFAD --h0005 PFAD --out ORDNER
"""
import argparse
import json
import math
import os

import numpy as np

Q_ZIEL = (300.0, 1000.0)


def familien(zeilen):
    fam = {}
    for z in zeilen:
        if z["nls"] or not z.get("gueltig") or abs(z.get("virial", 1.0)) > 1e-5:
            continue
        fam.setdefault(z["m"], []).append(z)
    for m in fam:
        fam[m].sort(key=lambda z: z["Q"])  # aufsteigend in Q (= absteigend in omega^2)
    return fam


def e_linlog(zz, q):
    lnQ = np.log([z["Q"] for z in zz])
    lnE = np.log([z["E"] for z in zz])
    if not (lnQ[0] <= math.log(q) <= lnQ[-1]):
        return None
    return float(np.exp(np.interp(math.log(q), lnQ, lnE)))


def intervall(zz, q):
    for a, b in zip(zz[:-1], zz[1:]):
        if a["Q"] <= q <= b["Q"]:
            return a, b
    return None


def hermite(x0, x1, y0, y1, d0, d1, x):
    hh = x1 - x0
    t = (x - x0) / hh
    h00 = 2 * t ** 3 - 3 * t ** 2 + 1
    h10 = t ** 3 - 2 * t ** 2 + t
    h01 = -2 * t ** 3 + 3 * t ** 2
    h11 = t ** 3 - t ** 2
    return h00 * y0 + h10 * hh * d0 + h01 * y1 + h11 * hh * d1


def e_hermite_q(zz, q):
    ab = intervall(zz, q)
    if ab is None:
        return None
    a, b = ab
    return float(hermite(a["Q"], b["Q"], a["E"], b["E"], a["omega"], b["omega"], q))


def e_hermite_lnq(zz, q):
    ab = intervall(zz, q)
    if ab is None:
        return None
    a, b = ab
    return float(hermite(math.log(a["Q"]), math.log(b["Q"]), a["E"], b["E"], a["omega"] * a["Q"], b["omega"] * b["Q"],
                         math.log(q)))


def lage(zz, q):
    ab = intervall(zz, q)
    if ab is None:
        return None
    a, b = ab
    t = (q - a["Q"]) / (b["Q"] - a["Q"])
    w2 = a["w2"] + t * (b["w2"] - a["w2"])
    ri = a["R_innen"] + t * (b["R_innen"] - a["R_innen"])
    ra = a["R_aussen"] + t * (b["R_aussen"] - a["R_aussen"])
    seit = ((ri + ra) / 2.0) / (ra - ri) if ri > 0 else None
    return dict(w2=w2, intervall_w2=[a["w2"], b["w2"]], intervall_Q=[a["Q"], b["Q"]], R_innen=ri, R_aussen=ra,
                seitenverhaeltnis=seit)


def r23(e):
    out = {}
    if all(k in e for k in (0, 1, 2)):
        d1 = e[1] ** 2 - e[0] ** 2
        out["R2"] = (e[2] ** 2 - e[0] ** 2) / d1
        if 3 in e:
            out["R3"] = (e[3] ** 2 - e[0] ** 2) / d1
        if 4 in e:
            out["R4"] = (e[4] ** 2 - e[0] ** 2) / d1
    return out


def exponent(e):
    if 0 not in e:
        return None
    pos = [m for m in sorted(e) if m > 0 and e[m] - e[0] > 0]
    if len(pos) < 3:
        return None
    x = np.log(pos)
    y = np.log([e[m] - e[0] for m in pos])
    A = np.vstack([x, np.ones_like(x)]).T
    (b, c), *_ = np.linalg.lstsq(A, y, rcond=None)
    return float(b)


def auswerten(tab, name):
    fam = familien(tab["tabelle"]["zeilen"])
    res = {}
    for q in Q_ZIEL:
        ein = {}
        for art, fn in (("A_linlog", e_linlog), ("B_hermite_Q", e_hermite_q), ("C_hermite_lnQ", e_hermite_lnq)):
            e = {}
            for m, zz in sorted(fam.items()):
                v = fn(zz, q)
                if v is not None:
                    e[m] = v
            ein[art] = dict(E={str(m): v for m, v in e.items()}, exponent_dE_gegen_m=exponent(e), **r23(e))
        ein["lage"] = {str(m): lage(zz, q) for m, zz in sorted(fam.items()) if lage(zz, q) is not None}
        res[str(q)] = ein
    return res


def pdg():
    # PDG 2024 mass_width_2024.txt (quellen/F4-pdg-mass_width_2024.txt): Zentralwerte und Fehler in GeV
    m = dict(rho=(0.77526, 0.00023), a2=(1.3182, 0.0006), rho3=(1.6888, 0.0021), a4=(1.967, 0.016))
    M2 = {k: v[0] ** 2 for k, v in m.items()}
    d1 = M2["a2"] - M2["rho"]
    R2 = (M2["rho3"] - M2["rho"]) / d1
    R3 = (M2["a4"] - M2["rho"]) / d1
    # lineare Fehlerfortpflanzung, unabhaengige Fehler
    def grad(f, k, eps=1e-7):
        mm = dict(m)
        mm[k] = (m[k][0] + eps, m[k][1])
        M2p = {kk: vv[0] ** 2 for kk, vv in mm.items()}
        return (f(M2p) - f(M2)) / eps
    fR2 = lambda M: (M["rho3"] - M["rho"]) / (M["a2"] - M["rho"])
    fR3 = lambda M: (M["a4"] - M["rho"]) / (M["a2"] - M["rho"])
    sR2 = math.sqrt(sum((grad(fR2, k) * m[k][1]) ** 2 for k in m))
    sR3 = math.sqrt(sum((grad(fR3, k) * m[k][1]) ** 2 for k in m))
    schritte = [M2["a2"] - M2["rho"], M2["rho3"] - M2["a2"], M2["a4"] - M2["rho3"]]
    return dict(M2=M2, R2=R2, R2_fehler=sR2, R3=R3, R3_fehler=sR3, schritte_GeV2=schritte,
                alpha_strich_je_schritt=[1.0 / s for s in schritte])


def kkl():
    # KKL 2005 (gr-qc/0505143) Tabelle III, Q = 410, n = 0, 1, 2, gerade Paritaet; m_B = sqrt(lambda b) = sqrt(1,1)
    E = {0: 293.8, 1: 363.4, 2: 414.7}
    return dict(E=E, **r23(E), schwelle_mB_Q=math.sqrt(1.1) * 410.0, anteil_n2=E[2] / (math.sqrt(1.1) * 410.0))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--h001", required=True)
    ap.add_argument("--h0005", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    with open(a.h001) as f:
        t1 = json.load(f)
    with open(a.h0005) as f:
        t2 = json.load(f)
    erg = dict(h001=auswerten(t1, "h001"), h0005=auswerten(t2, "h0005"), pdg=pdg(), kkl=kkl(),
               rg1_bericht_rotor=t1["auswertung"].get("rotor"))
    with open(os.path.join(a.out, "rohdaten.json"), "w") as f:
        json.dump(erg, f, indent=1, sort_keys=True)
    z = []
    for tn in ("h001", "h0005"):
        for q, ein in erg[tn].items():
            z.append(f"[{tn}] Q = {q}")
            for art in ("A_linlog", "B_hermite_Q", "C_hermite_lnQ"):
                v = ein[art]
                es = ", ".join(f"{m}: {x:.4f}" for m, x in v["E"].items())
                z.append(f"  {art}: R2 = {v.get('R2', float('nan')):.4f}, R3 = {v.get('R3', float('nan')):.4f}, "
                         f"R4 = {v.get('R4', float('nan')):.4f}, Exponent = {v['exponent_dE_gegen_m']}; E_m = {es}")
            for m, l in ein["lage"].items():
                sv = l["seitenverhaeltnis"]
                z.append(f"  m = {m}: omega^2 ~ {l['w2']:.4f} (Intervall {l['intervall_w2']}), R_innen {l['R_innen']:.3f}, "
                         f"R_aussen {l['R_aussen']:.3f}, A = {sv if sv is None else round(sv, 3)}")
    p = erg["pdg"]
    z.append(f"PDG: R2 = {p['R2']:.5f} +- {p['R2_fehler']:.5f}, R3 = {p['R3']:.5f} +- {p['R3_fehler']:.5f}, "
             f"Schritte {['%.5f' % s for s in p['schritte_GeV2']]}, M2 {p['M2']}")
    k = erg["kkl"]
    z.append(f"KKL Tab. III: R2 = {k['R2']:.5f}, n = 2 bei {k['anteil_n2']:.4f} der Schwelle {k['schwelle_mB_Q']:.2f}")
    with open(os.path.join(a.out, "rohdaten.txt"), "w") as f:
        f.write("\n".join(z) + "\n")
    print("\n".join(z))


if __name__ == "__main__":
    main()
