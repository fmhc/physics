#!/bin/bash
# L7: Homotopie S4 je Stufe. Aufruf: kette-L7.sh <stufe> <spur>
set -u
export LC_ALL=C
ST=$1; SP=$2
cd /home/fmh/fmhc-physics-remote/runde17-stille-zweifeld
bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh $SP r17-homot-st$ST code/stille3.py homotopie $ST laeufe/k1-K1E2-st$ST.json laeufe/homotopie-st$ST.json laeufe/schwelle.json > logs/L7-homotopie-st$ST.log 2>&1
echo KETTE_FERTIG
