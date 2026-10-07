#!/bin/bash
# TT-ISO-1 (Runde 43): einmalige Laufkette auf Spur cpu5, von Hand gestartet (kein Dienst, kein Timer, kein Hook).
# Jeder Lauf ueber kleintest.sh (<= 600 s, 1 Thread). Kein neuer Lauf nach SCHLUSS (21:00:00 UTC = 23:00:00 CEST).
set -u
R=/home/fmh/fmhc-physics-remote/tt-iso-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
P=$R/code/tti.py
SCHLUSS=$(date -u -d "2026-10-04 21:00:00 UTC" +%s)
KL=$R/lauf/kette-cpu5.log
run() {
  local name=$1; shift
  if [ "$(date -u +%s)" -ge "$SCHLUSS" ]; then echo "$name uebersprungen (Schluss) $(date -u +%T)" >> "$KL"; return; fi
  echo "$name start $(date -u +%T)" >> "$KL"
  bash "$K" cpu5 "$name" "$@" > "$R/lauf/$name.log" 2>&1
  echo "$name ende rc=$? $(date -u +%T)" >> "$KL"
}
cd "$R/lauf"
echo "kette start $(date -u +%T)" >> "$KL"
run ttiGV3 "$P" gitter --netz V --paarung A3R2 --npkt 9 --out "$R/lauf/gitter-V-A3R2.json"
run ttiVV3 "$P" verfeinern --netz V --paarung A3R2 --gitterdatei "$R/lauf/gitter-V-A3R2.json" --ng 5 --nmfaktor 0.67 --out "$R/lauf/verf-V-A3R2.json"
run ttiGV2 "$P" gitter --netz V --paarung A2R1 --npkt 9 --out "$R/lauf/gitter-V-A2R1.json"
run ttiVV2 "$P" verfeinern --netz V --paarung A2R1 --gitterdatei "$R/lauf/gitter-V-A2R1.json" --ng 5 --nmfaktor 0.67 --out "$R/lauf/verf-V-A2R1.json"
run ttiGS3 "$P" gitter --netz S --paarung A3R2 --npkt 9 --out "$R/lauf/gitter-S-A3R2.json"
run ttiVS3 "$P" verfeinern --netz S --paarung A3R2 --gitterdatei "$R/lauf/gitter-S-A3R2.json" --ng 5 --nmfaktor 0.67 --out "$R/lauf/verf-S-A3R2.json"
echo "kette ende $(date -u +%T)" >> "$KL"
