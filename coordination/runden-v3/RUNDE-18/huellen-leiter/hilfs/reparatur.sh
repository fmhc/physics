#!/bin/bash
# PLAN-NACHTRAG-1: Bloecke, die mit der alten Fassung liefen, mit der neuen Fassung nachrechnen (nur betroffene Zeilen
# und Paare werden neu gerechnet). Wartet, bis der alte Block beendet ist. Aufruf: bash hilfs/reparatur.sh <spur> <stufe:i0-i1> ...
cd /home/fmh/fmhc-physics-remote/runde18-huellen-leiter || exit 1
SPUR=$1; shift
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
for B in "$@"; do
  ST=${B%%:*}; R=${B#*:}; I0=${R%-*}; I1=${R#*-}
  until grep -q "^ende " logs/block-st$ST-$I0-$I1.log 2>/dev/null; do sleep 10; done
  bash $K $SPUR r18hl-r$ST-$I0 code/huellen_leiter.py block M2 $ST aus/prof-st$ST aus/laeufe aus/zeilen.json $I0 $I1 > logs/rep-st$ST-$I0-$I1.log 2>&1
done
echo "reparatur $SPUR fertig $(date --iso-8601=seconds)" >> logs/ketten.log
