# BILDUNG-3D (Runde 23), nur Darstellung: Familientabelle aus den Familiendateien beider Gitter.
# Aufruf: jq -r -s -f hilfs/familie.jq lauf-69/aus/fam02-*.json lauf-69/aus/fam04-*.json
def r(x; n): if x == null then "-" else ((x * pow(10; n) | round) / pow(10; n) | tostring) end;
(map(select(.dr == 0.02)) | map(.familie[])) as $a
| (map(select(.dr == 0.04)) | map(.familie[])) as $b
| "| omega^2 | Q_F | E_F/Q_F | R_rms | S0 | r_halb | Newton-Rest | Virialrest | Q_F(dr 0,04)/Q_F - 1 | E/Q(0,04) - E/Q |",
  "|---|---|---|---|---|---|---|---|---|---|",
  (($a | sort_by(.w2))[] as $e
   | ($b | map(select(((.w2 - $e.w2) | fabs) < 1e-9)) | first) as $g
   | "| \($e.w2) | \(r($e.Q_F; 2)) | \(r($e.E_durch_Q; 6)) | \(r($e.R_rms; 4)) | \(r($e.S0; 5)) | \(r($e.r_halb; 3)) | \($e.newton_rest) | \(r($e.virial_rest * 1e6; 1))e-6 | \(if $g then (r(($g.Q_F / $e.Q_F - 1) * 1e5; 2) + "e-5") else "-" end) | \(if $g then (r(($g.E_durch_Q - $e.E_durch_Q) * 1e6; 2) + "e-6") else "-" end) |")
