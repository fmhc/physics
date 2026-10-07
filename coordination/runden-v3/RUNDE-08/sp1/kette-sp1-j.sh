#!/bin/bash
# SP-1 (Runde 8), Kette J auf Spur cpu: Umlauf aufloesen (nur Argumente, kein Code): Die groessten Phasenspruenge lagen
# auf den rho-Seiten (W dreht dort auf < 1e-7 in rho). Mehr Startpunkte je rho-Seite (--u-n 3000), Mitte auf die
# A_out-Nullstelle. l = 2 bei 0,585391, danach l = 1, n = 4 bei 0,592242. Einmalig vom Code-Agenten gestartet.
B=/home/fmh/fmhc-physics-remote/runde7-bic2; K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh; cd $B || exit 1
echo KETTE-SP1-J-START $(date -Is)
bash $K cpu sp1d21r bic2.py exakt --geraet cpu --pot poly --beta 0.5 --l 2 --h 0.01 --x0 0.585391 --rho0 1.655298 --drho 2.73 --cgam 140 --offsets 0,2e-5,-2e-5,1e-4,-1e-4,5e-4,-5e-4 --u-n 3000 --reserve 150 --out aus-sp1-d-exakt-l2-0585-un3000
bash $K cpu sp1d14r bic2.py exakt --geraet cpu --pot poly --beta 0.5 --l 1 --h 0.01 --x0 0.592242 --rho0 1.636294 --drho 2.05 --cgam 130 --offsets 0,2e-5,-2e-5,1e-4,-1e-4,5e-4,-5e-4 --u-n 3000 --reserve 150 --out aus-sp1-d-exakt-l1-0592-un3000
echo KETTE-SP1-J-ENDE $(date -Is)
