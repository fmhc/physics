# Gauntlet v2, Runde 6: M1.4 mit berechtigtem PATCH (Paarnormierung), Kalibrierung ok

- Zeit: 2026-09-12 02:50–03:30
- Quelle: rounds/006/patches.md (10 Urteile, 3 Richter gpt-6-astra effort high), coordination/m14-bahnprior-bunker-20260912.md (Qwen-Gegenlesung mit Prüfvermerk)
- Ergebnis: Kalibrierung bestanden (K1 3×FAIL mit korrekter Algebra: 2π kürzt sich, a0 = cH0/2π ist keine Unruh-Folgerung). M1.4 FAIL von codex-jury-a (D3/D4): Importance-Gewicht w = p(a)·a ohne paarweise Normierung Z(s_i) gewichtet Paare statt Bahnen um; oberhalb des Knicks ∝ s_i^(1−β). Einwand geprüft und richtig. Qwen-Gegenlesung hatte ihn übersehen (Prüfvermerk). 0 hoch, 0 runter.
- Bedeutung: M1.4-Zahlen (+0,028; 0,988) hinfällig. Korrigierter Lauf claude-m1-bahnprior-20260912-c gestartet: V1 normierte Gewichte (200 Kataloge, Z per MC K=4096), V2 bedingter Sampler je Paar (100 Kataloge, 16 Vorschläge), plus Richtungsdiagnose. Danach M1.5. Marken heute nach Runde 6: 1.726.339 (Grenze 2 Mio; nächste Runde erst nach Nutzerwort oder Tageswechsel).
