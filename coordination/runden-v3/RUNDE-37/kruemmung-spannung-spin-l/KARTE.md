# KRUEMMUNG-SPANNUNG-SPIN-L: Wird Kruemmung im Netz zu Spannung und umgekehrt, und kann Kruemmung zu Spin bzw. Richtung werden? (Runde 48, Finns Fragen)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 10:35:57 CEST (date), vor jedem Abruf.
- **Herkunft:** Finn, 05.10.2026, Eingang vor 10:31, woertlich:
  - "Was ist wenn Krümmung zu Spannung wird und umgekehrt?"
  - "Könnte dann Krümmung zu Spin / Richtung werden"
- **Projektbefunde [P]** (nicht als neu fuehren):
  - REGGE-TORSION-L (RUNDE-44): Torsion sitzt je Grenzflaeche (3 Zahlen je Dreieck). Ein Band um eine von Finns Linien misst den Fehlwinkel (Kruemmung), ein Band zwischen zwei Zellen eine Torsionskomponente. Spin 1/2 ist dort nicht eingebaut.
  - TORSION-STEIF-1 (RUNDE-45): Die Rahmendrehung um eine Kante ist gleich dem Fehlwinkel (auf 2e-14). Je Zelle bleiben 4 kruemmungsfreie Rahmendrehungen frei, die keine Regel festlegt (vorab abzaehlbar: 18 gegen 14). Eine Guertel-Energie auf der Holonomie macht sie beweglich (Cosserat-Typ), ein Rest bleibt frei.
  - WELTKRISTALL-L (RUNDE-46):
    - Frank-Kasper-Phasen als Disklinationsnetz der geplaetteten 600-Zelle. Im flachen Raum wird Kruemmung in Defektlinien und Verzerrung umgesetzt ("Spannung statt Kruemmung"). C15 und A15 liegen beidseits der Flachheitszahl.
    - Kleinerts Weltkristall: Torsion gegen Kruemmung ist eine Eichwahl (Bennett u. a. 2013, nur Abstract).
  - GUERTEL-FINN-NETZ-1 (RUNDE-43): Ein SO(3)-Drehfeld auf Finns Diamant-Netz legt 720 Grad stetig ab, ein SO(2)-Feld nicht (quasistatisch).
  - IDEEN-EVOLUTION/GEN-04-SPIN-HALB.md: H2 Ladung + Monopol, H4 Finkelstein-Rubinstein, H7 Torsion als Spin-Traeger, H10 Spin-Struktur. Die unveraenderte Q-Ball-Formel ist nur bosonisch (zusammenziehbarer Konfigurationsraum).
  - INDUZIERT-1 (RUNDE-38): Ein Skalarfeld auf dem festen 4D-Kuhn-Netz erzeugt keine Einstein-Steifigkeit (Sakharov-Test).
  - RUNDE-22: In der CDT-Literatur gab es 2025 einen Hinweis auf einen teilchenartigen Zustand aus reiner Geometrie (Geon), nicht vertieft.
  - SOC-RAUM-L (RUNDE-48): Flache Umklappzuege verteilen keine Kruemmung um. SOC-UMKLAPP-1 braucht eine neue Regel, und das ist eine Weiche fuer Finn.
- Kennzeichen: [M] Mathematik, [S] an der Quelle gelesen (mit Abschnitt, Gleichung oder Seite), [S Abstract], [L] Gedaechtnis, [P] Projekt, [ES] Schreibtisch, [H] Hypothese.

## Ableitbarkeitsprobe (Leitung)

- **Vorab ableitbar [M]:**
  - **Schlaefli-Identitaet im 3D-Regge-Netz:** Die Ableitung von Summe_e l_e eps_e nach l_e ist eps_e. Die "Zugspannung" einer Kante in der Kruemmungsenergie ist also ihr Fehlwinkel. Mit Materie steht dem die Materiespannung an derselben Kante gegenueber; das ist die diskrete Einsteingleichung (Regge 1961) [M, L].
    - **Folge:** "Kruemmung = Spannung" ist im Netz keine neue Annahme, sondern die Feldgleichung selbst.
  - **Ein Fehlwinkel ist ein Holonomie-Drehwinkel:** Wird eine Richtung einmal um die Kante getragen, kommt sie um eps_e gedreht zurueck [M]. TORSION-STEIF-1 hat das auf dem Netz nachgerechnet [P].
  - **Gauss-Bonnet in 2D:** Die Summe der Fehlwinkel ist 2 pi chi, also topologisch erhalten ("Kruemmungskoerner" wie im Sandhaufen). In 3D gilt fuer Summe l_e eps_e keine solche Erhaltung [M].
  - **Spin-Struktur:** Jede orientierbare 3-Mannigfaltigkeit ist parallelisierbar und traegt eine Spin-Struktur. Spinoren lassen sich auf Finns Raum also immer definieren. Die Frage ist, ob Geometrie allein halbzahligen Drehimpuls **erzwingt** [M].
  - Eine SO(3)-Holonomie liefert halbzahligen Spin erst mit einer Z_2-Vorzeichenwahl (Hebung nach SU(2)) [M].
- **Nicht ableitbar:**
  - welche Arbeiten Spin 1/2 aus Topologie bzw. Torsion auf diskreten Raeumen konkret zeigen
  - ob Geonen mit halbzahligem Spin auch Fermionen sind
  - ob eine "Kruemmungs-Sandhaufen"-Regel schon untersucht ist
  - wie stark Labordaten eine Spin-Torsion-Kopplung einschraenken
- **Kennzahlen-Abgleich:** keine neue Rechnung; die Projektkennzahlen oben gelten.

## Fragen

1. **Geonen:**
   - Friedman/Sorkin 1980 ("Spin 1/2 from gravity") und Nachfolger: Welche 3-Mannigfaltigkeiten sind spinoriell, und unter welcher Bedingung?
   - Braucht es Quantengravitation, also eine Wellenfunktion auf dem Konfigurationsraum?
   - Gilt die Spin-Statistik-Verbindung (Aneziris u. a. 1989; Dowker/Sorkin 1998; Stand 2024 bis 2026)?
2. **Diskrete Umsetzungen:**
   - Halbzahliger Spin aus Topologie oder Torsion in Regge, CDT, Kausalmengen oder Gruppenfeldtheorie.
   - Den CDT-Geon-Hinweis von 2025 aus RUNDE-22 genau bestimmen (Autoren, arXiv-Nummer, was gezeigt ist).
   - Bei LQG ist SU(2) Eingabe, nicht Ergebnis; so kennzeichnen.
3. **Spin als Quelle der Torsion:**
   - Einstein-Cartan bzw. Poincare-Eichtheorie auf Simplex-Netzen mit Fermionen, ueber Yan/Ding/Ma und Christiansen/Hu/Lin hinaus (beide im Projekt).
   - Welche Energie laesst Torsion sich ausbreiten?
4. **Kruemmung <-> Spannung als Dynamik:**
   - Seung/Nelson 1988: Beulen einer Membran mit Disklination (Spannung -> Kruemmung)
   - Nelson, "decurving": Kruemmung -> Defekte und Verzerrung
   - Bowick/Nelson/Travesset: Kruemmung als Hintergrundladung fuer Disklinationen
   - Gibt es eine SOC- bzw. Sandhaufen-Regel mit Kruemmung (Fehlwinkel) als umverteilter Groesse, bei dynamischen Triangulierungen oder Membranen?
5. **Gegensweep:**
   - Argumente, dass Geometrie allein keine Fermionen liefert
   - Spin-Bahn- bzw. Mathisson-Papapetrou-Grenzen
   - Labor- und Astro-Schranken auf Spin-Torsion-Kopplung, z. B. Torsionspendel mit polarisierten Spins und Kostelecky/Russell/Tasson 2008, und was sie fuer Einstein-Cartan bedeuten
   - 24-Monats-Suche nach Arbeiten, die "Kruemmung -> Spin" auf Netzen behandeln

## Vorhersagen (vor jedem Abruf)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| KS1 | [L] Friedman/Sorkin 1980 zeigen halbzahligen Drehimpuls aus reiner Gravitation fuer spinorielle 3-Mannigfaltigkeiten. Bedingung: Die 2-pi-Drehung (Diffeomorphismus) ist nicht isotop zur Identitaet; zugelassen sind Wellenfunktionen, die darunter das Vorzeichen wechseln. | 85 % |
| KS2 | [L] Ohne Topologieaenderung koennen solche Geonen die Spin-Statistik-Verbindung verletzen (Aneziris u. a. 1989). Mit Topologieaenderung (Hosenbein-Geschichten) gilt sie fuer eine Klasse von Geonen (Dowker/Sorkin 1998). | 65 % |
| KS3 | [H] Mindestens eine Arbeit konstruiert spinorielle Geonen oder halbzahligen Spin aus Topologie konkret auf einem simplizialen bzw. diskreten Raum (Regge, CDT, Kausalmengen, Gruppenfeldtheorie) oder zeigt ihn numerisch. | 35 % |
| KS4 | [L] Einstein-Cartan: Die Spindichte bestimmt die Torsion algebraisch, ohne Ausbreitung. Labor-Schranken mit polarisierten Spins treffen deshalb vor allem Modelle mit ausbreitender Torsion bzw. Hintergrund-Torsion, nicht die reine Einstein-Cartan-Theorie. | 60 % |
| KS5 | [H] Eine Sandhaufen- bzw. SOC-Regel mit Kruemmung (Fehlwinkel) als umverteilter Groesse ist bei dynamischen Triangulierungen oder Membranen schon untersucht. | 30 % |

**Bedeutung (vorab):**
- **KS1 und KS2 treffen ein:** Halbzahliger Spin kann aus der Topologie des Raumes kommen, nicht aus Kruemmung allein. Fuer Finns Netz hiesse das: Spin entsteht aus Verknotung bzw. Henkeln im Netz, Kruemmung allein dreht nur Richtungen. Ob es Fermionen sind, haengt an der Topologieaenderung. Pachner-Zuege (2-3, 3-2, 1-4, 4-1) tauschen nur eine Kugel gegen eine Kugel mit gleichem Rand und aendern die Topologie deshalb nicht [M]; dafuer braucht es eine weitere Zugart.
- **KS3 verfehlt:** Eine Netz-Umsetzung waere offen und damit ein moeglicher eigener Beitrag [H].
- **KS5 verfehlt:** Finns Regel "Kruemmung wird Spannung" als Umverteilungsregel fuer SOC-UMKLAPP-1 waere neu [H].

## Rahmen

- feldforscher nach Feld-Regeln:
  - Arbeitsdatei ARBEITSFELD.md, Ergebnis DOSSIER.md, beide in diesem Kartenordner.
  - Erwartung vor jedem Abruf, Gegensweep, Erwartungsverstoesse, Negativliste.
- Hoechstens 20 Abrufe, Zeitbox 90 min. Keine Rechnung.
- Synthetisch bzw. Literatur, keine Messdatenbestaetigung.
