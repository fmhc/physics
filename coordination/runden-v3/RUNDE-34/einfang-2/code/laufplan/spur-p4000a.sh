#!/bin/bash
# EINFANG-2 Laufplan (Runde 34), Spur p4000a. Nur eine Folge von kleintest.sh-Aufrufen; kein Dienst.
set -u
SPUR=p4000a
B=/home/fmh/fmhc-physics-remote/runde34-einfang2
L=$B/lauf
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
P=$B/einfang2.py
cd $L
lauf() {
  local name=$1; shift
  bash $K $SPUR r34ef2-$name $P lauf --name $name --geraet cuda --aus $L/ef2-$name.json "$@" > $L/log-$name.txt 2>&1
  local i=1
  while [ "$(jq -r .meta.vollstaendig $L/ef2-$name.json 2>/dev/null)" = "false" ] && [ $i -le 4 ]; do
    bash $K $SPUR r34ef2-$name-f$i $P lauf --name $name --geraet cuda --aus $L/ef2-$name.json --fortsetzen $L/ef2-$name-zustand.npz "$@" >> $L/log-$name.txt 2>&1
    i=$((i+1))
  done
}
lauf ik-v0.05 --geo ikosaeder --nu 134 --a 40 --v 0.05 --dt 0.1 --T 8000
lauf ik-v0.1 --geo ikosaeder --nu 134 --a 40 --v 0.1 --dt 0.1 --T 8000
lauf torus-v0.05 --geo torus --N1 335 --N2 536 --h 0.29850746268656714 --v 0.05 --dt 0.1 --T 4000
lauf ik-v0 --geo ikosaeder --nu 134 --a 40 --v 0 --dt 0.1 --T 1000
# Verlaengerung (nur berichtet): aus dem Endzustand des Hauptlaufs, eigene Ausgabe und eigener Zustand
N=ik-v0.05-lang
if [ "$(jq -r .meta.vollstaendig $L/ef2-ik-v0.05.json 2>/dev/null)" = "true" ]; then
  bash $K $SPUR r34ef2-$N $P lauf --name $N --geraet cuda --geo ikosaeder --nu 134 --a 40 --v 0.05 --dt 0.1 --T 16000 --fortsetzen $L/ef2-ik-v0.05-zustand.npz --aus $L/ef2-$N.json --zustand $L/ef2-$N-zustand.npz > $L/log-$N.txt 2>&1
  i=1
  while [ "$(jq -r .meta.vollstaendig $L/ef2-$N.json 2>/dev/null)" = "false" ] && [ $i -le 4 ]; do
    bash $K $SPUR r34ef2-$N-f$i $P lauf --name $N --geraet cuda --geo ikosaeder --nu 134 --a 40 --v 0.05 --dt 0.1 --T 16000 --fortsetzen $L/ef2-$N-zustand.npz --aus $L/ef2-$N.json --zustand $L/ef2-$N-zustand.npz >> $L/log-$N.txt 2>&1
    i=$((i+1))
  done
fi
lauf ik-v0.05-b --geo ikosaeder --nu 134 --a 40 --v 0.05 --b 3.13 --dt 0.1 --T 8000
echo "spur $SPUR fertig $(date --iso-8601=seconds)" > $L/fertig-$SPUR.txt
