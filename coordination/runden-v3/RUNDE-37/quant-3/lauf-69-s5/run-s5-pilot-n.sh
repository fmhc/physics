#!/bin/bash
D=/home/fmh/fmhc-physics-remote/quant-3
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
G=datei:$D/code/gwp.npz
T=0.348006576329167
bash $K p4000b s5-pilot-n $D/code/su2flow.py lauf --gitter netz --L 6 --Nt 12 --tau $T --gew $G --betas 3.29 --ncfg 2 --mabst 20 --ntherm 100 --eps 0.01 --tmax 0.2 --test --volcheck --zeitlimit 400 --out $D/lauf-s5/pilot-n > $D/lauf-s5/pilot-n.out 2>&1
