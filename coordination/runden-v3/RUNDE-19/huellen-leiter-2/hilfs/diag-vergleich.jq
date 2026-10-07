# Eins-zu-eins-Zuordnung: je alte Stelle die naechste neue Stelle (gleiches Paar, gleiche Kurve, |d w2| <= Zeilenabstand/16)
def ab: if . < 0 then -. else . end;
def passt($a; $n): ($a.i == $n.i and $a.k == $n.k and (($a.w2 - $n.w2) | ab) <= $n.dw2 / 16);
[ $A[] as $a | {a: $a, n: ([ $N[] | select(passt($a; .)) ] | sort_by((.w2 - $a.w2) | ab) | first)} ] as $z
| [ $z[] | select(.n != null) | .n ] as $treffer
| { zusaetzlich: [ $N[] | . as $n | select(($treffer | index([$n])) == null) ],
    umgekehrt: [ $z[] | select(.n != null and .a.u != .n.u) | .n ],
    fehlend: [ $z[] | select(.n == null) | .a ],
    n_neu: ($N | length), n_alt: ($A | length), n_zugeordnet: ($treffer | length) }
