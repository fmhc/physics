#!/bin/bash
# SPLITTER-FREI-1, Nachtrag nach Sicht (beschreibend, kein Urteil): Formschranke q_s = 0,1 / 0,25 / 0,3 fuer Saat 1,
# je hm --rauch (Richtung [100], |k| = 1e-2 und 2e-2) mit dem eingefrorenen code/sf.py. Aufruf: bash nachtrag-q.sh <spur> <qs...>
set -u
W=/home/fmh/fmhc-physics-remote/splitter-frei-1
KT=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SP=$1; shift
cd "$W" || exit 1
mkdir -p "$W/nachtrag"
for q in "$@"; do
  n=q$(echo "$q" | tr -d .)
  bash "$KT" "$SP" "sf-nt-bau-$n" code/sf.py bau --saaten 1 --qs "$q" --zeit 480 --r0 0.05 --rmax 0.4 --out "nachtrag/bau-$n-s1.json" > "$W/nachtrag/bau-$n-s1.log" 2>&1
  echo "bau-$n-s1 rc=$? $(date --iso-8601=seconds)" >> "$W/nachtrag/kette-$SP.txt"
  bash "$KT" "$SP" "sf-nt-hm-$n" code/sf.py hm --art sf --saat 1 --bau "nachtrag/bau-$n-s1.json" --rauch --out "nachtrag/hm-$n-s1.json" > "$W/nachtrag/hm-$n-s1.log" 2>&1
  echo "hm-$n-s1 rc=$? $(date --iso-8601=seconds)" >> "$W/nachtrag/kette-$SP.txt"
done
echo "ende $(date --iso-8601=seconds)" >> "$W/nachtrag/kette-$SP.txt"
