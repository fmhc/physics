#!/bin/bash
# SD-1 (Runde 9), Kette V auf Spur cpu5 (ab 09:59, Freigabe der Leitung fuer cpu5): gebundene l = 1-Zustaende (Spin-Dipol-
# Gegenprobe, Existenzschwelle) bei g = 0,2 und 0,02, Schwelle des Gegenlaeufers bei g = 0,2 fein, Umlauf an 0,5564.
B=/home/fmh/fmhc-physics-remote/runde9-sd1; K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh; cd $B || exit 1
echo KETTE-SD1-V-START $(date -Is)
bash $K cpu5 sd1v1 sd1.py gebunden --kanal anti --g 0.2 --l 1 --omega2-liste 0.51,0.52,0.54,0.56,0.60,0.64,0.66,0.665,0.67,0.675 --h 0.02 --n-geb 400 --out /home/fmh/fmhc-physics-remote/runde9-sd1/aus-v1-gebunden-anti-g02-l1
bash $K cpu5 sd1v2 sd1.py gebunden --kanal anti --g 0.02 --l 1 --omega2-liste 0.60,0.65,0.70,0.75,0.80,0.85 --h 0.02 --n-geb 400 --out /home/fmh/fmhc-physics-remote/runde9-sd1/aus-v2-gebunden-anti-g002-l1
bash $K cpu5 sd1v3 sd1.py kurve --kanal anti --g 0.2 --l 1 --abstand 0 --omega2-liste 0.660,0.662,0.664,0.666,0.668,0.670,0.672 --h 0.02 --out /home/fmh/fmhc-physics-remote/runde9-sd1/aus-v3-kurve-anti-g02-l1-schwelle
bash $K cpu5 sd1v4 sd1.py exakt --kanal anti --g 0.2 --l 1 --h 0.02 --x0 0.5564 --rho0 1.659821 --drho 1.47 --cgam 0.1 --offsets 0,2e-5,-2e-5,1e-4,-1e-4,5e-4,-5e-4,1.5e-3,-1.5e-3 --u-n 3000 --reserve 150 --out /home/fmh/fmhc-physics-remote/runde9-sd1/aus-v4-exakt-anti-g02-l1-05564
echo KETTE-SD1-V-ENDE $(date -Is)
