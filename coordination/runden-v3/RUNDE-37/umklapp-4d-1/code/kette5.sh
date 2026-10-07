#!/bin/bash
# Laufkette UMKLAPP-4D-1: je Zeile "saat fall mu name [weitere Argumente]" ein Aufruf von kleintest.sh (einzeln, nacheinander).
# stdin der Aufrufe aus /dev/null (lesend), damit systemd-run --pipe die Liste nicht verbraucht.
set -u
SPUR=$1
LISTE=$2
cd /home/fmh/fmhc-physics-remote/umklapp-4d-1
while read -r S F MU NAME REST; do
  [ -z "${S:-}" ] && continue
  bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh "$SPUR" "u4-$NAME" code/umklapp4d.py lauf --saat "$S" --fall "$F" --mu "$MU" \
    --zuege X,Y --out "lauf/$NAME.json" $REST > "lauf/$NAME.log" 2>&1 < /dev/null
  echo "$NAME rc=$? $(date --iso-8601=seconds)" >> "lauf/kette-$SPUR.txt"
done < "$LISTE"
echo "kette fertig $(date --iso-8601=seconds)" >> "lauf/kette-$SPUR.txt"
