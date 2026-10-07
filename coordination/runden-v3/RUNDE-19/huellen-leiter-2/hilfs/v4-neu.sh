#!/bin/bash
# V4b: Auswertung Suchbereich (kleintest, Spur $1), schreibt auch aus/umlauf-punkte-st1/2.json
D=/home/fmh/fmhc-physics-remote/runde19-huellen-leiter-2
cd $D && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh $1 r19hl2-ausw-neu /home/fmh/fmhc-physics-remote/runde19-huellen-leiter-2/code/auswertung2.py neu $D/aus/laeufe $D/ref/stellen-r18.json $D/aus/prof-st1 $D/aus/prof-st2 $D/ref/profile-info-r18-st1.json $D/ref/profile-info-r18-st2.json $D/aus/neu-auswertung.json > $D/logs/r19hl2-ausw-neu.log 2>&1
