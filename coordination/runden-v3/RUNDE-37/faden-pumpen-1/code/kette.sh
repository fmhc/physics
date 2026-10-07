#!/bin/bash
# FADEN-PUMPEN-1: lokale Kette (nur ssh und Logs; Rechnung auf der .69 ueber kleintest.sh).
# Aufruf: bash kette.sh <spur> <name> "<argumente>" [<name> "<argumente>" ...]
SPUR=$1; shift
LOG=/home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-37/faden-pumpen-1/lauf-69
R='cd /home/fmh/fmhc-physics-remote/faden-pumpen-1 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh'
while [ $# -ge 2 ]; do
  N=$1; ARGS=$2; shift 2
  ssh -o BatchMode=yes fmh@192.168.178.69 "$R $SPUR fp-$N $ARGS" > $LOG/$N.log 2>&1
done
T=$(date '+%Y-%m-%d %H:%M:%S %Z')
printf 'kette %s fertig %s\n' "$SPUR" "$T" >> $LOG/ketten-fertig.txt
