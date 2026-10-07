Urteil: haelt mit Einschraenkung. Teil E (Finns Raute) und die Ableitbarkeitsprobe von RAUTE-ATEM-1 fallen. Vier A-Befunde
(A1 bis A4) sind vor der Weitergabe zu berichtigen. Abgeschlossen 2026-10-04 18:43:02 CEST (date), Dauer 21 min 49 s.

# GEGENLESEN: Schreibtisch-Rechnungen [M] und Literaturangaben [L] der Leitung (Runde 42 / RUNDE-37-Karten)

- Leser: pruefer-opus (Haus Anthropic), frischer Agent, kein Fork, ohne Vorkontext.
- Beginn: 2026-10-04 18:21:13 CEST (date). Zeitbox 50 min, also bis 19:11:13 CEST.
- Auftrag: RUNDE-37/schreibtisch-leser/KARTE.md (sha256 beim Lesen c10ab96a...183d, 50 Zeilen).
- Arbeitsweise: nur gelesen (cat, sed -n, grep, wc, ls, sha256sum, date); alle Zahlen im Kopf mit Rechenweg.
  Keine Laeufe, kein python/awk/perl. arXiv-Abrufe: siehe unten.

## Gesamturteil

**Haelt mit Einschraenkung. Teil E und die Raute-Karte fallen in ihrem Kernsatz.** Vor der Weitergabe in Rundenabschluss
und Journal sind vier A-Befunde zu berichtigen.

| Pruefobjekt | Urteil |
|---|---|
| 1 NEGATIV-LESARTEN | haelt mit Einschraenkung (nur B: Geltungsbereich N8, Rundung N2, Kennzeichen) |
| 2 SCHALTER-UND-ATMEN | A1, C2, D halten; B2 faellt im Wortlaut (A3); C1-Zahl falsch (A2); **E faellt (A1)** |
| 3 ATEM-NETZ-1, Schreibtisch | haelt mit Einschraenkung: Mittelung, Vorzeichen, Gegentakt, Pyrochlor richtig; Gueltigkeit und Ableitbarkeitsprobe falsch (A4) |
| 4 DREIECK-PUMPE-L, Schreibtisch | haelt mit Einschraenkung (nur Wortlaut: B15 bis B18) |
| 5 RAUTE-ATEM-1, Ableitbarkeitsprobe | Statik haelt als Wenn-dann; **Ableitbarkeitsprobe faellt (A1)**: falsches Phasenmuster, danach "Gegenteil von Finns Kraftbild" und "Umordnung nicht ableitbar" |

**Quote der nachgerechneten [M]-Schritte, 32 einzeln gezaehlt:**

- **24 halten:**
  - NEGATIV-LESARTEN: N1-Mechanik, N3-CPT, N4, N9-PT.
  - SCHALTER-UND-ATMEN:
    - A1-Herleitung, A1-Probe, A2 fuer 3D/4D, B1.
    - C2, D1-Dimension, D2-Polarisationen.
    - E: Maximum, Umlaufsinn, Gitterbilanz.
  - ATEM-NETZ-1: Mittelung, Vorzeichen, zweifaerbbar, Pyrochlor.
  - DREIECK-PUMPE-L: Freiheitsgrade, Faltwinkel, Maxwell, 1,5, Defizite.
  - RAUTE-ATEM-1: Statik bedingt.
- **3 halten mit Einschraenkung:** A2-2D-Zeile, B5 (reell), C1-Formel (nur Poisson).
- **5 fallen:**
  - B2 "Gamma = 0" fuer Taktphasen.
  - C1-Zahl und "nur".
  - Raute-Grundzustand 120 Grad.
  - ATEM-Gueltigkeit samt (a)/AN2.
  - RAUTE "Umordnung nicht ableitbar".
- Ergebnis: 24/32 = 75 % halten, 3/32 ~ 9 % mit Einschraenkung, 5/32 ~ 16 % fallen.

**Literatur:**

- 2 von 2 Abrufen bestaetigen die Angabe. Zhang/Fodor ist voll bestaetigt, Moessner/Chalker teilweise ("kollinear" bleibt
  [L?]).
- Kein [L] wird als [S] verkauft.

## Pruefobjekt 1: RUNDE-42/NEGATIV-LESARTEN.md

**Urteil: haelt mit Einschraenkung** (keine A-Befunde; fuenf B-Befunde zu Geltungsbereich und Rundung).

Gelesene Fassung: mtime 18:04:08, 38 Zeilen. Stichprobe der [S]-Angaben gegen RUNDE-37/dunkel-flip-l/DOSSIER.md
(per grep, Zeilen 18 bis 27, 45, 51, 55, 64, 82, 103):

- **N1 Geisterkopie:**
  - Fenster 20 bis 98 Mikrometer steht im Dossier Z. 103 ("lg >= 20 um, Daten lg <= 98 um (95 %); KS: 30 um"),
    Kennzeichen [S] ehrlich.
  - Mechanik selbst nachgerechnet [M]: Mit Aequivalenzprinzip haengt die Beschleunigung nur von der Quellmasse ab.
    - Eine Quelle mit E < 0 stoesst alles ab, eine mit E > 0 zieht alles an.
    - Im gemischten Paar beschleunigen beide in dieselbe Richtung (Bondi-Davonlaufen).
    - Das stimmt mit "stoesst ab, gemischte Paare laufen davon" ueberein.
  - "als Rueckseite, die anzieht, ausgeschlossen" ist ein Vorzeichen-Argument der Theorie, keine Messung (B4).
- **N2 Spiegelwelt:**
  - o-Ps unsichtbar < 4,2e-7: Dossier Z. 95 (Badertscher 2007) und meine Erinnerung [L] stimmen ueberein.
  - PSI 99,98 %: Dossier Z. 18 und 91 [S Abstract].
  - Doppelbrechung: Das Dossier (Z. 22, 55) hat 0,277 +- 0,057 Grad, 4,8 sigma, und "mit Staubschutz 3,5 sigma".
    - Aus den gerundeten Werten der Tabelle folgt 0,28/0,06 = 4,67, also 4,7 sigma, nicht 4,8.
    - Die 3,5-sigma-Fassung fehlt (B2).
  - "Lee/Yang 1956" steht ohne Kennzeichen; laut Dossier Z. 65 nicht gelesen, also [L] (B3).
- **N3 Antiteilchen:**
  - Nachgerechnet [M]: C laesst die Helizitaet, P kehrt sie um, T laesst sie.
  - CPT kehrt sie also um: linkshaendiges Teilchen <-> rechtshaendiges Antiteilchen. [M, L] stimmt.
  - eta ~ 6e-10 [L] plausibel (6,1e-10).
  - ALPHA-g ~25 % [P] plausibel: Erinnerung a_g = (0,75 +- 0,13 +- 0,16) g, Fehler zusammen ~0,21 g.
- **N4:** U psi = e^(-i pi) psi = -psi, also Vorzeichenwechsel je Schritt. Richtig.
- **N5:** Boyle/Finn/Turok 2018 (PRL 121, 251301) [L] plausibel. Die drei Vorhersagen (r ~ 0, leichtestes Neutrino
  masselos, Majorana) entsprechen meiner Erinnerung.
- **N7:** Das Dossier Z. 64 nennt d_DR = 5,11 +- 0,09 (FRG) und d_c ~ 4,2 bis 4,7 (perturbativ). "nur oberhalb d ~ 5,1"
  gibt nur die FRG-Zahl (B5).
- **N8 Garriga/Tanaka:** Das Zitat "light deflection from shadow matter is 25 % weaker" steht im Dossier Z. 45 [S Abstract].
  Dort steht auch der fehlende Geltungsbereich: **ohne Radion-Stabilisierung**, Brans-Dicke mit omega in (-3/2, 0).
  - Nachgerechnet [M]: gamma_PPN = (1 + omega)/(2 + omega).
    - omega -> -3/2 gibt gamma -> -1.
    - omega = -1/2 gibt gamma = 1/3.
    - omega -> 0 gibt gamma -> 1/2.
    - Fuer uns auf der negativen Brane gilt also gamma in (-1, 1/2).
  - Gegen Cassini, gamma - 1 = (2,1 +- 2,3)e-5 [L], ist das nicht "stark begrenzt", sondern ganz ausgeschlossen.
  - Mit Stabilisierung (Goldberger/Wise) gilt die 25-%-Aussage in dieser Form nicht mehr (B1).
  - Nebenbei: Cassini mass die Shapiro-Laufzeit, nicht die Lichtablenkung. gamma regelt beides, "Lichtablenkung gamma" ist
    also nur ungenau.
- **N9:**
  - PT-Paar H = [[i g, k],[k, -i g]] hat Eigenwerte +-sqrt(k^2 - g^2). Unterhalb g = k ist das Spektrum reell, die
    Schwelle liegt bei g = k [M]. "fuer einfache Paare ableitbar" stimmt.
  - 2601.03189 liegt im Scout-Lauf 20261002T200016Z-tick (arxiv-records.jsonl). "nur Titel" ist ehrlich gekennzeichnet.

Wortlaut-Vorschlaege (nur hier, Pruefobjekt unveraendert):

- **N8, Zeile 21:** "Materie auf der anderen Brane zieht an, lenkt Licht aber 25 % schwaecher ab (Garriga/Tanaka, **ohne
  Radion-Stabilisierung**) [S Abstract]. In dieser Fassung gilt auf unserer Brane gamma in (-1, 1/2); Cassini
  (gamma - 1 = (2,1 +- 2,3)e-5) [L] schliesst das aus, es bleibt nur RS1 mit Stabilisierung."
- **N2, Zeile 15:** "0,277 +- 0,057 Grad (4,8 sigma; mit Staubbehandlung 3,5 sigma; Kalibrierung offen) [S, DUNKEL-FLIP-L]".

## Pruefobjekt 2: RUNDE-42/SCHALTER-UND-ATMEN.md (Teile A bis E)

**Urteil: haelt mit Einschraenkung fuer A, C2, D. Faellt in zwei Punkten: Teil E ("Grundzustand") und B2 ("nur").
Dazu ein falscher Zahlenwert in C1.** Gelesene Fassung: mtime 18:18:56, 193 Zeilen.

**A1, Kreuzungsvorzeichen: haelt.** Selbst nachgerechnet [M].

- Konvention: Kreuzung positiv, wenn (u_oben x u_unten) . e_Betrachter > 0. Beim ueblichen Bild der positiven Kreuzung
  laeuft der obere Strich von links unten nach rechts oben: (1,1,0) x (-1,1,0) = (0,0,2).
- Fall 1: q - p = mu v, mit v als Blickrichtung in die Szene und mu > 0. Dann liegt ab oben.
  - Vorzeichen = sign((b-a) x (d-c) . (-v)) = sign((d-c) x (b-a) . (q-p)).
- Fall 2: mu < 0. Dann liegt cd oben.
  - Vorzeichen = sign((d-c) x (b-a) . (-v)), und -v ist parallel zu q - p.
  - Es ergibt sich derselbe Ausdruck wie in Fall 1. Z. 35 stimmt.
- q - p = (c-a) + t(d-c) - s(b-a). Die Anteile entlang d-c und b-a fallen im Spatprodukt weg, es bleibt det[d-c, b-a, c-a].
- Mit d - c = (d-a) - (c-a) wird daraus det[d-a, b-a, c-a]. Das ist eine zyklische Vertauschung, also gerade:
  = det[b-a, c-a, d-a]. Z. 36 stimmt.
- Probe Z. 37:
  - Die Determinante ist 1 * ((-1/2)(1) - (1/2)(1)) = -1.
  - Von oben liegt cd oben: (0,1,0) x (1,0,0) = (0,0,-1), mit e = (0,0,1) also -1.
  - Von unten liegt ab oben: (1,0,0) x (0,1,0) = (0,0,1), mit e = (0,0,-1) also -1. Stimmt.
- Gegenprobe: Vertauscht man die Rollen der Striche, gibt det[d-c, a-c, b-c] die Ordnung (c,d,a,b), eine gerade Permutation.
  Das Vorzeichen ist also symmetrisch, wie es sein muss.
- Das Vorzeichen stimmt auch mit dem Gauss-Integral ueberein: sign((p-q) . ((b-a) x (d-c))) = sign det[b-a, c-a, d-a].
- 3286 Kreuzungen bei 20 Punkten [E] ist plausibel. C(20,4) = 4845 Vierer geben je hoechstens eine Kreuzung, 3286/4845 =
  0,68. Fuer gleichverteilte Punkte im Quadrat waere 1 - 4 * 11/144 = 0,69 zu erwarten.
- B6: Z. 40 "beide Vorzeichen gleich haeufig" gilt nur im Erwartungswert. Vorschlag: "im Mittel gleich haeufig".

**A2, Dimensionsvergleich: haelt mit Einschraenkung (B7).**

- Die allgemeine Regel Z. 53/54 stimmt fuer 3D und 4D: 1 + 1 = 2, 1 + 2 = 3; (p+1) + (q+1) = D + 1 Punkte bilden ein
  D-Simplex. Der Beweis von A1 uebertraegt sich: Die Anteile entlang der Teile fallen aus der 4x4-Determinante heraus.
- Die 2D-Zeile passt aber nicht zur Regel. Nach der Regel waere es "2D, gesehen in 1D: Punkt gegen Strich" (0 + 1 = 1),
  mit dem Umlaufsinn des Dreiecks (Punkt plus Endpunkte).
- Die Tabelle beschreibt stattdessen echte Schnitte ohne Ansicht. Deren Vorzeichen ist sign det[b-a, d-c] = Umlaufsinn
  von (a,b,d) = -Umlaufsinn von (a,b,c).
- Vorschlag: zwei Zeilen, "2D gesehen in 1D: Punkt gegen Strich" und "2D ohne Ansicht: echter Schnitt".

**B1 haelt.** 3 Kantenwerte = 2 Gefaelle (Knoten - 1) + 1 Umlauf.

**B2: faellt im Wortlaut (A3).**

- Z. 65 bis 70 setzen w_ij = f_j - f_i voraus und nennen "Taktphase je Punkt" als Beispiel.
- Fuer Phasen ist der physikalische Kantenwert die auf (-180, 180] Grad gewickelte Differenz. Dann ist Gamma = 2 pi n mit
  Windungszahl n.
- Gegenbeispiel aus Teil E derselben Datei: Phasen 0, 120, 240 Grad im Dreieck.
  - B - A = 120 Grad, C - B = 120 Grad, A - C = -240 Grad, gewickelt 120 Grad.
  - Gamma = 360 Grad, n = 1. Das ist ein Phasenwirbel.
- Ebenso geben nichtlineare antisymmetrische Kantenwerte aus Punktgroessen Gamma != 0:
  - w = (f_j - f_i)^3 gibt Gamma = 3 (f_b-f_a)(f_c-f_b)(f_a-f_c), weil x^3 + y^3 + z^3 = 3xyz bei x + y + z = 0.
  - w = sign(f_j - f_i) gibt Gamma = +-1, aber nie einen geschlossenen Kreislauf.
- Richtig bleibt nur: Die Gruppen-Holonomie ist 1 (Ringprodukt O_a^-1 O_b ... = 1, GLUONEN-L).
- Damit sind "Umlauf nur mit eigenem Kantenwert" (Z. 70, Bewertung Z. 147) und B5 "keine Monopole" zu stark:
  kompakte Kantenwerte erlauben Monopole (DeGrand/Toussaint) [L].

**B3, B4 haelt.** Calugareanu/White/Fuller [L] und Fuller-Mittelung [L] sind richtig. B8 zum Wortlaut von Z. 78: Wr ist das
Richtungsmittel der *Vorzeichensumme der Selbstkreuzungen* der Achse, nicht "der Kreuzungsvorzeichen".

**C1: Zahl falsch, Aussage zu stark (A2).**

- Die Formel lambda = 1/(n sigma) = 2d/(3 phi) habe ich nachgerechnet:
  - sigma = pi d^2/4, n = 6 phi/(pi d^3).
  - Daraus 1/(n sigma) = 4d/(6 phi). Das stimmt.
- Sie gilt aber nur fuer unabhaengig (Poisson) gesetzte, sich ueberlappende Kugeln, mit phi = n V nominal, oder bei kleinem
  phi.
- Fuer harte Kugeln gibt Cauchys Sehnenformel die mittlere Sehne im Spaltraum 4(1 - phi)/s mit s = 6 phi/d:
  - lambda = 2d(1 - phi)/(3 phi).
  - Bei phi = 0,64 sind das 1,0417 * 0,36 = 0,375 d, nicht 1,04 d. Das ist Faktor 2,8.
  - Bei phi = 0,01 bleibt es bei ~66 d.
- "sieht nur seine Beruehrungsnachbarn" (Z. 94) ist zu stark:
  - Ein Beruehrungsnachbar deckt eine Kappe mit halbem Oeffnungswinkel 30 Grad, also (1 - cos 30)/2 = 0,067 des Himmels.
  - Bei z = 6 (Zufallspackung) sind das ~0,40, bei z = 12 (fcc) ~0,80.
  - Der Rest faellt auf die zweite Schale.
- Olbers 1 - exp(-R/lambda) ist exakt nur fuer Poisson.

**C2: haelt fuer Poisson.**

- Nachgerechnet mit V_0..V_4 = 1, 2, pi, 4pi/3, pi^2/2:
  - 1D: (d/2) * 2 = d.
  - 2D: (d/2)(pi/2) = pi d/4.
  - 3D: (d/2)(4/3) = 2d/3.
  - 4D: (d/2)(pi^2/2)(3/(4 pi)) = 3 pi d/16.
  - Jeweils durch phi. Alle richtig.
- Fuer harte Kugeln kommt in jeder Dimension der Faktor (1 - phi) dazu (Cauchy in D: mittlere Sehne = (D V_D/V_(D-1))
  (1 - phi)/s).
- In 1D zeigt das der Grenzfall phi -> 1 deutlich: d/phi ist der Mittelpunktsabstand, nicht die Luecke.

**D: haelt mit Einschraenkung.**

- Bjerknes (Vorzeichen, 1/r^2), Eshelby-Null (ausserhalb der Quelle ist div u = 0, die Wechselwirkungsenergie ist also -p
  div u = 0), Purcell, Najafi/Golestanian 2004, Shapere/Wilczek, Birkhoff, D(D-3)/2 = 0, 2, 5: alle richtig [L/M].
- B9 zu Z. 112: "Nur in 3D ist das Newton" ist missverstaendlich. Bjerknes und die Newtonkraft folgen in jeder Dimension
  demselben Gauss-Gesetz 1/r^(D-1); nur unser 1/r^2 gibt es allein in 3D.
- B10 zu Z. 131: Pushmepullyou (Avron/Kenneth/Oaknin 2005) braucht Volumentausch *und* Abstandsaenderung. Erst das sind die
  zwei Formfreiheiten.
- B11 zu Z. 132: "Strecke = Fluss der Kruemmung" ist exakt nur fuer Bewegung entlang einer Achse (abelsch). Sonst gilt es
  fuehrend fuer kleine Zyklen.
- D5 Zhang/Fodor: ehrlich als [L?] markiert.

**E, Finns Raute: faellt (A1).** Begruendung unter A1 unten. Die Kinematik bei *gesetzten* Phasen habe ich nachgerechnet:

- Zeitpunkt des Maximums t = (90 Grad - psi)/omega, also frueher bei groesserem psi. Reihenfolge C (240) -> B (120) -> A (0)
  -> C.
- Umlaufsinn:
  - C(-0,866; 0,5), B(0; 1), A(0; 0): (B-C) x (A-C) = -0,866, also im Uhrzeigersinn.
  - Rechts +0,866, also gegen den Uhrzeigersinn.
- Kantenrichtungen: B->A, A->C, C->B.
- Fuer das unendliche Dreiecksgitter (120 Grad, Drehsinn wechselnd) stimmt auch "an jedem Knoten gleich viel hinein wie
  heraus": 3 B-Nachbarn hinein, 3 C-Nachbarn hinaus.
- Falsch ist der Grundzustand der Raute selbst.

B12: In Z. 181 steht "d" fuer den Wirbelabstand, in C fuer den Punktdurchmesser. "120-Grad-Paare stossen sich schwach ab"
(Z. 184) gilt nur relativ zum Gleichtakt-Paar bei gleichem Abstand. A-C bei r = 1 (0,5) ist staerker als C-D bei r = sqrt 3
(1/3). Bei festen Stablaengen leisten diese Kraefte aber keine Arbeit, das Falten haengt nur an C-D.

## Pruefobjekt 3: RUNDE-37/atem-netz-1/KARTE.md, Schreibtisch-Abschnitt

**Urteil: haelt mit Einschraenkung.** Die Mittelung, das Vorzeichen, der Gegentakt und Pyrochlor stimmen. Zu korrigieren
sind die Gueltigkeitsbedingung und die Ableitbarkeitsprobe (A4). Gelesene Fassung: mtime 18:00:49, 138 Zeilen.

**Mittelung Z. 27, nachgerechnet [M]:**

- Mit d_i = 1 + eps sin(phi_i) ist eps die *Durchmesser*-Amplitude.
- Ueberlappung: o = delta + (eps/2)(sin phi_1 + sin phi_2).
- Mit <sin^2> = 1/2, <sin phi_1 sin phi_2> = (1/2) cos(phi_1 - phi_2) und <sin> = 0 folgt
  - <o^2> = delta^2 + (eps^2/4)(1 + cos D).
  - Also <U> = (k/2)<o^2> = const + (k eps^2/8) cos D. Der Faktor 1/8 stimmt.
- Bedingung fuer dauernden Kontakt: o_min = delta - eps > 0, also "delta > eps" (Z. 26). Stimmt.
- Zur Absicherung habe ich auch den Mittelwert der Ableitung gebildet:
  - <dU/dphi_1> = k (eps/2)^2 <(sin phi_1 + sin phi_2) cos phi_1> = -(k eps^2/8) sin(phi_1 - phi_2) = d<U>/dpsi_1.
  - Das ist konsistent.

**Vorzeichen und Stabilitaet Z. 28:**

- psi_1' = +mu (k eps^2/8) sin(psi_1 - psi_2), also D' = mu (k eps^2/4) sin D.
- Bei D = 0 ist D' ~ +c D, also instabil.
- Bei D = pi ist D' ~ -c (D - pi), also stabil. Gegentakt stabil, richtig (mu_phi > 0).
- Staerker als behauptet [M, Zusatz]:
  - Nach Jensen gilt fuer *jedes* konvexe Kontaktgesetz <U(delta + X)> >= U(delta + <X>).
  - Gleichheit gilt nur fuer konstantes X = (eps/2)(sin phi_1 + sin phi_2), also Gegentakt bei gleichen Amplituden.
  - Z. 41 ("Gleichtakt entsteht durch die Huelle allein nicht") gilt damit fuer alle konvexen Kontaktgesetze, auch fuer
    zeitweisen Kontakt. Voraussetzung: feste Lagen und gleiche Amplituden.

**Gueltigkeitsbedingung Z. 29/30: zu schwach (A4).**

- dU/dphi_i enthaelt einen Term *erster* Ordnung in eps:
  - k delta (eps/2) cos phi_i je Kontakt.
  - Er mittelt sich in erster Ordnung weg, ist aber gross. Je Punkt ist seine Amplitude A_i = mu_phi k (eps/2) Summe_j delta_ij.
- Wegen delta > eps gilt A_i >= z mu k eps^2/2 = 4z * (mu k eps^2/8). Er ist also mindestens 4z-mal groesser als die
  Kopplung.
- Die Mittelung braucht deshalb A_i << omega, nicht nur mu k eps^2/8 << omega.
- Fuer A_i >= omega hat phi_i' = omega - A_i cos phi_i einen Fixpunkt (Adler). Der Takt bleibt dort stehen, bei
  sin phi* < 0, also im gestauchten Zustand.
- Unterhalb der Schwelle ist die mittlere Taktrate sqrt(omega^2 - A_i^2).

**Ableitbarkeitsprobe:**

- **(a) ist in fuehrender Ordnung ableitbar** (siehe oben, Adler). Einfrieren tritt ein, wenn mu k eps z delta/2 = omega.
- **Folge fuer AN2 (A4):**
  - Pyrochlor hat z = 6 (zwei Tetraeder je Ecke, je 3 Nachbarn), der Diamant z = 4.
  - Bei gleichem delta liegt die Einfrier-Kopplung auf Pyrochlor um genau 6/4 = 1,5 tiefer, ohne jede Frustration.
  - Die Schwelle "mindestens Faktor 1,5" sitzt also auf dem ableitbaren Wert. Der Ausgang haengt an Korrekturen der
    Ordnung eps/(4 delta), nicht an der Frustration.
- **(c) ist fuer ein einzelnes, gebundenes Dreieck ableitbar (B13):**
  - Zentralkraefte und gleiche ueberdaempfte Beweglichkeit geben Summe F_i = 0 und Summe r_i x r_i' = 0.
  - Die Drehung je Takt ist dann die Holonomie der Formschleife (Pseudorotation; Groessenordnung eps^2; Vorzeichen =
    Drehsinn).
  - Gegeben habe ich nur das Vorzeichen und die Skalierung, keinen Zahlwert.
  - Bei 120 Grad schwingen die drei Seitenlaengen mit 60, 180, 300 Grad, der Umfang bleibt konstant. Die Formschleife
    umschliesst also Flaeche.
  - Nicht ableitbar bleibt nur der Verband in der Packung (AN4).
- **(b), (d):** wirklich nicht ableitbar, soweit ich sehe.

**Weitere Punkte:**

- Pyrochlor Z. 36/37 nachgerechnet:
  - E_Tetraeder = (J/2)(|Summe S_i|^2 - 4) >= -2, mit Gleichheit genau fuer Summe S = 0.
  - Vier ebene Einheitszeiger mit Summe 0 bilden eine gleichseitige Viererkette, also eine Raute. Sie zerfallen daher in
    zwei antiparallele Paare. Richtig.
  - Weil Pyrochlor eckenteilend ist (jede Kante in genau einem Tetraeder), ist E = Summe der Tetraeder-Energien. Die
    Entartung ist richtig.
- Moessner/Chalker 1998, n = 2, kollinear [L?]: Das deckt sich mit meiner Erinnerung (PRB 58, 12049), bleibt aber ehrlich
  [L?].
- n ~ ln(t)/t [L]: richtig fuer XY-Wirbel bei nicht erhaltener Dynamik. Im 120-Grad-Fall kommen Z2-Drehsinn-Waende hinzu.
- B14 (Auftrag Teil C, Z. 101): Beim Antiferromagneten hat *jedes* 120-Grad-Dreieck die Phasenwindung +-1. "Wirbel" als
  Phasenwindung um Delaunay-Dreiecke zaehlt also den Drehsinn mit. Noetig ist eine Definition ueber Untergitter-gedrehte
  Phasen, sonst messen zwei Groessen dasselbe.

Wortlaut-Vorschlaege:

- **Z. 29/30:** "Gueltig, solange mu_phi k eps^2/8 << omega *und* mu_phi k (eps/2) Summe_j delta_ij << omega (Term erster
  Ordnung aus der Vorpressung, wegen delta > eps mindestens 4z-mal groesser)."
- **Z. 52/53:** "(a) Einfrieren: in fuehrender Ordnung ableitbar (Adler, Schwelle mu k eps z delta/2 = omega). Nicht
  ableitbar ist nur der Unterschied frustriert gegen zweifaerbbar bei *gleichem* z."
- **AN2:** Pyrochlor (z = 6) gegen einfach-kubisch (z = 6, zweifaerbbar) statt gegen Diamant. Oder die Kopplung auf z delta
  normieren.

## Pruefobjekt 4: RUNDE-37/dreieck-pumpe-l/KARTE.md, Schreibtisch-Abschnitt

**Urteil: haelt mit Einschraenkung.** Die Mathematik stimmt, es bleiben drei Wortlaut-Punkte. Gelesene Fassung: mtime
18:11:34, 98 Zeilen.

- **Freiheitsgrade (Z. 17 bis 19):**
  - Eine Bindung: 12 - 3 - 6 = 3 relative Drehungen.
  - Zwei Bindungen: Die zweite Bindung zaehlt nur 2, weil beide zweiten Ecken schon auf derselben Kugel mit Radius 1 um
    das erste Gelenk liegen. 12 - 3 - 2 - 6 = 1 Faltwinkel. Richtig.
  - Das gilt nur fuer gleich lange Kanten. Bei ungleich grossen Dreiecken (Frage 3 der Karte) erzwingen zwei Bindungen
    Verspannung oder sind nicht moeglich (B15).
- **Faltwinkel (Z. 22):**
  - Die Spitzen liegen h = sqrt(3)/2 von der Kantenmitte entfernt, also CD = 2h sin(theta/2) = sqrt(3) sin(theta/2).
  - Aus CD = 1 folgt sin^2(theta/2) = 1/3 und cos theta = 1 - 2/3 = 1/3. theta = arccos(1/3) ~ 70,53 Grad, richtig.
  - Proben: theta = 180 Grad gibt sqrt 3 (flache Raute), theta = 0 gibt 0.
  - B16: theta ist hier der *Diederwinkel* (180 Grad = flach). Als "Faltwinkel" liest man leicht 180 - theta = 109,47 Grad.
    Vorschlag: "Diederwinkel theta (180 Grad = flach)".
  - "5 Kanten plus 1 neue = 6" stimmt.
- **"Er folgt nicht aus den Ecken" (Z. 20), B17:**
  - Richtig ist: Er folgt nicht aus den *zwei Kantenecken*.
  - Aus allen vier Eckpunkten ist er bestimmt: der Betrag ueber den Spitzenabstand, die Seite ueber das Vorzeichen von
    det[b-a, c-a, d-a].
  - Vorschlag: "Er folgt nicht aus den beiden Ecken der Kante allein."
- **Maxwell (Z. 27 bis 33):**
  - Je D-Simplex gibt es (D+1)/2 Ecken, also D(D+1)/2 Freiheitsgrade. Dem stehen C(D+1,2) = (D+1)D/2 Staebe gegenueber.
    Ausgeglichen, richtig.
  - Gegenprobe mit starren Koerpern:
    - 2D: 3 - 3*2/2 = 0.
    - 3D-Tetraeder: 6 - 4*3/2 = 0.
    - Dreiecke in 3D: 6 - 3*3/2 = 1,5.
    - Alles richtig.
  - beta-Cristobalit als eckenteilendes Tetraedernetz (O-Lagen = Pyrochlor) stimmt.
- **Winkeldefizite (Z. 36 bis 41):**
  - Pro Ecke 360 - 60n Grad, also n = 5, 4, 3 gibt 60, 120, 180 Grad.
  - Summe 720 Grad: 12 * 60 = 6 * 120 = 4 * 180 = 720. Ikosaeder, Oktaeder, Tetraeder stimmen.
  - n = 7 gibt -60 Grad, einen Sattel.
  - "genau 12" gilt nur, wenn alle uebrigen Ecken Sechser sind (Euler: Summe (6 - n) = 12). Kleiner Zusatz.
- **Z. 49 Cristobalit "schrumpfen beim Erwaermen" [L], B18:** Das ist mir nicht sicher. Klar negativ ist ZrW2O8 (RUM-Modell).
  Fuer beta-Quarz und beta-Cristobalit erinnere ich nur "nahe null bzw. leicht negativ". Vorschlag: [L?], oder "kleine bis
  negative Waermeausdehnung (ZrW2O8, beta-Quarz)".
- **Literatur [L]/[L?] in 4, 5 und E1 bis E6:** Sun/Souslov/Mao/Lubensky 2012, Kane/Lubensky 2014, Stenull/Kane/Lubensky 2016,
  Rocklin u. a. 2017, Chen/Bae/Granick 2011, Sigl u. a. 2021, Chen/Upadhyaya/Vitelli 2014, Guest/Hutchinson 2003.
  - Alle sind nach meiner Erinnerung plausibel und richtig zugeordnet.
  - Die [L?]-Kennzeichen sind ehrlich vorsichtig.
- **"nicht ableitbar":** Karte 4 fuehrt keine solche Liste. 5(d) ist ehrlich [H].

## Pruefobjekt 5: RUNDE-37/raute-atem-1/KARTE.md, Ableitbarkeitsprobe

**Urteil: Die Statik haelt als Wenn-dann-Satz. Die Ableitbarkeitsprobe faellt (A1)**, weil ihr Eingang, das Phasenmuster,
falsch ist. Gelesene Fassung: mtime 18:20:18, 89 Zeilen.

**Statik (Z. 38 bis 43), nachgerechnet:**

- 4 Knoten * 3 - 6 starre Bewegungen = 6 = Zahl der Staebe. Ein nicht entartetes Tetraeder hat keine Eigenspannung, ist
  also statisch bestimmt.
- Jedes Paar ist durch einen Stab verbunden (K4), und die Paarkraefte sind zentral und entgegengesetzt gleich.
- Deshalb ist "Stab ij traegt -F_ij" eine Gleichgewichtsloesung, und nach der Eindeutigkeit ist es die einzige.
  - Anziehung f bedeutet Druck f, Abstossung f bedeutet Zug f.
- Mit den *gesetzten* Phasen 0/120/240/240 und r = 1:
  - C-D: cos 0 = 1, also Druck B.
  - Die uebrigen fuenf: cos 120 = -1/2, also Zug B/2. Rechnerisch richtig.

**Der Eingang ist falsch (A1).**

- Z. 35 fuehrt "120 Grad, C = D" als vorab ableitbares Phasenmuster der flachen Raute. Mit gleich starken Bindungen gilt
  das nicht (Rechnung unter A1).
- Der ableitbare Zustand ist A = B, C = D = A + 180 Grad.
- Daraus folgt fuer die Karte:
  - **RA0 (85 %)** sagt "120 Grad je Dreieck" voraus. Bei festen oder langsamen Lagen ist das Scheitern ableitbar.
  - **Statik mit dem ableitbaren Muster:**
    - A-B und C-D gleichphasig: Druck B.
    - A-C, A-D, B-C, B-D gegenphasig: Zug B.
    - Alle sechs Staebe tragen also *denselben Betrag* B.
    - Der Satz "das Gegenteil von Finns Kraftbild, die groesste Kraft sitzt im Schliessstab" (Z. 42/43) faellt damit.
    - FP ist in fuehrender Ordnung ein Gleichstand und wird von Nebeneffekten entschieden.
  - **"Nicht ableitbar: wie sich die Phasen nach dem Schliessen umordnen" (Z. 46) stimmt so nicht.**
    - Das Tetraeder hat E = (1/2)(|Summe S|^2 - 4) >= -2.
    - Der Zustand A = B, C = D = A + 180 Grad hat Summe S = 0 und ist damit schon ein Grundzustand des Tetraeders. Es muss sich
      nichts umordnen, und C-D bleiben gleichphasig.
    - Auch vom 120-Grad-Muster aus erhaelt der rauschfreie Gradientenfluss die Symmetrie C <-> D. Er endet daher ebenfalls
      bei C = D gleichphasig, A = B.
      - Bei C = D verlangt Summe S = 0 die Paare (A,C), (B,D) gegenphasig. Daraus folgt A = B.
    - "C-D gegenphasig" (Z. 46; SCHALTER-UND-ATMEN Z. 187) ist nur einer von entarteten Grundzustaenden:
      - Die Paare (A,C), (B,D) haben einen freien Relativwinkel chi.
      - chi = 0 gibt C-D gleichphasig, chi = 180 Grad gibt gegenphasig. Dazwischen kostet nichts.
  - **RA2 Klapptakt:** Ein Antrieb ist nur mit Rauschen denkbar, als Diffusion von chi entlang einer Nullmode. Das waere ein
    zufaelliges Oeffnen, kein selbst erzeugter Takt. Wortlaut von RA2/Bedeutung anpassen.

**Weitere Punkte:**

- B19, Modell Z. 24/25: Die Bjerknes-Kraft wirkt nur auf die Lagen, nicht auf die Phasen.
  - ATEM-NETZ-1 Z. 41/42 nennt aber gerade das Medium als Quelle von Gleichtakt.
  - Die Rueckwirkung der Bjerknes-Energie (-B cos D / r^(D-1)) auf die Phasen begruenden oder einbauen.
- B20, Lagen frei (Z. 27):
  - Die Raute (5 Staebe, 6 innere Freiheitsgrade in 3D) und das Tetraeder (6/6) koennen jede Ruhelaenge exakt annehmen.
  - Folgen die Lagen dem Atmen schnell, verschwindet die Huellen-Kopplung.
  - Fuer eine einzelne Bindung mit Tiefpass-Rate gamma (= 2 mu_x k) habe ich nachgerechnet:
    - Die Kopplung wird um omega^2/(omega^2 + gamma^2) kleiner.
    - Das Vorzeichen bleibt Gegentakt.
  - Ungleiche Raten je Kante koennen J_AB/J_aussen verschieben. Das ist genau die Groesse, die ueber 120 Grad oder
    kollinear entscheidet (A1).
  - Das Verhaeltnis mu_x k/omega gehoert in den Plan.
- Die Ableitbarkeitsprobe nennt die Zeitmittel der Stabkraefte "vorab ableitbar" (Z. 38) und zugleich "nicht ableitbar"
  (Z. 48). Bei langsamen Lagen ist auch der Wechselanteil ableitbar: Amplitude k eps |cos(D/2)|.

## A-Befunde (vor Weitergabe zu berichtigen)

**A1: Der 120-Grad-Zustand ist nicht der Grundzustand von Finns Raute.**

- Fundstellen:
  - SCHALTER-UND-ATMEN.md Z. 170 bis 176, Z. 187 bis 189.
  - RAUTE-ATEM-1/KARTE.md Z. 13 bis 15, Z. 35, Z. 42/43, Z. 46, RA0 (Z. 64), FP-Bedeutung (Z. 73/74).
- Modell der Leitung selbst:
  - E = J Summe cos(psi_i - psi_j) mit J = k eps^2/8 > 0 auf den fuenf Beruehrungskanten AB, AC, BC, AD, BD.
  - C-D liegen bei sqrt 3 > 1 auseinander und haben keinen Kontakt.
- Rechnung [M], Schritt fuer Schritt:
  1. Setze psi_A = 0 und psi_B = theta. Fuer C gilt cos x + cos(x - theta) = 2 cos(theta/2) cos(x - theta/2). Das Minimum
     ist -2 |cos(theta/2)|, ebenso fuer D.
  2. E(theta)/J = cos theta - 4 |cos(theta/2)|. Mit c = |cos(theta/2)| wird daraus 2c^2 - 1 - 4c.
     - dE/dc = 4c - 4 <= 0, also liegt das Minimum bei c = 1, d. h. theta = 0.
     - Dort ist E = -3 J.
  3. Zum Vergleich der Zustand der Leitung (c = 1/2, theta = 120 Grad):
     - E = -0,5 - 2 = -2,5 J, also 0,5 J hoeher.
     - Er ist nicht einmal stationaer. Am Knoten A gilt dE/dpsi_A = sin 120 + 2 sin 240 = 0,866 - 1,732 = -0,866 J, an B
       +0,866 J.
     - Der Gradientenfluss zieht A und B zusammen.
  4. Grundzustand: psi_A = psi_B, psi_C = psi_D = psi_A + 180 Grad.
     - Die Scharnierkante ist geopfert, die vier Aussenkanten sind voll erfuellt.
     - Hesse-Eigenwerte {0, 0, 2, 4} J: globale Drehung und eine weiche theta-Mode mit E ~ -3 J + J theta^4/32.
     - Die Konvergenz ist also langsam, mit Rauschen breit um theta = 0, aber nicht um 120 Grad.
- Folgen:
  - In diesem Zustand gibt es weder Laufrichtung noch gegenlaeufige Umlaeufe.
  - "Die Skizze ist genau der gemittelte Grundzustand" (Z. 176) ist falsch.
  - RA0 sagt fuer die Kontrolle ein ableitbares Scheitern voraus.
  - Die Statik ergibt sechsmal den Betrag B, nicht "C-D am groessten" (Pruefobjekt 5).
- Warum es im unendlichen Dreiecksgitter anders ist:
  - Dort gehoert jede Kante zu zwei Dreiecken, in der Raute nur AB.
  - Mit J_AB = J' gilt allgemein c = J/J'. 120 Grad (c = 1/2) braucht also J' = 2 J_aussen.
  - Wegen J_ij ~ eps_i eps_j (Mittelung mit ungleichen Amplituden: (k eps_i eps_j/8) cos D) trifft das z. B. zu, wenn C und
    D mit halber Amplitude von A und B atmen.
  - Das ist eine pruefbare Bedingung [M]. Ob Finns "kleine Seitenkreise" das meinen, ist offen.
- Wortlaut-Vorschlag fuer Z. 170 bis 176:
  > "Bei gleich starker Huellen-Kopplung ist der gemittelte Grundzustand der Raute kollinear: A und B gleichphasig, C und D
  > gleichphasig und gegenphasig zu A, B (E = -3 J gegen -2,5 J). Das 120-Grad-Muster ist dort nicht stationaer, eine
  > Laufrichtung gibt es nicht. Das 120-Grad-Muster der Skizze, mit gegenlaeufigen Umlaeufen und B -> A auf dem Scharnier,
  > ist Grundzustand, wenn das Scharnier doppelt so stark koppelt wie die Aussenkanten (J_AB = 2 J_aussen), etwa bei halber
  > Atemamplitude von C und D [M]."

**A2: C1 Sichtlaenge. Zahl falsch, "nur" zu stark (SCHALTER-UND-ATMEN.md Z. 13/14, Z. 91 bis 94).**

- lambda = 2d/(3 phi) gilt fuer Poisson-Kugeln (ueberlappend erlaubt, phi = nV) oder kleines phi.
- Fuer harte Kugeln gilt lambda = 2d(1 - phi)/(3 phi). Rechnung unter Pruefobjekt 2: Cauchy, mittlere Sehne 4(1 - phi)/s,
  s = 6 phi/d.
- Bei phi = 0,64 ergibt das 0,375 d statt 1,04 d.
- Beruehrungsnachbarn decken bei z = 6 nur ~40 % des Himmels, bei z = 12 ~80 %.
- Wortlaut-Vorschlag:
  > "lambda = 2d/(3 phi) fuer unabhaengig verteilte Punkte bzw. kleines phi; fuer sich nicht ueberlappende Punkte
  > 2d(1 - phi)/(3 phi), bei dichtester Zufallspackung ~0,4 d. Im dichten Netz sieht jeder Punkt fast nur seine naechsten
  > Nachbarn (Beruehrung und zweite Schale)."
- Die Faktoren in C2 erhalten fuer harte Kugeln ebenfalls (1 - phi).

**A3: B2 "Umlauf nur mit eigenem Kantenwert" ist fuer Taktphasen falsch (SCHALTER-UND-ATMEN.md Z. 65 bis 70, Z. 147; B5
Z. 83/84).**

- Phasen 0, 120, 240 Grad geben gewickelt Gamma = 360 Grad (Windung 1, Phasenwirbel).
- Nichtlineare antisymmetrische Kantenwerte aus Punktgroessen geben Gamma != 0. Ein Beispiel ist (f_j - f_i)^3.
- Das widerspricht Teil E derselben Datei, wo aus Punktphasen eine umlaufende Welle folgt.
- Wortlaut-Vorschlag:
  > "Ist der Kantenwert die Differenz einer reellen Punktgroesse (w_ij = f_j - f_i), dann ist Gamma = 0. Bei Phasen gilt
  > das nur bis auf 2 pi n: Ein Dreieck mit 0, 120, 240 Grad hat die Windung 1 (Phasenwirbel). Die Gruppen-Holonomie bleibt
  > 1. Einen nicht-topologischen Umlauf gibt es nur mit einem eigenen Kantenwert."
- Ebenso B5: "solange die Werte reell sind. Bei Winkelwerten (kompakt) sind Monopole moeglich."

**A4: ATEM-NETZ-1. Gueltigkeitsbedingung zu schwach, (a) ableitbar, AN2 prueft z statt Frustration (KARTE Z. 29/30,
Z. 52/53, AN2 Z. 114).**

- Der Term erster Ordnung mu k (eps/2) delta cos phi_i je Kontakt ist wegen delta > eps mindestens 4z-mal groesser als die
  Kopplung.
- Einfrieren nach Adler setzt bei mu k eps z delta/2 = omega ein.
- Pyrochlor (z = 6) gegen Diamant (z = 4) gibt genau 6/4 = 1,5. Das ist die Schwelle von AN2.
- AN0 ("volle und gemittelte Dynamik auf 10 % gleich") kann aus demselben Grund ableitbar scheitern, wenn "schwach" nur
  ueber mu k eps^2/8 gewaehlt wird.
- Wortlaut-Vorschlaege stehen unter Pruefobjekt 3.

## B-Befunde

Nicht falsch im Kern. Genauer fassen.

**NEGATIV-LESARTEN.md:**

- **B1, Z. 21 (N8):** Garriga/Tanaka gilt ohne Radion-Stabilisierung. Dann ist gamma auf unserer Brane in (-1, 1/2), und
  Cassini schliesst das ganz aus.
- **B2, Z. 15 (N2):** 0,277 +- 0,057 Grad statt gerundet. Dazu "mit Staubbehandlung 3,5 sigma".
- **B3, Z. 15:** "Lee/Yang 1956" mit [L] kennzeichnen (laut Dossier nicht gelesen).
- **B4, Z. 14 und Z. 27:** "als anziehende Rueckseite ausgeschlossen" folgt aus dem Vorzeichen (Theorie), nicht aus
  Messung. Bitte so benennen.
- **B5, Z. 20 (N7):** Bruchgrenze "d ~ 4,2 bis 5,1 je nach Methode" (Dossier Z. 64).

**SCHALTER-UND-ATMEN.md:**

- **B6, Z. 40:** "im Mittel gleich haeufig".
- **B7, Z. 49:** Die 2D-Zeile passt nicht zur Regel D - 1. Aufteilen in "gesehen in 1D: Punkt gegen Strich" und "ohne
  Ansicht: echter Schnitt".
- **B8, Z. 78:** Wr ist das Mittel der Vorzeichen*summe* der Selbstkreuzungen.
- **B9, Z. 112:** "Nur in 3D ist das Newton" ist irrefuehrend. Bjerknes und Newton folgen in jeder Dimension demselben
  Gauss-Gesetz.
- **B10, Z. 131:** Pushmepullyou braucht Volumentausch plus Abstandsaenderung.
- **B11, Z. 132:** Shapere/Wilczek ist exakt fuer Bewegung auf einer Achse, sonst fuehrend fuer kleine Zyklen.
- **B12, Z. 181 und 184:**
  - "d" ist doppelt belegt.
  - "schwach" gilt nur bei gleichem Abstand. A-C bei r = 1 (0,5 B) ist staerker als C-D bei sqrt 3 (B/3).
  - Fuer das Falten zaehlt nur C-D, weil die Stablaengen fest sind.

**ATEM-NETZ-1:**

- **B13, (c):** Fuer das einzelne gebundene Dreieck ableitbar: Pseudorotation, O(eps^2), Vorzeichen = Drehsinn.
- **B14, Z. 101:** "Wirbel" um Delaunay-Dreiecke zaehlt beim Antiferromagneten den Drehsinn mit. Untergitter-Drehung
  definieren.
- **B21:** Das Modell liegt laut Abstract nahe an Zhang/Fodor 2023, siehe Literatur. Die Neuheit entsprechend eingrenzen.

**DREIECK-PUMPE-L:**

- **B15, Z. 18:** Zwei Bindungen ergeben nur bei gleich langen Kanten ein spannungsfreies Scharnier.
- **B16, Z. 22:** "Diederwinkel (180 Grad = flach)".
- **B17, Z. 20:** "nicht aus den beiden Kantenecken allein".
- **B18, Z. 49:** Cristobalit "schrumpft" auf [L?] setzen, oder ZrW2O8 nennen.

**RAUTE-ATEM-1:**

- **B19, Z. 24/25:** Die Bjerknes-Energie wirkt nicht auf die Phasen. Das widerspricht ATEM-NETZ-1 Z. 41/42 (Medium als
  Gleichtakt-Quelle).
- **B20, Z. 27:**
  - Freie Lagen schwaechen die Kopplung um omega^2/(omega^2 + gamma^2), mit gamma = 2 mu_x k.
  - Ungleiche Raten je Kante verschieben J_AB/J_aussen.
  - mu_x k/omega gehoert in den Plan.

## Literaturangaben und Kennzeichen

**Abrufe:** Es gab 2 gezielte arXiv-API-Abrufe (export.arxiv.org/api/query), beide zwischen 18:40:20 und 18:41:32 CEST
(je date davor und danach).

1. **"pulsating active matter" (SCHALTER-UND-ATMEN D5, ATEM-NETZ-1 Z. 76, beide [L?]):** gefunden als arXiv 2208.06831,
   Yiwei Zhang, Etienne Fodor, PRL 131, 238302 (2023). **Die Angabe stimmt** [S Abstract, pruefer-opus].
   - Wortlaut im Abstract: "dense repulsive particles", "locally synchronised particles", "propagate deformation waves",
     "ranging from spiral waves to defect turbulence", "competition between repulsion and synchronisation".
   - Folge: Das ist das naechste Literaturmodell zu ATEM-NETZ-1 (B21).
   - "competition between repulsion and synchronisation" passt zur eigenen Herleitung: Abstossung allein gibt Gegentakt,
     Gleichtakt braucht eine eigene Kopplung.
   - Die Folgearbeiten Pineros/Fodor (2403.16961, PRL 134, 038301) und Casagrande/Manacorda/Fodor (2605.25996, "Defect
     asymmetry controls emergent motility") betreffen das Pumpen bzw. die Bewegung. Fuer AN4 sind sie vor dem Lauf lesenswert.
2. **Moessner/Chalker 1998 (ATEM-NETZ-1 Z. 38, [L?]):** gefunden als cond-mat/9807384, "Low-temperature properties of
   classical, geometrically frustrated antiferromagnets".
   - Der Abstract sagt: Thermische Auswahl "happens only for the models with the smallest ground-state degeneracies".
     Fuer das Pyrochlor (dort Heisenberg) gilt: "no freezing transition or selection of preferred states".
   - "n = 2" und "kollinear" stehen *nicht* im Abstract.
   - Meine Zaehlung [M]:
     - Je Tetraeder gibt es F = 4(n-1)/2 = 2(n-1) Freiheitsgrade und K = n Bedingungen, also D = n - 2.
     - n = 2 gibt D = 0, die kleinste Entartung.
     - Damit ist die Auswahl fuer n = 2 mit dem Abstract vertraeglich.
   - "kollinear" bleibt aber **[L?]**. Das Kennzeichen der Karte ist ehrlich.

**Ohne Abruf, aus Gedaechtnis [L] geprueft:**

- **Plausibel und ehrlich gekennzeichnet:** Gauss-Verschlingungszahl, Calugareanu/White/Fuller, Olbers, Zufallspackung
  0,64, Bjerknes, Eshelby, Purcell, Najafi/Golestanian 2004, Avron u. a. 2005, Shapere/Wilczek 1987/89, Birkhoff,
  Nordstroem, Kitagawa u. a., Boyle/Finn/Turok 2018, Parisi/Sourlas, Badertscher 2007, ALPHA-g 2023.
- **Nicht beurteilt:** Read 2017 (nur ueber WINDUNG-LESER). Das ist mit meiner eigenen Ueberlegung vertraeglich:
  - K_1 von C[t_1^+-1 .. t_d^+-1] ist C^* + Z^d.
  - Damit hat ein streng lokaler Takt keine 3D-Windung.

**Kennzeichen-Ehrlichkeit:**

- Es wird kein [L] als [S] verkauft, die [S]-Stichproben stimmen mit dem Dossier ueberein.
- Kein [M] wird als Messung verkauft. Die [E]-Verweise sind Projektmessungen mit Fundstelle.
- Einzige Kennzeichen-Luecke: Namen und Jahre in der Spalte "Was es physikalisch heisst" (NEGATIV-LESARTEN) stehen ohne
  Kennzeichen (B3).
- Inhaltlich zu stark sind dagegen drei [M]-Saetze: A1, A3 und die Ableitbarkeitsprobe in A4.

## Einfach gesagt

Die meisten Rechnungen der Leitung stimmen. Das gilt fuer die Kreuzungs-Haendigkeit, den Gegentakt zweier atmender
Nachbarn, den Tetraeder-Faltwinkel und die Kraefte im Stabwerk.

Ein wichtiger Satz stimmt aber nicht. Bei Finns Raute aus zwei Dreiecken ist das schoene 120-Grad-Muster mit den
gegenlaeufigen Wellen nicht der ruhigste Zustand. Am ruhigsten atmen die beiden Scharnierpunkte gleich und die beiden
Seitenpunkte genau entgegengesetzt, und dann laeuft keine Welle.

Das 120-Grad-Muster kaeme nur heraus, wenn die Scharnierkante doppelt so stark koppelt wie die Aussenkanten, zum Beispiel
wenn die Seitenpunkte nur halb so stark atmen. Ausserdem ist die Sichtweite in dichten Packungen etwa dreimal kuerzer als
angegeben. Und ein geplanter Test (Einfrieren im Pyrochlor gegen den Diamant) misst vor allem die Zahl der Nachbarn, 6
gegen 4, nicht die Frustration.
