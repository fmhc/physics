#!/bin/bash
# Hauptlaeufe Spur cpu2 (PLAN 8): v0, s, b1, vneu Teil 2, hstern 321; danach Auswertung, sobald alle Dateien da sind.
set -u
D=/home/fmh/fmhc-physics-remote/ueberleitung-v-2
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
L=$D/lauf
cd $D
bash $K cpu2 uw-v0 code/uw.py punkte --netz V --menge raster --out $L/v0.json > $L/v0.log 2>&1
bash $K cpu2 uw-s code/uw.py punkte --netz S --menge rasterbz --out $L/s.json > $L/s.log 2>&1
bash $K cpu2 uw-b1 code/uw.py punkte --netz B1 --menge rasterbz --out $L/b1.json > $L/b1.log 2>&1
bash $K cpu2 uw-n2 code/uw.py punkte --netz V --menge neu --teil 2 --out $L/vneu2.json > $L/vneu2.log 2>&1
bash $K cpu2 uw-hs321 code/uw.py hstern --richtung 321 --out $L/hs321.json > $L/hs321.log 2>&1
until [ -f $L/vneu0.json ] && [ -f $L/vneu1.json ] && [ -f $L/hs100.json ] && [ -f $L/hs111.json ]; do sleep 5; done
bash $K cpu2 uw-aw code/uw.py auswertung --ein v0=$L/v0.json s=$L/s.json b1=$L/b1.json vneu0=$L/vneu0.json vneu1=$L/vneu1.json vneu2=$L/vneu2.json hs100=$L/hs100.json hs111=$L/hs111.json hs321=$L/hs321.json --out $L/auswertung.json > $L/auswertung.log 2>&1
cd $L && sha256sum *.json *.log > PRUEFSUMMEN.txt
echo "kette cpu2 fertig $(date -u +%H:%M:%S)" > $L/kette-cpu2.txt
