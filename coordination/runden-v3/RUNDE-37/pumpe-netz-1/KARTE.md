# PUMPE-NETZ-1: Veraendert viel Bewegung bzw. Energieuebertragung das Netz ringsum in Laenge und Richtung, wie eine Pumpe? Strahlt Finns Netz Gravitationswellen ab? (Runde 46, Finn-Auftrag)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 06:00:25 CEST (date), vor jeder Rechnung.
- **Finn (05.10., vor 05:58:58), woertlich:** "Kann vllt viel Bewegung oder viel Energieübertragung das Netz rundrum verändern in der Länge oder in der Richtung wie was pumpt? Review auch Hodge Theorie"
- **Lesart der Leitung:**
  - Ruhende Energie aendert Takt und Laengen. Das ist gezeigt (MATERIE-NETZ-1, V1).
  - Bewegung, also Impuls- und Spannungsfluss, muesste das Netz zusaetzlich in der Richtung verformen: Scherung, Mitfuehrung (Lense-Thirring).
  - Eine schwingende Energieverteilung muesste es periodisch "pumpen": Gravitationswellen, also Laengen quer zur Ausbreitung.
  - Das ist datennah: Die Bahnverkuerzung des Doppelpulsars stimmt mit Einsteins Quadrupolformel auf etwa 1e-3 bzw. besser ueberein; dazu LIGO [L?, Zahl im Ergebnis mit Quelle].
- Kennzeichen: [M], [E], [P], [S], [L], [L?], [H].

## Ableitbarkeitsprobe (vor der Karte, Leitung) [M]

- **V1 koppelt nur Energie, also einen Skalar je Ecke, an die Eckregel.**
  - Bei k = 0 kann ein Skalar unter Wuerfelsymmetrie nur an die Spur-Verzerrung (A1g) koppeln, nicht an spurfreie Verzerrungen.
  - Bei kleinem k ist die Kopplung an quer-spurfreie (TT-)Moden hoechstens O((k l)^2) ueber die Gitteranisotropie: Eine Skalarquelle bei k erzeugt nur die Laengsstruktur k_i k_j, deren TT-Projektion null ist.
  - **Folge (vorab ableitbar):** Mit V1 allein strahlt Finns Netz bei langen Wellen keine Gravitationswellen ab, auch wenn Massen schwingen. Das stuende gegen die Doppelpulsar-Daten.
  - In Einsteins Theorie kommt die Abstrahlung ueber die Spannungen T^ij der Materie. Ueber die Erhaltung haengen sie am zweiten Zeitableitung des Quadrupols.
- **Damit ist die eigentliche Frage nicht ableitbar:**
  - Koppelt man Materie so an das Netz, dass ihre Bewegung bzw. Spannung die Kantenlaengen richtungsabhaengig aendert (etwa ein Materiefeld mit Hodge-Gewichten aus den Kantenlaengen), strahlt das Netz dann?
  - Mit welcher Staerke relativ zur statischen Kopplung (Newton)?
  - Folgt die Leistung der Quadrupolform (~ omega^6 bei fester Amplitude)?
  - Wirkt eine bewegte Quelle als Mitfuehrung (Richtungsaenderung)?

## Rechnung (Code-Agent; Code aus materie-netz-1 und eine-welt-loch-1)

1. **Kontrolle K1 (vorab ableitbar):** Auf dem gefuellten Netz (V1, Paarung A1R1) schwingt eine Quadrupol-Verteilung der Eckenergie mit Frequenz omega. Die abgestrahlte TT-Amplitude im Fernfeld ist bei kleinem k null bis auf O((k l)^2).
2. **Spannungskopplung S:**
   - Ein Materiefeld (Skalarfeld phi auf den Ecken) mit Gradientenenergie ueber Hodge-Gewichte aus den Kantenlaengen (wie die Laengengewichte fuer Maxwell in MATERIE-NETZ-1).
   - Seine Spannung koppelt damit an alle Kantenlaengen.
   - Linearisiert: Quelle = Spannungstensor eines schwingenden phi-Quadrupols, also zwei gegenphasige Klumpen.
   - Messen: TT-Amplitude bzw. -Leistung im Fernfeld gegen omega und gegen den Abstand; Verhaeltnis zur statischen Newton-Kopplung derselben Quelle (gleiche Kopplungskonstante?).
3. **Beschreibend:**
   - Bewegte Quelle (gleichfoermig verschobene Klumpen): Gibt es eine geschwindigkeitsabhaengige Antwort des Netzes in Richtung bzw. Scherung (Mitfuehrung)?
   - Und "Pumpen": Verstaerkt ein periodisch getriebenes Netz Wellen parametrisch?
4. **Ableitbarkeitsprobe des Plans:** Was folgt im Kontinuum aus der linearisierten Einstein-Theorie? Das ist dann die Erwartung, kein Messwert. Gemessen werden nur Gitterabweichungen und die Konsistenz der Kopplungen.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| PN0 | Kontrolle [vorab ableitbar]: Mit V1 allein ist die TT-Abstrahlung eines schwingenden Energie-Quadrupols bei kleinem k unter 1e-3 der Spannungskopplung bzw. skaliert wie (k l)^2 | 85 % |
| PN1 | [H] Mit Spannungskopplung S strahlt das Netz TT-Wellen ab; die Leistung folgt der Quadrupolform (omega^6 bei fester Amplitude) innerhalb von 20 % im Bereich k l < 0,3 | 55 % |
| PN2 | [H] Die Kopplung der Abstrahlung passt zur statischen Newton-Kopplung derselben Quelle (Verhaeltnis wie in der linearisierten Einstein-Theorie innerhalb von 10 %) | 45 % |

**Bedeutung (vorab):**
- **PN0 trifft ein:** Finns Frage trifft den Kern. Damit das Netz Gravitationswellen abstrahlt, muss Bewegung bzw. Spannung das Netz in der Richtung verformen. Energie allein (V1) reicht nicht.
- **PN1 und PN2 treffen ein:** Mit Spannungskopplung (Hodge-Gewichte) "pumpt" schwingende Materie das Netz wie bei Einstein, und die Kopplung ist dieselbe wie bei der Schwerkraft. Das waere ein starkes Indiz fuer Finns Netz.
- **PN2 verfehlt:** Statische Schwerkraft und Abstrahlung haetten verschiedene Staerken. Der Doppelpulsar schliesst das aus [L?].

## Rahmen

- Code-Agent; Code aus materie-netz-1/code und eine-welt-loch-1/code kopieren, dort nichts aendern.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren p4000a bzw. p4000b (GPU), sobald QBALL-DOPPELSPALT-1 sie freigibt, sonst cpu6. Je Lauf hoechstens 10 min, ein Thread. Zeitbox 150 min.
- Plan und Code vor den Hauptlaeufen einfrieren (sha256).
- Ein ehrlicher Teilbericht ist besser als keiner: zuerst K1, dann S.
