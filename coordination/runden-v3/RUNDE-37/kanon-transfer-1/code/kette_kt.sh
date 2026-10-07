#!/bin/bash
# KANON-TRANSFER-1, einmalige Laufkette je Spur (kein Dienst, kein Timer).
# Aufruf auf der .69: bash code/kette_kt.sh <cpu5|cpu6|abschluss>
# Jeder Lauf ueber kleintest.sh (1 Thread, <= 600 s je Aufruf). Nur Spuren cpu5 und cpu6.
# Schlusszeit: nach 2026-10-05 14:15:00 UTC (16:15 CEST) startet kein neuer Aufruf.
set -u
SP=$1
cd /home/fmh/fmhc-physics-remote/kanon-transfer-1 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SCHLUSS=$(date -u -d '2026-10-05 14:15:00' +%s)
lauf() {   # lauf <saat> <spur>
  local s=$1 sp=$2
  if [ "$(date -u +%s)" -ge "$SCHLUSS" ]; then echo "s$s nicht gestartet (Schlusszeit)"; return 9; fi
  bash "$K" "$sp" "kt1-s$s" code/kanon.py lauf --saat "$s" --eingabe "eingabe/konfluenz-s$s.json" --out "lauf/kanon-s$s.json" > "lauf/kanon-s$s-$sp.log" 2>&1
  local rc=$?
  echo "s$s spur=$sp rc=$rc $(date -u +%H:%M:%S)"
  return $rc
}
case "$SP" in
  cpu5) lauf 1 cpu5; lauf 3 cpu5 ;;
  cpu6) lauf 2 cpu6; lauf 4 cpu6 ;;
  abschluss)
    if [ "$(date -u +%s)" -ge "$SCHLUSS" ]; then echo "abschluss nicht gestartet (Schlusszeit)"; exit 9; fi
    bash "$K" cpu5 kt1-aw code/kanon.py auswertung --ordner lauf --out lauf/auswertung.json > lauf/auswertung.log 2>&1
    echo "auswertung rc=$? $(date -u +%H:%M:%S)"
    bash "$K" cpu5 kt1-tab code/kanon.py tabellen --aw lauf/auswertung.json --out lauf/tabellen.md > lauf/tabellen.log 2>&1
    echo "tabellen rc=$? $(date -u +%H:%M:%S)"
    (cd lauf && sha256sum *.json *.md *.log > PRUEFSUMMEN.txt)
    echo "pruefsummen $(date -u +%H:%M:%S)" ;;
  *) echo "unbekannte Spur $SP"; exit 2 ;;
esac
echo "kette $SP fertig $(date -u +%H:%M:%S)"
