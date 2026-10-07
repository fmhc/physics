#!/bin/bash
# V-1-WEITER Hauptlaeufe (nach dem Einfrieren 2026-10-04 00:30:57 CEST), nacheinander auf p4000a.
# Fenster laut Plan Abschnitt 4: rho_WB -+ 0,01, 11 Punkte (erster Kettenstart 00:31 ohne diese Argumente: Fehlstart, siehe ERGEBNIS).
cd /home/fmh/fmhc-physics-remote/runde36-v1 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
lauf() { # name eps h rtol
  bash "$K" p4000a "r36v1-$1" code/v1w.py "$2" "$3" "$4" "lauf/$1.json" 1.7734530718064692 0.01 11 > "lauf/$1.log" 2>&1
  echo "$1 rc=$? $(date -u +%H:%M:%S)" >> lauf/kette.txt
}
echo "kette start $(date -u +%H:%M:%S)" >> lauf/kette.txt
lauf A_e0      0       0.0025 1e-11
lauf A_p1e-3   0.001   0.0025 1e-11
lauf A_p3e-3   0.003   0.0025 1e-11
lauf A_p1e-2   0.01    0.0025 1e-11
lauf A_m1e-3   -0.001  0.0025 1e-11
lauf A_m3e-3   -0.003  0.0025 1e-11
lauf A_m1e-2   -0.01   0.0025 1e-11
lauf B_e0      0       0.005  1e-10
lauf B_p1e-3   0.001   0.005  1e-10
lauf B_p3e-3   0.003   0.005  1e-10
lauf B_p1e-2   0.01    0.005  1e-10
lauf B_m1e-3   -0.001  0.005  1e-10
lauf B_m3e-3   -0.003  0.005  1e-10
lauf B_m1e-2   -0.01   0.005  1e-10
# Zusatz (beschreibend, Plan Abschnitt 9)
lauf Z_m7e-3   -0.007  0.0025 1e-11
lauf Z_m1.5e-2 -0.015  0.0025 1e-11
lauf Z_m2e-2   -0.02   0.0025 1e-11
lauf Z_m2.5e-2 -0.025  0.0025 1e-11
echo "kette ende $(date -u +%H:%M:%S)" >> lauf/kette.txt
