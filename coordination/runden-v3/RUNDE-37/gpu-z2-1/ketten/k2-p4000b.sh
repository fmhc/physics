#!/bin/bash
# GPU-Z2-1, Kette 2 Spur p4000b: Abgleich (10, 32) mit CPU-Parametern (nbis 1500), dann R = 48 (nbis 4000).
set -u
B=/home/fmh/fmhc-physics-remote/gpu-z2-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=$B/code/gz1.py
A=$B/lauf/gross
AB=$B/lauf/abgleich
mkdir -p $A $AB
cd $B/code || exit 1
run() { local name=$1; local d=$2; shift 2; bash $K p4000b "$name" "$@" >> $d/$name.log 2>&1; echo "rc=$? $name $(date -u +%H:%M:%S)" >> $A/kette-p4000b.out; }
echo "kette start $(date -u +%H:%M:%S)" >> $A/kette-p4000b.out
nvidia-smi --query-gpu=index,memory.used,memory.free --format=csv,noheader | tr '\n' ' ' >> $A/kette-p4000b.out; echo >> $A/kette-p4000b.out
run gz1s1032 $AB $C start --r0 10 --R 32 --darst quat --budget 560 --aus $AB
run gz1b1032 $AB $C bisekt --r0 10 --R 32 --start $AB/start-r10-R32.npz --budget 560 --aus $AB
run gz1w1032 $AB $C weg --r0 10 --R 32 --start $AB/start-r10-R32.npz --zugpfad $AB/bisekt-r10-R32.npz --budget 480 --aus $AB
nvidia-smi --query-gpu=index,memory.used,memory.free --format=csv,noheader | tr '\n' ' ' >> $A/kette-p4000b.out; echo >> $A/kette-p4000b.out
run gz1s1048 $A $C start --r0 10 --R 48 --darst quat --budget 560 --aus $A
run gz1b1048 $A $C bisekt --r0 10 --R 48 --start $A/start-r10-R48.npz --budget 560 --nbis 4000 --aus $A
run gz1w1048 $A $C weg --r0 10 --R 48 --start $A/start-r10-R48.npz --zugpfad $A/bisekt-r10-R48.npz --budget 480 --aus $A
echo "kette ende $(date -u +%H:%M:%S)" >> $A/kette-p4000b.out
touch $A/k2b.fertig
