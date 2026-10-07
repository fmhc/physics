# PLAN 4.6: (a) und (b) aus den Bio-28b-Rohdaten (grob_roh.json) nachrechnen, bei t = 20, 40, 60, 90.
# Aufruf: jq -c -f bio28b_probe.jq RUNDE-22/bio28b/lauf-69/ausgabe/grob_roh.json
.ergebnis.grob[] | .lauf as $n | .J_box_start as $L0 | .reihe[]
| select(.t == 20 or .t == 40 or .t == 60 or .t == 90)
| .t as $t | .gebiete as $g
| ($g | map(.Q) | add) as $qs
| ($g | map(.Q * .X) | add / $qs) as $X0
| ($g | map(.Q * .Y) | add / $qs) as $Y0
| {lauf: $n, t: $t, L0: $L0, n: ($g | length),
   a_L0: (($g | map((.X - $X0) * .vy * .E - (.Y - $Y0) * .vx * .E) | add) / $L0),
   b_L0: (($g | map(.Jspin_Q * .Q) | add) / $L0),
   gebiete: ($g | map([.Q, .X, .Y]))}
