# BILDUNG-LEITER, Auswertung Arm M (Code-Agent, nach PLAN.md.eingefroren-20261002-204146, Abschnitt 4).
# Eingabe: eine lin-JSON aus zeit2d_v2.py. Ausgabe je Reihe, Quelle und Fenster eine Zeile (TSV):
# w2 dr reihe quelle t0 t1 Re(band) gamma=-Im(band) amp(band) rel_rest
. as $d
| .analyse[] as $e
| (["projektion", "projektion_k24", "zentrum", "wand"][]) as $q
| ($e[$q] // [])[]
| [$d.w2, $d.dr, $e.reihe, $q, .t0, .t1,
   (if .band then .band.re else "kein_band" end),
   (if .band then (-.band.im) else "kein_band" end),
   (if .band then .band.amp else "-" end),
   (if .band then .band.rel_rest else "-" end)]
| @tsv
