#!/bin/bash
# Z2-SCHUTZ-1, Rauchtest 5 Spur cpu: Keim und Weg S -> K auf (9, 18) (keine Plangroesse), NEB, M = 8, Budget 110 s.
set -u
B=/home/fmh/fmhc-physics-remote/z2-schutz-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=$B/code/z2.py
A=$B/rauch5
mkdir -p $A
cd $B/code || exit 1
run() { local name=$1; shift; bash $K cpu "$name" "$@" >> $A/$name.log 2>&1; echo "rc=$? $name $(date -u +%H:%M:%S)" >> $A/kette-cpu.out; }
echo "kette start $(date -u +%H:%M:%S)" >> $A/kette-cpu.out
run z2Ns9 $C start --r0 9 --R 18 --nmax 20000 --ftol 1e-7 --budget 100 --aus $A
run z2Nk9 $C keim --r0 9 --R 18 --start $A/start-r9-R18.npz --d_grad 30 --nmax 6000 --budget 110 --aus $A
touch $A/keim.fertig
run z2Nn9 $C weg --aufgabe haupt --verfahren neb --r0 9 --R 18 --start $A/start-r9-R18.npz --keim $A/keim-r9-R18.npz --M 8 --nmax 6000 --nvor 150 --budget 110 --ftol_ci 5e-3 --ftol_band 1.0 --aus $A
echo "kette ende $(date -u +%H:%M:%S)" >> $A/kette-cpu.out
touch $A/cpu.fertig
