#!/usr/bin/env python3
"""BAG-DIM (Runde 24): mechanische Auswertung nach PLAN.md Abschnitt 5. Code-Agent fuer die Leitung, 03.10.2026.

Aufruf: python auswertung.py <ordner mit s_*.json und b_*.json> <aus.json>
- K0: Plateau-Werte der Spektren (s_*.json).
- Beutel: alle Starts aller Dateien eines Graphen je k zusammen; Wahl wie im Lauf:
  Gitter und Sierpinski = kleinste Energie unter konvergierten kompakten Beuteln am Mittelknoten,
  Zufallsgraph = kleinste Energie unter allen konvergierten Starts.
- Urteile BD0 bis BD4 nach den Regeln des Plans; Tabellen als Text auf stdout.
"""
import glob
import json
import math
import os
import sys

P_SG = 2 * math.log(3) / (2 * math.log(3) + math.log(5))      # d_s/(d_s+1), d_s = 2 ln3/ln5
P_SG_HAUS = math.log(3) / (math.log(3) + math.log(2))         # d_f/(d_f+1)
P_THEO = {"g2": 2.0 / 3.0, "g3": 0.75, "sg": P_SG, "zr": None}
DS_SOLL = {"g2": (2.0, 0.15), "g3": (3.0, 0.15), "sg": (1.365, 0.08)}
SCHRITTE_HALBDEKADE = 4      # Raster 10^(k/8): 4 Schritte = Faktor 10^0,5
SCHRITTE_PERIODE = 8         # Sierpinski-Raster (3 sqrt5)^(j/8): 8 Schritte = eine Periode


def lade(pfad):
    with open(pfad) as fh:
        return json.load(fh)


def spektren(ordner):
    out = {}
    for p in sorted(glob.glob(os.path.join(ordner, "s_*.json"))):
        d = lade(p)
        art = d["graph"]["art"]
        pl = d.get("plateau")
        out[art] = {"datei": os.path.basename(p), "graph": d["graph"]["spec"], "N": d["graph"]["N"],
                    "verfahren": d.get("verfahren"), "plateau": pl, "plateau_ja": d.get("plateau_ja"),
                    "bauprobe": d.get("bauprobe"), "sek": d.get("sek"), "sek_eig": d.get("sek_eig")}
    return out


def urteil_bd0(sp):
    teile = {}
    for art in ("sg", "g2", "g3"):
        if art not in sp or sp[art]["plateau"] is None:
            teile[art] = {"urteil": "offen" if art not in sp else "nicht eingetroffen", "grund": "kein Plateau/Datei"}
            continue
        soll, tol = DS_SOLL[art]
        ds = sp[art]["plateau"]["d_s"]
        ok = bool(sp[art]["plateau_ja"]) and abs(ds - soll) <= tol
        teile[art] = {"d_s": ds, "schwankung": sp[art]["plateau"]["schwankung"], "soll": soll, "tol": tol,
                      "plateau_ja": sp[art]["plateau_ja"], "urteil": "eingetroffen" if ok else "nicht eingetroffen"}
    us = [t["urteil"] for t in teile.values()]
    if all(u == "eingetroffen" for u in us):
        g = "eingetroffen"
    elif any(u == "nicht eingetroffen" for u in us):
        g = "nicht eingetroffen"
    else:
        g = "offen"
    return {"urteil": g, "teile": teile}


def beutel(ordner):
    graphen = {}
    for p in sorted(glob.glob(os.path.join(ordner, "b_*.json"))):
        d = lade(p)
        art = d["graph"]["art"]
        g = graphen.setdefault(art, {"spec": d["graph"]["spec"], "graph": d["graph"], "dateien": [], "k": {}})
        if g["spec"] != d["graph"]["spec"]:
            raise SystemExit(f"zwei Graphen derselben Art: {g['spec']} / {d['graph']['spec']}")
        g["dateien"].append({"datei": os.path.basename(p), "fertig": d.get("fertig"), "abbruch": d.get("abbruch"),
                             "punkte": len(d["punkte"]), "sek": d.get("sek"), "argv": d.get("argv")})
        for pt in d["punkte"]:
            e = g["k"].setdefault(pt["k"], {"Q": pt["Q"], "starts": [], "dEdQ": [], "profil": None})
            if abs(e["Q"] / pt["Q"] - 1) > 1e-12:
                raise SystemExit(f"Q passt nicht: {art} k={pt['k']}")
            for s in pt["starts"]:
                e["starts"].append(dict(s, datei=os.path.basename(p)))
            if "dEdQ" in pt:
                e["dEdQ"].append(pt["dEdQ"])
            if pt.get("profil"):
                e["profil"] = pt["profil"]
    return graphen


def waehle(art, starts):
    if art == "zr":
        kand = [s for s in starts if s["konvergiert"]]
    else:
        kand = [s for s in starts if s["konvergiert"] and s["diag"]["kompakt"]]
    alle = [s for s in starts if s["konvergiert"]]
    a = min(kand, key=lambda s: s["E"]) if kand else None
    t = min(alle, key=lambda s: s["E"]) if alle else None
    return a, t


def laengster_lauf(ks):
    """Laengster zusammenhaengender Lauf; bei Gleichstand der mit groesserem k."""
    ks = sorted(ks)
    best, cur = [], []
    for k in ks:
        if cur and k == cur[-1] + 1:
            cur.append(k)
        else:
            cur = [k]
        if len(cur) >= len(best):
            best = list(cur)
    return best


def sekante(tab, k1, k0):
    return math.log(tab[k1]["E"] / tab[k0]["E"]) / math.log(tab[k1]["Q"] / tab[k0]["Q"])


def auswerten_graph(art, g):
    tab = {}
    for k in sorted(g["k"]):
        e = g["k"][k]
        a, t = waehle(art, e["starts"])
        zeile = {"k": k, "Q": e["Q"], "n_starts": len(e["starts"]),
                 "n_konv": sum(1 for s in e["starts"] if s["konvergiert"])}
        if a is not None:
            d = a["diag"]
            zeile.update({"E": a["E"], "start": a["start"], "omega": d["omega"], "p_omega": d["p_omega"],
                          "nB": d["nB"], "Rg": d["Rg"], "Rs": d.get("Rs"), "Reff": d["Reff"],
                          "chi_zentrum": d["chi_zentrum"], "f2_innen": d["f2_innen"], "kompakt": d["kompakt"],
                          "nicht_fuellend": d["nicht_fuellend"], "teile": d["teile"],
                          "gmax": max(a["gmax_f"], a["gmax_chi"]), "nit": a["nit"]})
        else:
            zeile.update({"E": None})
        if t is not None:
            zeile["tiefster"] = {"start": t["start"], "E": t["E"], "kompakt": t["diag"]["kompakt"],
                                 "nB": t["diag"]["nB"], "dmin": t["diag"]["dmin"], "chi_zentrum": t["diag"]["chi_zentrum"],
                                 "tiefer_als_gewaehlt": bool(a is not None and t["E"] < a["E"] * (1 - 1e-9))}
        # Nebental-Probe: kompakte zentrale Starts, die hoeher liegen
        if art != "zr" and a is not None:
            kz = [s for s in e["starts"] if s["konvergiert"] and s["diag"]["kompakt"]]
            zeile["kompakt_starts"] = [{"start": s["start"], "E": s["E"], "dE_rel": s["E"] / a["E"] - 1,
                                        "nB": s["diag"]["nB"]} for s in kz]
        zeile["dEdQ"] = e["dEdQ"]
        tab[k] = zeile
    ks = sorted(tab)
    # oertliche Exponenten (Nachbarn)
    for k in ks:
        if k + 1 in tab and tab[k]["E"] is not None and tab[k + 1]["E"] is not None:
            tab[k]["p_FD_bis_naechstem"] = sekante(tab, k + 1, k)
    # Bereich
    if art == "zr":
        bereich = []
        for k in ks:
            if tab[k]["E"] is not None and tab[k]["nicht_fuellend"]:
                bereich.append(k)
            else:
                break
        bereich = bereich if bereich and bereich[0] == ks[0] else []
    else:
        bereich = laengster_lauf([k for k in ks if tab[k]["E"] is not None and tab[k]["kompakt"]])
    res = {"art": art, "spec": g["spec"], "graph": g["graph"], "dateien": g["dateien"], "bereich": bereich,
           "tabelle": [tab[k] for k in ks]}
    if bereich:
        q0, q1 = tab[bereich[0]]["Q"], tab[bereich[-1]]["Q"]
        res["bereich_Q"] = [q0, q1]
        res["bereich_dekaden"] = math.log10(q1 / q0)
        res["bereich_R"] = [tab[bereich[0]].get("Reff"), tab[bereich[-1]].get("Reff")]
    # Urteile
    if art in ("g2", "g3", "zr"):
        if len(bereich) > SCHRITTE_HALBDEKADE:
            kt = bereich[-1]
            kl = kt - SCHRITTE_HALBDEKADE
            p_end = sekante(tab, kt, kl)
            res["p_end"] = {"wert": p_end, "k_oben": kt, "k_unten": kl, "Q_oben": tab[kt]["Q"],
                            "Q_unten": tab[kl]["Q"], "p_omega_oben": tab[kt]["p_omega"]}
        else:
            res["p_end"] = None
    if art == "sg":
        res["periodenmittel"] = None
        for n_per in (2, 1):
            schritte = n_per * SCHRITTE_PERIODE
            if len(bereich) > schritte:
                kt = bereich[-1]
                kl = kt - schritte
                res["periodenmittel"] = {"wert": sekante(tab, kt, kl), "perioden": n_per, "k_oben": kt, "k_unten": kl,
                                         "Q_oben": tab[kt]["Q"], "Q_unten": tab[kl]["Q"]}
                break
        # gleitende Ein- und Zwei-Perioden-Sekanten (nur berichtet)
        res["gleitend_1"] = [{"k_oben": k, "p": sekante(tab, k, k - 8)} for k in bereich if k - 8 in bereich]
        res["gleitend_2"] = [{"k_oben": k, "p": sekante(tab, k, k - 16)} for k in bereich if k - 16 in bereich]
    return res


def urteil(art, res):
    if art in ("g2", "g3"):
        pe = res.get("p_end")
        if pe is None:
            return {"urteil": "offen", "grund": "Beutelbereich kuerzer als eine halbe Dekade"}
        soll = P_THEO[art]
        ok = abs(pe["wert"] - soll) <= 0.03
        return {"urteil": "eingetroffen" if ok else "nicht eingetroffen", "p_end": pe["wert"], "soll": soll,
                "abstand": pe["wert"] - soll}
    if art == "sg":
        pm = res.get("periodenmittel")
        if pm is None:
            return {"urteil": "offen", "grund": "weniger als eine volle Periode im Beutelbereich"}
        p = pm["wert"]
        ok = abs(p - 0.577) <= 0.03 and abs(p - 0.577) < abs(p - 0.613)
        return {"urteil": "eingetroffen" if ok else "nicht eingetroffen", "p_mittel": p, "perioden": pm["perioden"],
                "abstand_0577": p - 0.577, "abstand_0613": p - 0.613}
    if art == "zr":
        pe = res.get("p_end")
        if pe is None:
            return {"urteil": "offen", "grund": "Bereich kuerzer als eine halbe Dekade"}
        return {"urteil": "eingetroffen" if pe["wert"] > 0.85 else "nicht eingetroffen", "p_end": pe["wert"]}


def kontrollen(graphen_res, roh):
    out = {}
    # dE/dQ = omega
    rels = []
    for art, g in roh.items():
        for k, e in g["k"].items():
            for d in e["dEdQ"]:
                rels.append({"art": art, "k": k, "Q": e["Q"], "rel": d["rel"], "D": d["D"], "omega": d["omega"]})
    out["dEdQ"] = {"werte": rels, "max_abs_rel": max([abs(r["rel"]) for r in rels]) if rels else None,
                   "bestanden": bool(rels) and all(abs(r["rel"]) <= 1e-4 for r in rels)}
    # Beutelbild 2D: Profil am groessten k mit Profil
    bild = None
    if "g2" in roh:
        ks = sorted(k for k, e in roh["g2"]["k"].items() if e["profil"])
        if ks:
            k = ks[-1]
            pr = roh["g2"]["k"][k]["profil"]
            x, chi = pr["x"], pr["chi"]

            def kreuz(w):
                for i in range(len(x) - 1):
                    if chi[i] < w <= chi[i + 1]:
                        return x[i] + (w - chi[i]) / (chi[i + 1] - chi[i]) * (x[i + 1] - x[i])
                return None
            x10, x50, x90 = kreuz(0.1), kreuz(0.5), kreuz(0.9)
            breite = (x90 - x10) if (x10 is not None and x90 is not None) else None
            bild = {"k": k, "Q": roh["g2"]["k"][k]["Q"], "chi_zentrum": chi[0], "x10": x10, "x50": x50, "x90": x90,
                    "wandbreite_10_90": breite,
                    "bestanden": bool(chi[0] < 0.05 and breite is not None and breite <= 6.0)}
    out["beutelbild_2d"] = bild
    return out


def main():
    ordner, aus = sys.argv[1], sys.argv[2]
    sp = spektren(ordner)
    roh = beutel(ordner)
    res = {art: auswerten_graph(art, g) for art, g in roh.items()}
    urt = {"BD0": urteil_bd0(sp)}
    for nr, art in (("BD1", "g2"), ("BD2", "g3"), ("BD3", "sg"), ("BD4", "zr")):
        urt[nr] = urteil(art, res[art]) if art in res else {"urteil": "offen", "grund": "keine Daten"}
    ko = kontrollen(res, roh)
    out = {"spektren": sp, "urteile": urt, "kontrollen": ko, "graphen": res,
           "theorie": {"p_g2": 2 / 3, "p_g3": 0.75, "p_sg": P_SG, "p_sg_hausdorff": P_SG_HAUS}}
    with open(aus + ".tmp", "w") as fh:
        json.dump(out, fh, indent=1)
    os.replace(aus + ".tmp", aus)
    # Text
    print("== Urteile")
    for nr, u in urt.items():
        print(nr, json.dumps(u, ensure_ascii=False)[:600])
    print("== Kontrollen")
    print("dEdQ max |rel|", ko["dEdQ"]["max_abs_rel"], "bestanden", ko["dEdQ"]["bestanden"])
    print("Beutelbild 2D", json.dumps(ko["beutelbild_2d"]))
    for art, r in res.items():
        print(f"== {art} {r['spec']} Bereich k {r['bereich'][:1]}..{r['bereich'][-1:]} "
              f"Dekaden {r.get('bereich_dekaden')} R {r.get('bereich_R')}")
        print("| k | Q | E | p (Nachbar) | p_omega | omega | nB | Reff/Rg | chi(0) | Start | tiefster anders |")
        for z in r["tabelle"]:
            if z["E"] is None:
                print(f"| {z['k']} | {z['Q']:.5g} | - | | | | | | | kein Beutel | {z.get('tiefster')} |")
                continue
            ti = z.get("tiefster") or {}
            anders = (f"{ti['start']} E={ti['E']:.6g} kompakt={ti['kompakt']} nB={ti['nB']}"
                      if ti.get("tiefer_als_gewaehlt") else "")
            pfd = z.get("p_FD_bis_naechstem")
            print(f"| {z['k']} | {z['Q']:.5g} | {z['E']:.8g} | {'' if pfd is None else f'{pfd:.4f}'} | "
                  f"{z['p_omega']:.4f} | {z['omega']:.5g} | {z['nB']} | {z['Reff']:.2f} | {z['chi_zentrum']:.2g} | "
                  f"{z['start']} | {anders} |")
        if art == "sg":
            print("gleitend_1", [(x["k_oben"], round(x["p"], 4)) for x in r["gleitend_1"]])
            print("gleitend_2", [(x["k_oben"], round(x["p"], 4)) for x in r["gleitend_2"]])


if __name__ == "__main__":
    main()
