#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Z2-SCHUTZ-2: mechanische Urteile nach PLAN.md Abschnitt 7 (ZT0 bis ZT3). Synthetisch, keine Messdaten.
Aufruf nur ueber kleintest.sh auf der .69."""
import argparse
import hashlib
import json
import math
import os
import time

GROESSEN = [(10.0, 20.0), (10.0, 24.0), (10.0, 28.0), (10.0, 32.0), (8.0, 24.0), (12.0, 24.0), (14.0, 24.0)]
B_REF_PLAN = 25.028515686495666   # Z2-SCHUTZ-1 lauf-69/weg-haupt-r10-R20-neb.json, B(G1)
B_REF_WORT = 25.03                # Kartenwortlaut ZT0


def sha_datei(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def lade(p):
    if not os.path.exists(p):
        return None
    with open(p) as f:
        return json.load(f)


def gtag(r0, R):
    return "r%g-R%g" % (r0, R)


def hesse_S_ok(st):
    if st is None or "hesse_S" not in st:
        return None, "fehlt"
    s = st["hesse_S"]
    w = s.get("eigenwerte")
    if w is None or len(w) < 3:
        return False, "keine Eigenwerte (%s)" % s.get("fehler")
    ok = (abs(w[0]) <= 1e-5 and abs(w[1]) <= 1e-5 and w[2] > 1e-4
          and min(s.get("symmetrie_ueberlapp", [0.0])) >= 0.99)
    return bool(ok), "lambda %s, ueberlapp %s" % (w, s.get("symmetrie_ueberlapp"))


def groesse(L, r0, R):
    t = gtag(r0, R)
    st = lade(os.path.join(L, "start-%s.json" % t))
    bi = lade(os.path.join(L, "bisekt-%s.json" % t))
    wg = lade(os.path.join(L, "weg-haupt-%s-neb.json" % t))
    h_ok, h_txt = hesse_S_ok(st)
    s_ok = bool(st is not None and st.get("grund") == "konvergiert" and st.get("fmax", 1.0) <= 1e-7 and h_ok)
    g = {"r0": r0, "R": R, "E_S": st.get("E_S") if st else None, "start_grund": st.get("grund") if st else None,
         "start_fmax": st.get("fmax") if st else None, "hesse_S_ok": h_ok, "hesse_S": h_txt, "S_gueltig": s_ok}
    # Verfahren A
    frei = (bi or {}).get("freigabe") or {}
    g["A"] = {"vorhanden": bool(bi is not None and bi.get("klammer")),
              "barriere": (bi or {}).get("barriere"), "n_halb": (bi or {}).get("n_halb"),
              "lambda1_klasse": (bi or {}).get("lambda1_klasse"), "klammer": (bi or {}).get("klammer"),
              "lambda_lo": (bi or {}).get("lambda_lo"), "lambda_hi": (bi or {}).get("lambda_hi"),
              "sattel1": (bi or {}).get("sattel1"), "weg_art": (bi or {}).get("weg_art"),
              "pfad_ok": (bi or {}).get("pfad_ok"), "stufe3_gerechnet": ((bi or {}).get("stufe3") or {}).get("gerechnet"),
              "sattel2": ((bi or {}).get("stufe3") or {}).get("sattel2"),
              "freigabe_klasse": frei.get("klasse"), "freigabe_T": frei.get("T_erreicht"),
              "zwischenminimum": frei.get("zwischenminimum"), "E_freigabe_ende": frei.get("E_end"),
              "zahl_M": (bi or {}).get("zahl_M"), "zahl_offen": (bi or {}).get("zahl_offen"),
              "genau": (bi or {}).get("genau"), "stufe2_gilt": ((bi or {}).get("stufe2") or {}).get("gilt"),
              "L10": ((bi or {}).get("lokalisierung") or {}).get("L10"),
              "n50": ((bi or {}).get("lokalisierung") or {}).get("n50"),
              "laufzeit_s": (bi or {}).get("laufzeit_s")}
    g["A"]["gueltig"] = bool(bi is not None and bi.get("gueltig_A_ohne_S") and s_ok)
    # Verfahren B
    wk = (wg or {}).get("weg") or {}
    g["B"] = {"vorhanden": bool(wg is not None and wg.get("barriere") is not None),
              "barriere": (wg or {}).get("barriere"), "konvergiert": wk.get("konvergiert"), "ki": wk.get("ki"),
              "iterationen": wk.get("iterationen"), "fki": wk.get("fki"), "grund": wk.get("grund"),
              "L10": ((wg or {}).get("lokalisierung") or {}).get("L10"),
              "n50": ((wg or {}).get("lokalisierung") or {}).get("n50"),
              "laufzeit_s": (wg or {}).get("laufzeit_s")}
    g["B"]["gueltig"] = bool(wg is not None and wk.get("konvergiert") and (wk.get("ki") or 0) > 0 and s_ok
                             and frei.get("T_erreicht") is True)
    werte = {m: (g[m]["barriere"], g[m]["L10"]) for m in ("A", "B") if g[m]["gueltig"]}
    if werte:
        vb = min(werte, key=lambda k: werte[k][0])
        g["B_G"], g["B_verfahren"], g["L10_G"] = werte[vb][0], vb, werte[vb][1]
    else:
        g["B_G"], g["B_verfahren"], g["L10_G"] = None, None, None
    g["L10_gueltige_verfahren"] = {m: werte[m][1] for m in werte}
    if g["A"]["gueltig"] and g["B"]["gueltig"]:
        a, b = g["A"]["barriere"], g["B"]["barriere"]
        g["K_weg_rel"] = abs(a - b) / min(a, b) if min(a, b) > 0 else None
        g["K_weg"] = "bestanden" if (g["K_weg_rel"] is not None and g["K_weg_rel"] <= 0.05) else "verfehlt"
    else:
        g["K_weg"] = "nicht auswertbar"
    if bi is not None and bi.get("klammer") and not g["A"]["gueltig"]:
        g["austrittsbarriere_beschreibend"] = bi.get("barriere")
    return g


def steigung(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sxx if sxx > 0 else None


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--lauf", default=".")
    p.add_argument("--aus", default=".")
    args = p.parse_args()
    L = args.lauf
    aus = {"karte": "Z2-SCHUTZ-2 (Runde 49)", "code_sha256": sha_datei(os.path.abspath(__file__)),
           "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "groessen": {}, "urteile": {}}
    G = {}
    for r0, R in GROESSEN:
        G[(r0, R)] = groesse(L, r0, R)
        aus["groessen"][gtag(r0, R)] = G[(r0, R)]
    u = aus["urteile"]
    # ZT0
    g1 = G[(10.0, 20.0)]
    if g1["A"]["gueltig"] and g1["B"]["gueltig"]:
        da = abs(g1["A"]["barriere"] / B_REF_PLAN - 1.0)
        db = abs(g1["B"]["barriere"] / B_REF_PLAN - 1.0)
        plan = "eingetroffen" if (da <= 1e-3 and db <= 1e-3) else "nicht eingetroffen"
    else:
        da = db = None
        plan = "nicht auswertbar"
    if g1["A"]["vorhanden"] and g1["B"]["vorhanden"]:
        wa = abs(g1["A"]["barriere"] / B_REF_WORT - 1.0)
        wb = abs(g1["B"]["barriere"] / B_REF_WORT - 1.0)
        wort = "eingetroffen" if (wa <= 1e-3 and wb <= 1e-3) else "nicht eingetroffen"
    else:
        wa = wb = None
        wort = "nicht auswertbar"
    u["ZT0"] = {"plan": plan, "wortlaut": wort, "rel_A_plan": da, "rel_B_plan": db, "rel_A_wort": wa,
                "rel_B_wort": wb, "B_A": g1["A"]["barriere"], "B_B": g1["B"]["barriere"]}
    # ZT1
    b20 = G[(10.0, 20.0)]["B_G"]
    rel = {}
    for R in (24.0, 28.0, 32.0):
        bR = G[(10.0, R)]["B_G"]
        if b20 is not None and bR is not None:
            rel["%g" % R] = abs(bR / b20 - 1.0)
    if b20 is None:
        plan = "nicht auswertbar"
    elif any(v >= 0.10 for v in rel.values()):
        plan = "nicht eingetroffen"
    elif ("28" in rel) or ("32" in rel):
        plan = "eingetroffen"
    else:
        plan = "nicht auswertbar"
    Rs = "28" if "28" in rel else ("32" if "32" in rel else None)
    if b20 is None or Rs is None:
        wort = "nicht auswertbar"
    else:
        wort = "eingetroffen" if rel[Rs] < 0.10 else "nicht eingetroffen"
    u["ZT1"] = {"plan": plan, "wortlaut": wort, "rel_aenderung": rel, "R_stern": Rs, "B_10_20": b20,
                "B": {"%g" % R: G[(10.0, R)]["B_G"] for R in (20.0, 24.0, 28.0, 32.0)}}
    # ZT2
    pts = [(r0, G[(r0, 24.0)]["B_G"]) for r0 in (8.0, 10.0, 12.0, 14.0) if G[(r0, 24.0)]["B_G"] is not None]
    pts = [(r0, b) for r0, b in pts if b > 0]
    if len(pts) >= 3:
        pe = steigung([math.log(r) for r, _ in pts], [math.log(b) for _, b in pts])
        mono = all(pts[i + 1][1] > pts[i][1] for i in range(len(pts) - 1))
        im = pe is not None and 1.5 <= pe <= 2.5
        plan = "eingetroffen" if (im and mono) else "nicht eingetroffen"
        wort = "eingetroffen" if im else "nicht eingetroffen"
        lokal = [math.log(pts[i + 1][1] / pts[i][1]) / math.log(pts[i + 1][0] / pts[i][0]) for i in range(len(pts) - 1)]
    else:
        pe, mono, lokal = None, None, None
        plan = wort = "nicht auswertbar"
    u["ZT2"] = {"plan": plan, "wortlaut": wort, "exponent": pe, "streng_wachsend": mono, "punkte": pts,
                "lokale_exponenten": lokal}
    # ZT3
    gv = [g for g in G.values() if g["B_G"] is not None]
    if len(gv) >= 3:
        ok = all(all(v is not None and v >= 0.5 for v in g["L10_gueltige_verfahren"].values()) for g in gv)
        plan = "eingetroffen" if ok else "nicht eingetroffen"
    else:
        plan = "nicht auswertbar"
    if len(gv) >= 1:
        okw = all(g["L10_G"] is not None and g["L10_G"] >= 0.5 for g in gv)
        wort = "eingetroffen" if okw else "nicht eingetroffen"
    else:
        wort = "nicht auswertbar"
    u["ZT3"] = {"plan": plan, "wortlaut": wort,
                "L10": {gtag(g["r0"], g["R"]): g["L10_gueltige_verfahren"] for g in gv},
                "zahl_gueltig": len(gv)}
    with open(os.path.join(args.aus, "auswertung.json"), "w") as f:
        json.dump(aus, f, indent=1)
    print("auswertung fertig")


if __name__ == "__main__":
    main()
