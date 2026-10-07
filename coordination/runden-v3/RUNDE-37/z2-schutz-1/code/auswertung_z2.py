#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Z2-SCHUTZ-1: mechanische Urteile nach PLAN.md Abschnitt 5 (ZS0 bis ZS3, Kontrollen). Synthetisch, keine Messdaten.
Aufruf nur ueber kleintest.sh auf der .69."""
import argparse
import hashlib
import json
import os
import time

GROESSEN = [("G1", 10.0, 20.0), ("G2", 12.0, 24.0), ("G3", 14.0, 28.0)]


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


def lade_letzte(L, basis):
    """Letzter Lauf der Kette: Fortsetzung -f2, sonst -f1, sonst der erste Lauf (PLAN Abschnitt 2)."""
    for suf in ("-f2", "-f1", ""):
        w = lade(os.path.join(L, basis + suf + ".json"))
        if w is not None:
            w["datei"] = basis + suf + ".json"
            return w
    return None


def gtag(r0, R):
    return "r%g-R%g" % (r0, R)


def hesse_S_ok(h):
    if h is None or "S" not in h["ergebnisse"]:
        return None, "fehlt"
    s = h["ergebnisse"]["S"]
    w = s.get("eigenwerte")
    if w is None or len(w) < 3:
        return None, "keine Eigenwerte"
    ok = (abs(w[0]) <= 1e-5 and abs(w[1]) <= 1e-5 and w[2] > 1e-4
          and min(s.get("symmetrie_ueberlapp", [0.0])) >= 0.99)
    return bool(ok), "lambda %s, ueberlapp %s" % (w, s.get("symmetrie_ueberlapp"))


def hesse_T_ok(h):
    if h is None or "T" not in h["ergebnisse"]:
        return None
    w = h["ergebnisse"]["T"].get("eigenwerte")
    return None if w is None else bool(w[0] > 1e-4)


def weg_gueltig(w, s_ok, k_ok):
    if w is None:
        return False, "fehlt"
    g = w["weg"]
    if not g["konvergiert"]:
        return False, "nicht konvergiert (%s)" % g["grund"]
    if g["ki"] <= 0:
        return False, "kein Kletterbild"
    if not s_ok:
        return False, "S besteht K-Hesse nicht"
    if not k_ok:
        return False, "Endpunkt (Zugende) fuehrt nach Freigabe nicht nach T"
    return True, "gueltig"


def keim_ok(kj):
    if kj is None or not kj.get("K_gefunden"):
        return False
    kt = kj.get("K_nach_T") or {}
    return bool(kt.get("T_erreicht") and kt.get("E_max_unter_ES"))


def monoton(E, tol):
    return all(E[k + 1] <= E[k] + tol for k in range(len(E) - 1))


def zs0_pruef(w, ref, mit_konv):
    if w is None or ref is None:
        return None, "fehlt"
    E = w["weg"]["E_profil"]
    i = monoton(E, 1e-9 * abs(E[0]))
    ii = w["weg"]["sonde_lauf"] > 0.0
    iii = (abs(E[0] / ref["E_vor"] - 1.0) <= 1e-6) and (abs(E[-1] / ref["E_end"] - 1.0) <= 1e-6)
    iv = w["weg"]["grund"].startswith("konvergiert")
    ok = i and ii and iii and (iv or not mit_konv)
    return bool(ok), {"monoton": bool(i), "sonde_lauf": w["weg"]["sonde_lauf"], "sonde_ok": bool(ii),
                      "E_0": E[0], "E_vor_GF2": ref["E_vor"], "E_ende": E[-1], "E_end_GF2": ref["E_end"],
                      "endenergien_ok": bool(iii), "konvergiert": bool(iv), "grund": w["weg"]["grund"]}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--lauf", default=".")
    p.add_argument("--eingaben", default="../eingaben-gfn1")
    p.add_argument("--aus", default=".")
    args = p.parse_args()
    L = args.lauf
    aus = {"karte": "Z2-SCHUTZ-1 (Runde 49)", "code_sha256": sha_datei(os.path.abspath(__file__)),
           "zeit_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "groessen": {}, "urteile": {}}
    B_plan, L6_plan = {}, {}
    for name, r0, R in GROESSEN:
        t = gtag(r0, R)
        h = lade(os.path.join(L, "hesse-%s.json" % t))
        s_ok, s_txt = hesse_S_ok(h)
        zj = lade(os.path.join(L, "bisekt-%s.json" % t))
        z_frei_T = bool(zj and zj.get("freigabe") and zj["freigabe"]["T_erreicht"] and zj["freigabe"]["E_max_unter_ES"])
        t_ok = hesse_T_ok(h)
        st = lade(os.path.join(L, "start-%s.json" % t))
        g = {"hesse_S_ok": s_ok, "hesse_S": s_txt, "hesse_T_ok": t_ok,
             "E_S": st["E_S"] if st else None, "start_fmax": st["fmax"] if st else None,
             "start_grund": st.get("grund") if st else None}
        werte = {}
        # Verfahren A: Zugverfahren (zug-*.json)
        if zj is None:
            g["zug"] = {"gueltig": False, "status": "fehlt"}
        else:
            okA = bool(zj["gueltig"] and s_ok)
            g["zug"] = {"gueltig": okA, "status": "gueltig" if okA else (
                "S besteht K-Hesse nicht" if not s_ok else "Bisektion ungueltig (keine Klammer, zu wenige Schritte "
                "oder Freigabe erreicht T nicht)"), "barriere": zj.get("barriere"), "klammer": zj.get("klammer"),
                "lambda_lo": zj.get("lambda_lo"), "lambda_hi": zj.get("lambda_hi"), "schritte": zj.get("schritte"),
                "freigabe": zj.get("freigabe"), "fmin_T": zj.get("fmin_T"), "fmin_S": zj.get("fmin_S"),
                "L6": (zj.get("lokalisierung") or {}).get("L6"), "n50": (zj.get("lokalisierung") or {}).get("n50"),
                "laufzeit_s": zj["laufzeit_s"]}
            if okA:
                werte["zug"] = (zj["barriere"], (zj.get("lokalisierung") or {}).get("L6"))
        # Verfahren B: CI-NEB auf dem Zugweg (weg-haupt-*-neb.json)
        w = lade_letzte(L, "weg-haupt-%s-neb" % t)
        ok, txt = weg_gueltig(w, s_ok, z_frei_T)
        g["neb"] = {"gueltig": ok, "status": txt,
                    "barriere": w["barriere"] if w else None, "ki": w["weg"]["ki"] if w else None,
                    "iterationen": w["weg"]["iterationen"] if w else None, "fki": w["weg"]["fki"] if w else None,
                    "fband": w["weg"]["fband"] if w else None,
                    "L6": (w.get("lokalisierung") or {}).get("L6") if w else None,
                    "n50": (w.get("lokalisierung") or {}).get("n50") if w else None,
                    "erstes_sprungbild": w["erstes_sprungbild"] if w else None,
                    "laufzeit_s": w["laufzeit_s"] if w else None}
        if ok:
            werte["neb"] = (w["barriere"], (w.get("lokalisierung") or {}).get("L6"))
        if werte:
            vb = min(werte, key=lambda k: werte[k][0])
            B_plan[name] = werte[vb][0]
            L6_plan[name] = werte[vb][1]
            g["B"] = werte[vb][0]
            g["B_verfahren"] = vb
        else:
            g["B"] = None
        if "zug" in werte and "neb" in werte:
            a, b = werte["zug"][0], werte["neb"][0]
            g["K_weg_rel"] = abs(a - b) / min(a, b) if min(a, b) > 0 else None
            g["K_weg"] = "bestanden" if (g["K_weg_rel"] is not None and g["K_weg_rel"] <= 0.05) else "verfehlt"
        else:
            g["K_weg"] = "nicht auswertbar"
        aus["groessen"][name] = g
    alle = all(n in B_plan for n, _, _ in GROESSEN)
    u = aus["urteile"]
    if alle:
        zs1 = all(2.0 <= B_plan[n] <= 8.0 for n in B_plan)
        u["ZS1"] = {"plan": "eingetroffen" if zs1 else "nicht eingetroffen"}
        bmax, bmin = max(B_plan.values()), min(B_plan.values())
        rel = (bmax - bmin) / bmin if bmin > 0 else None
        u["ZS2"] = {"plan": "eingetroffen" if (rel is not None and rel < 0.20) else "nicht eingetroffen",
                    "rel_aenderung": rel}
        l6ok = all(L6_plan[n] is not None and L6_plan[n] > 0.5 for n in L6_plan)
        u["ZS3"] = {"plan": "eingetroffen" if l6ok else "nicht eingetroffen", "L6": L6_plan}
    else:
        u["ZS1"] = {"plan": "nicht auswertbar"}
        u["ZS2"] = {"plan": "nicht auswertbar"}
        u["ZS3"] = {"plan": "nicht auswertbar", "L6": L6_plan}
    u["ZS1"]["wortlaut"] = u["ZS1"]["plan"]
    u["ZS2"]["wortlaut"] = u["ZS2"]["plan"]
    if "G2" in L6_plan and L6_plan["G2"] is not None:
        u["ZS3"]["wortlaut"] = "eingetroffen" if L6_plan["G2"] > 0.5 else "nicht eingetroffen"
    else:
        u["ZS3"]["wortlaut"] = "nicht auswertbar"
    u["B"] = B_plan
    ref = lade(os.path.join(args.eingaben, "stoss-diamant-so3-T420-e0.01.json"))
    wa = lade_letzte(L, "weg-zs0-neb")
    wb = lade_letzte(L, "weg-zs0-string")
    oka, da = zs0_pruef(wa, ref, True)
    okb, db = zs0_pruef(wb, ref, True)
    okw, dw = zs0_pruef(wa, ref, False)
    u["ZS0"] = {"plan": ("nicht auswertbar" if (oka is None or okb is None)
                         else ("eingetroffen" if (oka and okb) else "nicht eingetroffen")),
                "wortlaut": ("nicht auswertbar" if okw is None else ("eingetroffen" if okw else "nicht eingetroffen")),
                "A": da, "B": db}
    w2 = lade_letzte(L, "weg-so2-neb")
    if w2 is None:
        aus["gegenprobe_so2"] = {"urteil": "nicht auswertbar"}
    else:
        E = w2["weg"]["E_profil"]
        aus["gegenprobe_so2"] = {"urteil": "bestanden" if max(E) > E[0] * (1.0 + 1e-6) else "verfehlt",
                                 "E_0": E[0], "E_max": max(E), "E_ende": E[-1], "sonde_lauf": w2["weg"]["sonde_lauf"],
                                 "grund": w2["weg"]["grund"], "ki": w2["weg"]["ki"]}
    with open(os.path.join(args.aus, "auswertung.json"), "w") as f:
        json.dump(aus, f, indent=1)
    print("auswertung fertig")


if __name__ == "__main__":
    main()
