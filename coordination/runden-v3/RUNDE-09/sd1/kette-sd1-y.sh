#!/bin/bash
# SD-1 (Runde 9), Kette Y auf Spur cpu2 (ab 10:08): Gegentakt l = 0 bei g = 0,2 (Gegenlaeufer-Leiter), fuer die optionale
# Regel 5 (halbe Stufe zwischen l = 0 und l = 1). Einmalig gestartet; kein Dienst, kein Timer.
B=/home/fmh/fmhc-physics-remote/runde9-sd1; K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh; cd $B || exit 1
echo KETTE-SD1-Y-START $(date -Is)
bash $K cpu2 sd1y1 sd1.py kurve --kanal anti --g 0.2 --l 0 --abstand 0 --xmin 0.50 --xmax 0.58 --dx 0.005 --h 0.02 --out /home/fmh/fmhc-physics-remote/runde9-sd1/aus-y1-kurve-anti-g02-l0-050
bash $K cpu2 sd1y2 sd1.py kurve --kanal anti --g 0.2 --l 0 --abstand 0 --xmin 0.585 --xmax 0.675 --dx 0.01 --h 0.02 --out /home/fmh/fmhc-physics-remote/runde9-sd1/aus-y2-kurve-anti-g02-l0-0585
echo KETTE-SD1-Y-ENDE $(date -Is)
