#!/bin/bash
# QUANT-2 Netz gewichtet, Feinscan L=3, Nt=8, heiss aufwaerts (Spur cpu).
set -u
D=/home/fmh/fmhc-physics-remote/quant-2
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
L=$D/lauf
cd $D
TAU=0.348006576329167
G=datei:$L/gwp.npz
BF="1.30 1.35 1.40 1.42 1.44 1.46 1.48 1.50 1.55 1.60 1.70"
df -h /home | tail -1
bash $K cpu q2-f3h code/qu2.py scan --gitter netz --L 3 --Nt 8 --tau $TAU --gew $G --betas $BF --start heiss --ntherm 60 --nmess 160 --nbin 16 --nor 1 --out $L/f3-heiss > $L/f3-heiss.log 2>&1
echo "kette-f3h fertig $(date -u +%H:%M:%S)" > $L/kette-f3h.txt
