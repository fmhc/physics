#!/bin/bash
# GUERTEL-FELD-STAB-2, Hauptlaeufe Kette K3 (Spur cpu3), eingefrorener Code.
R=/home/fmh/fmhc-physics-remote/guertel-feld-stab-2
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
S=$R/code/stab2.py
L=$R/lauf
cd $L || exit 1
bash $K cpu3 gfs2-p16a $S prot --aus $L --tag g16a --r0 16 --R 32 --tmax 450 > $L/prot-g16a.log 2>&1
touch $L/p16a.fertig
for e in 0.01 0.1 0.3; do
  bash $K cpu3 gfs2-g16-T450-e$e $S stoss --aus $L --tag g16 --r0 16 --R 32 --zust $L/prot-g16a-zust.npz --theta 450 --eps $e > $L/stoss-g16-T450-e$e.log 2>&1
done
bash $K cpu3 gfs2-g16-T270 $S stoss --aus $L --tag g16 --r0 16 --R 32 --zust $L/prot-g16a-zust.npz --theta 270 --eps 0 > $L/stoss-g16-T270-e0.log 2>&1
touch $L/K3-haupt.fertig
# Zusatz (beschreibend): (16, 32) bei 420 Grad mit Referenz 300
bash $K cpu3 gfs2-g16-T300 $S stoss --aus $L --tag g16 --r0 16 --R 32 --zust $L/prot-g16a-zust.npz --theta 300 --eps 0 > $L/stoss-g16-T300-e0.log 2>&1
for e in 0.01 0.1 0.3; do
  bash $K cpu3 gfs2-g16-T420-e$e $S stoss --aus $L --tag g16 --r0 16 --R 32 --zust $L/prot-g16a-zust.npz --theta 420 --eps $e > $L/stoss-g16-T420-e$e.log 2>&1
done
touch $L/K3.fertig
