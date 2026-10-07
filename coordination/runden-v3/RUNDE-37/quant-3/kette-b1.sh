#!/bin/bash
# QUANT-3 Netz (Spur p4000b): M2 grob (L=4, Nt=4, 21 beta von 1 bis 6, heiss), dann M1-Zyklus (L=4, Nt=8,
# 2 Replikas heiss aufwaerts, 2 kalt abwaerts, 21 Stufen).
set -u
D=/home/fmh/fmhc-physics-remote/quant-3
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
L=$D/lauf
cd $D
TAU=0.348006576329167
G=datei:$D/code/gwp.npz
pruef() { F=$(df --output=avail -BG /home | tail -1 | tr -dc 0-9); echo "df frei ${F}G $(date -u +%H:%M:%S)"; [ "$F" -ge 10 ] || exit 9; }
BN="1.0 1.25 1.5 1.75 2.0 2.25 2.5 2.75 3.0 3.25 3.5 3.75 4.0 4.25 4.5 4.75 5.0 5.25 5.5 5.75 6.0"
UP=$(echo $BN | tr ' ' ':')
DOWN=$(echo $BN | tr ' ' '\n' | tac | tr '\n' ':' | sed 's/:$//')
pruef
bash $K p4000b q3-n4t4 code/su2.py lauf --gitter netz --L 4 --Nt 4 --tau $TAU --gew $G --betas $BN --starts heiss --ntherm 300 --nmess 20000 --nbin 50 --nor 2 --graph --zeitlimit 300 --out $L/n4t4 > $L/n4t4.log 2>&1
pruef
bash $K p4000b q3-m1 code/su2.py lauf --gitter netz --L 4 --Nt 8 --tau $TAU --gew $G --betas $UP $UP $DOWN $DOWN --starts heiss heiss kalt kalt --ntherm 100 --nmess 200 --nbin 10 --nor 2 --graph --zeitlimit 540 --seed 7 --out $L/m1 > $L/m1.log 2>&1
echo "kette-b1 fertig $(date -u +%H:%M:%S)" > $L/kette-b1.txt
