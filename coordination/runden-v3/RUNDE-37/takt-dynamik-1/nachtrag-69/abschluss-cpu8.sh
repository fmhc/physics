#!/bin/bash
# TAKT-DYNAMIK-1: Auswertung und Bild mit dem eingefrorenen code/td.py, Tabellen mit nachtrag/code/tabellen.py, dann Pruefsummen.
set -u
cd /home/fmh/fmhc-physics-remote/takt-dynamik-1 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
bash $K cpu8 td-aw code/td.py auswertung --ordner lauf --out lauf/auswertung.json > lauf/td-aw.log 2>&1; echo "td-aw rc=$? $(date -u +%H:%M:%S)"
bash $K cpu8 td-bild code/td.py bild --ordner lauf --out lauf/bild-takt-dynamik.png > lauf/td-bild.log 2>&1; echo "td-bild rc=$? $(date -u +%H:%M:%S)"
bash $K cpu8 td-tab nachtrag/code/tabellen.py lauf/auswertung.json lauf/tabellen.md > lauf/td-tab.log 2>&1; echo "td-tab rc=$? $(date -u +%H:%M:%S)"
(cd lauf && sha256sum *.json *.png *.md *.log *.out > PRUEFSUMMEN.txt)
(cd nachtrag && sha256sum dehnung.json nt-dehnung.log code/*.py > PRUEFSUMMEN.txt)
echo "abschluss ende $(date -u +%H:%M:%S)"
