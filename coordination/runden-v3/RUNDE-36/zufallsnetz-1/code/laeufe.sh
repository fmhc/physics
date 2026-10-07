#!/bin/bash
# ZUFALLSNETZ-1 Hauptlaeufe nach PLAN.md (eingefroren). Zwei Spuren (cpu3, cpu4) parallel, je Spur nacheinander,
# danach die Auswertung auf cpu3. Start auf der .69 im Ordner runde36-zufall, nur ueber kleintest.sh.
set -u
cd /home/fmh/fmhc-physics-remote/runde36-zufall
KT=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
lauf() {
  local spur=$1 name=$2; shift 2
  echo "$(date -u +%FT%TZ) start $name" >> lauf/laeufe.log
  bash $KT $spur z36-$name "$@" > lauf/$name.log 2>&1
  echo "$(date -u +%FT%TZ) ende $name rc=$?" >> lauf/laeufe.log
}
spurA() {
  lauf cpu3 netz_N64000_s1_k1 code/zufallsnetz.py netz 64000 1 k1 lauf/netz_N64000_s1_k1.json
  lauf cpu3 netz_N64000_s1_kl code/zufallsnetz.py netz 64000 1 kl lauf/netz_N64000_s1_kl.json
  lauf cpu3 netz_N16000_s1_k1 code/zufallsnetz.py netz 16000 1 k1 lauf/netz_N16000_s1_k1.json
  lauf cpu3 netz_N16000_s1_kl code/zufallsnetz.py netz 16000 1 kl lauf/netz_N16000_s1_kl.json
  lauf cpu3 netz_N4000_s1_k1 code/zufallsnetz.py netz 4000 1 k1 lauf/netz_N4000_s1_k1.json
  lauf cpu3 netz_N4000_s1_kl code/zufallsnetz.py netz 4000 1 kl lauf/netz_N4000_s1_kl.json
  lauf cpu3 fcc code/zufallsnetz.py fcc lauf/fcc.json lauf/netz_a.npz
}
spurB() {
  lauf cpu4 netz_N64000_s2_k1 code/zufallsnetz.py netz 64000 2 k1 lauf/netz_N64000_s2_k1.json
  lauf cpu4 netz_N64000_s2_kl code/zufallsnetz.py netz 64000 2 kl lauf/netz_N64000_s2_kl.json
  lauf cpu4 netz_N16000_s2_k1 code/zufallsnetz.py netz 16000 2 k1 lauf/netz_N16000_s2_k1.json
  lauf cpu4 netz_N16000_s2_kl code/zufallsnetz.py netz 16000 2 kl lauf/netz_N16000_s2_kl.json
  lauf cpu4 netz_N4000_s2_k1 code/zufallsnetz.py netz 4000 2 k1 lauf/netz_N4000_s2_k1.json
  lauf cpu4 netz_N4000_s2_kl code/zufallsnetz.py netz 4000 2 kl lauf/netz_N4000_s2_kl.json
  lauf cpu4 kontrolle_N4000_s1_k1 code/zufallsnetz.py kontrolle 4000 1 k1 lauf/kontrolle_N4000_s1_k1.json
}
echo "$(date -u +%FT%TZ) laeufe start" >> lauf/laeufe.log
spurA &
spurB &
wait
lauf cpu3 auswertung code/auswertung.py lauf lauf/auswertung.json
echo "$(date -u +%FT%TZ) laeufe fertig" >> lauf/laeufe.log
