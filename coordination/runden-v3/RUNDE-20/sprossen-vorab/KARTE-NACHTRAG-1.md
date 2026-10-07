# SPROSSEN-VORAB, Nachtrag 1 der Leitung: Offenlegung vor jedem Lauf

- Geschrieben ab 2026-10-02 17:09:55 CEST (date). Der Kartenordner enthielt dabei nur KARTE.md (kein Plan, kein Lauf, kein Ergebnis).
- Zweck: eine Vorbelastung offenlegen, die in die Karte gehoert haette.
- Die Wertungsregeln der Karte bleiben woertlich unveraendert, keine Lockerung.

## Was vor der Karte bekannt war

- In HUELLEN-LEITER-2 endete ein ungewerteter Newton-Lauf bei einer echten stillen Stelle mit **R = 40,49, rho = 1,248**.
- HUELLEN-LEITER-3 (Runde 19) stellte fest, dass diese Stelle nicht auf k = 1 liegt, sondern auf einer hoeheren Kurve.
  Welche Kurve, ist unbestimmt.
- Beides stand in RUNDE-19.md, bevor die Karte geschrieben wurde.
- In der Naehe liegen die Vorhersagen k = 5 bei 40,51 und k = 7 bei 40,65. Liegt die bekannte Stelle auf einer der Kurven
  k = 4 bis 7, ist die Vorhersage dieser Kurve nahe R = 40,5 **nicht blind**.

## Zusatz zur Wertung (gekennzeichnete Zusatzvorgabe der Leitung, vor jedem Lauf)

- **Formal:** V0 bis V3 werden genau wie in der Karte gewertet.
- **Zusaetzlich zu berichten:**
  - Faellt eine angenommene Sprosse mit der bekannten Stelle zusammen (|Delta R| <= 0,01 und |Delta rho| <= 0,005),
    wird sie als "nicht blind" markiert.
  - V2 wird dann zusaetzlich ohne diese Sprosse ausgewertet, mit "mindestens 6 von 7". Das ist eine Nebenlesart; sie
    ersetzt das formale V2 nicht.
- Die Kurvenzuordnung der bekannten Stelle folgt demselben Annahmekriterium (Stetigkeit von rho und Rang) wie alle
  Sprossen.

## Selbstanzeige der Leitung

- Die Vorbelastung haette in die Karte gehoert; ich habe sie erst bei der Pruefung der Eingangszahlen nach dem Start
  bemerkt.
- Die Eingangszahlen der Karte habe ich gegen RUNDE-18/huellen-leiter/ERGEBNIS.md geprueft; alle stimmen.
  - k = 4 bis 7: letzte Lagen 36,92 / 38,26 / 37,19 / 38,27, kleinste Abstaende 2,206 / 2,248 / 2,322 / 2,379.
  - k = 0 bis 3: Lagen aus HUELLEN-LEITER-3.
- Beide Karten der Runde 20 habe ich mit einem ungequoteten Heredoc geschrieben (nur $D eingesetzt, keine Backticks,
  keine Befehle). Das verstoesst gegen die Heredoc-Regel und war folgenlos.
