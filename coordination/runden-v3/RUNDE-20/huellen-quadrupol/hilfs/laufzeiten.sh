#!/bin/bash
# Laufzeiten-Tabelle aus aus/logs/q20-*.log (Start, Ende in UTC, Service runtime, rc)
cd /home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-20/huellen-quadrupol/aus/logs || exit 1
for f in $(ls -tr q20-*.log); do
  n=${f%.log}
  s=$(grep -m1 '^start ' $f | sed -E 's/^start [0-9-]+T([0-9:]+)\+00:00.*/\1/')
  e=$(grep -m1 '^ende ' $f | sed -E 's/^ende [0-9-]+T([0-9:]+)\+00:00 rc=([0-9]+).*/\1 rc=\2/')
  t=$(grep -m1 'Service runtime' $f | sed -E 's/.*Service runtime: //')
  echo "| $n | $s | ${e% rc=*} | $t | ${e##*rc=} |"
done
