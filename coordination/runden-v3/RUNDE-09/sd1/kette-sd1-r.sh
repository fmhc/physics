#!/bin/bash
# SD-1 (Runde 9), Kette R auf Spur cpu2 (nach der Freigabe 08:28): Gegentakt des gemischten Balls ("anti"), l = 1,
# g = 0,2: gebundene Zustaende (Spin-Dipol-Gegenprobe, Existenz) und Suche nach dem Gegenlaeufer oberhalb 0,56.
# Einmalig vom Code-Agenten gestartet; kein Dienst, kein Timer, kein Hook.
B=/home/fmh/fmhc-physics-remote/runde9-sd1; K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh; cd $B || exit 1
echo KETTE-SD1-R-START $(date -Is)
bash $K cpu2 sd1r1 sd1.py gebunden --kanal anti --g 0.2 --l 1 --omega2-liste 0.50,0.52,0.54,0.56,0.58,0.60,0.62,0.64,0.66,0.68,0.70,0.72 --h 0.02 --n-geb 400 --out /home/fmh/fmhc-physics-remote/runde9-sd1/aus-r1-gebunden-anti-g02-l1
bash $K cpu2 sd1r2 sd1.py kurve --kanal anti --g 0.2 --l 1 --abstand 0 --xmin 0.56 --xmax 0.64 --dx 0.01 --h 0.02 --out /home/fmh/fmhc-physics-remote/runde9-sd1/aus-r2-kurve-anti-g02-l1-056
bash $K cpu2 sd1r3 sd1.py kurve --kanal anti --g 0.2 --l 1 --abstand 0 --xmin 0.65 --xmax 0.73 --dx 0.01 --h 0.02 --out /home/fmh/fmhc-physics-remote/runde9-sd1/aus-r3-kurve-anti-g02-l1-065
echo KETTE-SD1-R-ENDE $(date -Is)
