#!/bin/bash
# Folgeauftrag Licht (ohne Karte): dec + w4d Teil 0 auf cpu5, w4d Teil 1 auf cpu6, danach aw auf cpu5.
set -u
D=/home/fmh/fmhc-physics-remote/ueberleitung-v-1/licht
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
L=$D/lauf
cd $D
(bash $K cpu6 uvl-w1 code/licht.py w4d --teil 1 --out $L/w4d1.json > $L/w4d1.log 2>&1; echo fertig > $L/w4d1.txt) &
bash $K cpu5 uvl-dec code/licht.py dec --out $L/dec.json > $L/dec.log 2>&1
bash $K cpu5 uvl-w0 code/licht.py w4d --teil 0 --out $L/w4d0.json > $L/w4d0.log 2>&1
until [ -f $L/w4d1.txt ]; do sleep 3; done
bash $K cpu5 uvl-aw code/licht.py aw --ein gw=/home/fmh/fmhc-physics-remote/ueberleitung-v-1/nachtrag/nt3r.json dec=$L/dec.json w4a=$L/w4d0.json w4b=$L/w4d1.json --out $L/aw.json > $L/aw.log 2>&1
echo "kette fertig $(date -u +%H:%M:%S)" > $L/kette.txt
