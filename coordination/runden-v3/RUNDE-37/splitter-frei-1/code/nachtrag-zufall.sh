#!/bin/bash
# SPLITTER-FREI-1, Nachtrag nach Sicht (beschreibend): Zufallsstoerung ohne Formziel, Saat 1, mittlerer Betrag 0,0701
# (= mittlere Verschiebung des splitterarmen Baus s1), zwei Zufallssaaten; je hm --rauch mit dem eingefrorenen sf.py.
set -u
W=/home/fmh/fmhc-physics-remote/splitter-frei-1
KT=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SP=$1
cd "$W" || exit 1
for rs in 1 2; do
  bash "$KT" "$SP" "sf-nt-zufall-r$rs" code-nachtrag/nachtrag_zufall.py 1 0.0701 $rs "nachtrag/zufall-s1-r$rs.json" > "$W/nachtrag/zufall-s1-r$rs.log" 2>&1
  echo "zufall-s1-r$rs rc=$? $(date --iso-8601=seconds)" >> "$W/nachtrag/kette-zufall.txt"
  bash "$KT" "$SP" "sf-nt-hm-zufall-r$rs" code/sf.py hm --art sf --saat 1 --bau "nachtrag/zufall-s1-r$rs.json" --rauch --out "nachtrag/hm-zufall-s1-r$rs.json" > "$W/nachtrag/hm-zufall-s1-r$rs.log" 2>&1
  echo "hm-zufall-s1-r$rs rc=$? $(date --iso-8601=seconds)" >> "$W/nachtrag/kette-zufall.txt"
done
echo "ende $(date --iso-8601=seconds)" >> "$W/nachtrag/kette-zufall.txt"
