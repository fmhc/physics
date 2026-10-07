#!/bin/bash
# QUANT-2 Rauchtest 1 (Spur cpu): Netz-Gewichte, Bauprobe L=2/3, Zeitprobe je Sweep.
set -u
D=/home/fmh/fmhc-physics-remote/quant-2
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
L=$D/lauf
cd $D
df -h /home | tail -1
bash $K cpu q2-netz code/qu2.py netz --taus 0.2924 1.0 --nk 10 --out $L/netz.json > $L/netz.log 2>&1
bash $K cpu q2-r1k code/qu2.py scan --gitter kubisch --L 6 --Nt 6 --betas 0.95 1.05 --ntherm 10 --nmess 40 --nbin 4 --out $L/r1-kub > $L/r1-kub.log 2>&1
bash $K cpu q2-r1n code/qu2.py scan --gitter netz --L 3 --Nt 8 --tau 0.2924 --betas 1.0 --ntherm 5 --nmess 20 --nbin 4 --out $L/r1-netz > $L/r1-netz.log 2>&1
bash $K cpu q2-r1n2 code/qu2.py scan --gitter netz --L 2 --Nt 8 --tau 0.2924 --betas 1.0 --ntherm 2 --nmess 8 --nbin 4 --out $L/r1-netz2 > $L/r1-netz2.log 2>&1
bash $K cpu q2-r1a code/qu2.py auswertung --ein $L/r1-kub $L/r1-netz --out $L/r1-aus.json > $L/r1-aus.log 2>&1
echo "rauch1 fertig $(date -u +%H:%M:%S)" > $L/rauch1.txt
