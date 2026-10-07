#!/bin/bash
# Laufzeiten aus den kleintest-Logs: Name | Spur | Start (UTC) | Ende (UTC) | Service runtime | rc
B=/home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-19/huellen-leiter-2
for f in $B/logs/r19hl2-*.log; do
  n=$(basename $f .log)
  s=$(grep -m1 '^start' $f | sed 's/^start \([^ ]*\) spur=\([^ ]*\).*/\1 \2/')
  e=$(grep -m1 '^ende' $f | sed 's/^ende \([^ ]*\) rc=\([^ ]*\).*/\1 \2/')
  r=$(grep -m1 'Service runtime' $f | sed 's/.*Service runtime: //')
  set -- $s $e
  echo "| $n | $2 | ${1:11:8} | ${3:11:8} | $r | $4 |"
done
