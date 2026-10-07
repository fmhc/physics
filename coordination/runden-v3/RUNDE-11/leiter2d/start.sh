cd /home/fmh/fmhc-physics-remote/runde11-leiter2d
K="bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh"
( $K cpu  l2d-a bic2_2d.py kurve --dim 2 --beta 0.5 --h 0.02 --omega2-liste 0.533,0.535,0.537 --n-wechsel-fein 2 --out lauf-69/a > /home/fmh/fmhc-physics-remote/runde11-leiter2d/LAUF-L2D-a.log 2>&1 ) &
( $K cpu2 l2d-b bic2_2d.py kurve --dim 2 --beta 0.5 --h 0.02 --omega2-liste 0.527,0.529,0.531,0.533 --n-wechsel-fein 2 --out lauf-69/b > /home/fmh/fmhc-physics-remote/runde11-leiter2d/LAUF-L2D-b.log 2>&1 ) &
( $K cpu6 l2d-c bic2_2d.py kurve --dim 2 --beta 0.5 --h 0.02 --omega2-liste 0.523,0.525,0.527 --n-wechsel-fein 2 --out lauf-69/c > /home/fmh/fmhc-physics-remote/runde11-leiter2d/LAUF-L2D-c.log 2>&1 ) &
wait
echo "KETTE-L2D-ENDE $(date -Is)" >> /home/fmh/fmhc-physics-remote/runde11-leiter2d/LAUF-L2D-a.log
