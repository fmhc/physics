#!/bin/bash
# Rauchlaeufe LEITER-1D (Parameter in keinem echten Lauf), Code-Agent, 03.10.2026
R=/home/fmh/fmhc-physics-remote/runde25-leiter-1d
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd $R
nohup bash $K cpu r25l1-rauch-selbst leiter_1d.py selbsttest --n-rho 1501 --out rauch/selbsttest.json > $R/rauch/selbsttest.log 2>&1 < /dev/null &
nohup bash $K cpu2 r25l1-rauch-k0 leiter_1d.py k0 --h-liste 0.025,0.0125 --h-g210 0.025 --n-g210 401 --out rauch/k0.json > $R/rauch/k0.log 2>&1 < /dev/null &
nohup bash $K cpu3 r25l1-rauch-scan leiter_1d.py scan --h 0.025 --D 25 --j-von 232 --j-bis 252 --n-rho 501 --out rauch/scan.json > $R/rauch/scan.log 2>&1 < /dev/null &
echo gestartet
