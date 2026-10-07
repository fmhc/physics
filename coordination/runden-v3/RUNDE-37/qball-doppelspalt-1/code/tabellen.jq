# QBALL-DOPPELSPALT-1: Lesefilter fuer lauf-69/auswertung.json (nur Anzeige, keine Rechnung ausser Rundung)
def r3: if . == null then null else (. * 1000 | round / 1000) end;
.kombis | to_entries[] | select(.value.modell == "qball" and .value.nspalt == 2) |
  [.key, .value.klassen, .value.n_durch, (.value.I2_kde.r2 | r3), (.value.I2_bin5.r2 | r3), (.value.I2_ladung.r2 | r3),
   (.value.periode_kde | if . then {p: (.peaks | map(r3)), per: .periodisch, T: (.periode | r3)} else null end), .value.VQ4]
