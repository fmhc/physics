#!/bin/bash
# DS-EICHUNG-2D-1: Fortsetzung der Zwischenstaende s0a (N2 = 16000, T = 80) und s0b (N2 = 4000, T = 40) aus NETZ-DYN-1,
# jeweils auf eigener Kopie (Original bleibt unveraendert); jeder Abschnitt mit --neu_mess, um die Drift von <r> zu sehen.
cd /home/fmh/fmhc-physics-remote/ds-eichung-2d-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
N=/home/fmh/fmhc-physics-remote/netz-dyn-1
df -h /home | tail -1
cp -n $N/stand/s0a.pkl stand/cdt-s0a.pkl; cp -n $N/stand/s0b.pkl stand/cdt-s0b.pkl
sha256sum stand/cdt-s0a.pkl $N/stand/s0a.pkl stand/cdt-s0b.pkl $N/stand/s0b.pkl
for c in 1 2 3; do
bash $K cpu10 dse-cdta$c $N/code/netzdyn.py --modus cdt2 --T 80 --L0 100 --Nz 16000 --k4 0.693 --eps 1e-4 --therm 300 --sweeps 1000000 --voll_int 25 --pruef_int 500 --ds_starts 24 --ds_smax 600 --sch_starts 16 --sch_rmax 150 --zeit 480 --seed 3$c --aus aus/cdt-a-c$c --fort stand/cdt-s0a.pkl --neu_mess
done
echo cdt-fort ende $(date --iso-8601=seconds)
