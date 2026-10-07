#!/bin/bash
# FRUST-3D (Runde 27): echte Laeufe nach PLAN.md Abschnitt 2, je Spur nacheinander ueber kleintest.sh.
# Aufruf auf der .69 aus /home/fmh/fmhc-physics-remote/runde27-frust-3d/lauf: bash ../code/laeufe.sh
set -u
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=/home/fmh/fmhc-physics-remote/runde27-frust-3d/code/frust_3d.py
D=/home/fmh/fmhc-physics-remote/runde27-frust-3d/lauf
cd "$D" || exit 1

lauf() {  # spur name n_tet N lagerung wunsch anstoss amp
  bash "$K" "$1" "r27fr-$2" "$C" "$2" "$3" "$4" "$5" "$6" "$7" "$8" 1 1 "$D/$2.json" > "$D/$2.log" 2>&1
}

( lauf cpu e_20 5 20 E M keine 0; lauf cpu k1_G_12 1 12 G M aus 0.001; lauf cpu k1_G_20 1 20 G M aus 0.001
  lauf cpu k1_E_12 1 12 E M aus 0.001 ) &
( lauf cpu2 e_aus_20 5 20 E M aus 0.001; lauf cpu2 k1_E_20 1 20 E M aus 0.001; lauf cpu2 k4_G_12 4 12 G M aus 0.001 ) &
( lauf cpu3 ek_20 5 20 E K keine 0; lauf cpu3 k4_G_20 4 20 G M aus 0.001; lauf cpu3 k4_E_12 4 12 E M aus 0.001 ) &
( lauf cpu4 e_12 5 12 E M keine 0; lauf cpu4 e_aus_12 5 12 E M aus 0.001; lauf cpu4 k4_E_20 4 20 E M aus 0.001 ) &
( lauf cpu6 ek_12 5 12 E K keine 0; lauf cpu6 g_12 5 12 G M aus 0.001; lauf cpu6 g_20 5 20 G M aus 0.001
  lauf cpu6 g_ein_20 5 20 G M ein 0.001 ) &
wait
echo "alle fertig $(date --iso-8601=seconds)"
