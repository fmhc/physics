# KUGEL-GEGENLESEN: Frischer Leser fuer INDUZIERT-KUGEL-1 (Einsteins Vorzeichen auf dem S^4-Netz?) (Runde 40)

- Leitung claude-primary. Auftrag geschrieben, date direkt danach: 2026-10-04 11:49:09 CEST.
- **Anlass:** INDUZIERT-KUGEL-1 (RUNDE-37/induziert-kugel-1/ERGEBNIS.md, lauf-69/auswertung.json) findet auf einem exakt
  kovarianten S^4-Zufallsnetz beta(Regel S) = -1,651 +- 0,052 (40 Saaten), also B < 0 und ein positives induziertes G
  (Einsteins Vorzeichen), das Gegenteil des Torus-Befunds (INDUZIERT-DICHTE-4D, c = +0,111 +- 0,045). 2D-Kontrolle
  beta_2D = +0,020 +- 0,029. Die Volumenkonvention ist so gross wie das Signal (+1,70 sqrt N bei Regel C, -0,48 sqrt N bei
  Regel S); ohne Umrechnung wird eine von acht Kombinationen positiv (Gamma_M mit Sehnen, +0,16).
- Das ist ein Kehrbefund fuer Finns Weiche (Ue1 in 4D). Bevor die Leitung ihn Finn als tragend meldet, braucht er einen
  frischen Leser.

## Fragen

1. **Identifikation:** Misst beta wirklich B (Gamma enthaelt B Int sqrt(g) R, Int sqrt(g) R = 61,6 sqrt N auf S^4 bei
   Dichte 1)? Welche anderen Glieder wachsen auf S^4 wie sqrt N (Kosmologieglied mal O(h^2)-Volumenfehler,
   Diskretisierung der Kruemmung im Polytop, aeussere Kruemmung der Einbettung bei Regel C, Rand- oder
   Endlichkeitseffekte)? Ist die Trennung im Lauf sauber?
2. **Volumenkonvention:** Ist die volumen-umgerechnete Fassung unter "Zahl = Volumen" die begruendete? Stimmen die
   Korrekturformeln (je Regel mit eigenem Volumen; fuer Gamma_M mit umgekehrtem Vorzeichen)? Welche Lesart haengt am
   Vorzeichen, welche nicht?
3. **Schreibtischfehler der Karte:** Der Agent fand den Faktor 0,9168 des Torus-Schemas (Zielwert KU2 11,19 c statt
   10,26 c). Richtig?
4. **2D-Kontrolle:** Taugt beta_2D = 0 als Kontrolle fuer 4D-Artefakte, oder prueft sie nur die Konstruktion?
5. **Statistik:** 40 Saaten in 4D, N = 1000 bis 8000, Fitguete p = 0,29, Konstanz von Delta Gamma/sqrt N; tragen die
   SE?
6. **Lesart:** "Das Torus-Vorzeichen kam aus nicht kovarianten Anteilen" [H]: gedeckt? Ist das Torus-c ueberhaupt mit
   beta vergleichbar?
7. **Rueckwaerts:** Vorbehalte und Selbstanzeigen des Agenten (Auswerteskript waehrend der Rauchlaeufe entstanden;
   Festlegung auf die umgerechnete Fassung; Lesung "2 SE" in KU2): aendert einer das Urteil?
8. **Folgetest:** Welcher kleine Test (<= 10 min je Lauf) trennt am schaerfsten, ob beta das innere R misst? Vorschlag
   der Leitung zum Pruefen: ein gestauchtes S^4 (Ellipsoid in R^5), auf dem Int sqrt(g) R bei festem Volumen anders ist
   und aeussere Kruemmung sich anders verhaelt.

## Abgabe

- RUNDE-37/kugel-gegenlesen/GEGENLESEN.md: Ergebnis zuerst (traegt / traegt mit Einschraenkung / traegt nicht); je
  Frage ein Urteil mit Fundstelle; Befunde A/B/C mit Vorschlag im Wortlaut; Folgetest mit Ableitbarkeitsprobe;
  "Einfach gesagt".

## Rahmen

- pruefer-opus, Zeitbox 45 min. Schreibtisch; keine neuen Laeufe; lokal kein python, awk oder perl (jq, grep, sed zum
  Lesen erlaubt).
- Versiegeltes nie oeffnen (Dateien mit VERSIEGELT im Namen, coordination/vertraege-20260925/, KS-1-Ergebnisse,
  T8-SOLL-*, ks-1-dk-lauf/, ks-1-dk-laeufe/); keine Geheimnisdateien.
- Nur in RUNDE-37/kugel-gegenlesen/ schreiben; nicht in /tmp/claude-1000/. Zeiten nur per date.
