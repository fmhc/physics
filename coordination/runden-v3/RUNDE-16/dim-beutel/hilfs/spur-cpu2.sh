#!/bin/bash
# Laufreihe Spur cpu2 (DIM-BEUTEL, Hauptlaeufe 2). Nur Folge von kleintest.sh-Aufrufen, kein Dienst.
cd /home/fmh/fmhc-physics-remote/runde16-dim-beutel || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
P=code/dimbeutel.py
mkdir -p aus/logs aus/haupt aus/kontrolle aus/frisch aus/ds
bash $K cpu2 db-sie10s1-auf $P ast --graph sierpinski --size 10 --start s1 --tag sie10s1-auf --out aus/haupt --kstart 40 --kende 87 --richtung 1 > aus/logs/sie10s1-auf.log 2>&1
bash $K cpu2 db-qu256-auf $P ast --graph quadrat --size 256 --tag qu256-auf --out aus/haupt --kstart 40 --kende 79 --richtung 1 > aus/logs/qu256-auf.log 2>&1
bash $K cpu2 db-kub64-ab $P ast --graph kubisch --size 64 --tag kub64-ab --out aus/haupt --kstart 40 --kende 0 --richtung -1 > aus/logs/kub64-ab.log 2>&1
bash $K cpu2 db-qu256-ab $P ast --graph quadrat --size 256 --tag qu256-ab --out aus/haupt --kstart 40 --kende 0 --richtung -1 > aus/logs/qu256-ab.log 2>&1
bash $K cpu2 db-qu192-auf $P ast --graph quadrat --size 192 --tag qu192-auf --out aus/kontrolle --kstart 40 --kende 73 --richtung 1 > aus/logs/qu192-auf.log 2>&1
bash $K cpu2 db-sie9s1-auf $P ast --graph sierpinski --size 9 --start s1 --tag sie9s1-auf --out aus/kontrolle --kstart 40 --kende 75 --richtung 1 > aus/logs/sie9s1-auf.log 2>&1
bash $K cpu2 db-ds $P ds --out aus/ds --ds-g 7 --walk-g 10 --walk-starts s1,s2 --walk-tmax 15625 > aus/logs/ds.log 2>&1
bash $K cpu2 db-frisch-sie10 $P frisch --graph sierpinski --size 10 --start s1 --tag sie10s1 --out aus/frisch --klist 30,50,70,80 --formen A,B > aus/logs/frisch-sie10s1.log 2>&1
bash $K cpu2 db-frisch-qu256 $P frisch --graph quadrat --size 256 --tag qu256 --out aus/frisch --klist 30,50,70 --formen A,B > aus/logs/frisch-qu256.log 2>&1
bash $K cpu2 db-ket8192-auf $P ast --graph kette --size 8192 --tag ket8192-auf --out aus/kontrolle --kstart 40 --kende 79 --richtung 1 > aus/logs/ket8192-auf.log 2>&1
echo "spur cpu2 fertig $(date --iso-8601=seconds)" > aus/logs/spur-cpu2.fertig
