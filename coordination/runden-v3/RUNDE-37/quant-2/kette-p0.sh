#!/bin/bash
# QUANT-2 Produktion (Spur cpu): Einschluss beta=1.42 (heiss), Coulomb beta=1.6 (kalt), dann Feinscan L=3 kalt abwaerts.
set -u
D=/home/fmh/fmhc-physics-remote/quant-2
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
L=$D/lauf
cd $D
TAU=0.348006576329167
G=datei:$L/gwp.npz
until [ -f $L/r5-aus.json ] || [ -f $L/kette-p7.txt ]; do sleep 5; done
[ -f $L/r5-aus.json ] || exit 1
df -h /home | tail -1
bash $K cpu q2-p142 code/qu2.py scan --gitter netz --L 3 --Nt 8 --tau $TAU --gew $G --betas 1.42 --start heiss --ntherm 200 --nmess 2400 --nbin 20 --nor 1 --zeitlimit 520 --seed 21 --out $L/p142 > $L/p142.log 2>&1
df -h /home | tail -1
bash $K cpu q2-p160 code/qu2.py scan --gitter netz --L 3 --Nt 8 --tau $TAU --gew $G --betas 1.6 --start kalt --ntherm 200 --nmess 2400 --nbin 20 --nor 1 --zeitlimit 520 --seed 31 --out $L/p160 > $L/p160.log 2>&1
df -h /home | tail -1
bash $K cpu q2-f3k code/qu2.py scan --gitter netz --L 3 --Nt 8 --tau $TAU --gew $G --betas 1.60 1.55 1.50 1.48 1.46 1.44 1.42 1.40 1.35 1.30 --start kalt --ntherm 60 --nmess 160 --nbin 16 --nor 1 --seed 41 --out $L/f3-kalt > $L/f3-kalt.log 2>&1
echo "kette-p0 fertig $(date -u +%H:%M:%S)" > $L/kette-p0.txt
