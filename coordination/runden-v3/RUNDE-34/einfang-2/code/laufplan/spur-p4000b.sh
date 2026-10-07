#!/bin/bash
# EINFANG-2 Laufplan (Runde 34), Spur p4000b (Konvergenzproben). Nur eine Folge von kleintest.sh-Aufrufen; kein Dienst.
# p4000b nur, solange WM-1-MB nicht laeuft (kleintest.sh prueft selbst und bricht sonst mit rc 3 ab).
set -u
SPUR=p4000b
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
lauf ik-v0.05-h0.2 --geo ikosaeder --nu 200 --a 40 --v 0.05 --dt 0.05 --T 8000
lauf ik-v0.05-dt0.05 --geo ikosaeder --nu 134 --a 40 --v 0.05 --dt 0.05 --T 8000
echo "spur $SPUR fertig $(date --iso-8601=seconds)" > $L/fertig-$SPUR.txt
