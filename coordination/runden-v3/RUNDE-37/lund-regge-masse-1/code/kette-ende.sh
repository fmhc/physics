#!/bin/bash
# LUND-REGGE-MASSE-1, Abschluss nach beiden Ketten (Spur cpu5): Glas-Teillaeufe zusammenfuehren, Bild.
W=/home/fmh/fmhc-physics-remote/lund-regge-masse-1
KT=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd "$W" || exit 1
lauf() { n=$1; shift; bash "$KT" cpu5 "$n" code/lrm.py "$@" > "$W/lauf/$n.log" 2>&1; echo "$n rc=$? $(date --iso-8601=seconds)" >> "$W/lauf/kette-ende.txt"; }
for s in 1 2 3 4; do
  lauf zuG$s zusammen --ein lauf/sp-glas-s$s-a.json lauf/sp-glas-s$s-b.json --out lauf/sp-glas-s$s.json
done
lauf bild bild --ein lauf/sp-V.json lauf/sp-S.json lauf/sp-A15.json lauf/sp-glas-s1.json lauf/sp-glas-s2.json lauf/sp-glas-s3.json lauf/sp-glas-s4.json --bild lauf/lrm-bild.png --out lauf/bild.json
echo "ende $(date --iso-8601=seconds)" >> "$W/lauf/kette-ende.txt"
