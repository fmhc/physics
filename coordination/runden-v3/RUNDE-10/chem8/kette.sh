cd /home/fmh/fmhc-physics-remote/runde10-chem8
echo "== $(date -Is) lauf1 T300"
bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000b chem8-t300 chem8_dicht.py katalyse --out lauf-69/t300 --kat-v 0.05,0.06,0.07,0.08,0.09,0.10,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,0.20,0.21,0.22,0.23,0.24,0.25 --kat-t 300
echo "== rc=$? $(date -Is)"
echo "== $(date -Is) lauf2 T600"
bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000b chem8-t600 chem8_dicht.py katalyse --out lauf-69/t600 --kat-v 0.05,0.06,0.07,0.08,0.09,0.10,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,0.20,0.21,0.22,0.23,0.24,0.25 --kat-t 600
echo "== rc=$? $(date -Is)"
echo "KETTE-CHEM8-ENDE $(date -Is)"
