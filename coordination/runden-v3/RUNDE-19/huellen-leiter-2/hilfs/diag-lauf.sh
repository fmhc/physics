#!/bin/bash
# PLAN-NACHTRAG-1, D1/D2: Newton + sigma2/sigma1 + Rechteck-Umlauf (stabilisierte Kopplung) an den Diagnosepunkten
# Aufruf: diag-lauf.sh <spur> <stufe> <i0> <i1>
D=/home/fmh/fmhc-physics-remote/runde19-huellen-leiter-2
s=$2
cd $D && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh $1 r19hl2-diag-st$s-$3-$4 $D/code/huellen_leiter2.py umlauf M2 $s $D/aus/prof-st$s $D/hilfs/zeilen-126.json $D/hilfs/diag-punkte-st$s.json $D/aus/diag/umlauf-st$s-$3-$4.json $3 $4 > $D/logs/r19hl2-diag-st$s-$3-$4.log 2>&1
