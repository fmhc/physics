#!/bin/bash
# Rauchtest r1 (technisch, PLAN 8): je Netz K1 bis K5, K7, K8, Netzgroessen, Laufzeit. Aufruf im Ordner ueberleitung-v-2.
set -u
D=/home/fmh/fmhc-physics-remote/ueberleitung-v-2
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
R=$D/rauch
mkdir -p $R
cd $D
bash $K cpu2 uw-r1-v code/uw.py rauch1 --netz V --out $R/r1-V.json > $R/r1-V.log 2>&1 &
bash $K cpu3 uw-r1-s code/uw.py rauch1 --netz S --out $R/r1-S.json > $R/r1-S.log 2>&1 &
bash $K cpu4 uw-r1-b1 code/uw.py rauch1 --netz B1 --out $R/r1-B1.json > $R/r1-B1.log 2>&1 &
wait
echo "rauch r1 fertig $(date -u +%H:%M:%S)" > $R/r1-fertig.txt
