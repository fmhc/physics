#!/bin/bash
# S6 Netz L=8, Nt=6, beta-Scan Teil 3 (Spitze lag unter 3,40)
D=/home/fmh/fmhc-physics-remote/quant-3
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
O=$D/lauf-s6
G=datei:$D/code/gwp.npz
T=0.348006576329167
bash $K p4000a s6-n3 $D/code/su2b_s6.py lauf --gitter netz --L 8 --Nt 6 --tau $T --gew $G --betas 3.30:3.35:3.375 3.375:3.35:3.30 --starts heiss kalt --ntherm 120 --nmess 400 --nbin 20 --nor 2 --graph --zeitlimit 560 --seed 20261403 --out $O/n3-n8t6 > $O/n3.out 2>&1
