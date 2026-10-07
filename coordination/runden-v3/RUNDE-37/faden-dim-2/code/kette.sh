#!/bin/bash
# FADEN-DIM-2 (Runde 43): einmalige Laufkette je Spur, von Hand gestartet (kein Dienst, kein Timer, kein Hook).
# Aufruf auf der .69: bash kette.sh cpu   bzw.   bash kette.sh cpu10
# Jeder Lauf ueber kleintest.sh (<= 600 s, 1 Thread, 4 GB). Kein neuer Lauf nach SCHLUSS (20:45:00 UTC = 22:45:00 CEST).
set -u
SPUR=${1:?Spur cpu oder cpu10}
R=/home/fmh/fmhc-physics-remote/faden-dim-2
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
P=$R/code/fd2.py
SCHLUSS=$(date -u -d "2026-10-04 20:45:00 UTC" +%s)
KL=$R/lauf/kette-$SPUR.log
run() {
  local name=$1; shift
  if [ "$(date -u +%s)" -ge "$SCHLUSS" ]; then echo "$name uebersprungen (Schluss) $(date -u +%T)" >> "$KL"; return; fi
  echo "$name start $(date -u +%T)" >> "$KL"
  bash "$K" "$SPUR" "$name" "$P" lauf --zellen "$1" --out "$R/lauf/$name.jsonl" > "$R/lauf/$name.log" 2>&1
  echo "$name ende rc=$? $(date -u +%T)" >> "$KL"
}
cd "$R/lauf" || exit 1
echo "kette $SPUR start $(date -u +%T)" >> "$KL"
case "$SPUR" in
  cpu)
    run fd2a RP:4:64:kal:1024:0,RP:4:48:kal:1024:0
    run fd2b RP:4:64:kal:1024:1,RP:4:16:kal:3072:0,RP:4:24:kal:3072:0
    ;;
  cpu10)
    run fd2c RP:4:64:kal:1024:2,RP:4:48:kal:1024:1
    run fd2d RP:4:48:kal:1024:2,RP:4:32:kal:3072:0,G:4:32:0:8192:0,G:4:48:0:8192:0,G:4:64:0:8192:0,RP:5:8:kal:4096:0,RP:5:12:kal:4096:0,RP:5:16:kal:4096:0,RP:5:24:kal:4096:0
    ;;
  *) echo "unbekannte Spur $SPUR" >> "$KL"; exit 2 ;;
esac
echo "kette $SPUR ende $(date -u +%T)" >> "$KL"
