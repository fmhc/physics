#!/bin/bash
# TAKT-DYNAMIK-1, einmalige Laufkette je Spur (kein Dienst, kein Timer). Aufruf: bash code/kette.sh <cpu8|cpu9|cpu10>
# Jeder Lauf ueber kleintest.sh (1 Thread, <= 600 s je Aufruf); nicht fertige Laeufe werden mit ihrem Zwischenstand
# sofort fortgesetzt (hoechstens 4 Abschnitte). Schlusszeit: nach 2026-10-05 08:20:00 UTC (10:20 CEST) startet kein neuer Aufruf.
set -u
SP=$1
cd /home/fmh/fmhc-physics-remote/takt-dynamik-1 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SCHLUSS=$(date -u -d '2026-10-05 08:20:00' +%s)
lauf() {   # lauf <netz> <A> <arm> [lesart] [h]
  local netz=$1 A=$2 arm=$3 les=${4:-R} h=${5:-0.5}
  local name="td-${netz}-A${A}-${arm}"
  [ "$les" = "P" ] && name="${name}-P"
  [ "$h" = "0.25" ] && name="${name}-h025"
  local extra=""
  if [ "$arm" = "c" ]; then
    local bn="lauf/td-${netz}-A${A}-b"; [ "$h" = "0.25" ] && bn="${bn}-h025"
    if [ "$(jq -r .ergebnis.fertig ${bn}.json 2>/dev/null)" != "true" ]; then echo "$name nicht gestartet (Arm b fehlt)"; return; fi
    extra="--ereignisse ${bn}.json"
  fi
  for abschn in 1 2 3 4; do
    if [ "$(date -u +%s)" -ge "$SCHLUSS" ]; then echo "$name Abschnitt $abschn nicht gestartet (Schlusszeit) $(date -u +%H:%M:%S)"; return; fi
    bash "$K" "$SP" "${name}-${abschn}" code/td.py lauf --netz "$netz" --A "$A" --arm "$arm" --lesart "$les" --h "$h" --budget 500 $extra --out "lauf/${name}.json" > "lauf/${name}-${abschn}.log" 2>&1
    local rc=$?
    echo "$name Abschnitt $abschn rc=$rc $(date -u +%H:%M:%S)"
    [ $rc -ne 0 ] && return
    [ "$(jq -r .ergebnis.fertig lauf/${name}.json 2>/dev/null)" = "true" ] && return
  done
}
case "$SP" in
  cpu8)
    lauf glas-N128-s1 1e-3 a; lauf glas-N128-s1 1e-3 b; lauf glas-N128-s4 1e-3 a; lauf glas-N128-s4 1e-3 b
    lauf glas-N128-s1 1e-3 c; lauf glas-N128-s4 1e-3 c
    lauf glas-N128-s1 1e-2 a; lauf glas-N128-s1 1e-2 b; lauf glas-N128-s1 1e-2 c
    lauf VD2 1e-3 a; lauf VD2 1e-3 b; lauf VD2 1e-2 a; lauf VD2 1e-2 b
    lauf glas-N128-s1 1e-3 b P; lauf glas-N128-s1 1e-3 a R 0.25; lauf glas-N128-s1 1e-3 b R 0.25
    lauf glas-N128-s1 1e-2 b P ;;
  cpu9)
    lauf glas-N128-s2 1e-3 a; lauf glas-N128-s2 1e-3 b; lauf glas-N128-s2 1e-3 c
    lauf glas-N128-s2 1e-2 a; lauf glas-N128-s2 1e-2 b; lauf glas-N128-s2 1e-2 c
    lauf glas-N128-s4 1e-2 a; lauf glas-N128-s4 1e-2 b; lauf glas-N128-s4 1e-2 c
    lauf glas-N128-s2 1e-3 b P; lauf glas-N128-s2 1e-3 a R 0.25; lauf glas-N128-s2 1e-3 b R 0.25
    lauf glas-N128-s2 1e-2 b P ;;
  cpu10)
    lauf glas-N128-s3 1e-3 a; lauf glas-N128-s3 1e-3 b; lauf glas-N128-s3 1e-3 c
    lauf glas-N128-s3 1e-2 a; lauf glas-N128-s3 1e-2 b; lauf glas-N128-s3 1e-2 c
    lauf glas-N128-s3 1e-3 b P; lauf glas-N128-s4 1e-3 b P
    lauf glas-N128-s3 1e-3 a R 0.25; lauf glas-N128-s3 1e-3 b R 0.25; lauf glas-N128-s4 1e-3 a R 0.25; lauf glas-N128-s4 1e-3 b R 0.25
    lauf glas-N128-s3 1e-2 b P; lauf glas-N128-s4 1e-2 b P ;;
esac
echo "kette $SP ende $(date -u +%H:%M:%S)"
