## 5 Kontrollen

### K1 (bewiesene M1-Stelle, chi-Kopplung aus; Variante K1E1 von Code 1)

- Dieselbe Kette wie die Suche: Zeilen omega^2 = 0,78 bis 0,82 (ganze E1-Zeile, 201 Punkte), Rang, Unterzeilen,
  zwei Halbierungen, dann Newton und Rechteck aus Code 1 (unveraendert).
- In jeder Zeile genau eine Nullstelle der geschlossenen Bedingung; s an ihr wie in Runde 17 (Stufe 2: -0,0708 bei 0,78,
  -0,0271 bei 0,79, +0,0071 bei 0,80, +0,0300 bei 0,81, +0,0449 bei 0,82). Genau ein Vorzeichenwechsel, Zellen-Umlauf -1.

| Stufe | Lage aus Halbierung (omega^2 / rho) | Lage nach Newton | Abstand zur bewiesenen Stelle | Umlauf (Rechteck) | groesster Sprung | Randpunkte | sigma2/sigma1 |
|---|---|---|---|---|---|---|---|
| 1 (hp 0,01) | 0,79767681 / 1,74461753 | 0,7976767750 / 1,7446175408 | 2,3e-7 / 4,6e-7 | -1 aufgeloest | 0,170 rad | 64 | 1,2e-13 |
| 2 (hp 0,005) | 0,79767683 / 1,74461754 | 0,7976767864 / 1,7446175446 | 2,1e-7 / 4,6e-7 | -1 aufgeloest | 0,170 rad | 64 | 1,4e-13 |

- **K1 bestanden** (Kriterium 1e-4, Umlauf -1 aufgeloest, beide Stufen, Zellen-Umlauf -1). Die Newton-Lagen stimmen mit
  Runde 17 (0,797676775 / 1,744617541) auf 1e-9 ueberein.

### Hintergrund (Konvergenz vor der Suche)

- Alle 263 Zeilen auf beiden Stufen (hp 0,01 mit N bis 19 900 Gitterpunkten; hp 0,005 mit N bis 39 800):
  - |dQ/Q| <= 6,2e-11 und |dE/E| <= 6,3e-11 zwischen den Stufen; Huellenradius R auf beiden Stufen bis 3,5e-6 gleich.
  - Rand des Gebiets: |f(R_bg)|/f(0) <= 3,4e-17.
  - Kein Profil ueber der Schwelle 1e-6. **Sauber bis omega^2 = 0,74 (R = 114,2)**, also im ganzen Suchbereich.
- Lauf-Dauer: Die Fortsetzung zur Schranke wird teuer (bei R ~ 110 je Profil 11 bis 26 s, Newton-Schritte mehrfach
  halbiert). Beide Profillaeufe erreichten die 600-s-Grenze und wurden mit derselben Fortsetzung ab dem letzten
  gespeicherten Profil weitergefuehrt (Option "weiter", Selbstanzeige).
