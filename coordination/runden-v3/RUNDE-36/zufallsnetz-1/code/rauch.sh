#!/bin/bash
# ZUFALLSNETZ-1 Rauchlaeufe (vor dem Einfrieren). Saat 9 fuer die Zeit- und Pruefproben (keine Hauptsaat),
# Auswertetest mit kleinen Netzen (N = 500, 1000, 2000; dort Saaten 1, 2), Ausgabe nur auf rc und Schluessel geprueft.
set -u
cd /home/fmh/fmhc-physics-remote/runde36-zufall
KT=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
lauf() {
  local spur=$1 name=$2; shift 2
  echo "$(date -u +%FT%TZ) start $name" >> rauch/rauch.log
  bash $KT $spur z36r-$name "$@" > rauch/$name.log 2>&1
  echo "$(date -u +%FT%TZ) ende $name rc=$?" >> rauch/rauch.log
}
spurA() {
  lauf cpu3 netz_N4000_s9_k1 code/zufallsnetz.py netz 4000 9 k1 rauch/netz_N4000_s9_k1.json rauch
  lauf cpu3 fcc code/zufallsnetz.py fcc rauch/fcc.json rauch/netz_a.npz
  lauf cpu3 kontrolle_N4000_s9_k1 code/zufallsnetz.py kontrolle 4000 9 k1 rauch/kontrolle_N4000_s9_k1.json rauch
}
spurB() {
  lauf cpu4 netz_N64000_s9_k1 code/zufallsnetz.py netz 64000 9 k1 rauch/netz_N64000_s9_k1.json rauch
  mkdir -p rauch/test-auswertung
  for N in 500 1000 2000; do
    for s in 1 2; do
      for f in k1 kl; do
        lauf cpu4 test_N${N}_s${s}_${f} code/zufallsnetz.py netz $N $s $f rauch/test-auswertung/netz_N${N}_s${s}_${f}.json
      done
    done
  done
}
spurA &
spurB &
wait
cp rauch/fcc.json rauch/test-auswertung/fcc.json 2>/dev/null
lauf cpu3 test_auswertung code/auswertung.py rauch/test-auswertung rauch/test-auswertung/auswertung.json 500,1000,2000
echo "$(date -u +%FT%TZ) rauch fertig" >> rauch/rauch.log
