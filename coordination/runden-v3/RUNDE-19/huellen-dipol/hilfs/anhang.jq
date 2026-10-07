# Liste der gezaehlten Stellen im Bereich (stellen.json); Differenzen St2 - St1 in Einheiten 1e-9
[.stellen[] | select(.gezaehlt and .bereich)] | sort_by(-.w2) | .[] |
"| \(.nr) | \(.k) | \(.w2 * 1e8 | round / 1e8) | \(.rho * 1e8 | round / 1e8) | \(.R * 1000 | round / 1000) | \(.dw2 * 1e11 | round / 100) | \(.drho * 1e11 | round / 100) | \(.dR * 1e8 | round / 100) | \(.umlauf_1) / \(.umlauf_2) | \(.kn_1 | map(tostring) | join(",")) |"
