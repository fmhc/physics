#!/bin/bash
# GPU-Z2-1, Kette 6 Spur p4000b (gz2): wartet auf Kette 4; dann R = 80 (start psi, bisekt in Units, Folgemodus).
# Jede Unit <= 10 min (einheit 540 s).
set -u
B=/home/fmh/fmhc-physics-remote/gpu-z2-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=$B/code/gz2.py
G=$B/lauf/gross
O=$G/kette6-p4000b.out
SP=p4000b
cd $B/code || exit 1
while [ ! -e $G/k4b.fertig ]; do sleep 5; done
run() { local name=$1; local d=$2; shift 2; bash $K $SP "$name" "$@" >> $d/$name.log 2>&1; local rc=$?; echo "rc=$rc $name $(date -u +%H:%M:%S)" >> $O; return $rc; }
bis_fertig() { local name=$1; local d=$2; local stand=$3; shift 3; local i=0
  while [ $i -lt 10 ]; do i=$((i+1)); run "$name$i" $d "$@" || break; grep -q '"fertig": true' $stand 2>/dev/null && break; done; }
F() { local kurz=$1; local d=$2; local r0=$3; local R=$4; local ab=$5; local z=$6; shift 6
  bis_fertig "gz2f$kurz" $d $d/folge-r$r0-R$R$z.stand.json $C folge --r0 $r0 --R $R --start $d/start-r$r0-R$R.npz \
    --bisekt_json $d/bisekt-r$r0-R$R.json --zugpfad $d/bisekt-r$r0-R$R.npz --freigabe $d/freigabe-r$r0-R$R.npz \
    --folge_ab $ab --tag_zusatz=$z --zwischen $d/zw-folge-r$r0-R$R$z --einheit 540 --nbis 4000 --aus $d "$@"; }
GR() { local kurz=$1; local r0=$2; local R=$3
  nvidia-smi --query-gpu=index,memory.used,memory.free --format=csv,noheader | tr '\n' ' ' >> $O; echo >> $O
  run "gz2s$kurz" $G $C start --r0 $r0 --R $R --darst psi --budget 560 --aus $G
  bis_fertig "gz2b$kurz" $G $G/bisekt-r$r0-R$R.stand.json $C bisekt --r0 $r0 --R $R --start $G/start-r$r0-R$R.npz \
    --budget 1e9 --einheit 540 --zwischen $G/zw-bisekt-r$r0-R$R --nbis 4000 --aus $G
  F ${kurz}m $G $r0 $R M1 -M1
  F ${kurz}f $G $r0 $R freigabe -fr
}
echo "kette start $(date -u +%H:%M:%S)" >> $O
GR 1080 10 80
echo "kette ende $(date -u +%H:%M:%S)" >> $O
touch $G/k6b.fertig
