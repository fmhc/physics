#!/bin/bash
# Laufkette UMKLAPP-FOLGE-1: je Zeile "name netz arm lesart h [perioden]" ein Lauf ueber kleintest.sh, nicht fertige Laeufe
# werden aus ihrem Zwischenstand fortgesetzt (hoechstens 6 Abschnitte). Vor jedem Aufruf df; unter 10 GB frei: Abbruch.
# stdin der Aufrufe aus der leeren Datei code/leer.txt (nicht /dev/null), Liste ueber Kanal 3.
set -u
SPUR=$1
LISTE=$2
cd /home/fmh/fmhc-physics-remote/umklapp-folge-1 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
while read -r NAME NETZ ARM LES H PER <&3; do
  [ -z "${NAME:-}" ] && continue
  PER=${PER:-10}
  for ab in 1 2 3 4 5 6; do
    frei=$(df -BG --output=avail /home/fmh | tail -1 | tr -dc '0-9')
    if [ "$frei" -lt 10 ]; then echo "$NAME abbruch: nur ${frei} GB frei $(date --iso-8601=seconds)" >> "lauf/kette-$SPUR.txt"; exit 4; fi
    bash "$K" "$SPUR" "uf-$NAME-$ab" code/uf.py lauf --netz "$NETZ" --arm "$ARM" --lesart "$LES" --h "$H" --perioden "$PER" \
      --budget 450 --out "lauf/$NAME.json" > "lauf/$NAME-$ab.log" 2>&1 < code/leer.txt
    rc=$?
    echo "$NAME abschnitt $ab rc=$rc frei=${frei}G $(date --iso-8601=seconds)" >> "lauf/kette-$SPUR.txt"
    [ $rc -ne 0 ] && break
    grep -q "fertig=True" "lauf/$NAME-$ab.log" && break
  done
done 3< "$LISTE"
echo "kette fertig $(date --iso-8601=seconds)" >> "lauf/kette-$SPUR.txt"
