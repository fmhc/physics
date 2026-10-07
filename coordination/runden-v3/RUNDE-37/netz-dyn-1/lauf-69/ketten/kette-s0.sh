#!/bin/bash
# NETZ-DYN-1 S0 (1+1D): Startkontrolle, dann N2 = 16000 (T = 80) und N2 = 4000 (T = 40)
cd /home/fmh/fmhc-physics-remote/netz-dyn-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
df -h /home | tail -1
bash $K cpu8 nd-s0flach code/netzdyn.py --modus cdt2 --T 80 --L0 100 --nur_start --ds_starts 24 --ds_smax 600 --sch_starts 24 --sch_rmax 60 --aus aus/s0-flach
bash $K cpu8 nd-s0a code/netzdyn.py --modus cdt2 --T 80 --L0 100 --Nz 16000 --k4 0.693 --eps 1e-4 --therm 300 --sweeps 100000 --voll_int 50 --pruef_int 500 --ds_starts 24 --ds_smax 600 --sch_starts 16 --sch_rmax 60 --zeit 540 --seed 11 --aus aus/s0a --fort stand/s0a.pkl
df -h /home | tail -1
bash $K cpu8 nd-s0b code/netzdyn.py --modus cdt2 --T 40 --L0 50 --Nz 4000 --k4 0.693 --eps 4e-4 --therm 300 --sweeps 100000 --voll_int 50 --pruef_int 500 --ds_starts 24 --ds_smax 600 --sch_starts 16 --sch_rmax 60 --zeit 400 --seed 12 --aus aus/s0b --fort stand/s0b.pkl
