#!/bin/bash
# V2 (K0') und V3 (Test): vier Ketten auf cpu, cpu2, cpu3, cpu4; je Aufruf eine kleintest-Unit (<= 600 s).
# Aufruf auf der .69 im eigenen Ordner mit nohup; jede Kette schreibt ihre Logs nach logs/.
R=/home/fmh/fmhc-physics-remote/runde19-huellen-leiter-3
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
P="$R/code/huellen_leiter3.py"
L="$R/hilfs/zeilen-126.json"
F="$R/ref/stellen-r18.json"
T="$R/aus/prof-st1/profile-info.json"
ALLE=62,72,81,69,78,88,68,76,85,65,74,83
cd "$R" || exit 1

kette_cpu() {
  bash "$K" cpu r19hl3-k0-st1 "$P" k0 1 "$R/aus/prof-st1" "$L" "$F" "$R/aus/k0/k0-st1-a.json" $ALLE haupt > "$R/logs/k0-st1-a.log" 2>&1
  bash "$K" cpu r19hl3-test-st1-a "$P" test 1 "$R/aus/prof-st1" "$L" "$F" "$T" "$R/aus/test/test-st1-a.json" 0:39.59,3:39.77,2:40.24,1:40.51 > "$R/logs/test-st1-a.log" 2>&1
  bash "$K" cpu r19hl3-k0s-st1 "$P" k0 1 "$R/aus/prof-st1" "$L" "$F" "$R/aus/k0/k0s-st1-a.json" $ALLE srechteck > "$R/logs/k0s-st1-a.log" 2>&1
  echo ende-kette > "$R/logs/kette-cpu.fertig"
}
kette_cpu2() {
  bash "$K" cpu2 r19hl3-k0-st2-a "$P" k0 2 "$R/aus/prof-st2" "$L" "$F" "$R/aus/k0/k0-st2-a.json" 62,72,81,69,78,88 haupt > "$R/logs/k0-st2-a.log" 2>&1
  bash "$K" cpu2 r19hl3-test-st2-a "$P" test 2 "$R/aus/prof-st2" "$L" "$F" "$T" "$R/aus/test/test-st2-a.json" 0:39.59,3:39.77 > "$R/logs/test-st2-a.log" 2>&1
  bash "$K" cpu2 r19hl3-test-st2-c "$P" test 2 "$R/aus/prof-st2" "$L" "$F" "$T" "$R/aus/test/test-st2-c.json" 3:41.93,0:42.00 > "$R/logs/test-st2-c.log" 2>&1
  bash "$K" cpu2 r19hl3-k0s-st2-a "$P" k0 2 "$R/aus/prof-st2" "$L" "$F" "$R/aus/k0/k0s-st2-a.json" 62,72,81,69,78,88 srechteck > "$R/logs/k0s-st2-a.log" 2>&1
  echo ende-kette > "$R/logs/kette-cpu2.fertig"
}
kette_cpu3() {
  bash "$K" cpu3 r19hl3-k0-st2-b "$P" k0 2 "$R/aus/prof-st2" "$L" "$F" "$R/aus/k0/k0-st2-b.json" 68,76,85,65,74,83 haupt > "$R/logs/k0-st2-b.log" 2>&1
  bash "$K" cpu3 r19hl3-test-st2-b "$P" test 2 "$R/aus/prof-st2" "$L" "$F" "$T" "$R/aus/test/test-st2-b.json" 2:40.24,1:40.51 > "$R/logs/test-st2-b.log" 2>&1
  bash "$K" cpu3 r19hl3-test-st2-d "$P" test 2 "$R/aus/prof-st2" "$L" "$F" "$T" "$R/aus/test/test-st2-d.json" 2:42.36,1:42.62 > "$R/logs/test-st2-d.log" 2>&1
  bash "$K" cpu3 r19hl3-k0s-st2-b "$P" k0 2 "$R/aus/prof-st2" "$L" "$F" "$R/aus/k0/k0s-st2-b.json" 68,76,85,65,74,83 srechteck > "$R/logs/k0s-st2-b.log" 2>&1
  echo ende-kette > "$R/logs/kette-cpu3.fertig"
}
kette_cpu4() {
  bash "$K" cpu4 r19hl3-test-st1-b "$P" test 1 "$R/aus/prof-st1" "$L" "$F" "$T" "$R/aus/test/test-st1-b.json" 3:41.93,0:42.00,2:42.36,1:42.62 > "$R/logs/test-st1-b.log" 2>&1
  echo ende-kette > "$R/logs/kette-cpu4.fertig"
}

kette_cpu &
kette_cpu2 &
kette_cpu3 &
kette_cpu4 &
wait
