# LIFE-FCC-1: Gibt es "Game of Life"-Gleiter, wenn jeder Knoten 12 Nachbarn hat (Tetraeder-Oktaeder-Packung)? (Runde 38)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-04 07:58:04 CEST (date), vor jeder Rechnung.
- **Anlass:**
  - LIFE-DIAMANT-1: Auf dem Diamantnetz (4 Nachbarn) entsteht in keiner der 512 Regeln ein Gleiter (239 616 Laeufe).
  - Folgevorschlag: mehr Nachbarn.
  - Das fcc-Gitter ist das Knotengitter der Tetraeder-Oktaeder-Packung. Jeder Knoten hat dort 12 Kanten zu den Ecken
    eines Kuboktaeders, also Finns Tetraeder plus Oktaeder als volles Packungsnetz.
  - Finns Frage nach Game-of-Life-Ansaetzen (04.10.).
- **Schreibtisch [M]:**
  - Aussen-totalistische Regeln mit 12 Nachbarn: B, S Teilmengen von {0..12}, 2^26 Regeln, nicht vollstaendig
    durchsuchbar.
  - Gesucht wird in der ueblichen Unterklasse der Intervallregeln: B = [b1..b2] mit 1 <= b1 <= b2 <= 12, S = [s1..s2]
    mit 0 <= s1 <= s2 <= 12. Das sind 78 x 91 = 7098 Regeln.
  - Die Lichtkegelgrenze haengt von der Richtung ab. Pro Schritt sind Spruenge bis zu einer Nachbarkante moeglich.
  - Literatur [L?]: Carter Bays hat 3D-Leben auf dem kubischen Gitter (26 Nachbarn) untersucht und Gleiter gefunden.
    Fuer fcc ist der Leitung nichts Sicheres bekannt.
- Kennzeichen: [M] Mathematik, [L] Literatur, [L?] unsicher, [H] Hypothese.

## Test (Code-Agent)

- Code aus LIFE-DIAMANT-1 wiederverwenden (unbegrenztes Gitter, Formkennung, Einordnung, Durchgangsprobe mit
  Kunst-Gleitern), Nachbarschaft auf fcc (12) umstellen.
- **Stufe 1:** alle 7098 Intervallregeln, je 16 bis 32 Saaten (Zufallsmuster in kleinem Bereich, mehrere Dichten).
- **Stufe 2:** die Regeln mit kleinen, langlebigen Mustern (weder Aussterben noch Wachstum) mit mehr Saaten und groesseren
  Startbereichen, im Plan vor dem Einfrieren festgelegt.
- **Fuer jeden Gleiter:** Periode, Verschiebung, Geschwindigkeit gegen die Lichtkegelgrenze in seiner Richtung, Groesse,
  Verhalten unter den 24 Drehungen des Wuerfels bzw. den 12 des Tetraeders.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| LF0 | Kontrolle: Gitter korrekt (12 Nachbarn); die Durchgangsprobe mit Kunst-Gleitern findet alle | 90 % |
| LF1 | [H] Mindestens eine Intervallregel hat einen Gleiter, der aus Zufallsstarts entsteht | 60 % |
| LF2 | [H] Falls Gleiter gefunden werden: Alle sind hoechstens halb so schnell wie die Lichtkegelgrenze ihrer Richtung | 60 % |
| LF3 | [H] Falls Gleiter gefunden werden: Es gibt mehr als eine Gleiterform (nicht nur eine Regel mit einem Gleiter) | 50 % |

**Bedeutung (vorab):**
- **LF1 trifft ein:** Auf der vollen Tetraeder-Oktaeder-Packung entstehen aus einfachen Ja/Nein-Regeln bewegte
  "Teilchen" mit Hoechstgeschwindigkeit. Diamant mit 4 Nachbarn ist zu arm, die Packung reich genug.
- **LF1 verfehlt:** Auch 12 Nachbarn reichen in der Intervallklasse nicht; klassische Gleiter brauchen dann andere
  Regelformen oder mehr Zustaende.
- **Grenze:** Klassische Muster tragen keinen Spin (-1). Fuer Spin ist der Quanten-Zellautomat zustaendig.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spur cpu7; je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 90 min.
