#!/bin/bash
# REGIME-K-3 h-Gang, BZ-Laeufe mit hgang2.py (keine Newton-Nachschaerfung bei abs(k) > 0,25). Aufruf: bash code/kette-hgang2.sh <spur>
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
G=/home/fmh/fmhc-physics-remote/regime-k-3/hgang
SPUR=${1:?Spur}
cd /home/fmh/fmhc-physics-remote/regime-k-3 || exit 2
lauf() { n=$1; shift; bash $K $SPUR "rk3-hg2-$n" code/hgang2.py lauf "$@" --out $G/$n.json > $G/$n.log 2>&1; echo "$n rc=$? $(date --iso-8601=seconds)" >> $G/kette2-$SPUR.txt; }
echo "start $(date --iso-8601=seconds)" > $G/kette2-$SPUR.txt
case "$SPUR" in
  cpu8)
    lauf B1-bz2 --arm B1-t1 --satz bz --h 1,0.5,0.25,0.125,0.0625,0.015625,0.00390625,0.0009765625
    lauf V-bz2-b --arm V-A --satz bz --h 0.0625,0.015625,0.00390625,0.0009765625 ;;
  cpu10)
    lauf V-bz2-a --arm V-A --satz bz --h 1,0.5,0.25,0.125 ;;
esac
echo "ende $(date --iso-8601=seconds)" >> $G/kette2-$SPUR.txt
