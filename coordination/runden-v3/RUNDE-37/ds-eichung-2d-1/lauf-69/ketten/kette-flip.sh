#!/bin/bash
# DS-EICHUNG-2D-1: Zufallstriangulierungen per Flips, Spur cpu9
cd /home/fmh/fmhc-physics-remote/ds-eichung-2d-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
df -h /home | tail -1
D="code/dseich.py --art flip"
bash $K cpu9 dse-f1000 $D --N 1000 --therm 1000 --gap 50 --ds_jede 2 --zeit 240 --seed 201 --aus aus/flip-N1000-a --fort stand/flip-N1000.pkl
bash $K cpu9 dse-f4000 $D --N 4000 --therm 2000 --gap 100 --ds_jede 2 --zeit 420 --seed 202 --aus aus/flip-N4000-a --fort stand/flip-N4000.pkl
bash $K cpu9 dse-f16000 $D --N 16000 --therm 4000 --gap 200 --ds_jede 2 --zeit 480 --seed 203 --aus aus/flip-N16000-a --fort stand/flip-N16000.pkl
bash $K cpu9 dse-f16000b $D --N 16000 --therm 4000 --gap 200 --ds_jede 2 --zeit 480 --seed 204 --aus aus/flip-N16000-b --fort stand/flip-N16000.pkl
echo kette-flip ende $(date --iso-8601=seconds)
