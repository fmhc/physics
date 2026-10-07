# Q-STERN-2 K4: Ast (Richtung +1) bei 0,750 (Zeile) und 0,755 (Zwischenreihe), lineare Interpolation von s
([.mitglieder[] | select((.x - 0.75) | fabs < 1e-9) | .wurzeln[] | select(.richtung == 1 and .rho > 1.6 and .rho < 1.8)][0]) as $a
| ([.zwischenreihen[] | select((.x - 0.755) | fabs < 1e-9) | .wurzeln[] | select(.richtung == 1 and .rho > 1.6 and .rho < 1.8)][0]) as $b
| {datei: (input_filename | split("/") | last), rho1: $a.rho, s1: $a.s, rho2: $b.rho, s2: $b.s,
   x_stern: (0.75 + 0.005 * $a.s / ($a.s - $b.s))}
