#!/bin/bash
# REGIME-K-3 Hauptlaeufe (PLAN 9, Hauptlaeufe). Aufruf auf der .69: bash code/kette.sh <spur>
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
L=/home/fmh/fmhc-physics-remote/regime-k-3/lauf
SPUR=${1:?Spur}
cd /home/fmh/fmhc-physics-remote/regime-k-3 || exit 2
lauf() { n=$1; shift; bash $K $SPUR "rk3-$n" code/rk3.py transfer "$@" --out $L/$n.json > $L/$n.log 2>&1; echo "$n rc=$? $(date --iso-8601=seconds)" >> $L/kette-$SPUR.txt; }
echo "start $(date --iso-8601=seconds)" > $L/kette-$SPUR.txt
case "$SPUR" in
  cpu8)
    lauf KW-raster --arm KW --satz raster
    lauf KW-bz --arm KW --satz bz
    lauf B1-t1-raster --arm B1-t1 --satz raster
    lauf B1-t1-bz --arm B1-t1 --satz bz
    lauf V-A-bz-3 --arm V-A --satz bz --teil 3/4
    lauf V-A-raster-3 --arm V-A --satz raster --teil 3/4 ;;
  cpu9)
    lauf V-A-raster-0 --arm V-A --satz raster --teil 0/4
    lauf V-A-raster-1 --arm V-A --satz raster --teil 1/4
    lauf V-A-raster-2 --arm V-A --satz raster --teil 2/4 ;;
  cpu10)
    lauf V-A-bz-0 --arm V-A --satz bz --teil 0/4
    lauf V-A-bz-1 --arm V-A --satz bz --teil 1/4
    lauf V-A-bz-2 --arm V-A --satz bz --teil 2/4 ;;
esac
echo "ende $(date --iso-8601=seconds)" >> $L/kette-$SPUR.txt
