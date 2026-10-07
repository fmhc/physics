# LEITER-3D-PRAEZ: Kurzauszug einer praez.json (jq -r -f tabellen.jq praez.json)
.ergebnisse.praez as $p
| "h=\($p.h) R=\($p.R_aus) r_m=\($p.r_m) Profile=\($p.x|length) vollst=\($p.profile_vollstaendig) prof_max_s=\($p.sek_profil_max) abtast_s=\($p.sek_abtastung) wurzel_s=\($p.sek_wurzeln) sek=\(.sek) entfallen=\(.entfallen)",
  "Kernwachstum Fenstermaximum: \($p.wachstum_fenster_max)",
  "Klammern je Zeile: \([$p.zeilen[] | (.nullstellen|length)])",
  "Zielast (x | rho_b | s | lb_rest | Kernwachstum | Ausloeschung | iter | konv):",
  ($p.ziel | to_entries[] | "  \($p.x[.key]) | \(.value.rho) | \(.value.s) | \(.value.lb_rest) | \(.value.wachstum) | \(.value.ausloeschung) | \(.value.iter) | \(.value.konvergiert)"),
  "Ziel konsistent gepaart: \($p.ziel_konsistent)",
  "Wechsel Zielast:",
  ($p.ziel_wechsel[] | "  x*=\(.x_stern) rho*=\(.rho_stern) zwischen \(.x_lo) und \(.x_hi) s=\(.s_lo)/\(.s_hi) KW=\(.kernwachstum_kandidat) Ausl=\(.ausloeschung_kandidat) Steig=\(.steigung_rho_x) konsistent=\(.ast_konsistent)"),
  "Wechsel andere Aeste: \($p.neben_wechsel | length) \([$p.neben_wechsel[] | {x_stern, rho_stern}])",
  "Ohne Wechsel: \($p.kandidat_ohne_wechsel // "-")",
  "Rechtecke:",
  ($p.rechtecke[] | "  \(.art) x \(.x_lo)..\(.x_hi) rho \(.rho_lo)..\(.rho_hi) drho=\(.drho) Umlauf=\(.umlauf) Kreuzung=\(.umlauf_kreuzung) Sprung=\(.max_sprung) aufgeloest=\(.aufgeloest) Punkte=\(.punkte) Runden=\(.runden_benutzt) Seiten=\(.max_sprung_seiten) min|W|=\(.min_absW) median|W|=\(.median_absW) KWpfad=\(.wachstum_max_pfad) sek=\(.sek) fehler=\(.fehler // "-")"),
  "Pole Zielast:",
  (($p.pole_ziel // [])[] | "  \(.x) | \(.pol[0]) \(.pol[1]) | Gamma \(.Gamma) | konv \(.konvergiert)")
