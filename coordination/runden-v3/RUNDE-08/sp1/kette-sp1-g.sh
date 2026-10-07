#!/bin/bash
# SP-1 (Runde 8), Kette G auf Spur cpu2: (d) exakt l = 2 an 0,60698 (kurve c1, h = 0,02, Feinverfahren 0,60698032 /
# rho 1,69403861), dann kurve l = 2 ueber die Luecke 0,64 bis 0,65 (Erwartung 0,6427, PLAN.md Nachtrag 07:26:25).
B=/home/fmh/fmhc-physics-remote/runde7-bic2; K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh; cd $B || exit 1
echo KETTE-SP1-G-START $(date -Is)
bash $K cpu2 sp1d22 bic2.py exakt --geraet cpu --pot poly --beta 0.5 --l 2 --h 0.01 --x0 0.606980 --rho0 1.694039 --drho 2.37 --cgam 58 --offsets 0,2e-5,-2e-5,1e-4,-1e-4,3e-4,-3e-4,5e-4,-5e-4 --reserve 150 --out aus-sp1-d-exakt-l2-0607
bash $K cpu2 sp1c12 bic2.py kurve --geraet cpu --pot poly --beta 0.5 --l 2 --abstand 0.05 --xmin 0.635 --xmax 0.655 --dx 0.005 --h 0.02 --n-wechsel-fein 1 --out aus-sp1-c12-kurve-l2-luecke
echo KETTE-SP1-G-ENDE $(date -Is)
