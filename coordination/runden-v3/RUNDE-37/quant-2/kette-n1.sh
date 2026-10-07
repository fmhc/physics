#!/bin/bash
# QUANT-2 Netz, erste Uebersicht (Spur cpu): L=2, Nt=8, tau=0.2924; DEC-Stern (omega=0) und ungewichtet, heiss aufwaerts.
set -u
D=/home/fmh/fmhc-physics-remote/quant-2
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
L=$D/lauf
cd $D
BD="0.4 0.6 0.8 1.0 1.2 1.4 1.6 1.8 2.0 2.4 3.0 4.0"
BE="0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0 1.2 1.5 2.0"
df -h /home | tail -1
bash $K cpu q2-n1d code/qu2.py scan --gitter netz --L 2 --Nt 8 --tau 0.2924 --gew dec --betas $BD --start heiss --ntherm 100 --nmess 300 --nbin 20 --nor 1 --out $L/n1-dec-heiss > $L/n1-dec-heiss.log 2>&1
df -h /home | tail -1
bash $K cpu q2-n1e code/qu2.py scan --gitter netz --L 2 --Nt 8 --tau 0.2924 --gew eins --betas $BE --start heiss --ntherm 100 --nmess 300 --nbin 20 --nor 1 --out $L/n1-eins-heiss > $L/n1-eins-heiss.log 2>&1
echo "kette-n1 fertig $(date -u +%H:%M:%S)" > $L/kette-n1.txt
