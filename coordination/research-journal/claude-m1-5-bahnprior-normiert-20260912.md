# M1.5: Bahnprior-Test mit paarweiser Normierung, Ausgang A bestätigt; Richtung korrigiert

- Zeit: 2026-09-12 00:57–01:42 UTC (Lauf c, 2717 s), Auswertung 05:00
- Quelle: claude-primary, TS440 run claude-m1-bahnprior-20260912-c; coordination/m1-bahnprior-20260912.md (Abschnitt M1.5); Verdichtung M1-BAHNPRIOR-kurz-v2.json
- Ergebnis: Mit korrekt normierten Gewichten w_i/Z(s_i) (Veto codex-jury-a R6) bleibt alles bei M1.4: größte Anhebung α = 2 mit +0,028 (0,29 SD, 12 % der Lücke), Saad-Ting-Form senkt auf 0,987; Kontrolle exakt (200/200), mittleres Gewicht 0,990–1,003. Sampler (90 Kataloge) bestätigt −0,077/+0,032, seine Öpik-Kontrolle verfehlt die vorab gesetzte Grenze knapp (0,0181 gegen 0,0181), Kriterium war zu eng (Archivstreuung fehlte); technical_passed false, V1 trägt. Richtung: Spearman(a, x) = +0,29, großes a = hohes x; meine und Qwens Erklärung waren falsch, korrigiert.
- Bedeutung: M1 ist innerhalb der Öpik-Knick- und e^α-Familie priorrobust; der stärkste Kandidat aus Saad & Ting trägt nicht. M1.5 im Laufregister (M1.4 ersetzt), Hauptregister-Nachtrag. Runde 7 wartet auf Marken-Freigabe.
