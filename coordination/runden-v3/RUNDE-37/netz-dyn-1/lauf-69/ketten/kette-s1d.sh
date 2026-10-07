#!/bin/bash
# NETZ-DYN-1: cpu10 nach s1c-1: s1c-2 (5.0, 0.6) fortsetzen, dann F1b: U(1) beta=2 + Rahmen J=1 bei k0 = 10.2 (Test der abgeschaetzten Verschiebung)
cd /home/fmh/fmhc-physics-remote/netz-dyn-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
lauf() { frei=$(df --output=avail -BG /home | tail -1 | tr -dc "0-9"); echo "frei ${frei}G"; if [ "$frei" -lt 10 ]; then echo "Platte unter 10 GB: Abbruch"; exit 1; fi; bash $K cpu10 "$@"; }
lauf nd-s1c-2 code/netzdyn.py --modus cdt4 --L 2 --T 4 --k0 5.0 --Delta 0.6 --k4 0.85 --Nz 8000 --eps 2e-4 --therm 400 --sweeps 100000 --voll_int 50 --grad_int 2 --pruef_int 400 --ds_starts 24 --ds_smax 400 --sch_starts 8 --sch_rmax 40 --zeit 540 --seed 22 --aus aus/s1c --fort stand/s1c.pkl
lauf nd-f1b-1 code/netzdyn.py --modus cdt4 --L 2 --T 4 --k0 10.2 --Delta 0.6 --k4 -0.05 --Nz 8000 --eps 2e-4 --therm 300 --sweeps 100000 --voll_int 50 --grad_int 2 --pruef_int 300 --ds_starts 24 --ds_smax 400 --sch_starts 8 --sch_rmax 40 --zeit 540 --bu 2.0 --J 1.0 --seed 45 --aus aus/f1b --fort stand/f1b.pkl
