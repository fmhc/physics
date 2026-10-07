#!/bin/bash
# NETZ-DYN-1 F4 (Erkundung D6/D7): cdt4 bei (2.2, 0.0) mit U(1) beta=2 und Rahmen J=1, ohne k0-Nachfuehrung
# (die Rueckwirkung der Felder darf die Eckenzahl senken; Suche nach Superpunkten mit Ladung)
cd /home/fmh/fmhc-physics-remote/netz-dyn-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
while kill -0 2596912; do sleep 15; done
for i in 1 2; do
  frei=$(df --output=avail -BG /home | tail -1 | tr -dc "0-9"); echo "frei ${frei}G"; if [ "$frei" -lt 10 ]; then echo "Platte unter 10 GB: Abbruch"; exit 1; fi
  bash $K cpu11 nd-f4-$i code/netzdyn.py --modus cdt4 --L 2 --T 4 --k0 2.2 --Delta 0.0 --k4 0.85 --Nz 8000 --eps 2e-4 --therm 300 --sweeps 100000 --voll_int 50 --grad_int 2 --pruef_int 300 --ds_starts 24 --ds_smax 400 --sch_starts 8 --sch_rmax 40 --zeit 540 --bu 2.0 --J 1.0 --seed 44 --aus aus/f4 --fort stand/f4.pkl
done
