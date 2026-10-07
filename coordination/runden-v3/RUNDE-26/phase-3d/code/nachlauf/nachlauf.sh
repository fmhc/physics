#!/bin/bash
# PHASE-3D Nachlauf (offen benannte Abweichung nach dem Einfrieren): phase beta = 1/2 brach bei rho_1 = 1,7446 ab
# (ebene Wand bei omega_min aussen offen fuer rho > 1 + omega_min). Neu: phase_3d_nach.py (eigene Datei), dann
# auswertung beta = 1/2 mit der neuen Phase-Datei. Haupt-Delta, K-Profil und Regeln unveraendert. Code-Agent, 03.10.2026.
R=/home/fmh/fmhc-physics-remote/runde26-phase-3d
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd $R
nohup bash -c "bash $K cpu4 r26p3-nach-phase-b05 phase_3d_nach.py phase --konfig lauf/k-phase-b05-nach.json --out lauf/phase-b05-nach.json > $R/lauf/LAUF-phase-b05-nach.log 2>&1; bash $K cpu4 r26p3-nach-ausw-b05 phase_3d_nach.py auswertung --konfig lauf/k-auswertung-b05-nach.json --out lauf/auswertung-b05-nach.json > $R/lauf/LAUF-auswertung-b05-nach.log 2>&1" > /dev/null 2>&1 < /dev/null &
echo "nachlauf gestartet $(date --iso-8601=seconds)"
