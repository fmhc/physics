# BILDUNG-3D (Runde 23), nur Darstellung: Tabelle je Klumpen, Gitter und Zeit aus der Gesamtauswertung.
# Aufruf: jq -r -f hilfs/tabelle.jq lauf-69/aus/gesamt.json
def r(x; n): if x == null then "-" else ((x * pow(10; n) | round) / pow(10; n) | tostring) end;
"| Reihe | dr | T | Q-Anteil | Kern r<30 | omega_mess | omega^2 | Q_Ball | Q_F(omega_mess) | Abw. | E/Q (Familie) | S0 Mittel (Familie) | Spanne rel | Atmung omega | R_rms r<30 (Familie) | Urteil |",
"|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|",
(.laeufe | sort_by(.dr))[] as $l | $l.reihen[] as $e | $e.zeiten[] as $z
| "| \($e.reihe) | \($l.dr) | \($z.T) | \(r($z.Q_Anteil; 4)) | \(r($z.Q_kern_anteil; 4)) | \(r($z.omega_mess; 6)) | \(r($z.w2_mess; 5)) | \(r($z.Q_Ball; 1)) | \(r($z.Q_F_mess; 1)) | \(if $z.abw == null then "-" else (r($z.abw * 100; 2) + " %") end) | \(r($z.E_durch_Q; 4)) (\(r($z.E_durch_Q_F_mess; 4))) | \(r($z.S_zentrum_mittel; 4)) (\(r($z.S0_F_mess; 4))) | \(r($z.Spanne_rel * 100; 2)) % | \(r($z.atmung_omega; 3)) | \(r($z.R_rms_kern; 3)) (\(r($z.R_rms_F_mess; 3))) | \($z.urteil) |"
