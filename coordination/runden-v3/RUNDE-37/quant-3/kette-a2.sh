#!/bin/bash
# QUANT-3 Wiederaufnahme (agy, 06.10.2026), Spur p4000a. Code unveraendert: code/su2.py (sha256 10cdeb47..., = su2.py.v2).
# A1 (S1): kubisch 12^3 x 4, 8 beta um 2,30, heisse Starts, laenger als k12 (dort nur 55 Messungen).
# A2 (S3): Netz L=6 Nt=4, 10 beta 3,1 bis 3,7 (Polyakov-Sprung lag bei L=4 zwischen 3,25 und 3,5).
# A3 (S2): Netz L=6 Nt=8, beta 3,0/3,2/3,3/3,5 je heiss und kalt (Plakette, Volumenabhaengigkeit von chiP gegen L=4).
set -u
D=/home/fmh/fmhc-physics-remote/quant-3
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
L=$D/lauf
cd $D
TAU=0.348006576329167
G=datei:$D/code/gwp.npz
pruef() { F=$(df --output=avail -BG /home | tail -1 | tr -dc 0-9); echo "df frei ${F}G $(date -u +%H:%M:%S)"; [ "$F" -ge 10 ] || exit 9; }
pruef
bash $K p4000a q3-a1 code/su2.py lauf --gitter kubisch --L 12 --Nt 4 --betas 2.26 2.28 2.29 2.30 2.31 2.32 2.34 2.36 --starts heiss --ntherm 300 --nmess 6000 --nbin 50 --nor 2 --graph --zeitlimit 520 --seed 121 --out $L/a1-k12 > $L/a1-k12.log 2>&1
pruef
bash $K p4000a q3-a2 code/su2.py lauf --gitter netz --L 6 --Nt 4 --tau $TAU --gew $G --betas 3.1 3.2 3.25 3.3 3.35 3.4 3.45 3.5 3.6 3.7 --starts heiss --ntherm 200 --nmess 4000 --nbin 50 --nor 2 --graph --zeitlimit 520 --seed 64 --out $L/a2-n6t4 > $L/a2-n6t4.log 2>&1
pruef
bash $K p4000a q3-a3 code/su2.py lauf --gitter netz --L 6 --Nt 8 --tau $TAU --gew $G --betas 3.0 3.2 3.3 3.5 3.0 3.2 3.3 3.5 --starts heiss heiss heiss heiss kalt kalt kalt kalt --ntherm 200 --nmess 4000 --nbin 50 --nor 2 --graph --zeitlimit 520 --seed 68 --out $L/a3-n6t8 > $L/a3-n6t8.log 2>&1
echo "kette-a2 fertig $(date -u +%H:%M:%S)" > $L/kette-a2.txt
