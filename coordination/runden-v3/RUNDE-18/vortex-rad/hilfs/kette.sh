#!/bin/bash
# Laufkette VORTEX-RAD, nacheinander auf Spur cpu6 (jeder Aufruf eigene Unit, <= 600 s)
R=/home/fmh/fmhc-physics-remote/runde18-vortex-rad
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
lauf () { echo "=== $(date '+%H:%M:%S') $*"; ssh fmh@192.168.178.69 "cd $R && bash $K cpu6 $*" 2>&1 | grep -v '^scan J\|^kontrolle J\|^L-a \|^L-b ' ; echo "=== ende $(date '+%H:%M:%S')"; }
lauf r18vx-scan002 code/vortex_rad.py scan $R/aus/scan_J0.02.json 0.02
lauf r18vx-scan005 code/vortex_rad.py scan $R/aus/scan_J0.05.json 0.05
lauf r18vx-scan010 code/vortex_rad.py scan $R/aus/scan_J0.1.json 0.1
lauf r18vx-lokal code/vortex_rad.py lokal $R/aus/lokal.json
lauf r18vx-kontrolle code/vortex_rad.py kontrolle $R/aus/kontrolle.json
lauf r18vx-nmax code/vortex_rad.py nmax $R/aus/nmax.json
lauf r18vx-zeit code/vortex_rad.py zeit $R/aus/zeit.json
lauf r18vx-ausw code/auswertung.py $R/aus
echo KETTE_FERTIG
