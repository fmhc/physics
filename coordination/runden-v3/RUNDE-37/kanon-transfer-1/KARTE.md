# KANON-TRANSFER-1: Wie gross sind Energie- und Ladungsfehler des Skalars am Umklappzug mit R, P und dem kanonischen Transfer K, und wie viel des Gesamtsprungs ist ueberhaupt Skalar? (Runde 49, Codex Ideation 4 Rang 1)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 14:39:07 CEST (date), vor jeder Rechnung.
- **Herkunft [P]:**
  - Codex, Ideation 4 Rang 1 (coordination/codex-ideation-20261005/IDEATION-4-CLAUDE-ABGLEICH.txt):
    - x' = x, p' = D p ist fuer D ungleich I nicht kanonisch.
    - Ein kanonischer Vergleich x' = F(q) x verlangt p'_x = F^-T p_x und den Rueckstoss p'_q,a = p_q,a - p_x^T F^-1 (d_a F) x.
    - Erwartung: Kanonischer Transfer allein beseitigt den Energiefehler nicht.
    - Kleinsttest an gespeicherten Zuegen; Zweiform und Ladung als Kontrollen, Energiefehler und Quellenabweichung offen.
  - Grundgleichung v2.5 Abschn. 6 (RUNDE-49/GRUNDGLEICHUNG-SKIZZE-v2.5.md):
    - R: phi' = phi, pi' = D pi mit D = *0'/*0 je Ecke.
    - P: pi stetig.
    - R aendert die U(1)-Ladung.
  - UEBERGABE-KONFLUENZ-1 (RUNDE-37/uebergabe-konfluenz-1): 32 Faelle auf Glas N = 128.
    - Flaechen durch eine Hintergrundverschiebung (mu = -1e-3) nicht lokal Delaunay; Arten D, T, K.
    - Skalar masselos: H_phi = 1/2 pi^T *0^-1 pi + Z_S/2 (d0 phi)^T *1 (d0 phi), Z_S = 8; stehende Welle A = 1e-3, 1e-2.
    - Geometrie in den Lesarten R und P, Formen A1 und A2.
  - HODGE-MASSE-1 Tab. 4.4: Energiesprung je 2-3-Zug im Glas im Mittel 1e-3 bis 4e-3 relativ, hoechstens 3e-2.
- Kennzeichen: [M], [E], [P], [H], [N] (Nachtrag nach Sicht).

## Ableitbarkeitsprobe (Leitung)

- **Drei Transfers des Eckenskalars** (die Ecken bleiben bei 2-3 und 3-2) [M]:
  - R: phi' = phi, pi' = D pi.
  - P: phi' = phi, pi' = pi (F = I, kanonisch, kein Rueckstoss).
  - K: phi' = D^(-1/2) phi, pi' = D^(1/2) pi (F = D^(-1/2) je Ecke, Kotangential-Lift). Dazu der Rueckstoss
    p'_q = p_q + 1/2 Summe_v Re(conj(pi_v) phi_v) d_q ln D_v.
    K haelt sqrt(*0) phi und pi / sqrt(*0) stetig.
- **Was daraus vorab folgt [M]:**
  - Feldblock der Klammern: bei R diag(D), bei P und K die Einheit.
  - Je Ecke kinetische Energie |pi|^2/(2 *0): bei R mal D, bei P mal 1/D, bei K unveraendert.
  - Massenterm m^2 |phi|^2 *0 / 2: bei R und P mal D, bei K unveraendert.
  - Lokale Ladung Im(conj(phi) pi) bei komplexem Feld: bei R mal D, bei P und K unveraendert. Ohne Licht ist das die
    Quelle; die Quellenabweichung ist damit vorab bekannt (Kontrolle).
  - Gradiententerm:
    - Er aendert sich bei allen drei Transfers durch die neuen *1, bei R und P gleich.
    - K aendert ihn zusaetzlich durch die Umskalierung von phi an den Zug-Ecken, in erster Ordnung in D - 1 und mit dem
      Gradienten gewichtet.
  - An exakter Kosphaerizitaet ist das Voronoi-Diagramm stetig, also *0 stetig und D = 1. Alle drei Transfers fallen
    dann zusammen. Jeder Unterschied waechst mit dem Ueberschuss des Zugs (hier mu).
  - Der Rueckstoss von K verschwindet fuer stationaer rotierende Felder (Re(conj(pi) phi) = 0).
  - Ein symplektischer Diffeomorphismus des ganzen ungekuerzten Phasenraums ist nicht moeglich, weil 2-3 die Kantenzahl
    aendert. Diese Karte prueft nur den Feldblock und die Energie.
- **Nicht ableitbar:**
  - die Verteilung von D - 1 an den Zug-Ecken der gespeicherten Faelle, die Gradientenanteile und die
    Rueckstossenergie einer stehenden Welle
  - die Rangfolge von R, P und K beim masselosen Skalar (K ist dort nicht vorab besser)
  - der Anteil des Skalars am Gesamtsprung, wenn Geometrie und Skalar vergleichbar viel Energie tragen

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| KT0 | Kontrolle [M]: Auf allen Faellen gibt der Code die [M]-Saetze auf 1e-12 relativ wieder (Feldblock, kinetischer und Massenterm je Ecke, lokale Ladung). D - 1 skaliert mit mu: max abs(D - 1) bei mu = -1e-3 geteilt durch den Wert bei mu = -1e-4 liegt zwischen 8 und 12 | 85 % |
| KT1 | [H] Masseloser Skalar (stehende Welle wie UEBERGABE-KONFLUENZ-1, Phase so gewaehlt, dass phi und pi an den Zug-Ecken beide ungleich null sind): Der Median von abs(Delta H_phi) / H_phi ist mit K hoechstens halb so gross wie mit dem besseren von R und P | 40 % |
| KT2 | [H] Massiver komplexer Skalar (m = 1, rotierende Welle phi = A f(r) exp(i (omega t + k1 . r)) mit omega = 0,8 m und Gauss-Profil f der Breite 3 mittlerer Kantenlaengen um den Zug): Der Median von abs(Delta H_phi) / H_phi ist mit K mindestens 10-mal kleiner als mit dem besseren von R und P | 60 % |
| KT3 | [H, Codex] Gesamtsprung bei vergleichbaren Energien (Skalar-Amplitude im Plan so gewaehlt, dass H_phi / H_geo im Anfangszustand zwischen 0,3 und 3 liegt; Geometrie in R bzw. P wie UEBERGABE-KONFLUENZ-1, Form A2): Der Median von abs(Delta H_gesamt) ist mit K fuer den Skalar hoechstens 2-mal kleiner als mit dem besseren von R und P | 60 % |

**Bedeutung (vorab):**
- **KT2 trifft ein:** Fuer Q-Ball-artige Felder ist der kanonische Transfer K der richtige Eintrag in die
  Grundgleichung (Energie, Ladung und Zweiform des Skalars bis auf Gradientenreste erhalten).
- **KT1 verfehlt, KT2 trifft ein:** Die Wahl des Transfers haengt vom Feldtyp ab. Fuer die Grundgleichung zaehlt der
  Q-Ball-Fall; der masselose Fall braucht einen anderen Ausgleich.
- **KT3 trifft ein:** Wie Codex erwartet, sitzt der Energiefehler am Zug vor allem in der Geometrie. Der naechste Schritt
  ist dann der geometrische Transfer, nicht der Skalar.
- **KT3 verfehlt:** Der Skalartransfer traegt einen wesentlichen Teil des Sprungs. K waere dann ein echter Gewinn fuer die
  Energiebilanz.

## Rahmen

- Code-Agent. Code aus RUNDE-37/uebergabe-konfluenz-1/code kopieren, dort nichts aendern. Nur Kopien erweitern um:
  komplexen Skalar mit Massenterm, Transfer K samt Rueckstoss, Zerlegung von Delta H in Geometrie, kinetisch, Masse,
  Gradient und Rueckstoss, sowie das mu-Raster.
- d_q ln D_v fuer alte und neue Zerlegung am Zug: analytisch oder mit zentralen Differenzen, im Plan begruendet. Bei
  Differenzen mit zwei Schrittweiten gegenpruefen.
- Faelle: die 32 Faelle wie UEBERGABE-KONFLUENZ-1 (gleiche Saaten und Auswahlregeln), mu = -1e-3 und -1e-4.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu5 und cpu6. Je Lauf hoechstens 10 min. Zeitbox 120 min.
- Plan und Code vor den Hauptlaeufen einfrieren (sha256).
- Synthetisch, keine Messdatenbestaetigung.
