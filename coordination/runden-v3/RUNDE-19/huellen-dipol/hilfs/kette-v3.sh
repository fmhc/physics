#!/bin/bash
H=/home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-19/huellen-dipol/hilfs
B=/home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-19/huellen-dipol
R=/home/fmh/fmhc-physics-remote/runde19-huellen-dipol
rsync -a $B/code/dipol.py $B/code/auswertung.py $B/code/auswertung_dipol.py fmh@192.168.178.69:$R/code/
rsync -a $B/hilfs/l0-kurven.json fmh@192.168.178.69:$R/aus/laeufe/l0-kurven.json
ssh fmh@192.168.178.69 "cp $R/aus/k1-st1.json $R/aus/k1-st2.json $R/aus/laeufe/"
$H/k.sh r19-pruef2 code/pruef.py code/dipol.py code/auswertung.py code/auswertung_dipol.py
$H/k.sh r19-stellen code/auswertung_dipol.py stellen aus/laeufe aus/zeilen.json aus/laeufe/l0-kurven.json aus/laeufe/auswertung.json
$H/k.sh r19-uP1 code/dipol.py umlauf 1 aus/prof-st1 aus/zeilen.json aus/laeufe/umlauf-punkte-P-st1.json aus/laeufe/umlauf-P-st1.json 0 99
$H/k.sh r19-uP2 code/dipol.py umlauf 2 aus/prof-st2 aus/zeilen.json aus/laeufe/umlauf-punkte-P-st2.json aus/laeufe/umlauf-P-st2.json 0 99
$H/k.sh r19-d4 code/dipol.py d4 1 aus/laeufe/k1-st1.json aus/laeufe/d4-st1.json
$H/k.sh r19-d4-w code/dipol.py d4 1 aus/laeufe/k1-st1.json aus/laeufe/d4-st1.json
$H/k.sh r19-final code/auswertung_dipol.py final aus/laeufe aus/laeufe/auswertung-final.json
$H/k.sh r19-bild code/auswertung_dipol.py bild aus/laeufe aus/abb-stellen.png aus/abb-abstand.png
$H/k.sh r19-uA1 code/dipol.py umlauf 1 aus/prof-st1 aus/zeilen.json aus/laeufe/umlauf-punkte-A-st1.json aus/laeufe/umlauf-A-st1.json 0 99
$H/k.sh r19-uA2 code/dipol.py umlauf 2 aus/prof-st2 aus/zeilen.json aus/laeufe/umlauf-punkte-A-st2.json aus/laeufe/umlauf-A-st2.json 0 99
$H/k.sh r19-final2 code/auswertung_dipol.py final aus/laeufe aus/laeufe/auswertung-final.json
