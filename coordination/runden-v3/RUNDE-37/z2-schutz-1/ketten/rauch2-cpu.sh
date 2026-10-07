#!/bin/bash
# Z2-SCHUTZ-1, Rauchtest 2 Spur cpu: neue Bildanordnung (P, N, k); (6, 12) kurz, (14, 28) nur Laufzeit.
set -u
B=/home/fmh/fmhc-physics-remote/z2-schutz-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=$B/code/z2.py
A=$B/rauch2
mkdir -p $A
cd $B/code || exit 1
run() { local name=$1; shift; bash $K cpu "$name" "$@" >> $A/$name.log 2>&1; echo "rc=$? $name $(date -u +%H:%M:%S)" >> $A/kette-cpu.out; }
echo "kette start $(date -u +%H:%M:%S)" >> $A/kette-cpu.out
run z2Qs6 $C start --r0 6 --R 12 --nmax 500 --aus $A
run z2Qn6 $C weg --aufgabe haupt --verfahren neb --r0 6 --R 12 --start $A/start-r6-R12.npz --nmax 60 --nvor 20 --budget 100 --aus $A
run z2Qt6 $C weg --aufgabe haupt --verfahren string --r0 6 --R 12 --start $A/start-r6-R12.npz --nmax 60 --nvor 20 --budget 100 --aus $A
run z2Qh6 $C hesse --r0 6 --R 12 --start $A/start-r6-R12.npz --zusatz SA=$A/weg-haupt-r6-R12-neb.npz:X --aus $A
run z2Qs14 $C start --r0 14 --R 28 --nmax 30 --aus $A
run z2Qn14 $C weg --aufgabe haupt --verfahren neb --r0 14 --R 28 --start $A/start-r14-R28.npz --nmax 20 --nvor 5 --budget 100 --aus $A
run z2Qt14 $C weg --aufgabe haupt --verfahren string --r0 14 --R 28 --start $A/start-r14-R28.npz --nmax 20 --nvor 5 --budget 100 --aus $A
echo "kette ende $(date -u +%H:%M:%S)" >> $A/kette-cpu.out
touch $A/cpu.fertig
