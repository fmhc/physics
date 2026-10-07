#!/bin/bash
# NETZ-DYN-1 S2: Felder mit Rueckwirkung bei Delta = 0.6, k0 nachgefuehrt auf N0/N4 = 0.04 (wie S1-A ohne Felder)
# F1: U(1) beta=2 + Rahmen J=1 (2 Abschnitte); F2: nur Rahmen J=1; F3: nur SU(2) beta=2.5
cd /home/fmh/fmhc-physics-remote/netz-dyn-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
while kill -0 2596565; do sleep 15; done
lauf() { frei=$(df --output=avail -BG /home | tail -1 | tr -dc "0-9"); echo "frei ${frei}G"; if [ "$frei" -lt 10 ]; then echo "Platte unter 10 GB: Abbruch"; exit 1; fi; bash $K cpu8 "$@"; }
A="--modus cdt4 --L 2 --T 4 --k0 2.2 --Delta 0.6 --k4 0.85 --Nz 8000 --eps 2e-4 --therm 300 --sweeps 100000 --voll_int 50 --grad_int 2 --pruef_int 300 --ds_starts 24 --ds_smax 400 --sch_starts 8 --sch_rmax 40 --zeit 540 --n0_anteil 0.04 --k0_rate 2e-4"
lauf nd-f1-1 code/netzdyn.py $A --bu 2.0 --J 1.0 --seed 41 --aus aus/f1 --fort stand/f1.pkl
lauf nd-f1-2 code/netzdyn.py $A --bu 2.0 --J 1.0 --seed 41 --aus aus/f1 --fort stand/f1.pkl
lauf nd-f2-1 code/netzdyn.py $A --J 1.0 --seed 42 --aus aus/f2 --fort stand/f2.pkl
lauf nd-f3-1 code/netzdyn.py $A --bs 2.5 --seed 43 --aus aus/f3 --fort stand/f3.pkl
