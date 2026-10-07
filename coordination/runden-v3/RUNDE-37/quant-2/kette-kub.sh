#!/bin/bash
# QUANT-2 Kontrolle kubisch (Spur cpu): L=6 heiss aufwaerts / kalt abwaerts, dann L=8 nahe beta_c.
set -u
D=/home/fmh/fmhc-physics-remote/quant-2
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
L=$D/lauf
cd $D
B6="0.90 0.95 0.98 0.99 1.00 1.005 1.01 1.015 1.02 1.03 1.05 1.10"
B6R="1.10 1.05 1.03 1.02 1.015 1.01 1.005 1.00 0.99 0.98 0.95 0.90"
B8="0.98 0.995 1.00 1.005 1.01 1.02 1.04"
B8R="1.04 1.02 1.01 1.005 1.00 0.995 0.98"
df -h /home | tail -1
bash $K cpu q2-k6h code/qu2.py scan --gitter kubisch --L 6 --Nt 6 --betas $B6 --start heiss --ntherm 200 --nmess 600 --nbin 20 --nor 2 --out $L/k6-heiss > $L/k6-heiss.log 2>&1
df -h /home | tail -1
bash $K cpu q2-k6k code/qu2.py scan --gitter kubisch --L 6 --Nt 6 --betas $B6R --start kalt --ntherm 200 --nmess 600 --nbin 20 --nor 2 --seed 7 --out $L/k6-kalt > $L/k6-kalt.log 2>&1
df -h /home | tail -1
bash $K cpu q2-k8h code/qu2.py scan --gitter kubisch --L 8 --Nt 8 --betas $B8 --start heiss --ntherm 150 --nmess 300 --nbin 20 --nor 1 --mabst 2 --out $L/k8-heiss > $L/k8-heiss.log 2>&1
df -h /home | tail -1
bash $K cpu q2-k8k code/qu2.py scan --gitter kubisch --L 8 --Nt 8 --betas $B8R --start kalt --ntherm 150 --nmess 300 --nbin 20 --nor 1 --mabst 2 --seed 7 --out $L/k8-kalt > $L/k8-kalt.log 2>&1
echo "kette-kub fertig $(date -u +%H:%M:%S)" > $L/kette-kub.txt
