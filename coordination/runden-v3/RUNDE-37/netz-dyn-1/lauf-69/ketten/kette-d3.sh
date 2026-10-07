#!/bin/bash
# NETZ-DYN-1 S1-D3: 4D ohne Zeitschichten (freie Pachner-Zuege, DT), Start V 2x2x2 x 4, Nz = 8000, k0-Abtastung
cd /home/fmh/fmhc-physics-remote/netz-dyn-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
for k0 in 1.5 2.6 4.0; do
  frei=$(df --output=avail -BG /home | tail -1 | tr -dc "0-9"); echo "frei ${frei}G"; if [ "$frei" -lt 10 ]; then echo "Platte unter 10 GB: Abbruch"; exit 1; fi
  bash $K cpu11 nd-d3-$k0 code/netzdyn.py --modus dt4 --L 2 --T 4 --k0 $k0 --k4 1.0 --Nz 8000 --eps 2e-4 --therm 400 --sweeps 100000 --voll_int 50 --grad_int 2 --pruef_int 400 --ds_starts 24 --ds_smax 400 --sch_starts 8 --sch_rmax 40 --zeit 540 --seed 31 --aus aus/d3-$k0 --fort stand/d3-$k0.pkl
done
