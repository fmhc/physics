#!/bin/bash
DIR=/home/fmh/fmhc-physics-remote/quant-3
KLEIN=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SU2=$DIR/code/su2b.py
GEW=datei:$DIR/code/gwp.npz
TAU=0.348006576329167

bash $KLEIN p4000a m3-n4t10 $SU2 lauf --gitter netz --L 4 --Nt 10 --tau $TAU --gew $GEW --betas 3.33 --starts heiss --ntherm 200 --nmess 800 --nbin 20 --nor 2 --korr --mh --out $DIR/lauf/m3-n4t10 > $DIR/lauf/m3.out 2>&1 &
bash $KLEIN p4000b m2-n4t8 $SU2 lauf --gitter netz --L 4 --Nt 8 --tau $TAU --gew $GEW --betas 3.33 --starts heiss --ntherm 200 --nmess 800 --nbin 20 --nor 2 --korr --mh --out $DIR/lauf/m2-n4t8 > $DIR/lauf/m2.out 2>&1 &

wait
bash $KLEIN p4000a m4-n4t12 $SU2 lauf --gitter netz --L 4 --Nt 12 --tau $TAU --gew $GEW --betas 3.33 --starts heiss --ntherm 200 --nmess 800 --nbin 20 --nor 2 --korr --mh --out $DIR/lauf/m4-n4t12 > $DIR/lauf/m4.out 2>&1 &
wait
