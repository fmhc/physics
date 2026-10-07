#!/usr/bin/env python3
"""RUNDE-35, PEITSCHE-1: mechanische Urteile nach PLAN.md (eingefroren), Abschnitte A.4 und B.3.

Aufruf: python3 auswertung.py --lauf lauf --out lauf/auswertung.json
Erwartet lauf/a_<d>_<R0>_{fein,grob}/zusammenfassung.json und lauf/b_{h0005,h001}/teil_b.json.
"""
import argparse
import datetime
import json
import math
import os

A_LAEUFE = ("a_d2_R80", "a_d2_R40", "a_d2_R20", "a_d3_R40", "a_d3_R20")
E_TOL = 1e-4
RATIO_TOL = 1.0 + 1e-6
A1_TOL = 0.02
A2_TOL = 0.02
A3_SCHWELLE = 0.99
A5_ANTEIL = 0.05
A5_FREQ = math.sqrt(2.0)
B0_J = 1e-8
B0_QE = 1e-5
B1_TOL = 1e-12
B2_LO, B2_HI = 0.35, 0.65
B3_M = (3, 5, 8)
W2_RAND = (0.52, 0.99)


def lade(pfad):
    if not os.path.exists(pfad):
        return None
    with open(pfad) as fh:
        return json.load(fh)


def urteile_a(lauf, gitter):
    L = {}
    for n in A_LAEUFE:
        z = lade(os.path.join(lauf, f"{n}_{gitter}", "zusammenfassung.json"))
        L[n] = z["messung"] if z else None
    U = {}

    def a0_lauf(m):
        return (m is not None and m.get("t_c") is not None and m["E_fehler_bis_tc"] < E_TOL
                and m["ratio_max_jederzeit"] <= RATIO_TOL)

    # A0
    if any(L[n] is None or L[n].get("t_c") is None for n in A_LAEUFE):
        U["A0"] = dict(urteil="nicht auswertbar", vermerk="Lauf oder t_c fehlt: " +
                       ", ".join(n for n in A_LAEUFE if L[n] is None or L[n].get("t_c") is None))
    else:
        w = {n: dict(E_fehler_bis_tc=L[n]["E_fehler_bis_tc"], ratio_max=L[n]["ratio_max_jederzeit"]) for n in A_LAEUFE}
        ok = all(a0_lauf(L[n]) for n in A_LAEUFE)
        U["A0"] = dict(urteil="eingetroffen" if ok else "nicht eingetroffen", werte=w)
    # A1
    n1 = ("a_d2_R40", "a_d2_R80", "a_d3_R40")
    if any(L[n] is None or L[n].get("t_c") is None for n in n1):
        U["A1"] = dict(urteil="nicht auswertbar")
    else:
        w = {n: dict(t_c=L[n]["t_c"], t_c_duenn=L[n]["tc_duenn"], rel_abw=L[n]["t_c_rel_abw"]) for n in n1}
        ok = all(abs(L[n]["t_c_rel_abw"]) <= A1_TOL for n in n1)
        U["A1"] = dict(urteil="eingetroffen" if ok else "nicht eingetroffen", werte=w)
    # A2, A3
    m80 = L["a_d2_R80"]
    if m80 is None or m80.get("t_c") is None or any(m80["v_bei_R"][k]["v"] is None for k in ("R0/2", "R0/4", "R0/10")):
        U["A2"] = dict(urteil="nicht auswertbar")
    else:
        w = {k: dict(v=m80["v_bei_R"][k]["v"], v_duenn=m80["v_bei_R"][k]["v_duenn"], rel_abw=m80["v_bei_R"][k]["rel_abw"])
             for k in ("R0/2", "R0/4", "R0/10")}
        ok = all(abs(w[k]["rel_abw"]) <= A2_TOL for k in w)
        U["A2"] = dict(urteil="eingetroffen" if ok else "nicht eingetroffen", werte=w)
    if m80 is None or m80.get("t_c") is None or m80.get("v_max_R_ab_2") is None:
        U["A3"] = dict(urteil="nicht auswertbar")
    else:
        w = m80["v_max_R_ab_2"]
        U["A3"] = dict(urteil="eingetroffen" if w["v"] > A3_SCHWELLE else "nicht eingetroffen", werte=w)
    # A4
    if any(L[n] is None or L[n].get("t_c") is None or L[n].get("musterschnelle") is None for n in A_LAEUFE):
        U["A4"] = dict(urteil="nicht auswertbar")
    else:
        w = {n: dict(musterschnelle=L[n]["musterschnelle"]["s"], paar=[L[n]["musterschnelle"]["t0"],
                                                                         L[n]["musterschnelle"]["t1"]],
                     R_paar=[L[n]["musterschnelle"]["R0_paar"], L[n]["musterschnelle"]["R1_paar"]],
                     A0_im_lauf=a0_lauf(L[n]), v_inst_max=(L[n]["v_inst_max_fenster"] or {}).get("v"))
             for n in A_LAEUFE}
        schlecht = [n for n in A_LAEUFE if not (w[n]["musterschnelle"] > 1.0 and w[n]["A0_im_lauf"])]
        U["A4"] = dict(urteil="eingetroffen" if not schlecht else "nicht eingetroffen", werte=w)
        if schlecht:
            U["A4"]["vermerk"] = "nicht erfuellt in: " + ", ".join(schlecht)
    # A5
    m20 = L["a_d2_R20"]
    if m20 is None or m20.get("t_c") is None or m20.get("nach_E_lok_anteil") is None or m20.get("nach_frequenz") is None:
        U["A5"] = dict(urteil="nicht auswertbar")
    else:
        w = dict(E_lok_anteil=m20["nach_E_lok_anteil"], omega_peak=m20["nach_frequenz"]["omega_peak"],
                 frequenz=m20["nach_frequenz"])
        ok = w["E_lok_anteil"] >= A5_ANTEIL and w["omega_peak"] < A5_FREQ
        U["A5"] = dict(urteil="eingetroffen" if ok else "nicht eingetroffen", werte=w)
    return U


def urteile_b(lauf, name):
    T = lade(os.path.join(lauf, name, "teil_b.json"))
    U = {}
    if T is None:
        for k in ("B0", "B1", "B2", "B3"):
            U[k] = dict(urteil="nicht auswertbar", vermerk=f"{name} fehlt")
        return U
    Z = T["zeilen"]
    gueltig = [z for z in Z if z["gueltig"] and z.get("vE_max") is not None]
    ungueltig = [dict(m=z["m"], w2=z["w2"], grund=z["grund"]) for z in Z if not (z["gueltig"] and z.get("vE_max") is not None)]
    verm_ung = ("ungueltige Zeilen: " + "; ".join(f"m={u['m']}, w2={u['w2']}: {u['grund']}" for u in ungueltig)) \
        if ungueltig else None
    # B0
    gp = T["gitterprobe"]
    jmax = max((abs(p["J_durch_mQ_minus_1"]) for p in gp), default=None)
    gem = [z for z in gueltig if z.get("rg1", {}).get("rg1_gueltig")]
    qmax = max((abs(z["rg1"]["Q_rel"]) for z in gem), default=None)
    emax = max((abs(z["rg1"]["E_rel"]) for z in gem), default=None)
    if jmax is None or qmax is None or len(gp) < 20:
        U["B0"] = dict(urteil="nicht auswertbar", werte=dict(n_gitter=len(gp), n_gemeinsam=len(gem)))
    else:
        ok = jmax <= B0_J and qmax <= B0_QE and emax <= B0_QE
        U["B0"] = dict(urteil="eingetroffen" if ok else "nicht eingetroffen",
                       werte=dict(J_mQ_max=jmax, Q_rel_max=qmax, E_rel_max=emax, n_gitter=len(gp), n_gemeinsam=len(gem)))
    # B1
    if not gueltig:
        U["B1"] = dict(urteil="nicht auswertbar")
    else:
        d = max(z["vE_minus_schranke_max"] for z in gueltig)
        q = max(z["vE_durch_schranke"] for z in gueltig)
        U["B1"] = dict(urteil="eingetroffen" if d <= B1_TOL else "nicht eingetroffen",
                       werte=dict(max_vE_minus_schranke=d, max_vE_durch_schranke=q))
    # B2
    if not gueltig:
        U["B2"] = dict(urteil="nicht auswertbar")
    else:
        zb = max(gueltig, key=lambda z: z["vE_max"])
        ok = B2_LO <= zb["vE_max"] <= B2_HI
        U["B2"] = dict(urteil="eingetroffen" if ok else "nicht eingetroffen",
                       werte=dict(vE_max=zb["vE_max"], m=zb["m"], w2=zb["w2"], r=zb["r_bei_vE_max"]))
    # B3
    w3 = {}
    auswertbar = True
    ok = True
    for m in B3_M:
        zm = sorted([z for z in gueltig if z["m"] == m], key=lambda z: z["w2"])
        w2s = [round(z["w2"], 6) for z in zm]
        if not all(round(r, 6) in w2s for r in W2_RAND):
            auswertbar = False
            w3[str(m)] = dict(fehlt="Randzeile ungueltig oder fehlt")
            continue
        zb = max(zm, key=lambda z: z["vE_max"])
        innen = W2_RAND[0] < zb["w2"] < W2_RAND[1]
        ok = ok and innen
        w3[str(m)] = dict(w2_bei_max=zb["w2"], vE_max=zb["vE_max"],
                          vE_bei_099=next(z["vE_max"] for z in zm if abs(z["w2"] - 0.99) < 1e-9), innen=innen)
    U["B3"] = dict(urteil=("nicht auswertbar" if not auswertbar else ("eingetroffen" if ok else "nicht eingetroffen")),
                   werte=w3)
    if verm_ung:
        for k in ("B1", "B2", "B3"):
            U[k]["vermerk"] = verm_ung
    return U


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lauf", default="lauf")
    ap.add_argument("--out", default="lauf/auswertung.json")
    args = ap.parse_args()
    fa = urteile_a(args.lauf, "fein")
    ga = urteile_a(args.lauf, "grob")
    fb = urteile_b(args.lauf, "b_h0005")
    gb = urteile_b(args.lauf, "b_h001")
    urteile = {}
    for k in ("A0", "A1", "A2", "A3", "A4", "A5"):
        u = dict(fa[k])
        u["grob"] = dict(urteil=ga[k]["urteil"], werte=ga[k].get("werte"))
        if ga[k]["urteil"] != fa[k]["urteil"]:
            u["vermerk"] = ((u.get("vermerk") + "; ") if u.get("vermerk") else "") + \
                f"nicht konvergiert (grobes Gitter: {ga[k]['urteil']})"
        urteile[k] = u
    for k in ("B0", "B1", "B2", "B3"):
        u = dict(fb[k])
        u["grob"] = dict(urteil=gb[k]["urteil"], werte=gb[k].get("werte"))
        if gb[k]["urteil"] != fb[k]["urteil"]:
            u["vermerk"] = ((u.get("vermerk") + "; ") if u.get("vermerk") else "") + \
                f"nicht konvergiert (h0 = 0,01: {gb[k]['urteil']})"
        urteile[k] = u
    aus = dict(karte="PEITSCHE-1", erstellt=datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
               regeln="PLAN.md (eingefroren), Abschnitte A.4 und B.3; Urteilsgitter fein bzw. h0 = 0,005",
               urteile=urteile)
    with open(args.out, "w") as fh:
        json.dump(aus, fh, indent=1, ensure_ascii=False)
    for k, u in urteile.items():
        print(k, u["urteil"], "|", u.get("vermerk", ""))


if __name__ == "__main__":
    main()
