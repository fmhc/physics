#!/bin/bash
# NETZ-DYN-1 Startunabhaengigkeit (cpu11, nach kette-f4): Endzustand von F1 (Felder, N0 niedrig) ohne Felder bei (2.2, 0.6) weiter
cd /home/fmh/fmhc-physics-remote/netz-dyn-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
while kill -0 2597189; do sleep 15; done
while kill -0 2596987; do sleep 15; done
cp stand/f1.pkl stand/s1x-unten.pkl
frei=$(df --output=avail -BG /home | tail -1 | tr -dc "0-9"); echo "frei ${frei}G"; if [ "$frei" -lt 10 ]; then echo "Platte unter 10 GB: Abbruch"; exit 1; fi
bash $K cpu11 nd-s1x-unten code/netzdyn.py --modus cdt4 --L 2 --T 4 --k0 2.2 --Delta 0.6 --k4 0.84 --Nz 8000 --eps 2e-4 --therm 400 --tune_ab 0 --sweeps 100000 --voll_int 50 --grad_int 2 --pruef_int 400 --ds_starts 24 --ds_smax 400 --sch_starts 8 --sch_rmax 40 --zeit 540 --seed 52 --aus aus/s1x-unten --fort stand/s1x-unten.pkl --neu_kopplung --felder_aus
