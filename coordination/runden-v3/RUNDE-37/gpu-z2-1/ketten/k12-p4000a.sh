#!/bin/bash
# GPU-Z2-1, Kette 12 Spur p4000a (gz3): Austrittssattel der 45-Grad-Kappenfamilie bei R = 80 (nur Bisektion, Units mit
# Zwischenstaenden). Pruefung einer vorher notierten Agenten-Vorhersage (ERGEBNIS.md), kein Urteil.
set -u
B=/home/fmh/fmhc-physics-remote/gpu-z2-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=$B/code/gz3.py
G=$B/lauf/gross
V=$B/lauf/var45
O=$V/kette12-p4000a.out
SP=p4000a
cd $B/code || exit 1
run() { local name=$1; local d=$2; shift 2; bash $K $SP "$name" "$@" >> $d/$name.log 2>&1; local rc=$?; echo "rc=$rc $name $(date -u +%H:%M:%S)" >> $O; return $rc; }
bis_fertig() { local name=$1; local d=$2; local stand=$3; shift 3; local i=0
  while [ $i -lt 4 ]; do i=$((i+1)); run "$name$i" $d "$@" || break; grep -q '"fertig": true' $stand 2>/dev/null && break; done; }
echo "kette start $(date -u +%H:%M:%S)" >> $O
nvidia-smi --query-gpu=index,memory.used,memory.free --format=csv,noheader | tr '\n' ' ' >> $O; echo >> $O
bis_fertig gz3vb1080 $V $V/bisekt-r10-R80.stand.json $C bisekt --r0 10 --R 80 --start $G/start-r10-R80.npz \
  --kappe_b 45 --budget 1e9 --einheit 540 --zwischen $V/zw-bisekt-r10-R80 --nbis 4000 --aus $V
echo "kette ende $(date -u +%H:%M:%S)" >> $O
touch $V/k12a.fertig
