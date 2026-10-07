#!/bin/bash
# ZUS-10 Pruefung, Kette C (Spur cpu6, teilt sich den Lock mit Kette A2): Idee 9, gfbic_delta.py spektrum an P1 mit
# g = 0,2 und Massenverstimmung delta = 0 (Kontrolle), 0,05, 0,10, 0,08.
# Aufruf auf der .69: cd /home/fmh/fmhc-physics-remote/runde9-zus10 && nohup bash kette-zus10-c.sh > KETTE-C.log 2>&1 < /dev/null &
cd /home/fmh/fmhc-physics-remote/runde9-zus10 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
S=cpu6
echo "Kette C Start $(date --iso-8601=seconds)"
for D in 0 0.05 0.10 0.08; do
  N=$(echo "$D" | tr -d '.')
  bash $K $S z9d$N gfbic_delta.py spektrum --stellen P1 --g 0.2 --delta-m2 $D --out aus-sp-P1-d$N > LAUF-z9d$N.log 2>&1
done
echo "Kette C fertig $(date --iso-8601=seconds)"
