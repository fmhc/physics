#!/bin/bash
# TT-GRUND-1, einmalige Laufliste Spur cpu10 (kein Dienst, kein Timer). Jeder Lauf ueber kleintest.sh.
# Kein neuer Lauf ab SCHLUSS = 2026-10-04 23:45:00 CEST (21:45:00 UTC).
set -u
SCHLUSS=$(date -d '2026-10-04 21:45:00 UTC' +%s)
D=/home/fmh/fmhc-physics-remote/tt-grund-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
L=$D/lauf
cd "$D/code" || exit 1
lauf() {
  local n=$1; shift
  if [ "$(date +%s)" -ge "$SCHLUSS" ]; then echo "SCHLUSS vor $n $(date -u +%FT%TZ)" >> "$L/kette-cpu10.log"; return 1; fi
  echo "start $n $(date -u +%FT%TZ)" >> "$L/kette-cpu10.log"
  bash "$K" cpu10 "tg$n" "$D/code/tg.py" "$@" > "$L/tg$n.log" 2>&1
  echo "ende $n rc=$? $(date -u +%FT%TZ)" >> "$L/kette-cpu10.log"
}
lauf PS profil --netz V --achse S --nprof 81 --nscan 161 --out "$L/profil-S-V.json"
lauf PK profil --netz V --achse K --nprof 81 --nscan 161 --out "$L/profil-K-V.json"
lauf B best --netz V --profile "$L/profil-S-V.json" "$L/profil-K-V.json" --out "$L/best-V.json"
while [ ! -f "$L/kontrolle.json" ] || [ ! -f "$L/regeln.json" ] || [ ! -f "$L/karte-V.json" ]; do
  [ "$(date +%s)" -ge "$SCHLUSS" ] && break
  sleep 10
done
lauf U urteil --kontrolle "$L/kontrolle.json" --karte "$L/karte-V.json" --profile "$L/profil-S-V.json" "$L/profil-K-V.json" --regeln "$L/regeln.json" --best "$L/best-V.json" --out "$L/urteil.json"
lauf BI bild --karte "$L/karte-V.json" --profile "$L/profil-S-V.json" "$L/profil-K-V.json" --regeln "$L/regeln.json" --best "$L/best-V.json" --png "$L/spannenkarte-V.png" --out "$L/bild.json"
echo "kette fertig $(date -u +%FT%TZ)" >> "$L/kette-cpu10.log"
