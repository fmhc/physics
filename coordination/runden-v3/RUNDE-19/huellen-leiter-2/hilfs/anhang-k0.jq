def ab: if . < 0 then -. else . end;
def sci: if . == 0 then "0" else (log10 | floor) as $e | ((. / pow(10; $e) * 10 | round / 10 | tostring) + "e" + ($e|tostring)) end;
(.newton.je_stelle | map({key: (.nr|tostring), value: .}) | from_entries) as $nw
| .kette.je_stelle[] | . as $z | $nw[($z.nr|tostring)] as $n
| ([$z.dw2_st1, $z.drho_st1, $z.dw2_st2, $z.drho_st2] | map(ab) | max) as $di
| ([$n.st1.dw2, $n.st1.drho, $n.st2.dw2, $n.st2.drho] | map(ab) | max) as $dn
| "| \($z.nr) | \($z.k) | \($z.i) | \($z.R*100|round/100) | \($z.umlauf_alt[0]) / \($z.umlauf_neu[0]) | \($z.umlauf_alt[1]) / \($z.umlauf_neu[1]) | \(if $di == 0 then "0" else ($di|sci) end) | \(if $dn == 0 then "0" else ($dn|sci) end) | \([$n.st1.svr[1], $n.st2.svr[1]] | max | sci) | \($n.st1.maske_anker) |"
