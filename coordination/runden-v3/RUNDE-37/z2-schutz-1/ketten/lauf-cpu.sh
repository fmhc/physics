#!/bin/bash
# Z2-SCHUTZ-1, Hauptlaeufe Spur cpu (PLAN Abschnitt 6): Start G3, Bisektion G3 (A), CI-NEB G3 (B), ZS0 CI-NEB und
# String, SO(2)-Gegenprobe, Hesse G3. Eingefrorener Code, je Lauf genau einmal.
set -u
B=/home/fmh/fmhc-physics-remote/z2-schutz-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=$B/code/z2.py
A=$B/lauf
E=$B/eingaben-gfn1
NB="--M 6 --nmax 6000 --nvor 50 --budget 480 --ftol_ci 5e-3 --ftol_band 1.0"
Z0="--M 8 --nmax 6000 --nvor 150 --budget 240 --ftol_ci 5e-3 --ftol_band 5e-2"
cd $B/code || exit 1
run() { local name=$1; shift; bash $K cpu "$name" "$@" >> $A/$name.log 2>&1; echo "rc=$? $name $(date -u +%H:%M:%S)" >> $A/kette-cpu.out; }
echo "kette start $(date -u +%H:%M:%S)" >> $A/kette-cpu.out
run z2S3 $C start --r0 14 --R 28 --nmax 20000 --ftol 1e-7 --budget 540 --aus $A
run z2A3 $C bisekt --r0 14 --R 28 --start $A/start-r14-R28.npz --nmax 6000 --budget 480 --aus $A
run z2B3 $C weg --aufgabe haupt --verfahren neb --r0 14 --R 28 --start $A/start-r14-R28.npz --zugpfad $A/bisekt-r14-R28.npz --zug_von 0 $NB --aus $A
run z2Z0A $C weg --aufgabe zs0 --verfahren neb --eingaben $E $Z0 --aus $A
run z2Z0B $C weg --aufgabe zs0 --verfahren string --eingaben $E $Z0 --aus $A
run z2SO2 $C weg --aufgabe so2 --verfahren neb --eingaben $E --M 8 --nmax 6000 --nvor 150 --budget 120 --ftol_ci 5e-3 --ftol_band 5e-2 --nmax_rel 20000 --aus $A
run z2H3 $C hesse --r0 14 --R 28 --start $A/start-r14-R28.npz --zusatz SB=$A/weg-haupt-r14-R28-neb.npz:X --aus $A
touch $A/cpu.fertig
echo "kette ende $(date -u +%H:%M:%S)" >> $A/kette-cpu.out
