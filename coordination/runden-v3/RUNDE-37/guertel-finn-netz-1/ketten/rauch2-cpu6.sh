#!/bin/bash
# GUERTEL-FINN-NETZ-1, zweiter Rauchlauf Spur cpu6: Wahl und Auswertung nach der Korrektur von gueltig_plan (Winkel 0).
set -u
B=/home/fmh/fmhc-physics-remote/guertel-finn-netz-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=$B/code/finn.py
A=$B/rauch
cd $B/code || exit 1
run() { local name=$1; shift; bash $K cpu6 "$name" "$@" >> $A/$name.log 2>&1; echo "rc=$? $name $(date -u +%H:%M:%S)" >> $A/kette2-cpu6.out; }
echo "kette start $(date -u +%H:%M:%S)" >> $A/kette2-cpu6.out
run gfnR2wahl $C wahl --lauf $A --aus $A --ziel 30,60 --grenze 60 --unten 0 --refsumme 90
run gfnR2ausw $B/code/auswertung_fn.py --lauf $A --gfs1 $B/eingaben-gfs1/prot.json --aus $A --eps 0.3 --so2_thetas 60 --grenze 60
echo "kette ende $(date -u +%H:%M:%S)" >> $A/kette2-cpu6.out
touch $A/alles2.fertig
