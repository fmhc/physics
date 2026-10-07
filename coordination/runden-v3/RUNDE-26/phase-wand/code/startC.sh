#!/bin/bash
# PHASE-WAND Phase C (Sprossen bei beta = 1 auf zwei Stufen und mit D = 40). Code-Agent, 03.10.2026. Unveraendert nach dem Einfrieren.
R=/home/fmh/fmhc-physics-remote/runde26-phase-wand
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
F=lauf/scan-h001-a.json,lauf/scan-h001-b.json
cd $R
nohup bash $K cpu2 r26pw-spr-g leiter_1d_beta.py sprossen --konfig lauf/k-leiter-b1.json --h 0.02 --D 30 --scan lauf/scan-h002.json --scan-fein $F --out lauf/sprossen-h002.json > $R/lauf/LAUF-sprossen-h002.log 2>&1 < /dev/null &
nohup bash $K cpu3 r26pw-spr-f leiter_1d_beta.py sprossen --konfig lauf/k-leiter-b1.json --h 0.01 --D 30 --scan $F --scan-fein $F --out lauf/sprossen-h001.json > $R/lauf/LAUF-sprossen-h001.log 2>&1 < /dev/null &
nohup bash $K cpu4 r26pw-spr-d40 leiter_1d_beta.py sprossen --konfig lauf/k-leiter-b1.json --h 0.01 --D 40 --scan $F --scan-fein $F --out lauf/sprossen-h001-D40.json > $R/lauf/LAUF-sprossen-h001-D40.log 2>&1 < /dev/null &
echo "phase C gestartet $(date --iso-8601=seconds)"
