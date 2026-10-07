#!/bin/bash
# LEITER-2D-PRAEZ, Folgelaeufe nach PLAN.md Abschnitt 7 (Nachtrag, eingefroren 20261001-173925). Einmal von Hand gestartet.
cd /home/fmh/fmhc-physics-remote/runde12-leiter2d-praez || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
D=/home/fmh/fmhc-physics-remote/runde12-leiter2d-praez
G="--dim 2 --beta 0.5 --h 0.02 --budget 540"
( bash $K cpu  praez-f7 bic2_2d_praez.py kurve $G --omega2-liste 0.5285,0.5290,0.5295,0.5300 --n-rho 4000 --rm 12 --n-wechsel-fein 1 --out lauf-69/f7 > $D/LAUF-F7.log 2>&1 ) &
( bash $K cpu2 praez-f8 bic2_2d_praez.py kurve $G --omega2-liste 0.5255,0.5260 --n-rho 4000 --rm 12 --n-wechsel-fein 1 --out lauf-69/f8 > $D/LAUF-F8.log 2>&1 ) &
( bash $K cpu3 praez-f6 bic2_2d_praez.py kurve $G --omega2-liste 0.533,0.535 --n-rho 4000 --rm 12 --n-wechsel-fein 1 --out lauf-69/f6 > $D/LAUF-F6.log 2>&1 ) &
( bash $K cpu4 praez-rec2 bic2_2d_praez_v2.py exakt $G --x0 0.5292 --rho0 1.5561 --rc 1.557 --drho 5.5 --cgam 3000 \
    --offsets=0,7.5e-5,-7.5e-5,1.5e-4,-1.5e-4,2.25e-4,-2.25e-4,3e-4,-3e-4 --w-dx 3e-4 \
    --w-drho=-1e-3,-3e-4,-1e-4,-3e-5,0,3e-5,1e-4,3e-4,1e-3 --u-dx 3e-4,1.5e-4 --u-drho 1.5e-3 \
    --u-drho-ohne-fit 1.5e-3 --u-n 60 --neu-legen nein --rm 12 --u-runden 20 --out lauf-69/rec2 > $D/LAUF-REC2.log 2>&1 ) &
wait
echo "KETTE-PRAEZ2-ENDE $(date -Is)" >> $D/LAUF-F7.log
