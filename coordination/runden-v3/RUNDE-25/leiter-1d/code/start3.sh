#!/bin/bash
# LEITER-1D Phase 3 (DOP853-Gegenprobe, dann mechanische Regel). Code-Agent, 03.10.2026. Unveraendert nach dem Einfrieren.
R=/home/fmh/fmhc-physics-remote/runde25-leiter-1d
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
F=lauf/scan-h001-a.json,lauf/scan-h001-b.json
cd $R
nohup bash -c "bash $K cpu6 r25l1-dop leiter_1d.py dop853 --sprossen lauf/sprossen-h001.json --D 40 --out lauf/dop853.json > $R/lauf/LAUF-dop853.log 2>&1; bash $K cpu r25l1-regel leiter_1d.py regel --k0 lauf/k0.json --grob lauf/sprossen-h002.json --fein lauf/sprossen-h001.json --scan-fein $F --d40 lauf/sprossen-h001-D40.json --dop lauf/dop853.json --out lauf/auswertung.json > $R/lauf/LAUF-regel.log 2>&1" > /dev/null 2>&1 < /dev/null &
echo "phase 3 gestartet $(date --iso-8601=seconds)"
