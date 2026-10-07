#!/bin/bash
# Laufzeiten aus den kleintest-Logs: Lauf | Spur | Start | Ende | Dauer | rc
L=/home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-21/sprossen-l1l2/logs
for f in $L/*.log; do
  n=${f##*/}; n=${n%.log}
  s=$(grep -m1 '^start ' "$f" | sed 's/^start [0-9-]*T\([0-9:]*\)+.* spur=\([a-z0-9]*\) .*/\1 \2/')
  e=$(grep -m1 '^ende ' "$f" | sed 's/^ende [0-9-]*T\([0-9:]*\)+.* rc=\([0-9]*\) .*/\1 \2/')
  r=$(grep -m1 'Service runtime' "$f" | sed 's/.*runtime: //')
  echo "| $n | ${s#* } | ${s% *} | ${e% *} | $r | ${e#* } |"
done
