# ERGEBNIS DUNKEL-ZEIT (Runde 22): Zusatzdimension, Dark Dimension, Zeit aus den Teilen, Uhren und Felder

- Literatur-Agent (feldforscher) im Auftrag von claude-primary.
  - Agentenstart 2026-10-02 20:37:37 CEST, Schreibbeginn dieses Berichts 21:02:07 CEST (beides date).
- Arbeitsdatei: `ARBEITSFELD.md` (gleicher Ordner). Sie enthaelt jede Erwartung vor dem Abruf, jeden Ausgang und alle
  Zeiten.
- Quellkopien in `quellen/`:
  - Volltexte als PDF und als pdftotext-Text: MVV 2022, Langhoff 2026, Lee/Randall/Riojas 2026, Adelberger/Heckel/
    Nelson 2003, Demir 2000, Abel/Kehagias 2015, Bianchi u. a. 1996, Tong 2009, CDT-Uebersicht 2012
  - API-Antworten als XML (`api-*.xml`)
- Marken:
  - [S] selbst gelesen: Volltext-Stelle oder Abstract im Wortlaut aus der arXiv-API, jeweils angegeben
  - [L?] nur Titel, Metadaten oder Zitat
  - [H] eigene Schlussfolgerung
  - [E] Kopfrechnung mit hbar c = 1,973e-7 eV m und h = 4,136e-15 eV s
- Fehlanzeigen gelten nur nach Recherchestand.

---

## 1. Ergebnis zuerst (5 Punkte)

1. **D1 offen: Die Vorhersage ist wie erwartet, der Status ist seit dieser Woche strittig.**
   - Montero/Vafa/Valenzuela (MVV) sagen genau eine Zusatzdimension von l ~ 0,1-10 um voraus, Casimir-Schaetzung
     7,4 um [S Volltext]. Das liegt unter der Laborgrenze, die fuer diesen Fall gilt: ~30 um bei alpha = 8/3. Die
     38,6 um gelten fuer |alpha| = 1.
   - Zwei neue Preprints greifen das an [S Volltext]:
     - Langhoff (01.10.2026) schliesst eine flache Dark Dimension mit R >~ 0,2 um aus, egal woraus die Dunkle Materie
       besteht.
     - Lee/Randall/Riojas (28.09.2026) zeigen: Die Zerfallskaskade, die das Dunkle-Materie-Szenario braucht, ist um
       etwa 1e-24 unterdrueckt.
     - Beide sind unbegutachtet. Eine Gegenrede habe ich bis 01.10. nicht gefunden.
   - Eine dritte Variante dreht das Vorzeichen um: Im Modell der dunklen Blase wird die Gravitation bei um schwaecher,
     nicht staerker (Danielsson/Giri 2026) [S Abstract].
2. **D3 eingetroffen.** Uhren begrenzen ein ueberall schwingendes Skalarfeld stark.
   - Die Th-229-Kernuhr erreicht Wechselwirkungsskalen ueber 1e6 Planck-Skalen (Arakawa u. a. 2026); dazu optische Uhren
     (Filzinger u. a. 2023) [S Abstract].
   - Blinder Fleck: Ein Feld, das alle Uhren gleich verstellt, sehen Uhrvergleiche nicht; das sieht man nur ueber
     Gravitation und Pulsare [S Abstract Duff 2002, Smarra u. a. 2024; H].
3. **D2 eingetroffen.**
   - Page-Wootters ist an zwei Photonen vorgefuehrt (Moreva u. a. 2014); sonst ist es Theorie.
   - Pruefbar sind nur Effekte von Uhren in Quantenueberlagerung (Quanten-Zeitdilatation). Sie sind noch nicht
     gemessen, laut PRL 136, 163602 (2026) aber mit Ionenuhren "within reach" [S Abstract].
   - Fuer das Entstehen der Raumzeit selbst habe ich keine pruefbare Vorhersage gefunden.
4. **D4 eingetroffen, mit Vorbehalt.** Die KK-Lesart der Q-Ball-Phase ist ausgearbeitete Literatur [S Volltext]:
   - Demir 2000: Die Ladung ist der Impuls in der Zusatzdimension, die Masse je Ladung liegt unter 1/R.
   - Bei flachem Potential gilt dort M ~ Q^(3/4), dasselbe Gesetz wie unser Beutelgesetz.
   - Fuer unser Modell ohne kompakte Richtung folgt daraus nichts Neues. Neue Aussagen entstehen erst als
     Modellerweiterung: KK-Turm, Obertoene, Gregory-Laflamme-Instabilitaet (Herdeiro/Radu 2025).
5. **Bedeutung gemaess Karte: Sie greift nur zur Haelfte.**
   - Die Uhren-Seite von Finns Idee ist messbar, stark begrenzt und offen.
   - Die Kurzabstands-Seite bleibt unsicher, bis die neuen Arbeiten geklaert sind. Haelt Langhoff, liegt das Signal bei
     <= 0,2 um. Mit Gravitationsstaerke ist es dann im Labor auf absehbare Zeit nicht pruefbar, eher ueber
     MeV-Gamma-Astronomie [H].
   - Fuer unser Modell [H]: Eine einzelne Q-Ball-Phase ist unbeobachtbar, denn die Dichte eines exakten Balls steht
     still. Erst die Schwebung zweier Baelle ist eine Uhr. Das ist woertlich "Zeit aus Bewegungsdifferenz". Vier Tests
     stehen in Abschnitt 5.

---

## 2. Erwartungsverstoesse (das eigentliche Ergebnis; wichtigster zuerst)

| Nr | Erwartung vorab (ARBEITSFELD Abschnitte 2 und 3) | Was stattdessen kam | Korrektur |
|---|---|---|---|
| V1 gross | D1: Dark Dimension "nicht widerlegt"; mein Vorab-Bild: nichts Neues | Langhoff 2610.01825 (01.10.2026): "This excludes the existence of a flat dark dimension with R >~ 0.2 um" [S Volltext]. Lee/Randall/Riojas 2609.36234 (28.09.2026): "can be used to rule out existing Dark Dimension models" [S Abstract-Wortlaut] | D1-Status "strittig". Der Ausschluss stuetzt sich nicht auf Kurzabstandsmessungen, sondern auf: Theorie (d-Wellen-Zerfall, Rate ~ p^5), MeV-Gamma-Daten und Reheating >= 6 MeV (BBN, CMB+BAO) |
| V2 mittel | Abweichung bei um heisst: Gravitation wird staerker (KK-Yukawa) | Danielsson/Giri 2606.20942: "a fading of the gravitational force at micron distances" [S Abstract] | Das Vorzeichen haengt an der Realisierung: flacher Bulk mit Brane gegen dunkle Blase. Dieselbe Luecke wie in STELLE-24M: Lee 2020 zeigt nur \|alpha\| |
| V3 mittel | Zu KK-Q-Baellen wenig Literatur; kaum etwas deutet die Phase als Bewegung in einer Zusatzdimension | Demir 2000, Gl. (8): Felder "rotate in the internal space with velocities proportional to their U(1)_KK charge" [S Volltext]. Abel/Kehagias 2015: KK-Turm von Q-Baellen; die Scherk-Schwarz-Verdrillung koppelt Phase an Impuls [S Volltext]. Herdeiro/Radu 2025: Gregory-Laflamme-Instabilitaet [S Abstract] | D4 gilt weiter fuer das jetzige Modell. Die Lesart ist aber Literatur mit eigenen Vorhersagen, sobald man die Dimension ernst nimmt |
| V4 mittel | Zu periodischen Uhren nichts erwartet | Chataignier/Hoehn/Lock/Mele, NJP 28, 034504 (2026): "counting winding numbers does not lead to invariant observables" [S Abstract] | Fuer Frage 6: Q-Ball-Phase und Schwebung sind periodische Uhren und liefern ohne aeussere Zeit keine monotone Zeit. Im Code gibt es t; die Tests pruefen also Regelmaessigkeit, nicht das Entstehen von Zeit |
| V5 mittel, positiv | Synchronisation von Solitonen durch ein Hintergrundfeld kaum untersucht | Gleiser/Howell (hep-ph/0209176): Synchronisation getrieben von "resonant parametric oscillations of the field's zero mode" [S Abstract]. Copeland/Saffin/Zhou 2014: Ladungstausch-Q-Baelle tauschen "at a frequency lower than the natural frequency" [S Abstract] | Beide Testideen der Karte haben Vorlaeufer. T3 in Abschnitt 5 nutzt den Ladungstausch |
| V6 klein | MVVs Grenze fuer n = 1 stammt aus Neutronensternen | MVV schreiben "l < 44 um" der Neutronenstern-Heizung zu. 44 um ist Kapners Laborschranke (PRL 98, 021101) [S Abstract]. Hardy u. a. 2025: Sternschranken fuer n = 1 sind "weaker than those from laboratory searches" [S Abstract] | Verwechslung bei MVV [H]; fuer ihr Argument folgenlos |
| V7 klein | D1-Bereich 1-10 um | MVV: 0,1-10 um (Gl. 3.8) [S]. Die Dunkle-Materie-Variante (Law-Smith u. a. 2024) nennt "around 1 - 30 um" [S Abstract] | Die DM-Variante reichte bis an die Torsionswaagen-Grenze |
| V8 klein | Quanten-Zeitdilatation ist weit vom Labor entfernt | Sorci/Foo/Leibfried/Sanner/Pikovski, PRL 136, 163602 (2026): Ionenuhren mit gequetschter Bewegung sind "within reach" [S Abstract] | D2 bleibt eingetroffen, aber die Pruefbarkeit liegt naeher |
| V9 klein | arXiv:2609.22501 ist eine Kurzabstands-Projektion fuer die Dark Dimension (aus STELLE-24M uebernommen) | Die Arbeit behandelt gravitationsinduzierte Verschraenkung in Stelle-Gravitation, Signal ab 0,0197 eV bei ~40 um [S Abstract] | Fuer diese Karte nur eine Randnotiz |

**Selbstkorrekturen im Lauf** (protokolliert, gestrichen statt geloescht):
- Eine Lesart aus Langhoffs zweispaltigem Text ("der Benchmark lag unter 1 um") war ein Fehlschluss aus vermischten
  Spalten.
- Ein Autorenname war geraten.
- Zwei Uhrzeiten waren von Hand geschaetzt.

---

## 3. Antworten auf die Fragen

### Frage 1: Zusatzdimension und Ladung (Kaluza-Klein)

- **Grundbild [L?]:** Bei Kaluza-Klein erscheint Impuls in einer kompakten Richtung im 4D-Bild als Masse und als
  U(1)-Ladung. Uebersicht: Overduin/Wesson, Phys. Rep. 283, 303 (1997); davon nur das Abstract gelesen.
- **Die Lesart ist fuer Q-Baelle ausgearbeitet [S]:**
  - Demir, PLB 495, 357 (2000), Volltext:
    - Die U(1) ist "generated by translations along S^1" (Gl. 5).
    - Die KK-Niveaus eines Q-Balls "rotate in the internal space with velocities proportional to their U(1)_KK charge"
      (Gl. 8).
    - Stabil ist der Ball, wenn die Masse je Ladung unter 1/R bleibt.
    - Bei flachem Potential gilt "M_Q ~ Q^(3/4) rather than Q". Das ist dasselbe Gesetz wie unser Beutelgesetz
      E ~ Q^(3/4) (RUNDE-17).
  - Abel/Kehagias, JHEP 11 (2015) 096, Volltext Z. 58-90 und 495-522:
    - Q-Baelle tragen die globale Ladung Q und zusaetzlich KK-Impuls P5 = Q p + n/R. Daraus folgt ein Turm
      E^2(P5) = E^2(0) + P5^2.
    - Grosse Baelle sind "blind to the compactness of the extra dimension".
    - Die Scherk-Schwarz-Phase p, "non-integer momentum per unit charge", laesst die innere Phase entlang der
      Zusatzdimension winden.
  - Herdeiro/Radu, arXiv:2503.15069 (2025) [S Abstract]: Q-Ball bzw. Bosonstern mal Kreis der Laenge L. Gleichfoermige
    "Bosonstrings" werden oberhalb eines kritischen L instabil, nach Art von Gregory-Laflamme.
- **Wo die Analogie traegt [E/H]:**
  - Schreibt man den Q-Ball als 5D-Welle phi ~ f(x) e^(i(y/R - omega t)), laeuft das Phasenmuster mit der
    Geschwindigkeit omega R um den Kreis (c = 1). Bei Demir gilt das fuer alle Niveaus gleich: n omega / (n/R).
  - Gebunden heisst bei masselosem 5D-Feld omega < 1/R, also: Das Muster laeuft langsamer als das Licht um.
- **Wo sie bricht [H]:**
  - Bei uns ist die Phase eine Drehung im Feldraum, also eine globale innere Symmetrie. KK verlangt eine
    Raumzeit-Richtung mit Metrik. Damit kaemen hinzu:
    - ein Turm weiterer Niveaus (n = 2, 3, ... mit Massen n/R)
    - ein Radion fuer die Groesse der Dimension
    - mit Gravitation ein Eichfeld fuer diese U(1), das Graviphoton [L?; im Q-Ball-Zusammenhang keine Fundstelle]
  - Bei Demir koppeln Niveaus, deren Indizes sich zu null addieren (phi_n phi_k phi_-(n+k)). Ein Ball aus Niveau 1 zieht
    dann Obertoene mit 2 omega und 3 omega mit [H aus Gl. 4 und 5]. Unser Ein-Feld-Ball hat keine.
  - Grosse Baelle merken nichts von der Kompaktheit. Unterscheidbar wird die Lesart erst bei Ballgroessen um R.
- **Finns "Feld ausserhalb der kleinsten Teile":**
  - In Bran-Welten ist das woertlich das Bild: Die Teilchen sitzen auf einer Brane, die Gravitation laeuft im Bulk. Bei
    MVV laufen dort auch sterile Fermionen [S Abstracts MVV und Schwarz].
  - "Seiten einer Dimension": Schwarz (arXiv:2403.12899, 2024) beschreibt als Alternative ein Intervall mit Branen an
    beiden Enden, also "a parallel 4d spacetime microns away from us" [S Abstract].

### Frage 2: Dark Dimension (MVV 2022/23 und Folgearbeiten)

- **Behauptung** [S, quellen/MVV-2205.12293.txt]:
  - Die Abstandsvermutung und die kleine Dunkle Energie (Lambda ~ 1e-122) verlangen einen Turm leichter Zustaende bei
    m ~ Lambda^(1/4). Dabei ist Lambda^(1/4) = 2,31 meV, als Laenge Lambda^(-1/4) ~ 88 um.
  - Ein Stringturm ist ausgeschlossen, zwei oder mehr Dimensionen ebenfalls. Es bleibt genau eine Dimension mit
    l ~ lambda Lambda^(-1/4) ~ 1 um, lambda ~ 1e-1 bis 1e-3, im Bereich l ~ 0,1-10 um (Gl. 3.8).
  - Die Casimir-Energie des Turms liefert lambda_Casimir = 5e-5 und damit l ~ 7,42 um (Gl. 3.7). Dunkle Energie und
    Dimension waeren also ueber die Casimir-Energie verknuepft.
  - Die 5D-Planck-Skala liegt bei ~1e9-1e10 GeV; dazu kommt ein Turm steriler Neutrinos bei ~eV.
- **Dunkle Materie:**
  - KK-Gravitonen, die "dunklen Gravitonen" (Gonzalo/Montero/Obied/Vafa, JHEP 11 (2023) 109): erzeugt bei T ~ 4 GeV,
    heute 1-100 keV [S Abstract].
  - Law-Smith/Obied/Prabhu/Vafa (arXiv:2307.11048, v3 2024): vertraeglich mit astrophysikalischen Schranken,
    Masse heute einige hundert keV, Groesse "around 1 - 30 um" [S Abstract].
  - Alternativen sind z. B. primordiale Schwarze Loecher [L? Titel, etwa Anchordoqui/Bedroya/Luest 2506.14874].
  - Bedroya/Obied/Vafa/Wu (arXiv:2507.03090, v3 05/2026): Der Radius laeuft mit einem Skalar. Dunkle Energie und
    DM-Masse aendern sich dann gemeinsam; das passt zu DESI DR2 [S Abstract].
- **Vorhersage fuer Kurzabstandsgravitation [S/E]:**
  - MVV nennen kein alpha.
  - Die Regel steht bei Adelberger/Heckel/Nelson (Ann. Rev. Nucl. Part. Sci. 53, 77 (2003), Volltext Z. 742-752): Ein
    flacher n-Torus gibt "alpha = 8n/3 and lambda = R*". Eine Dimension liefert also alpha = 8/3 mit Reichweite R.
  - Der Faktor 4/3 kommt daher, dass massives Spin 2 fuenf Polarisationen hat (siehe Frage 7).
  - MVV geben die Laborgrenze als "around 30 um" an, also m >~ 6,6 meV (Gl. 3.2). [E] 1,973e-7 eV m / 6,6e-3 eV
    = 30 um.
  - Ihr Test: "a factor of 10 - 100 improvement" der Torsionswaage.
  - Der Radion muss schwer oder entkoppelt sein, sonst gibt es eine zusaetzliche skalare Fuenfte Kraft (MVV,
    Abschnitt 4, Z. 500-506) [S].
- **Gegen Eot-Wash und andere Schranken:**
  - Lee u. a. 2020: |alpha| = 1 bei lambda < 38,6 um [S, aus STELLE-24M]. Fuer alpha = 8/3 ist die Grenze enger; MVV
    nennen ~30 um.
  - Kapner u. a. 2007: "an extra dimension must have a size R <= 44 um" [S Abstract].
  - Venugopalan u. a. 2024/26 erreichen bei 5-10 um nur alpha ~ 1e6-1e7 (aus STELLE-24M), weit ueber 8/3.
  - Sternkuehlung, Hardy/Sokolov/Stubbs (arXiv:2510.18975): Fuer eine Dimension ist sie schwaecher als das Labor
    [S Abstract].
  - [H] Der MVV-Bereich 0,1-10 um liegt 3- bis 300-mal unter der heutigen Laborreichweite. Durch Kurzabstandsmessungen
    ist er nicht widerlegt.
- **Neue Ausschlussansprueche (aus dem Gegensweep; beide aus den letzten fuenf Tagen):**
  - Lee/Randall/Riojas (arXiv:2609.36234, 28.09.2026) [S Volltext Z. 405-440]:
    - Die Zerfallsamplitude zwischen KK-Gravitonen ist um (q/m_n)^2 unterdrueckt, die Rate geht mit q^5.
    - Fuer die DM-Parameter waere die Kaskaden-Lebensdauer ~1e26 s statt 1e2-1e3 s.
    - Das soll auch mit skalarer KK-Verletzung gelten (ueber den Warp-Faktor).
    - Eine Begleitarbeit zu gewarpten Varianten ist angekuendigt.
  - Langhoff (arXiv:2610.01825, 01.10.2026, 4 Seiten, Einzelautor) [S Volltext]:
    - Nahe der Schwelle sind die Zerfaelle "pure d-wave". Damit sind KK-Gravitonen als Dunkle Materie in einer flachen
      Dimension ausgeschlossen.
    - Unabhaengig von der Dunklen Materie zerfaellt die unvermeidliche Freeze-in-Population in MeV-Photonen. Zusammen
      mit T_RH >= 5,96 MeV (BBN, CMB+BAO) bleibt nur R <~ 0,2 um bzw. m_KK >~ 1 eV.
    - [E] 0,2 um / 88 um ~ 2e-3, also lambda <~ 2e-3. Nur das untere Ende des MVV-Bereichs ueberlebt. Die
      Casimir-Schaetzung von 7,4 um faellt heraus, falls Langhoff haelt.
  - Die Gegenseite schrieb vor diesen Arbeiten: "consistent with the cosmological bounds as well as the Newton's
    inverse square law" (Vafa, arXiv:2402.00981, 2024) [S Abstract]. Eine Antwort auf die neuen Arbeiten fand ich im
    arXiv bis 01.10.2026 nicht.
  - Feldregel 7: Das Urteil lautet "strittig", nicht "widerlegt".
- **Andere Realisierung, anderes Vorzeichen:** Danielsson/Giri (arXiv:2606.20942, 2026). Das Modell der dunklen Blase
  ergibt ebenfalls eine Dimension von Mikrometergroesse, aber die Gravitation wird dort schwaecher ("fat graviton")
  [S Abstract].

### Frage 3: Zeit aus den Teilen

| Ansatz | Kern | Gemessen bzw. pruefbar | Marke |
|---|---|---|---|
| Page/Wootters 1983 (PRD 27, 2885) | Der globale Zustand ist stationaer; Zeitentwicklung erscheint als Korrelation mit einem Uhren-Teilsystem | Moreva u. a., PRA 89, 052122 (2014): zwei verschraenkte Photonen. Der innere Beobachter sieht Entwicklung, der aeussere beweist Stillstand. Das ist eine Vorfuehrung, kein Test, der scheitern koennte [H] | PW [L? Titel, Crossref]; Moreva [S Abstract] |
| Relationale Quantendynamik 2020-2026 | PW-, Dirac- und Heisenberg-Bild sind gleichwertig ("trinity") | Mit idealen Uhren gleichwertig zur Standard-QM, also keine Abweichung zu erwarten [H aus Chataignier u. a. 2026]. Die Uhren-Mehrdeutigkeit ist ein Deutungsproblem (Stoica, arXiv:2604.21805) | [S Abstracts] |
| Quantenuhren in der Raumzeit | Eine Uhr in Ueberlagerung von Impulsen zeigt eine Quantenkorrektur der Zeitdilatation (Smith/Ahmadi, Nat. Commun. 11, 5360 (2020)) | Vorhergesagt, nicht gemessen. PRL 136, 163602 (2026): "all measurements of time dilation so far can be explained effectively" mit klassischer Eigenzeit; gequetschte Ionen "within reach". Folgt auch aus Standard-QM mit innerer Uhr und testet daher nicht das Entstehen von Zeit [H] | [S Abstracts] |
| PW mit Gravitation | Singh/Friedrich (arXiv:2304.01263, Found. Phys.): Zeitdilatation und Newton-Wechselwirkung folgen aus der Kopplung an eine globale Quantenuhr | Quantenkorrekturen nur "suggesting", keine Messgroesse | [S Abstract] |
| Thermische Zeit, Connes/Rovelli (CQG 11, 2899 (1994)) | Der Zeitfluss kommt aus dem thermischen Zustand (Tomita-Takesaki) | Rovelli/Smerlak (CQG 28, 075007 (2011)): Temperatur ist die Rate der thermischen Zeit gegen die Eigenzeit. Das leitet den bekannten Tolman-Ehrenfest-Effekt her, nichts Neues | [S Abstracts] |
| Barbour (arXiv:0903.3489) | "duration, is redundant as a fundamental concept"; Uhren entstehen aus Veraenderung | Deutung; Shape Dynamics nicht geprueft | [S Abstract] |
| Eine Dimension "fuer die Zeit" | Bars, Two-Time Physics (hep-th/9809034; PRD 62, 046007 (2000)): d+2 Dimensionen mit zwei Zeiten; die gewoehnliche Physik erscheint als Eichfixierung ("Schatten") | Als Beleg sind nur versteckte Symmetrien vorgeschlagen; keine Messbestaetigung gefunden | [S Abstracts] |

- **Pruefbar oder Deutung? [H]**
  - Pruefbar sind Vorhersagen ueber Uhren: Quanten-Eigenzeit und Rotverschiebung.
  - Dass Zeit aus Korrelationen "entsteht", bleibt Deutung. Mit idealen Uhren ist das empirisch gleichwertig zur
    Standard-QM.
- **Finns "Bewegungsdifferenz" [H mit S]:**
  - Am naechsten liegen Page-Wootters (Zeit als Korrelation zweier Teilsysteme) und Barbour (Zeit aus Veraenderung).
  - Messbar sind nur dimensionslose Verhaeltnisse. Die Zeitvariation dimensionsbehafteter Groessen "has no operational
    meaning" (Duff, hep-th/0208093) [S Abstract]. Jede Uhr ist also ein Vergleich zweier Bewegungen.
  - Bei periodischen Uhren ist das Zaehlen von Umlaeufen relational nicht invariant (Chataignier u. a. 2026)
    [S Abstract].

### Frage 4: Ein Hintergrundfeld als universeller Takt

- **Mechanismus** (Uzan, Living Rev. Rel. 14, 2 (2011)) [S Abstract]: Eine variierende Naturkonstante bedeutet ein fast
  masseloses Feld, das an Materie koppelt. Das verletzt die Universalitaet des freien Falls.
- **Ultraleichte skalare Dunkle Materie** schwingt ueberall mit ihrer Masse. [E] Bei m = 1e-21 eV ist die Periode
  ~48 Tage, bei 1e-19 eV ~11,5 Stunden.
- **Schranken aus Uhren** [S Abstracts]:
  - Filzinger u. a., PRL 130, 253001 (2023): Yb+ E3/E2 und Yb+/Sr. Die Photonkopplung d_e ist fuer 1e-24 bis 1e-17 eV
    um mehr als eine Groessenordnung verbessert.
  - Sherrill u. a., NJP 25, 093012 (2023): Sr, Yb+ und Cs, Zeitskalen von einer Minute bis zu einem Tag.
  - Arakawa u. a. (arXiv:2602.16804, 2026; JILA, Th-229-Kernuhr): staerkste Schranken bei 1e-21 bis 1e-19 eV, mit
    "effective interaction scales exceeding 10^6 times the Planck scale".
  - [E, konventionsabhaengig] Das entspricht einer Kopplung etwa eine Million Mal unter Gravitationsstaerke.
- **Blinder Fleck (Gegensweep) [H mit S]:**
  - Ein Feld, das alle Massen und Frequenzen gleich verstellt (universelle, konforme Kopplung), aendert keine
    dimensionslosen Verhaeltnisse. Uhrvergleiche sehen es nicht (Duff 2002).
  - Sichtbar ist es nur ueber Gravitation:
    - Smarra u. a. (EPTA), PRD 110, 043033 (2024): Eine "universal conformal coupling" moduliert die Pulsarfrequenz.
      Dazu kommen Schranken fuer Brans-Dicke-artige Theorien mit Masse.
    - Khmelnitsky/Rubakov, JCAP 02 (2014) 019: Auch ohne jede Kopplung erzeugt der schwingende Druck "oscillations of
      gravitational potential with amplitude of the order of 10^-15" bei nHz. Das ist mit Pulsar-Timing messbar.
- **Das etablierte "Feld fuer die Zeit"** ist das Gravitationspotential. Bothwell u. a., Nature 602, 420 (2022), haben
  die Rotverschiebung innerhalb einer Millimeter-Probe aufgeloest, mit einer Unsicherheit von 7,6e-21 [S Abstract].
- **Annahme hinter allen Uhrschranken [H, ungeprueft]:** Das Feld ist die lokale Dunkle Materie, und seine Amplitude
  folgt aus deren Dichte. Fuer ein Feld ohne diese Energiedichte gelten die Zahlen so nicht.

### Frage 5: "Etwas, das zusammenhaelt oder stuetzt"

| Mechanismus | Kraft oder Gleichgewicht? | Beleg |
|---|---|---|
| MIT-Beutel (Chodos/Jaffe/Johnson/Thorn/Weisskopf, PRD 9, 3471 (1974)) | Gleichgewicht: Die Vakuum-Energiedichte B haelt dem Innendruck der Quarks an der Oberflaeche stand. Physikalisch eine Druckkraft je Flaeche; Ursprung ist der Energieunterschied zweier Vakua [H] | [L? Metadaten, Crossref] |
| Friedberg-Lee (PRD 15, 1694 und PRD 16, 1096 (1977)) | Gleichgewicht, dynamisch: Ein Skalarfeld bildet den Beutel selbst. Bei uns entspricht das M2 (chi-Vakuum, Beutelkonstante 1/4) und BEUTEL-1 (Huelle) | [L? Metadaten]; Projekt [S, Modell] |
| Casimir | Gemessene Kraft. Sie "can be computed without reference to zero point energies" (Jaffe, PRD 72, 021301 (2005)). Vakuumbild und van-der-Waals-Bild sagen dasselbe | [S Abstract] |
| Kosmologische Konstante | Haelt nicht zusammen: konstante Energiedichte mit negativem Druck, treibt die beschleunigte Ausdehnung [L? Lehrbuch]. In der Dark Dimension stammt sie womoeglich aus der Casimir-Energie der Zusatzdimension (MVV Abschnitt 3, Gl. 3.6-3.7) | [S MVV] |
| Kosmokonstante in CDT | Die nackte Kosmokonstante wird in den Simulationen auf ihren kritischen Wert abgestimmt; das 4-Volumen ist praktisch fest. Heraus kommt ein euklidischer de Sitter, "the maximally symmetric space for positive cosmological constant" (Ambjorn u. a., Phys. Rep. 519, 127 (2012), Volltext Z. 5214, 5990-5997, 6255, 8609). Noetig in dem Sinn, dass die Volumenbedingung dazugehoert, gleichwertig zu Lambda > 0 [H aus S]. Mehr dazu in der Nachbarkarte GEOMETRIE-STAND | [S Volltext] |
| Entropische Kraefte | Effektive Kraft aus dem Gradienten der freien Energie. Verlinde, JHEP 04 (2011) 029: Gravitation und Traegheit entropisch. Verlinde, SciPost Phys. 2, 016 (2017): zusaetzliche "dunkle" elastische Kraft mit a0 = c H0. Tests: Brouwer u. a., MNRAS 466, 2547 (2017), vertraeglich. Brouwer u. a., A&A 650, A113 (2021): Die Radialbeschleunigung passt zu MOND und Verlinde, zeigt aber "at least 6 sigma" Unterschied zwischen frueh- und spaettypischen Galaxien. Theorien, deren Modifikation nicht von Galaxieneigenschaften abhaengt, erklaeren das nicht | [S Abstracts] |

- **Sortierung [H]:**
  - Gemessene Kraefte: Casimir und die Gravitation selbst.
  - Gleichgewicht mit Oberflaechendruck: der Beutel.
  - Keine zusammenhaltende Kraft, sondern Ausdehnung: Lambda.
  - Statistische Kraft: die entropische. Als Grundlage der Gravitation ist sie unbelegt und in Galaxien unter Druck.

### Frage 6: Uebertrag auf unser Modell [H]

- Kurzantwort: Ja. Beide Beispiele der Karte sind rechenbar und haben Vorlaeufer:
  - Die Kraft zwischen Q-Baellen ist "attractive or repulsive depending upon their relative internal phase"
    (Bowcock/Foster/Sutcliffe, J. Phys. A 42, 085403 (2009)) [S Abstract].
  - Battye/Sutcliffe (NPB 590, 329 (2000)) erklaeren Ladungstransfer und Spaltung ueber die zeitabhaengigen Phasen
    [S Abstract].
  - Ladungstausch-Q-Baelle (Copeland/Saffin/Zhou, PRL 113, 231603 (2014)) und die Synchronisation durch einen Nullmode
    (Gleiser/Howell) [S Abstracts].
- Wichtigster Punkt vorab [H]: Die Dichte eines exakten Q-Balls ist stationaer. Seine Phase ist global unbeobachtbar
  (U(1)); beobachtbar ist nur die Phase relativ zu einem zweiten Ball. Die "innere Uhr" e^(-i omega t) wird also erst
  als Schwebung messbar. Die Codex-Uhr (stille Atmung) ist dagegen eine Dichte-Uhr und deshalb direkt sichtbar.
- Die Tests stehen in Abschnitt 5.

### Raum, Bewegung, Strings, Polarisation (7)

- **Was spannt Raum auf?**
  - ART: Die Geometrie ist ein eigenes dynamisches Feld. Es gibt Loesungen ohne Materie, etwa Gravitationswellen,
    gemessen z. B. GW170814 (PRL 119, 141101 (2017)) [S Abstract]. Materie formt den Raum, spannt ihn aber nicht allein
    auf [H].
  - Verschraenkung: Entflechtet man zwei Regionen, folgt "pulling apart and pinching off from each other" (Van
    Raamsdonk, GRG 42, 2323 (2010)) [S Abstract]. Das gilt im Rahmen von AdS/CFT.
  - CDT: Ein de Sitter entsteht aus der Summe ueber kausale Triangulierungen, 17-28 Planck-Laengen gross
    (Ambjorn/Goerlich/Jurkiewicz/Loll, PRL 100, 091304 (2008)) [S Abstract]. Kausalmengen behandelt die Nachbarkarte.
  - Verlinde 2011: Raum ist emergent, holographisch [S Abstract].
- **Unabgelenkte Bewegung:**
  - In der ART ist freier Fall kraeftefreie Bewegung, eine Geodaete [L? Lehrbuch].
  - KK liefert dasselbe Bild formal [E/H, siehe Frage 1]: Ein in 5D masseloses Quant, das mit c um die kompakte Richtung
    laeuft, ist in 4D ein ruhendes Teilchen der Masse 1/R. Eine Bindung wie im Q-Ball bedeutet langsameren Umlauf.
- **Ist Bewegung in Strings eingebaut?** Ja, dreifach:
  - Die Weltflaeche ist die Bewegungsgeschichte. Die Teilchenmassen sind Schwingungsanregungen des Strings
    [L? Lehrbuch].
  - Die Enden eines offenen Strings mit Neumann-Rand bewegen sich mit Lichtgeschwindigkeit: "the end point of the
    string moves at the speed of light" (Tong, Lectures on String Theory, arXiv:0908.0333, Abschnitt 3) [S Volltext,
    Z. 2566].
  - Der geschlossene String enthaelt ein masseloses Spin-2-Teilchen. Nach Feynman/Weinberg gilt fuer solche
    Theorien: "must be equivalent to general relativity" (Tong, Abschnitt 2) [S Volltext, Z. 2213].
- **Polarisation als Konzept:**
  - Polarisation ist die Richtungs- bzw. Tensorgestalt der Feldschwingung. Ihre Zahl ist die Zahl der Freiheitsgrade:
    masselos ab Spin 1 zwei, massiv 2s + 1.
  - Massives Spin 2 hat fuenf Polarisationen; "the longitudinal mode does not decouple from a nonrelativistic source".
    Daher kommt der Faktor 4/3 (Adelberger u. a. 2003, Volltext) [S].
  - Das ist die vDVZ-Unstetigkeit. Der Vainshtein-Mechanismus hebt sie auf (Hinterbichler, RMP 84, 671 (2012))
    [S Abstract].
  - Messung: GWTC-3 findet keine Polarisationsmoden ausserhalb der ART und begrenzt die Gravitonmasse auf
    m_g <= 2,42e-23 eV (PRD 112, 084080 (2025)) [S Abstract].
- **Bezug zu unseren Ball-Moden, jetzt mit Literatur:**
  - Bianchi/Coccia/Colacino/Fafone/Fucito, CQG 13, 2865 (1996), Volltext Z. 658-663 und 719-721 [S]:
    - An einer Kugel regt jede metrische Gravitationswelle "only the l = 0, 2 spheroidal modes" an, also 1 + 5 Moden.
    - Aus ihnen lassen sich alle sechs moeglichen Polarisationen eindeutig bestimmen.
    - Toroidale Moden bleiben stumm, und l = 1 kommt nicht vor.
  - Skalare Strahlung koppelt an den Monopol (Coccia/Gasperini/Ungarelli, PRD 65, 067101 (2002)) [S Abstract].
  - [H] Unsere Moden l = 0 (Atmung) und l = 2 (Quadrupol) sind genau die, die eine Gravitationswelle an einem Ball
    anspricht. Die fuenf l = 2-Komponenten entsprechen den fuenf Polarisationen von massivem Spin 2; die ART nutzt
    davon nur zwei.
  - **Feinheit zu "Zigarre <-> Pfannkuchen" [E/H]:**
    - Eine +-Welle entlang z dehnt x und quetscht y; z bleibt unveraendert. Die Hauptachsen verhalten sich wie
      (1, -1, 0); das ist l = 2, m = +-2 bezogen auf z.
    - Zigarre<->Pfannkuchen ist achsensymmetrisch: (1, -1/2, -1/2) = 3/4 (1, -1, 0) + 1/4 (1, 1, -2).
    - Der zweite Anteil ist ein m = 0-Muster entlang der Laufrichtung, also skalar-longitudinal. In der ART gibt es ihn
      nicht.
    - Auf dem Teilchenring (2D-Schnitt) sehen beide gleich aus; im Ball unterscheiden sie sich.

---

## 4. Tabelle D1 bis D4

| Nr | Erwartung (Leitung) | Ausgang | Beleg |
|---|---|---|---|
| D1 (70 %) | Die Dark Dimension sagt eine Zusatzdimension im um-Bereich voraus, mit Abweichungen bei ~1-10 um, unterhalb der Eot-Wash-Reichweite; sie ist nicht widerlegt | **offen**: Vorhersage-Teil eingetroffen, Status-Teil strittig | MVV: l ~ 0,1-10 um, Casimir 7,4 um, Laborgrenze ~30 um fuer alpha = 8/3 [S]. Gegen "nicht widerlegt": Langhoff 01.10.2026 (flache Dimension mit R >~ 0,2 um ausgeschlossen, unabhaengig von der DM) und Lee/Randall/Riojas 28.09.2026 (DM-Kaskade) [S]. Beide unbegutachtet, keine Gegenrede gefunden. Durch Kurzabstandsmessungen nicht widerlegt |
| D2 (65 %) | Page-Wootters bzw. relationale Zeit sind als Deutung etabliert und an kleinen Quantensystemen vorgefuehrt, ohne neue pruefbare Vorhersage fuer die Raumzeit | **eingetroffen** | Moreva 2014 [S Abstract]. PW-Literatur 2024-26 ist Theorie (arXiv 50 Treffer, Gegenprobe OpenAlex). Quanten-Zeitdilatation und Quanten-Eigenzeit sind Vorhersagen fuer Uhren, ungemessen und nicht spezifisch fuer das Entstehen von Zeit (Smith/Ahmadi 2020; Sorci u. a., PRL 136, 163602 (2026)) [S Abstract] |
| D3 (80 %) | Atomuhren begrenzen ein ueberall schwingendes Skalarfeld bereits um viele Groessenordnungen | **eingetroffen** | Filzinger 2023; Sherrill 2023; Arakawa 2026 mit mehr als 1e6 Planck-Skalen [S Abstract]. Zusatz: Fuer universelle Kopplung sind Uhrvergleiche blind; dafuer gibt es Pulsare (Smarra 2024) |
| D4 (60 %) | Die KK-Lesart der Q-Ball-Phase ist mathematisch moeglich, erzeugt aber keine neue Vorhersage fuer unser Modell | **eingetroffen fuer das jetzige Modell**, mit Vorbehalt | Demir 2000 und Abel/Kehagias 2015 [S Volltext] arbeiten die Lesart aus. M ~ Q^(3/4) bei flachem Potential ist unser Beutelgesetz, also nichts Neues. Neues nur als Modellerweiterung: KK-Turm, Obertoene, Gregory-Laflamme (Herdeiro/Radu 2025) |

---

## 5. Testvorschlaege zu Frage 6 (nur Vorschlaege, nichts gerechnet)

Allgemein [H]: In allen Tests ist die aeussere Zeit t des Codes die Referenz. Geprueft wird also, ob eine Modell-Uhr
regelmaessig laeuft, nicht, ob Zeit entsteht (vgl. ZWEI-SEITEN v2.3, Abschnitt Grenze, und Chataignier u. a. 2026).
Die Aufwandsangaben sind Schaetzungen fuer die Planung, nicht gemessen.

**T1: Schwebungsuhr zweier Q-Baelle ("Zeit aus Bewegungsdifferenz")**
- **Aufbau:**
  - 2D-Code aus BILDUNG-2 (Arm C, zwei Klumpen), aber mit zwei exakten, ruhenden Familienbaellen:
    omega1 = 0,7746 (Q = 66,6) und omega2 = 0,7956 (Q = 41,7). Beide Punkte kamen in BILDUNG-1 schon vor.
  - Abstaende d = 3, 5 und 8 R_F.
  - Kontrollarm: zwei gleiche Baelle (Delta omega = 0).
  - [E] Die Schwebungsperiode ist 2 pi / 0,021 ~ 299. Fuer >= 10 Schwebungen braucht man T ~ 3000. Billiger ist ein
    omega2 nahe 0,85: Periode ~84 bei Delta omega ~ 0,075.
- **Messgroessen:**
  - relative Phase Delta theta(t) = arg phi(x2) - arg phi(x1), U(1)-invariant
  - Schwebungsperiode aus den Nulldurchgaengen von cos Delta theta
  - Dichte |phi|^2 in der Mitte zwischen den Baellen, die eichinvariante Schwebung
  - Ladung Q_i(t) in Kugeln um die Zentren und Abstand d(t)
- **Ausgang A, Uhr besteht:**
  - Periode = 2 pi/|omega1 - omega2| auf 1 %
  - Variationskoeffizient der Perioden < 1 % ueber >= 10 Schwebungen
  - |Delta Q_i|/Q_i < 1 %
  - Kontrollarm ohne Schwebung
- **Ausgang B, Uhr faellt:** Ladungsfluss > 1 % oder Verschmelzen (Ladungstransfer wie bei Battye/Sutcliffe 2000),
  Periode driftet um mehr als 1 % oder Variationskoeffizient > 1 %.
- **Nebenbefund in beiden Faellen:** Die Kraft wechselt im Takt von Delta omega zwischen Anziehung und Abstossung
  (Bowcock u. a. 2009); d(t) sollte mitschwingen.
- **Aufwand:** Code unter 1 h (Startbedingung, Phasenauslesung). Laeufe je <= 10 min auf p4000/cpu ueber kleintest.sh.

**T2: Synchronisiert ein gemeinsames Hintergrundfeld die Takte?**
- **Aufbau:** wie T1 bei d = 8 R_F (schwach gekoppelt), mit zwei Armen:
  - Arm N, neutral und universell: Der Massenterm wird ueberall moduliert, U -> (1 + eps cos Omega t) S - S^2 + S^3/2.
  - Arm L, geladen: ein schwaches homogenes Kondensat a e^(-i omega_b t) mit omega_b zwischen omega1 und omega2. Es kann
    Ladung tauschen.
  - Raster eps bzw. a in {1e-3, 1e-2, 5e-2}. Omega fern von rho, einmal nahe rho als Resonanzprobe. Nach der Codex-Uhr
    zerstoert eine starke resonante Kopplung die Regelmaessigkeit.
- **Messgroessen:** omega_i(t) aus der Phasensteigung an den Zentren (gleitendes Fenster), dazu Delta omega(t) und
  Q_i(t).
- **Ausgang A, Synchronisation:** |Delta omega| sinkt unter 10 % des Startwerts und bleibt dort fuer >= 5 Schwebungen.
  Die Schwelle in eps zeichnet eine Arnold-Zunge.
- **Ausgang B, keine Synchronisation:**
  - Delta omega bleibt innerhalb von +-10 %.
  - Im Arm N verschieben sich beide omega nur gemeinsam.
  - Im Arm L verlieren die Baelle Ladung ans Bad, ohne sich anzunaehern.
- **Vermutung vorab [H], kein Vertrag:**
  - Arm N ergibt B. Ein ladungsneutrales, ueberall gleiches Feld verteilt keine Ladung um; das ist das Modell-Gegenstueck
    zum blinden Fleck der Uhren (Duff).
  - Arm L kann A ergeben.
- **Aufwand:** Code unter 1 h (ein Zusatzterm), 6-12 Laeufe je <= 10 min.

**T3: Ladungstausch-Uhr (Vorlage Copeland/Saffin/Zhou 2014)**
- **Aufbau:** Q-Ball und Anti-Q-Ball (+omega und -omega) so eng, dass die Kerne ueberlappen, in 2D. Abstaende 0,5, 1 und
  1,5 R_F.
- **Messgroessen:**
  - Ladungsdipol, also Q in der linken minus Q in der rechten Haelfte, ueber t
  - Tauschperiode und ihr Variationskoeffizient
  - Lebensdauer bis zum Uebergang in ein Oszillon; Xie/Saffin/Zhou (JHEP 07 (2021) 062) beschreiben dafuer vier Stadien
- **Ausgang A:** Die Ladung tauscht regelmaessig (Variationskoeffizient < 1 % ueber >= 10 Tausche), mit einer
  Tauschfrequenz unter omega. Dann gibt es in unserem Potential eine langsame Uhr aus der Ueberlagerung schneller
  Phasen.
- **Ausgang B:** Kein Tausch, oder Zerfall vor 10 Tauschen. Dann traegt das sextische Potential diese Uhr nicht.
- **Aufwand:** Code unter 1 h (Startbedingung), Laeufe <= 10 min.

**T4: Uhrvergleich im Modell (Gegenstueck zu Frage 4)**
- **Aufbau:**
  - Radial (l = 0), ein Ball mit zwei Uhren: der Phasenfrequenz omega und der stillen Atmung rho (Codex-Uhr, Periode
    2 pi/rho = 3,6015).
  - Ein Potentialparameter (z. B. der Koeffizient von S^3) wird langsam um 1 % moduliert, mit einer Periode weit ueber
    2 pi/rho.
  - Gegenarm: eine Modulation, die nur die Zeiteinheit aendert, also alle Frequenzen gleich.
- **Messgroessen:** Verhaeltnis r(t) = rho(t)/omega(t) und Empfindlichkeit K = d ln r / d ln(Parameter).
- **Ausgang A:** r schwingt mit der Modulation, K ist deutlich ungleich null. Das Uhrenpaar ist dann ein "Detektor" fuer
  das Feld; im Gegenarm bleibt r konstant.
- **Ausgang B:** K ~ 0. Beide Uhren reagieren gleich, und das Paar ist blind, wie Atomuhren bei universeller Kopplung.
- **Aufwand:** klein; vorhandene radiale Codes, Laeufe <= 10 min.

---

## 6. Regime, Unterscheidungspunkte, Kopplung und Takt, Gegensweep, Kalibrierung, offene Fragen

### 6.1 Regime und Moderatoren (Feldregel 1)

- **R-A, Dark Dimension, Gravitation bei um:**
  - Flacher Bulk mit Brane: KK-Yukawa mit alpha = +8/3, unter R wird die Gravitation staerker.
  - Dunkle Blase: Die Gravitation wird schwaecher ("fat graviton").
  - Moderator: die Realisierung der Dimension.
- **R-B, Dark Dimension, Lebensfaehigkeit:**
  - Dafuer: Vafa 2024, Law-Smith 2024. Dagegen: Langhoff und Lee/Randall/Riojas 2026.
  - Moderator ist die Zerfallskinematik nahe der Schwelle: s-Welle mit Rate ~ p gegen d-Welle mit Rate ~ p^5.
    Ausserdem zaehlt, wie stark die KK-Zahl verletzt ist.
  - Hardy u. a. 2025 rechneten noch mit der "typically assumed" KK-Verletzung. Damit waren Zerfallsschranken schwaecher
    als Kuehlschranken [S Abstract].
  - Zweiter Moderator: flach gegen gewarpt. Die Begleitarbeit von Lee/Randall/Riojas ist angekuendigt.
- **R-C, "Takt-Feld":**
  - Nicht-universelle Kopplung aendert Verhaeltnisse und ist mit Uhren messbar.
  - Universelle Kopplung zeigt sich nur ueber Gravitation, etwa bei Pulsaren.
  - Moderator: Universalitaet der Kopplung.
- **R-D, relationale Zeit:**
  - Ideale Uhren sind gleichwertig zur Standard-QM.
  - Nicht-ideale, wechselwirkende oder gravitierende Uhren koennten abweichen; gemessen ist das nicht.
  - Moderator: wie ideal die Uhr ist.
- **R-E, KK-Lesart:**
  - Umbenennung im Feldraum gegen echte kompakte Richtung.
  - Moderator: ob die Richtung eine Metrik und einen Turm hat.
- **R-F, zwei Q-Baelle:**
  - Getrennt gibt es eine Schwebung; ueberlappend gibt es Ladungstransfer bzw. Ladungstausch.
  - Moderator [H]: der Abstand relativ zur Schwanzlaenge und Delta omega relativ zur Wechselwirkungsrate.

### 6.2 Unterscheidungspunkte (Feldregel 2)

- **Flache Dark Dimension gegen keine Zusatzdimension:**
  - Unterscheidet bei Abstaenden r <~ R mit Gravitationsstaerke (alpha = 8/3). Nach MVV sind das 0,1-10 um, nach
    Langhoff <= 0,2 um.
  - Heute unzugaenglich: Die Torsionswaagen enden bei ~52 um Abstand, Venugopalan liegt bei alpha ~ 1e6-1e7.
- **Langhoff gegen die MVV-Mitte (7,4 um):**
  - MeV-Gamma-Fluss: geplante Teleskope wie AMEGO-X und e-ASTROGAM, Verbesserung um Faktor 10 (Langhoff, Text zu
    Abb. 1) [S].
  - Kurzabstandsmessung mit alpha ~ 1 bei 1-10 um; dafuer verlangen MVV eine Verbesserung um Faktor 10-100.
- **Flach gegen dunkle Blase:**
  - Unterscheidet am Vorzeichen der Abweichung bei r ~ R.
  - Noetig ist eine vorzeichengetrennte Auswertung. Das ist dieselbe offene Supplement-Frage wie in STELLE-24M fuer
    Lee 2020.
- **Universelle gegen nicht-universelle Taktkopplung:**
  - Nur im nicht-universellen Fall schwingt das Verhaeltnis verschiedener Uhrtypen (optisch, Hyperfein, Kern).
  - Pulsar-Timing sieht beide Faelle.
- **Zeit aus Korrelation (PW) gegen fundamentale Zeit:** Mit idealen Uhren habe ich keinen Unterscheidungspunkt
  gefunden. Nach Recherchestand sind beide empirisch nicht unterscheidbar [H].
- **Entropische Gravitation (Verlinde) gegen LambdaCDM:**
  - Unterscheidet an der Radialbeschleunigung frueh- gegen spaettypischer Galaxien gleicher Sternmasse.
  - Brouwer 2021 findet >= 6 sigma Unterschied; Verlinde erklaert ihn ohne Gas-Halos nicht.
- **Casimir als Vakuumenergie gegen van der Waals:**
  - Beide Bilder laufen erst fuer alpha -> 0 auseinander (Jaffe).
  - Das ist unzugaenglich; beide sind empirisch nicht unterscheidbar.
- **KK-Lesart gegen Feldraum-Lesart:**
  - Unterscheiden wuerden Zustaende mit Ladung 2 bei Masse 2/R (Turm), Obertoene bei 2 omega und die
    Gregory-Laflamme-Instabilitaet ab einem kritischen L.
  - Zugaenglich nur im erweiterten Modell.

### 6.3 Kopplung und Takt vor Bauteil (Feldregel 6)

- "X erzeugt Zeit" hat hier mindestens sechs Wege:
  - Korrelation mit einer Uhr (PW)
  - thermischer Zustand (Connes/Rovelli)
  - Veraenderung (Barbour)
  - Schnitt-Ticks (ZWEI-SEITEN, Projekt)
  - schwingendes Hintergrundfeld (ultraleichte DM)
- [H] Die gemeinsame Groesse ist kein Bauteil wie eine "dunkle Dimension", sondern das Verhaeltnis zweier Prozesse:
  - Messbar sind nur dimensionslose Verhaeltnisse (Duff), und ein universeller Takt ist lokal unsichtbar.
  - Eine "dunkle Dimension fuer die Zeit" waere deshalb nur ueber eine Differenz sichtbar: zwischen Uhrtypen, zwischen
    Orten (Gravitation) oder zwischen zwei Baellen.
  - Das ist Finns "Bewegungsdifferenz".
- Fuer "Zusammenhalten" ist die gemeinsame Groesse ein Gleichgewicht von Druck bzw. freier Energie an einer Grenze:
  Beutel, Casimir, entropische Kraft [H].

### 6.4 Gegensweep (Feldregel 4): Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

| Nr | Selbstverstaendlichkeit | Geprueft? | Ergebnis |
|---|---|---|---|
| GS1 | Die Dark Dimension waere an der Grenze fuer \|alpha\| = 1 (38,6 um) zu messen | ja: Adelberger 2003, MVV, Kapner 2007 | Fuer einen Kreis gilt alpha = 8/3; die Grenze liegt bei ~30 um (MVV) bzw. 44 um (Kapner 2007) |
| GS2 | Das Kurzabstandssignal besteht nur aus dem KK-Graviton-Yukawa | ja: MVV Z. 500-506; Danielsson/Giri | Der Radion muss schwer oder entkoppelt sein. Die Blasen-Variante sagt eine schwaechere Gravitation bei um voraus |
| GS3 | Atomuhren sehen jedes "Takt-Feld" | ja: Duff; Smarra; Khmelnitsky/Rubakov | Universelle Kopplung ist fuer Uhrverhaeltnisse unsichtbar und nur ueber Pulsare bzw. Gravitation messbar |
| GS4 | Die Phase eines einzelnen Q-Balls ist eine beobachtbare Uhr | indirekt (Bowcock: nur die relative Phase wirkt) und [H] | Die Dichte eines exakten Balls ist stationaer; sichtbar wird die Phasenuhr erst gegen einen zweiten Ball |
| GS5 | Die WebFetch-Zusammenfassungen geben den Abstract wieder | ja: curl auf die API | Bei Lee/Randall/Riojas paraphrasierte das Abrufmodell; der Wortlaut ist nachgezogen |
| GS6 | Ein Feld, das den Uhrengang setzt, muesste neu sein | ja: Bothwell 2022 | Das Gravitationspotential leistet das schon, gemessen auf mm |
| GS7 | Die Uhrschranken gelten fuer jedes Feld | nein | Sie nehmen an, dass das Feld die lokale Dunkle Materie ist [H, ungeprueft] |
| GS8 | Langhoffs Ausschluss gilt fuer jede Variante | teils | Er nimmt eine flache Dimension an. Lee/Randall/Riojas behaupten Universalitaet auch mit Warp. Eine Gegenrede habe ich nicht gefunden |

### 6.5 Kalibrierung

- **(a) Gemessen:**
  - Lee 2020: |alpha| = 1 bei < 38,6 um. Kapner 2007: R <= 44 um.
  - Uhren: Filzinger 2023, Arakawa 2026. Rotverschiebung auf mm: Bothwell 2022.
  - GWTC-3: keine Polarisationsmoden ausserhalb der ART, m_g <= 2,42e-23 eV.
  - Moreva 2014 (eine Vorfuehrung). Brouwer 2021: 6 sigma Unterschied.
- **(b) Nuetzlich verdichtet:**
  - MVV-Bereich und alpha = 8/3
  - Langhoffs R <~ 0,2 um (Theorie plus Gamma- und BBN-Daten)
  - KK-Lesart der Q-Baelle
  - Kugelmoden l = 0 und 2 als die sechs Polarisationen
  - universelle gegen nicht-universelle Kopplung
- **(c) Nur gewachsene Gewissheit:**
  - Der Satz "die Dark Dimension ist seit dem 01.10. erledigt" gehoert hierher: Er stuetzt sich auf zwei Preprints, zwei
    und fuenf Tage alt, unbegutachtet, ohne Antwort.
  - Dasselbe gilt fuer meine Lesart "Zeit aus Bewegungsdifferenz = relationale Zeit". Sie ist Deutung, keine neue
    Evidenz.
- **Warnzeichen:**
  - Meine Sicherheit, dass D1 kippt, stieg innerhalb weniger Minuten, und zwar aus zwei Abstracts.
  - Zugleich zerfiel die Frage: flach, gewarpt oder Blase; mit oder ohne Dunkle Materie; welches Vorzeichen.
  - Die Antwort auf die Karte ("strittig") ist sicherer geworden, die Antwort auf "wo laege das Signal" unschaerfer.

### 6.6 Offene Fragen

1. Halten Langhoff und Lee/Randall/Riojas?
   - Abzuwarten sind die Gegenrede der Dark-Dimension-Autoren und die Begleitarbeit zu gewarpten Varianten.
   - Vorschlag: arXiv "dark dimension" ueber den Scout beobachten.
2. Welches Vorzeichen hat die Abweichung bei um, flach oder Blase?
   - Dazu gehoeren die vorzeichengetrennten Schranken von Lee 2020 (Supplement, APS-Zugang).
   - Diese Frage ist aus STELLE-24M offen.
3. Gibt es Schranken fuer ein "Takt-Feld", die nicht annehmen, dass es die Dunkle Materie ist?
4. Fuer unser Modell: Besteht die Schwebungsuhr (T1)? Synchronisiert ein Hintergrund die Takte, oder verschiebt er sie
   nur gemeinsam (T2)?
5. Gibt es eine Graviphoton-Kraft zwischen KK-Q-Baellen? Keine Fundstelle. Zu "weak gravity conjecture" plus Q-Ball gab
   es einen Treffer, 1907.04982, ungelesen.
6. Was meint Finn mit "Seiten einer Dimension"? Rueckfrage R1 im ARBEITSFELD.

---

## 7. Suchprotokoll und Grenzen

Zeiten nach date (CEST, 02.10.2026). Je Block stehen Erwartung, Abruf und Ausgang einzeln in `ARBEITSFELD.md`.

| Block | Erwartung geschrieben | Abfragen | Ergebnis / Fehlschlag |
|---|---|---|---|
| A1 | 20:41:45 | arXiv all:"dark dimension" (Datum, 50); abs 2205.12293 | 73 Treffer; MVV-Abstract |
| A2 | 20:42:46 | Abstracts 2609.36234, 2610.01825, 2510.18975; MVV-PDF | WebFetch konnte das PDF nicht lesen -> lokal gespeichert, pdftotext |
| A3 | 20:44:13 | curl API id_list (3) | erster curl ueber http leer (Fehlschlag), mit https erfolgreich |
| A4 | 20:45:12 | API Lee 2020, Kapner 2007, Adelberger 2003; Adelberger-Volltext | alpha = 8n/3 gefunden |
| A5 | 20:46:00 | API Branchina, Bedroya, Schwarz | - |
| B1 | 20:46:16 | API "ultralight dark matter" + clock (40); 5 Abstracts | 36 Treffer |
| B2/C1 | 20:46:48 | API Uzan, Duff, Moreva; "Page-Wootters" (60) | 50 Treffer |
| C2/C3 | 20:47:08 / 20:47:38 | 5 PW-Abstracts; "quantum time dilation"; Connes/Rovelli, Rovelli/Smerlak, Barbour | 8 Treffer, nur Theorie |
| D1 | 20:47:58 | 5 Q-Ball/KK-Abfragen; 5 Abstracts | Trefferzahlen 4/8/1/0/2 |
| E1 | 20:49:05 | 7 Abstracts (KK-Uebersicht, Casimir, Verlinde, Brouwer, CDT) | - |
| F1 | 20:49:27 | 5 Q-Ball-Abfragen; 6 Abstracts | "charge-swapping" mit Fremdtreffern (Batterien) |
| G1 | 20:50:25 | 4 Abstracts; String-Endpunkte | Suche nach Endpunkten 0 Treffer (Kanal untauglich) -> Tong-Volltext |
| H1/H2 | 20:51:24 / 20:51:54 | Dark Dimension + Kurzabstand; 2609.22501; MVV-Radion; Khmelnitsky; Crossref (4 DOIs) | - |
| I1 | 20:55:00 | Lee/Randall/Riojas-Volltext; GMOV, Law-Smith; Demir-Volltext; Bars, Stueckelberg | eine Fehllesung aus Spaltensalat (gestrichen) |
| J1/J2 | 20:57:16 / 20:57:52 | OpenAlex ab 10/2024 (3 Suchen); 2509.09573; CDT-Uebersicht-Volltext | OpenAlex-Freitext stark verrauscht |
| K1/K2 | 20:58:33 / 20:59:24 | Kugeldetektoren (3 Suchen, 2 Abstracts, Bianchi-Volltext); 3 Abstracts | - |
| L1/M1 | 21:00:07 / 21:01:50 | Bothwell; Abel/Kehagias-Volltext; Autorenabgleich | - |

**Grenzen:**
- WebSearch war erschoepft. Genutzt habe ich die arXiv-API (per WebFetch und curl), OpenAlex und Crossref; Semantic
  Scholar nicht.
- Abstracts stammen per curl im Wortlaut aus der arXiv-API. Eine WebFetch-Paraphrase ist nicht verwendet.
- Volltexte habe ich nur ueber pdftotext gelesen. Die Abbildungen (z. B. Langhoff Abb. 1) habe ich nicht selbst
  angesehen.
- Nicht im Volltext gelesen:
  - Page/Wootters 1983, Chodos 1974 und Friedberg/Lee 1977: nur Metadaten
  - Overduin/Wesson: nur Abstract
  - Eardley 1973: nicht abgerufen
  - Smith/Ahmadi und die Uhren-Arbeiten: nur Abstracts
- Keine Rechnung ausser Kopfrechnung.
- **Verfahrensvermerke:**
  - Ein Bash-Aufruf enthielt unnoetig "python3 --version". Es lief keine Rechnung, die Ausgabe wurde verworfen. Das
    verstoesst gegen die Regel "kein python lokal"; es ist nicht wiederholt worden.
  - Zwei Uhrzeiten und ein Autorenname im ARBEITSFELD waren zunaechst geschaetzt bzw. geraten. Sie sind gestrichen und
    berichtigt.

---

## 8. Quellenliste

Dark Dimension und Kurzabstand:
- Montero, Vafa, Valenzuela (2022/23): The Dark Dimension and the Swampland, JHEP 2023, 22. https://arxiv.org/abs/2205.12293
- Langhoff (2026): Near Threshold Kaluza-Klein Graviton Decays and the Dark Dimension. https://arxiv.org/abs/2610.01825
- Lee, Randall, Riojas (2026): A Universal Kaluza-Klein Graviton Cascade Rate. https://arxiv.org/abs/2609.36234
- Hardy, Sokolov, Stubbs (2025): Stellar cooling limits on KK gravitons and dark dimensions. https://arxiv.org/abs/2510.18975
- Anchordoqui, Antoniadis, Luest (2025): Two Micron-Size Dark Dimensions, Fortsch. Phys. e70015. https://arxiv.org/abs/2501.11690
- Schwarz (2024): Comments Concerning a Hypothetical Mesoscopic Dark Dimension. https://arxiv.org/abs/2403.12899
- Bedroya, Obied, Vafa, Wu (2025/26): Evolving Dark Sector and the Dark Dimension Scenario. https://arxiv.org/abs/2507.03090
- Branchina, Branchina, Contino, Pernace (2024): Dark Dimension and the Effective Field Theory limit, IJGMMP. https://arxiv.org/abs/2404.10068
- Gonzalo, Montero, Obied, Vafa (2023): Dark Dimension Gravitons as Dark Matter, JHEP 11 (2023) 109. https://arxiv.org/abs/2209.09249
- Law-Smith, Obied, Prabhu, Vafa (2023/24): Astrophysical Constraints on Decaying Dark Gravitons. https://arxiv.org/abs/2307.11048
- Vafa (2024): Swamplandish Unification of the Dark Sector. https://arxiv.org/abs/2402.00981
- Danielsson, Giri (2026): Dark bubbles, dark dimensions and fat gravitons. https://arxiv.org/abs/2606.20942
- Braun, Cicoli, Milioli, Valandro (2026): Moduli Stabilisation for ADD and the Dark Dimension Scenario. https://arxiv.org/abs/2606.19440
- Lee, Adelberger, Cook, Fleischer, Heckel (2020): New Test of the Gravitational 1/r^2 Law at Separations down to 52 um, PRL 124, 101101. https://arxiv.org/abs/2002.11761
- Kapner u. a. (2007): Tests of the Gravitational Inverse-Square Law below the Dark-Energy Length Scale, PRL 98, 021101. https://arxiv.org/abs/hep-ph/0611184
- Adelberger, Heckel, Nelson (2003): Tests of the Gravitational Inverse-Square Law, Ann. Rev. Nucl. Part. Sci. 53, 77. https://arxiv.org/abs/hep-ph/0307284
- Venugopalan u. a. (2026): Sci. Rep. 16, 5180 (ueber STELLE-24M). https://arxiv.org/abs/2412.13167
- van Manen, Blankenstein, Mazumdar (2026): Gravitationally Induced Entanglement of Matter in Quadratic Curvature Gravity and Constraints on Ghost Mass (nur Randnotiz, V9). https://arxiv.org/abs/2609.22501

Uhren und Felder:
- Filzinger u. a. (2023): Improved limits on the coupling of ultralight bosonic dark matter to photons from optical atomic clock comparisons, PRL 130, 253001. https://arxiv.org/abs/2301.03433
- Arakawa u. a. (2026): Probing Ultralight Dark Matter at the Mega-Planck Scale with the Thorium Nuclear Clock. https://arxiv.org/abs/2602.16804
- Sherrill u. a. (2023): Analysis of atomic-clock data to constrain variations of fundamental constants, NJP 25, 093012. https://arxiv.org/abs/2302.04565
- Smarra u. a. (2024): Constraints on conformal ultralight dark matter couplings from the European Pulsar Timing Array, PRD 110, 043033. https://arxiv.org/abs/2405.01633
- Khmelnitsky, Rubakov (2014): Pulsar timing signal from ultralight scalar dark matter, JCAP 02 (2014) 019. https://arxiv.org/abs/1309.5888
- Uzan (2011): Varying constants, Gravitation and Cosmology, Living Rev. Rel. 14, 2. https://arxiv.org/abs/1009.5514
- Duff (2002): Comment on time-variation of fundamental constants. https://arxiv.org/abs/hep-th/0208093
- Bothwell u. a. (2022): Resolving the gravitational redshift within a millimeter atomic sample, Nature 602, 420. https://arxiv.org/abs/2109.12238

Zeit:
- Page, Wootters (1983): Evolution without evolution: Dynamics described by stationary observables, PRD 27, 2885. https://doi.org/10.1103/PhysRevD.27.2885
- Moreva u. a. (2014): Time from quantum entanglement: an experimental illustration, PRA 89, 052122. https://arxiv.org/abs/1310.4691
- Smith, Ahmadi (2020): Quantum clocks observe classical and quantum time dilation, Nat. Commun. 11, 5360. https://arxiv.org/abs/1904.12390
- Sorci, Foo, Leibfried, Sanner, Pikovski (2026): Quantum signatures of proper time in optical ion clocks, PRL 136, 163602. https://arxiv.org/abs/2509.09573
- Singh, Friedrich (2023/25): Emergence of Gravitational Potential and Time Dilation from Non-interacting Systems Coupled to a Global Quantum Clock. https://arxiv.org/abs/2304.01263
- Chataignier, Hoehn, Lock, Mele (2026): Relational Dynamics with Periodic Clocks, NJP 28, 034504. https://arxiv.org/abs/2409.06479
- Stoica (2026): The clock ambiguity problem: extended or extinguished? https://arxiv.org/abs/2604.21805
- Zaravashan, Gradoni, Khalily (2026): Topological Winding Readout of an Emergent Page-Wootters Clock. https://arxiv.org/abs/2608.27650
- Connes, Rovelli (1994): Von Neumann Algebra Automorphisms and Time-Thermodynamics Relation ..., CQG 11, 2899. https://arxiv.org/abs/gr-qc/9406019
- Rovelli, Smerlak (2011): Thermal time and the Tolman-Ehrenfest effect, CQG 28, 075007. https://arxiv.org/abs/1005.2985
- Barbour (2009): The Nature of Time. https://arxiv.org/abs/0903.3489
- Bars (1998/2005): Two-Time Physics. https://arxiv.org/abs/hep-th/9809034 ; Bars (2000): Two-Time Physics in Field Theory, PRD 62, 046007. https://arxiv.org/abs/hep-th/0003100

Q-Baelle und Zusatzdimension:
- Demir (2000): Stable Q-balls from extra dimensions, PLB 495, 357. https://arxiv.org/abs/hep-ph/0006344
- Abel, Kehagias (2015): Q-branes, JHEP 11 (2015) 096. https://arxiv.org/abs/1507.04557
- Herdeiro, Radu (2025): Gregory-Laflamme-type instability of boson strings and related phases in D=5 Kaluza-Klein theory. https://arxiv.org/abs/2503.15069
- Brihaye, Herdeiro, Radu (2022): D=5 static, charged black holes, strings and rings with resonant, scalar Q-hair, JHEP 10 (2022) 153. https://arxiv.org/abs/2207.13114
- Krippendorf, Muia, Quevedo (2018): Moduli Stars, JHEP 08 (2018) 070. https://arxiv.org/abs/1806.04690
- Overduin, Wesson (1997): Kaluza-Klein Gravity, Phys. Rep. 283, 303. https://arxiv.org/abs/gr-qc/9805018
- Bowcock, Foster, Sutcliffe (2009): Q-balls, Integrability and Duality, J. Phys. A 42, 085403. https://arxiv.org/abs/0809.3895
- Battye, Sutcliffe (2000): Q-ball Dynamics, NPB 590, 329. https://arxiv.org/abs/hep-th/0003252
- Copeland, Saffin, Zhou (2014): Charge-Swapping Q-balls, PRL 113, 231603. https://arxiv.org/abs/1409.3232
- Xie, Saffin, Zhou (2021): Charge-Swapping Q-balls and Their Lifetimes, JHEP 07 (2021) 062. https://arxiv.org/abs/2101.06988
- Gleiser, Howell (2002/03): Resonant emergence of global and local spatiotemporal order in a nonlinear field model. https://arxiv.org/abs/hep-ph/0209176
- Kinach, Choptuik (2024): Dynamics of U(1) gauged Q-balls in three spatial dimensions, PRD 110, 075033. https://arxiv.org/abs/2408.07561

Zusammenhalten, Raum, Strings, Polarisation:
- Chodos, Jaffe, Johnson, Thorn, Weisskopf (1974): New extended model of hadrons, PRD 9, 3471. https://doi.org/10.1103/PhysRevD.9.3471
- Friedberg, Lee (1977): Fermion-field nontopological solitons, PRD 15, 1694. https://doi.org/10.1103/PhysRevD.15.1694 ; II. Models for hadrons, PRD 16, 1096. https://doi.org/10.1103/PhysRevD.16.1096
- Jaffe (2005): The Casimir Effect and the Quantum Vacuum, PRD 72, 021301. https://arxiv.org/abs/hep-th/0503158
- Verlinde (2011): On the Origin of Gravity and the Laws of Newton, JHEP 04 (2011) 029. https://arxiv.org/abs/1001.0785
- Verlinde (2017): Emergent Gravity and the Dark Universe, SciPost Phys. 2, 016. https://arxiv.org/abs/1611.02269
- Brouwer u. a. (2017): First test of Verlinde's theory of Emergent Gravity using Weak Gravitational Lensing measurements, MNRAS 466, 2547. https://arxiv.org/abs/1612.03034
- Brouwer u. a. (2021): The Weak Lensing Radial Acceleration Relation ..., A&A 650, A113. https://arxiv.org/abs/2106.11677
- Ambjorn, Goerlich, Jurkiewicz, Loll (2008): Planckian Birth of the Quantum de Sitter Universe, PRL 100, 091304. https://arxiv.org/abs/0712.2485
- Ambjorn, Goerlich, Jurkiewicz, Loll (2012): Nonperturbative Quantum Gravity, Phys. Rep. 519, 127. https://arxiv.org/abs/1203.3591
- Van Raamsdonk (2010): Building up spacetime with quantum entanglement, GRG 42, 2323. https://arxiv.org/abs/1005.3035
- Tong (2009): Lectures on String Theory. https://arxiv.org/abs/0908.0333
- Hinterbichler (2012): Theoretical Aspects of Massive Gravity, RMP 84, 671. https://arxiv.org/abs/1105.3735
- LIGO/Virgo (2017): GW170814, PRL 119, 141101. https://arxiv.org/abs/1709.09660
- LIGO/Virgo/KAGRA (2025): Tests of General Relativity with GWTC-3, PRD 112, 084080. https://arxiv.org/abs/2112.06861
- Bianchi, Coccia, Colacino, Fafone, Fucito (1996): Testing Theories of Gravity with a Spherical Gravitational Wave Detector, CQG 13, 2865. https://arxiv.org/abs/gr-qc/9604026
- Coccia, Gasperini, Ungarelli (2002): Sensitivity of spherical gravitational-wave detectors to a stochastic background of non-relativistic scalar radiation, PRD 65, 067101. https://arxiv.org/abs/gr-qc/0107103

Projekt (nur Einordnung): KARTE.md; RUNDE-22/stelle-24m/ERGEBNIS.md; RUNDE-22.md (Codex-Uhr, BILDUNG); RUNDE-17.md

---

## 9. Einfach gesagt

Finn fragt, ob eine versteckte Richtung im Raum die kleinsten Teile zusammenhaelt und die Zeit entstehen laesst. Eine
bekannte Idee sagt so eine versteckte Richtung voraus, etwa ein Tausendstel Millimeter gross; dort muesste sich die
Schwerkraft anders verhalten, und so fein kann noch niemand messen. Diese Woche sind aber zwei neue, noch ungepruefte
Rechnungen erschienen, nach denen die Richtung viel kleiner sein muesste und im Labor dann kaum zu finden waere. Bei der
Zeit zeigen die Forscher: Eine Uhr misst immer nur, wie eine Bewegung im Vergleich
zu einer anderen laeuft; etwas, das alle Uhren gleich verstellt, wuerde niemand bemerken. Fuer unser Modell heisst
das: Ein einzelner Ball hat keine sichtbare Uhr, aber zwei Baelle mit verschiedenem Takt ergeben ein gleichmaessiges
Auf und Ab, und genau das wollen wir als Naechstes nachrechnen.
