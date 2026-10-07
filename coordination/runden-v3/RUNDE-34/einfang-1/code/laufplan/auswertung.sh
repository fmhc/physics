#!/bin/bash
# EINFANG-1 Auswertung und Bild (Runde 34), Spur cpu. Nur kleintest.sh-Aufrufe.
set -u
B=/home/fmh/fmhc-physics-remote/runde34-einfang
L=$B/lauf
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
P=$B/einfang.py
cd $L
bash $K cpu r34ef-auswertung $P auswertung --ordner $L --kraft5 $B/kegelq/kraft-n5-h0.3-Q200.json --kraft7 $B/kegelq/kraft-n7-h0.3-Q200.json > $L/log-auswertung.txt 2>&1
bash $K cpu r34ef-bild $P bild --ordner $L --namen f5-v0.1,f5-v0.05,f5-v0.02,s7-v0.05,e6-v0.05 --aus $L/bahnen.png > $L/log-bild.txt 2>&1
