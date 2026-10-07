# Markdown-Zeilen der Stellenliste (jq -n -r --slurpfile s aus/laeufe/stellen.json --slurpfile f aus/laeufe/auswertung-final.json -f hilfs/stellentab.jq)
def g(x; n): if x == null then "-" else ((x * pow(10; n) | round) / pow(10; n) | tostring) end;
def r(x): if x == null then "-" elif x.aufgeloest then "\(x.umlauf)" else "\(x.umlauf) nicht aufgeloest" end;
($f[0].rechteck_alle) as $ra
| $s[0].stellen[] | select(.bereich)
| ("S-nr\(.nr)-k\(.k)") as $n
| "| \(.nr) | \(.k) | \(g(.w2; 8)) | \(g(.rho; 8)) | \(g(.R; 3)) | \(g(.dw2 * 1e9; 2)) | \(g(.drho * 1e9; 2)) | \(g(.dR * 1e6; 2)) | \(.umlauf_1) / \(.umlauf_2) | \(.kn_1 | map(tostring) | join(",")) | \(r($ra[$n].st1)) / \(r($ra[$n].st2)) | \(g($ra[$n].st1.sprung; 3)) / \(g($ra[$n].st2.sprung; 3)) | \(if .gezaehlt then "ja" else "nein (" + ((.merker_1 + .merker_2) | unique | join(",")) + ")" end) |"
