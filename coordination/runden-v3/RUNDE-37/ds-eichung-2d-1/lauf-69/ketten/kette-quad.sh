#!/bin/bash
# DS-EICHUNG-2D-1: Viereckskarten (CVS), Spur cpu8
cd /home/fmh/fmhc-physics-remote/ds-eichung-2d-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
df -h /home | tail -1
D="code/dseich.py --art quad"
bash $K cpu8 dse-q1000 $D --N 1000 --nsamp 400 --zeit 240 --seed 101 --aus aus/quad-N1000-s101
bash $K cpu8 dse-q4000 $D --N 4000 --nsamp 300 --zeit 420 --seed 102 --aus aus/quad-N4000-s102
bash $K cpu8 dse-q16000 $D --N 16000 --nsamp 300 --zeit 480 --seed 103 --aus aus/quad-N16000-s103
df -h /home | tail -1
bash $K cpu8 dse-q64000a $D --N 64000 --nsamp 300 --zeit 440 --ds_starts 12 --ds_jede 2 --seed 104 --aus aus/quad-N64000-s104
bash $K cpu8 dse-q100000a $D --N 100000 --nsamp 300 --zeit 440 --ds_starts 12 --ds_jede 3 --seed 105 --aus aus/quad-N100000-s105
bash $K cpu8 dse-q64000b $D --N 64000 --nsamp 300 --zeit 440 --ds_starts 12 --ds_jede 2 --seed 106 --aus aus/quad-N64000-s106
bash $K cpu8 dse-q100000b $D --N 100000 --nsamp 300 --zeit 440 --ds_starts 12 --ds_jede 3 --seed 107 --aus aus/quad-N100000-s107
echo kette-quad ende $(date --iso-8601=seconds)
