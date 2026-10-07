#!/bin/bash
# QUANT-2: Gewichte pruefen/speichern (gwp.py), dann gewichtete Uebersicht heiss/kalt (Spur cpu7).
set -u
D=/home/fmh/fmhc-physics-remote/quant-2
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
L=$D/lauf
cd $D
df -h /home | tail -1
bash $K cpu7 q2-gwp code/gwp.py 0.348006576329167 0.014137937569648498,0.011037083825312329,0.01573722641571458,-0.012050982153698101,-0.014302907290987436,-0.03281588970182715,-0.035256558986060685,-0.0306034867035689,-0.0264557613759714 $L/gwp > $L/gwp.log 2>&1
bash kette-w1.sh
bash kette-w2.sh
