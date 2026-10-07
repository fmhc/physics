#!/bin/bash
# LICHT-1 NACHTRAG (nicht im eingefrorenen Plan; nach dem Fehlschlag von s = 48 in radial-haupt beschlossen; nur beschreibend):
# dieselbe Familie mit kleinerem Schritt (q = 0,99 statt 0,96), damit loese_Q auch bei Q' = 9600 eine Klammer findet.
set -u
B=/home/fmh/fmhc-physics-remote/runde34-licht
L=$B/lauf
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
P=$B/code/licht_nachtrag.py
cd $L
bash $K cpu r34li-radial-q099 $P radial --Q 200 --s 1.2,1.5,2,3,6,12,24,48 --s-dEdQ 48 --dr 0.01 --rmax 90 --eps-min 0.0065 --q 0.99 --aus $L/radial-q099.json > $L/log-radial-q099.txt 2>&1
bash $K cpu r34li-radial-q099-rmax $P radial --Q 200 --s 24,48 --dr 0.01 --rmax 120 --eps-min 0.0065 --q 0.99 --aus $L/radial-q099-rmax.json > $L/log-radial-q099-rmax.txt 2>&1
echo "nachtrag fertig $(date --iso-8601=seconds)" > $L/fertig-nachtrag-cpu.txt
