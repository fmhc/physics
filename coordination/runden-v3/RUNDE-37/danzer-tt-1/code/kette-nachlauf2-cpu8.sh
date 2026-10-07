#!/bin/bash
# DANZER-TT-1, Nachlauf 2 cpu8: L24b (3/2 Saat 4, Richtungen 7-12, |k| = 1e-3) nach dem Ende der Kette cpu8.
R=/home/fmh/fmhc-physics-remote/danzer-tt-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd $R
until [ -f $R/lauf/kette-cpu8.fertig ]; do sleep 10; done
bash $K cpu8 dtt-L24b code/dtt.py netz --ordnung 3/2 --saaten 4 --ridx 7-12 --eps 1e-3 --out lauf/n32-s4-b.json > $R/lauf/L24b.log 2>&1
echo "L24b rc=$? $(date --iso-8601=seconds)" >> $R/lauf/kette-nachlauf2-cpu8.log
