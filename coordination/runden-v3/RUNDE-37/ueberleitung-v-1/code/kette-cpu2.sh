#!/bin/bash
# Hauptlaeufe Spur cpu2 (PLAN 14): kw, vraster, hoeher; danach Auswertung, sobald vbz0 und vbz1 fertig sind.
set -u
D=/home/fmh/fmhc-physics-remote/ueberleitung-v-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
L=$D/lauf
bash $K cpu2 uv-kw code/uv.py kw --out $L/kw.json > $L/kw.log 2>&1
bash $K cpu2 uv-vr code/uv.py vraster --out $L/vraster.json > $L/vraster.log 2>&1
bash $K cpu2 uv-ho code/uv.py hoeher --out $L/hoeher.json > $L/hoeher.log 2>&1
until [ -f $L/vbz0.json ] && [ -f $L/vbz1.json ]; do sleep 5; done
bash $K cpu2 uv-aw code/uv.py auswertung --ein kw=$L/kw.json vraster=$L/vraster.json vbz0=$L/vbz0.json vbz1=$L/vbz1.json --out $L/auswertung.json > $L/auswertung.log 2>&1
echo "kette cpu2 fertig $(date -u +%H:%M:%S)" > $L/kette-cpu2.txt
