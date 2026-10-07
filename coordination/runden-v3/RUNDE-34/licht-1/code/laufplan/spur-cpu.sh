#!/bin/bash
# LICHT-1 Laufplan (Runde 34), Spur cpu: Teil A (radial) und Statik auf dem Dreier-Netz. Nur kleintest.sh-Aufrufe.
set -u
SPUR=cpu
B=/home/fmh/fmhc-physics-remote/runde34-licht
L=$B/lauf
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
P=$B/code/licht.py
SL=1.2,1.5,2,3,6,12,24,48
cd $L
bash $K $SPUR r34li-radial-haupt $P radial --Q 200 --s $SL --s-dEdQ 1.2,2,6,48 --dr 0.01 --rmax 90 --eps-min 0.0065 --aus $L/radial-haupt.json > $L/log-radial-haupt.txt 2>&1
bash $K $SPUR r34li-radial-dr $P radial --Q 200 --s $SL --dr 0.005 --rmax 90 --eps-min 0.0065 --aus $L/radial-dr.json > $L/log-radial-dr.txt 2>&1
bash $K $SPUR r34li-radial-rmax $P radial --Q 200 --s $SL --dr 0.01 --rmax 120 --eps-min 0.0065 --aus $L/radial-rmax.json > $L/log-radial-rmax.txt 2>&1
bash $K $SPUR r34li-statik-n3 $P statik --n 3 --h 0.3 --R 60 --Q 200 --d 0,1,2,3,4,5,6,7,8,9,10,11,12,14,16,25 --aus $L/statik-n3-h0.3.json > $L/log-statik-n3-h0.3.txt 2>&1
echo "spur $SPUR fertig $(date --iso-8601=seconds)" > $L/fertig-$SPUR.txt
