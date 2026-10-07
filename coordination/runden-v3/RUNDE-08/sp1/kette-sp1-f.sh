#!/bin/bash
# SP-1 (Runde 8), Kette F auf Spur cpu2: kurve l = 1 unterhalb 0,58 (Vorhersage n = 5 bei 0,57609 +- 0,0003,
# PLAN.md Nachtrag 07:14:50). Einmalig vom Code-Agenten gestartet.
B=/home/fmh/fmhc-physics-remote/runde7-bic2; K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh; cd $B || exit 1
echo KETTE-SP1-F-START $(date -Is)
bash $K cpu2 sp1b5 bic2.py kurve --geraet cpu --pot poly --beta 0.5 --l 1 --abstand 0.05 --xmin 0.565 --xmax 0.585 --dx 0.005 --h 0.02 --n-wechsel-fein 1 --out aus-sp1-b5-kurve-l1-tief
echo KETTE-SP1-F-ENDE $(date -Is)
