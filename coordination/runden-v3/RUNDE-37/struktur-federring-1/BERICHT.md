# STRUKTUR-FEDERRING-1: Bericht (Runde 41, zusammengelegt mit GUERTEL-1)

- **Bearbeitung:** Code-Agent fuer die Leitung claude-primary. Gemeinsamer Auftrag mit GUERTEL-1, Start 2026-10-04
  14:51:08 CEST. Text ab 15:30:28 CEST, nach den GUERTEL-1-Hauptlaeufen um deren Ergebnisse ergaenzt (letzte Aenderung
  vor 16:08:47 CEST, date).
- **Kennzeichen:**
  - [B] am Bild abgelesen (bild-finn-20261004.png, mit dem Read-Werkzeug angesehen; kann ungenau sein)
  - [M] Mathematik; [S] an der Quelle gelesen; [L] Gedaechtnis; [ES] eigener Schluss; [H] Hypothese
  - [G] in GUERTEL-1 gerechnet (synthetisch)
- **Abrufe:** 3 fuer beide Karten zusammen (Grenze 10), keine Websuche. Kopien in quellen/ (gleiche Dateien wie in
  RUNDE-37/guertel-1/quellen/):
  - Staley, "Understanding Quaternions and the Dirac Belt Trick", arXiv:1001.1778v3 (Eur. J. Phys. 31 (2010)).
  - Copeland, Saffin, Zhou, "Charge-Swapping Q-balls", arXiv:1409.3232v1 (2014).
  - Mebius, "A matrix-based proof of the quaternion representation theorem for four-dimensional rotations",
    arXiv:math/0501249v1 (2005).
- Alles Weitere ist [L] und als solches markiert. Keine Rechnung fuer diese Karte. Die Rechnung zum Guerteltrick steht in
  GUERTEL-1.

## Ergebnis zuerst

1. **Mechanik [B, ES]:** Finns Teil ist ein nachgiebiger Drehmechanismus. Nabe und drei Ringe haengen an
   Maeanderfedern, und Speichen mit Rastnasen sperren die Drehung in der Ebene an festen Winkeln.
   - Frei im Raum kann ein Ring um mehr als die Hoehe einer Rastnase aus der Ebene ausweichen. Dann gleitet die Nase
     ueber die Sperre, und die Drehung geht weiter.
   - Begrenzt bleibt sie durch die Federn: Ihre Energie waechst mit dem Drehwinkel, und gestreckt sind sie am Ende ihrer
     Laenge.
   - Die wirksame Sperre ist das Kleinere aus Rasthoehe und Ausweichenergie, also hoechstens min(V_R, k_z h^2/2).
2. **Der eine Mechanismus, der etwas vorhersagt [M, S, G]:** "Die dritte Dimension loest Sperren, aber nur bis auf
   einen Rest." In der Ebene ist eine Windung ganzzahlig und erhalten (pi_1(SO(2)) = Z). Im Raum bleibt bei angebundenen
   Koerpern nur ihre Paritaet (pi_1(SO(3)) = Z_2). Das ist der Guerteltrick; GUERTEL-1 hat ihn am Tetraeder-Knoten
   gerechnet [G]:
   - Im Raum kostet eine volle Umdrehung nur 1/65 der Energie in der Ebene (L = 1,8 d).
   - Die Entwirrung nach 720 Grad fand einfaches Abkuehlen aber nicht.
   - Stattdessen rastet der Knoten in Zwischenstellungen ein und springt ruckweise (Spruenge bei 375 bis 721 Grad).
     Das ist mechanisch dasselbe Bild wie Finns Federring: Rastung plus Ausweichen in die dritte Dimension, begrenzt.
3. **Gegenstuecke mit Vorhersagekraft:**
   - Frenkel-Kontorova-Ketten mit Kinks: dieselben Gleichungen wie eine Ringkette mit Rastung.
   - Orientierungsordnung mit Tetraeder-Rastung: Ihre Linienfehler bilden die Gruppe 2T mit 24 Elementen [L Mermin];
     darin ist die 360-Grad-Drehung ein eigener, nichttrivialer Fehler.
   - Nachgiebige mehrstabige Metamaterialien: Umschnappen, Uebergangswellen [L].
   - Nur schoene Analogien fuer das Weltmodell: Synchronisation verschachtelter Ringe (ohne Antrieb keine
     Synchronisation) und Finns Viertakt-Bild.
4. **Drehungs-Cluster [S, M]:** "Synchrones Drehen in zwei Ebenen" hat eine scharfe Form.
   - Die isokline Doppeldrehung ist eine Multiplikation mit einer Einheitsquaternion (Mebius [S]); ihre Bahnen auf S^3
     sind Hopf-Fasern [L].
   - Fuer ein zweikomponentiges Feld ist das die gemeinsame innere Phase eines Dublett-Q-Balls. Seine Projektion auf
     S^2 steht still, wie bei den isospinning Texturen aus SPIN-HOPF-L.
   - Ladungstauschende Q-Baelle [S] zeigen einen echten Takt "+, 0, -, 0" der Ladung an einem Ort. Er ist aber
     360-periodisch in der relativen Phase und hat keine Doppelueberlagerung.
5. **Kartenvorschlaege:**
   - SYNCHRON-QBALL-1 in der einfachen Form (SU(2)-symmetrisches Potential) ist vollstaendig ableitbar: Rechnen lohnt
     nicht.
   - Nicht ableitbar und damit einen Lauf wert waere nur die ladungstauschende Fassung mit zwei Komponenten, vorher
     mit einem Literaturabruf.
   - Fuer die Federring-Mechanik schlage ich FK-RINGKETTE-1 vor (Abschnitt 5). Sie hat geringen Physikwert und
     niedrige Prioritaet.

## 1. Mechanik der Struktur

### 1.1 Was das Bild zeigt [B]

- Gruener 3D-Druck, flach.
  - Aussenring mit geriffeltem Rand und eingepraegter Schrift.
  - Innen ein mittlerer und ein innerer Ring, dazu eine Nabe mit Scheibe.
- Maeanderfedern:
  - zwischen Aussen- und Mittelring in drei Boegen;
  - zwischen Mittel- und Innenring in zwei Boegen;
  - um die Nabe als radiale Schlaufen ("Bluetenblaetter").
- Radiale Speichen in etwa fuenf Richtungen kreuzen die Spalte zwischen den Ringen. An den Kreuzungen sitzen kleine
  T-foermige Nasen bzw. Kerben: die Rastung. Genauer laesst sich die Form am Bild nicht ablesen.

### 1.2 Freiheitsgrade und Steifigkeiten [ES, L Balkenbiegung]

- Jeder Ring und die Nabe sind fast starr. Relativ zum Nachbarn bleiben sechs Freiheitsgrade: Drehung in der Ebene
  (phi), zwei Verschiebungen in der Ebene, Hub z aus der Ebene, zwei Kippungen.
- Ein Federstreifen der Breite w (in der Ebene) und Hoehe t (Druckhoehe) biegt in der Ebene mit Steifigkeit proportional
  t w^3, aus der Ebene proportional w t^3 [L].
  - Das Bild deutet auf t >= w: Der Streifen ist in der Ebene weich (so gewollt, fuer die Drehung).
  - Aus der Ebene ist der Streifen steifer, aber die Ringe koennen durch Verdrillen der Streifen kippen und heben.
  - Die Nasen greifen nur ueber die Druckhoehe h.
- **Rastung:** In der Ebene stossen die Speichennasen an die Kerben. Das ergibt feste Winkel: Anschlaege oder
  einrastende Mulden.
- **Schwingungsmoden:**
  - In der Ebene: Drehmoden der drei Ringe gegeneinander, omega_i ~ sqrt(k_phi,i / I_i).
  - Aus der Ebene: weiche Trommelmoden (Hub, Kippen).
  - Frei schwebend koppeln beide ueber die Rastung nichtlinear.

### 1.3 Schreibtischmodell: warum frei im Raum mehr, aber begrenzt [M, ES]

- Ein Ring gegen seinen Nachbarn:
  E(phi, z) = k_phi phi^2 / 2 + k_z z^2 / 2 + V_R(phi) s(z),
  mit V_R(phi) den Rasthoehen an den Winkeln phi_n und s(z) = max(0, 1 - z/h)^2 dem Ueberlapp der Nase.
- **In der Ebene** (Tisch und Schwerkraft halten z = 0): Die Sperre ist V_R.
- **Frei im Raum:** Die wirksame Sperre ist B_eff = min_z [k_z z^2 / 2 + V_R s(z)] <= min(V_R, k_z h^2 / 2).
  - Ist das Ausweichen billig (k_z h^2 / 2 < V_R), laeuft die Drehung ueber die Rastung hinaus.
  - Gestoppt wird sie, wenn k_phi phi^2 / 2 die verfuegbare Energie erreicht oder wenn die Maeander gestreckt sind
    (geometrische Grenze aus der ausgezogenen Federlaenge). "Mehr, aber nicht unendlich."
- Bei einer Kette aus drei Ringen und Nabe addieren sich die Winkel. Die Sperren wirken je Spalt, deshalb koennen die
  Ringe nacheinander durchrutschen. Das fuehrt zu Abschnitt 2.1.

## 2. Gegenstuecke (Kennzeichen, Urteil: Analogie oder Mechanismus)

### 2.1 Waschbrett, Kinks, Sinus-Gordon, Frenkel-Kontorova [L Braun/Kivshar, Phys. Rep. 306 (1998)]

- **Gleich:** Ringe als Teilchen in einem periodischen Rastpotential, gekoppelt durch Federn:
  E = Summe [k (phi_n+1 - phi_n)^2 / 2 + V (1 - cos N phi_n)]. Das ist die Frenkel-Kontorova-Kette.
- **Vorhersage:**
  - Metastabile Zustaende werden durch Rastzahlen je Spalt gezaehlt.
  - Ein Durchrutschen ist ein Kink, im Kontinuum ein Sinus-Gordon-Soliton, mit Peierls-Nabarro-Sperre.
  - In laengeren Ketten wandern Kinks.
- **Urteil:** Mechanismus fuer die Ringkette (gleiche Gleichungen). Fuer Finns Netz nur, wenn die Knoten selbst eine
  Rastung haben; das hat unser Modell bisher nicht.

### 2.2 Synchronisation verschachtelter Oszillatoren, Arnold-Zungen [L Pikovsky/Rosenblum/Kurths 2001]

- **Gleich:** Ringe als gekoppelte Rotoren.
- **Unterschied:** Synchronisation braucht selbsterregte Oszillatoren mit Energiezufuhr. Finns Teil ist passiv und hat
  Normalmoden. Unter periodischem Antrieb waeren Modenrastung und Teufelstreppe moeglich (FK mit Antrieb [L]).
- **Urteil:** Analogie, solange nichts antreibt.

### 2.3 Diracs Guertel- und Tellertrick [S Staley; L Dirac, Newman 1942; G GUERTEL-1]

- **Gleich:** Ein Koerper (Nabe) haengt an elastischen Elementen an seiner Umgebung (Aussenring). Die dritte Dimension
  erlaubt Wege "aussen herum", die in der Ebene gesperrt sind.
- **Quelle [S]** (Staley, S. 9 f.): Eine 2-pi-Drehung um eine Achse laesst sich "continuously deformed into a rotation
  of 2pi about another axis, or into a rotation of -2pi about the original axis, without changing the end points". Bei
  4 pi heben sich die beiden Haelften auf.
- **Vorhersage [M]:**
  - In der Ebene ist die Windung eine ganze Zahl und erhalten.
  - Im Raum ist bei mindestens drei Faeden nur ihre Paritaet erhalten (Kugelzopfgruppe: Delta^2 hat Ordnung 2 [L]).
    360 Grad bleiben gesperrt, 720 Grad nicht.
- **Unterschied zum Federring:** Finns Federn liegen in einer Ebene und sind kurz und steif. Der volle Tellertrick
  (Federn ueber die Nabe hinweg fuehren) ist am Druckteil mechanisch nicht erreichbar, nur ein Teilweg.
- **Urteil:** Mechanismus mit Vorhersage. Ergebnis der Rechnung in GUERTEL-1/ERGEBNIS.md [G]:
  - Ebene: Windungen erhalten. 360 Grad kosten 2700 Energieeinheiten.
  - Raum: 41. Der Faden-Knoten bleibt nach 720 Grad unter einfachem Abkuehlen verheddert (Energie 21-mal der
    Grundzustand).
  - Bei 360 Grad wandert die Verdrillung von einer allgemeinen auf eine bevorzugte Achse.

### 2.4 Rastordnungen mit T bzw. 2T, nichtabelsche Fehler [L Mermin, Rev. Mod. Phys. 51 (1979); Poenaru/Toulouse 1977]

- **Gleich:** Ein Medium, dessen Knoten Tetraeder-Orientierungen mit Rastung tragen (Ordnungsparameterraum SO(3)/T).
- **Vorhersage [L, M]:**
  - Linienfehler werden durch pi_1(SO(3)/T) = 2T klassifiziert, die binaere Tetraedergruppe mit 24 Elementen.
  - Sie ist nichtabelsch: Fehler aus verschiedenen Konjugationsklassen koennen sich nicht frei kreuzen.
  - Das Element -1 (eine volle 2-pi-Drehung beim Umlauf) ist ein eigener, nichttrivialer Fehler. Zwei davon heben sich
    auf. Das ist der Guerteltrick in einem Medium.
- **Urteil:** Mechanismus. Die Klassifikation ist Literatur, also ableitbar. Neu waeren Energie und Dynamik solcher
  Fehler in Finns Netz (Idee H4 TETRA-RAHMEN-1).

### 2.5 Q-Baelle mit innerer Drehung und Rastung [S Copeland/Saffin/Zhou; L]

- Ein Q-Ball dreht seine innere Phase gleichmaessig (U(1)). Ein Rastterm eps Re(phi^N) bricht U(1). Dann ist die
  Ladung nicht mehr erhalten und die innere Drehung "rattert" [L, bekannt etwa von A-Termen der Affleck-Dine-
  Kondensate].
- **Ladungstauschende Q-Baelle [S]** (arXiv:1409.3232v1, S. 1 bis 3):
  - Ein Q-Ball und ein Anti-Q-Ball mit ueberlappenden Kernen bilden einen Verbund.
  - Positive und negative Ladung "swap at a frequency lower than the natural oscillation frequency of each constituent
    Q-ball".
  - In 2+1 Dimensionen lebt der Verbund "at least O(10^4) natural oscillation periods, as long as our simulations
    reliably run".
  - Erklaerung der Autoren: phi_2 schwingt "slightly higher" als phi_1, die relative Phase driftet, und das Vorzeichen
    der Ladung folgt ihr. Zwei Oszillonen ziehen sich an, wenn sie nahezu in Phase sind (Phasendifferenz <~ pi/2), und
    stossen sich in Gegenphase ab.
  - Coleman-Stabilitaet greift nicht, weil die Gesamtladung null ist; die Autoren schliessen absolute Stabilitaet aus.
- **Gleich:** Zwei gekoppelte innere Rotoren tauschen den Drehsinn. An einem Ort laeuft die Ladung +, 0, -, 0. Das
  ist Finns Viertakt in der Ladung.
- **Unterschied [M]:** Der Takt ist 360-periodisch in der relativen Phase; eine Doppelueberlagerung gibt es nicht.
- **Urteil:** Fuer den Viertakt eine echte Analogie mit Rechnung in der Literatur. Fuer halben Spin kein Mechanismus.

### 2.6 Nachgiebige mehrstabile Mechanismen und mechanische Metamaterialien [L Howell 2001; Shan u. a. 2015; Nadkarni u. a. 2016]

- **Gleich:** Finns Teil gehoert in diese Familie: Nachgiebigkeit statt Gelenken, mehrere stabile Zustaende,
  Umschnappen.
- **Vorhersage [L]:** Energie wird in Rastzustaenden gespeichert. In mehrstabilen Gittern laufen Uebergangswellen; das
  sind Kinks.
- **Urteil:** Mechanismus, aber Ingenieurwissen, keine neue Physik.

## 3. Inspiration fuer das Weltmodell (Analogie gegen Mechanismus)

| Idee | Art | Pruefbar? |
|---|---|---|
| Dritte Dimension loest Sperren bis auf eine Paritaet (Ebene Z, Raum Z_2) | Mechanismus [M] | ja, GUERTEL-1 (gerechnet: Raum 65-mal billiger; Entwirrung bei 720 Grad nicht gefunden, Zwischenrasten) |
| Tetraeder-Knoten mit T-Rastung: Fehler aus 2T, darunter die 2-pi-Disklination | Mechanismus [L] | Klassifikation ableitbar; Energetik auf dem Netz offen |
| Rastende Knoten: Kinks als teilchenartige Anregungen ohne Feldtopologie | Mechanismus [L] | in 1D ableitbar (FK); Netz offen, braucht Rastpotential als Zusatz |
| Synchrones Drehen verschachtelter Ringe | Analogie | ohne Antrieb keine Vorhersage |
| Viertakt / Nockenwelle | Analogie [M] | die 2:1-Uebersetzung ist in der Ebene beliebig, erst im Raum erzwungen (GUERTEL-1 PLAN 1.1) |
| Ladungstausch +, 0, -, 0 | Analogie [S] | 360-periodisch, kein halber Spin |

- Ehrliche Einordnung [ES]:
  - Das Bild liefert eine gute Anschauung fuer "Rastung plus Ausweichen in die dritte Dimension".
  - Neue Physik fuer das Netz folgt daraus erst, wenn die Knoten eine eigene Rastung oder Anbindung bekommen. Das
    waere eine Zusatzannahme, also eingesetzt und nicht entstanden.

## 4. Drehungs-Cluster (Finn: "synchrones drehen in mehreren dimensionen")

1. **Isokline Doppeldrehung und Quaternionen [S Mebius, Abschn. 4.1]:**
   - Jede Drehung des R^4 ist P -> L P R mit Einheitsquaternionen L, R, eindeutig bis auf das Vorzeichen des Paars.
   - Links- und Rechtsmultiplikation "rotating all half-lines originating from O through the same angle; such rotations
     are denoted as isoclinic".
   - Mit Q = cos alpha + i sin alpha dreht M_L in beiden Koordinatenebenen 1I und JK um alpha. M_R dreht in 1I um alpha
     und in JK um -alpha.
   - "Synchrones Drehen in zwei Ebenen" ist also genau eine links-isokline Drehung; gegensinnig ist sie
     rechts-isoklin.
2. **Hopf-Fasern [L]:** Die Bahnen einer isoklinen Drehung auf S^3 sind Grosskreise, je zwei einmal verschlungen. Die
   Hopf-Abbildung S^3 -> S^2 ist laengs der Bahnen konstant.
3. **SU(2) [S Staley; M]:** Einheitsquaternionen = SU(2) = S^3. Die Abbildung v -> q v q-quer gibt SO(3) zweifach;
   die 2-pi-Drehung ist q = -1.
4. **Physikalische Lesart [ES]:**
   - Ein zweikomponentiges komplexes Feld (z_1, z_2) mit gemeinsamer Phase e^(i omega t) dreht isoklin im
     vierdimensionalen Feldraum.
   - Seine Projektion n = z^dagger sigma z auf S^2 steht still. Das ist die "isospinning texture" aus SPIN-HOPF-L bzw.
     der B.5-Aufbau (C x S^2) im Projekt.
   - Verschiedene Geschwindigkeiten (omega_1 ungleich omega_2) sind eine nicht-isokline Doppeldrehung. Ihre
     Schwebung |omega_1 - omega_2| tauscht Ladung bzw. Isospin zwischen den Komponenten.
5. **Projektbezug:**
   - QB-BS-2D: drehender Knoten plus Q-Ball nicht gebunden, 8 bis 24 % ueber getrennt [Projekt].
   - SPIN-HOPF-L: isospinning Hopf-Solitonen sind Literatur; ungerade Hopf-Ladung darf fermionisch quantisiert werden
     [Projekt, dort S].
   - Codex B.5.
6. **Ableitbarkeitsprobe fuer SYNCHRON-QBALL-1 (nur Vorschlag, nicht gerechnet):**
   - (a) Dublett mit SU(2)-symmetrischem Potential V(|z_1|^2 + |z_2|^2), isokline Drehung: Der Dublett-Q-Ball ist eine
     SU(2)-Drehung des einkomponentigen. Gleiche Energie, eine entartete S^2-Familie von Isospin-Richtungen.
     **Vollstaendig ableitbar [M].**
   - (b) Nicht-isoklin im selben Potential: Ein Zustand ist nur stationaer, wenn eine Komponente verschwindet; sonst
     praezediert der Isospin mit |omega_1 - omega_2|. **Aus der Symmetrie ableitbar [M].**
   - (c) Kopplung lambda |z_1|^2 |z_2|^2 bricht SU(2) zu U(1) x U(1): Zweiladungs-Q-Baelle; gemischt oder getrennt
     haengt am Vorzeichen von lambda gegen den SU(2)-Punkt. **Im Duennwand-Bild weitgehend ableitbar; zweifeldrige
     nichttopologische Solitonen sind Literatur [L Friedberg/Lee/Sirlin 1976].**
   - (d) **Nicht ableitbar, kann scheitern [H]:** ein Verbund aus einem links- und einem rechts-isoklinen
     Dublett-Q-Ball (in einer Ebene gegensinnig), also ein ladungstauschender Q-Ball mit zwei Komponenten. Frage: lebt
     er laenger als 10^3 Eigenperioden, und tauscht er nur in einer Komponente? Vor einer Karte braucht es einen
     Literaturabruf (Folgearbeiten zu Copeland/Saffin/Zhou [L?]).
   - **Empfehlung:** (a) bis (c) nicht rechnen. (d) erst nach Literaturpruefung, und nur mit Bezug zu einer Frage des
     Projekts (QB-BS-2D zeigte keine Bindung; ein ladungstauschender Verbund waere eine andere Art von "Teilchen").

## 5. Kartenvorschlaege (hoechstens zwei, je Lauf <= 10 min)

1. **FK-RINGKETTE-1 [H], niedrige Prioritaet:** Finns Topologie als Kette (Nabe plus drei Ringe) mit Rastpotential je
   Spalt, Drehfedern und Ausweichfreiheitsgrad z je Ring; quasistatische Drehmomentrampe an der Nabe, eben gegen frei.
   - Messgroessen: Zahl und Reihenfolge der Durchrutscher (einzeln als Kinks oder als Lawine) und der erreichbare
     Gesamtwinkel bei fester Energie.
   - Ableitbarkeitsprobe: Fuer einen Ring folgt alles aus 1.3 (B_eff, phi_max), also nicht rechnen. Bei drei Ringen
     haengt die Reihenfolge an den Steifigkeitsverhaeltnissen. Die ist rechenbar, aber vorhersagbar, sobald diese
     Verhaeltnisse fest sind. Physikwert gering; nur als Anschauung fuer Finn.
2. **SYNCHRON-QBALL-1 (d) [H]:** siehe 4.6 (d); erst nach einem Literaturabruf.
- Fuer halben Spin im Netz stehen die Vorschlaege in GUERTEL-1/ERGEBNIS.md ("Grundsaetzlich").

## Einfach gesagt

Finns Federring ist ein Drehteil aus Kunststoff: Federn halten die Ringe zusammen, kleine Nasen lassen sie nur an
bestimmten Stellen einrasten. Liegt das Teil flach, sperren die Nasen. Schwebt es frei, koennen die Ringe ein wenig nach
oben oder unten ausweichen und so ueber die Nasen hinweg weiterdrehen, bis die Federn gespannt sind. Dahinter steckt
eine allgemeine Regel: Eine dritte Richtung zum Ausweichen loest viele Sperren, aber nicht alle. Beim Guerteltrick
bleibt genau ein Rest uebrig, naemlich ob man eine ungerade oder gerade Zahl von Umdrehungen gemacht hat. In GUERTEL-1
haben wir das nachgerechnet: Im Raum ist Verdrehen etwa 65-mal billiger als flach, aber das Entwirren nach zwei
Umdrehungen fand die Rechnung nicht von selbst; der Knoten rastet stattdessen ruckweise ein, wie Finns Federring.
