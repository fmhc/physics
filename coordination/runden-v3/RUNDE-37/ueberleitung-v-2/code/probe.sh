#!/bin/bash
# Codeprobe r2 (Rauchtest, PLAN 8; Werte nicht ansehen): ganze Kette mit --probe und Auswertung. Aufruf im Ordner ueberleitung-v-2.
set -u
D=/home/fmh/fmhc-physics-remote/ueberleitung-v-2
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
P=$D/rauch/probe
mkdir -p $P
cd $D
bash $K cpu2 uwp-v0 code/uw.py punkte --netz V --menge raster --probe --out $P/v0.json > $P/v0.log 2>&1
bash $K cpu2 uwp-s code/uw.py punkte --netz S --menge rasterbz --probe --out $P/s.json > $P/s.log 2>&1
bash $K cpu2 uwp-b1 code/uw.py punkte --netz B1 --menge rasterbz --probe --out $P/b1.json > $P/b1.log 2>&1
bash $K cpu2 uwp-n0 code/uw.py punkte --netz V --menge neu --teil 0 --probe --out $P/vneu0.json > $P/vneu0.log 2>&1
bash $K cpu2 uwp-n1 code/uw.py punkte --netz V --menge neu --teil 1 --probe --out $P/vneu1.json > $P/vneu1.log 2>&1
bash $K cpu2 uwp-n2 code/uw.py punkte --netz V --menge neu --teil 2 --probe --out $P/vneu2.json > $P/vneu2.log 2>&1
bash $K cpu2 uwp-hs code/uw.py hstern --richtung 100 --probe --out $P/hs100.json > $P/hs100.log 2>&1
bash $K cpu2 uwp-aw code/uw.py auswertung --ein v0=$P/v0.json s=$P/s.json b1=$P/b1.json vneu0=$P/vneu0.json vneu1=$P/vneu1.json vneu2=$P/vneu2.json hs100=$P/hs100.json --out $P/auswertung.json > $P/auswertung.log 2>&1
echo "probe fertig $(date -u +%H:%M:%S)" > $P/fertig.txt
