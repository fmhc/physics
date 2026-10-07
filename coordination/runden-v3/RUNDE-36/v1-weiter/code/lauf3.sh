#!/bin/bash
# V-1-WEITER, Kette 3 (2026-10-04 ~00:53 CEST): Rest der B-Laeufe eps > 0 (Hintergrundende 47 wie A),
# dann alle eps < 0 mit Hintergrundende 90 (Korrektur 2, siehe ERGEBNIS), Probe eps = +1e-2 mit Ende 90, Zusatz.
cd /home/fmh/fmhc-physics-remote/runde36-v1 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
lauf() { # name eps h rtol xr
  bash "$K" p4000a "r36v1-$1" code/v1w.py "$2" "$3" "$4" "lauf/$1.json" 1.7734530718064692 0.01 11 1.0 "$5" > "lauf/$1.log" 2>&1
  echo "$1 rc=$? $(date -u +%H:%M:%S)" >> lauf/kette.txt
}
echo "kette3 start $(date -u +%H:%M:%S)" >> lauf/kette.txt
lauf A_m3e-3x  -0.003  0.0025 1e-11 90
lauf B_p3e-3    0.003  0.005  1e-10 47
lauf B_p1e-2    0.01   0.005  1e-10 47
lauf A_m1e-2x  -0.01   0.0025 1e-11 90
lauf A_m1e-3x  -0.001  0.0025 1e-11 90
lauf B_m3e-3x  -0.003  0.005  1e-10 90
lauf B_m1e-2x  -0.01   0.005  1e-10 90
lauf B_m1e-3x  -0.001  0.005  1e-10 90
lauf A_p1e-2x   0.01   0.0025 1e-11 90
lauf Z_m7e-3x   -0.007 0.0025 1e-11 90
lauf Z_m1.5e-2x -0.015 0.0025 1e-11 90
lauf Z_m2e-2x   -0.02  0.0025 1e-11 90
lauf Z_m2.5e-2x -0.025 0.0025 1e-11 90
echo "kette ende $(date -u +%H:%M:%S)" >> lauf/kette.txt
