#!/bin/bash
# V3 (auf der .69): Stellen/Abgleich/L-Wertung, dann Rechteck-Umlauf der Stichprobe, dann Endauswertung und Bilder.
cd /home/fmh/fmhc-physics-remote/runde18-huellen-leiter || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SPUR=${1:-cpu}; SPUR2=${2:-cpu3}
bash $K $SPUR r18hl-ausw code/auswertung.py stellen aus/laeufe aus/laeufe/auswertung.json > logs/ausw-stellen.log 2>&1
cp aus/umlauf-L1-st1.json aus/laeufe/umlauf-L1-st1.json; cp aus/umlauf-L1-st2.json aus/laeufe/umlauf-L1-st2.json
bash $K $SPUR r18hl-uP1 code/huellen_leiter.py umlauf M2 1 aus/prof-st1 aus/zeilen.json aus/laeufe/umlauf-punkte-P-st1.json aus/laeufe/umlauf-P-st1.json 0 20 > logs/umlauf-P-st1.log 2>&1 &
bash $K $SPUR2 r18hl-uP2 code/huellen_leiter.py umlauf M2 2 aus/prof-st2 aus/zeilen.json aus/laeufe/umlauf-punkte-P-st2.json aus/laeufe/umlauf-P-st2.json 0 20 > logs/umlauf-P-st2.log 2>&1 &
wait
bash $K $SPUR r18hl-final code/auswertung.py final aus/laeufe aus/laeufe/auswertung-final.json > logs/ausw-final.log 2>&1
bash $K $SPUR r18hl-bild code/auswertung.py bild aus/laeufe aus/abb-stellen.png aus/abb-abstand.png > logs/ausw-bild.log 2>&1
echo "v3 fertig $(date --iso-8601=seconds)" >> logs/ketten.log
