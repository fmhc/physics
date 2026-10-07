#!/bin/bash
# QBALL-GITTER-1 (Runde 35): Hauptlaeufe auf der .69, zwei Spuren (cpu3, cpu4) parallel, je Spur nacheinander.
# Jeder Lauf einzeln ueber kleintest.sh (Lock je Spur, 1 Thread, MemoryMax 4G, Abbruch nach 600 s);
# Laeufe ueber 500 s Wandzeit schreiben einen Checkpoint und werden mit denselben Argumenten fortgesetzt.
# PLAN Abschnitt 5: dt1 = 0,02, dt2 = 0,01; Fenster 400 (lang: 800); a0 = Q0 E/M0 = 0,005 (E1) bzw. 0,01 (E2).
# Aufruf: bash code/laeufe.sh  (im Ordner /home/fmh/fmhc-physics-remote/runde35-qgitter)
set -u
cd /home/fmh/fmhc-physics-remote/runde35-qgitter
KT=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh

lauf() {
  local spur=$1 kurz=$2 name=$3; shift 3
  local i
  for i in 1 2 3 4 5; do
    bash $KT "$spur" "$kurz" code/qgitter.py "lauf/$name" "$@" >> "lauf/$name.log" 2>&1
    if ! grep -q '"status": "unterbrochen"' "lauf/$name.json" 2>/dev/null; then
      break
    fi
  done
}

spur3() {
  for H in 0.125 0.25 0.5; do
    lauf cpu3 r35qg0 g0_h$H $H 0 500 0.02 400
  done
  for H in 0.125 0.25 0.5; do
    lauf cpu3 r35qf1 f1_h${H}_dt1 $H 0.005 TB+25 0.02 400
  done
  for H in 0.5 0.25 0.125; do
    lauf cpu3 r35qf2 f2_h${H}_dt1 $H 0.01 TB+25 0.02 400
  done
  for H in 0.5 0.25; do
    lauf cpu3 r35qp2 f1_h${H}_dt2 $H 0.005 TB+25 0.01 400
  done
  date -u '+%Y-%m-%dT%H:%M:%SZ spur3 fertig' >> lauf/laeufe_fertig.txt
}

spur4() {
  lauf cpu4 r35qp2 f1_h0.125_dt2 0.125 0.005 TB+25 0.01 400
  lauf cpu4 r35qpl f1_h0.125_lang 0.125 0.005 TB+25 0.02 800
  date -u '+%Y-%m-%dT%H:%M:%SZ spur4 fertig' >> lauf/laeufe_fertig.txt
}

date -u '+%Y-%m-%dT%H:%M:%SZ start' >> lauf/laeufe_fertig.txt
spur3 &
spur4 &
wait
bash $KT cpu3 r35qaw code/auswertung.py lauf lauf/auswertung.json > lauf/auswertung.log 2>&1
date -u '+%Y-%m-%dT%H:%M:%SZ auswertung fertig' >> lauf/laeufe_fertig.txt
