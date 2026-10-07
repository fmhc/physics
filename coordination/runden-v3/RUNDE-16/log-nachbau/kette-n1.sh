#!/bin/bash
# NACHTRAG-1 (nachtraeglich): Umlauf mit bis zu 24 Halbierungsrunden. Aufruf: bash kette-n1.sh <stufe> <spur> <logw2> <logrho> <k1w2> <k1rho>
set -u
D=/home/fmh/fmhc-physics-remote/runde16-log-nachbau
cd "$D"
ST=$1
SP=$2
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
bash $K "$SP" "r16n1log$ST" stille_n1.py umlauf log "$ST" 24 1e-3 "$D/f1-log-st$ST.json" "$3" "$4"
bash $K "$SP" "r16n1k1$ST" stille_n1.py umlauf kontrolle "$ST" 24 1e-3 "$D/f1-k1-st$ST.json" "$5" "$6"
bash $K "$SP" "r16n2log$ST" stille_n1.py umlauf log "$ST" 24 1e-4 "$D/f2-log-st$ST.json" "$3" "$4"
