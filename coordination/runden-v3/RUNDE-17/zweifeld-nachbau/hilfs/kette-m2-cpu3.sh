#!/bin/bash
# Runde 17 ZWEIFELD-NACHBAU: M2-Kette Spur cpu3 (scan Stufe 1 in zwei Aufrufen, dann kand Stufe 1)
cd /home/fmh/fmhc-physics-remote/runde17-zweifeld-nachbau || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
A=$(seq -f "%.3f" 0.830 0.002 0.870 | tr '\n' ' ')
B=$(seq -f "%.3f" 0.872 0.002 0.910 | tr '\n' ' ')
bash $K cpu3 z17-m2-scan1a code/zweifeld.py scan M2 1 aus/prof-M2.npz aus/zeilen-M2-st1 $A > logs/L7-scan-M2-st1a.log 2>&1
bash $K cpu3 z17-m2-scan1b code/zweifeld.py scan M2 1 aus/prof-M2.npz aus/zeilen-M2-st1 $B > logs/L8-scan-M2-st1b.log 2>&1
while [ "$(ls aus/zeilen-M2-st2/*.json 2>/dev/null | wc -l)" -lt 41 ]; do sleep 5; done
sleep 2
bash $K cpu3 z17-m2-kand1 code/zweifeld.py kand M2 1 aus/prof-M2.npz aus/kand-M2-st1.json aus/zeilen-M2-st1/*.json aus/zeilen-M2-st2/*.json > logs/L13-kand-M2-st1.log 2>&1
echo kette-m2-cpu3 fertig > logs/kette-m2-cpu3.fertig
