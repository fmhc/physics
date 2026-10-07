#!/bin/bash
# GPU-Z2-1, Kette 3 Spur p4000b (gz2): wartet auf Kette 2; dann (a) CI-NEB (psi, GPU) auf den CPU-Wegen von Z2-SCHUTZ-2
# bei (10, 20), (10, 24), (8, 24), (10, 32) (Abgleich der Wegrechnung), (b) Folgemodus M1 bei (10, 32), (10, 40), (10, 48)
# und Folgemodus ab Freigabe bei (10, 40); jeweils in Units <= 10 min mit Zwischenstaenden.
set -u
B=/home/fmh/fmhc-physics-remote/gpu-z2-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=$B/code/gz2.py
G=$B/lauf/gross
AB=$B/lauf/abgleich
REF=/home/fmh/fmhc-physics-remote/z2-schutz-2/lauf
O=$G/kette3-p4000b.out
cd $B/code || exit 1
while [ ! -e $G/k2b.fertig ]; do sleep 5; done
run() { local name=$1; local d=$2; shift 2; bash $K p4000b "$name" "$@" >> $d/$name.log 2>&1; echo "rc=$? $name $(date -u +%H:%M:%S)" >> $O; }
bis_fertig() { local name=$1; local d=$2; local stand=$3; shift 3; local i=0
  while [ $i -lt 8 ]; do i=$((i+1)); run "$name$i" $d "$@"; grep -q '"fertig": true' $stand 2>/dev/null && break; done; }
echo "kette start $(date -u +%H:%M:%S)" >> $O
nvidia-smi --query-gpu=index,memory.used,memory.free --format=csv,noheader | tr '\n' ' ' >> $O; echo >> $O
for g in "1020 10 20" "1024 10 24" "824 8 24" "1032 10 32"; do
  set -- $g
  run "gz2c$1" $AB $C weg --r0 $2 --R $3 --start $REF/start-r$2-R$3.npz --zugpfad_quat $REF/bisekt-r$2-R$3.npz --nmax 6000 --budget 480 --tag_zusatz -cpuweg --aus $AB
done
F() { local kurz=$1; local d=$2; local r0=$3; local R=$4; local ab=$5; local z=$6; shift 6
  bis_fertig "gz2f$kurz" $d $d/folge-r$r0-R$R$z.stand.json $C folge --r0 $r0 --R $R --start $d/start-r$r0-R$R.npz \
    --bisekt_json $d/bisekt-r$r0-R$R.json --zugpfad $d/bisekt-r$r0-R$R.npz --freigabe $d/freigabe-r$r0-R$R.npz \
    --folge_ab $ab --tag_zusatz $z --zwischen $d/zw-folge-r$r0-R$R$z --einheit 540 --nbis 4000 --aus $d "$@"; }
F 1032m $AB 10 32 M1 -M1
F 1040m $G 10 40 M1 -M1
F 1048m $G 10 48 M1 -M1
F 1040f $G 10 40 freigabe -fr
echo "kette ende $(date -u +%H:%M:%S)" >> $O
touch $G/k3b.fertig
