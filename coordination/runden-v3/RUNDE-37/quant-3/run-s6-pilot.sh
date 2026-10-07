#!/bin/bash
# S6 Pilot (technisch): Speicher und Zeit. Ergebnisse gehen nicht in die Auswertung.
D=/home/fmh/fmhc-physics-remote/quant-3
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
O=$D/lauf-s6
G=datei:$D/code/gwp.npz
T=0.348006576329167
bash $K p4000b s6-pk $D/code/su2b.py lauf --gitter kubisch --L 18 --Nt 6 --betas 2.40:2.44 2.44:2.40 --starts heiss kalt --ntherm 30 --nmess 60 --nbin 6 --nor 2 --graph --zeitlimit 200 --out $O/pilot-k > $O/pilot-k.out 2>&1 &
bash $K p4000a s6-pn $D/code/su2flow.py lauf --gitter netz --L 6 --Nt 18 --tau $T --gew $G --ntherm 60 --mabst 20 --eps 0.02 --epsfrac 0.05 --epsmax 0.1 --tmax 30 --rec 2 --betas 3.55 --ncfg 2 --zeitlimit 300 --test --ttest 2.0 --seed 20261101 --out $O/pilot-n > $O/pilot-n.out 2>&1 &
wait
