#!/bin/bash
# S6 Hyperkubus 18^3 x 6, beta-Scan Teil 2
D=/home/fmh/fmhc-physics-remote/quant-3
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
O=$D/lauf-s6
bash $K p4000b s6-h2 $D/code/su2b_s6.py lauf --gitter kubisch --L 18 --Nt 6 --betas 2.40:2.43:2.46 2.46:2.43:2.40 --starts heiss kalt --ntherm 150 --nmess 1200 --nbin 20 --nor 2 --graph --zeitlimit 540 --seed 20261202 --out $O/h2-k18t6 > $O/h2.out 2>&1
