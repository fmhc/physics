#!/bin/bash
# S6 Netz L=8, Nt=6 (Ausweichgroesse laut VORAB-S6 Abschnitt 1.A, weil L=9 an Zeit/Speicher scheiterte), beta-Scan in zwei Teilen
D=/home/fmh/fmhc-physics-remote/quant-3
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
O=$D/lauf-s6
G=datei:$D/code/gwp.npz
T=0.348006576329167
bash $K p4000a s6-n2a $D/code/su2b_s6.py lauf --gitter netz --L 8 --Nt 6 --tau $T --gew $G --betas 3.40:3.50:3.60 3.60:3.50:3.40 --starts heiss kalt --ntherm 120 --nmess 400 --nbin 20 --nor 2 --graph --zeitlimit 560 --seed 20261401 --out $O/n2a-n8t6 > $O/n2a.out 2>&1 &
bash $K p4000b s6-n2b $D/code/su2b_s6.py lauf --gitter netz --L 8 --Nt 6 --tau $T --gew $G --betas 3.45:3.55:3.65 3.65:3.55:3.45 --starts heiss kalt --ntherm 120 --nmess 400 --nbin 20 --nor 2 --graph --zeitlimit 560 --seed 20261402 --out $O/n2b-n8t6 > $O/n2b.out 2>&1 &
wait
