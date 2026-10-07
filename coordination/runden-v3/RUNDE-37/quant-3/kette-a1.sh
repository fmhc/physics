#!/bin/bash
# QUANT-3 Kontrolle kubisch (Spur p4000a): 8^3x4 und 12^3x4, je 16 beta, heisse Starts; Plakette, |L|, chi_L (S1).
set -u
D=/home/fmh/fmhc-physics-remote/quant-3
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
L=$D/lauf
cd $D
pruef() { F=$(df --output=avail -BG /home | tail -1 | tr -dc 0-9); echo "df frei ${F}G $(date -u +%H:%M:%S)"; [ "$F" -ge 10 ] || exit 9; }
BK="2.20 2.24 2.26 2.27 2.28 2.29 2.295 2.30 2.305 2.31 2.32 2.33 2.34 2.36 2.40 2.50"
pruef
bash $K p4000a q3-k8 code/su2.py lauf --gitter kubisch --L 8 --Nt 4 --betas $BK --starts heiss --ntherm 1000 --nmess 40000 --nbin 50 --nor 2 --graph --zeitlimit 300 --out $L/k8 > $L/k8.log 2>&1
pruef
bash $K p4000a q3-k12 code/su2.py lauf --gitter kubisch --L 12 --Nt 4 --betas $BK --starts heiss --ntherm 1000 --nmess 40000 --nbin 50 --nor 2 --graph --zeitlimit 300 --seed 12 --out $L/k12 > $L/k12.log 2>&1
echo "kette-a1 fertig $(date -u +%H:%M:%S)" > $L/kette-a1.txt
