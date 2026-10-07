#!/bin/bash
# Kette fuer eine Spur: kette.sh <spur> <stelle> ; grob alle 8 Zeilen, dann fein in Paaren (PLAN-NACHTRAG-1 Punkt 2)
export LC_ALL=C
SP="$1"
ST="$2"
cd /home/fmh/fmhc-physics-remote/runde18-huellen-uhr || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
bash "$K" "$SP" "r18-lauf-$ST-st1" code/huelle.py lauf "aus/prep-$ST-st1.npz" 0,1,2,3,4,5,6,7 50 "aus/lauf-$ST-st1-alle.npz"
for Z in 0,1 2,3 4,5 6,7; do
  ZN=$(echo "$Z" | tr ',' '-')
  bash "$K" "$SP" "r18-lauf-$ST-st2-$ZN" code/huelle.py lauf "aus/prep-$ST-st2.npz" "$Z" 50 "aus/lauf-$ST-st2-z$ZN.npz"
done
echo "KETTE FERTIG $SP $ST"
