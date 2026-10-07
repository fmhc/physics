#!/bin/bash
D=/home/fmh/fmhc-physics-remote/quant-3
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
G=datei:$D/code/gwp.npz
T=0.348006576329167
C="$D/code/su2flow.py lauf --gitter netz --L 6 --Nt 12 --tau $T --gew $G --betas 3.29 --ncfg 2 --mabst 20 --ntherm 100 --test --zeitlimit 450"
bash $K p4000a s5-pil-met $C --metrik --eps 0.0005 --epsfrac 0.02 --epsmax 0.03 --tmax 1.0 --ttest 0.1 --out $D/lauf-s5/pilot-nm > $D/lauf-s5/pilot-nm.out 2>&1 &
bash $K p4000b s5-pil-nai $C --volcheck --eps 0.02 --epsfrac 0.05 --epsmax 0.3 --tmax 20 --ttest 1.0 --out $D/lauf-s5/pilot-nn > $D/lauf-s5/pilot-nn.out 2>&1 &
wait
