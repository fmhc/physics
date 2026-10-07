#!/bin/bash
# NETZ-DYN-1 S1-L3 (zweiter Anlauf): Start V 3x3x3 (N4 = 25056), T = 4, (2.2, 0.6), k4 fest 0.84 (aus L = 2), keine k4-Nachfuehrung
cd /home/fmh/fmhc-physics-remote/netz-dyn-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
for i in 1 2 3 4; do
  frei=$(df --output=avail -BG /home | tail -1 | tr -dc "0-9"); echo "frei ${frei}G"; if [ "$frei" -lt 10 ]; then echo "Platte unter 10 GB: Abbruch"; exit 1; fi
  bash $K cpu9 nd-l3b-$i code/netzdyn.py --modus cdt4 --L 3 --T 4 --k0 2.2 --Delta 0.6 --k4 0.84 --Nz 25056 --eps 6e-5 --therm 400 --tune_ab 0 --sweeps 100000 --voll_int 50 --grad_int 2 --pruef_int 400 --ds_starts 24 --ds_smax 800 --sch_starts 8 --sch_rmax 60 --zeit 540 --seed 62 --aus aus/s1l3 --fort stand/s1l3.pkl
done
