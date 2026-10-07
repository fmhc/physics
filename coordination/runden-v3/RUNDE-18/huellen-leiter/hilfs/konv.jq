# Hintergrund-Konvergenz: Q und E je Zeile auf Stufe 1 gegen Stufe 2 (Eingabe: -s prof-st1/profile-info.json prof-st2/profile-info.json)
(.[0] | map({key: (.w2*1e10|floor|tostring), value: .}) | from_entries) as $a
| (.[1] | map({key: (.w2*1e10|floor|tostring), value: .}) | from_entries) as $b
| [ $a | keys[] as $k | select($b[$k] != null)
    | {w2: $a[$k].w2, Q2: $b[$k].Q, E2: $b[$k].E,
       dQ: ((($a[$k].Q - $b[$k].Q)/$b[$k].Q)|fabs), dE: ((($a[$k].E - $b[$k].E)/$b[$k].E)|fabs),
       R1: $a[$k].Rchi, R2: $b[$k].Rchi, chi0: $b[$k].chi0, rhalf: $b[$k].rhalf, N1: $a[$k].N, N2: $b[$k].N,
       frand: $b[$k].f_rand, res2: $b[$k].res} ]
| sort_by(-.w2)
