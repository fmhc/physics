#!/bin/bash
# L6 (Reihenfolge absteigend in omega^2, da Duennwand-Kandidaten langsam): kette-L6b.sh <stufe> <spur> <tag> <teil> [<tag> <teil> ...]
set -u
export LC_ALL=C
ST=$1; SP=$2; shift 2
cd /home/fmh/fmhc-physics-remote/runde17-stille-zweifeld
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
while [ $# -ge 2 ]; do
  TAG=$1; TEIL=$2; shift 2
  bash $K $SP r17-kand-$TAG-st$ST code/stille3.py kand $ST laeufe/prof-st$ST laeufe/zeilen-st$ST laeufe/schwelle.json laeufe/kand/kand-$TAG-st$ST.json $TEIL > logs/L6-kand-$TAG-st$ST.log 2>&1
done
echo KETTE_FERTIG
