# Nachtraeglich: Abstand je Paar gegen den l = 0-Abstand derselben Kurve mit naechster Paarmitte (jq -c -f hilfs/paarweise.jq aus/laeufe/auswertung.json)
def sp($R): [range(1; $R | length) | {m: (($R[.] + $R[. - 1]) / 2), d: ($R[.] - $R[. - 1])}];
. as $a
| ($a.kurven_l0 | map({key: (.k | tostring), value: sp(.R)}) | from_entries) as $S0
| (["l1", $a.kurven_l1], ["l2", $a.kurven_l2]) as [$l, $K]
| $K[] | select(.k <= 2) | . as $e | ($S0[$e.k | tostring]) as $s0
| {l: $l, k: $e.k, q_paar: [sp($e.R)[] | . as $p | ($s0 | min_by((.m - $p.m) | fabs)) as $n | {m: ($p.m * 100 | round / 100), m0: ($n.m * 100 | round / 100), q: ($p.d / $n.d * 1000 | round / 1000)}]}
