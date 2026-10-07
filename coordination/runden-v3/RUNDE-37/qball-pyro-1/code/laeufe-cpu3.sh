#!/bin/bash
# QBALL-PYRO-1 Hauptlaeufe, Spur cpu3 (im Ordner /home/fmh/fmhc-physics-remote/runde37-pyro)
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd /home/fmh/fmhc-physics-remote/runde37-pyro || exit 1
bash $K cpu3 pyro-h1 code/pyro.py linear --nk 48 --nzufall 100000 --Lreal 4 --out lauf/linear.json
bash $K cpu3 pyro-h2 code/pyro.py ring --L 8 --h 1 --T 100 --dt 0.005 --rauschen 0 --out lauf/ring-qp1.json
bash $K cpu3 pyro-h3 code/pyro.py ring --L 8 --h 1 --T 200 --dt 0.005 --rauschen 1e-6 --saat 1 --out lauf/ring-qp2-s1.json
bash $K cpu3 pyro-h4 code/pyro.py ring --L 8 --h 1 --T 200 --dt 0.005 --rauschen 1e-6 --saat 2 --out lauf/ring-qp2-s2.json
bash $K cpu3 pyro-h5 code/pyro.py ring --L 10 --h 1 --T 200 --dt 0.005 --rauschen 1e-6 --saat 1 --out lauf/ring-qp2-L10.json
bash $K cpu3 pyro-h6 code/pyro.py ring --L 8 --h 1 --T 200 --dt 0.0025 --rauschen 1e-6 --saat 1 --out lauf/ring-qp2-dt2.json
bash $K cpu3 pyro-h7 code/pyro.py ring --L 4 --h 1 --T 200 --dt 0.005 --rauschen 1e-6 --saat 1 --out lauf/ring-qp2-L4.json
date -u +%Y-%m-%dT%H:%M:%SZ > lauf/fertig-cpu3.txt
