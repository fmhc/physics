#!/bin/bash
# Runde 17 ZWEIFELD-NACHBAU: Spur cpu4 (L2b profile M2, L4 scan M1 Stufe 2, L6 kand M1 Stufe 2)
cd /home/fmh/fmhc-physics-remote/runde17-zweifeld-nachbau || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
Z1="0.786 0.788 0.79 0.792 0.794 0.796 0.798 0.8 0.802 0.804 0.806 0.808 0.81"
bash $K cpu4 z17-prof-m2b code/zweifeld.py profile M2 aus/prof-M2 > logs/L2b-prof-M2.log 2>&1
bash $K cpu4 z17-k1-scan2 code/zweifeld.py scan M1 2 aus/prof-M1.npz aus/zeilen-M1-st2 $Z1 > logs/L4-scan-M1-st2.log 2>&1
while [ "$(ls aus/zeilen-M1-st1/*.json 2>/dev/null | wc -l)" -lt 13 ]; do sleep 5; done
sleep 2
bash $K cpu4 z17-k1-kand2 code/zweifeld.py kand M1 2 aus/prof-M1.npz aus/kand-M1-st2.json aus/zeilen-M1-st1/*.json aus/zeilen-M1-st2/*.json > logs/L6-kand-M1-st2.log 2>&1
echo kette-cpu4-a fertig > logs/kette-cpu4-a.fertig
