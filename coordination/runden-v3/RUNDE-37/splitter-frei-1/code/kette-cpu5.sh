#!/bin/bash
# SPLITTER-FREI-1, Laufkette Spur cpu5 (einmal von Hand gestartet). Jeder Schritt ueber kleintest.sh (<= 600 s).
# Saaten 1 und 3. Schlusszeit: nach 2026-10-05 11:20:00 UTC (13:20 CEST) startet kein Lauf.
set -u
W=/home/fmh/fmhc-physics-remote/splitter-frei-1
KT=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SP=cpu5
SCHLUSS=$(date -u -d '2026-10-05 11:20:00' +%s)
cd "$W" || exit 1
lauf() {
  n=$1; shift
  if [ "$(date -u +%s)" -ge "$SCHLUSS" ]; then echo "$n nicht gestartet (Schlusszeit) $(date --iso-8601=seconds)" >> "$W/lauf/kette-$SP.txt"; return; fi
  bash "$KT" "$SP" "sf-$n" code/sf.py "$@" > "$W/lauf/$n.log" 2>&1
  echo "$n rc=$? $(date --iso-8601=seconds)" >> "$W/lauf/kette-$SP.txt"
}
echo "start $(date --iso-8601=seconds)" >> "$W/lauf/kette-$SP.txt"
lauf bau-s13 bau --saaten 1,3 --qs 0.2 --zeit 270 --r0 0.05 --rmax 0.4 --out lauf/bau-s13.json
for s in 1 3; do
  lauf hm-orig-s$s-a hm --art orig --saat $s --ridx 0-6 --out lauf/hm-orig-s$s-a.json
  lauf hm-orig-s$s-b hm --art orig --saat $s --ridx 7-12 --out lauf/hm-orig-s$s-b.json
  lauf hm-sf-s$s-a hm --art sf --saat $s --bau lauf/bau-s13.json --ridx 0-6 --out lauf/hm-sf-s$s-a.json
  lauf hm-sf-s$s-b hm --art sf --saat $s --bau lauf/bau-s13.json --ridx 7-12 --out lauf/hm-sf-s$s-b.json
  lauf lr-orig-s$s lr --art orig --saat $s --out lauf/lr-orig-s$s.json
  lauf lr-sf-s$s lr --art sf --saat $s --bau lauf/bau-s13.json --out lauf/lr-sf-s$s.json
done
echo "ende $(date --iso-8601=seconds)" >> "$W/lauf/kette-$SP.txt"
