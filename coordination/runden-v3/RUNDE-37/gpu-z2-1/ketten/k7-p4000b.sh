#!/bin/bash
# GPU-Z2-1, Kette 7 Spur p4000b (gz2): wartet auf Kette 6 (R = 80); dann Gegenprobe zur Wegabhaengigkeit: zweite
# Kappenfamilie (Kappenwinkel 45 statt 30 Grad, sonst gleich) bei R = 32, 40, 48, 64: bisekt und Folgemodus (M1, Freigabe).
set -u
B=/home/fmh/fmhc-physics-remote/gpu-z2-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=$B/code/gz2.py
G=$B/lauf/gross
AB=$B/lauf/abgleich
V=$B/lauf/var45
O=$V/kette7-p4000b.out
SP=p4000b
mkdir -p $V
cd $B/code || exit 1
while [ ! -e $G/k6b.fertig ]; do sleep 5; done
run() { local name=$1; local d=$2; shift 2; bash $K $SP "$name" "$@" >> $d/$name.log 2>&1; local rc=$?; echo "rc=$rc $name $(date -u +%H:%M:%S)" >> $O; return $rc; }
bis_fertig() { local name=$1; local d=$2; local stand=$3; shift 3; local i=0
  while [ $i -lt 10 ]; do i=$((i+1)); run "$name$i" $d "$@" || break; grep -q '"fertig": true' $stand 2>/dev/null && break; done; }
VR() { local kurz=$1; local r0=$2; local R=$3; local S=$4
  nvidia-smi --query-gpu=index,memory.used,memory.free --format=csv,noheader | tr '\n' ' ' >> $O; echo >> $O
  bis_fertig "gz2vb$kurz" $V $V/bisekt-r$r0-R$R.stand.json $C bisekt --r0 $r0 --R $R --start $S \
    --kappe_b 45 --budget 1e9 --einheit 540 --zwischen $V/zw-bisekt-r$r0-R$R --nbis 4000 --aus $V
  for ab in M1 freigabe; do
    if [ $ab = M1 ]; then z=-M1; k=m; else z=-fr; k=f; fi
    bis_fertig "gz2vf$kurz$k" $V $V/folge-r$r0-R$R$z.stand.json $C folge --r0 $r0 --R $R --start $S \
      --bisekt_json $V/bisekt-r$r0-R$R.json --zugpfad $V/bisekt-r$r0-R$R.npz --freigabe $V/freigabe-r$r0-R$R.npz \
      --kappe_b 45 --folge_ab $ab --tag_zusatz=$z --zwischen $V/zw-folge-r$r0-R$R$z --einheit 540 --nbis 4000 --aus $V
  done
}
echo "kette start $(date -u +%H:%M:%S)" >> $O
VR 1032 10 32 $AB/start-r10-R32.npz
VR 1040 10 40 $G/start-r10-R40.npz
VR 1048 10 48 $G/start-r10-R48.npz
VR 1064 10 64 $G/start-r10-R64.npz
echo "kette ende $(date -u +%H:%M:%S)" >> $O
touch $V/k7b.fertig
