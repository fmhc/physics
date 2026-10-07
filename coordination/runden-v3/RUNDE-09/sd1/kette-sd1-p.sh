#!/bin/bash
# SD-1 (Runde 9), Kette P auf Spur cpu2: Proben Q0 (punkt Z1 wie R9, l = 0) und Q3 (l-Verdrahtung im psi_1-Kanal gegen
# SP-1 P1). Einmalig vom Code-Agenten gestartet; kein Dienst, kein Timer, kein Hook.
B=/home/fmh/fmhc-physics-remote/runde9-sd1; K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh; cd $B || exit 1
echo KETTE-SD1-P-START $(date -Is)
bash $K cpu2 sd1q0 sd1.py punkt --name Z1 --out /home/fmh/fmhc-physics-remote/runde9-sd1/aus-q0-Z1
bash $K cpu2 sd1q3 sd1.py kurve --kanal psi1 --l 1 --omega2-liste 0.72,0.75 --h 0.01 --out /home/fmh/fmhc-physics-remote/runde9-sd1/aus-q3-kurve-psi1-l1
echo KETTE-SD1-P-ENDE $(date -Is)
