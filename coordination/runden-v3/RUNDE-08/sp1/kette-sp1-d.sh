#!/bin/bash
# SP-1 (Runde 8), Kette D auf Spur cpu2: (a) zweiter Lauf, zentriert auf die W-Nullstelle aus dem ersten Lauf
# (aus-sp1-a-exakt-l1-0756: neu gelegt, zweiter Fit 0,754503912 / rho 1,8263470357). Einmalig vom Code-Agenten gestartet.
B=/home/fmh/fmhc-physics-remote/runde7-bic2; K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh; cd $B || exit 1
echo KETTE-SP1-D-START $(date -Is)
bash $K cpu2 sp1a2 bic2.py exakt --geraet cpu --pot poly --beta 0.5 --l 1 --h 0.01 --x0 0.754504 --rho0 1.826347 --drho 1.16 --cgam 0.92 --offsets 0,2e-5,-2e-5,1e-4,-1e-4,3e-4,-3e-4,5e-4,-5e-4 --reserve 150 --out aus-sp1-a2-exakt-l1-07545
echo KETTE-SP1-D-ENDE $(date -Is)
