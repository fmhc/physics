#!/bin/bash
# SP-1 (Runde 8), Kette L auf Spur cpu2: exakt l = 1, n = 5 bei 0,57607 (kurve b6, h = 0,02: Gamma-Minimum, Feinverfahren
# s -> 7,9e-8, Pol 1,61682695 - 4,7e-9 i; Vorhersage PLAN.md Nachtrag 07:14:50: 0,57609 +- 0,0003, Umlauf -1).
B=/home/fmh/fmhc-physics-remote/runde7-bic2; K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh; cd $B || exit 1
echo KETTE-SP1-L-START $(date -Is)
bash $K cpu2 sp1d15 bic2.py exakt --geraet cpu --pot poly --beta 0.5 --l 1 --h 0.01 --x0 0.576070 --rho0 1.616827 --drho 2.56 --cgam 300 --offsets 0,2e-5,-2e-5,1e-4,-1e-4,5e-4,-5e-4 --u-n 3000 --reserve 150 --out aus-sp1-d-exakt-l1-0576
echo KETTE-SP1-L-ENDE $(date -Is)
