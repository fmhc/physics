# Anzeige (nach dem Einfrieren geschrieben, nicht Teil der Auswertung). Aufruf: jq -r -f code/tabellen.jq lauf-69/auswertung.json
def r3: . * 1000 | round / 1000;
def r1: if . == null then "-" else . * 10 | round / 10 end;
.laeufe | to_entries[] | .key as $k | .value as $m
| if ($k | startswith("var_haupt_d3")) then
    "\($k) | zu1 \($m.t_erstes_schliessen | r1) | auf P/K \($m.n_oeffnen_plan)/\($m.n_oeffnen_karte) | Umordnung \($m.umordnung) t \($m.t_umordnung | r1) max|dCD| \(if $m.max_abs_dphi_CD_zu == null then "-" else ($m.max_abs_dphi_CD_zu * 57.29578 | r1) end) Grad | Zyklus \($m.zyklus_takte_plan | r1) | Anteil zu \($m.anteil_zu_plan | r3) | th_min \($m.theta_min_grad | r1) th_ende \($m.theta_ende_grad | r1) | FP \($m.fp_lauf) (\($m.fp_fenster), \($m.fp_dauer_takte | r1) T, CD geb \(if $m.cd_anteil_gebunden == null then "-" else ($m.cd_anteil_gebunden | r3) end)) | Mittel/B \(if $m.stab_mittel == null then "-" else ([$m.stab_mittel[] / $m.B | r3] | tostring) end) | Wechsel/B \(if $m.stab_wechsel_amp == null then "-" else ([$m.stab_wechsel_amp[] / $m.B | r3] | tostring) end) | dphi Fenster (Grad) \(if $m.dphi_fenster == null then "-" else ([$m.dphi_fenster[] * 57.29578 | r1] | tostring) end)"
  elif ($k | startswith("var_haupt_d2")) then
    "\($k) | 2. Haelfte Mittel/B \([$m.zweite_haelfte.stab_mittel[] / $m.B | r3] | tostring) | Wechsel/B \([$m.zweite_haelfte.stab_wechsel_amp[] / $m.B | r3] | tostring) | r_CD \($m.zweite_haelfte.r_CD_mittel | r3) | dphi (Grad) \([$m.zweite_haelfte.dphi[] * 57.29578 | r1] | tostring)"
  else
    "\($k) | dphi Ende (Grad) \([$m.dphi_ende[] * 57.29578 | r1] | tostring) | max dtheta 200 \($m.max_dtheta_200_grad | r3) | max dtheta alle \($m.max_dtheta_alle_grad | r3) | theta0 \($m.theta0_grad | r1)"
  end
