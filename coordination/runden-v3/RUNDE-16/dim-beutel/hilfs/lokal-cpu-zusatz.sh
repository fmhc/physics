#!/bin/bash
# Lokale Zusatzreihe Spur cpu (10:29): Quadrat-Kontrollen von cpu2 hierher verlegt.
D=/home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-16/dim-beutel
ssh fmh@192.168.178.69 'cd /home/fmh/fmhc-physics-remote/runde16-dim-beutel && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu db-qu192-auf code/dimbeutel2.py ast --graph quadrat --size 192 --tag qu192-auf --out aus/kontrolle --kstart 40 --kende 73 --richtung 1 --maxcor 5' > $D/aus/logs/qu192-auf.log 2>&1
ssh fmh@192.168.178.69 'cd /home/fmh/fmhc-physics-remote/runde16-dim-beutel && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu db-frisch-qu256 code/dimbeutel2.py frisch --graph quadrat --size 256 --tag qu256 --out aus/frisch --klist 30,50,70 --formen A,B --maxcor 5' > $D/aus/logs/frisch-qu256.log 2>&1
date --iso-8601=seconds > $D/aus/logs/cpu-zusatz.fertig
