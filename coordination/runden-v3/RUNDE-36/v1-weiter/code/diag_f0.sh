#!/bin/bash
# V-1-WEITER, Diagnose nach dem Einfrieren (2026-10-04 ~00:58 CEST): eps nur in den Schwankungen, Hintergrund f0.
# Frage: Stammt die gemessene Restkopplung bei eps < 0 aus dem FD-Hintergrund (Schwanzwellen) oder aus der Wand selbst?
cd /home/fmh/fmhc-physics-remote/runde36-v1 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
lauf() { # name eps
  bash "$K" p4000a "r36v1-$1" code/v1w.py "$2" 0.0025 1e-11 "lauf/$1.json" 1.7734530718064692 0.01 11 1.0 90 f0 > "lauf/$1.log" 2>&1
  echo "$1 rc=$? $(date -u +%H:%M:%S)" >> lauf/kette.txt
}
lauf D_m1e-2f0   -0.01
lauf D_m3e-3f0   -0.003
lauf D_m2e-2f0   -0.02
lauf D_m1.5e-2f0 -0.015
lauf D_m1e-3f0   -0.001
echo "diag ende $(date -u +%H:%M:%S)" >> lauf/kette.txt
