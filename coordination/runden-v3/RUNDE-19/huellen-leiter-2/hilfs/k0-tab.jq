# K0 je Stelle: Nr | k | Paar | R | Umlauf alt -> neu (St1/St2) | interp. d omega^2 St1 | d rho St1 | d omega^2 St2 | d rho St2 | Newton d omega^2 St1 | d rho St1 | St2 | St2 | Maske Anker St1
(.newton.je_stelle | map({key: (.nr|tostring), value: .}) | from_entries) as $nw
| .kette.je_stelle[] | . as $z | $nw[($z.nr|tostring)] as $n
| "| \($z.nr) | \($z.k) | \($z.i) | \($z.R*100|round/100) | \($z.umlauf_alt|map(tostring)|join("/")) -> \($z.umlauf_neu|map(tostring)|join("/")) | \($z.dw2_st1) | \($z.drho_st1) | \($z.dw2_st2) | \($z.drho_st2) | \($n.st1.dw2) | \($n.st1.drho) | \($n.st2.dw2) | \($n.st2.drho) | \($n.st1.maske_anker) |"
