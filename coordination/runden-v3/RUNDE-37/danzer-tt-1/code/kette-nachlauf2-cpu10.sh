#!/bin/bash
# DANZER-TT-1, Nachlauf 2 cpu10: L24c (3/2 Saat 4, Richtungen 0-6, |k| = 2e-3) nach dem Ende der Kette cpu10.
R=/home/fmh/fmhc-physics-remote/danzer-tt-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd $R
until [ -f $R/lauf/kette-cpu10.fertig ]; do sleep 10; done
bash $K cpu10 dtt-L24c code/dtt.py netz --ordnung 3/2 --saaten 4 --ridx 0-6 --eps 2e-3 --out lauf/n32-s4-c.json > $R/lauf/L24c.log 2>&1
echo "L24c rc=$? $(date --iso-8601=seconds)" >> $R/lauf/kette-nachlauf2-cpu10.log
