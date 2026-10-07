#!/bin/bash
# EINFANG-1 Laufplan (Runde 34), Spur p4000a. Nur eine Folge von kleintest.sh-Aufrufen; kein Dienst.
set -u
SPUR=p4000a
B=/home/fmh/fmhc-physics-remote/runde34-einfang
L=$B/lauf
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
P=$B/einfang.py
cd $L
lauf() {
  local name=$1; shift
  bash $K $SPUR r34ef-$name $P lauf --name $name --geraet cuda --aus $L/ef-$name.json "$@" > $L/log-$name.txt 2>&1
  local i=1
  while [ "$(jq -r .meta.vollstaendig $L/ef-$name.json 2>/dev/null)" = "false" ] && [ $i -le 3 ]; do
    bash $K $SPUR r34ef-$name-f$i $P lauf --name $name --geraet cuda --aus $L/ef-$name.json --fortsetzen $L/ef-$name-zustand.npz "$@" >> $L/log-$name.txt 2>&1
    i=$((i+1))
  done
}
lauf f5-v0.02 --n 5 --h 0.3 --v 0.02 --dt 0.1 --T 3200
lauf e6-v0 --n 6 --h 0.3 --v 0 --dt 0.1 --T 300
lauf e6-v0.05-ohne --n 6 --h 0.3 --v 0.05 --dt 0.1 --T 300 --gmax 0
lauf f5-v0.02-dt0.05 --n 5 --h 0.3 --v 0.02 --dt 0.05 --T 3200
echo "spur $SPUR fertig $(date --iso-8601=seconds)" > $L/fertig-$SPUR.txt
