.saetze | to_entries[] | .key as $k | .value | to_entries[] | select(.value|type=="object") |
[$k, .key, (.value.E_exc // "-"), (.value.E_aus_T // "-"), (.value.f_rad // "-"), (.value.gamma // "-"), (.value.gamma_se // "-"),
 (.value.P_tick_fit // "-"), (.value.n_ticks // "-"), (.value.dP_rel_karte // "-"), (.value.dP_rel_mode // "-"),
 (.value.bilanz_E_rel // "-"), (.value.bilanz_E_rel_nullkorr // "-"), (.value.bilanz_Q_rel // "-"), (.value.bilanz_gesamt_rel // "-"),
 (.value.f_rad_n // "-"), (.value.max_abw_rel_zu_Aref // "-")] | @tsv
