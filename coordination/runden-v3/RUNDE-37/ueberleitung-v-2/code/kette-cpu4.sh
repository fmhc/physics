#!/bin/bash
# Hauptlaeufe Spur cpu4 (PLAN 8): vneu Teil 1, hstern 111.
set -u
D=/home/fmh/fmhc-physics-remote/ueberleitung-v-2
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
L=$D/lauf
cd $D
bash $K cpu4 uw-n1 code/uw.py punkte --netz V --menge neu --teil 1 --out $L/vneu1.json > $L/vneu1.log 2>&1
bash $K cpu4 uw-hs111 code/uw.py hstern --richtung 111 --out $L/hs111.json > $L/hs111.log 2>&1
echo "kette cpu4 fertig $(date -u +%H:%M:%S)" > $L/kette-cpu4.txt
