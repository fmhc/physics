#!/bin/bash
# G2-10 Stufe E (L3, h = 0,01, je gefundene Stelle ein Aufruf) und danach leiter mit --l3 (Leitung, 30.09.2026).
cd /home/fmh/fmhc-physics-remote/ie-gen02-g2-10 || exit 1
stufe() {
  for spur in cpu cpu2 cpu6; do
    ( grep -E "kleintest.sh $spur " "$1" | while IFS= read -r z; do echo "== $(date -Is) $z"; bash -c "$z"; echo "== rc=$? $(date -Is)"; done ) &
  done
  wait
}
echo "KETTE-G210E E-START $(date -Is)"; stufe g210-E.txt
echo "KETTE-G210E F-START $(date -Is)"; stufe g210-F.txt
echo "KETTE-G210E-ENDE $(date -Is)"
