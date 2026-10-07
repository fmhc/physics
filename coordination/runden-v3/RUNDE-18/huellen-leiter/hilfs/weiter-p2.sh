#!/bin/bash
# Wartet auf das Ende der ersten Fortsetzung Stufe 2; bei erneutem Abbruch eine zweite Fortsetzung (auf der .69).
cd /home/fmh/fmhc-physics-remote/runde18-huellen-leiter || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
until grep -q "^ende " logs/prof-st2-weiter.log 2>/dev/null; do sleep 5; done
if [ "$(ls aus/prof-st2/ | grep -c npz)" -lt 263 ]; then
  bash $K cpu2 r18hl-prof2w2 code/huellen_leiter.py profile M2 2 aus/prof-st2 aus/zeilen.json weiter > logs/prof-st2-weiter2.log 2>&1
fi
