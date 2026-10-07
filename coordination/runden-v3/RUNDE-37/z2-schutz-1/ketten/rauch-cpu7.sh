#!/bin/bash
# Z2-SCHUTZ-1, Rauchtest Spur cpu7 (PLAN Abschnitt 6): ZS0- und SO(2)-Pfad nur mit 3 Iterationen, Auswertung.
set -u
B=/home/fmh/fmhc-physics-remote/z2-schutz-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=$B/code/z2.py
A=$B/rauch
cd $B/code || exit 1
run() { local name=$1; shift; bash $K cpu7 "$name" "$@" >> $A/$name.log 2>&1; echo "rc=$? $name $(date -u +%H:%M:%S)" >> $A/kette-cpu7.out; }
echo "kette start $(date -u +%H:%M:%S)" >> $A/kette-cpu7.out
run z2Rz0n $C weg --aufgabe zs0 --verfahren neb --eingaben $B/eingaben-gfn1 --nmax 3 --nvor 1 --budget 110 --aus $A
run z2Rz0t $C weg --aufgabe zs0 --verfahren string --eingaben $B/eingaben-gfn1 --nmax 3 --nvor 1 --budget 110 --aus $A
run z2Ro2 $C weg --aufgabe so2 --verfahren neb --eingaben $B/eingaben-gfn1 --nmax 3 --nvor 1 --nmax_rel 200 --budget 110 --aus $A
while [ ! -e $A/cpu.fertig ]; do sleep 5; done
run z2Rausw $B/code/auswertung_z2.py --lauf $A --eingaben $B/eingaben-gfn1 --aus $A
echo "kette ende $(date -u +%H:%M:%S)" >> $A/kette-cpu7.out
touch $A/alles.fertig
