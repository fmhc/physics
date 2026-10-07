#!/bin/bash
# NETZ-DYN-1: nach dem laufenden Abschnitt s1b-2: Punkt c (5.0, 0.6) 2 Abschnitte, dann F0 (ohne Felder, k0 auf N0/N4 = 0.04)
cd /home/fmh/fmhc-physics-remote/netz-dyn-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
lauf() { frei=$(df --output=avail -BG /home | tail -1 | tr -dc "0-9"); echo "frei ${frei}G"; if [ "$frei" -lt 10 ]; then echo "Platte unter 10 GB: Abbruch"; exit 1; fi; bash $K cpu10 "$@"; }
for i in 1 2; do
  lauf nd-s1c-$i code/netzdyn.py --modus cdt4 --L 2 --T 4 --k0 5.0 --Delta 0.6 --k4 0.85 --Nz 8000 --eps 2e-4 --therm 400 --sweeps 100000 --voll_int 50 --grad_int 2 --pruef_int 400 --ds_starts 24 --ds_smax 400 --sch_starts 8 --sch_rmax 40 --zeit 540 --seed 22 --aus aus/s1c --fort stand/s1c.pkl
done
lauf nd-f0-1 code/netzdyn.py --modus cdt4 --L 2 --T 4 --k0 2.2 --Delta 0.6 --k4 0.85 --Nz 8000 --eps 2e-4 --therm 300 --sweeps 100000 --voll_int 50 --grad_int 2 --pruef_int 300 --ds_starts 24 --ds_smax 400 --sch_starts 8 --sch_rmax 40 --zeit 540 --n0_anteil 0.04 --k0_rate 2e-4 --seed 40 --aus aus/f0 --fort stand/f0.pkl
