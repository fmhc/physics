#!/bin/bash
# SD-1 (Runde 9), Kette X auf Spur cpu5 (ab 10:08): exakt zentriert auf die A_out-Nullstellen 0,556504 und 0,649310
# (kleine Rechtecke fehlten bzw. Umlauf nicht aufgeloest) und an 0,505096 (Duennwand). Einmalig gestartet.
B=/home/fmh/fmhc-physics-remote/runde9-sd1; K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh; cd $B || exit 1
echo KETTE-SD1-X-START $(date -Is)
bash $K cpu5 sd1x1 sd1.py exakt --kanal anti --g 0.2 --l 1 --h 0.02 --x0 0.556504 --rho0 1.659970 --drho 1.465 --cgam 0.1 --offsets 0,2e-5,-2e-5,1e-4,-1e-4,5e-4,-5e-4 --u-n 3000 --reserve 150 --out /home/fmh/fmhc-physics-remote/runde9-sd1/aus-x1-exakt-anti-g02-l1-055650
bash $K cpu5 sd1x2 sd1.py exakt --kanal anti --g 0.2 --l 1 --h 0.02 --x0 0.649310 --rho0 1.792567 --drho 1.30 --cgam 0.003 --offsets 0,2e-5,-2e-5,1e-4,-1e-4,5e-4,-5e-4 --u-n 6000 --reserve 150 --out /home/fmh/fmhc-physics-remote/runde9-sd1/aus-x2-exakt-anti-g02-l1-064931
bash $K cpu5 sd1x3 sd1.py exakt --kanal anti --g 0.2 --l 1 --h 0.02 --x0 0.505096 --rho0 1.587877 --drho 1.33 --cgam 0.5 --offsets 0,2e-5,-2e-5,1e-4,-1e-4,5e-4,-5e-4 --u-n 3000 --reserve 150 --out /home/fmh/fmhc-physics-remote/runde9-sd1/aus-x3-exakt-anti-g02-l1-050510
echo KETTE-SD1-X-ENDE $(date -Is)
