#!/bin/bash
# AETHER-UHR-1 (Runde 36): Hauptlaeufe und Proben nacheinander auf einer Spur, jeder Lauf ueber kleintest.sh.
# Aufruf auf der .69 im Ordner /home/fmh/fmhc-physics-remote/runde36-aether:
#   bash code/laeufe.sh <spur: cpu3 oder cpu4> <lauf> [<lauf> ...]
# Laeufe: H-* Hauptlauf (h = 0,05, dt = 0,01, T_r = 500, T_p = 480, b = 1e-3); A-* Adiabatik-Probe (T_r = 1000);
#   G-* Gitterprobe (h = 0,025, dt = 0,005); R0 Rueckwirkungsprobe (b = 0, nur Ruhephase bis t = 480).
# Wandzeit-Abschnitte: Lauf mit Status "unterbrochen" wird mit denselben Argumenten fortgesetzt (hoechstens 4 Abschnitte).
set -u
SPUR=$1; shift
for L in "$@"; do
  case "$L" in
    H-100) ARGS="1.0 0.05 0.01 500 480 1e-3 -" ;;
    H-115) ARGS="1.15 0.05 0.01 500 480 1e-3 -" ;;
    H-170) ARGS="1.7 0.05 0.01 500 480 1e-3 -" ;;
    A-100) ARGS="1.0 0.05 0.01 1000 480 1e-3 -" ;;
    A-115) ARGS="1.15 0.05 0.01 1000 480 1e-3 -" ;;
    A-170) ARGS="1.7 0.05 0.01 1000 480 1e-3 -" ;;
    G-100) ARGS="1.0 0.025 0.005 500 480 1e-3 -" ;;
    G-115) ARGS="1.15 0.025 0.005 500 480 1e-3 -" ;;
    G-170) ARGS="1.7 0.025 0.005 500 480 1e-3 -" ;;
    R0)    ARGS="1.0 0.05 0.01 500 480 0 480" ;;
    *) echo "unbekannter Lauf $L"; continue ;;
  esac
  for versuch in 1 2 3 4; do
    bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh "$SPUR" "r36ae-$L" code/aether.py "lauf/$L" $ARGS 500 >> "lauf/$L.log" 2>&1
    if [ -f "lauf/$L.json" ] && grep -q '"status": "unterbrochen"' "lauf/$L.json"; then
      continue
    fi
    break
  done
  echo "$L fertig $(date --iso-8601=seconds)" >> "lauf/laeufe-$SPUR.txt"
done
