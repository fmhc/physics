# Leseauszug aus aus/urteile.json (aus2); vor der ersten Sicht angelegt, nur Formatierung, keine Auswerteregel.
# Aufruf: jq -r -f jq/tabelle.jq aus-69/urteile.json
def r(x; n): if x == null then "-" else ((x * pow(10; n) | round) / pow(10; n) | tostring) end;
def ki(a; n): if a == null then "-" else "[" + r(a[0]; n) + "; " + r(a[1]; n) + "]" end;
"## Faelle",
"| Fall | Schritte | Lawinen s>=1 | Anteil s=0 | <s> | s_max | Abbruch | tau M1 [95 %] | s_c M1 | s_c2 [95 %] | dAIC M2-M1 | dAIC M3-M1 | (c) max. Abw. (Bins) | n(s>=200) | P2D (verletzt) | Drift z | Einschw. | Alter Ende | Zusatzantriebe |",
"|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|",
(.faelle | to_entries[] | .key as $k | .value |
 "| " + $k + " | " + ((.schritte // "-")|tostring) + " | " + ((.lawinen_s_ge_1 // "-")|tostring) + " | " + r(.anteil_s0; 3)
 + " | " + r(.s_mittel; 2) + " | " + ((.s_max // "-")|tostring) + " | " + r(.abbruchanteil; 5)
 + " | " + r(.m1.tau; 3) + " " + ki(.m1.tau_ki95; 3) + " | " + r(.m1.sc; 1) + " | " + r(.sc2; 1) + " " + ki(.sc2_ki95; 1)
 + " | " + r(.p2d.kriterien.a_aic_m2_minus_m1; 0) + " | " + r(.p2d.kriterien.a_aic_m3_minus_m1; 0)
 + " | " + r(.p2d.kriterien.c_max_abw_log10; 3) + " (" + ((.p2d.kriterien.c_n_bins // "-")|tostring) + ")"
 + " | " + ((.p2d.kriterien.d_n_ueber_100smin // "-")|tostring) + " | " + (.p2d.urteil // "-") + " (" + ((.p2d.gruende // [])|join("")) + ")"
 + " | " + r(.stationaritaet.z; 2)
 + " | " + ((.einschwingen.schritte // "-")|tostring) + (if .einschwingen.zeitbegrenzt then " (zeitbegr.)" else "" end)
 + " | " + r(.alter_ende; 2) + " | " + ((.zaehler.extra_antrieb // "-")|tostring) + " |"),
"",
"## Urteile",
(.urteile | to_entries[] | "- " + .key + ": Plan = " + .value.plan + "; Wortlaut = " + .value.wortlaut
   + (if .value.urteile_haupt_W1_W2 then " (Haupt/W1/W2: " + (.value.urteile_haupt_W1_W2|join(" / ")) + ")" else "" end)),
"",
"## KS0",
(.urteile.KS0 | "s_c2 neu = " + r(.sc2_neu; 1) + " " + ki(.sc2_neu_ki95; 1) + ", 2D-1 = " + r(.sc2_2d1; 1) + ", Q = " + r(.quotient; 4)),
(.faelle["ref-2d1-N2000"] | "Referenz neu berechnet: " + r(.sc2; 4) + ", gleich veroeffentlicht: " + (.gleich_veroeffentlicht|tostring)),
"",
"## KS1 D je Schaetzer",
(.urteile.KS1.D | to_entries[] | "- " + .key + ": s_c2 = " + ((.value.sc2 // []) | map(r(.; 1)) | join(" / ")) + "; D = " + r(.value.D; 3) + " " + ki(.value.D_ki95; 3) + ", 68 %: " + ki(.value.D_ki68; 3) + ", monoton " + ((.value.monoton // "-")|tostring) + (if .value.D_m1 then ", D(M1) = " + r(.value.D_m1; 3) else "" end)),
(.urteile.KS1.fenster | to_entries[] | "- Fenster " + .key + " Alter " + ((.value.alter // []) | map(r(.; 2)) | join(" bis ")) + ": " + (.value.faelle | map("N=" + (.N|tostring) + " s_c2 " + r(.sc2; 1) + " " + ki(.ki95; 1) + " (" + (.lawinen|tostring) + " Lawinen)") | join("; "))),
"",
"## KS2 Quotient r 0,01 / 0,003 bei N = 8000",
(.urteile.KS2.schaetzer // {} | to_entries[] | "- " + .key + " (Alter " + ((.value.alter // ["ganz"]) | map(if type == "number" then r(.; 2) else . end) | join(" bis ")) + "): s_c2(0,01) = " + r(.value["sc2_r0.01"].sc2; 1) + " " + ki(.value["sc2_r0.01"].ki95; 1) + ", s_c2(0,003) = " + r(.value["sc2_r0.003"].sc2; 1) + " " + ki(.value["sc2_r0.003"].ki95; 1) + ", Q = " + r(.value.quotient; 3) + " " + ki(.value.ki95; 3) + " -> " + .value.urteil),
"",
"## KS3 Gradanteile (ganz | zweite Haelfte)",
"| Fall | rho4 | rho5 | rho6 | rho7 | rho8 | Rest | 2rho5+rho7 | rho5+2rho7 | rho5/6/7 zweite Haelfte | Zeilen | Urteil Fall |",
"|---|---|---|---|---|---|---|---|---|---|---|---|",
(.urteile.KS3.faelle | to_entries[] | "| " + .key + " | " + r(.value.ganz.rho4; 4) + " | " + r(.value.ganz.rho5; 4) + " | " + r(.value.ganz.rho6; 4) + " | " + r(.value.ganz.rho7; 4) + " | " + r(.value.ganz.rho8; 4) + " | " + r(.value.ganz.rho_rest; 4) + " | " + r(.value.ganz.verzweigung_plus; 3) + " | " + r(.value.ganz.verzweigung_minus; 3) + " | " + r(.value.zweite_haelfte.rho5; 4) + " / " + r(.value.zweite_haelfte.rho6; 4) + " / " + r(.value.zweite_haelfte.rho7; 4) + " | " + (.value.zeilen|tostring) + " | " + .value.urteil_fall + " |"),
"",
"## KS4",
(.urteile.KS4 | "N = " + ((.N // "-")|tostring) + "; ganz: " + (.p2d_ganz.urteil // "-") + " (" + ((.p2d_ganz.gruende // [])|join("")) + "), tau " + r(.tau_ganz; 3) + ", s_c " + r(.sc_ganz; 1) + ", (c) " + r(.p2d_ganz.kriterien.c_max_abw_log10; 3) + ", dAIC M3-M1 " + r(.p2d_ganz.kriterien.a_aic_m3_minus_m1; 1) + ", dAIC M2-M1 " + r(.p2d_ganz.kriterien.a_aic_m2_minus_m1; 1) + "; zweite Haelfte: " + (.p2d_zweite_haelfte.urteil // "-") + " (" + ((.p2d_zweite_haelfte.gruende // [])|join("")) + "), tau " + r(.tau_zweite; 3) + ", s_c " + r(.sc_zweite; 1) + ", (c) " + r(.p2d_zweite_haelfte.kriterien.c_max_abw_log10; 3) + ", dAIC M3-M1 " + r(.p2d_zweite_haelfte.kriterien.a_aic_m3_minus_m1; 1)),
"",
"## Drift: Viertel je Fall (s_c2 | <s> | Alter Ende)",
(.faelle | to_entries[] | select(.value.viertel) | "- " + .key + ": s_c2 " + (.value.viertel.sc2_viertel | map(r(.; 1)) | join(" / ")) + "; <s> " + (.value.viertel.s_mittel_viertel | map(r(.; 2)) | join(" / ")) + "; Alter " + (.value.viertel.alter_viertel_ende | map(r(.; 1)) | join(" / "))),
"",
"## K-ID",
(.k_id // {} | tostring)
