# L1-Zuordnung (PLAN 5): je bekannte Stelle der Kandidat derselben Stufe mit |w2 - bekannt| < Zeilenabstand und
# |rho - bekannt| < 0,3 Luecke, naechster in w2. Eingabe: -s paar-stX-*.json
[ .[] | . as $p | .punkte[] | . + {i: $p.i, dw2_zeile: ($p.w2a - $p.w2b)} ] as $P
| [ [1,0.81864948,1.05187987,1],[2,0.82057924,1.36200257,-1],[3,0.82123499,1.23411245,1],[4,0.83578650,1.05931135,-1],
    [5,0.83728947,1.24903866,-1],[6,0.84015011,1.40944022,1],[7,0.84743426,1.33956049,1],[8,0.86038074,1.27174185,1],
    [9,0.86085981,1.06976351,1],[10,0.88121651,1.39804343,-1],[11,0.89702906,1.30955352,-1],[12,0.90096911,1.08553960,-1],
    [13,0.96850582,1.37891993,1],[14,0.97514752,1.11223140,1],[15,1.15865988,1.17041521,-1] ]
| {punkte: [ .[] as $b
    | [ $P[] | select(((.w2 - $b[1])|fabs) < .dw2_zeile and ((.rho - $b[2])|fabs) < 0.3 * .gap) ]
    | sort_by((.w2 - $b[1])|fabs) | select(length > 0) | .[0]
    | {name: ("L1-" + ($b[0]|tostring)), w2, rho, gap, dw2_zeile, k, umlauf_zelle, i} ]}
