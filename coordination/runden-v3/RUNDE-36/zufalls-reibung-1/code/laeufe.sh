#!/bin/bash
# ZUFALLS-REIBUNG-1 (Runde 36): Laeufe nacheinander auf einer Spur, jeder einzeln ueber kleintest.sh (Lock je Spur,
# 1 Thread, MemoryMax 4G, Abbruch nach 600 s). Kein '&': der naechste Lauf startet erst nach dem vorigen.
# Aufruf auf der .69 im Ordner /home/fmh/fmhc-physics-remote/runde36-reibung:
#   bash code/laeufe.sh <spur: cpu oder cpu6> <ordner> <t_end> <lauf> [<lauf> ...]
# Laufnamen: v<v>_s0 (sigma = 0, Saat 1), v<v>_s<sigma>_<A|B|C> (Saat 1|2|3); Zusatz _dt2 = halber Zeitschritt 0,01.
set -u
SPUR=$1; ORD=$2; TEND=$3; shift 3
for L in "$@"; do
  v=$(echo "$L" | sed -E 's/^v([0-9.]+)_.*/\1/')
  s=$(echo "$L" | sed -E 's/^v[0-9.]+_s([0-9.]+).*/\1/')
  saat=1
  case "$L" in *_B|*_B_dt2) saat=2 ;; *_C|*_C_dt2) saat=3 ;; esac
  dt=0.02
  case "$L" in *_dt2) dt=0.01 ;; esac
  bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh "$SPUR" "r36zr-$L" code/reibung.py "$ORD/$L" "$v" "$s" "$saat" "$TEND" "$dt" > "$ORD/$L.log" 2>&1
  echo "$L rc=$? v=$v sigma=$s saat=$saat dt=$dt $(date -u '+%Y-%m-%dT%H:%M:%SZ')" >> "$ORD/laeufe-$SPUR.txt"
done
