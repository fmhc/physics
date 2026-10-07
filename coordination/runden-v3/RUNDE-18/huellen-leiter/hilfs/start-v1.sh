#!/bin/bash
# V1: Profile beider Stufen und K1 beider Stufen, parallel auf vier Spuren (auf der .69 auszufuehren)
cd /home/fmh/fmhc-physics-remote/runde18-huellen-leiter || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
bash $K cpu  r18hl-prof1 code/huellen_leiter.py profile M2 1 aus/prof-st1 aus/zeilen.json > logs/prof-st1.log 2>&1 &
bash $K cpu2 r18hl-prof2 code/huellen_leiter.py profile M2 2 aus/prof-st2 aus/zeilen.json > logs/prof-st2.log 2>&1 &
bash $K cpu3 r18hl-k1a   code/huellen_leiter.py k1 1 - aus/k1-st1.json > logs/k1-st1.log 2>&1 &
bash $K cpu4 r18hl-k1b   code/huellen_leiter.py k1 2 - aus/k1-st2.json > logs/k1-st2.log 2>&1 &
wait
