#!/bin/bash
# G2-10 gestaffelt (Leitung, 30.09.2026): Stufe A (x_B) vor Stufe B (Polsuche); C parallel zu B; D danach. Stufe E (L3) von Hand.
cd /home/fmh/fmhc-physics-remote/ie-gen02-g2-10 || exit 1
stufe() {  # $1 = Datei mit Aufrufzeilen; je Spur (cpu, cpu2, cpu6) nacheinander, Spuren parallel
  for spur in cpu cpu2 cpu6; do
    ( grep -E "kleintest.sh $spur " "$1" | while IFS= read -r z; do echo "== $(date -Is) $z"; bash -c "$z"; echo "== rc=$? $(date -Is)"; done ) &
  done
  wait
}
echo "KETTE-G210 A-START $(date -Is)"; stufe g210-A.txt
echo "KETTE-G210 BC-START $(date -Is)"; cat g210-B.txt g210-C.txt > g210-BC.txt; stufe g210-BC.txt
echo "KETTE-G210 D-START $(date -Is)"; stufe g210-D.txt
echo "KETTE-G210-ENDE $(date -Is)"
