#!/bin/bash
# S6 Netz L=9, Nt=6, beta-Scan Teil 1 (heiss aufwaerts, kalt abwaerts)
D=/home/fmh/fmhc-physics-remote/quant-3
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
O=$D/lauf-s6
G=datei:$D/code/gwp.npz
T=0.348006576329167
bash $K p4000a s6-n1 $D/code/su2b.py lauf --gitter netz --L 9 --Nt 6 --tau $T --gew $G --betas 3.40:3.50:3.60:3.70 3.70:3.60:3.50:3.40 --starts heiss kalt --ntherm 120 --nmess 700 --nbin 20 --nor 2 --graph --zeitlimit 545 --seed 20261301 --out $O/n1-n9t6 > $O/n1.out 2>&1
