# Auszuege aus lauf-69/auswertung.json fuer ERGEBNIS.md (nur Lesen; jq -r -f auswertung-tabellen.jq auswertung.json)
def r4: if . == null then "null" else ((. * 10000 | round) / 10000 | tostring) end;
def r5: if . == null then "null" else ((. * 100000 | round) / 100000 | tostring) end;
def ms: "\(.mittel | r4) +- \(.se | r4)";
"TOR " + (.tor | tostring),
"KE0rep " + (.KE0_reproduktion | tostring),
"--- b je Netz (N-Mittel) und y je N",
(.messgroessen | to_entries[] |
  "\(.key): b \(.value.b | ms) (std \(.value.b.std | r4), neg \(.value.b.neg)) | y: "
  + ([.value.y_je_N | to_entries[] | "\(.key) \(.value | ms)"] | join(" / "))
  + " | dGamma: " + ([.value.dGamma_je_N | to_entries[] | "\(.key) \(.value.mittel | r4)"] | join(" / "))
  + (if .value.y_E then " | y_E \(.value.y_E | r5)" else "" end)),
"--- Netze",
(.messgroessen | to_entries[] | "\(.key): " + (.value.netze | tostring)),
"--- gerade/ungerade",
(.gerade_ungerade | to_entries[] |
  "\(.key): G \(.value.G | ms) U \(.value.U | ms) yE_g \(.value.y_E_gerade | r5) | je N: "
  + ([.value.je_N | to_entries[] | "\(.key) G \(.value.G | ms) U \(.value.U | ms)"] | join(" / "))),
"--- Steigungen",
(.steigungen | to_entries[] | "\(.key): \(.value.steigung | r4) +- \(.value.se | r4)"),
"--- Scherkontrolle",
(.scherkontrolle | to_entries[] | "\(.key): " + (.value | tostring)),
"--- Urteile",
(.urteile | to_entries[] | "\(.key): " + (.value | tostring))
