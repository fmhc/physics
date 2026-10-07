#!/bin/bash
# Z2-SCHUTZ-2, Rauchtest 5 Spur cpu: (11, 22) (nicht im Raster) start, bisekt (mit Stufe 2), weg. Je Lauf <= 120 s.
set -u
B=/home/fmh/fmhc-physics-remote/z2-schutz-2
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=$B/code/z2s2.py
A=$B/rauch5
mkdir -p $A
cd $B/code || exit 1
run() { local name=$1; shift; bash $K cpu "$name" "$@" >> $A/$name.log 2>&1; echo "rc=$? $name $(date -u +%H:%M:%S)" >> $A/kette-cpu.out; }
echo "kette start $(date -u +%H:%M:%S)" >> $A/kette-cpu.out
cp $B/rauch3/start-r11-R22.npz $B/rauch3/start-r11-R22.json $A/
run z2s2R5b11 $C bisekt --r0 11 --R 22 --start $A/start-r11-R22.npz --budget 110 --aus $A
run z2s2R5w11 $C weg --r0 11 --R 22 --start $A/start-r11-R22.npz --zugpfad $A/bisekt-r11-R22.npz --nmax 6000 --budget 100 --aus $A
run z2s2R5aus $B/code/auswertung_z2s2.py --lauf $A --aus $A
echo "kette ende $(date -u +%H:%M:%S)" >> $A/kette-cpu.out
touch $A/cpu.fertig
