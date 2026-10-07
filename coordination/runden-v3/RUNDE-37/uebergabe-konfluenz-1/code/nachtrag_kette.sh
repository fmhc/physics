#!/bin/bash
# UEBERGABE-KONFLUENZ-1, Nachtrag nach Sicht (beschreibend): mehr T-Faelle. Einmalige Kette je Spur, kein Dienst.
# Aufruf auf der .69: bash code/nachtrag_kette.sh <p4000a|p4000b|abschluss>
set -u
SP=$1
cd /home/fmh/fmhc-physics-remote/uebergabe-konfluenz-1 || exit 1
mkdir -p nachtrag
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SCHLUSS=$(date -u -d '2026-10-05 11:00:00' +%s)
nt() {   # nt <saat> <spur>
  local s=$1 sp=$2
  if [ "$(date -u +%s)" -ge "$SCHLUSS" ]; then echo "s$s nicht gestartet (Schlusszeit)"; return 9; fi
  bash "$K" "$sp" "uk1-nt-s$s" code/nachtrag_t.py "$s" 600 "nachtrag/konfluenz-s$s.json" > "nachtrag/nt-s$s-$sp.log" 2>&1
  local rc=$?
  echo "nt s$s spur=$sp rc=$rc $(date -u +%H:%M:%S)"
  return $rc
}
case "$SP" in
  p4000a) nt 1 p4000a; nt 3 p4000a ;;
  p4000b)
    for s in 2 4; do
      nt "$s" p4000b
      if [ $? -eq 3 ]; then nt "$s" p4000a; fi
    done ;;
  abschluss)
    bash "$K" p4000a uk1-nt-aw code/konfluenz.py auswertung --ordner nachtrag --out nachtrag/auswertung-nt.json > nachtrag/auswertung-nt.log 2>&1
    echo "auswertung-nt rc=$? $(date -u +%H:%M:%S)"
    bash "$K" p4000a uk1-nt-tab code/konfluenz.py tabellen --aw nachtrag/auswertung-nt.json --out nachtrag/tabellen-nt.md > nachtrag/tabellen-nt.log 2>&1
    echo "tabellen-nt rc=$? $(date -u +%H:%M:%S)"
    (cd nachtrag && sha256sum *.json *.md *.log > PRUEFSUMMEN.txt)
    echo "pruefsummen $(date -u +%H:%M:%S)" ;;
  *) echo "unbekannte Spur $SP"; exit 2 ;;
esac
echo "nachtrag-kette $SP fertig $(date -u +%H:%M:%S)"
