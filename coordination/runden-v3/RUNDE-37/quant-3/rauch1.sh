#!/bin/bash
# QUANT-3 Rauchtest 1 (Spur p4000a): Selbstpruefung, kubisch 4^4 (Plakette gegen Literatur), 8^3x4 (Zeit),
# Netz L=2 Nt=4 und L=6 Nt=4 (Bau, Zeit, Speicher).
set -u
D=/home/fmh/fmhc-physics-remote/quant-3
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
L=$D/lauf
cd $D
TAU=0.348006576329167
G=datei:$D/code/gwp.npz
pruef() { F=$(df --output=avail -BG /home | tail -1 | tr -dc 0-9); echo "df frei ${F}G $(date -u +%H:%M:%S)"; [ "$F" -ge 10 ] || exit 9; }
pruef
bash $K p4000a q3-test code/su2.py test --out $L/r1-test.json > $L/r1-test.log 2>&1
pruef
bash $K p4000a q3-r1k4 code/su2.py lauf --gitter kubisch --L 4 --Nt 4 --betas 2.3 2.3 2.5 2.5 --starts heiss kalt heiss kalt --ntherm 100 --nmess 400 --nbin 10 --out $L/r1-k4 > $L/r1-k4.log 2>&1
pruef
bash $K p4000a q3-r1k8 code/su2.py lauf --gitter kubisch --L 8 --Nt 4 --betas 2.2 2.3 2.4 2.5 --starts heiss --ntherm 50 --nmess 200 --nbin 10 --out $L/r1-k8 > $L/r1-k8.log 2>&1
pruef
bash $K p4000a q3-r1n2 code/su2.py lauf --gitter netz --L 2 --Nt 4 --tau $TAU --gew $G --betas 2 4 --starts heiss --ntherm 20 --nmess 50 --nbin 5 --korr --out $L/r1-n2 > $L/r1-n2.log 2>&1
pruef
bash $K p4000a q3-r1n6 code/su2.py lauf --gitter netz --L 6 --Nt 4 --tau $TAU --gew $G --betas 3 3 --starts heiss kalt --ntherm 20 --nmess 40 --nbin 4 --korr --out $L/r1-n6 > $L/r1-n6.log 2>&1
echo "rauch1 fertig $(date -u +%H:%M:%S)" > $L/rauch1.txt
