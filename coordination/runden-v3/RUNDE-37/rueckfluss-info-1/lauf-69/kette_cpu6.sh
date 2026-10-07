#!/bin/bash
# RUECKFLUSS-INFO-1: Kette Spur cpu6 (F2, N2, L8), je Lauf ein kleintest.sh-Aufruf
R=/home/fmh/fmhc-physics-remote/runde45-rueckfluss-info
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
O=$R/lauf
cd $R/code || exit 1
bash $K cpu6 ri-f2 rueckfluss_info.py --modus fest --N 96 --sigma 4 --W '2*pi' --saaten 6 --saatbasis 46000 --out $O/haupt_F2.json > $O/haupt_F2.log 2>&1
bash $K cpu6 ri-n2 rueckfluss_info.py --modus neu --N 96 --sigma 4 --W '2*pi' --M 8 --saatbasis 48000 --out $O/haupt_N2.json > $O/haupt_N2.log 2>&1
bash $K cpu6 ri-l8 rueckfluss_info.py --modus leiter --N 128 --sigma 8 --W '2*pi' --saaten 6 --saatbasis 50000 --out $O/haupt_L8.json > $O/haupt_L8.log 2>&1
