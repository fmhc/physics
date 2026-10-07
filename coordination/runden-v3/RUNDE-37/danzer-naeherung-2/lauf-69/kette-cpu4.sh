#!/bin/bash
# DANZER-NAEHERUNG-2, Laufkette cpu4 (PLAN Abschnitt 5)
R=/home/fmh/fmhc-physics-remote/danzer-naeherung-2
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd $R
bash $K cpu4 dn2-L3a code/dn2.py rechnen 3/2 S,M 0,1,2,3 lauf/n32a.json --probe --zitter-kontrolle > $R/lauf/L3a.log 2>&1
bash $K cpu4 dn2-L4a code/dn2.py rechnen 5/3 S,M 0 lauf/n53a.json > $R/lauf/L4a.log 2>&1
echo "kette cpu4 ende $(date --iso-8601=seconds)" > $R/lauf/kette-cpu4.fertig
