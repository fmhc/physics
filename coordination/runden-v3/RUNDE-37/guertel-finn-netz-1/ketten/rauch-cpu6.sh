#!/bin/bash
# GUERTEL-FINN-NETZ-1, Rauchlauf Spur cpu6 (PLAN Abschnitt 8). Nur Winkel bis 60 Grad.
set -u
B=/home/fmh/fmhc-physics-remote/guertel-finn-netz-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=$B/code/finn.py
A=$B/rauch
cd $B/code || exit 1
run() { local name=$1; shift; bash $K cpu6 "$name" "$@" >> $A/$name.log 2>&1; echo "rc=$? $name $(date -u +%H:%M:%S)" >> $A/kette-cpu6.out; }
echo "kette start $(date -u +%H:%M:%S)" >> $A/kette-cpu6.out
run gfnRd10 $C prot --netz diamant --feld so3 --fdtheta 10 --tmax 60 --speicher 30,60 --aus $A
run gfnRd30 $C prot --netz diamant --feld so3 --fdtheta 30 --tmax 60 --speicher "" --aus $A
run gfnRwahl $C wahl --lauf $A --aus $A --ziel 30,60 --grenze 60 --unten 0 --refsumme 90
for k in 0 1; do
  run gfnRs$k $C stoss --netz diamant --feld so3 --zust $A/prot-diamant-so3-d10-zust.npz --wahl $A/wahl.json --wahl_k $k --eps 0.3 --nmax 100 --aus $A
  run gfnRr$k $C stoss --netz diamant --feld so3 --zust $A/prot-diamant-so3-d10-zust.npz --wahl $A/wahl.json --wahl_k $k --ref 1 --eps 0 --nmax 60 --aus $A
done
run gfnRs2 $C stoss --netz diamant --feld so3 --zust $A/prot-diamant-so3-d10-zust.npz --wahl $A/wahl.json --wahl_k 2 --eps 0.3 --nmax 100 --aus $A
touch $A/cpu6.fertig
while [ ! -e $A/cpu7.fertig ]; do sleep 5; done
run gfnRausw $B/code/auswertung_fn.py --lauf $A --gfs1 $B/eingaben-gfs1/prot.json --aus $A --eps 0.3 --so2_thetas 60 --grenze 60
echo "kette ende $(date -u +%H:%M:%S)" >> $A/kette-cpu6.out
touch $A/alles.fertig
