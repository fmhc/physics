#!/bin/bash
# SD-1 (Runde 9), Kette Q auf Spur cpu: Proben Q2 (kurve psi_2, l = 0, g = 0,2 ueber Z1 und Z2) und Q1 (exakt psi_2,
# l = 0, an Z2). Einmalig vom Code-Agenten gestartet; kein Dienst, kein Timer, kein Hook.
B=/home/fmh/fmhc-physics-remote/runde9-sd1; K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh; cd $B || exit 1
echo KETTE-SD1-Q-START $(date -Is)
bash $K cpu sd1q2 sd1.py kurve --kanal psi2 --g 0.2 --abstand 0.05 --xmin 0.63 --xmax 0.73 --dx 0.01 --h 0.02 --out /home/fmh/fmhc-physics-remote/runde9-sd1/aus-q2-kurve-psi2-l0
bash $K cpu sd1q1 sd1.py exakt --kanal psi2 --g 0.2 --h 0.02 --x0 0.645862 --rho0 1.610366 --drho 1.25 --cgam 0.01 --offsets 0,2e-5,-2e-5,1e-4,-1e-4,5e-4,-5e-4 --u-n 3000 --reserve 150 --out /home/fmh/fmhc-physics-remote/runde9-sd1/aus-q1-exakt-psi2-Z2
echo KETTE-SD1-Q-ENDE $(date -Is)
