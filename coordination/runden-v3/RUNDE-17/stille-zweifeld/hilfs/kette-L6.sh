#!/bin/bash
# L6: Kandidaten je Stufe: E1, E2, E3. Aufruf: kette-L6.sh <stufe> <spur>
set -u
export LC_ALL=C
ST=$1; SP=$2
cd /home/fmh/fmhc-physics-remote/runde17-stille-zweifeld
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
for T in E1 E2 E3; do
  bash $K $SP r17-kand-$T-st$ST code/stille3.py kand $ST laeufe/prof-st$ST laeufe/zeilen-st$ST laeufe/schwelle.json laeufe/kand/kand-$T-st$ST.json $T > logs/L6-kand-$T-st$ST.log 2>&1
done
echo KETTE_FERTIG
