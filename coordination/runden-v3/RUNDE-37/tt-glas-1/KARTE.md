# TT-GLAS-1: Laufen Schwerewellen auf einem Zufalls-Tetraedernetz ("Glas") im Mittel in alle Richtungen gleich, und wie gross ist die Streuung je Netz? (Runde 45, Finns Weiche "Kristall oder Glas", Zweig Glas)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 04:16:30 CEST (date), vor jeder Rechnung.
- **Finn (05.10., gegen 04:15):** "Führe alle Themen weiter und stell mir die Fragen noch mal bzw teste herum.was richtig ist"; zur Netzart: "Teste beides".
- **Herkunft:**
  - TT-ISO-1 und TT-GRUND-1: Auf Finns regelmaessigem, gefuelltem Netz sind die TT-Zweige nur mit fein abgestimmten Tetraedermassen isotrop. Es gibt keine natuerliche Massenregel. Die Steifigkeit war schon isotrop, die Anisotropie sass in der Masse.
  - Schwerewellen auf einem Zufallsnetz sind im Projekt nicht gerechnet (GEMEINSAMES-NETZ-V3-LESER, B6).
  - Gerechnet sind dort nur elastische Federnetze (RUNDE-36/zufallsnetz-1) sowie Skalar- und Weyl-Felder (STRICH-NETZ-1, WEYL-LINEAR-1/2: Streuung je Netz ~ N^(-1/2)).
- Kennzeichen: [M], [E], [P], [S], [H].

## Ableitbarkeitsprobe (vor der Karte)

- **Projektsuche:** Regge bzw. TT auf Zufallsnetzen kommt nicht vor.
  - Codes, die wiederverwendet werden koennen: eine-welt-loch-1/code/ew.py (Hamilton-Netz mit Bewegungsenergie je Tetraeder, skalaren Regeln, Reduktion), strich-netz-1/code (periodische Poisson-Delaunay-Netze), regge-welle-1 (Regge-Hesse auf regelmaessigen Netzen).
- **Vorab ableitbar [M]:**
  - Das Ensemble-Mittel ist isotrop, weil Poisson-Punkte statistisch isotrop sind. TG2 ist nur Kontrolle.
  - Die Streuung je Netz sollte nach dem Zentralen Grenzwertsatz wie N^(-1/2) fallen, solange die Beitraege kurzreichweitig korreliert sind. TG1 ist daher nur schwach informativ.
- **Nicht ableitbar:**
  - der Vorfaktor der Streuung (TG3)
  - ob es auf Zufallsnetzen ueberhaupt genau zwei masselose TT-Moden gibt (Zaehlung)
  - ob die Moden stabil sind
  - ob nichtaffine Relaxation die Lage aendert

## Auftrag (Code-Agent)

1. **Netze:** periodische 3D-Poisson-Delaunay-Triangulierungen mit N Punkten, mehrere Saaten, N in einer Leiter (etwa 500 bis 8000).
2. **Modell:** das Hamilton-Netz aus EINE-WELT-LOCH-1 auf diese Triangulierung uebertragen, also Kantenlaengen als Lagen, Bewegungsenergie je Tetraeder (J = 1) und skalare Regeln je Ecke mit Gewicht l_e, falls moeglich.
   - Geht das in der Zeitbox nicht, gilt als Ersatz: Rayleigh-Quotient affiner TT-Wellen. Das ist Steifigkeit (Regge-Hesse) durch Masse fuer eine ebene TT-Welle mit erlaubtem k. Den Ersatz kennzeichnest du als Naeherung.
   - Die Wahl steht im Plan vor jeder Rechnung.
3. **Messgroessen:**
   - Zahl der masselosen TT-artigen Moden bei kleinem k (wenn exakt gerechnet).
   - omega^2/k^2 bzw. der Rayleigh-Quotient in mindestens 13 Richtungen und beiden TT-Polarisationen.
   - Spanne max/min - 1 je Netz.
   - Mittel und Streuung ueber Saaten, Exponent der Streuung gegen N.
4. **Kontrolle:** derselbe Code auf Finns regelmaessigem gefuelltem Netz (V, A1R1) gibt die bekannte Spanne von 6,34 % (TT-ISO-1).

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| TG-G0 | Kontrolle: Das regelmaessige Netz gibt mit demselben Code 6,34 % auf 1e-3 relativ (bzw. der Rayleigh-Quotient die TT-ISO-1-Werte) | 80 % |
| TG-G1 | [H, schwach informativ] Die Spanne je Netz faellt mit N wie N^p mit p = -0,5 +- 0,15 | 65 % |
| TG-G2 | Kontrolle [vorab ableitbar]: Das Mittel ueber Saaten ist richtungsunabhaengig innerhalb von 2 Standardfehlern | 85 % |
| TG-G3 | [H] Bei N ~ 8000 liegt die Spanne je Netz unter 1 % | 50 % |

**Bedeutung (vorab):**
- **TG-G1 und TG-G3 treffen ein:** Ein Glas-Netz wird ohne Abstimmung immer isotroper, je mehr Punkte ein Wellenzug ueberstreicht. Fuer makroskopische Wellen waere die Restanisotropie verschwindend [H]. Der Preis ist das Rauschen.
- **TG-G3 verfehlt:** Die Streuung ist gross; ein Glas braeuchte sehr viele Punkte je Wellenlaenge [H].
- **Wenn auf Zufallsnetzen nicht genau zwei masselose TT-Moden entstehen:** Das Glas-Netz traegt die Schwerewellen nicht wie das gefuellte regelmaessige Netz. Dann ist das der wichtigere Befund.

## Rahmen

- Code-Agent.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu3 und cpu4 (frei seit KOMPAKT-1).
- Je Lauf hoechstens 10 min, 1 Thread. Zeitbox 120 min.
- Ein ehrlicher Teilbericht ist besser als keiner.
