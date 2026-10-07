#!/bin/bash
# SP-1 (Runde 8), Kette E auf Spur cpu: (d) exakt an l = 1, n = 3 und n = 4 (kurve b1, h = 0,02, Feinverfahren:
# 0,61710516 / rho 1,66605112 und 0,59224319 / rho 1,63629451). Einmalig vom Code-Agenten gestartet.
B=/home/fmh/fmhc-physics-remote/runde7-bic2; K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh; cd $B || exit 1
echo KETTE-SP1-E-START $(date -Is)
bash $K cpu sp1d13 bic2.py exakt --geraet cpu --pot poly --beta 0.5 --l 1 --h 0.01 --x0 0.617105 --rho0 1.666051 --drho 1.71 --cgam 48 --offsets 0,2e-5,-2e-5,1e-4,-1e-4,3e-4,-3e-4,5e-4,-5e-4 --reserve 150 --out aus-sp1-d-exakt-l1-0617
bash $K cpu sp1d14 bic2.py exakt --geraet cpu --pot poly --beta 0.5 --l 1 --h 0.01 --x0 0.592243 --rho0 1.636295 --drho 2.05 --cgam 130 --offsets 0,2e-5,-2e-5,1e-4,-1e-4,3e-4,-3e-4,5e-4,-5e-4 --reserve 150 --out aus-sp1-d-exakt-l1-0592
echo KETTE-SP1-E-ENDE $(date -Is)
