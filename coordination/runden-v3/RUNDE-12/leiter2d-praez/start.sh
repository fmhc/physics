#!/bin/bash
# LEITER-2D-PRAEZ, Hauptlaeufe nach PLAN.md (eingefroren 20261001-172446). Einmal von Hand gestartet, kein Dienst.
cd /home/fmh/fmhc-physics-remote/runde12-leiter2d-praez || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
D=/home/fmh/fmhc-physics-remote/runde12-leiter2d-praez
G="--dim 2 --beta 0.5 --h 0.02 --budget 540"
L="0.5285,0.5290,0.5295,0.5300,0.533,0.535"
( bash $K cpu  praez-rm9  bic2_2d_praez.py kurve $G --omega2-liste $L --rm 9  --n-wechsel-fein 2 --out lauf-69/rm9  > $D/LAUF-RM9.log 2>&1 ) &
( bash $K cpu2 praez-rm12 bic2_2d_praez.py kurve $G --omega2-liste $L --rm 12 --n-wechsel-fein 2 --out lauf-69/rm12 > $D/LAUF-RM12.log 2>&1 ) &
( bash $K cpu3 praez-rm15 bic2_2d_praez.py kurve $G --omega2-liste $L --rm 15 --n-wechsel-fein 2 --out lauf-69/rm15 > $D/LAUF-RM15.log 2>&1 ) &
( bash $K cpu4 praez-rec bic2_2d_praez.py exakt $G --x0 0.5292 --rho0 1.5561 --rc 1.557 --drho 5.5 --cgam 3000 \
    --offsets=0,7.5e-5,-7.5e-5,1.5e-4,-1.5e-4,2.25e-4,-2.25e-4,3e-4,-3e-4 --w-dx 3e-4 \
    --w-drho=-1e-3,-3e-4,-1e-4,-3e-5,0,3e-5,1e-4,3e-4,1e-3 --u-dx 3e-4,1.5e-4 --u-drho 1.5e-3 \
    --u-drho-ohne-fit 1.5e-3 --u-n 60 --neu-legen nein --rm 12 --out lauf-69/rec > $D/LAUF-REC.log 2>&1 ) &
( bash $K cpu6 praez-fein bic2_2d_praez.py kurve $G --omega2-liste 0.5292,0.52925,0.5293,0.52935 --rm 12 --n-wechsel-fein 0 --out lauf-69/fein > $D/LAUF-FEIN.log 2>&1 ) &
wait
echo "KETTE-PRAEZ-ENDE $(date -Is)" >> $D/LAUF-RM9.log
