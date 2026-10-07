#!/bin/bash
# Laufreihe Spur cpu (DIM-BEUTEL, Hauptlaeufe 1). Nur Folge von kleintest.sh-Aufrufen, kein Dienst.
cd /home/fmh/fmhc-physics-remote/runde16-dim-beutel || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
P=code/dimbeutel.py
mkdir -p aus/logs aus/haupt aus/kontrolle aus/frisch aus/ds
bash $K cpu db-kub64-auf $P ast --graph kubisch --size 64 --tag kub64-auf --out aus/haupt --kstart 40 --kende 77 --richtung 1 > aus/logs/kub64-auf.log 2>&1
bash $K cpu db-ket4096-auf $P ast --graph kette --size 4096 --tag ket4096-auf --out aus/haupt --kstart 40 --kende 79 --richtung 1 > aus/logs/ket4096-auf.log 2>&1
bash $K cpu db-ket4096-ab $P ast --graph kette --size 4096 --tag ket4096-ab --out aus/haupt --kstart 40 --kende 0 --richtung -1 > aus/logs/ket4096-ab.log 2>&1
bash $K cpu db-sie10s1-ab $P ast --graph sierpinski --size 10 --start s1 --tag sie10s1-ab --out aus/haupt --kstart 40 --kende 0 --richtung -1 > aus/logs/sie10s1-ab.log 2>&1
bash $K cpu db-sie10s2-auf $P ast --graph sierpinski --size 10 --start s2 --tag sie10s2-auf --out aus/kontrolle --kstart 40 --kende 87 --richtung 1 > aus/logs/sie10s2-auf.log 2>&1
bash $K cpu db-kub48-auf $P ast --graph kubisch --size 48 --tag kub48-auf --out aus/kontrolle --kstart 40 --kende 70 --richtung 1 > aus/logs/kub48-auf.log 2>&1
bash $K cpu db-frisch-kub64 $P frisch --graph kubisch --size 64 --tag kub64 --out aus/frisch --klist 30,50,70 --formen A,B > aus/logs/frisch-kub64.log 2>&1
bash $K cpu db-frisch-ket $P frisch --graph kette --size 4096 --tag ket4096 --out aus/frisch --klist 30,50,70 --formen A,B > aus/logs/frisch-ket4096.log 2>&1
echo "spur cpu fertig $(date --iso-8601=seconds)" > aus/logs/spur-cpu.fertig
