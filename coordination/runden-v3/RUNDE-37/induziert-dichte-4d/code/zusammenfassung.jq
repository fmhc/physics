# Kompakte Uebersicht aus lauf-69/auswertung.json (nur Lesen; Aufruf: jq -r -f zusammenfassung.jq auswertung.json)
def r6: if type == "number" then (. * 1000000 | round / 1000000) else . end;
def ms: "\(.[0] | r6) +- \(.[1] | r6) (\(.[2]))";
"TOR: urteil \(.tor.bestanden_urteil), karte \(.tor.bestanden_karte)",
(.tor | to_entries[] | select(.key | startswith("N")) | "\(.key): saaten \(.value.saaten), ausgeschlossen \(.value.ausgeschlossen | length) (\(.value.anteil_ausgeschlossen | r6)), lauf_ok \(.value.lauf_ok), neue_simplizes \(.value.neue_simplizes_mittel | r6), ersetzt_bild \(.value.ersetzt_anteil_mittel_bild | r6) (max \(.value.ersetzt_anteil_max_bild | r6)), ersetzt_fest \(.value.ersetzt_anteil_mittel_fest | r6), marge_min \(.value.saum_marge_min | r6), qhull_faktor \(.value.qhull_faktor_mittel | r6)"),
"",
(.analyse | to_entries[] | "\(.key): c \(.value.c | ms), a \(.value.a | ms), a_korr \(.value.a_korr | ms), dy \(.value.dy_global | r6), c_std \(.value.c_std_je_saat | r6), c0 \(.value.c_ohne_achsenabschnitt | ms)\n   y_je_n \([.value.y_je_n[] | "\(.mittel | r6) +- \(.se | r6)"] | join(" ; ")), y_std \([.value.y_std_je_n[] | r6] | join(" ; ")), c_je_n_direkt \([.value.c_je_n_direkt[] | "\(.mittel | r6) +- \(.se | r6)"] | join(" ; "))" + (if .value.c_je_n_nach_abzug_global then ", c_je_n_nach_abzug \([.value.c_je_n_nach_abzug_global[] | "\(.mittel | r6) +- \(.se | r6)"] | join(" ; "))" else "" end)),
"",
(.urteile | to_entries[] | "\(.key): \(.value.urteil)  \(.value.werte | tostring)")
