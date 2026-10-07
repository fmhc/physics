# l = 0-Lagen je Kurve im Fenster R <= 19,41 (Obergrenze der l = 2-Suche) mit Abstaenden, Mittel, CV (jq -r -f hilfs/l0fenster.jq aus/laeufe/auswertung.json)
def g(x; n): if x == null then "-" else ((x * pow(10; n) | round) / pow(10; n) | tostring) end;
.kurven_l0[] | select(.k <= 4) | . as $e | [$e.R[] | select(. <= 19.41)] as $R
| [range(1; $R | length) | $R[.] - $R[. - 1]] as $d
| ($d | if length > 0 then add / length else null end) as $m
| (if ($d | length) >= 2 then (([$d[] | (. - $m) * (. - $m)] | add / (($d | length) - 1)) | sqrt) / $m else null end) as $cv
| "| \($e.k) | \($R | length) | \([$R[] | g(.; 2)] | join(" ")) | \([$d[] | g(.; 3)] | join(" ")) | \(g($m; 3)) (\(g($cv; 3))) |"
