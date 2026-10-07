#!/bin/bash
# V4a: K0-Auswertung (kleintest, Spur $1)
D=/home/fmh/fmhc-physics-remote/runde19-huellen-leiter-2
cd $D && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh $1 r19hl2-ausw-k0 /home/fmh/fmhc-physics-remote/runde19-huellen-leiter-2/code/auswertung2.py k0 $D/aus/laeufe $D/ref/stellen-r18.json $D/aus/k0 $D/aus/k0-auswertung.json > $D/logs/r19hl2-ausw-k0.log 2>&1
