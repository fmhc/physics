#!/bin/bash
D=/home/fmh/fmhc-physics-remote/quant-3
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
O=$D/lauf-s6
G=datei:$D/code/gwp.npz
T=0.348006576329167
bash $K p4000a s6-pn2 $D/code/su2flow_s6.py lauf --gitter netz --L 6 --Nt 18 --tau $T --gew $G --ntherm 60 --mabst 20 --eps 0.02 --epsfrac 0.05 --epsmax 0.1 --tmax 30 --rec 2 --betas 3.55 --ncfg 2 --zeitlimit 300 --test --ttest 2.0 --seed 20261101 --out $O/pilot-n2 > $O/pilot-n2.out 2>&1
