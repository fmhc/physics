#!/bin/bash
# SP-1 (Runde 8), Kette M auf Spur cpu: exakt l = 2 bei 0,643905 (kurve c12, h = 0,02, Feinverfahren s -> 4e-9,
# Pol 1,76208261 + 2,75e-9 i). Einmalig vom Code-Agenten gestartet.
B=/home/fmh/fmhc-physics-remote/runde7-bic2; K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh; cd $B || exit 1
echo KETTE-SP1-M-START $(date -Is)
bash $K cpu sp1d20 bic2.py exakt --geraet cpu --pot poly --beta 0.5 --l 2 --h 0.01 --x0 0.643905 --rho0 1.762083 --drho 2.06 --cgam 13.5 --offsets 0,2e-5,-2e-5,1e-4,-1e-4,5e-4,-5e-4 --u-n 3000 --reserve 150 --out aus-sp1-d-exakt-l2-0644
echo KETTE-SP1-M-ENDE $(date -Is)
