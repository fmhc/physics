#!/bin/bash
# REGULAER-V-1, Laufkette p4000b (PLAN Abschnitt 10): H2, H5
R=/home/fmh/fmhc-physics-remote/regulaer-v-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd $R
bash $K p4000b rv-H2 code/rv.py lp 2 lauf/lp2.json > $R/lauf/H2.log 2>&1
bash $K p4000b rv-H5 code/rv.py kammer 2 lauf/kammer2.json > $R/lauf/H5.log 2>&1
echo "kette p4000b ende $(date --iso-8601=seconds)" > $R/lauf/kette-p4000b.fertig
