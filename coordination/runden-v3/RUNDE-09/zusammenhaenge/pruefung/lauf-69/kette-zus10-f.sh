#!/bin/bash
# ZUS-10 Pruefung, Kette F (Spur cpu2, falls frei): Idee 3 Gegenprobe l = 0 mit feiner d-Liste (R6-Minima bei ~1,5 und
# ~2,25 als V-Form?). Zwei Teile, explizite Listen, LC_ALL=C; Teil b startet am Spurpunkt d = 2,3 aus Teil a.
export LC_ALL=C
cd /home/fmh/fmhc-physics-remote/runde9-zus10 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
S=cpu2
echo "Kette F Start $(date --iso-8601=seconds)"
bash $K $S z3ca bic2.py bruecke --geraet cpu --omega2 0.7 --l 0 --start 1.4937770-6.716e-5j --dims 1,1.25,1.4,1.5,1.6,1.75,2,2.1,2.2,2.25,2.3 --h 0.02 --budget 540 --out aus-bruecke-l0-070-a > LAUF-z3ca.log 2>&1
echo "z3ca rc=$? $(date --iso-8601=seconds)"
J=aus-bruecke-l0-070-a/bruecke.json
ST=$(jq -r '.ergebnisse["0.7_l0"] | map(select(.dim == 2.3)) | .[0].rho | "\(.[0])\(if .[1] < 0 then "" else "+" end)\(.[1])j"' "$J")
DIMS="2.3,2.4,2.5,2.6,2.7,2.8,2.9,3.0"
echo "Teil b: Start-rho (d = 2,3): $ST; dims: $DIMS"
case "$ST" in
  *,*|null*) echo "FEHLER: Startwert unbrauchbar: $ST"; exit 2 ;;
esac
bash $K $S z3cb bic2.py bruecke --geraet cpu --omega2 0.7 --l 0 --start "$ST" --dims "$DIMS" --h 0.02 --budget 540 --out aus-bruecke-l0-070-b > LAUF-z3cb.log 2>&1
echo "z3cb rc=$? $(date --iso-8601=seconds)"
echo "Kette F fertig $(date --iso-8601=seconds)"
