#!/bin/bash
# SP-1 (Runde 8), Kette K auf Spur cpu2: Umlauf aufloesen wie Kette J, l = 2 bei 0,606981 (--u-n 3000).
# Einmalig vom Code-Agenten gestartet.
B=/home/fmh/fmhc-physics-remote/runde7-bic2; K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh; cd $B || exit 1
echo KETTE-SP1-K-START $(date -Is)
bash $K cpu2 sp1d22r bic2.py exakt --geraet cpu --pot poly --beta 0.5 --l 2 --h 0.01 --x0 0.606981 --rho0 1.694040 --drho 2.37 --cgam 58 --offsets 0,2e-5,-2e-5,1e-4,-1e-4,5e-4,-5e-4 --u-n 3000 --reserve 150 --out aus-sp1-d-exakt-l2-0607-un3000
echo KETTE-SP1-K-ENDE $(date -Is)
