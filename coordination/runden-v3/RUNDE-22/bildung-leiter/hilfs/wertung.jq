# BILDUNG-LEITER, Wertung nach PLAN.md.eingefroren-20261002-204146, Abschnitt 4 (Code-Agent, nach dem Einfrieren
# geschrieben; setzt nur die dort festgelegten Regeln um). Aufruf: jq -s -f wertung.jq <alle Haupt- und Scan-JSONs>
def band($d; $t0; $q):
  ([$d.analyse[] | select(.reihe == "kick") | .[$q][] | select(.t0 == $t0) | .band] | first) as $b
  | if $b then {re: $b.re, gamma: (-$b.im), amp: $b.amp} else null end;
def g200($d): band($d; 200.0; "projektion");
def g50($d): band($d; 50.0; "projektion");
def vfit($p): if ($p | length) < 3 then null else
  ($p | min_by(.g | fabs)) as $m
  | [$p[] | select(.x != $m.x) | {x, s: ((if .x < $m.x then -1 else 1 end) * (.g | fabs | sqrt))}] as $q
  | ($q | length) as $n
  | ([$q[].x] | add / $n) as $mx | ([$q[].s] | add / $n) as $ms
  | (([$q[] | (.x - $mx) * (.s - $ms)] | add) / ([$q[] | (.x - $mx) * (.x - $mx)] | add)) as $a
  | ($ms - $a * $mx) as $b
  | {punkte: $p, min_punkt: $m, steigung: $a, nullstelle: (-$b / $a), kruemmung: ($a * $a),
     rest_max: ([$q[] | (.s - ($a * .x + $b)) | fabs] | max)} end;
[.[] | select(.arm == "lin")] as $lin
| [.[] | select(.arm == "nl")] as $nl
| {
  L0_K0: [$nl[] | {w2, dr, k0: ([.analyse[] | select(.reihe == "exakt") | .S_zentrum_rel_abw_max] | first)}]
         | sort_by(.dr, .w2),
  L1_L2_ArmM: [$lin[] | select(.w2 == 0.52905 or .w2 == 0.529266 or .w2 == 0.5295 or .w2 == 0.53139)
               | {w2, dr, wertfenster: (if .w2 == 0.53139 then "50-400" else "200-2000" end),
                  band: (if .w2 == 0.53139 then g50(.) else g200(.) end),
                  k24: (if .w2 == 0.53139 then band(.; 50.0; "projektion_k24") else band(.; 200.0; "projektion_k24") end)}]
              | sort_by(.dr, .w2),
  L3_ArmG: [$nl[] | {w2, dr, schwelle_a,
                     anteile: ([.analyse[] | select(.reihe == "gauss") | .S_zentrum_spektrum[] | select(.t0 == 100.0)
                                | .anteile] | first)}]
           | sort_by(.dr, .w2),
  V_dr004: vfit([$lin[] | select(.dr == 0.04 and .w2 < 0.5300) | {x: .w2, g: (g200(.) | if . then .gamma else null end)}]
                | map(select(.g != null)) | sort_by(.x)),
  V_dr002_zweipunkt: ([$lin[] | select(.dr == 0.02 and (.w2 == 0.52905 or .w2 == 0.5295)) | {x: .w2, g: g200(.).gamma}]
                      | map(select(.g != null)) | sort_by(.x)
                      | if length == 2 then
                          {x1: .[0].x, x2: .[1].x, g1: .[0].g, g2: .[1].g,
                           nullstelle: ((.[0].x * (.[1].g | fabs | sqrt) + .[1].x * (.[0].g | fabs | sqrt))
                                        / ((.[0].g | fabs | sqrt) + (.[1].g | fabs | sqrt))),
                           steigung: (((.[0].g | fabs | sqrt) + (.[1].g | fabs | sqrt)) / (.[1].x - .[0].x))}
                        else null end)
}
