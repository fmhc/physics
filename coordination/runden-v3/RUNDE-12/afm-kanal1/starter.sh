#!/bin/bash
# AFM-KANAL-1, einmaliger Starter (kein Dienst, kein Timer, kein Hook): startet die Aufrufe der Reihe nach ueber
# kleintest.sh, jeweils nur auf einer gerade freien CPU-Spur (cpu, cpu2, cpu3, cpu4, cpu6), damit kein Aufruf am Lock
# wartet. Danach die Auswertung. Logs mit absolutem Pfad.
set -u
D=/home/fmh/fmhc-physics-remote/runde12-afm-kanal1
L=/home/fmh/fmhc-physics-remote
cd "$D" || exit 1
JOBS=(
"fam-k0.017-h0.01|familie --kappa -0.017 --h 0.01"
"fam-k0.05-h0.01|familie --kappa -0.05 --h 0.01"
"fam-k0.10-h0.01|familie --kappa -0.10 --h 0.01"
"fam-k0.19-h0.01|familie --kappa -0.19 --h 0.01"
"fam-k0.20-h0.01|familie --kappa -0.20 --h 0.01"
"kon-h0.02|kontrollen --h 0.02"
"kon-h0.01|kontrollen --h 0.01"
"fam-k0.017-h0.02|familie --kappa -0.017 --h 0.02"
"fam-k0.05-h0.02|familie --kappa -0.05 --h 0.02"
"fam-k0.10-h0.02|familie --kappa -0.10 --h 0.02"
"fam-k0.19-h0.02|familie --kappa -0.19 --h 0.02"
"fam-k0.20-h0.02|familie --kappa -0.20 --h 0.02"
)
SPUREN=(cpu cpu2 cpu3 cpu4 cpu6)
starte() {
  local name=$1 args=$2
  while true; do
    for s in "${SPUREN[@]}"; do
      if flock -n "$L/lock-klein-$s.lock" true; then
        echo "$(date --iso-8601=seconds) starte $name auf $s"
        # shellcheck disable=SC2086
        nohup bash "$L/kleintests/kleintest.sh" "$s" "$name" afm_kanal.py $args --aus "$D/aus" --name "$name" \
          > "$D/log/$name.log" 2>&1 &
        sleep 3
        return 0
      fi
    done
    sleep 5
  done
}
for job in "${JOBS[@]}"; do
  starte "${job%%|*}" "${job#*|}"
done
wait
echo "$(date --iso-8601=seconds) alle Rechenaufrufe beendet"
starte auswertung "auswertung"
wait
echo "$(date --iso-8601=seconds) Auswertung beendet"
grep -h -E "^(ende|start)" "$D"/log/*.log
