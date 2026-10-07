#!/bin/bash
# NETZ-DYN-1 S1-A: 3+1D CDT ohne Felder bei (k0, Delta) = (2.2, 0.6), Start V 2x2x2, T = 4, Nz = 8000
cd /home/fmh/fmhc-physics-remote/netz-dyn-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
for i in 1 2 3 4 5 6; do
  frei=$(df --output=avail -BG /home | tail -1 | tr -dc "0-9"); echo "frei ${frei}G"; if [ "$frei" -lt 10 ]; then echo "Platte unter 10 GB: Abbruch"; exit 1; fi
  bash $K cpu9 nd-s1a-$i code/netzdyn.py --modus cdt4 --L 2 --T 4 --k0 2.2 --Delta 0.6 --k4 0.85 --Nz 8000 --eps 2e-4 --therm 400 --sweeps 100000 --voll_int 50 --grad_int 2 --pruef_int 400 --ds_starts 24 --ds_smax 400 --sch_starts 8 --sch_rmax 40 --zeit 540 --seed 21 --aus aus/s1a --fort stand/s1a.pkl
done
