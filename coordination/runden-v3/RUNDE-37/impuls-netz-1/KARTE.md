# IMPULS-NETZ-1: Spuert Finns Netz den Schwung der Materie? Impulskopplung gegen die Laengs-Leckage der Abstrahlung (Doppelpulsar) und fuer die Mitfuehrung (Runde 46, Folgekarte zu PUMPE-NETZ-1)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 07:12:50 CEST (date), vor jeder Rechnung.
- **Finn (05.10.):** "Kann vllt viel Bewegung oder viel Energieübertragung das Netz rundrum verändern in der Länge oder in der Richtung wie was pumpt?"
- **Herkunft:** PUMPE-NETZ-1 (RUNDE-37/pumpe-netz-1/ERGEBNIS.md), frisch gegengelesen:
  - Mit Spannungskopplung (P1-Hodge-Gewichte) strahlt ein schwingender Quadrupol TT-Wellen ab, im reinen TT-Kanal wie Einstein, mit G wie Newton auf 3e-6.
  - **Aber:** Laengs- und Energieanteile der Quelle erreichen die TT-Moden (Laengsspannung bis 17 % in der Amplitude). Damit ist G_rad/G_N = 1,18 / 0,91 / 0,98 je nach Quellachse; Kreisbahnen -0,75 % bis +3,4 % je nach Lage.
  - Der Doppelpulsar bestaetigt die Quadrupolformel auf 1,3e-4 (Kramer u. a. 2021) [S].
  - Deutung [H]: Ohne Impulskopplung ist die Quelle fuer das Netz nicht erhalten. Am Schreibtisch [M]: keine Mitfuehrung in O(v), weil die Impulsbedingung des Netzes keine Materiequelle hat. Das Netz haette damit ein Vorzugssystem.
  - Codex' Luecke L10 (gemeinsame Wirkung, universelle Kopplung) [P].
- Kennzeichen: [M], [E], [P], [S], [L], [H].

## Ableitbarkeitsprobe (vor der Karte, Leitung)

- **Vorab ableitbar [L]:** In der linearisierten Einstein-Theorie mit erhaltener Quelle (Energie, Impuls und Spannung gekoppelt) erreicht nur der TT-Anteil die Wellen. Die Leckage verschwindet wegen der Eichinvarianz, die Mitfuehrung hat den Einstein-Koeffizienten (Lense-Thirring).
- **Nicht ableitbar:**
  - Ob sich auf Finns Hamilton-Netz eine Impulskopplung widerspruchsfrei einbauen laesst. Die skalare Regel ist dort zweiter Klasse (TT-ISO-1), und eine eigene Vektor- bzw. Impulsregel gibt es bisher nicht als Zwangsbedingung mit Materiequelle.
  - Ob die Leckage dann verschwindet.
  - Ob die Mitfuehrung den Einstein-Wert hat.
- **Gedaechtnis-Regel:** Mein eigenes Symmetrieargument zu PN0 war falsch (gilt nur bei k = 0). Darum wird hier jede Vorab-Aussage ueber Kopplungen bei k != 0 am Code geprueft, nicht nur an der Gruppe.

## Rechnung (Code-Agent; Code aus pumpe-netz-1/code)

1. **Formulierung (Schreibtisch, zuerst):** Welche Netzgroesse ist die Impuls- bzw. Verschiebungsregel (Erzeuger der Eckverschiebung bzw. des Shifts), und wie koppelt die Impulsdichte des Materiefelds daran?
   - Gibt es keine widerspruchsfreie Kopplung im jetzigen Netz, ist das ein gueltiges Ergebnis; es steht dann mit Begruendung im Plan.
2. **Leckage:** dieselbe Quelle wie PUMPE-NETZ-1 (schwingender phi-Quadrupol, drei Achsen) mit Impulskopplung. G_rad/G_N je Achse; Kreisbahnen in mehreren Lagen.
3. **Mitfuehrung:** gleichfoermig bewegte bzw. rotierende Quelle; gravitomagnetische Antwort des Netzes gegen den Einstein-Koeffizienten.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| IN0 | Kontrolle: Ohne Impulskopplung reproduziert der Code PUMPE-NETZ-1 (G_rad/G_N = 1,18 / 0,91 / 0,98 auf 1 %) | 90 % |
| IN1 | [H] Es gibt im jetzigen Hamilton-Netz eine widerspruchsfreie Impulskopplung (Plan-Teil 1) | 55 % |
| IN2 | [H] Mit Impulskopplung liegt G_rad/G_N fuer alle drei Achsen innerhalb 1e-2 bei 1 | 40 % |
| IN3 | [H] Die Mitfuehrung hat den Einstein-Koeffizienten auf 10 % | 40 % |

**Bedeutung (vorab):**
- **IN2 und IN3 treffen ein:** Spuert das Netz den Schwung der Materie, strahlt und dreht es wie bei Einstein. Doppelpulsar und Lense-Thirring waeren dann im Bereich, und L10 haette einen ersten gemeinsamen Baustein.
- **IN1 verfehlt:** Das jetzige Netz kann den Impuls nicht aufnehmen; es braucht eine neue Regel. Das wird die wichtigste Baustelle fuer L1 und L10.

## Rahmen

- Code-Agent; Code aus pumpe-netz-1/code kopieren, dort nichts aendern.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu5 und cpu6. Je Lauf hoechstens 10 min, ein Thread. Zeitbox 150 min.
- Plan und Code vor den Hauptlaeufen einfrieren (sha256).
- Ein ehrlicher Teilbericht ist besser als keiner: Teil 1 zuerst.
