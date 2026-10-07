#!/bin/bash
# QBALL-DREIPOL-1, Hauptlaeufe Spur p4000b (eingefrorener Code; PLAN.md Abschnitt 7). Laeuft auf der .69.
set -u
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
P=/home/fmh/fmhc-physics-remote/runde42-qball-dreipol/code
cd /home/fmh/fmhc-physics-remote/runde42-qball-dreipol/lauf || exit 1
bash $K p4000b dreipol-a $P/dreipol.py a --out a.json --Q=30,60,90,120,180 --g4=-0.1,0,0.1 --extern --wand 60 > a.log 2>&1
echo "a rc=$? $(date --iso-8601=seconds)" >> laeufe-p4000b.log
bash $K p4000b dreipol-c-p01 $P/dreipol.py c --out c_p01.json --Q1 60 --g4=0.1 --nfluss 12000 --laeufe c1,c2 \
  > c_p01.log 2>&1
echo "c_p01 rc=$? $(date --iso-8601=seconds)" >> laeufe-p4000b.log
for t in 0:0 m01:-0.1; do
  tag=${t%%:*}
  g=${t##*:}
  bash $K p4000b dreipol-c-$tag $P/dreipol.py c --out c_$tag.json --Q1 60 --g4=$g --nfluss 12000 --laeufe c1 \
    > c_$tag.log 2>&1
  echo "c_$tag rc=$? $(date --iso-8601=seconds)" >> laeufe-p4000b.log
done
