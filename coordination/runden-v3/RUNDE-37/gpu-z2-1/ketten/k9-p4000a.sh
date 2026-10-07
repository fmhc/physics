#!/bin/bash
# GPU-Z2-1, Kette 9 Spur p4000a (gz3): R = 80 (a) Fortsetzung des Folgelaufs M1 ab seinem letzten Ruhezustand (180 Grad),
# (b) zweiter Folgelauf ab M1 mit groesserer erster Kappe (90 Grad; gz2-Lauf ging bei 60 Grad zu S zurueck).
set -u
B=/home/fmh/fmhc-physics-remote/gpu-z2-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=$B/code/gz3.py
G=$B/lauf/gross
O=$G/kette9-p4000a.out
SP=p4000a
cd $B/code || exit 1
run() { local name=$1; local d=$2; shift 2; bash $K $SP "$name" "$@" >> $d/$name.log 2>&1; local rc=$?; echo "rc=$rc $name $(date -u +%H:%M:%S)" >> $O; return $rc; }
bis_fertig() { local name=$1; local d=$2; local stand=$3; shift 3; local i=0
  while [ $i -lt 10 ]; do i=$((i+1)); run "$name$i" $d "$@" || break; grep -q '"fertig": true' $stand 2>/dev/null && break; done; }
echo "kette start $(date -u +%H:%M:%S)" >> $O
nvidia-smi --query-gpu=index,memory.used,memory.free --format=csv,noheader | tr '\n' ' ' >> $O; echo >> $O
bis_fertig gz3f1080w $G $G/folge-r10-R80-M1w.stand.json $C folge --r0 10 --R 80 --start $G/start-r10-R80.npz \
  --bisekt_json $G/bisekt-r10-R80.json --zugpfad $G/bisekt-r10-R80.npz --freigabe $G/freigabe-r10-R80.npz \
  --folge_ab ende --folge_json $G/folge-r10-R80-M1.json --folge_ende $G/folge-r10-R80-M1-ende.npz --folge_alpha_start 150 \
  --folge_max 10 --tag_zusatz=-M1w --zwischen $G/zw-folge-r10-R80-M1w --einheit 540 --nbis 4000 --aus $G
bis_fertig gz3f1080k $G $G/folge-r10-R80-M1k60.stand.json $C folge --r0 10 --R 80 --start $G/start-r10-R80.npz \
  --bisekt_json $G/bisekt-r10-R80.json --zugpfad $G/bisekt-r10-R80.npz --freigabe $G/freigabe-r10-R80.npz \
  --folge_ab M1 --kappe_b 60 --folge_max 10 --tag_zusatz=-M1k60 --zwischen $G/zw-folge-r10-R80-M1k60 --einheit 540 \
  --nbis 4000 --aus $G
echo "kette ende $(date -u +%H:%M:%S)" >> $O
touch $G/k9a.fertig
