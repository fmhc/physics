#!/bin/bash
# LEITER-3D-PRAEZ (Runde 13), Laeufe nach PLAN.md (eingefrorene Fassung, siehe PLAN.md.eingefroren-*).
# Einmal von Hand per nohup auf der .69 gestartet; kein Dienst, kein Timer. Nur Spuren cpu und cpu2 (Zusatz der Leitung).
cd /home/fmh/fmhc-physics-remote/runde13-leiter3d-praez || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
D=/home/fmh/fmhc-physics-remote/runde13-leiter3d-praez
P=bic2_3d_praez.py
G="--beta 0.5 --n-zeilen 9 --zeilen-dx 2.5e-4 --n-rho 400 --n-dicht 401 --dicht-halb 0.02 --u-n 60 --u-runden 30 --pr-drho 0.01 --pr-drho-max 0.03 --pr-u-halb 3 --iter-wurzel 80 --tol-wurzel 1e-13 --budget 500 --reserve 150"
K1="--x0 0.797677 --rho0 1.744618 --rho-steig 0.4049 --x-pol 0.797677 --art k1"
K2="--x0 0.56940 --rho0 1.5991684 --rho-steig 2.8 --x-pol 0.56940 --art k2"
N7="--x0 0.5598 --rho0 1.5897567 --rho-steig 3.3 --x-pol 0.5598"
N8="--x0 0.5526 --rho0 1.5826358 --rho-steig 3.9 --x-pol 0.5526"
N9="--x0 0.5470 --rho0 1.5772052 --rho-steig 4.6 --x-pol 0.5470"
N10="--x0 0.5424 --rho0 1.57178 --rho-steig 5.3 --x-pol 0.5424"
lauf() {   # spur name h argumente...
  local s=$1 n=$2 h=$3
  shift 3
  bash $K $s $n $P praez $G --h $h "$@" --out lauf-69/$n > $D/LAUF-$n.log 2>&1
}
regel() {  # name art x_pol dateien [rho_pol]
  local n=$1 art=$2 xp=$3 da=$4 rp=${5:-}
  if [ -n "$rp" ]; then
    bash $K cpu $n $P regel --art $art --x-pol $xp --rho-pol $rp --dateien $da --out lauf-69/$n > $D/LAUF-$n.log 2>&1
  else
    bash $K cpu $n $P regel --art $art --x-pol $xp --dateien $da --out lauf-69/$n > $D/LAUF-$n.log 2>&1
  fi
}
echo "KETTE-START $(date -Is)" > $D/KETTE.log
# Phase 1: Kontrollen K1 und K2 auf beiden Stufen (h = 0,04 und h/2 = 0,02)
( lauf cpu  k2-h002 0.02 $K2 ; lauf cpu  k1-h004 0.04 $K1 ) &
( lauf cpu2 k1-h002 0.02 $K1 ; lauf cpu2 k2-h004 0.04 $K2 ) &
wait
regel regel-k1 k1 0.797677 lauf-69/k1-h004/praez.json,lauf-69/k1-h002/praez.json 1.744618
regel regel-k2 k2 0.56940 lauf-69/k2-h004/praez.json,lauf-69/k2-h002/praez.json
if grep -q -- "-> bestanden" $D/LAUF-regel-k1.log && grep -q -- "-> bestanden" $D/LAUF-regel-k2.log; then
  echo "KONTROLLEN BESTANDEN $(date -Is)" >> $D/KETTE.log
else
  echo "KONTROLLE VERFEHLT, Abbruch $(date -Is)" >> $D/KETTE.log
  exit 0
fi
# Phase 2: Stellen n = 7, 8, 9, 10 (Reihenfolge nach Vorrang)
( lauf cpu  n7-h002 0.02 $N7 ; lauf cpu  n8-h004 0.04 $N8 ; lauf cpu  n9-h002 0.02 $N9 ; lauf cpu  n10-h004 0.04 $N10 ) &
( lauf cpu2 n7-h004 0.04 $N7 ; lauf cpu2 n8-h002 0.02 $N8 ; lauf cpu2 n9-h004 0.04 $N9 ; lauf cpu2 n10-h002 0.02 $N10 ) &
wait
regel regel-n7 leiter 0.5598 lauf-69/n7-h004/praez.json,lauf-69/n7-h002/praez.json
regel regel-n8 leiter 0.5526 lauf-69/n8-h004/praez.json,lauf-69/n8-h002/praez.json
regel regel-n9 leiter 0.5470 lauf-69/n9-h004/praez.json,lauf-69/n9-h002/praez.json
regel regel-n10 leiter 0.5424 lauf-69/n10-h004/praez.json,lauf-69/n10-h002/praez.json
echo "KETTE-ENDE $(date -Is)" >> $D/KETTE.log
