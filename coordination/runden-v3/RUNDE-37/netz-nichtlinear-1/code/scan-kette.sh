#!/bin/bash
# Kreuzungsscan-Kette: je Zeile "name netz lesart K" ein Aufruf von nn_scan.py ueber kleintest.sh; df vor jedem Aufruf.
set -u
SPUR=$1
LISTE=$2
cd /home/fmh/fmhc-physics-remote/netz-nichtlinear-1 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
while read -r NAME NETZ LES KZ <&3; do
  [ -z "${NAME:-}" ] && continue
  frei=$(df -BG --output=avail /home/fmh | tail -1 | tr -dc '0-9')
  if [ "$frei" -lt 10 ]; then echo "$NAME abbruch: nur ${frei} GB frei $(date --iso-8601=seconds)" >> "scan/kette-$SPUR.txt"; exit 4; fi
  bash "$K" "$SPUR" "nn-$NAME" code/nn_scan.py --netz "$NETZ" --lesart "$LES" --K "$KZ" --out "scan/$NAME.json" \
    > "scan/$NAME.log" 2>&1 < code/leer.txt
  echo "$NAME rc=$? frei=${frei}G $(date --iso-8601=seconds)" >> "scan/kette-$SPUR.txt"
done 3< "$LISTE"
echo "kette fertig $(date --iso-8601=seconds)" >> "scan/kette-$SPUR.txt"
