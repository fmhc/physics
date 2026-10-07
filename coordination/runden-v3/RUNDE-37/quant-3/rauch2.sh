#!/bin/bash
# QUANT-3 Rauchtest 2 (Spur p4000a): schnelle Fassung (Quaternion-Produkt mit Permutation, Waermebad ohne Schleife),
# eager gegen CUDA-Graph auf kubisch 4^4 (gleiche Physik, Zeit), dann 8^3x4 und Netz L=6 Nt=4 mit Graph (Zeit).
set -u
D=/home/fmh/fmhc-physics-remote/quant-3
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
L=$D/lauf
cd $D
TAU=0.348006576329167
G=datei:$D/code/gwp.npz
pruef() { F=$(df --output=avail -BG /home | tail -1 | tr -dc 0-9); echo "df frei ${F}G $(date -u +%H:%M:%S)"; [ "$F" -ge 10 ] || exit 9; }
pruef
bash $K p4000a q3-test2 code/su2.py test --out $L/r2-test.json > $L/r2-test.log 2>&1
pruef
bash $K p4000a q3-r2e code/su2.py lauf --gitter kubisch --L 4 --Nt 4 --betas 2.3 2.3 2.5 2.5 --starts heiss kalt heiss kalt --ntherm 100 --nmess 400 --nbin 10 --out $L/r2-k4e > $L/r2-k4e.log 2>&1
pruef
bash $K p4000a q3-r2g code/su2.py lauf --gitter kubisch --L 4 --Nt 4 --betas 2.3 2.3 2.5 2.5 --starts heiss kalt heiss kalt --ntherm 100 --nmess 400 --nbin 10 --graph --out $L/r2-k4g > $L/r2-k4g.log 2>&1
pruef
bash $K p4000a q3-r2k8 code/su2.py lauf --gitter kubisch --L 8 --Nt 4 --betas 2.2 2.25 2.3 2.35 2.4 2.5 --starts heiss --ntherm 100 --nmess 400 --nbin 10 --graph --out $L/r2-k8 > $L/r2-k8.log 2>&1
pruef
bash $K p4000a q3-r2n6 code/su2.py lauf --gitter netz --L 6 --Nt 4 --tau $TAU --gew $G --betas 3 3 --starts heiss kalt --ntherm 50 --nmess 100 --nbin 10 --korr --graph --out $L/r2-n6 > $L/r2-n6.log 2>&1
echo "rauch2 fertig $(date -u +%H:%M:%S)" > $L/rauch2.txt
