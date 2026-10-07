#!/bin/bash
# Rauchlaeufe Runde 2 LEITER-1D (Parameter in keinem echten Lauf), Code-Agent, 03.10.2026
R=/home/fmh/fmhc-physics-remote/runde25-leiter-1d
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd $R
nohup bash $K cpu r25l1-rauch-k0b leiter_1d.py k0 --h-liste 0.025,0.0125 --h-g210 0.025 --n-g210 401 --out rauch/k0b.json > $R/rauch/k0b.log 2>&1 < /dev/null &
nohup bash $K cpu2 r25l1-rauch-scanb leiter_1d.py scan --h 0.025 --D 25 --j-von 232 --j-bis 252 --n-rho 501 --out rauch/scanb.json > $R/rauch/scanb.log 2>&1 < /dev/null &
nohup bash $K cpu3 r25l1-rauch-zeit leiter_1d.py scan --h 0.0125 --D 25 --j-von 247 --j-bis 252 --n-rho 2001 --out rauch/scan-zeit.json > $R/rauch/scan-zeit.log 2>&1 < /dev/null &
nohup bash $K cpu4 r25l1-rauch-spr leiter_1d.py sprossen --h 0.025 --D 25 --scan rauch/scan.json --scan-fein rauch/scan.json --out rauch/sprossen.json > $R/rauch/sprossen.log 2>&1 < /dev/null &
echo gestartet
