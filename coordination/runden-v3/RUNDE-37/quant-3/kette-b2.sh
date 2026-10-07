#!/bin/bash
# QUANT-3 Wiederaufnahme (agy, 06.10.2026), Spur p4000b. Code unveraendert: code/su2.py (sha256 10cdeb47..., = su2.py.v2).
# B1 (S3): Netz L=4 Nt=4, 16 beta 3,0 bis 3,75 fein (Endlichkeitsvergleich zu A2, L=6).
# B2 (S3): Netz L=6 Nt=6, 10 beta 3,2 bis 4,4 grob (Verschiebung von beta_c mit Nt).
# B3 (S2): Netz L=4 Nt=8, feste beta, heiss und kalt: ergaenzt m1 (Zyklus) um Gegenstarts ausserhalb der Ueberlappung
#          und um ein feines Fenster 3,0 bis 3,5 je heiss und kalt.
set -u
D=/home/fmh/fmhc-physics-remote/quant-3
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
L=$D/lauf
cd $D
TAU=0.348006576329167
G=datei:$D/code/gwp.npz
pruef() { F=$(df --output=avail -BG /home | tail -1 | tr -dc 0-9); echo "df frei ${F}G $(date -u +%H:%M:%S)"; [ "$F" -ge 10 ] || exit 9; }
pruef
bash $K p4000b q3-b1 code/su2.py lauf --gitter netz --L 4 --Nt 4 --tau $TAU --gew $G --betas 3.0 3.1 3.15 3.2 3.25 3.3 3.325 3.35 3.375 3.4 3.425 3.45 3.5 3.55 3.6 3.75 --starts heiss --ntherm 300 --nmess 6000 --nbin 50 --nor 2 --graph --zeitlimit 520 --seed 44 --out $L/b1-n4t4 > $L/b1-n4t4.log 2>&1
pruef
bash $K p4000b q3-b2 code/su2.py lauf --gitter netz --L 6 --Nt 6 --tau $TAU --gew $G --betas 3.2 3.4 3.5 3.6 3.7 3.8 3.9 4.0 4.2 4.4 --starts heiss --ntherm 200 --nmess 4000 --nbin 50 --nor 2 --graph --zeitlimit 520 --seed 66 --out $L/b2-n6t6 > $L/b2-n6t6.log 2>&1
pruef
bash $K p4000b q3-b3 code/su2.py lauf --gitter netz --L 4 --Nt 8 --tau $TAU --gew $G --betas 1.0 2.0 2.5 4.5 5.0 3.0 3.1 3.2 3.3 3.4 3.5 3.0 3.1 3.2 3.3 3.4 3.5 --starts kalt kalt kalt heiss heiss heiss heiss heiss heiss heiss heiss kalt kalt kalt kalt kalt kalt --ntherm 300 --nmess 4000 --nbin 50 --nor 2 --graph --zeitlimit 520 --seed 48 --out $L/b3-n4t8 > $L/b3-n4t8.log 2>&1
echo "kette-b2 fertig $(date -u +%H:%M:%S)" > $L/kette-b2.txt
