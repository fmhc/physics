# RUNDE-33 r33-messung: Kurzbericht OHNE Lagen aus MESSUNG-R33-VERSIEGELT.json (nach dem Einfrieren geschrieben, nur
# Darstellung). Gibt Status, Klassen, Kriterienzaehlung und Umlauffolge aus, keine omega^2-, eps-, z- oder Fensterwerte.
{
  gesamtstatus,
  n_gemessen,
  ziele_status,
  ziele_klasse: [.fortsetzungen[] | select(.k == -10 or .k == -18 or .k == -25) | {k, status, klasse}],
  klassen: ([.fortsetzungen[] | select(.status == "OK") | .klasse] | group_by(.) | map({(.[0]): length}) | add),
  lage_aus: ([.fortsetzungen[] | select(.status == "OK") | .lage_aus] | group_by(.) | map({(.[0]): length}) | add),
  unresolved_erste: [.fortsetzungen[] | select(.status != "OK") | {k, grund}] | .[0:2],
  umlauf_folge: [.fortsetzungen[] | select(.status == "OK") | .umlauf],
  phase_aufgeloest_und_gleich: ([.fortsetzungen[] | select(.status == "OK") | .kriterien.phase_aufgeloest_und_gleich
                                 | tostring] | group_by(.) | map({(.[0]): length}) | add),
  max_sprung_rad_max: ([.fortsetzungen[] | select(.status == "OK") | .rechteck_max_sprung] | max),
  n_zeilen_erweitert_min: ([.fortsetzungen[] | select(.status == "OK") | .kriterien.n_zeilen_erweitert] | min),
  n_wechsel_erweitert: ([.fortsetzungen[] | select(.status == "OK") | .kriterien.n_wechsel_erweitert | tostring]
                        | group_by(.) | map({(.[0]): length}) | add),
  n_L1_nullstellen_max: ([.fortsetzungen[] | select(.status == "OK") | .kriterien.n_L1_nullstellen_max] | max),
  beinahe_nullstellen: ([.fortsetzungen[] | select(.status == "OK") | .kriterien.beinahe_nullstellen | length] | add),
  randprobe_gerechnet: ([.fortsetzungen[] | select(.status == "OK") | has("randprobe_minus_h004_omega2")
                         | tostring] | group_by(.) | map({(.[0]): length}) | add),
  randzeilen_doppelt: {n: (.randzeilen_doppelt | length),
                       alle_gleiches_vorzeichen: ([.randzeilen_doppelt[].s_gleiches_vorzeichen] | all)},
  abtastung_n_z: .abtastung.n_z,
  harte_verletzt_irgendwo: ([.fortsetzungen[] | .harte_kriterien_verletzt // [] | .[]] | unique)
}
