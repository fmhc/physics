#!/bin/bash
# QBALL-DREIPOL-3, Hauptlaeufe Spur p4000b (eingefrorener Code; PLAN.md Abschnitt 7): 2D-Bisektion, dann Teil B
# (Stoerungen des 3D-Tropfens bei Q1 = 800). Laeuft auf der .69.
set -u
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
P=/home/fmh/fmhc-physics-remote/qball-dreipol-3/code
O=/home/fmh/fmhc-physics-remote/qball-dreipol-3/lauf
cd /home/fmh/fmhc-physics-remote/qball-dreipol-3 || exit 1
bash $K p4000b dp3-B2 $P/dreipol3.py bisekt --out $O/bisekt2.json --dim 2 --N 256 --L 64 --g4=-0.1 --Q_hi 60 \
  --Q_abstieg 30,20,15 --n_bisekt 6 --tol 1e-7 --tol_ball 1e-8 --nmax_ball 6000 --wand_ball 120 --nfluss 60000 \
  --wand_fluss 45 --beta 1.5 --zeitgrenze 330 > $O/bisekt2.log 2>&1
echo "bisekt2 rc=$? $(date --iso-8601=seconds)" >> $O/laeufe-p4000b.log
bash $K p4000b dp3-S3 $P/dreipol3.py stab3 --out $O/stab3.json --N 80 --L 48 --g4=-0.1 --Q1 800 --tol 1e-6 \
  --tol_ball 1e-6 --nmax_ball 20000 --wand_ball 90 --nfluss 60000 --wand_fluss 75 --tol_ref 1e-9 --nmax_ref 20000 \
  --wand_ref 90 --tol_st 1e-8 --nmax_st 30000 --wand_st 60 --amp_v 0.15 --amp_l 0.05 \
  --liste V1,V2,L1,L2,P1,P2,Z1,R5,R20 --zeitgrenze 420 > $O/stab3.log 2>&1
echo "stab3 rc=$? $(date --iso-8601=seconds)" >> $O/laeufe-p4000b.log
