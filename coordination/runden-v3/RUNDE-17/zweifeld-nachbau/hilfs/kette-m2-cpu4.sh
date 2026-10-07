#!/bin/bash
# Runde 17 ZWEIFELD-NACHBAU: M2-Kette Spur cpu4 (scan Stufe 2 in vier Aufrufen, dann kand Stufe 2)
cd /home/fmh/fmhc-physics-remote/runde17-zweifeld-nachbau || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
while [ ! -f logs/kette-cpu4-a.fertig ]; do sleep 5; done
A=$(seq -f "%.3f" 0.830 0.002 0.850 | tr '\n' ' ')
B=$(seq -f "%.3f" 0.852 0.002 0.870 | tr '\n' ' ')
C=$(seq -f "%.3f" 0.872 0.002 0.890 | tr '\n' ' ')
D=$(seq -f "%.3f" 0.892 0.002 0.910 | tr '\n' ' ')
bash $K cpu4 z17-m2-scan2a code/zweifeld.py scan M2 2 aus/prof-M2.npz aus/zeilen-M2-st2 $A > logs/L9-scan-M2-st2a.log 2>&1
bash $K cpu4 z17-m2-scan2b code/zweifeld.py scan M2 2 aus/prof-M2.npz aus/zeilen-M2-st2 $B > logs/L10-scan-M2-st2b.log 2>&1
bash $K cpu4 z17-m2-scan2c code/zweifeld.py scan M2 2 aus/prof-M2.npz aus/zeilen-M2-st2 $C > logs/L11-scan-M2-st2c.log 2>&1
bash $K cpu4 z17-m2-scan2d code/zweifeld.py scan M2 2 aus/prof-M2.npz aus/zeilen-M2-st2 $D > logs/L12-scan-M2-st2d.log 2>&1
while [ "$(ls aus/zeilen-M2-st1/*.json 2>/dev/null | wc -l)" -lt 41 ]; do sleep 5; done
sleep 2
bash $K cpu4 z17-m2-kand2 code/zweifeld.py kand M2 2 aus/prof-M2.npz aus/kand-M2-st2.json aus/zeilen-M2-st1/*.json aus/zeilen-M2-st2/*.json > logs/L14-kand-M2-st2.log 2>&1
echo kette-m2-cpu4 fertig > logs/kette-m2-cpu4.fertig
