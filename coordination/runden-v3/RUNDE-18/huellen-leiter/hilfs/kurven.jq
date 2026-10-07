# Tabelle je chi-Kurve aus auswertung.json
def f(n): if . == null then "-" else (. * pow(10; n) | round / pow(10; n) | tostring) end;
"| k | Stellen | omega^2 oben .. unten | R oben .. unten | mittl. Abstand R | CV Abstand R | min/max Abstand R | Spearman (d omega^2, omega^2) | Umlauf wechselt |",
"|---|---|---|---|---|---|---|---|---|",
(.kurven[] | "| \(.k) | \(.n) | \(.w2_max|f(6)) .. \(.w2_min|f(6)) | \(.R[0]|f(2)) .. \(.R[-1]|f(2)) | \(.dR_mittel|f(3)) | \(.cv_dR|f(3)) | \(if (.dR|length) > 0 then "\(.dR|min|f(3)) / \(.dR|max|f(3))" else "-" end) | \(.spearman_dw2_w2|f(3)) | \(if .umlauf_wechselt then "ja" else "nein" end) |")
