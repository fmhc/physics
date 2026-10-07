#!/bin/bash
# LUND-REGGE-MASSE-1, Laufkette Spur cpu6 (einmal von Hand gestartet). Jeder Schritt ueber kleintest.sh (<= 600 s).
W=/home/fmh/fmhc-physics-remote/lund-regge-masse-1
KT=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd "$W" || exit 1
lauf() { n=$1; shift; bash "$KT" cpu6 "$n" code/lrm.py "$@" > "$W/lauf/$n.log" 2>&1; echo "$n rc=$? $(date --iso-8601=seconds)" >> "$W/lauf/kette-cpu6.txt"; }
echo "start $(date --iso-8601=seconds)" >> "$W/lauf/kette-cpu6.txt"
lauf spG2a spanne --netz glas-s2 --teil 0 --out lauf/sp-glas-s2-a.json
lauf spG2b spanne --netz glas-s2 --teil 1 --out lauf/sp-glas-s2-b.json
lauf stG2 stabil --netz glas-s2 --out lauf/st-glas-s2.json
lauf spG4a spanne --netz glas-s4 --teil 0 --out lauf/sp-glas-s4-a.json
lauf spG4b spanne --netz glas-s4 --teil 1 --out lauf/sp-glas-s4-b.json
lauf stG4 stabil --netz glas-s4 --out lauf/st-glas-s4.json
echo "ende $(date --iso-8601=seconds)" >> "$W/lauf/kette-cpu6.txt"
