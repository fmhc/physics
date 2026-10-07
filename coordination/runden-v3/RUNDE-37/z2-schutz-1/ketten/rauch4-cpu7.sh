#!/bin/bash
# Z2-SCHUTZ-1, Rauchtest 4 Spur cpu7: ZS0 und SO(2) mit 3 Iterationen (FIRE je Bild), danach Stringmethode S -> K auf (9, 18).
set -u
B=/home/fmh/fmhc-physics-remote/z2-schutz-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=$B/code/z2.py
A=$B/rauch4
mkdir -p $A
cd $B/code || exit 1
run() { local name=$1; shift; bash $K cpu7 "$name" "$@" >> $A/$name.log 2>&1; echo "rc=$? $name $(date -u +%H:%M:%S)" >> $A/kette-cpu7.out; }
echo "kette start $(date -u +%H:%M:%S)" >> $A/kette-cpu7.out
run z2Oz0n $C weg --aufgabe zs0 --verfahren neb --eingaben $B/eingaben-gfn1 --M 8 --nmax 3 --nvor 1 --budget 110 --aus $A
run z2Oo2 $C weg --aufgabe so2 --verfahren neb --eingaben $B/eingaben-gfn1 --M 8 --nmax 3 --nvor 1 --nmax_rel 200 --budget 110 --aus $A
while [ ! -e $A/keim.fertig ]; do sleep 2; done
run z2Ot9 $C weg --aufgabe haupt --verfahren string --r0 9 --R 18 --start $A/start-r9-R18.npz --keim $A/keim-r9-R18.npz --M 8 --nmax 6000 --nvor 150 --budget 110 --ftol_ci 5e-3 --ftol_band 5e-2 --aus $A
while [ ! -e $A/cpu.fertig ]; do sleep 2; done
run z2Oausw $B/code/auswertung_z2.py --lauf $A --eingaben $B/eingaben-gfn1 --aus $A
echo "kette ende $(date -u +%H:%M:%S)" >> $A/kette-cpu7.out
touch $A/alles.fertig
