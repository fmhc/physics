#!/bin/bash
# Wartet auf das Ende des Profil-Laufs Stufe 1 und setzt ihn bei Abbruch fort (gleiches Verfahren, auf der .69).
cd /home/fmh/fmhc-physics-remote/runde18-huellen-leiter || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
until grep -q "^ende " logs/prof-st1.log; do sleep 5; done
if [ "$(ls aus/prof-st1/ | grep -c npz)" -lt 263 ]; then
  bash $K cpu r18hl-prof1w code/huellen_leiter.py profile M2 1 aus/prof-st1 aus/zeilen.json weiter > logs/prof-st1-weiter.log 2>&1
fi
