#!/bin/bash
# Z2-SCHUTZ-1, Rauchtest 3 Spur cpu: Konvergenzverhalten auf (9, 18) (keine Plangroesse), NEB, Budget 110 s.
set -u
B=/home/fmh/fmhc-physics-remote/z2-schutz-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=$B/code/z2.py
A=$B/rauch3
mkdir -p $A
cd $B/code || exit 1
run() { local name=$1; shift; bash $K cpu "$name" "$@" >> $A/$name.log 2>&1; echo "rc=$? $name $(date -u +%H:%M:%S)" >> $A/kette-cpu.out; }
echo "kette start $(date -u +%H:%M:%S)" >> $A/kette-cpu.out
while [ ! -e $B/rauch2/cpu.fertig ]; do sleep 2; done
run z2Ps9 $C start --r0 9 --R 18 --nmax 20000 --ftol 1e-7 --budget 100 --aus $A
touch $A/start.fertig
run z2Pn9 $C weg --aufgabe haupt --verfahren neb --r0 9 --R 18 --start $A/start-r9-R18.npz --M 12 --nmax 6000 --nvor 150 --budget 110 --aus $A
echo "kette ende $(date -u +%H:%M:%S)" >> $A/kette-cpu.out
touch $A/cpu.fertig
