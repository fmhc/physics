#!/bin/bash
# Laufkette NETZ-NICHTLINEAR-1: je Zeile "name netz arm lesart h perioden maxab" ein Lauf ueber kleintest.sh; nicht fertige
# Laeufe werden aus ihrem Zwischenstand fortgesetzt (hoechstens maxab Abschnitte). Vor jedem Aufruf df; unter 10 GB frei:
# Abbruch. stdin der Aufrufe aus der leeren Datei code/leer.txt (nicht /dev/null), Liste ueber Kanal 3.
set -u
SPUR=$1
LISTE=$2
cd /home/fmh/fmhc-physics-remote/netz-nichtlinear-1 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
while read -r NAME NETZ ARM LES H PER MAXAB BGD <&3; do
  [ -z "${NAME:-}" ] && continue
  PER=${PER:-10}
  MAXAB=${MAXAB:-4}
  BGD=${BGD:-1}
  for ab in $(seq 1 "$MAXAB"); do
    frei=$(df -BG --output=avail /home/fmh | tail -1 | tr -dc '0-9')
    if [ "$frei" -lt 10 ]; then echo "$NAME abbruch: nur ${frei} GB frei $(date --iso-8601=seconds)" >> "lauf/kette-$SPUR.txt"; exit 4; fi
    bash "$K" "$SPUR" "nn-$NAME-$ab" code/nn.py lauf --netz "$NETZ" --arm "$ARM" --lesart "$LES" --h "$H" --perioden "$PER" --bgd "$BGD" \
      --budget 420 --out "lauf/$NAME.json" > "lauf/$NAME-$ab.log" 2>&1 < code/leer.txt
    rc=$?
    echo "$NAME abschnitt $ab rc=$rc frei=${frei}G $(date --iso-8601=seconds)" >> "lauf/kette-$SPUR.txt"
    [ $rc -ne 0 ] && break
    grep -q "fertig=True" "lauf/$NAME-$ab.log" && break
  done
done 3< "$LISTE"
echo "kette fertig $(date --iso-8601=seconds)" >> "lauf/kette-$SPUR.txt"
