# QUANT-2: Licht quantisch: Kompaktes U(1) auf Finns Netz, Photon-Phase gegen Einschluss-Phase mit Faeden (Runde 50, schlanke Karte)

- Leitung claude-primary, geschrieben ab 2026-10-05 18:05:52 CEST (date), vor jeder Rechnung.
- **Finn, 05.10.:** "quantisier mal los". Das Ziel nennt die Schritte (a) quantisieren, (c) Faeden als Mesonen und
  (d) Einschluss.
- **Herkunft [P]:**
  - Fluss-Eis ist klassisch eine Coulomb-Phase; das Licht ist DEC-Maxwell auf V (LICHT-SEKTOR-NOTIZ,
    GRUNDGLEICHUNG-v3).
  - STRING-1: klassische Faeden bei teurem Fluss.
  - Die INDUZIERT-Karten (Runde 38 bis 42) haben freie Felder einschleifig quantisiert (induzierte Schwerkraft). Ein
    kompaktes U(1) mit Monte Carlo gab es im Projekt bisher nicht (grep nach Wilson-Schleife, Polyakov-Schleife,
    kompaktes U(1): nur Polyakovs 2D-Anomalie).
- **Ansatz [L]:** euklidische kompakte U(1)-Eichtheorie, Wilson-Wirkung S = Summe beta_f (1 - cos theta_f) ueber die
  Dreiecke des 4D-Netzes (V mal Zeit, Zeltnetz aus REGIME-K-2). Die Gewichte beta_f folgen aus den Hodge-Sternen, damit
  der Grenzfall Maxwell ist. Kontrolle: dasselbe auf dem hyperkubischen Gitter; dort ist der Phasenuebergang bei
  beta ~ 1,01 bekannt [L].
  - In der Einschluss-Phase (kleines beta) entstehen Flussfaeden zwischen Ladungen: Flaechengesetz der Wilson- bzw.
    Polyakov-Schleifen, Fadenspannung sigma.
  - In der Coulomb-Phase (grosses beta) gibt es ein masseloses Photon.
- **Ableitbarkeit:** Dass es auf dem kubischen Gitter einen Uebergang gibt, ist Literatur. Nicht ableitbar sind die
  Lage auf Finns Netz, sigma, die Lage des Luescher-Terms und ob das Photon auf V richtungsgleich ist.

## Erwartungen (vor jeder Rechnung)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| U1 | Kontrolle: Der Code findet auf dem kubischen Gitter den Uebergang bei beta = 1,01 +- 0,03 | 80 % |
| U2 | Auf Finns 4D-Netz gibt es einen Uebergang bei einem beta_c zwischen 0,5 und 2 (in den Einheiten der gewichteten Wirkung) | 70 % |
| U3 | Unterhalb von beta_c Flaechengesetz mit sigma > 0, oberhalb Umfangsgesetz und ein masseloses Photon (Korrelator faellt wie eine Potenz) | 70 % |
| U4 | Nahe beta_c auf der Einschlussseite passt das statische Potential zu sigma r - c/r mit c auf 50 % bei pi/12 (Luescher) | 35 % |

## Rahmen

- Code-Agent ohne Einfrieren und Leser (Finn: einfach machen).
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu und cpu7 (cpu7 kurz geteilt mit dem Webserver der Ansicht), je
  Lauf hoechstens 10 min; df vor jedem Lauf.
- Synthetisch, keine Messdaten.
