#!/bin/bash
# HOEHE-ISOTROP-1, Rauch-Pfadtests Spur p4000b (PLAN Abschnitt 11): R5 proben --rauch, R6 strahlen 0 --rauch, R7 l2 0
R=/home/fmh/fmhc-physics-remote/hoehe-isotrop-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd $R
bash $K p4000b hi-R5 code/hi.py proben rauch/r5-proben.json alt/kammer1.json --rauch > $R/rauch/R5.log 2>&1
bash $K p4000b hi-R6 code/hi.py strahlen 0 rauch/r6-f43.json --rauch > $R/rauch/R6.log 2>&1
bash $K p4000b hi-R7 code/hi.py l2 rauch/r7-l2.json 0 > $R/rauch/R7.log 2>&1
echo "kette b ende $(date --iso-8601=seconds)" > $R/rauch/kette-b.fertig
