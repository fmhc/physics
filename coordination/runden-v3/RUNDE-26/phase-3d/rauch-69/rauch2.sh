#!/bin/bash
# PHASE-3D Rauchlauf 2 (nur Code-Test, beta = 0,6, frei gewaehlte Werte; ungueltig fuer jede Wertung). Code-Agent, 03.10.2026.
R=/home/fmh/fmhc-physics-remote/runde26-phase-3d
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd $R
nohup bash $K cpu4 r26p3-rauch2-prof phase_3d.py profile --konfig rauch/k-profile2-b06.json --out rauch/profile2-b06.json > $R/rauch/LAUF-profile2-b06.log 2>&1 < /dev/null &
echo "rauch2 gestartet $(date --iso-8601=seconds)"
