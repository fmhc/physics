#!/bin/bash
# NETZ-DYN-1 zweite Welle cpu10 (nach kette-s1c): S0 fortsetzen mit vollen Schalen (sch_rmax 150), Messung neu
cd /home/fmh/fmhc-physics-remote/netz-dyn-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
while kill -0 2597882; do sleep 15; done
lauf() { frei=$(df --output=avail -BG /home | tail -1 | tr -dc "0-9"); echo "frei ${frei}G"; if [ "$frei" -lt 10 ]; then echo "Platte unter 10 GB: Abbruch"; exit 1; fi; bash $K cpu10 "$@"; }
lauf nd-s0a2 code/netzdyn.py --modus cdt2 --T 80 --L0 100 --Nz 16000 --k4 0.693 --eps 1e-4 --therm 300 --sweeps 100000 --voll_int 25 --pruef_int 500 --ds_starts 24 --ds_smax 600 --sch_starts 16 --sch_rmax 150 --zeit 540 --seed 11 --aus aus/s0a2 --fort stand/s0a.pkl --neu_mess
lauf nd-s0b2 code/netzdyn.py --modus cdt2 --T 40 --L0 50 --Nz 4000 --k4 0.693 --eps 4e-4 --therm 300 --sweeps 100000 --voll_int 25 --pruef_int 500 --ds_starts 24 --ds_smax 600 --sch_starts 16 --sch_rmax 150 --zeit 300 --seed 12 --aus aus/s0b2 --fort stand/s0b.pkl --neu_mess
