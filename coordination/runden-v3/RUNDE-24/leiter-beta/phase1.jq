# LEITER-BETA Phase 1 -> Kandidaten (PLAN.md Abschnitt 5). Aufruf: jq -s -f phase1.jq lauf-69/g1/praez.json ... g5
# Kandidat = jeder Vorzeichenwechsel von s auf dem Zielast; dazu Wechsel auf anderen gepaarten Aesten, wenn rho* im
# dichten Band liegt. Nummer k nach omega*^2 aufsteigend (also eps aufsteigend).
[ .[] | .argumente as $a | .ergebnisse.praez as $p | ($a.out | split("/") | last) as $f
  | ([ $p.rechtecke[] | select(.art == "wechsel") ]) as $re
  | ( ($p.ziel_wechsel | to_entries[]) | .key as $j | .value
      | {fenster: $f, ast: "ziel", x_stern, rho_stern, steigung: .steigung_rho_x, x_lo, x_hi, s_lo, s_hi,
         kw: .kernwachstum_kandidat, ast_konsistent,
         umlauf_grob: ($re[$j].umlauf // null), aufgeloest_grob: ($re[$j].aufgeloest // null),
         sprung_grob: ($re[$j].max_sprung // null), fehler_grob: ($re[$j].fehler // null)} ),
    ( $p.neben_wechsel[]
      | select(((.rho_stern - ($a.rho0 + $a.rho_steig * (.x_stern - $a.x0))) | fabs) <= $a.dicht_halb)
      | {fenster: $f, ast: "neben", x_stern, rho_stern, steigung: .steigung_rho_x, x_lo, x_hi, s_lo, s_hi,
         kw: .kernwachstum_kandidat, ast_konsistent: null, umlauf_grob: null, aufgeloest_grob: null,
         sprung_grob: null, fehler_grob: null} )
] | sort_by(.x_stern) | to_entries | map(.value + {k: (.key + 1), eps_grob: (.value.x_stern - 0.75)})
