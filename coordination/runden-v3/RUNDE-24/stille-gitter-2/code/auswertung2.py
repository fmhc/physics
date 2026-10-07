#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
STILLE-GITTER-2: mechanische Auswertung nach PLAN.md Abschnitt 5.
Aufruf: auswertung2.py <ordner mit lauf-json> <ausgabe.json>
- Scan-Dateien (modus scan) liefern je (typ, stern, h) das Minimum.
- Punkt-Dateien (modus punkt) ergaenzen fehlende Werte: PML wie P2 des Scans (lin2, lpml2, sig02, pexp2) -> Gamma_P2;
  PML wie P1 und punkt_sigoff != 0 -> Gamma_doppel.
- K0: Quadratgitter A und B bei h = 0,3 gegen RUNDE-23 (2,3375e-5 und 3,9974e-9), Schranke 5 %.
- TG0 bis TG3: Dreiecksgitter, nur die Karten-h {0,5; 0,4; 0,3; 0,25; 0,2}; weitere h nur berichtet.
"""
import os
import sys
import json
import glob
import math
import numpy as np
from scipy.optimize import curve_fit

REF = 0.529266
K0_REF = {"A": 2.3375e-5, "B": 3.9974e-9}
KARTEN_H = (0.5, 0.4, 0.3, 0.25, 0.2)
# RUNDE-23 (ERGEBNIS.md, Tabellen), nur zum Berichten, ohne Wertung
R23 = {"A": {0.5: 2.0579e-4, 0.4: 7.8257e-5, 0.3: 2.3375e-5, 0.25: 1.1022e-5, 0.2: 4.4327e-6, 0.15: 1.3828e-6},
       "B": {0.5: 3.2970e-7, 0.4: 4.5787e-8, 0.3: 3.9974e-9, 0.25: 8.8290e-10, 0.2: 1.4219e-10, 0.15: 1.3875e-11}}


def lade(d):
    tab = {}
    punkte = []
    for fn in sorted(glob.glob(os.path.join(d, "*.json"))):
        with open(fn) as fh:
            e = json.load(fh)
        a = e["args"]
        key = (a["typ"], a["stern"], round(float(a["h"]), 6))
        if a["modus"] == "scan" and "minimum" in e:
            m = e["minimum"]
            r = dict(datei=os.path.basename(fn), typ=a["typ"], stern=a["stern"], h=float(a["h"]), x=m["x"],
                     pml1=(a["lin"], a["lpml"], a["sig0"], a["pexp"]),
                     pml2=(a["lin"] if a.get("lin2") is None else a["lin2"], a["lpml2"], a["sig02"], a["pexp2"]),
                     G=m["Gamma_fit"], sG=m.get("sigma_fit"), sx=m.get("sigma_x"), Gd=m["Gamma_direkt"],
                     Gdop=m.get("Gamma_doppel"), GP2=m.get("Gamma_P2"), a=m["a"], rho=m["rho_re"],
                     R_achse=m.get("R_achse"), R_diag=m.get("R_diag"), l=m["fluss"][0].get("l"),
                     fl1=m["fluss"][0]["anteil"], fl2=m["fluss"][1]["anteil"], fehlt=e.get("fehlt", []),
                     n_punkte=len(e["punkte"]), sek=e.get("sek"), sha=e.get("sha256_skript"))
            tab[key] = r
        elif a["modus"] == "punkt" and e.get("punkte"):
            p = e["punkte"][-1]
            punkte.append((key, a, p, os.path.basename(fn)))
    for key, a, p, fn in punkte:
        if key not in tab:
            continue
        r = tab[key]
        if abs(p["om2"] - r["x"]) > 1e-12:
            r.setdefault("hinweise", []).append("%s: x weicht ab (%.3e)" % (fn, p["om2"] - r["x"]))
            continue
        pml = (a["lin"], a["lpml"], a["sig0"], a["pexp"])
        if pml == tuple(r["pml2"]) and r["GP2"] is None:
            r["GP2"] = p["Gamma"]
            r.setdefault("ergaenzt", []).append("P2 aus " + fn)
        elif pml == tuple(r["pml1"]) and abs(float(a.get("punkt_sigoff", 0.0))) > 0 and r["Gdop"] is None:
            r["Gdop"] = p["Gamma"]
            r.setdefault("ergaenzt", []).append("DOPPEL aus " + fn)
    for r in tab.values():
        if r["Gdop"] is not None and r["GP2"] is not None:
            r["boden"] = abs(r["Gd"] - r["Gdop"]) + abs(r["Gd"] - r["GP2"])
            r["ueber"] = bool(r["G"] > 0 and r["G"] >= 10.0 * r["boden"])
        else:
            r["boden"] = None
            r["ueber"] = None
    return tab


def gerade(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    n = len(x)
    xm, ym = x.mean(), y.mean()
    sxx = float(np.sum((x - xm) ** 2))
    b = float(np.sum((x - xm) * (y - ym)) / sxx)
    a0 = ym - b * xm
    res = y - (a0 + b * x)
    se = float(math.sqrt(np.sum(res ** 2) / (n - 2) / sxx)) if n > 2 else float("nan")
    return b, se, float(a0)


def main():
    d, out = sys.argv[1], sys.argv[2]
    tab = lade(d)
    erg = dict(tabelle=[tab[k] for k in sorted(tab)])
    # ---------------- K0
    k0 = {}
    for s in ("A", "B"):
        r = tab.get(("sq", s, 0.3))
        if r is None:
            k0[s] = None
            continue
        rel = r["G"] / K0_REF[s] - 1.0
        k0[s] = dict(G=r["G"], ref=K0_REF[s], rel=rel, ok=bool(abs(rel) <= 0.05), boden=r["boden"])
    erg["K0_teile"] = k0
    erg["K0"] = (None if any(v is None for v in k0.values()) else bool(all(v["ok"] for v in k0.values())))
    # ---------------- Dreiecksgitter
    alle = sorted([r for r in tab.values() if r["typ"] == "tri"], key=lambda r: r["h"])
    rs = [r for r in alle if any(abs(r["h"] - hk) < 1e-9 for hk in KARTEN_H)]
    hs = np.array([r["h"] for r in rs])
    xs = np.array([r["x"] for r in rs])
    e = dict(h=hs.tolist(), x=xs.tolist(), h_zusatz=[r["h"] for r in alle if r not in rs])
    if len(rs) >= 3:
        try:
            popt, pcov = curve_fit(lambda h, w0, c, q: w0 + c * h ** q, hs, xs, p0=(REF, 4e-3, 2.0), maxfev=20000)
            e["q"] = float(popt[2])
            e["sigma_q"] = float(math.sqrt(max(pcov[2, 2], 0.0)))
            e["w0_q"] = float(popt[0])
            e["c_q"] = float(popt[1])
        except Exception as ex:  # noqa
            e["q_fehler"] = str(ex)
        sel = hs <= 0.3 + 1e-9
        if np.sum(sel) >= 2:
            c1, c0 = np.polyfit(hs[sel] ** 2, xs[sel], 1)
            e["w0_h2"] = float(c0)
            e["c_h2"] = float(c1)
            e["w0_h2_abw"] = float(c0 - REF)
    ub = [r for r in rs if r["ueber"]]
    e["h_ueber"] = [r["h"] for r in ub]
    e["h_unter"] = [r["h"] for r in rs if r["ueber"] is False]
    if len(ub) >= 3:
        p, se, _ = gerade(np.log([r["h"] for r in ub]), np.log([r["G"] for r in ub]))
        e["p"] = p
        e["sigma_p"] = se
    lok = []
    for i in range(len(alle) - 1):
        r1, r2 = alle[i], alle[i + 1]
        if r1["G"] > 0 and r2["G"] > 0:
            lok.append(dict(h1=r1["h"], h2=r2["h"], p=float(math.log(r2["G"] / r1["G"]) / math.log(r2["h"] / r1["h"])),
                            beide_ueber=bool(r1["ueber"] and r2["ueber"])))
    e["lokal"] = lok
    # Vergleich mit RUNDE-23 (nur berichtet)
    e["vergleich_r23"] = [dict(h=r["h"], B_durch_T=(R23["B"].get(round(r["h"], 6)) / r["G"]
                                                    if r["G"] > 0 and round(r["h"], 6) in R23["B"] else None),
                               A_durch_T=(R23["A"].get(round(r["h"], 6)) / r["G"]
                                          if r["G"] > 0 and round(r["h"], 6) in R23["A"] else None))
                          for r in alle]
    erg["tri"] = e
    rT = {round(r["h"], 6): r for r in rs}
    # TG0
    if "q" in e and "w0_h2" in e:
        erg["TG0"] = bool(abs(e["q"] - 2.0) <= 0.4 and abs(e["w0_h2"] - REF) <= 3e-5)
    else:
        erg["TG0"] = None
    # TG1
    erg["TG1"] = bool(len(ub) >= 3 and "p" in e and 6.5 <= e["p"] <= 9.5)
    # TG2: F6-Anteil (r = 20) am MIN-Punkt fuer alle Karten-h <= 0,4
    f6 = {}
    fehlt2 = []
    for hk in KARTEN_H:
        if hk > 0.4 + 1e-9:
            continue
        r = rT.get(round(hk, 6))
        if r is None:
            fehlt2.append(hk)
        else:
            f6[hk] = r["fl1"][1]
    erg["TG2_F6"] = f6
    erg["TG2_fehlt"] = fehlt2
    erg["TG2_unter_080"] = [h for h, v in f6.items() if v < 0.80]
    if erg["TG2_unter_080"]:
        erg["TG2"] = False
    elif fehlt2 or not f6:
        erg["TG2"] = None
    else:
        erg["TG2"] = True
    # TG3
    r3 = rT.get(0.3)
    if r3 is None or r3["ueber"] is None:
        erg["TG3"] = None
    else:
        g3 = r3["G"] if r3["ueber"] else max(r3["G"], 10.0 * r3["boden"])
        erg["TG3_wert"] = g3
        erg["TG3"] = bool(g3 < 4.0e-9)
    with open(out, "w") as fh:
        json.dump(erg, fh, indent=1)
    # Textausgabe
    print("typ stern h x* Gamma_fit sigma Gamma_dir Gamma_doppel Gamma_P2 Boden ueber a rho F0 F1 F2 (r=20) F1(r=22.5) R_achse-R_diag")
    for r in erg["tabelle"]:
        print("%s %s %.2f %.9f %.5e %.1e %.5e %s %s %s %s %.1f %.9f %.4f %.4f %.4f %.4f %.4f" % (
            r["typ"], r["stern"], r["h"], r["x"], r["G"], r["sG"] or float("nan"), r["Gd"],
            "%.5e" % r["Gdop"] if r["Gdop"] is not None else "-", "%.5e" % r["GP2"] if r["GP2"] is not None else "-",
            "%.1e" % r["boden"] if r["boden"] is not None else "-", r["ueber"], r["a"], r["rho"],
            r["fl1"][0], r["fl1"][1], r["fl1"][2], r["fl2"][1], (r["R_achse"] or 0) - (r["R_diag"] or 0)))
    print("tri", json.dumps(e))
    print("K0", erg["K0"], json.dumps(k0))
    print("TG0", erg["TG0"], "TG1", erg["TG1"], "TG2", erg["TG2"], f6, erg["TG2_unter_080"], fehlt2,
          "TG3", erg["TG3"], erg.get("TG3_wert"))


if __name__ == "__main__":
    main()
