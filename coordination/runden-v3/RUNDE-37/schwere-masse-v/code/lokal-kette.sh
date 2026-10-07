#!/bin/bash
# SCHWERE-MASSE-V: lokale Kette (nur ssh und Logs; Rechnung auf der .69 ueber kleintest.sh).
# Aufruf: bash lokal-kette.sh <spur> <omega> "h L" "h L" ...   bzw. Familie: <spur> fam "om h L" ...
SPUR=$1; shift
LOG=/home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-37/schwere-masse-v/lauf-69
R='cd /home/fmh/fmhc-physics-remote/schwere-masse-v && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh'
if [ "$1" = fam ]; then
  shift
  for ohl in "$@"; do
    set -- $ohl
    N=qb-o$1-h$2
    ssh -o BatchMode=yes fmh@192.168.178.69 "$R $SPUR sm-o$1-h$2 code/sm.py qball --om $1 --h $2 --L $3 --maxiter 20000 --tmax 480 --out lauf/$N.json --npz lauf/$N.npz" > $LOG/$N.log 2>&1
  done
else
  OM=$1; shift
  for hl in "$@"; do
    set -- $hl
    N=qb-o$OM-h$1
    ssh -o BatchMode=yes fmh@192.168.178.69 "$R $SPUR sm-o$OM-h$1 code/sm.py qball --om $OM --h $1 --L $2 --maxiter 20000 --tmax 480 --out lauf/$N.json --npz lauf/$N.npz" > $LOG/$N.log 2>&1
  done
fi
T=$(date '+%Y-%m-%d %H:%M:%S %Z')
printf 'kette %s fertig %s\n' "$SPUR" "$T" >> $LOG/ketten-fertig.txt
