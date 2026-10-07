#!/bin/bash
# UEBERGABE-KONFLUENZ-1, einmalige Laufkette je Spur (kein Dienst, kein Timer).
# Aufruf auf der .69: bash code/kette.sh <p4000a|p4000b|abschluss>
# Jeder Lauf ueber kleintest.sh (1 Thread, <= 600 s je Aufruf). Ist p4000b gesperrt (rc = 3, WM-1-MB laeuft), laeuft die
# Saat auf p4000a. Schlusszeit: nach 2026-10-05 11:00:00 UTC (13:00 CEST) startet kein neuer Aufruf.
set -u
SP=$1
cd /home/fmh/fmhc-physics-remote/uebergabe-konfluenz-1 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SCHLUSS=$(date -u -d '2026-10-05 11:00:00' +%s)
lauf() {   # lauf <saat> <spur>
  local s=$1 sp=$2
  if [ "$(date -u +%s)" -ge "$SCHLUSS" ]; then echo "s$s nicht gestartet (Schlusszeit)"; return 9; fi
  bash "$K" "$sp" "uk1-s$s" code/konfluenz.py lauf --saat "$s" --out "lauf/konfluenz-s$s.json" > "lauf/konfluenz-s$s-$sp.log" 2>&1
  local rc=$?
  echo "s$s spur=$sp rc=$rc $(date -u +%H:%M:%S)"
  return $rc
}
case "$SP" in
  p4000a) lauf 1 p4000a; lauf 3 p4000a ;;
  p4000b)
    for s in 2 4; do
      lauf "$s" p4000b
      if [ $? -eq 3 ]; then lauf "$s" p4000a; fi
    done ;;
  abschluss)
    bash "$K" p4000a uk1-hf code/konfluenz.py haeufigkeit --ordner /home/fmh/fmhc-physics-remote/takt-dynamik-1/lauf --out lauf/haeufigkeit.json > lauf/haeufigkeit.log 2>&1
    echo "haeufigkeit rc=$? $(date -u +%H:%M:%S)"
    bash "$K" p4000a uk1-aw code/konfluenz.py auswertung --ordner lauf --haeufigkeit lauf/haeufigkeit.json --out lauf/auswertung.json > lauf/auswertung.log 2>&1
    echo "auswertung rc=$? $(date -u +%H:%M:%S)"
    bash "$K" p4000a uk1-tab code/konfluenz.py tabellen --aw lauf/auswertung.json --out lauf/tabellen.md > lauf/tabellen.log 2>&1
    echo "tabellen rc=$? $(date -u +%H:%M:%S)"
    (cd lauf && sha256sum *.json *.md *.log > PRUEFSUMMEN.txt)
    echo "pruefsummen $(date -u +%H:%M:%S)" ;;
  *) echo "unbekannte Spur $SP"; exit 2 ;;
esac
echo "kette $SP fertig $(date -u +%H:%M:%S)"
