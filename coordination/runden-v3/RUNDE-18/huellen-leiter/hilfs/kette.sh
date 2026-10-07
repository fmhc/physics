#!/bin/bash
# Kette (auf der .69): Bloecke nacheinander auf einer Spur. Anspruch je Block per mkdir (atomar), keine Doppelarbeit.
# Aufruf: bash hilfs/kette.sh <spur> <stufe:i0-i1> ...   (Sonderform "P2" = Profile Stufe 2 fortsetzen)
cd /home/fmh/fmhc-physics-remote/runde18-huellen-leiter || exit 1
SPUR=$1; shift
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
for B in "$@"; do
  if [ "$B" = "P2" ]; then
    bash $K $SPUR r18hl-prof2w code/huellen_leiter.py profile M2 2 aus/prof-st2 aus/zeilen.json weiter > logs/prof-st2-weiter.log 2>&1
    continue
  fi
  ST=${B%%:*}; R=${B#*:}; I0=${R%-*}; I1=${R#*-}
  mkdir aus/anspruch-st$ST-$I0-$I1 2>/dev/null || continue
  n=0
  while [ "$(ls aus/prof-st$ST/ 2>/dev/null | grep -c npz)" -le "$I1" ] && [ $n -lt 80 ]; do sleep 15; n=$((n+1)); done
  bash $K $SPUR r18hl-b$ST-$I0 code/huellen_leiter.py block M2 $ST aus/prof-st$ST aus/laeufe aus/zeilen.json $I0 $I1 > logs/block-st$ST-$I0-$I1.log 2>&1
done
echo "kette $SPUR fertig $(date --iso-8601=seconds)" >> logs/ketten.log
