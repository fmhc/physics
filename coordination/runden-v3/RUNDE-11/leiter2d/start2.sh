cd /home/fmh/fmhc-physics-remote/runde11-leiter2d
K="bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh"
( $K cpu  l2d-d bic2_2d.py kurve --dim 2 --beta 0.5 --h 0.02 --omega2-liste 0.5285,0.5290,0.5295,0.5300 --n-wechsel-fein 2 --out lauf-69/d > /home/fmh/fmhc-physics-remote/runde11-leiter2d/LAUF-L2D-d.log 2>&1 ) &
( $K cpu2 l2d-e bic2_2d.py kurve --dim 2 --beta 0.5 --h 0.01 --omega2-liste 0.5285,0.5290,0.5295,0.5300 --n-wechsel-fein 2 --out lauf-69/e > /home/fmh/fmhc-physics-remote/runde11-leiter2d/LAUF-L2D-e.log 2>&1 ) &
( $K cpu6 l2d-f bic2_2d.py kurve --dim 2 --beta 0.5 --h 0.02 --omega2-liste 0.5255,0.5260 --n-wechsel-fein 2 --out lauf-69/f > /home/fmh/fmhc-physics-remote/runde11-leiter2d/LAUF-L2D-f.log 2>&1 ) &
wait
echo "KETTE-L2D2-ENDE $(date -Is)" >> /home/fmh/fmhc-physics-remote/runde11-leiter2d/LAUF-L2D-d.log
