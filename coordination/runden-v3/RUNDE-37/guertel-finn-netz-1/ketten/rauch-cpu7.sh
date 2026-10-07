#!/bin/bash
# GUERTEL-FINN-NETZ-1, Rauchlauf Spur cpu7 (PLAN Abschnitt 8). Nur Winkel bis 60 Grad.
set -u
B=/home/fmh/fmhc-physics-remote/guertel-finn-netz-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=$B/code/finn.py
A=$B/rauch
cd $B/code || exit 1
run() { local name=$1; shift; bash $K cpu7 "$name" "$@" >> $A/$name.log 2>&1; echo "rc=$? $name $(date -u +%H:%M:%S)" >> $A/kette-cpu7.out; }
echo "kette start $(date -u +%H:%M:%S)" >> $A/kette-cpu7.out
run gfnRz10 $C prot --netz z3 --feld so3 --fdtheta 10 --tmax 60 --speicher "" --aus $A
run gfnRz30 $C prot --netz z3 --feld so3 --fdtheta 30 --tmax 60 --speicher "" --aus $A
run gfnRd2 $C prot --netz diamant --feld so2 --fdtheta 10 --tmax 60 --speicher 30,60 --aus $A
run gfnRs2a $C stoss --netz diamant --feld so2 --zust $A/prot-diamant-so2-d10-zust.npz --theta 60 --eps 0.3 --nmax 100 --aus $A
run gfnRs2b $C stoss --netz diamant --feld so2 --zust $A/prot-diamant-so2-d10-zust.npz --theta 60 --eps 0 --nmax 60 --aus $A
run gfnRz2 $C prot --netz z3 --feld so2 --fdtheta 10 --tmax 60 --speicher "" --aus $A
echo "kette ende $(date -u +%H:%M:%S)" >> $A/kette-cpu7.out
touch $A/cpu7.fertig
