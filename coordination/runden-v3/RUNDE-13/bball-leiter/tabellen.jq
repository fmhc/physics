# Tabellen fuer ERGEBNIS.md aus einer Familien-JSON von bball.py (jq -r -f tabellen.jq <datei>)
def r6: . * 1000000 | round / 1000000;
def e2: if . == null then "-" elif (. | type) == "string" then . else (. * 1000 | round / 1000 | tostring) end;
def sci: if . == null then "-" else (tostring | if test("[eE]") then (ascii_downcase | split("e") | (.[0] | .[0:6]) + "e" + .[1]) elif length > 9 then .[0:9] else . end) end;
"Datei: \(.argumente.name)  modell \(.modell)  band \(.band)  h \(.h)  laufzeit \(.laufzeit | floor) s  entfallen \(.budget_entfallen | length)",
"| x | R | r_m | R_w | Rand-Abw. | Nullstellen | rho (s/median, Richtung, Gamma) |",
"|---|---|---|---|---|---|---|",
(.mitglieder[] | select(.gueltig) |
  "| \(.x) | \(.R) | \(.r_m | r6) | \(.R_w | r6) | \(.rand_abw | sci) | \(.wurzeln | length) | " +
  ([.wurzeln[] | "\(.rho | r6) (\(.s_rel | sci), \(.richtung), \(if .Gamma then (.Gamma | sci) else "-" end))"] | join("; ")) + " |"),
"Streifen:",
(.streifen[] | if .umlauf_roh then "  \(.i): \(.x_lo) .. \(.x_hi) Umlauf \(.umlauf) (roh \(.umlauf_roh | sci), Kreuzung \(.umlauf_kreuzung)) Sprung \(.max_sprung | sci) aufgeloest \(.aufgeloest) neue Profile \(.neue_profile) min/median \((.min_absW / .median_absW) | sci)" else "  \(.i): FEHLER \(.fehler)" end),
"Vorzeichenwechsel: \(.vorzeichenwechsel | length); ungepaart: \([.paarung[] | (.rho_ungepaart_1 | length) + (.rho_ungepaart_2 | length)] | add)",
"Ungepaart je Reihenpaar: \([.paarung[] | select(((.rho_ungepaart_1 | length) + (.rho_ungepaart_2 | length)) > 0) | {x1, x2, u1: .rho_ungepaart_1, u2: .rho_ungepaart_2}])",
"Kandidaten: \(.kandidaten | length)"
