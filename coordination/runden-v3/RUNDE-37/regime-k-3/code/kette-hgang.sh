#!/bin/bash
# REGIME-K-3 Folgeauftrag h-Gang (Leitung 05.10.). Aufruf auf der .69: bash code/kette-hgang.sh <spur>
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
G=/home/fmh/fmhc-physics-remote/regime-k-3/hgang
SPUR=${1:?Spur}
cd /home/fmh/fmhc-physics-remote/regime-k-3 || exit 2
H1=1,0.5,0.25
H2=0.125,0.0625,0.015625
H3=0.00390625,0.0009765625
HA=1,0.5,0.25,0.125,0.0625,0.015625,0.00390625,0.0009765625
lauf() { n=$1; shift; bash $K $SPUR "rk3-hg-$n" code/hgang.py lauf "$@" --out $G/$n.json > $G/$n.log 2>&1; echo "$n rc=$? $(date --iso-8601=seconds)" >> $G/kette-$SPUR.txt; }
echo "start $(date --iso-8601=seconds)" > $G/kette-$SPUR.txt
case "$SPUR" in
  cpu8)
    lauf KW-raster --arm KW --satz raster --h $HA
    lauf KW-bz --arm KW --satz bz --h $HA
    lauf B1-raster-a --arm B1-t1 --satz raster --h 1,0.5,0.25,0.125
    lauf B1-raster-b --arm B1-t1 --satz raster --h 0.0625,0.015625,0.00390625,0.0009765625
    lauf B1-bz --arm B1-t1 --satz bz --h $HA ;;
  cpu9)
    lauf V-raster-1 --arm V-A --satz raster --h $H1
    lauf V-raster-2 --arm V-A --satz raster --h $H2
    lauf V-raster-3 --arm V-A --satz raster --h $H3 ;;
  cpu10)
    lauf V-bz-1 --arm V-A --satz bz --h $H1
    lauf V-bz-2 --arm V-A --satz bz --h $H2
    lauf V-bz-3 --arm V-A --satz bz --h $H3 ;;
esac
echo "ende $(date --iso-8601=seconds)" >> $G/kette-$SPUR.txt
