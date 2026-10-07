# Q-STERN: Kurztabelle eines familie-Laufs (jq -r -f tabelle.jq aus/<lauf>.json)
"\(.argumente.name) alpha=\(.alpha) h=\(.h) r_fak=\(.r_fak) quelle=\(.quelle)",
(.mitglieder[]? | select(.gueltig) | "  x=\(.x) R_w=\(.R_w*1000|round/1000) R=\(.R) komp=\(.info.kompaktheit*1e5|round/1e5) Phi0=\(.info.Phi0*1e6|round/1e6) PhiRw=\(.info.Phi_Rw*1e5|round/1e5) c=\(.info.c_asym*1e5|round/1e5) it=\(.info.phi_iter) | " + ([.wurzeln[] | "\(.rho*1e6|round/1e6) (s/med \(.s_rel*1e6|round/1e6|tostring) bzw. \(.s_rel), \(.richtung))"] | join("; "))),
(.mitglieder[]? | select(.gueltig|not) | "  x=\(.x) UNGUELTIG"),
(.streifen[]? | "  Streifen \(.i) \(.x_lo)..\(.x_hi): U=\(.umlauf // "-") Sprung=\((.max_sprung // 0)*1000|round/1000) aufl=\(.aufgeloest // "-") neu=\(.neue_profile // "-") \(.fehler // "")"),
(.vorzeichenwechsel[]? | "  s-Wechsel \(.x1*1e6|round/1e6)..\(.x2*1e6|round/1e6) rho \(.rho1*1e6|round/1e6)..\(.rho2*1e6|round/1e6) s \(.s1) / \(.s2) Richtung \(.richtung)"),
(.kandidaten[]? | "  Kandidat x*=\(.lokal.x_stern // "-") rho*=\(.lokal.rho_stern // "-") U=\(.rechteck.umlauf // "-") roh=\(.rechteck.umlauf_roh // "-") Sprung=\(.rechteck.max_sprung // "-") aufl=\(.rechteck.aufgeloest // "-") \(.fehler // "") \(.rechteck.fehler // "")"),
"  entfallen: \((.budget_entfallen // []) | join(", ")); Laufzeit \(.laufzeit // .laufzeit_bisher); Fehler \(.fehler // "keiner" | tostring | .[0:200])"
