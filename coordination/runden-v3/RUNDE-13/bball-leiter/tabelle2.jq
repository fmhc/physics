# Zusammenfassungstabelle B-BALL-2 aus der Ausgabe von auswertung2.jq (jq -r -f tabelle2.jq <auswertung2.json>)
def f($n): if . == null then "-" else ((. * pow(10; $n) | round) / pow(10; $n) | tostring) end;
def s3: if . == null then "-" else (. as $v | if ($v | fabs) == 0 then "0" else (($v | fabs | log10 | floor) as $e |
  (($v / pow(10; $e)) * 100 | round / 100 | tostring) + "e" + ($e | tostring)) end) end;
"| Lauf | Ausgang | omega*^2 h = 0,02 / 0,01 | rho* h = 0,02 / 0,01 | Abstand zur Vorhersage (omega^2; rho) | Stufen gleich auf (omega^2; rho) | Umlauf h = 0,02 / 0,01 | groesster Sprung (rad) | Breitenminimum Gamma (Zeile) | Streifen aufgeloest mit Umlauf 0 / ungleich 0 |",
"|---|---|---|---|---|---|---|---|---|---|",
(.je_band | sort_by(.ziel.x)[] | . as $e | ($e.treffer[0] // null) as $t |
  ($e.stufen | map(select(.h == 0.02)) | .[0]) as $a | ($e.stufen | map(select(.h == 0.01)) | .[0]) as $c |
  (if $t == null then
     ([$a.kand[]?, $c.kand[]?] | map(select(((.x - $e.ziel.x) | fabs) <= 0.04)) | .[0]) as $k |
     "| \($e.band) | \($e.ausgang) | \($a.kand[0].x | f(8)) / \($c.kand[0].x | f(8)) | \($a.kand[0].rho | f(8)) / \($c.kand[0].rho | f(8)) | - | - | \($a.kand[0].u // "-") / \($c.kand[0].u // "-") | \($a.kand[0].sprung | f(3)) / \($c.kand[0].sprung | f(3)) | - | \($a.streifen_aufl_u0)+\($c.streifen_aufl_u0) / \(($a.streifen_u_ne0 | length) + ($c.streifen_u_ne0 | length)) |"
   else
     "| \($e.band) | \($e.ausgang) | \($t.x_h002 | f(8)) / \($t.x_h001 | f(8)) | \($t.rho_h002 | f(8)) / \($t.rho_h001 | f(8)) | \($t.dx_vorhersage | f(5)); \($t.drho_vorhersage | f(5)) | \($t.dx_stufen | s3); \($t.drho_stufen | s3) | \($t.u_h002) / \($t.u_h001) | \($t.sprung_h002 | f(3)) / \($t.sprung_h001 | f(3)) | \($e.breitenminimum_h002.Gamma | s3) (\($e.breitenminimum_h002.x)) | \($a.streifen_aufl_u0)+\($c.streifen_aufl_u0) / \(($a.streifen_u_ne0 | length) + ($c.streifen_u_ne0 | length)) |"
   end))
