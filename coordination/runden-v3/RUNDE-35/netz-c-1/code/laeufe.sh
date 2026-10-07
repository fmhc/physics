#!/bin/bash
# NETZ-C-1 (Runde 35): Hauptlaeufe auf der .69, zwei Spuren (cpu3, cpu4) parallel, je Spur nacheinander.
# Jeder Lauf einzeln ueber kleintest.sh (Lock je Spur, 1 Thread, MemoryMax 4G, Abbruch nach 600 s).
# Zeitschritt (PLAN 3.1): dt1 = 0,0125 fuer h >= 0,125 (Teiler 80 h), dt1 = 0,01 fuer h = 0,1; Probe dt2 = dt1/2.
# Aufruf: bash code/laeufe.sh  (im Ordner /home/fmh/fmhc-physics-remote/runde35-netz)
set -u
cd /home/fmh/fmhc-physics-remote/runde35-netz
KT=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
# F = (4 eta / pi) q mit eta = 0,01 und q = pi F/(4 eta) = 0,3; 1; 3; 10
declare -A FQ=( [0.3]=0.0038197186342054883 [1.0]=0.012732395447351628 [3.0]=0.038197186342054883 [10.0]=0.12732395447351628 )
# Teiler (dt = h/Teiler) je h fuer dt1; dt2 = doppelter Teiler
declare -A TE=( [0.1]=10 [0.125]=10 [0.25]=20 [0.5]=40 [1]=80 )

# Lauf mit Fortsetzung: bis zu 4 Aufrufe, solange die Kopfdatei "unterbrochen" meldet
lauf() {
  local spur=$1 kurz=$2 name=$3; shift 3
  local i
  for i in 1 2 3 4; do
    bash $KT "$spur" "$kurz" code/kette.py "lauf/$name" "$@" >> "lauf/$name.log" 2>&1
    if ! grep -q '"status": "unterbrochen"' "lauf/$name.json" 2>/dev/null; then
      break
    fi
  done
}

spur3() {
  lauf cpu3 r35k4 f_h0.125_dt2 0.125 0.02 0 0 3312 $((2*${TE[0.125]})) 3420 50
  for D in 1 2; do
    lauf cpu3 r35k0 k0_h0.1_dt$D 0.1 0 0 0.9 300 $((D*${TE[0.1]})) 400 50
    lauf cpu3 r35k0 k0_h1_dt$D 1 0 0 0.9 300 $((D*${TE[1]})) 400 50
    for Q in 0.3 1.0 3.0 10.0; do
      lauf cpu3 r35b1 r_h1_q${Q}_dt$D 1 ${FQ[$Q]} 0.01 0 1000 $((D*${TE[1]})) 1150 50
    done
    lauf cpu3 r35k4 f_h0.5_dt$D 0.5 0.02 0 0 828 $((D*${TE[0.5]})) 930 50
    lauf cpu3 r35k4 f_h0.25_dt$D 0.25 0.02 0 0 1656 $((D*${TE[0.25]})) 1760 50
  done
  date -u '+%Y-%m-%dT%H:%M:%SZ spur3 fertig' >> lauf/laeufe_fertig.txt
}

spur4() {
  bash $KT cpu4 r35a code/netz_a.py lauf/netz_a.json > lauf/netz_a.log 2>&1
  lauf cpu4 r35k4 f_h0.125_dt1 0.125 0.02 0 0 3312 ${TE[0.125]} 3420 50
  for D in 1 2; do
    for Q in 0.3 1.0 3.0 10.0; do
      lauf cpu4 r35b1 r_h0.1_q${Q}_dt$D 0.1 ${FQ[$Q]} 0.01 0 1000 $((D*${TE[0.1]})) 1150 50
    done
  done
  date -u '+%Y-%m-%dT%H:%M:%SZ spur4 fertig' >> lauf/laeufe_fertig.txt
}

date -u '+%Y-%m-%dT%H:%M:%SZ start' >> lauf/laeufe_fertig.txt
spur3 &
spur4 &
wait
