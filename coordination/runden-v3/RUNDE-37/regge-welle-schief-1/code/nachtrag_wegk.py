#!/usr/bin/env python3
"""REGGE-WELLE-SCHIEF-1, Nachtrag (beschreibend, nach dem Einfrieren, nicht geurteilt):
Gegenprobe Weg K (komplexer Schritt mit schiefen Laengen) an den Ueberlicht-Richtungen fib10 und fib01, s = 0,2.
Importiert den eingefrorenen Code unveraendert (regge_welle_schief.analyse_s, eK_schief).

Aufruf: python nachtrag_wegk.py <ausgabe.json>
"""
import json
import os
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import regge4d as R4  # noqa: E402
import regge_welle as RW  # noqa: E402
import regge_schief as RS  # noqa: E402
import regge_welle_schief as WS  # noqa: E402


def main():
    ziel = sys.argv[1]
    s = 0.2
    git = RS.GitterSchief(RS.matrix_A(s))
    eT, _, _ = git.ableitung_T()
    B = git.B0()
    basis, _ = git.sym_basis()
    Ckomp, _ = R4.komplement(git, B)
    formen = (("T", RW.Form(git, eT)), ("K", RW.Form(git, WS.eK_schief(git))))
    R = dict(RW.richtungen())
    out = []
    for nm in ("fib10", "fib01"):
        for kb in (0.05, 0.4, 0.8):
            row = {"richtung": nm, "betrag": kb}
            for name, form in formen:
                a = WS.analyse_s(git, form, eT, B, basis, Ckomp, nm, R[nm], kb, False, mit_extra=False)
                row[name] = [[x["re"], x["im"]] for x in a["nullstellen"]]
                row[name + "_v"] = [x["v_re"] for x in a["nullstellen"]]
                row[name + "_windung"] = a["windung"]["windung"]
            row["max_abw_v"] = max(abs(x - y) for x, y in zip(row["T_v"], row["K_v"])) \
                if len(row["T_v"]) == len(row["K_v"]) else None
            print(nm, kb, row["T_v"], row["K_v"], row["max_abw_v"], flush=True)
            out.append(row)
    with open(ziel, "w") as f:
        json.dump({"s": s, "skript_sha256": WS.SKRIPT_SHA, "punkte": out}, f, indent=1)
    print("geschrieben", ziel, flush=True)


if __name__ == "__main__":
    main()
