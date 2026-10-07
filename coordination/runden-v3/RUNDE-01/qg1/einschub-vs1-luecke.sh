#!/bin/bash
# Einmaliges Einschieben von QG-1 (Runde 1 nach v3) in eine VS-1-Portionsluecke. Leitung claude-primary, 30.09.2026.
# Kein Dienst, kein Timer: einmal per nohup setsid gestartet, endet von selbst.
# Ablauf: Ende der laufenden VS-1-Portion abwarten; Kette nur anhalten, wenn sie nachweislich in ihrer 10-s-Pause ist;
# QG-1 Rauchtest und Hauptlauf unter dem gemeinsamen Lock; VS-1-Kette mit derselben Freigabe neu starten (nur nach rc=75).
set -u
VS=/home/fmh/fmhc-physics-remote/vs1-20260929
Q=/home/fmh/fmhc-physics-remote/qg1-20260930
KETTE_PID=${1:?PID der VS-1-Kette}
UNIT_ALT=${2:?Unitname der laufenden VS-1-Portion}
LOCK=/home/fmh/fmhc-physics-remote/gauntlet-gpu.lock
GPU=GPU-127dc217-5693-98a2-3209-573ba346484f
PY=/home/fmh/fmhc-physics-gpu-venv/bin/python
exec >>"$Q/EINSCHUB.log" 2>&1
echo "start $(date --iso-8601=seconds) kette=$KETTE_PID portion=$UNIT_ALT"
for i in $(seq 1 2400); do
  grep -q "^$UNIT_ALT rc=" "$VS/HAUPTLAUF-UNITS.txt" && break
  sleep 1
done
sleep 1
RCZEILE=$(grep "^$UNIT_ALT rc=" "$VS/HAUPTLAUF-UNITS.txt" || true)
PREV=$(tail -n 2 "$VS/HAUPTLAUF-UNITS.txt" | head -n 1)
echo "portionsende: '$RCZEILE' vorletzte Zeile: '$PREV' $(date --iso-8601=seconds)"
if [ "$PREV" != "$UNIT_ALT rc=75" ]; then
  echo "nicht nachweislich in der 10-s-Pause nach rc=75: kein Eingriff, Ende"
  exit 1
fi
kill "$KETTE_PID"
sleep 2
if ps -p "$KETTE_PID" >/dev/null; then echo "Kette lebt noch: Ende ohne QG-1"; exit 1; fi
if systemctl --user list-units 'fmhc-physics-vs1-teil-*' --no-legend | grep -q running; then
  echo "eine VS-1-Portion laeuft trotzdem: Ende ohne QG-1"; exit 1
fi
echo "VS-1-Kette angehalten $(date --iso-8601=seconds)"
HHMM=$(date +%H%M)
flock -w 45 "$LOCK" systemd-run --user --collect --wait --pipe --unit="fmhc-physics-qg1-rauch-$HHMM" \
  -p CPUQuota=100% -p MemoryMax=4G -p RuntimeMaxSec=300 \
  -E CUDA_VISIBLE_DEVICES="$GPU" -E PYTHONDONTWRITEBYTECODE=1 \
  "$PY" "$Q/qg1.py" --T 40 --out "$Q/rauchtest"
RC1=$?
echo "rauchtest rc=$RC1 $(date --iso-8601=seconds)"
if [ "$RC1" = 0 ]; then
  flock -w 45 "$LOCK" systemd-run --user --collect --wait --pipe --unit="fmhc-physics-qg1-haupt-$HHMM" \
    -p CPUQuota=100% -p MemoryMax=4G -p RuntimeMaxSec=600 \
    -E CUDA_VISIBLE_DEVICES="$GPU" -E PYTHONDONTWRITEBYTECODE=1 \
    "$PY" "$Q/qg1.py" --out "$Q/ausgabe"
  echo "hauptlauf rc=$? $(date --iso-8601=seconds)"
fi
cd "$VS" && (nohup setsid bash hauptlauf-kette.sh "$VS/FREIGABE-VS-1-HAUPTLAUF.json" >> KETTE-NOHUP.log 2>&1 < /dev/null &)
sleep 3
echo "VS-1-Kette neu gestartet $(date --iso-8601=seconds): $(pgrep -f '[h]auptlauf-kette.sh' | tr '\n' ' ')"
