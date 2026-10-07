#!/bin/bash
# Lokale Laufreihe Spur cpu2, Version 5 (10:29). Je Zeile ein ssh-Aufruf von kleintest.sh.
D=/home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-16/dim-beutel
while kill -0 2259214 2>/dev/null; do sleep 5; done
ssh fmh@192.168.178.69 'cd /home/fmh/fmhc-physics-remote/runde16-dim-beutel && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu2 db-z4-g9 code/dimbeutel2.py frisch --graph sierpinski --size 9 --start s1 --tag sie9s1-z4 --out aus/frisch --klist 46,58,70 --formen A --maxcor 5' > $D/aus/logs/frisch-sie9s1-z4.log 2>&1
ssh fmh@192.168.178.69 'cd /home/fmh/fmhc-physics-remote/runde16-dim-beutel && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu2 db-z4-s2 code/dimbeutel2.py frisch --graph sierpinski --size 10 --start s2 --tag sie10s2-z4 --out aus/frisch --klist 46,58,70 --formen A --maxcor 5' > $D/aus/logs/frisch-sie10s2-z4.log 2>&1
ssh fmh@192.168.178.69 'cd /home/fmh/fmhc-physics-remote/runde16-dim-beutel && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu2 db-sie10s1-oben code/dimbeutel2.py ast --graph sierpinski --size 10 --start s1 --tag sie10s1-oben --out aus/haupt --kstart 87 --kende 0 --richtung -1 --maxcor 5 --tmax 420' > $D/aus/logs/sie10s1-oben.log 2>&1
date --iso-8601=seconds > $D/aus/logs/spur-cpu2-v5.fertig
