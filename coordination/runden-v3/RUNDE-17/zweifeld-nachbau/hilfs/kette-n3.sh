#!/bin/bash
# Runde 17 ZWEIFELD-NACHBAU, PLAN-NACHTRAG-3. Aufruf: kette-n3.sh <spur> <stufe>
cd /home/fmh/fmhc-physics-remote/runde17-zweifeld-nachbau || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SP=$1; ST=$2
bash $K $SP z17-n3w2-m2-st$ST code/zweifeld_n3.py kand W2 M2 $ST aus/prof-M2.npz aus/n3w2-kand-M2-st$ST.json aus/zeilen-M2-st1-b/*.json aus/zeilen-M2-st2-b/*.json > logs/N3W2-M2-st$ST.log 2>&1
bash $K $SP z17-n3w2-m1-st$ST code/zweifeld_n3.py kand W2 M1 $ST aus/prof-M1.npz aus/n3w2-kand-M1-st$ST.json aus/zeilen-M1-st1/*.json aus/zeilen-M1-st2/*.json > logs/N3W2-M1-st$ST.log 2>&1
bash $K $SP z17-n3w1-m2-st$ST code/zweifeld_n3.py kand W1 M2 $ST aus/prof-M2.npz aus/n3w1-kand-M2-st$ST.json aus/zeilen-M2-st1-b/*.json aus/zeilen-M2-st2-b/*.json > logs/N3W1-M2-st$ST.log 2>&1
echo fertig > logs/kette-n3-st$ST.fertig
