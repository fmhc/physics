# Nur Darstellung: Tabellenzeilen je Fall, Gitter und Zeit aus <stufe>_<gruppe>_<von>-<bis>_ergebnis.json (BILDUNG-2)
# (Aufruf: jq -r --arg s0 0.3 -f tabelle.jq DATEI ..., danach LC_ALL=C sort -t'|' -k2,2 -k4,4n -k3,3r).
# Q/Q_F = Q_net / Q_F des Familienpunkts; Ring/Q_F = Q(r <= 12 bzw. 24) / Q_F am Fensterbeginn; N = Fenstertropfen.
def f(d): if . == null then "-" elif type == "number" then (((. * pow(10; d)) | round) / pow(10; d) | tostring) else tostring end;
def pc(d): if . == null then "-" else ((. * 100) | f(d)) + " %" end;
.stufe as $st
| .ergebnisse[]
| select((.S0 | tostring) == $s0)
| "| \(.fall) | \($st) | \(.T | f(0)) | \(.klasse) | \(.N_fenstertropfen) | \(if .rund == null then "-" elif .rund then "ja" else "nein" end) \(.rmax_zu_ra | f(3)) | \(.Q_anteil_F | f(4)) | \(.Q_ring_F_start | f(4)) | \(.omega_ruhe | f(5)) +- \(.u_omega | f(5)) | \(.E_zu_Q | f(4)) (\(.E_zu_Q_familie | f(4))) | \(.dQ_stern | pc(1)) | \(.EQ_abstand | pc(2)) | \(.omega_abstand | f(4)) | \(.Q_schwankung | pc(1)) | \(.v_mess | f(4)) |"
