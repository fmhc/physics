#!/bin/bash
# QBALL-DREIPOL-3, Laufzeitprobe (vor dem Einfrieren) in Hauptgroesse mit fremdem g4 = +0,1: Zeit je Flussschritt
# (mit Beobachter) bei 3D N = 80 und 2D N = 256, Stoerungsfluss 3D. Keine Hauptwerte.
set -u
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
P=/home/fmh/fmhc-physics-remote/qball-dreipol-3/code
O=/home/fmh/fmhc-physics-remote/qball-dreipol-3/rauch/zeit
mkdir -p $O
cd /home/fmh/fmhc-physics-remote/qball-dreipol-3 || exit 1
bash $K p4000a dp3-zB3 $P/dreipol3.py bisekt --out $O/bisekt3.json --dim 3 --N 80 --L 48 --g4=0.1 --Q_hi 800 \
  --Q_abstieg 400 --n_bisekt 0 --nfluss 1000 --tol 1e-30 > $O/bisekt3.log 2>&1
echo "bisekt3 rc=$? $(date --iso-8601=seconds)" >> $O/zeit.log
bash $K p4000a dp3-zB2 $P/dreipol3.py bisekt --out $O/bisekt2.json --dim 2 --N 256 --L 64 --g4=0.1 --Q_hi 25 \
  --Q_abstieg 20 --n_bisekt 0 --nfluss 3000 --tol 1e-30 --tol_ball 1e-8 --nmax_ball 6000 --wand_ball 120 \
  > $O/bisekt2.log 2>&1
echo "bisekt2 rc=$? $(date --iso-8601=seconds)" >> $O/zeit.log
bash $K p4000a dp3-zS3 $P/dreipol3.py stab3 --out $O/stab3.json --N 80 --L 48 --g4=0.1 --Q1 800 --nfluss 300 \
  --nmax_ref 300 --nmax_st 1000 --tol_st 1e-30 --liste V1,R20 > $O/stab3.log 2>&1
echo "stab3 rc=$? $(date --iso-8601=seconds)" >> $O/zeit.log
