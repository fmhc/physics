#!/bin/bash
# LICHT-1 Rauchlaeufe (vor dem Einfrieren; andere Parameter als jeder echte Lauf: Q = 150, h = 0,5, R = 30).
# Eine CPU-Spur, nacheinander. Nur kleintest.sh-Aufrufe.
set -u
SPUR=${1:-cpu}
B=/home/fmh/fmhc-physics-remote/runde34-licht
L=$B/rauch
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
P=$B/code/licht.py
cd $L
bash $K $SPUR r34li-rauch-radial $P radial --Q 150 --s 1.2,2,12 --s-dEdQ 2 --dr 0.02 --rmax 60 --eps-min 0.012 --aus $L/radial-rauch.json > $L/log-rauch-radial.txt 2>&1
bash $K $SPUR r34li-rauch-statik $P statik --n 3 --h 0.5 --R 30 --Q 150 --d 0,3,6,9,15 --aus $L/statik-rauch.json > $L/log-rauch-statik.txt 2>&1
bash $K $SPUR r34li-rauch-lauf $P lauf --name rauch-t3 --n 3 --h 0.5 --R 30 --rs 22 --Q 150 --v 0.05 --d0 12 --dt 0.1 --T 600 --T-nach 30 --geraet cpu --aus $L/li-rauch-t3.json > $L/log-rauch-lauf.txt 2>&1
bash $K $SPUR r34li-rauch-ruhe $P lauf --name rauch-ruhe --n 3 --h 0.5 --R 30 --rs 22 --Q 150 --v 0 --d0 0 --dt 0.1 --T 40 --kreuz-stopp 0 --geraet cpu --aus $L/li-rauch-ruhe.json > $L/log-rauch-ruhe.txt 2>&1
bash $K $SPUR r34li-rauch-ausw $P auswertung --ordner $L --radial $L/radial-rauch.json --statik $L/statik-rauch.json --haupt rauch-t3 > $L/log-rauch-ausw.txt 2>&1
bash $K $SPUR r34li-rauch-bild $P bild --ordner $L --name rauch-t3 --aus $L/rauch-t3.png > $L/log-rauch-bild.txt 2>&1
echo "rauch fertig $(date --iso-8601=seconds)" > $L/fertig-rauch.txt
