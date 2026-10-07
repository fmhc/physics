#!/bin/bash
# S6 Hyperkubus 18^3 x 6, beta-Scan Teil 1 (heiss aufwaerts, kalt abwaerts)
D=/home/fmh/fmhc-physics-remote/quant-3
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
O=$D/lauf-s6
bash $K p4000b s6-h1 $D/code/su2b.py lauf --gitter kubisch --L 18 --Nt 6 --betas 2.38:2.42:2.44:2.48 2.48:2.44:2.42:2.38 --starts heiss kalt --ntherm 150 --nmess 1000 --nbin 20 --nor 2 --graph --zeitlimit 540 --seed 20261201 --out $O/h1-k18t6 > $O/h1.out 2>&1
