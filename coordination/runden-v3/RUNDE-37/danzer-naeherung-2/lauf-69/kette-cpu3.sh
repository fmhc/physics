#!/bin/bash
# DANZER-NAEHERUNG-2, Laufkette cpu3 (PLAN Abschnitt 5)
R=/home/fmh/fmhc-physics-remote/danzer-naeherung-2
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd $R
bash $K cpu3 dn2-L1 code/dn2.py rechnen 1/1 S,M 0,1,2,3,4,5,6,7 lauf/n11.json --probe --zitter-kontrolle > $R/lauf/L1.log 2>&1
bash $K cpu3 dn2-L2 code/dn2.py rechnen 2/1 S,M 0,1,2,3,4,5,6,7 lauf/n21.json --probe --zitter-kontrolle > $R/lauf/L2.log 2>&1
bash $K cpu3 dn2-L3b code/dn2.py rechnen 3/2 S,M 4,5,6,7 lauf/n32b.json > $R/lauf/L3b.log 2>&1
bash $K cpu3 dn2-L4b code/dn2.py rechnen 5/3 S,M 1 lauf/n53b.json > $R/lauf/L4b.log 2>&1
echo "kette cpu3 ende $(date --iso-8601=seconds)" > $R/lauf/kette-cpu3.fertig
