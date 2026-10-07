#!/bin/bash
# SD-1 (Runde 9), Kette S auf Spur cpu (nach der Freigabe 08:28): Gegentakt "anti", l = 1: Duennwand-Bereich bei g = 0,2
# (vorhergesagte Stellen 0,515 bis 0,539), Gegenprobe g = 0,02 (Existenzschwelle), Querprobe l = 0 gegen ROT-2.
# Einmalig vom Code-Agenten gestartet; kein Dienst, kein Timer, kein Hook.
B=/home/fmh/fmhc-physics-remote/runde9-sd1; K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh; cd $B || exit 1
echo KETTE-SD1-S-START $(date -Is)
bash $K cpu sd1s1 sd1.py kurve --kanal anti --g 0.2 --l 1 --abstand 0 --xmin 0.505 --xmax 0.555 --dx 0.005 --h 0.02 --out /home/fmh/fmhc-physics-remote/runde9-sd1/aus-s1-kurve-anti-g02-l1-0505
bash $K cpu sd1s2 sd1.py gebunden --kanal anti --g 0.02 --l 1 --omega2-liste 0.52,0.55,0.58,0.60,0.62,0.64,0.66,0.68,0.70,0.72,0.74 --h 0.02 --n-geb 400 --out /home/fmh/fmhc-physics-remote/runde9-sd1/aus-s2-gebunden-anti-g002-l1
bash $K cpu sd1s3 sd1.py kurve --kanal anti --g 0.02 --l 1 --abstand 0 --xmin 0.56 --xmax 0.70 --dx 0.02 --h 0.02 --out /home/fmh/fmhc-physics-remote/runde9-sd1/aus-s3-kurve-anti-g002-l1
bash $K cpu sd1q5 sd1.py kurve --kanal anti --g 0.05 --l 0 --abstand 0 --omega2-liste 0.70,0.72 --h 0.02 --out /home/fmh/fmhc-physics-remote/runde9-sd1/aus-q5-kurve-anti-g005-l0
echo KETTE-SD1-S-ENDE $(date -Is)
