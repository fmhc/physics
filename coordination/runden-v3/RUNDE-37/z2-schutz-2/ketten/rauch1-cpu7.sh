#!/bin/bash
# Z2-SCHUTZ-2, Rauchtest 1 Spur cpu7: (9, 18) start, pruef (Konsistenz psi gegen Quaternion), bisekt, weg. Je Lauf <= 120 s.
set -u
B=/home/fmh/fmhc-physics-remote/z2-schutz-2
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=$B/code/z2s2.py
A=$B/rauch1
mkdir -p $A
cd $B/code || exit 1
run() { local name=$1; shift; bash $K cpu7 "$name" "$@" >> $A/$name.log 2>&1; echo "rc=$? $name $(date -u +%H:%M:%S)" >> $A/kette-cpu7.out; }
echo "kette start $(date -u +%H:%M:%S)" >> $A/kette-cpu7.out
run z2s2R1s9 $C start --r0 9 --R 18 --budget 100 --aus $A
run z2s2R1p9 $C pruef --r0 9 --R 18 --start $A/start-r9-R18.npz --nschritt 60 --aus $A
run z2s2R1b9 $C bisekt --r0 9 --R 18 --start $A/start-r9-R18.npz --budget 110 --aus $A
run z2s2R1w9 $C weg --r0 9 --R 18 --start $A/start-r9-R18.npz --zugpfad $A/bisekt-r9-R18.npz --nmax 6000 --budget 100 --aus $A
echo "kette ende $(date -u +%H:%M:%S)" >> $A/kette-cpu7.out
touch $A/cpu7.fertig
