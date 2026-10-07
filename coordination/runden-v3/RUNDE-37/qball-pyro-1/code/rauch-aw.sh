#!/bin/bash
# Rauch 5: Auswertepfad mit Kurzlaeufen unter den Namen der Hauptlaeufe (Urteile dort ohne Bedeutung)
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd /home/fmh/fmhc-physics-remote/runde37-pyro || exit 1
R=rauch/aw
mkdir -p $R
bash $K cpu3 pyro-r5a code/pyro.py linear --nk 8 --nzufall 1000 --Lreal 2 --out $R/linear.json
bash $K cpu3 pyro-r5b code/pyro.py ring --L 3 --T 2 --dt 0.005 --rauschen 0 --out $R/ring-qp1.json
bash $K cpu3 pyro-r5c code/pyro.py ring --L 3 --T 2 --dt 0.005 --rauschen 1e-6 --out $R/ring-qp2-s1.json
bash $K cpu3 pyro-r5d code/pyro.py ring --L 3 --T 2 --dt 0.005 --rauschen 1e-6 --saat 2 --out $R/ring-qp2-s2.json
bash $K cpu3 pyro-r5e code/pyro.py ring --L 3 --T 2 --dt 0.005 --rauschen 1e-6 --kick 0.1 --out $R/ring-kick-0.1.json
bash $K cpu3 pyro-r5f code/pyro.py bogo --L 2 --a2 2.5 --out $R/bogo-L3.json
bash $K cpu3 pyro-r5g code/pyro.py ball --L 12 --h 0.5 --om2 0.8 --T 2 --dt 0.01 --kick 0.1 --Rw 8 --out $R/ball-kick-0.1.json
bash $K cpu3 pyro-r5h code/auswertung.py $R
