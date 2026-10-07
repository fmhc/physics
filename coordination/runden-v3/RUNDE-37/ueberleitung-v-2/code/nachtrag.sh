#!/bin/bash
# Nachtrag nt1 (beschreibend): h*_letzt bei kl = 0,0005 bis 0,002, drei Richtungen parallel.
set -u
D=/home/fmh/fmhc-physics-remote/ueberleitung-v-2
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
N=$D/nachtrag
mkdir -p $N
cd $D
bash $K cpu2 uw-nt1-100 code/nachtrag_hs.py --richtung 100 --out $N/nt1-100.json > $N/nt1-100.log 2>&1 &
bash $K cpu3 uw-nt1-111 code/nachtrag_hs.py --richtung 111 --out $N/nt1-111.json > $N/nt1-111.log 2>&1 &
bash $K cpu4 uw-nt1-321 code/nachtrag_hs.py --richtung 321 --out $N/nt1-321.json > $N/nt1-321.log 2>&1 &
wait
echo "nachtrag nt1 fertig $(date -u +%H:%M:%S)" > $N/nt1-fertig.txt
