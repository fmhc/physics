#!/bin/bash
# PHASE-3D-BLIND (Runde 31): echte Laeufe nach PLAN.md (eingefrorene Fassung PLAN.md.eingefroren-*), Code
# bic2_3d_suche_v2.py. Einmal von Hand per nohup auf der .69 gestartet; kein Dienst, kein Timer.
# Spuren cpu, cpu2, cpu3, cpu4, cpu6 (nicht cpu5, keine GPU). Je Sprosse: h004 (Fenster, Illinois), h002 (enge Klammer
# x* +- 1e-5 um die h004-Wurzel, h = 0,02), u004 (Umlauf-Rechteck auf x* +- d, h = 0,04), dazu Randprobe (R + 20) fuer
# b05-n18 und b1-km2 und die Rechtecke an den bekannten Sprossen (pb0-*-u004, Klammer aus rauch2/*-pb0-h004).
cd /home/fmh/fmhc-physics-remote/runde31-phase-3d-blind || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
D=/home/fmh/fmhc-physics-remote/runde31-phase-3d-blind
P=bic2_3d_suche_v2.py
G="--n-scan 5 --n-rho 1000 --n-dicht 801 --dicht-halb 0.04 --n-zoom 201 --korr-drho 1e-8 --n-rho-schritt 100 --n-dicht-schritt 201 --dicht-halb-schritt 2e-4 --iter-wurzel 80 --tol-wurzel 1e-11 --tol-x 1e-9 --iter-x 14 --u-n 60 --u-runden 50 --pr-drho 0.01 --pr-drho-max 0.03 --budget 560 --reserve 40"
lauf() {   # spur name argumente...
  local s=$1 n=$2
  shift 2
  bash $K $s r31pb-$n $P suche $G "$@" --out lauf/$n > $D/lauf/LAUF-$n.log 2>&1
}
h004() {   # spur name beta fensterargumente...
  local s=$1 n=$2 b=$3
  shift 3
  lauf $s $n-h004 --beta $b --h 0.04 --rechteck nein "$@"
}
h002() { lauf $1 $2-h002 --beta $3 --h 0.02 --klammer-aus lauf/$2-h004/suche.json --klammer-modus eng --klammer-halb 1e-5 --rechteck nein ; }
u004() { lauf $1 $2-u004 --beta $3 --h 0.04 --klammer-aus ${5:-lauf}/$2-h004/suche.json --klammer-modus eng --klammer-halb $4 --iter-x 0 --rechteck ja ; }
rand() { lauf $1 $2-rand --beta $3 --h 0.04 --r-zusatz 20 --klammer-aus lauf/$2-h004/suche.json --klammer-modus eng --klammer-halb 1e-5 --rechteck nein ; }
warte() {  # bis der Lauf $1 sein Ende geschrieben hat (hoechstens 40 min)
  local i=0
  until grep -q "^ende " $D/lauf/LAUF-$1.log 2>/dev/null || [ $i -ge 240 ]; do sleep 10; i=$((i + 1)); done
}
W16="--fenster-u 36.279306,38.586067 --x0 0.526715 --rho0 1.555432 --rho-steig 1.07"
W17="--fenster-u 38.586067,40.892827 --x0 0.525164 --rho0 1.553773 --rho-steig 1.07"
W18="--fenster-u 40.892827,43.199587 --x0 0.523783 --rho0 1.552296 --rho-steig 1.07"
WK0="--fenster-u 33.682376,36.278796 --x0 0.778587 --rho0 1.800790 --rho-steig 0.86"
WK1="--fenster-u 36.278796,38.875217 --x0 0.776612 --rho0 1.799091 --rho-steig 0.86"
WK2="--fenster-u 38.875217,41.471637 --x0 0.774892 --rho0 1.797612 --rho-steig 0.86"
mkdir -p $D/lauf
echo "KETTE-START $(date -Is)" > $D/lauf/KETTE.log
( h004 cpu6 b05-n18 0.5 $W18 ; h002 cpu6 b05-n18 0.5 ; u004 cpu6 b05-n18 0.5 5.2e-4 ; rand cpu6 b05-n18 0.5 ) &
( h004 cpu2 b1-km2 1.0 $WK2 ; h004 cpu2 b1-km1 1.0 $WK1 ; h002 cpu2 b1-km2 1.0 ; h002 cpu2 b1-km1 1.0 ; u004 cpu2 b1-km2 1.0 6.4e-4 ; rand cpu2 b1-km2 1.0 ) &
( h004 cpu b05-n16 0.5 $W16 ; h002 cpu b05-n16 0.5 ; u004 cpu b05-n16 0.5 6.6e-4 ; lauf cpu pb0-b05-u004 --beta 0.5 --h 0.04 --klammer-aus rauch2/b05-pb0-h004/suche.json --klammer-modus eng --klammer-halb 7.5e-4 --iter-x 0 --rechteck ja ) &
( h004 cpu3 b05-n17 0.5 $W17 ; h002 cpu3 b05-n17 0.5 ; u004 cpu3 b05-n17 0.5 5.8e-4 ) &
( h004 cpu4 b1-k0 1.0 $WK0 ; h002 cpu4 b1-k0 1.0 ; u004 cpu4 b1-k0 1.0 8.5e-4 ; lauf cpu4 pb0-b1-u004 --beta 1.0 --h 0.04 --klammer-aus rauch2/b1-pb0-h004/suche.json --klammer-modus eng --klammer-halb 9.9e-4 --iter-x 0 --rechteck ja ; warte b1-km1-h004 ; u004 cpu4 b1-km1 1.0 7.4e-4 ) &
wait
echo "KETTE-ENDE $(date -Is)" >> $D/lauf/KETTE.log
