# Nachtrag 1 (nachtraeglich): Stetigkeitsmass der Wurzel l = 2, k = 2 bei R = 22,29 mit anderen Fortsetzungen.
def lag(p; R): (1/R) as $x0 | (p | length) as $n | [p[] | {x: (1/.R), y: .rho}] as $q |
  reduce range(0; $n) as $i (0; . + ($q[$i].y * (reduce range(0; $n) as $j (1; if $j == $i then . else . * (($x0 - $q[$j].x) / ($q[$i].x - $q[$j].x)) end))));
($b[0].stellen | map(select(.k == 2)) | sort_by(.R)) as $kurve |
($t[0].sprossen[] | select(.ell == 2 and .k == 2 and .sprosse == 1)) as $neu1 |
{R: $w.R, rho: $w.rho, d_nb: $w.d_nb} as $wz |
[ {art: "Test (Parabel 12,715/15,268/17,68)", p: $kurve[-3:]},
  {art: "Gerade 15,268/17,68", p: $kurve[-2:]},
  {art: "verkettet (Parabel 15,268/17,68/20,0114)", p: ($kurve[-2:] + [{R: $neu1.R_gefunden, rho: $neu1.st1.rho}])} ] |
.[] | (lag(.p; $wz.R)) as $f | [.art, $f, ($wz.rho - $f), (($wz.rho - $f) | fabs) / $wz.d_nb] | @tsv
