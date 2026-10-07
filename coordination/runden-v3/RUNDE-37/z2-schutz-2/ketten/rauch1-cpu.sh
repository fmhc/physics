#!/bin/bash
# Z2-SCHUTZ-2, Rauchtest 1 Spur cpu: (6, 12) start, bisekt, weg; Laufzeitprobe (10, 32) im Modus pruef (20 Schritte,
# harmonisches Profil ohne Relaxation). Je Lauf <= 120 s.
set -u
B=/home/fmh/fmhc-physics-remote/z2-schutz-2
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=$B/code/z2s2.py
A=$B/rauch1
mkdir -p $A
cd $B/code || exit 1
run() { local name=$1; shift; bash $K cpu "$name" "$@" >> $A/$name.log 2>&1; echo "rc=$? $name $(date -u +%H:%M:%S)" >> $A/kette-cpu.out; }
echo "kette start $(date -u +%H:%M:%S)" >> $A/kette-cpu.out
run z2s2R1p32 $C pruef --r0 10 --R 32 --nschritt 20 --aus $A
run z2s2R1s6 $C start --r0 6 --R 12 --budget 100 --aus $A
run z2s2R1b6 $C bisekt --r0 6 --R 12 --start $A/start-r6-R12.npz --budget 110 --aus $A
run z2s2R1w6 $C weg --r0 6 --R 12 --start $A/start-r6-R12.npz --zugpfad $A/bisekt-r6-R12.npz --nmax 6000 --budget 100 --aus $A
echo "kette ende $(date -u +%H:%M:%S)" >> $A/kette-cpu.out
touch $A/cpu.fertig
