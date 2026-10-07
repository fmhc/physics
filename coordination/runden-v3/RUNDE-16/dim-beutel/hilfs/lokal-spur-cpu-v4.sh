#!/bin/bash
# Lokale Laufreihe Spur cpu, Version 4 (10:22). Je Zeile ein ssh-Aufruf von kleintest.sh.
D=/home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-16/dim-beutel
while kill -0 2246046 2>/dev/null; do sleep 5; done
ssh fmh@192.168.178.69 'cd /home/fmh/fmhc-physics-remote/runde16-dim-beutel && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu db-kub64-ab code/dimbeutel2.py ast --graph kubisch --size 64 --tag kub64-ab --out aus/haupt --kstart 40 --kende 0 --richtung -1 --maxcor 5' > $D/aus/logs/kub64-ab.log 2>&1
ssh fmh@192.168.178.69 'cd /home/fmh/fmhc-physics-remote/runde16-dim-beutel && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu db-kub48-auf code/dimbeutel2.py ast --graph kubisch --size 48 --tag kub48-auf --out aus/kontrolle --kstart 40 --kende 70 --richtung 1 --maxcor 5' > $D/aus/logs/kub48-auf.log 2>&1
ssh fmh@192.168.178.69 'cd /home/fmh/fmhc-physics-remote/runde16-dim-beutel && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu db-frisch-kub64 code/dimbeutel2.py frisch --graph kubisch --size 64 --tag kub64 --out aus/frisch --klist 30,50,70 --formen A,B --maxcor 5' > $D/aus/logs/frisch-kub64.log 2>&1
ssh fmh@192.168.178.69 'cd /home/fmh/fmhc-physics-remote/runde16-dim-beutel && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu db-frisch-ket code/dimbeutel2.py frisch --graph kette --size 4096 --tag ket4096 --out aus/frisch --klist 30,50,70 --formen A,B --maxcor 20' > $D/aus/logs/frisch-ket4096.log 2>&1
date --iso-8601=seconds > $D/aus/logs/spur-cpu-v4.fertig
