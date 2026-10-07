#!/bin/bash
# Folgeauftrag Licht, zweite Kette: W4D mit h = 2^-4 ... 2^-10 (quartisch), dann Auswertung mit Massenterm-Fit.
set -u
D=/home/fmh/fmhc-physics-remote/ueberleitung-v-1/licht
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
L=$D/lauf
cd $D
(bash $K cpu6 uvl-g1 code/licht.py w4d --teil 1 --hset grob --out $L/g4d1.json > $L/g4d1.log 2>&1; echo fertig > $L/g4d1.txt) &
bash $K cpu5 uvl-g0 code/licht.py w4d --teil 0 --hset grob --out $L/g4d0.json > $L/g4d0.log 2>&1
until [ -f $L/g4d1.txt ]; do sleep 3; done
bash $K cpu5 uvl-aw2 code/licht.py aw --ein gw=/home/fmh/fmhc-physics-remote/ueberleitung-v-1/nachtrag/nt3r.json dec=$L/dec.json w4a=$L/w4d0.json w4b=$L/w4d1.json g4a=$L/g4d0.json g4b=$L/g4d1.json --out $L/aw2.json > $L/aw2.log 2>&1
echo "kette2 fertig $(date -u +%H:%M:%S)" > $L/kette2.txt
