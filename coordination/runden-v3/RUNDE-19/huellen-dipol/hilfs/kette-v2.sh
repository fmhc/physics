#!/bin/bash
H=/home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-19/huellen-dipol/hilfs
$H/k.sh r19-b1-0-71 code/dipol.py block 1 aus/prof-st1 aus/laeufe aus/zeilen.json 0 71
$H/k.sh r19-b2-0-40 code/dipol.py block 2 aus/prof-st2 aus/laeufe aus/zeilen.json 0 40
$H/k.sh r19-b2-40-71 code/dipol.py block 2 aus/prof-st2 aus/laeufe aus/zeilen.json 40 71
$H/k.sh r19-b1-0-71-w code/dipol.py block 1 aus/prof-st1 aus/laeufe aus/zeilen.json 0 71
$H/k.sh r19-b2-0-40-w code/dipol.py block 2 aus/prof-st2 aus/laeufe aus/zeilen.json 0 40
$H/k.sh r19-b2-40-71-w code/dipol.py block 2 aus/prof-st2 aus/laeufe aus/zeilen.json 40 71
