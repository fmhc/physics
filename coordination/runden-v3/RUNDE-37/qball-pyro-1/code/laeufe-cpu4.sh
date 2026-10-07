#!/bin/bash
# QBALL-PYRO-1 Hauptlaeufe, Spur cpu4 (im Ordner /home/fmh/fmhc-physics-remote/runde37-pyro)
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd /home/fmh/fmhc-physics-remote/runde37-pyro || exit 1
bash $K cpu4 pyro-b3 code/pyro.py bogo --L 3 --h 1 --out lauf/bogo-L3.json
bash $K cpu4 pyro-b4 code/pyro.py bogo --L 4 --h 1 --out lauf/bogo-L4.json
for k in 0.1 0.05 0.02; do
  bash $K cpu4 pyro-k$k code/pyro.py ring --L 8 --h 1 --T 200 --dt 0.005 --rauschen 1e-6 --saat 1 --kick $k --richtung 1,0,0 --Rw 2.5 --out lauf/ring-kick-$k.json
done
bash $K cpu4 pyro-ball1 code/pyro.py ball --L 17 --h 0.5 --om2 0.7 --T 200 --dt 0.01 --kick 0.1 --richtung 1,0,0 --Rw 8 --out lauf/ball-kick-0.1.json
bash $K cpu4 pyro-ball0 code/pyro.py ball --L 17 --h 0.5 --om2 0.7 --T 50 --dt 0.01 --kick 0 --Rw 8 --out lauf/ball-ruhe.json
bash $K cpu4 pyro-ball2 code/pyro.py ball --L 17 --h 0.5 --om2 0.7 --T 200 --dt 0.01 --kick 0.02 --richtung 1,0,0 --Rw 8 --out lauf/ball-kick-0.02.json
date -u +%Y-%m-%dT%H:%M:%SZ > lauf/fertig-cpu4.txt
