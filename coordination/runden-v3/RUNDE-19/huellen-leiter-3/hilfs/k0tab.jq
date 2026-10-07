# K0'-Tabelle aus aus/k0-auswertung.json (Markdown-Zeilen)
def e: if . == null then "-" elif (. | type) == "number" then (if . == 0 then "0" else ((. | fabs | log10 | floor) as $x | ((. / pow(10; $x)) * 10 | round / 10 | tostring) + "e" + ($x | tostring)) end) else tostring end;
def mx(a; b): ([a, b] | map(fabs) | max);
.stellen[] |
"| \(.nr) | \(.k) | \(.R * 100 | round / 100) | \(mx(.st1.dS[0]; .st1.dS[1]) | e) / \(mx(.st2.dS[0]; .st2.dS[1]) | e) | \(mx(.st1.dF[0]; .st1.dF[1]) | e) / \(mx(.st2.dF[0]; .st2.dF[1]) | e) | \(.st1.umlauf_r18) / \(.st2.umlauf_r18) | \(.st1.umlauf_F) / \(.st2.umlauf_F) | \(.st1.aufgeloest_F) / \(.st2.aufgeloest_F) | \(.st1.sprung_F * 1000 | round / 1000) / \(.st2.sprung_F * 1000 | round / 1000) | \(.st1.punkte_F) / \(.st2.punkte_F) | \(.st1.umlauf_S // "-") / \(.st2.umlauf_S // "-") | \(.st1.absW.S | e) / \(.st1.absW.F | e) | \(.st1.svr.F | e) / \(.st2.svr.F | e) | \(.st1.k0a and .st2.k0a and .st1.k0F and .st2.k0F and .st1.k0b and .st2.k0b) |"
