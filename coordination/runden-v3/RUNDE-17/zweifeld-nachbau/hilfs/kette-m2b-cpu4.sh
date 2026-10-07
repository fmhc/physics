#!/bin/bash
# Runde 17 ZWEIFELD-NACHBAU: Wiederholung M2-Scan Stufe 2; danach Kopie beider Stufen in die Ordner der alten Kette
# (erst Stufe 2, dann Stufe 1), damit deren kand-Aufrufe vollstaendige Zeilensaetze sehen.
cd /home/fmh/fmhc-physics-remote/runde17-zweifeld-nachbau || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
A=$(LC_ALL=C seq -f "%.3f" 0.830 0.002 0.850 | tr '\n' ' ')
B=$(LC_ALL=C seq -f "%.3f" 0.852 0.002 0.870 | tr '\n' ' ')
C=$(LC_ALL=C seq -f "%.3f" 0.872 0.002 0.890 | tr '\n' ' ')
D=$(LC_ALL=C seq -f "%.3f" 0.892 0.002 0.910 | tr '\n' ' ')
bash $K cpu4 z17-m2-scan2a2 code/zweifeld.py scan M2 2 aus/prof-M2.npz aus/zeilen-M2-st2-b $A > logs/L9b-scan-M2-st2a.log 2>&1
bash $K cpu4 z17-m2-scan2b2 code/zweifeld.py scan M2 2 aus/prof-M2.npz aus/zeilen-M2-st2-b $B > logs/L10b-scan-M2-st2b.log 2>&1
bash $K cpu4 z17-m2-scan2c2 code/zweifeld.py scan M2 2 aus/prof-M2.npz aus/zeilen-M2-st2-b $C > logs/L11b-scan-M2-st2c.log 2>&1
bash $K cpu4 z17-m2-scan2d2 code/zweifeld.py scan M2 2 aus/prof-M2.npz aus/zeilen-M2-st2-b $D > logs/L12b-scan-M2-st2d.log 2>&1
while [ ! -f logs/kette-m2b-cpu3.fertig ]; do sleep 5; done
if [ "$(ls aus/zeilen-M2-st1-b/*.json | wc -l)" -eq 41 ] && [ "$(ls aus/zeilen-M2-st2-b/*.json | wc -l)" -eq 41 ]; then
  mkdir -p aus/zeilen-M2-st1 aus/zeilen-M2-st2
  cp aus/zeilen-M2-st2-b/*.json aus/zeilen-M2-st2/
  cp aus/zeilen-M2-st1-b/*.json aus/zeilen-M2-st1/
  echo kopiert $(date --iso-8601=seconds) > logs/kette-m2b-kopie.txt
else
  echo unvollstaendig $(date --iso-8601=seconds) > logs/kette-m2b-kopie.txt
fi
