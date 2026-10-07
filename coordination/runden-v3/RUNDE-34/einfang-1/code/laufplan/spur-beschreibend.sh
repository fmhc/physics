#!/bin/bash
# EINFANG-1 beschreibende Zusatzlaeufe (PLAN.md Abschnitt 3, nicht gewertet). Spur p4000a, nach den Hauptlaeufen.
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
lauf f5-v0.035 --n 5 --h 0.3 --v 0.035 --dt 0.1 --T 2000
lauf f5-v0.01 --n 5 --h 0.3 --v 0.01 --d0 16 --dt 0.1 --T 3200
echo "spur beschreibend fertig $(date --iso-8601=seconds)" > $L/fertig-beschreibend.txt
