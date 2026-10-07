#!/bin/bash
# Laufzeiten aus den Kleintest-Logs (Start, Ende UTC, Service runtime, rc)
cd /home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-19/huellen-dipol/aus/logs
for f in r19-*.log; do
  s=$(grep -m1 '^start ' $f | sed -E 's/^start ([^ ]+).*/\1/' | cut -c12-19)
  e=$(grep -m1 '^ende ' $f | sed -E 's/^ende ([^ ]+) rc=([0-9]+).*/\1 rc=\2/' | cut -c12-)
  r=$(grep -m1 'Service runtime' $f | sed -E 's/.*runtime: //')
  echo "| ${f%.log} | $s | $e | $r |"
done
