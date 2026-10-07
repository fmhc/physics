#!/bin/bash
# HODGE-MASSE-1, einmalige Laufkette je Spur (kein Dienst, kein Timer). Aufruf: bash code/kette.sh <cpu8|cpu9|cpu10|cpu3|cpu4>
# Jeder Lauf ueber kleintest.sh (1 Thread, <= 600 s je Aufruf). td-Laeufe: nicht fertige werden mit Zwischenstand
# sofort fortgesetzt (hoechstens 4 Abschnitte). Schlusszeit: nach 2026-10-05 09:25:00 UTC (11:25 CEST) startet kein Aufruf.
set -u
SP=$1
cd /home/fmh/fmhc-physics-remote/hodge-masse-1 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SCHLUSS=$(date -u -d '2026-10-05 09:25:00' +%s)
spanne() {   # spanne <netz> [ridx a|b]
  local netz=$1 teil=${2:-}
  local name="sp-${netz}" extra=""
  if [ -n "$teil" ]; then
    name="${name}-${teil}"
    if [ "$teil" = "a" ]; then extra="--ridx 0-6"; else extra="--ridx 7-12"; fi
  fi
  if [ "$(date -u +%s)" -ge "$SCHLUSS" ]; then echo "$name nicht gestartet (Schlusszeit)"; return; fi
  bash "$K" "$SP" "hm-$name" code/hm.py spanne --netz "$netz" $extra --out "lauf/${name}.json" > "lauf/${name}.log" 2>&1
  echo "$name rc=$? $(date -u +%H:%M:%S)"
}
td() {   # td <kin> <red> <saat> <arm> [mess]
  local kin=$1 red=$2 s=$3 arm=$4 mess=${5:-}
  local name="td-${kin}${red}-s${s}-${arm}" extra=""
  if [ "$mess" = "mess" ]; then name="td-mess-s${s}-${arm}"; extra="--messformen"; fi
  for abschn in 1 2 3 4; do
    if [ "$(date -u +%s)" -ge "$SCHLUSS" ]; then echo "$name Abschnitt $abschn nicht gestartet (Schlusszeit)"; return; fi
    bash "$K" "$SP" "hm-${name}-${abschn}" code/hm_td.py lauf --kin "$kin" --red "$red" $extra --netz "glas-N128-s${s}" --A 1e-3 --arm "$arm" --lesart R --h 0.5 --budget 500 --out "lauf/${name}.json" > "lauf/${name}-${abschn}.log" 2>&1
    local rc=$?
    echo "$name Abschnitt $abschn rc=$rc $(date -u +%H:%M:%S)"
    [ $rc -ne 0 ] && return
    [ "$(jq -r .ergebnis.fertig lauf/${name}.json 2>/dev/null)" = "true" ] && return
  done
}
case "$SP" in
  cpu8)  spanne V; spanne S; spanne A15; spanne glas-s1 a; spanne glas-s1 b ;;
  cpu9)  spanne glas-s2 a; spanne glas-s2 b; spanne glas-s3 a; spanne glas-s3 b ;;
  cpu10) spanne glas-s4 a; spanne glas-s4 b; td A2 R1 4 b; td A2 R1 4 a ;;
  cpu3)  td A2 R1 1 b; td A2 R1 1 a; td A2 R1 2 b; td A2 R1 2 a; td A2 R1 3 b; td A2 R1 3 a ;;
  cpu4)  td A2L R1 1 b; td A2L R1 2 b; td A2L R1 3 b; td A2L R1 4 b; td A1 R1 1 b mess; td A1 R1 3 b mess; td A1 R1 2 b mess ;;
  *) echo "unbekannte Spur $SP"; exit 2 ;;
esac
echo "kette $SP fertig $(date -u +%H:%M:%S)"
