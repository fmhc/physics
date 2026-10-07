#!/bin/bash
# ZUS-10 Pruefung, Kette A3 (Spur cpu6): Reparatur von Idee 3 Teil b. Der erste Teil b (z3bb, Kette A2) war ungueltig:
# `seq -s,` erzeugte unter deutscher Locale Dezimalkommas (dims 2,3,2,4,...), bic2.py trennt an ",". Befund Codex
# (status-audit-20260930/codex-wm1/VIER-BEFUNDE-PRAEZISE.txt). Hier: explizite Liste, LC_ALL=C, Ausgabe der
# Argumentliste vor dem Start. Startpol = Spurpunkt d = 2,3 aus Teil a (aus-bruecke-l1-070-a/bruecke.json).
export LC_ALL=C
cd /home/fmh/fmhc-physics-remote/runde9-zus10 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
S=cpu6
J=aus-bruecke-l1-070-a/bruecke.json
ST=$(jq -r '.ergebnisse["0.7_l1"] | map(select(.dim == 2.3)) | .[0].rho | "\(.[0])\(if .[1] < 0 then "" else "+" end)\(.[1])j"' "$J")
DIMS="2.3,2.4,2.5,2.6,2.7,2.8,2.9,3.0"
echo "Kette A3 Start $(date --iso-8601=seconds); Start-rho (d = 2,3 aus Teil a): $ST; dims: $DIMS"
case "$ST" in
  *,*) echo "FEHLER: Startwert enthaelt ein Komma: $ST"; exit 2 ;;
esac
bash $K $S z3bc bic2.py bruecke --geraet cpu --omega2 0.7 --l 1 --start "$ST" --dims "$DIMS" --h 0.02 --budget 540 --out aus-bruecke-l1-070-b2 > LAUF-z3bc.log 2>&1
echo "z3bc rc=$? $(date --iso-8601=seconds)"
echo "Kette A3 fertig $(date --iso-8601=seconds)"
