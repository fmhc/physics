# Strich-Schalter, gerichtetes Dreieck, atmende Punkte (Schreibtisch der Leitung, Runde 42)

- Leitung claude-primary, geschrieben ab 2026-10-04 17:50:44 CEST (date). Nicht gegengelesen.

## BERICHTIGUNG nach SCHREIBTISCH-LESER (eingetragen 2026-10-04 18:45:23 CEST; RUNDE-37/schreibtisch-leser/GEGENLESEN.md)

- **A1, Teil E faellt:**
  - Bei gleich starker Huellen-Kopplung auf den fuenf Rautenkanten ist der Grundzustand nicht das 120-Grad-Muster. Er
    ist A = B, C = D, und C/D gegenphasig zu A/B (E = cos theta - 4 |cos(theta/2)|: -3 J gegen -2,5 J).
  - Das 120-Grad-Muster ist nicht einmal stationaer. Es gibt also keine Laufrichtung der Atemwelle und keine
    gegenlaeufigen Umlaeufe.
  - Finns Skizze ist **nicht** der Grundzustand.
  - 120 Grad entstuende erst bei doppelt so starker Scharnier-Kopplung (zum Beispiel Seitenpunkte mit halber Amplitude)
    [M, Leser].
  - Im geschlossenen Tetraeder tragen dann alle sechs Staebe denselben Betrag; "das Gegenteil von Finns Kraftbild"
    faellt.
- **A2, C1 zu stark:**
  - lambda = 2d/(3 phi) gilt fuer zufaellige, sich ueberlappende Kugeln. Fuer harte Kugeln gilt
    lambda = 2d(1 - phi)/(3 phi), bei phi = 0,64 also 0,375 d.
  - "Sieht nur seine Beruehrungsnachbarn" ist zu stark: Die Nachbarn decken etwa 40 % (6 Kontakte) bis 80 % (12) des
    Himmels.
- **A3, B2 fuer Phasen falsch:** Taktphasen 0, 120 und 240 Grad um ein Dreieck ergeben eine volle Windung (Phasenwirbel).
  Ein Umlauf ist fuer Winkelgroessen also auch ohne eigenen Kantenwert moeglich, aber nur in ganzen Vielfachen von
  2 pi. Fuer reelle Groessen wie Tiefe oder Potential bleibt B2 richtig.
- **B-Befunde (Auswahl):**
  - N8 (Garriga/Tanaka) gilt nur ohne Radion-Stabilisierung; in dieser Fassung schliesst Cassini sie ganz aus.
  - "Nur in 3D ist das Newton" ist irrefuehrend.
  - Bei Pushmepullyou fehlt die Abstandsaenderung.
  - "Faltwinkel" heisst besser "Diederwinkel".
  - Die Cristobalit-Waermeaussage ist [L?].
- **Literatur des Lesers:** Zhang/Fodor bestaetigt (arXiv 2208.06831, PRL 131, 238302); Moessner/Chalker nur teilweise
  ("kollinear" bleibt [L?]).
- **Finn, Nachricht 1 (zwischen 17:40 und 17:42), woertlich:** "und wenn punkte linien und dreiecke formen dann müsste es ja
  auch einen switch in 2d von linien geben wenn die überlagern. wenn man die dicker oder so darstellt an einer seite, dann
  könnte man daraus ein gerichtetes/gewichtetes dreieck machen right?"
- **Finn, Nachricht 2 (zwischen 17:42 und 17:46), woertlich:** "udn wenn punkte einen durchmesser von PU haben, wie verhalten
  sich dann perspektiven aus einem punkt zu anderen punkten. nehmen wir an das punkte auch miteinander viben können vllt -
  und jeder punkt mit anderen punkten koppelt der im gleichen takt läuft (sinus welle einfach) was für pumpenden konstrukte
  werden dann daraus wenn die aneinander koppeln können an ihrer hülle und damit "atmen" und einen takt erzeugen?"
- ~~**Lesart "PU":** Planck-Einheit [Annahme der Leitung].~~ **PU, Finn (zwischen 17:55 und 17:57), woertlich:** "PU ist
  meine eigene Punkt Unit einheit mit der wir rechnen können mal auf punkt ebene". Der Punktdurchmesser ist die Einheit,
  d = 1 PU. Alle Aussagen unten haengen nur vom Verhaeltnis Abstand zu Durchmesser ab; mit d = 1 PU gilt zum Beispiel
  lambda = 2/(3 phi) PU. Weiterfuehrung als Rechenkarte: RUNDE-37/atem-netz-1/KARTE.md (dort auch: Kopplung an der Huelle
  gibt im Mittel Gegentakt, nicht Gleichtakt [M]).
- **Kennzeichen:** [M] eigene Mathematik (Schreibtisch), [L] Gedaechtnis, [L?] unsicher, [P] Projektdatei, [E] Messung im
  Modell, [H] Hypothese.
- **Regel Dimensionsvergleich (AGENTS.md, Finn 04.10.):** je Teil getrennt ausgewiesen.
- **Projekt-grep (17:46 bis 17:50):**
  - Kreuzungszahlen: STRICH-NETZ-1, 3286 Kreuzungen je Ansicht bei 20 Punkten.
  - Bjerknes: laser-experimente-20260928/BERICHT-LASER.md Z. 166 [S].
  - Birkhoff: RUNDE-14/q-stern2/ERGEBNIS.md Z. 279 [L?].
  - Eshelby: RUNDE-17.md Z. 393; RUNDE-34/TETRAEDER-ANALYSE.md Z. 20.
  - Q-Baelle verschmelzen gleichphasig: RUNDE-02/AUFTRAG-1D-TESTS.md Z. 31.
  - Kein Treffer zu Schwimmern mit Formwechsel (Shapere/Wilczek, Najafi/Golestanian) und zu "pulsating active matter".

## Teil A: Der Schalter beim Ueberlagern

**A1. Satz [M]: Das Kreuzungsvorzeichen ist die Haendigkeit eines Tetraeders.**
- Zwei gerichtete Striche a->b und c->d in 3D, die sich nicht schneiden. In jeder Blickrichtung, in der sie sich in der
  Ansicht kreuzen, hat die Kreuzung dasselbe Vorzeichen (rechtshaendig +1, linkshaendig -1).
- Dieses Vorzeichen ist das Vorzeichen von det[b-a, c-a, d-a], also die Orientierung (Auf/Ab) des Tetraeders aus den vier
  Endpunkten. Das gilt auch von der Gegenseite, weil dort oben/unten und Spiegelbild zugleich wechseln.
- Herleitung: p auf ab und q auf cd fallen in der Ansicht zusammen, q - p = lambda n. Vorzeichen =
  sign(((d-c) x (b-a)) . (q-p)) in beiden Faellen von lambda; die Anteile entlang der Striche fallen heraus. Es bleibt
  sign det[d-c, b-a, c-a] = sign det[b-a, c-a, d-a].
- Probe: a = (0,0,0), b = (1,0,0), c = (1/2,-1/2,1), d = (1/2,1/2,1). Die Determinante ist -1; die Kreuzung von oben
  und von unten ist ebenfalls -1.
- Folge: Der 2D-Schalter speichert 3D-Haendigkeit. Bei 20 Zufallspunkten traegt jede der rund 3286 Kreuzungen je Ansicht
  [E, STRICH-NETZ-1] das Vorzeichen ihres Tetraeders. Im Zufallshaufen sind beide Vorzeichen gleich haeufig
  (Spiegelsymmetrie) [M].
- Bekannt [L]: Gauss' Verschlingungszahl geschlossener Polygone ist die Haelfte der Summe dieser Vorzeichen, aus jeder
  Richtung gleich.

**A2. Dimensionsvergleich [M, Skizze]:**

| Raum | Was "schaltet" in der Ansicht | Vorzeichen |
|---|---|---|
| 2D (Punkte in der Ebene, keine Ansicht) | Striche schneiden sich wirklich; es gibt kein oben/unten | Umlaufsinn des Dreiecks aus 3 Punkten |
| 3D, gesehen in 2D | Strich gegen Strich | Tetraeder aus 4 Punkten (A1) |
| 4D, gesehen in 3D | Strich gegen Dreieck (zwei Striche verfehlen sich in 3D) | Orientierung des 4-Simplex aus 5 Punkten |

- Allgemein schalten in der Ansicht eines D-Raums Teile, deren Dimensionen zusammen D - 1 ergeben. Das Vorzeichen ist die
  Orientierung des D-Simplex.

## Teil B: Gerichtetes und gewichtetes Dreieck

**B1. Lesart "dicker an einem Ende" = Pfeil mit Gewicht [M, L]:**
- Jede Kante traegt einen Wert w_ij = -w_ji. Um das Dreieck ergibt sich ein Umlauf Gamma = w_ab + w_bc + w_ca, der
  "Fluss durch das Dreieck".
- Das ist das Grundobjekt der Gittereichtheorie: Linkvariable und Plakette [L]. Von den drei Kantenwerten sind zwei
  Gefaelle zwischen Punkten und einer Umlauf.

**B2. Haken [M]:** **[A3 des Lesers: fuer Phasen falsch, siehe BERICHTIGUNG oben]**
- Kommt die Dicke aus einer Groesse der Punkte selbst (Tiefe zum Betrachter, Potential, Taktphase je Punkt), dann gilt
  w_ij = f_j - f_i, und Gamma = 0 in jedem Dreieck. Das Dreieck ist gerichtet, hat aber keinen Umlauf.
- Die Perspektiv-Dicke (nah = dick) ist genau so ein Fall.
- Derselbe Befund wie in GLUONEN-L V2 (Verdrehung O_i^-1 O_j, Ringprodukt 1) und KOPPLUNG-TETRA-1 (Ring-Holonomie kostet
  nichts).
- Einen Umlauf gibt es nur mit einem eigenen Wert je Kante.

**B3. Anschluss [E, P]:**
- DREIECK-TAKT-1: In 2D gibt ein Umlauf (Takt-Drehsinn im Dreieck) einseitige Randwellen mit Richtung nach dem Drehsinn (die Umkehr mit dem Drehsinn ist durch die Zeitumkehr erzwungen und bekannt, Kitagawa u. a.).
- In 3D hat ein streng lokaler Takt W3 = 0. WINDUNG-LESER: haelt (Read 2017), Geltungsbereich unitaer, freie Teilchen, translationsinvariant, im Volumen.

**B4. Lesart "dicker an einer Laengsseite" = Band mit markierter Kante:**
- Fuer geschlossene Baender gilt Lk = Tw + Wr (Calugareanu/White/Fuller) [L].
- Die Verwindung Wr ist das Mittel der Kreuzungsvorzeichen ueber alle Blickrichtungen ("von allen Seiten anschauen") [L].
- Auf solchen Baendern lebt der Guertel-Trick (GUERTEL-1, GUERTEL-2 laeuft).

**B5. Dimensionsvergleich [M, L]:**
- In 2D ist der Umlauf je Dreieck eine Zahl.
- In 3D bilden die Umlaeufe ein Feld (wie B). Die Summe ueber die vier Flaechen eines Tetraeders ist null, solange die
  Werte auf Kanten sitzen (keine Monopole).
- Fuer Gluonen (SU(3)) wird jeder Kantenwert eine 3x3-Matrix, und der Umlauf haengt von der Reihenfolge ab (GLUONEN-L).

## Teil C: Punkte mit Durchmesser d

**C1. Blick aus einem Punkt [M]:** **[A2 des Lesers: zu stark, siehe BERICHTIGUNG oben]**
- Ein Nachbar im Abstand r erscheint unter dem Winkel ~ d/r.
- Bei Fuellgrad phi endet eine Sichtlinie im Mittel nach lambda = 2d/(3 phi). Dichteste Zufallspackung phi ~ 0,64 [L]
  gibt lambda ~ 1,04 d; bei phi = 0,01 sind es ~ 67 d.
- Der bedeckte Himmelsanteil bis zum Abstand R ist 1 - exp(-R/lambda) (Olbers).
- Im dichten Netz sieht jeder Punkt nur seine Beruehrungsnachbarn, alles Weitere muss ueber das Netz laufen:
  Lokalitaet aus Verdeckung.

**C2. Dimensionsvergleich [M]:**
- lambda = (d/2) V_D / (V_(D-1) phi).
- 1D: d/phi; man sieht genau die zwei Nachbarn.
- 2D: pi d/(4 phi).
- 3D: 2d/(3 phi).
- 4D: 3 pi d/(16 phi).

## Teil D: Atmende Punkte im gleichen Takt

**D1. Gleichtakt ueber ein Medium (Finns "Tuch"): Anziehung [L, P]:**
- Gleichphasig pulsierende Kugeln in einer Fluessigkeit ziehen sich an, gegenphasige stossen sich ab (Bjerknes, 1870er)
  [L; Projekt BERICHT-LASER Z. 166 S].
- Im inkompressiblen Medium faellt die gemittelte Kraft wie 1/r^2 ab. Bjerknes hat das als Modell der Schwerkraft
  betrachtet [L].
- Q-Baelle zeigen dasselbe Muster: gleichphasige verschmelzen [P, RUNDE-02].
- Dimension: Die Kraft faellt wie 1/r^(D-1), also 1/r in 2D, 1/r^2 in 3D und 1/r^3 in 4D. Nur in 3D ist das Newton.

**D2. Haken: Volumenatmen ist Spin 0 [L]:**
- Ein Skalar lenkt Licht falsch ab; die Nordstroem-Theorie gibt gar keine Ablenkung.
- In der ART strahlt eine kugelfoermig atmende Masse nichts ab (Birkhoff) [L?; Projekt RUNDE-14].
- Schwerkraftwellen brauchen Quadrupol-Atmen: in eine Richtung quetschen, in die andere dehnen. Das passt zur
  Spin-2-Frage des Projekts.
- Dimension: Gravitonpolarisationen D(D-3)/2 bei Raumzeit-Dimension D, also 0 in 2+1, 2 in 3+1 und 5 in 4+1.

**D3. Elastisches Netz statt Fluessigkeit [L, P]:**
- Zwei ruhend atmende Punkte (Dilatationszentren) wechselwirken im isotropen elastischen Medium in erster Ordnung gar nicht
  (Eshelby) [L; Projekt RUNDE-17, RUNDE-34].
- Wechselwirkung entsteht erst durch Anisotropie (Kristall, ~ 1/r^3 mit Winkelgang), durch Raender oder durch Dynamik (die
  Bjerknes-Kraft ist eine Traegheitskraft der Stroemung).

**D4. Pumpen braucht einen Phasenversatz [L]:**
- Gleichtakt allein pumpt nichts: Hin-und-her-Atmen gibt bei kleiner Reynoldszahl keinen Netto-Transport
  (Purcell-Muscheltheorem).
- Netto-Pumpen braucht mindestens zwei Formfreiheiten mit Phasenversatz. Beispiele: drei Kugeln (Najafi/Golestanian 2004)
  und zwei atmende Kugeln, die Volumen tauschen ("pushmepullyou", Avron u. a. 2005).
- Die Strecke je Zyklus ist der Fluss einer Eichkruemmung durch die Flaeche, die der Zyklus im Formraum umlaeuft
  (Shapere/Wilczek 1987/89). Damit ist es wieder ein Umlauf wie in Teil B.
- Spielzeug [E, tetra-ticks]:
  - Gleichtakt 4:0 gibt keinen Netto-Drehimpuls.
  - Versetzte Takte drehen.
  - Sequentiell gibt es eine kleine Ratsche (0,0061).

**D5. Kopplung nur an der Huelle, ohne Medium [L?]:**
- Kurzreichweitig. Synchronisation laeuft ueber Beruehrung (Kuramoto-artig), dazu Wellen und Spiralen, ohne 1/r^2.
- Modell "pulsating active matter" (Zhang/Fodor 2023) [L?, an der Quelle pruefen].

## Bewertung der Leitung [ES]

1. **Abgeleitet bzw. Literatur, keine Karte noetig:**
   - A1, A2 (Schalter = Haendigkeit)
   - B1, B2 (Umlauf nur mit eigenem Kantenwert)
   - C1, C2 (Lokalitaet aus Verdeckung)
   - D1, D2, D4
2. **Offen und rechenbar [H]:** Wie wechselwirken zwei gleichphasig atmende Punkte in Finns Netz (beta-Cristobalit, mit
   weichen Drehmoden), und welches Abstandsgesetz und Vorzeichen gilt?
   - Vergleichspunkte: Eshelby-Null (isotrop, ruhend) und Bjerknes 1/r^2 (Fluessigkeit, dynamisch).
   - Formt ein Haufen mit zufaelligen Startphasen einen gemeinsamen Takt, und pumpt ein Phasenversatz im Netz in eine
     Richtung?
   - Moegliche Karte ATEM-NETZ-1, sobald ein Rechenplatz frei ist; vorher Ableitbarkeitsprobe (Gitter-Greenfunktion
     liefert den ruhenden Teil).
3. **Keine Gravitationsaussage:** Volumenatmen bleibt Spin 0 (D2). Fuer Spin 2 muesste das Netz quadrupolar atmen.

## [FAELLT, A1 des Lesers, siehe BERICHTIGUNG oben] Teil E: Finns Raute aus zwei Dreiecken mit atmenden Ecken (nachgetragen 2026-10-04 18:18:56 CEST)

- **Finn (zwischen 18:13 und 18:16), woertlich:** "also vllt dann die connection dings mit dem radius 1PU vom punkt dazu der
  auf sinus atmet."
  - Dazu die Skizze RUNDE-42/finn-skizze-raute-20261004.png:
    - oben zwei Dreiecke mit Pfeilen
    - unten eine Raute aus zwei Dreiecken mit gemeinsamer senkrechter Kante (dicker Pfeil nach unten)
    - aussen Pfeile nach oben
    - an den Ecken Kreise verschiedener Groesse
- **Schreibtisch [M] (gemittelte Huellen-Kopplung aus ATEM-NETZ-1, XY-Antiferromagnet):**
  - Ecken: B oben, A unten (gemeinsame Kante), C links, D rechts.
  - Jedes Dreieck will 120 Grad. Aus psi_A = 0 und psi_B = 120 Grad folgt psi_C = psi_D = 240 Grad (die einzige Richtung,
    die zu beiden 120 Grad hat). **C und D atmen im Gleichtakt**; in der Skizze sind beide Seitenkreise klein.
  - Das Maximum von sin(omega t + psi) kommt bei groesserem psi frueher. Die Atemwelle laeuft also C bzw. D -> B -> A.
  - Links ist der Umlauf C -> B -> A -> C im Uhrzeigersinn, rechts D -> B -> A -> D gegen den Uhrzeigersinn: **gegenlaeufig.**
  - Auf der gemeinsamen Kante laufen beide Wellen von B nach A, also nach unten (Finns dicker Pfeil). Aussen laufen sie
    zurueck nach oben (A -> C -> B und A -> D -> B; Finns duenne Pfeile).
  - **Die Skizze ist genau der gemittelte Grundzustand.**
  - Auf dem ganzen Dreiecksgitter wechselt der Drehsinn von Dreieck zu Dreieck (bekannter 120-Grad-Zustand [L]). Jede Kante
    hat dann eine feste Laufrichtung, und an jedem Knoten fliesst gleich viel hinein wie heraus [M].
- **Im Medium [L, M, H]:**
  - Zwei gegenlaeufige Wirbel mit einem Strahl dazwischen sind ein Wirbelpaar. In 2D-Fluessigkeiten bewegt sich ein solches
    Paar von selbst in Strahlrichtung (Tempo Gamma/(2 pi d)); in 3D entspricht dem ein Wirbelring (Rauchring) [L].
  - Bjerknes (gemittelt) [L, M]:
    - Gleichtakt-Paare ziehen sich an (C-D).
    - 120-Grad-Paare stossen sich schwach ab (cos 120 Grad = -1/2).
    - In 3D will sich die Raute deshalb um AB falten, bis C und D sich treffen: ein Tetraeder. Bei freiem Scharnier geht
      das bergab, ist also vorab ableitbar [M].
  - Nach dem Schliessen bevorzugt die Huellen-Kopplung auf dem Tetraeder zwei Gegentakt-Paare (C-D gegenphasig). Dann
    stossen sich C und D ab; die Raute koennte sich wieder oeffnen. Ein langsamer, selbst erzeugter Klapptakt waere die
    Folge [H] (Rechenkarte RAUTE-ATEM-1).
- **Dimension:**
  - In 2D kann die Raute nicht falten; C-D-Anziehung staucht sie nur in der Ebene.
  - In 3D kann sie zum Tetraeder falten.
  - In 1D gibt es keine Dreiecke.
