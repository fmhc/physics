#!/bin/bash
# NETZ-DYN-1 S1-B: 3+1D CDT ohne Felder bei (2.2, 0.0) [Erwartung B/C_b] und (5.0, 0.6) [Erwartung A], je 3 Abschnitte
cd /home/fmh/fmhc-physics-remote/netz-dyn-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
for pkt in "b 2.2 0.0" "c 5.0 0.6"; do
  set -- $pkt
  for i in 1 2 3; do
    frei=$(df --output=avail -BG /home | tail -1 | tr -dc "0-9"); echo "frei ${frei}G"; if [ "$frei" -lt 10 ]; then echo "Platte unter 10 GB: Abbruch"; exit 1; fi
    bash $K cpu10 nd-s1$1-$i code/netzdyn.py --modus cdt4 --L 2 --T 4 --k0 $2 --Delta $3 --k4 0.85 --Nz 8000 --eps 2e-4 --therm 400 --sweeps 100000 --voll_int 50 --grad_int 2 --pruef_int 400 --ds_starts 24 --ds_smax 400 --sch_starts 8 --sch_rmax 40 --zeit 540 --seed 22 --aus aus/s1$1 --fort stand/s1$1.pkl
  done
done
