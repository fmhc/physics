#!/bin/bash
# L2-L4: K1 (beide Varianten), Eichzeilen, (Stufe 2: K2); Stufe $1, Spur $2
set -u
export LC_ALL=C
ST=$1; SP=$2
cd /home/fmh/fmhc-physics-remote/runde17-stille-zweifeld
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
bash $K $SP r17-k1e1-st$ST code/stille3.py k1 K1E1 $ST laeufe/k1prof-st$ST laeufe/k1-K1E1-st$ST.json > logs/L3-k1e1-st$ST.log 2>&1
bash $K $SP r17-k1e2-st$ST code/stille3.py k1 K1E2 $ST laeufe/k1prof-st$ST laeufe/k1-K1E2-st$ST.json > logs/L3-k1e2-st$ST.log 2>&1
bash $K $SP r17-eich-st$ST code/stille3.py zeilen $ST laeufe/prof-st$ST laeufe/eich-st$ST 0.85 1.25 1.65 1.93 > logs/L4-eich-st$ST.log 2>&1
if [ "$ST" = "2" ]; then
  bash $K $SP r17-k2 code/stille3.py k2 laeufe/prof-st2 laeufe/k2.json > logs/L2-k2.log 2>&1
fi
echo KETTE_FERTIG
