#!/bin/bash
# QBALL-DOPPELSPALT-1: Auswertung mit eingefrorenem code/auswertung.py (PLAN Abschn. 5 und 6). Aufruf: bash auswerten.sh <spur> <tag>
set -u
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
D=/home/fmh/fmhc-physics-remote/qball-doppelspalt-1
cd $D || exit 1
bash $K ${1:-p4000a} qds-aw-${2:-x} $D/code/auswertung.py --dir $D --out $D/lauf/auswertung.json --bild $D/lauf/qds-bild.png > $D/lauf/auswertung-${2:-x}.log 2>&1
echo "auswertung-${2:-x} rc=$? $(date --iso-8601=seconds)" >> $D/lauf/auswertung.log
