#!/bin/bash
# QUANT-1: lokale Kette (nur ssh und Logs; Rechnung auf der .69 ueber kleintest.sh, je Lauf <= 10 min).
# Aufruf: bash kette.sh <spur> <name> "<q1-argumente ohne --out>" [<name> "<argumente>" ...]
SPUR=$1; shift
LOG=/home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-37/quant-1/lauf-69
R='cd /home/fmh/fmhc-physics-remote/quant-1 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh'
while [ $# -ge 2 ]; do
  N=$1; A=$2; shift 2
  FREI=$(ssh -o BatchMode=yes fmh@192.168.178.69 "df --output=avail -BG /home | tail -1 | tr -dc 0-9")
  if [ "${FREI:-0}" -lt 10 ]; then
    printf 'ABBRUCH vor %s: nur %s GB frei\n' "$N" "$FREI" >> $LOG/ketten-fertig.txt
    exit 4
  fi
  ssh -o BatchMode=yes fmh@192.168.178.69 "$R $SPUR q1-$N code/q1.py hmc $A --out lauf/$N" > $LOG/$N.log 2>&1
  T=$(date '+%Y-%m-%d %H:%M:%S %Z')
  printf 'lauf %s spur %s fertig %s (df vorher %s GB)\n' "$N" "$SPUR" "$T" "$FREI" >> $LOG/ketten-fertig.txt
done
