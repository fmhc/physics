#!/bin/bash
# Runde 17 ZWEIFELD-NACHBAU: Wiederholung M2-Scan Stufe 1 (erste Kette scheiterte an "0,830" aus seq unter de_DE).
# Die kand-Aufrufe macht die alte Kette (wartet auf 41 Dateien je Stufe in aus/zeilen-M2-st1 und -st2).
cd /home/fmh/fmhc-physics-remote/runde17-zweifeld-nachbau || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
A=$(LC_ALL=C seq -f "%.3f" 0.830 0.002 0.870 | tr '\n' ' ')
B=$(LC_ALL=C seq -f "%.3f" 0.872 0.002 0.910 | tr '\n' ' ')
bash $K cpu3 z17-m2-scan1a2 code/zweifeld.py scan M2 1 aus/prof-M2.npz aus/zeilen-M2-st1-b $A > logs/L7b-scan-M2-st1a.log 2>&1
bash $K cpu3 z17-m2-scan1b2 code/zweifeld.py scan M2 1 aus/prof-M2.npz aus/zeilen-M2-st1-b $B > logs/L8b-scan-M2-st1b.log 2>&1
echo fertig > logs/kette-m2b-cpu3.fertig
