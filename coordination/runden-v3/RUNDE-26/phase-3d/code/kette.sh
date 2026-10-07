#!/bin/bash
# PHASE-3D: Kette der echten Laeufe (Profile und Phase parallel, danach Auswertung). Code-Agent, 03.10.2026.
# Unveraendert nach dem Einfrieren. Aufruf nur ueber start.sh.
R=/home/fmh/fmhc-physics-remote/runde26-phase-3d
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd $R
echo "kette beginn $(date --iso-8601=seconds)"
bash $K cpu  r26p3-prof-b05-a phase_3d.py profile --konfig lauf/k-profile-b05-a.json --out lauf/profile-b05-a.json > $R/lauf/LAUF-profile-b05-a.log 2>&1 &
bash $K cpu2 r26p3-prof-b05-b phase_3d.py profile --konfig lauf/k-profile-b05-b.json --out lauf/profile-b05-b.json > $R/lauf/LAUF-profile-b05-b.log 2>&1 &
bash $K cpu3 r26p3-prof-b05-c phase_3d.py profile --konfig lauf/k-profile-b05-c.json --out lauf/profile-b05-c.json > $R/lauf/LAUF-profile-b05-c.log 2>&1 &
bash $K cpu6 r26p3-prof-b1-b phase_3d.py profile --konfig lauf/k-profile-b1-b.json --out lauf/profile-b1-b.json > $R/lauf/LAUF-profile-b1-b.log 2>&1 &
( bash $K cpu4 r26p3-phase-b05 phase_3d.py phase --konfig lauf/k-phase-b05.json --out lauf/phase-b05.json > $R/lauf/LAUF-phase-b05.log 2>&1
  bash $K cpu4 r26p3-phase-b1 phase_3d.py phase --konfig lauf/k-phase-b1.json --out lauf/phase-b1.json > $R/lauf/LAUF-phase-b1.log 2>&1
  bash $K cpu4 r26p3-prof-b1-a phase_3d.py profile --konfig lauf/k-profile-b1-a.json --out lauf/profile-b1-a.json > $R/lauf/LAUF-profile-b1-a.log 2>&1 ) &
wait
echo "profile und phase fertig $(date --iso-8601=seconds)"
bash $K cpu4 r26p3-ausw-b05 phase_3d.py auswertung --konfig lauf/k-auswertung-b05.json --out lauf/auswertung-b05.json > $R/lauf/LAUF-auswertung-b05.log 2>&1
bash $K cpu4 r26p3-ausw-b1 phase_3d.py auswertung --konfig lauf/k-auswertung-b1.json --out lauf/auswertung-b1.json > $R/lauf/LAUF-auswertung-b1.log 2>&1
echo "kette ende $(date --iso-8601=seconds)"
