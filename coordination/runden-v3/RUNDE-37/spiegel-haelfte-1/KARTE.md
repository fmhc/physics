# SPIEGEL-HAELFTE-1: Wird die sichtbare Haelfte unseres Einbahn-Automaten doppler-frei, wenn die verborgene Haelfte ihren eigenen Takt je Knoten hat ("dark tick")? (Runde 42)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-04 17:34:35 CEST (date), vor jeder
  Rechnung.
- **Herkunft:** Kartenvorschlag aus DUNKEL-FLIP-L (RUNDE-37/dunkel-flip-l/DOSSIER.md, Abschnitt SPIEGEL-HAELFTE-1;
  ARBEITSFELD Abschnitt 9).
- **Finns Bilder (04.10.):** negative Parallelwelt (verborgene Haelfte 2'); "dark tick der pro einzelteil einzeln laeuft"
  (Taktphase je Knoten); Ausgleich (Abfluss nach 2'); Links-rechts-Spiegel (Partner entgegengesetzter Chiralitaet in 2').
  Modellintern, keine Messdaten.
- **Behauptung des Agenten [M, nicht gegengelesen]:** Das doppler-freie, nicht unitaere 3+1-Schachbrett von
  Foster/Jacobson (FJ) ist die Kompression des unitaeren Einbahn-Automaten W = C S_+ aus QCA-DIAMANT-4 auf die
  Komponente 2. Der Partner sitzt in 2' bei einer anderen Taktphase.
- **Ableitbarkeitsprobe (aus dem Dossier):**
  - Vorab ableitbar:
    - W = 0: Bloch-Analyse; Kegel auf 2 bei alpha, Partner auf 2' bei beta, kohaerente Rueckkehr.
    - schwache Unordnung: Zerfall des 2-Gewichts ~ W^2 (Born, Groessenordnung).
    - FJ-Referenz A(theta) aus der Quelle.
  - Nicht ableitbar:
    - ob das 2-Gewicht bei starker Unordnung der FJ-Kurve folgt (Senke ohne Rueckkehr) oder 2' lokalisiert und
      zurueckgibt
    - ob die Ausbreitung ballistisch bei 1/3 bleibt
    - ob Doppler-Anteile verschwinden
  - Projekt-grep: keine Karte mit Taktunordnung in der verborgenen Haelfte; SPIN-ZUFALLSNETZ-1 hatte raeumliche
    Unordnung.
- Kennzeichen: [M] Mathematik, [E] Messung im Modell, [P] Projektdatei, [S] Quelle, [H] Hypothese.

## Auftrag (Code-Agent)

1. **Teil A, Schreibtisch vor jeder Rechnung:** Die Herleitung "FJ = Kompression von W = C S_+ auf Komponente 2" pruefen,
   mit der Phasenwahl der Spinoren (DUNKEL-FLIP-L DOSSIER 6.2, ARBEITSFELD 9; FJ-Quelle in dunkel-flip-l/quellen/).
   Haelt sie nicht, Teil B nur als Beschreibung rechnen und das melden.
2. **Teil B (klein):**
   - BCC, 4 Zustaende, W = C_x S_+ mit C_x = e^{i alpha} P_2 + e^{i beta_x} P_2'.
   - beta_x je Knoten fest und zufaellig, gleichverteilt in [beta - W/2, beta + W/2]; W von 0 bis 2 pi, mehrere Saaten.
   - Start: Paket in Komponente 2 nahe k = 0.
   - Messungen:
     - Gewicht auf 2 ueber t
     - Vergleich mit der FJ-Normabnahme fuer dasselbe Paket
     - Ausbreitung des 2-Anteils gegen 1/3
     - Anteil grosser Wellenvektoren im 2-Anteil
   - Daten und Code: qca-diamant-4/lauf-69/haupt_B*.json und code/ (nur kopieren).
3. Plan, Rauchlauf, Einfrieren wie ueblich.

## Vorhersagen (vor jeder Rechnung; Vorschlag des Dossiers, Wahrscheinlichkeiten von der Leitung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| SH0 | Kontrollen: Teil-A-Herleitung haelt; W = 0 reproduziert die Bloch-Vorhersage (Kegel auf 2, Partner auf 2', kohaerente Rueckkehr) auf 1e-8 | 75 % |
| SH1 | [H] Bei W = 2 pi folgt das 2-Gewicht ueber 100 Schritte der FJ-Kurve auf 10 % | 45 % |
| SH2 | [H] Die Ausbreitung des 2-Anteils bleibt bei 1/3 +- 10 % | 60 % |

**Bedeutung (vorab):**
- **SH1 und SH2 treffen ein:** Ein eigener Takt je Knoten in der verborgenen Haelfte macht die sichtbare Haelfte zum
  doppler-freien Schachbrett. Der Spiegelpartner verschwindet in die "Negativseite", ohne das Tempo zu stoeren [H].
  Offen bleibt die Unitaritaet der sichtbaren Welt (Normverlust).
- **SH1 verfehlt:** Die verborgene Haelfte gibt zurueck (Resonator), oder der Abfluss ist anders als bei FJ.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spur cpu11 (neu). Je Lauf <= 10 min, 1 Thread. Zeitbox 150 min.
