#!/bin/bash
# Lokale Laufreihe Nachtrag 2 (Z1, Z2)
D=/home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-16/dim-beutel
ssh fmh@192.168.178.69 'cd /home/fmh/fmhc-physics-remote/runde16-dim-beutel && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu2 db-sie10s1-oben code/dimbeutel.py ast --graph sierpinski --size 10 --start s1 --tag sie10s1-oben --out aus/haupt --kstart 87 --kende 0 --richtung -1' > $D/aus/logs/sie10s1-oben.log 2>&1
ssh fmh@192.168.178.69 'cd /home/fmh/fmhc-physics-remote/runde16-dim-beutel && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu db-qu256-oben code/dimbeutel.py ast --graph quadrat --size 256 --tag qu256-oben --out aus/haupt --kstart 79 --kende 0 --richtung -1' > $D/aus/logs/qu256-oben.log 2>&1
date --iso-8601=seconds > $D/aus/logs/nachtrag2.fertig
