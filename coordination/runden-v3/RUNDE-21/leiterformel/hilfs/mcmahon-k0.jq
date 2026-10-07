# Nachtraeglich [H], keine Wertung: Wandkurve k = 0. Rest(l) minus Rest(l = 0, linear in R_n interpoliert)
# gegen den McMahon-Term l(l+1)/(2 pi) (1/Phi_n - 1/Phi_n+1) (Feld mcmahon der Auswertung).
[.paare[] | select(.k == 0 and .l == 0)] as $n0
| [.paare[] | select(.k == 0 and .l > 0)]
| map(. as $p
    | ([$n0[] | select(.R_n <= $p.R_n)] | last) as $a
    | ([$n0[] | select(.R_n > $p.R_n)] | first) as $b
    | if ($a == null or $b == null) then empty else
        ($a.rest + ($b.rest - $a.rest) * ($p.R_n - $a.R_n) / ($b.R_n - $a.R_n)) as $r0
        | {l: $p.l, R_n: $p.R_n, rest: $p.rest, rest_l0_interp: $r0, ueberschuss: ($p.rest - $r0),
           mcmahon: $p.mcmahon, verhaeltnis: (($p.rest - $r0) / $p.mcmahon)}
      end)
