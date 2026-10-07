#!/bin/bash
# QBALL-DREIPOL-2, Nachtrag N1 nach Sicht der Hauptwerte (ohne Urteil): 3D-Dreiecksfluss bei kleinerer Ladung,
# eingefrorener Code dreipol2.py, nur andere Argumente. Frage: Gibt es das 3D-Dreieck auch dort, wo der Mischball
# unter drei getrennten Baellen liegt (wie in 2D)? Laeuft auf der .69.
set -u
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
P=/home/fmh/fmhc-physics-remote/qball-dreipol-2/code
O=/home/fmh/fmhc-physics-remote/qball-dreipol-2/lauf/nachtrag
mkdir -p $O
cd /home/fmh/fmhc-physics-remote/qball-dreipol-2 || exit 1
SPUR=${1:?Spur}
shift
for q in "$@"; do
  Q=${q%%:*}
  L=${q##*:}
  bash $K $SPUR dp2-N1-q$Q $P/dreipol2.py B --out $O/B_m01_Q$Q.json --g4=-0.1 --Q1 $Q --N 80 --L $L --nfluss 60000 \
    --wand_fluss 420 > $O/B_m01_Q$Q.log 2>&1
  echo "B_m01_Q$Q rc=$? $(date --iso-8601=seconds)" >> $O/laeufe-nachtrag.log
done
