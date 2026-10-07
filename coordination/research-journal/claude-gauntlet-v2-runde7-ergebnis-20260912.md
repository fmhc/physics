# Gauntlet v2, Runde 7: zwei Text-PATCHes (M1.5, T4.3) umgesetzt; Kalibrierung ok; Marken-Grenze erreicht

- Zeit: 2026-09-12 03:45–04:25 UTC
- Quelle: rounds/007/patches.md (11 Urteile, 3 Richter gpt-6-astra effort high)
- Ergebnis: M7 3×PASS, K1 3×FAIL (Kalibrierung ok). M1.5 FAIL codex-jury-b (D4): gewichteter Median ist nicht automatisch Erwartungswert des ungewichteten Γ unter neuem Prior; Sampler ohne K-Konvergenz, Kontrolle nicht bestanden. PATCH umgesetzt: Text auf V1-Sensitivität beschränkt, Sampler als Plausibilisierung. T4.3 FAIL codex-jury-c (D3): „trennt Grenzverhalten scharf" nicht isoliert, Übergangsverlauf als Alternative; PATCH umgesetzt im Register und als Korrekturabschnitt am v2-Bericht, Zentralwerte als Bootstrap-Mittel gekennzeichnet; C1 als behoben bestätigt. Stichprobe bronze (S1.2, S2.2, M3.3) je 1 PASS. 0 hoch, 0 runter.
- Bedeutung: Beide Vetos aus R5/R6 sind durch Rechnung beantwortet; die neuen Einwände sind Reichweitenfragen der Schlussfolgerung, keine Rechenfehler. Marken heute 2.084.679 über der 2-Mio-Grenze: keine Runde 8 ohne Nutzerwort. Rechenoption M1.6 benannt.
