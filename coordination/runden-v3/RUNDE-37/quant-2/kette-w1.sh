#!/bin/bash
# QUANT-2 Netz gewichtet (Potenz-Dual aus gw.py), Uebersicht L=2, Nt=8, heiss aufwaerts (Spur cpu7).
set -u
D=/home/fmh/fmhc-physics-remote/quant-2
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
L=$D/lauf
cd $D
TAU=0.348006576329167
G=datei:$L/gwp.npz
BW="0.6 0.8 1.0 1.1 1.2 1.3 1.4 1.5 1.6 1.8 2.0 2.5"
df -h /home | tail -1
bash $K cpu7 q2-w1h code/qu2.py scan --gitter netz --L 2 --Nt 8 --tau $TAU --gew $G --betas $BW --start heiss --ntherm 100 --nmess 300 --nbin 20 --nor 1 --out $L/w1-heiss > $L/w1-heiss.log 2>&1
echo "kette-w1 fertig $(date -u +%H:%M:%S)" > $L/kette-w1.txt
