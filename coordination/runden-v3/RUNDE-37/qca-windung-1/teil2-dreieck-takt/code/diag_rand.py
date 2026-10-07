#!/usr/bin/env python3
# DREIECK-TAKT-1, Diagnose NACH dem Einfrieren (aendert kein Urteil): Randfluss mit anderem k-Gitter (1201 Punkte,
# kein k = 0 im Gitter) und anderer Streifenbreite (41 Zellen), mit Summenprobe N_oben + N_unten + N_bulk = 0
# (det U_streifen = 1, also ist der gesamte spektrale Fluss null). Nutzt die eingefrorenen Funktionen aus teil2.py.
# Start nur auf der .69 ueber kleintest.sh: diag_rand.py --out DATEI.json
import argparse
import json

import teil2 as T2

ap = argparse.ArgumentParser()
ap.add_argument("--out", required=True)
args = ap.parse_args()
out = {}
for name in ("voll", "lam4", "lam3"):
    prot = T2.PROTOKOLLE[name]
    for umk in (False, True):
        b = T2.baender_und_chern(prot, umk)
        rf = T2.randfluss(prot, umk, W=41, Nk=1201, luecken=b["luecken"])
        for v in rf.values():
            v["summe"] = v["N_oben"] + v["N_unten"] + v["N_bulk"]
        out[f"{name}|{'umkehr' if umk else 'vorwaerts'}"] = rf
        print(name, umk, {k: (v["N_oben"], v["N_unten"], v["N_bulk"], v["summe"]) for k, v in rf.items()}, flush=True)
json.dump(out, open(args.out, "w"), indent=1)
