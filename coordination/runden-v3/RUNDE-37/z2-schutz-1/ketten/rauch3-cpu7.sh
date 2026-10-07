#!/bin/bash
# Z2-SCHUTZ-1, Rauchtest 3 Spur cpu7: Konvergenzverhalten auf (9, 18), Stringmethode, Budget 110 s.
set -u
B=/home/fmh/fmhc-physics-remote/z2-schutz-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=$B/code/z2.py
A=$B/rauch3
mkdir -p $A
cd $B/code || exit 1
run() { local name=$1; shift; bash $K cpu7 "$name" "$@" >> $A/$name.log 2>&1; echo "rc=$? $name $(date -u +%H:%M:%S)" >> $A/kette-cpu7.out; }
echo "kette start $(date -u +%H:%M:%S)" >> $A/kette-cpu7.out
while [ ! -e $B/rauch2/alles.fertig ]; do sleep 2; done
while [ ! -e $A/start.fertig ]; do sleep 2; done
run z2Pt9 $C weg --aufgabe haupt --verfahren string --r0 9 --R 18 --start $A/start-r9-R18.npz --M 12 --nmax 6000 --nvor 150 --budget 110 --aus $A
echo "kette ende $(date -u +%H:%M:%S)" >> $A/kette-cpu7.out
touch $A/cpu7.fertig
