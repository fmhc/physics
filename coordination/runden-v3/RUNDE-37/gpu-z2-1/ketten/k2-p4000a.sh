#!/bin/bash
# GPU-Z2-1, Kette 2 Spur p4000a: grosse Kugeln bei festem Kern r0 = 10: R = 40, dann R = 64 (start quat, bisekt, weg).
# Bisektion mit --nbis 4000 (CPU-Wert 1500; groessere Netze relaxieren langsamer), sonst Parameter wie Z2-SCHUTZ-2.
set -u
B=/home/fmh/fmhc-physics-remote/gpu-z2-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=$B/code/gz1.py
A=$B/lauf/gross
mkdir -p $A
cd $B/code || exit 1
run() { local name=$1; shift; bash $K p4000a "$name" "$@" >> $A/$name.log 2>&1; echo "rc=$? $name $(date -u +%H:%M:%S)" >> $A/kette-p4000a.out; }
gr() {
  nvidia-smi --query-gpu=index,memory.used,memory.free --format=csv,noheader | tr '\n' ' ' >> $A/kette-p4000a.out; echo >> $A/kette-p4000a.out
  run "gz1s$1" $C start --r0 $2 --R $3 --darst quat --budget 560 --aus $A
  run "gz1b$1" $C bisekt --r0 $2 --R $3 --start $A/start-r$2-R$3.npz --budget 560 --nbis 4000 --aus $A
  run "gz1w$1" $C weg --r0 $2 --R $3 --start $A/start-r$2-R$3.npz --zugpfad $A/bisekt-r$2-R$3.npz --budget 480 --aus $A
}
echo "kette start $(date -u +%H:%M:%S)" >> $A/kette-p4000a.out
gr 1040 10 40
gr 1064 10 64
echo "kette ende $(date -u +%H:%M:%S)" >> $A/kette-p4000a.out
touch $A/k2a.fertig
