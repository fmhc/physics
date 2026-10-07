# AFM-KANAL-2: Tabellen aus den Lauf-JSON (jq, kein python). Aufruf: jq -r -f tabellen.jq <lauf>.json
def sci: if . == null then "-" elif . == 0 then "0" else (. as $v | ($v|fabs|log10|floor) as $e | ($v / pow(10;$e)) as $m | "\($m*100|round/100)e\($e)") end;
def r6: . * 1e6 | round / 1e6;
"## \(.argumente.name) (Modell \(.modell), kappa \(.kappa), h \(.h)), Laufzeit \(.laufzeit|round) s",
"| f | Omega^2 | R | r_m | Rand-Abw. | n | Nullstellen von L(y_b): rho (s/median|W|, Richtung, Gamma) |",
"|---|---|---|---|---|---|---|",
(.mitglieder[] | "| \(.info.f // "-" | if type == "number" then (. * 1000 | round / 1000) else . end) | \(.x|r6) | \(.R*100|round/100) | \(.r_m*100|round/100) | \(.rand_abw|sci) | \(.wurzeln|length) | \(.wurzeln|map("\(.rho|r6) (\(.s_rel|sci), \(.richtung), \(.Gamma|sci))")|join("; ")) |"),
"",
"| Streifen | Omega^2 | rho | Umlauf | Kreuzung | max Sprung (u/o/r/l) | aufgeloest | Omega^2-Punkte (neu) | min/median |W| | Zeit |",
"|---|---|---|---|---|---|---|---|---|---|",
(.streifen[] | if .umlauf_roh == null then "| \(.i) | Fehler: \(.fehler) |" else "| \(.i) | \(.x_lo|r6) .. \(.x_hi|r6) | \(.rho_lo*1e4|round/1e4) .. \(.rho_hi*1e4|round/1e4) | \(.umlauf_roh*1e4|round/1e4) | \(.umlauf_kreuzung) | \(.max_sprung*1000|round/1000) (\(.max_sprung_seiten.unten*100|round/100)/\(.max_sprung_seiten.oben*100|round/100)/\(.max_sprung_seiten.rechts*100|round/100)/\(.max_sprung_seiten.links*100|round/100)) | \(.aufgeloest) | \(.x_punkte) (\(.neue_profile)) | \((.min_absW/.median_absW)|sci) | \(.zeit*10|round/10) s |" end),
"",
"Vorzeichenwechsel von s: \(.vorzeichenwechsel|length) \(.vorzeichenwechsel|map("[\(.x1|r6)..\(.x2|r6), rho \(.rho1|r6)->\(.rho2|r6), s \(.s1|sci)->\(.s2|sci)]")|join(" "))",
"Ungepaart: \([.paarung[] | select((.rho_ungepaart_1|length) + (.rho_ungepaart_2|length) > 0) | "x \(.x1|r6)->\(.x2|r6): \(.rho_ungepaart_1|map(r6)) / \(.rho_ungepaart_2|map(r6))"]|join("; "))",
"Kandidaten: \(.kandidaten|map("x* \(.lokal.x_stern // "-") rho* \(.lokal.rho_stern // "-") Umlauf \(.rechteck.umlauf_roh // "-") aufgeloest \(.rechteck.aufgeloest // "-") Sprung \(.rechteck.max_sprung // "-")")|join("; "))",
"Entfallen (Zeit): \(.budget_entfallen)",
""
