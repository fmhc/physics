#!/bin/bash
# PHASE-WAND Phase B (1D-Leiter bei beta = 1: k0, Scans, Uebersicht; Kontrolle beta = 1/2 bitgleich zu R25).
# Code-Agent, 03.10.2026. Unveraendert nach dem Einfrieren. Start erst, wenn lauf/formel-b1.json eingefroren ist.
R=/home/fmh/fmhc-physics-remote/runde26-phase-wand
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd $R
test -f lauf/formel-b1.json -a ! -w lauf/formel-b1.json || { echo "formel-b1.json nicht eingefroren"; exit 4; }
nohup bash -c "bash $K cpu r26pw-k0-b1 leiter_1d_beta.py k0 --konfig lauf/k-leiter-b1.json --h-liste 0.01,0.005 --out lauf/k0-b1.json > $R/lauf/LAUF-k0-b1.log 2>&1; bash $K cpu r26pw-repro-b05 leiter_1d_beta.py scan --konfig lauf/k-leiter-b05.json --h 0.02 --D 30 --j-von 0 --j-bis 252 --n-rho 2001 --out lauf/repro-scan-h002-b05.json > $R/lauf/LAUF-repro-scan-h002-b05.log 2>&1" > /dev/null 2>&1 < /dev/null &
nohup bash $K cpu2 r26pw-scan-g leiter_1d_beta.py scan --konfig lauf/k-leiter-b1.json --h 0.02 --D 30 --j-von 0 --j-bis 280 --n-rho 2001 --out lauf/scan-h002.json > $R/lauf/LAUF-scan-h002.log 2>&1 < /dev/null &
nohup bash $K cpu3 r26pw-scan-fa leiter_1d_beta.py scan --konfig lauf/k-leiter-b1.json --h 0.01 --D 30 --j-von 0 --j-bis 140 --n-rho 2001 --out lauf/scan-h001-a.json > $R/lauf/LAUF-scan-h001-a.log 2>&1 < /dev/null &
nohup bash $K cpu4 r26pw-scan-fb leiter_1d_beta.py scan --konfig lauf/k-leiter-b1.json --h 0.01 --D 30 --j-von 140 --j-bis 280 --n-rho 2001 --out lauf/scan-h001-b.json > $R/lauf/LAUF-scan-h001-b.log 2>&1 < /dev/null &
nohup bash $K cpu6 r26pw-survey leiter_1d_beta.py scan --konfig lauf/k-leiter-b1.json --h 0.02 --D 30 --j-von 0 --j-bis 280 --j-schritt 4 --n-rho 4001 --voll --out lauf/survey-h002.json > $R/lauf/LAUF-survey-h002.log 2>&1 < /dev/null &
echo "phase B gestartet $(date --iso-8601=seconds)"
