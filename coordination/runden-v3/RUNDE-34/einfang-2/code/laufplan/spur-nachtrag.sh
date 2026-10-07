#!/bin/bash
# EINFANG-2 NACHTRAG (nicht im eingefrorenen Plan; beschlossen nach Sicht auf die Auswertung, nur beschreibend).
# Frage: Sind die K-Zuwaechse von ik-v0.1 (x1,90 an Spitze 10, x1,70 an Spitze 1), an denen E2-3 scheitert, gegen dt und h
# stabil? Eigener Ordner nachtrag/, geht in kein Urteil ein.
# Aufruf: bash spur-nachtrag.sh <spur> <name> <argumente...>
set -u
SPUR=$1; shift
B=/home/fmh/fmhc-physics-remote/runde34-einfang2
L=$B/nachtrag
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
P=$B/einfang2.py
mkdir -p $L
cd $L
name=$1; shift
bash $K $SPUR r34ef2-$name $P lauf --name $name --geraet cuda --aus $L/ef2-$name.json "$@" > $L/log-$name.txt 2>&1
i=1
while [ "$(jq -r .meta.vollstaendig $L/ef2-$name.json 2>/dev/null)" = "false" ] && [ $i -le 4 ]; do
  bash $K $SPUR r34ef2-$name-f$i $P lauf --name $name --geraet cuda --aus $L/ef2-$name.json --fortsetzen $L/ef2-$name-zustand.npz "$@" >> $L/log-$name.txt 2>&1
  i=$((i+1))
done
echo "nachtrag $name fertig $(date --iso-8601=seconds)" > $L/fertig-nachtrag-$name.txt
