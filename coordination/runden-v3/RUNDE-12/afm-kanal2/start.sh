#!/bin/bash
# AFM-KANAL-2, einmaliger Starter (kein Dienst, kein Timer, kein Hook): startet die Aufrufe der Reihe nach ueber
# kleintest.sh, jeweils nur auf einer gerade freien CPU-Spur (cpu, cpu2, cpu3, cpu4, cpu6), danach die Auswertung.
# Logs mit absolutem Pfad.
set -u
D=/home/fmh/fmhc-physics-remote/runde12-afm-kanal2
L=/home/fmh/fmhc-physics-remote
cd "$D" || exit 1
mkdir -p "$D/aus" "$D/log"
A="0.5,0.575,0.65,0.725"
B="0.725,0.8,0.875,0.95"
JOBS=(
"kg-h0.02|familie --modell kg --h 0.02"
"kg-h0.01|familie --modell kg --h 0.01 --pole nein"
"afm-k0.20-h0.01-B|familie --modell afm --kappa -0.20 --f $B --h 0.01 --pole nein"
"afm-k0.20-h0.02-B|familie --modell afm --kappa -0.20 --f $B --h 0.02"
"afm-k0.19-h0.01-B|familie --modell afm --kappa -0.19 --f $B --h 0.01 --pole nein"
"afm-k0.19-h0.02-B|familie --modell afm --kappa -0.19 --f $B --h 0.02"
"afm-k0.10-h0.01-B|familie --modell afm --kappa -0.10 --f $B --h 0.01 --pole nein"
"afm-k0.10-h0.02-B|familie --modell afm --kappa -0.10 --f $B --h 0.02"
"afm-k0.20-h0.01-A|familie --modell afm --kappa -0.20 --f $A --h 0.01 --pole nein"
"afm-k0.20-h0.02-A|familie --modell afm --kappa -0.20 --f $A --h 0.02"
"afm-k0.19-h0.01-A|familie --modell afm --kappa -0.19 --f $A --h 0.01 --pole nein"
"afm-k0.19-h0.02-A|familie --modell afm --kappa -0.19 --f $A --h 0.02"
"afm-k0.10-h0.01-A|familie --modell afm --kappa -0.10 --f $A --h 0.01 --pole nein"
"afm-k0.10-h0.02-A|familie --modell afm --kappa -0.10 --f $A --h 0.02"
)
SPUREN=(cpu cpu2 cpu3 cpu4 cpu6)
starte() {
  local name=$1 args=$2
  while true; do
    for s in "${SPUREN[@]}"; do
      if flock -n "$L/lock-klein-$s.lock" true; then
        echo "$(date --iso-8601=seconds) starte $name auf $s"
        # shellcheck disable=SC2086
        nohup bash "$L/kleintests/kleintest.sh" "$s" "$name" afm_bic.py $args --aus "$D/aus" --name "$name" \
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
