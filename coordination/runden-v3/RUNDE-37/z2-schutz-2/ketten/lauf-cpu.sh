#!/bin/bash
# Z2-SCHUTZ-2, Hauptlaeufe Spur cpu (PLAN Abschnitt 9): (10, 32) start, bisekt; (10, 28) start, bisekt, weg;
# (10, 32) weg. Eingefrorener Code, je Lauf genau einmal.
set -u
B=/home/fmh/fmhc-physics-remote/z2-schutz-2
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=$B/code/z2s2.py
A=$B/lauf
mkdir -p $A
cd $B/code || exit 1
run() { local name=$1; shift; bash $K cpu "$name" "$@" >> $A/$name.log 2>&1; echo "rc=$? $name $(date -u +%H:%M:%S)" >> $A/kette-cpu.out; }
st() { run "z2T$1s" $C start --r0 $2 --R $3 --budget 540 --aus $A; }
bi() { run "z2T$1b" $C bisekt --r0 $2 --R $3 --start $A/start-r$2-R$3.npz --budget 540 --aus $A; }
wg() { run "z2T$1w" $C weg --r0 $2 --R $3 --start $A/start-r$2-R$3.npz --zugpfad $A/bisekt-r$2-R$3.npz --M 6 --nmax 6000 --nvor 50 --budget 480 --ftol_ci 5e-3 --ftol_band 1.0 --aus $A; }
echo "kette start $(date -u +%H:%M:%S)" >> $A/kette-cpu.out
st 1032 10 32
bi 1032 10 32
st 1028 10 28
bi 1028 10 28
wg 1028 10 28
wg 1032 10 32
touch $A/cpu.fertig
echo "kette ende $(date -u +%H:%M:%S)" >> $A/kette-cpu.out
