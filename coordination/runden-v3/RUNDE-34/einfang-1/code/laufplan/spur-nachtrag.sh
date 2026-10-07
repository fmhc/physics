#!/bin/bash
# EINFANG-1 NACHTRAG (nicht im eingefrorenen Plan, nachtraeglich nach Sicht auf f5-v0.01 beschlossen; nur beschreibend):
# Schwelle des Einfangs zwischen v = 0,01 und 0,02 eingrenzen und den Einfang bei v = 0,01 mit dt = 0,05 nachpruefen.
# Aufruf: bash spur-nachtrag.sh <spur> <name> <argumente...>
set -u
SPUR=$1; shift
B=/home/fmh/fmhc-physics-remote/runde34-einfang
L=$B/lauf
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
P=$B/einfang.py
cd $L
name=$1; shift
bash $K $SPUR r34ef-$name $P lauf --name $name --geraet cuda --aus $L/ef-$name.json "$@" > $L/log-$name.txt 2>&1
i=1
while [ "$(jq -r .meta.vollstaendig $L/ef-$name.json 2>/dev/null)" = "false" ] && [ $i -le 3 ]; do
  bash $K $SPUR r34ef-$name-f$i $P lauf --name $name --geraet cuda --aus $L/ef-$name.json --fortsetzen $L/ef-$name-zustand.npz "$@" >> $L/log-$name.txt 2>&1
  i=$((i+1))
done
echo "nachtrag $name fertig $(date --iso-8601=seconds)" > $L/fertig-nachtrag-$name.txt
