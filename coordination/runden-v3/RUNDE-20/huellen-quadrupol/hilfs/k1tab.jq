# Markdown-Zeilen der K1-Tabelle aus aus/laeufe/k1-l*-st*.json (Aufruf: jq -r -f hilfs/k1tab.jq <dateien>)
def e(x): if x == null then "-" else (x | tostring) end;
def g(x; n): if x == null then "-" else ((x * pow(10; n) | round) / pow(10; n) | tostring) end;
def s(x): if x == null then "-" else (x | fabs | if . == 0 then "0" else (. | log10 | floor) as $p | ((. / pow(10; $p) * 10 | round) / 10 | tostring) + "e" + ($p | tostring) end) end;
.stufe as $st | .ell as $l | .stellen[]
| "| \($l) | \(.name) | \(.k) | \(.i) | \($st) | \(e(.gefunden)) | \(e(.zelle.umlauf_zelle)) | \(g(.newton.w2; 10)) / \(g(.newton.rho; 10)) | \(s(.d_ref[0])) / \(s(.d_ref[1])) | \(e(.umlauf.umlauf)) \(if .umlauf.aufgeloest then "aufgeloest" else "NICHT aufgeloest" end) | \(g(.umlauf.sprung; 3)) | \(e(.umlauf.punkte)) | \(s(.newton.svr)) | \(if .ok then "ja" else "NEIN" end) |"
