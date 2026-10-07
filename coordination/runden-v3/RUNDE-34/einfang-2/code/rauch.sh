#!/bin/bash
# EINFANG-2 Rauchlaeufe (Runde 34), nur kleintest.sh-Aufrufe. Parameter kommen in keinem echten Lauf vor:
# Ikosaeder a = 25 (nu = 84), Q = 150; Torus klein, Q = 150; Zeitmessung a = 40 bzw. nu = 200 mit Q = 150.
# Aufruf: bash rauch.sh <spur> <teil: a oder b>
set -u
SPUR=$1
TEIL=$2
B=/home/fmh/fmhc-physics-remote/runde34-einfang2
R=$B/rauch
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
P=$B/einfang2.py
cd $R
if [ "$TEIL" = "a" ]; then
  bash $K $SPUR r34ef2-rauch-ik25 $P lauf --name rauch-ik25 --geo ikosaeder --nu 84 --a 25 --Q 150 --v 0.1 --dt 0.1 --T 700 --geraet cuda --aus $R/ef2-rauch-ik25.json > $R/log-rauch-ik25.txt 2>&1
  bash $K $SPUR r34ef2-rauch-torus $P lauf --name rauch-torus --geo torus --N1 168 --N2 194 --h 0.297619047619 --Q 150 --v 0.15 --dt 0.1 --T 240 --geraet cuda --aus $R/ef2-rauch-torus.json > $R/log-rauch-torus.txt 2>&1
fi
if [ "$TEIL" = "b" ]; then
  bash $K $SPUR r34ef2-rauch-ik40ruh $P lauf --name rauch-ik40ruh --geo ikosaeder --nu 134 --a 40 --Q 150 --v 0 --dt 0.1 --T 100 --geraet cuda --aus $R/ef2-rauch-ik40ruh.json > $R/log-rauch-ik40ruh.txt 2>&1
  bash $K $SPUR r34ef2-rauch-ik200 $P lauf --name rauch-ik200 --geo ikosaeder --nu 200 --a 40 --Q 150 --v 0 --dt 0.05 --T 10 --geraet cuda --aus $R/ef2-rauch-ik200.json > $R/log-rauch-ik200.txt 2>&1
fi
echo "rauch $TEIL fertig $(date --iso-8601=seconds)" > $R/fertig-rauch-$TEIL.txt
