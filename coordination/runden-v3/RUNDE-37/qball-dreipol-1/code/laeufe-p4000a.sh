#!/bin/bash
# QBALL-DREIPOL-1, Hauptlaeufe Spur p4000a (eingefrorener Code; PLAN.md Abschnitt 7). Laeuft auf der .69.
set -u
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
P=/home/fmh/fmhc-physics-remote/runde42-qball-dreipol/code
cd /home/fmh/fmhc-physics-remote/runde42-qball-dreipol/lauf || exit 1
for t in m01:-0.1 0:0 p01:0.1; do
  tag=${t%%:*}
  g=${t##*:}
  bash $K p4000a dreipol-b-$tag $P/dreipol.py b --out b_$tag.json --Q1 60 --g4=$g --wand_relax 60 > b_$tag.log 2>&1
  echo "b_$tag rc=$? $(date --iso-8601=seconds)" >> laeufe-p4000a.log
done
bash $K p4000a dreipol-c1s2-p01 $P/dreipol.py c --out c1s2_p01.json --Q1 60 --g4=0.1 --nfluss 0 --laeufe c1 --saat 2 \
  > c1s2_p01.log 2>&1
echo "c1s2_p01 rc=$? $(date --iso-8601=seconds)" >> laeufe-p4000a.log
bash $K p4000a dreipol-c1dt-p01 $P/dreipol.py c --out c1dt_p01.json --Q1 60 --g4=0.1 --nfluss 0 --laeufe c1 --saat 1 \
  --dt 0.0125 --wand_t 420 > c1dt_p01.log 2>&1
echo "c1dt_p01 rc=$? $(date --iso-8601=seconds)" >> laeufe-p4000a.log
