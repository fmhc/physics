#!/bin/bash
# kette.sh <spur> <auftragsdatei>: Auftraege nacheinander ueber kleintest.sh (je Zeile: kurzname skript argumente)
D=/home/fmh/fmhc-physics-remote/runde19-huellen-leiter-2
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
spur=$1
liste=$2
mapfile -t AUF < "$liste"
for zeile in "${AUF[@]}"; do
  [ -z "$zeile" ] && continue
  case "$zeile" in \#*) continue;; esac
  name=${zeile%% *}
  rest=${zeile#* }
  cd "$D" && bash "$K" "$spur" "$name" $rest > "$D/logs/$name.log" 2>&1
done
echo "kette $spur $liste fertig $(date -Is)" >> "$D/logs/ketten.log"
