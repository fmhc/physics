#!/bin/bash
# RUNDE-33 r33-messung: Rauchlauf vor dem Einfrieren. Nur an den bekannten Sprossen k = 0, -1, -2 (RUNDE-31) und bei
# z >= 112 (jenseits aller Zielfenster; das letzte Fenster endet bei Abstaenden um b_inf nahe z ~ 102). Kein Zeilen-
# lauf im Bereich 41,1 <= z <= 106. Einmal von Hand per nohup auf der .69 gestartet; kein Dienst, kein Timer.
# Spuren cpu, cpu2, cpu3, cpu4 (nicht cpu5, keine GPU).
cd /home/fmh/fmhc-physics-remote/runde33-messung || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
D=/home/fmh/fmhc-physics-remote/runde33-messung
P=r33_stab.py
lauf() {   # spur name argumente...
  local s=$1 n=$2
  shift 2
  bash $K $s r33m-$n $P "$@" --out rauch/$n > $D/rauch/LAUF-$n.log 2>&1
}
mkdir -p $D/rauch
echo "RAUCH-START $(date -Is)" > $D/rauch/KETTE.log
# cpu: Profil skalar gegen bic2.profil (k = -2 und z = 112), dann Kontrolle k = 0 (RUNDE-31 h002 0,7785854399; +-1e-5)
( lauf cpu r-profil profilvergleich --h 0.04 --z-liste 40.18844229618716,112.0 ;
  lauf cpu r-k0-h004 wurzel --h 0.04 --klammer-x 0.7785754399,0.7785954399 ;
  lauf cpu r-k0-h002 wurzel --h 0.02 --klammer-x 0.7785754399,0.7785954399 --rechteck nein ) &
# cpu2: Gleichwertigkeit mit dem direkten Verfahren (RUNDE-31) zwischen bekannten Sprossen, dann Wachstum und
# erreichbare Genauigkeit bei z = 112 .. 115 (R ~ 56 .. 58): n_orth 0 (nur Schluss-Orthonormierung = direkt), 2, 8, 32
( lauf cpu2 r-gleich zeilen --h 0.04 --z-liste 36.28,38.88 --vergleich 0,2,32 --r31 ja ;
  lauf cpu2 r-weit zeilen --h 0.04 --z-liste 112.0,112.327325,115.0 --vergleich 0,2,32 --r31 ja ) &
# cpu3: ganze Kette an der bekannten Sprosse k = -1 (Fenster aus k = 0 plus b_inf, Abtastung dz = b_inf/8, nur
# z <= 39,9): zeilen -> wurzel (aus zeilen) -> h002 und Randprobe (aus wurzeln) -> kette (Start k = 0)
( lauf cpu3 r-km1-zeilen zeilen --h 0.04 --z0 35.964819535665684 --dz 0.327325 --j-von 0 --j-bis 12 ;
  lauf cpu3 r-km1-h004 wurzel --h 0.04 --aus-zeilen rauch/r-km1-zeilen/zeilen.json ;
  lauf cpu3 r-km1-h002 wurzel --h 0.02 --aus-wurzeln rauch/r-km1-h004/wurzel.json --klammer-halb 1e-5 --rechteck nein ;
  lauf cpu3 r-km1-rand wurzel --h 0.04 --r-zusatz 20 --aus-wurzeln rauch/r-km1-h004/wurzel.json --klammer-halb 1e-5 --rechteck nein ;
  lauf cpu3 r-km1-kette kette --dz 0.327325 --aus-zeilen rauch/r-km1-zeilen/zeilen.json --aus-wurzeln rauch/r-km1-h004/wurzel.json --aus-h002 rauch/r-km1-h002/wurzel.json --aus-rand rauch/r-km1-rand/wurzel.json --z-start 34.982844535665684 --umlauf-start -1 --start-quelle Rauchlauf-k0 ) &
# cpu4: Kontrolle k = -2 (RUNDE-31 h002 0,7748827758; +-1e-5)
( lauf cpu4 r-km2-h004 wurzel --h 0.04 --klammer-x 0.7748727758,0.7748927758 ;
  lauf cpu4 r-km2-h002 wurzel --h 0.02 --klammer-x 0.7748727758,0.7748927758 --rechteck nein ) &
wait
echo "RAUCH-ENDE $(date -Is)" >> $D/rauch/KETTE.log
