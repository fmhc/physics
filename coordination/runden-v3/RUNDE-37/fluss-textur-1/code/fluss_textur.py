#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""FLUSS-TEXTUR-1: Pruefung der Kaefigprodukte und Fermionfluesse auf dem Diamantnetz.

Importiert gerahmter_faden, twist_spin und twist_pyro.
Berechnet v_C, das Produkt der Fermionfluesse je Kaefig, sowie topologische Defekte
fuer verschiedene Texturen (R0, R1, Igel, Igel-Antiigel) und Rahmen (w).
"""
import math, json, time, os, sys

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import twist_pyro as tp
import twist_spin as ts
import gerahmter_faden as gf

W_HAUPT = (-5.0, 4.0, 0.0)
W_ALT = (-1.0, 0.0, 0.0)
W_ZUFALL = (3.14, -2.71, 1.41)

def norm3(v):
    r = math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
    return (v[0]/r, v[1]/r, v[2]/r) if r > 1e-9 else (0.0, 0.0, 1.0)

def vec_to_q(d):
    # Rotiert (0,0,1) nach d auf kuerzestem Weg
    n = gf.norm3((d[1], -d[0], 0.0))
    if n == (0.0, 0.0, 0.0): return (1.0, 0.0, 0.0, 0.0) if d[2] > 0 else (0.0, 1.0, 0.0, 0.0)
    w = math.acos(max(-1.0, min(1.0, d[2])))
    return gf.qachse(n, w)

def feld_igel(N, zentrum):
    """Radiales Igel-Feld +1 vom Zentrum aus."""
    res = []
    for pos in N.sites:
        d = (pos[0]-zentrum[0], pos[1]-zentrum[1], pos[2]-zentrum[2])
        res.append(vec_to_q(norm3(d)))
    return res

def feld_dipol(N, z1, z2):
    """Igel-Antiigel Dipol (+1 bei z1, -1 bei z2)."""
    res = []
    for pos in N.sites:
        d1 = (pos[0]-z1[0], pos[1]-z1[1], pos[2]-z1[2])
        d2 = (pos[0]-z2[0], pos[1]-z2[1], pos[2]-z2[2])
        r1 = math.sqrt(d1[0]**2 + d1[1]**2 + d1[2]**2)
        r2 = math.sqrt(d2[0]**2 + d2[1]**2 + d2[2]**2)
        if r1 < 1e-9: v = (0.0, 0.0, 1.0)
        elif r2 < 1e-9: v = (0.0, 0.0, -1.0)
        else:
            v = (d1[0]/r1**3 - d2[0]/r2**3,
                 d1[1]/r1**3 - d2[1]/r2**3,
                 d1[2]/r1**3 - d2[2]/r2**3)
        res.append(vec_to_q(norm3(v)))
    return res

def lauf(n, modus):
    Mo = ts.Modell("diamant", n)
    lok = gf.Lokal(Mo)
    nv = len(Mo.N.sites)
    
    texturen = {}
    if modus == "basis":
        texturen["R0"] = gf.feld_R0(Mo.N)
        texturen["Igel"] = feld_igel(Mo.N, (2.0, 2.0, 2.0))
        texturen["Dipol"] = feld_dipol(Mo.N, (2.0, 2.0, 2.0), (n*4-2.0, n*4-2.0, n*4-2.0))
    elif modus == "r1":
        for th in [15, 30, 45, 60]:
            for saat in range(2):
                texturen[f"R1_{th}_{saat}"] = gf.feld_R1(Mo.N, th, saat)

    rahmen = {"haupt": W_HAUPT, "alt": W_ALT, "zufall": W_ZUFALL}
    
    ergebnisse = []
    for t_name, n_feld in texturen.items():
        for w_name, w_vec in rahmen.items():
            st = gf.neues_st()
            konv = gf.konv_B(nv, n_feld, w_vec, (-w_vec[0], -w_vec[1], -w_vec[2]))
            TH, TS = lok.alle(konv, st)
            
            # Phi berechnen (Fermionfluss je Schleife)
            phi, phi_info = ts.fermionfluss(Mo, TH, TS)
            
            # Kaefige auswerten
            kaefig_res = {"plus": 0, "minus": 0, "anders": 0, "v_C_minus": 0, "inkonsistent": 0}
            for c, sel in ts.kaefige(Mo):
                v_C = ts.kaefig_vorzeichen(Mo, TS, sel)
                if v_C == -1: kaefig_res["v_C_minus"] += 1
                
                # Produkt der phi ueber die 4 Flaechen
                phi_prod = 1
                for idx in sel:
                    if phi[idx] is None:
                        phi_prod = 0
                        break
                    phi_prod *= phi[idx]
                
                if phi_prod == 1: kaefig_res["plus"] += 1
                elif phi_prod == -1: kaefig_res["minus"] += 1
                else: kaefig_res["anders"] += 1
                
                if phi_prod != 0 and phi_prod != v_C:
                    kaefig_res["inkonsistent"] += 1
                    
            ergebnisse.append({
                "textur": t_name, "rahmen": w_name,
                "kaefige": kaefig_res, "phi_info": phi_info
            })
            
    return {"n": n, "laeufe": ergebnisse}

if __name__ == "__main__":
    t0 = time.time()
    n_list = [3, 4]
    out = {"meta": {"skript": "fluss_textur.py"}, "daten": []}
    for n in n_list:
        out["daten"].append(lauf(n, "basis"))
    out["zeit_s"] = round(time.time() - t0, 2)
    
    with open("lauf_fluss_textur.json", "w") as f:
        json.dump(out, f, indent=1)
    print(f"Fertig in {out['zeit_s']} s.")
