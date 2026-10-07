"""KAUSAL-4D-SCHICHT-2: Zusatzprobe NACH dem Befund (nicht eingefroren, ohne Urteilskraft; ERGEBNIS Selbstanzeige).

Anlass: Die Gitter-Lokalisierung in S (aus SCHICHT-1 uebernommen) nimmt die Randzeile Im omega = 0,002 nicht als Kandidat.
V-00 hat bei rho = 4 eine gezaehlte Nullstelle in S (N_S = 1), die nicht lokalisiert wurde; die Schalennullstelle nach F
liegt bei Im ~ 0,004. Diese Probe prueft unabhaengig, ob die gezaehlte Nullstelle die Schalennullstelle ist:
  1) Windungszahl in einem kleinen Rechteck um die Schalennullstelle (Re +-0,15, Im 0,002 bis 0,05) und im Rest von S
     (S ohne dieses Rechteck, als Differenz zweier Zaehlungen: S gesamt minus Rechteck);
  2) Gittersuche wie SCHICHT-1, aber mit Gitter ab Im = 0,001 (Randzeile 0,002 dann innen);
  3) Newton auf g_I (nicht F) ab der Schalennullstelle.
Aufruf (nur ueber kleintest.sh): zusatz_lokalisierung.py <pole.json> <ausgabe.json> <V00> <rho1,rho2>
"""
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import schicht2_kont as sk  # noqa: E402


def main():
    P = json.load(open(sys.argv[1]))
    aus = sys.argv[2]
    v = sys.argv[3]
    rhos = [float(x) for x in sys.argv[4].split(",")]
    out = {"skript_sha256": __import__("hashlib").sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
           "schicht2_kont_sha256": sk.SKRIPT_SHA, "ergebnisse": {}}
    for r in rhos:
        for k in sk.KS:
            key = f"{v}_rho{r:g}_k{k:.4f}"
            sh = P["ergebnisse"][key]["schale"]
            z0 = complex(sh["omega_re"], sh["omega_im"])
            cs = sk.VAR[v]
            f1 = lambda om: sk.g1(om, k, r, cs)  # noqa: E731
            x1, x2 = z0.real - 0.15, z0.real + 0.15
            klein = sk.zaehle(f1, sk.stuecke_rechteck(x1, x2, 0.002, 0.05))
            gesamt = sk.zaehle(f1, sk.stuecke_rechteck(sk.S_X[0], sk.S_X[1], sk.S_Y[0], sk.S_Y[1]))
            nS = sk.suche(f1, np.arange(sk.S_X[0], sk.S_X[1] + 1e-9, 0.01), np.arange(0.001, sk.S_Y[1] + 1e-9, 0.01),
                          lambda W: np.ones(W.shape, dtype=bool),
                          lambda om: (sk.S_X[0] <= om.real <= sk.S_X[1]) and (sk.S_Y[0] <= om.imag <= sk.S_Y[1]))
            zn, rn = sk.newton(f1, z0)
            out["ergebnisse"][key] = {
                "schale_F": [z0.real, z0.imag],
                "rechteck": [x1, x2, 0.002, 0.05], "zahl_rechteck": klein["zahl"], "stabil_rechteck": klein["stabil"],
                "zahl_S_gesamt": gesamt["zahl"], "stabil_S_gesamt": gesamt["stabil"],
                "gitter_ab_0_001_lokalisiert": [[z.real, z.imag] for z in nS],
                "newton_g1_ab_schale": [zn.real, zn.imag, rn], "abstand_newton_g1": float(abs(zn - z0))}
            print(json.dumps({key: out["ergebnisse"][key]}), flush=True)
    with open(aus, "w") as fh:
        json.dump(out, fh, indent=1)


if __name__ == "__main__":
    main()
