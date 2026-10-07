# Fortsetzung (quadratisch in 1/R durch die letzten drei bekannten Stellen mit R < R_ziel - 1, hier R_ziel = R18-Ende + 1 Schritt
# bzw. nur R18-Stellen) gegen die Zeilennullstellen mit Rang k aus HUELLEN-LEITER-3 (Stufe 1). Nur Kurvenlagen.
def lag3(p; R): (1/R) as $x0 | [p[] | {x: (1/.R), y: .rho}] as $q |
  reduce range(0;3) as $i (0; . + ($q[$i].y * (reduce range(0;3) as $j (1; if $j == $i then . else . * (($x0 - $q[$j].x)/($q[$i].x - $q[$j].x)) end))));
$bek[0].stellen as $b |
[ ($t + $t2)[] | .sprossen[] | .versuche[-1] | select(.kurve.rho_null) | {R: .S.Rchi, z: .kurve.rho_null} ] | unique_by(.R) | .[] as $row |
range(4;8) as $k |
([ $b[] | select(.k == $k and (.quelle|startswith("R18"))) ] | sort_by(.R) | .[-3:]) as $p |
lag3($p; $row.R) as $f |
($row.z[$k] - $f) as $err |
([ ($row.z[$k] - $row.z[$k-1]), ($row.z[$k+1] - $row.z[$k]) ] | min) as $dnb |
[$k, ($row.R*1000|round/1000), ($p|map(.quelle)|join(",")), $row.z[$k], $f, $err, $dnb, (($err|length)/$dnb)] | @tsv
