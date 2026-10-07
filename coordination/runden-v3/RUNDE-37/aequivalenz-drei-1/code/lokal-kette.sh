#!/bin/bash
# Lokale Kette: startet je Konfiguration einen kleintest.sh-Lauf auf der .69 (Rechnung nur dort).
# Aufruf: bash lokal-kette.sh <spur> "<name> <args...>" ["<name> <args...>" ...]
set -u
SPUR=$1
shift
R=/home/fmh/fmhc-physics-remote/aequivalenz-drei-1
for job in "$@"; do
  set -- $job
  NAME=$1
  shift
  FREI=$(ssh -o BatchMode=yes fmh@192.168.178.69 "df -BG --output=avail /home | tail -1 | tr -dc 0-9")
  printf '%s %s frei %s GB\n' "$(date '+%H:%M:%S')" "$NAME" "$FREI"
  if [ "${FREI:-0}" -lt 10 ]; then
    echo "Abbruch: unter 10 GB frei"
    exit 1
  fi
  ssh -o BatchMode=yes fmh@192.168.178.69 "cd $R/lauf && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh $SPUR aq$NAME $R/code/aq.py $R/lauf/$NAME.json $* > $R/lauf/$NAME.log 2>&1; tail -3 $R/lauf/$NAME.log"
  printf '%s %s fertig\n' "$(date '+%H:%M:%S')" "$NAME"
done
