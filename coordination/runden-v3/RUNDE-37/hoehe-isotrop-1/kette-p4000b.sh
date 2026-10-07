#!/bin/bash
# HOEHE-ISOTROP-1, Laufkette p4000b (PLAN Abschnitt 10): H2 proben, H4 strahlen 1, H6 gitter, H7 l2
R=/home/fmh/fmhc-physics-remote/hoehe-isotrop-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd $R
bash $K p4000b hi-H2 code/hi.py proben lauf/proben.json alt/kammer1.json > $R/lauf/H2.log 2>&1
bash $K p4000b hi-H4 code/hi.py strahlen 1 lauf/f43-1.json > $R/lauf/H4.log 2>&1
bash $K p4000b hi-H6 code/hi.py gitter lauf/gitter.json > $R/lauf/H6.log 2>&1
bash $K p4000b hi-H7 code/hi.py l2 lauf/l2.json 4 > $R/lauf/H7.log 2>&1
echo "kette p4000b ende $(date --iso-8601=seconds)" > $R/lauf/kette-p4000b.fertig
