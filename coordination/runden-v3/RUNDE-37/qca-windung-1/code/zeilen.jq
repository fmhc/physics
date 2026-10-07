# QCA-WINDUNG-1: Markdown-Zeilen je Automat (nur Anzeige, jq). Aufruf: jq -r -f zeilen.jq DATEI.json
def r6: . * 1e6 | round / 1e6;
def ort: .t as $t
  | ($t | map(. - ($t[0])) | map(if . > 0.5 then . - 1 elif . < -0.5 then . + 1 else . end) | map(fabs) | max) as $d
  | if $d > 1e-6 then "allg."
    else ($t[0] | if fabs < 1e-6 or fabs > 1 - 1e-6 then "Gamma" elif fabs - 0.25 | fabs < 1e-6 then "P"
          elif fabs - 0.5 | fabs < 1e-6 then "H" elif fabs - 0.75 | fabs < 1e-6 then "P'" else "allg." end) end;
.automaten[]
| [ (.name | gsub("[|]"; " ")), (.s|tostring), (if .inversion.inversion then "ja" else "nein" end),
    ((.w3.gitter // {}) | [.["16"].W3, .["24"].W3, .["32"].W3, .["48"].W3] | map(if . == null then "-" else (r6|tostring) end) | join(" / ")),
    (if .trivial then "trivial" elif .weyl == null then "-" else
       "\(.weyl.anzahl[0])/\(.weyl.anzahl[1])" + (if .weyl.vollstaendig then " voll." else " unvoll." end) end),
    (if .weyl == null then "-" else
       ((.weyl.takt_tabelle // {}) | to_entries | map("\(.key): \(.value.anzahl) (+\(.value.chi_plus)/-\(.value.chi_minus), netto \(.value.netto))") | join("; ")) end),
    (if .weyl.luecken.netto_je_luecke == null then "-" else (.weyl.luecken.netto_je_luecke | map(tostring) | join(",")) end) ]
| "| " + join(" | ") + " |"
