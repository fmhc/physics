#!/bin/bash
# PHASE-WAND Rauchlaeufe Runde 1 (Parameter in keinem echten Lauf: beta = 0,6; beta = 1/2 nur Rauch-Scan von R25). Code-Agent, 03.10.2026.
R=/home/fmh/fmhc-physics-remote/runde26-phase-wand
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd $R
nohup bash $K cpu r26pw-rauch-phase phase_wand.py phase --konfig rauch/k-phase-b06.json --out rauch/phase-b06.json > $R/rauch/phase-b06.log 2>&1 < /dev/null &
nohup bash $K cpu2 r26pw-rauch-selbst leiter_1d_beta.py selbsttest --konfig rauch/k-leiter-b05.json --n-rho 1501 --out rauch/selbsttest.json > $R/rauch/selbsttest.log 2>&1 < /dev/null &
nohup bash $K cpu3 r26pw-rauch-scan05 leiter_1d_beta.py scan --konfig rauch/k-leiter-b05.json --h 0.025 --D 25 --j-von 232 --j-bis 252 --n-rho 501 --out rauch/scan-b05-r25rauch.json > $R/rauch/scan-b05-r25rauch.log 2>&1 < /dev/null &
nohup bash $K cpu4 r26pw-rauch-k0 leiter_1d_beta.py k0 --konfig rauch/k-leiter-b06.json --h-liste 0.025,0.0125 --h-g210 0.025 --n-g210 401 --out rauch/k0-b06.json > $R/rauch/k0-b06.log 2>&1 < /dev/null &
nohup bash $K cpu6 r26pw-rauch-scan06 leiter_1d_beta.py scan --konfig rauch/k-leiter-b06.json --h 0.025 --D 25 --j-von 0 --j-bis 200 --n-rho 801 --out rauch/scan-b06.json > $R/rauch/scan-b06.log 2>&1 < /dev/null &
echo "rauch1 gestartet $(date --iso-8601=seconds)"
