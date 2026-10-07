#!/bin/bash
# SD-1 (Runde 9), Kette W auf Spur cpu (ab 10:05): Existenzschwellen fein ueber gebundene l = 1-Zustaende, g = 0,2
# (zwischen 0,670 und 0,675) und g = 0,02 (zwischen 0,70 und 0,75). Einmalig gestartet; kein Dienst, kein Timer.
B=/home/fmh/fmhc-physics-remote/runde9-sd1; K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh; cd $B || exit 1
echo KETTE-SD1-W-START $(date -Is)
bash $K cpu sd1w1 sd1.py gebunden --kanal anti --g 0.2 --l 1 --omega2-liste 0.671,0.672,0.673,0.674 --h 0.02 --n-geb 400 --out /home/fmh/fmhc-physics-remote/runde9-sd1/aus-w1-gebunden-anti-g02-l1-schwelle
bash $K cpu sd1w2 sd1.py gebunden --kanal anti --g 0.02 --l 1 --omega2-liste 0.71,0.72,0.73,0.74 --h 0.02 --n-geb 400 --out /home/fmh/fmhc-physics-remote/runde9-sd1/aus-w2-gebunden-anti-g002-l1-schwelle
echo KETTE-SD1-W-ENDE $(date -Is)
