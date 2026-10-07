#!/bin/bash
# TT-ISO-1 (Runde 43): einmalige Laufkette auf Spur cpu3, von Hand gestartet (kein Dienst, kein Timer, kein Hook).
# Jeder Lauf ueber kleintest.sh (<= 600 s, 1 Thread). Kein neuer Lauf nach SCHLUSS (21:00:00 UTC = 23:00:00 CEST).
set -u
R=/home/fmh/fmhc-physics-remote/tt-iso-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
P=$R/code/tti.py
SCHLUSS=$(date -u -d "2026-10-04 21:00:00 UTC" +%s)
KL=$R/lauf/kette-cpu3.log
run() {
  local name=$1; shift
  if [ "$(date -u +%s)" -ge "$SCHLUSS" ]; then echo "$name uebersprungen (Schluss) $(date -u +%T)" >> "$KL"; return; fi
  echo "$name start $(date -u +%T)" >> "$KL"
  bash "$K" cpu3 "$name" "$@" > "$R/lauf/$name.log" 2>&1
  echo "$name ende rc=$? $(date -u +%T)" >> "$KL"
}
cd "$R/lauf"
echo "kette start $(date -u +%T)" >> "$KL"
run ttiK "$P" kontrolle --ref "$R/ref/kinetik.json" --out "$R/lauf/kontrolle.json"
run ttiGV1 "$P" gitter --netz V --paarung A1R1 --npkt 9 --out "$R/lauf/gitter-V-A1R1.json"
run ttiVV1 "$P" verfeinern --netz V --paarung A1R1 --gitterdatei "$R/lauf/gitter-V-A1R1.json" --ng 5 --nmfaktor 0.67 --out "$R/lauf/verf-V-A1R1.json"
run ttiGS1 "$P" gitter --netz S --paarung A1R1 --npkt 9 --out "$R/lauf/gitter-S-A1R1.json"
run ttiVS1 "$P" verfeinern --netz S --paarung A1R1 --gitterdatei "$R/lauf/gitter-S-A1R1.json" --ng 5 --nmfaktor 0.67 --out "$R/lauf/verf-S-A1R1.json"
run ttiGS2 "$P" gitter --netz S --paarung A2R1 --npkt 9 --out "$R/lauf/gitter-S-A2R1.json"
run ttiVS2 "$P" verfeinern --netz S --paarung A2R1 --gitterdatei "$R/lauf/gitter-S-A2R1.json" --ng 5 --nmfaktor 0.67 --out "$R/lauf/verf-S-A2R1.json"
echo "kette ende $(date -u +%T)" >> "$KL"
