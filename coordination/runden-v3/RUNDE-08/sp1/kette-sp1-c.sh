#!/bin/bash
# SP-1 (Runde 8), Kette C auf Spur cpu: (d) exakt an den gefundenen Stellen. Einmalig vom Code-Agenten gestartet.
# l = 1, n = 2: kurve (b2, h = 0,02) Vorzeichenwechsel bei 0,66027975, rho 1,71730131; h = 0,01 etwas hoeher erwartet.
B=/home/fmh/fmhc-physics-remote/runde7-bic2; K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh; cd $B || exit 1
echo KETTE-SP1-C-START $(date -Is)
bash $K cpu sp1d12 bic2.py exakt --geraet cpu --pot poly --beta 0.5 --l 1 --h 0.01 --x0 0.660282 --rho0 1.717304 --drho 1.41 --cgam 12 --offsets 0,2e-5,-2e-5,1e-4,-1e-4,3e-4,-3e-4,5e-4,-5e-4 --reserve 150 --out aus-sp1-d-exakt-l1-0660
echo KETTE-SP1-C-ENDE $(date -Is)
