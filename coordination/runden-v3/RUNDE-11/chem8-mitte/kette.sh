cd /home/fmh/fmhc-physics-remote/runde11-chem8-mitte
for T in 300 600; do echo "== $(date -Is) T$T"; bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000b chem8m-t$T chem8_mitte.py katalyse --out lauf-69/t$T --kat-v 0.05,0.06,0.07,0.08,0.09,0.10,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,0.20,0.21,0.22,0.23,0.24,0.25 --kat-t $T; echo "== rc=$? $(date -Is)"; done
echo KETTE-CHEM8M-ENDE $(date -Is)
