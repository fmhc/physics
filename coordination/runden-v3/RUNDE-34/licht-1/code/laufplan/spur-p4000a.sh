#!/bin/bash
# LICHT-1 Laufplan (Runde 34), Spur p4000a: Teil B Zeitentwicklung an der Dreier-Spitze. Nur kleintest.sh-Aufrufe.
set -u
SPUR=p4000a
B=/home/fmh/fmhc-physics-remote/runde34-licht
L=$B/lauf
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
P=$B/code/licht.py
cd $L
lauf() {
  local name=$1; shift
  bash $K $SPUR r34li-$name $P lauf --name $name --geraet cuda --aus $L/li-$name.json "$@" > $L/log-$name.txt 2>&1
  local i=1
  while [ "$(jq -r .meta.vollstaendig $L/li-$name.json 2>/dev/null)" = "false" ] && [ $i -le 3 ]; do
    bash $K $SPUR r34li-$name-f$i $P lauf --name $name --geraet cuda --aus $L/li-$name.json --fortsetzen $L/li-$name-zustand.npz "$@" >> $L/log-$name.txt 2>&1
    i=$((i+1))
  done
}
lauf t3-v0.01 --n 3 --h 0.3 --v 0.01 --d0 25 --dt 0.1 --T 3000
lauf t3-ruhe --n 3 --h 0.3 --v 0 --d0 0 --dt 0.1 --T 200 --kreuz-stopp 0
lauf t3-v0.01-dt0.05 --n 3 --h 0.3 --v 0.01 --d0 25 --dt 0.05 --T 3000
lauf t3-v0.01-h0.2 --n 3 --h 0.2 --v 0.01 --d0 25 --dt 0.05 --T 3000
echo "spur $SPUR fertig $(date --iso-8601=seconds)" > $L/fertig-$SPUR.txt
