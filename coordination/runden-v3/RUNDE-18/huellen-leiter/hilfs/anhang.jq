# Anhang A: alle auf beiden Stufen gepaarten Stellen (stellen.json), Markdown-Tabelle
def f(n): if . == null then "-" else (. * pow(10; n) | round / pow(10; n) | tostring) end;
def sci: if . == null then "-" elif . == 0 then "0" else (. as $x | ($x|fabs|log10|floor) as $e | ((($x / pow(10; $e)) * 100 | round / 100 | tostring) + "e" + ($e|tostring))) end;
"| Nr | k | omega^2 (St1) | rho (St1) | R (St1) | omega^2 St2 - St1 | rho St2 - St1 | Zellen-Umlauf St1 / St2 | gezaehlt | bek. (Nr R17) |",
"|---|---|---|---|---|---|---|---|---|---|",
(.stellen[] | select(.bereich) | "| \(.nr) | \(.k) | \(.w2|f(8)) | \(.rho|f(8)) | \(.R|f(3)) | \(.dw2|sci) | \(.drho|sci) | \(.umlauf_1) / \(.umlauf_2) | \(if .gezaehlt then "ja" else "nein" end) | \(.bekannt // "-") |")
