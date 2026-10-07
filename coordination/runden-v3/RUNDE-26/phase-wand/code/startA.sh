#!/bin/bash
# PHASE-WAND Phase A (Phase phi bei beta = 1/2 und 1, Formel, PW1, Vorhersage beta = 1). Code-Agent, 03.10.2026.
# Unveraendert nach dem Einfrieren. Die Vorhersagedatei lauf/formel-b1.json wird danach eingefroren (chmod a-w),
# bevor startB.sh laeuft.
R=/home/fmh/fmhc-physics-remote/runde26-phase-wand
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd $R
nohup bash -c "bash $K cpu r26pw-phase-b05 phase_wand.py phase --konfig lauf/k-phase-b05.json --out lauf/phase-b05.json > $R/lauf/LAUF-phase-b05.log 2>&1; bash $K cpu r26pw-formel-b05 phase_wand.py formel --konfig lauf/k-formel-b05.json --phase lauf/phase-b05.json --out lauf/formel-b05.json > $R/lauf/LAUF-formel-b05.log 2>&1; bash $K cpu r26pw-pw1 phase_wand.py vergleich --konfig lauf/k-vergleich-pw1.json --formel lauf/formel-b05.json --sprossen lauf/r25-auswertung.json --out lauf/vergleich-pw1.json > $R/lauf/LAUF-vergleich-pw1.log 2>&1" > /dev/null 2>&1 < /dev/null &
nohup bash -c "bash $K cpu2 r26pw-phase-b1 phase_wand.py phase --konfig lauf/k-phase-b1.json --out lauf/phase-b1.json > $R/lauf/LAUF-phase-b1.log 2>&1; bash $K cpu2 r26pw-formel-b1 phase_wand.py formel --konfig lauf/k-formel-b1.json --phase lauf/phase-b1.json --out lauf/formel-b1.json > $R/lauf/LAUF-formel-b1.log 2>&1" > /dev/null 2>&1 < /dev/null &
echo "phase A gestartet $(date --iso-8601=seconds)"
