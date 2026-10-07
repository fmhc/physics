#!/bin/bash
# S6 Hyperkubus 18^4 (T = T_c/3, Nt = 18 = 3 Nt_c), Gradient-Flow. Aufruf: run-s6-fh.sh SPUR NAME SEED "BETAS" NCFG [ZEITLIMIT]
D=/home/fmh/fmhc-physics-remote/quant-3
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
O=$D/lauf-s6
SPUR=$1; NAME=$2; SEED=$3; BETAS=$4; NCFG=$5; ZL=${6:-540}
bash $K $SPUR s6-$NAME $D/code/su2flow_s6.py lauf --gitter kubisch --L 18 --Nt 18 --ntherm 150 --mabst 20 --eps 0.02 --epsfrac 0.05 --epsmax 0.1 --tmax 8.0 --rec 1 --betas $BETAS --ncfg $NCFG --zeitlimit $ZL --seed $SEED --test --ttest 2.0 --out $O/$NAME > $O/$NAME.out 2>&1
