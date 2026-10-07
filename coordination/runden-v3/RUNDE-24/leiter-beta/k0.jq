# LEITER-BETA K0 (PLAN.md Abschnitt 3). Aufruf: jq -n --slurpfile a <k0-h004/praez.json> --slurpfile b <k0-h002/praez.json> -f k0.jq
# Je Stufe bestanden: ein Vorzeichenwechsel von s auf dem Zielast mit |omega*^2 - 0,5423644| <= 1e-5 und
# |rho* - 1,57218| <= 1e-4, dessen Rechteck aufgeloest ist (groesster Sprung < 0,4 rad) mit Umlauf +-1 (|abs U - 1| < 0,1).
def stufe($e):
  ($e.ergebnisse.praez) as $p
  | ([ ($p.rechtecke // [])[] | select(.art == "wechsel") ]) as $re
  | [ ($p.ziel_wechsel // []) | to_entries[] | .key as $j | .value
      | {x_stern, rho_stern, dx: (.x_stern - 0.5423644), drho: (.rho_stern - 1.57218), umlauf: ($re[$j].umlauf // null),
         sprung: ($re[$j].max_sprung // null), aufgeloest: ($re[$j].aufgeloest // false),
         kw: .kernwachstum_kandidat}
      | . + {ok: ((.dx | fabs) <= 1e-5 and (.drho | fabs) <= 1e-4 and .aufgeloest == true and .umlauf != null
                  and (((.umlauf | fabs) - 1) | fabs) < 0.1)} ]
  | {wechsel: ., ok: (map(.ok) | any)};
{h004: stufe($a[0]), h002: stufe($b[0])} | . + {bestanden: (.h004.ok and .h002.ok)}
