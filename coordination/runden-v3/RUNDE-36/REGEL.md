# Die Regel: Was ein Netz braucht, damit sein Minus-Glied genau 1/2 ist (Leitung, Runde 36)

- Leitung claude-primary, geschrieben ab 2026-10-04 01:27:31 CEST (date).
- **Anlass, Finn ~01:25:** "Bau die Regel". Bezug sind TENSOR-EIS-N und LAMBDA-1:
  - Ein Erhaltungsregel-Netz zieht gleiche Massen nach Newton an, wenn ein Spurglied das Minuszeichen traegt.
  - Stabil ist es nur bei genau c = 1/2.
  - Dazu braucht es eine Regel, die diesen Regler festhaelt.
- Kennzeichen: [M] Mathematik (hier gerechnet bzw. aus LAMBDA-1), [E] Projektergebnis, [L] Literatur aus dem Gedaechtnis,
  [H] Hypothese.

## 1. Die Regel in einem Satz

**Ein Spannungsmuster, das nur die "Kruemmung" einer einzigen Zahl pro Knoten ist, kostet keine Energie.**

- Formal: Die Netzenergie bleibt gleich, wenn man die Spannung E^ij an jeder Stelle um (delta_ij d^2 - d_i d_j) f_0
  verschiebt, fuer jede Knotenzahl f_0 (Gu/Wen Gl. 23). Das ist die Eichsymmetrie, die die Massenregel R^ii = 0 erzeugt.

## 2. Warum sie genau c = 1/2 festlegt [M]

- Kinetische Energie E^ij E_ij - c (E^ii)^2. Unter E -> E + (delta d^2 - d d) f_0 aendert sie sich um 2 (1 - 2c) E^ii
  d^2 f_0, wenn das Vektor-Gauss-Gesetz d_i E^ij = 0 gilt.
  - Der Zusatzterm E^ij d_i d_j f_0 faellt durch partielle Summation weg.
  - Die Aenderung verschwindet fuer jede Wahl genau dann, wenn c = 1/2.
  - LAMBDA-1 hat das auf dem Gitter gemessen: Invarianzdefekt 8,4e-16 bei c = 1/2, sonst ~ abs(1 - 2c).
- **Gleichwertig:** Fuer quellenfreie Spannung zerfaellt E in einen spurfreien, quellenfreien Teil E_TT und genau das
  Kruemmungsmuster. Dann gilt |E|^2 - (1/2)(E^ii)^2 = |E_TT|^2 [M].
  - Bei c = 1/2 kostet also nur der Gravitationswellen-Teil Energie. Das Kruemmungsmuster ist reine Umbenennung.
- **In der ART** ist das die Spur der allgemeinen Kovarianz [L]: Die Hamilton-Bedingung erzeugt die Umbenennung der Zeit;
  der Koeffizient 1/(d - 1) = 1/2 der DeWitt-Supermetrik folgt daraus. In Hořavas Sprache ist es lambda = 1.

## 3. Zwei Wege, die Regel in Finns Netz einzubauen

### Weg A: Striche sind Laengen (Regge)

- Verschiebt man die Knoten eines flachen Netzes, aendert sich die Form nicht, nur die Beschriftung. Das ist die
  Umbenennung von selbst.
- Die Regel ist dann eingebaut, nicht aufgesetzt (Rocek/Williams: 4 Nullmoden je Ecke = Eichung [S, Dossier]).
- REGGE-4D-1 laeuft gerade und prueft, ob der Minus-Modus dort von selbst den richtigen Faktor (-2 gegen Spin 2, also
  c = 1/2) hat.
- **Grenze [L]:** Auf gekruemmtem Hintergrund ist diese Umbenennung im Regge-Netz nur naeherungsweise erhalten (bekanntes
  Problem der Gitter-Diffeomorphismen).

### Weg B: Striche tragen Kraftfluss (Gu/Wen, Tensor-Eis)

- Die Regel muss hier als zweite Eichsymmetrie gefordert werden: Netzenergie nur aus E_TT bzw. invariant unter Gl. 23.
- Daraus folgt c = 1/2 zwingend.
- Ohne die Regel braucht ein Netz mit c ungleich 1/2 eine Zusatzbedingung E_T = 0 (LAMBDA-1: die Massenregel wird zweiter
  Klasse). Das ist die nicht projizierbare Hořava-Fassung, die um zeitabhaengige Hintergruende instabil wird [S nach
  LAMBDA-1].

## 4. Die zweite Haelfte der Regel: was als Masse zaehlt

- Fuer Schwerkraft muss die Verletzung der Massenregel die **Energiedichte** der Materie sein, nicht eine abzaehlbare
  Ladung: R^ii = 16 pi G rho_E.
- Und die Materie muss das Feld ueber ihre Energie spueren (Kopplung an h_00, LAPSE-0).
  - Dann fallen alle Klumpen gleich (Aequivalenzprinzip).

## 5. Was offen bleibt [H]

1. **Exakte Lorentz-Invarianz:** Licht und Materie muessen denselben Lichtkegel haben (AETHER-UHR-1, Carlip).
2. **Nichtlinear:** Die Regeln muessen auch bei starken Feldern zusammenpassen (geschlossene Algebra der Umbenennungen).
   Auf Gittern ist das ein bekanntes, ungeloestes Problem [L].
3. **Finns Tetraedergitter:** Dort entsteht von selbst eher eine Rang-2-Theorie mit Vektorladung (Yan u. a. [S]), nicht
   die Gu/Wen-Massenregel. Die Regel muesste also eigens gebaut werden.

## 6. Rechentest: REGEL-1 (startet beim naechsten freien Platz)

- Gu/Wen-Gitter (Code TENSOR-EIS-N und LAMBDA-1) mit **eingebauter Regel**: kinetische Energie nur aus E_TT, ohne
  Strafterme.
- Dazu Materie: Die Massenregel wird von der Energiedichte zweier Q-Baelle gespeist (statisch).
- Gemessen:
  - Zahl und Dispersion der laufenden Moden (2 Gravitationswellen-Polarisationen, omega ~ k?)
  - Stabilitaet
  - Anziehung zweier Q-Baelle ~ E1 E2/r
  - Gleiches Fallen zweier verschieden aufgebauter Q-Baelle (Q = 50 gegen Q = 500, verschiedenes E/Q) im Feld eines
    dritten, auf 1e-3

## 7. Woher die 1/2 kommt (Finn ~01:29: "ist das 1/2 vllt die Mitte zwischen 1 und 0 bei einem Übergang bzw das gaussche mittel?"; eingetragen 2026-10-04 01:28:45 CEST)

- **Rechnung in d Raumdimensionen [M]:**
  - Unter E -> E + (delta d^2 - d d) f_0 ist die Spur der Aenderung (d - 1) d^2 f_0.
  - Also aendert sich E^ij E_ij - c (E^ii)^2 um 2 E^ii d^2 f_0 (1 - c (d - 1)).
  - Invariant genau fuer c = 1/(d - 1).
- **Bedeutung:** Das Kruemmungsmuster ist im Fourierraum ~ k^2 mal der Querprojektor delta_ij - k_i k_j/k^2. Dessen Spur ist
  d - 1, die Zahl der Richtungen senkrecht zur Wellenrichtung.
  - Die 1/2 ist also der Kehrwert der Zahl der Querrichtungen (2 im Raum). Gleichwertig ist sie der Mittelwert von cos^2
    ueber die Querebene (ueber einen Kreis gemittelt = 1/2).
  - Ein Mittel ist sie also, aber ueber Richtungen, nicht zwischen 0 und 1.
- **Dimensionskette:**
  - Linie (d = 1): 1/(d - 1) unendlich, die Regel ist nicht erfuellbar. In 1+1 Dimensionen ist Einsteins Theorie leer [L].
  - Flaeche (d = 2): c = 1; keine spurfreien quellenfreien Tensoren, also keine Schwerewellen (Kegel ohne Kraft) [L].
  - Raum (d = 3): c = 1/2, Wellen und Newton.
  - d = 4: c = 1/3.
- **Uebergang:** Ja, im Sinn von LAMBDA-1. Unter 1/2 ist der Zusatzmodus instabil, ueber 1/2 ein Geist. Genau bei 1/2 wird er
  zur kostenlosen Umbenennung, also der Kipppunkt zwischen zwei schlechten Bereichen. Seine Lage legt die Geometrie fest
  (Querrichtungen), nicht die Mitte von 0 und 1.
- **Der zweite besondere Wert** ist 1/d = 1/3, der Mittelwert von cos^2 ueber alle drei Richtungen. Dort zaehlt nur der
  spurfreie Teil (Hořava lambda -> unendlich). Einstein ist 1/2, nicht 1/3.

### Berichtigung zu Abschnitt 7, Linie (Leitung, eingetragen 2026-10-04 01:45:30 CEST)

- Der Satz "Linie (d = 1): 1/(d - 1) unendlich, die Regel ist nicht erfuellbar" ist falsch. Beim Bau der Anschauungsseite
  selbst gefunden.
- **Richtig [M]:** In d = 1 ist das Kruemmungsmuster (delta d^2 - d d) f_0 identisch null (der Querprojektor hat Spur 0).
  - Die Umbenennung ist also leer, und die Energie bleibt fuer jedes c gleich.
  - Die Regel verlangt dort nichts; c bleibt frei.
  - Die Bedingung 1 - c (d - 1) = 0 setzt eine nicht leere Umbenennung voraus.
- Unveraendert gilt: Einsteins Theorie ist in 1+1 Dimensionen leer [L].
- Dieselbe falsche Aussage stand in der Chat-Antwort an Finn (Punkt 3) und wird dort berichtigt.
- **Zusatz [M]:** Im Laengen-Bild ist das Verhaeltnis konformer Modus zu Spin 2 gleich -(D - 2) = -(d - 1) = -1/c.
  - REGGE-4D-1: -2 (d = 3); 3D-Kontrolle: -1 (d = 2).

## 8. Die Regel heisst: Zeit umbenennen ist frei (Leitung, Schreibtisch nach REGEL-1; eingetragen 2026-10-04 02:26:10 CEST)

- **Zuordnung [L: lineares ADM um flachen Raum]:**
  - Die linearisierte Hamilton-Bedingung ist R^(3) = d_i d_j h_ij - d^2 h_ii. Das ist genau die Gu/Wen-Massenregel R^ii.
    h_ij ist die Raummetrik, E^ij ihr Impuls pi^ij.
  - Der Lapse N (wie schnell an jedem Ort die Zeit weiterlaeuft) multipliziert diese Bedingung. Er verschiebt den Impuls
    um (d^i d^j - delta^ij d^2) N.
  - Das ist Gu/Wen Gl. 23 mit f_0 = N [M, Abgleich der Leitung].
- **Also [M]:** "Ein Kruemmungsmuster kostet nichts" bedeutet: Wie schnell an jedem Ort die Zeit weiterlaeuft, ist frei
  waehlbar. c = 1/2 ist die Bedingung, dass die Bewegungsenergie diese Freiheit respektiert.
- **Zweite Haelfte [L]:** Mit Materie wird die Bedingung zu R^(3) = 16 pi G rho. Die Bedingung erzeugt die
  Zeitentwicklung des ganzen Systems, und fuer Materie ist das ihre Energiedichte (Hamilton-Dichte).
  - Respektiert auch die Materie die freie Zeitumbenennung, muss also ihre Energie die Quelle sein.
  - Damit sind beide Haelften der Regel (c = 1/2 und Energie als Quelle, also gleiches Fallen) dieselbe Symmetrie [H/M].
  - REGEL-1 hat beide eingegeben. Das erklaert, warum es zusammen funktioniert, nicht, warum ein Netz es tut.
- **Was ein Raum-Netz mit aeusserer Uhr von selbst gaebe [M, Rechnung der Leitung]:**
  - Annahme: Jede Kante hat eigene Bewegungsenergie ~ ldot_e^2, die Kantenrichtungen sind gleichverteilt, und
    delta l/l = (n.h.n)/2.
  - Dann ist die Bewegungsenergie ~ <(n.hdot.n)^2> = (2 tr(hdot^2) + (tr hdot)^2)/15 (mit <n_i n_j n_k n_l> = Summe
    der drei delta-Paare/15).
  - In Horavas Form K_ij K^ij - lambda K^2 ist das lambda = -1/2, also c = lambda/(3 lambda - 1) = 1/5, weit weg von 1/2.
  - Nach LAMBDA-1 ist das instabil, sobald das Netz eine Regge-artige Kruemmungsenergie hat. Bei reiner Elastizitaet gibt
    es keine Schwerkraft (LAST-1).
- **Folge fuer Finns Bild [H]:**
  - Ein Raum-Netz, das in einer aeusseren Zeit lebt, hat die Zeit-Umbenennung nicht von selbst. Es landet nicht bei 1/2
    (Horava-Problem), zeichnet ein Ruhesystem aus (ZUFALLS-REIBUNG-1) und braucht einen gemeinsamen Lichtkegel
    (AETHER-UHR-1).
  - Ein Raumzeit-Netz (Laengen in 4D, REGGE-4D-1) hat sie eingebaut.
  - Die Rechnungen sprechen also fuer ein Netz in Raum und Zeit statt eines Raum-Netzes mit aeusserer Uhr.
