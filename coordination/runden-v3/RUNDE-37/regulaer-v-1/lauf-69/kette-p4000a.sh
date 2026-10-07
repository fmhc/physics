#!/bin/bash
# REGULAER-V-1, Laufkette p4000a (PLAN Abschnitt 10): H1, H3, H4
R=/home/fmh/fmhc-physics-remote/regulaer-v-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd $R
bash $K p4000a rv-H1 code/rv.py lp 1 lauf/lp1.json > $R/lauf/H1.log 2>&1
bash $K p4000a rv-H3 code/rv.py kontrollen lauf/kontrollen.json > $R/lauf/H3.log 2>&1
bash $K p4000a rv-H4 code/rv.py kammer 1 lauf/kammer1.json > $R/lauf/H4.log 2>&1
echo "kette p4000a ende $(date --iso-8601=seconds)" > $R/lauf/kette-p4000a.fertig
