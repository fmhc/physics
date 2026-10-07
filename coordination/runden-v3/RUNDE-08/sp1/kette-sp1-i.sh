#!/bin/bash
# SP-1 (Runde 8), Kette I auf Spur cpu2: kurve l = 1 fein 0,574 bis 0,578 (zweiter Vorzeichenwechsel aus Lauf b5
# zwischen 0,575 und 0,58 wurde nicht verfeinert; Vorhersage n = 5: 0,57609 +- 0,0003). Einmalig vom Code-Agenten gestartet.
B=/home/fmh/fmhc-physics-remote/runde7-bic2; K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh; cd $B || exit 1
echo KETTE-SP1-I-START $(date -Is)
bash $K cpu2 sp1b6 bic2.py kurve --geraet cpu --pot poly --beta 0.5 --l 1 --abstand 0.05 --xmin 0.574 --xmax 0.579 --dx 0.001 --h 0.02 --out aus-sp1-b6-kurve-l1-n5
echo KETTE-SP1-I-ENDE $(date -Is)
