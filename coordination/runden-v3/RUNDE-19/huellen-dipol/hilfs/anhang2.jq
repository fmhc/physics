# Liste der Stellen mit Rechteck-Ergebnissen (stellen.json + --slurpfile fin auswertung-final.json)
(($fin[0].stichprobe // {}) + ($fin[0].weitere_rechtecke // {})) as $R |
($R | to_entries | map({key: (.key | capture("nr(?<n>[0-9]+)$").n), value: .value}) | from_entries) as $RN |
[.stellen[] | select(.gezaehlt and .bereich)] | sort_by(-.w2) | .[] | . as $d | ($RN[($d.nr|tostring)]) as $r |
"| \(.nr) | \(.k) | \(.w2 * 1e8 | round / 1e8) | \(.rho * 1e8 | round / 1e8) | \(.R * 1000 | round / 1000) | \(.dw2 * 1e11 | round / 100) | \(.drho * 1e11 | round / 100) | \(.dR * 1e8 | round / 100) | \(.umlauf_1) / \(.umlauf_2) | \(.kn_1 | map(tostring) | join(",")) | \(if $r then "\($r.st1.umlauf // "-") / \($r.st2.umlauf // "-")" + (if ($r.st1.aufgeloest and $r.st2.aufgeloest) then " aufgeloest" else " nicht aufgeloest" end) else "-" end) |"
