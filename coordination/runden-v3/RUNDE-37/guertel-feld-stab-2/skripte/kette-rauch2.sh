#!/bin/bash
# GUERTEL-FELD-STAB-2, Rauchlauf 2 (Spur cpu3): SO(2)-Referenz eps = 0 bei 20 Grad und geaenderte Auswertung.
R=/home/fmh/fmhc-physics-remote/guertel-feld-stab-2
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
S=$R/code/stab2.py
cd $R/rauch || exit 1
bash $K cpu3 gfs2-r11 $S stoss --aus $R/rauch --tag s2 --dim 2 --r0 12 --R 24 --zust $R/rauch/prot-s2-zust.npz --theta 20 --eps 0 --nmax 3000 > $R/rauch/r11.log 2>&1
bash $K cpu3 gfs2-r12 $R/code/auswertung.py --lauf $R/rauch --gfs1 $R/eingaben-gfs1 --aus $R/rauch --theta_a 20 --theta_ref 10 --tmax_b 20 > $R/rauch/r12.log 2>&1
touch $R/rauch/RAUCH2.fertig
