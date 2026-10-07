#!/bin/bash
# TAKT-UMKLAPP-1: Auswertung und Bild (eingefrorenes code/tu.py) nach dem Ende aller drei Laufketten, Spur cpu9; dann Pruefsummen.
set -u
cd /home/fmh/fmhc-physics-remote/takt-umklapp-1 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
until grep -q "kette cpu8 ende" kette-cpu8.out && grep -q "kette cpu9 ende" kette-cpu9.out && grep -q "kette cpu10 ende" kette-cpu10.out; do sleep 5; done
bash "$K" cpu9 tu-aw code/tu.py auswertung --ordner lauf --out lauf/auswertung.json > lauf/tu-aw.log 2>&1; echo "tu-aw rc=$? $(date -u +%H:%M:%S)"
bash "$K" cpu9 tu-bild code/tu.py bild --aw lauf/auswertung.json --ordner lauf --out lauf/bild-takt-umklapp.png > lauf/tu-bild.log 2>&1; echo "tu-bild rc=$? $(date -u +%H:%M:%S)"
cp kette-cpu8.out kette-cpu9.out kette-cpu10.out lauf/
(cd lauf && sha256sum $(ls | grep -v PRUEFSUMMEN.txt) > PRUEFSUMMEN.txt)
(cd nachtrag && sha256sum $(ls | grep -v -E "PRUEFSUMMEN.txt|abschluss") > PRUEFSUMMEN.txt)
echo "abschluss ende $(date -u +%H:%M:%S)"
