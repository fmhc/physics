#!/bin/bash
# L5: Hauptzeilen. Aufruf: kette-L5.sh <stufe> <spur> <j0> <j1>  (Zeilen j0..j1 inklusive)
set -u
export LC_ALL=C
ST=$1; SP=$2; J0=$3; J1=$4
cd /home/fmh/fmhc-physics-remote/runde17-stille-zweifeld
W2=$(seq -f '%.2f' 0.75 0.02 1.95 | sed -n "$((J0+1)),$((J1+1))p" | tr '\n' ' ')
bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh $SP r17-zeilen-st$ST-$J0 code/stille3.py zeilen $ST laeufe/prof-st$ST laeufe/zeilen-st$ST $W2 > logs/L5-zeilen-st$ST-$J0-$J1.log 2>&1
echo KETTE_FERTIG
