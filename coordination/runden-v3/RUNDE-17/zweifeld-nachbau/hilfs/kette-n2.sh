#!/bin/bash
# Runde 17 ZWEIFELD-NACHBAU, PLAN-NACHTRAG-2: kand mit W2 (zweifeld_n2.py). Aufruf: kette-n2.sh <spur> <stufe>
cd /home/fmh/fmhc-physics-remote/runde17-zweifeld-nachbau || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SP=$1; ST=$2
bash $K $SP z17-n2-k1-st$ST code/zweifeld_n2.py kand M1 $ST aus/prof-M1.npz aus/n2-kand-M1-st$ST.json aus/zeilen-M1-st1/*.json aus/zeilen-M1-st2/*.json > logs/N2-K1-st$ST.log 2>&1
while [ ! -f logs/kette-m2b-kopie.txt ]; do sleep 5; done
bash $K $SP z17-n2-m2-st$ST code/zweifeld_n2.py kand M2 $ST aus/prof-M2.npz aus/n2-kand-M2-st$ST.json aus/zeilen-M2-st1-b/*.json aus/zeilen-M2-st2-b/*.json > logs/N2-M2-st$ST.log 2>&1
echo fertig > logs/kette-n2-st$ST.fertig
