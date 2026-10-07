#!/bin/bash
# PHASE-WAND Rauchlaeufe Runde 2 (beta = 0,6, in keinem echten Lauf): Sprossen, Regel, Formel, Vergleich. Code-Agent, 03.10.2026.
R=/home/fmh/fmhc-physics-remote/runde26-phase-wand
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd $R
nohup bash -c "bash $K cpu6 r26pw-rauch-spr leiter_1d_beta.py sprossen --konfig rauch/k-leiter-b06.json --h 0.025 --D 25 --scan rauch/scan-b06.json --scan-fein rauch/scan-b06.json --out rauch/sprossen-b06.json > $R/rauch/sprossen-b06.log 2>&1; bash $K cpu6 r26pw-rauch-regel leiter_1d_beta.py regel --konfig rauch/k-leiter-b06.json --k0 rauch/k0-b06.json --grob rauch/sprossen-b06.json --fein rauch/sprossen-b06.json --scan-fein rauch/scan-b06.json --out rauch/regel-b06.json > $R/rauch/regel-b06.log 2>&1; bash $K cpu6 r26pw-rauch-formel phase_wand.py formel --konfig rauch/k-formel-b06.json --phase rauch/phase-b06.json --out rauch/formel-b06.json > $R/rauch/formel-b06.log 2>&1; bash $K cpu6 r26pw-rauch-vgl phase_wand.py vergleich --konfig rauch/k-vergleich-b06.json --formel rauch/formel-b06.json --sprossen rauch/regel-b06.json --out rauch/vergleich-b06.json > $R/rauch/vergleich-b06.log 2>&1" > /dev/null 2>&1 < /dev/null &
echo "rauch2 gestartet $(date --iso-8601=seconds)"
