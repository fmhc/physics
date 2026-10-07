# SPLITTER-FREI-1: Kommen die wachsenden Moden auf Glas von fast flachen Splitter-Tetraedern? (Runde 48, nach Finns Heilbronn-Link)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 11:19:33 CEST (date), vor jeder Rechnung.
- **Herkunft:**
  - Finn, 05.10.2026, Heilbronn-Link ("hilft die uns irgendwie weiter im Ansatz?"). Leitung: Die lokale Fassung von Heilbronn ist das Splitter-Problem der Netzerzeugung.
  - **Projektbefunde [P]:**
    - HODGE-MASSE-1, Tabelle 4.2 (Glas N = 128, Saaten 1 bis 4):
      - A1RH 9 bis 10 und A2RH 5 bis 7 wachsende Moden; auf V, S, A15 regulaer.
      - A2LRH 46 bis 50 (Kristalle je 1).
      - A2LR2 nur auf s2 (1).
    - LUND-REGGE-MASSE-1: Lund-Regge-Masse mit R1 hat auf Glas an jedem k 27 bis 33 wachsende Moden, auch bei kl = 0,005. Die Kristalle wachsen erst ab kl ~ 0,9. Die wachsenden Richtungen liegen knapp am Nullkegel der lambda = 1-Form.
    - Glas hat Splitter bis vol_min/Mittel 0,007 (HODGE-MASSE-1). GLAS-STRAHLUNG-1: P1-Gewichte bis 838 durch Splitter; umkreisbasiert ~1 +- 0,5.
    - INDUZIERT-KUGEL-2: 3 bis 9 % Splitter machten eine Regel unbaubar ("braucht ein splitterfreies Netz").
  - Berichtigung des frischen Lesers zu GRUNDGLEICHUNG-SKIZZE-v2 (A2): Nicht "alle Paarungen ausser A1R1 und A2R1" wachsen auf Glas. Die Zielmenge dieser Karte ist deshalb ausdruecklich A1RH, A2RH, A2LR1 und A2LRH.
- Kennzeichen: [M], [E], [P], [S], [L], [H].

## Ableitbarkeitsprobe (Leitung)

- **Vorab ableitbar [M]:**
  - Ein Splitter hat fast kein Volumen. Bei Masse ~ Volumen (A2, Lund-Regge) wird seine Masse sehr klein, die Traegheit gross. Steife Moden sind damit zu erwarten.
  - Ob Moden **wachsen** (negative Richtungen der reduzierten Steifigkeit bzw. indefinite Masse unter der Reduktion), folgt daraus nicht.
  - Bei Delaunay ist der umkreisbasierte Dualraum das Voronoi-Diagramm. Die umkreisbasierten Gewichte sind deshalb nicht negativ, auch an Splittern.
- **Nicht ableitbar:**
  - ob die wachsenden Eigenvektoren an Splittern sitzen
  - ob sie auf splitterarmem Glas verschwinden
  - ob die Richtungsabhaengigkeit auf Glas teils von Splittern kommt
- **Kennzahlen-Abgleich:** Glasnetze und Zahlen aus HODGE-MASSE-1 und LUND-REGGE-MASSE-1. Ein splitterarmes Glas gibt es im Projekt noch nicht.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| SF0 | Kontrolle [P]: Auf den Originalglaesern (N = 128, Saaten 1 bis 4) reproduziert der Code die Zahl wachsender Moden aus HODGE-MASSE-1 (A1RH, A2RH) und LUND-REGGE-MASSE-1 (Lund-Regge mit R1) je Saat exakt | 85 % |
| SF1 | [H] Auf dem Originalglas liegen bei jeder wachsenden Mode von A1RH und A2RH mindestens 50 % der Eigenvektornorm auf Kanten der 5 % Tetraeder mit der schlechtesten Form (Mass im Plan festlegen, z. B. Volumen durch Umkugelradius hoch 3) | 45 % |
| SF2 | [H] Auf splitterarmem Glas (gleiche Punktzahl, Formschranke im Plan festgelegt) haben A1RH und A2RH an allen gerechneten k keine wachsende Mode | 35 % |
| SF3 | [H] Die Lund-Regge-Masse mit R1 hat auch auf splitterarmem Glas an jedem gerechneten k mindestens 10 wachsende Moden (nicht splitterbedingt) | 55 % |
| SF4 | [H] Die TT-Spanne mit A1R1 auf splitterarmem Glas ist hoechstens halb so gross wie auf dem Originalglas (dort 10,9 bis 23,7 %) | 40 % |

**Bedeutung (vorab):**
- **SF1 und SF2 treffen ein:** Die Instabilitaet unter RH auf Glas ist ein Netzfehler (Splitter), keine Physik. Der Glas-Zweig ist fuer RH neu zu bewerten, und Finns Netz braucht eine Formregel (keine fast flachen Zellen). Das ist die lokale Heilbronn-Bedingung.
- **SF3 trifft ein:** Die Lund-Regge-Instabilitaet ist nicht splitterbedingt, sondern eine Eigenschaft der Masse mit R1.
- **SF4 trifft ein:** Ein Teil der Glas-Anisotropie kommt von Splittern; Glas-Isotropie-Zahlen (TT-GLAS-1/2) waeren dann splitterabhaengig.
- **Alles verfehlt:** Splitter erklaeren die Glas-Befunde nicht. Der Heilbronn-Gedanke bleibt dann ohne Folge fuer die Dynamik.

## Rahmen

- Code-Agent. Code aus RUNDE-37/hodge-masse-1/code, RUNDE-37/lund-regge-masse-1/code und RUNDE-37/tt-glas-2/code kopieren, dort nichts aendern.
- **Splitterarmes Glas:** Bauweise im Plan begruenden und gegen Kristallisation pruefen (z. B. Paarkorrelation bzw. Bindungsordnung).
  - Kandidaten: Punktprozess mit Mindestabstand und kurzer Relaxation; kleine Stoerung der Punkte, bis keine Zelle unter der Formschranke liegt. Delaunay bleibt die Zerlegungsregel.
- k-Satz wie in HODGE-MASSE-1 bzw. LUND-REGGE-MASSE-1; gleiche Reduktionen R1, RH.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu5 und cpu6. Je Lauf hoechstens 10 min. Zeitbox 150 min.
- Plan und Code vor den Hauptlaeufen einfrieren (sha256).
- Synthetisch, keine Messdatenbestaetigung.
