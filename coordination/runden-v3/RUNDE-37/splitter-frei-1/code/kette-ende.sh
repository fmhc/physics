#!/bin/bash
# SPLITTER-FREI-1, Abschluss nach beiden Ketten (Spur cpu5): mechanische Auswertung (sf.py aw -> sf_aw.py).
set -u
W=/home/fmh/fmhc-physics-remote/splitter-frei-1
KT=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd "$W" || exit 1
timeout 5400 bash -c "until grep -q '^ende' $W/lauf/kette-cpu5.txt 2>/dev/null && grep -q '^ende' $W/lauf/kette-cpu6.txt 2>/dev/null; do sleep 10; done"
bash "$KT" cpu5 sf-aw code/sf.py aw --lauf lauf --out lauf/auswertung.json > "$W/lauf/aw.log" 2>&1
echo "aw rc=$? $(date --iso-8601=seconds)" >> "$W/lauf/kette-ende.txt"
