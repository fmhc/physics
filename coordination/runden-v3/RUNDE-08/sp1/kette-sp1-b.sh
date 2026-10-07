#!/bin/bash
# SP-1 (Runde 8), Kette B auf Spur cpu2. Einmalig vom Code-Agenten gestartet; kein Dienst, kein Timer, kein Hook.
# (b) kurve l = 1 von 0,58 bis 0,75 in drei Teilen, (c) kurve l = 2 von 0,55 bis 0,74 in zwei Teilen, dazu l = 1 oberhalb.
B=/home/fmh/fmhc-physics-remote/runde7-bic2; K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh; cd $B || exit 1
echo KETTE-SP1-B-START $(date -Is)
bash $K cpu2 sp1b2 bic2.py kurve --geraet cpu --pot poly --beta 0.5 --l 1 --abstand 0.05 --xmin 0.63 --xmax 0.675 --dx 0.005 --h 0.02 --out aus-sp1-b2-kurve-l1
bash $K cpu2 sp1b1 bic2.py kurve --geraet cpu --pot poly --beta 0.5 --l 1 --abstand 0.05 --xmin 0.58 --xmax 0.625 --dx 0.005 --h 0.02 --out aus-sp1-b1-kurve-l1
bash $K cpu2 sp1b3 bic2.py kurve --geraet cpu --pot poly --beta 0.5 --l 1 --abstand 0.05 --xmin 0.68 --xmax 0.75 --dx 0.01 --h 0.02 --out aus-sp1-b3-kurve-l1
bash $K cpu2 sp1c1 bic2.py kurve --geraet cpu --pot poly --beta 0.5 --l 2 --abstand 0.05 --xmin 0.55 --xmax 0.64 --dx 0.01 --h 0.02 --out aus-sp1-c1-kurve-l2
bash $K cpu2 sp1c2 bic2.py kurve --geraet cpu --pot poly --beta 0.5 --l 2 --abstand 0.05 --xmin 0.65 --xmax 0.74 --dx 0.01 --h 0.02 --out aus-sp1-c2-kurve-l2
bash $K cpu2 sp1b4 bic2.py kurve --geraet cpu --pot poly --beta 0.5 --l 1 --abstand 0.05 --xmin 0.77 --xmax 0.95 --dx 0.02 --h 0.02 --out aus-sp1-b4-kurve-l1-oben
echo KETTE-SP1-B-ENDE $(date -Is)
