# Eingabe: [rand.json, haupt2d.json] per --slurpfile; Ausgabe: Vergleich fester Rand gegen periodisch (E_inf)
def median: sort | if length == 0 then null else .[(length/2|floor)] end;
def pick(arr; d): [arr[] | select((.[0] - d) | fabs < 1e-6)][0][1];
$r[0] as $R | $h[0] as $H |
[ ("M-iso","M-aniso2") as $m |
  ("AA","BB_par") as $k |
  (if $m == "M-iso" then ("0","30") else ("0","45") end) as $dn |
  ($R[$m]["50"].N) as $N1 | ($R[$m]["100"].N) as $N2 |
  ($R[$m]["50"].E[$k][$dn]) as $e1 | ($R[$m]["100"].E[$k][$dn]) as $e2 |
  ([ $e2[] | select(.[0] >= 3 and .[0] <= 8) | . as $p | (pick($e1; $p[0])) as $v1 | select($v1 != null) | (($v1 - $p[1]) / (1/$N1 - 1/$N2)) ] | median) as $b |
  ($H[$m].analyse[$k].richtungen[$dn]) as $P |
  ([ $P.d, $P.E_inf ] | transpose) as $per |
  { medium: $m, paar: $k, richtung: $dn, b_fest: $b, b_period: $H[$m].analyse[$k].b_benutzt,
    vergleich: [ (5, 10, 20) as $d |
       (pick($e2; $d)) as $ef | (pick($per; $d)) as $ep |
       if ($ef == null or $ep == null) then {d: $d, fehlt: true} else
       { d: $d, E_fest_roh: $ef, E_fest_inf: ($ef - $b/$N2), E_period_inf: $ep,
         rel_abw: ((($ef - $b/$N2) - $ep) / $ep) } end ] } ]
