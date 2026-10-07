#!/usr/bin/env python3
"""QBALL-HADRON-1, Auswertung (Regeln in PLAN.md, vor den Hauptlaeufen eingefroren).

Liest:
  --b2d     festq.py radial D = 2 (Weg B, Q-Raster)
  --a2d     RG-1-Kopie, dichte Tabelle h0 = 0,01 (Weg A);  --a2d_l3 dieselbe bei h0 = 0,005
  --rg1bahn RG-1-Kopie, bahn-Auswertung der neu gerechneten Standardtabelle (QH0 Codeweg)
  --d3      festq.py axi3 (eine oder mehrere Dateien, Komma);  --d4  festq.py dop4 (Komma)
  --dl3 / --dl4  DIM-LEITER-QBALL-1 d3.json / d4.json (radiale Referenz fuer m = 0)
Schreibt auswertung.json und auswertung.txt nach --out.
"""
import argparse
import json
import math
import os

import numpy as np

Q_A = (300.0, 400.0, 600.0, 800.0, 1000.0, 1200.0, 1400.0)     # Weg A: nur wo die dichte Tabelle klammert
Q_QH1 = 1000.0
PDG = dict(rho=0.77526, a2=1.3182, rho3=1.6888, a4=1.967)       # GeV, PDG 2024 mass_width_2024.txt


def lade(p):
    with open(p) as f:
        return json.load(f)


def r23(E):
    out = {}
    if all(k in E for k in (0, 1, 2)):
        d1 = E[1] ** 2 - E[0] ** 2
        out["R2"] = (E[2] ** 2 - E[0] ** 2) / d1
        for k in (3, 4):
            if k in E:
                out[f"R{k}"] = (E[k] ** 2 - E[0] ** 2) / d1
        out["dE_verh_2"] = (E[2] - E[0]) / (E[1] - E[0])
    return out


def hermite(x0, x1, y0, y1, d0, d1, x):
    hh = x1 - x0
    t = (x - x0) / hh
    return ((2 * t ** 3 - 3 * t ** 2 + 1) * y0 + (t ** 3 - 2 * t ** 2 + t) * hh * d0 + (-2 * t ** 3 + 3 * t ** 2) * y1
            + (t ** 3 - t ** 2) * hh * d1)


def e_bei_q(punkte, q):
    """punkte: Liste (Q, E, omega, w2) einer Familie; Hermite in Q mit dE/dQ = omega; dazu linear interpoliertes w2."""
    p = sorted(punkte)
    for a, b in zip(p[:-1], p[1:]):
        if a[0] <= q <= b[0]:
            e = hermite(a[0], b[0], a[1], b[1], a[2], b[2], q)
            # Fehlermarke: Hermite gegen lineare Interpolation auf diesem Intervall (nur Groessenordnung)
            t = (q - a[0]) / (b[0] - a[0])
            return dict(E=float(e), w2=float(a[3] + t * (b[3] - a[3])), dQ_intervall=float(b[0] - a[0]),
                        lin_minus_hermite=float(a[1] + t * (b[1] - a[1]) - e))
    return None


def stabil_2d(m, w2, A):
    """HAGEDORN-1/-2 (lineare Stabilitaet, 2D), nur beschreibend."""
    if m == 0:
        return "stabil (m = 0, VK; HAGEDORN-1 HG0)"
    if w2 >= 0.70:
        return "instabil (HAGEDORN-1: jeder Ring ab 0,70)"
    if w2 > 0.55:
        return "unbekannt (0,55 < omega^2 < 0,70 nicht gerechnet)"
    if A is None:
        return "unbekannt"
    if A <= 1.79:
        return "stabil (A-Regel HAGEDORN-2)"
    if A >= 1.99:
        return "instabil (A-Regel HAGEDORN-2)"
    return "Grauzone (1,79 < A < 1,99)"


def weg_b(datei):
    d = lade(datei)
    proQ = {}
    for e in d["ergebnisse"]:
        q = e["Q"]
        f = e["fein"]
        w2 = e["omega_richardson"] ** 2
        A = f.get("A")
        proQ.setdefault(q, {})[e["m1"]] = dict(
            E_R=e["E_richardson"], E_h=f["E"], E_2h=e["grob"]["E"], omega=e["omega_richardson"], w2=w2,
            E_durch_Q=e["E_richardson"] / q, gebunden=bool(e["E_richardson"] < q), A=A,
            R_innen=f.get("R_innen"), R_aussen=f.get("R_aussen"), virial=f["virial_rest"],
            feld=f["feld_rest_max"], rand=f["rand_rel"], dE_fein_grob_rel=e["dE_fein_grob_rel"],
            stabil=stabil_2d(e["m1"], w2, A))
    tab = {}
    for q, mm in sorted(proQ.items()):
        Eg = {m: v["E_R"] for m, v in mm.items() if v["gebunden"] and v["rand"] < 1e-6}
        stab = [m for m in sorted(mm) if mm[m]["stabil"].startswith("stabil")]
        Es = {m: Eg[m] for m in Eg if m in stab}
        tab[str(q)] = dict(m=mm, alle=r23(Eg), nur_stabile=r23(Es), stabile_m=stab,
                           E_h_R2=r23({m: v["E_h"] for m, v in mm.items()}).get("R2"),
                           E_2h_R2=r23({m: v["E_2h"] for m, v in mm.items()}).get("R2"))
    return tab


def weg_a(datei):
    d = lade(datei)
    fam = {}
    for z in d["tabelle"]["zeilen"]:
        if z["nls"] or not z.get("gueltig") or abs(z.get("virial", 1.0)) > 1e-5:
            continue
        fam.setdefault(z["m"], []).append((z["Q"], z["E"], z["omega"], z["w2"]))
    tab = {}
    for q in Q_A:
        E, info = {}, {}
        for m, pp in sorted(fam.items()):
            r = e_bei_q(pp, q)
            if r is not None:
                E[m] = r["E"]
                info[str(m)] = r
        tab[str(q)] = dict(E={str(m): v for m, v in E.items()}, info=info, **r23(E))
    ungueltig = [dict(m=z["m"], w2=z["w2"], grund=z.get("grund")) for z in d["tabelle"]["zeilen"] if not z.get("gueltig")]
    return dict(Q=tab, ungueltige_zeilen=ungueltig, zeilen=len(d["tabelle"]["zeilen"]))


def ref_radial(datei, D):
    """DIM-LEITER: Q, E, omega je omega^2 (feines Gitter) -> Funktion E(Q) per Hermite (unterer Ast, omega < omega_c)."""
    d = lade(datei)
    pkt = d["ergebnisse"][str(D)]["fein"]["punkte"]
    pp = [(p["Q"], p["E"], p["omega"], p["om2"]) for p in pkt]
    # nur der monotone untere Ast: Q faellt mit omega^2 bis zum Minimum
    pp.sort(key=lambda t: t[3])
    ast = []
    for t in pp:
        if ast and t[0] > ast[-1][0]:
            break
        ast.append(t)
    return lambda q: e_bei_q(ast, q)


def gitter(dateien, ref, D):
    out = {}
    for datei in dateien:
        d = lade(datei)
        for e in d["ergebnisse"]:
            q = e["Q"]
            f = e["fein"]
            key = f"{e['m1']},{e['m2']}"
            eintrag = dict(E_R=e["E_richardson"], E_h=f["E"], E_2h=e["grob"]["E"], omega=e["omega_richardson"],
                           E_durch_Q=e["E_richardson"] / q, gebunden=bool(e["E_richardson"] < q and f["rand_rel"] < 1e-4
                                                                      and e["omega_richardson"] < 1.0),
                           virial=f["virial_rest"], feld=f["feld_rest_max"], rand=f["rand_rel"],
                           dE_fein_grob_rel=e["dE_fein_grob_rel"], h=f["h"], n=f["n"],
                           form={k: f.get(k) for k in ("x_max", "y_max", "x_halb_innen", "x_halb_aussen",
                                                       "y_halb_innen", "y_halb_aussen", "A_x", "T_x_max", "T_y_max",
                                                       "T_mitte_durch_max", "S_mitte_durch_max")},
                           J1=e["J1"], J2=e["J2"])
            if key == "0,0" and ref is not None:
                r = ref(q)
                if r is not None:
                    eintrag["ref_radial_E"] = r["E"]
                    eintrag["ref_abw_rel"] = (e["E_richardson"] - r["E"]) / r["E"]
            out.setdefault(str(q), {})[key] = eintrag
    tab = {}
    for q, mm in sorted(out.items(), key=lambda kv: float(kv[0])):
        g = {k: v["E_R"] for k, v in mm.items() if v["gebunden"]}
        z = dict(m=mm)
        if D == 3:
            E = {int(k.split(",")[0]): v for k, v in g.items()}
            z.update(r23(E))
            z["alle_gebunden"] = all(v["gebunden"] for v in mm.values())
        else:
            if all(k in g for k in ("0,0", "1,0", "2,0")):
                E0 = g["0,0"]
                d10 = g["1,0"] ** 2 - E0 ** 2
                d20 = g["2,0"] ** 2 - E0 ** 2
                z["R2_m0"] = d20 / d10
                if "1,1" in g:
                    z["K"] = (g["1,1"] ** 2 - E0 ** 2) / d20
                    z["E11_minus_E20"] = g["1,1"] - g["2,0"]
            z["alle_gebunden"] = all(v["gebunden"] for v in mm.values())
        tab[q] = z
    return tab


def pdg():
    M2 = {k: v * v for k, v in PDG.items()}
    d1 = M2["a2"] - M2["rho"]
    return dict(R2=(M2["rho3"] - M2["rho"]) / d1, R3=(M2["a4"] - M2["rho"]) / d1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--b2d", required=True)
    ap.add_argument("--a2d", required=True)
    ap.add_argument("--a2d_l3", required=True)
    ap.add_argument("--rg1bahn", required=True)
    ap.add_argument("--d3", required=True)
    ap.add_argument("--d4", required=True)
    ap.add_argument("--dl3", required=True)
    ap.add_argument("--dl4", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    B = weg_b(a.b2d)
    A = weg_a(a.a2d)
    A2 = weg_a(a.a2d_l3)
    bahn = lade(a.rg1bahn)
    rot = bahn["auswertung"]["rotor"] if "auswertung" in bahn else bahn.get("rotor")
    exp300 = rot["300.0"]["exponent_dE_gegen_m"]["steigung"]
    exp1000 = rot["1000.0"]["exponent_dE_gegen_m"]["steigung"]
    T3 = gitter(a.d3.split(","), ref_radial(a.dl3, 3), 3)
    T4 = gitter(a.d4.split(","), ref_radial(a.dl4, 4), 4)
    # Vergleich Weg A gegen Weg B
    ab = {}
    for q, za in A["Q"].items():
        zb = B.get(q)
        if zb is None:
            continue
        ab[q] = {m: (za["E"][m] - zb["m"][int(m)]["E_R"]) / zb["m"][int(m)]["E_R"] for m in za["E"]
                 if int(m) in zb["m"]}
    l3 = {}
    for q, za in A["Q"].items():
        zb = A2["Q"].get(q)
        if zb and "R2" in za and "R2" in zb:
            l3[q] = dict(dR2=za["R2"] - zb["R2"], dR3=(za.get("R3", float("nan")) - zb.get("R3", float("nan"))))
    # QH0 und QH1 nach den Regeln in PLAN.md Abschnitt 5
    qh0 = dict(datenweg_exponent=0.8988705813012974, codeweg_exponent_300=exp300, codeweg_exponent_1000=exp1000,
               urteil=("eingetroffen" if abs(exp300 - 0.899) <= 0.01 else "nicht eingetroffen"))
    zq = B.get(str(Q_QH1), dict(nur_stabile={}, alle={}, stabile_m=[]))
    za = A["Q"].get(str(Q_QH1), {})
    r2b = zq["nur_stabile"].get("R2")
    r2a = za.get("R2")
    qh1 = dict(Q=Q_QH1, stabile_m=zq["stabile_m"], R2_wegB=r2b, R2_wegA=r2a, R3_wegB_alle=zq["alle"].get("R3"),
               R3_wegA=za.get("R3"),
               urteil=("eingetroffen" if (r2b is not None and abs(r2b - 2.0) <= 0.2) else
                       ("nicht eingetroffen" if r2b is not None else "nicht auswertbar")),
               A_B_einig=(abs(r2a - r2b) <= 1e-3 if (r2a is not None and r2b is not None) else None))
    # Q-Band: R2 ueber alle Q, deren m = 0, 1, 2 nach HAGEDORN stabil sind
    band = {q: z["nur_stabile"].get("R2") for q, z in B.items()
            if all(m in z["stabile_m"] for m in (0, 1, 2))}
    erg = dict(weg_b_2d=B, weg_a_2d=A, weg_a_2d_l3=A2, a_gegen_b_rel=ab, l3_wegA=l3, d3=T3, d4=T4, pdg=pdg(),
               qh0=qh0, qh1=qh1, r2_stabiles_band=band)
    with open(os.path.join(a.out, "auswertung.json"), "w") as f:
        json.dump(erg, f, indent=1, sort_keys=True)
    z = ["QBALL-HADRON-1 Auswertung", f"PDG: {erg['pdg']}", f"QH0: {qh0}", f"QH1: {qh1}",
         f"R2 im stabilen Band (2D, m = 0..2 stabil): {band}", "", "2D Weg B (Richardson):"]
    for q, zz in B.items():
        z.append(f" Q = {q}: R2 alle {zz['alle'].get('R2')}, R3 {zz['alle'].get('R3')}, R4 {zz['alle'].get('R4')}; "
                 f"nur stabile {zz['nur_stabile']} (m {zz['stabile_m']}); R2 aus h {zz['E_h_R2']}, aus 2h {zz['E_2h_R2']}")
        for m, v in zz["m"].items():
            z.append(f"   m = {m}: E = {v['E_R']:.6f}, E/Q = {v['E_durch_Q']:.5f}, omega^2 = {v['w2']:.5f}, A = {v['A']}, "
                     f"{v['stabil']}; virial {v['virial']:.1e}, rand {v['rand']:.1e}, fein-grob {v['dE_fein_grob_rel']:.1e}")
    z.append("2D Weg A (RG-1 dicht, Hermite):")
    for q, zz in A["Q"].items():
        z.append(f" Q = {q}: R2 {zz.get('R2')}, R3 {zz.get('R3')}, R4 {zz.get('R4')}, E {zz['E']}")
    z.append(f" A gegen B (relativ): {ab}")
    z.append(f" L3 Weg A (h0 0,01 gegen 0,005): {l3}")
    z.append(f" ungueltige Zeilen Weg A: {A['ungueltige_zeilen']}")
    for name, T in (("3D", T3), ("4D", T4)):
        z.append(f"{name}:")
        for q, zz in T.items():
            kurz = {k: v for k, v in zz.items() if k != "m"}
            z.append(f" Q = {q}: {kurz}")
            for k, v in zz["m"].items():
                z.append(f"   ({k}): E = {v['E_R']:.4f}, E/Q = {v['E_durch_Q']:.5f}, gebunden {v['gebunden']}, "
                         f"omega {v['omega']:.5f}, rand {v['rand']:.1e}, virial {v['virial']:.1e}, "
                         f"fein-grob {v['dE_fein_grob_rel']:.1e}, ref {v.get('ref_abw_rel')}, form {v['form']}")
    with open(os.path.join(a.out, "auswertung.txt"), "w") as f:
        f.write("\n".join(z) + "\n")
    print("\n".join(z))


if __name__ == "__main__":
    main()
