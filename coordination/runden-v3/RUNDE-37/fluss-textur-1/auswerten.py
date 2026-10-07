#!/usr/bin/env python3
import json, glob

for datei in glob.glob("lauf_fluss_textur_*.json"):
    with open(datei) as f:
        d = json.load(f)
    print("=== Datei:", datei, "===")
    for lauf in d["daten"]:
        n = lauf["n"]
        for erg in lauf["laeufe"]:
            textur = erg["textur"]
            rahmen = erg["rahmen"]
            k = erg["kaefige"]
            print(f"n={n} | Textur={textur:<10} | w={rahmen:<6} | v_C_minus={k['v_C_minus']} | phi_prod (-1,1,anders)=({k['minus']},{k['plus']},{k['anders']}) | inkonsistent={k['inkonsistent']}")
            
            # Print distances for cages with v_C == -1
            minus_dists = [round(c["dist"], 2) if c["dist"] is not None else None for c in erg["detail"] if c["v_C"] == -1]
            if minus_dists:
                print(f"  -> Abstaende der Quellen: {minus_dists}")
