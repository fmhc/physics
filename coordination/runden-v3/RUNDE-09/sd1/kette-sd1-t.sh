#!/bin/bash
# SD-1 (Runde 9), Kette T auf Spur cpu (nach der Pause, ab 09:59): Umlauf (exakt, Kanal anti, g = 0,2, l = 1) an den
# Kandidaten 0,51271 und 0,5361 im Fenster 0,51 bis 0,545 und an 0,6498. Einmalig gestartet; kein Dienst, kein Timer.
B=/home/fmh/fmhc-physics-remote/runde9-sd1; K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh; cd $B || exit 1
echo KETTE-SD1-T-START $(date -Is)
bash $K cpu sd1t1 sd1.py exakt --kanal anti --g 0.2 --l 1 --h 0.02 --x0 0.512706 --rho0 1.598031 --drho 1.35 --cgam 0.5 --offsets 0,2e-5,-2e-5,1e-4,-1e-4,5e-4,-5e-4,1.5e-3,-1.5e-3 --u-n 3000 --reserve 150 --out /home/fmh/fmhc-physics-remote/runde9-sd1/aus-t1-exakt-anti-g02-l1-05127
bash $K cpu sd1t2 sd1.py exakt --kanal anti --g 0.2 --l 1 --h 0.02 --x0 0.5361 --rho0 1.630491 --drho 1.43 --cgam 0.5 --offsets 0,2e-5,-2e-5,1e-4,-1e-4,5e-4,-5e-4,1.5e-3,-1.5e-3 --u-n 3000 --reserve 150 --out /home/fmh/fmhc-physics-remote/runde9-sd1/aus-t2-exakt-anti-g02-l1-05361
bash $K cpu sd1t3 sd1.py exakt --kanal anti --g 0.2 --l 1 --h 0.02 --x0 0.6498 --rho0 1.793189 --drho 1.30 --cgam 0.003 --offsets 0,2e-5,-2e-5,1e-4,-1e-4,5e-4,-5e-4,1.5e-3,-1.5e-3 --u-n 3000 --reserve 150 --out /home/fmh/fmhc-physics-remote/runde9-sd1/aus-t3-exakt-anti-g02-l1-06498
echo KETTE-SD1-T-ENDE $(date -Is)
