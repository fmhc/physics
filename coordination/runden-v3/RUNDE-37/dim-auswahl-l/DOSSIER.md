# DIM-AUSWAHL-L: Dossier. Warum drei grosse Raumdimensionen? Mechanismen, die Dimensionen auswaehlen, teilweise existieren lassen oder kurzlebig machen (Runde 42, Literatur)

- feldforscher fuer Leitung claude-primary. Agentenstart 2026-10-04 18:49:10 CEST, Dossier ab 19:09:56 CEST (date).
- Grundlage: KARTE.md (E1 bis E6, Fragen 1 bis 5). Protokoll im selben Ordner: ARBEITSFELD.md. Es enthaelt die
  Erwartung vor jedem Abruf mit date-Zeit, den Ausgang, Berichtigungen, den Gegensweep und die offenen Rueckfragen.
- 10 von 10 Abrufen verbraucht: drei davon leer (Server-Antwort 503), einer fast leer (Anfrage zu breit). Keine
  Websuche. Lokale Kopien liegen in quellen/.
- Kennzeichen:
  - [S] an der Quelle gelesen; "Z." ist die Zeile der pdftotext-Datei in quellen/
  - [S Abstract] nur das Abstract gelesen (Wortlaut aus der arXiv-API)
  - [S Abb.] Abbildung im PDF angesehen, Werte nach Augenmass
  - [P] Projektdatei (die Quelle ist dort belegt); [L] Gedaechtnis; [L?] unsicher; [M] Schreibtisch der Leitung
  - [ES] eigener Schluss; [H] Hypothese

## 1. Ergebnis zuerst

1. **Die "3" hat einen klaren Ursprung, aber keinen Attraktor.** Faeden treffen sich generisch nur in hoechstens 3
   Raumdimensionen; nur dort koennen sich gewickelte Strings vernichten und ihre Richtungen freigeben.
   - Brandenberger/Vafa 1989 [L].
   - Statisch numerisch bestaetigt von Sakellariadou 1995 [S Abstract].
   - Im verduennten Regime nach der Hagedorn-Phase sind Treffen fuer d > 3 exponentiell unterdrueckt
     (Greene/Kabat/Marnerides 2009 [S]).
   - Mit Membranen wird daraus eine Hierarchie: 3 grosse, 2 mittlere, 4 kleine Raumrichtungen
     (Alexander/Brandenberger/Easson 2000 [S]).
2. **Von selbst pendelt sich nichts bei 3 ein.** Die einzige gelesene Rechnung, die den Anfangszustand zufaellig
   waehlt, findet ein "alles oder nichts". Die Zahl grosser Dimensionen ist eine Glocke ueber 0 bis 9; wo sie liegt,
   bestimmt der Anfangswert der Kopplung. Bei 3 liegt sie nur in einem schmalen Fenster (Easther/Greene/Jackson/Kabat
   2004, Abb. 4 [S Abb.]).
3. **Eine scharfe Wahrscheinlichkeitsverteilung ueber die Dimensionszahl gibt es in einem Modell, aber ihr Gipfel
   wandert.**
   - Bei Carroll/Johnson/Randall 2009 sind Uebergaenge in Vakua mit einer bestimmten Zahl grosser Dimensionen
     exponentiell gewichtet. Das Gewicht kommt aus Sphaerenvolumina.
   - Bei D = 8 liegt der Gipfel bei 4D, bei D = 10 bei 5D [S, S Abb.].
   - Das Wahrscheinlichkeitsmass ist dort ausdruecklich nicht eindeutig [S].
4. **Finns Bild der Lebensdauern steht in der Stringliteratur eher auf dem Kopf.**
   - Ein 3+1-All mit positiver Vakuumenergie ist dort generisch instabil. Der typische Zerfall ist, dass die
     Zusatzdimensionen wieder gross werden (Giddings 2003 [S Abstract]).
   - Kurzlebig sind die hoeherdimensionalen Gebilde: Branen mit p >= 4 vernichten sich zuerst (ABE [S]). Von
     Dimensionen sagt das nichts.
5. **Zahlen der Literatur:**
   - 3 (Strings), 5 (Membranen)
   - 3 und 7 (Branen in AdS)
   - 10 und 11 (Superstring, M-Theorie [L])
   - 12 nur formal: die 12 der F-Theorie (Vafa 1996 [S Abstract]) und eine Schwelle in einer
     Matrixmodell-Klassifikation (Liao 2026 [S Abstract])
   - 26 bosonisch [L]
   - Finns "3-4 stabil, 12 teilweise" sagt nach Recherchestand keine Arbeit als Mechanismus voraus. Belegt ist es
     nicht, widerlegt auch nicht.
6. **Schreibtisch:**
   - Die Schnittregel stimmt, gilt aber nur fuer glatte Faeden und eine Topologie mit Schleifen.
   - Das PU-Bild ist richtig gerechnet. 4 und 12 haengen aber an r = a und am Wuerfelgitter; robust ist hoechstens das
     Verhaeltnis von etwa 3 bis 4 [ES].
   - Das V_D-Maximum bei 5,26 stimmt, waehlt aber ohne festgelegte Skala nichts aus. Sauber wird dasselbe Argument
     erst als dimensionsloses Verhaeltnis zweier Wirkungen, wie bei Carroll/Johnson/Randall [ES].

## 2. Erwartungsverstoesse (das eigentliche Ergebnis, wichtigstes zuerst)

| Nr | Erwartet (vorab) | Gefunden | Fundstelle | Korrektur |
|---|---|---|---|---|
| V1 gross | E1 und Finn: Die Auswahl von 3 ist robust, das All "pendelt sich ein" | Ausdehnung "all or nothing". Viele gewickelte Strings: alle Richtungen bleiben klein. Wenige: alle werden gross. 3 nur bei feinabgestimmten Anfangswerten; die Glocke wandert mit der Anfangskopplung phi. Raten "negligible", Gleichgewicht "cannot apply" | EGJK 2004 Z. 798-801, 821-823, 836-844, Abb. 4 [S]; Danos/Frey/Mazumdar 2004 [S Abstract] | Die Zaehlung stimmt statisch, die Dynamik waehlt nicht. Drei Regime, siehe Abschnitt 6 |
| V2 gross | A8-E: keine Verteilung ueber D, 4 nicht ausgezeichnet | Exponentiell scharfe Verteilung P_i/P_j ~ exp[-S_dS (alpha_i - alpha_j)]. Gipfel bei 4 nicht kompakten Dimensionen fuer D = 8, bei 5 fuer D = 10 | CJR Gl. 79, 80, 84, 94; Z. 1642-1647, 1950-1955; Abb. 16 [S, S Abb.] | Die Verteilung existiert im Modell. Ihr Gipfel haengt an der Gesamtdimension und am Mass |
| V3 gross | Finns Bild: die vielen Dimensionen sind kurzlebig | 4D mit positiver Vakuumenergie ist "catastrophic[ally]" instabil, typisch durch Dekompaktifizierung. Gewickelte Strings koennen die Zusatzdimensionen spaet nicht stabilisieren | Giddings 2003 [S Abstract]; Battefeld/Watson 2006 [S Abstract] | Die Lebensdauer eines Vakuums haengt an seiner Vakuumenergie, nicht an D. Die Rate aus einem dS geht gegen null, wenn dessen Lambda gegen null geht (CJR Z. 1862-1869 [S]) |
| V4 mittel | Das Lorentz-IKKT-Modell belegt "3 von 9 expandieren" | Der expandierende Teil ist "essentially ... the Pauli matrices", ein Artefakt einer Naeherung. Neue Arbeiten (2025/26) zeigen analytisch auf so(1,3) bzw. 4D | Aoki u. a. 2019 [S Abstract]; Muramatsu 2026, Liao 2026, Liao/Maeta 2025 [S Abstract] | Belastbarer ist der euklidische Befund: SO(3), mit zwei Methoden (GEM, CLM) |
| V5 mittel | E5: KK-Anregungen zerfallen schnell | Der Zerfall von KK-Gravitonen an der Schwelle ist ~q^5 unterdrueckt | DD-SPUREN [P] | Kompakte Richtungen hinterlassen langlebige Tuerme |
| V6 mittel | "Dimension" heisst Zahl grosser Raumrichtungen | Drei Bedeutungen: Zahl grosser Richtungen; Dimension der Brane, auf der wir leben; skalenabhaengige Dimension | Durrer u. a. 2005, Karch/Randall 2005, Anchordoqui u. a. 2010 [S Abstract] | Neuer Moderator: Was ist mit "Dimension" gemeint? (Gegensweep G1) |
| V7 klein | Die Hierarchie "3 gross, einige teilweise" ist ein Rechenergebnis | Bei ABE ist sie ein Zaehlargument. Die M-Theorie-Rechnung startet von gewaehlten Anfangszustaenden | ABE Z. 274-290 [S]; GKM Z. 96-105 [S]; Easther u. a. 2002 [S Abstract] | "3 gross, einige teilweise" ist dort vorgegeben, nicht vorhergesagt |
| V8 Kanal | 3 bis 5 falsche arXiv-Nummern aus dem Gedaechtnis | 0 von 27 falsch. Dafuer 3 von 10 Abrufen mit 503, einer zu breit | ARBEITSFELD A1 bis A10 | Die 24-Monats-Suche gelang erst im vierten Anlauf |

## 3. Pruefung des Schreibtischs [M, von mir geprueft]

### 3.1 Schnittregel D_Raum <= 2k + 1

- **Richtig als Transversalitaetszaehlung** [ES, Kopf]. Die Weltvolumina zweier k-dimensionaler Gebilde haben die
  Dimension k + 1. In der Raumzeit mit D_Raum + 1 Dimensionen schneiden sie sich generisch, wenn
  2(k + 1) >= D_Raum + 1. Das ergibt Punkte 1, Faeden 3, Membranen 5.
- **An der Quelle:**
  - ABE: "the winding modes of p-branes can interact in at most 2p + 1 large spatial dimensions" (Z. 276-278 [S])
  - GKM: Der Stossparameter lebt in den "D − 4 directions transverse to the motion of both strings" (Z. 237-239 [S]);
    bei D = 4 gibt es keine Querrichtung.
- **Drei Voraussetzungen, die die Regel nicht enthaelt:**
  1. *Rate gegen Ausdehnung.*
     - Danos/Frey/Mazumdar: Wechselwirkungsraten "negligible" [S Abstract].
     - EGJK: "due to the rolling dilaton the string annihilation cross section becomes weaker" (Z. 847 [S]).
  2. *Glatte Faeden.*
     - GKM Z. 666-676 [S]: Die Regel gilt nur fuer "semiclassical one-dimensional objects". In der Hagedorn-Phase
       "the classical picture fails".
     - [ES] Fuer raue Faeden (Irrfahrten) zaehlt die fraktale Dimension 2 statt 1. Zwei Brownsche Pfade schneiden sich
       raeumlich genau fuer d <= 3 [L, Dvoretzky/Erdoes/Kakutani].
     - [H] Mit unabhaengig zitternden Faeden waere 3 + 3 >= D_Raum + 1 die Grenze, also bis 5.
     - Das ist der Unterscheidungspunkt der Karte in 5.5.
  3. *Topologie mit Schleifen (Torus).*
     - Annahme "existence of one-cycles in all spatial directions" (ABE Z. 62 [S]).
     - Auf Calabi-Yau-Dreifaltigkeiten "one cycles are absent" (ABE Z. 415 [S]).
     - Ersatz sind "pseudo-wound" Strings auf Orbifolds (GKM Z. 106-118 [S], dort aus zweiter Hand).
- **Urteil:** Die Regel ist richtig. Sie ist aber eine Bedingung fuer moegliche Treffen, kein Auswahlmechanismus.

### 3.2 Finns PU-Ueberdeckung

- **Volle Ueberdeckung:** Der weiteste Punkt einer Gitterzelle ist die Zellmitte, im Abstand (a/2) sqrt(D). Also gilt
  r >= (a/2) sqrt(D), gleichbedeutend mit D <= 4 (r/a)^2. Richtig [ES, Kopf].
- **Im Mittel:** V_D (r/a)^D >= 1. Bei r = a ist V_12 = pi^6/720 ~ 1,335 und V_13 ~ 0,911. "Bis 12" ist richtig
  [ES, Kopf].
- **Einschraenkungen:**
  - (a) Beide Zahlen haengen an r = a. Bei r/a = sqrt(3)/2 liegt die volle Grenze genau bei 3; das ist tautologisch.
  - (b) Fuer grosses r/a gilt D_voll = 4 (r/a)^2 und D_Mittel ~ 2 pi e (r/a)^2 (Stirling). Robust ist hoechstens das
    Verhaeltnis ~ pi e/2 ~ 4,3; bei r = a betraegt es 12/4 = 3 [ES, Kopf, nicht gegengelesen].
  - (c) Andere Gitter, etwa ein Tetraeder- oder Zufallsnetz wie bei Finn, haben andere Ueberdeckungsradien [L].
  - (d) "Im Mittel >= 1" beschreibt die mittlere Mehrfachueberdeckung, keine Ueberdeckung.
- **Strenger Verwandter:** die Lebesgue-Ueberdeckungsdimension. Dort zaehlt die Ordnung der Ueberlappung, nicht der
  Radius [L].
- **Urteil:** Die Rechnung stimmt. Als Auswahlmechanismus traegt sie ohne festes r/a nicht.

### 3.3 V_D-Maximum bei D ~ 5,26

- **Richtig:**
  - V_D/V_(D-2) = 2 pi/D.
  - Ganzzahlig ist V_5 ~ 5,264 > V_6 ~ 5,168.
  - Stetig liegt das Maximum bei psi(D/2 + 1) = ln pi [L].
- **Aber:** V_D r^D hat sein Maximum bei ~2 pi r^2. Ohne Skala waehlt das nichts aus [ES].
- **Physikalisch sauber** erscheint dasselbe Sphaerenvolumen-Argument bei CJR [S, Abb. 16 S Abb.]:
  - alpha = S_inst/S_dS ist dimensionslos; Gl. 84 enthaelt Vol(Omega_(p+2)) Vol(Omega_q)/Vol(Omega_(p+q+2)).
  - Der Gipfel "is due to the relative volumes of the unit spheres" (Z. 1643-1644).
  - Der Gipfel wandert mit der Gesamtdimension.
- **Ein weiteres Maximum-ueber-n-Argument:** Das Minimum der freien Energie je Hypervolumen der Hohlraumstrahlung
  waehlt n = 3 (Gonzalez-Ayala/Angulo-Brown 2015 [S Abstract]).
  - [ES, offen] T^(n+1) hat fuer jedes n eine andere Einheit. Das Minimum muesste deshalb an T in einer gewaehlten
    Einheit haengen.
  - Den Volltext habe ich nicht gelesen, das Budget war erschoepft.

## 4. Erwartungen E1 bis E6 mit Ausgang

| Nr | Erwartung (Kurzform) | Ausgang | Beleg |
|---|---|---|---|
| E1 | BV 1989: Nur 3 Richtungen werden gross, weil Windungsstrings nur dort generisch zusammentreffen | **im Wortlaut eingetroffen, im Kern verletzt** (V1) | Zaehlung: EGJK Z. 76-84 [S] referiert BV; Sakellariadou "verified in a static background" (Z. 83). GKM Abstract und Z. 628-647 [S]: Fuer d = 3 vernichten sich Strings auch in der Strahlungsphase; fuer d > 3 werden nur ~1 % der Faelle gross. Dagegen: EGJK Abb. 4 und Z. 836-844 [S]; Danos u. a. [S Abstract]. BV-Original nicht auf arXiv [L] |
| E2 | ABE 2000: 3 grosse und bis zu 2 mittlere Dimensionen | **eingetroffen** | ABE Z. 274-290 [S]: "only allow 5 spatial dimensions", "T 3 subspace", "2 extra spatial dimensions which are larger than the remaining ones". Vorbehalte Z. 286-298 [S]: die mm-Skala ist schwer zu erzeugen; mindestens 1 Windungsmode je Hubble-Volumen bleibt; Branen wirken in 4D als Domaenenwaende, "even one-branes will overclose the Universe" |
| E3 | CDT: Aus kausalen Triangulierungen entsteht 4D; ohne Kausalitaet zerknuellte oder verzweigte Phasen | **eingetroffen** (Projektstand) mit Vorbehalt | geometrie-stand [P, dort S]: EDT hat d_h = unendlich bzw. 2; CDT hat d_s = 4,02 +- 0,1. "Die Zahl 4 kommt aus den Bausteinen" [H dort]: CDT waehlt die Zahl nicht |
| E4 | d_s faellt auf ~2 (Carlip) | **teilweise** | Carlip 2017: "effectively two dimensional" [S Abstract]. Projekt [P]: CDT ~3/2 (Coumbe/Jurkiewicz), Kausalmengen steigend (Eichhorn/Mizera) |
| E5 | KK-Turm m_k = k/R, schwer, zerfaellt schnell; Schranken aus LHC, Newton-Tests, GW170817 | **Turm und Schranken eingetroffen, "zerfaellt schnell" verletzt** (V5) | n-dim-grundlagen 9c [P]; DD-SPUREN q^5 [P]; Anker in Abschnitt 7 |
| E6 | Es gibt Wahrscheinlichkeitsverteilungen ueber die Zahl grosser Dimensionen | **eingetroffen und uebertroffen** (V2) | EGJK Abb. 4 [S Abb.]; CJR Gl. 94 [S]; Schwartz-Perlov/Vilenkin 2010, Blanco-Pillado u. a. 2010, Brown/Dahlen 2011, Graham u. a. 2010 [S Abstract] |

Quote: E2, E3 und E6 eingetroffen; E4 teilweise; E5 teilweise verletzt; E1 im Kern verletzt.

## 5. Antworten auf die Fragen 1 bis 5

### 5.1 Welche Mechanismen waehlen 3 grosse Dimensionen aus?

| Mechanismus | Voraussetzungen | Ergebnis | Stand |
|---|---|---|---|
| Stringgas (Brandenberger/Vafa 1989) | 9-Torus mit Schleifen; heisses Gleichgewichtsgas; gewickelte Strings bremsen ihre Richtung | 3 = 2 x 1 + 1 | Zaehlung bewiesen (Transversalitaet). Statisch numerisch (Sakellariadou [S Abstract]). Dynamisch bei Gleichverteilung nicht bevorzugt (EGJK [S]). Wirksam im verduennten Regime nach Hagedorn, isotrop gerechnet (GKM [S]). 24 Monate: keine neue Arbeit zur Auswahl |
| Branengas (ABE 2000; Easther u. a. 2002) | wie oben, dazu Membranen | 3 gross, 2 mittel, 4 klein | Zaehlargument [S]. M-Theorie-Rechnung mit gewaehlten Anfangszustaenden: "The biggest hierarchy ... produces three large unwrapped dimensions" [S Abstract] |
| Relaxation (Karch/Randall 2005) | gleich viele Branen und Antibranen; hoeherdimensionale FRW-Entwicklung | 3- und 7-Branen dominieren | Rechnung, Vorschlag [S Abstract]. "3" ist hier die Branendimension |
| Branenzerfall (Durrer/Kunz/Sakellariadou 2005) | Dp-Branen im 9+1-dimensionalen Volumen | D3-Branen bleiben uebrig | Argument [S Abstract] |
| Knotennetz (Berera/Buniy/Kephart/Paes/Rosa 2015) | Netz geknoteter Flussroehren aus einem QCD-artigen Uebergang treibt die Inflation | Das Netz ist nur in 3 Raumdimensionen topologisch stabil | Vorschlag [S Abstract]. Dass Knoten nur in R^3 existieren, ist bewiesen (Zeeman [P 4e]) |
| IKKT-Matrixmodell | 10 Matrizen, grosses N | Euklidisch: freie Energie minimal bei d = 3 (GEM 3. Ordnung), CLM bestaetigt SO(3). Lorentz: 3 von 9 Richtungen expandieren, aber als Pauli-Artefakt | numerisch [S Abstract]. 2025/26 analytisch: so(1,3) bzw. 4D euklidisch (Muramatsu 2026, NPB laut arXiv; Liao 2026; Liao/Maeta 2025) [S Abstract] |
| Keimbildung in der Landschaft (Carroll/Johnson/Randall 2009) | Einstein-Maxwell mit q-Form-Fluss, Kompaktifizierung auf S^q | Rate maximal bei 4D fuer D = 8 | Rechnung im Spielzeugmodell, massabhaengig [S] |
| Thermodynamik (Gonzalez-Ayala/Angulo-Brown 2015) | Hohlraumstrahlung in n Dimensionen | Minimum der freien Energie bei n = 3 | Vorschlag [S Abstract]. Einheitenfrage offen [ES] |
| Stabilitaet und Beobachter (Ehrenfest, Tegmark) | Bahnen, Atome, vorhersagbare Wellen | nur 3+1 | bewiesene Teilsaetze [P 1a, 1b, 9a]; anthropisch |

- [ES, Feld-Regel 6] Drei verschiedene Wege fuehren zur 3:
  - glatte Weltflaechen: 2 + 2 >= 3 + 1
  - Brownsche Pfade schneiden sich bis d = 3 [L]
  - Knoten und Verschlingung gibt es nur in R^3 [P]
- Sie teilen eine Groesse: Schnitt und Verschlingung eindimensionaler Gebilde brauchen Kodimension 2
  (p + q = n − 1, Alexander-Dualitaet [L]).
- Die 3 kommt also daher, dass die leichtesten ausgedehnten Objekte Faeden sind, nicht aus einer Statistik. Waeren es
  Membranen, kaeme 5 heraus (ABE).

### 5.2 Gibt es eine Hierarchie "3 bis 4 stabil, einige teilweise, Rest kurzlebig"?

- **Ja, aber in anderer Form:**
  - ABE: 3 gross, 2 mittel, 4 klein (zusammen 9 Raumrichtungen) [S].
  - M-Theorie-Rechnungen: Anfangszustaende mit "3 dimensions unwrapped, some ... partially wrapped and some fully
    wrapped" ergeben eine Hierarchie (GKM Z. 96-105 [S]). Mit Fluessen werden "3 out of the 6 unwrapped dimensions"
    gebremst. Die Anfangszustaende sind dafuer gewaehlt (V7).
  - Eine Hierarchie nach Laengenskala statt nach Lebensdauer: Kurz ist der Raum niedrigdimensional, mittel 3, gross
    "effectively higher dimensional" (Anchordoqui u. a. 2010 [S Abstract]). Spektrale Dimension 4 bei grossen
    Abstaenden, bei kleinen ~2 bzw. 3/2 [P, S Abstract].
- **Kurzlebig sind Gebilde, nicht Dimensionen:**
  - Windungen der Branen mit p = 8, 6, 5, 4 "will disappear first" (ABE Z. 272-281 [S], zweispaltiger Satz).
  - Bei Vakua bestimmt die Vakuumenergie die Lebensdauer (V3).
- **"Teilweise existierend" hat in der Literatur fuenf Formen:**
  1. kompakt mit KK-Turm [P]
  2. mittelgross (ABE) [S]
  3. skalenabhaengig (d_s, verschwindende Dimensionen) [P, S Abstract]
  4. unscharf: "Fuzzy Extra Dimensions" im IKKT-Modell (Manta/Steinacker 2025, nur Titel gelesen)
  5. formal ohne eigene Dynamik: die 12 der F-Theorie (Vafa 1996 [S Abstract]; dass die zwei zusaetzlichen Richtungen
     reine Hilfsrichtungen sind, nur [L])
- **Zahlen:**
  - 3, 5, 7, 10 bzw. 11, 12 (formal), 26 [S bzw. L wie oben].
  - Obergrenze fuer supersymmetrische Theorien mit Spin <= 2: 11 Dimensionen (Nahm 1978) [L].
  - Liao 2026: Sattel "reach every signature only from twelve" [S Abstract]. Das ist eine Zahl von Matrizen, keine
    Schicht von Dimensionen [ES].
- **Finns "3-4" und "12":** Keine gelesene Arbeit sagt diese Zahlen aus einem Mechanismus voraus. Das gilt nach
  Recherchestand, einschliesslich der 24-Monats-Suche: nicht belegt, nicht widerlegt.

### 5.3 Wahrscheinlichkeitsverteilung ueber D, und wie faellt sie fuer grosse D ab?

- **Ohne Dynamik (reines Abzaehlen) gewinnt keine Dimension, sondern gar keine.**
  - EDT mit gleichen Gewichten: d_h = unendlich [P].
  - Kausalmengen: "most causal sets are not at all manifold-like" (Loomis/Carlip 2017 [S Abstract]).
  - [ES] Zufall allein fuehrt also nicht zu 3, sondern zu Strukturen ohne endliche Dimension. Das trifft Finns
    "unendlich (Kugel)".
- **Mit Dynamik gibt es drei gelesene Formen:**
  1. **Stringgas** (EGJK 2004, Abb. 4 [S Abb.], je 10^3 Laeufe):
     - Gipfel nach Anfangskopplung: phi = -1,0: alle 9 gross; -1,5: 7; -2,0: 5; -2,5: 2; -3,0 und -3,5: 0.
     - Die Breite ist ~ +-1 bis 2.
     - Es gibt keinen Abfall "fuer grosses D", sondern eine wandernde Glocke.
     - [ES] Das Liouville-Mass (Gl. 32, Z. 646-656 [S]) hat sein Entropiemaximum bei schwacher Kopplung, also im Regime,
       in dem alle Richtungen klein bleiben.
  2. **Landschaft** (CJR 2009):
     - P_i/P_j ~ exp[-S_dS (alpha_i - alpha_j)] (Gl. 94 [S]).
     - Die alpha-Unterschiede sind klein, ~0,005 bis 0,08 (Abb. 16 [S Abb.]). Weil |S_dS| riesig ist, wird die
       Verteilung trotzdem exponentiell scharf [ES].
     - "alpha is in general larger when the total dimensionality is increased" (Z. 1647 [S]).
     - Das Mass ist "inherently ambiguous" (Z. 2000-2004 [S]).
     - Schwartz-Perlov/Vilenkin: Die naive Verallgemeinerung des Masses widerspricht den Beobachtungen [S Abstract].
     - Brown/Dahlen: Ewige Inflation besiedelt die ganze Landschaft [S Abstract].
  3. **IKKT:** freie Energie fuer d = 2 bis 7, Minimum bei d = 3 (Nishimura/Okubo/Sugino 2011 [S Abstract]). Eine
     normierte Verteilung steht im Abstract nicht.
- **Abfall fuer grosses D:** Nach Recherchestand gibt keine gelesene Arbeit dafuer ein Gesetz an.
- [ES] Gemeinsames Muster: Jede gefundene Verteilung hat einen Gipfel, dessen Lage ein aeusserer Parameter setzt:
  - beim PU-Bild r/a
  - bei V_D der Radius r
  - beim Stringgas die Anfangskopplung phi
  - bei CJR die Gesamtdimension D
  Ohne Parameter waehlt nur die Zaehlregel (k = 1 ergibt 3), und die hat keine Dynamik.

### 5.4 Messanker

- **Gemessen ist:**
  - keine nicht kompakte Zusatzrichtung mit Leckage auf Mpc-Skala (D = 4,02 +0,07/-0,10)
  - keine gravitativ starke Zusatzkraft oberhalb von ~40 um
- **Nicht gemessen ist "genau 3":** Kompakte Richtungen unter ~30 um bleiben fuer die Gravitation offen, unterhalb von
  ~1/(4 TeV) auch fuer Felder des Standardmodells [P]. Tabelle in Abschnitt 7.
- **Fuer die Auswahlmechanismen selbst gibt es keine Daten.** Vorgeschlagen sind:
  - anisotrope Kruemmung bzw. ein CMB-Quadrupol, falls unser Eltern-Vakuum niedriger dimensional war (Graham u. a.
    2010 [S Abstract])
  - eine Grenzfrequenz primordialer Gravitationswellen bei verschwindenden Dimensionen, weil "(2+1)-dimensional
    spacetimes have no gravitational degrees of freedom" (Mureika/Stojkovic 2011 [S Abstract])
- Messergebnisse dazu habe ich nicht gefunden. In den letzten 24 Monaten gibt es 0 Treffer zu "vanishing dimensions".

### 5.5 Kartenvorschlag (einer) mit Ableitbarkeitsprobe

**FADEN-DIM-1 (Vorschlag):** Treffen und vernichten sich gewickelte Faeden auf einem periodischen Netz der
Raumdimension D = 2 bis 6? Und wo kippt das, wenn die Faeden rau werden?

- **Aufbau:**
  - Hyperkubischer Torus mit je ~1e6 Knoten: D = 3 mit L = 100, D = 4 mit L = 32, D = 5 mit L = 16, D = 6 mit L = 10.
  - Ein Paar geschlossener Faeden mit Windung +1 und -1 um Richtung 1. Teilen sie einen Knoten, vernichten sie sich.
  - Zwei Bewegungsarten:
    - (G) glatt: starre Faeden, je Schritt Verschiebung in eine zufaellige Querrichtung
    - (R) rau: lokale Metropolis-Zuege, die Rauheit ueber eine Biegesteifigkeit einstellbar
  - Messgroessen je D und Rauheit: der Anteil der Paare, die sich bis T = c L^2 Schritte treffen, und die Zeit bis zum
    Treffen.
- **Ableitbarkeitsprobe:**
  - (G) ist vorab ableitbar. Die Treffwahrscheinlichkeit je Durchlauf ist ~ (w/L)^(D-3) bei Fadendicke w
    (Transversalitaet; entspricht dem GKM-Stossparameter in D − 4 Richtungen [S]) [ES]. (G) taugt nur als Kontrolle
    K0, nicht als Messung.
  - (R) ist nicht vollstaendig ableitbar. Hier konkurrieren die raeumliche Brownsche Schnittregel (d <= 3) [L] und das
    Zittern in der Zeit (bis 5) [H]; dazu kommen endliche Dicke und Netzkorrelationen. Messgroesse ist die
    Kippdimension D*: ab ihr faellt der Treffanteil mit L.
  - Projekt-grep: kein Vorgaenger (Gegensweep G6). Die Parallelkarten DIM-LEITER-QBALL-1 und VERSCHRAENK-DIM-1 behandeln
    Q-Baelle und Verschraenkung, keine Faeden.
- **Vorab festzuschreiben:**
  - F1: (G) trifft in D = 3 mit Anteil ~1, in D = 4 mit Anteil ~ w/L (das ist K0).
  - F2 [H]: (R) verschiebt D* von 3 auf 4 oder 5.
  - Bleibt D* bei 3, ist die 3 auch fuer raue Faeden robust. Beide Ausgaenge sind moeglich.
- **Unterscheidungspunkt:** D = 4 und D = 5 bei grossem L. Dort sagen "glatt" und "rau" verschiedene Skalierungen mit L
  voraus.
- **Grenzen:**
  - Ohne Ausdehnung und ohne Dilaton: Die Karte testet nicht die Auswahl selbst, also nicht die EGJK-Dynamik.
  - Sie testet die Schnittregel im Netz, auf der alle Faden-Mechanismen stehen.
  - Die Laufzeit habe ich nicht abgeschaetzt, weil die Karte das Rechnen verbietet.

## 6. Regime, Moderatoren, Unterscheidungspunkte

| Paar | Regime A | Regime B | Moderator | Wo sie messbar auseinanderlaufen |
|---|---|---|---|---|
| Zaehlung gegen Dynamik (Stringgas) | statisch bzw. isotrop-verduennt: d = 3 vernichtet, d > 3 friert aus (Sakellariadou; GKM [S]) | anisotroper 9-Torus, rollender Dilaton, Gleichverteilung: "alles oder nichts" (EGJK [S]) | Anfangskopplung, Windungsdichte, Mass | Anisotroper Lauf mit festgehaltenem Dilaton: Waehlt allein die Zaehlung, muss die Glocke bei 3 stehen bleiben. Nach Recherchestand nicht gerechnet; im Netz zugaenglich |
| Glatte gegen raue Faeden | Laenge >> Dicke: Grenze 3 | Hagedorn-artig: "spread in all directions" (GKM Z. 666-676 [S]); Grenze 3 bis 5 [H] | Rauheit, Dicke/Torusweite | D = 4 und 5 (FADEN-DIM-1) |
| Landschaft: welche D? | D = 8: Gipfel bei 4D | D = 10: Gipfel bei 5D (CJR Abb. 16 [S Abb.]) | Gesamtdimension, Fluss Q, Mass | D = 10 bzw. 11 mit realistischem Flussgehalt; nach Recherchestand nicht gerechnet |
| IKKT euklidisch gegen Lorentz | SO(3) (GEM + CLM [S Abstract]) | 3 von 9, aber Pauli-Artefakt (Aoki u. a. [S Abstract]) | Behandlung des Phasenfaktors e^(iS_b) | Lorentz-Simulation mit exaktem e^(iS_b) bei grossem N; nach Recherchestand nicht vorhanden (2608.29688 nur N = 5) |
| Stringauswahl gegen IKKT gegen Knotennetz | alle sagen 3 | - | - | Keine beobachtbare Groesse gefunden, die sie trennt [ES]: **empirisch nicht unterscheidbar nach Recherchestand** |
| Bedeutung von "3" | Zahl grosser Richtungen | Branendimension; skalenabhaengige Dimension | Definition | GW170817 trifft nur nicht kompakte Leckage; d_s nur kurze Abstaende |

## 7. Ankertabelle

| Anker | Zahl | Quelle | Was er misst | Bezug zu Finns Frage |
|---|---|---|---|---|
| GW170817, Amplitude | D = 4,02 +0,07/-0,10 (H0 aus SH0ES), 3,98 +0,07/-0,09 (H0 aus Planck), 68 %; Abschirmskala > ~20 Mpc | Pardo u. a. 2018, arXiv:1801.08160 [P, STRANG-ANKER-L, dort S Abstract] | Leckage in nicht kompakte Zusatzdimensionen | Keine grosse vierte Raumrichtung, die die Gravitation sieht |
| Newton bei kleinen Abstaenden | 52 um bis 3 mm; abs(alpha) = 1 bei lambda < 38,6 um; R < 30 um fuer eine Dimension | Lee u. a. 2020 [P, MESSLAGE] | kompakte Gravitationsrichtungen | "Teilweise" Richtungen unter ~30 um sind erlaubt |
| Potenzterm k = 3 | abs(beta_3) <= 1,3e-4 (68 %) | Adelberger u. a. 2007 [P, BLASE-EW] | Schwanz des Kraftgesetzes | - |
| Flache Dark Dimension | R <~ 0,2 um (m_KK >~ 1 eV), unbegutachtet | Langhoff 2026 [P, DD-SPUREN] | eine flache mesoskopische Dimension | Das Mikrometerfenster ist fuer flache Varianten fast geschlossen |
| LHC | M_D > 11,2 TeV (n = 2) bis 5,9 TeV (n = 6); RS-KK > 4,78 TeV; UED 1/R > 4,16 TeV | ATLAS 2021, PDG 2025 [P, MESSLAGE] | grosse und verzerrte Zusatzdimensionen; Standardmodell-Felder in Zusatzdimensionen | Standardmodell-Felder sehen Zusatzrichtungen hoechstens unterhalb ~1/(4 TeV) |
| Cassini | gamma - 1 = (2,1 +- 2,3)e-5 | Will 2014 [P] | Spin-2 ohne gravitativ gekoppelten Skalar | [ES dort] linearisiert gamma = 1/(D-3) |
| Coulomb, Photonmasse | mu < 1e-14 eV (Labor), < 1e-18 eV (Sonnenwind); Exponent q = (2,7 +- 3,1)e-16 [L] | Goldhaber/Nieto 2010 [P] | Gauss-Gesetz in d = 3 | Fuer das Licht ist d_eff - 3 kleiner als ~1e-15 |
| Licht-Dispersion | E_QG,1 > 1,0e20 GeV | LHAASO 2024 [P] | planck-nahe Struktur | Nur indirekt fuer den Fluss von d_s, kein d_s-Messwert [ES] |
| Spitzen von Strings | Spitzen sind nur in 3+1 generisch; etwa eine Groessenordnung weniger Bursts je Zusatzdimension | O'Callaghan u. a. 2010 [P] | Bewegungsraum von Strings | gleicher Kodimensionsgrund wie die Schnittregel [ES] |
| Eltern-Vakuum | anisotrope Kruemmung, durch den CMB-Quadrupol begrenzt; keine Zahl gelesen | Graham/Harnik/Rajendran 2010 [S Abstract] | Vorgeschichte der Dekompaktifizierung | Der einzige vorgeschlagene Test der Frage "aus welchem D kamen wir?" |
| Verschwindende Dimensionen | Grenzfrequenz primordialer GW; "planar alignment" in alten Hoehenstrahl-Daten behauptet | Mureika/Stojkovic 2011 [S Abstract] | skalenabhaengige Dimension | Keine neue Arbeit in 24 Monaten [S Trefferliste] |

## 8. Gegensweep: Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

- **G1, geprueft:** "Drei" hat drei Bedeutungen.
  - Zahl grosser Richtungen: BV, EGJK, GKM, IKKT.
  - Dimension unserer Brane in einem 9+1-dimensionalen Volumen: Durrer u. a.; Karch/Randall [S Abstract].
  - Skalenabhaengige Dimension: Anchordoqui u. a.; CDT; Carlip [S Abstract, P].
  - Ich hatte stillschweigend die erste angenommen. Finns "3-4" passt je nach Bedeutung anders.
- **G2, geprueft:** Die Auswahl durch Windungen braucht nicht zusammenziehbare Schleifen.
  - Belege: ABE Z. 11, 62, 415 [S]; GKM Z. 106-118 [S].
  - Die 3 haengt also auch an einer Topologie-Annahme, nicht nur an der Zaehlung.
- **G3, im Kopf geprueft:** Die PU-Zahlen haengen zusaetzlich am Wuerfelgitter. Fuer ein Tetraeder- oder Zufallsnetz
  aendern sich 4 und 12 [ES, L].
- **G4, nicht geprueft:** Dass es genau eine Zeitrichtung gibt, habe ich als gegeben genommen. Tegmark behandelt
  (n, m) [P]; Liao 2026 stellt "criteria for the emergence of time" auf [S Abstract].
- **G5, nicht geprueft:** Dass sich Brownsche Pfade in R^d genau fuer d <= 3 schneiden [L]. Darauf steht F2 der
  Kartenidee.
- **G6, geprueft per Projekt-grep:** Es gibt keinen frueheren Netz-Test, in dem sich Faeden bei einstellbarer Dimension
  vernichten. Der Treffer "d = 6 vernichtet" in RUNDE-10 ist ein Startabstand, keine Dimension.
- **G7, geprueft am Projekt:** D = 4,02 gilt nur fuer nicht kompakte Zusatzdimensionen (STRANG-ANKER-L). Gemessen ist
  also nicht "genau drei", sondern "keine grosse Zusatzrichtung mit Leckage".

## 9. Offene Fragen

1. Ergibt ein anisotroper Stringgas-Lauf mit festgehaltenem Dilaton eine Glocke bei 3? Das ist der Unterscheidungspunkt
   zwischen Zaehlung und Dynamik. Ich habe keine solche Rechnung gelesen.
2. Wo liegt der CJR-Gipfel fuer D = 10 bzw. 11 mit realistischem Flussgehalt, und welches Mass passt zu den
   Beobachtungen?
3. Gibt es eine Lorentz-IKKT-Simulation mit exaktem e^(iS_b) bei grossem N? In der Trefferliste ist die groesste
   N = 5.
4. Haengt das Minimum bei Gonzalez-Ayala/Angulo-Brown an der Temperatureinheit? Den Volltext habe ich nicht gelesen.
5. Gibt es Tests verschwindender Dimensionen zwischen 2011 und 2024? Gesucht habe ich nur in den letzten 24 Monaten.
6. Muss die Zahl der Zeitrichtungen mit ausgewaehlt werden (G4)?
7. Rueckfrage an die Leitung (R1 im ARBEITSFELD): Soll FADEN-DIM-1 mit DIM-LEITER-QBALL-1 und VERSCHRAENK-DIM-1 auf
   dieselbe D-Leiter und dieselben Netzgroessen abgestimmt werden?

## 10. Kalibrierung

- **(a) Gemessen:**
  - D = 4,02 fuer nicht kompakte Leckage
  - Newton bis 52 um
  - LHC-Schranken
  - Photonmasse
  Zu den Auswahlmechanismen ist nichts gemessen.
- **(b) Nuetzlich verdichtet [ES]:**
  - "3 = 2k + 1 mit k = 1" bzw. "Kodimension 2 fuer Faeden" fasst Stringgas, Knoten und Brownsche Pfade zusammen.
  - "Gipfel wandert mit einem aeusseren Parameter" fasst PU, V_D, EGJK und CJR zusammen.
- **(c) Gewachsene Gewissheit ohne neue Evidenz:**
  - Meine Sicherheit, dass die 3 "aus den Faeden" kommt, ist im Lauf der Recherche gestiegen. Gleichzeitig hat sich die
    Frage in drei Bedeutungen und vier Regime aufgeloest. **Das ist ein Warnzeichen.**
  - Die Vereinheitlichung stuetzt sich auf zwei [L]-Saetze (Brownsche Schnitte, Alexander-Dualitaet), die ich nicht
    abgerufen habe.
  - F2 ("raue Faeden bis 5") ist reine Hypothese.

## 11. Quellenliste (Abrufstand 04.10.2026; lokale Kopien in quellen/)

Abgerufen (arXiv-API A1, Abstracts in quellen/A1-api-idlist.xml und A1-abstracts.txt, sofern nicht anders vermerkt):

- Alexander, Brandenberger, Easson (2000): Brane Gases in the Early Universe. PRD 62, 103509.
  https://arxiv.org/abs/hep-th/0005212. Volltext: quellen/A7-ABE-hep-th-0005212v2.pdf/.txt [S]
- Sakellariadou (1996): Numerical Experiments in String Cosmology. NPB 468, 319. https://arxiv.org/abs/hep-th/9511075
  [S Abstract]
- Easther, Greene, Jackson, Kabat (2003): Brane gas cosmology in M-theory: late time behavior. PRD 67, 123501.
  https://arxiv.org/abs/hep-th/0211124 [S Abstract]
- Easther, Greene, Jackson, Kabat (2005): String windings in the early universe. JCAP 0502:009.
  https://arxiv.org/abs/hep-th/0409121. Volltext: quellen/A5-EGJK-hep-th-0409121v1.pdf/.txt; Abb. 3 und 4 angesehen
  [S, S Abb.]
- Danos, Frey, Mazumdar (2004): Interaction Rates in String Gas Cosmology. PRD 70, 106010.
  https://arxiv.org/abs/hep-th/0409162 [S Abstract]
- Battefeld, Watson (2006): String Gas Cosmology. RMP 78, 435. https://arxiv.org/abs/hep-th/0510022 [S Abstract]
- Brandenberger (2008): String Gas Cosmology. https://arxiv.org/abs/0808.0746 [S Abstract]
- Greene, Kabat, Marnerides (2010): Dynamical Decompactification and Three Large Dimensions. PRD 82, 043528.
  https://arxiv.org/abs/0908.0955. Volltext: quellen/A6-GKM-0908.0955v2.pdf/.txt [S]
- Durrer, Kunz, Sakellariadou (2005): Why do we live in 3+1 dimensions? PLB 614, 125.
  https://arxiv.org/abs/hep-th/0501163 [S Abstract]
- Karch, Randall (2005): Relaxing to Three Dimensions. PRL 95, 161601. https://arxiv.org/abs/hep-th/0506053
  [S Abstract]
- Kim, Nishimura, Tsuchiya (2012): Expanding (3+1)-dimensional universe from a Lorentzian matrix model for superstring
  theory in (9+1)-dimensions. PRL 108, 011601. https://arxiv.org/abs/1108.1540 [S Abstract]
- Nishimura, Okubo, Sugino (2011): Systematic study of the SO(10) symmetry breaking vacua in the matrix model for type
  IIB superstrings. JHEP 1110, 135. https://arxiv.org/abs/1108.1293 [S Abstract]
- Anagnostopoulos, Azuma, Ito, Nishimura, Okubo, Papadoudis (2020): Complex Langevin analysis of the spontaneous
  breaking of 10D rotational symmetry in the Euclidean IKKT matrix model. JHEP 06 (2020) 069.
  https://arxiv.org/abs/2002.07410 [S Abstract]
- Aoki, Hirasawa, Ito, Nishimura, Tsuchiya (2019): On the structure of the emergent 3d expanding space in the Lorentzian
  type IIB matrix model. PTEP 2019. https://arxiv.org/abs/1904.05914 [S Abstract]
- Vafa (1996): Evidence for F-Theory. NPB 469, 403. https://arxiv.org/abs/hep-th/9602022 [S Abstract]
- Berera, Buniy, Kephart, Paes, Rosa (2015): Knotty inflation and the dimensionality of spacetime.
  https://arxiv.org/abs/1508.01458 [S Abstract]
- Giddings (2003): The fate of four dimensions. PRD 68, 026006. https://arxiv.org/abs/hep-th/0303031 [S Abstract]
- Carroll, Johnson, Randall (2009): Dynamical compactification from de Sitter space. JHEP 0911:094.
  https://arxiv.org/abs/0904.3115. Volltext: quellen/A8-CJR-0904.3115v2.pdf/.txt; Abb. 16 bis 18 angesehen [S, S Abb.]
- Blanco-Pillado, Schwartz-Perlov, Vilenkin (2010): Transdimensional Tunneling in the Multiverse. JCAP 1005:005.
  https://arxiv.org/abs/0912.4082 [S Abstract]
- Schwartz-Perlov, Vilenkin (2010): Measures for a Transdimensional Multiverse. JCAP 1006:024.
  https://arxiv.org/abs/1004.4567 [S Abstract]
- Graham, Harnik, Rajendran (2010): Observing the Dimensionality of Our Parent Vacuum. PRD 82, 063524.
  https://arxiv.org/abs/1003.0236 [S Abstract]
- Brown, Dahlen (2011): Populating the Whole Landscape. PRL 107, 171301. https://arxiv.org/abs/1108.0119 [S Abstract]
- Carlip (2017): Dimension and Dimensional Reduction in Quantum Gravity. https://arxiv.org/abs/1705.05417 [S Abstract]
- Anchordoqui, Dai, Fairbairn, Landsberg, Stojkovic (2010): Vanishing Dimensions and Planar Events at the LHC.
  https://arxiv.org/abs/1003.5914 [S Abstract]
- Mureika, Stojkovic (2011): Detecting Vanishing Dimensions Via Primordial Gravitational Wave Astronomy. PRL 106,
  101101. https://arxiv.org/abs/1102.3434 [S Abstract]
- Loomis, Carlip (2017): Suppression of non-manifold-like sets in the causal set path integral.
  https://arxiv.org/abs/1709.00064 [S Abstract]
- Gonzalez-Ayala, Angulo-Brown (2015): Is the (3+1)-d nature of the universe a thermodynamic necessity?
  https://arxiv.org/abs/1502.01843 [S Abstract]

24-Monats-Suche (A10; quellen/A10-api-24m-abs.xml und A10-abstracts.txt; 57 Treffer, 04.10.2024 bis 04.10.2026):

- Muramatsu (2026): Supersymmetric Origin of Four-Dimensional Space-time in the IIB Matrix Model. NPB 1030, 117610
  (laut arXiv). https://arxiv.org/abs/2605.03611 [S Abstract]
- Liao (2026): Lie Algebra Saddles in the IKKT Matrix Model and Criteria for the Emergence of Time.
  https://arxiv.org/abs/2609.40183 [S Abstract]
- Liao, Maeta (2025): A New Type of Saddle in the Euclidean IKKT Matrix Model and Its Emergent Geometry.
  https://arxiv.org/abs/2512.03161 [S Abstract]
- Muramatsu (2026): One-Loop Fluctuation Response Along a Constrained Noncommutative Modulus in the Lorentzian IIB
  Matrix Model. https://arxiv.org/abs/2608.29688 [S Abstract]
- Chou, Nishimura, Wang (2025): Monte Carlo studies of the emergent spacetime in the polarized IKKT model.
  https://arxiv.org/abs/2507.18472 [S Abstract]
- Manta, Steinacker (2025): Dynamical Covariant Quantum Spacetime with Fuzzy Extra Dimensions in the IKKT model.
  https://arxiv.org/abs/2509.24753 [S Titel]
- Nayeri (2026): T-Duality Selection of a Disformal Effective Metric in String Gas Cosmology.
  https://arxiv.org/abs/2603.19334 [S Abstract]
- Moradpouri (2025): The species scale and the refined TCC bound in time-dependent backgrounds of string theory.
  https://arxiv.org/abs/2512.22694 [S Abstract]

Nur aus dem Gedaechtnis oder zweiter Hand:

- Brandenberger, Vafa (1989): Superstrings in the early universe. NPB 316, 391 [L; als Ref. 1 bei ABE gesehen]
- Nahm (1978), NPB 135, 149: Obergrenze 11 fuer Supergravitation [L]
- Dvoretzky, Erdoes, Kakutani (1950): Schnitte Brownscher Pfade [L]

Projektdateien [P]:

- coordination/n-dimensionen-grundlagen-20260912.md
- RUNDE-37/strang-anker-l/DOSSIER.md
- RUNDE-23/dd-spuren/ERGEBNIS.md
- RUNDE-22/geometrie-stand/ERGEBNIS.md
- RUNDE-22.md (Abschnitt CDT)
- RUNDE-24/bag-dim/ERGEBNIS.md
- RUNDE-41.md (WOLFRAM-SCAN-L)

## 12. Selbstanzeigen

1. **A2 war zu breit:** 3314 Treffer, abgedeckt nur 17.09. bis 01.10.2026. Ein Abruf war damit fast verloren.
2. **A3, A4 und A9 endeten mit 503 (leer).** Ich habe sie vorsichtshalber als Abrufe gezaehlt. Wirksam waren 6 von 10.
   Die 24-Monats-Suche gelang erst mit A10, und ohne die Phrase "IIB matrix model" (siehe Grenze dort).
3. **Eine geschaetzte Uhrzeit** stand im ARBEITSFELD ("bis 18:58"). Sofort durch den gemessenen Wert 18:56:15
   ersetzt.
4. **Zwei falsche Zeilennummern** zu GKM im ARBEITSFELD. Um 19:05 berichtigt, der alte Wert ist vermerkt.
5. **Die Aussage "alle unbegutachtet"** zu den IKKT-Treffern war falsch, weil 2605.03611 in NPB erschienen ist (laut
   arXiv). Im ARBEITSFELD gestrichen und berichtigt.
6. **Kopfrechnungen im Schreibtisch-Teil:** V_12, V_13, Stirling-Abschaetzung, digamma-Bedingung. Ausgefuehrt habe ich
   keine Rechnung, aber die Werte sind nicht gegengelesen.
7. **Werte aus Abbildungen nach Augenmass:** Drei PDF-Seiten habe ich mit dem Lesewerkzeug als Bild angesehen (EGJK
   Abb. 3 und 4, CJR Abb. 16 bis 18).
8. **Hilfswerkzeuge ausserhalb der Liste** (jq, sed, grep, curl, pdftotext): tr, wc, file, ls, cat, mkdir, date. Kein
   python, awk oder perl.
9. **Mehrere Aussagen bleiben [L]:** BV-Original, Nahm 11, Brownsche Schnitte, Hilfscharakter der F-Theorie-Richtungen,
   26.
10. **Gedaechtnisfehler bei den Autoren** von 1502.01843 (drei statt zwei). Ueber die API gefunden und berichtigt.

## 13. Einfach gesagt

Die beste Erklaerung fuer "drei" kommt aus der Stringtheorie. Faeden koennen sich nur in hoechstens drei Richtungen
zufaellig treffen und ausloeschen, und nur Richtungen ohne aufgewickelte Faeden koennen wachsen. Genaue Rechnungen
zeigen aber, dass das junge Weltall nicht von selbst bei drei landet: Je nach Anfang wachsen alle, keine oder
irgendeine Zahl von Richtungen. Eine andere Rechnung gibt eine scharfe Wahrscheinlichkeit fuer 4D, aber nur, wenn es
insgesamt genau acht Dimensionen gibt. Deine 12 taucht nirgends als Mechanismus auf, und mit dem "kurzlebig" ist es
eher umgekehrt: Unsere 3+1-Welt koennte die instabile sein. Im Netz koennen wir pruefen, ob raue, zitternde Faeden sich
auch in 4 oder 5 Richtungen noch finden.
