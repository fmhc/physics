#!/bin/bash
# Baut hilfs/stellen-eingabe.json aus den Quellen (PLAN Abschnitt 2). Nur jq.
set -euo pipefail
V=/home/fmh/fmhc-physics/coordination/runden-v3
O=$V/RUNDE-21/leiterformel/hilfs/stellen-eingabe.json
jq -n \
  --slurpfile r18 $V/RUNDE-18/huellen-leiter/aus/laeufe/stellen.json \
  --slurpfile svl4 $V/RUNDE-20/sprossen-vorab/aus/l4-d1/l4-auswertung.json \
  --slurpfile svt $V/RUNDE-20/sprossen-vorab/aus/test/test-auswertung.json \
  --slurpfile dip $V/RUNDE-19/huellen-dipol/aus/laeufe/stellen.json \
  --slurpfile quad $V/RUNDE-20/huellen-quadrupol/aus/laeufe/stellen.json \
  --slurpfile slt $V/RUNDE-21/sprossen-l1l2/aus/test/test-auswertung.json \
  --slurpfile n1 $V/RUNDE-21/sprossen-l1l2/aus/nachtrag1/umlauf-st1.json \
'
  [ $r18[0].stellen[] | select(.bereich == true and .gezaehlt == true)
    | {l: 0, k, w2, rho, R, umlauf: .umlauf_1, quelle: ("R18 Nr " + (.nr|tostring)), flag: ""} ]
+ [ $svl4[0].sprossen[] | select(.bekannt.quelle | startswith("HL3"))
    | {l: 0, k, w2: .st1.w2, rho: .st1.rho, R: .st1.R, umlauf: .st1.umlauf_F,
       quelle: ("HL3 " + .bekannt.quelle[4:] + " (Werte SPROSSEN-VORAB L4 St1)"), flag: ""} ]
+ [ $svt[0].sprossen[] | select(.angenommen == true)
    | {l: 0, k, w2: .st1.w2, rho: .st1.rho, R: .st1.R, umlauf: .st1.umlauf_F,
       quelle: ("SPROSSEN-VORAB Ziel " + (.R_ziel|tostring)), flag: ""} ]
+ [ $dip[0].stellen[] | select(.bereich == true and .gezaehlt == true)
    | {l: 1, k, w2, rho, R, umlauf: .umlauf_1, quelle: ("DIPOL Nr " + (.nr|tostring)), flag: ""} ]
+ [ $quad[0].stellen[] | select(.bereich == true and .gezaehlt == true)
    | {l: 2, k, w2, rho, R, umlauf: .umlauf_1, quelle: ("QUADRUPOL Nr " + (.nr|tostring)), flag: ""} ]
+ [ $slt[0].sprossen[] | select(.angenommen == true)
    | {l: .ell, k, w2: .st1.w2, rho: .st1.rho, R: .st1.R, umlauf: .st1.umlauf,
       quelle: ("SPROSSEN-L1L2 Satz " + .satz + " Sprosse " + (.sprosse|tostring)), flag: ""} ]
+ [ $slt[0].sprossen[] | select(.angenommen == false and .ell == 2 and .k == 2 and .sprosse == 2)
    | {l: .ell, k, w2: .st1.w2, rho: .st1.rho, R: .st1.R, umlauf: $n1[0].punkte[0].umlauf.umlauf,
       quelle: "SPROSSEN-L1L2 Satz B Sprosse 2 (Wurzel 22,2923)",
       flag: "nachtraeglich belegt (SPROSSEN-L1L2 Nachtrag 1, Umlauf +1 aufgeloest), formal nicht angenommen"} ]
| sort_by(.l, .k, .R)
| {stellen: ., n: length}
' > $O
jq -c '.n, ([.stellen[] | .l] | group_by(.) | map({l: .[0], n: length}))' $O
