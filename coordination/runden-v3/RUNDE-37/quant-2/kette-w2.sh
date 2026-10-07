#!/bin/bash
# QUANT-2 Netz gewichtet (Potenz-Dual aus gw.py), Uebersicht L=2, Nt=8, kalt abwaerts (Spur cpu7, nach kette-w1).
set -u
D=/home/fmh/fmhc-physics-remote/quant-2
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
L=$D/lauf
cd $D
TAU=0.348006576329167
G=datei:$L/gwp.npz
BW="2.5 2.0 1.8 1.6 1.5 1.4 1.3 1.2 1.1 1.0 0.8 0.6"
df -h /home | tail -1
bash $K cpu7 q2-w2k code/qu2.py scan --gitter netz --L 2 --Nt 8 --tau $TAU --gew $G --betas $BW --start kalt --ntherm 100 --nmess 300 --nbin 20 --nor 1 --seed 7 --out $L/w2-kalt > $L/w2-kalt.log 2>&1
echo "kette-w2 fertig $(date -u +%H:%M:%S)" > $L/kette-w2.txt
