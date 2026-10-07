#!/bin/bash
# QBALL-DREIPOL-3, Leitungstest (vor dem Einfrieren): alle Modi mit fremden Werten (g4 = +0,1, grobe Gitter, wenige
# Schritte) und die Auswertung. Prueft nur, dass der Weg durchlaeuft, und misst die Laufzeit; keine Hauptwerte.
set -u
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
P=/home/fmh/fmhc-physics-remote/qball-dreipol-3/code
O=/home/fmh/fmhc-physics-remote/qball-dreipol-3/rauch/pipe
mkdir -p $O
cd /home/fmh/fmhc-physics-remote/qball-dreipol-3 || exit 1
bash $K p4000a dp3-pB3 $P/dreipol3.py bisekt --out $O/bisekt3.json --dim 3 --N 32 --L 48 --g4=0.1 --Q_hi 800 \
  --Q_abstieg 400 --n_bisekt 1 --nfluss 40 --nmax_ball 40 --wand_fluss 20 > $O/bisekt3.log 2>&1
echo "bisekt3 rc=$? $(date --iso-8601=seconds)" >> $O/pipe.log
bash $K p4000a dp3-pB2 $P/dreipol3.py bisekt --out $O/bisekt2.json --dim 2 --N 64 --L 64 --g4=0.1 --Q_hi 25 \
  --Q_abstieg 20 --n_bisekt 1 --nfluss 40 --nmax_ball 40 --tol 1e-7 --tol_ball 1e-8 --wand_fluss 20 \
  > $O/bisekt2.log 2>&1
echo "bisekt2 rc=$? $(date --iso-8601=seconds)" >> $O/pipe.log
bash $K p4000a dp3-pS3 $P/dreipol3.py stab3 --out $O/stab3.json --N 32 --L 48 --g4=0.1 --Q1 300 --nfluss 40 \
  --nmax_ball 40 --nmax_ref 40 --nmax_st 20 --wand_st 10 > $O/stab3.log 2>&1
echo "stab3 rc=$? $(date --iso-8601=seconds)" >> $O/pipe.log
bash $K p4000a dp3-paw $P/auswertung3.py $O > $O/aw.log 2>&1
echo "aw rc=$? $(date --iso-8601=seconds)" >> $O/pipe.log
