#!/bin/bash
# QBALL-DREIPOL-3, Nachtrag N2 nach Sicht (beschreibend): Teil B mit laengeren Wandzeiten (Referenz 150 s, je Stoerung
# 150 s), eingefrorener Code dreipol3.py, nur andere Argumente. Anlass: Im Hauptlauf endeten die Stoerungsfluesse an
# der Wandzeit 60 s vor dem Residuum 1e-8. Laeuft auf der .69. Aufruf: laeufe-nachtrag2.sh <spur> <liste> <name>
set -u
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
P=/home/fmh/fmhc-physics-remote/qball-dreipol-3/code
O=/home/fmh/fmhc-physics-remote/qball-dreipol-3/lauf/nachtrag
mkdir -p $O
cd /home/fmh/fmhc-physics-remote/qball-dreipol-3 || exit 1
bash $K $1 dp3-N2-$3 $P/dreipol3.py stab3 --out $O/stab3_$3.json --N 80 --L 48 --g4=-0.1 --Q1 800 --tol 1e-6 \
  --tol_ball 1e-6 --nmax_ball 20000 --wand_ball 90 --nfluss 60000 --wand_fluss 75 --tol_ref 1e-9 --nmax_ref 40000 \
  --wand_ref 150 --tol_st 1e-8 --nmax_st 60000 --wand_st 150 --amp_v 0.15 --amp_l 0.05 --liste $2 \
  --zeitgrenze 400 > $O/stab3_$3.log 2>&1
echo "stab3_$3 rc=$? $(date --iso-8601=seconds)" >> $O/laeufe-nachtrag.log
