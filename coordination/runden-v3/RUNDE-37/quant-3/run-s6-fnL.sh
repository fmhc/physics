#!/bin/bash
# S6 Netz L (Umgebungsvariable L, Standard 6), Nt=18, Gradient-Flow. Aufruf wie run-s6-fn.sh
D=/home/fmh/fmhc-physics-remote/quant-3
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
O=$D/lauf-s6
G=datei:$D/code/gwp.npz
T=0.348006576329167
L=${L:-6}; SPUR=$1; NAME=$2; SEED=$3; BETAS=$4; NCFG=$5; TMAX=$6; ZL=${7:-540}; TT=${8:-2.0}
bash $K $SPUR s6-$NAME $D/code/su2flow_s6.py lauf --gitter netz --L $L --Nt 18 --tau $T --gew $G --ntherm 150 --mabst 20 --eps 0.02 --epsfrac 0.05 --epsmax 0.15 --tmax $TMAX --rec 2 --betas $BETAS --ncfg $NCFG --zeitlimit $ZL --seed $SEED --test --ttest $TT --out $O/$NAME > $O/$NAME.out 2>&1
