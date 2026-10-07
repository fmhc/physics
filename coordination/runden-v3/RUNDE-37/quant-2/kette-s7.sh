#!/bin/bash
# QUANT-2 Zusatz (Spur cpu7): Einschluss beta=1.42 mit kuerzerer Zeitrichtung (Nt=6, dann Nt=4), damit der
# Polyakov-Korrelator ueber r ~ 0,5 hinaus messbar wird. Ausserhalb des Kartenrahmens 8 bis 16 Zeitschichten.
set -u
D=/home/fmh/fmhc-physics-remote/quant-2
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
L=$D/lauf
cd $D
TAU=0.348006576329167
G=datei:$L/gwp.npz
df -h /home | tail -1
bash $K cpu7 q2-s6 code/qu2.py scan --gitter netz --L 3 --Nt 6 --tau $TAU --gew $G --betas 1.42 --start heiss --ntherm 200 --nmess 2400 --nbin 20 --nor 1 --zeitlimit 520 --seed 51 --out $L/s142-nt6 > $L/s142-nt6.log 2>&1
df -h /home | tail -1
bash $K cpu7 q2-s4 code/qu2.py scan --gitter netz --L 3 --Nt 4 --tau $TAU --gew $G --betas 1.42 --start heiss --ntherm 200 --nmess 2400 --nbin 20 --nor 1 --zeitlimit 400 --seed 61 --out $L/s142-nt4 > $L/s142-nt4.log 2>&1
echo "kette-s7 fertig $(date -u +%H:%M:%S)" > $L/kette-s7.txt
