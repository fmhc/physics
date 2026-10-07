#!/bin/bash
# SP-1 (Runde 8), Kette H auf Spur cpu: (d) exakt l = 2 an 0,58539 (kurve c1, h = 0,02, Feinverfahren 0,58539473 /
# rho 1,65530469), dann kurve l = 2 fein 0,562 bis 0,580 (s bei 0,57 fast null; PLAN.md Nachtrag 07:26:25).
B=/home/fmh/fmhc-physics-remote/runde7-bic2; K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh; cd $B || exit 1
echo KETTE-SP1-H-START $(date -Is)
bash $K cpu sp1d21 bic2.py exakt --geraet cpu --pot poly --beta 0.5 --l 2 --h 0.01 --x0 0.585395 --rho0 1.655305 --drho 2.7 --cgam 140 --offsets 0,2e-5,-2e-5,1e-4,-1e-4,3e-4,-3e-4,5e-4,-5e-4 --reserve 150 --out aus-sp1-d-exakt-l2-0585
bash $K cpu sp1c0 bic2.py kurve --geraet cpu --pot poly --beta 0.5 --l 2 --abstand 0.05 --xmin 0.562 --xmax 0.58 --dx 0.002 --h 0.02 --out aus-sp1-c0-kurve-l2-fein
echo KETTE-SP1-H-ENDE $(date -Is)
