#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
STILLE-AUF-GITTER: mechanische Auswertung nach PLAN.md Abschnitt 5 (eingefroren 2026-10-02 22:56:18 CEST).
Aufruf: auswertung.py <ordner mit lauf-json> <ausgabe.json>
- Scan-Dateien (modus scan) liefern je (Stern, h) das Minimum.
- Punkt-Dateien (modus punkt) ergaenzen fehlende Werte: lpml = 22 -> Gamma_P2, punkt_sigoff != 0 -> Gamma_doppel.
"""
import os
import sys
import json
import glob
import math
import numpy as np
from scipy.optimize import curve_fit

REF = 0.529266


def lade(d):
    tab = {}
    punkte = []
    for fn in sorted(glob.glob(os.path.join(d, "*.json"))):
        with open(fn) as fh:
            e = json.load(fh)
        a = e["args"]
        key = (a["stern"], round(float(a["h"]), 6))
        if a["modus"] == "scan" and "minimum" in e:
            m = e["minimum"]
            r = dict(datei=os.path.basename(fn), stern=a["stern"], h=float(a["h"]), x=m["x"], G=m["Gamma_fit"],
                     sG=m.get("sigma_fit"), sx=m.get("sigma_x"), Gd=m["Gamma_direkt"], Gdop=m.get("Gamma_doppel"),
                     GP2=m.get("Gamma_P2"), a=m["a"], rho=m["rho_re"], R_achse=m.get("R_achse"), R_diag=m.get("R_diag"),
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
        if abs(float(a["lpml"]) - 22.0) < 1e-9 and r["GP2"] is None:
            r["GP2"] = p["Gamma"]
            r.setdefault("ergaenzt", []).append("P2 aus " + fn)
        elif abs(float(a.get("punkt_sigoff", 0.0))) > 0 and r["Gdop"] is None:
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
    erg = dict(tabelle=[tab[k] for k in sorted(tab)], sg={})
    for stern in ("A", "B"):
        rs = sorted([r for r in tab.values() if r["stern"] == stern], key=lambda r: r["h"])
        hs = np.array([r["h"] for r in rs])
        xs = np.array([r["x"] for r in rs])
        e = dict(h=hs.tolist(), x=xs.tolist())
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
        if len(ub) >= 3:
            p, se, _ = gerade(np.log([r["h"] for r in ub]), np.log([r["G"] for r in ub]))
            e["p"] = p
            e["sigma_p"] = se
        lok = []
        for i in range(len(rs) - 1):
            r1, r2 = rs[i], rs[i + 1]
            if r1["G"] > 0 and r2["G"] > 0:
                lok.append(dict(h1=r1["h"], h2=r2["h"], p=float(math.log(r2["G"] / r1["G"]) / math.log(r2["h"] / r1["h"])),
                                beide_ueber=bool(r1["ueber"] and r2["ueber"])))
        e["lokal"] = lok
        erg["sg"][stern] = e
    A, B = erg["sg"]["A"], erg["sg"]["B"]
    # SG0
    ok0 = True
    for s in (A, B):
        if "q" not in s or "w0_h2" not in s:
            ok0 = None if ok0 is not False else False
            continue
        if not (abs(s["q"] - 2.0) <= 0.4 and abs(s["w0_h2"] - REF) <= 3e-5):
            ok0 = False
    erg["SG0"] = ok0
    # SG1
    erg["SG1"] = bool(len(A["h_ueber"]) >= 3 and "p" in A and 3.2 <= A["p"] <= 4.8)
    # SG2
    rB = {round(r["h"], 6): r for r in tab.values() if r["stern"] == "B"}
    rA = {round(r["h"], 6): r for r in tab.values() if r["stern"] == "A"}
    a_ok = bool(len(B["h_ueber"]) >= 3 and "p" in B and 6.0 <= B["p"] <= 10.0)
    hs_klein = [h for h in rB if h <= 0.3 + 1e-9]
    b_ok = bool(hs_klein) and all(rB[h]["ueber"] is False for h in hs_klein)
    c_ok = None
    if 0.3 in rB and 0.3 in rA:
        gb = rB[0.3]["G"] if rB[0.3]["ueber"] else max(rB[0.3]["G"], 10.0 * (rB[0.3]["boden"] or 0.0))
        c_ok = bool(gb < rA[0.3]["G"] / 30.0)
        erg["SG2_c"] = dict(GB=gb, GA=rA[0.3]["G"], verhaeltnis=rA[0.3]["G"] / gb if gb > 0 else None)
    erg["SG2_teile"] = dict(a=a_ok, b=b_ok, c=c_ok)
    erg["SG2"] = bool((a_ok or b_ok) and c_ok) if c_ok is not None else None
    # SG3
    f4 = {r["h"]: r["fl1"][1] for r in tab.values() if r["stern"] == "A" and r["ueber"]}
    erg["SG3_F4"] = f4
    erg["SG3_unter_080"] = [h for h, v in f4.items() if v < 0.80]
    erg["SG3"] = bool(f4) and all(v >= 0.80 for v in f4.values())
    with open(out, "w") as fh:
        json.dump(erg, fh, indent=1)
    # Textausgabe
    print("Stern h x* Gamma_fit sigma Gamma_dir Gamma_doppel Gamma_P2 Boden ueber a rho F0 F4 F8 (r=20) F4(r=22.5) R_achse-R_diag")
    for r in erg["tabelle"]:
        print("%s %.2f %.9f %.5e %.1e %.5e %s %s %s %s %.1f %.9f %.3f %.3f %.3f %.3f %.4f" % (
            r["stern"], r["h"], r["x"], r["G"], r["sG"] or float("nan"), r["Gd"],
            "%.5e" % r["Gdop"] if r["Gdop"] is not None else "-", "%.5e" % r["GP2"] if r["GP2"] is not None else "-",
            "%.1e" % r["boden"] if r["boden"] is not None else "-", r["ueber"], r["a"], r["rho"],
            r["fl1"][0], r["fl1"][1], r["fl1"][2], r["fl2"][1], (r["R_achse"] or 0) - (r["R_diag"] or 0)))
    for s in ("A", "B"):
        e = dict(erg["sg"][s])
        print(s, json.dumps(e))
    print("SG0", erg["SG0"], "SG1", erg["SG1"], "SG2", erg["SG2"], erg["SG2_teile"], erg.get("SG2_c"), "SG3", erg["SG3"],
          erg["SG3_F4"], erg["SG3_unter_080"])


if __name__ == "__main__":
    main()
