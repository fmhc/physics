#!/bin/bash
# Hauptlaeufe Spur cpu3 (PLAN 8): vneu Teil 0, hstern 100.
set -u
D=/home/fmh/fmhc-physics-remote/ueberleitung-v-2
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
L=$D/lauf
cd $D
bash $K cpu3 uw-n0 code/uw.py punkte --netz V --menge neu --teil 0 --out $L/vneu0.json > $L/vneu0.log 2>&1
bash $K cpu3 uw-hs100 code/uw.py hstern --richtung 100 --out $L/hs100.json > $L/hs100.log 2>&1
echo "kette cpu3 fertig $(date -u +%H:%M:%S)" > $L/kette-cpu3.txt
