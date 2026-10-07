#!/bin/bash
# LUND-REGGE-MASSE-1, Laufkette Spur cpu5 (einmal von Hand gestartet). Jeder Schritt ueber kleintest.sh (<= 600 s).
W=/home/fmh/fmhc-physics-remote/lund-regge-masse-1
KT=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd "$W" || exit 1
lauf() { n=$1; shift; bash "$KT" cpu5 "$n" code/lrm.py "$@" > "$W/lauf/$n.log" 2>&1; echo "$n rc=$? $(date --iso-8601=seconds)" >> "$W/lauf/kette-cpu5.txt"; }
echo "start $(date --iso-8601=seconds)" >> "$W/lauf/kette-cpu5.txt"
lauf lr0 lr0 --out lauf/lr0.json
lauf spV spanne --netz V --out lauf/sp-V.json
lauf spS spanne --netz S --out lauf/sp-S.json
lauf spA15 spanne --netz A15 --out lauf/sp-A15.json
lauf stV stabil --netz V --out lauf/st-V.json
lauf stS stabil --netz S --out lauf/st-S.json
lauf stA15 stabil --netz A15 --out lauf/st-A15.json
lauf gang gang --out lauf/gang.json
lauf spG1a spanne --netz glas-s1 --teil 0 --out lauf/sp-glas-s1-a.json
lauf spG1b spanne --netz glas-s1 --teil 1 --out lauf/sp-glas-s1-b.json
lauf stG1 stabil --netz glas-s1 --out lauf/st-glas-s1.json
lauf spG3a spanne --netz glas-s3 --teil 0 --out lauf/sp-glas-s3-a.json
lauf spG3b spanne --netz glas-s3 --teil 1 --out lauf/sp-glas-s3-b.json
lauf stG3 stabil --netz glas-s3 --out lauf/st-glas-s3.json
echo "ende $(date --iso-8601=seconds)" >> "$W/lauf/kette-cpu5.txt"
