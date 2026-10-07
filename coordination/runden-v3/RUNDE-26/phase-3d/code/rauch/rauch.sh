#!/bin/bash
# PHASE-3D Rauchlauf (nur Code-Test, beta = 0,6, frei gewaehlte Werte; ungueltig fuer jede Wertung). Code-Agent, 03.10.2026.
R=/home/fmh/fmhc-physics-remote/runde26-phase-3d
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd $R
nohup bash -c "bash $K cpu3 r26p3-rauch-prof phase_3d.py profile --konfig rauch/k-profile-b06.json --out rauch/profile-b06.json > $R/rauch/LAUF-profile-b06.log 2>&1; bash $K cpu3 r26p3-rauch-ausw phase_3d.py auswertung --konfig rauch/k-auswertung-b06.json --out rauch/auswertung-b06.json > $R/rauch/LAUF-auswertung-b06.log 2>&1" > /dev/null 2>&1 < /dev/null &
nohup bash $K cpu4 r26p3-rauch-phase phase_3d.py phase --konfig rauch/k-phase-b06.json --out rauch/phase-b06.json > $R/rauch/LAUF-phase-b06.log 2>&1 < /dev/null &
echo "rauch gestartet $(date --iso-8601=seconds)"
