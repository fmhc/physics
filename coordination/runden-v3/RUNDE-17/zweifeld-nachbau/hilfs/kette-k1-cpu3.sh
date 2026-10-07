#!/bin/bash
# Runde 17 ZWEIFELD-NACHBAU: K1-Kette Spur cpu3 (L3 scan M1 Stufe 1, dann L5 kand M1 Stufe 1)
cd /home/fmh/fmhc-physics-remote/runde17-zweifeld-nachbau || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
Z1="0.786 0.788 0.79 0.792 0.794 0.796 0.798 0.8 0.802 0.804 0.806 0.808 0.81"
bash $K cpu3 z17-k1-scan1 code/zweifeld.py scan M1 1 aus/prof-M1.npz aus/zeilen-M1-st1 $Z1 > logs/L3-scan-M1-st1.log 2>&1
while [ "$(ls aus/zeilen-M1-st2/*.json 2>/dev/null | wc -l)" -lt 13 ]; do sleep 5; done
sleep 2
bash $K cpu3 z17-k1-kand1 code/zweifeld.py kand M1 1 aus/prof-M1.npz aus/kand-M1-st1.json aus/zeilen-M1-st1/*.json aus/zeilen-M1-st2/*.json > logs/L5-kand-M1-st1.log 2>&1
echo kette-k1-cpu3 fertig > logs/kette-k1-cpu3.fertig
