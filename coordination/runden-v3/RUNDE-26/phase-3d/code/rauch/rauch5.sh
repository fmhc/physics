#!/bin/bash
# PHASE-3D Rauchlauf 5 und 6 (nur Code-Test, beta = 0,6, frei gewaehlte Werte; ungueltig fuer jede Wertung). Code-Agent, 03.10.2026.
R=/home/fmh/fmhc-physics-remote/runde26-phase-3d
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd $R
nohup bash -c "bash $K cpu4 r26p3-rauch5-phase phase_3d.py phase --konfig rauch/k-phase-b06.json --out rauch/phase5-b06.json > $R/rauch/LAUF-phase5-b06.log 2>&1; bash $K cpu4 r26p3-rauch5-prof phase_3d.py profile --konfig rauch/k-profile5-b06.json --out rauch/profile5-b06.json > $R/rauch/LAUF-profile5-b06.log 2>&1; bash $K cpu4 r26p3-rauch5-ausw phase_3d.py auswertung --konfig rauch/k-auswertung5-b06.json --out rauch/auswertung5-b06.json > $R/rauch/LAUF-auswertung5-b06.log 2>&1" > /dev/null 2>&1 < /dev/null &
nohup bash $K cpu3 r26p3-rauch6-prof phase_3d.py profile --konfig rauch/k-profile6-b06.json --out rauch/profile6-b06.json > $R/rauch/LAUF-profile6-b06.log 2>&1 < /dev/null &
echo "rauch5 gestartet $(date --iso-8601=seconds)"
