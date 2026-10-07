#!/bin/bash
# Z2-SCHUTZ-1, Hauptlaeufe Spur cpu7 (PLAN Abschnitt 6): Start G1 und G2, Bisektion G1 und G2 (A), CI-NEB G1 und G2 (B),
# Hesse G1 und G2 (G2 mit ZS0-Endpunkten), danach die Auswertung. Eingefrorener Code, je Lauf genau einmal.
set -u
B=/home/fmh/fmhc-physics-remote/z2-schutz-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=$B/code/z2.py
A=$B/lauf
E=$B/eingaben-gfn1
NB="--M 6 --nmax 6000 --nvor 50 --budget 480 --ftol_ci 5e-3 --ftol_band 1.0"
cd $B/code || exit 1
run() { local name=$1; shift; bash $K cpu7 "$name" "$@" >> $A/$name.log 2>&1; echo "rc=$? $name $(date -u +%H:%M:%S)" >> $A/kette-cpu7.out; }
echo "kette start $(date -u +%H:%M:%S)" >> $A/kette-cpu7.out
run z2S1 $C start --r0 10 --R 20 --nmax 20000 --ftol 1e-7 --budget 540 --aus $A
run z2S2 $C start --r0 12 --R 24 --nmax 20000 --ftol 1e-7 --budget 540 --aus $A
run z2A1 $C bisekt --r0 10 --R 20 --start $A/start-r10-R20.npz --nmax 6000 --budget 480 --aus $A
run z2A2 $C bisekt --r0 12 --R 24 --start $A/start-r12-R24.npz --nmax 6000 --budget 480 --aus $A
run z2B1 $C weg --aufgabe haupt --verfahren neb --r0 10 --R 20 --start $A/start-r10-R20.npz --zugpfad $A/bisekt-r10-R20.npz --zug_von 0 $NB --aus $A
run z2B2 $C weg --aufgabe haupt --verfahren neb --r0 12 --R 24 --start $A/start-r12-R24.npz --zugpfad $A/bisekt-r12-R24.npz --zug_von 0 $NB --aus $A
run z2H1 $C hesse --r0 10 --R 20 --start $A/start-r10-R20.npz --zusatz SB=$A/weg-haupt-r10-R20-neb.npz:X --aus $A
run z2H2 $C hesse --r0 12 --R 24 --start $A/start-r12-R24.npz --zusatz SB=$A/weg-haupt-r12-R24-neb.npz:X Z420=$E/prot-diamant-so3-d10-zust.npz:420 Zend=$E/stoss-diamant-so3-T420-e0.01-end.npz:q --aus $A
while [ ! -e $A/cpu.fertig ]; do sleep 5; done
run z2Ausw $B/code/auswertung_z2.py --lauf $A --eingaben $E --aus $A
echo "kette ende $(date -u +%H:%M:%S)" >> $A/kette-cpu7.out
touch $A/alles.fertig
