#!/bin/bash
# L1: Profile (M2 Zeilen + K2-Werte) und K1-Profile, Stufe $1, Spur $2
set -u
export LC_ALL=C
ST=$1; SP=$2
cd /home/fmh/fmhc-physics-remote/runde17-stille-zweifeld
W2=$(seq -f '%.2f' 0.75 0.02 1.95 | tr '\n' ' ')
K2="0.76 0.90 1.10 1.30 1.50 1.70 1.84 1.94"
bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh $SP r17-prof-st$ST code/stille3.py profile M2 $ST laeufe/prof-st$ST $W2 $K2 > logs/L1-prof-st$ST.log 2>&1
# K1-Profile bereits in Lauf 1 erzeugt
echo KETTE_FERTIG
