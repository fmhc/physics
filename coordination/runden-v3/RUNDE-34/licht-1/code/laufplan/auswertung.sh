#!/bin/bash
# LICHT-1 Auswertung und Bild (Runde 34), Spur cpu. Nur kleintest.sh-Aufrufe.
set -u
B=/home/fmh/fmhc-physics-remote/runde34-licht
L=$B/lauf
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
P=$B/code/licht.py
cd $L
bash $K cpu r34li-auswertung $P auswertung --ordner $L --radial $L/radial-haupt.json --radial-dr $L/radial-dr.json --radial-rmax $L/radial-rmax.json --statik $L/statik-n3-h0.3.json --haupt t3-v0.01 --konvergenz t3-v0.01-dt0.05,t3-v0.01-h0.2 --ruhe t3-ruhe > $L/log-auswertung.txt 2>&1
bash $K cpu r34li-bild $P bild --ordner $L --name t3-v0.01 --aus $L/v-t.png > $L/log-bild.txt 2>&1
