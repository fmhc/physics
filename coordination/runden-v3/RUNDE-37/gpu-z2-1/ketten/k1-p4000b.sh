#!/bin/bash
# GPU-Z2-1, Kette 1 Spur p4000b: Abgleich Gradient und Zeit je Gradient bei (10, 32) (pruef, E_S aus der CPU-npz).
set -u
B=/home/fmh/fmhc-physics-remote/gpu-z2-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=$B/code/gz1.py
A=$B/lauf/abgleich
REF=/home/fmh/fmhc-physics-remote/z2-schutz-2/lauf
mkdir -p $A
cd $B/code || exit 1
run() { local name=$1; shift; bash $K p4000b "$name" "$@" >> $A/$name.log 2>&1; echo "rc=$? $name $(date -u +%H:%M:%S)" >> $A/kette-p4000b.out; }
echo "kette start $(date -u +%H:%M:%S)" >> $A/kette-p4000b.out
nvidia-smi --query-gpu=index,memory.used,memory.free --format=csv,noheader >> $A/kette-p4000b.out
run gz1p1032 $C pruef --r0 10 --R 32 --start $REF/start-r10-R32.npz --nzufall 1 --aus $A
echo "kette ende $(date -u +%H:%M:%S)" >> $A/kette-p4000b.out
touch $A/p4000b.fertig
