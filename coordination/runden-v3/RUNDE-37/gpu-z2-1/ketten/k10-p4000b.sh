#!/bin/bash
# GPU-Z2-1, Kette 10 Spur p4000b (gz3): wartet auf Kette 7; setzt offene Folgelaeufe M1 der zweiten Kappenfamilie
# (R = 40, 48, 64) ab ihrem letzten Ruhezustand fort (180 Grad), bis T oder 10 Stufen.
set -u
B=/home/fmh/fmhc-physics-remote/gpu-z2-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=$B/code/gz3.py
G=$B/lauf/gross
V=$B/lauf/var45
O=$V/kette10-p4000b.out
SP=p4000b
cd $B/code || exit 1
while [ ! -e $V/k7b.fertig ]; do sleep 5; done
run() { local name=$1; local d=$2; shift 2; bash $K $SP "$name" "$@" >> $d/$name.log 2>&1; local rc=$?; echo "rc=$rc $name $(date -u +%H:%M:%S)" >> $O; return $rc; }
bis_fertig() { local name=$1; local d=$2; local stand=$3; shift 3; local i=0
  while [ $i -lt 10 ]; do i=$((i+1)); run "$name$i" $d "$@" || break; grep -q '"fertig": true' $stand 2>/dev/null && break; done; }
echo "kette start $(date -u +%H:%M:%S)" >> $O
for R in 40 48 64; do
  J=$V/folge-r10-R$R-M1.json
  if [ -e $J ] && jq -e '.weg_geschlossen == false' $J > /dev/null; then
    nvidia-smi --query-gpu=index,memory.used,memory.free --format=csv,noheader | tr '\n' ' ' >> $O; echo >> $O
    bis_fertig "gz3vw10$R" $V $V/folge-r10-R$R-M1w.stand.json $C folge --r0 10 --R $R --start $G/start-r10-R$R.npz \
      --bisekt_json $V/bisekt-r10-R$R.json --zugpfad $V/bisekt-r10-R$R.npz --freigabe $V/freigabe-r10-R$R.npz \
      --kappe_b 45 --folge_ab ende --folge_json $J --folge_ende $V/folge-r10-R$R-M1-ende.npz --folge_alpha_start 150 \
      --folge_max 10 --tag_zusatz=-M1w --zwischen $V/zw-folge-r10-R$R-M1w --einheit 540 --nbis 4000 --aus $V
  fi
done
echo "kette ende $(date -u +%H:%M:%S)" >> $O
touch $V/k10b.fertig
