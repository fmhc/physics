#!/bin/bash
# GPU-Z2-1, Kette 1 Spur p4000a: Abgleich (10, 20) gegen Z2-SCHUTZ-2: pruef, start (quat), bisekt, weg (CI-NEB psi).
set -u
B=/home/fmh/fmhc-physics-remote/gpu-z2-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=$B/code/gz1.py
A=$B/lauf/abgleich
REF=/home/fmh/fmhc-physics-remote/z2-schutz-2/lauf
mkdir -p $A
cd $B/code || exit 1
run() { local name=$1; shift; bash $K p4000a "$name" "$@" >> $A/$name.log 2>&1; echo "rc=$? $name $(date -u +%H:%M:%S)" >> $A/kette-p4000a.out; }
echo "kette start $(date -u +%H:%M:%S)" >> $A/kette-p4000a.out
nvidia-smi --query-gpu=index,memory.used,memory.free --format=csv,noheader >> $A/kette-p4000a.out
run gz1p1020 $C pruef --r0 10 --R 20 --start $REF/start-r10-R20.npz --aus $A
run gz1s1020 $C start --r0 10 --R 20 --darst quat --budget 560 --aus $A
run gz1b1020 $C bisekt --r0 10 --R 20 --start $A/start-r10-R20.npz --budget 560 --aus $A
run gz1w1020 $C weg --r0 10 --R 20 --start $A/start-r10-R20.npz --zugpfad $A/bisekt-r10-R20.npz --budget 480 --aus $A
echo "kette ende $(date -u +%H:%M:%S)" >> $A/kette-p4000a.out
touch $A/p4000a.fertig
