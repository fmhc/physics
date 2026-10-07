# KRUEMMUNGS-SANDHAUFEN-2D-2: Organisiert Finns Kruemmungs-Regel eine geschlossene Flaeche von selbst in einen kritischen Zustand? (Runde 49, Fast Lane nach KRUEMMUNGS-SANDHAUFEN-2D-1)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 12:03:38 CEST (date), vor jeder Rechnung.
- **Herkunft [P]:** KRUEMMUNGS-SANDHAUFEN-2D-1 (RUNDE-37/kruemmungs-sandhaufen-2d-1/ERGEBNIS.md):
  - Auf der offenen Scheibe keine Lawinen ueber 2 Dekaden (Abschneiden 46).
  - Auf der geschlossenen Kugel (ohne Senke) die breiteren Lawinen: s_c2 = 358 / 830 / 989 bei wachsendem N, tau 1,29 bis 1,34, alle Lawinen enden.
  - Endzustand je ~1/3 Ecken vom Grad 5, 6, 7; grobe Verzweigungszahl 1,01 (Nachtrag nach Sicht).
  - Potenzgesetz nur knapp verfehlt (Fitguete 0,167 > 0,15).
  - Antriebsrate ist ein versteckter Parameter (r = 0,1: s_c2 x 3,9).
  - Deterministischer Arm unbrauchbar (Zyklen).
  - Finns Idee: "Was ist wenn Krümmung zu Spannung wird und umgekehrt?" bzw. "Self organized criticality und so".
- Kennzeichen: [M], [E], [P], [H].

## Ableitbarkeitsprobe (Leitung)

- **Vorab ableitbar [M]:**
  - Summe q_v = 12 auf der Kugel, mittlerer Grad 6 - 12/N.
  - Ein Kristall (fast alle Ecken vom Grad 6, 12 Fuenfer) hat kleine Ladungsvarianz. Je ~1/3 der Grade 5, 6, 7 heisst Varianz der Ladung ~2/3, also ein ungeordneter Zustand.
- **Nicht ableitbar:**
  - Skalierung des Abschneidens mit N auf der Kugel
  - ob es einen Grenzwert fuer r -> 0 gibt
  - ob die Gradverteilung von N abhaengt
  - ob P(s) bei grossem N ein Potenzgesetz ueber 2 Dekaden zeigt
- **Kennzahlen-Abgleich:** Code und Netze aus KRUEMMUNGS-SANDHAUFEN-2D-1, keine neue Bauweise.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| KS0 | Kontrolle [P]: Mit denselben Einstellungen gibt die Kugel bei N = 2000 das s_c2 aus KRUEMMUNGS-SANDHAUFEN-2D-1 auf 15 % wieder | 85 % |
| KS1 | [H] Auf der Kugel waechst s_c2 bei r = 0,01 mit N wie N^D, D >= 0,3 (N = 2000, 8000 und das groesste in 10 min machbare N, mindestens 16000) | 50 % |
| KS2 | [H] Bei N = 8000 aendert sich s_c2 zwischen r = 0,003 und r = 0,01 um weniger als den Faktor 1,5 (Grenzwert fuer kleine Rate) | 50 % |
| KS3 | [H] Im stationaeren Zustand liegt der Anteil der Grade 5, 6 und 7 auf der Kugel je zwischen 0,25 und 0,40, fuer alle gerechneten N | 60 % |
| KS4 | [H] Beim groessten N folgt P(s) auf der Kugel ueber mindestens 2 Dekaden einem Potenzgesetz (Fitguete <= 0,15 und Potenzgesetz vor gestreckter Exponentialfunktion um dAIC > 10) | 35 % |

**Bedeutung (vorab):**
- **KS1, KS2 und KS4 treffen ein:** Finns Umverteilungsregel bringt eine geschlossene Flaeche ohne Senke von selbst in einen kritischen Zustand. Das waere Selbstorganisation ohne Rand und, nach Recherchestand (KRUEMMUNG-SPANNUNG-SPIN-L, KS5), neu [H]. Dann folgt die 3D-Fassung (SOC-UMKLAPP-1).
- **KS1 verfehlt:** Die breiten Lawinen waren ein Effekt endlicher Groesse.
- **KS2 verfehlt:** Der Zustand haengt an der Antriebsrate, also an einer versteckten Abstimmung (SOC-RAUM-L-Kriterium).
- **Nur 2D und nur Kombinatorik:** keine Folge fuer Lambda oder Schwerewellen.

## Rahmen

- Code-Agent. Code aus RUNDE-37/kruemmungs-sandhaufen-2d-1/code kopieren, dort nichts aendern. Nur der zufaellige Arm.
- Auswerteregeln (Potenzgesetz, s_c2, Fitguete, dAIC, Einschwingzeit) woertlich aus dem dortigen eingefrorenen Plan, dazu die Drift-Probe aus dessen Nachtrag (Altersfenster) als Pflicht.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu und cpu7. Je Lauf hoechstens 10 min. Zeitbox 120 min.
- Plan und Code vor den Hauptlaeufen einfrieren (sha256).
- Synthetisch, keine Messdatenbestaetigung.
