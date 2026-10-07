#!/bin/bash
# Z2-SCHUTZ-2, Hauptlaeufe Spur cpu7 (PLAN Abschnitt 9): (10, 20), (10, 24), (8, 24), (12, 24), (14, 24) je start, bisekt,
# weg; dann warten auf cpu und Auswertung. Eingefrorener Code, je Lauf genau einmal.
set -u
B=/home/fmh/fmhc-physics-remote/z2-schutz-2
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=$B/code/z2s2.py
A=$B/lauf
mkdir -p $A
cd $B/code || exit 1
run() { local name=$1; shift; bash $K cpu7 "$name" "$@" >> $A/$name.log 2>&1; echo "rc=$? $name $(date -u +%H:%M:%S)" >> $A/kette-cpu7.out; }
st() { run "z2T$1s" $C start --r0 $2 --R $3 --budget 540 --aus $A; }
bi() { run "z2T$1b" $C bisekt --r0 $2 --R $3 --start $A/start-r$2-R$3.npz --budget 540 --aus $A; }
wg() { run "z2T$1w" $C weg --r0 $2 --R $3 --start $A/start-r$2-R$3.npz --zugpfad $A/bisekt-r$2-R$3.npz --M 6 --nmax 6000 --nvor 50 --budget 480 --ftol_ci 5e-3 --ftol_band 1.0 --aus $A; }
echo "kette start $(date -u +%H:%M:%S)" >> $A/kette-cpu7.out
for g in "1020 10 20" "1024 10 24" "824 8 24" "1224 12 24" "1424 14 24"; do
  set -- $g
  st $1 $2 $3
  bi $1 $2 $3
  wg $1 $2 $3
done
while [ ! -e $A/cpu.fertig ]; do sleep 5; done
run z2TAusw $B/code/auswertung_z2s2.py --lauf $A --aus $A
echo "kette ende $(date -u +%H:%M:%S)" >> $A/kette-cpu7.out
touch $A/alles.fertig
