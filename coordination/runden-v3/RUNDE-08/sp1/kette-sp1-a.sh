#!/bin/bash
# SP-1 (Runde 8), Kette A auf Spur cpu. Einmalig vom Code-Agenten gestartet; kein Dienst, kein Timer, kein Hook.
# P0 (l = 0 bitgleich gegen aus-kurve-050-dicht), (a) exakt l = 1 um 0,7556, P1 (l = 1 gegen V6), (c) l = 2 oberer Teil.
B=/home/fmh/fmhc-physics-remote/runde7-bic2; K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh; cd $B || exit 1
echo KETTE-SP1-A-START $(date -Is)
bash $K cpu sp1p0 bic2.py kurve --geraet cpu --pot poly --beta 0.5 --xmin 0.555 --xmax 0.645 --dx 0.01 --h 0.02 --out aus-sp1-p0-kurve-050-dicht
bash $K cpu sp1a bic2.py exakt --geraet cpu --pot poly --beta 0.5 --l 1 --h 0.01 --x0 0.75565 --rho0 1.8276876 --drho 1.17 --cgam 0.45 --offsets 0,2e-5,-2e-5,1e-4,-1e-4,3e-4,-3e-4,5e-4,-5e-4 --reserve 150 --out aus-sp1-a-exakt-l1-0756
bash $K cpu sp1p1 bic2.py kurve --geraet cpu --pot poly --beta 0.5 --l 1 --omega2-liste 0.72,0.75 --h 0.01 --out aus-sp1-p1-kurve-l1
bash $K cpu sp1c3 bic2.py kurve --geraet cpu --pot poly --beta 0.5 --l 2 --abstand 0.05 --xmin 0.75 --xmax 0.84 --dx 0.01 --h 0.02 --out aus-sp1-c3-kurve-l2
bash $K cpu sp1c4 bic2.py kurve --geraet cpu --pot poly --beta 0.5 --l 2 --abstand 0.05 --xmin 0.85 --xmax 0.95 --dx 0.01 --h 0.02 --out aus-sp1-c4-kurve-l2
echo KETTE-SP1-A-ENDE $(date -Is)
