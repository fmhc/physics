#!/bin/bash
# QBALL-DREIPOL-3, Hauptlauf Spur p4000a (eingefrorener Code; PLAN.md Abschnitt 7): 3D-Bisektion. Laeuft auf der .69.
set -u
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
P=/home/fmh/fmhc-physics-remote/qball-dreipol-3/code
O=/home/fmh/fmhc-physics-remote/qball-dreipol-3/lauf
cd /home/fmh/fmhc-physics-remote/qball-dreipol-3 || exit 1
bash $K p4000a dp3-B3 $P/dreipol3.py bisekt --out $O/bisekt3.json --dim 3 --N 80 --L 48 --g4=-0.1 --Q_hi 800 \
  --Q_abstieg 400 --n_bisekt 6 --tol 1e-6 --tol_ball 1e-6 --nmax_ball 20000 --wand_ball 90 --nfluss 60000 \
  --wand_fluss 75 --beta 1.5 --zeitgrenze 330 > $O/bisekt3.log 2>&1
echo "bisekt3 rc=$? $(date --iso-8601=seconds)" >> $O/laeufe-p4000a.log
