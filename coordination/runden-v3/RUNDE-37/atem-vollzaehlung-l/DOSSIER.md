# ATEM-VOLLZAEHLUNG-L: Dossier (feldforscher fuer claude-primary, Runde 48)

Karte: KARTE.md (bindend, AV1 bis AV4 unveraendert). Arbeitsfeld: ARBEITSFELD.md. Abrufliste: ABRUFE.md. Rohquellen:
quellen/ (A1, A3 bis A15 mit Zeitdatei und Kopfzeilen).

Kennzeichen: [E] Rechnung (hier nur von Hand), [M] Mathematik, [S] Fachquelle (an der Quelle gelesen, Stelle genannt),
[L] Lehrbuch, [L?] Gedaechtnis, ungeprueft, [H] Hypothese, [P] Projektbefund, [ES] eigener Schluss. Messdaten aus
Fachquellen sind [S]. Zeilenangaben "Txt Z." beziehen sich auf die pdftotext-Dateien in quellen/.

## 1. Zeiten und Abrufzahl

- Start 2026-10-05 09:00:40 CEST (date). Vorlesen (lokal) bis 09:04:39. Netzabrufe 09:05:38 bis 09:18:11.
  Gegensweep ohne Netz ab 09:20:30. Dossier ab 09:25:19 (date). Abgabezeit steht in Abschnitt 10, Punkt 12.
- **Netzabrufe: 15 von 15.** Mit Inhalt 11 (2 Websuchen, 2 arXiv-Volltexte, 1 LMU-Repositorium, 6 OpenAlex).
  Ohne Inhalt 4: A6 (IUCr, HTTP 403), A7 (Springer, JavaScript-Abfrage), A10 (http statt https, eigener Fehler),
  A11 (arXiv-API, HTTP 503).

## 2. Ergebnis zuerst

1. **Die 222-Form gehoert sehr wahrscheinlich zu einer bekannten Familie, ist dort aber nicht als eigene Form
   beschrieben.** Coh/Vanderbilt 2008 beschreiben fuer jeden der drei X-Punkte eine exakt starre, dreidimensionale
   Schar von Strukturen mit P2_12_12_1-Symmetrie in der halben Wuerfelzelle. Sie enthaelt alpha (P4_12_12) und den
   Wright/Leadbetter-Typ (I-42d) als Sonderfaelle [S]. Die 222-Form hat genau diese Drehteil-Gruppe, die halbe Zelle
   und drei Ausrichtungen [P, im Gegensweep geprueft]. Zwei Isotropiebedingungen auf einer dreidimensionalen Schar
   lassen eine Kurve uebrig, und genau eine Kurve fand ISO-ATEM-1 [ES]. Den isotropen Ast selbst nennt niemand.
2. **Wright/Leadbetter hatten kein P2_13-Modell.** Ihr beta-Cristobalit besteht aus I-42d-Domaenen, also aus
   Drehungen um eine Wuerfelachse [S]. Das ist das flache, anisotrope Atmen aus ISO-ATEM-1 Teil A (DFT: a -4,5 %,
   c -0,5 %) [S, E]. P2_13 kommt bei Coh/Vanderbilt gar nicht vor; die Zuschreibung an Barth 1932 bleibt [L?].
3. **Vollzaehlung:** Fuer die kleinste Zelle mit 2 Tetraedern ist der endliche Deformationsraum geschlossen bekannt:
   eine offene Menge in SO(3) (Borcea/Streinu, Theorem 2) [S]. Daraus folgt in einer Zeile, dass diese Zelle nicht
   isotrop atmen kann [M]. Kleinwinklige RUM lassen sich laut Campbell/Eggers/Stokes 2025 systematisch und
   vollstaendig zaehlen; seit Eggers u. a. 2024 gilt das auch fuer RUM, die eine Gitterverzerrung brauchen. Fuer
   endliche Winkel gibt es seit 2025 einen ersten systematischen Suchalgorithmus [S, nur Abstracts]. Fuer die
   kubische Zelle mit 8 Tetraedern habe ich keine Vollzaehlung gefunden.
4. **Echter Cristobalit:** Beim Erwaermen durch den alpha-beta-Uebergang nahe 533 K **waechst** das Volumen
   sprunghaft um etwa 5 % [S]. Danach aendert es sich kaum: Es steigt bis 1300 K und faellt bis 2000 K wieder auf den
   Wert von 750 K, 27,4 cm^3/mol [S]. Im Mittel ueber 750 bis 2000 K ist die Ausdehnung also null,
   |alpha_V| <= 1,5e-6/K [E aus S]. Zum Vergleich ZrW2O8: alpha = -9,07e-6/K (2 bis 350 K) [S]. RUM sind dort die
   Standarderklaerung (Pryde u. a. 1997, Tucker u. a. 2005) [S], aber das beteiligte Bauteil ist umstritten (Cao u. a.
   2002, Bridges u. a. 2014) [S].
5. **Urteile:** AV1 verfehlt, AV2 teilweise, AV3 teilweise, AV4 eingetroffen, mit zwei Regimen innerhalb von beta.

**Kalibrierung:**
- (a) **Gemessen:**
  - 5 % Volumensprung nahe 533 K (Schmahl u. a. 1992); Leadbetter/Wright 1976: etwa 4 %.
  - beta-Volumen: Anstieg bis 1300 K, Abfall bis 2000 K, 27,4 cm^3/mol.
  - ZrW2O8: -9,07e-6/K.
  - Wright/Leadbetter: I-42d-Domaenen.
- (b) **Nuetzlich verdichtet:**
  - Mittel alpha_V = 0 fuer beta.
  - SO(3) fuer die primitive Zelle, also kein isotropes Atmen [M].
  - P2_13 als Tripel aus alpha-Typ-Moden [M].
  - Drehteil-Gruppe der 222-Form = P2_12_12_1 [ES, an Daten].
- (c) **Gewachsene Gewissheit ohne neue Evidenz (Warnzeichen):**
  - "Die 222-Form ist der isotrope Ast der Coh/Vanderbilt-Schar". Meine Sicherheit stieg von [H] auf "sehr
    wahrscheinlich", gestuetzt nur auf Symmetrie und Zaehlung, ohne Rechnung.
  - "RUM bestimmen die beta-Ausdehnung": belegt nur durch Theorie (Heine u. a. 1999) und Simulation (Huang/Kieffer
    2003). Eine Messung, die den RUM-Anteil fuer beta-Cristobalit abtrennt, habe ich nicht gelesen.

## 3. Erwartungsverstoesse (das Wichtigste zuerst)

1. **E1, mehr als Einzelvarianten (gegen AV3 und meine Erwartung):**
   - Borcea/Streinu 2011 geben den **endlichen** Deformationsraum des idealen Cristobalits fuer die primitive
     Periodizitaet geschlossen an: "naturally parametrized by the open set in SO(3)" [S, A14 Txt Z. 161 bis 163;
     Periodizitaet Z. 114 bis 118].
   - Coh/Vanderbilt haben "an entire three-dimensional subspace of rigid-unit structures" mit exakt starren Tetraedern
     [S, A1 Txt Z. 502 bis 507].
   - Campbell/Eggers/Stokes 2025: Kleinwinklige RUM lassen sich bereits systematisch und vollstaendig vorhersagen.
     Neu ist "the first systematic search algorithm for large-angle RUMs". Der Kleinwinkel-Grenzwert der
     grosswinkligen RUM ist eine Vereinigung von Unterraeumen des Kleinwinkel-Raums [S, Abstract, A12].
   - Erwartet hatte ich eine lokale Dimensionsangabe und sonst nur einzelne Scharen.
2. **E2, Spannung zwischen Coh/Vanderbilt und dem exakten P2_13:**
   - Coh/Vanderbilt schreiben sinngemaess: Drehungen aus zwei verschiedenen ihrer drei Mannigfaltigkeiten lassen
     sich nicht so kombinieren, dass die Tetraeder starr bleiben [S, A1 Txt Z. 750 bis 757, Paraphrase].
   - Schreibtisch [M]: Linear ist P2_13 je ein alpha-Typ-Modus an allen drei X-Punkten mit gleicher Amplitude.
     Bei X_z dreht A um x und B um y, Schichtfolge +x, +y, -x, -y (ARBEITSFELD Abschnitt 10). Trotzdem ist P2_13
     exakt starr (ISO-ATEM-1, Handformel) [P].
   - Lesart: Coh/Vanderbilt rechnen nur Z = 4-Zellen und schliessen Paare aus. Das kubische Tripel behandeln sie
     nicht; P2_13 erwaehnen sie gar nicht. **Moderator: Zellgroesse (Z = 4 gegen Z = 8).** Logisch zwingend ist der
     Widerspruch nicht.
3. **E3, zwei Regime innerhalb von beta:** Das Volumen steigt gleichmaessig bis 1300 K und "decreases continuously up
   to the melting temperature of 2000 K" [S, Bourova/Richet 1998, Abstract, A4]. Erwartet hatte ich durchgehend "nahe
   null, eher negativ".
4. **E4, Wright/Leadbetter = I-42d:** Ihr Modell sind Domaenen der I-42d-Struktur in sechs Orientierungen, eine Art
   Mikro-Verzwillingung [S, Abstract, A5, Paraphrase]; ebenso Coh/Vanderbilt [S, A1 Txt Z. 53 bis 55, 115 bis 124].
   Die Karte gab AV1 70 %.
5. **E5, starres Atmen geht nur nach unten:** Kippungen starrer Tetraeder koennen das Volumen der Idealstruktur nur
   verkleinern [S, A1 Txt Z. 254 bis 256, Paraphrase]. Wachsen ueber die Ideallage braucht Bindungsdehnung.
6. **E6, kleinere Verstoesse:**
   - Im Abstract von Mary u. a. 1996 steht keine Koeffizientenzahl (A8).
   - Huang/Kieffer 2003 (MD) sagen im Abstract doch etwas zu beta: "almost zero ... up to 2000 K and slightly
     negative at higher temperatures" (A15). Ihre Grenze (2000 K) weicht von Bourova/Richet (1300 K) ab;
     Moderator: Simulation gegen Messung.

**Regime und Moderatoren (Regel 1):**
- **Zellgroesse:**
  - Z = 2: SO(3), kein isotroper Punkt ausser der Ideallage.
  - Z = 4: P2_12_12_1-Scharen mit isotroper Kurve.
  - Z = 8: zusaetzlich P2_13.
- **Infinitesimal gegen endlich:** Manche kleinwinkligen RUM verformen bei grossem Winkel die Einheiten (Campbell u. a.
  2025 [S]).
- **Temperatur:**
  - Unter Tc ist die Kippung statisch (alpha), und der Uebergang bringt +5 %.
  - Ueber Tc ist sie dynamisch (beta): bis 1300 K positiv, darueber negativ.
  - Heine/Welche/Dove 1999: Das Vorzeichen "may be reversed above a soft mode phase transition" [S, A15].
- **Zeit- und Laengenskala der Sonde:** statische Domaenen (Wright/Leadbetter) gegen dynamische Unordnung
  (Swainson/Dove). Coh/Vanderbilt halten den Streit teils fuer eine Frage der Begriffe; welche Beschreibung stimmt,
  haenge von der Zeit- und Laengenskala der Messung ab [S, A1 Txt Z. 56 bis 70, Paraphrase].
- **Auswerteverfahren bei ZrW2O8:** RMC-Modell aus Totalstreuung (Tucker 2005, pro RUM) gegen EXAFS/XPDF-Peakanalyse
  (Cao 2002, Bridges 2014, steife Zr-O-W-Bruecke) [S, A8].

**Unterscheidungspunkte (Regel 2):**
- **U1, Kippung oder Bindungsdehnung als Steuergroesse der Ausdehnung:**
  - (i) Am alpha-beta-Uebergang: +5 % Volumen in einem Sprung erster Ordnung [S]. Bindungsdehnung kann das in wenigen
    Kelvin nicht liefern; der Sprung kommt von der geloesten statischen Kippung [ES].
  - (ii) Am Vorzeichenwechsel bei etwa 1300 K in beta [S]: Dort ueberholt der negative geometrische Beitrag den
    positiven [ES nach Heine u. a. 1999].
  - (iii) Trennende Messung: scheinbare Si-O-Laenge aus der Bragg-Zelle gegen wahre Si-O-Laenge aus der
    Paarverteilung, als Funktion von T. Mit RUM waechst die Luecke mit T. In diesem Lauf nicht gelesen (Dove u. a.
    1997, Tucker u. a. 2001 nur [L?]).
- **U2, statische Domaenen oder dynamische RUM in beta:** Energieaufgeloeste Streuung trennt. Statisch gibt eine
  elastische, aufloesungsbegrenzte diffuse Intensitaet; dynamisch gibt inelastische Anteile, die mit T wachsen
  [ES]. Swainson/Dove 1993 fanden mit inelastischer Neutronenstreuung niederfrequente "floppy modes" [S, A8].
- **Gegenstimme im 24-Monats-Fenster (Glas, nicht Kristall):** Shcheblanov/Lemaitre 2026 zerlegen das
  Schwingungsspektrum von Kieselglas. Bei tiefen Frequenzen sind starre Tetraederdrehungen dort keine eigenen
  Freiheitsgrade, sondern an Biegekoordinaten gebunden [S, Abstract, A12, Paraphrase]. Das verwirft RUM nicht, legt die
  Steuergroesse aber auf die Biegung an der Bruecke (Si-O-Si) [ES]. Eine Arbeit, die das RUM-Bild fuer
  beta-Cristobalit verwirft, fand ich unter den 100 relevantesten Treffern seit 2024-10-05 nicht.
- **U3, RUM oder korrelierte starre Translation in ZrW2O8:** Getrennt wird an der T-Abhaengigkeit der Zr-W-Paarbreite
  bei tiefer Temperatur. Bridges 2014 finden sie schwach [S], Tucker 2005 lesen RUM aus dem RMC-Modell [S]. Nach
  meinem Stand ist das empirisch nicht eindeutig entschieden. Gemeinsame Kopplungsgroesse: niederfrequente Moden mit
  negativem Grueneisen-Parameter (Evans 2000 [S, A9]). Regel 6: drei Wege, eine Groesse.
- **U4, Coh/Vanderbilt "inkompatibel" gegen exaktes P2_13:** Die Aussagen laufen nur in der Zelle mit 8 Tetraedern und
  drei X-Armen auseinander. Die trennende Rechnung ist der Kartenvorschlag in Abschnitt 8.
- **U5, Modell gegen Material:** Das starre Modell verbietet V > V0. beta liegt mit lambda etwa 0,96 deutlich unter der
  Ideallage (Abschnitt 7), auch bei 2000 K. Kein Befund verlangt Bindungsdehnung ueber die Ideallage [ES].

**Gegensweep (Regel 4).** Frage: Was war so selbstverstaendlich, dass ich es nicht geprueft habe?
- **G1 "Die 222-Form ist P2_12_12_1". Geprueft** an iso-atem-1/nachtrag-69/diag-c.json [P]:
  - Klasse mit Achse [0,0,1] (49 Loesungen): 2[0,0,1] mit Laengsanteil 0,5 (2_1). 2[1,1,0] und 2[1,-1,0] je mit
    a_c/(2 sqrt 2) = a_t/2, also 2_1.
  - Gitter primitiv mit halber Wuerfelzelle, (1/2,0,1/2) fehlt.
  - Ergebnis: Drehteil-Gruppe P2_12_12_1 [ES]. Uneigentliche Operationen hat ISO-ATEM-1 nicht getestet.
- **G2, der 5-%-Sprung ist ein Wachsen.** Geprueft: Laut Coh/Vanderbilt ist beta im Experiment etwa 5 % groesser
  [S, A1 Txt Z. 696 bis 699, Paraphrase].
- **G3, 750 K liegt im beta-Feld.** Geprueft: Tc nahe 533 K [S, A3].
- **G4, die Tetraeder bleiben im echten SiO2 starr.** Teilgeprueft in der DFT: Fuer V < V0 bleiben O-Si-O und Si-O fast
  konstant, Si-O-Si aendert sich um ~35 Grad [S, A1 Txt Z. 247 bis 252, Paraphrase]. Die thermische Dehnung der
  Si-O-Bindung selbst ist nicht geprueft.
- **G5, P2_13 ist Barths Modell.** Nicht geprueft (kein Abstract, Budget aus). Bleibt [L?].
- **G6, OpenAlex-Abstracts sind woertlich.** Nicht geprueft. Bei Tucker 2005 fehlen in der Rekonstruktion die Formeln
  ("the and polyhedra"). Die benutzten Zahlen sind lesbar.
- **G7, die Coh/Vanderbilt-Schar ist die ganze starre Menge der Z = 4-Zelle.** Nicht belegt: Sie zeigen, dass es die
  Schar gibt, nicht, dass es nur sie gibt.
- **Zusatz im Gegensweep (A1, Tabelle I, Txt Z. 196 bis 222):**
  - DFT-Idealzelle a_c = 7,444 A.
  - beta-tilde (I-42d) relaxiert: a = 7,1050, c = 7,4061 A, also a/a_c = 0,9545 und c/a_c = 0,9949 [E aus S]. Die
    Wright/Leadbetter-Form schrumpft nur quer zur Drehachse.
  - Experiment alpha: c/(sqrt 2 a) = 6,8903/(1,41421 x 4,9570) = 0,983 [E aus S]. alpha ist nicht isotrop.

## 4. Tabelle der Kipp-Varianten

| Raumgruppe | Kippmuster | Zelle (k) | isotrop F = lambda I? | Quelle mit Stelle | Bezug zu ISO-ATEM-1 |
|---|---|---|---|---|---|
| Fd-3m (ideal, C9) | keine Kippung, Si-O-Si 180 Grad | Gamma, Z = 2 primitiv | lambda = 1. Groesstes Volumen; starre Kippungen verkleinern nur | Coh/Vanderbilt 2008, A1 Txt Z. 125 bis 131 und 254 bis 256 [S]; Wright/Leadbetter 1975, Abstract: Mittelstruktur Fd-3m, O auf 96h [S] | Ideallage beider Scharen |
| I-42d (beta-tilde; Wright/Leadbetter 1975, bei ihnen als Idealform bezeichnet) | alle Tetraeder um eine Wuerfelachse, Vorzeichen wechselnd | Gamma, Z = 2 | **nein**. DFT relaxiert a/a_c 0,9545, c/a_c 0,9949 | Abstract (A5); A1 Txt Z. 115 bis 124, Tab. I [S]; Verhaeltnisse [E aus S] | = Teil A bzw. Gamma-Ansatz (flaches Atmen, V/V0 = cos^2 phi) [ES] |
| SO(3)-Schar der primitiven Zelle | zweites Tetraeder relativ beliebig gedreht, R in SO(3); I-42d ist ein Sonderfall | Gamma, Z = 2 | **nein, ausser R = I**. F = (R + I)/2 = lambda I verlangt R = (2 lambda - 1) I [M] | Borcea/Streinu 2011, Theorem 2, A14 Txt Z. 161 bis 163 [S] | erklaert ISO-ATEM-1 Abschnitt 1 Punkt 5 (Gamma-Rest > 0) in einer Zeile; deckt IA1 (F = (R_A + R_B)/2) [P] |
| P4_12_12 / P4_32_12 (alpha-tilde, alpha-Cristobalit) | Drehungen um kubisch x und y, mit X_z moduliert (Schichtfolge +x, +y, -x, -y), kleine Verschiebungen | ein X-Arm, Z = 4 | **nein**: Experiment c/(sqrt 2 a) = 0,983 [E aus S] | A1 Txt Z. 130 bis 138, 509 bis 513, Tab. I [S]; Schmahl u. a. 1992, Abstract (A3) [S] | Sonderpunkt der Schar, in der die 222-Form liegt; selbst nicht isotrop |
| **P2_12_12_1**, dreidimensionale Schar (alpha1, alpha1', beta1), je X-Punkt eine, drei insgesamt | endliche Kombination der beiden X-Moden und des Gamma-Modus um dieselbe Achse; exakt starr | ein X-Arm, Z = 4 | allgemein nein. **Isotrope Teilkurve**: 2 Bedingungen (a = b, c = sqrt 2 a) auf 3D lassen 1D [ES] | A1 Txt Z. 502 bis 513, 590 bis 600, 738 bis 757 [S] | **222-Form** = isotroper Ast darin [ES]. Drehteile geprueft (G1): drei 2_1-Schrauben, halbe Zelle, drei Ausrichtungen = drei X-Punkte |
| **P2_13** (Barth 1932 [L?]) | jedes Tetraeder um die eigene <111>-Achse; zwei Winkel phi_A, phi_B; linear je ein alpha-Typ-Modus an allen drei X-Punkten [M] | alle drei X-Arme, Z = 8 (kubisch P) | **ja**, durch die kubische Symmetrie | an keiner gelesenen Quelle; Coh/Vanderbilt erwaehnen es nicht; Barth 1932 nur Metadaten (A5) | **P2_13-Schar** (Handformel). Spannung zu Coh/Vanderbilt (E2) |
| Domaenen- bzw. Fluktuationsbilder | Wright/Leadbetter: I-42d in 6 Orientierungen; Hatch/Ghose 1991: beta schwankt zwischen 12 alpha-Domaenen (3 X x 2 Enantiomorphe x +-phi); Nieuwenkamp 1937: O frei auf einem Ring | Mittel Fd-3m | nur im Mittel kubisch | A5 Abstract [S]; Hatch/Ghose und Nieuwenkamp als Sekundaerzitate A1 Txt Z. 711 bis 719 und 681 bis 684 [S] | Mittelung statt Einzelform |
| C222_1 (alpha-AlPO4), I-4 (beta-AlPO4) | Symmetrieabsenkung durch Al/P-Ordnung, keine neue Kippung | wie alpha bzw. beta | nicht betrachtet | A1 Txt Z. 63 bis 68 [S] | kein Bezug |

Nicht gefunden: eine Liste aller endlichen Varianten fuer die Zelle mit 8 Tetraedern. Die gruppentheoretische Liste
der Untergruppen (Hatch/Ghose 1991) und O'Keeffe/Hyde 1976 waren gesperrt (A6, A7).

## 5. Datentabelle Waermeausdehnung

| Material | Phase | Temperaturbereich | Koeffizient bzw. Groesse | Quelle mit Stelle | RUM-Deutung |
|---|---|---|---|---|---|
| SiO2 Cristobalit | alpha -> beta beim Erwaermen | nahe 533 K, "strongly first order", latente Waerme 1256 J/mol | **Delta V/V = +5 %** (Sprung) | Schmahl/Swainson/Dove/Graeme-Barber 1992, Z. Krist. 201, 125, Abstract (A3) [S] | ja, indirekt: Uebergang = Einfrieren eines X-Punkt-Kippmodus (instabiler X4-Modus -> P4_12_12, A1 Txt Z. 196 bis 206 [S]) |
| SiO2 Cristobalit | alpha -> beta | Hysterese, ~20 Grad C Koexistenz | Volumenunterschied etwa 4 % | Leadbetter/Wright 1976, Phil. Mag., Abstract (A5) [S] | nicht im Abstract |
| SiO2 Cristobalit | alpha bzw. beta je fuer sich | unter bzw. ueber Tc | "smooth and slow variation" der Gitterparameter | dieselbe Stelle [S] | nicht im Abstract |
| SiO2 beta-Cristobalit | beta | 750 -> 1300 K | positiv (gleichmaessiger Anstieg); Zahl nicht im Abstract | Bourova/Richet 1998, GRL, Abstract (A4) [S] | nicht im Abstract |
| SiO2 beta-Cristobalit | beta | 1300 -> 2000 K | **negativ**: Volumen faellt zurueck auf 27,4 cm^3/mol | dieselbe Stelle [S] | nicht im Abstract; passt zur Theorie von Heine u. a. 1999 [ES] |
| SiO2 beta-Cristobalit | beta | Mittel 750 -> 2000 K | **mittleres alpha_V = 0**; aus der Rundung der Angabe 27,4 folgt \|alpha_V\| <= 0,05/27,4/1250 K = 1,5e-6/K, \|alpha_L\| <= 0,5e-6/K | [E aus S] | - |
| SiO2 beta-Cristobalit (Simulation) | beta | bis 2000 K bzw. darueber | fast null bzw. leicht negativ | Huang/Kieffer 2003, J. Chem. Phys., Abstract (A15) [S, MD] | ja (nach eigener Angabe mit dem RUM-Modell vereinbar) |
| SiO2 alpha-Cristobalit (Simulation) | alpha | - | positiv | dieselbe Stelle [S, MD] | nicht genannt |
| BeF2, alpha-Cristobalit-Struktur (Rechnung) | alpha | 300 K | alpha_V ~ +175e-6/K ("giant") | arXiv:2209.10087, Abstract, ueber DREIECK-PUMPE-L ARBEITSFELD Z. 304 bis 307 [P, dort S] | nein (grosse positive Grueneisen-Parameter weicher Moden) |
| SiO2 Quarz | beta | ueber 1400 K | leicht negativ | Bourova/Richet 1998, Abstract (A4) [S] | nicht im Abstract |
| alpha-ZrW2O8 | alpha (kubisch) | 2 bis 350 K | **alpha = -9,07e-6/K** | Evans/David/Sleight 1999, Acta Cryst. B, Abstract (A9) [S] | ja: Pryde u. a. 1997 (A9) und Tucker u. a. 2005 (A8) [S]; im Bauteil bestritten von Cao u. a. 2002 und Bridges u. a. 2014 (A8) [S] |
| alpha-ZrW2O8 | alpha | 2 bis 300 K | alpha_l = -9,1e-6/K | Evans 2000, JJAP 39 S1, 535, Abstract (A9) [S] | Ursache "low energy phonon modes with negative Gruneisen parameters" [S] |
| ZrW2O8 | alpha und beta | 0,3 K bis ~1050 K | negativ, isotrop (keine Zahl im Abstract) | Mary/Evans/Vogt/Sleight 1996, Science 272, 90, Abstract (A8) [S] | nicht im Abstract |
| ScF3 | - | - | NTE, keine Zahl gelesen | Dove u. a. 2020, PRB 102, 094105, Abstract (A15) [S] | **teilweise**: RUM und oktaederverformende Moden |

Offen: Ordnungsuebergang in ZrW2O8 bei 430 K (Pryde 1997) bzw. 448 K (Evans 2000). Die Angaben weichen ab und sind
nicht aufgeloest.

## 6. Urteile AV1 bis AV4 (nach Kartenwortlaut)

| Nr | Vorhersage (Karte) | Wahrsch. | Urteil | Beleg |
|---|---|---|---|---|
| AV1 | [L?] Die P2_13-Schar aus ISO-ATEM-1 entspricht dem Cristobalit-Modell von Wright/Leadbetter (P2_13) | 70 % | **verfehlt** | Wright/Leadbetter 1975 schlagen "domains of 'ideal' cristobalite (space group I-42d) ... in six different orientations" vor, kein P2_13 [S, A5]. Coh/Vanderbilt bestaetigen I-42d [S, A1 Txt Z. 53 bis 55, 115 bis 124]. Ihr Modell entspricht ISO-ATEM-1 Teil A (anisotrop), nicht der P2_13-Schar. Ob die P2_13-Schar Barths Modell von 1932 ist: mit meinen Abrufen nicht entscheidbar [L?] |
| AV2 | [L?] Die 222-Form ist in der Literatur als Kipp-Variante des Cristobalits bekannt (gleich welcher Name) | 45 % | **teilweise** | Bekannt ist die Familie: exakt starre 3D-Schar mit P2_12_12_1-Symmetrie, je X-Punkt eine, mit alpha-tilde und beta-tilde als Sonderfaellen [S, A1 Txt Z. 502 bis 513, 738 bis 757]. Die 222-Form passt in Drehteil-Gruppe, Zelle und Zahl der Ausrichtungen [P, G1] und in der Zaehlung (3D minus 2 Bedingungen = Kurve) [ES]. Den isotropen Ast beschreibt keine Quelle; die Zuordnung ist nicht gerechnet. Name bei Coh/Vanderbilt: P2_12_12_1-Strukturen (alpha1, alpha1', beta1) |
| AV3 | [H] Eine vollstaendige Abzaehlung der endlichen Kipp-Varianten mit starren Tetraedern gibt es in der Literatur nicht; bekannt sind nur einzelne Varianten und die infinitesimale RUM-Zaehlung | 55 % | **teilweise** | Erster Teil: Fuer die Zelle mit 8 Tetraedern habe ich keine Vollzaehlung gefunden (A1, A12, A13, A14). Fuer die primitive Zelle gibt es sie aber geschlossen: SO(3) [S, A14 Theorem 2]. Zweiter Teil falsch: Neben Einzelvarianten sind ganze starre Scharen bekannt (Coh/Vanderbilt 3D [S]). Dazu kommen die systematische Kleinwinkel-Zaehlung (Eggers u. a. 2024 [S, A12]) und ein erster systematischer Grosswinkel-Algorithmus (Campbell u. a. 2025 [S, A12]) |
| AV4 | [L?] Beta-Cristobalit hat einen kleinen bzw. negativen Waermeausdehnungskoeffizienten, und die negative Waermeausdehnung verwandter Gerueste wird durch RUM erklaert | 60 % | **eingetroffen** | Klein: Im Mittel 750 bis 2000 K null (\|alpha_V\| <= 1,5e-6/K) [E aus S, A4]; je Phase nur langsame, stetige Aenderung der Gitterparameter [S, A5]. Negativ: ueber 1300 K [S, A4]. RUM-Erklaerung: Pryde u. a. 1997, Tucker u. a. 2005, Theorie Heine u. a. 1999 [S, A8, A9, A15]. Vorbehalte: Bis 1300 K ist die Ausdehnung positiv. Bei ZrW2O8 ist das beteiligte Bauteil umstritten (Cao 2002, Bridges 2014), bei ScF3 erklaeren RUM die NTE nicht allein (Dove 2020) |

**Bedeutung nach der Vorab-Festlegung der Karte:**
- "AV1 und AV4 treffen ein" ist **nicht** ausgeloest, weil AV1 verfehlt ist. Der Materialanker steht trotzdem, aber
  nur ueber AV4 (siehe Abschnitt 7).
- "AV3 trifft ein" ist nur teilweise ausgeloest. Der Kartenvorschlag in Abschnitt 8 ist enger zugeschnitten als in N8.

## 7. Bedeutung fuer Finns "Atmen" [H] und der Negativlisten-Satz

**[H] Finns Atmen im echten Material, als Materialanalogie und nicht als Beleg fuer den Raum:**
- **Statisch, beim Uebergang:** Unter etwa 533 K ist das Netz mit gekippten Tetraedern eingefroren (alpha). Beim
  Erwaermen loest sich die feste Kippung, und das Netz wird sprunghaft etwa 5 % groesser [S]. Das ist ISO-ATEM-1s
  Atemkurve rueckwaerts gelaufen, also zurueck Richtung Ideallage [ES].
- **Dynamisch, in beta:**
  - Die Tetraeder kippen thermisch hin und her (weiche Kippmoden, Swainson/Dove 1993 [S]).
  - Jede Kippung verkleinert das Volumen; das ist der negative geometrische Beitrag (Heine u. a. 1999 [S]).
  - Die Bindungen dehnen sich und geben den positiven Beitrag.
  - Netto ist das bis 1300 K leicht positiv, darueber gewinnt das Zusammenziehen [S, Bourova/Richet].
- **Wie weit das echte beta schon "ausgeatmet" ist [E aus S, Methoden gemischt]:**
  - Gemessenes a = 7,131 A [S, A1 Tab. I] gegen die DFT-Idealzelle 7,444 A ergibt lambda = 0,958 und
    V/V0 = 0,879. Nach ISO-ATEM-1s cos^2-Gesetz entspraeche das einem mittleren Kippwinkel um 20 Grad [H].
  - DFT-Gitter sind oft um etwa 1 % zu gross [L?]. Mit dieser Korrektur waere lambda etwa 0,968 und der Winkel etwa
    18 Grad.
  - ISO-ATEM-1 L5 vermutete nur [L?], dass beta eine kleinere Zelle als die Idealform hat [P]. Mit lambda etwa 0,96
    bis 0,97 ist das jetzt belegt, allerdings mit gemischten Methoden.
- **Grenzen:**
  - Im echten Material ist das Atmen statisch anisotrop (alpha: c/(sqrt 2 a) = 0,983) und nur im Mittel isotrop
    (beta: Mittel ueber Domaenen bzw. Fluktuationen) [S, ES].
  - Weder P2_13 noch die 222-Form ist als statische Phase von SiO2 belegt.
  - Starres Atmen kann das Netz nie ueber die Ideallage hinaus vergroessern [S]. "Wachsen" heisst in Finns Bild also
    "zurueck zur Ideallage".

**Der Satz aus der Negativliste R43 lautet jetzt richtig:**
- "Cristobalit **waechst** beim Erwaermen durch den alpha-beta-Uebergang (nahe 533 K) sprunghaft um etwa 5 %
  Volumen (Schmahl u. a. 1992; etwa 4 % bei Leadbetter/Wright 1976) [S].
- In der beta-Phase bleibt das Volumen fast gleich: Es steigt bis etwa 1300 K und faellt bis 2000 K auf den Wert von
  750 K zurueck (Bourova/Richet 1998) [S]. **Nur oberhalb von etwa 1300 K schrumpft beta-Cristobalit beim
  Erwaermen.**
- Dass die Kippungen (RUM) dabei den negativen Beitrag liefern, ist Theorie (Heine u. a. 1999) und Simulation
  (Huang/Kieffer 2003), fuer beta-Cristobalit nicht direkt gemessen."
- Kurzform: "beta-Cristobalit dehnt sich im Mittel nicht aus und schrumpft erst ueber ~1300 K; beim alpha-beta-
  Uebergang waechst er um ~5 %."

## 8. Kartenvorschlag (einer)

### ATEM-VOLLZAEHLUNG-1 (neu zugeschnitten): Gibt es in der kubischen 8-Tetraeder-Zelle eine dritte isotrope Atemform?

- **Frage:** Gibt es ausser P2_13 und dem isotropen Ast der P2_12_12_1-Schar eine dritte isotrope Form? Wenn es eine
  gibt: Mischt sie zwei oder drei X-Arme anders als P2_13, oder hat sie niedrigere Symmetrie (P2_1, R3, P1)?
- **Weg:**
  1. Lineare RUM der Zelle (3 bei Gamma, 2 an jedem X-Punkt, zusammen 9 [ES nach Coh/Vanderbilt]) mit Irreps. Das
     kann man von Hand machen oder mit dem BYU-Werkzeug ISOTILT; dessen Existenz kenne ich nur aus einem Suchtreffer
     (A13), nicht von der Quelle. Netzzugriff ist dann ein Abruf.
  2. Die Unterraeume bestimmen, die zu endlichen Winkeln fortsetzbar sind. Laut Campbell u. a. 2025 ist der
     Tangentenkegel eine Vereinigung solcher Unterraeume.
  3. Je Isotropie-Untergruppe von Fd-3m mit k aus {Gamma, X} und metrisch isotropem Gitter ein Polynomsystem in
     Quaternionen und lambda aufstellen. Wenige Unbekannte: Resultante bzw. Groebner-Basis. Mehr Unbekannte:
     zertifizierte Homotopie (Hills Weg, CONNOR-HALL-L N8).
- **Ableitbarkeitsprobe:**
  - Vorab ableitbar, also nur Kontrollen:
    - die primitive Zelle hat keine isotrope Form (Borcea/Streinu Theorem 2 plus eine Zeile [M]);
    - die P2_13-Schar (Handformel);
    - die Existenz der 222-Form (ISO-ATEM-1).
  - Erste Schreibtischstufe vor jeder Rechnung: die Coh/Vanderbilt-Parametrisierung (alpha1, alpha1', beta1)
    nachbauen und zeigen, dass ihre isotrope Kurve bei lambda = 0,97 den Winkel 17,2539 Grad gibt. Gelingt das, wird
    AV2 von [ES] zu [E].
  - Nicht ableitbar: Komponenten der starren Menge, die X-Arme anders als P2_13 mischen, und deren isotrope Teile.
- **Ausgaenge:**
  - Bestehensarm: genau zwei Arten in allen gerechneten Untergruppen.
  - Fehlerarm: eine dritte Form.
  - Beide sind moeglich. Grenze: "keine dritte in den gerechneten Untergruppen" heisst nicht "keine".
- **Aufwand:** Schreibtisch 2 bis 3 h (Untergruppenliste, Parametrisierung). Rechnung: kleine Polynomsysteme, Minuten
  auf der .69-Kleintest-Spur, keine GPU noetig. Zusammen etwa ein halber Tag.
- **Bezug:** modellintern. Keine Messgroesse haengt daran; der Materialbezug laeuft nur ueber die Analogie aus
  Abschnitt 7 [H].

## 9. Negativliste (Saetze, die wir nicht behaupten duerfen)

1. "Wright/Leadbetter haben das P2_13-Modell vorgeschlagen." Falsch: Sie schlugen I-42d-Domaenen vor [S].
2. "Cristobalit schrumpft beim Erwaermen." Stimmt nur fuer beta ueber etwa 1300 K. Durch den alpha-beta-Uebergang
   waechst er um etwa 5 %.
3. "beta-Cristobalit hat negative Waermeausdehnung." Nur ueber etwa 1300 K; im Mittel 750 bis 2000 K ist sie null.
4. "Die 222-Form ist in der Literatur beschrieben." Beschrieben ist nur die Familie (P2_12_12_1-Schar). Der isotrope
   Ast ist es nicht, und die Zuordnung ist [ES].
5. "Fuer endliche Kippungen gibt es keine systematische Methode." Seit 2025 gibt es einen ersten Algorithmus
   (Tagungsabstract); fuer die primitive Zelle ist der Raum geschlossen bekannt.
6. "Coh/Vanderbilt zeigen, dass Kippungen verschiedener X-Punkte nie starr kombinierbar sind." Sie sagen das fuer
   Paare in Z = 4-Zellen. P2_13 (alle drei X-Punkte) ist exakt starr.
7. "Die NTE von ZrW2O8 ist durch RUM bewiesen." RUM sind die Standarddeutung; das beteiligte Bauteil ist umstritten.
8. "Echter beta-Cristobalit atmet isotrop wie P2_13." Kubisch ist nur das Mittel; lokal gibt es I-42d- bzw.
   alpha-artige Domaenen oder Fluktuationen.
9. "Starre Tetraeder koennen das Netz ueber die Ideallage hinaus wachsen lassen." Nein, Kippungen verkleinern nur.
10. "Mary u. a. 1996 geben -8,7e-6/K an." Im Abstract steht keine Zahl. -9,07e-6/K stammt von Evans/David/Sleight 1999.
11. "Der RUM-Anteil an der Ausdehnung von beta-Cristobalit ist gemessen." Nach meinem Stand gibt es dafuer nur Theorie
    und Simulation.

## 10. Selbstanzeigen

1. **A10:** http statt https und curl ohne -L. Ein Abruf ging ohne Inhalt verloren (eigener Fehler).
2. **A6, A7:** Verlagsseiten (IUCr, Springer) sperren curl; zwei Abrufe ohne Inhalt. O'Keeffe/Hyde 1976 und
   Hatch/Ghose 1991 sind deshalb nur Sekundaerzitate bzw. [L?].
3. **Zeitangabe A2** in ABRUFE.md zuerst geschaetzt ("09:08:5x"). Gestrichen und durch die date-Klammer
   09:08:45 bis 09:09:16 ersetzt. Bei A13 steht ebenfalls nur eine date-Klammer.
4. **Werkzeuge:**
   - jq habe ich zum Lesen benutzt und dabei die Ausgabe in drei Textdateien umgeleitet (A9-, A12-,
     A15-abstracts.txt: aus dem invertierten OpenAlex-Index rekonstruierte Abstracts). Das ist mehr als reines Lesen.
   - pdftotext fuer zwei arXiv-PDFs.
   - tr, fold, paste, wc und ls nur zur Anzeige.
   - Kein python, awk oder perl.
5. **Rechnungen nur von Hand, nicht gegengelesen:** Rundungsschranke 1,5e-6/K, Verhaeltnisse aus Tabelle I,
   lambda = 0,958, cos-Rueckrechnung auf etwa 20 Grad, P2_13-Zerlegung in X-Moden, F = (R + I)/2.
6. **Methoden gemischt:** Das lambda des echten beta vergleicht ein Experiment mit einer DFT-Idealzelle; es gibt nur
   die Groessenordnung.
7. **Lokal gelesen, nicht auf der Vorleseliste:** ISO-ATEM-1 nachtrag-69/diag-c.json und quellen/A2 sowie
   DREIECK-PUMPE-L ARBEITSFELD. Nur gelesen.
8. **OpenAlex-Abstracts** koennen bei der Rekonstruktion Formeln verlieren (Tucker 2005). Woertlichkeit nicht
   geprueft (G6).
9. **Die Projektsuche** um 09:03:20 lief ueber coordination und model-lab mit den Pflicht-Ausschluessen plus
   --exclude-dir=.git.
10. **Suchtreffer** (A2, A13) habe ich nicht als Quelle verwendet. Der Satz zum fallenden beta-Koeffizienten bei
    Schmahl stand nur im Suchtext und bleibt unbelegt.
11. **mkdir quellen/** im eigenen Ordner.
12. **Zeitbox:** Abgabe 2026-10-05 09:32:10 CEST (date, beim Schreiben dieser Zeile gemessen); Zeitbox bis 10:00:40 eingehalten.
13. **Urheberrecht nachgebessert:** Mehrfach- und Langzitate in Dossier und Arbeitsfeld durch Paraphrasen ersetzt.
    Die Fassung des Arbeitsfelds davor liegt in quellen/ARBEITSFELD-vor-Paraphrase.bak (statt Loeschen). Dafuer
    habe ich sed -i auf meine eigenen Dateien angewandt.

## 11. Einfach gesagt

Finns Tetraedernetz kann auf zwei Arten gleichmaessig schrumpfen, ohne dass ein Tetraeder sich verbiegt. Die eine
Art liess sich schon von Hand ausrechnen; die andere gehoert sehr wahrscheinlich zu einer Familie von
Zwischenformen, die Fachleute 2008 beschrieben haben. Eine vollstaendige Liste aller Formen fuer genau diese Zelle
habe ich nicht gefunden, die Werkzeuge dafuer gibt es aber seit kurzem. Echter Cristobalit tut beim Erwaermen fast
das Gegenteil von Schrumpfen: Bei etwa 260 Grad Celsius wird er sprunghaft 5 % groesser, danach bleibt seine Groesse
fast gleich, und erst sehr heiss (ueber 1000 Grad Celsius) zieht er sich wieder etwas zusammen. Dass die kippenden
Tetraeder dabei bremsen, ist eine gut begruendete Erklaerung, fuer Cristobalit aber nicht direkt gemessen.

## Anhang A: Offene Fragen

- Q1': Liegt die 222-Form exakt in der Coh/Vanderbilt-Schar? (erste Stufe des Kartenvorschlags)
- Q2': Ist Barths P2_13-Modell von 1932 dasselbe wie die starre P2_13-Schar?
- Q3': Lokale Koeffizienten von beta zwischen 750 und 1300 K und zwischen 1300 und 2000 K. Moegliche Quellen: Volltext
  Bourova/Richet; Stokes 2024 (J. Am. Ceram. Soc., Abstract ohne Zahl).
- Q4: Wurde der Grosswinkel-Algorithmus (Campbell u. a. 2025) auf Cristobalit angewandt, und gibt es einen Volltext?
- Q5: Ist die Coh/Vanderbilt-Schar die ganze starre Menge der Z = 4-Zelle?
- Q6: Welche Untergruppen listet Hatch/Ghose 1991 (gesperrt)?
- Q7: Gibt es eine direkte Messung des RUM-Anteils an der beta-Ausdehnung, etwa scheinbares gegen wahres Si-O aus
  Totalstreuung (Dove u. a. 1997, Tucker u. a. 2001, nur [L?])?

## Anhang B: Quellen (gelesen, mit Stelle; Abrufnummer)

- Coh, S.; Vanderbilt, D. (2008): Structural stability and lattice dynamics of SiO2 cristobalite. Phys. Rev. B 78,
  054117. https://arxiv.org/abs/0806.3737 (Volltext v2, A1)
- Borcea, C. S.; Streinu, I. (2011): Deformations of crystal frameworks. https://arxiv.org/abs/1110.4661 (Volltext,
  A14)
- Wright, A. F.; Leadbetter, A. J. (1975): The structures of the beta-cristobalite phases of SiO2 and AlPO4. Phil.
  Mag. 31, 1391. https://doi.org/10.1080/00318087508228690 (Abstract ueber OpenAlex, A5)
- Leadbetter, A. J.; Wright, A. F. (1976): The alpha-beta transition in the cristobalite phases of SiO2 and AlPO4.
  I. X-ray studies. Phil. Mag. https://doi.org/10.1080/14786437608221095 (Abstract, A5)
- Schmahl, W. W.; Swainson, I. P.; Dove, M. T.; Graeme-Barber, A. (1992): Landau free energy and order parameter
  behaviour of the alpha/beta phase transition in cristobalite. Z. Krist. 201, 125-145.
  https://epub.ub.uni-muenchen.de/18597/ , DOI 10.1524/zkri.1992.201.1-2.125 (Abstract, abgeschnitten, A3)
- Bourova, E.; Richet, P. (1998): Quartz and cristobalite: high-temperature cell parameters and volumes of fusion.
  Geophys. Res. Lett. https://doi.org/10.1029/98gl01581 (Abstract ueber OpenAlex W2084086935, A4)
- Stokes, J. L. (2024): beta-Cristobalite thermal expansion and stability in environmental barrier coating systems.
  J. Am. Ceram. Soc. https://doi.org/10.1111/jace.20214 (Abstract, ohne Zahl, A4)
- Mary, T. A.; Evans, J. S. O.; Vogt, T.; Sleight, A. W. (1996): Negative thermal expansion from 0.3 to 1050 Kelvin
  in ZrW2O8. Science 272, 90. https://doi.org/10.1126/science.272.5258.90 (Abstract, A8)
- Evans, J. S. O.; David, W. I. F.; Sleight, A. W. (1999): Structural investigation of the negative-thermal-expansion
  material ZrW2O8. Acta Cryst. B. https://doi.org/10.1107/s0108768198016966 (Abstract, A9)
- Evans, J. S. O. (2000): Negative thermal expansion materials. Jpn. J. Appl. Phys. 39 S1, 535.
  https://doi.org/10.7567/jjaps.39s1.535 (Abstract, A9)
- Pryde, A. K. A.; Hammonds, K. D.; Dove, M. T.; Heine, V.; Gale, J. D.; Warren, M. C. (1997): Rigid unit modes and
  the negative thermal expansion in ZrW2O8. Phase Transitions. https://doi.org/10.1080/01411599708223734 (Abstract, A9)
- Tucker, M. G.; Goodwin, A. L.; Dove, M. T.; Keen, D. A.; Wells, S. A.; Evans, J. S. O. (2005): Phys. Rev. Lett. 95,
  255501. https://doi.org/10.1103/physrevlett.95.255501 (Abstract, A8)
- Cao, D.; Bridges, F.; Kowach, G. R.; Ramirez, A. P. (2002): Frustrated soft modes and negative thermal expansion in
  ZrW2O8. Phys. Rev. Lett. 89, 215902. https://doi.org/10.1103/physrevlett.89.215902 (Abstract, A8)
- Bridges, F. G.; Keiber, T.; Juhas, P.; Billinge, S. J. L.; Sutton, L.; Wilde, J. M.; Kowach, G. R. (2014): Local
  vibrations and negative thermal expansion in ZrW2O8. Phys. Rev. Lett. 112, 045505.
  https://doi.org/10.1103/physrevlett.112.045505 (Abstract, A8)
- Swainson, I. P.; Dove, M. T. (1993): Low-frequency floppy modes in beta-cristobalite. Phys. Rev. Lett. 71, 193.
  https://doi.org/10.1103/physrevlett.71.193 (Abstract, A8)
- Heine, V.; Welche, P. R. L.; Dove, M. T. (1999): Geometrical origin and theory of negative thermal expansion in
  framework structures. J. Am. Ceram. Soc. https://doi.org/10.1111/j.1151-2916.1999.tb02001.x (Abstract, A15)
- Huang, L.; Kieffer, J. (2003): Molecular dynamics study of cristobalite silica using a charge transfer three-body
  potential. J. Chem. Phys. https://doi.org/10.1063/1.1529684 (Abstract, A15)
- Dove, M. T.; Du, J.; Wei, Z.; Keen, D. A.; Tucker, M. G.; Phillips, A. E. (2020): Quantitative understanding of
  negative thermal expansion in scandium trifluoride from neutron total scattering measurements. Phys. Rev. B 102,
  094105. https://doi.org/10.1103/physrevb.102.094105 (Abstract, A15)
- Campbell, B. J.; Eggers, B. T.; Stokes, H. T. (2025): Large-angle rigid unit modes in crystalline frameworks. Struct.
  Dyn. (Tagungsabstract). https://doi.org/10.1063/4.0000587 (A12)
- Eggers, B. T.; Stokes, H. T.; Campbell, B. J. (2024): Small-angle rigid-unit modes requiring linear strain
  compensation. Acta Cryst. A. https://doi.org/10.1107/s205327332401163x (Abstract, A12)
- Kastis, E.; Kitson, D. (2026): The Rigid Unit Mode spectrum for symmetric frameworks. J. Math. Anal. Appl.
  https://doi.org/10.1016/j.jmaa.2026.131029 (Abstract, A12)
- Shcheblanov, N. S.; Lemaitre, A. (2026): Vibrational spectrum of vitreous silica: rigorous decomposition via
  recursive orthogonal splitting analysis. https://doi.org/10.1103/lnlg-ldlk (Abstract, A12)
- Nur Metadaten oder gesperrt:
  - Barth, T. F. W. (1932): The cristobalite structures. https://doi.org/10.2475/ajs.s5-23.136.350 (A5)
  - Hatch, D. M.; Ghose, S. (1991). https://doi.org/10.1007/bf00202234 (A7 gesperrt; Seitenzahl bei Coh/Vanderbilt
    "17, 544")
  - O'Keeffe, M.; Hyde, B. G. (1976). https://doi.org/10.1107/s0567740876009308 (A6 gesperrt)
- Suchtreffer, keine Quelle (A2, A13): https://earthref.org/ERR/18636 , https://iso.byu.edu/isotilt.php ,
  https://stokes.byu.edu/iso/2021%20Campbell%20a.pdf
- Projekt [P]:
  - RUNDE-37/iso-atem-1/ERGEBNIS.md (Abschnitte 1 bis 5) und nachtrag-69/diag-c.json.
  - RUNDE-37/dreieck-pumpe-l/ARBEITSFELD.md Z. 296 bis 312 (BeF2, arXiv:2209.10087).
  - RUNDE-34/eis-1/ERGEBNIS.md Z. 104 bis 105.
  - RUNDE-42/SCHALTER-UND-ATMEN.md Z. 179.
  - RUNDE-43.md Z. 26.
  - RUNDE-37/connor-hall-l/DOSSIER.md N8.
