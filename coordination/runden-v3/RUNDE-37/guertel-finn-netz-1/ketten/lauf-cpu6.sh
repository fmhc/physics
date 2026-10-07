#!/bin/bash
# GUERTEL-FINN-NETZ-1, Hauptlaeufe Spur cpu6 (PLAN Abschnitt 8): P10 Diamant SO(3), Wahl, Stoesse, Referenzen,
# Kontrollen eps = 0, danach die Auswertung. Eingefrorener Code, je Lauf genau einmal.
set -u
B=/home/fmh/fmhc-physics-remote/guertel-finn-netz-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=$B/code/finn.py
A=$B/lauf
cd $B/code || exit 1
run() { local name=$1; shift; bash $K cpu6 "$name" "$@" >> $A/$name.log 2>&1; echo "rc=$? $name $(date -u +%H:%M:%S)" >> $A/kette-cpu6.out; }
echo "kette start $(date -u +%H:%M:%S)" >> $A/kette-cpu6.out
run gfnPd10 $C prot --netz diamant --feld so3 --fdtheta 10 --tmax 720 --aus $A
touch $A/pd10.fertig
while [ ! -e $A/pd30.fertig ]; do sleep 5; done
run gfnWahl $C wahl --lauf $A --aus $A
Z=$A/prot-diamant-so3-d10-zust.npz
for k in 0 1 2; do
  i=0
  for e in 0.01 0.1 0.3; do
    i=$((i+1))
    run gfnS${k}e$i $C stoss --netz diamant --feld so3 --zust $Z --wahl $A/wahl.json --wahl_k $k --eps $e --aus $A
  done
  run gfnR$k $C stoss --netz diamant --feld so3 --zust $Z --wahl $A/wahl.json --wahl_k $k --ref 1 --eps 0 --aus $A
  run gfnK$k $C stoss --netz diamant --feld so3 --zust $Z --wahl $A/wahl.json --wahl_k $k --eps 0 --aus $A
done
touch $A/cpu6.fertig
while [ ! -e $A/cpu7.fertig ]; do sleep 5; done
run gfnAusw $B/code/auswertung_fn.py --lauf $A --gfs1 $B/eingaben-gfs1/prot.json --aus $A
echo "kette ende $(date -u +%H:%M:%S)" >> $A/kette-cpu6.out
touch $A/alles.fertig
