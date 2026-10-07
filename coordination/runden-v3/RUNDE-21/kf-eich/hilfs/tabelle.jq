# Nur Darstellung: Tabellenzeilen je Ball, Lauf und Zeit aus <stufe>_<gruppe>_ergebnis.json (Aufruf mit --arg s0 0.3).
def f(d): if . == null then "-" elif type == "number" then (((. * pow(10; d)) | round) / pow(10; d) | tostring) else tostring end;
def pc(d): if . == null then "-" else ((. * 100) | f(d)) + " %" end;
.stufe as $st
| .ergebnisse[]
| select((.S0 | tostring) == $s0)
| "| \($st) | \(.ball) | \(.T | f(0)) | \(.klasse) | \(if .rund == null then "-" elif .rund then "ja" else "nein" end) \(.rmax_zu_ra | f(3)) | \(.Q_net | f(3)) | \(.E_ruhe_net | f(3)) | \(.E_zu_Q | f(5)) (\(.E_zu_Q_familie | f(5))) | \(.omega_ruhe | f(5)) +- \(.u_omega | f(6)) | \(.v_mess | f(4)) | \(.dQ_stern | pc(2)) | \(.EQ_abstand | pc(3)) | \(.omega_abstand | f(5)) | \(.d_set | pc(2)) | \(.Q_schwankung | pc(2)) | \(if .satz == "E" and .v == 0 then (.diagnose // "-") else "(nur E0)" end) |"
