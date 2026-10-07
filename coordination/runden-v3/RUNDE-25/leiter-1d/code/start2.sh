#!/bin/bash
# LEITER-1D Phase 2 (Sprossen auf zwei Stufen und mit D = 40). Code-Agent, 03.10.2026. Unveraendert nach dem Einfrieren.
R=/home/fmh/fmhc-physics-remote/runde25-leiter-1d
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
F=lauf/scan-h001-a.json,lauf/scan-h001-b.json
cd $R
nohup bash $K cpu2 r25l1-spr-g leiter_1d.py sprossen --h 0.02 --D 30 --scan lauf/scan-h002.json --scan-fein $F --out lauf/sprossen-h002.json > $R/lauf/LAUF-sprossen-h002.log 2>&1 < /dev/null &
nohup bash $K cpu3 r25l1-spr-f leiter_1d.py sprossen --h 0.01 --D 30 --scan $F --scan-fein $F --out lauf/sprossen-h001.json > $R/lauf/LAUF-sprossen-h001.log 2>&1 < /dev/null &
nohup bash $K cpu4 r25l1-spr-d40 leiter_1d.py sprossen --h 0.01 --D 40 --scan $F --scan-fein $F --out lauf/sprossen-h001-D40.json > $R/lauf/LAUF-sprossen-h001-D40.log 2>&1 < /dev/null &
echo "phase 2 gestartet $(date --iso-8601=seconds)"
