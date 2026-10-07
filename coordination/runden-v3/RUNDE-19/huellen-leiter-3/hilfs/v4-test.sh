#!/bin/bash
# V4b: formale Testauswertung, sobald alle sechs Testlaeufe beendet sind (Spur cpu4).
R=/home/fmh/fmhc-physics-remote/runde19-huellen-leiter-3
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd "$R" || exit 1
until [ "$(cat logs/test-st1-a.log logs/test-st1-b.log logs/test-st2-a.log logs/test-st2-b.log logs/test-st2-c.log logs/test-st2-d.log 2>/dev/null | grep -c '^ende ')" -ge 6 ]; do sleep 5; done
bash "$K" cpu4 r19hl3-ausw-test "$R/code/huellen_leiter3.py" ausw-test "$R/aus" "$R/aus/k0-auswertung.json" "$R/aus/test-auswertung.json" > "$R/logs/ausw-test.log" 2>&1
