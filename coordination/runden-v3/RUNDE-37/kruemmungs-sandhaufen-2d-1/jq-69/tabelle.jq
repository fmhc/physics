# Leseauszug aus aus-69/urteile.json; vor der ersten Sicht angelegt, nur Formatierung, keine Auswerteregel.
# Aufruf: jq -r -f jq-69/tabelle.jq aus-69/urteile.json
def r(x; n): if x == null then "-" else ((x * pow(10; n) | round) / pow(10; n) | tostring) end;
def ki(a; n): if a == null then "-" else "[" + r(a[0]; n) + ", " + r(a[1]; n) + "]" end;
"| Fall | Schritte | Lawinen s>=1 | Anteil s=0 | <s> | s_max | Abbruch | blockiert | tau (M1) [95 %] | s_c (M1) | s_c2 [95 %] | dAIC M2 | dAIC M3 | beta (M3) | (c) max abw | Bins | n(s>=200) | P2D | Gruende | Einschw. | z Drift |",
"|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|",
(.faelle | to_entries[] | .value |
 "| " + .name + " | " + (.schritte|tostring) + " | " + (.lawinen_s_ge_1|tostring) + " | " + r(.anteil_s0; 3)
 + " | " + r(.s_mittel; 2) + " | " + (.s_max|tostring) + " | " + r(.abbruchanteil; 5)
 + " | " + r(.anteil_status["1"]; 4) + " | " + r(.m1.tau; 3) + " " + ki(.m1.tau_ki95; 3)
 + " | " + r(.m1.sc; 1) + " | " + r(.sc2; 2) + " " + ki(.sc2_ki95; 2)
 + " | " + r(.p2d.kriterien.a_aic_m2_minus_m1; 1) + " | " + r(.p2d.kriterien.a_aic_m3_minus_m1; 1)
 + " | " + r(.m3.beta; 3) + " | " + r(.p2d.kriterien.c_max_abw_log10; 3) + " | " + ((.p2d.kriterien.c_n_bins // "-")|tostring)
 + " | " + ((.p2d.kriterien.d_n_ueber_100smin // "-")|tostring) + " | " + .p2d.urteil + " | " + (.p2d.gruende|join(""))
 + " | " + ((.einschwingen.schritte // "-")|tostring) + (if .einschwingen.zeitbegrenzt then " (zeitbegr.)" else "" end)
 + " | " + r(.stationaritaet.z; 2) + " |")
