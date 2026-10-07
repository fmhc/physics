#!/bin/bash
# NETZ-DYN-1 Kontrollen der Messmethode am regulaeren Startnetz V x S^1 (L = 2) mit T = 4, 8, 16
cd /home/fmh/fmhc-physics-remote/netz-dyn-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
for T in 4 8 16; do
  bash $K cpu8 nd-k-$T code/netzdyn.py --modus cdt4 --L 2 --T $T --nur_start --ds_starts 24 --ds_smax 400 --sch_starts 16 --sch_rmax 40 --aus aus/k-start-T$T
done
