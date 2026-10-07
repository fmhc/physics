# M1.4: Bahnprior-Test, Ausgang A (Überschuss priorrobust)

- Zeit: 2026-09-12 00:43–00:49 UTC (Lauf), Auswertung 03:20
- Quelle: claude-primary, TS440 run claude-m1-bahnprior-20260912-a; coordination/m1-bahnprior-20260912.md; Verdichtung coordination/claude-m1-bahnprior-20260912/M1-BAHNPRIOR-kurz.json
- Ergebnis: Kontrolle exakt (200/200 Archivziehungen auf 0,0; Mittel 1,0693010762019923). Keine Variante der Prior-Familie (Öpik-Knick bei 2/5 kAU mit a^-1,6 und a^-2; e mit α = 0,5, 1,3, 2; Kombination) bewegt das Modell-Γ um mehr als 0,29 Katalog-SD auf 1,30 zu; größte Anhebung α = 2: +0,028 (12 % der Lücke). Saad-Ting-Form (Knick 5 kAU, a^-1,6) senkt Γ auf 0,988 und vergrößert die Lücke. Mediane De-Projektions-Halbachse im schwächsten Bin 37.599 AU, im Referenzbin 1.515 AU.
- Bedeutung: Der stärkste rechenbare Kandidat aus dem Saad-Ting-Abgleich trägt nicht; M1 ist innerhalb dieser Familie priorrobust. Grenzen: Importance-Gewichtung (n_eff 207–262 von 267), keine massen- oder binabhängigen Priors. Neue Registerversion M1.4, Gauntlet-Runde 6 wird eingefroren.
