#!/bin/bash
# NETZ-DYN-1 zweite Welle cpu11 (nach kette-f4): Startunabhaengigkeit, Endzustand von (2.2, 0.0) weiter bei (2.2, 0.6)
cd /home/fmh/fmhc-physics-remote/netz-dyn-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
while kill -0 2597189; do sleep 15; done
cp stand/s1b.pkl stand/s1x.pkl
lauf() { frei=$(df --output=avail -BG /home | tail -1 | tr -dc "0-9"); echo "frei ${frei}G"; if [ "$frei" -lt 10 ]; then echo "Platte unter 10 GB: Abbruch"; exit 1; fi; bash $K cpu11 "$@"; }
lauf nd-s1x-1 code/netzdyn.py --modus cdt4 --L 2 --T 4 --k0 2.2 --Delta 0.6 --k4 0.84 --Nz 8000 --eps 2e-4 --therm 400 --sweeps 100000 --voll_int 50 --grad_int 2 --pruef_int 400 --ds_starts 24 --ds_smax 400 --sch_starts 8 --sch_rmax 40 --zeit 540 --seed 51 --aus aus/s1x --fort stand/s1x.pkl --neu_kopplung
