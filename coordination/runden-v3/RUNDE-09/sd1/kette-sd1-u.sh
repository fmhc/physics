#!/bin/bash
# SD-1 (Runde 9), Kette U auf Spur cpu2 (ab 09:59): Umlauf an 0,5223 (Fenster 0,51 bis 0,545) und 0,58872 (oberhalb 0,56),
# danach Gegenprobe g = 0,02: kurve 0,70 bis 0,84 (Existenzschwelle). Einmalig gestartet; kein Dienst, kein Timer.
B=/home/fmh/fmhc-physics-remote/runde9-sd1; K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh; cd $B || exit 1
echo KETTE-SD1-U-START $(date -Is)
bash $K cpu2 sd1u1 sd1.py exakt --kanal anti --g 0.2 --l 1 --h 0.02 --x0 0.5223 --rho0 1.611139 --drho 1.38 --cgam 0.5 --offsets 0,2e-5,-2e-5,1e-4,-1e-4,5e-4,-5e-4,1.5e-3,-1.5e-3 --u-n 3000 --reserve 150 --out /home/fmh/fmhc-physics-remote/runde9-sd1/aus-u1-exakt-anti-g02-l1-05223
bash $K cpu2 sd1u2 sd1.py exakt --kanal anti --g 0.2 --l 1 --h 0.02 --x0 0.588716 --rho0 1.707484 --drho 1.47 --cgam 0.02 --offsets 0,2e-5,-2e-5,1e-4,-1e-4,5e-4,-5e-4,1.5e-3,-1.5e-3 --u-n 3000 --reserve 150 --out /home/fmh/fmhc-physics-remote/runde9-sd1/aus-u2-exakt-anti-g02-l1-05887
bash $K cpu2 sd1u3 sd1.py kurve --kanal anti --g 0.02 --l 1 --abstand 0 --xmin 0.70 --xmax 0.84 --dx 0.02 --h 0.02 --out /home/fmh/fmhc-physics-remote/runde9-sd1/aus-u3-kurve-anti-g002-l1-070
echo KETTE-SD1-U-ENDE $(date -Is)
