#!/bin/bash
D=/home/fmh/fmhc-physics-remote/quant-3
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
O=$D/lauf-s6
G=datei:$D/code/gwp.npz
T=0.348006576329167
bash $K p4000b s6-pn3 $D/code/su2b_s6.py lauf --gitter netz --L 8 --Nt 6 --tau $T --gew $G --betas 3.50:3.55 3.55:3.50 --starts heiss kalt --ntherm 20 --nmess 40 --nbin 4 --nor 2 --graph --zeitlimit 200 --out $O/pilot-n3 > $O/pilot-n3.out 2>&1
