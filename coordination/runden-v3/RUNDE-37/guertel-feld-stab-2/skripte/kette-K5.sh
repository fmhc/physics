#!/bin/bash
# GUERTEL-FELD-STAB-2, Hauptlaeufe Kette K5 (Spur cpu5), eingefrorener Code.
R=/home/fmh/fmhc-physics-remote/guertel-feld-stab-2
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
S=$R/code/stab2.py
L=$R/lauf
cd $L || exit 1
bash $K cpu5 gfs2-p8 $S prot --aus $L --tag g8 --r0 8 --R 16 --tmax 720 > $L/prot-g8.log 2>&1
bash $K cpu5 gfs2-p12 $S prot --aus $L --tag g12 --r0 12 --R 24 --tmax 720 > $L/prot-g12.log 2>&1
bash $K cpu5 gfs2-ps2 $S prot --aus $L --tag s2 --dim 2 --r0 12 --R 24 --tmax 450 > $L/prot-s2.log 2>&1
for e in 0 0.01 0.1 0.3; do
  bash $K cpu5 gfs2-s2-T450-e$e $S stoss --aus $L --tag s2 --dim 2 --r0 12 --R 24 --zust $L/prot-s2-zust.npz --theta 450 --eps $e > $L/stoss-s2-T450-e$e.log 2>&1
done
for e in 0.01 0.1 0.3; do
  bash $K cpu5 gfs2-g8-T450-e$e $S stoss --aus $L --tag g8 --r0 8 --R 16 --zust $L/prot-g8-zust.npz --theta 450 --eps $e > $L/stoss-g8-T450-e$e.log 2>&1
done
bash $K cpu5 gfs2-g8-T270 $S stoss --aus $L --tag g8 --r0 8 --R 16 --zust $L/prot-g8-zust.npz --theta 270 --eps 0 > $L/stoss-g8-T270-e0.log 2>&1
for e in 0.01 0.1 0.3; do
  bash $K cpu5 gfs2-g12-T450-e$e $S stoss --aus $L --tag g12 --r0 12 --R 24 --zust $L/prot-g12-zust.npz --theta 450 --eps $e > $L/stoss-g12-T450-e$e.log 2>&1
done
bash $K cpu5 gfs2-g12-T270 $S stoss --aus $L --tag g12 --r0 12 --R 24 --zust $L/prot-g12-zust.npz --theta 270 --eps 0 > $L/stoss-g12-T270-e0.log 2>&1
while [ ! -f $L/p16a.fertig ]; do sleep 10; done
bash $K cpu5 gfs2-p16b $S prot --aus $L --tag g16b --r0 16 --R 32 --tmin 450 --tmax 720 --von $L/prot-g16a-ck.npz --speicher "" > $L/prot-g16b.log 2>&1
touch $L/K5.fertig
while [ ! -f $L/K3.fertig ]; do sleep 10; done
bash $K cpu5 gfs2-ausw $R/code/auswertung.py --lauf $L --gfs1 $R/eingaben-gfs1 --aus $L > $L/ausw.log 2>&1
touch $L/ALLES.fertig
