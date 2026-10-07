#!/bin/bash
# RUNDE-33 r33-messung: echte Laeufe nach PLAN.md (eingefrorene Fassung PLAN.md.eingefroren-*), Code r33_stab.py.
# Einmal von Hand per nohup auf der .69 gestartet; kein Dienst, kein Timer. Spuren cpu, cpu2, cpu3, cpu4 (hoechstens
# vier zugleich; nicht cpu5, keine GPU). Je Aufruf <= 600 s (kleintest.sh), intern Budget 540 s.
# Phase 1 Abtastung (13 Abschnitte zu 17 Zeilen, Randzeilen doppelt), Phase 2 Wurzeln h = 0,04 mit Umlauf-Rechteck
# (8 Teile), Phase 3 Gitter h = 0,02 und Randprobe R + 20 (je 8 Teile), Phase 4 Fensterlogik (kette).
# Jeder Teil der Phasen 2 und 3 wird einmal mit --fortsetzen wiederholt (nur Klammern ohne Ergebnis, sonst leer).
cd /home/fmh/fmhc-physics-remote/runde33-messung || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
D=/home/fmh/fmhc-physics-remote/runde33-messung
P=r33_stab.py
Z0=41.17041729618716   # z(k = -2, RUNDE-31 h002) + b_inf/2 - dz
DZ=0.327325            # b_inf/8
lauf() {   # spur name argumente...
  local s=$1 n=$2
  shift 2
  bash $K $s r33m-$n $P "$@" --out lauf/$n > $D/lauf/LAUF-$n.log 2>&1
}
fort() {   # spur name argumente... (Wiederholung mit --fortsetzen, eigenes Log)
  local s=$1 n=$2
  shift 2
  bash $K $s r33m-$n-f $P "$@" --out lauf/$n --fortsetzen > $D/lauf/LAUF-$n-fort.log 2>&1
}
zeilen() { lauf $1 z-c$2 zeilen --h 0.04 --z0 $Z0 --dz $DZ --j-von $((16 * $2)) --j-bis $((16 * $2 + 16)) ; }
W="--h 0.04 --aus-zeilen lauf/z-c*/zeilen.json --teile 8"
G="--h 0.02 --aus-wurzeln lauf/w-p*/wurzel.json --klammer-halb 1e-5 --rechteck nein --teile 8"
R="--h 0.04 --r-zusatz 20 --aus-wurzeln lauf/w-p*/wurzel.json --klammer-halb 1e-5 --rechteck nein --teile 8"
wurzel() { lauf $1 w-p$2 wurzel $W --teil $2 ; fort $1 w-p$2 wurzel $W --teil $2 ; }
gitter() { lauf $1 g-p$2 wurzel $G --teil $2 ; fort $1 g-p$2 wurzel $G --teil $2 ; }
rand() { lauf $1 r-p$2 wurzel $R --teil $2 ; fort $1 r-p$2 wurzel $R --teil $2 ; }
set -f   # keine Dateinamen-Erweiterung der Muster lauf/*-p*/... in bash (Python liest sie per glob)
mkdir -p $D/lauf
echo "KETTE-START $(date -Is)" > $D/lauf/KETTE.log
( zeilen cpu 0 ; zeilen cpu 4 ; zeilen cpu 8 ; zeilen cpu 12 ) &
( zeilen cpu2 1 ; zeilen cpu2 5 ; zeilen cpu2 9 ) &
( zeilen cpu3 2 ; zeilen cpu3 6 ; zeilen cpu3 10 ) &
( zeilen cpu4 3 ; zeilen cpu4 7 ; zeilen cpu4 11 ) &
wait
echo "PHASE1-ENDE $(date -Is)" >> $D/lauf/KETTE.log
( wurzel cpu 0 ; wurzel cpu 4 ) &
( wurzel cpu2 1 ; wurzel cpu2 5 ) &
( wurzel cpu3 2 ; wurzel cpu3 6 ) &
( wurzel cpu4 3 ; wurzel cpu4 7 ) &
wait
echo "PHASE2-ENDE $(date -Is)" >> $D/lauf/KETTE.log
( gitter cpu 0 ; gitter cpu 4 ; rand cpu 0 ; rand cpu 4 ) &
( gitter cpu2 1 ; gitter cpu2 5 ; rand cpu2 1 ; rand cpu2 5 ) &
( gitter cpu3 2 ; gitter cpu3 6 ; rand cpu3 2 ; rand cpu3 6 ) &
( gitter cpu4 3 ; gitter cpu4 7 ; rand cpu4 3 ; rand cpu4 7 ) &
wait
echo "PHASE3-ENDE $(date -Is)" >> $D/lauf/KETTE.log
bash $K cpu r33m-kette $P kette --dz $DZ --aus-zeilen 'lauf/z-c*/zeilen.json' --aus-wurzeln 'lauf/w-p*/wurzel.json' \
  --aus-h002 'lauf/g-p*/wurzel.json' --aus-rand 'lauf/r-p*/wurzel.json' \
  --out lauf/MESSUNG-R33-VERSIEGELT.json > $D/lauf/LAUF-kette.log 2>&1
echo "KETTE-ENDE $(date -Is)" >> $D/lauf/KETTE.log
