#!/bin/bash
# LEITER-1D Phase 1 (k0, Scans, Uebersicht). Code-Agent, 03.10.2026. Unveraendert nach dem Einfrieren.
R=/home/fmh/fmhc-physics-remote/runde25-leiter-1d
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd $R
nohup bash $K cpu r25l1-k0 leiter_1d.py k0 --h-liste 0.01,0.005 --h-g210 0.01 --n-g210 2001 --out lauf/k0.json > $R/lauf/LAUF-k0.log 2>&1 < /dev/null &
nohup bash $K cpu2 r25l1-scan-g leiter_1d.py scan --h 0.02 --D 30 --j-von 0 --j-bis 252 --n-rho 2001 --out lauf/scan-h002.json > $R/lauf/LAUF-scan-h002.log 2>&1 < /dev/null &
nohup bash $K cpu3 r25l1-scan-fa leiter_1d.py scan --h 0.01 --D 30 --j-von 0 --j-bis 126 --n-rho 2001 --out lauf/scan-h001-a.json > $R/lauf/LAUF-scan-h001-a.log 2>&1 < /dev/null &
nohup bash $K cpu4 r25l1-scan-fb leiter_1d.py scan --h 0.01 --D 30 --j-von 126 --j-bis 252 --n-rho 2001 --out lauf/scan-h001-b.json > $R/lauf/LAUF-scan-h001-b.log 2>&1 < /dev/null &
nohup bash $K cpu6 r25l1-survey leiter_1d.py scan --h 0.02 --D 30 --j-von 0 --j-bis 252 --j-schritt 4 --n-rho 4001 --voll --out lauf/survey-h002.json > $R/lauf/LAUF-survey-h002.log 2>&1 < /dev/null &
echo "phase 1 gestartet $(date --iso-8601=seconds)"
