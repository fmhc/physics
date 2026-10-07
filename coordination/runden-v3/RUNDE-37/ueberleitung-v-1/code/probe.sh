#!/bin/bash
# Codeprobe r2 (Rauchtest, Werte nicht ansehen): Kette mit --probe und Auswertung. Aufruf im Ordner ueberleitung-v-1.
set -u
D=/home/fmh/fmhc-physics-remote/ueberleitung-v-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
P=$D/rauch/probe
mkdir -p $P
bash $K cpu2 uvp-kw code/uv.py kw --probe --out $P/kw.json > $P/kw.log 2>&1
bash $K cpu2 uvp-vr code/uv.py vraster --probe --out $P/vraster.json > $P/vraster.log 2>&1
bash $K cpu2 uvp-vb0 code/uv.py vbz --teil 0 --probe --out $P/vbz0.json > $P/vbz0.log 2>&1
bash $K cpu2 uvp-vb1 code/uv.py vbz --teil 1 --probe --out $P/vbz1.json > $P/vbz1.log 2>&1
bash $K cpu2 uvp-ho code/uv.py hoeher --out $P/hoeher.json > $P/hoeher.log 2>&1
bash $K cpu2 uvp-aw code/uv.py auswertung --ein kw=$P/kw.json vraster=$P/vraster.json vbz0=$P/vbz0.json vbz1=$P/vbz1.json --out $P/auswertung.json > $P/auswertung.log 2>&1
echo "probe fertig $(date -u +%H:%M:%S)" > $P/fertig.txt
