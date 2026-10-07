#!/bin/bash
# Z2-SCHUTZ-1, Rauchtest 7 Spur cpu: Bisektion (Verfahren A) und CI-NEB zwischen den Klammerzustaenden (B), (9, 18).
set -u
B=/home/fmh/fmhc-physics-remote/z2-schutz-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=$B/code/z2.py
A=$B/rauch7c
mkdir -p $A
cd $B/code || exit 1
run() { local name=$1; shift; bash $K cpu "$name" "$@" >> $A/$name.log 2>&1; echo "rc=$? $name $(date -u +%H:%M:%S)" >> $A/kette-cpu.out; }
echo "kette start $(date -u +%H:%M:%S)" >> $A/kette-cpu.out
cp $B/rauch5/start-r9-R18.npz $B/rauch5/start-r9-R18.json $A/
run z2Lb9 $C bisekt --r0 9 --R 18 --start $A/start-r9-R18.npz --nmax 6000 --budget 115 --aus $A
run z2Ln9 $C weg --aufgabe haupt --verfahren neb --r0 9 --R 18 --start $A/start-r9-R18.npz --zugpfad $A/bisekt-r9-R18.npz --zug_von 0 --M 6 --nmax 6000 --nvor 50 --budget 110 --ftol_ci 5e-3 --ftol_band 1.0 --aus $A
echo "kette ende $(date -u +%H:%M:%S)" >> $A/kette-cpu.out
touch $A/cpu.fertig
