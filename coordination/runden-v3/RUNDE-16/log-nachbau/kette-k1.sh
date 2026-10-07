#!/bin/bash
# Einmaliger Starter fuer K1 je Stufe: Zeilen, danach Kandidaten. Aufruf: bash kette-k1.sh <stufe> <spur>
set -u
D=/home/fmh/fmhc-physics-remote/runde16-log-nachbau
cd "$D"
ST=$1
SP=$2
bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh "$SP" "r16k1scan$ST" stille.py scan kontrolle "$ST" "$D/aus-k1-st$ST" 0.780 0.785 0.790 0.795 0.800 0.805 0.810 0.815
bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh "$SP" "r16k1kand$ST" stille.py kand kontrolle "$ST" "$D/k1-kand-st$ST.json" "$D"/aus-k1-st"$ST"/zeile-kontrolle-st"$ST"-*.json
