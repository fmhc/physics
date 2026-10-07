# Tabelle je Tropfen aus lauf-69/zusammen_<arm>.json (nur Darstellung, keine Rechnung ausser Runden)
def r(x; n): if x == null then "-" else ((x * pow(10; n) | round) / pow(10; n) | tostring) end;
.stufen | to_entries[] | .key as $st |
  (.value.tropfen[] |
    .r6_k as $k | .wurzel as $w | .akte as $a |
    (.werte | to_entries[] |
      "| \($st) | R6-k\($k) (\($w)) | \(.key) | " +
      (if .value.Q_net == null then "\(.value.status) | | | | | | |"
       else "\(r(.value.Q_net; 1)) | \(r(.value.E_ruhe_net; 1)) | \(r(.value.E_zu_Q; 4)) (\(r(.value.E_zu_Q_familie; 4))) | \(r(.value.omega_ruhe; 4)) +- \(r(.value.u_omega; 4)) (\(r(.value.omega_familie_bei_Q; 4))) | \(r(.value.rmax_zu_ra_start; 3)) | \(.value.klasse) | \(r(.value.dQ_stern; 3)) | \(.value.status) |"
       end)
    )
  )
