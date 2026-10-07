#!/bin/bash
# Laufzeiten aus den kleintest-Logs (lokaler Spiegel logs/): Name, Spur, Start, Ende, Service runtime, rc.
D=${1:-/home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-19/huellen-leiter-3/logs}
for f in "$D"/*.log; do
  n=$(basename "$f" .log)
  s=$(grep -m1 '^start ' "$f" | sed -e 's/^start \([^ ]*\) spur=\([^ ]*\) .*/\1 \2/')
  e=$(grep -m1 '^ende ' "$f" | sed -e 's/^ende \([^ ]*\) rc=\([0-9]*\) .*/\1 rc=\2/')
  r=$(grep -m1 'Service runtime' "$f" | sed -e 's/.*runtime: //')
  echo "$n | $s | $e | $r"
done
