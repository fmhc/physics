#!/bin/bash
# GUERTEL-FINN-NETZ-1, Hauptlaeufe Spur cpu7 (PLAN Abschnitt 8): P30 Diamant, K0 (P10 Z^3), P30 Z^3, SO(2) P10 Diamant,
# SO(2)-Stoesse bei 420 und 450 Grad, Zusatz SO(2) P10 Z^3. Eingefrorener Code, je Lauf genau einmal.
set -u
B=/home/fmh/fmhc-physics-remote/guertel-finn-netz-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=$B/code/finn.py
A=$B/lauf
cd $B/code || exit 1
run() { local name=$1; shift; bash $K cpu7 "$name" "$@" >> $A/$name.log 2>&1; echo "rc=$? $name $(date -u +%H:%M:%S)" >> $A/kette-cpu7.out; }
echo "kette start $(date -u +%H:%M:%S)" >> $A/kette-cpu7.out
run gfnQd30 $C prot --netz diamant --feld so3 --fdtheta 30 --tmax 720 --speicher "" --aus $A
touch $A/pd30.fertig
run gfnQz10 $C prot --netz z3 --feld so3 --fdtheta 10 --tmax 720 --speicher "" --aus $A
run gfnQz30 $C prot --netz z3 --feld so3 --fdtheta 30 --tmax 720 --speicher "" --aus $A
run gfnQd2 $C prot --netz diamant --feld so2 --fdtheta 10 --tmax 720 --aus $A
Z2=$A/prot-diamant-so2-d10-zust.npz
for th in 420 450; do
  i=0
  for e in 0.01 0.1 0.3; do
    i=$((i+1))
    run gfnC${th}e$i $C stoss --netz diamant --feld so2 --zust $Z2 --theta $th --eps $e --aus $A
  done
  run gfnC${th}e0 $C stoss --netz diamant --feld so2 --zust $Z2 --theta $th --eps 0 --aus $A
done
run gfnQz2 $C prot --netz z3 --feld so2 --fdtheta 10 --tmax 720 --speicher "" --aus $A
echo "kette ende $(date -u +%H:%M:%S)" >> $A/kette-cpu7.out
touch $A/cpu7.fertig
