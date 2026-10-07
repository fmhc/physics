#!/bin/bash
# QUANT-2 Produktion (Spur cpu7): Rauchprobe Multihit-Fassung, dann Einschluss beta=1.30 (heiss) und Coulomb beta=2.0 (kalt).
set -u
D=/home/fmh/fmhc-physics-remote/quant-2
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
L=$D/lauf
cd $D
TAU=0.348006576329167
G=datei:$L/gwp.npz
df -h /home | tail -1
bash $K cpu7 q2-r5 code/qu2.py scan --gitter netz --L 2 --Nt 8 --tau $TAU --gew $G --betas 1.3 --start heiss --ntherm 5 --nmess 40 --nbin 4 --nor 1 --out $L/r5 > $L/r5.log 2>&1 || exit 1
bash $K cpu7 q2-r5a code/qu2.py auswertung --ein $L/r5 --out $L/r5-aus.json > $L/r5-aus.log 2>&1 || exit 1
df -h /home | tail -1
bash $K cpu7 q2-p130 code/qu2.py scan --gitter netz --L 3 --Nt 8 --tau $TAU --gew $G --betas 1.30 --start heiss --ntherm 200 --nmess 2400 --nbin 20 --nor 1 --zeitlimit 520 --out $L/p130 > $L/p130.log 2>&1
df -h /home | tail -1
bash $K cpu7 q2-p200 code/qu2.py scan --gitter netz --L 3 --Nt 8 --tau $TAU --gew $G --betas 2.0 --start kalt --ntherm 200 --nmess 2400 --nbin 20 --nor 1 --zeitlimit 520 --seed 11 --out $L/p200 > $L/p200.log 2>&1
echo "kette-p7 fertig $(date -u +%H:%M:%S)" > $L/kette-p7.txt
