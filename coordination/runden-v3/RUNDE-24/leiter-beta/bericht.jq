# LEITER-BETA: Berichtstabellen aus lauf-69/auswertung/auswertung.json (nur Darstellung, keine Wertung; nach dem
# Einfrieren geschrieben). Aufruf: jq -r -f bericht.jq lauf-69/auswertung/auswertung.json
def r($n): if . == null then "-" else (. * pow(10; $n) | round / pow(10; $n)) end;
def e($n): if . == null then "-" else (. as $v | if $v == 0 then "0" else
  ((($v | fabs | log10 | floor)) as $p | ($v / pow(10; $p) | r($n)) as $m | "\($m)e\($p)") end) end;
"| k | omega*^2 (h = 0,02) | eps | 1/eps | rho* | c = (rho* - rho_z)/eps | Umlauf h = 0,04 / 0,02 | Schritt zum naechsten k | Stufen-Diff. omega^2 / rho | Kernwachstum Kand. | Runden | groesster Sprung |",
"|---|---|---|---|---|---|---|---|---|---|---|---|",
(.kandidaten as $K | range(0; $K | length) as $i | $K[$i] as $c
  | (if $i + 1 < ($K | length) and $K[$i + 1].eps != null and $c.eps != null then ((1 / $c.eps) - (1 / $K[$i + 1].eps)) | r(4) else "-" end) as $st
  | "| \($c.k) | \($c.x | r(8)) | \($c.eps | r(6)) | \(if $c.eps == null then "-" else ((1 / $c.eps) | r(4)) end) | \($c.rho | r(7)) | \($c.c_wert | r(4)) | \($c.h004.umlauf | r(4)) / \($c.h002.umlauf | r(4)) | \($st) | \($c.d_x_stufen | e(1)) / \($c.d_rho_stufen | e(1)) | \($c.h004.kw | e(1)) / \($c.h002.kw | e(1)) | \($c.h004.runden) / \($c.h002.runden) | \($c.h004.sprung | r(3)) / \($c.h002.sprung | r(3)) |")
