# BILDUNG-LEITER, Auswertung Arm G und K0 (Code-Agent, nach PLAN.md.eingefroren-20261002-204146, Abschnitt 4).
# Eingabe: eine nl-JSON aus zeit2d_v2.py. Ausgabe (TSV) je Reihe und Fenster:
# w2 dr reihe K0-Mass t0 t1 gebunden still S_mittel S_spanne schwelle_a  Pencil-Komponenten (re/im/amp, nach amp)
. as $d
| .analyse[] as $e
| ($e.S_zentrum_spektrum // [])[]
| [$d.w2, $d.dr, $e.reihe, $e.S_zentrum_rel_abw_max, .t0, .t1, .anteile.gebunden, .anteile.still, .S_mittel,
   .S_spanne, $d.schwelle_a,
   ([.pencil[] | "\(.re * 10000 | round / 10000)/\(.im * 1e7 | round / 1e7)/\(.amp * 1e6 | round / 1e6)"] | join(" "))]
| @tsv
