#!/bin/bash
H=/home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-19/huellen-dipol/hilfs
$H/k.sh r19-liste code/dipol.py liste aus/zeilen.json
$H/k.sh r19-k1-st1 code/dipol.py k1 1 aus/k1-st1.json
$H/k.sh r19-prof-st1 code/dipol.py profile 1 aus/prof-st1 aus/zeilen.json
$H/k.sh r19-k1-st2 code/dipol.py k1 2 aus/k1-st2.json
$H/k.sh r19-prof-st2 code/dipol.py profile 2 aus/prof-st2 aus/zeilen.json
