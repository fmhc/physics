#!/bin/bash
# PHASE-WAND Phase D (DOP853-Gegenprobe, Regel mit PW2, Vergleich PW3 gegen die eingefrorene Vorhersage). Code-Agent, 03.10.2026.
# Unveraendert nach dem Einfrieren.
R=/home/fmh/fmhc-physics-remote/runde26-phase-wand
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
F=lauf/scan-h001-a.json,lauf/scan-h001-b.json
cd $R
nohup bash -c "bash $K cpu6 r26pw-dop leiter_1d_beta.py dop853 --konfig lauf/k-leiter-b1.json --sprossen lauf/sprossen-h001.json --D 40 --out lauf/dop853.json > $R/lauf/LAUF-dop853.log 2>&1; bash $K cpu r26pw-regel leiter_1d_beta.py regel --konfig lauf/k-leiter-b1.json --k0 lauf/k0-b1.json --grob lauf/sprossen-h002.json --fein lauf/sprossen-h001.json --scan-fein $F --d40 lauf/sprossen-h001-D40.json --dop lauf/dop853.json --out lauf/auswertung-b1.json > $R/lauf/LAUF-regel.log 2>&1; bash $K cpu r26pw-pw3 phase_wand.py vergleich --konfig lauf/k-vergleich-pw3.json --formel lauf/formel-b1.json --sprossen lauf/auswertung-b1.json --out lauf/vergleich-pw3.json > $R/lauf/LAUF-vergleich-pw3.log 2>&1" > /dev/null 2>&1 < /dev/null &
echo "phase D gestartet $(date --iso-8601=seconds)"
