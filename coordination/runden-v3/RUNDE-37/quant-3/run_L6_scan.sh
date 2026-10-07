#!/bin/bash
DIR=/home/fmh/fmhc-physics-remote/quant-3
KLEIN=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SU2=$DIR/code/su2b.py
GEW=datei:$DIR/code/gwp.npz
TAU=0.348006576329167

bash $KLEIN p4000a m5-n6t4 $SU2 lauf --gitter netz --L 6 --Nt 4 --tau $TAU --gew $GEW --betas 3.2:3.25:3.3:3.325:3.35:3.375:3.4:3.45 3.45:3.4:3.375:3.35:3.325:3.3:3.25:3.2 --starts heiss kalt --ntherm 150 --nmess 400 --nbin 20 --nor 2 --out $DIR/lauf/m5-n6t4 > $DIR/lauf/m5.out 2>&1 &

wait
