#!/bin/bash
# GUERTEL-FELD-STAB-2, Rauchlauf (Spur cpu3). Nur Winkel <= 20 Grad.
R=/home/fmh/fmhc-physics-remote/guertel-feld-stab-2
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
S=$R/code/stab2.py
cd $R/rauch || exit 1
bash $K cpu3 gfs2-r1 $S prot --aus $R/rauch --tag g8 --r0 8 --R 16 --tmax 20 --speicher 10,20 > $R/rauch/r1.log 2>&1
bash $K cpu3 gfs2-r2 $S prot --aus $R/rauch --tag g8s1 --r0 8 --R 16 --tmax 10 --speicher "" > $R/rauch/r2.log 2>&1
bash $K cpu3 gfs2-r3 $S prot --aus $R/rauch --tag g8s2 --r0 8 --R 16 --tmin 10 --tmax 20 --von $R/rauch/prot-g8s1-ck.npz --speicher "" > $R/rauch/r3.log 2>&1
bash $K cpu3 gfs2-r4 $S prot --aus $R/rauch --tag g12 --r0 12 --R 24 --tmax 20 --speicher 10,20 > $R/rauch/r4.log 2>&1
bash $K cpu3 gfs2-r5 $S prot --aus $R/rauch --tag g16a --r0 16 --R 32 --tmax 20 --speicher 10,20 > $R/rauch/r5.log 2>&1
bash $K cpu3 gfs2-r6 $S stoss --aus $R/rauch --tag g16 --r0 16 --R 32 --zust $R/rauch/prot-g16a-zust.npz --theta 20 --eps 0.3 --nmax 100 > $R/rauch/r6.log 2>&1
bash $K cpu3 gfs2-r7 $S stoss --aus $R/rauch --tag g16 --r0 16 --R 32 --zust $R/rauch/prot-g16a-zust.npz --theta 10 --eps 0 --nmax 60 > $R/rauch/r7.log 2>&1
bash $K cpu3 gfs2-r8 $S prot --aus $R/rauch --tag s2 --dim 2 --r0 12 --R 24 --tmax 20 --speicher 10,20 > $R/rauch/r8.log 2>&1
bash $K cpu3 gfs2-r9 $S stoss --aus $R/rauch --tag s2 --dim 2 --r0 12 --R 24 --zust $R/rauch/prot-s2-zust.npz --theta 20 --eps 0.3 --nmax 100 > $R/rauch/r9.log 2>&1
bash $K cpu3 gfs2-r10 $R/code/auswertung.py --lauf $R/rauch --gfs1 $R/eingaben-gfs1 --aus $R/rauch --theta_a 20 --theta_ref 10 --tmax_b 20 > $R/rauch/r10.log 2>&1
touch $R/rauch/RAUCH.fertig
