#!/bin/bash
# DS-EICHUNG-2D-1: d_s mit grossem sigma-Bereich (smax 3000) auf Viereckskarten, Spur cpu9 (nach den Flip-Laeufen)
cd /home/fmh/fmhc-physics-remote/ds-eichung-2d-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
df -h /home | tail -1
D="code/dseich.py --art quad"
bash $K cpu9 dse-ds4000 $D --N 4000 --nsamp 100 --zeit 300 --ds_smax 3000 --sch_starts 4 --seed 401 --aus aus/dslang-N4000-s401
bash $K cpu9 dse-ds16000 $D --N 16000 --nsamp 100 --zeit 420 --ds_smax 3000 --sch_starts 4 --seed 402 --aus aus/dslang-N16000-s402
echo kette-ds ende $(date --iso-8601=seconds)
