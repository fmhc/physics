#!/bin/bash
# PHASE-3D-BLIND (Runde 31): zweiter Rauchlauf = PB0-Kontrolle mit Code Version 2 (bic2_3d_suche_v2.py), an den
# bekannten Sprossen, ausserhalb der echten Fenster (u_bekannt +- 0,4 b wie rauch.sh). Je Sprosse drei Laeufe wie im
# Plan: h004 (Fenster, Illinois, ohne Rechteck), u004 (Rechteck auf den Startzeilen von h004), h002 (enge Klammer
# x* +- 1e-5 um die h004-Wurzel). Einmal von Hand per nohup auf der .69 gestartet; kein Dienst, kein Timer.
# Spuren cpu3 (beta = 1/2) und cpu4 (beta = 1).
cd /home/fmh/fmhc-physics-remote/runde31-phase-3d-blind || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
D=/home/fmh/fmhc-physics-remote/runde31-phase-3d-blind
P=bic2_3d_suche_v2.py
G="--n-scan 5 --n-rho 1000 --n-dicht 801 --dicht-halb 0.04 --n-zoom 201 --korr-drho 1e-8 --n-rho-schritt 100 --n-dicht-schritt 201 --dicht-halb-schritt 2e-4 --iter-wurzel 80 --tol-wurzel 1e-11 --tol-x 1e-9 --iter-x 14 --u-n 60 --u-runden 50 --pr-drho 0.01 --pr-drho-max 0.03 --budget 560 --reserve 40"
lauf() {   # spur name argumente...
  local s=$1 n=$2
  shift 2
  bash $K $s r31pb-$n $P suche $G "$@" --out rauch2/$n > $D/rauch2/LAUF-$n.log 2>&1
}
kette() {  # spur name beta fensterargumente...
  local s=$1 n=$2 b=$3
  shift 3
  lauf $s $n-h004 --beta $b --h 0.04 --rechteck nein "$@"
  lauf $s $n-u004 --beta $b --h 0.04 --klammer-aus rauch2/$n-h004/suche.json --klammer-modus start --iter-x 0 --rechteck ja
  lauf $s $n-h002 --beta $b --h 0.02 --klammer-aus rauch2/$n-h004/suche.json --klammer-modus eng --klammer-halb 1e-5 --rechteck nein
}
mkdir -p $D/rauch2
echo "RAUCH2-START $(date -Is)" > $D/rauch2/KETTE.log
( kette cpu3 b05-pb0 0.5 --fenster-u 34.203222,36.048630 --x0 0.528469 --rho0 1.557309 --rho-steig 1.07 ) &
( kette cpu4 b1-pb0 1.0 --fenster-u 31.345598,33.422734 --x0 0.780879 --rho0 1.802761 --rho-steig 0.86 ) &
wait
echo "RAUCH2-ENDE $(date -Is)" >> $D/rauch2/KETTE.log
