#!/bin/bash
# DS-EICHUNG-2D-1: 1+1D-CDT mit unabhaengiger Abtastung der Schichtlaengen (cdtexakt.py), Spur cpu10; T/Wurzel(N) = 0,63 wie D1
cd /home/fmh/fmhc-physics-remote/ds-eichung-2d-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
df -h /home | tail -1
D="code/cdtexakt.py"
bash $K cpu10 dse-cx4000 $D --T 40 --N 4000 --nsamp 250 --zeit 240 --seed 301 --aus aus/cdtx-T40-N4000-s301
bash $K cpu10 dse-cx16000 $D --T 80 --N 16000 --nsamp 250 --zeit 420 --therm_faktor 6 --seed 302 --aus aus/cdtx-T80-N16000-s302
bash $K cpu10 dse-cx64000a $D --T 160 --N 64000 --nsamp 250 --zeit 460 --therm_faktor 4 --ds_starts 12 --ds_jede 2 --seed 303 --aus aus/cdtx-T160-N64000-s303
bash $K cpu10 dse-cx32000 $D --T 113 --N 32000 --nsamp 250 --zeit 460 --therm_faktor 4 --ds_starts 12 --ds_jede 2 --seed 304 --aus aus/cdtx-T113-N32000-s304
bash $K cpu10 dse-cx64000b $D --T 160 --N 64000 --nsamp 250 --zeit 460 --therm_faktor 4 --ds_starts 12 --ds_jede 2 --seed 305 --aus aus/cdtx-T160-N64000-s305
echo kette-cdtx ende $(date --iso-8601=seconds)
