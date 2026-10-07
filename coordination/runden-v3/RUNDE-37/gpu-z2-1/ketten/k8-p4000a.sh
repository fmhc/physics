#!/bin/bash
# GPU-Z2-1, Kette 8 Spur p4000a (gz3): Fortsetzung des Folgelaufs M1 bei R = 64 ab seinem letzten Ruhezustand
# (gz2 brach bei 180 Grad ohne Versuch ab). Units teilen sich die Spur ueber den Lock von kleintest.sh mit Kette 5.
set -u
B=/home/fmh/fmhc-physics-remote/gpu-z2-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=$B/code/gz3.py
G=$B/lauf/gross
O=$G/kette8-p4000a.out
SP=p4000a
cd $B/code || exit 1
run() { local name=$1; local d=$2; shift 2; bash $K $SP "$name" "$@" >> $d/$name.log 2>&1; local rc=$?; echo "rc=$rc $name $(date -u +%H:%M:%S)" >> $O; return $rc; }
bis_fertig() { local name=$1; local d=$2; local stand=$3; shift 3; local i=0
  while [ $i -lt 10 ]; do i=$((i+1)); run "$name$i" $d "$@" || break; grep -q '"fertig": true' $stand 2>/dev/null && break; done; }
echo "kette start $(date -u +%H:%M:%S)" >> $O
nvidia-smi --query-gpu=index,memory.used,memory.free --format=csv,noheader | tr '\n' ' ' >> $O; echo >> $O
bis_fertig gz3f1064w $G $G/folge-r10-R64-M1w.stand.json $C folge --r0 10 --R 64 --start $G/start-r10-R64.npz \
  --bisekt_json $G/bisekt-r10-R64.json --zugpfad $G/bisekt-r10-R64.npz --freigabe $G/freigabe-r10-R64.npz \
  --folge_ab ende --folge_json $G/folge-r10-R64-M1.json --folge_ende $G/folge-r10-R64-M1-ende.npz --folge_alpha_start 150 \
  --folge_max 10 --tag_zusatz=-M1w --zwischen $G/zw-folge-r10-R64-M1w --einheit 540 --nbis 4000 --aus $G
echo "kette ende $(date -u +%H:%M:%S)" >> $O
touch $G/k8a.fertig
