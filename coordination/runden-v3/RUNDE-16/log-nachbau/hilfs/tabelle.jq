# Eingabe: zwei Arrays (Stufe 1, Stufe 2) von Zeilen-JSONs
def sgn: if . > 0 then "+" elif . < 0 then "-" else "0" end;
def r4: (. * 1e5 | round) / 1e5;
def e2: if . == 0 then "0" else (tostring) end;
(.[0] | sort_by(.w2)) as $a | (.[1] | sort_by(.w2)) as $b
| range(0; $b|length) as $i
| $a[$i] as $x | $b[$i] as $y
| [ ($y.w2|tostring),
    ($y.nullstellen|length|tostring) + "/" + ($x.nullstellen|length|tostring),
    ([ $y.nullstellen[] | r4 | tostring ] | join("; ")),
    ([ $y.s[] | sgn ] | join("")),
    ([ $x.s[] | sgn ] | join("")),
    ([ $y.s[] | (. * 1e9 | round / 1e9) | tostring ] | join("; ")),
    (if ($x.nullstellen|length) == ($y.nullstellen|length) and ($y.nullstellen|length) > 0
     then ([ range(0; $y.nullstellen|length) as $k | (($y.nullstellen[$k] - $x.nullstellen[$k]) | fabs) ] | max | tostring)
     else "-" end)
  ] | "| " + join(" | ") + " |"
